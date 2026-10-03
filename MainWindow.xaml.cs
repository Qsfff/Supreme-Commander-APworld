using ColorPicker;
using ColorPicker.Models;
using Newtonsoft.Json;
using OfficeOpenXml;
using System;
using System.Data;
using System.Diagnostics;
using System.IO;
using System.IO.Compression;
using System.Text;
using System.Text.Json.Serialization;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Controls.Primitives;
using System.Windows.Documents;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Shapes;
using Path = System.IO.Path;

namespace SupComClient
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        Process proc;

        string binFolder = "X:\\Games\\IG\\FAF Client\\Data\\bin\\";
        string mapmodFolder = "X:\\Games\\IG\\FAF Client\\MapMods\\";
        string FAinstallFolder = "X:\\Programs\\Steam\\steamapps\\common\\Supreme Commander Forged Alliance\\";
        string SettingsSaved = "Settings.json";
        string mapname = "SCCA_R01";
        public MainWindow()
        {
            InitializeComponent();
            ExcelPackage.License.SetNonCommercialPersonal("l.txt");
            CheckDefaultColor();
        }

        private void OpenM1(object sender, RoutedEventArgs e)
        {
            #region copy
            mapname = levelText.Text;
            string source = "Maps\\" + mapname + "\\";
            string newLocation = MapFol.Text + "\\maps\\" + mapname + "\\";
            Copy(source, newLocation);
            #endregion

            #region properties
            string LuaInput = MapFol.Text + "\\maps\\" + mapname + "\\Variables.lua";
            string InputData = "Red = " + ColorPick.SelectedColor.R + Environment.NewLine + "Green = " + ColorPick.SelectedColor.G + Environment.NewLine + "Blue = " + ColorPick.SelectedColor.B + Environment.NewLine + "Name = '" + nameText.Text + "'" + Environment.NewLine + "Faction = " + factionSelector.SelectedIndex + Environment.NewLine;
            File.WriteAllText(LuaInput, InputData);
            #endregion

            #region launch
            string filename = DataFol.Text + "\\bin\\ForgedAlliance.exe";
            Directory.CreateDirectory("C:\\LOG");
            string cparams = "/init init_coop_spec.lua /diff " + (diffSelector.SelectedIndex + 1).ToString() + " /EnableDiskWatch /log  C:\\LOG\\ap.log /map " + mapname;
            proc = new Process();
            proc.StartInfo.FileName = filename;
            proc.StartInfo.Arguments = cparams;
            proc.EnableRaisingEvents = true;
            proc.Exited += new EventHandler(SupComExit);
            proc.Start();
            #endregion
        }
        void CheckDefaultColor()
        {
            if (File.Exists(SettingsSaved))
            {
                string jsonSt = File.ReadAllText(SettingsSaved);
                ColorPick.SelectedColor = JsonConvert.DeserializeObject<Color>(jsonSt);
            }
            else
            {
                Color a = new Color();
                a.R = 255;
                a.G = 255;
                a.B = 0;
                a.A = 255;
                string jsonSt = JsonConvert.SerializeObject(a);
                File.WriteAllText(SettingsSaved, jsonSt);
                ColorPick.SelectedColor = a;
            }
        }
        private void SupComExit(object sender, System.EventArgs e)
        {
            //Delete map
            string source = MapFol.Text + "\\maps\\" + mapname + "\\";
            DirectoryInfo dir = new DirectoryInfo(source);
            dir.Delete(true);
        }
        public static void Copy(string sourceDirectory, string targetDirectory)
        {
            DirectoryInfo diSource = new DirectoryInfo(sourceDirectory);
            DirectoryInfo diTarget = new DirectoryInfo(targetDirectory);

            CopyAll(diSource, diTarget);
        }
        public static void CopyAll(DirectoryInfo source, DirectoryInfo target)
        {
            Directory.CreateDirectory(target.FullName);

            // Copy each file into the new directory.
            foreach (FileInfo fi in source.GetFiles())
            {
                Console.WriteLine(@"Copying {0}\{1}", target.FullName, fi.Name);
                fi.CopyTo(Path.Combine(target.FullName, fi.Name), true);
            }

            // Copy each subdirectory using recursion.
            foreach (DirectoryInfo diSourceSubDir in source.GetDirectories())
            {
                DirectoryInfo nextTargetSubDir =
                    target.CreateSubdirectory(diSourceSubDir.Name);
                CopyAll(diSourceSubDir, nextTargetSubDir);
            }
        }
        private void SaveChangedColor(object sender, RoutedEventArgs e)
        {
            string jsonSt = JsonConvert.SerializeObject(ColorPick.SelectedColor);
            File.WriteAllText(SettingsSaved, jsonSt);
        }

        private void Parse(object sender, RoutedEventArgs e)
        {
            #region setup
            int CI = new int(), CL = new int(), AI = new int(), AL = new int(), UI = new int(), UL = new int(), SI = new int(), SL = new int(), filler = new int(), Levels = new int();
            ExcelPackage Data = new ExcelPackage(new FileInfo("SupComAP.xlsx"));
            for (int i = 0; i < Data.Workbook.Worksheets.Count; i++)
            {
                int temp = i;
                switch (Data.Workbook.Worksheets[i].Name)
                {
                    case "Cybran Items":
                        CI = temp;
                        break;
                    case "Cybran Locations":
                        CL = temp;
                        break;
                    case "Aeon Items":
                        AI = temp;
                        break;
                    case "Aeon Locations":
                        AL = temp;
                        break;
                    case "UEF Items":
                        UI = temp;
                        break;
                    case "UEF Locations":
                        UL = temp;
                        break;
                    case "Sera Items":
                        SI = temp;
                        break;
                    case "FA Locations":
                        SL = temp;
                        break;
                    case "Filler Items":
                        filler = temp;
                        break;
                    case "Levels":
                        Levels = temp;
                        break;
                    default:
                        break;
                }
            }
            ExcelWorksheet CybIt = Data.Workbook.Worksheets[CI];
            ExcelWorksheet UEFIt = Data.Workbook.Worksheets[UI];
            ExcelWorksheet AeonIt = Data.Workbook.Worksheets[AI];
            ExcelWorksheet SeraIt = Data.Workbook.Worksheets[SI];
            ExcelWorksheet FillerIt = Data.Workbook.Worksheets[filler];
            ExcelWorksheet CybLoc = Data.Workbook.Worksheets[CL];
            ExcelWorksheet AeonLoc = Data.Workbook.Worksheets[AL];
            ExcelWorksheet UEFLoc = Data.Workbook.Worksheets[UL];
            ExcelWorksheet FALoc = Data.Workbook.Worksheets[SL];
            ExcelWorksheet LevelSheet = Data.Workbook.Worksheets[Levels];
            #endregion

            #region read

            #region read items and locations
            //Read cybran items
            List<string> CybranItems = new List<string>();
            for (int i = 1; i < 100; i++)
            {
                if (CybIt.Cells[i, 3].GetCellValue<string>() != null)
                {
                    CybranItems.Add(CybIt.Cells[i, 3].GetCellValue<string>());
                }
            }
            for (int i = 1; i < 100; i++)
            {
                if (CybIt.Cells[i, 6].GetCellValue<string>() != null)
                {
                    CybranItems.Add(CybIt.Cells[i, 6].GetCellValue<string>());
                }
            }
            //Read uef items
            List<string> UefItems = new List<string>();
            for (int i = 1; i < 100; i++)
            {
                if (UEFIt.Cells[i, 3].GetCellValue<string>() != null)
                {
                    UefItems.Add(UEFIt.Cells[i, 3].GetCellValue<string>());
                }
            }
            for (int i = 1; i < 100; i++)
            {
                if (UEFIt.Cells[i, 6].GetCellValue<string>() != null)
                {
                    UefItems.Add(UEFIt.Cells[i, 6].GetCellValue<string>());
                }
            }
            //Read sera items
            List<string> SeraItems = new List<string>();
            for (int i = 1; i < 100; i++)
            {
                if (SeraIt.Cells[i, 3].GetCellValue<string>() != null)
                {
                    SeraItems.Add(SeraIt.Cells[i, 3].GetCellValue<string>());
                }
            }
            for (int i = 1; i < 100; i++)
            {
                if (SeraIt.Cells[i, 6].GetCellValue<string>() != null)
                {
                    SeraItems.Add(SeraIt.Cells[i, 6].GetCellValue<string>());
                }
            }
            //Read aeon items
            List<string> AeonItems = new List<string>();
            for (int i = 1; i < 100; i++)
            {
                if (AeonIt.Cells[i, 3].GetCellValue<string>() != null)
                {
                    AeonItems.Add(AeonIt.Cells[i, 3].GetCellValue<string>());
                }
            }
            for (int i = 1; i < 100; i++)
            {
                if (AeonIt.Cells[i, 6].GetCellValue<string>() != null)
                {
                    AeonItems.Add(AeonIt.Cells[i, 6].GetCellValue<string>());
                }
            }
            //Read filler items
            List<string> FillerItems = new List<string>();
            for (int i = 1; i < 100; i++)
            {
                if (FillerIt.Cells[i, 1].GetCellValue<string>() != null)
                {
                    FillerItems.Add(FillerIt.Cells[i, 1].GetCellValue<string>());
                }
            }
            //Read cybran locations
            List<string> CybranLocations = new List<string>();
            for (int i = 2; i < 100; i++)
            {
                if (CybLoc.Cells[i, 1].GetCellValue<string>() != null)
                {
                    CybranLocations.Add(CybLoc.Cells[i, 1].GetCellValue<string>());
                }
            }
            #endregion


            #region make a list of all level names
            List<string> levelNAMES = new List<string>();
            for (int i = 0; i < CybranLocations.Count; i++)
            {
                if (CybranLocations[i] != "-")
                {
                    string levelName = CybranLocations[i].Substring(0, CybranLocations[i].IndexOf(":"));
                    if (!levelNAMES.Contains(levelName))
                    {
                        levelNAMES.Add(levelName);
                    }
                }
            }
            #endregion

            List<SCItem> AllRequeredItems = new List<SCItem>();
            List<SCRule> AllRequeredRules = new List<SCRule>();
            List<SCItem> tempItems = new List<SCItem>();
            List<SCRule> tempRules = new List<SCRule>();
            //Read rules for cybran locations
            #region cybran rules
            //Rules if it is UEF
            #region UEF on Cybran rules
            List<string> UEFrulesFORcybranLOCATIONS = new List<string>();
            List<string> UEFtoCYBRANlevelNAMES = new List<string>();
            int missionPos = 1;
            for (int i = 0; i < CybranLocations.Count; i++)
            {
                if (CybranLocations[i] != "-")
                {
                    string levelName = CybranLocations[i].Substring(0, CybranLocations[i].IndexOf(":")) + " (UEF)";
                    if (!UEFtoCYBRANlevelNAMES.Contains(levelName))
                    {
                        UEFtoCYBRANlevelNAMES.Add(levelName);
                    }
                    if (CybLoc.Cells[i + 2, 3].GetCellValue<string>() != null)
                    {
                        string rule = CybLoc.Cells[i + 2, 3].GetCellValue<string>();
                        List<List<string>> rule2 = new List<List<string>>();
                        //First easy case: only 1 item needed
                        if (!rule.Contains(",") && !rule.Contains("/"))
                        {
                            SCItem thisThing = new SCItem(rule, levelName, missionPos);
                            if (!tempItems.Contains(thisThing))
                            {
                                tempItems.Add(thisThing);
                            }
                            rule2.Add(new List<string>());
                            rule2[0].Add("\"" + rule + "\"");
                            rule = "Has(\"" + rule + "\")";
                        }
                        //Second case: only , or /
                        else if (!(rule.Contains(",") && rule.Contains("/")))
                        {
                            //Second case A: only ,
                            if (rule.Contains(","))
                            {
                                List<string> WhatItHas = new List<string>();
                                string temp = rule;
                                while (temp.Contains(","))
                                {
                                    string a = temp.Substring(0, temp.IndexOf(","));
                                    temp = temp.Remove(0, temp.IndexOf(",") + 2);
                                    WhatItHas.Add(a);
                                }
                                WhatItHas.Add(temp);
                                rule = "";
                                for (int j = 0; j < WhatItHas.Count; j++)
                                {
                                    SCItem thisThing = new SCItem(WhatItHas[j], levelName, missionPos);
                                    if (!tempItems.Contains(thisThing))
                                    {
                                        tempItems.Add(thisThing);
                                    }
                                    if (j != 0)
                                    {
                                        rule += " & ";
                                    }
                                    rule += "Has(\"" + WhatItHas[j] + "\")";
                                    rule2.Add(new List<string>());
                                    rule2[j].Add("\"" + WhatItHas[j] + "\"");
                                }
                            }
                            //Second case B: only /
                            else if (rule.Contains("/"))
                            {
                                List<string> WhatItHas = new List<string>();
                                string temp = rule;
                                while (temp.Contains("/"))
                                {
                                    string a = temp.Substring(0, temp.IndexOf("/"));
                                    temp = temp.Remove(0, temp.IndexOf("/") + 1);
                                    WhatItHas.Add(a);
                                }
                                WhatItHas.Add(temp);
                                rule = "";
                                rule2.Add(new List<string>());
                                for (int j = 0; j < WhatItHas.Count; j++)
                                {
                                    SCItem thisThing = new SCItem(WhatItHas[j], levelName, missionPos);
                                    if (!tempItems.Contains(thisThing))
                                    {
                                        tempItems.Add(thisThing);
                                    }
                                    if (j != 0)
                                    {
                                        rule += " | ";
                                    }
                                    rule += "Has(\"" + WhatItHas[j] + "\")";
                                    rule2[0].Add("\"" + WhatItHas[j] + "\"");
                                }
                            }
                        }
                        //Third case, contains both and and or
                        else if(rule.Contains(",") && rule.Contains("/"))
                        {
                            List<string> WhatItHas = new List<string>();
                            string temp = rule;
                            while (temp.Contains(","))
                            {
                                string a = temp.Substring(0, temp.IndexOf(","));
                                temp = temp.Remove(0, temp.IndexOf(",") + 2);
                                WhatItHas.Add(a);
                            }
                            WhatItHas.Add(temp);
                            List<bool> isItSingle = new List<bool>();
                            for (int j = 0; j < WhatItHas.Count; j++)
                            {
                                List<string> WhatItAlsoHas = new List<string>();
                                rule2.Add(new List<string>());
                                int currentIndexOfRule2 = rule2.Count - 1;
                                if (WhatItHas[j].Contains("/"))
                                {
                                    isItSingle.Add(false);
                                    temp = WhatItHas[j];
                                    while (temp.Contains("/"))
                                    {
                                        string a = temp.Substring(0, temp.IndexOf("/"));
                                        temp = temp.Remove(0, temp.IndexOf("/") + 1);
                                        WhatItAlsoHas.Add(a);
                                    }
                                    WhatItAlsoHas.Add(temp);
                                    WhatItHas[j] = "";
                                    List<string> WhatItHas2 = new List<string>();
                                    for (int ij = 0; ij < WhatItAlsoHas.Count; ij++)
                                    {
                                        WhatItHas2.Add(WhatItAlsoHas[ij]);
                                        SCItem thisThing = new SCItem(WhatItAlsoHas[ij], levelName, missionPos);
                                        if (!tempItems.Contains(thisThing))
                                        {
                                            tempItems.Add(thisThing);
                                        }
                                        if (ij != 0)
                                        {
                                            WhatItHas[j] += " | ";
                                        }
                                        WhatItHas[j] += "Has(\"" + WhatItAlsoHas[ij] + "\")";
                                        rule2[currentIndexOfRule2].Add("\"" + WhatItAlsoHas[ij] + "\"");
                                    }
                                }
                                else
                                {
                                    isItSingle.Add(true);
                                }
                            }
                            rule = "";
                            for (int j = 0; j < WhatItHas.Count; j++)
                            {
                                SCItem thisThing = new SCItem(WhatItHas[j], levelName, missionPos);
                                if (!tempItems.Contains(thisThing) && isItSingle[j])
                                {
                                    tempItems.Add(thisThing);
                                }
                                if (j != 0)
                                {
                                    rule += " & ";
                                }
                                if (isItSingle[j])
                                {
                                    rule += "Has(\"" + WhatItHas[j] + "\")";
                                    rule2[j].Add("\"" + WhatItHas[j] + "\"");
                                }
                                else
                                {
                                    rule += "(" + WhatItHas[j] + ")";
                                }
                            }
                        }
                        UEFrulesFORcybranLOCATIONS.Add(rule);
                        for (int j = 0; j < rule2.Count; j++)
                        {
                            tempRules.Add(new SCRule(levelName, rule2[j]));
                        }
                    }
                    else
                    {
                        UEFrulesFORcybranLOCATIONS.Add("");
                    }
                    if (i != 0 && UEFrulesFORcybranLOCATIONS[i - 1] != "")
                    {
                        if (UEFrulesFORcybranLOCATIONS[i] == "")
                        {
                            UEFrulesFORcybranLOCATIONS[i] = UEFrulesFORcybranLOCATIONS[i - 1];
                        }
                        else
                        {
                            UEFrulesFORcybranLOCATIONS[i] = "(" + UEFrulesFORcybranLOCATIONS[i - 1] + ") & (" + UEFrulesFORcybranLOCATIONS[i] + ")";
                        }
                    }
                    if (i > 1 && CybranLocations[i - 1] == "-" && UEFrulesFORcybranLOCATIONS[i - 2] != "")
                    {
                        if (UEFrulesFORcybranLOCATIONS[i] == "")
                        {
                            UEFrulesFORcybranLOCATIONS[i] = UEFrulesFORcybranLOCATIONS[i - 2];
                        }
                        else
                        {
                            UEFrulesFORcybranLOCATIONS[i] = "(" + UEFrulesFORcybranLOCATIONS[i - 2] + ") & (" + UEFrulesFORcybranLOCATIONS[i] + ")";
                        }
                    }
                }
                else
                {
                    missionPos++;
                    UEFrulesFORcybranLOCATIONS.Add("");
                }
            }
            for (int i = 0; i < tempItems.Count; i++)
            {
                for (int j = tempItems[i].LevelPos - 1; j < UEFtoCYBRANlevelNAMES.Count; j++)
                {
                    SCItem thisThing = new SCItem(tempItems[i].name, UEFtoCYBRANlevelNAMES[j], j);
                    AllRequeredItems.Add(thisThing);
                }
            }
            AllRequeredRules.AddRange(tempRules);
            tempItems = new List<SCItem>();
            tempRules = new List<SCRule>();
            #endregion
            //Rules if it is Cybran
            #region Cybran on Cybran rules
            List<string> CYBRANrulesFORcybranLOCATIONS = new List<string>();
            List<string> CYBRANtoCYBRANlevelNAMES = new List<string>();
            missionPos = 1;
            for (int i = 0; i < CybranLocations.Count; i++)
            {
                if (CybranLocations[i] != "-")
                {
                    string levelName = CybranLocations[i].Substring(0, CybranLocations[i].IndexOf(":")) + " (Cybran)";
                    if (!CYBRANtoCYBRANlevelNAMES.Contains(levelName))
                    {
                        CYBRANtoCYBRANlevelNAMES.Add(levelName);
                    }
                    if (CybLoc.Cells[i + 2, 4].GetCellValue<string>() != null)
                    {
                        string rule = CybLoc.Cells[i + 2, 4].GetCellValue<string>();
                        List<List<string>> rule2 = new List<List<string>>();
                        //First easy case: only 1 item needed
                        if (!rule.Contains(",") && !rule.Contains("/"))
                        {
                            SCItem thisThing = new SCItem(rule, levelName, missionPos);
                            if (!tempItems.Contains(thisThing))
                            {
                                tempItems.Add(thisThing);
                            }
                            rule2.Add(new List<string>());
                            rule2[0].Add("\"" + rule + "\"");
                            rule = "Has(\"" + rule + "\")";
                        }
                        //Second case: only , or /
                        else if (!(rule.Contains(",") && rule.Contains("/")))
                        {
                            //Second case A: only ,
                            if (rule.Contains(","))
                            {
                                List<string> WhatItHas = new List<string>();
                                string temp = rule;
                                while (temp.Contains(","))
                                {
                                    string a = temp.Substring(0, temp.IndexOf(","));
                                    temp = temp.Remove(0, temp.IndexOf(",") + 2);
                                    WhatItHas.Add(a);
                                }
                                WhatItHas.Add(temp);
                                rule = "";
                                for (int j = 0; j < WhatItHas.Count; j++)
                                {
                                    SCItem thisThing = new SCItem(WhatItHas[j], levelName, missionPos);
                                    if (!tempItems.Contains(thisThing))
                                    {
                                        tempItems.Add(thisThing);
                                    }
                                    if (j != 0)
                                    {
                                        rule += " & ";
                                    }
                                    rule += "Has(\"" + WhatItHas[j] + "\")";
                                    rule2.Add(new List<string>());
                                    rule2[j].Add("\"" + WhatItHas[j] + "\"");
                                }
                            }
                            //Second case B: only /
                            else if (rule.Contains("/"))
                            {
                                List<string> WhatItHas = new List<string>();
                                string temp = rule;
                                while (temp.Contains("/"))
                                {
                                    string a = temp.Substring(0, temp.IndexOf("/"));
                                    temp = temp.Remove(0, temp.IndexOf("/") + 1);
                                    WhatItHas.Add(a);
                                }
                                WhatItHas.Add(temp);
                                rule = "";
                                rule2.Add(new List<string>());
                                for (int j = 0; j < WhatItHas.Count; j++)
                                {
                                    SCItem thisThing = new SCItem(WhatItHas[j], levelName, missionPos);
                                    if (!tempItems.Contains(thisThing))
                                    {
                                        tempItems.Add(thisThing);
                                    }
                                    if (j != 0)
                                    {
                                        rule += " | ";
                                    }
                                    rule += "Has(\"" + WhatItHas[j] + "\")";
                                    rule2[0].Add("\"" + WhatItHas[j] + "\"");
                                }
                            }
                        }
                        //Third case, contains both and and or
                        else if (rule.Contains(",") && rule.Contains("/"))
                        {
                            List<string> WhatItHas = new List<string>();
                            string temp = rule;
                            while (temp.Contains(","))
                            {
                                string a = temp.Substring(0, temp.IndexOf(","));
                                temp = temp.Remove(0, temp.IndexOf(",") + 2);
                                WhatItHas.Add(a);
                            }
                            WhatItHas.Add(temp);
                            List<bool> isItSingle = new List<bool>();
                            for (int j = 0; j < WhatItHas.Count; j++)
                            {
                                List<string> WhatItAlsoHas = new List<string>();
                                rule2.Add(new List<string>());
                                int currentIndexOfRule2 = rule2.Count - 1;
                                if (WhatItHas[j].Contains("/"))
                                {
                                    isItSingle.Add(false);
                                    temp = WhatItHas[j];
                                    while (temp.Contains("/"))
                                    {
                                        string a = temp.Substring(0, temp.IndexOf("/"));
                                        temp = temp.Remove(0, temp.IndexOf("/") + 1);
                                        WhatItAlsoHas.Add(a);
                                    }
                                    WhatItAlsoHas.Add(temp);
                                    WhatItHas[j] = "";
                                    List<string> WhatItHas2 = new List<string>();
                                    for (int ij = 0; ij < WhatItAlsoHas.Count; ij++)
                                    {
                                        WhatItHas2.Add(WhatItAlsoHas[ij]);
                                        SCItem thisThing = new SCItem(WhatItAlsoHas[ij], levelName, missionPos);
                                        if (!tempItems.Contains(thisThing))
                                        {
                                            tempItems.Add(thisThing);
                                        }
                                        if (ij != 0)
                                        {
                                            WhatItHas[j] += " | ";
                                        }
                                        WhatItHas[j] += "Has(\"" + WhatItAlsoHas[ij] + "\")";
                                        rule2[currentIndexOfRule2].Add("\"" + WhatItAlsoHas[ij] + "\"");
                                    }
                                }
                                else
                                {
                                    isItSingle.Add(true);
                                }
                            }
                            rule = "";
                            for (int j = 0; j < WhatItHas.Count; j++)
                            {
                                SCItem thisThing = new SCItem(WhatItHas[j], levelName, missionPos);
                                if (!tempItems.Contains(thisThing) && isItSingle[j])
                                {
                                    tempItems.Add(thisThing);
                                }
                                if (j != 0)
                                {
                                    rule += " & ";
                                }
                                if (isItSingle[j])
                                {
                                    rule += "Has(\"" + WhatItHas[j] + "\")";
                                    rule2[j].Add("\"" + WhatItHas[j] + "\"");
                                }
                                else
                                {
                                    rule += "(" + WhatItHas[j] + ")";
                                }
                            }
                        }
                        CYBRANrulesFORcybranLOCATIONS.Add(rule);
                        for (int j = 0; j < rule2.Count; j++)
                        {
                            tempRules.Add(new SCRule(levelName, rule2[j]));
                        }
                    }
                    else
                    {
                        CYBRANrulesFORcybranLOCATIONS.Add("");
                    }
                    if (i != 0 && CYBRANrulesFORcybranLOCATIONS[i - 1] != "")
                    {
                        if (CYBRANrulesFORcybranLOCATIONS[i] == "")
                        {
                            CYBRANrulesFORcybranLOCATIONS[i] = CYBRANrulesFORcybranLOCATIONS[i - 1];
                        }
                        else
                        {
                            CYBRANrulesFORcybranLOCATIONS[i] = "(" + CYBRANrulesFORcybranLOCATIONS[i - 1] + ") & (" + CYBRANrulesFORcybranLOCATIONS[i] + ")";
                        }
                    }
                    if (i > 1 && CybranLocations[i - 1] == "-" && CYBRANrulesFORcybranLOCATIONS[i - 2] != "")
                    {
                        if (CYBRANrulesFORcybranLOCATIONS[i] == "")
                        {
                            CYBRANrulesFORcybranLOCATIONS[i] = CYBRANrulesFORcybranLOCATIONS[i - 2];
                        }
                        else
                        {
                            CYBRANrulesFORcybranLOCATIONS[i] = "(" + CYBRANrulesFORcybranLOCATIONS[i - 2] + ") & (" + CYBRANrulesFORcybranLOCATIONS[i] + ")";
                        }
                    }
                }
                else
                {
                    missionPos++;
                    CYBRANrulesFORcybranLOCATIONS.Add("");
                }
            }
            for (int i = 0; i < tempItems.Count; i++)
            {
                for (int j = tempItems[i].LevelPos - 1; j < CYBRANtoCYBRANlevelNAMES.Count; j++)
                {
                    SCItem thisThing = new SCItem(tempItems[i].name, CYBRANtoCYBRANlevelNAMES[j], j);
                    AllRequeredItems.Add(thisThing);
                }
            }
            AllRequeredRules.AddRange(tempRules);
            tempItems = new List<SCItem>();
            tempRules = new List<SCRule>();
            #endregion
            //Rules if it is Aeon
            #region Aeon on Cybran rules
            List<string> AEONrulesFORcybranLOCATIONS = new List<string>();
            List<string> AEONtoCYBRANlevelNAMES = new List<string>();
            missionPos = 1;
            for (int i = 0; i < CybranLocations.Count; i++)
            {
                if (CybranLocations[i] != "-")
                {
                    string levelName = CybranLocations[i].Substring(0, CybranLocations[i].IndexOf(":")) + " (Aeon)";
                    if (!AEONtoCYBRANlevelNAMES.Contains(levelName))
                    {
                        AEONtoCYBRANlevelNAMES.Add(levelName);
                    }
                    if (CybLoc.Cells[i + 2, 5].GetCellValue<string>() != null)
                    {
                        string rule = CybLoc.Cells[i + 2, 5].GetCellValue<string>();
                        List<List<string>> rule2 = new List<List<string>>();
                        //First easy case: only 1 item needed
                        if (!rule.Contains(",") && !rule.Contains("/"))
                        {
                            SCItem thisThing = new SCItem(rule, levelName, missionPos);
                            if (!tempItems.Contains(thisThing))
                            {
                                tempItems.Add(thisThing);
                            }
                            rule2.Add(new List<string>());
                            rule2[0].Add("\"" + rule + "\"");
                            rule = "Has(\"" + rule + "\")";
                        }
                        //Second case: only , or /
                        else if (!(rule.Contains(",") && rule.Contains("/")))
                        {
                            //Second case A: only ,
                            if (rule.Contains(","))
                            {
                                List<string> WhatItHas = new List<string>();
                                string temp = rule;
                                while (temp.Contains(","))
                                {
                                    string a = temp.Substring(0, temp.IndexOf(","));
                                    temp = temp.Remove(0, temp.IndexOf(",") + 2);
                                    WhatItHas.Add(a);
                                }
                                WhatItHas.Add(temp);
                                rule = "";
                                for (int j = 0; j < WhatItHas.Count; j++)
                                {
                                    SCItem thisThing = new SCItem(WhatItHas[j], levelName, missionPos);
                                    if (!tempItems.Contains(thisThing))
                                    {
                                        tempItems.Add(thisThing);
                                    }
                                    if (j != 0)
                                    {
                                        rule += " & ";
                                    }
                                    rule += "Has(\"" + WhatItHas[j] + "\")";
                                    rule2.Add(new List<string>());
                                    rule2[j].Add("\"" + WhatItHas[j] + "\"");
                                }
                            }
                            //Second case B: only /
                            else if (rule.Contains("/"))
                            {
                                List<string> WhatItHas = new List<string>();
                                string temp = rule;
                                while (temp.Contains("/"))
                                {
                                    string a = temp.Substring(0, temp.IndexOf("/"));
                                    temp = temp.Remove(0, temp.IndexOf("/") + 1);
                                    WhatItHas.Add(a);
                                }
                                WhatItHas.Add(temp);
                                rule = "";
                                rule2.Add(new List<string>());
                                for (int j = 0; j < WhatItHas.Count; j++)
                                {
                                    SCItem thisThing = new SCItem(WhatItHas[j], levelName, missionPos);
                                    if (!tempItems.Contains(thisThing))
                                    {
                                        tempItems.Add(thisThing);
                                    }
                                    if (j != 0)
                                    {
                                        rule += " | ";
                                    }
                                    rule += "Has(\"" + WhatItHas[j] + "\")";
                                    rule2[0].Add("\"" + WhatItHas[j] + "\"");
                                }
                            }
                        }
                        //Third case, contains both and and or
                        else if (rule.Contains(",") && rule.Contains("/"))
                        {
                            List<string> WhatItHas = new List<string>();
                            string temp = rule;
                            while (temp.Contains(","))
                            {
                                string a = temp.Substring(0, temp.IndexOf(","));
                                temp = temp.Remove(0, temp.IndexOf(",") + 2);
                                WhatItHas.Add(a);
                            }
                            WhatItHas.Add(temp);
                            List<bool> isItSingle = new List<bool>();
                            for (int j = 0; j < WhatItHas.Count; j++)
                            {
                                List<string> WhatItAlsoHas = new List<string>();
                                rule2.Add(new List<string>());
                                int currentIndexOfRule2 = rule2.Count - 1;
                                if (WhatItHas[j].Contains("/"))
                                {
                                    isItSingle.Add(false);
                                    temp = WhatItHas[j];
                                    while (temp.Contains("/"))
                                    {
                                        string a = temp.Substring(0, temp.IndexOf("/"));
                                        temp = temp.Remove(0, temp.IndexOf("/") + 1);
                                        WhatItAlsoHas.Add(a);
                                    }
                                    WhatItAlsoHas.Add(temp);
                                    WhatItHas[j] = "";
                                    List<string> WhatItHas2 = new List<string>();
                                    for (int ij = 0; ij < WhatItAlsoHas.Count; ij++)
                                    {
                                        WhatItHas2.Add(WhatItAlsoHas[ij]);
                                        SCItem thisThing = new SCItem(WhatItAlsoHas[ij], levelName, missionPos);
                                        if (!tempItems.Contains(thisThing))
                                        {
                                            tempItems.Add(thisThing);
                                        }
                                        if (ij != 0)
                                        {
                                            WhatItHas[j] += " | ";
                                        }
                                        WhatItHas[j] += "Has(\"" + WhatItAlsoHas[ij] + "\")";
                                        rule2[currentIndexOfRule2].Add("\"" + WhatItAlsoHas[ij] + "\"");
                                    }
                                }
                                else
                                {
                                    isItSingle.Add(true);
                                }
                            }
                            rule = "";
                            for (int j = 0; j < WhatItHas.Count; j++)
                            {
                                SCItem thisThing = new SCItem(WhatItHas[j], levelName, missionPos);
                                if (!tempItems.Contains(thisThing) && isItSingle[j])
                                {
                                    tempItems.Add(thisThing);
                                }
                                if (j != 0)
                                {
                                    rule += " & ";
                                }
                                if (isItSingle[j])
                                {
                                    rule += "Has(\"" + WhatItHas[j] + "\")";
                                    rule2[j].Add("\"" + WhatItHas[j] + "\"");
                                }
                                else
                                {
                                    rule += "(" + WhatItHas[j] + ")";
                                }
                            }
                        }
                        AEONrulesFORcybranLOCATIONS.Add(rule);
                        for (int j = 0; j < rule2.Count; j++)
                        {
                            tempRules.Add(new SCRule(levelName, rule2[j]));
                        }
                    }
                    else
                    {
                        AEONrulesFORcybranLOCATIONS.Add("");
                    }
                    if (i != 0 && AEONrulesFORcybranLOCATIONS[i - 1] != "")
                    {
                        if (AEONrulesFORcybranLOCATIONS[i] == "")
                        {
                            AEONrulesFORcybranLOCATIONS[i] = AEONrulesFORcybranLOCATIONS[i - 1];
                        }
                        else
                        {
                            AEONrulesFORcybranLOCATIONS[i] = "(" + AEONrulesFORcybranLOCATIONS[i - 1] + ") & (" + AEONrulesFORcybranLOCATIONS[i] + ")";
                        }
                    }
                    if (i > 1 && CybranLocations[i - 1] == "-" && AEONrulesFORcybranLOCATIONS[i - 2] != "")
                    {
                        if (AEONrulesFORcybranLOCATIONS[i] == "")
                        {
                            AEONrulesFORcybranLOCATIONS[i] = AEONrulesFORcybranLOCATIONS[i - 2];
                        }
                        else
                        {
                            AEONrulesFORcybranLOCATIONS[i] = "(" + AEONrulesFORcybranLOCATIONS[i - 2] + ") & (" + AEONrulesFORcybranLOCATIONS[i] + ")";
                        }
                    }
                }
                else
                {
                    missionPos++;
                    AEONrulesFORcybranLOCATIONS.Add("");
                }
            }
            for (int i = 0; i < tempItems.Count; i++)
            {
                for (int j = tempItems[i].LevelPos - 1; j < AEONtoCYBRANlevelNAMES.Count; j++)
                {
                    SCItem thisThing = new SCItem(tempItems[i].name, AEONtoCYBRANlevelNAMES[j], j);
                    AllRequeredItems.Add(thisThing);
                }
            }
            AllRequeredRules.AddRange(tempRules);
            tempItems = new List<SCItem>();
            tempRules = new List<SCRule>();
            #endregion
            //Rules if it is Sera
            #region Sera on Cybran rules
            List<string> SERArulesFORcybranLOCATIONS = new List<string>();
            List<string> SERAtoCYBRANlevelNAMES = new List<string>();
            missionPos = 1;
            for (int i = 0; i < CybranLocations.Count; i++)
            {
                if (CybranLocations[i] != "-")
                {
                    string levelName = CybranLocations[i].Substring(0, CybranLocations[i].IndexOf(":")) + " (Sera)";
                    if (!SERAtoCYBRANlevelNAMES.Contains(levelName))
                    {
                        SERAtoCYBRANlevelNAMES.Add(levelName);
                    }
                    if (CybLoc.Cells[i + 2, 6].GetCellValue<string>() != null)
                    {
                        string rule = CybLoc.Cells[i + 2, 6].GetCellValue<string>();
                        List<List<string>> rule2 = new List<List<string>>();
                        //First easy case: only 1 item needed
                        if (!rule.Contains(",") && !rule.Contains("/"))
                        {
                            SCItem thisThing = new SCItem(rule, levelName, missionPos);
                            if (!tempItems.Contains(thisThing))
                            {
                                tempItems.Add(thisThing);
                            }
                            rule2.Add(new List<string>());
                            rule2[0].Add("\"" + rule + "\"");
                            rule = "Has(\"" + rule + "\")";
                        }
                        //Second case: only , or /
                        else if (!(rule.Contains(",") && rule.Contains("/")))
                        {
                            //Second case A: only ,
                            if (rule.Contains(","))
                            {
                                List<string> WhatItHas = new List<string>();
                                string temp = rule;
                                while (temp.Contains(","))
                                {
                                    string a = temp.Substring(0, temp.IndexOf(","));
                                    temp = temp.Remove(0, temp.IndexOf(",") + 2);
                                    WhatItHas.Add(a);
                                }
                                WhatItHas.Add(temp);
                                rule = "";
                                for (int j = 0; j < WhatItHas.Count; j++)
                                {
                                    SCItem thisThing = new SCItem(WhatItHas[j], levelName, missionPos);
                                    if (!tempItems.Contains(thisThing))
                                    {
                                        tempItems.Add(thisThing);
                                    }
                                    if (j != 0)
                                    {
                                        rule += " & ";
                                    }
                                    rule += "Has(\"" + WhatItHas[j] + "\")";
                                    rule2.Add(new List<string>());
                                    rule2[j].Add("\"" + WhatItHas[j] + "\"");
                                }
                            }
                            //Second case B: only /
                            else if (rule.Contains("/"))
                            {
                                List<string> WhatItHas = new List<string>();
                                string temp = rule;
                                while (temp.Contains("/"))
                                {
                                    string a = temp.Substring(0, temp.IndexOf("/"));
                                    temp = temp.Remove(0, temp.IndexOf("/") + 1);
                                    WhatItHas.Add(a);
                                }
                                WhatItHas.Add(temp);
                                rule = "";
                                rule2.Add(new List<string>());
                                for (int j = 0; j < WhatItHas.Count; j++)
                                {
                                    SCItem thisThing = new SCItem(WhatItHas[j], levelName, missionPos);
                                    if (!tempItems.Contains(thisThing))
                                    {
                                        tempItems.Add(thisThing);
                                    }
                                    if (j != 0)
                                    {
                                        rule += " | ";
                                    }
                                    rule += "Has(\"" + WhatItHas[j] + "\")";
                                    rule2[0].Add("\"" + WhatItHas[j] + "\"");
                                }
                            }
                        }
                        //Third case, contains both and and or
                        else if (rule.Contains(",") && rule.Contains("/"))
                        {
                            List<string> WhatItHas = new List<string>();
                            string temp = rule;
                            while (temp.Contains(","))
                            {
                                string a = temp.Substring(0, temp.IndexOf(","));
                                temp = temp.Remove(0, temp.IndexOf(",") + 2);
                                WhatItHas.Add(a);
                            }
                            WhatItHas.Add(temp);
                            List<bool> isItSingle = new List<bool>();
                            for (int j = 0; j < WhatItHas.Count; j++)
                            {
                                List<string> WhatItAlsoHas = new List<string>();
                                rule2.Add(new List<string>());
                                int currentIndexOfRule2 = rule2.Count - 1;
                                if (WhatItHas[j].Contains("/"))
                                {
                                    isItSingle.Add(false);
                                    temp = WhatItHas[j];
                                    while (temp.Contains("/"))
                                    {
                                        string a = temp.Substring(0, temp.IndexOf("/"));
                                        temp = temp.Remove(0, temp.IndexOf("/") + 1);
                                        WhatItAlsoHas.Add(a);
                                    }
                                    WhatItAlsoHas.Add(temp);
                                    WhatItHas[j] = "";
                                    List<string> WhatItHas2 = new List<string>();
                                    for (int ij = 0; ij < WhatItAlsoHas.Count; ij++)
                                    {
                                        WhatItHas2.Add(WhatItAlsoHas[ij]);
                                        SCItem thisThing = new SCItem(WhatItAlsoHas[ij], levelName, missionPos);
                                        if (!tempItems.Contains(thisThing))
                                        {
                                            tempItems.Add(thisThing);
                                        }
                                        if (ij != 0)
                                        {
                                            WhatItHas[j] += " | ";
                                        }
                                        WhatItHas[j] += "Has(\"" + WhatItAlsoHas[ij] + "\")";
                                        rule2[currentIndexOfRule2].Add("\"" + WhatItAlsoHas[ij] + "\"");
                                    }
                                }
                                else
                                {
                                    isItSingle.Add(true);
                                }
                            }
                            rule = "";
                            for (int j = 0; j < WhatItHas.Count; j++)
                            {
                                SCItem thisThing = new SCItem(WhatItHas[j], levelName, missionPos);
                                if (!tempItems.Contains(thisThing) && isItSingle[j])
                                {
                                    tempItems.Add(thisThing);
                                }
                                if (j != 0)
                                {
                                    rule += " & ";
                                }
                                if (isItSingle[j])
                                {
                                    rule += "Has(\"" + WhatItHas[j] + "\")";
                                    rule2[j].Add("\"" + WhatItHas[j] + "\"");
                                }
                                else
                                {
                                    rule += "(" + WhatItHas[j] + ")";
                                }
                            }
                        }
                        SERArulesFORcybranLOCATIONS.Add(rule);
                        for (int j = 0; j < rule2.Count; j++)
                        {
                            tempRules.Add(new SCRule(levelName, rule2[j]));
                        }
                    }
                    else
                    {
                        SERArulesFORcybranLOCATIONS.Add("");
                    }
                    if (i != 0 && SERArulesFORcybranLOCATIONS[i - 1] != "")
                    {
                        if (SERArulesFORcybranLOCATIONS[i] == "")
                        {
                            SERArulesFORcybranLOCATIONS[i] = SERArulesFORcybranLOCATIONS[i - 1];
                        }
                        else
                        {
                            SERArulesFORcybranLOCATIONS[i] = "(" + SERArulesFORcybranLOCATIONS[i - 1] + ") & (" + SERArulesFORcybranLOCATIONS[i] + ")";
                        }
                    }
                    if (i > 1 && CybranLocations[i - 1] == "-" && SERArulesFORcybranLOCATIONS[i - 2] != "")
                    {
                        if (SERArulesFORcybranLOCATIONS[i] == "")
                        {
                            SERArulesFORcybranLOCATIONS[i] = SERArulesFORcybranLOCATIONS[i - 2];
                        }
                        else
                        {
                            SERArulesFORcybranLOCATIONS[i] = "(" + SERArulesFORcybranLOCATIONS[i - 2] + ") & (" + SERArulesFORcybranLOCATIONS[i] + ")";
                        }
                    }
                }
                else
                {
                    missionPos++;
                    SERArulesFORcybranLOCATIONS.Add("");
                }
            }
            for (int i = 0; i < tempItems.Count; i++)
            {
                for (int j = tempItems[i].LevelPos - 1; j < SERAtoCYBRANlevelNAMES.Count; j++)
                {
                    SCItem thisThing = new SCItem(tempItems[i].name, SERAtoCYBRANlevelNAMES[j], j);
                    AllRequeredItems.Add(thisThing);
                }
            }
            AllRequeredRules.AddRange(tempRules);
            #endregion

            #endregion

            #endregion

            #region parse

            #region intro
            string outputString = "from __future__ import annotations" + Environment.NewLine + "from BaseClasses import Item, ItemClassification, Location, Entrance, Region"
                + Environment.NewLine  + "from rule_builder.options import OptionFilter" + Environment.NewLine + "from rule_builder.rules import Has, HasAll, Rule" + Environment.NewLine +
                "from typing import TYPE_CHECKING" + Environment.NewLine + "if TYPE_CHECKING:" + Environment.NewLine + "    from .world import SupComWorld"
                + Environment.NewLine + Environment.NewLine;
            outputString += "from .options import Mapset" + Environment.NewLine + Environment.NewLine;
            outputString += "ITEM_NAME_TO_ID = {";

            #endregion

            #region itemsID
            //Write uef items id
            for (int i = 0; i < UefItems.Count; i++)
            {
                int temp = i;
                string id = "1";
                if (temp < 100)
                {
                    if (temp < 10)
                    {
                        id += "0";
                    }
                    id += "0";
                }
                id += temp.ToString();
                outputString += "\"" + UefItems[i] + "\": " + id + ", ";
            }
            //Write cybran items id
            for (int i = 0; i < CybranItems.Count; i++)
            {
                int temp = i;
                string id = "2";
                if (temp < 100)
                {
                    if (temp < 10)
                    {
                        id += "0";
                    }
                    id += "0";
                }
                id += temp.ToString();
                outputString += "\"" + CybranItems[i] + "\": " + id + ", ";
            }
            //Write aeon items id
            for (int i = 0; i < AeonItems.Count; i++)
            {
                int temp = i;
                string id = "3";
                if (temp < 100)
                {
                    if (temp < 10)
                    {
                        id += "0";
                    }
                    id += "0";
                }
                id += temp.ToString();
                outputString += "\"" + AeonItems[i] + "\": " + id + ", ";
            }
            //Write sera items id
            for (int i = 0; i < SeraItems.Count; i++)
            {
                int temp = i;
                string id = "4";
                if (temp < 100)
                {
                    if (temp < 10)
                    {
                        id += "0";
                    }
                    id += "0";
                }
                id += temp.ToString();
                outputString += "\"" + SeraItems[i] + "\": " + id + ", ";
            }
            //Write filler items id
            for (int i = 0; i < FillerItems.Count; i++)
            {
                int temp = i;
                string id = "5";
                if (temp < 100)
                {
                    if (temp < 10)
                    {
                        id += "0";
                    }
                    id += "0";
                }
                id += temp.ToString();
                outputString += "\"" + FillerItems[i] + "\": " + id + ", ";
            }
            outputString += "}" + Environment.NewLine;
            #endregion

            #region itemsType
            outputString += "DEFAULT_ITEM_CLASSIFICATIONS = {";
            //Write uef items type
            for (int i = 0; i < UefItems.Count; i++)
            {

                outputString += "\"" + UefItems[i] + "\": ItemClassification.progression | ItemClassification.useful, ";
            }
            //Write cybran items type
            for (int i = 0; i < CybranItems.Count; i++)
            {

                outputString += "\"" + CybranItems[i] + "\": ItemClassification.progression | ItemClassification.useful, ";
            }
            //Write aeon items type
            for (int i = 0; i < AeonItems.Count; i++)
            {

                outputString += "\"" + AeonItems[i] + "\": ItemClassification.progression | ItemClassification.useful, ";
            }
            //Write sera items type
            for (int i = 0; i < SeraItems.Count; i++)
            {

                outputString += "\"" + SeraItems[i] + "\": ItemClassification.progression | ItemClassification.useful, ";
            }
            //Write filler items type
            for (int i = 0; i < FillerItems.Count; i++)
            {

                outputString += "\"" + FillerItems[i] + "\": ItemClassification.filler, ";
            }
            outputString += "}" + Environment.NewLine + Environment.NewLine;
            #endregion

            #region items separate

            //Write uef items
            outputString += "uef_items = [";
            for (int i = 0; i < UefItems.Count; i++)
            {
                outputString += "\"" + UefItems[i] + "\"";
                int temp = i + 1;
                if (temp != UefItems.Count)
                {
                    outputString += ", ";
                }
            }
            outputString += "]" + Environment.NewLine;
            //Write cybran items
            outputString += "cybran_items = [";
            for (int i = 0; i < CybranItems.Count; i++)
            {
                outputString += "\"" + CybranItems[i] + "\"";
                int temp = i + 1;
                if (temp != CybranItems.Count)
                {
                    outputString += ", ";
                }
            }
            outputString += "]" + Environment.NewLine;
            //Write aeon items
            outputString += "aeon_items = [";
            for (int i = 0; i < AeonItems.Count; i++)
            {
                outputString += "\"" + AeonItems[i] + "\"";
                int temp = i + 1;
                if (temp != AeonItems.Count)
                {
                    outputString += ", ";
                }
            }
            outputString += "]" + Environment.NewLine;
            //Write sera items
            outputString += "sera_items = [";
            for (int i = 0; i < SeraItems.Count; i++)
            {
                outputString += "\"" + SeraItems[i] + "\"";
                int temp = i + 1;
                if (temp != SeraItems.Count)
                {
                    outputString += ", ";
                }
            }
            outputString += "]" + Environment.NewLine;
            //Write filler items
            outputString += "filler_items = [";
            for (int i = 0; i < FillerItems.Count; i++)
            {
                outputString += "\"" + FillerItems[i] + "\"";
                int temp = i + 1;
                if (temp != FillerItems.Count)
                {
                    outputString += ", ";
                }
            }
            outputString += "]" + Environment.NewLine + Environment.NewLine;
            #endregion

            #region locations to list
            outputString += "LOCATION_NAME_TO_ID = {";
            //Write cybran locations
            int mission = 1;
            int localID = 0;
            for (int j = 0; j < 4; j++)
            {
                mission = 1;
                localID = 0;
                for (int i = 0; i < CybranLocations.Count; i++)
                {
                    if (CybranLocations[i] == "-")
                    {
                        mission += 1;
                        localID = 0;
                    }
                    else
                    {
                        for (int ij = 0; ij < 16; ij++)
                        {
                            string faction = "";
                            switch (j)
                            {
                                case 0:
                                    faction = " (UEF) ";
                                    break;
                                case 1:
                                    faction = " (Cybran) ";
                                    break;
                                case 2:
                                    faction = " (Aeon Illuminate) ";
                                    break;
                                case 3:
                                    faction = " (Serafim) ";
                                    break;
                                default:
                                    break;
                            }
                            int facN = j + 1;
                            string id = "2" + facN.ToString();
                            if (mission < 10)
                            {
                                id += "0";
                            }
                            id += mission.ToString();
                            if (localID < 10)
                            {
                                id += "0";
                            }
                            id += localID.ToString();
                            if (ij < 10)
                            {
                                id += "0";
                            }
                            id += ij.ToString();
                            int copyN = ij + 1;
                            outputString += "\"" + CybranLocations[i] + faction + copyN + "\": " + id + ", ";
                        }

                        localID += 1;
                    }
                }
            }
            
            outputString += "}";
            outputString += Environment.NewLine;
            #endregion

            #region classes
            outputString += Environment.NewLine + "class SupComLocation(Location):" + Environment.NewLine + "    game = \"Supreme Commander\"" + Environment.NewLine + Environment.NewLine;
            outputString += "class SupComItem(Item):" + Environment.NewLine + "    game = \"Supreme Commander\"" + Environment.NewLine + Environment.NewLine;
            outputString += "THE_GRID = []" + Environment.NewLine + Environment.NewLine;
            #endregion

            outputString += "def makeEverything(world: SupComWorld) -> None:" + Environment.NewLine + Environment.NewLine;

            #region level grid

            #region create list of levels here
            //Get list of cybran levels
            List<string> CybranLevelList = new List<string>();
            for (int i = 0; i < CybranLocations.Count; i++)
            {
                if (CybranLocations[i] != "-")
                {
                    string RegionName = CybranLocations[i].Substring(0, CybranLocations[i].IndexOf(":"));
                    if (!CybranLevelList.Contains(RegionName))
                    {
                        CybranLevelList.Add(RegionName);
                    }
                }
            }
            //Get every cybran level it's own list of objectives from first to last and also rules for every faction
            List<SCLevel> FullListOfLevels = new List<SCLevel>();
            for (int i = 0; i < CybranLevelList.Count; i++)
            {
                List<string> localObjList = new List<string>();
                List<string> localURList = new List<string>();
                List<string> localCRList = new List<string>();
                List<string> localARList = new List<string>();
                List<string> localSRList = new List<string>();
                for (int j = 0; j < CybranLocations.Count; j++)
                {
                    if (CybranLocations[j] != "-")
                    {
                        string RegionName = CybranLocations[j].Substring(0, CybranLocations[j].IndexOf(":"));
                        if (RegionName == CybranLevelList[i])
                        {
                            localObjList.Add(CybranLocations[j]);
                            localURList.Add(UEFrulesFORcybranLOCATIONS[j]);
                            localCRList.Add(CYBRANrulesFORcybranLOCATIONS[j]);
                            localARList.Add(AEONrulesFORcybranLOCATIONS[j]);
                            localSRList.Add(SERArulesFORcybranLOCATIONS[j]);
                        }
                    }
                }
                FullListOfLevels.Add(new SCLevel(CybranLevelList[i], localObjList, localURList, localCRList, localARList, localSRList, LevelSheet.Cells[i + 2, 3].GetCellValue<int>(), LevelSheet.Cells[i + 2, 4].GetCellValue<int>()));
            }
            #endregion

            #region write 4 tiered lists
            //Create lists of levels depending on tier
            //During grid creation 1 level must be tier 1, 1 level must be tier 4 and 2 levels must be tier 2
            //Everithing else is thrown from tier 3 list which contains every single level enabled

            outputString += "    " + "levelsTier1FOREVER = []" + Environment.NewLine;
            outputString += "    " + "levelsTier1 = []" + Environment.NewLine;
            outputString += "    " + "levelsTier2 = []" + Environment.NewLine;
            outputString += "    " + "levelsTier3 = []" + Environment.NewLine;
            outputString += "    " + "levelsTier4 = []" + Environment.NewLine;

            #region Default factions (boring version)

            outputString += "    " + "if not world.options.randfacs:" + Environment.NewLine; 
            for (int i = 0; i < FullListOfLevels.Count; i++)
            {
                if (FullListOfLevels[i].tier == 1)
                {
                    if (FullListOfLevels[i].default_faction == 0)
                    {
                        outputString += "    " + "    levelsTier1.append(\"" + FullListOfLevels[i].name + " (UEF)\")" + Environment.NewLine;
                        outputString += "    " + "    levelsTier1FOREVER.append(\"" + FullListOfLevels[i].name + " (UEF)\")" + Environment.NewLine;
                        outputString += "    " + "    levelsTier2.append(\"" + FullListOfLevels[i].name + " (UEF)\")" + Environment.NewLine;
                        outputString += "    " + "    levelsTier3.append(\"" + FullListOfLevels[i].name + " (UEF)\")" + Environment.NewLine;
                    }
                    else if (FullListOfLevels[i].default_faction == 1)
                    {
                        outputString += "    " + "    levelsTier1.append(\"" + FullListOfLevels[i].name + " (Cybran)\")" + Environment.NewLine;
                        outputString += "    " + "    levelsTier1FOREVER.append(\"" + FullListOfLevels[i].name + " (Cybran)\")" + Environment.NewLine;
                        outputString += "    " + "    levelsTier2.append(\"" + FullListOfLevels[i].name + " (Cybran)\")" + Environment.NewLine;
                        outputString += "    " + "    levelsTier3.append(\"" + FullListOfLevels[i].name + " (Cybran)\")" + Environment.NewLine;
                    }
                    else if (FullListOfLevels[i].default_faction == 2)
                    {
                        outputString += "    " + "    levelsTier1.append(\"" + FullListOfLevels[i].name + " (Aeon)\")" + Environment.NewLine;
                        outputString += "    " + "    levelsTier1FOREVER.append(\"" + FullListOfLevels[i].name + " (Aeon)\")" + Environment.NewLine;
                        outputString += "    " + "    levelsTier2.append(\"" + FullListOfLevels[i].name + " (Aeon)\")" + Environment.NewLine;
                        outputString += "    " + "    levelsTier3.append(\"" + FullListOfLevels[i].name + " (Aeon)\")" + Environment.NewLine;
                    }
                    else
                    {
                        outputString += "    " + "    levelsTier1.append(\"" + FullListOfLevels[i].name + " (Sera)\")" + Environment.NewLine;
                        outputString += "    " + "    levelsTier1FOREVER.append(\"" + FullListOfLevels[i].name + " (Sera)\")" + Environment.NewLine;
                        outputString += "    " + "    levelsTier2.append(\"" + FullListOfLevels[i].name + " (Sera)\")" + Environment.NewLine;
                        outputString += "    " + "    levelsTier3.append(\"" + FullListOfLevels[i].name + " (Sera)\")" + Environment.NewLine;
                    }
                }

            }
            for (int i = 0; i < FullListOfLevels.Count; i++)
            {
                if (FullListOfLevels[i].tier == 2)
                {
                    if (FullListOfLevels[i].default_faction == 0)
                    {
                        outputString += "    " + "    levelsTier2.append(\"" + FullListOfLevels[i].name + " (UEF)\")" + Environment.NewLine;
                        outputString += "    " + "    levelsTier3.append(\"" + FullListOfLevels[i].name + " (UEF)\")" + Environment.NewLine;
                    }
                    else if (FullListOfLevels[i].default_faction == 1)
                    {
                        outputString += "    " + "    levelsTier2.append(\"" + FullListOfLevels[i].name + " (Cybran)\")" + Environment.NewLine;
                        outputString += "    " + "    levelsTier3.append(\"" + FullListOfLevels[i].name + " (Cybran)\")" + Environment.NewLine;
                    }
                    else if (FullListOfLevels[i].default_faction == 2)
                    {
                        outputString += "    " + "    levelsTier2.append(\"" + FullListOfLevels[i].name + " (Aeon)\")" + Environment.NewLine;
                        outputString += "    " + "    levelsTier3.append(\"" + FullListOfLevels[i].name + " (Aeon)\")" + Environment.NewLine;
                    }
                    else
                    {
                        outputString += "    " + "    levelsTier2.append(\"" + FullListOfLevels[i].name + " (Sera)\")" + Environment.NewLine;
                        outputString += "    " + "    levelsTier3.append(\"" + FullListOfLevels[i].name + " (Sera)\")" + Environment.NewLine;
                    }
                }

            }
            for (int i = 0; i < FullListOfLevels.Count; i++)
            {
                if (FullListOfLevels[i].tier == 3)
                {
                    if (FullListOfLevels[i].default_faction == 0)
                    {
                        outputString += "    " + "    levelsTier3.append(\"" + FullListOfLevels[i].name + " (UEF)\")" + Environment.NewLine;
                    }
                    else if (FullListOfLevels[i].default_faction == 1)
                    {
                        outputString += "    " + "    levelsTier3.append(\"" + FullListOfLevels[i].name + " (Cybran)\")" + Environment.NewLine;
                    }
                    else if (FullListOfLevels[i].default_faction == 2)
                    {
                        outputString += "    " + "    levelsTier3.append(\"" + FullListOfLevels[i].name + " (Aeon)\")" + Environment.NewLine;
                    }
                    else
                    {
                        outputString += "    " + "    levelsTier3.append(\"" + FullListOfLevels[i].name + " (Sera)\")" + Environment.NewLine;
                    }
                }
            }
            for (int i = 0; i < FullListOfLevels.Count; i++)
            {
                if (FullListOfLevels[i].tier == 4)
                {
                    if (FullListOfLevels[i].default_faction == 0)
                    {
                        outputString += "    " + "    levelsTier4.append(\"" + FullListOfLevels[i].name + " (UEF)\")" + Environment.NewLine;
                        outputString += "    " + "    levelsTier3.append(\"" + FullListOfLevels[i].name + " (UEF)\")" + Environment.NewLine;
                    }
                    else if (FullListOfLevels[i].default_faction == 1)
                    {
                        outputString += "    " + "    levelsTier4.append(\"" + FullListOfLevels[i].name + " (Cybran)\")" + Environment.NewLine;
                        outputString += "    " + "    levelsTier3.append(\"" + FullListOfLevels[i].name + " (Cybran)\")" + Environment.NewLine;
                    }
                    else if (FullListOfLevels[i].default_faction == 2)
                    {
                        outputString += "    " + "    levelsTier4.append(\"" + FullListOfLevels[i].name + " (Aeon)\")" + Environment.NewLine;
                        outputString += "    " + "    levelsTier3.append(\"" + FullListOfLevels[i].name + " (Aeon)\")" + Environment.NewLine;
                    }
                    else
                    {
                        outputString += "    " + "    levelsTier4.append(\"" + FullListOfLevels[i].name + " (Sera)\")" + Environment.NewLine;
                        outputString += "    " + "    levelsTier3.append(\"" + FullListOfLevels[i].name + " (Sera)\")" + Environment.NewLine;
                    }
                }

            }

            #endregion

            #region Mapset Unique

            outputString += "    " + "elif world.options.mapset == Mapset.option_unique:" + Environment.NewLine;

            for (int i = 0; i < FullListOfLevels.Count; i++)
            {
                if (FullListOfLevels[i].tier == 1)
                {
                    outputString += "    " + "    temp = world.random.randrange(0, len(world.options.faction.value))" + Environment.NewLine;
                    outputString += "    " + "    if world.options.faction.value[temp] == \"uef\":" + Environment.NewLine;
                    outputString += "    " + "        levelsTier1.append(\"" + FullListOfLevels[i].name + " (UEF)\")" + Environment.NewLine;
                    outputString += "    " + "        levelsTier1FOREVER.append(\"" + FullListOfLevels[i].name + " (UEF)\")" + Environment.NewLine;
                    outputString += "    " + "        levelsTier2.append(\"" + FullListOfLevels[i].name + " (UEF)\")" + Environment.NewLine;
                    outputString += "    " + "        levelsTier3.append(\"" + FullListOfLevels[i].name + " (UEF)\")" + Environment.NewLine;
                    outputString += "    " + "    elif  world.options.faction.value[temp] == \"cybran\":" + Environment.NewLine;
                    outputString += "    " + "        levelsTier1.append(\"" + FullListOfLevels[i].name + " (Cybran)\")" + Environment.NewLine;
                    outputString += "    " + "        levelsTier1FOREVER.append(\"" + FullListOfLevels[i].name + " (Cybran)\")" + Environment.NewLine;
                    outputString += "    " + "        levelsTier2.append(\"" + FullListOfLevels[i].name + " (Cybran)\")" + Environment.NewLine;
                    outputString += "    " + "        levelsTier3.append(\"" + FullListOfLevels[i].name + " (Cybran)\")" + Environment.NewLine;
                    outputString += "    " + "    elif  world.options.faction.value[temp] == \"aeon\":" + Environment.NewLine;
                    outputString += "    " + "        levelsTier1.append(\"" + FullListOfLevels[i].name + " (Aeon)\")" + Environment.NewLine;
                    outputString += "    " + "        levelsTier1FOREVER.append(\"" + FullListOfLevels[i].name + " (Aeon)\")" + Environment.NewLine;
                    outputString += "    " + "        levelsTier2.append(\"" + FullListOfLevels[i].name + " (Aeon)\")" + Environment.NewLine;
                    outputString += "    " + "        levelsTier3.append(\"" + FullListOfLevels[i].name + " (Aeon)\")" + Environment.NewLine;
                    outputString += "    " + "    elif  world.options.faction.value[temp] == \"sera\":" + Environment.NewLine;
                    outputString += "    " + "        levelsTier1.append(\"" + FullListOfLevels[i].name + " (Sera)\")" + Environment.NewLine;
                    outputString += "    " + "        levelsTier1FOREVER.append(\"" + FullListOfLevels[i].name + " (Sera)\")" + Environment.NewLine;
                    outputString += "    " + "        levelsTier2.append(\"" + FullListOfLevels[i].name + " (Sera)\")" + Environment.NewLine;
                    outputString += "    " + "        levelsTier3.append(\"" + FullListOfLevels[i].name + " (Sera)\")" + Environment.NewLine;
                }
            }
            for (int i = 0; i < FullListOfLevels.Count; i++)
            {
                if (FullListOfLevels[i].tier == 2)
                {
                    outputString += "    " + "    temp = world.random.randrange(0, len(world.options.faction.value))" + Environment.NewLine;
                    outputString += "    " + "    if world.options.faction.value[temp] == \"uef\":" + Environment.NewLine + "    " + "        levelsTier2.append(\"" +
                        FullListOfLevels[i].name + " (UEF)\")" + Environment.NewLine + "    " + "        levelsTier3.append(\"" +
                        FullListOfLevels[i].name + " (UEF)\")" + Environment.NewLine +
                        "    " + "    elif  world.options.faction.value[temp] == \"cybran\":" + Environment.NewLine + "    " + "        levelsTier2.append(\"" +
                        FullListOfLevels[i].name + " (Cybran)\")" + Environment.NewLine + "    " + "        levelsTier3.append(\"" +
                        FullListOfLevels[i].name + " (Cybran)\")" + Environment.NewLine +
                        "    " + "    elif  world.options.faction.value[temp] == \"aeon\":" + Environment.NewLine + "    " + "        levelsTier2.append(\"" +
                        FullListOfLevels[i].name + " (Aeon)\")" + Environment.NewLine + "    " + "        levelsTier3.append(\"" +
                        FullListOfLevels[i].name + " (Aeon)\")" + Environment.NewLine +
                        "    " + "    elif  world.options.faction.value[temp] == \"sera\":" + Environment.NewLine + "    " + "        levelsTier2.append(\"" +
                        FullListOfLevels[i].name + " (Sera)\")" + Environment.NewLine + "    " + "        levelsTier3.append(\"" +
                        FullListOfLevels[i].name + " (Sera)\")" + Environment.NewLine;
                }
            }
            for (int i = 0; i < FullListOfLevels.Count; i++)
            {
                if (FullListOfLevels[i].tier == 3)
                {
                    outputString += "    " + "    temp = world.random.randrange(0, len(world.options.faction.value))" + Environment.NewLine;
                    outputString += "    " + "    if world.options.faction.value[temp] == \"uef\":" + Environment.NewLine + "    " + "        levelsTier3.append(\"" +
                        FullListOfLevels[i].name + " (UEF)\")" + Environment.NewLine +
                        "    " + "    elif  world.options.faction.value[temp] == \"cybran\":" + Environment.NewLine + "    " + "        levelsTier3.append(\"" +
                        FullListOfLevels[i].name + " (Cybran)\")" + Environment.NewLine +
                        "    " + "    elif  world.options.faction.value[temp] == \"aeon\":" + Environment.NewLine + "    " + "        levelsTier3.append(\"" +
                        FullListOfLevels[i].name + " (Aeon)\")" + Environment.NewLine +
                        "    " + "    elif  world.options.faction.value[temp] == \"sera\":" + Environment.NewLine + "    " + "        levelsTier3.append(\"" +
                        FullListOfLevels[i].name + " (Sera)\")" + Environment.NewLine;
                }
            }
            for (int i = 0; i < FullListOfLevels.Count; i++)
            {
                if (FullListOfLevels[i].tier == 4)
                {
                    outputString += "    " + "    temp = world.random.randrange(0, len(world.options.faction.value))" + Environment.NewLine;
                    outputString += "    " + "    if world.options.faction.value[temp] == \"uef\":" + Environment.NewLine + "    " + "        levelsTier4.append(\"" +
                        FullListOfLevels[i].name + " (UEF)\")" + Environment.NewLine + "    " + "        levelsTier3.append(\"" +
                        FullListOfLevels[i].name + " (UEF)\")" + Environment.NewLine +
                        "    " + "    elif  world.options.faction.value[temp] == \"cybran\":" + Environment.NewLine + "    " + "        levelsTier4.append(\"" +
                        FullListOfLevels[i].name + " (Cybran)\")" + Environment.NewLine + "    " + "        levelsTier3.append(\"" +
                        FullListOfLevels[i].name + " (Cybran)\")" + Environment.NewLine +
                        "    " + "    elif  world.options.faction.value[temp] == \"aeon\":" + Environment.NewLine + "    " + "        levelsTier4.append(\"" +
                        FullListOfLevels[i].name + " (Aeon)\")" + Environment.NewLine + "    " + "        levelsTier3.append(\"" +
                        FullListOfLevels[i].name + " (Aeon)\")" + Environment.NewLine +
                        "    " + "    elif  world.options.faction.value[temp] == \"sera\":" + Environment.NewLine + "    " + "        levelsTier4.append(\"" +
                        FullListOfLevels[i].name + " (Sera)\")" + Environment.NewLine + "    " + "        levelsTier3.append(\"" +
                        FullListOfLevels[i].name + " (Sera)\")" + Environment.NewLine;
                }
            }

            #endregion

            #region Mapset ALL
            outputString += "    " + "else:" + Environment.NewLine;
            for (int i = 0; i < FullListOfLevels.Count; i++)
            {
                if (FullListOfLevels[i].tier == 1)
                {
                    outputString += "    " + "    if \"uef\" in world.options.faction:" + Environment.NewLine;
                    outputString += "    " + "        levelsTier1.append(\"" + FullListOfLevels[i].name + " (UEF)\")" + Environment.NewLine;
                    outputString += "    " + "        levelsTier1FOREVER.append(\"" + FullListOfLevels[i].name + " (UEF)\")" + Environment.NewLine;
                    outputString += "    " + "        levelsTier2.append(\"" + FullListOfLevels[i].name + " (UEF)\")" + Environment.NewLine;
                    outputString += "    " + "        levelsTier3.append(\"" + FullListOfLevels[i].name + " (UEF)\")" + Environment.NewLine;
                    outputString += "    " + "    if \"cybran\" in world.options.faction:" + Environment.NewLine;
                    outputString += "    " + "        levelsTier1.append(\"" + FullListOfLevels[i].name + " (Cybran)\")" + Environment.NewLine;
                    outputString += "    " + "        levelsTier1FOREVER.append(\"" + FullListOfLevels[i].name + " (Cybran)\")" + Environment.NewLine;
                    outputString += "    " + "        levelsTier2.append(\"" + FullListOfLevels[i].name + " (Cybran)\")" + Environment.NewLine;
                    outputString += "    " + "        levelsTier3.append(\"" + FullListOfLevels[i].name + " (Cybran)\")" + Environment.NewLine;
                    outputString += "    " + "    if \"aeon\" in world.options.faction:" + Environment.NewLine;
                    outputString += "    " + "        levelsTier1.append(\"" + FullListOfLevels[i].name + " (Aeon)\")" + Environment.NewLine;
                    outputString += "    " + "        levelsTier1FOREVER.append(\"" + FullListOfLevels[i].name + " (Aeon)\")" + Environment.NewLine;
                    outputString += "    " + "        levelsTier2.append(\"" + FullListOfLevels[i].name + " (Aeon)\")" + Environment.NewLine;
                    outputString += "    " + "        levelsTier3.append(\"" + FullListOfLevels[i].name + " (Aeon)\")" + Environment.NewLine;
                    outputString += "    " + "    if \"sera\" in world.options.faction:" + Environment.NewLine;
                    outputString += "    " + "        levelsTier1.append(\"" + FullListOfLevels[i].name + " (Sera)\")" + Environment.NewLine;
                    outputString += "    " + "        levelsTier1FOREVER.append(\"" + FullListOfLevels[i].name + " (Sera)\")" + Environment.NewLine;
                    outputString += "    " + "        levelsTier2.append(\"" + FullListOfLevels[i].name + " (Sera)\")" + Environment.NewLine;
                    outputString += "    " + "        levelsTier3.append(\"" + FullListOfLevels[i].name + " (Sera)\")" + Environment.NewLine;
                }
            }
            for (int i = 0; i < FullListOfLevels.Count; i++)
            {
                if (FullListOfLevels[i].tier == 2)
                {
                    outputString += "    " + "    if \"uef\" in world.options.faction:" + Environment.NewLine;
                    outputString += "    " + "        levelsTier2.append(\"" + FullListOfLevels[i].name + " (UEF)\")" + Environment.NewLine;
                    outputString += "    " + "        levelsTier3.append(\"" + FullListOfLevels[i].name + " (UEF)\")" + Environment.NewLine;
                    outputString += "    " + "    if \"cybran\" in world.options.faction:" + Environment.NewLine;
                    outputString += "    " + "        levelsTier2.append(\"" + FullListOfLevels[i].name + " (Cybran)\")" + Environment.NewLine;
                    outputString += "    " + "        levelsTier3.append(\"" + FullListOfLevels[i].name + " (Cybran)\")" + Environment.NewLine;
                    outputString += "    " + "    if \"aeon\" in world.options.faction:" + Environment.NewLine;
                    outputString += "    " + "        levelsTier2.append(\"" + FullListOfLevels[i].name + " (Aeon)\")" + Environment.NewLine;
                    outputString += "    " + "        levelsTier3.append(\"" + FullListOfLevels[i].name + " (Aeon)\")" + Environment.NewLine;
                    outputString += "    " + "    if \"sera\" in world.options.faction:" + Environment.NewLine;
                    outputString += "    " + "        levelsTier2.append(\"" + FullListOfLevels[i].name + " (Sera)\")" + Environment.NewLine;
                    outputString += "    " + "        levelsTier3.append(\"" + FullListOfLevels[i].name + " (Sera)\")" + Environment.NewLine;
                }
            }
            for (int i = 0; i < FullListOfLevels.Count; i++)
            {
                if (FullListOfLevels[i].tier == 3)
                {
                    outputString += "    " + "    if \"uef\" in world.options.faction:" + Environment.NewLine;
                    outputString += "    " + "        levelsTier3.append(\"" + FullListOfLevels[i].name + " (UEF)\")" + Environment.NewLine;
                    outputString += "    " + "    if \"cybran\" in world.options.faction:" + Environment.NewLine;
                    outputString += "    " + "        levelsTier3.append(\"" + FullListOfLevels[i].name + " (Cybran)\")" + Environment.NewLine;
                    outputString += "    " + "    if \"aeon\" in world.options.faction:" + Environment.NewLine;
                    outputString += "    " + "        levelsTier3.append(\"" + FullListOfLevels[i].name + " (Aeon)\")" + Environment.NewLine;
                    outputString += "    " + "    if \"sera\" in world.options.faction:" + Environment.NewLine;
                    outputString += "    " + "        levelsTier3.append(\"" + FullListOfLevels[i].name + " (Sera)\")" + Environment.NewLine;
                }
            }
            for (int i = 0; i < FullListOfLevels.Count; i++)
            {
                if (FullListOfLevels[i].tier == 4)
                {
                    outputString += "    " + "    if \"uef\" in world.options.faction:" + Environment.NewLine;
                    outputString += "    " + "        levelsTier4.append(\"" + FullListOfLevels[i].name + " (UEF)\")" + Environment.NewLine;
                    outputString += "    " + "        levelsTier3.append(\"" + FullListOfLevels[i].name + " (UEF)\")" + Environment.NewLine;
                    outputString += "    " + "    if \"cybran\" in world.options.faction:" + Environment.NewLine;
                    outputString += "    " + "        levelsTier4.append(\"" + FullListOfLevels[i].name + " (Cybran)\")" + Environment.NewLine;
                    outputString += "    " + "        levelsTier3.append(\"" + FullListOfLevels[i].name + " (Cybran)\")" + Environment.NewLine;
                    outputString += "    " + "    if \"aeon\" in world.options.faction:" + Environment.NewLine;
                    outputString += "    " + "        levelsTier4.append(\"" + FullListOfLevels[i].name + " (Aeon)\")" + Environment.NewLine;
                    outputString += "    " + "        levelsTier3.append(\"" + FullListOfLevels[i].name + " (Aeon)\")" + Environment.NewLine;
                    outputString += "    " + "    if \"sera\" in world.options.faction:" + Environment.NewLine;
                    outputString += "    " + "        levelsTier4.append(\"" + FullListOfLevels[i].name + " (Sera)\")" + Environment.NewLine;
                    outputString += "    " + "        levelsTier3.append(\"" + FullListOfLevels[i].name + " (Sera)\")" + Environment.NewLine;
                }
            }
            #endregion

            #endregion

            #region grid
            //Now to grid generation
            //First thing that must be done is calculation of closest possible height and width
            outputString += Environment.NewLine + "    " + "amountOfLevels = len(levelsTier3)" + Environment.NewLine;
            outputString += "    " + "AllLevelsListToCheckRegionCreation = []" + Environment.NewLine;
            outputString += "    " + "possibleAnswers = []" + Environment.NewLine;
            outputString += "    " + "for i in range(1, amountOfLevels + 1):" + Environment.NewLine;
            outputString += "    " + "    if amountOfLevels % i == 0:" + Environment.NewLine;
            outputString += "    " + "        possibleAnswers.append(i)" + Environment.NewLine;
            outputString += "    " + "        if amountOfLevels / i == i:" +  Environment.NewLine;
            outputString += "    " + "            possibleAnswers.append(i)" + Environment.NewLine;
            outputString += "    " + "Width = possibleAnswers[int(len(possibleAnswers) / 2)]" +    Environment.NewLine;
            outputString += "    " + "Height = possibleAnswers[int(len(possibleAnswers) / 2) - 1]" + Environment.NewLine + Environment.NewLine;

            outputString += "    " + "THE_GRID = [[\"\" for i in range(Height)] for j in range(Width)]" + Environment.NewLine;

            outputString += "    " + "temp = world.random.randrange(0,len(levelsTier1))" + Environment.NewLine;
            outputString += "    " + "THE_GRID[0][0] = levelsTier1[temp]" + Environment.NewLine;
            outputString += "    " + "AllLevelsListToCheckRegionCreation.append(levelsTier1[temp])" + Environment.NewLine;
            outputString += "    " + "levelsTier3.remove(levelsTier1[temp])" + Environment.NewLine;
            outputString += "    " + "levelsTier2.remove(levelsTier1[temp])" + Environment.NewLine;
            outputString += "    " + "levelsTier1.remove(levelsTier1[temp])" +  Environment.NewLine;
            outputString += "    " + "temp = world.random.randrange(0,len(levelsTier2))" + Environment.NewLine;

            outputString += "    " + "THE_GRID[0][1] = levelsTier2[temp]" + Environment.NewLine;
            outputString += "    " + "AllLevelsListToCheckRegionCreation.append(levelsTier2[temp])" + Environment.NewLine;
            outputString += "    " + "levelsTier3.remove(levelsTier2[temp])" + Environment.NewLine;
            outputString += "    " + "levelsTier2.remove(levelsTier2[temp])" +  Environment.NewLine;
            outputString += "    " + "temp = world.random.randrange(0,len(levelsTier2))" +  Environment.NewLine;

            outputString += "    " + "THE_GRID[1][0] = levelsTier2[temp]" + Environment.NewLine;
            outputString += "    " + "AllLevelsListToCheckRegionCreation.append(levelsTier2[temp])" + Environment.NewLine;
            outputString += "    " + "levelsTier3.remove(levelsTier2[temp])" + Environment.NewLine;
            outputString += "    " + "levelsTier2.remove(levelsTier2[temp])" +  Environment.NewLine;
            outputString += "    " + "temp = world.random.randrange(0,len(levelsTier4))" +  Environment.NewLine;

            outputString += "    " + "THE_GRID[Width - 1][Height - 1] = levelsTier4[temp]" + Environment.NewLine;
            outputString += "    " + "AllLevelsListToCheckRegionCreation.append(levelsTier4[temp])" + Environment.NewLine;
            outputString += "    " + "levelsTier3.remove(levelsTier4[temp])" + Environment.NewLine;
            outputString += "    " + "levelsTier4.remove(levelsTier4[temp])" +  Environment.NewLine + Environment.NewLine;

            outputString += "    " + "for i in range(Width):" + Environment.NewLine;
            outputString += "    " + "    for j in range(Height):" + Environment.NewLine;
            outputString += "    " + "        CheckFilled = bool(not((i == 0 and j == 0) or (i == 1 and j == 0) or (i == 0 and j == 1) or (i == Width - 1 and j == Height - 1)))" + Environment.NewLine;
            outputString += "    " + "        if CheckFilled:" + Environment.NewLine;
            outputString += "    " + "            temp = world.random.randrange(0,len(levelsTier3))" +  Environment.NewLine;
            outputString += "    " + "            THE_GRID[i][j] = levelsTier3[temp]" + Environment.NewLine;
            outputString += "    " + "            AllLevelsListToCheckRegionCreation.append(levelsTier3[temp])" + Environment.NewLine;
            outputString += "    " + "            levelsTier3.remove(levelsTier3[temp])" +   Environment.NewLine + Environment.NewLine;

            outputString += "    " + "world.THE_GRID = THE_GRID" + Environment.NewLine + Environment.NewLine;

            #endregion

            #endregion

            #region create regions

            //Write cybran locations
            outputString += "    " + "DictionaryOfRegions = {}" + Environment.NewLine;
            List<string> CybranRegions = new List<string>();
            mission = 1;
            localID = 0;
            for (int j = 0; j < 4; j++)
            {
                string faction = "";
                switch (j)
                {
                    case 0:
                        faction = "UEF";
                        break;
                    case 1:
                        faction = "Cybran";
                        break;
                    case 2:
                        faction = "Aeon";
                        break;
                    case 3:
                        faction = "Sera";
                        break;
                    default:
                        break;
                }
                mission = 1;
                localID = 0;
                for (int i = 0; i < CybranLocations.Count; i++)
                {
                    if (CybranLocations[i] == "-")
                    {
                        mission += 1;
                        localID = 0;
                    }
                    else
                    {
                        string RegionName = CybranLocations[i].Substring(0, CybranLocations[i].IndexOf(":"));
                        while (RegionName.Contains(" "))
                        {
                            RegionName = RegionName.Remove(RegionName.IndexOf(" "), 1);
                        }
                        string current_location = CybranLocations[i] + " (" + faction + ")";
                        string objID = "2" + (j + 1).ToString();
                        if (mission < 10)
                        {
                            objID += "0";
                        }
                        objID += mission.ToString();
                        if (localID < 10)
                        {
                            objID += "0";
                        }
                        objID += localID;
                        string levelName = CybranLocations[i].Substring(0, CybranLocations[i].IndexOf(":")) + " (" + faction + ")";
                        string ThisExactRegion = RegionName + faction + localID.ToString();
                        outputString += "    " + "if \"" + levelName + "\" in AllLevelsListToCheckRegionCreation:" + Environment.NewLine;
                        outputString += "    " + "    " + ThisExactRegion + " = Region(\"" + CybranLocations[i] + " (" + faction + ")\", world.player, world.multiworld)" + Environment.NewLine;
                        outputString += "    " + "    " + "DictionaryOfRegions[\"" + CybranLocations[i] + " (" + faction + ")\"] = " + ThisExactRegion + Environment.NewLine;
                        outputString += "    " + "    " + "for i in range(0, world.options.locamount):" + Environment.NewLine;
                        outputString += "    " + "    " + "    index = i + 1" + Environment.NewLine;
                        outputString += "    " + "    " + "    lname = \"" + CybranLocations[i] + " (" + faction + ") \" + str(index)" + Environment.NewLine;
                        outputString += "    " + "    " + "    objID = \"" + objID + "\"" + Environment.NewLine;
                        outputString += "    " + "    " + "    if i < 10:" + Environment.NewLine;
                        outputString += "    " + "    " + "        objID = objID + \"0\"" + Environment.NewLine;
                        outputString += "    " + "    " + "    objID = objID + str(i)" + Environment.NewLine;
                        outputString += "    " + "    " + "    " + RegionName + faction + localID.ToString() + ".add_locations({lname: int(objID)}, SupComLocation)" + Environment.NewLine + Environment.NewLine;

                        localID += 1;
                    }
                }
            }

            outputString += Environment.NewLine;
            #endregion

            #region rules

            #region dictionary of level objectives for each level
            outputString += "    " + "TotalListOfTtotallyLevels = {}" + Environment.NewLine;
            for (int current_faction = 0; current_faction < 4; current_faction++)
            {
                string faction = "";
                switch (current_faction)
                {
                    case 0:
                        faction = " (UEF)";
                        break;
                    case 1:
                        faction = " (Cybran)";
                        break;
                    case 2:
                        faction = " (Aeon)";
                        break;
                    case 3:
                        faction = " (Sera)";
                        break;
                    default:
                        break;
                }
                for (int i = 0; i < FullListOfLevels.Count; i++)
                {
                    string LevelNameWithFaction = FullListOfLevels[i].name + faction;
                    outputString += "    " + "TempRegionlist = []" + Environment.NewLine;
                    for (int j = 0; j < FullListOfLevels[i].objectives.Count; j++)
                    {
                        
                        string Region = FullListOfLevels[i].objectives[j] + faction;
                        outputString += "    " + "TempRegionlist.append(\"" + Region + "\")" + Environment.NewLine;
                    }
                    outputString += "    " + "TotalListOfTtotallyLevels[\"" + LevelNameWithFaction + "\"] = TempRegionlist" + Environment.NewLine;
                }
            }
            outputString += Environment.NewLine;
            #endregion

            #region dictionary of rules for every objective
            outputString += "    " + "TheCompleteListOfRulesForEverySingleRegion = {}" + Environment.NewLine;
            for (int current_faction = 0; current_faction < 4; current_faction++)
            {
                string faction = "";
                switch (current_faction)
                {
                    case 0:
                        faction = " (UEF)";
                        break;
                    case 1:
                        faction = " (Cybran)";
                        break;
                    case 2:
                        faction = " (Aeon)";
                        break;
                    case 3:
                        faction = " (Sera)";
                        break;
                    default:
                        break;
                }
                for (int i = 0; i < FullListOfLevels.Count; i++)
                {
                    for (int j = 0; j < FullListOfLevels[i].objectives.Count; j++)
                    {
                        if (FullListOfLevels[i].Cybranrules[j] != "")
                        {
                            string Region = FullListOfLevels[i].objectives[j] + faction;
                            string ruleForCurrentRegion = "";
                            switch (current_faction)
                            {
                                case 0:
                                    ruleForCurrentRegion = FullListOfLevels[i].UEFrules[j];
                                    break;
                                case 1:
                                    ruleForCurrentRegion = FullListOfLevels[i].Cybranrules[j];
                                    break;
                                case 2:
                                    ruleForCurrentRegion = FullListOfLevels[i].Aeonrules[j];
                                    break;
                                case 3:
                                    ruleForCurrentRegion = FullListOfLevels[i].Serarules[j];
                                    break;
                                default:
                                    break;
                            }
                            outputString += "    " + "rule = " + ruleForCurrentRegion + Environment.NewLine;
                            outputString += "    " + "TheCompleteListOfRulesForEverySingleRegion[\"" + Region + "\"] = rule" + Environment.NewLine;
                        }
                    }
                }
            }
            outputString += Environment.NewLine;
            #endregion

            #endregion

            #region Add region to world (It is important to do that before next step)
            outputString += "    " + "ListOfUsedRegions = []" + Environment.NewLine;
            outputString += "    " + "for i in range(Width):" + Environment.NewLine;
            outputString += "    " + "    for j in range(Height):" + Environment.NewLine;
            outputString += "    " + "        for c in range(len(TotalListOfTtotallyLevels[THE_GRID[i][j]])):" + Environment.NewLine;
            outputString += "    " + "            ListOfUsedRegions.append(DictionaryOfRegions[TotalListOfTtotallyLevels[THE_GRID[i][j]][c]])" + Environment.NewLine;
            outputString += "    " + "world.multiworld.regions += ListOfUsedRegions" + Environment.NewLine + Environment.NewLine;
            #endregion

            #region connections

            #region connectionsInternal
            int indexOfEntrance = 0;
            for (int current_faction = 0; current_faction < 4; current_faction++)
            {
                string faction = "";
                switch (current_faction)
                {
                    case 0:
                        faction = "UEF";
                        break;
                    case 1:
                        faction = "Cybran";
                        break;
                    case 2:
                        faction = "Aeon";
                        break;
                    case 3:
                        faction = "Sera";
                        break;
                    default:
                        break;
                }
                for (int i = 0; i < FullListOfLevels.Count; i++)
                {
                    for (int j = 1; j < FullListOfLevels[i].objectives.Count; j++)
                    {
                        if (FullListOfLevels[i].Cybranrules[j] != "")
                        {
                            string RegionName = FullListOfLevels[i].name;
                            while (RegionName.Contains(" "))
                            {
                                RegionName = RegionName.Remove(RegionName.IndexOf(" "), 1);
                            }
                            string CurrentLevelName = FullListOfLevels[i].name + " (" + faction + ")";
                            outputString += "    " + "if \"" + CurrentLevelName + "\" in AllLevelsListToCheckRegionCreation:" + Environment.NewLine;
                            outputString += "    " + "    " + RegionName + faction + (j - 1).ToString() + ".connect(" +
                                RegionName + faction + j.ToString() + ", \"e" + indexOfEntrance.ToString() + "\", TheCompleteListOfRulesForEverySingleRegion[\"" +
                                FullListOfLevels[i].objectives[j] + " (" + faction + ")" + "\"])" + Environment.NewLine;
                            indexOfEntrance++;
                        }
                        else
                        {
                            string RegionName = FullListOfLevels[i].name;
                            while (RegionName.Contains(" "))
                            {
                                RegionName = RegionName.Remove(RegionName.IndexOf(" "), 1);
                            }

                            string CurrentLevelName = FullListOfLevels[i].name + " (" + faction + ")";
                            outputString += "    " + "if \"" + CurrentLevelName + "\" in AllLevelsListToCheckRegionCreation:" + Environment.NewLine;
                            outputString += "    " + "    " + RegionName + faction + (j - 1).ToString() + ".connect(" +
                                RegionName + faction + j.ToString() + ", \"e" + indexOfEntrance.ToString() + "\")" + Environment.NewLine;
                            indexOfEntrance++;
                        }
                    }
                }
            }
            outputString += Environment.NewLine;
            #endregion

            #region connectionsExternal
            outputString += "    " + "indexOfEntrance = " + indexOfEntrance + Environment.NewLine;
            outputString += "    " + "for i in range(Width):" + Environment.NewLine;
            outputString += "    " + "    for j in range(Height):" + Environment.NewLine;
            outputString += "    " + "        CheckFilled = bool(not(i == 0 and j == 0))" + Environment.NewLine;
            outputString += "    " + "        if CheckFilled:" + Environment.NewLine;
            // i - 1
            outputString += "    " + "            if i > 0:" + Environment.NewLine;
            outputString += "    " + "                regionLast = world.get_region(TotalListOfTtotallyLevels[THE_GRID[i - 1][j]][len(TotalListOfTtotallyLevels[THE_GRID[i - 1][j]]) - 1])" + Environment.NewLine;
            outputString += "    " + "                regionFirst = world.get_region(TotalListOfTtotallyLevels[THE_GRID[i][j]][0])" + Environment.NewLine;
            outputString += "    " + "                tempSTR = \"e\" + str(indexOfEntrance)" + Environment.NewLine;
            outputString += "    " + "                if not THE_GRID[i][j] in levelsTier1FOREVER:" + Environment.NewLine;
            outputString += "    " + "    " + "                regionLast.connect(regionFirst, tempSTR, TheCompleteListOfRulesForEverySingleRegion[TotalListOfTtotallyLevels[THE_GRID[i][j]][0]])" + Environment.NewLine;
            outputString += "    " + "                else:" + Environment.NewLine;
            outputString += "    " + "    " + "                regionLast.connect(regionFirst, tempSTR)" + Environment.NewLine;
            outputString += "    " + "                indexOfEntrance = 1 + indexOfEntrance" + Environment.NewLine;
            // j - 1
            outputString += "    " + "            if j > 0:" + Environment.NewLine;
            outputString += "    " + "                regionLast = world.get_region(TotalListOfTtotallyLevels[THE_GRID[i][j - 1]][len(TotalListOfTtotallyLevels[THE_GRID[i][j - 1]]) - 1])" + Environment.NewLine;
            outputString += "    " + "                regionFirst = world.get_region(TotalListOfTtotallyLevels[THE_GRID[i][j]][0])" +  Environment.NewLine;
            outputString += "    " + "                tempSTR = \"e\" + str(indexOfEntrance)" + Environment.NewLine;
            outputString += "    " + "                if not THE_GRID[i][j] in levelsTier1FOREVER:" + Environment.NewLine;
            outputString += "    " + "    " + "                regionLast.connect(regionFirst, tempSTR, TheCompleteListOfRulesForEverySingleRegion[TotalListOfTtotallyLevels[THE_GRID[i][j]][0]])" + Environment.NewLine;
            outputString += "    " + "                else:" + Environment.NewLine;
            outputString += "    " + "    " + "                regionLast.connect(regionFirst, tempSTR)" + Environment.NewLine;
            outputString += "    " + "                indexOfEntrance = 1 + indexOfEntrance" + Environment.NewLine;
            // i + 1
            outputString += "    " + "            if i < Width - 1:" + Environment.NewLine;
            outputString += "    " + "                regionLast = world.get_region(TotalListOfTtotallyLevels[THE_GRID[i + 1][j]][len(TotalListOfTtotallyLevels[THE_GRID[i + 1][j]]) - 1])" + Environment.NewLine;
            outputString += "    " + "                regionFirst = world.get_region(TotalListOfTtotallyLevels[THE_GRID[i][j]][0])" + Environment.NewLine;
            outputString += "    " + "                tempSTR = \"e\" + str(indexOfEntrance)" + Environment.NewLine;
            outputString += "    " + "                if not THE_GRID[i][j] in levelsTier1FOREVER:" + Environment.NewLine;
            outputString += "    " + "    " + "                regionLast.connect(regionFirst, tempSTR, TheCompleteListOfRulesForEverySingleRegion[TotalListOfTtotallyLevels[THE_GRID[i][j]][0]])" + Environment.NewLine;
            outputString += "    " + "                else:" + Environment.NewLine;
            outputString += "    " + "    " + "                regionLast.connect(regionFirst, tempSTR)" + Environment.NewLine;
            outputString += "    " + "                indexOfEntrance = 1 + indexOfEntrance" + Environment.NewLine;
            // j + 1
            outputString += "    " + "            if j < Height - 1:" + Environment.NewLine;
            outputString += "    " + "                regionLast = world.get_region(TotalListOfTtotallyLevels[THE_GRID[i][j + 1]][len(TotalListOfTtotallyLevels[THE_GRID[i][j + 1]]) - 1])" + Environment.NewLine;
            outputString += "    " + "                regionFirst = world.get_region(TotalListOfTtotallyLevels[THE_GRID[i][j]][0])" + Environment.NewLine;
            outputString += "    " + "                tempSTR = \"e\" + str(indexOfEntrance)" + Environment.NewLine;
            outputString += "    " + "                if not THE_GRID[i][j] in levelsTier1FOREVER:" + Environment.NewLine;
            outputString += "    " + "    " + "                regionLast.connect(regionFirst, tempSTR, TheCompleteListOfRulesForEverySingleRegion[TotalListOfTtotallyLevels[THE_GRID[i][j]][0]])" + Environment.NewLine;
            outputString += "    " + "                else:" + Environment.NewLine;
            outputString += "    " + "    " + "                regionLast.connect(regionFirst, tempSTR)" + Environment.NewLine;
            outputString += "    " + "                indexOfEntrance = 1 + indexOfEntrance" + Environment.NewLine;
            outputString += Environment.NewLine;
            #endregion

            #endregion

            #region Final region

            #region included factions
            //Check which factions we actually got randomised
            outputString += "    " + "listOfFactionsThatActuallyExist = []" + Environment.NewLine;
            outputString += "    " + "for i in range(Width):" + Environment.NewLine;
            outputString += "    " + "    for j in range(Height):" + Environment.NewLine;
            outputString += "    " + "        if (\"UEF\" in THE_GRID[i][j]) and not \"uef\" in listOfFactionsThatActuallyExist:" + Environment.NewLine;
            outputString += "    " + "            listOfFactionsThatActuallyExist.append(\"uef\")" + Environment.NewLine;
            outputString += "    " + "        if \"Cybran\" in THE_GRID[i][j] and not \"cybran\" in listOfFactionsThatActuallyExist:" + Environment.NewLine;
            outputString += "    " + "            listOfFactionsThatActuallyExist.append(\"cybran\")" + Environment.NewLine;
            outputString += "    " + "        if \"Aeon\" in THE_GRID[i][j] and not \"aeon\" in listOfFactionsThatActuallyExist:" + Environment.NewLine;
            outputString += "    " + "            listOfFactionsThatActuallyExist.append(\"aeon\")" + Environment.NewLine;
            outputString += "    " + "        if \"Sera\" in THE_GRID[i][j] and not \"sera\" in listOfFactionsThatActuallyExist:" + Environment.NewLine;
            outputString += "    " + "            listOfFactionsThatActuallyExist.append(\"sera\")" + Environment.NewLine + Environment.NewLine;
            #endregion

            #region progression items

            #region make a list of units needed on each possible level
            outputString += "    " + "PossibleItemList = []" + Environment.NewLine;
            for (int factionIndex = 0; factionIndex < 4; factionIndex++)
            {
                string faction = "";
                switch (factionIndex)
                {
                    case 0:
                        faction = "UEF";
                        break;
                    case 1:
                        faction = "Cybran";
                        break;
                    case 2:
                        faction = "Aeon";
                        break;
                    case 3:
                        faction = "Sera";
                        break;
                    default:
                        break;
                }
                for (int i = 0; i < levelNAMES.Count; i++)
                {
                    for (int j = 0; j < AllRequeredRules.Count; j++)
                    {
                        if (AllRequeredRules[j].Level == levelNAMES[i] + " (" + faction + ")")
                        {
                            for (int idk_another_index = i; idk_another_index < levelNAMES.Count; idk_another_index++)
                            {
                                string curLevName = levelNAMES[idk_another_index];
                                while (curLevName.Contains(" "))
                                {
                                    curLevName = curLevName.Remove(curLevName.IndexOf(" "), 1);
                                }
                                outputString += "    " + "if \"" + levelNAMES[idk_another_index] + " (" + faction + ")\" in AllLevelsListToCheckRegionCreation:" + Environment.NewLine;
                                outputString += "    " + "    " + curLevName + faction + "PossibleUnitList = [";
                                for (int ruleIndex = 0; ruleIndex < AllRequeredRules[j].Sets.Count; ruleIndex++)
                                {
                                    outputString += AllRequeredRules[j].Sets[ruleIndex];
                                    if (ruleIndex != AllRequeredRules[j].Sets.Count - 1)
                                    {
                                        outputString += ", ";
                                    }
                                }
                                outputString += "]" + Environment.NewLine;
                                outputString += "    " + "    " + "temp = world.random.randrange(0, len(" + curLevName + faction + "PossibleUnitList))" + Environment.NewLine;
                                outputString += "    " + "    " + "if not " + curLevName + faction + "PossibleUnitList[temp] in PossibleItemList:" + Environment.NewLine;
                                outputString += "    " + "    " + "    " + "PossibleItemList.append(" + curLevName + faction + "PossibleUnitList[temp])" + Environment.NewLine + Environment.NewLine;
                            }
                        }
                    }
                }
            }
            outputString += "    " + "print(PossibleItemList)" + Environment.NewLine + Environment.NewLine;
            #endregion

            #endregion

            #region useful items
            //make a list of ALL items that should be included based on factions we got
            outputString += "    " + "number_of_unfilled_locations = len(ListOfUsedRegions) * world.options.locamount - len(PossibleItemList)" + Environment.NewLine;
            outputString += "    " + "ItemsFromFactions = []" + Environment.NewLine;
            outputString += "    " + "if \"uef\" in listOfFactionsThatActuallyExist:" + Environment.NewLine;
            outputString += "    " + "    ItemsFromFactions.extend(uef_items)" + Environment.NewLine;
            outputString += "    " + "if \"cybran\" in listOfFactionsThatActuallyExist:" + Environment.NewLine;
            outputString += "    " + "    ItemsFromFactions.extend(cybran_items)" + Environment.NewLine;
            outputString += "    " + "if \"aeon\" in listOfFactionsThatActuallyExist:" + Environment.NewLine;
            outputString += "    " + "    ItemsFromFactions.extend(aeon_items)" + Environment.NewLine;
            outputString += "    " + "if \"sera\" in listOfFactionsThatActuallyExist:" + Environment.NewLine;
            outputString += "    " + "    ItemsFromFactions.extend(sera_items)" + Environment.NewLine + Environment.NewLine;
            outputString += "    " + "for i in range(len(PossibleItemList)):" + Environment.NewLine;
            outputString += "    " + "    " + "if PossibleItemList[i] in ItemsFromFactions:" + Environment.NewLine;
            outputString += "    " + "    " + "    " + "ItemsFromFactions.remove(PossibleItemList[i])" + Environment.NewLine + Environment.NewLine;

            outputString += "    " + "if len(ItemsFromFactions) >= number_of_unfilled_locations:" + Environment.NewLine;
            outputString += "    " + "    PossibleItemList.extend(world.random.sample(ItemsFromFactions, number_of_unfilled_locations))" + Environment.NewLine;
            outputString += "    " + "else:" + Environment.NewLine;
            outputString += "    " + "    PossibleItemList.extend(ItemsFromFactions)" + Environment.NewLine;
            outputString += "    " + "    for i in range(number_of_unfilled_locations - len(ItemsFromFactions)):" + Environment.NewLine;
            #endregion

            #region filler items
            //THIS IS THE PLACE THAT ADDS FILLER IF I AM GOING TO IMPLEMENT IT
            outputString += "    " + "        PossibleItemList.append(\"Nothing\")" + Environment.NewLine + Environment.NewLine;
            outputString += "    " + "itempoolREAL = []" + Environment.NewLine;
            outputString += "    " + "for i in range(len(PossibleItemList)):" + Environment.NewLine ;
            outputString += "    " + "    " + "itempoolREAL.append(world.create_item(PossibleItemList[i]))" + Environment.NewLine + Environment.NewLine;
            outputString += "    " + "world.multiworld.itempool += itempoolREAL" + Environment.NewLine + Environment.NewLine;
            outputString += "    " + "world.origin_region_name = TotalListOfTtotallyLevels[THE_GRID[0][0]][0]" + Environment.NewLine + Environment.NewLine;

            outputString += "    " + "print(len(ListOfUsedRegions) * world.options.locamount)" + Environment.NewLine;
            outputString += "    " + "print(len(PossibleItemList))" + Environment.NewLine + Environment.NewLine;

            #endregion

            #region set goal to make balls
            outputString += "    " + "final_boss_room = world.get_region(TotalListOfTtotallyLevels[THE_GRID[Width - 1][Height - 1]][len(TotalListOfTtotallyLevels[THE_GRID[Width - 1][Height - 1]]) - 1])" + Environment.NewLine;
            outputString += "    " + "final_boss_room.add_event(\"Final Boss Defeated\", \"Victory\", location_type=SupComLocation, item_type=SupComItem)" + Environment.NewLine;
            outputString += "    " + "world.set_completion_rule(Has(\"Victory\"))" + Environment.NewLine;
            #endregion

            #region some shit needed to make all work
            outputString += "def create_item_with_correct_classification(world: SupComWorld, name: str) -> SupComItem:" + Environment.NewLine;
            outputString += "    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]" + Environment.NewLine;
            outputString += "    return SupComItem(name, classification, ITEM_NAME_TO_ID[name], world.player)" + Environment.NewLine;
            #endregion

            #endregion

            #endregion

            File.WriteAllText("data.py", outputString);
        }
    }
    public class SCLevel
    {
        public string name;
        public List<string> objectives;
        public List<string> UEFrules;
        public List<string> Cybranrules;
        public List<string> Aeonrules;
        public List<string> Serarules;
        public int tier;
        public int default_faction;
        public SCLevel(string NAME, List<string> OBJECTIVES, List<string> URules, List<string> CRules, List<string> ARules, List<string> SRules, int TIER, int DEFAULT_FACTION)
        {
            name = NAME;
            objectives = OBJECTIVES;
            tier = TIER;
            default_faction = DEFAULT_FACTION;
            UEFrules = URules;
            Cybranrules = CRules;
            Aeonrules = ARules;
            Serarules = SRules;
        }
    }
    public class SCItem
    {
        public string name;
        public string ReqLevel;
        public int LevelPos;
        public SCItem(string NAME, string LEV, int POS)
        {
            name = NAME;
            ReqLevel = LEV;
            LevelPos = POS;
        }
    }
    public class SCRule
    {
        public string Level;
        public List<string> Sets;
        public SCRule(string NAME, List<string> RUL)
        {
            Level = NAME;
            Sets = RUL;
        }
    }
}