using Archipelago.MultiClient.Net;
using Archipelago.MultiClient.Net.Enums;
using Archipelago.MultiClient.Net.MessageLog.Messages;
using ColorPicker;
using ColorPicker.Models;
using Newtonsoft.Json;
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
//using static System.Net.WebRequestMethods;
//using Path = System.IO.Path;

namespace SupComClient
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        bool GameActive = false;
        Dictionary<string, object> daT;
        DispatcherTimer updTimer = new DispatcherTimer();
        Dictionary<string, int> LocationLogToId = new Dictionary<string, int>();
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
        public MainWindow()
        {
            InitializeComponent();
            CheckDefaultOptions();
            ReadExcel();
            updTimer.Interval = new TimeSpan(0, 0, 2);
            updTimer.Tick += UpdTimer_Tick;
            initialised = true;
        }

        private void UpdTimer_Tick(object? sender, EventArgs e)
        {
            if (TheSession.Socket.Connected)
            {
                #region receive
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
                #region send
                if (GameActive)
                {
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
                        long[] a = new long[Locations.Count];
                        for (int i = 0; i < Locations.Count; i++)
                        {
                            a[i] = LocationLogToId[Locations[i]];
                        }
                        TheSession.Locations.CompleteLocationChecks(a);
                    }
                    string ThisMustBeUpdated = CurrentMap + "\\UnlockRestriction.Lua";
                    string ThisIsUpdate = "local ScenarioFramework = import('/lua/scenarioframework.lua')" + Environment.NewLine + "Unlock = {}" + Environment.NewLine;
                    for (int i = 0; i < Unlocked_Units.Count; i++)
                    {
                        ThisIsUpdate += "Unlock[" + (i + 1).ToString() + "] = categories." + Units[Unlocked_Units[i]] + Environment.NewLine;
                    }
                    ThisIsUpdate += "Elements = " + Unlocked_Units.Count + Environment.NewLine;

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
                        ThisIsUpdate = ThisIsUpdate.Remove(ThisIsUpdate.LastIndexOf(",") , 1);
                    }
                    ThisIsUpdate += "})" + Environment.NewLine + "end" + Environment.NewLine;
                    File.WriteAllText(ThisMustBeUpdated, ThisIsUpdate);
                }
                #endregion
            }
        }

        void OpenMission(string LevelName, string PlayerName, int faction, int difficulty)
        {
            #region copy
            mapname = LevelName;
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
            Directory.CreateDirectory("C:\\LOG");
            string cparams = "/init init_coop_spec.lua /diff " + difficulty.ToString() + " /EnableDiskWatch /log  C:\\LOG\\ap.log /map " + mapname;
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

            //Read cybran locations
            List<string> CybranLocations = new List<string>();
            for (int i = 2; i < 100; i++)
            {
                if (CybLoc.Cells[i, 1].GetCellValue<string>() != null)
                {
                    CybranLocations.Add(CybLoc.Cells[i, 1].GetCellValue<string>());
                }
            }
            //Write cybran locations
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
                    string id = "1" + mission.ToString();
                    if (localID < 10)
                    {
                        id += "0";
                    }
                    id += localID.ToString();
                    localID += 1;
                    LocationLogToId.Add(CybLoc.Cells[i + 2, 2].GetCellValue<string>(), int.Parse(id));
                }

            }
        }
        private void OpenM1(object sender, RoutedEventArgs e)
        {
            if (TheSession.Socket.Connected)
            {
                string Fstring = daT["faction"].ToString();
                OpenMission("SCCA_R01", TheSession.Players.ActivePlayer.Name, int.Parse(daT["faction"].ToString()), int.Parse(daT["difficulty"].ToString()));
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
            //Delete map
            string source = mapmodFolder + "maps\\" + mapname + "\\";
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
}