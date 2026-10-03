using Archipelago.MultiClient.Net;
using Archipelago.MultiClient.Net.Enums;
using Archipelago.MultiClient.Net.MessageLog.Messages;
using Archipelago.MultiClient.Net.Models;
using ColorPicker;
using ColorPicker.Models;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using OfficeOpenXml;
using System;
using System.Diagnostics;
using System.IO;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Controls.Primitives;
using System.Windows.Media;
using System.Windows.Media.Imaging;
//using System.Windows.Shapes;
using System.Windows.Threading;
using Color = System.Windows.Media.Color;
//using static System.Net.WebRequestMethods;
//using Path = System.IO.Path;

namespace SupComClient
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        int GridHeight;
        int GridWidth;
        Dictionary<Button, LevelData> BDATA = new Dictionary<Button, LevelData>();
        Dictionary<(string, int), Button> ADATA = new Dictionary<(string, int), Button>();
        List<LevelData> LDATA = new List<LevelData>();

        bool GameActive = false;
        Dictionary<string, object> daT;
        DispatcherTimer updTimer = new DispatcherTimer();

        Dictionary<(string, int), (string, int)> finalRegiontoLevelName = new Dictionary<(string, int), (string, int)>();
        Dictionary<string, string> LevelToID = new Dictionary<string, string>();
        Dictionary<(string, int), long> LocationLogToId = new Dictionary<(string, int), long>();
        Dictionary<long, (string, int)> IdToLocation = new Dictionary<long, (string, int)>();
        Dictionary<string, string> ACU_Upgrades = new Dictionary<string, string>();
        List<string> Unlocked_Upgrades = new List<string>();
        Dictionary<string, string> Units = new Dictionary<string, string>();
        List<string> Unlocked_Units = new List<string>();

        ArchipelagoSession TheSession;
        Process proc;
        bool initialised = false;
        string CurrentMap = "";
        string binFolder = "X:\\Games\\IG\\FAF Client\\Data";
        string mapmodFolder = "X:\\Games\\IG\\FAF Client\\MapMods";
        string logfile = "C:\\LOG\\ap.log";
        //string FAinstallFolder = "X:\\Programs\\Steam\\steamapps\\common\\Supreme Commander Forged Alliance\\";
        string SettingsSaved = "Settings.json";
        string mapname = "SCCA_R01";
        int faction = 1;
        public MainWindow()
        {
            InitializeComponent();
            CheckDefaultOptions();
            ReadExcel();
            DeleteOldShit();
            updTimer.Interval = new TimeSpan(0, 0, 3);
            updTimer.Tick += UpdTimer_Tick;
            initialised = true;
        }

        private void UpdTimer_Tick(object? sender, EventArgs e)
        {
            if (TheSession.Socket.Connected)
            {
                #region receive

                #region receive items
                MessageBox.Items.Refresh();
                List<string> Recived = new List<string>();
                for (int i = 0; i < TheSession.Items.AllItemsReceived.Count; i++)
                {
                    Recived.Add(TheSession.Items.AllItemsReceived[i].ItemName);
                }
                while (Recived.Count > 0)
                {
                    if (Units.ContainsKey(Recived[0]))
                    {
                        if (!Unlocked_Units.Contains(Recived[0]))
                        {
                            Unlocked_Units.Add(Recived[0]);
                        }
                        Recived.RemoveAt(0);
                    }
                    else if (ACU_Upgrades.ContainsKey(Recived[0]))
                    {
                        if (!Unlocked_Upgrades.Contains(Recived[0]))
                        {
                            Unlocked_Upgrades.Add(Recived[0]);
                        }
                        Recived.RemoveAt(0);
                    }
                    else
                    {
                        Recived.RemoveAt(0);
                    }
                }
                #endregion

                #region receive checked locations and mark levels
                //Get list of checked locations
                List<long> locationsChecked = new List<long>();
                for (int i = 0; i < TheSession.Locations.AllLocationsChecked.Count; i++)
                {
                    long tempLONG = TheSession.Locations.AllLocationsChecked[i];
                    string tempSTRING = tempLONG.ToString();
                    tempSTRING = tempSTRING.Remove(tempSTRING.Length - 2);
                    locationsChecked.Add(long.Parse(tempSTRING));
                }
                //Get list of completed levels
                List<(string, int)> LevelPair = new List<(string, int)>();
                for (int i = 0; i < locationsChecked.Count; i++)
                {
                    (string, int) LocationPair = IdToLocation[locationsChecked[i]];
                    if (finalRegiontoLevelName.ContainsKey(LocationPair))
                    {
                        LevelPair.Add(finalRegiontoLevelName[LocationPair]);
                    }
                }
                //Mark levels as completed in BDATA
                for (int i = 0; i < LevelPair.Count; i++)
                {
                    BDATA[ADATA[LevelPair[i]]].bSTATE = ButtonState.done;
                }
                //Iterate on BDATA to mark levels as unfinished and change font color
                foreach (LevelData item in BDATA.Values)
                {
                    if (item.bSTATE == ButtonState.locked)
                    {
                        (int, int) Pos = (item.PositionHorisontal, item.PositionVertical);
                        foreach (LevelData item2 in BDATA.Values)
                        {
                            if (item2.bSTATE == ButtonState.done)
                            {
                                (int, int) Pos2 = (item2.PositionHorisontal, item2.PositionVertical);
                                if (Pos != Pos2 && Pos != (0, 0))
                                {
                                    bool sosed1 = (item.PositionHorisontal != 0) && (item.PositionVertical == item2.PositionVertical) && (item.PositionHorisontal - 1 == item2.PositionHorisontal);
                                    bool sosed2 = (item.PositionVertical != 0) && (item.PositionHorisontal == item2.PositionHorisontal) && (item.PositionVertical - 1 == item2.PositionVertical);
                                    bool sosed3 = (item.PositionHorisontal != GridWidth - 1) && (item.PositionVertical == item2.PositionVertical) && (item.PositionHorisontal + 1 == item2.PositionHorisontal);
                                    bool sosed4 = (item.PositionVertical != GridHeight - 1) && (item.PositionHorisontal == item2.PositionHorisontal) && (item.PositionVertical + 1 == item2.PositionVertical);
                                    if (sosed1 || sosed2 || sosed3 || sosed4)
                                    {
                                        item.bSTATE = ButtonState.unfinished;
                                    }
                                }
                            }
                            
                        }
                    }
                    if (item.bSTATE == ButtonState.done)
                    {
                        item.ButtonText.Foreground = new SolidColorBrush(Color.FromRgb(80, 255, 0));
                        if (item.PositionHorisontal == GridWidth - 1 && item.PositionVertical == GridHeight - 1)
                        {
                            TheSession.SetGoalAchieved();
                        }
                    }
                    else if (item.bSTATE == ButtonState.unfinished)
                    {
                        item.ButtonText.Foreground = new SolidColorBrush(Color.FromRgb(113, 239, 255));
                    }
                    else
                    {
                        item.ButtonText.Foreground = new SolidColorBrush(Color.FromRgb(56, 119, 127));
                    }
                }
                #endregion

                #region receive hints and display them
                HintBox.Items.Clear();
                List<Hint> THE_hints = new List<Hint>();
                THE_hints.AddRange(TheSession.Hints.GetHints());
                for (int i = 0; i < THE_hints.Count(); i++)
                {
                    string Wants = TheSession.Players.GetPlayerName(THE_hints[i].ReceivingPlayer);
                    string Has = TheSession.Players.GetPlayerName(THE_hints[i].FindingPlayer);
                    string Item = TheSession.Items.GetItemName(THE_hints[i].ItemId);
                    string Place = TheSession.Locations.GetLocationNameFromId(THE_hints[i].LocationId);
                    string Hint = "Player \"" + Wants + "\" desires to get item \"" + Item + "\" from Player \"" + Has + "\" located at \"" + Place + "\"";
                    HintBox.Items.Add(Hint);
                }
                Points.Content = TheSession.RoomState.HintPoints;
                Costs.Content = TheSession.RoomState.HintCost;
                #endregion

                #endregion

                #region send
                if (GameActive)
                {
                    if (File.Exists(logfile))
                    {
                        #region send locations
                        FileStream logFileStream = new FileStream(logfile, FileMode.Open, FileAccess.Read, FileShare.ReadWrite);
                        StreamReader logFileReader = new StreamReader(logFileStream);
                        string Log = logFileReader.ReadToEnd();
                        List<string> Locations = new List<string>();
                        while (Log.IndexOf("APLOG-") != -1)
                        {
                            int a = Log.IndexOf("APLOG-");
                            Log = Log.Remove(0, Log.IndexOf("APLOG-") + 6);
                            Locations.Add(Log.Substring(0, Log.IndexOf(Environment.NewLine)));
                        }
                        if (Locations.Count > 0)
                        {
                            long location_multiplier = (long)daT["locamount"];
                            long[] locations_to_send = new long[Locations.Count * location_multiplier];
                            List<long> locations_list = new List<long>();
                            for (int i = 0; i < Locations.Count; i++)
                            {
                                for (int j = 0; j < location_multiplier; j++)
                                {
                                    string curLocST = LocationLogToId[(Locations[i], faction)].ToString();
                                    if (j < 10)
                                    {
                                        curLocST += "0";
                                    }
                                    curLocST += j.ToString();
                                    long curLoc = long.Parse(curLocST);
                                    locations_list.Add(curLoc);
                                }
                            }
                            for (int i = 0; i < locations_list.Count; i++)
                            {
                                locations_to_send[i] = locations_list[i];
                            }
                            TheSession.Locations.CompleteLocationChecks(locations_to_send);
                        }
                        #endregion

                        #region send unlocked units
                        string ThisMustBeUpdated = CurrentMap + "\\UnlockRestriction.Lua";
                        string ThisIsUpdate = "local ScenarioFramework = import('/lua/scenarioframework.lua')" + Environment.NewLine + "Unlock = {}" + Environment.NewLine;
                        for (int i = 0; i < Unlocked_Units.Count; i++)
                        {
                            ThisIsUpdate += "Unlock[" + (i + 1).ToString() + "] = categories." + Units[Unlocked_Units[i]] + Environment.NewLine;
                        }
                        ThisIsUpdate += "Elements = " + Unlocked_Units.Count + Environment.NewLine;
                        #endregion

                        #region send uef acu upgrades
                        ThisIsUpdate += "function EnchanceUEF()" + Environment.NewLine + "ScenarioFramework.RestrictEnhancements({";
                        int its = 0;
                        foreach (var item in ACU_Upgrades)
                        {
                            if (item.Key.Contains("UEF") && !Unlocked_Upgrades.Contains(item.Key))
                            {
                                its++;
                                ThisIsUpdate += "'" + item.Value + "'," + Environment.NewLine;
                            }
                        }
                        if (its > 0)
                        {
                            ThisIsUpdate = ThisIsUpdate.Remove(ThisIsUpdate.LastIndexOf(","), 1);
                        }
                        ThisIsUpdate += "})" + Environment.NewLine + "end" + Environment.NewLine;
                        #endregion

                        #region send cybran acu upgrades
                        its = 0;
                        ThisIsUpdate += "function EnchanceCYB()" + Environment.NewLine + "ScenarioFramework.RestrictEnhancements({";
                        foreach (var item in ACU_Upgrades)
                        {
                            if (item.Key.Contains("Cybran") && !Unlocked_Upgrades.Contains(item.Key))
                            {
                                its++;
                                ThisIsUpdate += "'" + item.Value + "'," + Environment.NewLine;
                            }
                        }
                        if (its > 0)
                        {
                            ThisIsUpdate = ThisIsUpdate.Remove(ThisIsUpdate.LastIndexOf(","), 1);
                        }
                        ThisIsUpdate += "})" + Environment.NewLine + "end" + Environment.NewLine;
                        #endregion

                        #region send aeon acu upgrades
                        its = 0;
                        ThisIsUpdate += "function EnchanceAEON()" + Environment.NewLine + "ScenarioFramework.RestrictEnhancements({";
                        foreach (var item in ACU_Upgrades)
                        {
                            if (item.Key.Contains("Aeon") && !Unlocked_Upgrades.Contains(item.Key))
                            {
                                its++;
                                ThisIsUpdate += "'" + item.Value + "'," + Environment.NewLine;
                            }
                        }
                        if (its > 0)
                        {
                            ThisIsUpdate = ThisIsUpdate.Remove(ThisIsUpdate.LastIndexOf(","), 1);
                        }
                        ThisIsUpdate += "})" + Environment.NewLine + "end" + Environment.NewLine;
                        #endregion

                        #region send sera acu upgrades
                        its = 0;
                        ThisIsUpdate += "function EnchanceSERA()" + Environment.NewLine + "ScenarioFramework.RestrictEnhancements({";
                        foreach (var item in ACU_Upgrades)
                        {
                            if (item.Key.Contains("Sera") && !Unlocked_Upgrades.Contains(item.Key))
                            {
                                its++;
                                ThisIsUpdate += "'" + item.Value + "'," + Environment.NewLine;
                            }
                        }
                        if (its > 0)
                        {
                            ThisIsUpdate = ThisIsUpdate.Remove(ThisIsUpdate.LastIndexOf(","), 1);
                        }
                        ThisIsUpdate += "})" + Environment.NewLine + "end" + Environment.NewLine;
                        File.WriteAllText(ThisMustBeUpdated, ThisIsUpdate);
                        #endregion
                    }
                }
                #endregion
            }
        }

        void OpenMission(string LevelName, string PlayerName, int faction, int difficulty)
        {
            #region copy
            mapmodFolder = SettingMapFolder.Text; 
            binFolder = SettingDataFolder.Text;
            Directory.CreateDirectory("C:\\LOG");

            File.Copy("init_coop_spec.lua", binFolder + "\\bin\\" + "init_coop_spec.lua");
            string source = "Maps\\" + mapname + "\\";
            string newLocation = mapmodFolder + "\\maps\\" + mapname + "\\";
            Copy(source, newLocation);
            CurrentMap = newLocation;
            #endregion

            #region properties
            string LuaInput = mapmodFolder + "\\maps\\" + mapname + "\\Variables.lua";
            string InputData = "Red = " + ColorPick.SelectedColor.R + Environment.NewLine + "Green = " + ColorPick.SelectedColor.G + Environment.NewLine + "Blue = " + ColorPick.SelectedColor.B + Environment.NewLine + "Name = '" + PlayerName + "'" + Environment.NewLine + "Faction = " + faction + Environment.NewLine;
            File.WriteAllText(LuaInput, InputData);
            #endregion

            #region launch
            string filename = binFolder + "\\bin\\ForgedAlliance.exe";
            string cparams = "/init init_coop_spec.lua /diff " + difficulty.ToString() + " /EnableDiskWatch /log " + logfile + " /map " + mapname;
            proc = new Process();
            proc.StartInfo.FileName = filename;
            proc.StartInfo.Arguments = cparams;
            proc.EnableRaisingEvents = true;
            proc.Exited += new EventHandler(SupComExit);
            proc.Start(); 
            GameActive = true;
            #endregion
        }
        void ReadExcel()
        {
            ExcelPackage.License.SetNonCommercialPersonal("l.txt");
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
            ExcelWorksheet LVLs = Data.Workbook.Worksheets[Levels];

            //Read uef items
            for (int i = 1; i < 100; i++)
            {
                if (UEFIt.Cells[i, 3].GetCellValue<string>() != null)
                {
                    Units.Add(UEFIt.Cells[i, 3].GetCellValue<string>(), UEFIt.Cells[i, 4].GetCellValue<string>());
                }
            }
            //Read uef upgrades
            for (int i = 1; i < 100; i++)
            {
                if (UEFIt.Cells[i, 6].GetCellValue<string>() != null)
                {
                    ACU_Upgrades.Add(UEFIt.Cells[i, 6].GetCellValue<string>(), UEFIt.Cells[i, 7].GetCellValue<string>());
                }
            }
            //Read cybran items
            for (int i = 1; i < 100; i++)
            {
                if (CybIt.Cells[i, 3].GetCellValue<string>() != null)
                {
                    Units.Add(CybIt.Cells[i, 3].GetCellValue<string>(), CybIt.Cells[i, 4].GetCellValue<string>());
                }
            }
            //Read cybran upgrades
            for (int i = 1; i < 100; i++)
            {
                if (CybIt.Cells[i, 6].GetCellValue<string>() != null)
                {
                    ACU_Upgrades.Add(CybIt.Cells[i, 6].GetCellValue<string>(), CybIt.Cells[i, 7].GetCellValue<string>());
                }
            }
            //Read aeon items
            for (int i = 1; i < 100; i++)
            {
                if (AeonIt.Cells[i, 3].GetCellValue<string>() != null)
                {
                    Units.Add(AeonIt.Cells[i, 3].GetCellValue<string>(), AeonIt.Cells[i, 4].GetCellValue<string>());
                }
            }
            //Read aeon upgrades
            for (int i = 1; i < 100; i++)
            {
                if (AeonIt.Cells[i, 6].GetCellValue<string>() != null)
                {
                    ACU_Upgrades.Add(AeonIt.Cells[i, 6].GetCellValue<string>(), AeonIt.Cells[i, 7].GetCellValue<string>());
                }
            }
            //Read sera items
            for (int i = 1; i < 100; i++)
            {
                if (SeraIt.Cells[i, 3].GetCellValue<string>() != null)
                {
                    Units.Add(SeraIt.Cells[i, 3].GetCellValue<string>(), SeraIt.Cells[i, 4].GetCellValue<string>());
                }
            }
            //Read sera upgrades
            for (int i = 1; i < 100; i++)
            {
                if (SeraIt.Cells[i, 6].GetCellValue<string>() != null)
                {
                    ACU_Upgrades.Add(SeraIt.Cells[i, 6].GetCellValue<string>(), SeraIt.Cells[i, 7].GetCellValue<string>());
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
            //Read levels
            for (int i = 2; i < 100; i++)
            {
                if (LVLs.Cells[i, 1].GetCellValue<string>() != null)
                {
                    LevelToID.Add(LVLs.Cells[i, 1].GetCellValue<string>(), LVLs.Cells[i, 2].GetCellValue<string>());
                }
            }
            //Write cybran locations
            for (int facID = 0; facID < 4; facID++)
            {
                int mission = 1;
                int localID = 0;
                for (int i = 0; i < CybranLocations.Count; i++)
                {
                    if (CybranLocations[i] == "-")
                    {
                        mission += 1;
                        localID = 0;
                    }
                    else
                    {
                        if (i == CybranLocations.Count - 1 || CybranLocations[i + 1] == "-")
                        {
                            string location = CybranLocations[i];
                            string LevelName = CybranLocations[i].Substring(0, CybranLocations[i].IndexOf(":"));
                            finalRegiontoLevelName.Add((location, facID), (LevelName, facID));
                        }
                        string id = "2" + (facID + 1).ToString();
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
                        LocationLogToId.Add((CybLoc.Cells[i + 2, 2].GetCellValue<string>(), facID), int.Parse(id));
                        IdToLocation.Add(int.Parse(id), (CybranLocations[i], facID));
                        localID += 1;
                    }

                }
            }
            
        }
        private void OpenM1(object sender, RoutedEventArgs e)
        {
            DeleteOldShit();
            if (TheSession.Socket.Connected)
            {
                Button abut = (Button)sender;
                if (!(BDATA[abut].bSTATE == ButtonState.locked))
                {
                    mapname = BDATA[abut].LevelID;
                    faction = BDATA[abut].faction;
                    OpenMission(mapname, TheSession.Players.ActivePlayer.Name, faction, int.Parse(daT["difficulty"].ToString()));
                }
            }
        }
        void CheckDefaultOptions()
        {
            if (File.Exists(SettingsSaved))
            {
                string jsonSt = File.ReadAllText(SettingsSaved);
                SettingsData setData = JsonConvert.DeserializeObject<SettingsData>(jsonSt);
                ColorPick.SelectedColor = setData.PlayerColor;
                ServerName.Text = setData.ServerName;
                ServerNumbers.Text = setData.ServerNumbers;
                SlotName.Text = setData.PlayerName;
                ServerPassword.Text = setData.password;
                SettingDataFolder.Text = setData.DataFolder;
                SettingMapFolder.Text = setData.MapModFolder;
            }
            else
            {
                Color a = new Color();
                a.R = 255;
                a.G = 255;
                a.B = 0;
                a.A = 255;
                SettingsData setData = new SettingsData();
                setData.PlayerColor = a;
                setData.ServerName = "archipelago.gg";
                setData.ServerNumbers = "38281";
                setData.PlayerName = "SupCom";
                setData.password = "";
                setData.DataFolder = "X:\\Games\\IG\\FAF Client\\Data";
                setData.MapModFolder = "X:\\Games\\IG\\FAF Client\\MapMods";
                string jsonSt = JsonConvert.SerializeObject(setData);
                File.WriteAllText(SettingsSaved, jsonSt);
                ColorPick.SelectedColor = a;
                ServerName.Text = setData.ServerName;
                ServerNumbers.Text = setData.ServerNumbers;
                SlotName.Text = setData.PlayerName;
                ServerPassword.Text = setData.password;
                SettingDataFolder.Text = setData.DataFolder;
                SettingMapFolder.Text = setData.MapModFolder;
            }
        }
        private void SupComExit(object sender, System.EventArgs e)
        {
            //Delete init
            File.Delete(binFolder + "\\bin\\" + "init_coop_spec.lua");
            //Delete map
            string source = mapmodFolder + "\\maps\\" + mapname + "\\";
            DirectoryInfo dir = new DirectoryInfo(source);
            dir.Delete(true);
            GameActive = false;
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
            SaveSettings();
        }
        void SaveSettings()
        {
            if (initialised)
            {
                SettingsData setData = new SettingsData();
                setData.PlayerColor = ColorPick.SelectedColor;
                setData.ServerName = ServerName.Text;
                setData.ServerNumbers = ServerNumbers.Text;
                setData.PlayerName = SlotName.Text;
                setData.password = ServerPassword.Text;
                setData.DataFolder = SettingDataFolder.Text;
                setData.MapModFolder = SettingMapFolder.Text;
                string jsonSt = JsonConvert.SerializeObject(setData);
                File.WriteAllText(SettingsSaved, jsonSt);
            }
        }
        private void SaveChangedColor(object sender, TextChangedEventArgs e)
        {
            SaveSettings();
        }
        private void Connect(object sender, RoutedEventArgs e)
        {
            DeleteOldShit();
            LDATA.Clear();
            TheSession = ArchipelagoSessionFactory.CreateSession(ServerName.Text, int.Parse(ServerNumbers.Text));
            string pWord = "";
            if (ServerPassword.Text == "")
            {
                pWord = null;
            }
            else
            {
                pWord = ServerPassword.Text;
            }
            ItemsHandlingFlags IHF = ItemsHandlingFlags.AllItems;
            LoginResult TheResult = TheSession.TryConnectAndLogin("Supreme Commander", SlotName.Text, IHF, null, null, null, pWord);
            if (TheResult.Successful)
            {
                LoginSuccessful a = (LoginSuccessful)TheResult;
                TheSession.MessageLog.OnMessageReceived += ReceiveMessage;
                daT = TheSession.DataStorage.GetSlotData();
                makeLevels();
                updTimer.Start();
            }
            else
            {
                LoginFailure a = (LoginFailure)TheResult;
                for (int i = 0; i < a.Errors.Length; i++)
                {
                    MessageBox.Items.Add(a.Errors[i]);
                    MessageBox.Items.Refresh();
                }
            }

        }
        private void makeLevels()
        {
            Newtonsoft.Json.Linq.JArray a;
            a = (Newtonsoft.Json.Linq.JArray)daT["GRID"];
            List<List<string>> gridC = new List<List<string>>();
            for (int i = 0; i < a.Count; i++)
            {
                gridC.Add(a[i].ToObject<List<string>>());
            }
            GridWidth = gridC.Count;
            GridHeight = gridC[0].Count;
            for (int i = 0; i < GridWidth; i++)
            {
                for (int j = 0; j < GridHeight; j++)
                {
                    string levlnm = gridC[i][j].Substring(0, gridC[i][j].IndexOf("(") - 1);
                    string facU = gridC[i][j].Substring(gridC[i][j].IndexOf("(") + 1, gridC[i][j].IndexOf(")") - (gridC[i][j].IndexOf("(") + 1));
                    int Lfaction = -1;
                    switch (facU)
                    {
                        case "UEF":
                            Lfaction = 0;
                            break;
                        case "Cybran":
                            Lfaction = 1;
                            break;
                        case "Aeon":
                            Lfaction = 2;
                            break;
                        case "Sera":
                            Lfaction = 3;
                            break;
                        default:
                            break;
                    }
                    LDATA.Add(new LevelData(levlnm, Lfaction, LevelToID[levlnm], j, i));
                }
            }
            Grid ALL_OF_BUTTONS = new Grid();
            for (int i = 0; i < GridWidth; i++)
            {
                ColumnDefinition cln = new ColumnDefinition();
                cln.Width = new GridLength(1, GridUnitType.Star);
                ALL_OF_BUTTONS.ColumnDefinitions.Add(cln);
            }
            for (int i = 0; i < GridHeight; i++)
            {
                RowDefinition rdf = new RowDefinition();
                rdf.Height = new GridLength(1, GridUnitType.Star);
                ALL_OF_BUTTONS.RowDefinitions.Add(rdf);
            }
            for (int i = 0; i < LDATA.Count; i++)
            {
                Button the_Button = makeMeAButton(LDATA[i].faction, LDATA[i].Name, i);
                ADATA.Add((LDATA[i].Name, LDATA[i].faction), the_Button);
                BDATA.Add(the_Button, LDATA[i]); 
                ALL_OF_BUTTONS.Children.Add(the_Button);
                Grid.SetRow(the_Button, LDATA[i].PositionVertical);
                Grid.SetColumn(the_Button, LDATA[i].PositionHorisontal);
            }
            ButtonHolder.Content = ALL_OF_BUTTONS;
        }
        private Button makeMeAButton(int faction, string labelText, int index)
        {
            Grid Launch = new Grid();

            ColumnDefinition cln = new ColumnDefinition();
            cln.Width = new GridLength(1, GridUnitType.Star);
            ColumnDefinition cln2 = new ColumnDefinition();
            cln2.Width = new GridLength(5, GridUnitType.Star);
            RowDefinition rdf = new RowDefinition();
            rdf.Height = new GridLength(1, GridUnitType.Star);

            Launch.ColumnDefinitions.Add(cln);
            Launch.ColumnDefinitions.Add(cln2);
            Launch.RowDefinitions.Add(rdf);

            Label buttonName = new Label();
            buttonName.Content = labelText;
            buttonName.Foreground = new SolidColorBrush(Color.FromRgb(113, 239, 255));
            buttonName.FontSize = 20;
            Image buttonIcon = new Image();
            BitmapImage logo = new BitmapImage();
            logo.BeginInit();
            switch (faction)
            {
                case 0:
                    logo.UriSource = new Uri("pack://application:,,,/uef.png");
                    break;
                case 1:
                    logo.UriSource = new Uri("pack://application:,,,/cybran.png");
                    break;
                case 2:
                    logo.UriSource = new Uri("pack://application:,,,/aeon.png");
                    break;
                case 3:
                    logo.UriSource = new Uri("pack://application:,,,/seraphim.png");
                    break;
                default:
                    logo.UriSource = new Uri("pack://application:,,,/cybran.png");
                    break;
            }
            logo.EndInit();
            buttonIcon.Source = logo;

            Launch.Children.Add(buttonIcon);
            Launch.Children.Add(buttonName);
            Grid.SetRow(buttonIcon, 0);
            Grid.SetRow(buttonName, 0);
            Grid.SetColumn(buttonIcon, 0);
            Grid.SetColumn(buttonName, 1);

            LDATA[index].ButtonText = buttonName;

            Button a = new Button();
            a.Background = new SolidColorBrush(Color.FromRgb(23, 46, 76));
            a.Content = Launch;

            a.Click += (sender, e) => { OpenM1(sender,e); };
            return a;
        }
        void ReceiveMessage(LogMessage message)
        {
            string messageLine = message.ToString();
            
            MessageBox.Items.Add(messageLine);
            MessageBox.Items.Refresh();
        }
        private void SayHelloWorldToServer(object sender, System.Windows.Input.KeyEventArgs e)
        {
            if (e.Key == System.Windows.Input.Key.Enter && InputMsg.Text != "" && TheSession.Socket.Connected)
            {
                TheSession.Say(InputMsg.Text);
                InputMsg.Text = "";
            }
        }
        void DeleteOldShit()
        {
            if (File.Exists(logfile))
            {
                File.Delete(logfile);
            }
            if (File.Exists(binFolder + "\\bin\\" + "init_coop_spec.lua"))
            {
                File.Delete(binFolder + "\\bin\\" + "init_coop_spec.lua");
            }
            for (int i = 0; i < LevelToID.Values.Count; i++)
            {
                if (Directory.Exists(mapmodFolder + "\\maps\\" + mapname))
                {
                    Directory.Delete(mapmodFolder + "\\maps\\" + mapname, true);
                }
            }
        }

        private void ExitAPP(object sender, RoutedEventArgs e)
        {
            Application.Current.Shutdown();
        }
    }
    public class SettingsData() 
    {
        public Color PlayerColor;
        public string ServerName;
        public string ServerNumbers;
        public string PlayerName;
        public string password;
        public string DataFolder;
        public string MapModFolder;
    }
    public class LevelData
    {
        public string Name;
        public int faction;
        public string LevelID;
        public int PositionVertical;
        public int PositionHorisontal;
        public ButtonState bSTATE;
        public Label ButtonText;
        public LevelData(string NAME, int FACTION, string LEVELID, int Vertical, int Horisontal)
        {
            Name = NAME;
            faction = FACTION;
            LevelID = LEVELID;
            PositionVertical = Vertical;
            PositionHorisontal = Horisontal;
            if (PositionVertical == 0 && PositionHorisontal == 0)
            {
                bSTATE = ButtonState.unfinished;
            }
            else
            {
                bSTATE = ButtonState.locked;
            }
        }
    }
    public enum ButtonState
    {
        locked,
        unfinished,
        done,
    }
}