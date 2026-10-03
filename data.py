from __future__ import annotations
from BaseClasses import Item, ItemClassification, Location, Entrance, Region
from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasAll, Rule
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .world import SupComWorld

from .options import Mapset

ITEM_NAME_TO_ID = {"Snoop": 1000, "Mech Marine": 1001, "MA12 Striker": 1002, "Archer": 1003, "Lobo": 1004, "Mongoose": 1005, "Pillar": 1006, "Riptide": 1007, "Sky Boxer": 1008, "Flapjack": 1009, "Parashield": 1010, "Sparky": 1011, "Titan": 1012, "Cougar": 1013, "Demolisher": 1014, "Persival": 1015, "Spearhead": 1016, "Fatboy": 1017, "Hummingbird": 1018, "Cyclone": 1019, "Scorcher": 1020, "C-6 Courier": 1021, "Janus": 1022, "Stork": 1023, "Stinger": 1024, "C14 Star Lifter": 1025, "SR90 Blackbird": 1026, "Wasp": 1027, "Ambassador": 1028, "Broadsword": 1029, "Continental": 1030, "Tigershark": 1031, "Thunderhead Class": 1032, "Cooper": 1033, "Valiant Class": 1034, "Governor Class": 1035, "Bulwark": 1036, "Ace": 1037, "Summit Class": 1038, "Neptune Class": 1039, "Atlantis": 1040, "UEF Energy Storage": 1041, "UEF Mass Storage": 1042, "DM1 Plasma Cannon": 1043, "DA1 Railgun": 1044, "DN1": 1045, "UEF T1 Radar": 1046, "UEF T1 Sonar": 1047, "UEF T2 Mass Extractor": 1048, "UEF T2 Mass Fabricator": 1049, "EG - 200 Fusion Reactor": 1050, "Triad": 1051, "Air Cleaner": 1052, "Tsunami": 1053, "Klink Hammer": 1054, "Aloha": 1055, "Buzzkill": 1056, "SD - Pulse": 1057, "UEF T2 Radar": 1058, "UEF T2 Sonar": 1059, "Scattershield": 1060, "The Kennel": 1061, "UEF T3 Mass Extractor": 1062, "UEF T3 Mass Fabricator": 1063, "EG 900 Fusion Reactor": 1064, "Flayer": 1065, "Ravager": 1066, "Duke": 1067, "Stonager": 1068, "HSD Pulse": 1069, "Nuke Eliminator": 1070, "UEF Omni": 1071, "QGW R-32": 1072, "UEF T3 Sonar": 1073, "Novax Center": 1074, "Mavor": 1075, "UEF RAS": 1076, "UEF Personal shield": 1077, "UEF Area shield": 1078, "UEF Teleporter": 1079, "UEF Gun": 1080, "UEF T2": 1081, "UEF T3": 1082, "UEF TML": 1083, "UEF Billy": 1084, "UEF Regen": 1085, "UEF Drone": 1086, "UEF Second drone": 1087, "Mole": 2000, "Hunter": 2001, "Mantis": 2002, "Sky Slammer": 2003, "Medusa": 2004, "Hoplite": 2005, "Rhino": 2006, "Wagner": 2007, "Banger": 2008, "Viper": 2009, "Deceiver": 2010, "Fire Beetle": 2011, "Loyalist": 2012, "The Brick": 2013, "Bouncer": 2014, "Trebuchet": 2015, "Monkeylord": 2016, "Megalith": 2017, "Scathis": 2018, "Flying Eyes": 2019, "Prowler": 2020, "Zeus": 2021, "Jester": 2022, "Sky Hook": 2023, "Corsair": 2024, "Cormorant": 2025, "Renegade": 2026, "Dragonfly": 2027, "Spook": 2028, "Gemini": 2029, "Revenant": 2030, "Wailer": 2031, "Soul Ripper": 2032, "Sliver": 2033, "Trident Class": 2034, "Barracuda": 2035, "Salem Class": 2036, "Siren Class": 2037, "CI:18 Mermaid": 2038, "Plan B": 2039, "Galaxy Class": 2040, "Command Class": 2041, "Cybran Energy Storage": 2042, "Cybran Mass Storage": 2043, "Auto Gun": 2044, "Tracer": 2045, "Scuttle": 2046, "Cybran T1 Radar": 2047, "Cybran T1 Sonar": 2048, "Cybran T2 Mass Extractor": 2049, "Cybran T2 Mass Fabricator": 2050, "Cybran T2 Generator": 2051, "Cerberus": 2052, "Burst Master": 2053, "Nanite Torpedo Array": 2054, "Gunther": 2055, "TML-4": 2056, "Zapper": 2057, "ED1": 2058, "Cybran T2 Radar": 2059, "Cybran T2 Sonar": 2060, "Twilight": 2061, "Hive": 2062, "Cybran T3 Mass Extractor": 2063, "Cybran T3 Mass Fabricator": 2064, "Ion Reactor": 2065, "Myrmidon": 2066, "HARMS": 2067, "Disruptor": 2068, "Liberator": 2069, "ED4": 2070, "Guardian": 2071, "Cybran Omni": 2072, "Soothsayer": 2073, "Summoner": 2074, "Flood XR": 2075, "Cybran RAS": 2076, "Cybran Stealth": 2077, "Cybran Regen": 2078, "Cybran Cloak": 2079, "Cybran Teleporter": 2080, "Cybran Gun": 2081, "Cybran T2": 2082, "Cybran T3": 2083, "Cybran Torpedo": 2084, "Cybran Laser": 2085, "Spirit": 3000, "Flare": 3001, "Aurora": 3002, "Thisle": 3003, "Fervor": 3004, "Obsidian": 3005, "Blaze": 3006, "Ascendant": 3007, "Eversong": 3008, "Asylum": 3009, "Sprite Striker": 3010, "Harbringer Mk4": 3011, "Redeemer": 3012, "Serenity": 3013, "Absolver": 3014, "Galactic Colossus": 3015, "Mirage": 3016, "Conservator": 3017, "Shimmer": 3018, "Chariot": 3019, "Swift Wind": 3020, "Skimmer": 3021, "Specter": 3022, "Mercy": 3023, "Aluminar": 3024, "Seer": 3025, "Corona": 3026, "Solace": 3027, "Shocker": 3028, "Restorer": 3029, "Czar": 3030, "Sylph": 3031, "Shard": 3032, "Beacon Class": 3033, "Vesper": 3034, "Exodus Class": 3035, "Infinity Class": 3036, "Silencer": 3037, "Omen Class": 3038, "Torrent Class": 3039, "Keefer Class": 3040, "Tempest": 3041, "Aeon Energy Storage": 3042, "Aeon Mass Storage": 3043, "Erupter": 3044, "Seeker": 3045, "Tide": 3046, "Aeon T1 Radar": 3047, "Aeon T1 Sonar": 3048, "Aeon T2 Mass Extractor": 3049, "Aeon T2 Mass Fabricator": 3050, "Aeon T2 Generator": 3051, "Oblivion": 3052, "Marr": 3053, "Wave Break": 3054, "Miasma": 3055, "Serpentine": 3056, "Volcano": 3057, "Shield Of Light": 3058, "Aeon T2 Radar": 3059, "Aeon T2 Sonar": 3060, "Veil": 3061, "Aeon T3 Mass Extractor": 3062, "Aeon T3 Mass Fabricator": 3063, "Quantum Reactor": 3064, "Transcender": 3065, "Emissary": 3066, "Apocalypse": 3067, "Patron": 3068, "Radiance": 3069, "Eye Of Rhianne": 3070, "Aeon Omni": 3071, "Portal": 3072, "Paragon": 3073, "Salvation": 3074, "Aeon RAS": 3075, "Aeon RAS+": 3076, "Aeon Teleporter": 3077, "Aeon Shield": 3078, "Aeon Heavy Shield": 3079, "Aeon Speed": 3080, "Aeon Range": 3081, "Aeon Extra Range": 3082, "Aeon T2": 3083, "Aeon T3": 3084, "Aeon Sensor": 3085, "Aeon Chrono Dampener": 3086, "Selen": 4000, "Thaam": 4001, "Ia-istle": 4002, "Zthuee": 4003, "Ilshavoh": 4004, "Yenzyne": 4005, "Iashavoh": 4006, "Ythisah": 4007, "Athanah": 4008, "Othuum": 4009, "Usha-Ah": 4010, "Uyanah": 4011, "Suthanus": 4012, "Ythotha": 4013, "Sele-istle": 4014, "Ia-atha": 4015, "Sinnve": 4016, "Vish": 4017, "Notha": 4018, "Uosioz": 4019, "Vulthoo": 4020, "Vishala": 4021, "Iaselen": 4022, "Iazyne": 4023, "Sinntha": 4024, "Ahwassa": 4025, "Sou-istle": 4026, "Hau-esel": 4027, "Uashavoh": 4028, "Ithalua": 4029, "Yathsou": 4030, "Hauthuum": 4031, "Iavish": 4032, "Vishyal": 4033, "Vishuyal": 4034, "Uttaus": 4035, "Ialla": 4036, "Sou-atha": 4037, "Esel": 4038, "Shou": 4039, "Sera T2 Mass Extractor": 4040, "Sera T2 Mass Fabricator": 4041, "Sera T2 Generator": 4042, "Uttaushala": 4043, "Sinnatha": 4044, "Uosthu": 4045, "Zthuthaam": 4046, "Ythis": 4047, "Ythisatha": 4048, "Atha": 4049, "Sele-esel": 4050, "Shou-esel": 4051, "Sele-ioz": 4052, "Sera T3 Mass Extractor": 4053, "Sera T3 Mass Fabricator": 4054, "Uya-iya": 4055, "Iathu-ioz": 4056, "Hovatham": 4057, "Hastue": 4058, "Ythisioz": 4059, "Athanuhthe": 4060, "Aezesel": 4061, "Aezthu-uhthe": 4062, "Yolona Oss": 4063, "Sera RAS": 4064, "Sera ARAS": 4065, "Sera Regen": 4066, "Sera Super Regen": 4067, "Sera Repair field": 4068, "Sera Super repair field": 4069, "Sera TML": 4070, "Sera Gun": 4071, "Sera Super Gun": 4072, "Sera Teleporter": 4073, "Sera T2": 4074, "Sera T3": 4075, "Nothing": 5000, }
DEFAULT_ITEM_CLASSIFICATIONS = {"Snoop": ItemClassification.progression | ItemClassification.useful, "Mech Marine": ItemClassification.progression | ItemClassification.useful, "MA12 Striker": ItemClassification.progression | ItemClassification.useful, "Archer": ItemClassification.progression | ItemClassification.useful, "Lobo": ItemClassification.progression | ItemClassification.useful, "Mongoose": ItemClassification.progression | ItemClassification.useful, "Pillar": ItemClassification.progression | ItemClassification.useful, "Riptide": ItemClassification.progression | ItemClassification.useful, "Sky Boxer": ItemClassification.progression | ItemClassification.useful, "Flapjack": ItemClassification.progression | ItemClassification.useful, "Parashield": ItemClassification.progression | ItemClassification.useful, "Sparky": ItemClassification.progression | ItemClassification.useful, "Titan": ItemClassification.progression | ItemClassification.useful, "Cougar": ItemClassification.progression | ItemClassification.useful, "Demolisher": ItemClassification.progression | ItemClassification.useful, "Persival": ItemClassification.progression | ItemClassification.useful, "Spearhead": ItemClassification.progression | ItemClassification.useful, "Fatboy": ItemClassification.progression | ItemClassification.useful, "Hummingbird": ItemClassification.progression | ItemClassification.useful, "Cyclone": ItemClassification.progression | ItemClassification.useful, "Scorcher": ItemClassification.progression | ItemClassification.useful, "C-6 Courier": ItemClassification.progression | ItemClassification.useful, "Janus": ItemClassification.progression | ItemClassification.useful, "Stork": ItemClassification.progression | ItemClassification.useful, "Stinger": ItemClassification.progression | ItemClassification.useful, "C14 Star Lifter": ItemClassification.progression | ItemClassification.useful, "SR90 Blackbird": ItemClassification.progression | ItemClassification.useful, "Wasp": ItemClassification.progression | ItemClassification.useful, "Ambassador": ItemClassification.progression | ItemClassification.useful, "Broadsword": ItemClassification.progression | ItemClassification.useful, "Continental": ItemClassification.progression | ItemClassification.useful, "Tigershark": ItemClassification.progression | ItemClassification.useful, "Thunderhead Class": ItemClassification.progression | ItemClassification.useful, "Cooper": ItemClassification.progression | ItemClassification.useful, "Valiant Class": ItemClassification.progression | ItemClassification.useful, "Governor Class": ItemClassification.progression | ItemClassification.useful, "Bulwark": ItemClassification.progression | ItemClassification.useful, "Ace": ItemClassification.progression | ItemClassification.useful, "Summit Class": ItemClassification.progression | ItemClassification.useful, "Neptune Class": ItemClassification.progression | ItemClassification.useful, "Atlantis": ItemClassification.progression | ItemClassification.useful, "UEF Energy Storage": ItemClassification.progression | ItemClassification.useful, "UEF Mass Storage": ItemClassification.progression | ItemClassification.useful, "DM1 Plasma Cannon": ItemClassification.progression | ItemClassification.useful, "DA1 Railgun": ItemClassification.progression | ItemClassification.useful, "DN1": ItemClassification.progression | ItemClassification.useful, "UEF T1 Radar": ItemClassification.progression | ItemClassification.useful, "UEF T1 Sonar": ItemClassification.progression | ItemClassification.useful, "UEF T2 Mass Extractor": ItemClassification.progression | ItemClassification.useful, "UEF T2 Mass Fabricator": ItemClassification.progression | ItemClassification.useful, "EG - 200 Fusion Reactor": ItemClassification.progression | ItemClassification.useful, "Triad": ItemClassification.progression | ItemClassification.useful, "Air Cleaner": ItemClassification.progression | ItemClassification.useful, "Tsunami": ItemClassification.progression | ItemClassification.useful, "Klink Hammer": ItemClassification.progression | ItemClassification.useful, "Aloha": ItemClassification.progression | ItemClassification.useful, "Buzzkill": ItemClassification.progression | ItemClassification.useful, "SD - Pulse": ItemClassification.progression | ItemClassification.useful, "UEF T2 Radar": ItemClassification.progression | ItemClassification.useful, "UEF T2 Sonar": ItemClassification.progression | ItemClassification.useful, "Scattershield": ItemClassification.progression | ItemClassification.useful, "The Kennel": ItemClassification.progression | ItemClassification.useful, "UEF T3 Mass Extractor": ItemClassification.progression | ItemClassification.useful, "UEF T3 Mass Fabricator": ItemClassification.progression | ItemClassification.useful, "EG 900 Fusion Reactor": ItemClassification.progression | ItemClassification.useful, "Flayer": ItemClassification.progression | ItemClassification.useful, "Ravager": ItemClassification.progression | ItemClassification.useful, "Duke": ItemClassification.progression | ItemClassification.useful, "Stonager": ItemClassification.progression | ItemClassification.useful, "HSD Pulse": ItemClassification.progression | ItemClassification.useful, "Nuke Eliminator": ItemClassification.progression | ItemClassification.useful, "UEF Omni": ItemClassification.progression | ItemClassification.useful, "QGW R-32": ItemClassification.progression | ItemClassification.useful, "UEF T3 Sonar": ItemClassification.progression | ItemClassification.useful, "Novax Center": ItemClassification.progression | ItemClassification.useful, "Mavor": ItemClassification.progression | ItemClassification.useful, "UEF RAS": ItemClassification.progression | ItemClassification.useful, "UEF Personal shield": ItemClassification.progression | ItemClassification.useful, "UEF Area shield": ItemClassification.progression | ItemClassification.useful, "UEF Teleporter": ItemClassification.progression | ItemClassification.useful, "UEF Gun": ItemClassification.progression | ItemClassification.useful, "UEF T2": ItemClassification.progression | ItemClassification.useful, "UEF T3": ItemClassification.progression | ItemClassification.useful, "UEF TML": ItemClassification.progression | ItemClassification.useful, "UEF Billy": ItemClassification.progression | ItemClassification.useful, "UEF Regen": ItemClassification.progression | ItemClassification.useful, "UEF Drone": ItemClassification.progression | ItemClassification.useful, "UEF Second drone": ItemClassification.progression | ItemClassification.useful, "Mole": ItemClassification.progression | ItemClassification.useful, "Hunter": ItemClassification.progression | ItemClassification.useful, "Mantis": ItemClassification.progression | ItemClassification.useful, "Sky Slammer": ItemClassification.progression | ItemClassification.useful, "Medusa": ItemClassification.progression | ItemClassification.useful, "Hoplite": ItemClassification.progression | ItemClassification.useful, "Rhino": ItemClassification.progression | ItemClassification.useful, "Wagner": ItemClassification.progression | ItemClassification.useful, "Banger": ItemClassification.progression | ItemClassification.useful, "Viper": ItemClassification.progression | ItemClassification.useful, "Deceiver": ItemClassification.progression | ItemClassification.useful, "Fire Beetle": ItemClassification.progression | ItemClassification.useful, "Loyalist": ItemClassification.progression | ItemClassification.useful, "The Brick": ItemClassification.progression | ItemClassification.useful, "Bouncer": ItemClassification.progression | ItemClassification.useful, "Trebuchet": ItemClassification.progression | ItemClassification.useful, "Monkeylord": ItemClassification.progression | ItemClassification.useful, "Megalith": ItemClassification.progression | ItemClassification.useful, "Scathis": ItemClassification.progression | ItemClassification.useful, "Flying Eyes": ItemClassification.progression | ItemClassification.useful, "Prowler": ItemClassification.progression | ItemClassification.useful, "Zeus": ItemClassification.progression | ItemClassification.useful, "Jester": ItemClassification.progression | ItemClassification.useful, "Sky Hook": ItemClassification.progression | ItemClassification.useful, "Corsair": ItemClassification.progression | ItemClassification.useful, "Cormorant": ItemClassification.progression | ItemClassification.useful, "Renegade": ItemClassification.progression | ItemClassification.useful, "Dragonfly": ItemClassification.progression | ItemClassification.useful, "Spook": ItemClassification.progression | ItemClassification.useful, "Gemini": ItemClassification.progression | ItemClassification.useful, "Revenant": ItemClassification.progression | ItemClassification.useful, "Wailer": ItemClassification.progression | ItemClassification.useful, "Soul Ripper": ItemClassification.progression | ItemClassification.useful, "Sliver": ItemClassification.progression | ItemClassification.useful, "Trident Class": ItemClassification.progression | ItemClassification.useful, "Barracuda": ItemClassification.progression | ItemClassification.useful, "Salem Class": ItemClassification.progression | ItemClassification.useful, "Siren Class": ItemClassification.progression | ItemClassification.useful, "CI:18 Mermaid": ItemClassification.progression | ItemClassification.useful, "Plan B": ItemClassification.progression | ItemClassification.useful, "Galaxy Class": ItemClassification.progression | ItemClassification.useful, "Command Class": ItemClassification.progression | ItemClassification.useful, "Cybran Energy Storage": ItemClassification.progression | ItemClassification.useful, "Cybran Mass Storage": ItemClassification.progression | ItemClassification.useful, "Auto Gun": ItemClassification.progression | ItemClassification.useful, "Tracer": ItemClassification.progression | ItemClassification.useful, "Scuttle": ItemClassification.progression | ItemClassification.useful, "Cybran T1 Radar": ItemClassification.progression | ItemClassification.useful, "Cybran T1 Sonar": ItemClassification.progression | ItemClassification.useful, "Cybran T2 Mass Extractor": ItemClassification.progression | ItemClassification.useful, "Cybran T2 Mass Fabricator": ItemClassification.progression | ItemClassification.useful, "Cybran T2 Generator": ItemClassification.progression | ItemClassification.useful, "Cerberus": ItemClassification.progression | ItemClassification.useful, "Burst Master": ItemClassification.progression | ItemClassification.useful, "Nanite Torpedo Array": ItemClassification.progression | ItemClassification.useful, "Gunther": ItemClassification.progression | ItemClassification.useful, "TML-4": ItemClassification.progression | ItemClassification.useful, "Zapper": ItemClassification.progression | ItemClassification.useful, "ED1": ItemClassification.progression | ItemClassification.useful, "Cybran T2 Radar": ItemClassification.progression | ItemClassification.useful, "Cybran T2 Sonar": ItemClassification.progression | ItemClassification.useful, "Twilight": ItemClassification.progression | ItemClassification.useful, "Hive": ItemClassification.progression | ItemClassification.useful, "Cybran T3 Mass Extractor": ItemClassification.progression | ItemClassification.useful, "Cybran T3 Mass Fabricator": ItemClassification.progression | ItemClassification.useful, "Ion Reactor": ItemClassification.progression | ItemClassification.useful, "Myrmidon": ItemClassification.progression | ItemClassification.useful, "HARMS": ItemClassification.progression | ItemClassification.useful, "Disruptor": ItemClassification.progression | ItemClassification.useful, "Liberator": ItemClassification.progression | ItemClassification.useful, "ED4": ItemClassification.progression | ItemClassification.useful, "Guardian": ItemClassification.progression | ItemClassification.useful, "Cybran Omni": ItemClassification.progression | ItemClassification.useful, "Soothsayer": ItemClassification.progression | ItemClassification.useful, "Summoner": ItemClassification.progression | ItemClassification.useful, "Flood XR": ItemClassification.progression | ItemClassification.useful, "Cybran RAS": ItemClassification.progression | ItemClassification.useful, "Cybran Stealth": ItemClassification.progression | ItemClassification.useful, "Cybran Regen": ItemClassification.progression | ItemClassification.useful, "Cybran Cloak": ItemClassification.progression | ItemClassification.useful, "Cybran Teleporter": ItemClassification.progression | ItemClassification.useful, "Cybran Gun": ItemClassification.progression | ItemClassification.useful, "Cybran T2": ItemClassification.progression | ItemClassification.useful, "Cybran T3": ItemClassification.progression | ItemClassification.useful, "Cybran Torpedo": ItemClassification.progression | ItemClassification.useful, "Cybran Laser": ItemClassification.progression | ItemClassification.useful, "Spirit": ItemClassification.progression | ItemClassification.useful, "Flare": ItemClassification.progression | ItemClassification.useful, "Aurora": ItemClassification.progression | ItemClassification.useful, "Thisle": ItemClassification.progression | ItemClassification.useful, "Fervor": ItemClassification.progression | ItemClassification.useful, "Obsidian": ItemClassification.progression | ItemClassification.useful, "Blaze": ItemClassification.progression | ItemClassification.useful, "Ascendant": ItemClassification.progression | ItemClassification.useful, "Eversong": ItemClassification.progression | ItemClassification.useful, "Asylum": ItemClassification.progression | ItemClassification.useful, "Sprite Striker": ItemClassification.progression | ItemClassification.useful, "Harbringer Mk4": ItemClassification.progression | ItemClassification.useful, "Redeemer": ItemClassification.progression | ItemClassification.useful, "Serenity": ItemClassification.progression | ItemClassification.useful, "Absolver": ItemClassification.progression | ItemClassification.useful, "Galactic Colossus": ItemClassification.progression | ItemClassification.useful, "Mirage": ItemClassification.progression | ItemClassification.useful, "Conservator": ItemClassification.progression | ItemClassification.useful, "Shimmer": ItemClassification.progression | ItemClassification.useful, "Chariot": ItemClassification.progression | ItemClassification.useful, "Swift Wind": ItemClassification.progression | ItemClassification.useful, "Skimmer": ItemClassification.progression | ItemClassification.useful, "Specter": ItemClassification.progression | ItemClassification.useful, "Mercy": ItemClassification.progression | ItemClassification.useful, "Aluminar": ItemClassification.progression | ItemClassification.useful, "Seer": ItemClassification.progression | ItemClassification.useful, "Corona": ItemClassification.progression | ItemClassification.useful, "Solace": ItemClassification.progression | ItemClassification.useful, "Shocker": ItemClassification.progression | ItemClassification.useful, "Restorer": ItemClassification.progression | ItemClassification.useful, "Czar": ItemClassification.progression | ItemClassification.useful, "Sylph": ItemClassification.progression | ItemClassification.useful, "Shard": ItemClassification.progression | ItemClassification.useful, "Beacon Class": ItemClassification.progression | ItemClassification.useful, "Vesper": ItemClassification.progression | ItemClassification.useful, "Exodus Class": ItemClassification.progression | ItemClassification.useful, "Infinity Class": ItemClassification.progression | ItemClassification.useful, "Silencer": ItemClassification.progression | ItemClassification.useful, "Omen Class": ItemClassification.progression | ItemClassification.useful, "Torrent Class": ItemClassification.progression | ItemClassification.useful, "Keefer Class": ItemClassification.progression | ItemClassification.useful, "Tempest": ItemClassification.progression | ItemClassification.useful, "Aeon Energy Storage": ItemClassification.progression | ItemClassification.useful, "Aeon Mass Storage": ItemClassification.progression | ItemClassification.useful, "Erupter": ItemClassification.progression | ItemClassification.useful, "Seeker": ItemClassification.progression | ItemClassification.useful, "Tide": ItemClassification.progression | ItemClassification.useful, "Aeon T1 Radar": ItemClassification.progression | ItemClassification.useful, "Aeon T1 Sonar": ItemClassification.progression | ItemClassification.useful, "Aeon T2 Mass Extractor": ItemClassification.progression | ItemClassification.useful, "Aeon T2 Mass Fabricator": ItemClassification.progression | ItemClassification.useful, "Aeon T2 Generator": ItemClassification.progression | ItemClassification.useful, "Oblivion": ItemClassification.progression | ItemClassification.useful, "Marr": ItemClassification.progression | ItemClassification.useful, "Wave Break": ItemClassification.progression | ItemClassification.useful, "Miasma": ItemClassification.progression | ItemClassification.useful, "Serpentine": ItemClassification.progression | ItemClassification.useful, "Volcano": ItemClassification.progression | ItemClassification.useful, "Shield Of Light": ItemClassification.progression | ItemClassification.useful, "Aeon T2 Radar": ItemClassification.progression | ItemClassification.useful, "Aeon T2 Sonar": ItemClassification.progression | ItemClassification.useful, "Veil": ItemClassification.progression | ItemClassification.useful, "Aeon T3 Mass Extractor": ItemClassification.progression | ItemClassification.useful, "Aeon T3 Mass Fabricator": ItemClassification.progression | ItemClassification.useful, "Quantum Reactor": ItemClassification.progression | ItemClassification.useful, "Transcender": ItemClassification.progression | ItemClassification.useful, "Emissary": ItemClassification.progression | ItemClassification.useful, "Apocalypse": ItemClassification.progression | ItemClassification.useful, "Patron": ItemClassification.progression | ItemClassification.useful, "Radiance": ItemClassification.progression | ItemClassification.useful, "Eye Of Rhianne": ItemClassification.progression | ItemClassification.useful, "Aeon Omni": ItemClassification.progression | ItemClassification.useful, "Portal": ItemClassification.progression | ItemClassification.useful, "Paragon": ItemClassification.progression | ItemClassification.useful, "Salvation": ItemClassification.progression | ItemClassification.useful, "Aeon RAS": ItemClassification.progression | ItemClassification.useful, "Aeon RAS+": ItemClassification.progression | ItemClassification.useful, "Aeon Teleporter": ItemClassification.progression | ItemClassification.useful, "Aeon Shield": ItemClassification.progression | ItemClassification.useful, "Aeon Heavy Shield": ItemClassification.progression | ItemClassification.useful, "Aeon Speed": ItemClassification.progression | ItemClassification.useful, "Aeon Range": ItemClassification.progression | ItemClassification.useful, "Aeon Extra Range": ItemClassification.progression | ItemClassification.useful, "Aeon T2": ItemClassification.progression | ItemClassification.useful, "Aeon T3": ItemClassification.progression | ItemClassification.useful, "Aeon Sensor": ItemClassification.progression | ItemClassification.useful, "Aeon Chrono Dampener": ItemClassification.progression | ItemClassification.useful, "Selen": ItemClassification.progression | ItemClassification.useful, "Thaam": ItemClassification.progression | ItemClassification.useful, "Ia-istle": ItemClassification.progression | ItemClassification.useful, "Zthuee": ItemClassification.progression | ItemClassification.useful, "Ilshavoh": ItemClassification.progression | ItemClassification.useful, "Yenzyne": ItemClassification.progression | ItemClassification.useful, "Iashavoh": ItemClassification.progression | ItemClassification.useful, "Ythisah": ItemClassification.progression | ItemClassification.useful, "Athanah": ItemClassification.progression | ItemClassification.useful, "Othuum": ItemClassification.progression | ItemClassification.useful, "Usha-Ah": ItemClassification.progression | ItemClassification.useful, "Uyanah": ItemClassification.progression | ItemClassification.useful, "Suthanus": ItemClassification.progression | ItemClassification.useful, "Ythotha": ItemClassification.progression | ItemClassification.useful, "Sele-istle": ItemClassification.progression | ItemClassification.useful, "Ia-atha": ItemClassification.progression | ItemClassification.useful, "Sinnve": ItemClassification.progression | ItemClassification.useful, "Vish": ItemClassification.progression | ItemClassification.useful, "Notha": ItemClassification.progression | ItemClassification.useful, "Uosioz": ItemClassification.progression | ItemClassification.useful, "Vulthoo": ItemClassification.progression | ItemClassification.useful, "Vishala": ItemClassification.progression | ItemClassification.useful, "Iaselen": ItemClassification.progression | ItemClassification.useful, "Iazyne": ItemClassification.progression | ItemClassification.useful, "Sinntha": ItemClassification.progression | ItemClassification.useful, "Ahwassa": ItemClassification.progression | ItemClassification.useful, "Sou-istle": ItemClassification.progression | ItemClassification.useful, "Hau-esel": ItemClassification.progression | ItemClassification.useful, "Uashavoh": ItemClassification.progression | ItemClassification.useful, "Ithalua": ItemClassification.progression | ItemClassification.useful, "Yathsou": ItemClassification.progression | ItemClassification.useful, "Hauthuum": ItemClassification.progression | ItemClassification.useful, "Iavish": ItemClassification.progression | ItemClassification.useful, "Vishyal": ItemClassification.progression | ItemClassification.useful, "Vishuyal": ItemClassification.progression | ItemClassification.useful, "Uttaus": ItemClassification.progression | ItemClassification.useful, "Ialla": ItemClassification.progression | ItemClassification.useful, "Sou-atha": ItemClassification.progression | ItemClassification.useful, "Esel": ItemClassification.progression | ItemClassification.useful, "Shou": ItemClassification.progression | ItemClassification.useful, "Sera T2 Mass Extractor": ItemClassification.progression | ItemClassification.useful, "Sera T2 Mass Fabricator": ItemClassification.progression | ItemClassification.useful, "Sera T2 Generator": ItemClassification.progression | ItemClassification.useful, "Uttaushala": ItemClassification.progression | ItemClassification.useful, "Sinnatha": ItemClassification.progression | ItemClassification.useful, "Uosthu": ItemClassification.progression | ItemClassification.useful, "Zthuthaam": ItemClassification.progression | ItemClassification.useful, "Ythis": ItemClassification.progression | ItemClassification.useful, "Ythisatha": ItemClassification.progression | ItemClassification.useful, "Atha": ItemClassification.progression | ItemClassification.useful, "Sele-esel": ItemClassification.progression | ItemClassification.useful, "Shou-esel": ItemClassification.progression | ItemClassification.useful, "Sele-ioz": ItemClassification.progression | ItemClassification.useful, "Sera T3 Mass Extractor": ItemClassification.progression | ItemClassification.useful, "Sera T3 Mass Fabricator": ItemClassification.progression | ItemClassification.useful, "Uya-iya": ItemClassification.progression | ItemClassification.useful, "Iathu-ioz": ItemClassification.progression | ItemClassification.useful, "Hovatham": ItemClassification.progression | ItemClassification.useful, "Hastue": ItemClassification.progression | ItemClassification.useful, "Ythisioz": ItemClassification.progression | ItemClassification.useful, "Athanuhthe": ItemClassification.progression | ItemClassification.useful, "Aezesel": ItemClassification.progression | ItemClassification.useful, "Aezthu-uhthe": ItemClassification.progression | ItemClassification.useful, "Yolona Oss": ItemClassification.progression | ItemClassification.useful, "Sera RAS": ItemClassification.progression | ItemClassification.useful, "Sera ARAS": ItemClassification.progression | ItemClassification.useful, "Sera Regen": ItemClassification.progression | ItemClassification.useful, "Sera Super Regen": ItemClassification.progression | ItemClassification.useful, "Sera Repair field": ItemClassification.progression | ItemClassification.useful, "Sera Super repair field": ItemClassification.progression | ItemClassification.useful, "Sera TML": ItemClassification.progression | ItemClassification.useful, "Sera Gun": ItemClassification.progression | ItemClassification.useful, "Sera Super Gun": ItemClassification.progression | ItemClassification.useful, "Sera Teleporter": ItemClassification.progression | ItemClassification.useful, "Sera T2": ItemClassification.progression | ItemClassification.useful, "Sera T3": ItemClassification.progression | ItemClassification.useful, "Nothing": ItemClassification.filler, }

uef_items = ["Snoop", "Mech Marine", "MA12 Striker", "Archer", "Lobo", "Mongoose", "Pillar", "Riptide", "Sky Boxer", "Flapjack", "Parashield", "Sparky", "Titan", "Cougar", "Demolisher", "Persival", "Spearhead", "Fatboy", "Hummingbird", "Cyclone", "Scorcher", "C-6 Courier", "Janus", "Stork", "Stinger", "C14 Star Lifter", "SR90 Blackbird", "Wasp", "Ambassador", "Broadsword", "Continental", "Tigershark", "Thunderhead Class", "Cooper", "Valiant Class", "Governor Class", "Bulwark", "Ace", "Summit Class", "Neptune Class", "Atlantis", "UEF Energy Storage", "UEF Mass Storage", "DM1 Plasma Cannon", "DA1 Railgun", "DN1", "UEF T1 Radar", "UEF T1 Sonar", "UEF T2 Mass Extractor", "UEF T2 Mass Fabricator", "EG - 200 Fusion Reactor", "Triad", "Air Cleaner", "Tsunami", "Klink Hammer", "Aloha", "Buzzkill", "SD - Pulse", "UEF T2 Radar", "UEF T2 Sonar", "Scattershield", "The Kennel", "UEF T3 Mass Extractor", "UEF T3 Mass Fabricator", "EG 900 Fusion Reactor", "Flayer", "Ravager", "Duke", "Stonager", "HSD Pulse", "Nuke Eliminator", "UEF Omni", "QGW R-32", "UEF T3 Sonar", "Novax Center", "Mavor", "UEF RAS", "UEF Personal shield", "UEF Area shield", "UEF Teleporter", "UEF Gun", "UEF T2", "UEF T3", "UEF TML", "UEF Billy", "UEF Regen", "UEF Drone", "UEF Second drone"]
cybran_items = ["Mole", "Hunter", "Mantis", "Sky Slammer", "Medusa", "Hoplite", "Rhino", "Wagner", "Banger", "Viper", "Deceiver", "Fire Beetle", "Loyalist", "The Brick", "Bouncer", "Trebuchet", "Monkeylord", "Megalith", "Scathis", "Flying Eyes", "Prowler", "Zeus", "Jester", "Sky Hook", "Corsair", "Cormorant", "Renegade", "Dragonfly", "Spook", "Gemini", "Revenant", "Wailer", "Soul Ripper", "Sliver", "Trident Class", "Barracuda", "Salem Class", "Siren Class", "CI:18 Mermaid", "Plan B", "Galaxy Class", "Command Class", "Cybran Energy Storage", "Cybran Mass Storage", "Auto Gun", "Tracer", "Scuttle", "Cybran T1 Radar", "Cybran T1 Sonar", "Cybran T2 Mass Extractor", "Cybran T2 Mass Fabricator", "Cybran T2 Generator", "Cerberus", "Burst Master", "Nanite Torpedo Array", "Gunther", "TML-4", "Zapper", "ED1", "Cybran T2 Radar", "Cybran T2 Sonar", "Twilight", "Hive", "Cybran T3 Mass Extractor", "Cybran T3 Mass Fabricator", "Ion Reactor", "Myrmidon", "HARMS", "Disruptor", "Liberator", "ED4", "Guardian", "Cybran Omni", "Soothsayer", "Summoner", "Flood XR", "Cybran RAS", "Cybran Stealth", "Cybran Regen", "Cybran Cloak", "Cybran Teleporter", "Cybran Gun", "Cybran T2", "Cybran T3", "Cybran Torpedo", "Cybran Laser"]
aeon_items = ["Spirit", "Flare", "Aurora", "Thisle", "Fervor", "Obsidian", "Blaze", "Ascendant", "Eversong", "Asylum", "Sprite Striker", "Harbringer Mk4", "Redeemer", "Serenity", "Absolver", "Galactic Colossus", "Mirage", "Conservator", "Shimmer", "Chariot", "Swift Wind", "Skimmer", "Specter", "Mercy", "Aluminar", "Seer", "Corona", "Solace", "Shocker", "Restorer", "Czar", "Sylph", "Shard", "Beacon Class", "Vesper", "Exodus Class", "Infinity Class", "Silencer", "Omen Class", "Torrent Class", "Keefer Class", "Tempest", "Aeon Energy Storage", "Aeon Mass Storage", "Erupter", "Seeker", "Tide", "Aeon T1 Radar", "Aeon T1 Sonar", "Aeon T2 Mass Extractor", "Aeon T2 Mass Fabricator", "Aeon T2 Generator", "Oblivion", "Marr", "Wave Break", "Miasma", "Serpentine", "Volcano", "Shield Of Light", "Aeon T2 Radar", "Aeon T2 Sonar", "Veil", "Aeon T3 Mass Extractor", "Aeon T3 Mass Fabricator", "Quantum Reactor", "Transcender", "Emissary", "Apocalypse", "Patron", "Radiance", "Eye Of Rhianne", "Aeon Omni", "Portal", "Paragon", "Salvation", "Aeon RAS", "Aeon RAS+", "Aeon Teleporter", "Aeon Shield", "Aeon Heavy Shield", "Aeon Speed", "Aeon Range", "Aeon Extra Range", "Aeon T2", "Aeon T3", "Aeon Sensor", "Aeon Chrono Dampener"]
sera_items = ["Selen", "Thaam", "Ia-istle", "Zthuee", "Ilshavoh", "Yenzyne", "Iashavoh", "Ythisah", "Athanah", "Othuum", "Usha-Ah", "Uyanah", "Suthanus", "Ythotha", "Sele-istle", "Ia-atha", "Sinnve", "Vish", "Notha", "Uosioz", "Vulthoo", "Vishala", "Iaselen", "Iazyne", "Sinntha", "Ahwassa", "Sou-istle", "Hau-esel", "Uashavoh", "Ithalua", "Yathsou", "Hauthuum", "Iavish", "Vishyal", "Vishuyal", "Uttaus", "Ialla", "Sou-atha", "Esel", "Shou", "Sera T2 Mass Extractor", "Sera T2 Mass Fabricator", "Sera T2 Generator", "Uttaushala", "Sinnatha", "Uosthu", "Zthuthaam", "Ythis", "Ythisatha", "Atha", "Sele-esel", "Shou-esel", "Sele-ioz", "Sera T3 Mass Extractor", "Sera T3 Mass Fabricator", "Uya-iya", "Iathu-ioz", "Hovatham", "Hastue", "Ythisioz", "Athanuhthe", "Aezesel", "Aezthu-uhthe", "Yolona Oss", "Sera RAS", "Sera ARAS", "Sera Regen", "Sera Super Regen", "Sera Repair field", "Sera Super repair field", "Sera TML", "Sera Gun", "Sera Super Gun", "Sera Teleporter", "Sera T2", "Sera T3"]
filler_items = ["Nothing"]

LOCATION_NAME_TO_ID = {"Liberation: Build mass (UEF) 1": 21010000, "Liberation: Build mass (UEF) 2": 21010001, "Liberation: Build mass (UEF) 3": 21010002, "Liberation: Build mass (UEF) 4": 21010003, "Liberation: Build mass (UEF) 5": 21010004, "Liberation: Build mass (UEF) 6": 21010005, "Liberation: Build mass (UEF) 7": 21010006, "Liberation: Build mass (UEF) 8": 21010007, "Liberation: Build mass (UEF) 9": 21010008, "Liberation: Build mass (UEF) 10": 21010009, "Liberation: Build mass (UEF) 11": 21010010, "Liberation: Build mass (UEF) 12": 21010011, "Liberation: Build mass (UEF) 13": 21010012, "Liberation: Build mass (UEF) 14": 21010013, "Liberation: Build mass (UEF) 15": 21010014, "Liberation: Build mass (UEF) 16": 21010015, "Liberation: Build power (UEF) 1": 21010100, "Liberation: Build power (UEF) 2": 21010101, "Liberation: Build power (UEF) 3": 21010102, "Liberation: Build power (UEF) 4": 21010103, "Liberation: Build power (UEF) 5": 21010104, "Liberation: Build power (UEF) 6": 21010105, "Liberation: Build power (UEF) 7": 21010106, "Liberation: Build power (UEF) 8": 21010107, "Liberation: Build power (UEF) 9": 21010108, "Liberation: Build power (UEF) 10": 21010109, "Liberation: Build power (UEF) 11": 21010110, "Liberation: Build power (UEF) 12": 21010111, "Liberation: Build power (UEF) 13": 21010112, "Liberation: Build power (UEF) 14": 21010113, "Liberation: Build power (UEF) 15": 21010114, "Liberation: Build power (UEF) 16": 21010115, "Liberation: Build air factory (UEF) 1": 21010200, "Liberation: Build air factory (UEF) 2": 21010201, "Liberation: Build air factory (UEF) 3": 21010202, "Liberation: Build air factory (UEF) 4": 21010203, "Liberation: Build air factory (UEF) 5": 21010204, "Liberation: Build air factory (UEF) 6": 21010205, "Liberation: Build air factory (UEF) 7": 21010206, "Liberation: Build air factory (UEF) 8": 21010207, "Liberation: Build air factory (UEF) 9": 21010208, "Liberation: Build air factory (UEF) 10": 21010209, "Liberation: Build air factory (UEF) 11": 21010210, "Liberation: Build air factory (UEF) 12": 21010211, "Liberation: Build air factory (UEF) 13": 21010212, "Liberation: Build air factory (UEF) 14": 21010213, "Liberation: Build air factory (UEF) 15": 21010214, "Liberation: Build air factory (UEF) 16": 21010215, "Liberation: Build bombers (UEF) 1": 21010300, "Liberation: Build bombers (UEF) 2": 21010301, "Liberation: Build bombers (UEF) 3": 21010302, "Liberation: Build bombers (UEF) 4": 21010303, "Liberation: Build bombers (UEF) 5": 21010304, "Liberation: Build bombers (UEF) 6": 21010305, "Liberation: Build bombers (UEF) 7": 21010306, "Liberation: Build bombers (UEF) 8": 21010307, "Liberation: Build bombers (UEF) 9": 21010308, "Liberation: Build bombers (UEF) 10": 21010309, "Liberation: Build bombers (UEF) 11": 21010310, "Liberation: Build bombers (UEF) 12": 21010311, "Liberation: Build bombers (UEF) 13": 21010312, "Liberation: Build bombers (UEF) 14": 21010313, "Liberation: Build bombers (UEF) 15": 21010314, "Liberation: Build bombers (UEF) 16": 21010315, "Liberation: Destroy radar defenders (UEF) 1": 21010400, "Liberation: Destroy radar defenders (UEF) 2": 21010401, "Liberation: Destroy radar defenders (UEF) 3": 21010402, "Liberation: Destroy radar defenders (UEF) 4": 21010403, "Liberation: Destroy radar defenders (UEF) 5": 21010404, "Liberation: Destroy radar defenders (UEF) 6": 21010405, "Liberation: Destroy radar defenders (UEF) 7": 21010406, "Liberation: Destroy radar defenders (UEF) 8": 21010407, "Liberation: Destroy radar defenders (UEF) 9": 21010408, "Liberation: Destroy radar defenders (UEF) 10": 21010409, "Liberation: Destroy radar defenders (UEF) 11": 21010410, "Liberation: Destroy radar defenders (UEF) 12": 21010411, "Liberation: Destroy radar defenders (UEF) 13": 21010412, "Liberation: Destroy radar defenders (UEF) 14": 21010413, "Liberation: Destroy radar defenders (UEF) 15": 21010414, "Liberation: Destroy radar defenders (UEF) 16": 21010415, "Liberation: Capture radars (UEF) 1": 21010500, "Liberation: Capture radars (UEF) 2": 21010501, "Liberation: Capture radars (UEF) 3": 21010502, "Liberation: Capture radars (UEF) 4": 21010503, "Liberation: Capture radars (UEF) 5": 21010504, "Liberation: Capture radars (UEF) 6": 21010505, "Liberation: Capture radars (UEF) 7": 21010506, "Liberation: Capture radars (UEF) 8": 21010507, "Liberation: Capture radars (UEF) 9": 21010508, "Liberation: Capture radars (UEF) 10": 21010509, "Liberation: Capture radars (UEF) 11": 21010510, "Liberation: Capture radars (UEF) 12": 21010511, "Liberation: Capture radars (UEF) 13": 21010512, "Liberation: Capture radars (UEF) 14": 21010513, "Liberation: Capture radars (UEF) 15": 21010514, "Liberation: Capture radars (UEF) 16": 21010515, "Liberation: Destroy mex (UEF) 1": 21010600, "Liberation: Destroy mex (UEF) 2": 21010601, "Liberation: Destroy mex (UEF) 3": 21010602, "Liberation: Destroy mex (UEF) 4": 21010603, "Liberation: Destroy mex (UEF) 5": 21010604, "Liberation: Destroy mex (UEF) 6": 21010605, "Liberation: Destroy mex (UEF) 7": 21010606, "Liberation: Destroy mex (UEF) 8": 21010607, "Liberation: Destroy mex (UEF) 9": 21010608, "Liberation: Destroy mex (UEF) 10": 21010609, "Liberation: Destroy mex (UEF) 11": 21010610, "Liberation: Destroy mex (UEF) 12": 21010611, "Liberation: Destroy mex (UEF) 13": 21010612, "Liberation: Destroy mex (UEF) 14": 21010613, "Liberation: Destroy mex (UEF) 15": 21010614, "Liberation: Destroy mex (UEF) 16": 21010615, "Liberation: Destroy UEF defences (UEF) 1": 21010700, "Liberation: Destroy UEF defences (UEF) 2": 21010701, "Liberation: Destroy UEF defences (UEF) 3": 21010702, "Liberation: Destroy UEF defences (UEF) 4": 21010703, "Liberation: Destroy UEF defences (UEF) 5": 21010704, "Liberation: Destroy UEF defences (UEF) 6": 21010705, "Liberation: Destroy UEF defences (UEF) 7": 21010706, "Liberation: Destroy UEF defences (UEF) 8": 21010707, "Liberation: Destroy UEF defences (UEF) 9": 21010708, "Liberation: Destroy UEF defences (UEF) 10": 21010709, "Liberation: Destroy UEF defences (UEF) 11": 21010710, "Liberation: Destroy UEF defences (UEF) 12": 21010711, "Liberation: Destroy UEF defences (UEF) 13": 21010712, "Liberation: Destroy UEF defences (UEF) 14": 21010713, "Liberation: Destroy UEF defences (UEF) 15": 21010714, "Liberation: Destroy UEF defences (UEF) 16": 21010715, "Liberation: Destroy UEF patrols (UEF) 1": 21010800, "Liberation: Destroy UEF patrols (UEF) 2": 21010801, "Liberation: Destroy UEF patrols (UEF) 3": 21010802, "Liberation: Destroy UEF patrols (UEF) 4": 21010803, "Liberation: Destroy UEF patrols (UEF) 5": 21010804, "Liberation: Destroy UEF patrols (UEF) 6": 21010805, "Liberation: Destroy UEF patrols (UEF) 7": 21010806, "Liberation: Destroy UEF patrols (UEF) 8": 21010807, "Liberation: Destroy UEF patrols (UEF) 9": 21010808, "Liberation: Destroy UEF patrols (UEF) 10": 21010809, "Liberation: Destroy UEF patrols (UEF) 11": 21010810, "Liberation: Destroy UEF patrols (UEF) 12": 21010811, "Liberation: Destroy UEF patrols (UEF) 13": 21010812, "Liberation: Destroy UEF patrols (UEF) 14": 21010813, "Liberation: Destroy UEF patrols (UEF) 15": 21010814, "Liberation: Destroy UEF patrols (UEF) 16": 21010815, "Liberation: Destroy UEF base defenders (UEF) 1": 21010900, "Liberation: Destroy UEF base defenders (UEF) 2": 21010901, "Liberation: Destroy UEF base defenders (UEF) 3": 21010902, "Liberation: Destroy UEF base defenders (UEF) 4": 21010903, "Liberation: Destroy UEF base defenders (UEF) 5": 21010904, "Liberation: Destroy UEF base defenders (UEF) 6": 21010905, "Liberation: Destroy UEF base defenders (UEF) 7": 21010906, "Liberation: Destroy UEF base defenders (UEF) 8": 21010907, "Liberation: Destroy UEF base defenders (UEF) 9": 21010908, "Liberation: Destroy UEF base defenders (UEF) 10": 21010909, "Liberation: Destroy UEF base defenders (UEF) 11": 21010910, "Liberation: Destroy UEF base defenders (UEF) 12": 21010911, "Liberation: Destroy UEF base defenders (UEF) 13": 21010912, "Liberation: Destroy UEF base defenders (UEF) 14": 21010913, "Liberation: Destroy UEF base defenders (UEF) 15": 21010914, "Liberation: Destroy UEF base defenders (UEF) 16": 21010915, "Liberation: Destroy UEF base (UEF) 1": 21011000, "Liberation: Destroy UEF base (UEF) 2": 21011001, "Liberation: Destroy UEF base (UEF) 3": 21011002, "Liberation: Destroy UEF base (UEF) 4": 21011003, "Liberation: Destroy UEF base (UEF) 5": 21011004, "Liberation: Destroy UEF base (UEF) 6": 21011005, "Liberation: Destroy UEF base (UEF) 7": 21011006, "Liberation: Destroy UEF base (UEF) 8": 21011007, "Liberation: Destroy UEF base (UEF) 9": 21011008, "Liberation: Destroy UEF base (UEF) 10": 21011009, "Liberation: Destroy UEF base (UEF) 11": 21011010, "Liberation: Destroy UEF base (UEF) 12": 21011011, "Liberation: Destroy UEF base (UEF) 13": 21011012, "Liberation: Destroy UEF base (UEF) 14": 21011013, "Liberation: Destroy UEF base (UEF) 15": 21011014, "Liberation: Destroy UEF base (UEF) 16": 21011015, "Liberation: Kill Aeon Commander (UEF) 1": 21011100, "Liberation: Kill Aeon Commander (UEF) 2": 21011101, "Liberation: Kill Aeon Commander (UEF) 3": 21011102, "Liberation: Kill Aeon Commander (UEF) 4": 21011103, "Liberation: Kill Aeon Commander (UEF) 5": 21011104, "Liberation: Kill Aeon Commander (UEF) 6": 21011105, "Liberation: Kill Aeon Commander (UEF) 7": 21011106, "Liberation: Kill Aeon Commander (UEF) 8": 21011107, "Liberation: Kill Aeon Commander (UEF) 9": 21011108, "Liberation: Kill Aeon Commander (UEF) 10": 21011109, "Liberation: Kill Aeon Commander (UEF) 11": 21011110, "Liberation: Kill Aeon Commander (UEF) 12": 21011111, "Liberation: Kill Aeon Commander (UEF) 13": 21011112, "Liberation: Kill Aeon Commander (UEF) 14": 21011113, "Liberation: Kill Aeon Commander (UEF) 15": 21011114, "Liberation: Kill Aeon Commander (UEF) 16": 21011115, "Artifact: Destroy first village defenders (UEF) 1": 21020000, "Artifact: Destroy first village defenders (UEF) 2": 21020001, "Artifact: Destroy first village defenders (UEF) 3": 21020002, "Artifact: Destroy first village defenders (UEF) 4": 21020003, "Artifact: Destroy first village defenders (UEF) 5": 21020004, "Artifact: Destroy first village defenders (UEF) 6": 21020005, "Artifact: Destroy first village defenders (UEF) 7": 21020006, "Artifact: Destroy first village defenders (UEF) 8": 21020007, "Artifact: Destroy first village defenders (UEF) 9": 21020008, "Artifact: Destroy first village defenders (UEF) 10": 21020009, "Artifact: Destroy first village defenders (UEF) 11": 21020010, "Artifact: Destroy first village defenders (UEF) 12": 21020011, "Artifact: Destroy first village defenders (UEF) 13": 21020012, "Artifact: Destroy first village defenders (UEF) 14": 21020013, "Artifact: Destroy first village defenders (UEF) 15": 21020014, "Artifact: Destroy first village defenders (UEF) 16": 21020015, "Artifact: Destroy first temple (UEF) 1": 21020100, "Artifact: Destroy first temple (UEF) 2": 21020101, "Artifact: Destroy first temple (UEF) 3": 21020102, "Artifact: Destroy first temple (UEF) 4": 21020103, "Artifact: Destroy first temple (UEF) 5": 21020104, "Artifact: Destroy first temple (UEF) 6": 21020105, "Artifact: Destroy first temple (UEF) 7": 21020106, "Artifact: Destroy first temple (UEF) 8": 21020107, "Artifact: Destroy first temple (UEF) 9": 21020108, "Artifact: Destroy first temple (UEF) 10": 21020109, "Artifact: Destroy first temple (UEF) 11": 21020110, "Artifact: Destroy first temple (UEF) 12": 21020111, "Artifact: Destroy first temple (UEF) 13": 21020112, "Artifact: Destroy first temple (UEF) 14": 21020113, "Artifact: Destroy first temple (UEF) 15": 21020114, "Artifact: Destroy first temple (UEF) 16": 21020115, "Artifact: Protect first artifact (UEF) 1": 21020200, "Artifact: Protect first artifact (UEF) 2": 21020201, "Artifact: Protect first artifact (UEF) 3": 21020202, "Artifact: Protect first artifact (UEF) 4": 21020203, "Artifact: Protect first artifact (UEF) 5": 21020204, "Artifact: Protect first artifact (UEF) 6": 21020205, "Artifact: Protect first artifact (UEF) 7": 21020206, "Artifact: Protect first artifact (UEF) 8": 21020207, "Artifact: Protect first artifact (UEF) 9": 21020208, "Artifact: Protect first artifact (UEF) 10": 21020209, "Artifact: Protect first artifact (UEF) 11": 21020210, "Artifact: Protect first artifact (UEF) 12": 21020211, "Artifact: Protect first artifact (UEF) 13": 21020212, "Artifact: Protect first artifact (UEF) 14": 21020213, "Artifact: Protect first artifact (UEF) 15": 21020214, "Artifact: Protect first artifact (UEF) 16": 21020215, "Artifact: Find second artifact (UEF) 1": 21020300, "Artifact: Find second artifact (UEF) 2": 21020301, "Artifact: Find second artifact (UEF) 3": 21020302, "Artifact: Find second artifact (UEF) 4": 21020303, "Artifact: Find second artifact (UEF) 5": 21020304, "Artifact: Find second artifact (UEF) 6": 21020305, "Artifact: Find second artifact (UEF) 7": 21020306, "Artifact: Find second artifact (UEF) 8": 21020307, "Artifact: Find second artifact (UEF) 9": 21020308, "Artifact: Find second artifact (UEF) 10": 21020309, "Artifact: Find second artifact (UEF) 11": 21020310, "Artifact: Find second artifact (UEF) 12": 21020311, "Artifact: Find second artifact (UEF) 13": 21020312, "Artifact: Find second artifact (UEF) 14": 21020313, "Artifact: Find second artifact (UEF) 15": 21020314, "Artifact: Find second artifact (UEF) 16": 21020315, "Artifact: Destroy Aeon reinforcements (UEF) 1": 21020400, "Artifact: Destroy Aeon reinforcements (UEF) 2": 21020401, "Artifact: Destroy Aeon reinforcements (UEF) 3": 21020402, "Artifact: Destroy Aeon reinforcements (UEF) 4": 21020403, "Artifact: Destroy Aeon reinforcements (UEF) 5": 21020404, "Artifact: Destroy Aeon reinforcements (UEF) 6": 21020405, "Artifact: Destroy Aeon reinforcements (UEF) 7": 21020406, "Artifact: Destroy Aeon reinforcements (UEF) 8": 21020407, "Artifact: Destroy Aeon reinforcements (UEF) 9": 21020408, "Artifact: Destroy Aeon reinforcements (UEF) 10": 21020409, "Artifact: Destroy Aeon reinforcements (UEF) 11": 21020410, "Artifact: Destroy Aeon reinforcements (UEF) 12": 21020411, "Artifact: Destroy Aeon reinforcements (UEF) 13": 21020412, "Artifact: Destroy Aeon reinforcements (UEF) 14": 21020413, "Artifact: Destroy Aeon reinforcements (UEF) 15": 21020414, "Artifact: Destroy Aeon reinforcements (UEF) 16": 21020415, "Artifact: Protect second artifact (UEF) 1": 21020500, "Artifact: Protect second artifact (UEF) 2": 21020501, "Artifact: Protect second artifact (UEF) 3": 21020502, "Artifact: Protect second artifact (UEF) 4": 21020503, "Artifact: Protect second artifact (UEF) 5": 21020504, "Artifact: Protect second artifact (UEF) 6": 21020505, "Artifact: Protect second artifact (UEF) 7": 21020506, "Artifact: Protect second artifact (UEF) 8": 21020507, "Artifact: Protect second artifact (UEF) 9": 21020508, "Artifact: Protect second artifact (UEF) 10": 21020509, "Artifact: Protect second artifact (UEF) 11": 21020510, "Artifact: Protect second artifact (UEF) 12": 21020511, "Artifact: Protect second artifact (UEF) 13": 21020512, "Artifact: Protect second artifact (UEF) 14": 21020513, "Artifact: Protect second artifact (UEF) 15": 21020514, "Artifact: Protect second artifact (UEF) 16": 21020515, "Artifact: Defend from Aeon attack (UEF) 1": 21020600, "Artifact: Defend from Aeon attack (UEF) 2": 21020601, "Artifact: Defend from Aeon attack (UEF) 3": 21020602, "Artifact: Defend from Aeon attack (UEF) 4": 21020603, "Artifact: Defend from Aeon attack (UEF) 5": 21020604, "Artifact: Defend from Aeon attack (UEF) 6": 21020605, "Artifact: Defend from Aeon attack (UEF) 7": 21020606, "Artifact: Defend from Aeon attack (UEF) 8": 21020607, "Artifact: Defend from Aeon attack (UEF) 9": 21020608, "Artifact: Defend from Aeon attack (UEF) 10": 21020609, "Artifact: Defend from Aeon attack (UEF) 11": 21020610, "Artifact: Defend from Aeon attack (UEF) 12": 21020611, "Artifact: Defend from Aeon attack (UEF) 13": 21020612, "Artifact: Defend from Aeon attack (UEF) 14": 21020613, "Artifact: Defend from Aeon attack (UEF) 15": 21020614, "Artifact: Defend from Aeon attack (UEF) 16": 21020615, "Artifact: Destroy eastern base (UEF) 1": 21020700, "Artifact: Destroy eastern base (UEF) 2": 21020701, "Artifact: Destroy eastern base (UEF) 3": 21020702, "Artifact: Destroy eastern base (UEF) 4": 21020703, "Artifact: Destroy eastern base (UEF) 5": 21020704, "Artifact: Destroy eastern base (UEF) 6": 21020705, "Artifact: Destroy eastern base (UEF) 7": 21020706, "Artifact: Destroy eastern base (UEF) 8": 21020707, "Artifact: Destroy eastern base (UEF) 9": 21020708, "Artifact: Destroy eastern base (UEF) 10": 21020709, "Artifact: Destroy eastern base (UEF) 11": 21020710, "Artifact: Destroy eastern base (UEF) 12": 21020711, "Artifact: Destroy eastern base (UEF) 13": 21020712, "Artifact: Destroy eastern base (UEF) 14": 21020713, "Artifact: Destroy eastern base (UEF) 15": 21020714, "Artifact: Destroy eastern base (UEF) 16": 21020715, "Artifact: Destroy navy base (UEF) 1": 21020800, "Artifact: Destroy navy base (UEF) 2": 21020801, "Artifact: Destroy navy base (UEF) 3": 21020802, "Artifact: Destroy navy base (UEF) 4": 21020803, "Artifact: Destroy navy base (UEF) 5": 21020804, "Artifact: Destroy navy base (UEF) 6": 21020805, "Artifact: Destroy navy base (UEF) 7": 21020806, "Artifact: Destroy navy base (UEF) 8": 21020807, "Artifact: Destroy navy base (UEF) 9": 21020808, "Artifact: Destroy navy base (UEF) 10": 21020809, "Artifact: Destroy navy base (UEF) 11": 21020810, "Artifact: Destroy navy base (UEF) 12": 21020811, "Artifact: Destroy navy base (UEF) 13": 21020812, "Artifact: Destroy navy base (UEF) 14": 21020813, "Artifact: Destroy navy base (UEF) 15": 21020814, "Artifact: Destroy navy base (UEF) 16": 21020815, "Artifact: Protect third artifact (UEF) 1": 21020900, "Artifact: Protect third artifact (UEF) 2": 21020901, "Artifact: Protect third artifact (UEF) 3": 21020902, "Artifact: Protect third artifact (UEF) 4": 21020903, "Artifact: Protect third artifact (UEF) 5": 21020904, "Artifact: Protect third artifact (UEF) 6": 21020905, "Artifact: Protect third artifact (UEF) 7": 21020906, "Artifact: Protect third artifact (UEF) 8": 21020907, "Artifact: Protect third artifact (UEF) 9": 21020908, "Artifact: Protect third artifact (UEF) 10": 21020909, "Artifact: Protect third artifact (UEF) 11": 21020910, "Artifact: Protect third artifact (UEF) 12": 21020911, "Artifact: Protect third artifact (UEF) 13": 21020912, "Artifact: Protect third artifact (UEF) 14": 21020913, "Artifact: Protect third artifact (UEF) 15": 21020914, "Artifact: Protect third artifact (UEF) 16": 21020915, "Artifact: Kill Aeon Commander (optional) (UEF) 1": 21021000, "Artifact: Kill Aeon Commander (optional) (UEF) 2": 21021001, "Artifact: Kill Aeon Commander (optional) (UEF) 3": 21021002, "Artifact: Kill Aeon Commander (optional) (UEF) 4": 21021003, "Artifact: Kill Aeon Commander (optional) (UEF) 5": 21021004, "Artifact: Kill Aeon Commander (optional) (UEF) 6": 21021005, "Artifact: Kill Aeon Commander (optional) (UEF) 7": 21021006, "Artifact: Kill Aeon Commander (optional) (UEF) 8": 21021007, "Artifact: Kill Aeon Commander (optional) (UEF) 9": 21021008, "Artifact: Kill Aeon Commander (optional) (UEF) 10": 21021009, "Artifact: Kill Aeon Commander (optional) (UEF) 11": 21021010, "Artifact: Kill Aeon Commander (optional) (UEF) 12": 21021011, "Artifact: Kill Aeon Commander (optional) (UEF) 13": 21021012, "Artifact: Kill Aeon Commander (optional) (UEF) 14": 21021013, "Artifact: Kill Aeon Commander (optional) (UEF) 15": 21021014, "Artifact: Kill Aeon Commander (optional) (UEF) 16": 21021015, "Artifact: Kill Mach (UEF) 1": 21021100, "Artifact: Kill Mach (UEF) 2": 21021101, "Artifact: Kill Mach (UEF) 3": 21021102, "Artifact: Kill Mach (UEF) 4": 21021103, "Artifact: Kill Mach (UEF) 5": 21021104, "Artifact: Kill Mach (UEF) 6": 21021105, "Artifact: Kill Mach (UEF) 7": 21021106, "Artifact: Kill Mach (UEF) 8": 21021107, "Artifact: Kill Mach (UEF) 9": 21021108, "Artifact: Kill Mach (UEF) 10": 21021109, "Artifact: Kill Mach (UEF) 11": 21021110, "Artifact: Kill Mach (UEF) 12": 21021111, "Artifact: Kill Mach (UEF) 13": 21021112, "Artifact: Kill Mach (UEF) 14": 21021113, "Artifact: Kill Mach (UEF) 15": 21021114, "Artifact: Kill Mach (UEF) 16": 21021115, "Artifact: Go to Gate (UEF) 1": 21021200, "Artifact: Go to Gate (UEF) 2": 21021201, "Artifact: Go to Gate (UEF) 3": 21021202, "Artifact: Go to Gate (UEF) 4": 21021203, "Artifact: Go to Gate (UEF) 5": 21021204, "Artifact: Go to Gate (UEF) 6": 21021205, "Artifact: Go to Gate (UEF) 7": 21021206, "Artifact: Go to Gate (UEF) 8": 21021207, "Artifact: Go to Gate (UEF) 9": 21021208, "Artifact: Go to Gate (UEF) 10": 21021209, "Artifact: Go to Gate (UEF) 11": 21021210, "Artifact: Go to Gate (UEF) 12": 21021211, "Artifact: Go to Gate (UEF) 13": 21021212, "Artifact: Go to Gate (UEF) 14": 21021213, "Artifact: Go to Gate (UEF) 15": 21021214, "Artifact: Go to Gate (UEF) 16": 21021215, "Defrag: Protect York 18 (UEF) 1": 21030000, "Defrag: Protect York 18 (UEF) 2": 21030001, "Defrag: Protect York 18 (UEF) 3": 21030002, "Defrag: Protect York 18 (UEF) 4": 21030003, "Defrag: Protect York 18 (UEF) 5": 21030004, "Defrag: Protect York 18 (UEF) 6": 21030005, "Defrag: Protect York 18 (UEF) 7": 21030006, "Defrag: Protect York 18 (UEF) 8": 21030007, "Defrag: Protect York 18 (UEF) 9": 21030008, "Defrag: Protect York 18 (UEF) 10": 21030009, "Defrag: Protect York 18 (UEF) 11": 21030010, "Defrag: Protect York 18 (UEF) 12": 21030011, "Defrag: Protect York 18 (UEF) 13": 21030012, "Defrag: Protect York 18 (UEF) 14": 21030013, "Defrag: Protect York 18 (UEF) 15": 21030014, "Defrag: Protect York 18 (UEF) 16": 21030015, "Defrag: Destroy western UEF base (UEF) 1": 21030100, "Defrag: Destroy western UEF base (UEF) 2": 21030101, "Defrag: Destroy western UEF base (UEF) 3": 21030102, "Defrag: Destroy western UEF base (UEF) 4": 21030103, "Defrag: Destroy western UEF base (UEF) 5": 21030104, "Defrag: Destroy western UEF base (UEF) 6": 21030105, "Defrag: Destroy western UEF base (UEF) 7": 21030106, "Defrag: Destroy western UEF base (UEF) 8": 21030107, "Defrag: Destroy western UEF base (UEF) 9": 21030108, "Defrag: Destroy western UEF base (UEF) 10": 21030109, "Defrag: Destroy western UEF base (UEF) 11": 21030110, "Defrag: Destroy western UEF base (UEF) 12": 21030111, "Defrag: Destroy western UEF base (UEF) 13": 21030112, "Defrag: Destroy western UEF base (UEF) 14": 21030113, "Defrag: Destroy western UEF base (UEF) 15": 21030114, "Defrag: Destroy western UEF base (UEF) 16": 21030115, "Defrag: Destroy north-western UEF base (UEF) 1": 21030200, "Defrag: Destroy north-western UEF base (UEF) 2": 21030201, "Defrag: Destroy north-western UEF base (UEF) 3": 21030202, "Defrag: Destroy north-western UEF base (UEF) 4": 21030203, "Defrag: Destroy north-western UEF base (UEF) 5": 21030204, "Defrag: Destroy north-western UEF base (UEF) 6": 21030205, "Defrag: Destroy north-western UEF base (UEF) 7": 21030206, "Defrag: Destroy north-western UEF base (UEF) 8": 21030207, "Defrag: Destroy north-western UEF base (UEF) 9": 21030208, "Defrag: Destroy north-western UEF base (UEF) 10": 21030209, "Defrag: Destroy north-western UEF base (UEF) 11": 21030210, "Defrag: Destroy north-western UEF base (UEF) 12": 21030211, "Defrag: Destroy north-western UEF base (UEF) 13": 21030212, "Defrag: Destroy north-western UEF base (UEF) 14": 21030213, "Defrag: Destroy north-western UEF base (UEF) 15": 21030214, "Defrag: Destroy north-western UEF base (UEF) 16": 21030215, "Defrag: Destroy northern UEF base (UEF) 1": 21030300, "Defrag: Destroy northern UEF base (UEF) 2": 21030301, "Defrag: Destroy northern UEF base (UEF) 3": 21030302, "Defrag: Destroy northern UEF base (UEF) 4": 21030303, "Defrag: Destroy northern UEF base (UEF) 5": 21030304, "Defrag: Destroy northern UEF base (UEF) 6": 21030305, "Defrag: Destroy northern UEF base (UEF) 7": 21030306, "Defrag: Destroy northern UEF base (UEF) 8": 21030307, "Defrag: Destroy northern UEF base (UEF) 9": 21030308, "Defrag: Destroy northern UEF base (UEF) 10": 21030309, "Defrag: Destroy northern UEF base (UEF) 11": 21030310, "Defrag: Destroy northern UEF base (UEF) 12": 21030311, "Defrag: Destroy northern UEF base (UEF) 13": 21030312, "Defrag: Destroy northern UEF base (UEF) 14": 21030313, "Defrag: Destroy northern UEF base (UEF) 15": 21030314, "Defrag: Destroy northern UEF base (UEF) 16": 21030315, "Defrag: Sink UEF cruiser (UEF) 1": 21030400, "Defrag: Sink UEF cruiser (UEF) 2": 21030401, "Defrag: Sink UEF cruiser (UEF) 3": 21030402, "Defrag: Sink UEF cruiser (UEF) 4": 21030403, "Defrag: Sink UEF cruiser (UEF) 5": 21030404, "Defrag: Sink UEF cruiser (UEF) 6": 21030405, "Defrag: Sink UEF cruiser (UEF) 7": 21030406, "Defrag: Sink UEF cruiser (UEF) 8": 21030407, "Defrag: Sink UEF cruiser (UEF) 9": 21030408, "Defrag: Sink UEF cruiser (UEF) 10": 21030409, "Defrag: Sink UEF cruiser (UEF) 11": 21030410, "Defrag: Sink UEF cruiser (UEF) 12": 21030411, "Defrag: Sink UEF cruiser (UEF) 13": 21030412, "Defrag: Sink UEF cruiser (UEF) 14": 21030413, "Defrag: Sink UEF cruiser (UEF) 15": 21030414, "Defrag: Sink UEF cruiser (UEF) 16": 21030415, "Defrag: Destroy static artillery (UEF) 1": 21030500, "Defrag: Destroy static artillery (UEF) 2": 21030501, "Defrag: Destroy static artillery (UEF) 3": 21030502, "Defrag: Destroy static artillery (UEF) 4": 21030503, "Defrag: Destroy static artillery (UEF) 5": 21030504, "Defrag: Destroy static artillery (UEF) 6": 21030505, "Defrag: Destroy static artillery (UEF) 7": 21030506, "Defrag: Destroy static artillery (UEF) 8": 21030507, "Defrag: Destroy static artillery (UEF) 9": 21030508, "Defrag: Destroy static artillery (UEF) 10": 21030509, "Defrag: Destroy static artillery (UEF) 11": 21030510, "Defrag: Destroy static artillery (UEF) 12": 21030511, "Defrag: Destroy static artillery (UEF) 13": 21030512, "Defrag: Destroy static artillery (UEF) 14": 21030513, "Defrag: Destroy static artillery (UEF) 15": 21030514, "Defrag: Destroy static artillery (UEF) 16": 21030515, "Defrag: Escort trucks (UEF) 1": 21030600, "Defrag: Escort trucks (UEF) 2": 21030601, "Defrag: Escort trucks (UEF) 3": 21030602, "Defrag: Escort trucks (UEF) 4": 21030603, "Defrag: Escort trucks (UEF) 5": 21030604, "Defrag: Escort trucks (UEF) 6": 21030605, "Defrag: Escort trucks (UEF) 7": 21030606, "Defrag: Escort trucks (UEF) 8": 21030607, "Defrag: Escort trucks (UEF) 9": 21030608, "Defrag: Escort trucks (UEF) 10": 21030609, "Defrag: Escort trucks (UEF) 11": 21030610, "Defrag: Escort trucks (UEF) 12": 21030611, "Defrag: Escort trucks (UEF) 13": 21030612, "Defrag: Escort trucks (UEF) 14": 21030613, "Defrag: Escort trucks (UEF) 15": 21030614, "Defrag: Escort trucks (UEF) 16": 21030615, "Defrag: Escort ALL trucks (optional) (UEF) 1": 21030700, "Defrag: Escort ALL trucks (optional) (UEF) 2": 21030701, "Defrag: Escort ALL trucks (optional) (UEF) 3": 21030702, "Defrag: Escort ALL trucks (optional) (UEF) 4": 21030703, "Defrag: Escort ALL trucks (optional) (UEF) 5": 21030704, "Defrag: Escort ALL trucks (optional) (UEF) 6": 21030705, "Defrag: Escort ALL trucks (optional) (UEF) 7": 21030706, "Defrag: Escort ALL trucks (optional) (UEF) 8": 21030707, "Defrag: Escort ALL trucks (optional) (UEF) 9": 21030708, "Defrag: Escort ALL trucks (optional) (UEF) 10": 21030709, "Defrag: Escort ALL trucks (optional) (UEF) 11": 21030710, "Defrag: Escort ALL trucks (optional) (UEF) 12": 21030711, "Defrag: Escort ALL trucks (optional) (UEF) 13": 21030712, "Defrag: Escort ALL trucks (optional) (UEF) 14": 21030713, "Defrag: Escort ALL trucks (optional) (UEF) 15": 21030714, "Defrag: Escort ALL trucks (optional) (UEF) 16": 21030715, "Defrag: Optional objective  (optional) (UEF) 1": 21030800, "Defrag: Optional objective  (optional) (UEF) 2": 21030801, "Defrag: Optional objective  (optional) (UEF) 3": 21030802, "Defrag: Optional objective  (optional) (UEF) 4": 21030803, "Defrag: Optional objective  (optional) (UEF) 5": 21030804, "Defrag: Optional objective  (optional) (UEF) 6": 21030805, "Defrag: Optional objective  (optional) (UEF) 7": 21030806, "Defrag: Optional objective  (optional) (UEF) 8": 21030807, "Defrag: Optional objective  (optional) (UEF) 9": 21030808, "Defrag: Optional objective  (optional) (UEF) 10": 21030809, "Defrag: Optional objective  (optional) (UEF) 11": 21030810, "Defrag: Optional objective  (optional) (UEF) 12": 21030811, "Defrag: Optional objective  (optional) (UEF) 13": 21030812, "Defrag: Optional objective  (optional) (UEF) 14": 21030813, "Defrag: Optional objective  (optional) (UEF) 15": 21030814, "Defrag: Optional objective  (optional) (UEF) 16": 21030815, "Defrag: Kill UEF Commander (UEF) 1": 21030900, "Defrag: Kill UEF Commander (UEF) 2": 21030901, "Defrag: Kill UEF Commander (UEF) 3": 21030902, "Defrag: Kill UEF Commander (UEF) 4": 21030903, "Defrag: Kill UEF Commander (UEF) 5": 21030904, "Defrag: Kill UEF Commander (UEF) 6": 21030905, "Defrag: Kill UEF Commander (UEF) 7": 21030906, "Defrag: Kill UEF Commander (UEF) 8": 21030907, "Defrag: Kill UEF Commander (UEF) 9": 21030908, "Defrag: Kill UEF Commander (UEF) 10": 21030909, "Defrag: Kill UEF Commander (UEF) 11": 21030910, "Defrag: Kill UEF Commander (UEF) 12": 21030911, "Defrag: Kill UEF Commander (UEF) 13": 21030912, "Defrag: Kill UEF Commander (UEF) 14": 21030913, "Defrag: Kill UEF Commander (UEF) 15": 21030914, "Defrag: Kill UEF Commander (UEF) 16": 21030915, "Mainframe Tango: Defeat Aeon Commander (UEF) 1": 21040000, "Mainframe Tango: Defeat Aeon Commander (UEF) 2": 21040001, "Mainframe Tango: Defeat Aeon Commander (UEF) 3": 21040002, "Mainframe Tango: Defeat Aeon Commander (UEF) 4": 21040003, "Mainframe Tango: Defeat Aeon Commander (UEF) 5": 21040004, "Mainframe Tango: Defeat Aeon Commander (UEF) 6": 21040005, "Mainframe Tango: Defeat Aeon Commander (UEF) 7": 21040006, "Mainframe Tango: Defeat Aeon Commander (UEF) 8": 21040007, "Mainframe Tango: Defeat Aeon Commander (UEF) 9": 21040008, "Mainframe Tango: Defeat Aeon Commander (UEF) 10": 21040009, "Mainframe Tango: Defeat Aeon Commander (UEF) 11": 21040010, "Mainframe Tango: Defeat Aeon Commander (UEF) 12": 21040011, "Mainframe Tango: Defeat Aeon Commander (UEF) 13": 21040012, "Mainframe Tango: Defeat Aeon Commander (UEF) 14": 21040013, "Mainframe Tango: Defeat Aeon Commander (UEF) 15": 21040014, "Mainframe Tango: Defeat Aeon Commander (UEF) 16": 21040015, "Mainframe Tango: Capture Network Node (UEF) 1": 21040100, "Mainframe Tango: Capture Network Node (UEF) 2": 21040101, "Mainframe Tango: Capture Network Node (UEF) 3": 21040102, "Mainframe Tango: Capture Network Node (UEF) 4": 21040103, "Mainframe Tango: Capture Network Node (UEF) 5": 21040104, "Mainframe Tango: Capture Network Node (UEF) 6": 21040105, "Mainframe Tango: Capture Network Node (UEF) 7": 21040106, "Mainframe Tango: Capture Network Node (UEF) 8": 21040107, "Mainframe Tango: Capture Network Node (UEF) 9": 21040108, "Mainframe Tango: Capture Network Node (UEF) 10": 21040109, "Mainframe Tango: Capture Network Node (UEF) 11": 21040110, "Mainframe Tango: Capture Network Node (UEF) 12": 21040111, "Mainframe Tango: Capture Network Node (UEF) 13": 21040112, "Mainframe Tango: Capture Network Node (UEF) 14": 21040113, "Mainframe Tango: Capture Network Node (UEF) 15": 21040114, "Mainframe Tango: Capture Network Node (UEF) 16": 21040115, "Mainframe Tango: Save Network Node (UEF) 1": 21040200, "Mainframe Tango: Save Network Node (UEF) 2": 21040201, "Mainframe Tango: Save Network Node (UEF) 3": 21040202, "Mainframe Tango: Save Network Node (UEF) 4": 21040203, "Mainframe Tango: Save Network Node (UEF) 5": 21040204, "Mainframe Tango: Save Network Node (UEF) 6": 21040205, "Mainframe Tango: Save Network Node (UEF) 7": 21040206, "Mainframe Tango: Save Network Node (UEF) 8": 21040207, "Mainframe Tango: Save Network Node (UEF) 9": 21040208, "Mainframe Tango: Save Network Node (UEF) 10": 21040209, "Mainframe Tango: Save Network Node (UEF) 11": 21040210, "Mainframe Tango: Save Network Node (UEF) 12": 21040211, "Mainframe Tango: Save Network Node (UEF) 13": 21040212, "Mainframe Tango: Save Network Node (UEF) 14": 21040213, "Mainframe Tango: Save Network Node (UEF) 15": 21040214, "Mainframe Tango: Save Network Node (UEF) 16": 21040215, "Mainframe Tango: Save 80% civilian buildings (optional) (UEF) 1": 21040300, "Mainframe Tango: Save 80% civilian buildings (optional) (UEF) 2": 21040301, "Mainframe Tango: Save 80% civilian buildings (optional) (UEF) 3": 21040302, "Mainframe Tango: Save 80% civilian buildings (optional) (UEF) 4": 21040303, "Mainframe Tango: Save 80% civilian buildings (optional) (UEF) 5": 21040304, "Mainframe Tango: Save 80% civilian buildings (optional) (UEF) 6": 21040305, "Mainframe Tango: Save 80% civilian buildings (optional) (UEF) 7": 21040306, "Mainframe Tango: Save 80% civilian buildings (optional) (UEF) 8": 21040307, "Mainframe Tango: Save 80% civilian buildings (optional) (UEF) 9": 21040308, "Mainframe Tango: Save 80% civilian buildings (optional) (UEF) 10": 21040309, "Mainframe Tango: Save 80% civilian buildings (optional) (UEF) 11": 21040310, "Mainframe Tango: Save 80% civilian buildings (optional) (UEF) 12": 21040311, "Mainframe Tango: Save 80% civilian buildings (optional) (UEF) 13": 21040312, "Mainframe Tango: Save 80% civilian buildings (optional) (UEF) 14": 21040313, "Mainframe Tango: Save 80% civilian buildings (optional) (UEF) 15": 21040314, "Mainframe Tango: Save 80% civilian buildings (optional) (UEF) 16": 21040315, "Mainframe Tango: Survive attacks (UEF) 1": 21040400, "Mainframe Tango: Survive attacks (UEF) 2": 21040401, "Mainframe Tango: Survive attacks (UEF) 3": 21040402, "Mainframe Tango: Survive attacks (UEF) 4": 21040403, "Mainframe Tango: Survive attacks (UEF) 5": 21040404, "Mainframe Tango: Survive attacks (UEF) 6": 21040405, "Mainframe Tango: Survive attacks (UEF) 7": 21040406, "Mainframe Tango: Survive attacks (UEF) 8": 21040407, "Mainframe Tango: Survive attacks (UEF) 9": 21040408, "Mainframe Tango: Survive attacks (UEF) 10": 21040409, "Mainframe Tango: Survive attacks (UEF) 11": 21040410, "Mainframe Tango: Survive attacks (UEF) 12": 21040411, "Mainframe Tango: Survive attacks (UEF) 13": 21040412, "Mainframe Tango: Survive attacks (UEF) 14": 21040413, "Mainframe Tango: Survive attacks (UEF) 15": 21040414, "Mainframe Tango: Survive attacks (UEF) 16": 21040415, "Mainframe Tango: Capture northeast node (UEF) 1": 21040500, "Mainframe Tango: Capture northeast node (UEF) 2": 21040501, "Mainframe Tango: Capture northeast node (UEF) 3": 21040502, "Mainframe Tango: Capture northeast node (UEF) 4": 21040503, "Mainframe Tango: Capture northeast node (UEF) 5": 21040504, "Mainframe Tango: Capture northeast node (UEF) 6": 21040505, "Mainframe Tango: Capture northeast node (UEF) 7": 21040506, "Mainframe Tango: Capture northeast node (UEF) 8": 21040507, "Mainframe Tango: Capture northeast node (UEF) 9": 21040508, "Mainframe Tango: Capture northeast node (UEF) 10": 21040509, "Mainframe Tango: Capture northeast node (UEF) 11": 21040510, "Mainframe Tango: Capture northeast node (UEF) 12": 21040511, "Mainframe Tango: Capture northeast node (UEF) 13": 21040512, "Mainframe Tango: Capture northeast node (UEF) 14": 21040513, "Mainframe Tango: Capture northeast node (UEF) 15": 21040514, "Mainframe Tango: Capture northeast node (UEF) 16": 21040515, "Mainframe Tango: Capture northwest node (UEF) 1": 21040600, "Mainframe Tango: Capture northwest node (UEF) 2": 21040601, "Mainframe Tango: Capture northwest node (UEF) 3": 21040602, "Mainframe Tango: Capture northwest node (UEF) 4": 21040603, "Mainframe Tango: Capture northwest node (UEF) 5": 21040604, "Mainframe Tango: Capture northwest node (UEF) 6": 21040605, "Mainframe Tango: Capture northwest node (UEF) 7": 21040606, "Mainframe Tango: Capture northwest node (UEF) 8": 21040607, "Mainframe Tango: Capture northwest node (UEF) 9": 21040608, "Mainframe Tango: Capture northwest node (UEF) 10": 21040609, "Mainframe Tango: Capture northwest node (UEF) 11": 21040610, "Mainframe Tango: Capture northwest node (UEF) 12": 21040611, "Mainframe Tango: Capture northwest node (UEF) 13": 21040612, "Mainframe Tango: Capture northwest node (UEF) 14": 21040613, "Mainframe Tango: Capture northwest node (UEF) 15": 21040614, "Mainframe Tango: Capture northwest node (UEF) 16": 21040615, "Mainframe Tango: Do not attack main Aeon base (UEF) 1": 21040700, "Mainframe Tango: Do not attack main Aeon base (UEF) 2": 21040701, "Mainframe Tango: Do not attack main Aeon base (UEF) 3": 21040702, "Mainframe Tango: Do not attack main Aeon base (UEF) 4": 21040703, "Mainframe Tango: Do not attack main Aeon base (UEF) 5": 21040704, "Mainframe Tango: Do not attack main Aeon base (UEF) 6": 21040705, "Mainframe Tango: Do not attack main Aeon base (UEF) 7": 21040706, "Mainframe Tango: Do not attack main Aeon base (UEF) 8": 21040707, "Mainframe Tango: Do not attack main Aeon base (UEF) 9": 21040708, "Mainframe Tango: Do not attack main Aeon base (UEF) 10": 21040709, "Mainframe Tango: Do not attack main Aeon base (UEF) 11": 21040710, "Mainframe Tango: Do not attack main Aeon base (UEF) 12": 21040711, "Mainframe Tango: Do not attack main Aeon base (UEF) 13": 21040712, "Mainframe Tango: Do not attack main Aeon base (UEF) 14": 21040713, "Mainframe Tango: Do not attack main Aeon base (UEF) 15": 21040714, "Mainframe Tango: Do not attack main Aeon base (UEF) 16": 21040715, "Mainframe Tango: Kill Aeon Commander (UEF) 1": 21040800, "Mainframe Tango: Kill Aeon Commander (UEF) 2": 21040801, "Mainframe Tango: Kill Aeon Commander (UEF) 3": 21040802, "Mainframe Tango: Kill Aeon Commander (UEF) 4": 21040803, "Mainframe Tango: Kill Aeon Commander (UEF) 5": 21040804, "Mainframe Tango: Kill Aeon Commander (UEF) 6": 21040805, "Mainframe Tango: Kill Aeon Commander (UEF) 7": 21040806, "Mainframe Tango: Kill Aeon Commander (UEF) 8": 21040807, "Mainframe Tango: Kill Aeon Commander (UEF) 9": 21040808, "Mainframe Tango: Kill Aeon Commander (UEF) 10": 21040809, "Mainframe Tango: Kill Aeon Commander (UEF) 11": 21040810, "Mainframe Tango: Kill Aeon Commander (UEF) 12": 21040811, "Mainframe Tango: Kill Aeon Commander (UEF) 13": 21040812, "Mainframe Tango: Kill Aeon Commander (UEF) 14": 21040813, "Mainframe Tango: Kill Aeon Commander (UEF) 15": 21040814, "Mainframe Tango: Kill Aeon Commander (UEF) 16": 21040815, "Unlock: Destroy UEF generators (UEF) 1": 21050000, "Unlock: Destroy UEF generators (UEF) 2": 21050001, "Unlock: Destroy UEF generators (UEF) 3": 21050002, "Unlock: Destroy UEF generators (UEF) 4": 21050003, "Unlock: Destroy UEF generators (UEF) 5": 21050004, "Unlock: Destroy UEF generators (UEF) 6": 21050005, "Unlock: Destroy UEF generators (UEF) 7": 21050006, "Unlock: Destroy UEF generators (UEF) 8": 21050007, "Unlock: Destroy UEF generators (UEF) 9": 21050008, "Unlock: Destroy UEF generators (UEF) 10": 21050009, "Unlock: Destroy UEF generators (UEF) 11": 21050010, "Unlock: Destroy UEF generators (UEF) 12": 21050011, "Unlock: Destroy UEF generators (UEF) 13": 21050012, "Unlock: Destroy UEF generators (UEF) 14": 21050013, "Unlock: Destroy UEF generators (UEF) 15": 21050014, "Unlock: Destroy UEF generators (UEF) 16": 21050015, "Unlock: Destroy UEF shipyards (optional) (UEF) 1": 21050100, "Unlock: Destroy UEF shipyards (optional) (UEF) 2": 21050101, "Unlock: Destroy UEF shipyards (optional) (UEF) 3": 21050102, "Unlock: Destroy UEF shipyards (optional) (UEF) 4": 21050103, "Unlock: Destroy UEF shipyards (optional) (UEF) 5": 21050104, "Unlock: Destroy UEF shipyards (optional) (UEF) 6": 21050105, "Unlock: Destroy UEF shipyards (optional) (UEF) 7": 21050106, "Unlock: Destroy UEF shipyards (optional) (UEF) 8": 21050107, "Unlock: Destroy UEF shipyards (optional) (UEF) 9": 21050108, "Unlock: Destroy UEF shipyards (optional) (UEF) 10": 21050109, "Unlock: Destroy UEF shipyards (optional) (UEF) 11": 21050110, "Unlock: Destroy UEF shipyards (optional) (UEF) 12": 21050111, "Unlock: Destroy UEF shipyards (optional) (UEF) 13": 21050112, "Unlock: Destroy UEF shipyards (optional) (UEF) 14": 21050113, "Unlock: Destroy UEF shipyards (optional) (UEF) 15": 21050114, "Unlock: Destroy UEF shipyards (optional) (UEF) 16": 21050115, "Unlock: Destroy UEF radars (UEF) 1": 21050200, "Unlock: Destroy UEF radars (UEF) 2": 21050201, "Unlock: Destroy UEF radars (UEF) 3": 21050202, "Unlock: Destroy UEF radars (UEF) 4": 21050203, "Unlock: Destroy UEF radars (UEF) 5": 21050204, "Unlock: Destroy UEF radars (UEF) 6": 21050205, "Unlock: Destroy UEF radars (UEF) 7": 21050206, "Unlock: Destroy UEF radars (UEF) 8": 21050207, "Unlock: Destroy UEF radars (UEF) 9": 21050208, "Unlock: Destroy UEF radars (UEF) 10": 21050209, "Unlock: Destroy UEF radars (UEF) 11": 21050210, "Unlock: Destroy UEF radars (UEF) 12": 21050211, "Unlock: Destroy UEF radars (UEF) 13": 21050212, "Unlock: Destroy UEF radars (UEF) 14": 21050213, "Unlock: Destroy UEF radars (UEF) 15": 21050214, "Unlock: Destroy UEF radars (UEF) 16": 21050215, "Unlock: Go to Hex5 (UEF) 1": 21050300, "Unlock: Go to Hex5 (UEF) 2": 21050301, "Unlock: Go to Hex5 (UEF) 3": 21050302, "Unlock: Go to Hex5 (UEF) 4": 21050303, "Unlock: Go to Hex5 (UEF) 5": 21050304, "Unlock: Go to Hex5 (UEF) 6": 21050305, "Unlock: Go to Hex5 (UEF) 7": 21050306, "Unlock: Go to Hex5 (UEF) 8": 21050307, "Unlock: Go to Hex5 (UEF) 9": 21050308, "Unlock: Go to Hex5 (UEF) 10": 21050309, "Unlock: Go to Hex5 (UEF) 11": 21050310, "Unlock: Go to Hex5 (UEF) 12": 21050311, "Unlock: Go to Hex5 (UEF) 13": 21050312, "Unlock: Go to Hex5 (UEF) 14": 21050313, "Unlock: Go to Hex5 (UEF) 15": 21050314, "Unlock: Go to Hex5 (UEF) 16": 21050315, "Unlock: Defend from heavy gunships (UEF) 1": 21050400, "Unlock: Defend from heavy gunships (UEF) 2": 21050401, "Unlock: Defend from heavy gunships (UEF) 3": 21050402, "Unlock: Defend from heavy gunships (UEF) 4": 21050403, "Unlock: Defend from heavy gunships (UEF) 5": 21050404, "Unlock: Defend from heavy gunships (UEF) 6": 21050405, "Unlock: Defend from heavy gunships (UEF) 7": 21050406, "Unlock: Defend from heavy gunships (UEF) 8": 21050407, "Unlock: Defend from heavy gunships (UEF) 9": 21050408, "Unlock: Defend from heavy gunships (UEF) 10": 21050409, "Unlock: Defend from heavy gunships (UEF) 11": 21050410, "Unlock: Defend from heavy gunships (UEF) 12": 21050411, "Unlock: Defend from heavy gunships (UEF) 13": 21050412, "Unlock: Defend from heavy gunships (UEF) 14": 21050413, "Unlock: Defend from heavy gunships (UEF) 15": 21050414, "Unlock: Defend from heavy gunships (UEF) 16": 21050415, "Unlock: Infect UEF landing pad (optional) (UEF) 1": 21050500, "Unlock: Infect UEF landing pad (optional) (UEF) 2": 21050501, "Unlock: Infect UEF landing pad (optional) (UEF) 3": 21050502, "Unlock: Infect UEF landing pad (optional) (UEF) 4": 21050503, "Unlock: Infect UEF landing pad (optional) (UEF) 5": 21050504, "Unlock: Infect UEF landing pad (optional) (UEF) 6": 21050505, "Unlock: Infect UEF landing pad (optional) (UEF) 7": 21050506, "Unlock: Infect UEF landing pad (optional) (UEF) 8": 21050507, "Unlock: Infect UEF landing pad (optional) (UEF) 9": 21050508, "Unlock: Infect UEF landing pad (optional) (UEF) 10": 21050509, "Unlock: Infect UEF landing pad (optional) (UEF) 11": 21050510, "Unlock: Infect UEF landing pad (optional) (UEF) 12": 21050511, "Unlock: Infect UEF landing pad (optional) (UEF) 13": 21050512, "Unlock: Infect UEF landing pad (optional) (UEF) 14": 21050513, "Unlock: Infect UEF landing pad (optional) (UEF) 15": 21050514, "Unlock: Infect UEF landing pad (optional) (UEF) 16": 21050515, "Unlock: This will be retconned later (UEF) 1": 21050600, "Unlock: This will be retconned later (UEF) 2": 21050601, "Unlock: This will be retconned later (UEF) 3": 21050602, "Unlock: This will be retconned later (UEF) 4": 21050603, "Unlock: This will be retconned later (UEF) 5": 21050604, "Unlock: This will be retconned later (UEF) 6": 21050605, "Unlock: This will be retconned later (UEF) 7": 21050606, "Unlock: This will be retconned later (UEF) 8": 21050607, "Unlock: This will be retconned later (UEF) 9": 21050608, "Unlock: This will be retconned later (UEF) 10": 21050609, "Unlock: This will be retconned later (UEF) 11": 21050610, "Unlock: This will be retconned later (UEF) 12": 21050611, "Unlock: This will be retconned later (UEF) 13": 21050612, "Unlock: This will be retconned later (UEF) 14": 21050613, "Unlock: This will be retconned later (UEF) 15": 21050614, "Unlock: This will be retconned later (UEF) 16": 21050615, "Unlock: Kill UEF Commander (UEF) 1": 21050700, "Unlock: Kill UEF Commander (UEF) 2": 21050701, "Unlock: Kill UEF Commander (UEF) 3": 21050702, "Unlock: Kill UEF Commander (UEF) 4": 21050703, "Unlock: Kill UEF Commander (UEF) 5": 21050704, "Unlock: Kill UEF Commander (UEF) 6": 21050705, "Unlock: Kill UEF Commander (UEF) 7": 21050706, "Unlock: Kill UEF Commander (UEF) 8": 21050707, "Unlock: Kill UEF Commander (UEF) 9": 21050708, "Unlock: Kill UEF Commander (UEF) 10": 21050709, "Unlock: Kill UEF Commander (UEF) 11": 21050710, "Unlock: Kill UEF Commander (UEF) 12": 21050711, "Unlock: Kill UEF Commander (UEF) 13": 21050712, "Unlock: Kill UEF Commander (UEF) 14": 21050713, "Unlock: Kill UEF Commander (UEF) 15": 21050714, "Unlock: Kill UEF Commander (UEF) 16": 21050715, "Freedom: Destroy CZAR (UEF) 1": 21060000, "Freedom: Destroy CZAR (UEF) 2": 21060001, "Freedom: Destroy CZAR (UEF) 3": 21060002, "Freedom: Destroy CZAR (UEF) 4": 21060003, "Freedom: Destroy CZAR (UEF) 5": 21060004, "Freedom: Destroy CZAR (UEF) 6": 21060005, "Freedom: Destroy CZAR (UEF) 7": 21060006, "Freedom: Destroy CZAR (UEF) 8": 21060007, "Freedom: Destroy CZAR (UEF) 9": 21060008, "Freedom: Destroy CZAR (UEF) 10": 21060009, "Freedom: Destroy CZAR (UEF) 11": 21060010, "Freedom: Destroy CZAR (UEF) 12": 21060011, "Freedom: Destroy CZAR (UEF) 13": 21060012, "Freedom: Destroy CZAR (UEF) 14": 21060013, "Freedom: Destroy CZAR (UEF) 15": 21060014, "Freedom: Destroy CZAR (UEF) 16": 21060015, "Freedom: Build Quantum Gate (UEF) 1": 21060100, "Freedom: Build Quantum Gate (UEF) 2": 21060101, "Freedom: Build Quantum Gate (UEF) 3": 21060102, "Freedom: Build Quantum Gate (UEF) 4": 21060103, "Freedom: Build Quantum Gate (UEF) 5": 21060104, "Freedom: Build Quantum Gate (UEF) 6": 21060105, "Freedom: Build Quantum Gate (UEF) 7": 21060106, "Freedom: Build Quantum Gate (UEF) 8": 21060107, "Freedom: Build Quantum Gate (UEF) 9": 21060108, "Freedom: Build Quantum Gate (UEF) 10": 21060109, "Freedom: Build Quantum Gate (UEF) 11": 21060110, "Freedom: Build Quantum Gate (UEF) 12": 21060111, "Freedom: Build Quantum Gate (UEF) 13": 21060112, "Freedom: Build Quantum Gate (UEF) 14": 21060113, "Freedom: Build Quantum Gate (UEF) 15": 21060114, "Freedom: Build Quantum Gate (UEF) 16": 21060115, "Freedom: Download Quantum Virus (UEF) 1": 21060200, "Freedom: Download Quantum Virus (UEF) 2": 21060201, "Freedom: Download Quantum Virus (UEF) 3": 21060202, "Freedom: Download Quantum Virus (UEF) 4": 21060203, "Freedom: Download Quantum Virus (UEF) 5": 21060204, "Freedom: Download Quantum Virus (UEF) 6": 21060205, "Freedom: Download Quantum Virus (UEF) 7": 21060206, "Freedom: Download Quantum Virus (UEF) 8": 21060207, "Freedom: Download Quantum Virus (UEF) 9": 21060208, "Freedom: Download Quantum Virus (UEF) 10": 21060209, "Freedom: Download Quantum Virus (UEF) 11": 21060210, "Freedom: Download Quantum Virus (UEF) 12": 21060211, "Freedom: Download Quantum Virus (UEF) 13": 21060212, "Freedom: Download Quantum Virus (UEF) 14": 21060213, "Freedom: Download Quantum Virus (UEF) 15": 21060214, "Freedom: Download Quantum Virus (UEF) 16": 21060215, "Freedom: Capture Black Sun control center (UEF) 1": 21060300, "Freedom: Capture Black Sun control center (UEF) 2": 21060301, "Freedom: Capture Black Sun control center (UEF) 3": 21060302, "Freedom: Capture Black Sun control center (UEF) 4": 21060303, "Freedom: Capture Black Sun control center (UEF) 5": 21060304, "Freedom: Capture Black Sun control center (UEF) 6": 21060305, "Freedom: Capture Black Sun control center (UEF) 7": 21060306, "Freedom: Capture Black Sun control center (UEF) 8": 21060307, "Freedom: Capture Black Sun control center (UEF) 9": 21060308, "Freedom: Capture Black Sun control center (UEF) 10": 21060309, "Freedom: Capture Black Sun control center (UEF) 11": 21060310, "Freedom: Capture Black Sun control center (UEF) 12": 21060311, "Freedom: Capture Black Sun control center (UEF) 13": 21060312, "Freedom: Capture Black Sun control center (UEF) 14": 21060313, "Freedom: Capture Black Sun control center (UEF) 15": 21060314, "Freedom: Capture Black Sun control center (UEF) 16": 21060315, "Freedom: Capture Black Sun (UEF) 1": 21060400, "Freedom: Capture Black Sun (UEF) 2": 21060401, "Freedom: Capture Black Sun (UEF) 3": 21060402, "Freedom: Capture Black Sun (UEF) 4": 21060403, "Freedom: Capture Black Sun (UEF) 5": 21060404, "Freedom: Capture Black Sun (UEF) 6": 21060405, "Freedom: Capture Black Sun (UEF) 7": 21060406, "Freedom: Capture Black Sun (UEF) 8": 21060407, "Freedom: Capture Black Sun (UEF) 9": 21060408, "Freedom: Capture Black Sun (UEF) 10": 21060409, "Freedom: Capture Black Sun (UEF) 11": 21060410, "Freedom: Capture Black Sun (UEF) 12": 21060411, "Freedom: Capture Black Sun (UEF) 13": 21060412, "Freedom: Capture Black Sun (UEF) 14": 21060413, "Freedom: Capture Black Sun (UEF) 15": 21060414, "Freedom: Capture Black Sun (UEF) 16": 21060415, "Freedom: Shoot Black Sun (UEF) 1": 21060500, "Freedom: Shoot Black Sun (UEF) 2": 21060501, "Freedom: Shoot Black Sun (UEF) 3": 21060502, "Freedom: Shoot Black Sun (UEF) 4": 21060503, "Freedom: Shoot Black Sun (UEF) 5": 21060504, "Freedom: Shoot Black Sun (UEF) 6": 21060505, "Freedom: Shoot Black Sun (UEF) 7": 21060506, "Freedom: Shoot Black Sun (UEF) 8": 21060507, "Freedom: Shoot Black Sun (UEF) 9": 21060508, "Freedom: Shoot Black Sun (UEF) 10": 21060509, "Freedom: Shoot Black Sun (UEF) 11": 21060510, "Freedom: Shoot Black Sun (UEF) 12": 21060511, "Freedom: Shoot Black Sun (UEF) 13": 21060512, "Freedom: Shoot Black Sun (UEF) 14": 21060513, "Freedom: Shoot Black Sun (UEF) 15": 21060514, "Freedom: Shoot Black Sun (UEF) 16": 21060515, "Liberation: Build mass (Cybran) 1": 22010000, "Liberation: Build mass (Cybran) 2": 22010001, "Liberation: Build mass (Cybran) 3": 22010002, "Liberation: Build mass (Cybran) 4": 22010003, "Liberation: Build mass (Cybran) 5": 22010004, "Liberation: Build mass (Cybran) 6": 22010005, "Liberation: Build mass (Cybran) 7": 22010006, "Liberation: Build mass (Cybran) 8": 22010007, "Liberation: Build mass (Cybran) 9": 22010008, "Liberation: Build mass (Cybran) 10": 22010009, "Liberation: Build mass (Cybran) 11": 22010010, "Liberation: Build mass (Cybran) 12": 22010011, "Liberation: Build mass (Cybran) 13": 22010012, "Liberation: Build mass (Cybran) 14": 22010013, "Liberation: Build mass (Cybran) 15": 22010014, "Liberation: Build mass (Cybran) 16": 22010015, "Liberation: Build power (Cybran) 1": 22010100, "Liberation: Build power (Cybran) 2": 22010101, "Liberation: Build power (Cybran) 3": 22010102, "Liberation: Build power (Cybran) 4": 22010103, "Liberation: Build power (Cybran) 5": 22010104, "Liberation: Build power (Cybran) 6": 22010105, "Liberation: Build power (Cybran) 7": 22010106, "Liberation: Build power (Cybran) 8": 22010107, "Liberation: Build power (Cybran) 9": 22010108, "Liberation: Build power (Cybran) 10": 22010109, "Liberation: Build power (Cybran) 11": 22010110, "Liberation: Build power (Cybran) 12": 22010111, "Liberation: Build power (Cybran) 13": 22010112, "Liberation: Build power (Cybran) 14": 22010113, "Liberation: Build power (Cybran) 15": 22010114, "Liberation: Build power (Cybran) 16": 22010115, "Liberation: Build air factory (Cybran) 1": 22010200, "Liberation: Build air factory (Cybran) 2": 22010201, "Liberation: Build air factory (Cybran) 3": 22010202, "Liberation: Build air factory (Cybran) 4": 22010203, "Liberation: Build air factory (Cybran) 5": 22010204, "Liberation: Build air factory (Cybran) 6": 22010205, "Liberation: Build air factory (Cybran) 7": 22010206, "Liberation: Build air factory (Cybran) 8": 22010207, "Liberation: Build air factory (Cybran) 9": 22010208, "Liberation: Build air factory (Cybran) 10": 22010209, "Liberation: Build air factory (Cybran) 11": 22010210, "Liberation: Build air factory (Cybran) 12": 22010211, "Liberation: Build air factory (Cybran) 13": 22010212, "Liberation: Build air factory (Cybran) 14": 22010213, "Liberation: Build air factory (Cybran) 15": 22010214, "Liberation: Build air factory (Cybran) 16": 22010215, "Liberation: Build bombers (Cybran) 1": 22010300, "Liberation: Build bombers (Cybran) 2": 22010301, "Liberation: Build bombers (Cybran) 3": 22010302, "Liberation: Build bombers (Cybran) 4": 22010303, "Liberation: Build bombers (Cybran) 5": 22010304, "Liberation: Build bombers (Cybran) 6": 22010305, "Liberation: Build bombers (Cybran) 7": 22010306, "Liberation: Build bombers (Cybran) 8": 22010307, "Liberation: Build bombers (Cybran) 9": 22010308, "Liberation: Build bombers (Cybran) 10": 22010309, "Liberation: Build bombers (Cybran) 11": 22010310, "Liberation: Build bombers (Cybran) 12": 22010311, "Liberation: Build bombers (Cybran) 13": 22010312, "Liberation: Build bombers (Cybran) 14": 22010313, "Liberation: Build bombers (Cybran) 15": 22010314, "Liberation: Build bombers (Cybran) 16": 22010315, "Liberation: Destroy radar defenders (Cybran) 1": 22010400, "Liberation: Destroy radar defenders (Cybran) 2": 22010401, "Liberation: Destroy radar defenders (Cybran) 3": 22010402, "Liberation: Destroy radar defenders (Cybran) 4": 22010403, "Liberation: Destroy radar defenders (Cybran) 5": 22010404, "Liberation: Destroy radar defenders (Cybran) 6": 22010405, "Liberation: Destroy radar defenders (Cybran) 7": 22010406, "Liberation: Destroy radar defenders (Cybran) 8": 22010407, "Liberation: Destroy radar defenders (Cybran) 9": 22010408, "Liberation: Destroy radar defenders (Cybran) 10": 22010409, "Liberation: Destroy radar defenders (Cybran) 11": 22010410, "Liberation: Destroy radar defenders (Cybran) 12": 22010411, "Liberation: Destroy radar defenders (Cybran) 13": 22010412, "Liberation: Destroy radar defenders (Cybran) 14": 22010413, "Liberation: Destroy radar defenders (Cybran) 15": 22010414, "Liberation: Destroy radar defenders (Cybran) 16": 22010415, "Liberation: Capture radars (Cybran) 1": 22010500, "Liberation: Capture radars (Cybran) 2": 22010501, "Liberation: Capture radars (Cybran) 3": 22010502, "Liberation: Capture radars (Cybran) 4": 22010503, "Liberation: Capture radars (Cybran) 5": 22010504, "Liberation: Capture radars (Cybran) 6": 22010505, "Liberation: Capture radars (Cybran) 7": 22010506, "Liberation: Capture radars (Cybran) 8": 22010507, "Liberation: Capture radars (Cybran) 9": 22010508, "Liberation: Capture radars (Cybran) 10": 22010509, "Liberation: Capture radars (Cybran) 11": 22010510, "Liberation: Capture radars (Cybran) 12": 22010511, "Liberation: Capture radars (Cybran) 13": 22010512, "Liberation: Capture radars (Cybran) 14": 22010513, "Liberation: Capture radars (Cybran) 15": 22010514, "Liberation: Capture radars (Cybran) 16": 22010515, "Liberation: Destroy mex (Cybran) 1": 22010600, "Liberation: Destroy mex (Cybran) 2": 22010601, "Liberation: Destroy mex (Cybran) 3": 22010602, "Liberation: Destroy mex (Cybran) 4": 22010603, "Liberation: Destroy mex (Cybran) 5": 22010604, "Liberation: Destroy mex (Cybran) 6": 22010605, "Liberation: Destroy mex (Cybran) 7": 22010606, "Liberation: Destroy mex (Cybran) 8": 22010607, "Liberation: Destroy mex (Cybran) 9": 22010608, "Liberation: Destroy mex (Cybran) 10": 22010609, "Liberation: Destroy mex (Cybran) 11": 22010610, "Liberation: Destroy mex (Cybran) 12": 22010611, "Liberation: Destroy mex (Cybran) 13": 22010612, "Liberation: Destroy mex (Cybran) 14": 22010613, "Liberation: Destroy mex (Cybran) 15": 22010614, "Liberation: Destroy mex (Cybran) 16": 22010615, "Liberation: Destroy UEF defences (Cybran) 1": 22010700, "Liberation: Destroy UEF defences (Cybran) 2": 22010701, "Liberation: Destroy UEF defences (Cybran) 3": 22010702, "Liberation: Destroy UEF defences (Cybran) 4": 22010703, "Liberation: Destroy UEF defences (Cybran) 5": 22010704, "Liberation: Destroy UEF defences (Cybran) 6": 22010705, "Liberation: Destroy UEF defences (Cybran) 7": 22010706, "Liberation: Destroy UEF defences (Cybran) 8": 22010707, "Liberation: Destroy UEF defences (Cybran) 9": 22010708, "Liberation: Destroy UEF defences (Cybran) 10": 22010709, "Liberation: Destroy UEF defences (Cybran) 11": 22010710, "Liberation: Destroy UEF defences (Cybran) 12": 22010711, "Liberation: Destroy UEF defences (Cybran) 13": 22010712, "Liberation: Destroy UEF defences (Cybran) 14": 22010713, "Liberation: Destroy UEF defences (Cybran) 15": 22010714, "Liberation: Destroy UEF defences (Cybran) 16": 22010715, "Liberation: Destroy UEF patrols (Cybran) 1": 22010800, "Liberation: Destroy UEF patrols (Cybran) 2": 22010801, "Liberation: Destroy UEF patrols (Cybran) 3": 22010802, "Liberation: Destroy UEF patrols (Cybran) 4": 22010803, "Liberation: Destroy UEF patrols (Cybran) 5": 22010804, "Liberation: Destroy UEF patrols (Cybran) 6": 22010805, "Liberation: Destroy UEF patrols (Cybran) 7": 22010806, "Liberation: Destroy UEF patrols (Cybran) 8": 22010807, "Liberation: Destroy UEF patrols (Cybran) 9": 22010808, "Liberation: Destroy UEF patrols (Cybran) 10": 22010809, "Liberation: Destroy UEF patrols (Cybran) 11": 22010810, "Liberation: Destroy UEF patrols (Cybran) 12": 22010811, "Liberation: Destroy UEF patrols (Cybran) 13": 22010812, "Liberation: Destroy UEF patrols (Cybran) 14": 22010813, "Liberation: Destroy UEF patrols (Cybran) 15": 22010814, "Liberation: Destroy UEF patrols (Cybran) 16": 22010815, "Liberation: Destroy UEF base defenders (Cybran) 1": 22010900, "Liberation: Destroy UEF base defenders (Cybran) 2": 22010901, "Liberation: Destroy UEF base defenders (Cybran) 3": 22010902, "Liberation: Destroy UEF base defenders (Cybran) 4": 22010903, "Liberation: Destroy UEF base defenders (Cybran) 5": 22010904, "Liberation: Destroy UEF base defenders (Cybran) 6": 22010905, "Liberation: Destroy UEF base defenders (Cybran) 7": 22010906, "Liberation: Destroy UEF base defenders (Cybran) 8": 22010907, "Liberation: Destroy UEF base defenders (Cybran) 9": 22010908, "Liberation: Destroy UEF base defenders (Cybran) 10": 22010909, "Liberation: Destroy UEF base defenders (Cybran) 11": 22010910, "Liberation: Destroy UEF base defenders (Cybran) 12": 22010911, "Liberation: Destroy UEF base defenders (Cybran) 13": 22010912, "Liberation: Destroy UEF base defenders (Cybran) 14": 22010913, "Liberation: Destroy UEF base defenders (Cybran) 15": 22010914, "Liberation: Destroy UEF base defenders (Cybran) 16": 22010915, "Liberation: Destroy UEF base (Cybran) 1": 22011000, "Liberation: Destroy UEF base (Cybran) 2": 22011001, "Liberation: Destroy UEF base (Cybran) 3": 22011002, "Liberation: Destroy UEF base (Cybran) 4": 22011003, "Liberation: Destroy UEF base (Cybran) 5": 22011004, "Liberation: Destroy UEF base (Cybran) 6": 22011005, "Liberation: Destroy UEF base (Cybran) 7": 22011006, "Liberation: Destroy UEF base (Cybran) 8": 22011007, "Liberation: Destroy UEF base (Cybran) 9": 22011008, "Liberation: Destroy UEF base (Cybran) 10": 22011009, "Liberation: Destroy UEF base (Cybran) 11": 22011010, "Liberation: Destroy UEF base (Cybran) 12": 22011011, "Liberation: Destroy UEF base (Cybran) 13": 22011012, "Liberation: Destroy UEF base (Cybran) 14": 22011013, "Liberation: Destroy UEF base (Cybran) 15": 22011014, "Liberation: Destroy UEF base (Cybran) 16": 22011015, "Liberation: Kill Aeon Commander (Cybran) 1": 22011100, "Liberation: Kill Aeon Commander (Cybran) 2": 22011101, "Liberation: Kill Aeon Commander (Cybran) 3": 22011102, "Liberation: Kill Aeon Commander (Cybran) 4": 22011103, "Liberation: Kill Aeon Commander (Cybran) 5": 22011104, "Liberation: Kill Aeon Commander (Cybran) 6": 22011105, "Liberation: Kill Aeon Commander (Cybran) 7": 22011106, "Liberation: Kill Aeon Commander (Cybran) 8": 22011107, "Liberation: Kill Aeon Commander (Cybran) 9": 22011108, "Liberation: Kill Aeon Commander (Cybran) 10": 22011109, "Liberation: Kill Aeon Commander (Cybran) 11": 22011110, "Liberation: Kill Aeon Commander (Cybran) 12": 22011111, "Liberation: Kill Aeon Commander (Cybran) 13": 22011112, "Liberation: Kill Aeon Commander (Cybran) 14": 22011113, "Liberation: Kill Aeon Commander (Cybran) 15": 22011114, "Liberation: Kill Aeon Commander (Cybran) 16": 22011115, "Artifact: Destroy first village defenders (Cybran) 1": 22020000, "Artifact: Destroy first village defenders (Cybran) 2": 22020001, "Artifact: Destroy first village defenders (Cybran) 3": 22020002, "Artifact: Destroy first village defenders (Cybran) 4": 22020003, "Artifact: Destroy first village defenders (Cybran) 5": 22020004, "Artifact: Destroy first village defenders (Cybran) 6": 22020005, "Artifact: Destroy first village defenders (Cybran) 7": 22020006, "Artifact: Destroy first village defenders (Cybran) 8": 22020007, "Artifact: Destroy first village defenders (Cybran) 9": 22020008, "Artifact: Destroy first village defenders (Cybran) 10": 22020009, "Artifact: Destroy first village defenders (Cybran) 11": 22020010, "Artifact: Destroy first village defenders (Cybran) 12": 22020011, "Artifact: Destroy first village defenders (Cybran) 13": 22020012, "Artifact: Destroy first village defenders (Cybran) 14": 22020013, "Artifact: Destroy first village defenders (Cybran) 15": 22020014, "Artifact: Destroy first village defenders (Cybran) 16": 22020015, "Artifact: Destroy first temple (Cybran) 1": 22020100, "Artifact: Destroy first temple (Cybran) 2": 22020101, "Artifact: Destroy first temple (Cybran) 3": 22020102, "Artifact: Destroy first temple (Cybran) 4": 22020103, "Artifact: Destroy first temple (Cybran) 5": 22020104, "Artifact: Destroy first temple (Cybran) 6": 22020105, "Artifact: Destroy first temple (Cybran) 7": 22020106, "Artifact: Destroy first temple (Cybran) 8": 22020107, "Artifact: Destroy first temple (Cybran) 9": 22020108, "Artifact: Destroy first temple (Cybran) 10": 22020109, "Artifact: Destroy first temple (Cybran) 11": 22020110, "Artifact: Destroy first temple (Cybran) 12": 22020111, "Artifact: Destroy first temple (Cybran) 13": 22020112, "Artifact: Destroy first temple (Cybran) 14": 22020113, "Artifact: Destroy first temple (Cybran) 15": 22020114, "Artifact: Destroy first temple (Cybran) 16": 22020115, "Artifact: Protect first artifact (Cybran) 1": 22020200, "Artifact: Protect first artifact (Cybran) 2": 22020201, "Artifact: Protect first artifact (Cybran) 3": 22020202, "Artifact: Protect first artifact (Cybran) 4": 22020203, "Artifact: Protect first artifact (Cybran) 5": 22020204, "Artifact: Protect first artifact (Cybran) 6": 22020205, "Artifact: Protect first artifact (Cybran) 7": 22020206, "Artifact: Protect first artifact (Cybran) 8": 22020207, "Artifact: Protect first artifact (Cybran) 9": 22020208, "Artifact: Protect first artifact (Cybran) 10": 22020209, "Artifact: Protect first artifact (Cybran) 11": 22020210, "Artifact: Protect first artifact (Cybran) 12": 22020211, "Artifact: Protect first artifact (Cybran) 13": 22020212, "Artifact: Protect first artifact (Cybran) 14": 22020213, "Artifact: Protect first artifact (Cybran) 15": 22020214, "Artifact: Protect first artifact (Cybran) 16": 22020215, "Artifact: Find second artifact (Cybran) 1": 22020300, "Artifact: Find second artifact (Cybran) 2": 22020301, "Artifact: Find second artifact (Cybran) 3": 22020302, "Artifact: Find second artifact (Cybran) 4": 22020303, "Artifact: Find second artifact (Cybran) 5": 22020304, "Artifact: Find second artifact (Cybran) 6": 22020305, "Artifact: Find second artifact (Cybran) 7": 22020306, "Artifact: Find second artifact (Cybran) 8": 22020307, "Artifact: Find second artifact (Cybran) 9": 22020308, "Artifact: Find second artifact (Cybran) 10": 22020309, "Artifact: Find second artifact (Cybran) 11": 22020310, "Artifact: Find second artifact (Cybran) 12": 22020311, "Artifact: Find second artifact (Cybran) 13": 22020312, "Artifact: Find second artifact (Cybran) 14": 22020313, "Artifact: Find second artifact (Cybran) 15": 22020314, "Artifact: Find second artifact (Cybran) 16": 22020315, "Artifact: Destroy Aeon reinforcements (Cybran) 1": 22020400, "Artifact: Destroy Aeon reinforcements (Cybran) 2": 22020401, "Artifact: Destroy Aeon reinforcements (Cybran) 3": 22020402, "Artifact: Destroy Aeon reinforcements (Cybran) 4": 22020403, "Artifact: Destroy Aeon reinforcements (Cybran) 5": 22020404, "Artifact: Destroy Aeon reinforcements (Cybran) 6": 22020405, "Artifact: Destroy Aeon reinforcements (Cybran) 7": 22020406, "Artifact: Destroy Aeon reinforcements (Cybran) 8": 22020407, "Artifact: Destroy Aeon reinforcements (Cybran) 9": 22020408, "Artifact: Destroy Aeon reinforcements (Cybran) 10": 22020409, "Artifact: Destroy Aeon reinforcements (Cybran) 11": 22020410, "Artifact: Destroy Aeon reinforcements (Cybran) 12": 22020411, "Artifact: Destroy Aeon reinforcements (Cybran) 13": 22020412, "Artifact: Destroy Aeon reinforcements (Cybran) 14": 22020413, "Artifact: Destroy Aeon reinforcements (Cybran) 15": 22020414, "Artifact: Destroy Aeon reinforcements (Cybran) 16": 22020415, "Artifact: Protect second artifact (Cybran) 1": 22020500, "Artifact: Protect second artifact (Cybran) 2": 22020501, "Artifact: Protect second artifact (Cybran) 3": 22020502, "Artifact: Protect second artifact (Cybran) 4": 22020503, "Artifact: Protect second artifact (Cybran) 5": 22020504, "Artifact: Protect second artifact (Cybran) 6": 22020505, "Artifact: Protect second artifact (Cybran) 7": 22020506, "Artifact: Protect second artifact (Cybran) 8": 22020507, "Artifact: Protect second artifact (Cybran) 9": 22020508, "Artifact: Protect second artifact (Cybran) 10": 22020509, "Artifact: Protect second artifact (Cybran) 11": 22020510, "Artifact: Protect second artifact (Cybran) 12": 22020511, "Artifact: Protect second artifact (Cybran) 13": 22020512, "Artifact: Protect second artifact (Cybran) 14": 22020513, "Artifact: Protect second artifact (Cybran) 15": 22020514, "Artifact: Protect second artifact (Cybran) 16": 22020515, "Artifact: Defend from Aeon attack (Cybran) 1": 22020600, "Artifact: Defend from Aeon attack (Cybran) 2": 22020601, "Artifact: Defend from Aeon attack (Cybran) 3": 22020602, "Artifact: Defend from Aeon attack (Cybran) 4": 22020603, "Artifact: Defend from Aeon attack (Cybran) 5": 22020604, "Artifact: Defend from Aeon attack (Cybran) 6": 22020605, "Artifact: Defend from Aeon attack (Cybran) 7": 22020606, "Artifact: Defend from Aeon attack (Cybran) 8": 22020607, "Artifact: Defend from Aeon attack (Cybran) 9": 22020608, "Artifact: Defend from Aeon attack (Cybran) 10": 22020609, "Artifact: Defend from Aeon attack (Cybran) 11": 22020610, "Artifact: Defend from Aeon attack (Cybran) 12": 22020611, "Artifact: Defend from Aeon attack (Cybran) 13": 22020612, "Artifact: Defend from Aeon attack (Cybran) 14": 22020613, "Artifact: Defend from Aeon attack (Cybran) 15": 22020614, "Artifact: Defend from Aeon attack (Cybran) 16": 22020615, "Artifact: Destroy eastern base (Cybran) 1": 22020700, "Artifact: Destroy eastern base (Cybran) 2": 22020701, "Artifact: Destroy eastern base (Cybran) 3": 22020702, "Artifact: Destroy eastern base (Cybran) 4": 22020703, "Artifact: Destroy eastern base (Cybran) 5": 22020704, "Artifact: Destroy eastern base (Cybran) 6": 22020705, "Artifact: Destroy eastern base (Cybran) 7": 22020706, "Artifact: Destroy eastern base (Cybran) 8": 22020707, "Artifact: Destroy eastern base (Cybran) 9": 22020708, "Artifact: Destroy eastern base (Cybran) 10": 22020709, "Artifact: Destroy eastern base (Cybran) 11": 22020710, "Artifact: Destroy eastern base (Cybran) 12": 22020711, "Artifact: Destroy eastern base (Cybran) 13": 22020712, "Artifact: Destroy eastern base (Cybran) 14": 22020713, "Artifact: Destroy eastern base (Cybran) 15": 22020714, "Artifact: Destroy eastern base (Cybran) 16": 22020715, "Artifact: Destroy navy base (Cybran) 1": 22020800, "Artifact: Destroy navy base (Cybran) 2": 22020801, "Artifact: Destroy navy base (Cybran) 3": 22020802, "Artifact: Destroy navy base (Cybran) 4": 22020803, "Artifact: Destroy navy base (Cybran) 5": 22020804, "Artifact: Destroy navy base (Cybran) 6": 22020805, "Artifact: Destroy navy base (Cybran) 7": 22020806, "Artifact: Destroy navy base (Cybran) 8": 22020807, "Artifact: Destroy navy base (Cybran) 9": 22020808, "Artifact: Destroy navy base (Cybran) 10": 22020809, "Artifact: Destroy navy base (Cybran) 11": 22020810, "Artifact: Destroy navy base (Cybran) 12": 22020811, "Artifact: Destroy navy base (Cybran) 13": 22020812, "Artifact: Destroy navy base (Cybran) 14": 22020813, "Artifact: Destroy navy base (Cybran) 15": 22020814, "Artifact: Destroy navy base (Cybran) 16": 22020815, "Artifact: Protect third artifact (Cybran) 1": 22020900, "Artifact: Protect third artifact (Cybran) 2": 22020901, "Artifact: Protect third artifact (Cybran) 3": 22020902, "Artifact: Protect third artifact (Cybran) 4": 22020903, "Artifact: Protect third artifact (Cybran) 5": 22020904, "Artifact: Protect third artifact (Cybran) 6": 22020905, "Artifact: Protect third artifact (Cybran) 7": 22020906, "Artifact: Protect third artifact (Cybran) 8": 22020907, "Artifact: Protect third artifact (Cybran) 9": 22020908, "Artifact: Protect third artifact (Cybran) 10": 22020909, "Artifact: Protect third artifact (Cybran) 11": 22020910, "Artifact: Protect third artifact (Cybran) 12": 22020911, "Artifact: Protect third artifact (Cybran) 13": 22020912, "Artifact: Protect third artifact (Cybran) 14": 22020913, "Artifact: Protect third artifact (Cybran) 15": 22020914, "Artifact: Protect third artifact (Cybran) 16": 22020915, "Artifact: Kill Aeon Commander (optional) (Cybran) 1": 22021000, "Artifact: Kill Aeon Commander (optional) (Cybran) 2": 22021001, "Artifact: Kill Aeon Commander (optional) (Cybran) 3": 22021002, "Artifact: Kill Aeon Commander (optional) (Cybran) 4": 22021003, "Artifact: Kill Aeon Commander (optional) (Cybran) 5": 22021004, "Artifact: Kill Aeon Commander (optional) (Cybran) 6": 22021005, "Artifact: Kill Aeon Commander (optional) (Cybran) 7": 22021006, "Artifact: Kill Aeon Commander (optional) (Cybran) 8": 22021007, "Artifact: Kill Aeon Commander (optional) (Cybran) 9": 22021008, "Artifact: Kill Aeon Commander (optional) (Cybran) 10": 22021009, "Artifact: Kill Aeon Commander (optional) (Cybran) 11": 22021010, "Artifact: Kill Aeon Commander (optional) (Cybran) 12": 22021011, "Artifact: Kill Aeon Commander (optional) (Cybran) 13": 22021012, "Artifact: Kill Aeon Commander (optional) (Cybran) 14": 22021013, "Artifact: Kill Aeon Commander (optional) (Cybran) 15": 22021014, "Artifact: Kill Aeon Commander (optional) (Cybran) 16": 22021015, "Artifact: Kill Mach (Cybran) 1": 22021100, "Artifact: Kill Mach (Cybran) 2": 22021101, "Artifact: Kill Mach (Cybran) 3": 22021102, "Artifact: Kill Mach (Cybran) 4": 22021103, "Artifact: Kill Mach (Cybran) 5": 22021104, "Artifact: Kill Mach (Cybran) 6": 22021105, "Artifact: Kill Mach (Cybran) 7": 22021106, "Artifact: Kill Mach (Cybran) 8": 22021107, "Artifact: Kill Mach (Cybran) 9": 22021108, "Artifact: Kill Mach (Cybran) 10": 22021109, "Artifact: Kill Mach (Cybran) 11": 22021110, "Artifact: Kill Mach (Cybran) 12": 22021111, "Artifact: Kill Mach (Cybran) 13": 22021112, "Artifact: Kill Mach (Cybran) 14": 22021113, "Artifact: Kill Mach (Cybran) 15": 22021114, "Artifact: Kill Mach (Cybran) 16": 22021115, "Artifact: Go to Gate (Cybran) 1": 22021200, "Artifact: Go to Gate (Cybran) 2": 22021201, "Artifact: Go to Gate (Cybran) 3": 22021202, "Artifact: Go to Gate (Cybran) 4": 22021203, "Artifact: Go to Gate (Cybran) 5": 22021204, "Artifact: Go to Gate (Cybran) 6": 22021205, "Artifact: Go to Gate (Cybran) 7": 22021206, "Artifact: Go to Gate (Cybran) 8": 22021207, "Artifact: Go to Gate (Cybran) 9": 22021208, "Artifact: Go to Gate (Cybran) 10": 22021209, "Artifact: Go to Gate (Cybran) 11": 22021210, "Artifact: Go to Gate (Cybran) 12": 22021211, "Artifact: Go to Gate (Cybran) 13": 22021212, "Artifact: Go to Gate (Cybran) 14": 22021213, "Artifact: Go to Gate (Cybran) 15": 22021214, "Artifact: Go to Gate (Cybran) 16": 22021215, "Defrag: Protect York 18 (Cybran) 1": 22030000, "Defrag: Protect York 18 (Cybran) 2": 22030001, "Defrag: Protect York 18 (Cybran) 3": 22030002, "Defrag: Protect York 18 (Cybran) 4": 22030003, "Defrag: Protect York 18 (Cybran) 5": 22030004, "Defrag: Protect York 18 (Cybran) 6": 22030005, "Defrag: Protect York 18 (Cybran) 7": 22030006, "Defrag: Protect York 18 (Cybran) 8": 22030007, "Defrag: Protect York 18 (Cybran) 9": 22030008, "Defrag: Protect York 18 (Cybran) 10": 22030009, "Defrag: Protect York 18 (Cybran) 11": 22030010, "Defrag: Protect York 18 (Cybran) 12": 22030011, "Defrag: Protect York 18 (Cybran) 13": 22030012, "Defrag: Protect York 18 (Cybran) 14": 22030013, "Defrag: Protect York 18 (Cybran) 15": 22030014, "Defrag: Protect York 18 (Cybran) 16": 22030015, "Defrag: Destroy western UEF base (Cybran) 1": 22030100, "Defrag: Destroy western UEF base (Cybran) 2": 22030101, "Defrag: Destroy western UEF base (Cybran) 3": 22030102, "Defrag: Destroy western UEF base (Cybran) 4": 22030103, "Defrag: Destroy western UEF base (Cybran) 5": 22030104, "Defrag: Destroy western UEF base (Cybran) 6": 22030105, "Defrag: Destroy western UEF base (Cybran) 7": 22030106, "Defrag: Destroy western UEF base (Cybran) 8": 22030107, "Defrag: Destroy western UEF base (Cybran) 9": 22030108, "Defrag: Destroy western UEF base (Cybran) 10": 22030109, "Defrag: Destroy western UEF base (Cybran) 11": 22030110, "Defrag: Destroy western UEF base (Cybran) 12": 22030111, "Defrag: Destroy western UEF base (Cybran) 13": 22030112, "Defrag: Destroy western UEF base (Cybran) 14": 22030113, "Defrag: Destroy western UEF base (Cybran) 15": 22030114, "Defrag: Destroy western UEF base (Cybran) 16": 22030115, "Defrag: Destroy north-western UEF base (Cybran) 1": 22030200, "Defrag: Destroy north-western UEF base (Cybran) 2": 22030201, "Defrag: Destroy north-western UEF base (Cybran) 3": 22030202, "Defrag: Destroy north-western UEF base (Cybran) 4": 22030203, "Defrag: Destroy north-western UEF base (Cybran) 5": 22030204, "Defrag: Destroy north-western UEF base (Cybran) 6": 22030205, "Defrag: Destroy north-western UEF base (Cybran) 7": 22030206, "Defrag: Destroy north-western UEF base (Cybran) 8": 22030207, "Defrag: Destroy north-western UEF base (Cybran) 9": 22030208, "Defrag: Destroy north-western UEF base (Cybran) 10": 22030209, "Defrag: Destroy north-western UEF base (Cybran) 11": 22030210, "Defrag: Destroy north-western UEF base (Cybran) 12": 22030211, "Defrag: Destroy north-western UEF base (Cybran) 13": 22030212, "Defrag: Destroy north-western UEF base (Cybran) 14": 22030213, "Defrag: Destroy north-western UEF base (Cybran) 15": 22030214, "Defrag: Destroy north-western UEF base (Cybran) 16": 22030215, "Defrag: Destroy northern UEF base (Cybran) 1": 22030300, "Defrag: Destroy northern UEF base (Cybran) 2": 22030301, "Defrag: Destroy northern UEF base (Cybran) 3": 22030302, "Defrag: Destroy northern UEF base (Cybran) 4": 22030303, "Defrag: Destroy northern UEF base (Cybran) 5": 22030304, "Defrag: Destroy northern UEF base (Cybran) 6": 22030305, "Defrag: Destroy northern UEF base (Cybran) 7": 22030306, "Defrag: Destroy northern UEF base (Cybran) 8": 22030307, "Defrag: Destroy northern UEF base (Cybran) 9": 22030308, "Defrag: Destroy northern UEF base (Cybran) 10": 22030309, "Defrag: Destroy northern UEF base (Cybran) 11": 22030310, "Defrag: Destroy northern UEF base (Cybran) 12": 22030311, "Defrag: Destroy northern UEF base (Cybran) 13": 22030312, "Defrag: Destroy northern UEF base (Cybran) 14": 22030313, "Defrag: Destroy northern UEF base (Cybran) 15": 22030314, "Defrag: Destroy northern UEF base (Cybran) 16": 22030315, "Defrag: Sink UEF cruiser (Cybran) 1": 22030400, "Defrag: Sink UEF cruiser (Cybran) 2": 22030401, "Defrag: Sink UEF cruiser (Cybran) 3": 22030402, "Defrag: Sink UEF cruiser (Cybran) 4": 22030403, "Defrag: Sink UEF cruiser (Cybran) 5": 22030404, "Defrag: Sink UEF cruiser (Cybran) 6": 22030405, "Defrag: Sink UEF cruiser (Cybran) 7": 22030406, "Defrag: Sink UEF cruiser (Cybran) 8": 22030407, "Defrag: Sink UEF cruiser (Cybran) 9": 22030408, "Defrag: Sink UEF cruiser (Cybran) 10": 22030409, "Defrag: Sink UEF cruiser (Cybran) 11": 22030410, "Defrag: Sink UEF cruiser (Cybran) 12": 22030411, "Defrag: Sink UEF cruiser (Cybran) 13": 22030412, "Defrag: Sink UEF cruiser (Cybran) 14": 22030413, "Defrag: Sink UEF cruiser (Cybran) 15": 22030414, "Defrag: Sink UEF cruiser (Cybran) 16": 22030415, "Defrag: Destroy static artillery (Cybran) 1": 22030500, "Defrag: Destroy static artillery (Cybran) 2": 22030501, "Defrag: Destroy static artillery (Cybran) 3": 22030502, "Defrag: Destroy static artillery (Cybran) 4": 22030503, "Defrag: Destroy static artillery (Cybran) 5": 22030504, "Defrag: Destroy static artillery (Cybran) 6": 22030505, "Defrag: Destroy static artillery (Cybran) 7": 22030506, "Defrag: Destroy static artillery (Cybran) 8": 22030507, "Defrag: Destroy static artillery (Cybran) 9": 22030508, "Defrag: Destroy static artillery (Cybran) 10": 22030509, "Defrag: Destroy static artillery (Cybran) 11": 22030510, "Defrag: Destroy static artillery (Cybran) 12": 22030511, "Defrag: Destroy static artillery (Cybran) 13": 22030512, "Defrag: Destroy static artillery (Cybran) 14": 22030513, "Defrag: Destroy static artillery (Cybran) 15": 22030514, "Defrag: Destroy static artillery (Cybran) 16": 22030515, "Defrag: Escort trucks (Cybran) 1": 22030600, "Defrag: Escort trucks (Cybran) 2": 22030601, "Defrag: Escort trucks (Cybran) 3": 22030602, "Defrag: Escort trucks (Cybran) 4": 22030603, "Defrag: Escort trucks (Cybran) 5": 22030604, "Defrag: Escort trucks (Cybran) 6": 22030605, "Defrag: Escort trucks (Cybran) 7": 22030606, "Defrag: Escort trucks (Cybran) 8": 22030607, "Defrag: Escort trucks (Cybran) 9": 22030608, "Defrag: Escort trucks (Cybran) 10": 22030609, "Defrag: Escort trucks (Cybran) 11": 22030610, "Defrag: Escort trucks (Cybran) 12": 22030611, "Defrag: Escort trucks (Cybran) 13": 22030612, "Defrag: Escort trucks (Cybran) 14": 22030613, "Defrag: Escort trucks (Cybran) 15": 22030614, "Defrag: Escort trucks (Cybran) 16": 22030615, "Defrag: Escort ALL trucks (optional) (Cybran) 1": 22030700, "Defrag: Escort ALL trucks (optional) (Cybran) 2": 22030701, "Defrag: Escort ALL trucks (optional) (Cybran) 3": 22030702, "Defrag: Escort ALL trucks (optional) (Cybran) 4": 22030703, "Defrag: Escort ALL trucks (optional) (Cybran) 5": 22030704, "Defrag: Escort ALL trucks (optional) (Cybran) 6": 22030705, "Defrag: Escort ALL trucks (optional) (Cybran) 7": 22030706, "Defrag: Escort ALL trucks (optional) (Cybran) 8": 22030707, "Defrag: Escort ALL trucks (optional) (Cybran) 9": 22030708, "Defrag: Escort ALL trucks (optional) (Cybran) 10": 22030709, "Defrag: Escort ALL trucks (optional) (Cybran) 11": 22030710, "Defrag: Escort ALL trucks (optional) (Cybran) 12": 22030711, "Defrag: Escort ALL trucks (optional) (Cybran) 13": 22030712, "Defrag: Escort ALL trucks (optional) (Cybran) 14": 22030713, "Defrag: Escort ALL trucks (optional) (Cybran) 15": 22030714, "Defrag: Escort ALL trucks (optional) (Cybran) 16": 22030715, "Defrag: Optional objective  (optional) (Cybran) 1": 22030800, "Defrag: Optional objective  (optional) (Cybran) 2": 22030801, "Defrag: Optional objective  (optional) (Cybran) 3": 22030802, "Defrag: Optional objective  (optional) (Cybran) 4": 22030803, "Defrag: Optional objective  (optional) (Cybran) 5": 22030804, "Defrag: Optional objective  (optional) (Cybran) 6": 22030805, "Defrag: Optional objective  (optional) (Cybran) 7": 22030806, "Defrag: Optional objective  (optional) (Cybran) 8": 22030807, "Defrag: Optional objective  (optional) (Cybran) 9": 22030808, "Defrag: Optional objective  (optional) (Cybran) 10": 22030809, "Defrag: Optional objective  (optional) (Cybran) 11": 22030810, "Defrag: Optional objective  (optional) (Cybran) 12": 22030811, "Defrag: Optional objective  (optional) (Cybran) 13": 22030812, "Defrag: Optional objective  (optional) (Cybran) 14": 22030813, "Defrag: Optional objective  (optional) (Cybran) 15": 22030814, "Defrag: Optional objective  (optional) (Cybran) 16": 22030815, "Defrag: Kill UEF Commander (Cybran) 1": 22030900, "Defrag: Kill UEF Commander (Cybran) 2": 22030901, "Defrag: Kill UEF Commander (Cybran) 3": 22030902, "Defrag: Kill UEF Commander (Cybran) 4": 22030903, "Defrag: Kill UEF Commander (Cybran) 5": 22030904, "Defrag: Kill UEF Commander (Cybran) 6": 22030905, "Defrag: Kill UEF Commander (Cybran) 7": 22030906, "Defrag: Kill UEF Commander (Cybran) 8": 22030907, "Defrag: Kill UEF Commander (Cybran) 9": 22030908, "Defrag: Kill UEF Commander (Cybran) 10": 22030909, "Defrag: Kill UEF Commander (Cybran) 11": 22030910, "Defrag: Kill UEF Commander (Cybran) 12": 22030911, "Defrag: Kill UEF Commander (Cybran) 13": 22030912, "Defrag: Kill UEF Commander (Cybran) 14": 22030913, "Defrag: Kill UEF Commander (Cybran) 15": 22030914, "Defrag: Kill UEF Commander (Cybran) 16": 22030915, "Mainframe Tango: Defeat Aeon Commander (Cybran) 1": 22040000, "Mainframe Tango: Defeat Aeon Commander (Cybran) 2": 22040001, "Mainframe Tango: Defeat Aeon Commander (Cybran) 3": 22040002, "Mainframe Tango: Defeat Aeon Commander (Cybran) 4": 22040003, "Mainframe Tango: Defeat Aeon Commander (Cybran) 5": 22040004, "Mainframe Tango: Defeat Aeon Commander (Cybran) 6": 22040005, "Mainframe Tango: Defeat Aeon Commander (Cybran) 7": 22040006, "Mainframe Tango: Defeat Aeon Commander (Cybran) 8": 22040007, "Mainframe Tango: Defeat Aeon Commander (Cybran) 9": 22040008, "Mainframe Tango: Defeat Aeon Commander (Cybran) 10": 22040009, "Mainframe Tango: Defeat Aeon Commander (Cybran) 11": 22040010, "Mainframe Tango: Defeat Aeon Commander (Cybran) 12": 22040011, "Mainframe Tango: Defeat Aeon Commander (Cybran) 13": 22040012, "Mainframe Tango: Defeat Aeon Commander (Cybran) 14": 22040013, "Mainframe Tango: Defeat Aeon Commander (Cybran) 15": 22040014, "Mainframe Tango: Defeat Aeon Commander (Cybran) 16": 22040015, "Mainframe Tango: Capture Network Node (Cybran) 1": 22040100, "Mainframe Tango: Capture Network Node (Cybran) 2": 22040101, "Mainframe Tango: Capture Network Node (Cybran) 3": 22040102, "Mainframe Tango: Capture Network Node (Cybran) 4": 22040103, "Mainframe Tango: Capture Network Node (Cybran) 5": 22040104, "Mainframe Tango: Capture Network Node (Cybran) 6": 22040105, "Mainframe Tango: Capture Network Node (Cybran) 7": 22040106, "Mainframe Tango: Capture Network Node (Cybran) 8": 22040107, "Mainframe Tango: Capture Network Node (Cybran) 9": 22040108, "Mainframe Tango: Capture Network Node (Cybran) 10": 22040109, "Mainframe Tango: Capture Network Node (Cybran) 11": 22040110, "Mainframe Tango: Capture Network Node (Cybran) 12": 22040111, "Mainframe Tango: Capture Network Node (Cybran) 13": 22040112, "Mainframe Tango: Capture Network Node (Cybran) 14": 22040113, "Mainframe Tango: Capture Network Node (Cybran) 15": 22040114, "Mainframe Tango: Capture Network Node (Cybran) 16": 22040115, "Mainframe Tango: Save Network Node (Cybran) 1": 22040200, "Mainframe Tango: Save Network Node (Cybran) 2": 22040201, "Mainframe Tango: Save Network Node (Cybran) 3": 22040202, "Mainframe Tango: Save Network Node (Cybran) 4": 22040203, "Mainframe Tango: Save Network Node (Cybran) 5": 22040204, "Mainframe Tango: Save Network Node (Cybran) 6": 22040205, "Mainframe Tango: Save Network Node (Cybran) 7": 22040206, "Mainframe Tango: Save Network Node (Cybran) 8": 22040207, "Mainframe Tango: Save Network Node (Cybran) 9": 22040208, "Mainframe Tango: Save Network Node (Cybran) 10": 22040209, "Mainframe Tango: Save Network Node (Cybran) 11": 22040210, "Mainframe Tango: Save Network Node (Cybran) 12": 22040211, "Mainframe Tango: Save Network Node (Cybran) 13": 22040212, "Mainframe Tango: Save Network Node (Cybran) 14": 22040213, "Mainframe Tango: Save Network Node (Cybran) 15": 22040214, "Mainframe Tango: Save Network Node (Cybran) 16": 22040215, "Mainframe Tango: Save 80% civilian buildings (optional) (Cybran) 1": 22040300, "Mainframe Tango: Save 80% civilian buildings (optional) (Cybran) 2": 22040301, "Mainframe Tango: Save 80% civilian buildings (optional) (Cybran) 3": 22040302, "Mainframe Tango: Save 80% civilian buildings (optional) (Cybran) 4": 22040303, "Mainframe Tango: Save 80% civilian buildings (optional) (Cybran) 5": 22040304, "Mainframe Tango: Save 80% civilian buildings (optional) (Cybran) 6": 22040305, "Mainframe Tango: Save 80% civilian buildings (optional) (Cybran) 7": 22040306, "Mainframe Tango: Save 80% civilian buildings (optional) (Cybran) 8": 22040307, "Mainframe Tango: Save 80% civilian buildings (optional) (Cybran) 9": 22040308, "Mainframe Tango: Save 80% civilian buildings (optional) (Cybran) 10": 22040309, "Mainframe Tango: Save 80% civilian buildings (optional) (Cybran) 11": 22040310, "Mainframe Tango: Save 80% civilian buildings (optional) (Cybran) 12": 22040311, "Mainframe Tango: Save 80% civilian buildings (optional) (Cybran) 13": 22040312, "Mainframe Tango: Save 80% civilian buildings (optional) (Cybran) 14": 22040313, "Mainframe Tango: Save 80% civilian buildings (optional) (Cybran) 15": 22040314, "Mainframe Tango: Save 80% civilian buildings (optional) (Cybran) 16": 22040315, "Mainframe Tango: Survive attacks (Cybran) 1": 22040400, "Mainframe Tango: Survive attacks (Cybran) 2": 22040401, "Mainframe Tango: Survive attacks (Cybran) 3": 22040402, "Mainframe Tango: Survive attacks (Cybran) 4": 22040403, "Mainframe Tango: Survive attacks (Cybran) 5": 22040404, "Mainframe Tango: Survive attacks (Cybran) 6": 22040405, "Mainframe Tango: Survive attacks (Cybran) 7": 22040406, "Mainframe Tango: Survive attacks (Cybran) 8": 22040407, "Mainframe Tango: Survive attacks (Cybran) 9": 22040408, "Mainframe Tango: Survive attacks (Cybran) 10": 22040409, "Mainframe Tango: Survive attacks (Cybran) 11": 22040410, "Mainframe Tango: Survive attacks (Cybran) 12": 22040411, "Mainframe Tango: Survive attacks (Cybran) 13": 22040412, "Mainframe Tango: Survive attacks (Cybran) 14": 22040413, "Mainframe Tango: Survive attacks (Cybran) 15": 22040414, "Mainframe Tango: Survive attacks (Cybran) 16": 22040415, "Mainframe Tango: Capture northeast node (Cybran) 1": 22040500, "Mainframe Tango: Capture northeast node (Cybran) 2": 22040501, "Mainframe Tango: Capture northeast node (Cybran) 3": 22040502, "Mainframe Tango: Capture northeast node (Cybran) 4": 22040503, "Mainframe Tango: Capture northeast node (Cybran) 5": 22040504, "Mainframe Tango: Capture northeast node (Cybran) 6": 22040505, "Mainframe Tango: Capture northeast node (Cybran) 7": 22040506, "Mainframe Tango: Capture northeast node (Cybran) 8": 22040507, "Mainframe Tango: Capture northeast node (Cybran) 9": 22040508, "Mainframe Tango: Capture northeast node (Cybran) 10": 22040509, "Mainframe Tango: Capture northeast node (Cybran) 11": 22040510, "Mainframe Tango: Capture northeast node (Cybran) 12": 22040511, "Mainframe Tango: Capture northeast node (Cybran) 13": 22040512, "Mainframe Tango: Capture northeast node (Cybran) 14": 22040513, "Mainframe Tango: Capture northeast node (Cybran) 15": 22040514, "Mainframe Tango: Capture northeast node (Cybran) 16": 22040515, "Mainframe Tango: Capture northwest node (Cybran) 1": 22040600, "Mainframe Tango: Capture northwest node (Cybran) 2": 22040601, "Mainframe Tango: Capture northwest node (Cybran) 3": 22040602, "Mainframe Tango: Capture northwest node (Cybran) 4": 22040603, "Mainframe Tango: Capture northwest node (Cybran) 5": 22040604, "Mainframe Tango: Capture northwest node (Cybran) 6": 22040605, "Mainframe Tango: Capture northwest node (Cybran) 7": 22040606, "Mainframe Tango: Capture northwest node (Cybran) 8": 22040607, "Mainframe Tango: Capture northwest node (Cybran) 9": 22040608, "Mainframe Tango: Capture northwest node (Cybran) 10": 22040609, "Mainframe Tango: Capture northwest node (Cybran) 11": 22040610, "Mainframe Tango: Capture northwest node (Cybran) 12": 22040611, "Mainframe Tango: Capture northwest node (Cybran) 13": 22040612, "Mainframe Tango: Capture northwest node (Cybran) 14": 22040613, "Mainframe Tango: Capture northwest node (Cybran) 15": 22040614, "Mainframe Tango: Capture northwest node (Cybran) 16": 22040615, "Mainframe Tango: Do not attack main Aeon base (Cybran) 1": 22040700, "Mainframe Tango: Do not attack main Aeon base (Cybran) 2": 22040701, "Mainframe Tango: Do not attack main Aeon base (Cybran) 3": 22040702, "Mainframe Tango: Do not attack main Aeon base (Cybran) 4": 22040703, "Mainframe Tango: Do not attack main Aeon base (Cybran) 5": 22040704, "Mainframe Tango: Do not attack main Aeon base (Cybran) 6": 22040705, "Mainframe Tango: Do not attack main Aeon base (Cybran) 7": 22040706, "Mainframe Tango: Do not attack main Aeon base (Cybran) 8": 22040707, "Mainframe Tango: Do not attack main Aeon base (Cybran) 9": 22040708, "Mainframe Tango: Do not attack main Aeon base (Cybran) 10": 22040709, "Mainframe Tango: Do not attack main Aeon base (Cybran) 11": 22040710, "Mainframe Tango: Do not attack main Aeon base (Cybran) 12": 22040711, "Mainframe Tango: Do not attack main Aeon base (Cybran) 13": 22040712, "Mainframe Tango: Do not attack main Aeon base (Cybran) 14": 22040713, "Mainframe Tango: Do not attack main Aeon base (Cybran) 15": 22040714, "Mainframe Tango: Do not attack main Aeon base (Cybran) 16": 22040715, "Mainframe Tango: Kill Aeon Commander (Cybran) 1": 22040800, "Mainframe Tango: Kill Aeon Commander (Cybran) 2": 22040801, "Mainframe Tango: Kill Aeon Commander (Cybran) 3": 22040802, "Mainframe Tango: Kill Aeon Commander (Cybran) 4": 22040803, "Mainframe Tango: Kill Aeon Commander (Cybran) 5": 22040804, "Mainframe Tango: Kill Aeon Commander (Cybran) 6": 22040805, "Mainframe Tango: Kill Aeon Commander (Cybran) 7": 22040806, "Mainframe Tango: Kill Aeon Commander (Cybran) 8": 22040807, "Mainframe Tango: Kill Aeon Commander (Cybran) 9": 22040808, "Mainframe Tango: Kill Aeon Commander (Cybran) 10": 22040809, "Mainframe Tango: Kill Aeon Commander (Cybran) 11": 22040810, "Mainframe Tango: Kill Aeon Commander (Cybran) 12": 22040811, "Mainframe Tango: Kill Aeon Commander (Cybran) 13": 22040812, "Mainframe Tango: Kill Aeon Commander (Cybran) 14": 22040813, "Mainframe Tango: Kill Aeon Commander (Cybran) 15": 22040814, "Mainframe Tango: Kill Aeon Commander (Cybran) 16": 22040815, "Unlock: Destroy UEF generators (Cybran) 1": 22050000, "Unlock: Destroy UEF generators (Cybran) 2": 22050001, "Unlock: Destroy UEF generators (Cybran) 3": 22050002, "Unlock: Destroy UEF generators (Cybran) 4": 22050003, "Unlock: Destroy UEF generators (Cybran) 5": 22050004, "Unlock: Destroy UEF generators (Cybran) 6": 22050005, "Unlock: Destroy UEF generators (Cybran) 7": 22050006, "Unlock: Destroy UEF generators (Cybran) 8": 22050007, "Unlock: Destroy UEF generators (Cybran) 9": 22050008, "Unlock: Destroy UEF generators (Cybran) 10": 22050009, "Unlock: Destroy UEF generators (Cybran) 11": 22050010, "Unlock: Destroy UEF generators (Cybran) 12": 22050011, "Unlock: Destroy UEF generators (Cybran) 13": 22050012, "Unlock: Destroy UEF generators (Cybran) 14": 22050013, "Unlock: Destroy UEF generators (Cybran) 15": 22050014, "Unlock: Destroy UEF generators (Cybran) 16": 22050015, "Unlock: Destroy UEF shipyards (optional) (Cybran) 1": 22050100, "Unlock: Destroy UEF shipyards (optional) (Cybran) 2": 22050101, "Unlock: Destroy UEF shipyards (optional) (Cybran) 3": 22050102, "Unlock: Destroy UEF shipyards (optional) (Cybran) 4": 22050103, "Unlock: Destroy UEF shipyards (optional) (Cybran) 5": 22050104, "Unlock: Destroy UEF shipyards (optional) (Cybran) 6": 22050105, "Unlock: Destroy UEF shipyards (optional) (Cybran) 7": 22050106, "Unlock: Destroy UEF shipyards (optional) (Cybran) 8": 22050107, "Unlock: Destroy UEF shipyards (optional) (Cybran) 9": 22050108, "Unlock: Destroy UEF shipyards (optional) (Cybran) 10": 22050109, "Unlock: Destroy UEF shipyards (optional) (Cybran) 11": 22050110, "Unlock: Destroy UEF shipyards (optional) (Cybran) 12": 22050111, "Unlock: Destroy UEF shipyards (optional) (Cybran) 13": 22050112, "Unlock: Destroy UEF shipyards (optional) (Cybran) 14": 22050113, "Unlock: Destroy UEF shipyards (optional) (Cybran) 15": 22050114, "Unlock: Destroy UEF shipyards (optional) (Cybran) 16": 22050115, "Unlock: Destroy UEF radars (Cybran) 1": 22050200, "Unlock: Destroy UEF radars (Cybran) 2": 22050201, "Unlock: Destroy UEF radars (Cybran) 3": 22050202, "Unlock: Destroy UEF radars (Cybran) 4": 22050203, "Unlock: Destroy UEF radars (Cybran) 5": 22050204, "Unlock: Destroy UEF radars (Cybran) 6": 22050205, "Unlock: Destroy UEF radars (Cybran) 7": 22050206, "Unlock: Destroy UEF radars (Cybran) 8": 22050207, "Unlock: Destroy UEF radars (Cybran) 9": 22050208, "Unlock: Destroy UEF radars (Cybran) 10": 22050209, "Unlock: Destroy UEF radars (Cybran) 11": 22050210, "Unlock: Destroy UEF radars (Cybran) 12": 22050211, "Unlock: Destroy UEF radars (Cybran) 13": 22050212, "Unlock: Destroy UEF radars (Cybran) 14": 22050213, "Unlock: Destroy UEF radars (Cybran) 15": 22050214, "Unlock: Destroy UEF radars (Cybran) 16": 22050215, "Unlock: Go to Hex5 (Cybran) 1": 22050300, "Unlock: Go to Hex5 (Cybran) 2": 22050301, "Unlock: Go to Hex5 (Cybran) 3": 22050302, "Unlock: Go to Hex5 (Cybran) 4": 22050303, "Unlock: Go to Hex5 (Cybran) 5": 22050304, "Unlock: Go to Hex5 (Cybran) 6": 22050305, "Unlock: Go to Hex5 (Cybran) 7": 22050306, "Unlock: Go to Hex5 (Cybran) 8": 22050307, "Unlock: Go to Hex5 (Cybran) 9": 22050308, "Unlock: Go to Hex5 (Cybran) 10": 22050309, "Unlock: Go to Hex5 (Cybran) 11": 22050310, "Unlock: Go to Hex5 (Cybran) 12": 22050311, "Unlock: Go to Hex5 (Cybran) 13": 22050312, "Unlock: Go to Hex5 (Cybran) 14": 22050313, "Unlock: Go to Hex5 (Cybran) 15": 22050314, "Unlock: Go to Hex5 (Cybran) 16": 22050315, "Unlock: Defend from heavy gunships (Cybran) 1": 22050400, "Unlock: Defend from heavy gunships (Cybran) 2": 22050401, "Unlock: Defend from heavy gunships (Cybran) 3": 22050402, "Unlock: Defend from heavy gunships (Cybran) 4": 22050403, "Unlock: Defend from heavy gunships (Cybran) 5": 22050404, "Unlock: Defend from heavy gunships (Cybran) 6": 22050405, "Unlock: Defend from heavy gunships (Cybran) 7": 22050406, "Unlock: Defend from heavy gunships (Cybran) 8": 22050407, "Unlock: Defend from heavy gunships (Cybran) 9": 22050408, "Unlock: Defend from heavy gunships (Cybran) 10": 22050409, "Unlock: Defend from heavy gunships (Cybran) 11": 22050410, "Unlock: Defend from heavy gunships (Cybran) 12": 22050411, "Unlock: Defend from heavy gunships (Cybran) 13": 22050412, "Unlock: Defend from heavy gunships (Cybran) 14": 22050413, "Unlock: Defend from heavy gunships (Cybran) 15": 22050414, "Unlock: Defend from heavy gunships (Cybran) 16": 22050415, "Unlock: Infect UEF landing pad (optional) (Cybran) 1": 22050500, "Unlock: Infect UEF landing pad (optional) (Cybran) 2": 22050501, "Unlock: Infect UEF landing pad (optional) (Cybran) 3": 22050502, "Unlock: Infect UEF landing pad (optional) (Cybran) 4": 22050503, "Unlock: Infect UEF landing pad (optional) (Cybran) 5": 22050504, "Unlock: Infect UEF landing pad (optional) (Cybran) 6": 22050505, "Unlock: Infect UEF landing pad (optional) (Cybran) 7": 22050506, "Unlock: Infect UEF landing pad (optional) (Cybran) 8": 22050507, "Unlock: Infect UEF landing pad (optional) (Cybran) 9": 22050508, "Unlock: Infect UEF landing pad (optional) (Cybran) 10": 22050509, "Unlock: Infect UEF landing pad (optional) (Cybran) 11": 22050510, "Unlock: Infect UEF landing pad (optional) (Cybran) 12": 22050511, "Unlock: Infect UEF landing pad (optional) (Cybran) 13": 22050512, "Unlock: Infect UEF landing pad (optional) (Cybran) 14": 22050513, "Unlock: Infect UEF landing pad (optional) (Cybran) 15": 22050514, "Unlock: Infect UEF landing pad (optional) (Cybran) 16": 22050515, "Unlock: This will be retconned later (Cybran) 1": 22050600, "Unlock: This will be retconned later (Cybran) 2": 22050601, "Unlock: This will be retconned later (Cybran) 3": 22050602, "Unlock: This will be retconned later (Cybran) 4": 22050603, "Unlock: This will be retconned later (Cybran) 5": 22050604, "Unlock: This will be retconned later (Cybran) 6": 22050605, "Unlock: This will be retconned later (Cybran) 7": 22050606, "Unlock: This will be retconned later (Cybran) 8": 22050607, "Unlock: This will be retconned later (Cybran) 9": 22050608, "Unlock: This will be retconned later (Cybran) 10": 22050609, "Unlock: This will be retconned later (Cybran) 11": 22050610, "Unlock: This will be retconned later (Cybran) 12": 22050611, "Unlock: This will be retconned later (Cybran) 13": 22050612, "Unlock: This will be retconned later (Cybran) 14": 22050613, "Unlock: This will be retconned later (Cybran) 15": 22050614, "Unlock: This will be retconned later (Cybran) 16": 22050615, "Unlock: Kill UEF Commander (Cybran) 1": 22050700, "Unlock: Kill UEF Commander (Cybran) 2": 22050701, "Unlock: Kill UEF Commander (Cybran) 3": 22050702, "Unlock: Kill UEF Commander (Cybran) 4": 22050703, "Unlock: Kill UEF Commander (Cybran) 5": 22050704, "Unlock: Kill UEF Commander (Cybran) 6": 22050705, "Unlock: Kill UEF Commander (Cybran) 7": 22050706, "Unlock: Kill UEF Commander (Cybran) 8": 22050707, "Unlock: Kill UEF Commander (Cybran) 9": 22050708, "Unlock: Kill UEF Commander (Cybran) 10": 22050709, "Unlock: Kill UEF Commander (Cybran) 11": 22050710, "Unlock: Kill UEF Commander (Cybran) 12": 22050711, "Unlock: Kill UEF Commander (Cybran) 13": 22050712, "Unlock: Kill UEF Commander (Cybran) 14": 22050713, "Unlock: Kill UEF Commander (Cybran) 15": 22050714, "Unlock: Kill UEF Commander (Cybran) 16": 22050715, "Freedom: Destroy CZAR (Cybran) 1": 22060000, "Freedom: Destroy CZAR (Cybran) 2": 22060001, "Freedom: Destroy CZAR (Cybran) 3": 22060002, "Freedom: Destroy CZAR (Cybran) 4": 22060003, "Freedom: Destroy CZAR (Cybran) 5": 22060004, "Freedom: Destroy CZAR (Cybran) 6": 22060005, "Freedom: Destroy CZAR (Cybran) 7": 22060006, "Freedom: Destroy CZAR (Cybran) 8": 22060007, "Freedom: Destroy CZAR (Cybran) 9": 22060008, "Freedom: Destroy CZAR (Cybran) 10": 22060009, "Freedom: Destroy CZAR (Cybran) 11": 22060010, "Freedom: Destroy CZAR (Cybran) 12": 22060011, "Freedom: Destroy CZAR (Cybran) 13": 22060012, "Freedom: Destroy CZAR (Cybran) 14": 22060013, "Freedom: Destroy CZAR (Cybran) 15": 22060014, "Freedom: Destroy CZAR (Cybran) 16": 22060015, "Freedom: Build Quantum Gate (Cybran) 1": 22060100, "Freedom: Build Quantum Gate (Cybran) 2": 22060101, "Freedom: Build Quantum Gate (Cybran) 3": 22060102, "Freedom: Build Quantum Gate (Cybran) 4": 22060103, "Freedom: Build Quantum Gate (Cybran) 5": 22060104, "Freedom: Build Quantum Gate (Cybran) 6": 22060105, "Freedom: Build Quantum Gate (Cybran) 7": 22060106, "Freedom: Build Quantum Gate (Cybran) 8": 22060107, "Freedom: Build Quantum Gate (Cybran) 9": 22060108, "Freedom: Build Quantum Gate (Cybran) 10": 22060109, "Freedom: Build Quantum Gate (Cybran) 11": 22060110, "Freedom: Build Quantum Gate (Cybran) 12": 22060111, "Freedom: Build Quantum Gate (Cybran) 13": 22060112, "Freedom: Build Quantum Gate (Cybran) 14": 22060113, "Freedom: Build Quantum Gate (Cybran) 15": 22060114, "Freedom: Build Quantum Gate (Cybran) 16": 22060115, "Freedom: Download Quantum Virus (Cybran) 1": 22060200, "Freedom: Download Quantum Virus (Cybran) 2": 22060201, "Freedom: Download Quantum Virus (Cybran) 3": 22060202, "Freedom: Download Quantum Virus (Cybran) 4": 22060203, "Freedom: Download Quantum Virus (Cybran) 5": 22060204, "Freedom: Download Quantum Virus (Cybran) 6": 22060205, "Freedom: Download Quantum Virus (Cybran) 7": 22060206, "Freedom: Download Quantum Virus (Cybran) 8": 22060207, "Freedom: Download Quantum Virus (Cybran) 9": 22060208, "Freedom: Download Quantum Virus (Cybran) 10": 22060209, "Freedom: Download Quantum Virus (Cybran) 11": 22060210, "Freedom: Download Quantum Virus (Cybran) 12": 22060211, "Freedom: Download Quantum Virus (Cybran) 13": 22060212, "Freedom: Download Quantum Virus (Cybran) 14": 22060213, "Freedom: Download Quantum Virus (Cybran) 15": 22060214, "Freedom: Download Quantum Virus (Cybran) 16": 22060215, "Freedom: Capture Black Sun control center (Cybran) 1": 22060300, "Freedom: Capture Black Sun control center (Cybran) 2": 22060301, "Freedom: Capture Black Sun control center (Cybran) 3": 22060302, "Freedom: Capture Black Sun control center (Cybran) 4": 22060303, "Freedom: Capture Black Sun control center (Cybran) 5": 22060304, "Freedom: Capture Black Sun control center (Cybran) 6": 22060305, "Freedom: Capture Black Sun control center (Cybran) 7": 22060306, "Freedom: Capture Black Sun control center (Cybran) 8": 22060307, "Freedom: Capture Black Sun control center (Cybran) 9": 22060308, "Freedom: Capture Black Sun control center (Cybran) 10": 22060309, "Freedom: Capture Black Sun control center (Cybran) 11": 22060310, "Freedom: Capture Black Sun control center (Cybran) 12": 22060311, "Freedom: Capture Black Sun control center (Cybran) 13": 22060312, "Freedom: Capture Black Sun control center (Cybran) 14": 22060313, "Freedom: Capture Black Sun control center (Cybran) 15": 22060314, "Freedom: Capture Black Sun control center (Cybran) 16": 22060315, "Freedom: Capture Black Sun (Cybran) 1": 22060400, "Freedom: Capture Black Sun (Cybran) 2": 22060401, "Freedom: Capture Black Sun (Cybran) 3": 22060402, "Freedom: Capture Black Sun (Cybran) 4": 22060403, "Freedom: Capture Black Sun (Cybran) 5": 22060404, "Freedom: Capture Black Sun (Cybran) 6": 22060405, "Freedom: Capture Black Sun (Cybran) 7": 22060406, "Freedom: Capture Black Sun (Cybran) 8": 22060407, "Freedom: Capture Black Sun (Cybran) 9": 22060408, "Freedom: Capture Black Sun (Cybran) 10": 22060409, "Freedom: Capture Black Sun (Cybran) 11": 22060410, "Freedom: Capture Black Sun (Cybran) 12": 22060411, "Freedom: Capture Black Sun (Cybran) 13": 22060412, "Freedom: Capture Black Sun (Cybran) 14": 22060413, "Freedom: Capture Black Sun (Cybran) 15": 22060414, "Freedom: Capture Black Sun (Cybran) 16": 22060415, "Freedom: Shoot Black Sun (Cybran) 1": 22060500, "Freedom: Shoot Black Sun (Cybran) 2": 22060501, "Freedom: Shoot Black Sun (Cybran) 3": 22060502, "Freedom: Shoot Black Sun (Cybran) 4": 22060503, "Freedom: Shoot Black Sun (Cybran) 5": 22060504, "Freedom: Shoot Black Sun (Cybran) 6": 22060505, "Freedom: Shoot Black Sun (Cybran) 7": 22060506, "Freedom: Shoot Black Sun (Cybran) 8": 22060507, "Freedom: Shoot Black Sun (Cybran) 9": 22060508, "Freedom: Shoot Black Sun (Cybran) 10": 22060509, "Freedom: Shoot Black Sun (Cybran) 11": 22060510, "Freedom: Shoot Black Sun (Cybran) 12": 22060511, "Freedom: Shoot Black Sun (Cybran) 13": 22060512, "Freedom: Shoot Black Sun (Cybran) 14": 22060513, "Freedom: Shoot Black Sun (Cybran) 15": 22060514, "Freedom: Shoot Black Sun (Cybran) 16": 22060515, "Liberation: Build mass (Aeon Illuminate) 1": 23010000, "Liberation: Build mass (Aeon Illuminate) 2": 23010001, "Liberation: Build mass (Aeon Illuminate) 3": 23010002, "Liberation: Build mass (Aeon Illuminate) 4": 23010003, "Liberation: Build mass (Aeon Illuminate) 5": 23010004, "Liberation: Build mass (Aeon Illuminate) 6": 23010005, "Liberation: Build mass (Aeon Illuminate) 7": 23010006, "Liberation: Build mass (Aeon Illuminate) 8": 23010007, "Liberation: Build mass (Aeon Illuminate) 9": 23010008, "Liberation: Build mass (Aeon Illuminate) 10": 23010009, "Liberation: Build mass (Aeon Illuminate) 11": 23010010, "Liberation: Build mass (Aeon Illuminate) 12": 23010011, "Liberation: Build mass (Aeon Illuminate) 13": 23010012, "Liberation: Build mass (Aeon Illuminate) 14": 23010013, "Liberation: Build mass (Aeon Illuminate) 15": 23010014, "Liberation: Build mass (Aeon Illuminate) 16": 23010015, "Liberation: Build power (Aeon Illuminate) 1": 23010100, "Liberation: Build power (Aeon Illuminate) 2": 23010101, "Liberation: Build power (Aeon Illuminate) 3": 23010102, "Liberation: Build power (Aeon Illuminate) 4": 23010103, "Liberation: Build power (Aeon Illuminate) 5": 23010104, "Liberation: Build power (Aeon Illuminate) 6": 23010105, "Liberation: Build power (Aeon Illuminate) 7": 23010106, "Liberation: Build power (Aeon Illuminate) 8": 23010107, "Liberation: Build power (Aeon Illuminate) 9": 23010108, "Liberation: Build power (Aeon Illuminate) 10": 23010109, "Liberation: Build power (Aeon Illuminate) 11": 23010110, "Liberation: Build power (Aeon Illuminate) 12": 23010111, "Liberation: Build power (Aeon Illuminate) 13": 23010112, "Liberation: Build power (Aeon Illuminate) 14": 23010113, "Liberation: Build power (Aeon Illuminate) 15": 23010114, "Liberation: Build power (Aeon Illuminate) 16": 23010115, "Liberation: Build air factory (Aeon Illuminate) 1": 23010200, "Liberation: Build air factory (Aeon Illuminate) 2": 23010201, "Liberation: Build air factory (Aeon Illuminate) 3": 23010202, "Liberation: Build air factory (Aeon Illuminate) 4": 23010203, "Liberation: Build air factory (Aeon Illuminate) 5": 23010204, "Liberation: Build air factory (Aeon Illuminate) 6": 23010205, "Liberation: Build air factory (Aeon Illuminate) 7": 23010206, "Liberation: Build air factory (Aeon Illuminate) 8": 23010207, "Liberation: Build air factory (Aeon Illuminate) 9": 23010208, "Liberation: Build air factory (Aeon Illuminate) 10": 23010209, "Liberation: Build air factory (Aeon Illuminate) 11": 23010210, "Liberation: Build air factory (Aeon Illuminate) 12": 23010211, "Liberation: Build air factory (Aeon Illuminate) 13": 23010212, "Liberation: Build air factory (Aeon Illuminate) 14": 23010213, "Liberation: Build air factory (Aeon Illuminate) 15": 23010214, "Liberation: Build air factory (Aeon Illuminate) 16": 23010215, "Liberation: Build bombers (Aeon Illuminate) 1": 23010300, "Liberation: Build bombers (Aeon Illuminate) 2": 23010301, "Liberation: Build bombers (Aeon Illuminate) 3": 23010302, "Liberation: Build bombers (Aeon Illuminate) 4": 23010303, "Liberation: Build bombers (Aeon Illuminate) 5": 23010304, "Liberation: Build bombers (Aeon Illuminate) 6": 23010305, "Liberation: Build bombers (Aeon Illuminate) 7": 23010306, "Liberation: Build bombers (Aeon Illuminate) 8": 23010307, "Liberation: Build bombers (Aeon Illuminate) 9": 23010308, "Liberation: Build bombers (Aeon Illuminate) 10": 23010309, "Liberation: Build bombers (Aeon Illuminate) 11": 23010310, "Liberation: Build bombers (Aeon Illuminate) 12": 23010311, "Liberation: Build bombers (Aeon Illuminate) 13": 23010312, "Liberation: Build bombers (Aeon Illuminate) 14": 23010313, "Liberation: Build bombers (Aeon Illuminate) 15": 23010314, "Liberation: Build bombers (Aeon Illuminate) 16": 23010315, "Liberation: Destroy radar defenders (Aeon Illuminate) 1": 23010400, "Liberation: Destroy radar defenders (Aeon Illuminate) 2": 23010401, "Liberation: Destroy radar defenders (Aeon Illuminate) 3": 23010402, "Liberation: Destroy radar defenders (Aeon Illuminate) 4": 23010403, "Liberation: Destroy radar defenders (Aeon Illuminate) 5": 23010404, "Liberation: Destroy radar defenders (Aeon Illuminate) 6": 23010405, "Liberation: Destroy radar defenders (Aeon Illuminate) 7": 23010406, "Liberation: Destroy radar defenders (Aeon Illuminate) 8": 23010407, "Liberation: Destroy radar defenders (Aeon Illuminate) 9": 23010408, "Liberation: Destroy radar defenders (Aeon Illuminate) 10": 23010409, "Liberation: Destroy radar defenders (Aeon Illuminate) 11": 23010410, "Liberation: Destroy radar defenders (Aeon Illuminate) 12": 23010411, "Liberation: Destroy radar defenders (Aeon Illuminate) 13": 23010412, "Liberation: Destroy radar defenders (Aeon Illuminate) 14": 23010413, "Liberation: Destroy radar defenders (Aeon Illuminate) 15": 23010414, "Liberation: Destroy radar defenders (Aeon Illuminate) 16": 23010415, "Liberation: Capture radars (Aeon Illuminate) 1": 23010500, "Liberation: Capture radars (Aeon Illuminate) 2": 23010501, "Liberation: Capture radars (Aeon Illuminate) 3": 23010502, "Liberation: Capture radars (Aeon Illuminate) 4": 23010503, "Liberation: Capture radars (Aeon Illuminate) 5": 23010504, "Liberation: Capture radars (Aeon Illuminate) 6": 23010505, "Liberation: Capture radars (Aeon Illuminate) 7": 23010506, "Liberation: Capture radars (Aeon Illuminate) 8": 23010507, "Liberation: Capture radars (Aeon Illuminate) 9": 23010508, "Liberation: Capture radars (Aeon Illuminate) 10": 23010509, "Liberation: Capture radars (Aeon Illuminate) 11": 23010510, "Liberation: Capture radars (Aeon Illuminate) 12": 23010511, "Liberation: Capture radars (Aeon Illuminate) 13": 23010512, "Liberation: Capture radars (Aeon Illuminate) 14": 23010513, "Liberation: Capture radars (Aeon Illuminate) 15": 23010514, "Liberation: Capture radars (Aeon Illuminate) 16": 23010515, "Liberation: Destroy mex (Aeon Illuminate) 1": 23010600, "Liberation: Destroy mex (Aeon Illuminate) 2": 23010601, "Liberation: Destroy mex (Aeon Illuminate) 3": 23010602, "Liberation: Destroy mex (Aeon Illuminate) 4": 23010603, "Liberation: Destroy mex (Aeon Illuminate) 5": 23010604, "Liberation: Destroy mex (Aeon Illuminate) 6": 23010605, "Liberation: Destroy mex (Aeon Illuminate) 7": 23010606, "Liberation: Destroy mex (Aeon Illuminate) 8": 23010607, "Liberation: Destroy mex (Aeon Illuminate) 9": 23010608, "Liberation: Destroy mex (Aeon Illuminate) 10": 23010609, "Liberation: Destroy mex (Aeon Illuminate) 11": 23010610, "Liberation: Destroy mex (Aeon Illuminate) 12": 23010611, "Liberation: Destroy mex (Aeon Illuminate) 13": 23010612, "Liberation: Destroy mex (Aeon Illuminate) 14": 23010613, "Liberation: Destroy mex (Aeon Illuminate) 15": 23010614, "Liberation: Destroy mex (Aeon Illuminate) 16": 23010615, "Liberation: Destroy UEF defences (Aeon Illuminate) 1": 23010700, "Liberation: Destroy UEF defences (Aeon Illuminate) 2": 23010701, "Liberation: Destroy UEF defences (Aeon Illuminate) 3": 23010702, "Liberation: Destroy UEF defences (Aeon Illuminate) 4": 23010703, "Liberation: Destroy UEF defences (Aeon Illuminate) 5": 23010704, "Liberation: Destroy UEF defences (Aeon Illuminate) 6": 23010705, "Liberation: Destroy UEF defences (Aeon Illuminate) 7": 23010706, "Liberation: Destroy UEF defences (Aeon Illuminate) 8": 23010707, "Liberation: Destroy UEF defences (Aeon Illuminate) 9": 23010708, "Liberation: Destroy UEF defences (Aeon Illuminate) 10": 23010709, "Liberation: Destroy UEF defences (Aeon Illuminate) 11": 23010710, "Liberation: Destroy UEF defences (Aeon Illuminate) 12": 23010711, "Liberation: Destroy UEF defences (Aeon Illuminate) 13": 23010712, "Liberation: Destroy UEF defences (Aeon Illuminate) 14": 23010713, "Liberation: Destroy UEF defences (Aeon Illuminate) 15": 23010714, "Liberation: Destroy UEF defences (Aeon Illuminate) 16": 23010715, "Liberation: Destroy UEF patrols (Aeon Illuminate) 1": 23010800, "Liberation: Destroy UEF patrols (Aeon Illuminate) 2": 23010801, "Liberation: Destroy UEF patrols (Aeon Illuminate) 3": 23010802, "Liberation: Destroy UEF patrols (Aeon Illuminate) 4": 23010803, "Liberation: Destroy UEF patrols (Aeon Illuminate) 5": 23010804, "Liberation: Destroy UEF patrols (Aeon Illuminate) 6": 23010805, "Liberation: Destroy UEF patrols (Aeon Illuminate) 7": 23010806, "Liberation: Destroy UEF patrols (Aeon Illuminate) 8": 23010807, "Liberation: Destroy UEF patrols (Aeon Illuminate) 9": 23010808, "Liberation: Destroy UEF patrols (Aeon Illuminate) 10": 23010809, "Liberation: Destroy UEF patrols (Aeon Illuminate) 11": 23010810, "Liberation: Destroy UEF patrols (Aeon Illuminate) 12": 23010811, "Liberation: Destroy UEF patrols (Aeon Illuminate) 13": 23010812, "Liberation: Destroy UEF patrols (Aeon Illuminate) 14": 23010813, "Liberation: Destroy UEF patrols (Aeon Illuminate) 15": 23010814, "Liberation: Destroy UEF patrols (Aeon Illuminate) 16": 23010815, "Liberation: Destroy UEF base defenders (Aeon Illuminate) 1": 23010900, "Liberation: Destroy UEF base defenders (Aeon Illuminate) 2": 23010901, "Liberation: Destroy UEF base defenders (Aeon Illuminate) 3": 23010902, "Liberation: Destroy UEF base defenders (Aeon Illuminate) 4": 23010903, "Liberation: Destroy UEF base defenders (Aeon Illuminate) 5": 23010904, "Liberation: Destroy UEF base defenders (Aeon Illuminate) 6": 23010905, "Liberation: Destroy UEF base defenders (Aeon Illuminate) 7": 23010906, "Liberation: Destroy UEF base defenders (Aeon Illuminate) 8": 23010907, "Liberation: Destroy UEF base defenders (Aeon Illuminate) 9": 23010908, "Liberation: Destroy UEF base defenders (Aeon Illuminate) 10": 23010909, "Liberation: Destroy UEF base defenders (Aeon Illuminate) 11": 23010910, "Liberation: Destroy UEF base defenders (Aeon Illuminate) 12": 23010911, "Liberation: Destroy UEF base defenders (Aeon Illuminate) 13": 23010912, "Liberation: Destroy UEF base defenders (Aeon Illuminate) 14": 23010913, "Liberation: Destroy UEF base defenders (Aeon Illuminate) 15": 23010914, "Liberation: Destroy UEF base defenders (Aeon Illuminate) 16": 23010915, "Liberation: Destroy UEF base (Aeon Illuminate) 1": 23011000, "Liberation: Destroy UEF base (Aeon Illuminate) 2": 23011001, "Liberation: Destroy UEF base (Aeon Illuminate) 3": 23011002, "Liberation: Destroy UEF base (Aeon Illuminate) 4": 23011003, "Liberation: Destroy UEF base (Aeon Illuminate) 5": 23011004, "Liberation: Destroy UEF base (Aeon Illuminate) 6": 23011005, "Liberation: Destroy UEF base (Aeon Illuminate) 7": 23011006, "Liberation: Destroy UEF base (Aeon Illuminate) 8": 23011007, "Liberation: Destroy UEF base (Aeon Illuminate) 9": 23011008, "Liberation: Destroy UEF base (Aeon Illuminate) 10": 23011009, "Liberation: Destroy UEF base (Aeon Illuminate) 11": 23011010, "Liberation: Destroy UEF base (Aeon Illuminate) 12": 23011011, "Liberation: Destroy UEF base (Aeon Illuminate) 13": 23011012, "Liberation: Destroy UEF base (Aeon Illuminate) 14": 23011013, "Liberation: Destroy UEF base (Aeon Illuminate) 15": 23011014, "Liberation: Destroy UEF base (Aeon Illuminate) 16": 23011015, "Liberation: Kill Aeon Commander (Aeon Illuminate) 1": 23011100, "Liberation: Kill Aeon Commander (Aeon Illuminate) 2": 23011101, "Liberation: Kill Aeon Commander (Aeon Illuminate) 3": 23011102, "Liberation: Kill Aeon Commander (Aeon Illuminate) 4": 23011103, "Liberation: Kill Aeon Commander (Aeon Illuminate) 5": 23011104, "Liberation: Kill Aeon Commander (Aeon Illuminate) 6": 23011105, "Liberation: Kill Aeon Commander (Aeon Illuminate) 7": 23011106, "Liberation: Kill Aeon Commander (Aeon Illuminate) 8": 23011107, "Liberation: Kill Aeon Commander (Aeon Illuminate) 9": 23011108, "Liberation: Kill Aeon Commander (Aeon Illuminate) 10": 23011109, "Liberation: Kill Aeon Commander (Aeon Illuminate) 11": 23011110, "Liberation: Kill Aeon Commander (Aeon Illuminate) 12": 23011111, "Liberation: Kill Aeon Commander (Aeon Illuminate) 13": 23011112, "Liberation: Kill Aeon Commander (Aeon Illuminate) 14": 23011113, "Liberation: Kill Aeon Commander (Aeon Illuminate) 15": 23011114, "Liberation: Kill Aeon Commander (Aeon Illuminate) 16": 23011115, "Artifact: Destroy first village defenders (Aeon Illuminate) 1": 23020000, "Artifact: Destroy first village defenders (Aeon Illuminate) 2": 23020001, "Artifact: Destroy first village defenders (Aeon Illuminate) 3": 23020002, "Artifact: Destroy first village defenders (Aeon Illuminate) 4": 23020003, "Artifact: Destroy first village defenders (Aeon Illuminate) 5": 23020004, "Artifact: Destroy first village defenders (Aeon Illuminate) 6": 23020005, "Artifact: Destroy first village defenders (Aeon Illuminate) 7": 23020006, "Artifact: Destroy first village defenders (Aeon Illuminate) 8": 23020007, "Artifact: Destroy first village defenders (Aeon Illuminate) 9": 23020008, "Artifact: Destroy first village defenders (Aeon Illuminate) 10": 23020009, "Artifact: Destroy first village defenders (Aeon Illuminate) 11": 23020010, "Artifact: Destroy first village defenders (Aeon Illuminate) 12": 23020011, "Artifact: Destroy first village defenders (Aeon Illuminate) 13": 23020012, "Artifact: Destroy first village defenders (Aeon Illuminate) 14": 23020013, "Artifact: Destroy first village defenders (Aeon Illuminate) 15": 23020014, "Artifact: Destroy first village defenders (Aeon Illuminate) 16": 23020015, "Artifact: Destroy first temple (Aeon Illuminate) 1": 23020100, "Artifact: Destroy first temple (Aeon Illuminate) 2": 23020101, "Artifact: Destroy first temple (Aeon Illuminate) 3": 23020102, "Artifact: Destroy first temple (Aeon Illuminate) 4": 23020103, "Artifact: Destroy first temple (Aeon Illuminate) 5": 23020104, "Artifact: Destroy first temple (Aeon Illuminate) 6": 23020105, "Artifact: Destroy first temple (Aeon Illuminate) 7": 23020106, "Artifact: Destroy first temple (Aeon Illuminate) 8": 23020107, "Artifact: Destroy first temple (Aeon Illuminate) 9": 23020108, "Artifact: Destroy first temple (Aeon Illuminate) 10": 23020109, "Artifact: Destroy first temple (Aeon Illuminate) 11": 23020110, "Artifact: Destroy first temple (Aeon Illuminate) 12": 23020111, "Artifact: Destroy first temple (Aeon Illuminate) 13": 23020112, "Artifact: Destroy first temple (Aeon Illuminate) 14": 23020113, "Artifact: Destroy first temple (Aeon Illuminate) 15": 23020114, "Artifact: Destroy first temple (Aeon Illuminate) 16": 23020115, "Artifact: Protect first artifact (Aeon Illuminate) 1": 23020200, "Artifact: Protect first artifact (Aeon Illuminate) 2": 23020201, "Artifact: Protect first artifact (Aeon Illuminate) 3": 23020202, "Artifact: Protect first artifact (Aeon Illuminate) 4": 23020203, "Artifact: Protect first artifact (Aeon Illuminate) 5": 23020204, "Artifact: Protect first artifact (Aeon Illuminate) 6": 23020205, "Artifact: Protect first artifact (Aeon Illuminate) 7": 23020206, "Artifact: Protect first artifact (Aeon Illuminate) 8": 23020207, "Artifact: Protect first artifact (Aeon Illuminate) 9": 23020208, "Artifact: Protect first artifact (Aeon Illuminate) 10": 23020209, "Artifact: Protect first artifact (Aeon Illuminate) 11": 23020210, "Artifact: Protect first artifact (Aeon Illuminate) 12": 23020211, "Artifact: Protect first artifact (Aeon Illuminate) 13": 23020212, "Artifact: Protect first artifact (Aeon Illuminate) 14": 23020213, "Artifact: Protect first artifact (Aeon Illuminate) 15": 23020214, "Artifact: Protect first artifact (Aeon Illuminate) 16": 23020215, "Artifact: Find second artifact (Aeon Illuminate) 1": 23020300, "Artifact: Find second artifact (Aeon Illuminate) 2": 23020301, "Artifact: Find second artifact (Aeon Illuminate) 3": 23020302, "Artifact: Find second artifact (Aeon Illuminate) 4": 23020303, "Artifact: Find second artifact (Aeon Illuminate) 5": 23020304, "Artifact: Find second artifact (Aeon Illuminate) 6": 23020305, "Artifact: Find second artifact (Aeon Illuminate) 7": 23020306, "Artifact: Find second artifact (Aeon Illuminate) 8": 23020307, "Artifact: Find second artifact (Aeon Illuminate) 9": 23020308, "Artifact: Find second artifact (Aeon Illuminate) 10": 23020309, "Artifact: Find second artifact (Aeon Illuminate) 11": 23020310, "Artifact: Find second artifact (Aeon Illuminate) 12": 23020311, "Artifact: Find second artifact (Aeon Illuminate) 13": 23020312, "Artifact: Find second artifact (Aeon Illuminate) 14": 23020313, "Artifact: Find second artifact (Aeon Illuminate) 15": 23020314, "Artifact: Find second artifact (Aeon Illuminate) 16": 23020315, "Artifact: Destroy Aeon reinforcements (Aeon Illuminate) 1": 23020400, "Artifact: Destroy Aeon reinforcements (Aeon Illuminate) 2": 23020401, "Artifact: Destroy Aeon reinforcements (Aeon Illuminate) 3": 23020402, "Artifact: Destroy Aeon reinforcements (Aeon Illuminate) 4": 23020403, "Artifact: Destroy Aeon reinforcements (Aeon Illuminate) 5": 23020404, "Artifact: Destroy Aeon reinforcements (Aeon Illuminate) 6": 23020405, "Artifact: Destroy Aeon reinforcements (Aeon Illuminate) 7": 23020406, "Artifact: Destroy Aeon reinforcements (Aeon Illuminate) 8": 23020407, "Artifact: Destroy Aeon reinforcements (Aeon Illuminate) 9": 23020408, "Artifact: Destroy Aeon reinforcements (Aeon Illuminate) 10": 23020409, "Artifact: Destroy Aeon reinforcements (Aeon Illuminate) 11": 23020410, "Artifact: Destroy Aeon reinforcements (Aeon Illuminate) 12": 23020411, "Artifact: Destroy Aeon reinforcements (Aeon Illuminate) 13": 23020412, "Artifact: Destroy Aeon reinforcements (Aeon Illuminate) 14": 23020413, "Artifact: Destroy Aeon reinforcements (Aeon Illuminate) 15": 23020414, "Artifact: Destroy Aeon reinforcements (Aeon Illuminate) 16": 23020415, "Artifact: Protect second artifact (Aeon Illuminate) 1": 23020500, "Artifact: Protect second artifact (Aeon Illuminate) 2": 23020501, "Artifact: Protect second artifact (Aeon Illuminate) 3": 23020502, "Artifact: Protect second artifact (Aeon Illuminate) 4": 23020503, "Artifact: Protect second artifact (Aeon Illuminate) 5": 23020504, "Artifact: Protect second artifact (Aeon Illuminate) 6": 23020505, "Artifact: Protect second artifact (Aeon Illuminate) 7": 23020506, "Artifact: Protect second artifact (Aeon Illuminate) 8": 23020507, "Artifact: Protect second artifact (Aeon Illuminate) 9": 23020508, "Artifact: Protect second artifact (Aeon Illuminate) 10": 23020509, "Artifact: Protect second artifact (Aeon Illuminate) 11": 23020510, "Artifact: Protect second artifact (Aeon Illuminate) 12": 23020511, "Artifact: Protect second artifact (Aeon Illuminate) 13": 23020512, "Artifact: Protect second artifact (Aeon Illuminate) 14": 23020513, "Artifact: Protect second artifact (Aeon Illuminate) 15": 23020514, "Artifact: Protect second artifact (Aeon Illuminate) 16": 23020515, "Artifact: Defend from Aeon attack (Aeon Illuminate) 1": 23020600, "Artifact: Defend from Aeon attack (Aeon Illuminate) 2": 23020601, "Artifact: Defend from Aeon attack (Aeon Illuminate) 3": 23020602, "Artifact: Defend from Aeon attack (Aeon Illuminate) 4": 23020603, "Artifact: Defend from Aeon attack (Aeon Illuminate) 5": 23020604, "Artifact: Defend from Aeon attack (Aeon Illuminate) 6": 23020605, "Artifact: Defend from Aeon attack (Aeon Illuminate) 7": 23020606, "Artifact: Defend from Aeon attack (Aeon Illuminate) 8": 23020607, "Artifact: Defend from Aeon attack (Aeon Illuminate) 9": 23020608, "Artifact: Defend from Aeon attack (Aeon Illuminate) 10": 23020609, "Artifact: Defend from Aeon attack (Aeon Illuminate) 11": 23020610, "Artifact: Defend from Aeon attack (Aeon Illuminate) 12": 23020611, "Artifact: Defend from Aeon attack (Aeon Illuminate) 13": 23020612, "Artifact: Defend from Aeon attack (Aeon Illuminate) 14": 23020613, "Artifact: Defend from Aeon attack (Aeon Illuminate) 15": 23020614, "Artifact: Defend from Aeon attack (Aeon Illuminate) 16": 23020615, "Artifact: Destroy eastern base (Aeon Illuminate) 1": 23020700, "Artifact: Destroy eastern base (Aeon Illuminate) 2": 23020701, "Artifact: Destroy eastern base (Aeon Illuminate) 3": 23020702, "Artifact: Destroy eastern base (Aeon Illuminate) 4": 23020703, "Artifact: Destroy eastern base (Aeon Illuminate) 5": 23020704, "Artifact: Destroy eastern base (Aeon Illuminate) 6": 23020705, "Artifact: Destroy eastern base (Aeon Illuminate) 7": 23020706, "Artifact: Destroy eastern base (Aeon Illuminate) 8": 23020707, "Artifact: Destroy eastern base (Aeon Illuminate) 9": 23020708, "Artifact: Destroy eastern base (Aeon Illuminate) 10": 23020709, "Artifact: Destroy eastern base (Aeon Illuminate) 11": 23020710, "Artifact: Destroy eastern base (Aeon Illuminate) 12": 23020711, "Artifact: Destroy eastern base (Aeon Illuminate) 13": 23020712, "Artifact: Destroy eastern base (Aeon Illuminate) 14": 23020713, "Artifact: Destroy eastern base (Aeon Illuminate) 15": 23020714, "Artifact: Destroy eastern base (Aeon Illuminate) 16": 23020715, "Artifact: Destroy navy base (Aeon Illuminate) 1": 23020800, "Artifact: Destroy navy base (Aeon Illuminate) 2": 23020801, "Artifact: Destroy navy base (Aeon Illuminate) 3": 23020802, "Artifact: Destroy navy base (Aeon Illuminate) 4": 23020803, "Artifact: Destroy navy base (Aeon Illuminate) 5": 23020804, "Artifact: Destroy navy base (Aeon Illuminate) 6": 23020805, "Artifact: Destroy navy base (Aeon Illuminate) 7": 23020806, "Artifact: Destroy navy base (Aeon Illuminate) 8": 23020807, "Artifact: Destroy navy base (Aeon Illuminate) 9": 23020808, "Artifact: Destroy navy base (Aeon Illuminate) 10": 23020809, "Artifact: Destroy navy base (Aeon Illuminate) 11": 23020810, "Artifact: Destroy navy base (Aeon Illuminate) 12": 23020811, "Artifact: Destroy navy base (Aeon Illuminate) 13": 23020812, "Artifact: Destroy navy base (Aeon Illuminate) 14": 23020813, "Artifact: Destroy navy base (Aeon Illuminate) 15": 23020814, "Artifact: Destroy navy base (Aeon Illuminate) 16": 23020815, "Artifact: Protect third artifact (Aeon Illuminate) 1": 23020900, "Artifact: Protect third artifact (Aeon Illuminate) 2": 23020901, "Artifact: Protect third artifact (Aeon Illuminate) 3": 23020902, "Artifact: Protect third artifact (Aeon Illuminate) 4": 23020903, "Artifact: Protect third artifact (Aeon Illuminate) 5": 23020904, "Artifact: Protect third artifact (Aeon Illuminate) 6": 23020905, "Artifact: Protect third artifact (Aeon Illuminate) 7": 23020906, "Artifact: Protect third artifact (Aeon Illuminate) 8": 23020907, "Artifact: Protect third artifact (Aeon Illuminate) 9": 23020908, "Artifact: Protect third artifact (Aeon Illuminate) 10": 23020909, "Artifact: Protect third artifact (Aeon Illuminate) 11": 23020910, "Artifact: Protect third artifact (Aeon Illuminate) 12": 23020911, "Artifact: Protect third artifact (Aeon Illuminate) 13": 23020912, "Artifact: Protect third artifact (Aeon Illuminate) 14": 23020913, "Artifact: Protect third artifact (Aeon Illuminate) 15": 23020914, "Artifact: Protect third artifact (Aeon Illuminate) 16": 23020915, "Artifact: Kill Aeon Commander (optional) (Aeon Illuminate) 1": 23021000, "Artifact: Kill Aeon Commander (optional) (Aeon Illuminate) 2": 23021001, "Artifact: Kill Aeon Commander (optional) (Aeon Illuminate) 3": 23021002, "Artifact: Kill Aeon Commander (optional) (Aeon Illuminate) 4": 23021003, "Artifact: Kill Aeon Commander (optional) (Aeon Illuminate) 5": 23021004, "Artifact: Kill Aeon Commander (optional) (Aeon Illuminate) 6": 23021005, "Artifact: Kill Aeon Commander (optional) (Aeon Illuminate) 7": 23021006, "Artifact: Kill Aeon Commander (optional) (Aeon Illuminate) 8": 23021007, "Artifact: Kill Aeon Commander (optional) (Aeon Illuminate) 9": 23021008, "Artifact: Kill Aeon Commander (optional) (Aeon Illuminate) 10": 23021009, "Artifact: Kill Aeon Commander (optional) (Aeon Illuminate) 11": 23021010, "Artifact: Kill Aeon Commander (optional) (Aeon Illuminate) 12": 23021011, "Artifact: Kill Aeon Commander (optional) (Aeon Illuminate) 13": 23021012, "Artifact: Kill Aeon Commander (optional) (Aeon Illuminate) 14": 23021013, "Artifact: Kill Aeon Commander (optional) (Aeon Illuminate) 15": 23021014, "Artifact: Kill Aeon Commander (optional) (Aeon Illuminate) 16": 23021015, "Artifact: Kill Mach (Aeon Illuminate) 1": 23021100, "Artifact: Kill Mach (Aeon Illuminate) 2": 23021101, "Artifact: Kill Mach (Aeon Illuminate) 3": 23021102, "Artifact: Kill Mach (Aeon Illuminate) 4": 23021103, "Artifact: Kill Mach (Aeon Illuminate) 5": 23021104, "Artifact: Kill Mach (Aeon Illuminate) 6": 23021105, "Artifact: Kill Mach (Aeon Illuminate) 7": 23021106, "Artifact: Kill Mach (Aeon Illuminate) 8": 23021107, "Artifact: Kill Mach (Aeon Illuminate) 9": 23021108, "Artifact: Kill Mach (Aeon Illuminate) 10": 23021109, "Artifact: Kill Mach (Aeon Illuminate) 11": 23021110, "Artifact: Kill Mach (Aeon Illuminate) 12": 23021111, "Artifact: Kill Mach (Aeon Illuminate) 13": 23021112, "Artifact: Kill Mach (Aeon Illuminate) 14": 23021113, "Artifact: Kill Mach (Aeon Illuminate) 15": 23021114, "Artifact: Kill Mach (Aeon Illuminate) 16": 23021115, "Artifact: Go to Gate (Aeon Illuminate) 1": 23021200, "Artifact: Go to Gate (Aeon Illuminate) 2": 23021201, "Artifact: Go to Gate (Aeon Illuminate) 3": 23021202, "Artifact: Go to Gate (Aeon Illuminate) 4": 23021203, "Artifact: Go to Gate (Aeon Illuminate) 5": 23021204, "Artifact: Go to Gate (Aeon Illuminate) 6": 23021205, "Artifact: Go to Gate (Aeon Illuminate) 7": 23021206, "Artifact: Go to Gate (Aeon Illuminate) 8": 23021207, "Artifact: Go to Gate (Aeon Illuminate) 9": 23021208, "Artifact: Go to Gate (Aeon Illuminate) 10": 23021209, "Artifact: Go to Gate (Aeon Illuminate) 11": 23021210, "Artifact: Go to Gate (Aeon Illuminate) 12": 23021211, "Artifact: Go to Gate (Aeon Illuminate) 13": 23021212, "Artifact: Go to Gate (Aeon Illuminate) 14": 23021213, "Artifact: Go to Gate (Aeon Illuminate) 15": 23021214, "Artifact: Go to Gate (Aeon Illuminate) 16": 23021215, "Defrag: Protect York 18 (Aeon Illuminate) 1": 23030000, "Defrag: Protect York 18 (Aeon Illuminate) 2": 23030001, "Defrag: Protect York 18 (Aeon Illuminate) 3": 23030002, "Defrag: Protect York 18 (Aeon Illuminate) 4": 23030003, "Defrag: Protect York 18 (Aeon Illuminate) 5": 23030004, "Defrag: Protect York 18 (Aeon Illuminate) 6": 23030005, "Defrag: Protect York 18 (Aeon Illuminate) 7": 23030006, "Defrag: Protect York 18 (Aeon Illuminate) 8": 23030007, "Defrag: Protect York 18 (Aeon Illuminate) 9": 23030008, "Defrag: Protect York 18 (Aeon Illuminate) 10": 23030009, "Defrag: Protect York 18 (Aeon Illuminate) 11": 23030010, "Defrag: Protect York 18 (Aeon Illuminate) 12": 23030011, "Defrag: Protect York 18 (Aeon Illuminate) 13": 23030012, "Defrag: Protect York 18 (Aeon Illuminate) 14": 23030013, "Defrag: Protect York 18 (Aeon Illuminate) 15": 23030014, "Defrag: Protect York 18 (Aeon Illuminate) 16": 23030015, "Defrag: Destroy western UEF base (Aeon Illuminate) 1": 23030100, "Defrag: Destroy western UEF base (Aeon Illuminate) 2": 23030101, "Defrag: Destroy western UEF base (Aeon Illuminate) 3": 23030102, "Defrag: Destroy western UEF base (Aeon Illuminate) 4": 23030103, "Defrag: Destroy western UEF base (Aeon Illuminate) 5": 23030104, "Defrag: Destroy western UEF base (Aeon Illuminate) 6": 23030105, "Defrag: Destroy western UEF base (Aeon Illuminate) 7": 23030106, "Defrag: Destroy western UEF base (Aeon Illuminate) 8": 23030107, "Defrag: Destroy western UEF base (Aeon Illuminate) 9": 23030108, "Defrag: Destroy western UEF base (Aeon Illuminate) 10": 23030109, "Defrag: Destroy western UEF base (Aeon Illuminate) 11": 23030110, "Defrag: Destroy western UEF base (Aeon Illuminate) 12": 23030111, "Defrag: Destroy western UEF base (Aeon Illuminate) 13": 23030112, "Defrag: Destroy western UEF base (Aeon Illuminate) 14": 23030113, "Defrag: Destroy western UEF base (Aeon Illuminate) 15": 23030114, "Defrag: Destroy western UEF base (Aeon Illuminate) 16": 23030115, "Defrag: Destroy north-western UEF base (Aeon Illuminate) 1": 23030200, "Defrag: Destroy north-western UEF base (Aeon Illuminate) 2": 23030201, "Defrag: Destroy north-western UEF base (Aeon Illuminate) 3": 23030202, "Defrag: Destroy north-western UEF base (Aeon Illuminate) 4": 23030203, "Defrag: Destroy north-western UEF base (Aeon Illuminate) 5": 23030204, "Defrag: Destroy north-western UEF base (Aeon Illuminate) 6": 23030205, "Defrag: Destroy north-western UEF base (Aeon Illuminate) 7": 23030206, "Defrag: Destroy north-western UEF base (Aeon Illuminate) 8": 23030207, "Defrag: Destroy north-western UEF base (Aeon Illuminate) 9": 23030208, "Defrag: Destroy north-western UEF base (Aeon Illuminate) 10": 23030209, "Defrag: Destroy north-western UEF base (Aeon Illuminate) 11": 23030210, "Defrag: Destroy north-western UEF base (Aeon Illuminate) 12": 23030211, "Defrag: Destroy north-western UEF base (Aeon Illuminate) 13": 23030212, "Defrag: Destroy north-western UEF base (Aeon Illuminate) 14": 23030213, "Defrag: Destroy north-western UEF base (Aeon Illuminate) 15": 23030214, "Defrag: Destroy north-western UEF base (Aeon Illuminate) 16": 23030215, "Defrag: Destroy northern UEF base (Aeon Illuminate) 1": 23030300, "Defrag: Destroy northern UEF base (Aeon Illuminate) 2": 23030301, "Defrag: Destroy northern UEF base (Aeon Illuminate) 3": 23030302, "Defrag: Destroy northern UEF base (Aeon Illuminate) 4": 23030303, "Defrag: Destroy northern UEF base (Aeon Illuminate) 5": 23030304, "Defrag: Destroy northern UEF base (Aeon Illuminate) 6": 23030305, "Defrag: Destroy northern UEF base (Aeon Illuminate) 7": 23030306, "Defrag: Destroy northern UEF base (Aeon Illuminate) 8": 23030307, "Defrag: Destroy northern UEF base (Aeon Illuminate) 9": 23030308, "Defrag: Destroy northern UEF base (Aeon Illuminate) 10": 23030309, "Defrag: Destroy northern UEF base (Aeon Illuminate) 11": 23030310, "Defrag: Destroy northern UEF base (Aeon Illuminate) 12": 23030311, "Defrag: Destroy northern UEF base (Aeon Illuminate) 13": 23030312, "Defrag: Destroy northern UEF base (Aeon Illuminate) 14": 23030313, "Defrag: Destroy northern UEF base (Aeon Illuminate) 15": 23030314, "Defrag: Destroy northern UEF base (Aeon Illuminate) 16": 23030315, "Defrag: Sink UEF cruiser (Aeon Illuminate) 1": 23030400, "Defrag: Sink UEF cruiser (Aeon Illuminate) 2": 23030401, "Defrag: Sink UEF cruiser (Aeon Illuminate) 3": 23030402, "Defrag: Sink UEF cruiser (Aeon Illuminate) 4": 23030403, "Defrag: Sink UEF cruiser (Aeon Illuminate) 5": 23030404, "Defrag: Sink UEF cruiser (Aeon Illuminate) 6": 23030405, "Defrag: Sink UEF cruiser (Aeon Illuminate) 7": 23030406, "Defrag: Sink UEF cruiser (Aeon Illuminate) 8": 23030407, "Defrag: Sink UEF cruiser (Aeon Illuminate) 9": 23030408, "Defrag: Sink UEF cruiser (Aeon Illuminate) 10": 23030409, "Defrag: Sink UEF cruiser (Aeon Illuminate) 11": 23030410, "Defrag: Sink UEF cruiser (Aeon Illuminate) 12": 23030411, "Defrag: Sink UEF cruiser (Aeon Illuminate) 13": 23030412, "Defrag: Sink UEF cruiser (Aeon Illuminate) 14": 23030413, "Defrag: Sink UEF cruiser (Aeon Illuminate) 15": 23030414, "Defrag: Sink UEF cruiser (Aeon Illuminate) 16": 23030415, "Defrag: Destroy static artillery (Aeon Illuminate) 1": 23030500, "Defrag: Destroy static artillery (Aeon Illuminate) 2": 23030501, "Defrag: Destroy static artillery (Aeon Illuminate) 3": 23030502, "Defrag: Destroy static artillery (Aeon Illuminate) 4": 23030503, "Defrag: Destroy static artillery (Aeon Illuminate) 5": 23030504, "Defrag: Destroy static artillery (Aeon Illuminate) 6": 23030505, "Defrag: Destroy static artillery (Aeon Illuminate) 7": 23030506, "Defrag: Destroy static artillery (Aeon Illuminate) 8": 23030507, "Defrag: Destroy static artillery (Aeon Illuminate) 9": 23030508, "Defrag: Destroy static artillery (Aeon Illuminate) 10": 23030509, "Defrag: Destroy static artillery (Aeon Illuminate) 11": 23030510, "Defrag: Destroy static artillery (Aeon Illuminate) 12": 23030511, "Defrag: Destroy static artillery (Aeon Illuminate) 13": 23030512, "Defrag: Destroy static artillery (Aeon Illuminate) 14": 23030513, "Defrag: Destroy static artillery (Aeon Illuminate) 15": 23030514, "Defrag: Destroy static artillery (Aeon Illuminate) 16": 23030515, "Defrag: Escort trucks (Aeon Illuminate) 1": 23030600, "Defrag: Escort trucks (Aeon Illuminate) 2": 23030601, "Defrag: Escort trucks (Aeon Illuminate) 3": 23030602, "Defrag: Escort trucks (Aeon Illuminate) 4": 23030603, "Defrag: Escort trucks (Aeon Illuminate) 5": 23030604, "Defrag: Escort trucks (Aeon Illuminate) 6": 23030605, "Defrag: Escort trucks (Aeon Illuminate) 7": 23030606, "Defrag: Escort trucks (Aeon Illuminate) 8": 23030607, "Defrag: Escort trucks (Aeon Illuminate) 9": 23030608, "Defrag: Escort trucks (Aeon Illuminate) 10": 23030609, "Defrag: Escort trucks (Aeon Illuminate) 11": 23030610, "Defrag: Escort trucks (Aeon Illuminate) 12": 23030611, "Defrag: Escort trucks (Aeon Illuminate) 13": 23030612, "Defrag: Escort trucks (Aeon Illuminate) 14": 23030613, "Defrag: Escort trucks (Aeon Illuminate) 15": 23030614, "Defrag: Escort trucks (Aeon Illuminate) 16": 23030615, "Defrag: Escort ALL trucks (optional) (Aeon Illuminate) 1": 23030700, "Defrag: Escort ALL trucks (optional) (Aeon Illuminate) 2": 23030701, "Defrag: Escort ALL trucks (optional) (Aeon Illuminate) 3": 23030702, "Defrag: Escort ALL trucks (optional) (Aeon Illuminate) 4": 23030703, "Defrag: Escort ALL trucks (optional) (Aeon Illuminate) 5": 23030704, "Defrag: Escort ALL trucks (optional) (Aeon Illuminate) 6": 23030705, "Defrag: Escort ALL trucks (optional) (Aeon Illuminate) 7": 23030706, "Defrag: Escort ALL trucks (optional) (Aeon Illuminate) 8": 23030707, "Defrag: Escort ALL trucks (optional) (Aeon Illuminate) 9": 23030708, "Defrag: Escort ALL trucks (optional) (Aeon Illuminate) 10": 23030709, "Defrag: Escort ALL trucks (optional) (Aeon Illuminate) 11": 23030710, "Defrag: Escort ALL trucks (optional) (Aeon Illuminate) 12": 23030711, "Defrag: Escort ALL trucks (optional) (Aeon Illuminate) 13": 23030712, "Defrag: Escort ALL trucks (optional) (Aeon Illuminate) 14": 23030713, "Defrag: Escort ALL trucks (optional) (Aeon Illuminate) 15": 23030714, "Defrag: Escort ALL trucks (optional) (Aeon Illuminate) 16": 23030715, "Defrag: Optional objective  (optional) (Aeon Illuminate) 1": 23030800, "Defrag: Optional objective  (optional) (Aeon Illuminate) 2": 23030801, "Defrag: Optional objective  (optional) (Aeon Illuminate) 3": 23030802, "Defrag: Optional objective  (optional) (Aeon Illuminate) 4": 23030803, "Defrag: Optional objective  (optional) (Aeon Illuminate) 5": 23030804, "Defrag: Optional objective  (optional) (Aeon Illuminate) 6": 23030805, "Defrag: Optional objective  (optional) (Aeon Illuminate) 7": 23030806, "Defrag: Optional objective  (optional) (Aeon Illuminate) 8": 23030807, "Defrag: Optional objective  (optional) (Aeon Illuminate) 9": 23030808, "Defrag: Optional objective  (optional) (Aeon Illuminate) 10": 23030809, "Defrag: Optional objective  (optional) (Aeon Illuminate) 11": 23030810, "Defrag: Optional objective  (optional) (Aeon Illuminate) 12": 23030811, "Defrag: Optional objective  (optional) (Aeon Illuminate) 13": 23030812, "Defrag: Optional objective  (optional) (Aeon Illuminate) 14": 23030813, "Defrag: Optional objective  (optional) (Aeon Illuminate) 15": 23030814, "Defrag: Optional objective  (optional) (Aeon Illuminate) 16": 23030815, "Defrag: Kill UEF Commander (Aeon Illuminate) 1": 23030900, "Defrag: Kill UEF Commander (Aeon Illuminate) 2": 23030901, "Defrag: Kill UEF Commander (Aeon Illuminate) 3": 23030902, "Defrag: Kill UEF Commander (Aeon Illuminate) 4": 23030903, "Defrag: Kill UEF Commander (Aeon Illuminate) 5": 23030904, "Defrag: Kill UEF Commander (Aeon Illuminate) 6": 23030905, "Defrag: Kill UEF Commander (Aeon Illuminate) 7": 23030906, "Defrag: Kill UEF Commander (Aeon Illuminate) 8": 23030907, "Defrag: Kill UEF Commander (Aeon Illuminate) 9": 23030908, "Defrag: Kill UEF Commander (Aeon Illuminate) 10": 23030909, "Defrag: Kill UEF Commander (Aeon Illuminate) 11": 23030910, "Defrag: Kill UEF Commander (Aeon Illuminate) 12": 23030911, "Defrag: Kill UEF Commander (Aeon Illuminate) 13": 23030912, "Defrag: Kill UEF Commander (Aeon Illuminate) 14": 23030913, "Defrag: Kill UEF Commander (Aeon Illuminate) 15": 23030914, "Defrag: Kill UEF Commander (Aeon Illuminate) 16": 23030915, "Mainframe Tango: Defeat Aeon Commander (Aeon Illuminate) 1": 23040000, "Mainframe Tango: Defeat Aeon Commander (Aeon Illuminate) 2": 23040001, "Mainframe Tango: Defeat Aeon Commander (Aeon Illuminate) 3": 23040002, "Mainframe Tango: Defeat Aeon Commander (Aeon Illuminate) 4": 23040003, "Mainframe Tango: Defeat Aeon Commander (Aeon Illuminate) 5": 23040004, "Mainframe Tango: Defeat Aeon Commander (Aeon Illuminate) 6": 23040005, "Mainframe Tango: Defeat Aeon Commander (Aeon Illuminate) 7": 23040006, "Mainframe Tango: Defeat Aeon Commander (Aeon Illuminate) 8": 23040007, "Mainframe Tango: Defeat Aeon Commander (Aeon Illuminate) 9": 23040008, "Mainframe Tango: Defeat Aeon Commander (Aeon Illuminate) 10": 23040009, "Mainframe Tango: Defeat Aeon Commander (Aeon Illuminate) 11": 23040010, "Mainframe Tango: Defeat Aeon Commander (Aeon Illuminate) 12": 23040011, "Mainframe Tango: Defeat Aeon Commander (Aeon Illuminate) 13": 23040012, "Mainframe Tango: Defeat Aeon Commander (Aeon Illuminate) 14": 23040013, "Mainframe Tango: Defeat Aeon Commander (Aeon Illuminate) 15": 23040014, "Mainframe Tango: Defeat Aeon Commander (Aeon Illuminate) 16": 23040015, "Mainframe Tango: Capture Network Node (Aeon Illuminate) 1": 23040100, "Mainframe Tango: Capture Network Node (Aeon Illuminate) 2": 23040101, "Mainframe Tango: Capture Network Node (Aeon Illuminate) 3": 23040102, "Mainframe Tango: Capture Network Node (Aeon Illuminate) 4": 23040103, "Mainframe Tango: Capture Network Node (Aeon Illuminate) 5": 23040104, "Mainframe Tango: Capture Network Node (Aeon Illuminate) 6": 23040105, "Mainframe Tango: Capture Network Node (Aeon Illuminate) 7": 23040106, "Mainframe Tango: Capture Network Node (Aeon Illuminate) 8": 23040107, "Mainframe Tango: Capture Network Node (Aeon Illuminate) 9": 23040108, "Mainframe Tango: Capture Network Node (Aeon Illuminate) 10": 23040109, "Mainframe Tango: Capture Network Node (Aeon Illuminate) 11": 23040110, "Mainframe Tango: Capture Network Node (Aeon Illuminate) 12": 23040111, "Mainframe Tango: Capture Network Node (Aeon Illuminate) 13": 23040112, "Mainframe Tango: Capture Network Node (Aeon Illuminate) 14": 23040113, "Mainframe Tango: Capture Network Node (Aeon Illuminate) 15": 23040114, "Mainframe Tango: Capture Network Node (Aeon Illuminate) 16": 23040115, "Mainframe Tango: Save Network Node (Aeon Illuminate) 1": 23040200, "Mainframe Tango: Save Network Node (Aeon Illuminate) 2": 23040201, "Mainframe Tango: Save Network Node (Aeon Illuminate) 3": 23040202, "Mainframe Tango: Save Network Node (Aeon Illuminate) 4": 23040203, "Mainframe Tango: Save Network Node (Aeon Illuminate) 5": 23040204, "Mainframe Tango: Save Network Node (Aeon Illuminate) 6": 23040205, "Mainframe Tango: Save Network Node (Aeon Illuminate) 7": 23040206, "Mainframe Tango: Save Network Node (Aeon Illuminate) 8": 23040207, "Mainframe Tango: Save Network Node (Aeon Illuminate) 9": 23040208, "Mainframe Tango: Save Network Node (Aeon Illuminate) 10": 23040209, "Mainframe Tango: Save Network Node (Aeon Illuminate) 11": 23040210, "Mainframe Tango: Save Network Node (Aeon Illuminate) 12": 23040211, "Mainframe Tango: Save Network Node (Aeon Illuminate) 13": 23040212, "Mainframe Tango: Save Network Node (Aeon Illuminate) 14": 23040213, "Mainframe Tango: Save Network Node (Aeon Illuminate) 15": 23040214, "Mainframe Tango: Save Network Node (Aeon Illuminate) 16": 23040215, "Mainframe Tango: Save 80% civilian buildings (optional) (Aeon Illuminate) 1": 23040300, "Mainframe Tango: Save 80% civilian buildings (optional) (Aeon Illuminate) 2": 23040301, "Mainframe Tango: Save 80% civilian buildings (optional) (Aeon Illuminate) 3": 23040302, "Mainframe Tango: Save 80% civilian buildings (optional) (Aeon Illuminate) 4": 23040303, "Mainframe Tango: Save 80% civilian buildings (optional) (Aeon Illuminate) 5": 23040304, "Mainframe Tango: Save 80% civilian buildings (optional) (Aeon Illuminate) 6": 23040305, "Mainframe Tango: Save 80% civilian buildings (optional) (Aeon Illuminate) 7": 23040306, "Mainframe Tango: Save 80% civilian buildings (optional) (Aeon Illuminate) 8": 23040307, "Mainframe Tango: Save 80% civilian buildings (optional) (Aeon Illuminate) 9": 23040308, "Mainframe Tango: Save 80% civilian buildings (optional) (Aeon Illuminate) 10": 23040309, "Mainframe Tango: Save 80% civilian buildings (optional) (Aeon Illuminate) 11": 23040310, "Mainframe Tango: Save 80% civilian buildings (optional) (Aeon Illuminate) 12": 23040311, "Mainframe Tango: Save 80% civilian buildings (optional) (Aeon Illuminate) 13": 23040312, "Mainframe Tango: Save 80% civilian buildings (optional) (Aeon Illuminate) 14": 23040313, "Mainframe Tango: Save 80% civilian buildings (optional) (Aeon Illuminate) 15": 23040314, "Mainframe Tango: Save 80% civilian buildings (optional) (Aeon Illuminate) 16": 23040315, "Mainframe Tango: Survive attacks (Aeon Illuminate) 1": 23040400, "Mainframe Tango: Survive attacks (Aeon Illuminate) 2": 23040401, "Mainframe Tango: Survive attacks (Aeon Illuminate) 3": 23040402, "Mainframe Tango: Survive attacks (Aeon Illuminate) 4": 23040403, "Mainframe Tango: Survive attacks (Aeon Illuminate) 5": 23040404, "Mainframe Tango: Survive attacks (Aeon Illuminate) 6": 23040405, "Mainframe Tango: Survive attacks (Aeon Illuminate) 7": 23040406, "Mainframe Tango: Survive attacks (Aeon Illuminate) 8": 23040407, "Mainframe Tango: Survive attacks (Aeon Illuminate) 9": 23040408, "Mainframe Tango: Survive attacks (Aeon Illuminate) 10": 23040409, "Mainframe Tango: Survive attacks (Aeon Illuminate) 11": 23040410, "Mainframe Tango: Survive attacks (Aeon Illuminate) 12": 23040411, "Mainframe Tango: Survive attacks (Aeon Illuminate) 13": 23040412, "Mainframe Tango: Survive attacks (Aeon Illuminate) 14": 23040413, "Mainframe Tango: Survive attacks (Aeon Illuminate) 15": 23040414, "Mainframe Tango: Survive attacks (Aeon Illuminate) 16": 23040415, "Mainframe Tango: Capture northeast node (Aeon Illuminate) 1": 23040500, "Mainframe Tango: Capture northeast node (Aeon Illuminate) 2": 23040501, "Mainframe Tango: Capture northeast node (Aeon Illuminate) 3": 23040502, "Mainframe Tango: Capture northeast node (Aeon Illuminate) 4": 23040503, "Mainframe Tango: Capture northeast node (Aeon Illuminate) 5": 23040504, "Mainframe Tango: Capture northeast node (Aeon Illuminate) 6": 23040505, "Mainframe Tango: Capture northeast node (Aeon Illuminate) 7": 23040506, "Mainframe Tango: Capture northeast node (Aeon Illuminate) 8": 23040507, "Mainframe Tango: Capture northeast node (Aeon Illuminate) 9": 23040508, "Mainframe Tango: Capture northeast node (Aeon Illuminate) 10": 23040509, "Mainframe Tango: Capture northeast node (Aeon Illuminate) 11": 23040510, "Mainframe Tango: Capture northeast node (Aeon Illuminate) 12": 23040511, "Mainframe Tango: Capture northeast node (Aeon Illuminate) 13": 23040512, "Mainframe Tango: Capture northeast node (Aeon Illuminate) 14": 23040513, "Mainframe Tango: Capture northeast node (Aeon Illuminate) 15": 23040514, "Mainframe Tango: Capture northeast node (Aeon Illuminate) 16": 23040515, "Mainframe Tango: Capture northwest node (Aeon Illuminate) 1": 23040600, "Mainframe Tango: Capture northwest node (Aeon Illuminate) 2": 23040601, "Mainframe Tango: Capture northwest node (Aeon Illuminate) 3": 23040602, "Mainframe Tango: Capture northwest node (Aeon Illuminate) 4": 23040603, "Mainframe Tango: Capture northwest node (Aeon Illuminate) 5": 23040604, "Mainframe Tango: Capture northwest node (Aeon Illuminate) 6": 23040605, "Mainframe Tango: Capture northwest node (Aeon Illuminate) 7": 23040606, "Mainframe Tango: Capture northwest node (Aeon Illuminate) 8": 23040607, "Mainframe Tango: Capture northwest node (Aeon Illuminate) 9": 23040608, "Mainframe Tango: Capture northwest node (Aeon Illuminate) 10": 23040609, "Mainframe Tango: Capture northwest node (Aeon Illuminate) 11": 23040610, "Mainframe Tango: Capture northwest node (Aeon Illuminate) 12": 23040611, "Mainframe Tango: Capture northwest node (Aeon Illuminate) 13": 23040612, "Mainframe Tango: Capture northwest node (Aeon Illuminate) 14": 23040613, "Mainframe Tango: Capture northwest node (Aeon Illuminate) 15": 23040614, "Mainframe Tango: Capture northwest node (Aeon Illuminate) 16": 23040615, "Mainframe Tango: Do not attack main Aeon base (Aeon Illuminate) 1": 23040700, "Mainframe Tango: Do not attack main Aeon base (Aeon Illuminate) 2": 23040701, "Mainframe Tango: Do not attack main Aeon base (Aeon Illuminate) 3": 23040702, "Mainframe Tango: Do not attack main Aeon base (Aeon Illuminate) 4": 23040703, "Mainframe Tango: Do not attack main Aeon base (Aeon Illuminate) 5": 23040704, "Mainframe Tango: Do not attack main Aeon base (Aeon Illuminate) 6": 23040705, "Mainframe Tango: Do not attack main Aeon base (Aeon Illuminate) 7": 23040706, "Mainframe Tango: Do not attack main Aeon base (Aeon Illuminate) 8": 23040707, "Mainframe Tango: Do not attack main Aeon base (Aeon Illuminate) 9": 23040708, "Mainframe Tango: Do not attack main Aeon base (Aeon Illuminate) 10": 23040709, "Mainframe Tango: Do not attack main Aeon base (Aeon Illuminate) 11": 23040710, "Mainframe Tango: Do not attack main Aeon base (Aeon Illuminate) 12": 23040711, "Mainframe Tango: Do not attack main Aeon base (Aeon Illuminate) 13": 23040712, "Mainframe Tango: Do not attack main Aeon base (Aeon Illuminate) 14": 23040713, "Mainframe Tango: Do not attack main Aeon base (Aeon Illuminate) 15": 23040714, "Mainframe Tango: Do not attack main Aeon base (Aeon Illuminate) 16": 23040715, "Mainframe Tango: Kill Aeon Commander (Aeon Illuminate) 1": 23040800, "Mainframe Tango: Kill Aeon Commander (Aeon Illuminate) 2": 23040801, "Mainframe Tango: Kill Aeon Commander (Aeon Illuminate) 3": 23040802, "Mainframe Tango: Kill Aeon Commander (Aeon Illuminate) 4": 23040803, "Mainframe Tango: Kill Aeon Commander (Aeon Illuminate) 5": 23040804, "Mainframe Tango: Kill Aeon Commander (Aeon Illuminate) 6": 23040805, "Mainframe Tango: Kill Aeon Commander (Aeon Illuminate) 7": 23040806, "Mainframe Tango: Kill Aeon Commander (Aeon Illuminate) 8": 23040807, "Mainframe Tango: Kill Aeon Commander (Aeon Illuminate) 9": 23040808, "Mainframe Tango: Kill Aeon Commander (Aeon Illuminate) 10": 23040809, "Mainframe Tango: Kill Aeon Commander (Aeon Illuminate) 11": 23040810, "Mainframe Tango: Kill Aeon Commander (Aeon Illuminate) 12": 23040811, "Mainframe Tango: Kill Aeon Commander (Aeon Illuminate) 13": 23040812, "Mainframe Tango: Kill Aeon Commander (Aeon Illuminate) 14": 23040813, "Mainframe Tango: Kill Aeon Commander (Aeon Illuminate) 15": 23040814, "Mainframe Tango: Kill Aeon Commander (Aeon Illuminate) 16": 23040815, "Unlock: Destroy UEF generators (Aeon Illuminate) 1": 23050000, "Unlock: Destroy UEF generators (Aeon Illuminate) 2": 23050001, "Unlock: Destroy UEF generators (Aeon Illuminate) 3": 23050002, "Unlock: Destroy UEF generators (Aeon Illuminate) 4": 23050003, "Unlock: Destroy UEF generators (Aeon Illuminate) 5": 23050004, "Unlock: Destroy UEF generators (Aeon Illuminate) 6": 23050005, "Unlock: Destroy UEF generators (Aeon Illuminate) 7": 23050006, "Unlock: Destroy UEF generators (Aeon Illuminate) 8": 23050007, "Unlock: Destroy UEF generators (Aeon Illuminate) 9": 23050008, "Unlock: Destroy UEF generators (Aeon Illuminate) 10": 23050009, "Unlock: Destroy UEF generators (Aeon Illuminate) 11": 23050010, "Unlock: Destroy UEF generators (Aeon Illuminate) 12": 23050011, "Unlock: Destroy UEF generators (Aeon Illuminate) 13": 23050012, "Unlock: Destroy UEF generators (Aeon Illuminate) 14": 23050013, "Unlock: Destroy UEF generators (Aeon Illuminate) 15": 23050014, "Unlock: Destroy UEF generators (Aeon Illuminate) 16": 23050015, "Unlock: Destroy UEF shipyards (optional) (Aeon Illuminate) 1": 23050100, "Unlock: Destroy UEF shipyards (optional) (Aeon Illuminate) 2": 23050101, "Unlock: Destroy UEF shipyards (optional) (Aeon Illuminate) 3": 23050102, "Unlock: Destroy UEF shipyards (optional) (Aeon Illuminate) 4": 23050103, "Unlock: Destroy UEF shipyards (optional) (Aeon Illuminate) 5": 23050104, "Unlock: Destroy UEF shipyards (optional) (Aeon Illuminate) 6": 23050105, "Unlock: Destroy UEF shipyards (optional) (Aeon Illuminate) 7": 23050106, "Unlock: Destroy UEF shipyards (optional) (Aeon Illuminate) 8": 23050107, "Unlock: Destroy UEF shipyards (optional) (Aeon Illuminate) 9": 23050108, "Unlock: Destroy UEF shipyards (optional) (Aeon Illuminate) 10": 23050109, "Unlock: Destroy UEF shipyards (optional) (Aeon Illuminate) 11": 23050110, "Unlock: Destroy UEF shipyards (optional) (Aeon Illuminate) 12": 23050111, "Unlock: Destroy UEF shipyards (optional) (Aeon Illuminate) 13": 23050112, "Unlock: Destroy UEF shipyards (optional) (Aeon Illuminate) 14": 23050113, "Unlock: Destroy UEF shipyards (optional) (Aeon Illuminate) 15": 23050114, "Unlock: Destroy UEF shipyards (optional) (Aeon Illuminate) 16": 23050115, "Unlock: Destroy UEF radars (Aeon Illuminate) 1": 23050200, "Unlock: Destroy UEF radars (Aeon Illuminate) 2": 23050201, "Unlock: Destroy UEF radars (Aeon Illuminate) 3": 23050202, "Unlock: Destroy UEF radars (Aeon Illuminate) 4": 23050203, "Unlock: Destroy UEF radars (Aeon Illuminate) 5": 23050204, "Unlock: Destroy UEF radars (Aeon Illuminate) 6": 23050205, "Unlock: Destroy UEF radars (Aeon Illuminate) 7": 23050206, "Unlock: Destroy UEF radars (Aeon Illuminate) 8": 23050207, "Unlock: Destroy UEF radars (Aeon Illuminate) 9": 23050208, "Unlock: Destroy UEF radars (Aeon Illuminate) 10": 23050209, "Unlock: Destroy UEF radars (Aeon Illuminate) 11": 23050210, "Unlock: Destroy UEF radars (Aeon Illuminate) 12": 23050211, "Unlock: Destroy UEF radars (Aeon Illuminate) 13": 23050212, "Unlock: Destroy UEF radars (Aeon Illuminate) 14": 23050213, "Unlock: Destroy UEF radars (Aeon Illuminate) 15": 23050214, "Unlock: Destroy UEF radars (Aeon Illuminate) 16": 23050215, "Unlock: Go to Hex5 (Aeon Illuminate) 1": 23050300, "Unlock: Go to Hex5 (Aeon Illuminate) 2": 23050301, "Unlock: Go to Hex5 (Aeon Illuminate) 3": 23050302, "Unlock: Go to Hex5 (Aeon Illuminate) 4": 23050303, "Unlock: Go to Hex5 (Aeon Illuminate) 5": 23050304, "Unlock: Go to Hex5 (Aeon Illuminate) 6": 23050305, "Unlock: Go to Hex5 (Aeon Illuminate) 7": 23050306, "Unlock: Go to Hex5 (Aeon Illuminate) 8": 23050307, "Unlock: Go to Hex5 (Aeon Illuminate) 9": 23050308, "Unlock: Go to Hex5 (Aeon Illuminate) 10": 23050309, "Unlock: Go to Hex5 (Aeon Illuminate) 11": 23050310, "Unlock: Go to Hex5 (Aeon Illuminate) 12": 23050311, "Unlock: Go to Hex5 (Aeon Illuminate) 13": 23050312, "Unlock: Go to Hex5 (Aeon Illuminate) 14": 23050313, "Unlock: Go to Hex5 (Aeon Illuminate) 15": 23050314, "Unlock: Go to Hex5 (Aeon Illuminate) 16": 23050315, "Unlock: Defend from heavy gunships (Aeon Illuminate) 1": 23050400, "Unlock: Defend from heavy gunships (Aeon Illuminate) 2": 23050401, "Unlock: Defend from heavy gunships (Aeon Illuminate) 3": 23050402, "Unlock: Defend from heavy gunships (Aeon Illuminate) 4": 23050403, "Unlock: Defend from heavy gunships (Aeon Illuminate) 5": 23050404, "Unlock: Defend from heavy gunships (Aeon Illuminate) 6": 23050405, "Unlock: Defend from heavy gunships (Aeon Illuminate) 7": 23050406, "Unlock: Defend from heavy gunships (Aeon Illuminate) 8": 23050407, "Unlock: Defend from heavy gunships (Aeon Illuminate) 9": 23050408, "Unlock: Defend from heavy gunships (Aeon Illuminate) 10": 23050409, "Unlock: Defend from heavy gunships (Aeon Illuminate) 11": 23050410, "Unlock: Defend from heavy gunships (Aeon Illuminate) 12": 23050411, "Unlock: Defend from heavy gunships (Aeon Illuminate) 13": 23050412, "Unlock: Defend from heavy gunships (Aeon Illuminate) 14": 23050413, "Unlock: Defend from heavy gunships (Aeon Illuminate) 15": 23050414, "Unlock: Defend from heavy gunships (Aeon Illuminate) 16": 23050415, "Unlock: Infect UEF landing pad (optional) (Aeon Illuminate) 1": 23050500, "Unlock: Infect UEF landing pad (optional) (Aeon Illuminate) 2": 23050501, "Unlock: Infect UEF landing pad (optional) (Aeon Illuminate) 3": 23050502, "Unlock: Infect UEF landing pad (optional) (Aeon Illuminate) 4": 23050503, "Unlock: Infect UEF landing pad (optional) (Aeon Illuminate) 5": 23050504, "Unlock: Infect UEF landing pad (optional) (Aeon Illuminate) 6": 23050505, "Unlock: Infect UEF landing pad (optional) (Aeon Illuminate) 7": 23050506, "Unlock: Infect UEF landing pad (optional) (Aeon Illuminate) 8": 23050507, "Unlock: Infect UEF landing pad (optional) (Aeon Illuminate) 9": 23050508, "Unlock: Infect UEF landing pad (optional) (Aeon Illuminate) 10": 23050509, "Unlock: Infect UEF landing pad (optional) (Aeon Illuminate) 11": 23050510, "Unlock: Infect UEF landing pad (optional) (Aeon Illuminate) 12": 23050511, "Unlock: Infect UEF landing pad (optional) (Aeon Illuminate) 13": 23050512, "Unlock: Infect UEF landing pad (optional) (Aeon Illuminate) 14": 23050513, "Unlock: Infect UEF landing pad (optional) (Aeon Illuminate) 15": 23050514, "Unlock: Infect UEF landing pad (optional) (Aeon Illuminate) 16": 23050515, "Unlock: This will be retconned later (Aeon Illuminate) 1": 23050600, "Unlock: This will be retconned later (Aeon Illuminate) 2": 23050601, "Unlock: This will be retconned later (Aeon Illuminate) 3": 23050602, "Unlock: This will be retconned later (Aeon Illuminate) 4": 23050603, "Unlock: This will be retconned later (Aeon Illuminate) 5": 23050604, "Unlock: This will be retconned later (Aeon Illuminate) 6": 23050605, "Unlock: This will be retconned later (Aeon Illuminate) 7": 23050606, "Unlock: This will be retconned later (Aeon Illuminate) 8": 23050607, "Unlock: This will be retconned later (Aeon Illuminate) 9": 23050608, "Unlock: This will be retconned later (Aeon Illuminate) 10": 23050609, "Unlock: This will be retconned later (Aeon Illuminate) 11": 23050610, "Unlock: This will be retconned later (Aeon Illuminate) 12": 23050611, "Unlock: This will be retconned later (Aeon Illuminate) 13": 23050612, "Unlock: This will be retconned later (Aeon Illuminate) 14": 23050613, "Unlock: This will be retconned later (Aeon Illuminate) 15": 23050614, "Unlock: This will be retconned later (Aeon Illuminate) 16": 23050615, "Unlock: Kill UEF Commander (Aeon Illuminate) 1": 23050700, "Unlock: Kill UEF Commander (Aeon Illuminate) 2": 23050701, "Unlock: Kill UEF Commander (Aeon Illuminate) 3": 23050702, "Unlock: Kill UEF Commander (Aeon Illuminate) 4": 23050703, "Unlock: Kill UEF Commander (Aeon Illuminate) 5": 23050704, "Unlock: Kill UEF Commander (Aeon Illuminate) 6": 23050705, "Unlock: Kill UEF Commander (Aeon Illuminate) 7": 23050706, "Unlock: Kill UEF Commander (Aeon Illuminate) 8": 23050707, "Unlock: Kill UEF Commander (Aeon Illuminate) 9": 23050708, "Unlock: Kill UEF Commander (Aeon Illuminate) 10": 23050709, "Unlock: Kill UEF Commander (Aeon Illuminate) 11": 23050710, "Unlock: Kill UEF Commander (Aeon Illuminate) 12": 23050711, "Unlock: Kill UEF Commander (Aeon Illuminate) 13": 23050712, "Unlock: Kill UEF Commander (Aeon Illuminate) 14": 23050713, "Unlock: Kill UEF Commander (Aeon Illuminate) 15": 23050714, "Unlock: Kill UEF Commander (Aeon Illuminate) 16": 23050715, "Freedom: Destroy CZAR (Aeon Illuminate) 1": 23060000, "Freedom: Destroy CZAR (Aeon Illuminate) 2": 23060001, "Freedom: Destroy CZAR (Aeon Illuminate) 3": 23060002, "Freedom: Destroy CZAR (Aeon Illuminate) 4": 23060003, "Freedom: Destroy CZAR (Aeon Illuminate) 5": 23060004, "Freedom: Destroy CZAR (Aeon Illuminate) 6": 23060005, "Freedom: Destroy CZAR (Aeon Illuminate) 7": 23060006, "Freedom: Destroy CZAR (Aeon Illuminate) 8": 23060007, "Freedom: Destroy CZAR (Aeon Illuminate) 9": 23060008, "Freedom: Destroy CZAR (Aeon Illuminate) 10": 23060009, "Freedom: Destroy CZAR (Aeon Illuminate) 11": 23060010, "Freedom: Destroy CZAR (Aeon Illuminate) 12": 23060011, "Freedom: Destroy CZAR (Aeon Illuminate) 13": 23060012, "Freedom: Destroy CZAR (Aeon Illuminate) 14": 23060013, "Freedom: Destroy CZAR (Aeon Illuminate) 15": 23060014, "Freedom: Destroy CZAR (Aeon Illuminate) 16": 23060015, "Freedom: Build Quantum Gate (Aeon Illuminate) 1": 23060100, "Freedom: Build Quantum Gate (Aeon Illuminate) 2": 23060101, "Freedom: Build Quantum Gate (Aeon Illuminate) 3": 23060102, "Freedom: Build Quantum Gate (Aeon Illuminate) 4": 23060103, "Freedom: Build Quantum Gate (Aeon Illuminate) 5": 23060104, "Freedom: Build Quantum Gate (Aeon Illuminate) 6": 23060105, "Freedom: Build Quantum Gate (Aeon Illuminate) 7": 23060106, "Freedom: Build Quantum Gate (Aeon Illuminate) 8": 23060107, "Freedom: Build Quantum Gate (Aeon Illuminate) 9": 23060108, "Freedom: Build Quantum Gate (Aeon Illuminate) 10": 23060109, "Freedom: Build Quantum Gate (Aeon Illuminate) 11": 23060110, "Freedom: Build Quantum Gate (Aeon Illuminate) 12": 23060111, "Freedom: Build Quantum Gate (Aeon Illuminate) 13": 23060112, "Freedom: Build Quantum Gate (Aeon Illuminate) 14": 23060113, "Freedom: Build Quantum Gate (Aeon Illuminate) 15": 23060114, "Freedom: Build Quantum Gate (Aeon Illuminate) 16": 23060115, "Freedom: Download Quantum Virus (Aeon Illuminate) 1": 23060200, "Freedom: Download Quantum Virus (Aeon Illuminate) 2": 23060201, "Freedom: Download Quantum Virus (Aeon Illuminate) 3": 23060202, "Freedom: Download Quantum Virus (Aeon Illuminate) 4": 23060203, "Freedom: Download Quantum Virus (Aeon Illuminate) 5": 23060204, "Freedom: Download Quantum Virus (Aeon Illuminate) 6": 23060205, "Freedom: Download Quantum Virus (Aeon Illuminate) 7": 23060206, "Freedom: Download Quantum Virus (Aeon Illuminate) 8": 23060207, "Freedom: Download Quantum Virus (Aeon Illuminate) 9": 23060208, "Freedom: Download Quantum Virus (Aeon Illuminate) 10": 23060209, "Freedom: Download Quantum Virus (Aeon Illuminate) 11": 23060210, "Freedom: Download Quantum Virus (Aeon Illuminate) 12": 23060211, "Freedom: Download Quantum Virus (Aeon Illuminate) 13": 23060212, "Freedom: Download Quantum Virus (Aeon Illuminate) 14": 23060213, "Freedom: Download Quantum Virus (Aeon Illuminate) 15": 23060214, "Freedom: Download Quantum Virus (Aeon Illuminate) 16": 23060215, "Freedom: Capture Black Sun control center (Aeon Illuminate) 1": 23060300, "Freedom: Capture Black Sun control center (Aeon Illuminate) 2": 23060301, "Freedom: Capture Black Sun control center (Aeon Illuminate) 3": 23060302, "Freedom: Capture Black Sun control center (Aeon Illuminate) 4": 23060303, "Freedom: Capture Black Sun control center (Aeon Illuminate) 5": 23060304, "Freedom: Capture Black Sun control center (Aeon Illuminate) 6": 23060305, "Freedom: Capture Black Sun control center (Aeon Illuminate) 7": 23060306, "Freedom: Capture Black Sun control center (Aeon Illuminate) 8": 23060307, "Freedom: Capture Black Sun control center (Aeon Illuminate) 9": 23060308, "Freedom: Capture Black Sun control center (Aeon Illuminate) 10": 23060309, "Freedom: Capture Black Sun control center (Aeon Illuminate) 11": 23060310, "Freedom: Capture Black Sun control center (Aeon Illuminate) 12": 23060311, "Freedom: Capture Black Sun control center (Aeon Illuminate) 13": 23060312, "Freedom: Capture Black Sun control center (Aeon Illuminate) 14": 23060313, "Freedom: Capture Black Sun control center (Aeon Illuminate) 15": 23060314, "Freedom: Capture Black Sun control center (Aeon Illuminate) 16": 23060315, "Freedom: Capture Black Sun (Aeon Illuminate) 1": 23060400, "Freedom: Capture Black Sun (Aeon Illuminate) 2": 23060401, "Freedom: Capture Black Sun (Aeon Illuminate) 3": 23060402, "Freedom: Capture Black Sun (Aeon Illuminate) 4": 23060403, "Freedom: Capture Black Sun (Aeon Illuminate) 5": 23060404, "Freedom: Capture Black Sun (Aeon Illuminate) 6": 23060405, "Freedom: Capture Black Sun (Aeon Illuminate) 7": 23060406, "Freedom: Capture Black Sun (Aeon Illuminate) 8": 23060407, "Freedom: Capture Black Sun (Aeon Illuminate) 9": 23060408, "Freedom: Capture Black Sun (Aeon Illuminate) 10": 23060409, "Freedom: Capture Black Sun (Aeon Illuminate) 11": 23060410, "Freedom: Capture Black Sun (Aeon Illuminate) 12": 23060411, "Freedom: Capture Black Sun (Aeon Illuminate) 13": 23060412, "Freedom: Capture Black Sun (Aeon Illuminate) 14": 23060413, "Freedom: Capture Black Sun (Aeon Illuminate) 15": 23060414, "Freedom: Capture Black Sun (Aeon Illuminate) 16": 23060415, "Freedom: Shoot Black Sun (Aeon Illuminate) 1": 23060500, "Freedom: Shoot Black Sun (Aeon Illuminate) 2": 23060501, "Freedom: Shoot Black Sun (Aeon Illuminate) 3": 23060502, "Freedom: Shoot Black Sun (Aeon Illuminate) 4": 23060503, "Freedom: Shoot Black Sun (Aeon Illuminate) 5": 23060504, "Freedom: Shoot Black Sun (Aeon Illuminate) 6": 23060505, "Freedom: Shoot Black Sun (Aeon Illuminate) 7": 23060506, "Freedom: Shoot Black Sun (Aeon Illuminate) 8": 23060507, "Freedom: Shoot Black Sun (Aeon Illuminate) 9": 23060508, "Freedom: Shoot Black Sun (Aeon Illuminate) 10": 23060509, "Freedom: Shoot Black Sun (Aeon Illuminate) 11": 23060510, "Freedom: Shoot Black Sun (Aeon Illuminate) 12": 23060511, "Freedom: Shoot Black Sun (Aeon Illuminate) 13": 23060512, "Freedom: Shoot Black Sun (Aeon Illuminate) 14": 23060513, "Freedom: Shoot Black Sun (Aeon Illuminate) 15": 23060514, "Freedom: Shoot Black Sun (Aeon Illuminate) 16": 23060515, "Liberation: Build mass (Serafim) 1": 24010000, "Liberation: Build mass (Serafim) 2": 24010001, "Liberation: Build mass (Serafim) 3": 24010002, "Liberation: Build mass (Serafim) 4": 24010003, "Liberation: Build mass (Serafim) 5": 24010004, "Liberation: Build mass (Serafim) 6": 24010005, "Liberation: Build mass (Serafim) 7": 24010006, "Liberation: Build mass (Serafim) 8": 24010007, "Liberation: Build mass (Serafim) 9": 24010008, "Liberation: Build mass (Serafim) 10": 24010009, "Liberation: Build mass (Serafim) 11": 24010010, "Liberation: Build mass (Serafim) 12": 24010011, "Liberation: Build mass (Serafim) 13": 24010012, "Liberation: Build mass (Serafim) 14": 24010013, "Liberation: Build mass (Serafim) 15": 24010014, "Liberation: Build mass (Serafim) 16": 24010015, "Liberation: Build power (Serafim) 1": 24010100, "Liberation: Build power (Serafim) 2": 24010101, "Liberation: Build power (Serafim) 3": 24010102, "Liberation: Build power (Serafim) 4": 24010103, "Liberation: Build power (Serafim) 5": 24010104, "Liberation: Build power (Serafim) 6": 24010105, "Liberation: Build power (Serafim) 7": 24010106, "Liberation: Build power (Serafim) 8": 24010107, "Liberation: Build power (Serafim) 9": 24010108, "Liberation: Build power (Serafim) 10": 24010109, "Liberation: Build power (Serafim) 11": 24010110, "Liberation: Build power (Serafim) 12": 24010111, "Liberation: Build power (Serafim) 13": 24010112, "Liberation: Build power (Serafim) 14": 24010113, "Liberation: Build power (Serafim) 15": 24010114, "Liberation: Build power (Serafim) 16": 24010115, "Liberation: Build air factory (Serafim) 1": 24010200, "Liberation: Build air factory (Serafim) 2": 24010201, "Liberation: Build air factory (Serafim) 3": 24010202, "Liberation: Build air factory (Serafim) 4": 24010203, "Liberation: Build air factory (Serafim) 5": 24010204, "Liberation: Build air factory (Serafim) 6": 24010205, "Liberation: Build air factory (Serafim) 7": 24010206, "Liberation: Build air factory (Serafim) 8": 24010207, "Liberation: Build air factory (Serafim) 9": 24010208, "Liberation: Build air factory (Serafim) 10": 24010209, "Liberation: Build air factory (Serafim) 11": 24010210, "Liberation: Build air factory (Serafim) 12": 24010211, "Liberation: Build air factory (Serafim) 13": 24010212, "Liberation: Build air factory (Serafim) 14": 24010213, "Liberation: Build air factory (Serafim) 15": 24010214, "Liberation: Build air factory (Serafim) 16": 24010215, "Liberation: Build bombers (Serafim) 1": 24010300, "Liberation: Build bombers (Serafim) 2": 24010301, "Liberation: Build bombers (Serafim) 3": 24010302, "Liberation: Build bombers (Serafim) 4": 24010303, "Liberation: Build bombers (Serafim) 5": 24010304, "Liberation: Build bombers (Serafim) 6": 24010305, "Liberation: Build bombers (Serafim) 7": 24010306, "Liberation: Build bombers (Serafim) 8": 24010307, "Liberation: Build bombers (Serafim) 9": 24010308, "Liberation: Build bombers (Serafim) 10": 24010309, "Liberation: Build bombers (Serafim) 11": 24010310, "Liberation: Build bombers (Serafim) 12": 24010311, "Liberation: Build bombers (Serafim) 13": 24010312, "Liberation: Build bombers (Serafim) 14": 24010313, "Liberation: Build bombers (Serafim) 15": 24010314, "Liberation: Build bombers (Serafim) 16": 24010315, "Liberation: Destroy radar defenders (Serafim) 1": 24010400, "Liberation: Destroy radar defenders (Serafim) 2": 24010401, "Liberation: Destroy radar defenders (Serafim) 3": 24010402, "Liberation: Destroy radar defenders (Serafim) 4": 24010403, "Liberation: Destroy radar defenders (Serafim) 5": 24010404, "Liberation: Destroy radar defenders (Serafim) 6": 24010405, "Liberation: Destroy radar defenders (Serafim) 7": 24010406, "Liberation: Destroy radar defenders (Serafim) 8": 24010407, "Liberation: Destroy radar defenders (Serafim) 9": 24010408, "Liberation: Destroy radar defenders (Serafim) 10": 24010409, "Liberation: Destroy radar defenders (Serafim) 11": 24010410, "Liberation: Destroy radar defenders (Serafim) 12": 24010411, "Liberation: Destroy radar defenders (Serafim) 13": 24010412, "Liberation: Destroy radar defenders (Serafim) 14": 24010413, "Liberation: Destroy radar defenders (Serafim) 15": 24010414, "Liberation: Destroy radar defenders (Serafim) 16": 24010415, "Liberation: Capture radars (Serafim) 1": 24010500, "Liberation: Capture radars (Serafim) 2": 24010501, "Liberation: Capture radars (Serafim) 3": 24010502, "Liberation: Capture radars (Serafim) 4": 24010503, "Liberation: Capture radars (Serafim) 5": 24010504, "Liberation: Capture radars (Serafim) 6": 24010505, "Liberation: Capture radars (Serafim) 7": 24010506, "Liberation: Capture radars (Serafim) 8": 24010507, "Liberation: Capture radars (Serafim) 9": 24010508, "Liberation: Capture radars (Serafim) 10": 24010509, "Liberation: Capture radars (Serafim) 11": 24010510, "Liberation: Capture radars (Serafim) 12": 24010511, "Liberation: Capture radars (Serafim) 13": 24010512, "Liberation: Capture radars (Serafim) 14": 24010513, "Liberation: Capture radars (Serafim) 15": 24010514, "Liberation: Capture radars (Serafim) 16": 24010515, "Liberation: Destroy mex (Serafim) 1": 24010600, "Liberation: Destroy mex (Serafim) 2": 24010601, "Liberation: Destroy mex (Serafim) 3": 24010602, "Liberation: Destroy mex (Serafim) 4": 24010603, "Liberation: Destroy mex (Serafim) 5": 24010604, "Liberation: Destroy mex (Serafim) 6": 24010605, "Liberation: Destroy mex (Serafim) 7": 24010606, "Liberation: Destroy mex (Serafim) 8": 24010607, "Liberation: Destroy mex (Serafim) 9": 24010608, "Liberation: Destroy mex (Serafim) 10": 24010609, "Liberation: Destroy mex (Serafim) 11": 24010610, "Liberation: Destroy mex (Serafim) 12": 24010611, "Liberation: Destroy mex (Serafim) 13": 24010612, "Liberation: Destroy mex (Serafim) 14": 24010613, "Liberation: Destroy mex (Serafim) 15": 24010614, "Liberation: Destroy mex (Serafim) 16": 24010615, "Liberation: Destroy UEF defences (Serafim) 1": 24010700, "Liberation: Destroy UEF defences (Serafim) 2": 24010701, "Liberation: Destroy UEF defences (Serafim) 3": 24010702, "Liberation: Destroy UEF defences (Serafim) 4": 24010703, "Liberation: Destroy UEF defences (Serafim) 5": 24010704, "Liberation: Destroy UEF defences (Serafim) 6": 24010705, "Liberation: Destroy UEF defences (Serafim) 7": 24010706, "Liberation: Destroy UEF defences (Serafim) 8": 24010707, "Liberation: Destroy UEF defences (Serafim) 9": 24010708, "Liberation: Destroy UEF defences (Serafim) 10": 24010709, "Liberation: Destroy UEF defences (Serafim) 11": 24010710, "Liberation: Destroy UEF defences (Serafim) 12": 24010711, "Liberation: Destroy UEF defences (Serafim) 13": 24010712, "Liberation: Destroy UEF defences (Serafim) 14": 24010713, "Liberation: Destroy UEF defences (Serafim) 15": 24010714, "Liberation: Destroy UEF defences (Serafim) 16": 24010715, "Liberation: Destroy UEF patrols (Serafim) 1": 24010800, "Liberation: Destroy UEF patrols (Serafim) 2": 24010801, "Liberation: Destroy UEF patrols (Serafim) 3": 24010802, "Liberation: Destroy UEF patrols (Serafim) 4": 24010803, "Liberation: Destroy UEF patrols (Serafim) 5": 24010804, "Liberation: Destroy UEF patrols (Serafim) 6": 24010805, "Liberation: Destroy UEF patrols (Serafim) 7": 24010806, "Liberation: Destroy UEF patrols (Serafim) 8": 24010807, "Liberation: Destroy UEF patrols (Serafim) 9": 24010808, "Liberation: Destroy UEF patrols (Serafim) 10": 24010809, "Liberation: Destroy UEF patrols (Serafim) 11": 24010810, "Liberation: Destroy UEF patrols (Serafim) 12": 24010811, "Liberation: Destroy UEF patrols (Serafim) 13": 24010812, "Liberation: Destroy UEF patrols (Serafim) 14": 24010813, "Liberation: Destroy UEF patrols (Serafim) 15": 24010814, "Liberation: Destroy UEF patrols (Serafim) 16": 24010815, "Liberation: Destroy UEF base defenders (Serafim) 1": 24010900, "Liberation: Destroy UEF base defenders (Serafim) 2": 24010901, "Liberation: Destroy UEF base defenders (Serafim) 3": 24010902, "Liberation: Destroy UEF base defenders (Serafim) 4": 24010903, "Liberation: Destroy UEF base defenders (Serafim) 5": 24010904, "Liberation: Destroy UEF base defenders (Serafim) 6": 24010905, "Liberation: Destroy UEF base defenders (Serafim) 7": 24010906, "Liberation: Destroy UEF base defenders (Serafim) 8": 24010907, "Liberation: Destroy UEF base defenders (Serafim) 9": 24010908, "Liberation: Destroy UEF base defenders (Serafim) 10": 24010909, "Liberation: Destroy UEF base defenders (Serafim) 11": 24010910, "Liberation: Destroy UEF base defenders (Serafim) 12": 24010911, "Liberation: Destroy UEF base defenders (Serafim) 13": 24010912, "Liberation: Destroy UEF base defenders (Serafim) 14": 24010913, "Liberation: Destroy UEF base defenders (Serafim) 15": 24010914, "Liberation: Destroy UEF base defenders (Serafim) 16": 24010915, "Liberation: Destroy UEF base (Serafim) 1": 24011000, "Liberation: Destroy UEF base (Serafim) 2": 24011001, "Liberation: Destroy UEF base (Serafim) 3": 24011002, "Liberation: Destroy UEF base (Serafim) 4": 24011003, "Liberation: Destroy UEF base (Serafim) 5": 24011004, "Liberation: Destroy UEF base (Serafim) 6": 24011005, "Liberation: Destroy UEF base (Serafim) 7": 24011006, "Liberation: Destroy UEF base (Serafim) 8": 24011007, "Liberation: Destroy UEF base (Serafim) 9": 24011008, "Liberation: Destroy UEF base (Serafim) 10": 24011009, "Liberation: Destroy UEF base (Serafim) 11": 24011010, "Liberation: Destroy UEF base (Serafim) 12": 24011011, "Liberation: Destroy UEF base (Serafim) 13": 24011012, "Liberation: Destroy UEF base (Serafim) 14": 24011013, "Liberation: Destroy UEF base (Serafim) 15": 24011014, "Liberation: Destroy UEF base (Serafim) 16": 24011015, "Liberation: Kill Aeon Commander (Serafim) 1": 24011100, "Liberation: Kill Aeon Commander (Serafim) 2": 24011101, "Liberation: Kill Aeon Commander (Serafim) 3": 24011102, "Liberation: Kill Aeon Commander (Serafim) 4": 24011103, "Liberation: Kill Aeon Commander (Serafim) 5": 24011104, "Liberation: Kill Aeon Commander (Serafim) 6": 24011105, "Liberation: Kill Aeon Commander (Serafim) 7": 24011106, "Liberation: Kill Aeon Commander (Serafim) 8": 24011107, "Liberation: Kill Aeon Commander (Serafim) 9": 24011108, "Liberation: Kill Aeon Commander (Serafim) 10": 24011109, "Liberation: Kill Aeon Commander (Serafim) 11": 24011110, "Liberation: Kill Aeon Commander (Serafim) 12": 24011111, "Liberation: Kill Aeon Commander (Serafim) 13": 24011112, "Liberation: Kill Aeon Commander (Serafim) 14": 24011113, "Liberation: Kill Aeon Commander (Serafim) 15": 24011114, "Liberation: Kill Aeon Commander (Serafim) 16": 24011115, "Artifact: Destroy first village defenders (Serafim) 1": 24020000, "Artifact: Destroy first village defenders (Serafim) 2": 24020001, "Artifact: Destroy first village defenders (Serafim) 3": 24020002, "Artifact: Destroy first village defenders (Serafim) 4": 24020003, "Artifact: Destroy first village defenders (Serafim) 5": 24020004, "Artifact: Destroy first village defenders (Serafim) 6": 24020005, "Artifact: Destroy first village defenders (Serafim) 7": 24020006, "Artifact: Destroy first village defenders (Serafim) 8": 24020007, "Artifact: Destroy first village defenders (Serafim) 9": 24020008, "Artifact: Destroy first village defenders (Serafim) 10": 24020009, "Artifact: Destroy first village defenders (Serafim) 11": 24020010, "Artifact: Destroy first village defenders (Serafim) 12": 24020011, "Artifact: Destroy first village defenders (Serafim) 13": 24020012, "Artifact: Destroy first village defenders (Serafim) 14": 24020013, "Artifact: Destroy first village defenders (Serafim) 15": 24020014, "Artifact: Destroy first village defenders (Serafim) 16": 24020015, "Artifact: Destroy first temple (Serafim) 1": 24020100, "Artifact: Destroy first temple (Serafim) 2": 24020101, "Artifact: Destroy first temple (Serafim) 3": 24020102, "Artifact: Destroy first temple (Serafim) 4": 24020103, "Artifact: Destroy first temple (Serafim) 5": 24020104, "Artifact: Destroy first temple (Serafim) 6": 24020105, "Artifact: Destroy first temple (Serafim) 7": 24020106, "Artifact: Destroy first temple (Serafim) 8": 24020107, "Artifact: Destroy first temple (Serafim) 9": 24020108, "Artifact: Destroy first temple (Serafim) 10": 24020109, "Artifact: Destroy first temple (Serafim) 11": 24020110, "Artifact: Destroy first temple (Serafim) 12": 24020111, "Artifact: Destroy first temple (Serafim) 13": 24020112, "Artifact: Destroy first temple (Serafim) 14": 24020113, "Artifact: Destroy first temple (Serafim) 15": 24020114, "Artifact: Destroy first temple (Serafim) 16": 24020115, "Artifact: Protect first artifact (Serafim) 1": 24020200, "Artifact: Protect first artifact (Serafim) 2": 24020201, "Artifact: Protect first artifact (Serafim) 3": 24020202, "Artifact: Protect first artifact (Serafim) 4": 24020203, "Artifact: Protect first artifact (Serafim) 5": 24020204, "Artifact: Protect first artifact (Serafim) 6": 24020205, "Artifact: Protect first artifact (Serafim) 7": 24020206, "Artifact: Protect first artifact (Serafim) 8": 24020207, "Artifact: Protect first artifact (Serafim) 9": 24020208, "Artifact: Protect first artifact (Serafim) 10": 24020209, "Artifact: Protect first artifact (Serafim) 11": 24020210, "Artifact: Protect first artifact (Serafim) 12": 24020211, "Artifact: Protect first artifact (Serafim) 13": 24020212, "Artifact: Protect first artifact (Serafim) 14": 24020213, "Artifact: Protect first artifact (Serafim) 15": 24020214, "Artifact: Protect first artifact (Serafim) 16": 24020215, "Artifact: Find second artifact (Serafim) 1": 24020300, "Artifact: Find second artifact (Serafim) 2": 24020301, "Artifact: Find second artifact (Serafim) 3": 24020302, "Artifact: Find second artifact (Serafim) 4": 24020303, "Artifact: Find second artifact (Serafim) 5": 24020304, "Artifact: Find second artifact (Serafim) 6": 24020305, "Artifact: Find second artifact (Serafim) 7": 24020306, "Artifact: Find second artifact (Serafim) 8": 24020307, "Artifact: Find second artifact (Serafim) 9": 24020308, "Artifact: Find second artifact (Serafim) 10": 24020309, "Artifact: Find second artifact (Serafim) 11": 24020310, "Artifact: Find second artifact (Serafim) 12": 24020311, "Artifact: Find second artifact (Serafim) 13": 24020312, "Artifact: Find second artifact (Serafim) 14": 24020313, "Artifact: Find second artifact (Serafim) 15": 24020314, "Artifact: Find second artifact (Serafim) 16": 24020315, "Artifact: Destroy Aeon reinforcements (Serafim) 1": 24020400, "Artifact: Destroy Aeon reinforcements (Serafim) 2": 24020401, "Artifact: Destroy Aeon reinforcements (Serafim) 3": 24020402, "Artifact: Destroy Aeon reinforcements (Serafim) 4": 24020403, "Artifact: Destroy Aeon reinforcements (Serafim) 5": 24020404, "Artifact: Destroy Aeon reinforcements (Serafim) 6": 24020405, "Artifact: Destroy Aeon reinforcements (Serafim) 7": 24020406, "Artifact: Destroy Aeon reinforcements (Serafim) 8": 24020407, "Artifact: Destroy Aeon reinforcements (Serafim) 9": 24020408, "Artifact: Destroy Aeon reinforcements (Serafim) 10": 24020409, "Artifact: Destroy Aeon reinforcements (Serafim) 11": 24020410, "Artifact: Destroy Aeon reinforcements (Serafim) 12": 24020411, "Artifact: Destroy Aeon reinforcements (Serafim) 13": 24020412, "Artifact: Destroy Aeon reinforcements (Serafim) 14": 24020413, "Artifact: Destroy Aeon reinforcements (Serafim) 15": 24020414, "Artifact: Destroy Aeon reinforcements (Serafim) 16": 24020415, "Artifact: Protect second artifact (Serafim) 1": 24020500, "Artifact: Protect second artifact (Serafim) 2": 24020501, "Artifact: Protect second artifact (Serafim) 3": 24020502, "Artifact: Protect second artifact (Serafim) 4": 24020503, "Artifact: Protect second artifact (Serafim) 5": 24020504, "Artifact: Protect second artifact (Serafim) 6": 24020505, "Artifact: Protect second artifact (Serafim) 7": 24020506, "Artifact: Protect second artifact (Serafim) 8": 24020507, "Artifact: Protect second artifact (Serafim) 9": 24020508, "Artifact: Protect second artifact (Serafim) 10": 24020509, "Artifact: Protect second artifact (Serafim) 11": 24020510, "Artifact: Protect second artifact (Serafim) 12": 24020511, "Artifact: Protect second artifact (Serafim) 13": 24020512, "Artifact: Protect second artifact (Serafim) 14": 24020513, "Artifact: Protect second artifact (Serafim) 15": 24020514, "Artifact: Protect second artifact (Serafim) 16": 24020515, "Artifact: Defend from Aeon attack (Serafim) 1": 24020600, "Artifact: Defend from Aeon attack (Serafim) 2": 24020601, "Artifact: Defend from Aeon attack (Serafim) 3": 24020602, "Artifact: Defend from Aeon attack (Serafim) 4": 24020603, "Artifact: Defend from Aeon attack (Serafim) 5": 24020604, "Artifact: Defend from Aeon attack (Serafim) 6": 24020605, "Artifact: Defend from Aeon attack (Serafim) 7": 24020606, "Artifact: Defend from Aeon attack (Serafim) 8": 24020607, "Artifact: Defend from Aeon attack (Serafim) 9": 24020608, "Artifact: Defend from Aeon attack (Serafim) 10": 24020609, "Artifact: Defend from Aeon attack (Serafim) 11": 24020610, "Artifact: Defend from Aeon attack (Serafim) 12": 24020611, "Artifact: Defend from Aeon attack (Serafim) 13": 24020612, "Artifact: Defend from Aeon attack (Serafim) 14": 24020613, "Artifact: Defend from Aeon attack (Serafim) 15": 24020614, "Artifact: Defend from Aeon attack (Serafim) 16": 24020615, "Artifact: Destroy eastern base (Serafim) 1": 24020700, "Artifact: Destroy eastern base (Serafim) 2": 24020701, "Artifact: Destroy eastern base (Serafim) 3": 24020702, "Artifact: Destroy eastern base (Serafim) 4": 24020703, "Artifact: Destroy eastern base (Serafim) 5": 24020704, "Artifact: Destroy eastern base (Serafim) 6": 24020705, "Artifact: Destroy eastern base (Serafim) 7": 24020706, "Artifact: Destroy eastern base (Serafim) 8": 24020707, "Artifact: Destroy eastern base (Serafim) 9": 24020708, "Artifact: Destroy eastern base (Serafim) 10": 24020709, "Artifact: Destroy eastern base (Serafim) 11": 24020710, "Artifact: Destroy eastern base (Serafim) 12": 24020711, "Artifact: Destroy eastern base (Serafim) 13": 24020712, "Artifact: Destroy eastern base (Serafim) 14": 24020713, "Artifact: Destroy eastern base (Serafim) 15": 24020714, "Artifact: Destroy eastern base (Serafim) 16": 24020715, "Artifact: Destroy navy base (Serafim) 1": 24020800, "Artifact: Destroy navy base (Serafim) 2": 24020801, "Artifact: Destroy navy base (Serafim) 3": 24020802, "Artifact: Destroy navy base (Serafim) 4": 24020803, "Artifact: Destroy navy base (Serafim) 5": 24020804, "Artifact: Destroy navy base (Serafim) 6": 24020805, "Artifact: Destroy navy base (Serafim) 7": 24020806, "Artifact: Destroy navy base (Serafim) 8": 24020807, "Artifact: Destroy navy base (Serafim) 9": 24020808, "Artifact: Destroy navy base (Serafim) 10": 24020809, "Artifact: Destroy navy base (Serafim) 11": 24020810, "Artifact: Destroy navy base (Serafim) 12": 24020811, "Artifact: Destroy navy base (Serafim) 13": 24020812, "Artifact: Destroy navy base (Serafim) 14": 24020813, "Artifact: Destroy navy base (Serafim) 15": 24020814, "Artifact: Destroy navy base (Serafim) 16": 24020815, "Artifact: Protect third artifact (Serafim) 1": 24020900, "Artifact: Protect third artifact (Serafim) 2": 24020901, "Artifact: Protect third artifact (Serafim) 3": 24020902, "Artifact: Protect third artifact (Serafim) 4": 24020903, "Artifact: Protect third artifact (Serafim) 5": 24020904, "Artifact: Protect third artifact (Serafim) 6": 24020905, "Artifact: Protect third artifact (Serafim) 7": 24020906, "Artifact: Protect third artifact (Serafim) 8": 24020907, "Artifact: Protect third artifact (Serafim) 9": 24020908, "Artifact: Protect third artifact (Serafim) 10": 24020909, "Artifact: Protect third artifact (Serafim) 11": 24020910, "Artifact: Protect third artifact (Serafim) 12": 24020911, "Artifact: Protect third artifact (Serafim) 13": 24020912, "Artifact: Protect third artifact (Serafim) 14": 24020913, "Artifact: Protect third artifact (Serafim) 15": 24020914, "Artifact: Protect third artifact (Serafim) 16": 24020915, "Artifact: Kill Aeon Commander (optional) (Serafim) 1": 24021000, "Artifact: Kill Aeon Commander (optional) (Serafim) 2": 24021001, "Artifact: Kill Aeon Commander (optional) (Serafim) 3": 24021002, "Artifact: Kill Aeon Commander (optional) (Serafim) 4": 24021003, "Artifact: Kill Aeon Commander (optional) (Serafim) 5": 24021004, "Artifact: Kill Aeon Commander (optional) (Serafim) 6": 24021005, "Artifact: Kill Aeon Commander (optional) (Serafim) 7": 24021006, "Artifact: Kill Aeon Commander (optional) (Serafim) 8": 24021007, "Artifact: Kill Aeon Commander (optional) (Serafim) 9": 24021008, "Artifact: Kill Aeon Commander (optional) (Serafim) 10": 24021009, "Artifact: Kill Aeon Commander (optional) (Serafim) 11": 24021010, "Artifact: Kill Aeon Commander (optional) (Serafim) 12": 24021011, "Artifact: Kill Aeon Commander (optional) (Serafim) 13": 24021012, "Artifact: Kill Aeon Commander (optional) (Serafim) 14": 24021013, "Artifact: Kill Aeon Commander (optional) (Serafim) 15": 24021014, "Artifact: Kill Aeon Commander (optional) (Serafim) 16": 24021015, "Artifact: Kill Mach (Serafim) 1": 24021100, "Artifact: Kill Mach (Serafim) 2": 24021101, "Artifact: Kill Mach (Serafim) 3": 24021102, "Artifact: Kill Mach (Serafim) 4": 24021103, "Artifact: Kill Mach (Serafim) 5": 24021104, "Artifact: Kill Mach (Serafim) 6": 24021105, "Artifact: Kill Mach (Serafim) 7": 24021106, "Artifact: Kill Mach (Serafim) 8": 24021107, "Artifact: Kill Mach (Serafim) 9": 24021108, "Artifact: Kill Mach (Serafim) 10": 24021109, "Artifact: Kill Mach (Serafim) 11": 24021110, "Artifact: Kill Mach (Serafim) 12": 24021111, "Artifact: Kill Mach (Serafim) 13": 24021112, "Artifact: Kill Mach (Serafim) 14": 24021113, "Artifact: Kill Mach (Serafim) 15": 24021114, "Artifact: Kill Mach (Serafim) 16": 24021115, "Artifact: Go to Gate (Serafim) 1": 24021200, "Artifact: Go to Gate (Serafim) 2": 24021201, "Artifact: Go to Gate (Serafim) 3": 24021202, "Artifact: Go to Gate (Serafim) 4": 24021203, "Artifact: Go to Gate (Serafim) 5": 24021204, "Artifact: Go to Gate (Serafim) 6": 24021205, "Artifact: Go to Gate (Serafim) 7": 24021206, "Artifact: Go to Gate (Serafim) 8": 24021207, "Artifact: Go to Gate (Serafim) 9": 24021208, "Artifact: Go to Gate (Serafim) 10": 24021209, "Artifact: Go to Gate (Serafim) 11": 24021210, "Artifact: Go to Gate (Serafim) 12": 24021211, "Artifact: Go to Gate (Serafim) 13": 24021212, "Artifact: Go to Gate (Serafim) 14": 24021213, "Artifact: Go to Gate (Serafim) 15": 24021214, "Artifact: Go to Gate (Serafim) 16": 24021215, "Defrag: Protect York 18 (Serafim) 1": 24030000, "Defrag: Protect York 18 (Serafim) 2": 24030001, "Defrag: Protect York 18 (Serafim) 3": 24030002, "Defrag: Protect York 18 (Serafim) 4": 24030003, "Defrag: Protect York 18 (Serafim) 5": 24030004, "Defrag: Protect York 18 (Serafim) 6": 24030005, "Defrag: Protect York 18 (Serafim) 7": 24030006, "Defrag: Protect York 18 (Serafim) 8": 24030007, "Defrag: Protect York 18 (Serafim) 9": 24030008, "Defrag: Protect York 18 (Serafim) 10": 24030009, "Defrag: Protect York 18 (Serafim) 11": 24030010, "Defrag: Protect York 18 (Serafim) 12": 24030011, "Defrag: Protect York 18 (Serafim) 13": 24030012, "Defrag: Protect York 18 (Serafim) 14": 24030013, "Defrag: Protect York 18 (Serafim) 15": 24030014, "Defrag: Protect York 18 (Serafim) 16": 24030015, "Defrag: Destroy western UEF base (Serafim) 1": 24030100, "Defrag: Destroy western UEF base (Serafim) 2": 24030101, "Defrag: Destroy western UEF base (Serafim) 3": 24030102, "Defrag: Destroy western UEF base (Serafim) 4": 24030103, "Defrag: Destroy western UEF base (Serafim) 5": 24030104, "Defrag: Destroy western UEF base (Serafim) 6": 24030105, "Defrag: Destroy western UEF base (Serafim) 7": 24030106, "Defrag: Destroy western UEF base (Serafim) 8": 24030107, "Defrag: Destroy western UEF base (Serafim) 9": 24030108, "Defrag: Destroy western UEF base (Serafim) 10": 24030109, "Defrag: Destroy western UEF base (Serafim) 11": 24030110, "Defrag: Destroy western UEF base (Serafim) 12": 24030111, "Defrag: Destroy western UEF base (Serafim) 13": 24030112, "Defrag: Destroy western UEF base (Serafim) 14": 24030113, "Defrag: Destroy western UEF base (Serafim) 15": 24030114, "Defrag: Destroy western UEF base (Serafim) 16": 24030115, "Defrag: Destroy north-western UEF base (Serafim) 1": 24030200, "Defrag: Destroy north-western UEF base (Serafim) 2": 24030201, "Defrag: Destroy north-western UEF base (Serafim) 3": 24030202, "Defrag: Destroy north-western UEF base (Serafim) 4": 24030203, "Defrag: Destroy north-western UEF base (Serafim) 5": 24030204, "Defrag: Destroy north-western UEF base (Serafim) 6": 24030205, "Defrag: Destroy north-western UEF base (Serafim) 7": 24030206, "Defrag: Destroy north-western UEF base (Serafim) 8": 24030207, "Defrag: Destroy north-western UEF base (Serafim) 9": 24030208, "Defrag: Destroy north-western UEF base (Serafim) 10": 24030209, "Defrag: Destroy north-western UEF base (Serafim) 11": 24030210, "Defrag: Destroy north-western UEF base (Serafim) 12": 24030211, "Defrag: Destroy north-western UEF base (Serafim) 13": 24030212, "Defrag: Destroy north-western UEF base (Serafim) 14": 24030213, "Defrag: Destroy north-western UEF base (Serafim) 15": 24030214, "Defrag: Destroy north-western UEF base (Serafim) 16": 24030215, "Defrag: Destroy northern UEF base (Serafim) 1": 24030300, "Defrag: Destroy northern UEF base (Serafim) 2": 24030301, "Defrag: Destroy northern UEF base (Serafim) 3": 24030302, "Defrag: Destroy northern UEF base (Serafim) 4": 24030303, "Defrag: Destroy northern UEF base (Serafim) 5": 24030304, "Defrag: Destroy northern UEF base (Serafim) 6": 24030305, "Defrag: Destroy northern UEF base (Serafim) 7": 24030306, "Defrag: Destroy northern UEF base (Serafim) 8": 24030307, "Defrag: Destroy northern UEF base (Serafim) 9": 24030308, "Defrag: Destroy northern UEF base (Serafim) 10": 24030309, "Defrag: Destroy northern UEF base (Serafim) 11": 24030310, "Defrag: Destroy northern UEF base (Serafim) 12": 24030311, "Defrag: Destroy northern UEF base (Serafim) 13": 24030312, "Defrag: Destroy northern UEF base (Serafim) 14": 24030313, "Defrag: Destroy northern UEF base (Serafim) 15": 24030314, "Defrag: Destroy northern UEF base (Serafim) 16": 24030315, "Defrag: Sink UEF cruiser (Serafim) 1": 24030400, "Defrag: Sink UEF cruiser (Serafim) 2": 24030401, "Defrag: Sink UEF cruiser (Serafim) 3": 24030402, "Defrag: Sink UEF cruiser (Serafim) 4": 24030403, "Defrag: Sink UEF cruiser (Serafim) 5": 24030404, "Defrag: Sink UEF cruiser (Serafim) 6": 24030405, "Defrag: Sink UEF cruiser (Serafim) 7": 24030406, "Defrag: Sink UEF cruiser (Serafim) 8": 24030407, "Defrag: Sink UEF cruiser (Serafim) 9": 24030408, "Defrag: Sink UEF cruiser (Serafim) 10": 24030409, "Defrag: Sink UEF cruiser (Serafim) 11": 24030410, "Defrag: Sink UEF cruiser (Serafim) 12": 24030411, "Defrag: Sink UEF cruiser (Serafim) 13": 24030412, "Defrag: Sink UEF cruiser (Serafim) 14": 24030413, "Defrag: Sink UEF cruiser (Serafim) 15": 24030414, "Defrag: Sink UEF cruiser (Serafim) 16": 24030415, "Defrag: Destroy static artillery (Serafim) 1": 24030500, "Defrag: Destroy static artillery (Serafim) 2": 24030501, "Defrag: Destroy static artillery (Serafim) 3": 24030502, "Defrag: Destroy static artillery (Serafim) 4": 24030503, "Defrag: Destroy static artillery (Serafim) 5": 24030504, "Defrag: Destroy static artillery (Serafim) 6": 24030505, "Defrag: Destroy static artillery (Serafim) 7": 24030506, "Defrag: Destroy static artillery (Serafim) 8": 24030507, "Defrag: Destroy static artillery (Serafim) 9": 24030508, "Defrag: Destroy static artillery (Serafim) 10": 24030509, "Defrag: Destroy static artillery (Serafim) 11": 24030510, "Defrag: Destroy static artillery (Serafim) 12": 24030511, "Defrag: Destroy static artillery (Serafim) 13": 24030512, "Defrag: Destroy static artillery (Serafim) 14": 24030513, "Defrag: Destroy static artillery (Serafim) 15": 24030514, "Defrag: Destroy static artillery (Serafim) 16": 24030515, "Defrag: Escort trucks (Serafim) 1": 24030600, "Defrag: Escort trucks (Serafim) 2": 24030601, "Defrag: Escort trucks (Serafim) 3": 24030602, "Defrag: Escort trucks (Serafim) 4": 24030603, "Defrag: Escort trucks (Serafim) 5": 24030604, "Defrag: Escort trucks (Serafim) 6": 24030605, "Defrag: Escort trucks (Serafim) 7": 24030606, "Defrag: Escort trucks (Serafim) 8": 24030607, "Defrag: Escort trucks (Serafim) 9": 24030608, "Defrag: Escort trucks (Serafim) 10": 24030609, "Defrag: Escort trucks (Serafim) 11": 24030610, "Defrag: Escort trucks (Serafim) 12": 24030611, "Defrag: Escort trucks (Serafim) 13": 24030612, "Defrag: Escort trucks (Serafim) 14": 24030613, "Defrag: Escort trucks (Serafim) 15": 24030614, "Defrag: Escort trucks (Serafim) 16": 24030615, "Defrag: Escort ALL trucks (optional) (Serafim) 1": 24030700, "Defrag: Escort ALL trucks (optional) (Serafim) 2": 24030701, "Defrag: Escort ALL trucks (optional) (Serafim) 3": 24030702, "Defrag: Escort ALL trucks (optional) (Serafim) 4": 24030703, "Defrag: Escort ALL trucks (optional) (Serafim) 5": 24030704, "Defrag: Escort ALL trucks (optional) (Serafim) 6": 24030705, "Defrag: Escort ALL trucks (optional) (Serafim) 7": 24030706, "Defrag: Escort ALL trucks (optional) (Serafim) 8": 24030707, "Defrag: Escort ALL trucks (optional) (Serafim) 9": 24030708, "Defrag: Escort ALL trucks (optional) (Serafim) 10": 24030709, "Defrag: Escort ALL trucks (optional) (Serafim) 11": 24030710, "Defrag: Escort ALL trucks (optional) (Serafim) 12": 24030711, "Defrag: Escort ALL trucks (optional) (Serafim) 13": 24030712, "Defrag: Escort ALL trucks (optional) (Serafim) 14": 24030713, "Defrag: Escort ALL trucks (optional) (Serafim) 15": 24030714, "Defrag: Escort ALL trucks (optional) (Serafim) 16": 24030715, "Defrag: Optional objective  (optional) (Serafim) 1": 24030800, "Defrag: Optional objective  (optional) (Serafim) 2": 24030801, "Defrag: Optional objective  (optional) (Serafim) 3": 24030802, "Defrag: Optional objective  (optional) (Serafim) 4": 24030803, "Defrag: Optional objective  (optional) (Serafim) 5": 24030804, "Defrag: Optional objective  (optional) (Serafim) 6": 24030805, "Defrag: Optional objective  (optional) (Serafim) 7": 24030806, "Defrag: Optional objective  (optional) (Serafim) 8": 24030807, "Defrag: Optional objective  (optional) (Serafim) 9": 24030808, "Defrag: Optional objective  (optional) (Serafim) 10": 24030809, "Defrag: Optional objective  (optional) (Serafim) 11": 24030810, "Defrag: Optional objective  (optional) (Serafim) 12": 24030811, "Defrag: Optional objective  (optional) (Serafim) 13": 24030812, "Defrag: Optional objective  (optional) (Serafim) 14": 24030813, "Defrag: Optional objective  (optional) (Serafim) 15": 24030814, "Defrag: Optional objective  (optional) (Serafim) 16": 24030815, "Defrag: Kill UEF Commander (Serafim) 1": 24030900, "Defrag: Kill UEF Commander (Serafim) 2": 24030901, "Defrag: Kill UEF Commander (Serafim) 3": 24030902, "Defrag: Kill UEF Commander (Serafim) 4": 24030903, "Defrag: Kill UEF Commander (Serafim) 5": 24030904, "Defrag: Kill UEF Commander (Serafim) 6": 24030905, "Defrag: Kill UEF Commander (Serafim) 7": 24030906, "Defrag: Kill UEF Commander (Serafim) 8": 24030907, "Defrag: Kill UEF Commander (Serafim) 9": 24030908, "Defrag: Kill UEF Commander (Serafim) 10": 24030909, "Defrag: Kill UEF Commander (Serafim) 11": 24030910, "Defrag: Kill UEF Commander (Serafim) 12": 24030911, "Defrag: Kill UEF Commander (Serafim) 13": 24030912, "Defrag: Kill UEF Commander (Serafim) 14": 24030913, "Defrag: Kill UEF Commander (Serafim) 15": 24030914, "Defrag: Kill UEF Commander (Serafim) 16": 24030915, "Mainframe Tango: Defeat Aeon Commander (Serafim) 1": 24040000, "Mainframe Tango: Defeat Aeon Commander (Serafim) 2": 24040001, "Mainframe Tango: Defeat Aeon Commander (Serafim) 3": 24040002, "Mainframe Tango: Defeat Aeon Commander (Serafim) 4": 24040003, "Mainframe Tango: Defeat Aeon Commander (Serafim) 5": 24040004, "Mainframe Tango: Defeat Aeon Commander (Serafim) 6": 24040005, "Mainframe Tango: Defeat Aeon Commander (Serafim) 7": 24040006, "Mainframe Tango: Defeat Aeon Commander (Serafim) 8": 24040007, "Mainframe Tango: Defeat Aeon Commander (Serafim) 9": 24040008, "Mainframe Tango: Defeat Aeon Commander (Serafim) 10": 24040009, "Mainframe Tango: Defeat Aeon Commander (Serafim) 11": 24040010, "Mainframe Tango: Defeat Aeon Commander (Serafim) 12": 24040011, "Mainframe Tango: Defeat Aeon Commander (Serafim) 13": 24040012, "Mainframe Tango: Defeat Aeon Commander (Serafim) 14": 24040013, "Mainframe Tango: Defeat Aeon Commander (Serafim) 15": 24040014, "Mainframe Tango: Defeat Aeon Commander (Serafim) 16": 24040015, "Mainframe Tango: Capture Network Node (Serafim) 1": 24040100, "Mainframe Tango: Capture Network Node (Serafim) 2": 24040101, "Mainframe Tango: Capture Network Node (Serafim) 3": 24040102, "Mainframe Tango: Capture Network Node (Serafim) 4": 24040103, "Mainframe Tango: Capture Network Node (Serafim) 5": 24040104, "Mainframe Tango: Capture Network Node (Serafim) 6": 24040105, "Mainframe Tango: Capture Network Node (Serafim) 7": 24040106, "Mainframe Tango: Capture Network Node (Serafim) 8": 24040107, "Mainframe Tango: Capture Network Node (Serafim) 9": 24040108, "Mainframe Tango: Capture Network Node (Serafim) 10": 24040109, "Mainframe Tango: Capture Network Node (Serafim) 11": 24040110, "Mainframe Tango: Capture Network Node (Serafim) 12": 24040111, "Mainframe Tango: Capture Network Node (Serafim) 13": 24040112, "Mainframe Tango: Capture Network Node (Serafim) 14": 24040113, "Mainframe Tango: Capture Network Node (Serafim) 15": 24040114, "Mainframe Tango: Capture Network Node (Serafim) 16": 24040115, "Mainframe Tango: Save Network Node (Serafim) 1": 24040200, "Mainframe Tango: Save Network Node (Serafim) 2": 24040201, "Mainframe Tango: Save Network Node (Serafim) 3": 24040202, "Mainframe Tango: Save Network Node (Serafim) 4": 24040203, "Mainframe Tango: Save Network Node (Serafim) 5": 24040204, "Mainframe Tango: Save Network Node (Serafim) 6": 24040205, "Mainframe Tango: Save Network Node (Serafim) 7": 24040206, "Mainframe Tango: Save Network Node (Serafim) 8": 24040207, "Mainframe Tango: Save Network Node (Serafim) 9": 24040208, "Mainframe Tango: Save Network Node (Serafim) 10": 24040209, "Mainframe Tango: Save Network Node (Serafim) 11": 24040210, "Mainframe Tango: Save Network Node (Serafim) 12": 24040211, "Mainframe Tango: Save Network Node (Serafim) 13": 24040212, "Mainframe Tango: Save Network Node (Serafim) 14": 24040213, "Mainframe Tango: Save Network Node (Serafim) 15": 24040214, "Mainframe Tango: Save Network Node (Serafim) 16": 24040215, "Mainframe Tango: Save 80% civilian buildings (optional) (Serafim) 1": 24040300, "Mainframe Tango: Save 80% civilian buildings (optional) (Serafim) 2": 24040301, "Mainframe Tango: Save 80% civilian buildings (optional) (Serafim) 3": 24040302, "Mainframe Tango: Save 80% civilian buildings (optional) (Serafim) 4": 24040303, "Mainframe Tango: Save 80% civilian buildings (optional) (Serafim) 5": 24040304, "Mainframe Tango: Save 80% civilian buildings (optional) (Serafim) 6": 24040305, "Mainframe Tango: Save 80% civilian buildings (optional) (Serafim) 7": 24040306, "Mainframe Tango: Save 80% civilian buildings (optional) (Serafim) 8": 24040307, "Mainframe Tango: Save 80% civilian buildings (optional) (Serafim) 9": 24040308, "Mainframe Tango: Save 80% civilian buildings (optional) (Serafim) 10": 24040309, "Mainframe Tango: Save 80% civilian buildings (optional) (Serafim) 11": 24040310, "Mainframe Tango: Save 80% civilian buildings (optional) (Serafim) 12": 24040311, "Mainframe Tango: Save 80% civilian buildings (optional) (Serafim) 13": 24040312, "Mainframe Tango: Save 80% civilian buildings (optional) (Serafim) 14": 24040313, "Mainframe Tango: Save 80% civilian buildings (optional) (Serafim) 15": 24040314, "Mainframe Tango: Save 80% civilian buildings (optional) (Serafim) 16": 24040315, "Mainframe Tango: Survive attacks (Serafim) 1": 24040400, "Mainframe Tango: Survive attacks (Serafim) 2": 24040401, "Mainframe Tango: Survive attacks (Serafim) 3": 24040402, "Mainframe Tango: Survive attacks (Serafim) 4": 24040403, "Mainframe Tango: Survive attacks (Serafim) 5": 24040404, "Mainframe Tango: Survive attacks (Serafim) 6": 24040405, "Mainframe Tango: Survive attacks (Serafim) 7": 24040406, "Mainframe Tango: Survive attacks (Serafim) 8": 24040407, "Mainframe Tango: Survive attacks (Serafim) 9": 24040408, "Mainframe Tango: Survive attacks (Serafim) 10": 24040409, "Mainframe Tango: Survive attacks (Serafim) 11": 24040410, "Mainframe Tango: Survive attacks (Serafim) 12": 24040411, "Mainframe Tango: Survive attacks (Serafim) 13": 24040412, "Mainframe Tango: Survive attacks (Serafim) 14": 24040413, "Mainframe Tango: Survive attacks (Serafim) 15": 24040414, "Mainframe Tango: Survive attacks (Serafim) 16": 24040415, "Mainframe Tango: Capture northeast node (Serafim) 1": 24040500, "Mainframe Tango: Capture northeast node (Serafim) 2": 24040501, "Mainframe Tango: Capture northeast node (Serafim) 3": 24040502, "Mainframe Tango: Capture northeast node (Serafim) 4": 24040503, "Mainframe Tango: Capture northeast node (Serafim) 5": 24040504, "Mainframe Tango: Capture northeast node (Serafim) 6": 24040505, "Mainframe Tango: Capture northeast node (Serafim) 7": 24040506, "Mainframe Tango: Capture northeast node (Serafim) 8": 24040507, "Mainframe Tango: Capture northeast node (Serafim) 9": 24040508, "Mainframe Tango: Capture northeast node (Serafim) 10": 24040509, "Mainframe Tango: Capture northeast node (Serafim) 11": 24040510, "Mainframe Tango: Capture northeast node (Serafim) 12": 24040511, "Mainframe Tango: Capture northeast node (Serafim) 13": 24040512, "Mainframe Tango: Capture northeast node (Serafim) 14": 24040513, "Mainframe Tango: Capture northeast node (Serafim) 15": 24040514, "Mainframe Tango: Capture northeast node (Serafim) 16": 24040515, "Mainframe Tango: Capture northwest node (Serafim) 1": 24040600, "Mainframe Tango: Capture northwest node (Serafim) 2": 24040601, "Mainframe Tango: Capture northwest node (Serafim) 3": 24040602, "Mainframe Tango: Capture northwest node (Serafim) 4": 24040603, "Mainframe Tango: Capture northwest node (Serafim) 5": 24040604, "Mainframe Tango: Capture northwest node (Serafim) 6": 24040605, "Mainframe Tango: Capture northwest node (Serafim) 7": 24040606, "Mainframe Tango: Capture northwest node (Serafim) 8": 24040607, "Mainframe Tango: Capture northwest node (Serafim) 9": 24040608, "Mainframe Tango: Capture northwest node (Serafim) 10": 24040609, "Mainframe Tango: Capture northwest node (Serafim) 11": 24040610, "Mainframe Tango: Capture northwest node (Serafim) 12": 24040611, "Mainframe Tango: Capture northwest node (Serafim) 13": 24040612, "Mainframe Tango: Capture northwest node (Serafim) 14": 24040613, "Mainframe Tango: Capture northwest node (Serafim) 15": 24040614, "Mainframe Tango: Capture northwest node (Serafim) 16": 24040615, "Mainframe Tango: Do not attack main Aeon base (Serafim) 1": 24040700, "Mainframe Tango: Do not attack main Aeon base (Serafim) 2": 24040701, "Mainframe Tango: Do not attack main Aeon base (Serafim) 3": 24040702, "Mainframe Tango: Do not attack main Aeon base (Serafim) 4": 24040703, "Mainframe Tango: Do not attack main Aeon base (Serafim) 5": 24040704, "Mainframe Tango: Do not attack main Aeon base (Serafim) 6": 24040705, "Mainframe Tango: Do not attack main Aeon base (Serafim) 7": 24040706, "Mainframe Tango: Do not attack main Aeon base (Serafim) 8": 24040707, "Mainframe Tango: Do not attack main Aeon base (Serafim) 9": 24040708, "Mainframe Tango: Do not attack main Aeon base (Serafim) 10": 24040709, "Mainframe Tango: Do not attack main Aeon base (Serafim) 11": 24040710, "Mainframe Tango: Do not attack main Aeon base (Serafim) 12": 24040711, "Mainframe Tango: Do not attack main Aeon base (Serafim) 13": 24040712, "Mainframe Tango: Do not attack main Aeon base (Serafim) 14": 24040713, "Mainframe Tango: Do not attack main Aeon base (Serafim) 15": 24040714, "Mainframe Tango: Do not attack main Aeon base (Serafim) 16": 24040715, "Mainframe Tango: Kill Aeon Commander (Serafim) 1": 24040800, "Mainframe Tango: Kill Aeon Commander (Serafim) 2": 24040801, "Mainframe Tango: Kill Aeon Commander (Serafim) 3": 24040802, "Mainframe Tango: Kill Aeon Commander (Serafim) 4": 24040803, "Mainframe Tango: Kill Aeon Commander (Serafim) 5": 24040804, "Mainframe Tango: Kill Aeon Commander (Serafim) 6": 24040805, "Mainframe Tango: Kill Aeon Commander (Serafim) 7": 24040806, "Mainframe Tango: Kill Aeon Commander (Serafim) 8": 24040807, "Mainframe Tango: Kill Aeon Commander (Serafim) 9": 24040808, "Mainframe Tango: Kill Aeon Commander (Serafim) 10": 24040809, "Mainframe Tango: Kill Aeon Commander (Serafim) 11": 24040810, "Mainframe Tango: Kill Aeon Commander (Serafim) 12": 24040811, "Mainframe Tango: Kill Aeon Commander (Serafim) 13": 24040812, "Mainframe Tango: Kill Aeon Commander (Serafim) 14": 24040813, "Mainframe Tango: Kill Aeon Commander (Serafim) 15": 24040814, "Mainframe Tango: Kill Aeon Commander (Serafim) 16": 24040815, "Unlock: Destroy UEF generators (Serafim) 1": 24050000, "Unlock: Destroy UEF generators (Serafim) 2": 24050001, "Unlock: Destroy UEF generators (Serafim) 3": 24050002, "Unlock: Destroy UEF generators (Serafim) 4": 24050003, "Unlock: Destroy UEF generators (Serafim) 5": 24050004, "Unlock: Destroy UEF generators (Serafim) 6": 24050005, "Unlock: Destroy UEF generators (Serafim) 7": 24050006, "Unlock: Destroy UEF generators (Serafim) 8": 24050007, "Unlock: Destroy UEF generators (Serafim) 9": 24050008, "Unlock: Destroy UEF generators (Serafim) 10": 24050009, "Unlock: Destroy UEF generators (Serafim) 11": 24050010, "Unlock: Destroy UEF generators (Serafim) 12": 24050011, "Unlock: Destroy UEF generators (Serafim) 13": 24050012, "Unlock: Destroy UEF generators (Serafim) 14": 24050013, "Unlock: Destroy UEF generators (Serafim) 15": 24050014, "Unlock: Destroy UEF generators (Serafim) 16": 24050015, "Unlock: Destroy UEF shipyards (optional) (Serafim) 1": 24050100, "Unlock: Destroy UEF shipyards (optional) (Serafim) 2": 24050101, "Unlock: Destroy UEF shipyards (optional) (Serafim) 3": 24050102, "Unlock: Destroy UEF shipyards (optional) (Serafim) 4": 24050103, "Unlock: Destroy UEF shipyards (optional) (Serafim) 5": 24050104, "Unlock: Destroy UEF shipyards (optional) (Serafim) 6": 24050105, "Unlock: Destroy UEF shipyards (optional) (Serafim) 7": 24050106, "Unlock: Destroy UEF shipyards (optional) (Serafim) 8": 24050107, "Unlock: Destroy UEF shipyards (optional) (Serafim) 9": 24050108, "Unlock: Destroy UEF shipyards (optional) (Serafim) 10": 24050109, "Unlock: Destroy UEF shipyards (optional) (Serafim) 11": 24050110, "Unlock: Destroy UEF shipyards (optional) (Serafim) 12": 24050111, "Unlock: Destroy UEF shipyards (optional) (Serafim) 13": 24050112, "Unlock: Destroy UEF shipyards (optional) (Serafim) 14": 24050113, "Unlock: Destroy UEF shipyards (optional) (Serafim) 15": 24050114, "Unlock: Destroy UEF shipyards (optional) (Serafim) 16": 24050115, "Unlock: Destroy UEF radars (Serafim) 1": 24050200, "Unlock: Destroy UEF radars (Serafim) 2": 24050201, "Unlock: Destroy UEF radars (Serafim) 3": 24050202, "Unlock: Destroy UEF radars (Serafim) 4": 24050203, "Unlock: Destroy UEF radars (Serafim) 5": 24050204, "Unlock: Destroy UEF radars (Serafim) 6": 24050205, "Unlock: Destroy UEF radars (Serafim) 7": 24050206, "Unlock: Destroy UEF radars (Serafim) 8": 24050207, "Unlock: Destroy UEF radars (Serafim) 9": 24050208, "Unlock: Destroy UEF radars (Serafim) 10": 24050209, "Unlock: Destroy UEF radars (Serafim) 11": 24050210, "Unlock: Destroy UEF radars (Serafim) 12": 24050211, "Unlock: Destroy UEF radars (Serafim) 13": 24050212, "Unlock: Destroy UEF radars (Serafim) 14": 24050213, "Unlock: Destroy UEF radars (Serafim) 15": 24050214, "Unlock: Destroy UEF radars (Serafim) 16": 24050215, "Unlock: Go to Hex5 (Serafim) 1": 24050300, "Unlock: Go to Hex5 (Serafim) 2": 24050301, "Unlock: Go to Hex5 (Serafim) 3": 24050302, "Unlock: Go to Hex5 (Serafim) 4": 24050303, "Unlock: Go to Hex5 (Serafim) 5": 24050304, "Unlock: Go to Hex5 (Serafim) 6": 24050305, "Unlock: Go to Hex5 (Serafim) 7": 24050306, "Unlock: Go to Hex5 (Serafim) 8": 24050307, "Unlock: Go to Hex5 (Serafim) 9": 24050308, "Unlock: Go to Hex5 (Serafim) 10": 24050309, "Unlock: Go to Hex5 (Serafim) 11": 24050310, "Unlock: Go to Hex5 (Serafim) 12": 24050311, "Unlock: Go to Hex5 (Serafim) 13": 24050312, "Unlock: Go to Hex5 (Serafim) 14": 24050313, "Unlock: Go to Hex5 (Serafim) 15": 24050314, "Unlock: Go to Hex5 (Serafim) 16": 24050315, "Unlock: Defend from heavy gunships (Serafim) 1": 24050400, "Unlock: Defend from heavy gunships (Serafim) 2": 24050401, "Unlock: Defend from heavy gunships (Serafim) 3": 24050402, "Unlock: Defend from heavy gunships (Serafim) 4": 24050403, "Unlock: Defend from heavy gunships (Serafim) 5": 24050404, "Unlock: Defend from heavy gunships (Serafim) 6": 24050405, "Unlock: Defend from heavy gunships (Serafim) 7": 24050406, "Unlock: Defend from heavy gunships (Serafim) 8": 24050407, "Unlock: Defend from heavy gunships (Serafim) 9": 24050408, "Unlock: Defend from heavy gunships (Serafim) 10": 24050409, "Unlock: Defend from heavy gunships (Serafim) 11": 24050410, "Unlock: Defend from heavy gunships (Serafim) 12": 24050411, "Unlock: Defend from heavy gunships (Serafim) 13": 24050412, "Unlock: Defend from heavy gunships (Serafim) 14": 24050413, "Unlock: Defend from heavy gunships (Serafim) 15": 24050414, "Unlock: Defend from heavy gunships (Serafim) 16": 24050415, "Unlock: Infect UEF landing pad (optional) (Serafim) 1": 24050500, "Unlock: Infect UEF landing pad (optional) (Serafim) 2": 24050501, "Unlock: Infect UEF landing pad (optional) (Serafim) 3": 24050502, "Unlock: Infect UEF landing pad (optional) (Serafim) 4": 24050503, "Unlock: Infect UEF landing pad (optional) (Serafim) 5": 24050504, "Unlock: Infect UEF landing pad (optional) (Serafim) 6": 24050505, "Unlock: Infect UEF landing pad (optional) (Serafim) 7": 24050506, "Unlock: Infect UEF landing pad (optional) (Serafim) 8": 24050507, "Unlock: Infect UEF landing pad (optional) (Serafim) 9": 24050508, "Unlock: Infect UEF landing pad (optional) (Serafim) 10": 24050509, "Unlock: Infect UEF landing pad (optional) (Serafim) 11": 24050510, "Unlock: Infect UEF landing pad (optional) (Serafim) 12": 24050511, "Unlock: Infect UEF landing pad (optional) (Serafim) 13": 24050512, "Unlock: Infect UEF landing pad (optional) (Serafim) 14": 24050513, "Unlock: Infect UEF landing pad (optional) (Serafim) 15": 24050514, "Unlock: Infect UEF landing pad (optional) (Serafim) 16": 24050515, "Unlock: This will be retconned later (Serafim) 1": 24050600, "Unlock: This will be retconned later (Serafim) 2": 24050601, "Unlock: This will be retconned later (Serafim) 3": 24050602, "Unlock: This will be retconned later (Serafim) 4": 24050603, "Unlock: This will be retconned later (Serafim) 5": 24050604, "Unlock: This will be retconned later (Serafim) 6": 24050605, "Unlock: This will be retconned later (Serafim) 7": 24050606, "Unlock: This will be retconned later (Serafim) 8": 24050607, "Unlock: This will be retconned later (Serafim) 9": 24050608, "Unlock: This will be retconned later (Serafim) 10": 24050609, "Unlock: This will be retconned later (Serafim) 11": 24050610, "Unlock: This will be retconned later (Serafim) 12": 24050611, "Unlock: This will be retconned later (Serafim) 13": 24050612, "Unlock: This will be retconned later (Serafim) 14": 24050613, "Unlock: This will be retconned later (Serafim) 15": 24050614, "Unlock: This will be retconned later (Serafim) 16": 24050615, "Unlock: Kill UEF Commander (Serafim) 1": 24050700, "Unlock: Kill UEF Commander (Serafim) 2": 24050701, "Unlock: Kill UEF Commander (Serafim) 3": 24050702, "Unlock: Kill UEF Commander (Serafim) 4": 24050703, "Unlock: Kill UEF Commander (Serafim) 5": 24050704, "Unlock: Kill UEF Commander (Serafim) 6": 24050705, "Unlock: Kill UEF Commander (Serafim) 7": 24050706, "Unlock: Kill UEF Commander (Serafim) 8": 24050707, "Unlock: Kill UEF Commander (Serafim) 9": 24050708, "Unlock: Kill UEF Commander (Serafim) 10": 24050709, "Unlock: Kill UEF Commander (Serafim) 11": 24050710, "Unlock: Kill UEF Commander (Serafim) 12": 24050711, "Unlock: Kill UEF Commander (Serafim) 13": 24050712, "Unlock: Kill UEF Commander (Serafim) 14": 24050713, "Unlock: Kill UEF Commander (Serafim) 15": 24050714, "Unlock: Kill UEF Commander (Serafim) 16": 24050715, "Freedom: Destroy CZAR (Serafim) 1": 24060000, "Freedom: Destroy CZAR (Serafim) 2": 24060001, "Freedom: Destroy CZAR (Serafim) 3": 24060002, "Freedom: Destroy CZAR (Serafim) 4": 24060003, "Freedom: Destroy CZAR (Serafim) 5": 24060004, "Freedom: Destroy CZAR (Serafim) 6": 24060005, "Freedom: Destroy CZAR (Serafim) 7": 24060006, "Freedom: Destroy CZAR (Serafim) 8": 24060007, "Freedom: Destroy CZAR (Serafim) 9": 24060008, "Freedom: Destroy CZAR (Serafim) 10": 24060009, "Freedom: Destroy CZAR (Serafim) 11": 24060010, "Freedom: Destroy CZAR (Serafim) 12": 24060011, "Freedom: Destroy CZAR (Serafim) 13": 24060012, "Freedom: Destroy CZAR (Serafim) 14": 24060013, "Freedom: Destroy CZAR (Serafim) 15": 24060014, "Freedom: Destroy CZAR (Serafim) 16": 24060015, "Freedom: Build Quantum Gate (Serafim) 1": 24060100, "Freedom: Build Quantum Gate (Serafim) 2": 24060101, "Freedom: Build Quantum Gate (Serafim) 3": 24060102, "Freedom: Build Quantum Gate (Serafim) 4": 24060103, "Freedom: Build Quantum Gate (Serafim) 5": 24060104, "Freedom: Build Quantum Gate (Serafim) 6": 24060105, "Freedom: Build Quantum Gate (Serafim) 7": 24060106, "Freedom: Build Quantum Gate (Serafim) 8": 24060107, "Freedom: Build Quantum Gate (Serafim) 9": 24060108, "Freedom: Build Quantum Gate (Serafim) 10": 24060109, "Freedom: Build Quantum Gate (Serafim) 11": 24060110, "Freedom: Build Quantum Gate (Serafim) 12": 24060111, "Freedom: Build Quantum Gate (Serafim) 13": 24060112, "Freedom: Build Quantum Gate (Serafim) 14": 24060113, "Freedom: Build Quantum Gate (Serafim) 15": 24060114, "Freedom: Build Quantum Gate (Serafim) 16": 24060115, "Freedom: Download Quantum Virus (Serafim) 1": 24060200, "Freedom: Download Quantum Virus (Serafim) 2": 24060201, "Freedom: Download Quantum Virus (Serafim) 3": 24060202, "Freedom: Download Quantum Virus (Serafim) 4": 24060203, "Freedom: Download Quantum Virus (Serafim) 5": 24060204, "Freedom: Download Quantum Virus (Serafim) 6": 24060205, "Freedom: Download Quantum Virus (Serafim) 7": 24060206, "Freedom: Download Quantum Virus (Serafim) 8": 24060207, "Freedom: Download Quantum Virus (Serafim) 9": 24060208, "Freedom: Download Quantum Virus (Serafim) 10": 24060209, "Freedom: Download Quantum Virus (Serafim) 11": 24060210, "Freedom: Download Quantum Virus (Serafim) 12": 24060211, "Freedom: Download Quantum Virus (Serafim) 13": 24060212, "Freedom: Download Quantum Virus (Serafim) 14": 24060213, "Freedom: Download Quantum Virus (Serafim) 15": 24060214, "Freedom: Download Quantum Virus (Serafim) 16": 24060215, "Freedom: Capture Black Sun control center (Serafim) 1": 24060300, "Freedom: Capture Black Sun control center (Serafim) 2": 24060301, "Freedom: Capture Black Sun control center (Serafim) 3": 24060302, "Freedom: Capture Black Sun control center (Serafim) 4": 24060303, "Freedom: Capture Black Sun control center (Serafim) 5": 24060304, "Freedom: Capture Black Sun control center (Serafim) 6": 24060305, "Freedom: Capture Black Sun control center (Serafim) 7": 24060306, "Freedom: Capture Black Sun control center (Serafim) 8": 24060307, "Freedom: Capture Black Sun control center (Serafim) 9": 24060308, "Freedom: Capture Black Sun control center (Serafim) 10": 24060309, "Freedom: Capture Black Sun control center (Serafim) 11": 24060310, "Freedom: Capture Black Sun control center (Serafim) 12": 24060311, "Freedom: Capture Black Sun control center (Serafim) 13": 24060312, "Freedom: Capture Black Sun control center (Serafim) 14": 24060313, "Freedom: Capture Black Sun control center (Serafim) 15": 24060314, "Freedom: Capture Black Sun control center (Serafim) 16": 24060315, "Freedom: Capture Black Sun (Serafim) 1": 24060400, "Freedom: Capture Black Sun (Serafim) 2": 24060401, "Freedom: Capture Black Sun (Serafim) 3": 24060402, "Freedom: Capture Black Sun (Serafim) 4": 24060403, "Freedom: Capture Black Sun (Serafim) 5": 24060404, "Freedom: Capture Black Sun (Serafim) 6": 24060405, "Freedom: Capture Black Sun (Serafim) 7": 24060406, "Freedom: Capture Black Sun (Serafim) 8": 24060407, "Freedom: Capture Black Sun (Serafim) 9": 24060408, "Freedom: Capture Black Sun (Serafim) 10": 24060409, "Freedom: Capture Black Sun (Serafim) 11": 24060410, "Freedom: Capture Black Sun (Serafim) 12": 24060411, "Freedom: Capture Black Sun (Serafim) 13": 24060412, "Freedom: Capture Black Sun (Serafim) 14": 24060413, "Freedom: Capture Black Sun (Serafim) 15": 24060414, "Freedom: Capture Black Sun (Serafim) 16": 24060415, "Freedom: Shoot Black Sun (Serafim) 1": 24060500, "Freedom: Shoot Black Sun (Serafim) 2": 24060501, "Freedom: Shoot Black Sun (Serafim) 3": 24060502, "Freedom: Shoot Black Sun (Serafim) 4": 24060503, "Freedom: Shoot Black Sun (Serafim) 5": 24060504, "Freedom: Shoot Black Sun (Serafim) 6": 24060505, "Freedom: Shoot Black Sun (Serafim) 7": 24060506, "Freedom: Shoot Black Sun (Serafim) 8": 24060507, "Freedom: Shoot Black Sun (Serafim) 9": 24060508, "Freedom: Shoot Black Sun (Serafim) 10": 24060509, "Freedom: Shoot Black Sun (Serafim) 11": 24060510, "Freedom: Shoot Black Sun (Serafim) 12": 24060511, "Freedom: Shoot Black Sun (Serafim) 13": 24060512, "Freedom: Shoot Black Sun (Serafim) 14": 24060513, "Freedom: Shoot Black Sun (Serafim) 15": 24060514, "Freedom: Shoot Black Sun (Serafim) 16": 24060515, }

class SupComLocation(Location):
    game = "Supreme Commander"

class SupComItem(Item):
    game = "Supreme Commander"

THE_GRID = []

def makeEverything(world: SupComWorld) -> None:

    levelsTier1FOREVER = []
    levelsTier1 = []
    levelsTier2 = []
    levelsTier3 = []
    levelsTier4 = []
    if not world.options.randfacs:
        levelsTier1.append("Liberation (Cybran)")
        levelsTier1FOREVER.append("Liberation (Cybran)")
        levelsTier2.append("Liberation (Cybran)")
        levelsTier3.append("Liberation (Cybran)")
        levelsTier2.append("Artifact (Cybran)")
        levelsTier3.append("Artifact (Cybran)")
        levelsTier2.append("Defrag (Cybran)")
        levelsTier3.append("Defrag (Cybran)")
        levelsTier3.append("Mainframe Tango (Cybran)")
        levelsTier3.append("Unlock (Cybran)")
        levelsTier4.append("Freedom (Cybran)")
        levelsTier3.append("Freedom (Cybran)")
    elif world.options.mapset == Mapset.option_unique:
        temp = world.random.randrange(0, len(world.options.faction.value))
        if world.options.faction.value[temp] == "uef":
            levelsTier1.append("Liberation (UEF)")
            levelsTier1FOREVER.append("Liberation (UEF)")
            levelsTier2.append("Liberation (UEF)")
            levelsTier3.append("Liberation (UEF)")
        elif  world.options.faction.value[temp] == "cybran":
            levelsTier1.append("Liberation (Cybran)")
            levelsTier1FOREVER.append("Liberation (Cybran)")
            levelsTier2.append("Liberation (Cybran)")
            levelsTier3.append("Liberation (Cybran)")
        elif  world.options.faction.value[temp] == "aeon":
            levelsTier1.append("Liberation (Aeon)")
            levelsTier1FOREVER.append("Liberation (Aeon)")
            levelsTier2.append("Liberation (Aeon)")
            levelsTier3.append("Liberation (Aeon)")
        elif  world.options.faction.value[temp] == "sera":
            levelsTier1.append("Liberation (Sera)")
            levelsTier1FOREVER.append("Liberation (Sera)")
            levelsTier2.append("Liberation (Sera)")
            levelsTier3.append("Liberation (Sera)")
        temp = world.random.randrange(0, len(world.options.faction.value))
        if world.options.faction.value[temp] == "uef":
            levelsTier2.append("Artifact (UEF)")
            levelsTier3.append("Artifact (UEF)")
        elif  world.options.faction.value[temp] == "cybran":
            levelsTier2.append("Artifact (Cybran)")
            levelsTier3.append("Artifact (Cybran)")
        elif  world.options.faction.value[temp] == "aeon":
            levelsTier2.append("Artifact (Aeon)")
            levelsTier3.append("Artifact (Aeon)")
        elif  world.options.faction.value[temp] == "sera":
            levelsTier2.append("Artifact (Sera)")
            levelsTier3.append("Artifact (Sera)")
        temp = world.random.randrange(0, len(world.options.faction.value))
        if world.options.faction.value[temp] == "uef":
            levelsTier2.append("Defrag (UEF)")
            levelsTier3.append("Defrag (UEF)")
        elif  world.options.faction.value[temp] == "cybran":
            levelsTier2.append("Defrag (Cybran)")
            levelsTier3.append("Defrag (Cybran)")
        elif  world.options.faction.value[temp] == "aeon":
            levelsTier2.append("Defrag (Aeon)")
            levelsTier3.append("Defrag (Aeon)")
        elif  world.options.faction.value[temp] == "sera":
            levelsTier2.append("Defrag (Sera)")
            levelsTier3.append("Defrag (Sera)")
        temp = world.random.randrange(0, len(world.options.faction.value))
        if world.options.faction.value[temp] == "uef":
            levelsTier3.append("Mainframe Tango (UEF)")
        elif  world.options.faction.value[temp] == "cybran":
            levelsTier3.append("Mainframe Tango (Cybran)")
        elif  world.options.faction.value[temp] == "aeon":
            levelsTier3.append("Mainframe Tango (Aeon)")
        elif  world.options.faction.value[temp] == "sera":
            levelsTier3.append("Mainframe Tango (Sera)")
        temp = world.random.randrange(0, len(world.options.faction.value))
        if world.options.faction.value[temp] == "uef":
            levelsTier3.append("Unlock (UEF)")
        elif  world.options.faction.value[temp] == "cybran":
            levelsTier3.append("Unlock (Cybran)")
        elif  world.options.faction.value[temp] == "aeon":
            levelsTier3.append("Unlock (Aeon)")
        elif  world.options.faction.value[temp] == "sera":
            levelsTier3.append("Unlock (Sera)")
        temp = world.random.randrange(0, len(world.options.faction.value))
        if world.options.faction.value[temp] == "uef":
            levelsTier4.append("Freedom (UEF)")
            levelsTier3.append("Freedom (UEF)")
        elif  world.options.faction.value[temp] == "cybran":
            levelsTier4.append("Freedom (Cybran)")
            levelsTier3.append("Freedom (Cybran)")
        elif  world.options.faction.value[temp] == "aeon":
            levelsTier4.append("Freedom (Aeon)")
            levelsTier3.append("Freedom (Aeon)")
        elif  world.options.faction.value[temp] == "sera":
            levelsTier4.append("Freedom (Sera)")
            levelsTier3.append("Freedom (Sera)")
    else:
        if "uef" in world.options.faction:
            levelsTier1.append("Liberation (UEF)")
            levelsTier1FOREVER.append("Liberation (UEF)")
            levelsTier2.append("Liberation (UEF)")
            levelsTier3.append("Liberation (UEF)")
        if "cybran" in world.options.faction:
            levelsTier1.append("Liberation (Cybran)")
            levelsTier1FOREVER.append("Liberation (Cybran)")
            levelsTier2.append("Liberation (Cybran)")
            levelsTier3.append("Liberation (Cybran)")
        if "aeon" in world.options.faction:
            levelsTier1.append("Liberation (Aeon)")
            levelsTier1FOREVER.append("Liberation (Aeon)")
            levelsTier2.append("Liberation (Aeon)")
            levelsTier3.append("Liberation (Aeon)")
        if "sera" in world.options.faction:
            levelsTier1.append("Liberation (Sera)")
            levelsTier1FOREVER.append("Liberation (Sera)")
            levelsTier2.append("Liberation (Sera)")
            levelsTier3.append("Liberation (Sera)")
        if "uef" in world.options.faction:
            levelsTier2.append("Artifact (UEF)")
            levelsTier3.append("Artifact (UEF)")
        if "cybran" in world.options.faction:
            levelsTier2.append("Artifact (Cybran)")
            levelsTier3.append("Artifact (Cybran)")
        if "aeon" in world.options.faction:
            levelsTier2.append("Artifact (Aeon)")
            levelsTier3.append("Artifact (Aeon)")
        if "sera" in world.options.faction:
            levelsTier2.append("Artifact (Sera)")
            levelsTier3.append("Artifact (Sera)")
        if "uef" in world.options.faction:
            levelsTier2.append("Defrag (UEF)")
            levelsTier3.append("Defrag (UEF)")
        if "cybran" in world.options.faction:
            levelsTier2.append("Defrag (Cybran)")
            levelsTier3.append("Defrag (Cybran)")
        if "aeon" in world.options.faction:
            levelsTier2.append("Defrag (Aeon)")
            levelsTier3.append("Defrag (Aeon)")
        if "sera" in world.options.faction:
            levelsTier2.append("Defrag (Sera)")
            levelsTier3.append("Defrag (Sera)")
        if "uef" in world.options.faction:
            levelsTier3.append("Mainframe Tango (UEF)")
        if "cybran" in world.options.faction:
            levelsTier3.append("Mainframe Tango (Cybran)")
        if "aeon" in world.options.faction:
            levelsTier3.append("Mainframe Tango (Aeon)")
        if "sera" in world.options.faction:
            levelsTier3.append("Mainframe Tango (Sera)")
        if "uef" in world.options.faction:
            levelsTier3.append("Unlock (UEF)")
        if "cybran" in world.options.faction:
            levelsTier3.append("Unlock (Cybran)")
        if "aeon" in world.options.faction:
            levelsTier3.append("Unlock (Aeon)")
        if "sera" in world.options.faction:
            levelsTier3.append("Unlock (Sera)")
        if "uef" in world.options.faction:
            levelsTier4.append("Freedom (UEF)")
            levelsTier3.append("Freedom (UEF)")
        if "cybran" in world.options.faction:
            levelsTier4.append("Freedom (Cybran)")
            levelsTier3.append("Freedom (Cybran)")
        if "aeon" in world.options.faction:
            levelsTier4.append("Freedom (Aeon)")
            levelsTier3.append("Freedom (Aeon)")
        if "sera" in world.options.faction:
            levelsTier4.append("Freedom (Sera)")
            levelsTier3.append("Freedom (Sera)")

    amountOfLevels = len(levelsTier3)
    AllLevelsListToCheckRegionCreation = []
    possibleAnswers = []
    for i in range(1, amountOfLevels + 1):
        if amountOfLevels % i == 0:
            possibleAnswers.append(i)
            if amountOfLevels / i == i:
                possibleAnswers.append(i)
    Width = possibleAnswers[int(len(possibleAnswers) / 2)]
    Height = possibleAnswers[int(len(possibleAnswers) / 2) - 1]

    THE_GRID = [["" for i in range(Height)] for j in range(Width)]
    temp = world.random.randrange(0,len(levelsTier1))
    THE_GRID[0][0] = levelsTier1[temp]
    AllLevelsListToCheckRegionCreation.append(levelsTier1[temp])
    levelsTier3.remove(levelsTier1[temp])
    levelsTier2.remove(levelsTier1[temp])
    levelsTier1.remove(levelsTier1[temp])
    temp = world.random.randrange(0,len(levelsTier2))
    THE_GRID[0][1] = levelsTier2[temp]
    AllLevelsListToCheckRegionCreation.append(levelsTier2[temp])
    levelsTier3.remove(levelsTier2[temp])
    levelsTier2.remove(levelsTier2[temp])
    temp = world.random.randrange(0,len(levelsTier2))
    THE_GRID[1][0] = levelsTier2[temp]
    AllLevelsListToCheckRegionCreation.append(levelsTier2[temp])
    levelsTier3.remove(levelsTier2[temp])
    levelsTier2.remove(levelsTier2[temp])
    temp = world.random.randrange(0,len(levelsTier4))
    THE_GRID[Width - 1][Height - 1] = levelsTier4[temp]
    AllLevelsListToCheckRegionCreation.append(levelsTier4[temp])
    levelsTier3.remove(levelsTier4[temp])
    levelsTier4.remove(levelsTier4[temp])

    for i in range(Width):
        for j in range(Height):
            CheckFilled = bool(not((i == 0 and j == 0) or (i == 1 and j == 0) or (i == 0 and j == 1) or (i == Width - 1 and j == Height - 1)))
            if CheckFilled:
                temp = world.random.randrange(0,len(levelsTier3))
                THE_GRID[i][j] = levelsTier3[temp]
                AllLevelsListToCheckRegionCreation.append(levelsTier3[temp])
                levelsTier3.remove(levelsTier3[temp])

    world.THE_GRID = THE_GRID

    DictionaryOfRegions = {}
    if "Liberation (UEF)" in AllLevelsListToCheckRegionCreation:
        LiberationUEF0 = Region("Liberation: Build mass (UEF)", world.player, world.multiworld)
        DictionaryOfRegions["Liberation: Build mass (UEF)"] = LiberationUEF0
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Liberation: Build mass (UEF) " + str(index)
            objID = "210100"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            LiberationUEF0.add_locations({lname: int(objID)}, SupComLocation)

    if "Liberation (UEF)" in AllLevelsListToCheckRegionCreation:
        LiberationUEF1 = Region("Liberation: Build power (UEF)", world.player, world.multiworld)
        DictionaryOfRegions["Liberation: Build power (UEF)"] = LiberationUEF1
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Liberation: Build power (UEF) " + str(index)
            objID = "210101"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            LiberationUEF1.add_locations({lname: int(objID)}, SupComLocation)

    if "Liberation (UEF)" in AllLevelsListToCheckRegionCreation:
        LiberationUEF2 = Region("Liberation: Build air factory (UEF)", world.player, world.multiworld)
        DictionaryOfRegions["Liberation: Build air factory (UEF)"] = LiberationUEF2
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Liberation: Build air factory (UEF) " + str(index)
            objID = "210102"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            LiberationUEF2.add_locations({lname: int(objID)}, SupComLocation)

    if "Liberation (UEF)" in AllLevelsListToCheckRegionCreation:
        LiberationUEF3 = Region("Liberation: Build bombers (UEF)", world.player, world.multiworld)
        DictionaryOfRegions["Liberation: Build bombers (UEF)"] = LiberationUEF3
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Liberation: Build bombers (UEF) " + str(index)
            objID = "210103"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            LiberationUEF3.add_locations({lname: int(objID)}, SupComLocation)

    if "Liberation (UEF)" in AllLevelsListToCheckRegionCreation:
        LiberationUEF4 = Region("Liberation: Destroy radar defenders (UEF)", world.player, world.multiworld)
        DictionaryOfRegions["Liberation: Destroy radar defenders (UEF)"] = LiberationUEF4
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Liberation: Destroy radar defenders (UEF) " + str(index)
            objID = "210104"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            LiberationUEF4.add_locations({lname: int(objID)}, SupComLocation)

    if "Liberation (UEF)" in AllLevelsListToCheckRegionCreation:
        LiberationUEF5 = Region("Liberation: Capture radars (UEF)", world.player, world.multiworld)
        DictionaryOfRegions["Liberation: Capture radars (UEF)"] = LiberationUEF5
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Liberation: Capture radars (UEF) " + str(index)
            objID = "210105"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            LiberationUEF5.add_locations({lname: int(objID)}, SupComLocation)

    if "Liberation (UEF)" in AllLevelsListToCheckRegionCreation:
        LiberationUEF6 = Region("Liberation: Destroy mex (UEF)", world.player, world.multiworld)
        DictionaryOfRegions["Liberation: Destroy mex (UEF)"] = LiberationUEF6
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Liberation: Destroy mex (UEF) " + str(index)
            objID = "210106"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            LiberationUEF6.add_locations({lname: int(objID)}, SupComLocation)

    if "Liberation (UEF)" in AllLevelsListToCheckRegionCreation:
        LiberationUEF7 = Region("Liberation: Destroy UEF defences (UEF)", world.player, world.multiworld)
        DictionaryOfRegions["Liberation: Destroy UEF defences (UEF)"] = LiberationUEF7
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Liberation: Destroy UEF defences (UEF) " + str(index)
            objID = "210107"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            LiberationUEF7.add_locations({lname: int(objID)}, SupComLocation)

    if "Liberation (UEF)" in AllLevelsListToCheckRegionCreation:
        LiberationUEF8 = Region("Liberation: Destroy UEF patrols (UEF)", world.player, world.multiworld)
        DictionaryOfRegions["Liberation: Destroy UEF patrols (UEF)"] = LiberationUEF8
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Liberation: Destroy UEF patrols (UEF) " + str(index)
            objID = "210108"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            LiberationUEF8.add_locations({lname: int(objID)}, SupComLocation)

    if "Liberation (UEF)" in AllLevelsListToCheckRegionCreation:
        LiberationUEF9 = Region("Liberation: Destroy UEF base defenders (UEF)", world.player, world.multiworld)
        DictionaryOfRegions["Liberation: Destroy UEF base defenders (UEF)"] = LiberationUEF9
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Liberation: Destroy UEF base defenders (UEF) " + str(index)
            objID = "210109"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            LiberationUEF9.add_locations({lname: int(objID)}, SupComLocation)

    if "Liberation (UEF)" in AllLevelsListToCheckRegionCreation:
        LiberationUEF10 = Region("Liberation: Destroy UEF base (UEF)", world.player, world.multiworld)
        DictionaryOfRegions["Liberation: Destroy UEF base (UEF)"] = LiberationUEF10
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Liberation: Destroy UEF base (UEF) " + str(index)
            objID = "210110"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            LiberationUEF10.add_locations({lname: int(objID)}, SupComLocation)

    if "Liberation (UEF)" in AllLevelsListToCheckRegionCreation:
        LiberationUEF11 = Region("Liberation: Kill Aeon Commander (UEF)", world.player, world.multiworld)
        DictionaryOfRegions["Liberation: Kill Aeon Commander (UEF)"] = LiberationUEF11
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Liberation: Kill Aeon Commander (UEF) " + str(index)
            objID = "210111"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            LiberationUEF11.add_locations({lname: int(objID)}, SupComLocation)

    if "Artifact (UEF)" in AllLevelsListToCheckRegionCreation:
        ArtifactUEF0 = Region("Artifact: Destroy first village defenders (UEF)", world.player, world.multiworld)
        DictionaryOfRegions["Artifact: Destroy first village defenders (UEF)"] = ArtifactUEF0
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Artifact: Destroy first village defenders (UEF) " + str(index)
            objID = "210200"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            ArtifactUEF0.add_locations({lname: int(objID)}, SupComLocation)

    if "Artifact (UEF)" in AllLevelsListToCheckRegionCreation:
        ArtifactUEF1 = Region("Artifact: Destroy first temple (UEF)", world.player, world.multiworld)
        DictionaryOfRegions["Artifact: Destroy first temple (UEF)"] = ArtifactUEF1
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Artifact: Destroy first temple (UEF) " + str(index)
            objID = "210201"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            ArtifactUEF1.add_locations({lname: int(objID)}, SupComLocation)

    if "Artifact (UEF)" in AllLevelsListToCheckRegionCreation:
        ArtifactUEF2 = Region("Artifact: Protect first artifact (UEF)", world.player, world.multiworld)
        DictionaryOfRegions["Artifact: Protect first artifact (UEF)"] = ArtifactUEF2
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Artifact: Protect first artifact (UEF) " + str(index)
            objID = "210202"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            ArtifactUEF2.add_locations({lname: int(objID)}, SupComLocation)

    if "Artifact (UEF)" in AllLevelsListToCheckRegionCreation:
        ArtifactUEF3 = Region("Artifact: Find second artifact (UEF)", world.player, world.multiworld)
        DictionaryOfRegions["Artifact: Find second artifact (UEF)"] = ArtifactUEF3
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Artifact: Find second artifact (UEF) " + str(index)
            objID = "210203"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            ArtifactUEF3.add_locations({lname: int(objID)}, SupComLocation)

    if "Artifact (UEF)" in AllLevelsListToCheckRegionCreation:
        ArtifactUEF4 = Region("Artifact: Destroy Aeon reinforcements (UEF)", world.player, world.multiworld)
        DictionaryOfRegions["Artifact: Destroy Aeon reinforcements (UEF)"] = ArtifactUEF4
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Artifact: Destroy Aeon reinforcements (UEF) " + str(index)
            objID = "210204"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            ArtifactUEF4.add_locations({lname: int(objID)}, SupComLocation)

    if "Artifact (UEF)" in AllLevelsListToCheckRegionCreation:
        ArtifactUEF5 = Region("Artifact: Protect second artifact (UEF)", world.player, world.multiworld)
        DictionaryOfRegions["Artifact: Protect second artifact (UEF)"] = ArtifactUEF5
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Artifact: Protect second artifact (UEF) " + str(index)
            objID = "210205"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            ArtifactUEF5.add_locations({lname: int(objID)}, SupComLocation)

    if "Artifact (UEF)" in AllLevelsListToCheckRegionCreation:
        ArtifactUEF6 = Region("Artifact: Defend from Aeon attack (UEF)", world.player, world.multiworld)
        DictionaryOfRegions["Artifact: Defend from Aeon attack (UEF)"] = ArtifactUEF6
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Artifact: Defend from Aeon attack (UEF) " + str(index)
            objID = "210206"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            ArtifactUEF6.add_locations({lname: int(objID)}, SupComLocation)

    if "Artifact (UEF)" in AllLevelsListToCheckRegionCreation:
        ArtifactUEF7 = Region("Artifact: Destroy eastern base (UEF)", world.player, world.multiworld)
        DictionaryOfRegions["Artifact: Destroy eastern base (UEF)"] = ArtifactUEF7
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Artifact: Destroy eastern base (UEF) " + str(index)
            objID = "210207"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            ArtifactUEF7.add_locations({lname: int(objID)}, SupComLocation)

    if "Artifact (UEF)" in AllLevelsListToCheckRegionCreation:
        ArtifactUEF8 = Region("Artifact: Destroy navy base (UEF)", world.player, world.multiworld)
        DictionaryOfRegions["Artifact: Destroy navy base (UEF)"] = ArtifactUEF8
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Artifact: Destroy navy base (UEF) " + str(index)
            objID = "210208"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            ArtifactUEF8.add_locations({lname: int(objID)}, SupComLocation)

    if "Artifact (UEF)" in AllLevelsListToCheckRegionCreation:
        ArtifactUEF9 = Region("Artifact: Protect third artifact (UEF)", world.player, world.multiworld)
        DictionaryOfRegions["Artifact: Protect third artifact (UEF)"] = ArtifactUEF9
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Artifact: Protect third artifact (UEF) " + str(index)
            objID = "210209"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            ArtifactUEF9.add_locations({lname: int(objID)}, SupComLocation)

    if "Artifact (UEF)" in AllLevelsListToCheckRegionCreation:
        ArtifactUEF10 = Region("Artifact: Kill Aeon Commander (optional) (UEF)", world.player, world.multiworld)
        DictionaryOfRegions["Artifact: Kill Aeon Commander (optional) (UEF)"] = ArtifactUEF10
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Artifact: Kill Aeon Commander (optional) (UEF) " + str(index)
            objID = "210210"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            ArtifactUEF10.add_locations({lname: int(objID)}, SupComLocation)

    if "Artifact (UEF)" in AllLevelsListToCheckRegionCreation:
        ArtifactUEF11 = Region("Artifact: Kill Mach (UEF)", world.player, world.multiworld)
        DictionaryOfRegions["Artifact: Kill Mach (UEF)"] = ArtifactUEF11
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Artifact: Kill Mach (UEF) " + str(index)
            objID = "210211"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            ArtifactUEF11.add_locations({lname: int(objID)}, SupComLocation)

    if "Artifact (UEF)" in AllLevelsListToCheckRegionCreation:
        ArtifactUEF12 = Region("Artifact: Go to Gate (UEF)", world.player, world.multiworld)
        DictionaryOfRegions["Artifact: Go to Gate (UEF)"] = ArtifactUEF12
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Artifact: Go to Gate (UEF) " + str(index)
            objID = "210212"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            ArtifactUEF12.add_locations({lname: int(objID)}, SupComLocation)

    if "Defrag (UEF)" in AllLevelsListToCheckRegionCreation:
        DefragUEF0 = Region("Defrag: Protect York 18 (UEF)", world.player, world.multiworld)
        DictionaryOfRegions["Defrag: Protect York 18 (UEF)"] = DefragUEF0
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Defrag: Protect York 18 (UEF) " + str(index)
            objID = "210300"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            DefragUEF0.add_locations({lname: int(objID)}, SupComLocation)

    if "Defrag (UEF)" in AllLevelsListToCheckRegionCreation:
        DefragUEF1 = Region("Defrag: Destroy western UEF base (UEF)", world.player, world.multiworld)
        DictionaryOfRegions["Defrag: Destroy western UEF base (UEF)"] = DefragUEF1
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Defrag: Destroy western UEF base (UEF) " + str(index)
            objID = "210301"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            DefragUEF1.add_locations({lname: int(objID)}, SupComLocation)

    if "Defrag (UEF)" in AllLevelsListToCheckRegionCreation:
        DefragUEF2 = Region("Defrag: Destroy north-western UEF base (UEF)", world.player, world.multiworld)
        DictionaryOfRegions["Defrag: Destroy north-western UEF base (UEF)"] = DefragUEF2
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Defrag: Destroy north-western UEF base (UEF) " + str(index)
            objID = "210302"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            DefragUEF2.add_locations({lname: int(objID)}, SupComLocation)

    if "Defrag (UEF)" in AllLevelsListToCheckRegionCreation:
        DefragUEF3 = Region("Defrag: Destroy northern UEF base (UEF)", world.player, world.multiworld)
        DictionaryOfRegions["Defrag: Destroy northern UEF base (UEF)"] = DefragUEF3
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Defrag: Destroy northern UEF base (UEF) " + str(index)
            objID = "210303"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            DefragUEF3.add_locations({lname: int(objID)}, SupComLocation)

    if "Defrag (UEF)" in AllLevelsListToCheckRegionCreation:
        DefragUEF4 = Region("Defrag: Sink UEF cruiser (UEF)", world.player, world.multiworld)
        DictionaryOfRegions["Defrag: Sink UEF cruiser (UEF)"] = DefragUEF4
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Defrag: Sink UEF cruiser (UEF) " + str(index)
            objID = "210304"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            DefragUEF4.add_locations({lname: int(objID)}, SupComLocation)

    if "Defrag (UEF)" in AllLevelsListToCheckRegionCreation:
        DefragUEF5 = Region("Defrag: Destroy static artillery (UEF)", world.player, world.multiworld)
        DictionaryOfRegions["Defrag: Destroy static artillery (UEF)"] = DefragUEF5
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Defrag: Destroy static artillery (UEF) " + str(index)
            objID = "210305"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            DefragUEF5.add_locations({lname: int(objID)}, SupComLocation)

    if "Defrag (UEF)" in AllLevelsListToCheckRegionCreation:
        DefragUEF6 = Region("Defrag: Escort trucks (UEF)", world.player, world.multiworld)
        DictionaryOfRegions["Defrag: Escort trucks (UEF)"] = DefragUEF6
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Defrag: Escort trucks (UEF) " + str(index)
            objID = "210306"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            DefragUEF6.add_locations({lname: int(objID)}, SupComLocation)

    if "Defrag (UEF)" in AllLevelsListToCheckRegionCreation:
        DefragUEF7 = Region("Defrag: Escort ALL trucks (optional) (UEF)", world.player, world.multiworld)
        DictionaryOfRegions["Defrag: Escort ALL trucks (optional) (UEF)"] = DefragUEF7
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Defrag: Escort ALL trucks (optional) (UEF) " + str(index)
            objID = "210307"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            DefragUEF7.add_locations({lname: int(objID)}, SupComLocation)

    if "Defrag (UEF)" in AllLevelsListToCheckRegionCreation:
        DefragUEF8 = Region("Defrag: Optional objective  (optional) (UEF)", world.player, world.multiworld)
        DictionaryOfRegions["Defrag: Optional objective  (optional) (UEF)"] = DefragUEF8
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Defrag: Optional objective  (optional) (UEF) " + str(index)
            objID = "210308"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            DefragUEF8.add_locations({lname: int(objID)}, SupComLocation)

    if "Defrag (UEF)" in AllLevelsListToCheckRegionCreation:
        DefragUEF9 = Region("Defrag: Kill UEF Commander (UEF)", world.player, world.multiworld)
        DictionaryOfRegions["Defrag: Kill UEF Commander (UEF)"] = DefragUEF9
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Defrag: Kill UEF Commander (UEF) " + str(index)
            objID = "210309"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            DefragUEF9.add_locations({lname: int(objID)}, SupComLocation)

    if "Mainframe Tango (UEF)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoUEF0 = Region("Mainframe Tango: Defeat Aeon Commander (UEF)", world.player, world.multiworld)
        DictionaryOfRegions["Mainframe Tango: Defeat Aeon Commander (UEF)"] = MainframeTangoUEF0
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Mainframe Tango: Defeat Aeon Commander (UEF) " + str(index)
            objID = "210400"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            MainframeTangoUEF0.add_locations({lname: int(objID)}, SupComLocation)

    if "Mainframe Tango (UEF)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoUEF1 = Region("Mainframe Tango: Capture Network Node (UEF)", world.player, world.multiworld)
        DictionaryOfRegions["Mainframe Tango: Capture Network Node (UEF)"] = MainframeTangoUEF1
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Mainframe Tango: Capture Network Node (UEF) " + str(index)
            objID = "210401"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            MainframeTangoUEF1.add_locations({lname: int(objID)}, SupComLocation)

    if "Mainframe Tango (UEF)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoUEF2 = Region("Mainframe Tango: Save Network Node (UEF)", world.player, world.multiworld)
        DictionaryOfRegions["Mainframe Tango: Save Network Node (UEF)"] = MainframeTangoUEF2
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Mainframe Tango: Save Network Node (UEF) " + str(index)
            objID = "210402"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            MainframeTangoUEF2.add_locations({lname: int(objID)}, SupComLocation)

    if "Mainframe Tango (UEF)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoUEF3 = Region("Mainframe Tango: Save 80% civilian buildings (optional) (UEF)", world.player, world.multiworld)
        DictionaryOfRegions["Mainframe Tango: Save 80% civilian buildings (optional) (UEF)"] = MainframeTangoUEF3
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Mainframe Tango: Save 80% civilian buildings (optional) (UEF) " + str(index)
            objID = "210403"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            MainframeTangoUEF3.add_locations({lname: int(objID)}, SupComLocation)

    if "Mainframe Tango (UEF)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoUEF4 = Region("Mainframe Tango: Survive attacks (UEF)", world.player, world.multiworld)
        DictionaryOfRegions["Mainframe Tango: Survive attacks (UEF)"] = MainframeTangoUEF4
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Mainframe Tango: Survive attacks (UEF) " + str(index)
            objID = "210404"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            MainframeTangoUEF4.add_locations({lname: int(objID)}, SupComLocation)

    if "Mainframe Tango (UEF)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoUEF5 = Region("Mainframe Tango: Capture northeast node (UEF)", world.player, world.multiworld)
        DictionaryOfRegions["Mainframe Tango: Capture northeast node (UEF)"] = MainframeTangoUEF5
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Mainframe Tango: Capture northeast node (UEF) " + str(index)
            objID = "210405"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            MainframeTangoUEF5.add_locations({lname: int(objID)}, SupComLocation)

    if "Mainframe Tango (UEF)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoUEF6 = Region("Mainframe Tango: Capture northwest node (UEF)", world.player, world.multiworld)
        DictionaryOfRegions["Mainframe Tango: Capture northwest node (UEF)"] = MainframeTangoUEF6
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Mainframe Tango: Capture northwest node (UEF) " + str(index)
            objID = "210406"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            MainframeTangoUEF6.add_locations({lname: int(objID)}, SupComLocation)

    if "Mainframe Tango (UEF)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoUEF7 = Region("Mainframe Tango: Do not attack main Aeon base (UEF)", world.player, world.multiworld)
        DictionaryOfRegions["Mainframe Tango: Do not attack main Aeon base (UEF)"] = MainframeTangoUEF7
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Mainframe Tango: Do not attack main Aeon base (UEF) " + str(index)
            objID = "210407"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            MainframeTangoUEF7.add_locations({lname: int(objID)}, SupComLocation)

    if "Mainframe Tango (UEF)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoUEF8 = Region("Mainframe Tango: Kill Aeon Commander (UEF)", world.player, world.multiworld)
        DictionaryOfRegions["Mainframe Tango: Kill Aeon Commander (UEF)"] = MainframeTangoUEF8
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Mainframe Tango: Kill Aeon Commander (UEF) " + str(index)
            objID = "210408"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            MainframeTangoUEF8.add_locations({lname: int(objID)}, SupComLocation)

    if "Unlock (UEF)" in AllLevelsListToCheckRegionCreation:
        UnlockUEF0 = Region("Unlock: Destroy UEF generators (UEF)", world.player, world.multiworld)
        DictionaryOfRegions["Unlock: Destroy UEF generators (UEF)"] = UnlockUEF0
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Unlock: Destroy UEF generators (UEF) " + str(index)
            objID = "210500"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            UnlockUEF0.add_locations({lname: int(objID)}, SupComLocation)

    if "Unlock (UEF)" in AllLevelsListToCheckRegionCreation:
        UnlockUEF1 = Region("Unlock: Destroy UEF shipyards (optional) (UEF)", world.player, world.multiworld)
        DictionaryOfRegions["Unlock: Destroy UEF shipyards (optional) (UEF)"] = UnlockUEF1
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Unlock: Destroy UEF shipyards (optional) (UEF) " + str(index)
            objID = "210501"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            UnlockUEF1.add_locations({lname: int(objID)}, SupComLocation)

    if "Unlock (UEF)" in AllLevelsListToCheckRegionCreation:
        UnlockUEF2 = Region("Unlock: Destroy UEF radars (UEF)", world.player, world.multiworld)
        DictionaryOfRegions["Unlock: Destroy UEF radars (UEF)"] = UnlockUEF2
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Unlock: Destroy UEF radars (UEF) " + str(index)
            objID = "210502"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            UnlockUEF2.add_locations({lname: int(objID)}, SupComLocation)

    if "Unlock (UEF)" in AllLevelsListToCheckRegionCreation:
        UnlockUEF3 = Region("Unlock: Go to Hex5 (UEF)", world.player, world.multiworld)
        DictionaryOfRegions["Unlock: Go to Hex5 (UEF)"] = UnlockUEF3
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Unlock: Go to Hex5 (UEF) " + str(index)
            objID = "210503"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            UnlockUEF3.add_locations({lname: int(objID)}, SupComLocation)

    if "Unlock (UEF)" in AllLevelsListToCheckRegionCreation:
        UnlockUEF4 = Region("Unlock: Defend from heavy gunships (UEF)", world.player, world.multiworld)
        DictionaryOfRegions["Unlock: Defend from heavy gunships (UEF)"] = UnlockUEF4
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Unlock: Defend from heavy gunships (UEF) " + str(index)
            objID = "210504"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            UnlockUEF4.add_locations({lname: int(objID)}, SupComLocation)

    if "Unlock (UEF)" in AllLevelsListToCheckRegionCreation:
        UnlockUEF5 = Region("Unlock: Infect UEF landing pad (optional) (UEF)", world.player, world.multiworld)
        DictionaryOfRegions["Unlock: Infect UEF landing pad (optional) (UEF)"] = UnlockUEF5
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Unlock: Infect UEF landing pad (optional) (UEF) " + str(index)
            objID = "210505"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            UnlockUEF5.add_locations({lname: int(objID)}, SupComLocation)

    if "Unlock (UEF)" in AllLevelsListToCheckRegionCreation:
        UnlockUEF6 = Region("Unlock: This will be retconned later (UEF)", world.player, world.multiworld)
        DictionaryOfRegions["Unlock: This will be retconned later (UEF)"] = UnlockUEF6
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Unlock: This will be retconned later (UEF) " + str(index)
            objID = "210506"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            UnlockUEF6.add_locations({lname: int(objID)}, SupComLocation)

    if "Unlock (UEF)" in AllLevelsListToCheckRegionCreation:
        UnlockUEF7 = Region("Unlock: Kill UEF Commander (UEF)", world.player, world.multiworld)
        DictionaryOfRegions["Unlock: Kill UEF Commander (UEF)"] = UnlockUEF7
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Unlock: Kill UEF Commander (UEF) " + str(index)
            objID = "210507"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            UnlockUEF7.add_locations({lname: int(objID)}, SupComLocation)

    if "Freedom (UEF)" in AllLevelsListToCheckRegionCreation:
        FreedomUEF0 = Region("Freedom: Destroy CZAR (UEF)", world.player, world.multiworld)
        DictionaryOfRegions["Freedom: Destroy CZAR (UEF)"] = FreedomUEF0
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Freedom: Destroy CZAR (UEF) " + str(index)
            objID = "210600"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            FreedomUEF0.add_locations({lname: int(objID)}, SupComLocation)

    if "Freedom (UEF)" in AllLevelsListToCheckRegionCreation:
        FreedomUEF1 = Region("Freedom: Build Quantum Gate (UEF)", world.player, world.multiworld)
        DictionaryOfRegions["Freedom: Build Quantum Gate (UEF)"] = FreedomUEF1
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Freedom: Build Quantum Gate (UEF) " + str(index)
            objID = "210601"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            FreedomUEF1.add_locations({lname: int(objID)}, SupComLocation)

    if "Freedom (UEF)" in AllLevelsListToCheckRegionCreation:
        FreedomUEF2 = Region("Freedom: Download Quantum Virus (UEF)", world.player, world.multiworld)
        DictionaryOfRegions["Freedom: Download Quantum Virus (UEF)"] = FreedomUEF2
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Freedom: Download Quantum Virus (UEF) " + str(index)
            objID = "210602"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            FreedomUEF2.add_locations({lname: int(objID)}, SupComLocation)

    if "Freedom (UEF)" in AllLevelsListToCheckRegionCreation:
        FreedomUEF3 = Region("Freedom: Capture Black Sun control center (UEF)", world.player, world.multiworld)
        DictionaryOfRegions["Freedom: Capture Black Sun control center (UEF)"] = FreedomUEF3
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Freedom: Capture Black Sun control center (UEF) " + str(index)
            objID = "210603"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            FreedomUEF3.add_locations({lname: int(objID)}, SupComLocation)

    if "Freedom (UEF)" in AllLevelsListToCheckRegionCreation:
        FreedomUEF4 = Region("Freedom: Capture Black Sun (UEF)", world.player, world.multiworld)
        DictionaryOfRegions["Freedom: Capture Black Sun (UEF)"] = FreedomUEF4
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Freedom: Capture Black Sun (UEF) " + str(index)
            objID = "210604"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            FreedomUEF4.add_locations({lname: int(objID)}, SupComLocation)

    if "Freedom (UEF)" in AllLevelsListToCheckRegionCreation:
        FreedomUEF5 = Region("Freedom: Shoot Black Sun (UEF)", world.player, world.multiworld)
        DictionaryOfRegions["Freedom: Shoot Black Sun (UEF)"] = FreedomUEF5
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Freedom: Shoot Black Sun (UEF) " + str(index)
            objID = "210605"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            FreedomUEF5.add_locations({lname: int(objID)}, SupComLocation)

    if "Liberation (Cybran)" in AllLevelsListToCheckRegionCreation:
        LiberationCybran0 = Region("Liberation: Build mass (Cybran)", world.player, world.multiworld)
        DictionaryOfRegions["Liberation: Build mass (Cybran)"] = LiberationCybran0
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Liberation: Build mass (Cybran) " + str(index)
            objID = "220100"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            LiberationCybran0.add_locations({lname: int(objID)}, SupComLocation)

    if "Liberation (Cybran)" in AllLevelsListToCheckRegionCreation:
        LiberationCybran1 = Region("Liberation: Build power (Cybran)", world.player, world.multiworld)
        DictionaryOfRegions["Liberation: Build power (Cybran)"] = LiberationCybran1
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Liberation: Build power (Cybran) " + str(index)
            objID = "220101"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            LiberationCybran1.add_locations({lname: int(objID)}, SupComLocation)

    if "Liberation (Cybran)" in AllLevelsListToCheckRegionCreation:
        LiberationCybran2 = Region("Liberation: Build air factory (Cybran)", world.player, world.multiworld)
        DictionaryOfRegions["Liberation: Build air factory (Cybran)"] = LiberationCybran2
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Liberation: Build air factory (Cybran) " + str(index)
            objID = "220102"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            LiberationCybran2.add_locations({lname: int(objID)}, SupComLocation)

    if "Liberation (Cybran)" in AllLevelsListToCheckRegionCreation:
        LiberationCybran3 = Region("Liberation: Build bombers (Cybran)", world.player, world.multiworld)
        DictionaryOfRegions["Liberation: Build bombers (Cybran)"] = LiberationCybran3
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Liberation: Build bombers (Cybran) " + str(index)
            objID = "220103"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            LiberationCybran3.add_locations({lname: int(objID)}, SupComLocation)

    if "Liberation (Cybran)" in AllLevelsListToCheckRegionCreation:
        LiberationCybran4 = Region("Liberation: Destroy radar defenders (Cybran)", world.player, world.multiworld)
        DictionaryOfRegions["Liberation: Destroy radar defenders (Cybran)"] = LiberationCybran4
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Liberation: Destroy radar defenders (Cybran) " + str(index)
            objID = "220104"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            LiberationCybran4.add_locations({lname: int(objID)}, SupComLocation)

    if "Liberation (Cybran)" in AllLevelsListToCheckRegionCreation:
        LiberationCybran5 = Region("Liberation: Capture radars (Cybran)", world.player, world.multiworld)
        DictionaryOfRegions["Liberation: Capture radars (Cybran)"] = LiberationCybran5
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Liberation: Capture radars (Cybran) " + str(index)
            objID = "220105"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            LiberationCybran5.add_locations({lname: int(objID)}, SupComLocation)

    if "Liberation (Cybran)" in AllLevelsListToCheckRegionCreation:
        LiberationCybran6 = Region("Liberation: Destroy mex (Cybran)", world.player, world.multiworld)
        DictionaryOfRegions["Liberation: Destroy mex (Cybran)"] = LiberationCybran6
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Liberation: Destroy mex (Cybran) " + str(index)
            objID = "220106"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            LiberationCybran6.add_locations({lname: int(objID)}, SupComLocation)

    if "Liberation (Cybran)" in AllLevelsListToCheckRegionCreation:
        LiberationCybran7 = Region("Liberation: Destroy UEF defences (Cybran)", world.player, world.multiworld)
        DictionaryOfRegions["Liberation: Destroy UEF defences (Cybran)"] = LiberationCybran7
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Liberation: Destroy UEF defences (Cybran) " + str(index)
            objID = "220107"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            LiberationCybran7.add_locations({lname: int(objID)}, SupComLocation)

    if "Liberation (Cybran)" in AllLevelsListToCheckRegionCreation:
        LiberationCybran8 = Region("Liberation: Destroy UEF patrols (Cybran)", world.player, world.multiworld)
        DictionaryOfRegions["Liberation: Destroy UEF patrols (Cybran)"] = LiberationCybran8
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Liberation: Destroy UEF patrols (Cybran) " + str(index)
            objID = "220108"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            LiberationCybran8.add_locations({lname: int(objID)}, SupComLocation)

    if "Liberation (Cybran)" in AllLevelsListToCheckRegionCreation:
        LiberationCybran9 = Region("Liberation: Destroy UEF base defenders (Cybran)", world.player, world.multiworld)
        DictionaryOfRegions["Liberation: Destroy UEF base defenders (Cybran)"] = LiberationCybran9
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Liberation: Destroy UEF base defenders (Cybran) " + str(index)
            objID = "220109"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            LiberationCybran9.add_locations({lname: int(objID)}, SupComLocation)

    if "Liberation (Cybran)" in AllLevelsListToCheckRegionCreation:
        LiberationCybran10 = Region("Liberation: Destroy UEF base (Cybran)", world.player, world.multiworld)
        DictionaryOfRegions["Liberation: Destroy UEF base (Cybran)"] = LiberationCybran10
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Liberation: Destroy UEF base (Cybran) " + str(index)
            objID = "220110"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            LiberationCybran10.add_locations({lname: int(objID)}, SupComLocation)

    if "Liberation (Cybran)" in AllLevelsListToCheckRegionCreation:
        LiberationCybran11 = Region("Liberation: Kill Aeon Commander (Cybran)", world.player, world.multiworld)
        DictionaryOfRegions["Liberation: Kill Aeon Commander (Cybran)"] = LiberationCybran11
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Liberation: Kill Aeon Commander (Cybran) " + str(index)
            objID = "220111"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            LiberationCybran11.add_locations({lname: int(objID)}, SupComLocation)

    if "Artifact (Cybran)" in AllLevelsListToCheckRegionCreation:
        ArtifactCybran0 = Region("Artifact: Destroy first village defenders (Cybran)", world.player, world.multiworld)
        DictionaryOfRegions["Artifact: Destroy first village defenders (Cybran)"] = ArtifactCybran0
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Artifact: Destroy first village defenders (Cybran) " + str(index)
            objID = "220200"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            ArtifactCybran0.add_locations({lname: int(objID)}, SupComLocation)

    if "Artifact (Cybran)" in AllLevelsListToCheckRegionCreation:
        ArtifactCybran1 = Region("Artifact: Destroy first temple (Cybran)", world.player, world.multiworld)
        DictionaryOfRegions["Artifact: Destroy first temple (Cybran)"] = ArtifactCybran1
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Artifact: Destroy first temple (Cybran) " + str(index)
            objID = "220201"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            ArtifactCybran1.add_locations({lname: int(objID)}, SupComLocation)

    if "Artifact (Cybran)" in AllLevelsListToCheckRegionCreation:
        ArtifactCybran2 = Region("Artifact: Protect first artifact (Cybran)", world.player, world.multiworld)
        DictionaryOfRegions["Artifact: Protect first artifact (Cybran)"] = ArtifactCybran2
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Artifact: Protect first artifact (Cybran) " + str(index)
            objID = "220202"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            ArtifactCybran2.add_locations({lname: int(objID)}, SupComLocation)

    if "Artifact (Cybran)" in AllLevelsListToCheckRegionCreation:
        ArtifactCybran3 = Region("Artifact: Find second artifact (Cybran)", world.player, world.multiworld)
        DictionaryOfRegions["Artifact: Find second artifact (Cybran)"] = ArtifactCybran3
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Artifact: Find second artifact (Cybran) " + str(index)
            objID = "220203"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            ArtifactCybran3.add_locations({lname: int(objID)}, SupComLocation)

    if "Artifact (Cybran)" in AllLevelsListToCheckRegionCreation:
        ArtifactCybran4 = Region("Artifact: Destroy Aeon reinforcements (Cybran)", world.player, world.multiworld)
        DictionaryOfRegions["Artifact: Destroy Aeon reinforcements (Cybran)"] = ArtifactCybran4
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Artifact: Destroy Aeon reinforcements (Cybran) " + str(index)
            objID = "220204"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            ArtifactCybran4.add_locations({lname: int(objID)}, SupComLocation)

    if "Artifact (Cybran)" in AllLevelsListToCheckRegionCreation:
        ArtifactCybran5 = Region("Artifact: Protect second artifact (Cybran)", world.player, world.multiworld)
        DictionaryOfRegions["Artifact: Protect second artifact (Cybran)"] = ArtifactCybran5
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Artifact: Protect second artifact (Cybran) " + str(index)
            objID = "220205"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            ArtifactCybran5.add_locations({lname: int(objID)}, SupComLocation)

    if "Artifact (Cybran)" in AllLevelsListToCheckRegionCreation:
        ArtifactCybran6 = Region("Artifact: Defend from Aeon attack (Cybran)", world.player, world.multiworld)
        DictionaryOfRegions["Artifact: Defend from Aeon attack (Cybran)"] = ArtifactCybran6
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Artifact: Defend from Aeon attack (Cybran) " + str(index)
            objID = "220206"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            ArtifactCybran6.add_locations({lname: int(objID)}, SupComLocation)

    if "Artifact (Cybran)" in AllLevelsListToCheckRegionCreation:
        ArtifactCybran7 = Region("Artifact: Destroy eastern base (Cybran)", world.player, world.multiworld)
        DictionaryOfRegions["Artifact: Destroy eastern base (Cybran)"] = ArtifactCybran7
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Artifact: Destroy eastern base (Cybran) " + str(index)
            objID = "220207"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            ArtifactCybran7.add_locations({lname: int(objID)}, SupComLocation)

    if "Artifact (Cybran)" in AllLevelsListToCheckRegionCreation:
        ArtifactCybran8 = Region("Artifact: Destroy navy base (Cybran)", world.player, world.multiworld)
        DictionaryOfRegions["Artifact: Destroy navy base (Cybran)"] = ArtifactCybran8
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Artifact: Destroy navy base (Cybran) " + str(index)
            objID = "220208"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            ArtifactCybran8.add_locations({lname: int(objID)}, SupComLocation)

    if "Artifact (Cybran)" in AllLevelsListToCheckRegionCreation:
        ArtifactCybran9 = Region("Artifact: Protect third artifact (Cybran)", world.player, world.multiworld)
        DictionaryOfRegions["Artifact: Protect third artifact (Cybran)"] = ArtifactCybran9
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Artifact: Protect third artifact (Cybran) " + str(index)
            objID = "220209"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            ArtifactCybran9.add_locations({lname: int(objID)}, SupComLocation)

    if "Artifact (Cybran)" in AllLevelsListToCheckRegionCreation:
        ArtifactCybran10 = Region("Artifact: Kill Aeon Commander (optional) (Cybran)", world.player, world.multiworld)
        DictionaryOfRegions["Artifact: Kill Aeon Commander (optional) (Cybran)"] = ArtifactCybran10
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Artifact: Kill Aeon Commander (optional) (Cybran) " + str(index)
            objID = "220210"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            ArtifactCybran10.add_locations({lname: int(objID)}, SupComLocation)

    if "Artifact (Cybran)" in AllLevelsListToCheckRegionCreation:
        ArtifactCybran11 = Region("Artifact: Kill Mach (Cybran)", world.player, world.multiworld)
        DictionaryOfRegions["Artifact: Kill Mach (Cybran)"] = ArtifactCybran11
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Artifact: Kill Mach (Cybran) " + str(index)
            objID = "220211"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            ArtifactCybran11.add_locations({lname: int(objID)}, SupComLocation)

    if "Artifact (Cybran)" in AllLevelsListToCheckRegionCreation:
        ArtifactCybran12 = Region("Artifact: Go to Gate (Cybran)", world.player, world.multiworld)
        DictionaryOfRegions["Artifact: Go to Gate (Cybran)"] = ArtifactCybran12
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Artifact: Go to Gate (Cybran) " + str(index)
            objID = "220212"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            ArtifactCybran12.add_locations({lname: int(objID)}, SupComLocation)

    if "Defrag (Cybran)" in AllLevelsListToCheckRegionCreation:
        DefragCybran0 = Region("Defrag: Protect York 18 (Cybran)", world.player, world.multiworld)
        DictionaryOfRegions["Defrag: Protect York 18 (Cybran)"] = DefragCybran0
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Defrag: Protect York 18 (Cybran) " + str(index)
            objID = "220300"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            DefragCybran0.add_locations({lname: int(objID)}, SupComLocation)

    if "Defrag (Cybran)" in AllLevelsListToCheckRegionCreation:
        DefragCybran1 = Region("Defrag: Destroy western UEF base (Cybran)", world.player, world.multiworld)
        DictionaryOfRegions["Defrag: Destroy western UEF base (Cybran)"] = DefragCybran1
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Defrag: Destroy western UEF base (Cybran) " + str(index)
            objID = "220301"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            DefragCybran1.add_locations({lname: int(objID)}, SupComLocation)

    if "Defrag (Cybran)" in AllLevelsListToCheckRegionCreation:
        DefragCybran2 = Region("Defrag: Destroy north-western UEF base (Cybran)", world.player, world.multiworld)
        DictionaryOfRegions["Defrag: Destroy north-western UEF base (Cybran)"] = DefragCybran2
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Defrag: Destroy north-western UEF base (Cybran) " + str(index)
            objID = "220302"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            DefragCybran2.add_locations({lname: int(objID)}, SupComLocation)

    if "Defrag (Cybran)" in AllLevelsListToCheckRegionCreation:
        DefragCybran3 = Region("Defrag: Destroy northern UEF base (Cybran)", world.player, world.multiworld)
        DictionaryOfRegions["Defrag: Destroy northern UEF base (Cybran)"] = DefragCybran3
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Defrag: Destroy northern UEF base (Cybran) " + str(index)
            objID = "220303"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            DefragCybran3.add_locations({lname: int(objID)}, SupComLocation)

    if "Defrag (Cybran)" in AllLevelsListToCheckRegionCreation:
        DefragCybran4 = Region("Defrag: Sink UEF cruiser (Cybran)", world.player, world.multiworld)
        DictionaryOfRegions["Defrag: Sink UEF cruiser (Cybran)"] = DefragCybran4
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Defrag: Sink UEF cruiser (Cybran) " + str(index)
            objID = "220304"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            DefragCybran4.add_locations({lname: int(objID)}, SupComLocation)

    if "Defrag (Cybran)" in AllLevelsListToCheckRegionCreation:
        DefragCybran5 = Region("Defrag: Destroy static artillery (Cybran)", world.player, world.multiworld)
        DictionaryOfRegions["Defrag: Destroy static artillery (Cybran)"] = DefragCybran5
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Defrag: Destroy static artillery (Cybran) " + str(index)
            objID = "220305"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            DefragCybran5.add_locations({lname: int(objID)}, SupComLocation)

    if "Defrag (Cybran)" in AllLevelsListToCheckRegionCreation:
        DefragCybran6 = Region("Defrag: Escort trucks (Cybran)", world.player, world.multiworld)
        DictionaryOfRegions["Defrag: Escort trucks (Cybran)"] = DefragCybran6
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Defrag: Escort trucks (Cybran) " + str(index)
            objID = "220306"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            DefragCybran6.add_locations({lname: int(objID)}, SupComLocation)

    if "Defrag (Cybran)" in AllLevelsListToCheckRegionCreation:
        DefragCybran7 = Region("Defrag: Escort ALL trucks (optional) (Cybran)", world.player, world.multiworld)
        DictionaryOfRegions["Defrag: Escort ALL trucks (optional) (Cybran)"] = DefragCybran7
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Defrag: Escort ALL trucks (optional) (Cybran) " + str(index)
            objID = "220307"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            DefragCybran7.add_locations({lname: int(objID)}, SupComLocation)

    if "Defrag (Cybran)" in AllLevelsListToCheckRegionCreation:
        DefragCybran8 = Region("Defrag: Optional objective  (optional) (Cybran)", world.player, world.multiworld)
        DictionaryOfRegions["Defrag: Optional objective  (optional) (Cybran)"] = DefragCybran8
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Defrag: Optional objective  (optional) (Cybran) " + str(index)
            objID = "220308"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            DefragCybran8.add_locations({lname: int(objID)}, SupComLocation)

    if "Defrag (Cybran)" in AllLevelsListToCheckRegionCreation:
        DefragCybran9 = Region("Defrag: Kill UEF Commander (Cybran)", world.player, world.multiworld)
        DictionaryOfRegions["Defrag: Kill UEF Commander (Cybran)"] = DefragCybran9
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Defrag: Kill UEF Commander (Cybran) " + str(index)
            objID = "220309"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            DefragCybran9.add_locations({lname: int(objID)}, SupComLocation)

    if "Mainframe Tango (Cybran)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoCybran0 = Region("Mainframe Tango: Defeat Aeon Commander (Cybran)", world.player, world.multiworld)
        DictionaryOfRegions["Mainframe Tango: Defeat Aeon Commander (Cybran)"] = MainframeTangoCybran0
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Mainframe Tango: Defeat Aeon Commander (Cybran) " + str(index)
            objID = "220400"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            MainframeTangoCybran0.add_locations({lname: int(objID)}, SupComLocation)

    if "Mainframe Tango (Cybran)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoCybran1 = Region("Mainframe Tango: Capture Network Node (Cybran)", world.player, world.multiworld)
        DictionaryOfRegions["Mainframe Tango: Capture Network Node (Cybran)"] = MainframeTangoCybran1
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Mainframe Tango: Capture Network Node (Cybran) " + str(index)
            objID = "220401"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            MainframeTangoCybran1.add_locations({lname: int(objID)}, SupComLocation)

    if "Mainframe Tango (Cybran)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoCybran2 = Region("Mainframe Tango: Save Network Node (Cybran)", world.player, world.multiworld)
        DictionaryOfRegions["Mainframe Tango: Save Network Node (Cybran)"] = MainframeTangoCybran2
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Mainframe Tango: Save Network Node (Cybran) " + str(index)
            objID = "220402"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            MainframeTangoCybran2.add_locations({lname: int(objID)}, SupComLocation)

    if "Mainframe Tango (Cybran)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoCybran3 = Region("Mainframe Tango: Save 80% civilian buildings (optional) (Cybran)", world.player, world.multiworld)
        DictionaryOfRegions["Mainframe Tango: Save 80% civilian buildings (optional) (Cybran)"] = MainframeTangoCybran3
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Mainframe Tango: Save 80% civilian buildings (optional) (Cybran) " + str(index)
            objID = "220403"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            MainframeTangoCybran3.add_locations({lname: int(objID)}, SupComLocation)

    if "Mainframe Tango (Cybran)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoCybran4 = Region("Mainframe Tango: Survive attacks (Cybran)", world.player, world.multiworld)
        DictionaryOfRegions["Mainframe Tango: Survive attacks (Cybran)"] = MainframeTangoCybran4
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Mainframe Tango: Survive attacks (Cybran) " + str(index)
            objID = "220404"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            MainframeTangoCybran4.add_locations({lname: int(objID)}, SupComLocation)

    if "Mainframe Tango (Cybran)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoCybran5 = Region("Mainframe Tango: Capture northeast node (Cybran)", world.player, world.multiworld)
        DictionaryOfRegions["Mainframe Tango: Capture northeast node (Cybran)"] = MainframeTangoCybran5
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Mainframe Tango: Capture northeast node (Cybran) " + str(index)
            objID = "220405"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            MainframeTangoCybran5.add_locations({lname: int(objID)}, SupComLocation)

    if "Mainframe Tango (Cybran)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoCybran6 = Region("Mainframe Tango: Capture northwest node (Cybran)", world.player, world.multiworld)
        DictionaryOfRegions["Mainframe Tango: Capture northwest node (Cybran)"] = MainframeTangoCybran6
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Mainframe Tango: Capture northwest node (Cybran) " + str(index)
            objID = "220406"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            MainframeTangoCybran6.add_locations({lname: int(objID)}, SupComLocation)

    if "Mainframe Tango (Cybran)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoCybran7 = Region("Mainframe Tango: Do not attack main Aeon base (Cybran)", world.player, world.multiworld)
        DictionaryOfRegions["Mainframe Tango: Do not attack main Aeon base (Cybran)"] = MainframeTangoCybran7
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Mainframe Tango: Do not attack main Aeon base (Cybran) " + str(index)
            objID = "220407"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            MainframeTangoCybran7.add_locations({lname: int(objID)}, SupComLocation)

    if "Mainframe Tango (Cybran)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoCybran8 = Region("Mainframe Tango: Kill Aeon Commander (Cybran)", world.player, world.multiworld)
        DictionaryOfRegions["Mainframe Tango: Kill Aeon Commander (Cybran)"] = MainframeTangoCybran8
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Mainframe Tango: Kill Aeon Commander (Cybran) " + str(index)
            objID = "220408"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            MainframeTangoCybran8.add_locations({lname: int(objID)}, SupComLocation)

    if "Unlock (Cybran)" in AllLevelsListToCheckRegionCreation:
        UnlockCybran0 = Region("Unlock: Destroy UEF generators (Cybran)", world.player, world.multiworld)
        DictionaryOfRegions["Unlock: Destroy UEF generators (Cybran)"] = UnlockCybran0
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Unlock: Destroy UEF generators (Cybran) " + str(index)
            objID = "220500"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            UnlockCybran0.add_locations({lname: int(objID)}, SupComLocation)

    if "Unlock (Cybran)" in AllLevelsListToCheckRegionCreation:
        UnlockCybran1 = Region("Unlock: Destroy UEF shipyards (optional) (Cybran)", world.player, world.multiworld)
        DictionaryOfRegions["Unlock: Destroy UEF shipyards (optional) (Cybran)"] = UnlockCybran1
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Unlock: Destroy UEF shipyards (optional) (Cybran) " + str(index)
            objID = "220501"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            UnlockCybran1.add_locations({lname: int(objID)}, SupComLocation)

    if "Unlock (Cybran)" in AllLevelsListToCheckRegionCreation:
        UnlockCybran2 = Region("Unlock: Destroy UEF radars (Cybran)", world.player, world.multiworld)
        DictionaryOfRegions["Unlock: Destroy UEF radars (Cybran)"] = UnlockCybran2
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Unlock: Destroy UEF radars (Cybran) " + str(index)
            objID = "220502"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            UnlockCybran2.add_locations({lname: int(objID)}, SupComLocation)

    if "Unlock (Cybran)" in AllLevelsListToCheckRegionCreation:
        UnlockCybran3 = Region("Unlock: Go to Hex5 (Cybran)", world.player, world.multiworld)
        DictionaryOfRegions["Unlock: Go to Hex5 (Cybran)"] = UnlockCybran3
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Unlock: Go to Hex5 (Cybran) " + str(index)
            objID = "220503"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            UnlockCybran3.add_locations({lname: int(objID)}, SupComLocation)

    if "Unlock (Cybran)" in AllLevelsListToCheckRegionCreation:
        UnlockCybran4 = Region("Unlock: Defend from heavy gunships (Cybran)", world.player, world.multiworld)
        DictionaryOfRegions["Unlock: Defend from heavy gunships (Cybran)"] = UnlockCybran4
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Unlock: Defend from heavy gunships (Cybran) " + str(index)
            objID = "220504"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            UnlockCybran4.add_locations({lname: int(objID)}, SupComLocation)

    if "Unlock (Cybran)" in AllLevelsListToCheckRegionCreation:
        UnlockCybran5 = Region("Unlock: Infect UEF landing pad (optional) (Cybran)", world.player, world.multiworld)
        DictionaryOfRegions["Unlock: Infect UEF landing pad (optional) (Cybran)"] = UnlockCybran5
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Unlock: Infect UEF landing pad (optional) (Cybran) " + str(index)
            objID = "220505"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            UnlockCybran5.add_locations({lname: int(objID)}, SupComLocation)

    if "Unlock (Cybran)" in AllLevelsListToCheckRegionCreation:
        UnlockCybran6 = Region("Unlock: This will be retconned later (Cybran)", world.player, world.multiworld)
        DictionaryOfRegions["Unlock: This will be retconned later (Cybran)"] = UnlockCybran6
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Unlock: This will be retconned later (Cybran) " + str(index)
            objID = "220506"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            UnlockCybran6.add_locations({lname: int(objID)}, SupComLocation)

    if "Unlock (Cybran)" in AllLevelsListToCheckRegionCreation:
        UnlockCybran7 = Region("Unlock: Kill UEF Commander (Cybran)", world.player, world.multiworld)
        DictionaryOfRegions["Unlock: Kill UEF Commander (Cybran)"] = UnlockCybran7
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Unlock: Kill UEF Commander (Cybran) " + str(index)
            objID = "220507"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            UnlockCybran7.add_locations({lname: int(objID)}, SupComLocation)

    if "Freedom (Cybran)" in AllLevelsListToCheckRegionCreation:
        FreedomCybran0 = Region("Freedom: Destroy CZAR (Cybran)", world.player, world.multiworld)
        DictionaryOfRegions["Freedom: Destroy CZAR (Cybran)"] = FreedomCybran0
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Freedom: Destroy CZAR (Cybran) " + str(index)
            objID = "220600"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            FreedomCybran0.add_locations({lname: int(objID)}, SupComLocation)

    if "Freedom (Cybran)" in AllLevelsListToCheckRegionCreation:
        FreedomCybran1 = Region("Freedom: Build Quantum Gate (Cybran)", world.player, world.multiworld)
        DictionaryOfRegions["Freedom: Build Quantum Gate (Cybran)"] = FreedomCybran1
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Freedom: Build Quantum Gate (Cybran) " + str(index)
            objID = "220601"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            FreedomCybran1.add_locations({lname: int(objID)}, SupComLocation)

    if "Freedom (Cybran)" in AllLevelsListToCheckRegionCreation:
        FreedomCybran2 = Region("Freedom: Download Quantum Virus (Cybran)", world.player, world.multiworld)
        DictionaryOfRegions["Freedom: Download Quantum Virus (Cybran)"] = FreedomCybran2
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Freedom: Download Quantum Virus (Cybran) " + str(index)
            objID = "220602"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            FreedomCybran2.add_locations({lname: int(objID)}, SupComLocation)

    if "Freedom (Cybran)" in AllLevelsListToCheckRegionCreation:
        FreedomCybran3 = Region("Freedom: Capture Black Sun control center (Cybran)", world.player, world.multiworld)
        DictionaryOfRegions["Freedom: Capture Black Sun control center (Cybran)"] = FreedomCybran3
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Freedom: Capture Black Sun control center (Cybran) " + str(index)
            objID = "220603"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            FreedomCybran3.add_locations({lname: int(objID)}, SupComLocation)

    if "Freedom (Cybran)" in AllLevelsListToCheckRegionCreation:
        FreedomCybran4 = Region("Freedom: Capture Black Sun (Cybran)", world.player, world.multiworld)
        DictionaryOfRegions["Freedom: Capture Black Sun (Cybran)"] = FreedomCybran4
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Freedom: Capture Black Sun (Cybran) " + str(index)
            objID = "220604"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            FreedomCybran4.add_locations({lname: int(objID)}, SupComLocation)

    if "Freedom (Cybran)" in AllLevelsListToCheckRegionCreation:
        FreedomCybran5 = Region("Freedom: Shoot Black Sun (Cybran)", world.player, world.multiworld)
        DictionaryOfRegions["Freedom: Shoot Black Sun (Cybran)"] = FreedomCybran5
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Freedom: Shoot Black Sun (Cybran) " + str(index)
            objID = "220605"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            FreedomCybran5.add_locations({lname: int(objID)}, SupComLocation)

    if "Liberation (Aeon)" in AllLevelsListToCheckRegionCreation:
        LiberationAeon0 = Region("Liberation: Build mass (Aeon)", world.player, world.multiworld)
        DictionaryOfRegions["Liberation: Build mass (Aeon)"] = LiberationAeon0
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Liberation: Build mass (Aeon) " + str(index)
            objID = "230100"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            LiberationAeon0.add_locations({lname: int(objID)}, SupComLocation)

    if "Liberation (Aeon)" in AllLevelsListToCheckRegionCreation:
        LiberationAeon1 = Region("Liberation: Build power (Aeon)", world.player, world.multiworld)
        DictionaryOfRegions["Liberation: Build power (Aeon)"] = LiberationAeon1
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Liberation: Build power (Aeon) " + str(index)
            objID = "230101"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            LiberationAeon1.add_locations({lname: int(objID)}, SupComLocation)

    if "Liberation (Aeon)" in AllLevelsListToCheckRegionCreation:
        LiberationAeon2 = Region("Liberation: Build air factory (Aeon)", world.player, world.multiworld)
        DictionaryOfRegions["Liberation: Build air factory (Aeon)"] = LiberationAeon2
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Liberation: Build air factory (Aeon) " + str(index)
            objID = "230102"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            LiberationAeon2.add_locations({lname: int(objID)}, SupComLocation)

    if "Liberation (Aeon)" in AllLevelsListToCheckRegionCreation:
        LiberationAeon3 = Region("Liberation: Build bombers (Aeon)", world.player, world.multiworld)
        DictionaryOfRegions["Liberation: Build bombers (Aeon)"] = LiberationAeon3
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Liberation: Build bombers (Aeon) " + str(index)
            objID = "230103"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            LiberationAeon3.add_locations({lname: int(objID)}, SupComLocation)

    if "Liberation (Aeon)" in AllLevelsListToCheckRegionCreation:
        LiberationAeon4 = Region("Liberation: Destroy radar defenders (Aeon)", world.player, world.multiworld)
        DictionaryOfRegions["Liberation: Destroy radar defenders (Aeon)"] = LiberationAeon4
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Liberation: Destroy radar defenders (Aeon) " + str(index)
            objID = "230104"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            LiberationAeon4.add_locations({lname: int(objID)}, SupComLocation)

    if "Liberation (Aeon)" in AllLevelsListToCheckRegionCreation:
        LiberationAeon5 = Region("Liberation: Capture radars (Aeon)", world.player, world.multiworld)
        DictionaryOfRegions["Liberation: Capture radars (Aeon)"] = LiberationAeon5
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Liberation: Capture radars (Aeon) " + str(index)
            objID = "230105"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            LiberationAeon5.add_locations({lname: int(objID)}, SupComLocation)

    if "Liberation (Aeon)" in AllLevelsListToCheckRegionCreation:
        LiberationAeon6 = Region("Liberation: Destroy mex (Aeon)", world.player, world.multiworld)
        DictionaryOfRegions["Liberation: Destroy mex (Aeon)"] = LiberationAeon6
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Liberation: Destroy mex (Aeon) " + str(index)
            objID = "230106"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            LiberationAeon6.add_locations({lname: int(objID)}, SupComLocation)

    if "Liberation (Aeon)" in AllLevelsListToCheckRegionCreation:
        LiberationAeon7 = Region("Liberation: Destroy UEF defences (Aeon)", world.player, world.multiworld)
        DictionaryOfRegions["Liberation: Destroy UEF defences (Aeon)"] = LiberationAeon7
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Liberation: Destroy UEF defences (Aeon) " + str(index)
            objID = "230107"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            LiberationAeon7.add_locations({lname: int(objID)}, SupComLocation)

    if "Liberation (Aeon)" in AllLevelsListToCheckRegionCreation:
        LiberationAeon8 = Region("Liberation: Destroy UEF patrols (Aeon)", world.player, world.multiworld)
        DictionaryOfRegions["Liberation: Destroy UEF patrols (Aeon)"] = LiberationAeon8
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Liberation: Destroy UEF patrols (Aeon) " + str(index)
            objID = "230108"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            LiberationAeon8.add_locations({lname: int(objID)}, SupComLocation)

    if "Liberation (Aeon)" in AllLevelsListToCheckRegionCreation:
        LiberationAeon9 = Region("Liberation: Destroy UEF base defenders (Aeon)", world.player, world.multiworld)
        DictionaryOfRegions["Liberation: Destroy UEF base defenders (Aeon)"] = LiberationAeon9
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Liberation: Destroy UEF base defenders (Aeon) " + str(index)
            objID = "230109"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            LiberationAeon9.add_locations({lname: int(objID)}, SupComLocation)

    if "Liberation (Aeon)" in AllLevelsListToCheckRegionCreation:
        LiberationAeon10 = Region("Liberation: Destroy UEF base (Aeon)", world.player, world.multiworld)
        DictionaryOfRegions["Liberation: Destroy UEF base (Aeon)"] = LiberationAeon10
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Liberation: Destroy UEF base (Aeon) " + str(index)
            objID = "230110"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            LiberationAeon10.add_locations({lname: int(objID)}, SupComLocation)

    if "Liberation (Aeon)" in AllLevelsListToCheckRegionCreation:
        LiberationAeon11 = Region("Liberation: Kill Aeon Commander (Aeon)", world.player, world.multiworld)
        DictionaryOfRegions["Liberation: Kill Aeon Commander (Aeon)"] = LiberationAeon11
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Liberation: Kill Aeon Commander (Aeon) " + str(index)
            objID = "230111"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            LiberationAeon11.add_locations({lname: int(objID)}, SupComLocation)

    if "Artifact (Aeon)" in AllLevelsListToCheckRegionCreation:
        ArtifactAeon0 = Region("Artifact: Destroy first village defenders (Aeon)", world.player, world.multiworld)
        DictionaryOfRegions["Artifact: Destroy first village defenders (Aeon)"] = ArtifactAeon0
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Artifact: Destroy first village defenders (Aeon) " + str(index)
            objID = "230200"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            ArtifactAeon0.add_locations({lname: int(objID)}, SupComLocation)

    if "Artifact (Aeon)" in AllLevelsListToCheckRegionCreation:
        ArtifactAeon1 = Region("Artifact: Destroy first temple (Aeon)", world.player, world.multiworld)
        DictionaryOfRegions["Artifact: Destroy first temple (Aeon)"] = ArtifactAeon1
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Artifact: Destroy first temple (Aeon) " + str(index)
            objID = "230201"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            ArtifactAeon1.add_locations({lname: int(objID)}, SupComLocation)

    if "Artifact (Aeon)" in AllLevelsListToCheckRegionCreation:
        ArtifactAeon2 = Region("Artifact: Protect first artifact (Aeon)", world.player, world.multiworld)
        DictionaryOfRegions["Artifact: Protect first artifact (Aeon)"] = ArtifactAeon2
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Artifact: Protect first artifact (Aeon) " + str(index)
            objID = "230202"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            ArtifactAeon2.add_locations({lname: int(objID)}, SupComLocation)

    if "Artifact (Aeon)" in AllLevelsListToCheckRegionCreation:
        ArtifactAeon3 = Region("Artifact: Find second artifact (Aeon)", world.player, world.multiworld)
        DictionaryOfRegions["Artifact: Find second artifact (Aeon)"] = ArtifactAeon3
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Artifact: Find second artifact (Aeon) " + str(index)
            objID = "230203"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            ArtifactAeon3.add_locations({lname: int(objID)}, SupComLocation)

    if "Artifact (Aeon)" in AllLevelsListToCheckRegionCreation:
        ArtifactAeon4 = Region("Artifact: Destroy Aeon reinforcements (Aeon)", world.player, world.multiworld)
        DictionaryOfRegions["Artifact: Destroy Aeon reinforcements (Aeon)"] = ArtifactAeon4
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Artifact: Destroy Aeon reinforcements (Aeon) " + str(index)
            objID = "230204"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            ArtifactAeon4.add_locations({lname: int(objID)}, SupComLocation)

    if "Artifact (Aeon)" in AllLevelsListToCheckRegionCreation:
        ArtifactAeon5 = Region("Artifact: Protect second artifact (Aeon)", world.player, world.multiworld)
        DictionaryOfRegions["Artifact: Protect second artifact (Aeon)"] = ArtifactAeon5
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Artifact: Protect second artifact (Aeon) " + str(index)
            objID = "230205"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            ArtifactAeon5.add_locations({lname: int(objID)}, SupComLocation)

    if "Artifact (Aeon)" in AllLevelsListToCheckRegionCreation:
        ArtifactAeon6 = Region("Artifact: Defend from Aeon attack (Aeon)", world.player, world.multiworld)
        DictionaryOfRegions["Artifact: Defend from Aeon attack (Aeon)"] = ArtifactAeon6
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Artifact: Defend from Aeon attack (Aeon) " + str(index)
            objID = "230206"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            ArtifactAeon6.add_locations({lname: int(objID)}, SupComLocation)

    if "Artifact (Aeon)" in AllLevelsListToCheckRegionCreation:
        ArtifactAeon7 = Region("Artifact: Destroy eastern base (Aeon)", world.player, world.multiworld)
        DictionaryOfRegions["Artifact: Destroy eastern base (Aeon)"] = ArtifactAeon7
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Artifact: Destroy eastern base (Aeon) " + str(index)
            objID = "230207"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            ArtifactAeon7.add_locations({lname: int(objID)}, SupComLocation)

    if "Artifact (Aeon)" in AllLevelsListToCheckRegionCreation:
        ArtifactAeon8 = Region("Artifact: Destroy navy base (Aeon)", world.player, world.multiworld)
        DictionaryOfRegions["Artifact: Destroy navy base (Aeon)"] = ArtifactAeon8
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Artifact: Destroy navy base (Aeon) " + str(index)
            objID = "230208"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            ArtifactAeon8.add_locations({lname: int(objID)}, SupComLocation)

    if "Artifact (Aeon)" in AllLevelsListToCheckRegionCreation:
        ArtifactAeon9 = Region("Artifact: Protect third artifact (Aeon)", world.player, world.multiworld)
        DictionaryOfRegions["Artifact: Protect third artifact (Aeon)"] = ArtifactAeon9
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Artifact: Protect third artifact (Aeon) " + str(index)
            objID = "230209"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            ArtifactAeon9.add_locations({lname: int(objID)}, SupComLocation)

    if "Artifact (Aeon)" in AllLevelsListToCheckRegionCreation:
        ArtifactAeon10 = Region("Artifact: Kill Aeon Commander (optional) (Aeon)", world.player, world.multiworld)
        DictionaryOfRegions["Artifact: Kill Aeon Commander (optional) (Aeon)"] = ArtifactAeon10
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Artifact: Kill Aeon Commander (optional) (Aeon) " + str(index)
            objID = "230210"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            ArtifactAeon10.add_locations({lname: int(objID)}, SupComLocation)

    if "Artifact (Aeon)" in AllLevelsListToCheckRegionCreation:
        ArtifactAeon11 = Region("Artifact: Kill Mach (Aeon)", world.player, world.multiworld)
        DictionaryOfRegions["Artifact: Kill Mach (Aeon)"] = ArtifactAeon11
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Artifact: Kill Mach (Aeon) " + str(index)
            objID = "230211"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            ArtifactAeon11.add_locations({lname: int(objID)}, SupComLocation)

    if "Artifact (Aeon)" in AllLevelsListToCheckRegionCreation:
        ArtifactAeon12 = Region("Artifact: Go to Gate (Aeon)", world.player, world.multiworld)
        DictionaryOfRegions["Artifact: Go to Gate (Aeon)"] = ArtifactAeon12
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Artifact: Go to Gate (Aeon) " + str(index)
            objID = "230212"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            ArtifactAeon12.add_locations({lname: int(objID)}, SupComLocation)

    if "Defrag (Aeon)" in AllLevelsListToCheckRegionCreation:
        DefragAeon0 = Region("Defrag: Protect York 18 (Aeon)", world.player, world.multiworld)
        DictionaryOfRegions["Defrag: Protect York 18 (Aeon)"] = DefragAeon0
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Defrag: Protect York 18 (Aeon) " + str(index)
            objID = "230300"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            DefragAeon0.add_locations({lname: int(objID)}, SupComLocation)

    if "Defrag (Aeon)" in AllLevelsListToCheckRegionCreation:
        DefragAeon1 = Region("Defrag: Destroy western UEF base (Aeon)", world.player, world.multiworld)
        DictionaryOfRegions["Defrag: Destroy western UEF base (Aeon)"] = DefragAeon1
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Defrag: Destroy western UEF base (Aeon) " + str(index)
            objID = "230301"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            DefragAeon1.add_locations({lname: int(objID)}, SupComLocation)

    if "Defrag (Aeon)" in AllLevelsListToCheckRegionCreation:
        DefragAeon2 = Region("Defrag: Destroy north-western UEF base (Aeon)", world.player, world.multiworld)
        DictionaryOfRegions["Defrag: Destroy north-western UEF base (Aeon)"] = DefragAeon2
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Defrag: Destroy north-western UEF base (Aeon) " + str(index)
            objID = "230302"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            DefragAeon2.add_locations({lname: int(objID)}, SupComLocation)

    if "Defrag (Aeon)" in AllLevelsListToCheckRegionCreation:
        DefragAeon3 = Region("Defrag: Destroy northern UEF base (Aeon)", world.player, world.multiworld)
        DictionaryOfRegions["Defrag: Destroy northern UEF base (Aeon)"] = DefragAeon3
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Defrag: Destroy northern UEF base (Aeon) " + str(index)
            objID = "230303"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            DefragAeon3.add_locations({lname: int(objID)}, SupComLocation)

    if "Defrag (Aeon)" in AllLevelsListToCheckRegionCreation:
        DefragAeon4 = Region("Defrag: Sink UEF cruiser (Aeon)", world.player, world.multiworld)
        DictionaryOfRegions["Defrag: Sink UEF cruiser (Aeon)"] = DefragAeon4
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Defrag: Sink UEF cruiser (Aeon) " + str(index)
            objID = "230304"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            DefragAeon4.add_locations({lname: int(objID)}, SupComLocation)

    if "Defrag (Aeon)" in AllLevelsListToCheckRegionCreation:
        DefragAeon5 = Region("Defrag: Destroy static artillery (Aeon)", world.player, world.multiworld)
        DictionaryOfRegions["Defrag: Destroy static artillery (Aeon)"] = DefragAeon5
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Defrag: Destroy static artillery (Aeon) " + str(index)
            objID = "230305"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            DefragAeon5.add_locations({lname: int(objID)}, SupComLocation)

    if "Defrag (Aeon)" in AllLevelsListToCheckRegionCreation:
        DefragAeon6 = Region("Defrag: Escort trucks (Aeon)", world.player, world.multiworld)
        DictionaryOfRegions["Defrag: Escort trucks (Aeon)"] = DefragAeon6
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Defrag: Escort trucks (Aeon) " + str(index)
            objID = "230306"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            DefragAeon6.add_locations({lname: int(objID)}, SupComLocation)

    if "Defrag (Aeon)" in AllLevelsListToCheckRegionCreation:
        DefragAeon7 = Region("Defrag: Escort ALL trucks (optional) (Aeon)", world.player, world.multiworld)
        DictionaryOfRegions["Defrag: Escort ALL trucks (optional) (Aeon)"] = DefragAeon7
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Defrag: Escort ALL trucks (optional) (Aeon) " + str(index)
            objID = "230307"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            DefragAeon7.add_locations({lname: int(objID)}, SupComLocation)

    if "Defrag (Aeon)" in AllLevelsListToCheckRegionCreation:
        DefragAeon8 = Region("Defrag: Optional objective  (optional) (Aeon)", world.player, world.multiworld)
        DictionaryOfRegions["Defrag: Optional objective  (optional) (Aeon)"] = DefragAeon8
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Defrag: Optional objective  (optional) (Aeon) " + str(index)
            objID = "230308"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            DefragAeon8.add_locations({lname: int(objID)}, SupComLocation)

    if "Defrag (Aeon)" in AllLevelsListToCheckRegionCreation:
        DefragAeon9 = Region("Defrag: Kill UEF Commander (Aeon)", world.player, world.multiworld)
        DictionaryOfRegions["Defrag: Kill UEF Commander (Aeon)"] = DefragAeon9
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Defrag: Kill UEF Commander (Aeon) " + str(index)
            objID = "230309"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            DefragAeon9.add_locations({lname: int(objID)}, SupComLocation)

    if "Mainframe Tango (Aeon)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoAeon0 = Region("Mainframe Tango: Defeat Aeon Commander (Aeon)", world.player, world.multiworld)
        DictionaryOfRegions["Mainframe Tango: Defeat Aeon Commander (Aeon)"] = MainframeTangoAeon0
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Mainframe Tango: Defeat Aeon Commander (Aeon) " + str(index)
            objID = "230400"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            MainframeTangoAeon0.add_locations({lname: int(objID)}, SupComLocation)

    if "Mainframe Tango (Aeon)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoAeon1 = Region("Mainframe Tango: Capture Network Node (Aeon)", world.player, world.multiworld)
        DictionaryOfRegions["Mainframe Tango: Capture Network Node (Aeon)"] = MainframeTangoAeon1
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Mainframe Tango: Capture Network Node (Aeon) " + str(index)
            objID = "230401"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            MainframeTangoAeon1.add_locations({lname: int(objID)}, SupComLocation)

    if "Mainframe Tango (Aeon)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoAeon2 = Region("Mainframe Tango: Save Network Node (Aeon)", world.player, world.multiworld)
        DictionaryOfRegions["Mainframe Tango: Save Network Node (Aeon)"] = MainframeTangoAeon2
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Mainframe Tango: Save Network Node (Aeon) " + str(index)
            objID = "230402"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            MainframeTangoAeon2.add_locations({lname: int(objID)}, SupComLocation)

    if "Mainframe Tango (Aeon)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoAeon3 = Region("Mainframe Tango: Save 80% civilian buildings (optional) (Aeon)", world.player, world.multiworld)
        DictionaryOfRegions["Mainframe Tango: Save 80% civilian buildings (optional) (Aeon)"] = MainframeTangoAeon3
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Mainframe Tango: Save 80% civilian buildings (optional) (Aeon) " + str(index)
            objID = "230403"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            MainframeTangoAeon3.add_locations({lname: int(objID)}, SupComLocation)

    if "Mainframe Tango (Aeon)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoAeon4 = Region("Mainframe Tango: Survive attacks (Aeon)", world.player, world.multiworld)
        DictionaryOfRegions["Mainframe Tango: Survive attacks (Aeon)"] = MainframeTangoAeon4
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Mainframe Tango: Survive attacks (Aeon) " + str(index)
            objID = "230404"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            MainframeTangoAeon4.add_locations({lname: int(objID)}, SupComLocation)

    if "Mainframe Tango (Aeon)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoAeon5 = Region("Mainframe Tango: Capture northeast node (Aeon)", world.player, world.multiworld)
        DictionaryOfRegions["Mainframe Tango: Capture northeast node (Aeon)"] = MainframeTangoAeon5
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Mainframe Tango: Capture northeast node (Aeon) " + str(index)
            objID = "230405"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            MainframeTangoAeon5.add_locations({lname: int(objID)}, SupComLocation)

    if "Mainframe Tango (Aeon)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoAeon6 = Region("Mainframe Tango: Capture northwest node (Aeon)", world.player, world.multiworld)
        DictionaryOfRegions["Mainframe Tango: Capture northwest node (Aeon)"] = MainframeTangoAeon6
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Mainframe Tango: Capture northwest node (Aeon) " + str(index)
            objID = "230406"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            MainframeTangoAeon6.add_locations({lname: int(objID)}, SupComLocation)

    if "Mainframe Tango (Aeon)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoAeon7 = Region("Mainframe Tango: Do not attack main Aeon base (Aeon)", world.player, world.multiworld)
        DictionaryOfRegions["Mainframe Tango: Do not attack main Aeon base (Aeon)"] = MainframeTangoAeon7
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Mainframe Tango: Do not attack main Aeon base (Aeon) " + str(index)
            objID = "230407"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            MainframeTangoAeon7.add_locations({lname: int(objID)}, SupComLocation)

    if "Mainframe Tango (Aeon)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoAeon8 = Region("Mainframe Tango: Kill Aeon Commander (Aeon)", world.player, world.multiworld)
        DictionaryOfRegions["Mainframe Tango: Kill Aeon Commander (Aeon)"] = MainframeTangoAeon8
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Mainframe Tango: Kill Aeon Commander (Aeon) " + str(index)
            objID = "230408"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            MainframeTangoAeon8.add_locations({lname: int(objID)}, SupComLocation)

    if "Unlock (Aeon)" in AllLevelsListToCheckRegionCreation:
        UnlockAeon0 = Region("Unlock: Destroy UEF generators (Aeon)", world.player, world.multiworld)
        DictionaryOfRegions["Unlock: Destroy UEF generators (Aeon)"] = UnlockAeon0
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Unlock: Destroy UEF generators (Aeon) " + str(index)
            objID = "230500"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            UnlockAeon0.add_locations({lname: int(objID)}, SupComLocation)

    if "Unlock (Aeon)" in AllLevelsListToCheckRegionCreation:
        UnlockAeon1 = Region("Unlock: Destroy UEF shipyards (optional) (Aeon)", world.player, world.multiworld)
        DictionaryOfRegions["Unlock: Destroy UEF shipyards (optional) (Aeon)"] = UnlockAeon1
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Unlock: Destroy UEF shipyards (optional) (Aeon) " + str(index)
            objID = "230501"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            UnlockAeon1.add_locations({lname: int(objID)}, SupComLocation)

    if "Unlock (Aeon)" in AllLevelsListToCheckRegionCreation:
        UnlockAeon2 = Region("Unlock: Destroy UEF radars (Aeon)", world.player, world.multiworld)
        DictionaryOfRegions["Unlock: Destroy UEF radars (Aeon)"] = UnlockAeon2
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Unlock: Destroy UEF radars (Aeon) " + str(index)
            objID = "230502"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            UnlockAeon2.add_locations({lname: int(objID)}, SupComLocation)

    if "Unlock (Aeon)" in AllLevelsListToCheckRegionCreation:
        UnlockAeon3 = Region("Unlock: Go to Hex5 (Aeon)", world.player, world.multiworld)
        DictionaryOfRegions["Unlock: Go to Hex5 (Aeon)"] = UnlockAeon3
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Unlock: Go to Hex5 (Aeon) " + str(index)
            objID = "230503"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            UnlockAeon3.add_locations({lname: int(objID)}, SupComLocation)

    if "Unlock (Aeon)" in AllLevelsListToCheckRegionCreation:
        UnlockAeon4 = Region("Unlock: Defend from heavy gunships (Aeon)", world.player, world.multiworld)
        DictionaryOfRegions["Unlock: Defend from heavy gunships (Aeon)"] = UnlockAeon4
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Unlock: Defend from heavy gunships (Aeon) " + str(index)
            objID = "230504"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            UnlockAeon4.add_locations({lname: int(objID)}, SupComLocation)

    if "Unlock (Aeon)" in AllLevelsListToCheckRegionCreation:
        UnlockAeon5 = Region("Unlock: Infect UEF landing pad (optional) (Aeon)", world.player, world.multiworld)
        DictionaryOfRegions["Unlock: Infect UEF landing pad (optional) (Aeon)"] = UnlockAeon5
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Unlock: Infect UEF landing pad (optional) (Aeon) " + str(index)
            objID = "230505"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            UnlockAeon5.add_locations({lname: int(objID)}, SupComLocation)

    if "Unlock (Aeon)" in AllLevelsListToCheckRegionCreation:
        UnlockAeon6 = Region("Unlock: This will be retconned later (Aeon)", world.player, world.multiworld)
        DictionaryOfRegions["Unlock: This will be retconned later (Aeon)"] = UnlockAeon6
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Unlock: This will be retconned later (Aeon) " + str(index)
            objID = "230506"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            UnlockAeon6.add_locations({lname: int(objID)}, SupComLocation)

    if "Unlock (Aeon)" in AllLevelsListToCheckRegionCreation:
        UnlockAeon7 = Region("Unlock: Kill UEF Commander (Aeon)", world.player, world.multiworld)
        DictionaryOfRegions["Unlock: Kill UEF Commander (Aeon)"] = UnlockAeon7
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Unlock: Kill UEF Commander (Aeon) " + str(index)
            objID = "230507"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            UnlockAeon7.add_locations({lname: int(objID)}, SupComLocation)

    if "Freedom (Aeon)" in AllLevelsListToCheckRegionCreation:
        FreedomAeon0 = Region("Freedom: Destroy CZAR (Aeon)", world.player, world.multiworld)
        DictionaryOfRegions["Freedom: Destroy CZAR (Aeon)"] = FreedomAeon0
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Freedom: Destroy CZAR (Aeon) " + str(index)
            objID = "230600"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            FreedomAeon0.add_locations({lname: int(objID)}, SupComLocation)

    if "Freedom (Aeon)" in AllLevelsListToCheckRegionCreation:
        FreedomAeon1 = Region("Freedom: Build Quantum Gate (Aeon)", world.player, world.multiworld)
        DictionaryOfRegions["Freedom: Build Quantum Gate (Aeon)"] = FreedomAeon1
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Freedom: Build Quantum Gate (Aeon) " + str(index)
            objID = "230601"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            FreedomAeon1.add_locations({lname: int(objID)}, SupComLocation)

    if "Freedom (Aeon)" in AllLevelsListToCheckRegionCreation:
        FreedomAeon2 = Region("Freedom: Download Quantum Virus (Aeon)", world.player, world.multiworld)
        DictionaryOfRegions["Freedom: Download Quantum Virus (Aeon)"] = FreedomAeon2
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Freedom: Download Quantum Virus (Aeon) " + str(index)
            objID = "230602"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            FreedomAeon2.add_locations({lname: int(objID)}, SupComLocation)

    if "Freedom (Aeon)" in AllLevelsListToCheckRegionCreation:
        FreedomAeon3 = Region("Freedom: Capture Black Sun control center (Aeon)", world.player, world.multiworld)
        DictionaryOfRegions["Freedom: Capture Black Sun control center (Aeon)"] = FreedomAeon3
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Freedom: Capture Black Sun control center (Aeon) " + str(index)
            objID = "230603"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            FreedomAeon3.add_locations({lname: int(objID)}, SupComLocation)

    if "Freedom (Aeon)" in AllLevelsListToCheckRegionCreation:
        FreedomAeon4 = Region("Freedom: Capture Black Sun (Aeon)", world.player, world.multiworld)
        DictionaryOfRegions["Freedom: Capture Black Sun (Aeon)"] = FreedomAeon4
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Freedom: Capture Black Sun (Aeon) " + str(index)
            objID = "230604"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            FreedomAeon4.add_locations({lname: int(objID)}, SupComLocation)

    if "Freedom (Aeon)" in AllLevelsListToCheckRegionCreation:
        FreedomAeon5 = Region("Freedom: Shoot Black Sun (Aeon)", world.player, world.multiworld)
        DictionaryOfRegions["Freedom: Shoot Black Sun (Aeon)"] = FreedomAeon5
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Freedom: Shoot Black Sun (Aeon) " + str(index)
            objID = "230605"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            FreedomAeon5.add_locations({lname: int(objID)}, SupComLocation)

    if "Liberation (Sera)" in AllLevelsListToCheckRegionCreation:
        LiberationSera0 = Region("Liberation: Build mass (Sera)", world.player, world.multiworld)
        DictionaryOfRegions["Liberation: Build mass (Sera)"] = LiberationSera0
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Liberation: Build mass (Sera) " + str(index)
            objID = "240100"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            LiberationSera0.add_locations({lname: int(objID)}, SupComLocation)

    if "Liberation (Sera)" in AllLevelsListToCheckRegionCreation:
        LiberationSera1 = Region("Liberation: Build power (Sera)", world.player, world.multiworld)
        DictionaryOfRegions["Liberation: Build power (Sera)"] = LiberationSera1
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Liberation: Build power (Sera) " + str(index)
            objID = "240101"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            LiberationSera1.add_locations({lname: int(objID)}, SupComLocation)

    if "Liberation (Sera)" in AllLevelsListToCheckRegionCreation:
        LiberationSera2 = Region("Liberation: Build air factory (Sera)", world.player, world.multiworld)
        DictionaryOfRegions["Liberation: Build air factory (Sera)"] = LiberationSera2
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Liberation: Build air factory (Sera) " + str(index)
            objID = "240102"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            LiberationSera2.add_locations({lname: int(objID)}, SupComLocation)

    if "Liberation (Sera)" in AllLevelsListToCheckRegionCreation:
        LiberationSera3 = Region("Liberation: Build bombers (Sera)", world.player, world.multiworld)
        DictionaryOfRegions["Liberation: Build bombers (Sera)"] = LiberationSera3
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Liberation: Build bombers (Sera) " + str(index)
            objID = "240103"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            LiberationSera3.add_locations({lname: int(objID)}, SupComLocation)

    if "Liberation (Sera)" in AllLevelsListToCheckRegionCreation:
        LiberationSera4 = Region("Liberation: Destroy radar defenders (Sera)", world.player, world.multiworld)
        DictionaryOfRegions["Liberation: Destroy radar defenders (Sera)"] = LiberationSera4
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Liberation: Destroy radar defenders (Sera) " + str(index)
            objID = "240104"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            LiberationSera4.add_locations({lname: int(objID)}, SupComLocation)

    if "Liberation (Sera)" in AllLevelsListToCheckRegionCreation:
        LiberationSera5 = Region("Liberation: Capture radars (Sera)", world.player, world.multiworld)
        DictionaryOfRegions["Liberation: Capture radars (Sera)"] = LiberationSera5
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Liberation: Capture radars (Sera) " + str(index)
            objID = "240105"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            LiberationSera5.add_locations({lname: int(objID)}, SupComLocation)

    if "Liberation (Sera)" in AllLevelsListToCheckRegionCreation:
        LiberationSera6 = Region("Liberation: Destroy mex (Sera)", world.player, world.multiworld)
        DictionaryOfRegions["Liberation: Destroy mex (Sera)"] = LiberationSera6
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Liberation: Destroy mex (Sera) " + str(index)
            objID = "240106"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            LiberationSera6.add_locations({lname: int(objID)}, SupComLocation)

    if "Liberation (Sera)" in AllLevelsListToCheckRegionCreation:
        LiberationSera7 = Region("Liberation: Destroy UEF defences (Sera)", world.player, world.multiworld)
        DictionaryOfRegions["Liberation: Destroy UEF defences (Sera)"] = LiberationSera7
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Liberation: Destroy UEF defences (Sera) " + str(index)
            objID = "240107"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            LiberationSera7.add_locations({lname: int(objID)}, SupComLocation)

    if "Liberation (Sera)" in AllLevelsListToCheckRegionCreation:
        LiberationSera8 = Region("Liberation: Destroy UEF patrols (Sera)", world.player, world.multiworld)
        DictionaryOfRegions["Liberation: Destroy UEF patrols (Sera)"] = LiberationSera8
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Liberation: Destroy UEF patrols (Sera) " + str(index)
            objID = "240108"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            LiberationSera8.add_locations({lname: int(objID)}, SupComLocation)

    if "Liberation (Sera)" in AllLevelsListToCheckRegionCreation:
        LiberationSera9 = Region("Liberation: Destroy UEF base defenders (Sera)", world.player, world.multiworld)
        DictionaryOfRegions["Liberation: Destroy UEF base defenders (Sera)"] = LiberationSera9
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Liberation: Destroy UEF base defenders (Sera) " + str(index)
            objID = "240109"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            LiberationSera9.add_locations({lname: int(objID)}, SupComLocation)

    if "Liberation (Sera)" in AllLevelsListToCheckRegionCreation:
        LiberationSera10 = Region("Liberation: Destroy UEF base (Sera)", world.player, world.multiworld)
        DictionaryOfRegions["Liberation: Destroy UEF base (Sera)"] = LiberationSera10
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Liberation: Destroy UEF base (Sera) " + str(index)
            objID = "240110"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            LiberationSera10.add_locations({lname: int(objID)}, SupComLocation)

    if "Liberation (Sera)" in AllLevelsListToCheckRegionCreation:
        LiberationSera11 = Region("Liberation: Kill Aeon Commander (Sera)", world.player, world.multiworld)
        DictionaryOfRegions["Liberation: Kill Aeon Commander (Sera)"] = LiberationSera11
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Liberation: Kill Aeon Commander (Sera) " + str(index)
            objID = "240111"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            LiberationSera11.add_locations({lname: int(objID)}, SupComLocation)

    if "Artifact (Sera)" in AllLevelsListToCheckRegionCreation:
        ArtifactSera0 = Region("Artifact: Destroy first village defenders (Sera)", world.player, world.multiworld)
        DictionaryOfRegions["Artifact: Destroy first village defenders (Sera)"] = ArtifactSera0
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Artifact: Destroy first village defenders (Sera) " + str(index)
            objID = "240200"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            ArtifactSera0.add_locations({lname: int(objID)}, SupComLocation)

    if "Artifact (Sera)" in AllLevelsListToCheckRegionCreation:
        ArtifactSera1 = Region("Artifact: Destroy first temple (Sera)", world.player, world.multiworld)
        DictionaryOfRegions["Artifact: Destroy first temple (Sera)"] = ArtifactSera1
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Artifact: Destroy first temple (Sera) " + str(index)
            objID = "240201"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            ArtifactSera1.add_locations({lname: int(objID)}, SupComLocation)

    if "Artifact (Sera)" in AllLevelsListToCheckRegionCreation:
        ArtifactSera2 = Region("Artifact: Protect first artifact (Sera)", world.player, world.multiworld)
        DictionaryOfRegions["Artifact: Protect first artifact (Sera)"] = ArtifactSera2
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Artifact: Protect first artifact (Sera) " + str(index)
            objID = "240202"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            ArtifactSera2.add_locations({lname: int(objID)}, SupComLocation)

    if "Artifact (Sera)" in AllLevelsListToCheckRegionCreation:
        ArtifactSera3 = Region("Artifact: Find second artifact (Sera)", world.player, world.multiworld)
        DictionaryOfRegions["Artifact: Find second artifact (Sera)"] = ArtifactSera3
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Artifact: Find second artifact (Sera) " + str(index)
            objID = "240203"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            ArtifactSera3.add_locations({lname: int(objID)}, SupComLocation)

    if "Artifact (Sera)" in AllLevelsListToCheckRegionCreation:
        ArtifactSera4 = Region("Artifact: Destroy Aeon reinforcements (Sera)", world.player, world.multiworld)
        DictionaryOfRegions["Artifact: Destroy Aeon reinforcements (Sera)"] = ArtifactSera4
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Artifact: Destroy Aeon reinforcements (Sera) " + str(index)
            objID = "240204"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            ArtifactSera4.add_locations({lname: int(objID)}, SupComLocation)

    if "Artifact (Sera)" in AllLevelsListToCheckRegionCreation:
        ArtifactSera5 = Region("Artifact: Protect second artifact (Sera)", world.player, world.multiworld)
        DictionaryOfRegions["Artifact: Protect second artifact (Sera)"] = ArtifactSera5
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Artifact: Protect second artifact (Sera) " + str(index)
            objID = "240205"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            ArtifactSera5.add_locations({lname: int(objID)}, SupComLocation)

    if "Artifact (Sera)" in AllLevelsListToCheckRegionCreation:
        ArtifactSera6 = Region("Artifact: Defend from Aeon attack (Sera)", world.player, world.multiworld)
        DictionaryOfRegions["Artifact: Defend from Aeon attack (Sera)"] = ArtifactSera6
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Artifact: Defend from Aeon attack (Sera) " + str(index)
            objID = "240206"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            ArtifactSera6.add_locations({lname: int(objID)}, SupComLocation)

    if "Artifact (Sera)" in AllLevelsListToCheckRegionCreation:
        ArtifactSera7 = Region("Artifact: Destroy eastern base (Sera)", world.player, world.multiworld)
        DictionaryOfRegions["Artifact: Destroy eastern base (Sera)"] = ArtifactSera7
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Artifact: Destroy eastern base (Sera) " + str(index)
            objID = "240207"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            ArtifactSera7.add_locations({lname: int(objID)}, SupComLocation)

    if "Artifact (Sera)" in AllLevelsListToCheckRegionCreation:
        ArtifactSera8 = Region("Artifact: Destroy navy base (Sera)", world.player, world.multiworld)
        DictionaryOfRegions["Artifact: Destroy navy base (Sera)"] = ArtifactSera8
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Artifact: Destroy navy base (Sera) " + str(index)
            objID = "240208"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            ArtifactSera8.add_locations({lname: int(objID)}, SupComLocation)

    if "Artifact (Sera)" in AllLevelsListToCheckRegionCreation:
        ArtifactSera9 = Region("Artifact: Protect third artifact (Sera)", world.player, world.multiworld)
        DictionaryOfRegions["Artifact: Protect third artifact (Sera)"] = ArtifactSera9
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Artifact: Protect third artifact (Sera) " + str(index)
            objID = "240209"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            ArtifactSera9.add_locations({lname: int(objID)}, SupComLocation)

    if "Artifact (Sera)" in AllLevelsListToCheckRegionCreation:
        ArtifactSera10 = Region("Artifact: Kill Aeon Commander (optional) (Sera)", world.player, world.multiworld)
        DictionaryOfRegions["Artifact: Kill Aeon Commander (optional) (Sera)"] = ArtifactSera10
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Artifact: Kill Aeon Commander (optional) (Sera) " + str(index)
            objID = "240210"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            ArtifactSera10.add_locations({lname: int(objID)}, SupComLocation)

    if "Artifact (Sera)" in AllLevelsListToCheckRegionCreation:
        ArtifactSera11 = Region("Artifact: Kill Mach (Sera)", world.player, world.multiworld)
        DictionaryOfRegions["Artifact: Kill Mach (Sera)"] = ArtifactSera11
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Artifact: Kill Mach (Sera) " + str(index)
            objID = "240211"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            ArtifactSera11.add_locations({lname: int(objID)}, SupComLocation)

    if "Artifact (Sera)" in AllLevelsListToCheckRegionCreation:
        ArtifactSera12 = Region("Artifact: Go to Gate (Sera)", world.player, world.multiworld)
        DictionaryOfRegions["Artifact: Go to Gate (Sera)"] = ArtifactSera12
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Artifact: Go to Gate (Sera) " + str(index)
            objID = "240212"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            ArtifactSera12.add_locations({lname: int(objID)}, SupComLocation)

    if "Defrag (Sera)" in AllLevelsListToCheckRegionCreation:
        DefragSera0 = Region("Defrag: Protect York 18 (Sera)", world.player, world.multiworld)
        DictionaryOfRegions["Defrag: Protect York 18 (Sera)"] = DefragSera0
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Defrag: Protect York 18 (Sera) " + str(index)
            objID = "240300"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            DefragSera0.add_locations({lname: int(objID)}, SupComLocation)

    if "Defrag (Sera)" in AllLevelsListToCheckRegionCreation:
        DefragSera1 = Region("Defrag: Destroy western UEF base (Sera)", world.player, world.multiworld)
        DictionaryOfRegions["Defrag: Destroy western UEF base (Sera)"] = DefragSera1
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Defrag: Destroy western UEF base (Sera) " + str(index)
            objID = "240301"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            DefragSera1.add_locations({lname: int(objID)}, SupComLocation)

    if "Defrag (Sera)" in AllLevelsListToCheckRegionCreation:
        DefragSera2 = Region("Defrag: Destroy north-western UEF base (Sera)", world.player, world.multiworld)
        DictionaryOfRegions["Defrag: Destroy north-western UEF base (Sera)"] = DefragSera2
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Defrag: Destroy north-western UEF base (Sera) " + str(index)
            objID = "240302"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            DefragSera2.add_locations({lname: int(objID)}, SupComLocation)

    if "Defrag (Sera)" in AllLevelsListToCheckRegionCreation:
        DefragSera3 = Region("Defrag: Destroy northern UEF base (Sera)", world.player, world.multiworld)
        DictionaryOfRegions["Defrag: Destroy northern UEF base (Sera)"] = DefragSera3
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Defrag: Destroy northern UEF base (Sera) " + str(index)
            objID = "240303"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            DefragSera3.add_locations({lname: int(objID)}, SupComLocation)

    if "Defrag (Sera)" in AllLevelsListToCheckRegionCreation:
        DefragSera4 = Region("Defrag: Sink UEF cruiser (Sera)", world.player, world.multiworld)
        DictionaryOfRegions["Defrag: Sink UEF cruiser (Sera)"] = DefragSera4
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Defrag: Sink UEF cruiser (Sera) " + str(index)
            objID = "240304"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            DefragSera4.add_locations({lname: int(objID)}, SupComLocation)

    if "Defrag (Sera)" in AllLevelsListToCheckRegionCreation:
        DefragSera5 = Region("Defrag: Destroy static artillery (Sera)", world.player, world.multiworld)
        DictionaryOfRegions["Defrag: Destroy static artillery (Sera)"] = DefragSera5
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Defrag: Destroy static artillery (Sera) " + str(index)
            objID = "240305"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            DefragSera5.add_locations({lname: int(objID)}, SupComLocation)

    if "Defrag (Sera)" in AllLevelsListToCheckRegionCreation:
        DefragSera6 = Region("Defrag: Escort trucks (Sera)", world.player, world.multiworld)
        DictionaryOfRegions["Defrag: Escort trucks (Sera)"] = DefragSera6
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Defrag: Escort trucks (Sera) " + str(index)
            objID = "240306"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            DefragSera6.add_locations({lname: int(objID)}, SupComLocation)

    if "Defrag (Sera)" in AllLevelsListToCheckRegionCreation:
        DefragSera7 = Region("Defrag: Escort ALL trucks (optional) (Sera)", world.player, world.multiworld)
        DictionaryOfRegions["Defrag: Escort ALL trucks (optional) (Sera)"] = DefragSera7
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Defrag: Escort ALL trucks (optional) (Sera) " + str(index)
            objID = "240307"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            DefragSera7.add_locations({lname: int(objID)}, SupComLocation)

    if "Defrag (Sera)" in AllLevelsListToCheckRegionCreation:
        DefragSera8 = Region("Defrag: Optional objective  (optional) (Sera)", world.player, world.multiworld)
        DictionaryOfRegions["Defrag: Optional objective  (optional) (Sera)"] = DefragSera8
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Defrag: Optional objective  (optional) (Sera) " + str(index)
            objID = "240308"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            DefragSera8.add_locations({lname: int(objID)}, SupComLocation)

    if "Defrag (Sera)" in AllLevelsListToCheckRegionCreation:
        DefragSera9 = Region("Defrag: Kill UEF Commander (Sera)", world.player, world.multiworld)
        DictionaryOfRegions["Defrag: Kill UEF Commander (Sera)"] = DefragSera9
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Defrag: Kill UEF Commander (Sera) " + str(index)
            objID = "240309"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            DefragSera9.add_locations({lname: int(objID)}, SupComLocation)

    if "Mainframe Tango (Sera)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoSera0 = Region("Mainframe Tango: Defeat Aeon Commander (Sera)", world.player, world.multiworld)
        DictionaryOfRegions["Mainframe Tango: Defeat Aeon Commander (Sera)"] = MainframeTangoSera0
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Mainframe Tango: Defeat Aeon Commander (Sera) " + str(index)
            objID = "240400"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            MainframeTangoSera0.add_locations({lname: int(objID)}, SupComLocation)

    if "Mainframe Tango (Sera)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoSera1 = Region("Mainframe Tango: Capture Network Node (Sera)", world.player, world.multiworld)
        DictionaryOfRegions["Mainframe Tango: Capture Network Node (Sera)"] = MainframeTangoSera1
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Mainframe Tango: Capture Network Node (Sera) " + str(index)
            objID = "240401"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            MainframeTangoSera1.add_locations({lname: int(objID)}, SupComLocation)

    if "Mainframe Tango (Sera)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoSera2 = Region("Mainframe Tango: Save Network Node (Sera)", world.player, world.multiworld)
        DictionaryOfRegions["Mainframe Tango: Save Network Node (Sera)"] = MainframeTangoSera2
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Mainframe Tango: Save Network Node (Sera) " + str(index)
            objID = "240402"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            MainframeTangoSera2.add_locations({lname: int(objID)}, SupComLocation)

    if "Mainframe Tango (Sera)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoSera3 = Region("Mainframe Tango: Save 80% civilian buildings (optional) (Sera)", world.player, world.multiworld)
        DictionaryOfRegions["Mainframe Tango: Save 80% civilian buildings (optional) (Sera)"] = MainframeTangoSera3
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Mainframe Tango: Save 80% civilian buildings (optional) (Sera) " + str(index)
            objID = "240403"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            MainframeTangoSera3.add_locations({lname: int(objID)}, SupComLocation)

    if "Mainframe Tango (Sera)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoSera4 = Region("Mainframe Tango: Survive attacks (Sera)", world.player, world.multiworld)
        DictionaryOfRegions["Mainframe Tango: Survive attacks (Sera)"] = MainframeTangoSera4
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Mainframe Tango: Survive attacks (Sera) " + str(index)
            objID = "240404"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            MainframeTangoSera4.add_locations({lname: int(objID)}, SupComLocation)

    if "Mainframe Tango (Sera)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoSera5 = Region("Mainframe Tango: Capture northeast node (Sera)", world.player, world.multiworld)
        DictionaryOfRegions["Mainframe Tango: Capture northeast node (Sera)"] = MainframeTangoSera5
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Mainframe Tango: Capture northeast node (Sera) " + str(index)
            objID = "240405"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            MainframeTangoSera5.add_locations({lname: int(objID)}, SupComLocation)

    if "Mainframe Tango (Sera)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoSera6 = Region("Mainframe Tango: Capture northwest node (Sera)", world.player, world.multiworld)
        DictionaryOfRegions["Mainframe Tango: Capture northwest node (Sera)"] = MainframeTangoSera6
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Mainframe Tango: Capture northwest node (Sera) " + str(index)
            objID = "240406"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            MainframeTangoSera6.add_locations({lname: int(objID)}, SupComLocation)

    if "Mainframe Tango (Sera)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoSera7 = Region("Mainframe Tango: Do not attack main Aeon base (Sera)", world.player, world.multiworld)
        DictionaryOfRegions["Mainframe Tango: Do not attack main Aeon base (Sera)"] = MainframeTangoSera7
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Mainframe Tango: Do not attack main Aeon base (Sera) " + str(index)
            objID = "240407"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            MainframeTangoSera7.add_locations({lname: int(objID)}, SupComLocation)

    if "Mainframe Tango (Sera)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoSera8 = Region("Mainframe Tango: Kill Aeon Commander (Sera)", world.player, world.multiworld)
        DictionaryOfRegions["Mainframe Tango: Kill Aeon Commander (Sera)"] = MainframeTangoSera8
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Mainframe Tango: Kill Aeon Commander (Sera) " + str(index)
            objID = "240408"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            MainframeTangoSera8.add_locations({lname: int(objID)}, SupComLocation)

    if "Unlock (Sera)" in AllLevelsListToCheckRegionCreation:
        UnlockSera0 = Region("Unlock: Destroy UEF generators (Sera)", world.player, world.multiworld)
        DictionaryOfRegions["Unlock: Destroy UEF generators (Sera)"] = UnlockSera0
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Unlock: Destroy UEF generators (Sera) " + str(index)
            objID = "240500"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            UnlockSera0.add_locations({lname: int(objID)}, SupComLocation)

    if "Unlock (Sera)" in AllLevelsListToCheckRegionCreation:
        UnlockSera1 = Region("Unlock: Destroy UEF shipyards (optional) (Sera)", world.player, world.multiworld)
        DictionaryOfRegions["Unlock: Destroy UEF shipyards (optional) (Sera)"] = UnlockSera1
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Unlock: Destroy UEF shipyards (optional) (Sera) " + str(index)
            objID = "240501"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            UnlockSera1.add_locations({lname: int(objID)}, SupComLocation)

    if "Unlock (Sera)" in AllLevelsListToCheckRegionCreation:
        UnlockSera2 = Region("Unlock: Destroy UEF radars (Sera)", world.player, world.multiworld)
        DictionaryOfRegions["Unlock: Destroy UEF radars (Sera)"] = UnlockSera2
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Unlock: Destroy UEF radars (Sera) " + str(index)
            objID = "240502"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            UnlockSera2.add_locations({lname: int(objID)}, SupComLocation)

    if "Unlock (Sera)" in AllLevelsListToCheckRegionCreation:
        UnlockSera3 = Region("Unlock: Go to Hex5 (Sera)", world.player, world.multiworld)
        DictionaryOfRegions["Unlock: Go to Hex5 (Sera)"] = UnlockSera3
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Unlock: Go to Hex5 (Sera) " + str(index)
            objID = "240503"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            UnlockSera3.add_locations({lname: int(objID)}, SupComLocation)

    if "Unlock (Sera)" in AllLevelsListToCheckRegionCreation:
        UnlockSera4 = Region("Unlock: Defend from heavy gunships (Sera)", world.player, world.multiworld)
        DictionaryOfRegions["Unlock: Defend from heavy gunships (Sera)"] = UnlockSera4
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Unlock: Defend from heavy gunships (Sera) " + str(index)
            objID = "240504"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            UnlockSera4.add_locations({lname: int(objID)}, SupComLocation)

    if "Unlock (Sera)" in AllLevelsListToCheckRegionCreation:
        UnlockSera5 = Region("Unlock: Infect UEF landing pad (optional) (Sera)", world.player, world.multiworld)
        DictionaryOfRegions["Unlock: Infect UEF landing pad (optional) (Sera)"] = UnlockSera5
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Unlock: Infect UEF landing pad (optional) (Sera) " + str(index)
            objID = "240505"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            UnlockSera5.add_locations({lname: int(objID)}, SupComLocation)

    if "Unlock (Sera)" in AllLevelsListToCheckRegionCreation:
        UnlockSera6 = Region("Unlock: This will be retconned later (Sera)", world.player, world.multiworld)
        DictionaryOfRegions["Unlock: This will be retconned later (Sera)"] = UnlockSera6
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Unlock: This will be retconned later (Sera) " + str(index)
            objID = "240506"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            UnlockSera6.add_locations({lname: int(objID)}, SupComLocation)

    if "Unlock (Sera)" in AllLevelsListToCheckRegionCreation:
        UnlockSera7 = Region("Unlock: Kill UEF Commander (Sera)", world.player, world.multiworld)
        DictionaryOfRegions["Unlock: Kill UEF Commander (Sera)"] = UnlockSera7
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Unlock: Kill UEF Commander (Sera) " + str(index)
            objID = "240507"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            UnlockSera7.add_locations({lname: int(objID)}, SupComLocation)

    if "Freedom (Sera)" in AllLevelsListToCheckRegionCreation:
        FreedomSera0 = Region("Freedom: Destroy CZAR (Sera)", world.player, world.multiworld)
        DictionaryOfRegions["Freedom: Destroy CZAR (Sera)"] = FreedomSera0
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Freedom: Destroy CZAR (Sera) " + str(index)
            objID = "240600"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            FreedomSera0.add_locations({lname: int(objID)}, SupComLocation)

    if "Freedom (Sera)" in AllLevelsListToCheckRegionCreation:
        FreedomSera1 = Region("Freedom: Build Quantum Gate (Sera)", world.player, world.multiworld)
        DictionaryOfRegions["Freedom: Build Quantum Gate (Sera)"] = FreedomSera1
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Freedom: Build Quantum Gate (Sera) " + str(index)
            objID = "240601"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            FreedomSera1.add_locations({lname: int(objID)}, SupComLocation)

    if "Freedom (Sera)" in AllLevelsListToCheckRegionCreation:
        FreedomSera2 = Region("Freedom: Download Quantum Virus (Sera)", world.player, world.multiworld)
        DictionaryOfRegions["Freedom: Download Quantum Virus (Sera)"] = FreedomSera2
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Freedom: Download Quantum Virus (Sera) " + str(index)
            objID = "240602"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            FreedomSera2.add_locations({lname: int(objID)}, SupComLocation)

    if "Freedom (Sera)" in AllLevelsListToCheckRegionCreation:
        FreedomSera3 = Region("Freedom: Capture Black Sun control center (Sera)", world.player, world.multiworld)
        DictionaryOfRegions["Freedom: Capture Black Sun control center (Sera)"] = FreedomSera3
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Freedom: Capture Black Sun control center (Sera) " + str(index)
            objID = "240603"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            FreedomSera3.add_locations({lname: int(objID)}, SupComLocation)

    if "Freedom (Sera)" in AllLevelsListToCheckRegionCreation:
        FreedomSera4 = Region("Freedom: Capture Black Sun (Sera)", world.player, world.multiworld)
        DictionaryOfRegions["Freedom: Capture Black Sun (Sera)"] = FreedomSera4
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Freedom: Capture Black Sun (Sera) " + str(index)
            objID = "240604"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            FreedomSera4.add_locations({lname: int(objID)}, SupComLocation)

    if "Freedom (Sera)" in AllLevelsListToCheckRegionCreation:
        FreedomSera5 = Region("Freedom: Shoot Black Sun (Sera)", world.player, world.multiworld)
        DictionaryOfRegions["Freedom: Shoot Black Sun (Sera)"] = FreedomSera5
        for i in range(0, world.options.locamount):
            index = i + 1
            lname = "Freedom: Shoot Black Sun (Sera) " + str(index)
            objID = "240605"
            if i < 10:
                objID = objID + "0"
            objID = objID + str(i)
            FreedomSera5.add_locations({lname: int(objID)}, SupComLocation)


    TotalListOfTtotallyLevels = {}
    TempRegionlist = []
    TempRegionlist.append("Liberation: Build mass (UEF)")
    TempRegionlist.append("Liberation: Build power (UEF)")
    TempRegionlist.append("Liberation: Build air factory (UEF)")
    TempRegionlist.append("Liberation: Build bombers (UEF)")
    TempRegionlist.append("Liberation: Destroy radar defenders (UEF)")
    TempRegionlist.append("Liberation: Capture radars (UEF)")
    TempRegionlist.append("Liberation: Destroy mex (UEF)")
    TempRegionlist.append("Liberation: Destroy UEF defences (UEF)")
    TempRegionlist.append("Liberation: Destroy UEF patrols (UEF)")
    TempRegionlist.append("Liberation: Destroy UEF base defenders (UEF)")
    TempRegionlist.append("Liberation: Destroy UEF base (UEF)")
    TempRegionlist.append("Liberation: Kill Aeon Commander (UEF)")
    TotalListOfTtotallyLevels["Liberation (UEF)"] = TempRegionlist
    TempRegionlist = []
    TempRegionlist.append("Artifact: Destroy first village defenders (UEF)")
    TempRegionlist.append("Artifact: Destroy first temple (UEF)")
    TempRegionlist.append("Artifact: Protect first artifact (UEF)")
    TempRegionlist.append("Artifact: Find second artifact (UEF)")
    TempRegionlist.append("Artifact: Destroy Aeon reinforcements (UEF)")
    TempRegionlist.append("Artifact: Protect second artifact (UEF)")
    TempRegionlist.append("Artifact: Defend from Aeon attack (UEF)")
    TempRegionlist.append("Artifact: Destroy eastern base (UEF)")
    TempRegionlist.append("Artifact: Destroy navy base (UEF)")
    TempRegionlist.append("Artifact: Protect third artifact (UEF)")
    TempRegionlist.append("Artifact: Kill Aeon Commander (optional) (UEF)")
    TempRegionlist.append("Artifact: Kill Mach (UEF)")
    TempRegionlist.append("Artifact: Go to Gate (UEF)")
    TotalListOfTtotallyLevels["Artifact (UEF)"] = TempRegionlist
    TempRegionlist = []
    TempRegionlist.append("Defrag: Protect York 18 (UEF)")
    TempRegionlist.append("Defrag: Destroy western UEF base (UEF)")
    TempRegionlist.append("Defrag: Destroy north-western UEF base (UEF)")
    TempRegionlist.append("Defrag: Destroy northern UEF base (UEF)")
    TempRegionlist.append("Defrag: Sink UEF cruiser (UEF)")
    TempRegionlist.append("Defrag: Destroy static artillery (UEF)")
    TempRegionlist.append("Defrag: Escort trucks (UEF)")
    TempRegionlist.append("Defrag: Escort ALL trucks (optional) (UEF)")
    TempRegionlist.append("Defrag: Optional objective  (optional) (UEF)")
    TempRegionlist.append("Defrag: Kill UEF Commander (UEF)")
    TotalListOfTtotallyLevels["Defrag (UEF)"] = TempRegionlist
    TempRegionlist = []
    TempRegionlist.append("Mainframe Tango: Defeat Aeon Commander (UEF)")
    TempRegionlist.append("Mainframe Tango: Capture Network Node (UEF)")
    TempRegionlist.append("Mainframe Tango: Save Network Node (UEF)")
    TempRegionlist.append("Mainframe Tango: Save 80% civilian buildings (optional) (UEF)")
    TempRegionlist.append("Mainframe Tango: Survive attacks (UEF)")
    TempRegionlist.append("Mainframe Tango: Capture northeast node (UEF)")
    TempRegionlist.append("Mainframe Tango: Capture northwest node (UEF)")
    TempRegionlist.append("Mainframe Tango: Do not attack main Aeon base (UEF)")
    TempRegionlist.append("Mainframe Tango: Kill Aeon Commander (UEF)")
    TotalListOfTtotallyLevels["Mainframe Tango (UEF)"] = TempRegionlist
    TempRegionlist = []
    TempRegionlist.append("Unlock: Destroy UEF generators (UEF)")
    TempRegionlist.append("Unlock: Destroy UEF shipyards (optional) (UEF)")
    TempRegionlist.append("Unlock: Destroy UEF radars (UEF)")
    TempRegionlist.append("Unlock: Go to Hex5 (UEF)")
    TempRegionlist.append("Unlock: Defend from heavy gunships (UEF)")
    TempRegionlist.append("Unlock: Infect UEF landing pad (optional) (UEF)")
    TempRegionlist.append("Unlock: This will be retconned later (UEF)")
    TempRegionlist.append("Unlock: Kill UEF Commander (UEF)")
    TotalListOfTtotallyLevels["Unlock (UEF)"] = TempRegionlist
    TempRegionlist = []
    TempRegionlist.append("Freedom: Destroy CZAR (UEF)")
    TempRegionlist.append("Freedom: Build Quantum Gate (UEF)")
    TempRegionlist.append("Freedom: Download Quantum Virus (UEF)")
    TempRegionlist.append("Freedom: Capture Black Sun control center (UEF)")
    TempRegionlist.append("Freedom: Capture Black Sun (UEF)")
    TempRegionlist.append("Freedom: Shoot Black Sun (UEF)")
    TotalListOfTtotallyLevels["Freedom (UEF)"] = TempRegionlist
    TempRegionlist = []
    TempRegionlist.append("Liberation: Build mass (Cybran)")
    TempRegionlist.append("Liberation: Build power (Cybran)")
    TempRegionlist.append("Liberation: Build air factory (Cybran)")
    TempRegionlist.append("Liberation: Build bombers (Cybran)")
    TempRegionlist.append("Liberation: Destroy radar defenders (Cybran)")
    TempRegionlist.append("Liberation: Capture radars (Cybran)")
    TempRegionlist.append("Liberation: Destroy mex (Cybran)")
    TempRegionlist.append("Liberation: Destroy UEF defences (Cybran)")
    TempRegionlist.append("Liberation: Destroy UEF patrols (Cybran)")
    TempRegionlist.append("Liberation: Destroy UEF base defenders (Cybran)")
    TempRegionlist.append("Liberation: Destroy UEF base (Cybran)")
    TempRegionlist.append("Liberation: Kill Aeon Commander (Cybran)")
    TotalListOfTtotallyLevels["Liberation (Cybran)"] = TempRegionlist
    TempRegionlist = []
    TempRegionlist.append("Artifact: Destroy first village defenders (Cybran)")
    TempRegionlist.append("Artifact: Destroy first temple (Cybran)")
    TempRegionlist.append("Artifact: Protect first artifact (Cybran)")
    TempRegionlist.append("Artifact: Find second artifact (Cybran)")
    TempRegionlist.append("Artifact: Destroy Aeon reinforcements (Cybran)")
    TempRegionlist.append("Artifact: Protect second artifact (Cybran)")
    TempRegionlist.append("Artifact: Defend from Aeon attack (Cybran)")
    TempRegionlist.append("Artifact: Destroy eastern base (Cybran)")
    TempRegionlist.append("Artifact: Destroy navy base (Cybran)")
    TempRegionlist.append("Artifact: Protect third artifact (Cybran)")
    TempRegionlist.append("Artifact: Kill Aeon Commander (optional) (Cybran)")
    TempRegionlist.append("Artifact: Kill Mach (Cybran)")
    TempRegionlist.append("Artifact: Go to Gate (Cybran)")
    TotalListOfTtotallyLevels["Artifact (Cybran)"] = TempRegionlist
    TempRegionlist = []
    TempRegionlist.append("Defrag: Protect York 18 (Cybran)")
    TempRegionlist.append("Defrag: Destroy western UEF base (Cybran)")
    TempRegionlist.append("Defrag: Destroy north-western UEF base (Cybran)")
    TempRegionlist.append("Defrag: Destroy northern UEF base (Cybran)")
    TempRegionlist.append("Defrag: Sink UEF cruiser (Cybran)")
    TempRegionlist.append("Defrag: Destroy static artillery (Cybran)")
    TempRegionlist.append("Defrag: Escort trucks (Cybran)")
    TempRegionlist.append("Defrag: Escort ALL trucks (optional) (Cybran)")
    TempRegionlist.append("Defrag: Optional objective  (optional) (Cybran)")
    TempRegionlist.append("Defrag: Kill UEF Commander (Cybran)")
    TotalListOfTtotallyLevels["Defrag (Cybran)"] = TempRegionlist
    TempRegionlist = []
    TempRegionlist.append("Mainframe Tango: Defeat Aeon Commander (Cybran)")
    TempRegionlist.append("Mainframe Tango: Capture Network Node (Cybran)")
    TempRegionlist.append("Mainframe Tango: Save Network Node (Cybran)")
    TempRegionlist.append("Mainframe Tango: Save 80% civilian buildings (optional) (Cybran)")
    TempRegionlist.append("Mainframe Tango: Survive attacks (Cybran)")
    TempRegionlist.append("Mainframe Tango: Capture northeast node (Cybran)")
    TempRegionlist.append("Mainframe Tango: Capture northwest node (Cybran)")
    TempRegionlist.append("Mainframe Tango: Do not attack main Aeon base (Cybran)")
    TempRegionlist.append("Mainframe Tango: Kill Aeon Commander (Cybran)")
    TotalListOfTtotallyLevels["Mainframe Tango (Cybran)"] = TempRegionlist
    TempRegionlist = []
    TempRegionlist.append("Unlock: Destroy UEF generators (Cybran)")
    TempRegionlist.append("Unlock: Destroy UEF shipyards (optional) (Cybran)")
    TempRegionlist.append("Unlock: Destroy UEF radars (Cybran)")
    TempRegionlist.append("Unlock: Go to Hex5 (Cybran)")
    TempRegionlist.append("Unlock: Defend from heavy gunships (Cybran)")
    TempRegionlist.append("Unlock: Infect UEF landing pad (optional) (Cybran)")
    TempRegionlist.append("Unlock: This will be retconned later (Cybran)")
    TempRegionlist.append("Unlock: Kill UEF Commander (Cybran)")
    TotalListOfTtotallyLevels["Unlock (Cybran)"] = TempRegionlist
    TempRegionlist = []
    TempRegionlist.append("Freedom: Destroy CZAR (Cybran)")
    TempRegionlist.append("Freedom: Build Quantum Gate (Cybran)")
    TempRegionlist.append("Freedom: Download Quantum Virus (Cybran)")
    TempRegionlist.append("Freedom: Capture Black Sun control center (Cybran)")
    TempRegionlist.append("Freedom: Capture Black Sun (Cybran)")
    TempRegionlist.append("Freedom: Shoot Black Sun (Cybran)")
    TotalListOfTtotallyLevels["Freedom (Cybran)"] = TempRegionlist
    TempRegionlist = []
    TempRegionlist.append("Liberation: Build mass (Aeon)")
    TempRegionlist.append("Liberation: Build power (Aeon)")
    TempRegionlist.append("Liberation: Build air factory (Aeon)")
    TempRegionlist.append("Liberation: Build bombers (Aeon)")
    TempRegionlist.append("Liberation: Destroy radar defenders (Aeon)")
    TempRegionlist.append("Liberation: Capture radars (Aeon)")
    TempRegionlist.append("Liberation: Destroy mex (Aeon)")
    TempRegionlist.append("Liberation: Destroy UEF defences (Aeon)")
    TempRegionlist.append("Liberation: Destroy UEF patrols (Aeon)")
    TempRegionlist.append("Liberation: Destroy UEF base defenders (Aeon)")
    TempRegionlist.append("Liberation: Destroy UEF base (Aeon)")
    TempRegionlist.append("Liberation: Kill Aeon Commander (Aeon)")
    TotalListOfTtotallyLevels["Liberation (Aeon)"] = TempRegionlist
    TempRegionlist = []
    TempRegionlist.append("Artifact: Destroy first village defenders (Aeon)")
    TempRegionlist.append("Artifact: Destroy first temple (Aeon)")
    TempRegionlist.append("Artifact: Protect first artifact (Aeon)")
    TempRegionlist.append("Artifact: Find second artifact (Aeon)")
    TempRegionlist.append("Artifact: Destroy Aeon reinforcements (Aeon)")
    TempRegionlist.append("Artifact: Protect second artifact (Aeon)")
    TempRegionlist.append("Artifact: Defend from Aeon attack (Aeon)")
    TempRegionlist.append("Artifact: Destroy eastern base (Aeon)")
    TempRegionlist.append("Artifact: Destroy navy base (Aeon)")
    TempRegionlist.append("Artifact: Protect third artifact (Aeon)")
    TempRegionlist.append("Artifact: Kill Aeon Commander (optional) (Aeon)")
    TempRegionlist.append("Artifact: Kill Mach (Aeon)")
    TempRegionlist.append("Artifact: Go to Gate (Aeon)")
    TotalListOfTtotallyLevels["Artifact (Aeon)"] = TempRegionlist
    TempRegionlist = []
    TempRegionlist.append("Defrag: Protect York 18 (Aeon)")
    TempRegionlist.append("Defrag: Destroy western UEF base (Aeon)")
    TempRegionlist.append("Defrag: Destroy north-western UEF base (Aeon)")
    TempRegionlist.append("Defrag: Destroy northern UEF base (Aeon)")
    TempRegionlist.append("Defrag: Sink UEF cruiser (Aeon)")
    TempRegionlist.append("Defrag: Destroy static artillery (Aeon)")
    TempRegionlist.append("Defrag: Escort trucks (Aeon)")
    TempRegionlist.append("Defrag: Escort ALL trucks (optional) (Aeon)")
    TempRegionlist.append("Defrag: Optional objective  (optional) (Aeon)")
    TempRegionlist.append("Defrag: Kill UEF Commander (Aeon)")
    TotalListOfTtotallyLevels["Defrag (Aeon)"] = TempRegionlist
    TempRegionlist = []
    TempRegionlist.append("Mainframe Tango: Defeat Aeon Commander (Aeon)")
    TempRegionlist.append("Mainframe Tango: Capture Network Node (Aeon)")
    TempRegionlist.append("Mainframe Tango: Save Network Node (Aeon)")
    TempRegionlist.append("Mainframe Tango: Save 80% civilian buildings (optional) (Aeon)")
    TempRegionlist.append("Mainframe Tango: Survive attacks (Aeon)")
    TempRegionlist.append("Mainframe Tango: Capture northeast node (Aeon)")
    TempRegionlist.append("Mainframe Tango: Capture northwest node (Aeon)")
    TempRegionlist.append("Mainframe Tango: Do not attack main Aeon base (Aeon)")
    TempRegionlist.append("Mainframe Tango: Kill Aeon Commander (Aeon)")
    TotalListOfTtotallyLevels["Mainframe Tango (Aeon)"] = TempRegionlist
    TempRegionlist = []
    TempRegionlist.append("Unlock: Destroy UEF generators (Aeon)")
    TempRegionlist.append("Unlock: Destroy UEF shipyards (optional) (Aeon)")
    TempRegionlist.append("Unlock: Destroy UEF radars (Aeon)")
    TempRegionlist.append("Unlock: Go to Hex5 (Aeon)")
    TempRegionlist.append("Unlock: Defend from heavy gunships (Aeon)")
    TempRegionlist.append("Unlock: Infect UEF landing pad (optional) (Aeon)")
    TempRegionlist.append("Unlock: This will be retconned later (Aeon)")
    TempRegionlist.append("Unlock: Kill UEF Commander (Aeon)")
    TotalListOfTtotallyLevels["Unlock (Aeon)"] = TempRegionlist
    TempRegionlist = []
    TempRegionlist.append("Freedom: Destroy CZAR (Aeon)")
    TempRegionlist.append("Freedom: Build Quantum Gate (Aeon)")
    TempRegionlist.append("Freedom: Download Quantum Virus (Aeon)")
    TempRegionlist.append("Freedom: Capture Black Sun control center (Aeon)")
    TempRegionlist.append("Freedom: Capture Black Sun (Aeon)")
    TempRegionlist.append("Freedom: Shoot Black Sun (Aeon)")
    TotalListOfTtotallyLevels["Freedom (Aeon)"] = TempRegionlist
    TempRegionlist = []
    TempRegionlist.append("Liberation: Build mass (Sera)")
    TempRegionlist.append("Liberation: Build power (Sera)")
    TempRegionlist.append("Liberation: Build air factory (Sera)")
    TempRegionlist.append("Liberation: Build bombers (Sera)")
    TempRegionlist.append("Liberation: Destroy radar defenders (Sera)")
    TempRegionlist.append("Liberation: Capture radars (Sera)")
    TempRegionlist.append("Liberation: Destroy mex (Sera)")
    TempRegionlist.append("Liberation: Destroy UEF defences (Sera)")
    TempRegionlist.append("Liberation: Destroy UEF patrols (Sera)")
    TempRegionlist.append("Liberation: Destroy UEF base defenders (Sera)")
    TempRegionlist.append("Liberation: Destroy UEF base (Sera)")
    TempRegionlist.append("Liberation: Kill Aeon Commander (Sera)")
    TotalListOfTtotallyLevels["Liberation (Sera)"] = TempRegionlist
    TempRegionlist = []
    TempRegionlist.append("Artifact: Destroy first village defenders (Sera)")
    TempRegionlist.append("Artifact: Destroy first temple (Sera)")
    TempRegionlist.append("Artifact: Protect first artifact (Sera)")
    TempRegionlist.append("Artifact: Find second artifact (Sera)")
    TempRegionlist.append("Artifact: Destroy Aeon reinforcements (Sera)")
    TempRegionlist.append("Artifact: Protect second artifact (Sera)")
    TempRegionlist.append("Artifact: Defend from Aeon attack (Sera)")
    TempRegionlist.append("Artifact: Destroy eastern base (Sera)")
    TempRegionlist.append("Artifact: Destroy navy base (Sera)")
    TempRegionlist.append("Artifact: Protect third artifact (Sera)")
    TempRegionlist.append("Artifact: Kill Aeon Commander (optional) (Sera)")
    TempRegionlist.append("Artifact: Kill Mach (Sera)")
    TempRegionlist.append("Artifact: Go to Gate (Sera)")
    TotalListOfTtotallyLevels["Artifact (Sera)"] = TempRegionlist
    TempRegionlist = []
    TempRegionlist.append("Defrag: Protect York 18 (Sera)")
    TempRegionlist.append("Defrag: Destroy western UEF base (Sera)")
    TempRegionlist.append("Defrag: Destroy north-western UEF base (Sera)")
    TempRegionlist.append("Defrag: Destroy northern UEF base (Sera)")
    TempRegionlist.append("Defrag: Sink UEF cruiser (Sera)")
    TempRegionlist.append("Defrag: Destroy static artillery (Sera)")
    TempRegionlist.append("Defrag: Escort trucks (Sera)")
    TempRegionlist.append("Defrag: Escort ALL trucks (optional) (Sera)")
    TempRegionlist.append("Defrag: Optional objective  (optional) (Sera)")
    TempRegionlist.append("Defrag: Kill UEF Commander (Sera)")
    TotalListOfTtotallyLevels["Defrag (Sera)"] = TempRegionlist
    TempRegionlist = []
    TempRegionlist.append("Mainframe Tango: Defeat Aeon Commander (Sera)")
    TempRegionlist.append("Mainframe Tango: Capture Network Node (Sera)")
    TempRegionlist.append("Mainframe Tango: Save Network Node (Sera)")
    TempRegionlist.append("Mainframe Tango: Save 80% civilian buildings (optional) (Sera)")
    TempRegionlist.append("Mainframe Tango: Survive attacks (Sera)")
    TempRegionlist.append("Mainframe Tango: Capture northeast node (Sera)")
    TempRegionlist.append("Mainframe Tango: Capture northwest node (Sera)")
    TempRegionlist.append("Mainframe Tango: Do not attack main Aeon base (Sera)")
    TempRegionlist.append("Mainframe Tango: Kill Aeon Commander (Sera)")
    TotalListOfTtotallyLevels["Mainframe Tango (Sera)"] = TempRegionlist
    TempRegionlist = []
    TempRegionlist.append("Unlock: Destroy UEF generators (Sera)")
    TempRegionlist.append("Unlock: Destroy UEF shipyards (optional) (Sera)")
    TempRegionlist.append("Unlock: Destroy UEF radars (Sera)")
    TempRegionlist.append("Unlock: Go to Hex5 (Sera)")
    TempRegionlist.append("Unlock: Defend from heavy gunships (Sera)")
    TempRegionlist.append("Unlock: Infect UEF landing pad (optional) (Sera)")
    TempRegionlist.append("Unlock: This will be retconned later (Sera)")
    TempRegionlist.append("Unlock: Kill UEF Commander (Sera)")
    TotalListOfTtotallyLevels["Unlock (Sera)"] = TempRegionlist
    TempRegionlist = []
    TempRegionlist.append("Freedom: Destroy CZAR (Sera)")
    TempRegionlist.append("Freedom: Build Quantum Gate (Sera)")
    TempRegionlist.append("Freedom: Download Quantum Virus (Sera)")
    TempRegionlist.append("Freedom: Capture Black Sun control center (Sera)")
    TempRegionlist.append("Freedom: Capture Black Sun (Sera)")
    TempRegionlist.append("Freedom: Shoot Black Sun (Sera)")
    TotalListOfTtotallyLevels["Freedom (Sera)"] = TempRegionlist

    TheCompleteListOfRulesForEverySingleRegion = {}
    rule = Has("Scorcher")
    TheCompleteListOfRulesForEverySingleRegion["Liberation: Build bombers (UEF)"] = rule
    rule = Has("Scorcher")
    TheCompleteListOfRulesForEverySingleRegion["Liberation: Destroy radar defenders (UEF)"] = rule
    rule = Has("Scorcher")
    TheCompleteListOfRulesForEverySingleRegion["Liberation: Capture radars (UEF)"] = rule
    rule = (Has("Scorcher")) & (Has("Cyclone") | Has("Archer") | Has("DA1 Railgun"))
    TheCompleteListOfRulesForEverySingleRegion["Liberation: Destroy mex (UEF)"] = rule
    rule = (Has("Scorcher")) & (Has("Cyclone") | Has("Archer") | Has("DA1 Railgun"))
    TheCompleteListOfRulesForEverySingleRegion["Liberation: Destroy UEF defences (UEF)"] = rule
    rule = (Has("Scorcher")) & (Has("Cyclone") | Has("Archer") | Has("DA1 Railgun"))
    TheCompleteListOfRulesForEverySingleRegion["Liberation: Destroy UEF patrols (UEF)"] = rule
    rule = (Has("Scorcher")) & (Has("Cyclone") | Has("Archer") | Has("DA1 Railgun"))
    TheCompleteListOfRulesForEverySingleRegion["Liberation: Destroy UEF base defenders (UEF)"] = rule
    rule = (Has("Scorcher")) & (Has("Cyclone") | Has("Archer") | Has("DA1 Railgun"))
    TheCompleteListOfRulesForEverySingleRegion["Liberation: Destroy UEF base (UEF)"] = rule
    rule = (Has("Scorcher")) & (Has("Cyclone") | Has("Archer") | Has("DA1 Railgun"))
    TheCompleteListOfRulesForEverySingleRegion["Liberation: Kill Aeon Commander (UEF)"] = rule
    rule = (Has("Scorcher")) & (Has("Cyclone") | Has("Archer") | Has("DA1 Railgun"))
    TheCompleteListOfRulesForEverySingleRegion["Artifact: Destroy first village defenders (UEF)"] = rule
    rule = (Has("Scorcher")) & (Has("Cyclone") | Has("Archer") | Has("DA1 Railgun"))
    TheCompleteListOfRulesForEverySingleRegion["Artifact: Destroy first temple (UEF)"] = rule
    rule = (Has("Scorcher")) & (Has("Cyclone") | Has("Archer") | Has("DA1 Railgun"))
    TheCompleteListOfRulesForEverySingleRegion["Artifact: Protect first artifact (UEF)"] = rule
    rule = ((Has("Scorcher")) & (Has("Cyclone") | Has("Archer") | Has("DA1 Railgun"))) & (Has("MA12 Striker"))
    TheCompleteListOfRulesForEverySingleRegion["Artifact: Find second artifact (UEF)"] = rule
    rule = (((Has("Scorcher")) & (Has("Cyclone") | Has("Archer") | Has("DA1 Railgun"))) & (Has("MA12 Striker"))) & (Has("Mongoose") | Has("Pillar") | Has("Riptide") | Has("Sparky") | Has("Triad"))
    TheCompleteListOfRulesForEverySingleRegion["Artifact: Destroy Aeon reinforcements (UEF)"] = rule
    rule = ((((Has("Scorcher")) & (Has("Cyclone") | Has("Archer") | Has("DA1 Railgun"))) & (Has("MA12 Striker"))) & (Has("Mongoose") | Has("Pillar") | Has("Riptide") | Has("Sparky") | Has("Triad"))) & (Has("Triad") | Has("Tigershark") | Has("Thunderhead Class") | Has("Stork") | Has("DN1"))
    TheCompleteListOfRulesForEverySingleRegion["Artifact: Protect second artifact (UEF)"] = rule
    rule = ((((Has("Scorcher")) & (Has("Cyclone") | Has("Archer") | Has("DA1 Railgun"))) & (Has("MA12 Striker"))) & (Has("Mongoose") | Has("Pillar") | Has("Riptide") | Has("Sparky") | Has("Triad"))) & (Has("Triad") | Has("Tigershark") | Has("Thunderhead Class") | Has("Stork") | Has("DN1"))
    TheCompleteListOfRulesForEverySingleRegion["Artifact: Defend from Aeon attack (UEF)"] = rule
    rule = ((((Has("Scorcher")) & (Has("Cyclone") | Has("Archer") | Has("DA1 Railgun"))) & (Has("MA12 Striker"))) & (Has("Mongoose") | Has("Pillar") | Has("Riptide") | Has("Sparky") | Has("Triad"))) & (Has("Triad") | Has("Tigershark") | Has("Thunderhead Class") | Has("Stork") | Has("DN1"))
    TheCompleteListOfRulesForEverySingleRegion["Artifact: Destroy eastern base (UEF)"] = rule
    rule = (((((Has("Scorcher")) & (Has("Cyclone") | Has("Archer") | Has("DA1 Railgun"))) & (Has("MA12 Striker"))) & (Has("Mongoose") | Has("Pillar") | Has("Riptide") | Has("Sparky") | Has("Triad"))) & (Has("Triad") | Has("Tigershark") | Has("Thunderhead Class") | Has("Stork") | Has("DN1"))) & (Has("Valiant Class") | Has("Governor Class") | Has("Stinger") | Has("C-6 Courier") | Has("Klink Hammer") | Has("Aloha"))
    TheCompleteListOfRulesForEverySingleRegion["Artifact: Destroy navy base (UEF)"] = rule
    rule = (((((Has("Scorcher")) & (Has("Cyclone") | Has("Archer") | Has("DA1 Railgun"))) & (Has("MA12 Striker"))) & (Has("Mongoose") | Has("Pillar") | Has("Riptide") | Has("Sparky") | Has("Triad"))) & (Has("Triad") | Has("Tigershark") | Has("Thunderhead Class") | Has("Stork") | Has("DN1"))) & (Has("Valiant Class") | Has("Governor Class") | Has("Stinger") | Has("C-6 Courier") | Has("Klink Hammer") | Has("Aloha"))
    TheCompleteListOfRulesForEverySingleRegion["Artifact: Protect third artifact (UEF)"] = rule
    rule = (((((Has("Scorcher")) & (Has("Cyclone") | Has("Archer") | Has("DA1 Railgun"))) & (Has("MA12 Striker"))) & (Has("Mongoose") | Has("Pillar") | Has("Riptide") | Has("Sparky") | Has("Triad"))) & (Has("Triad") | Has("Tigershark") | Has("Thunderhead Class") | Has("Stork") | Has("DN1"))) & (Has("Valiant Class") | Has("Governor Class") | Has("Stinger") | Has("C-6 Courier") | Has("Klink Hammer") | Has("Aloha"))
    TheCompleteListOfRulesForEverySingleRegion["Artifact: Kill Aeon Commander (optional) (UEF)"] = rule
    rule = (((((Has("Scorcher")) & (Has("Cyclone") | Has("Archer") | Has("DA1 Railgun"))) & (Has("MA12 Striker"))) & (Has("Mongoose") | Has("Pillar") | Has("Riptide") | Has("Sparky") | Has("Triad"))) & (Has("Triad") | Has("Tigershark") | Has("Thunderhead Class") | Has("Stork") | Has("DN1"))) & (Has("Valiant Class") | Has("Governor Class") | Has("Stinger") | Has("C-6 Courier") | Has("Klink Hammer") | Has("Aloha"))
    TheCompleteListOfRulesForEverySingleRegion["Artifact: Kill Mach (UEF)"] = rule
    rule = (((((Has("Scorcher")) & (Has("Cyclone") | Has("Archer") | Has("DA1 Railgun"))) & (Has("MA12 Striker"))) & (Has("Mongoose") | Has("Pillar") | Has("Riptide") | Has("Sparky") | Has("Triad"))) & (Has("Triad") | Has("Tigershark") | Has("Thunderhead Class") | Has("Stork") | Has("DN1"))) & (Has("Valiant Class") | Has("Governor Class") | Has("Stinger") | Has("C-6 Courier") | Has("Klink Hammer") | Has("Aloha"))
    TheCompleteListOfRulesForEverySingleRegion["Artifact: Go to Gate (UEF)"] = rule
    rule = ((((((Has("Scorcher")) & (Has("Cyclone") | Has("Archer") | Has("DA1 Railgun"))) & (Has("MA12 Striker"))) & (Has("Mongoose") | Has("Pillar") | Has("Riptide") | Has("Sparky") | Has("Triad"))) & (Has("Triad") | Has("Tigershark") | Has("Thunderhead Class") | Has("Stork") | Has("DN1"))) & (Has("Valiant Class") | Has("Governor Class") | Has("Stinger") | Has("C-6 Courier") | Has("Klink Hammer") | Has("Aloha"))) & (Has("UEF T2 Mass Extractor") & Has("EG - 200 Fusion Reactor"))
    TheCompleteListOfRulesForEverySingleRegion["Defrag: Protect York 18 (UEF)"] = rule
    rule = ((((((Has("Scorcher")) & (Has("Cyclone") | Has("Archer") | Has("DA1 Railgun"))) & (Has("MA12 Striker"))) & (Has("Mongoose") | Has("Pillar") | Has("Riptide") | Has("Sparky") | Has("Triad"))) & (Has("Triad") | Has("Tigershark") | Has("Thunderhead Class") | Has("Stork") | Has("DN1"))) & (Has("Valiant Class") | Has("Governor Class") | Has("Stinger") | Has("C-6 Courier") | Has("Klink Hammer") | Has("Aloha"))) & (Has("UEF T2 Mass Extractor") & Has("EG - 200 Fusion Reactor"))
    TheCompleteListOfRulesForEverySingleRegion["Defrag: Destroy western UEF base (UEF)"] = rule
    rule = ((((((Has("Scorcher")) & (Has("Cyclone") | Has("Archer") | Has("DA1 Railgun"))) & (Has("MA12 Striker"))) & (Has("Mongoose") | Has("Pillar") | Has("Riptide") | Has("Sparky") | Has("Triad"))) & (Has("Triad") | Has("Tigershark") | Has("Thunderhead Class") | Has("Stork") | Has("DN1"))) & (Has("Valiant Class") | Has("Governor Class") | Has("Stinger") | Has("C-6 Courier") | Has("Klink Hammer") | Has("Aloha"))) & (Has("UEF T2 Mass Extractor") & Has("EG - 200 Fusion Reactor"))
    TheCompleteListOfRulesForEverySingleRegion["Defrag: Destroy north-western UEF base (UEF)"] = rule
    rule = ((((((Has("Scorcher")) & (Has("Cyclone") | Has("Archer") | Has("DA1 Railgun"))) & (Has("MA12 Striker"))) & (Has("Mongoose") | Has("Pillar") | Has("Riptide") | Has("Sparky") | Has("Triad"))) & (Has("Triad") | Has("Tigershark") | Has("Thunderhead Class") | Has("Stork") | Has("DN1"))) & (Has("Valiant Class") | Has("Governor Class") | Has("Stinger") | Has("C-6 Courier") | Has("Klink Hammer") | Has("Aloha"))) & (Has("UEF T2 Mass Extractor") & Has("EG - 200 Fusion Reactor"))
    TheCompleteListOfRulesForEverySingleRegion["Defrag: Destroy northern UEF base (UEF)"] = rule
    rule = ((((((Has("Scorcher")) & (Has("Cyclone") | Has("Archer") | Has("DA1 Railgun"))) & (Has("MA12 Striker"))) & (Has("Mongoose") | Has("Pillar") | Has("Riptide") | Has("Sparky") | Has("Triad"))) & (Has("Triad") | Has("Tigershark") | Has("Thunderhead Class") | Has("Stork") | Has("DN1"))) & (Has("Valiant Class") | Has("Governor Class") | Has("Stinger") | Has("C-6 Courier") | Has("Klink Hammer") | Has("Aloha"))) & (Has("UEF T2 Mass Extractor") & Has("EG - 200 Fusion Reactor"))
    TheCompleteListOfRulesForEverySingleRegion["Defrag: Sink UEF cruiser (UEF)"] = rule
    rule = (((((((Has("Scorcher")) & (Has("Cyclone") | Has("Archer") | Has("DA1 Railgun"))) & (Has("MA12 Striker"))) & (Has("Mongoose") | Has("Pillar") | Has("Riptide") | Has("Sparky") | Has("Triad"))) & (Has("Triad") | Has("Tigershark") | Has("Thunderhead Class") | Has("Stork") | Has("DN1"))) & (Has("Valiant Class") | Has("Governor Class") | Has("Stinger") | Has("C-6 Courier") | Has("Klink Hammer") | Has("Aloha"))) & (Has("UEF T2 Mass Extractor") & Has("EG - 200 Fusion Reactor"))) & (Has("Air Cleaner") | Has("Sky Boxer"))
    TheCompleteListOfRulesForEverySingleRegion["Defrag: Destroy static artillery (UEF)"] = rule
    rule = (((((((Has("Scorcher")) & (Has("Cyclone") | Has("Archer") | Has("DA1 Railgun"))) & (Has("MA12 Striker"))) & (Has("Mongoose") | Has("Pillar") | Has("Riptide") | Has("Sparky") | Has("Triad"))) & (Has("Triad") | Has("Tigershark") | Has("Thunderhead Class") | Has("Stork") | Has("DN1"))) & (Has("Valiant Class") | Has("Governor Class") | Has("Stinger") | Has("C-6 Courier") | Has("Klink Hammer") | Has("Aloha"))) & (Has("UEF T2 Mass Extractor") & Has("EG - 200 Fusion Reactor"))) & (Has("Air Cleaner") | Has("Sky Boxer"))
    TheCompleteListOfRulesForEverySingleRegion["Defrag: Escort trucks (UEF)"] = rule
    rule = (((((((Has("Scorcher")) & (Has("Cyclone") | Has("Archer") | Has("DA1 Railgun"))) & (Has("MA12 Striker"))) & (Has("Mongoose") | Has("Pillar") | Has("Riptide") | Has("Sparky") | Has("Triad"))) & (Has("Triad") | Has("Tigershark") | Has("Thunderhead Class") | Has("Stork") | Has("DN1"))) & (Has("Valiant Class") | Has("Governor Class") | Has("Stinger") | Has("C-6 Courier") | Has("Klink Hammer") | Has("Aloha"))) & (Has("UEF T2 Mass Extractor") & Has("EG - 200 Fusion Reactor"))) & (Has("Air Cleaner") | Has("Sky Boxer"))
    TheCompleteListOfRulesForEverySingleRegion["Defrag: Escort ALL trucks (optional) (UEF)"] = rule
    rule = (((((((Has("Scorcher")) & (Has("Cyclone") | Has("Archer") | Has("DA1 Railgun"))) & (Has("MA12 Striker"))) & (Has("Mongoose") | Has("Pillar") | Has("Riptide") | Has("Sparky") | Has("Triad"))) & (Has("Triad") | Has("Tigershark") | Has("Thunderhead Class") | Has("Stork") | Has("DN1"))) & (Has("Valiant Class") | Has("Governor Class") | Has("Stinger") | Has("C-6 Courier") | Has("Klink Hammer") | Has("Aloha"))) & (Has("UEF T2 Mass Extractor") & Has("EG - 200 Fusion Reactor"))) & (Has("Air Cleaner") | Has("Sky Boxer"))
    TheCompleteListOfRulesForEverySingleRegion["Defrag: Optional objective  (optional) (UEF)"] = rule
    rule = (((((((Has("Scorcher")) & (Has("Cyclone") | Has("Archer") | Has("DA1 Railgun"))) & (Has("MA12 Striker"))) & (Has("Mongoose") | Has("Pillar") | Has("Riptide") | Has("Sparky") | Has("Triad"))) & (Has("Triad") | Has("Tigershark") | Has("Thunderhead Class") | Has("Stork") | Has("DN1"))) & (Has("Valiant Class") | Has("Governor Class") | Has("Stinger") | Has("C-6 Courier") | Has("Klink Hammer") | Has("Aloha"))) & (Has("UEF T2 Mass Extractor") & Has("EG - 200 Fusion Reactor"))) & (Has("Air Cleaner") | Has("Sky Boxer"))
    TheCompleteListOfRulesForEverySingleRegion["Defrag: Kill UEF Commander (UEF)"] = rule
    rule = ((((((((Has("Scorcher")) & (Has("Cyclone") | Has("Archer") | Has("DA1 Railgun"))) & (Has("MA12 Striker"))) & (Has("Mongoose") | Has("Pillar") | Has("Riptide") | Has("Sparky") | Has("Triad"))) & (Has("Triad") | Has("Tigershark") | Has("Thunderhead Class") | Has("Stork") | Has("DN1"))) & (Has("Valiant Class") | Has("Governor Class") | Has("Stinger") | Has("C-6 Courier") | Has("Klink Hammer") | Has("Aloha"))) & (Has("UEF T2 Mass Extractor") & Has("EG - 200 Fusion Reactor"))) & (Has("Air Cleaner") | Has("Sky Boxer"))) & (Has("Valiant Class") | Has("Governor Class"))
    TheCompleteListOfRulesForEverySingleRegion["Mainframe Tango: Defeat Aeon Commander (UEF)"] = rule
    rule = ((((((((Has("Scorcher")) & (Has("Cyclone") | Has("Archer") | Has("DA1 Railgun"))) & (Has("MA12 Striker"))) & (Has("Mongoose") | Has("Pillar") | Has("Riptide") | Has("Sparky") | Has("Triad"))) & (Has("Triad") | Has("Tigershark") | Has("Thunderhead Class") | Has("Stork") | Has("DN1"))) & (Has("Valiant Class") | Has("Governor Class") | Has("Stinger") | Has("C-6 Courier") | Has("Klink Hammer") | Has("Aloha"))) & (Has("UEF T2 Mass Extractor") & Has("EG - 200 Fusion Reactor"))) & (Has("Air Cleaner") | Has("Sky Boxer"))) & (Has("Valiant Class") | Has("Governor Class"))
    TheCompleteListOfRulesForEverySingleRegion["Mainframe Tango: Capture Network Node (UEF)"] = rule
    rule = ((((((((Has("Scorcher")) & (Has("Cyclone") | Has("Archer") | Has("DA1 Railgun"))) & (Has("MA12 Striker"))) & (Has("Mongoose") | Has("Pillar") | Has("Riptide") | Has("Sparky") | Has("Triad"))) & (Has("Triad") | Has("Tigershark") | Has("Thunderhead Class") | Has("Stork") | Has("DN1"))) & (Has("Valiant Class") | Has("Governor Class") | Has("Stinger") | Has("C-6 Courier") | Has("Klink Hammer") | Has("Aloha"))) & (Has("UEF T2 Mass Extractor") & Has("EG - 200 Fusion Reactor"))) & (Has("Air Cleaner") | Has("Sky Boxer"))) & (Has("Valiant Class") | Has("Governor Class"))
    TheCompleteListOfRulesForEverySingleRegion["Mainframe Tango: Save Network Node (UEF)"] = rule
    rule = ((((((((Has("Scorcher")) & (Has("Cyclone") | Has("Archer") | Has("DA1 Railgun"))) & (Has("MA12 Striker"))) & (Has("Mongoose") | Has("Pillar") | Has("Riptide") | Has("Sparky") | Has("Triad"))) & (Has("Triad") | Has("Tigershark") | Has("Thunderhead Class") | Has("Stork") | Has("DN1"))) & (Has("Valiant Class") | Has("Governor Class") | Has("Stinger") | Has("C-6 Courier") | Has("Klink Hammer") | Has("Aloha"))) & (Has("UEF T2 Mass Extractor") & Has("EG - 200 Fusion Reactor"))) & (Has("Air Cleaner") | Has("Sky Boxer"))) & (Has("Valiant Class") | Has("Governor Class"))
    TheCompleteListOfRulesForEverySingleRegion["Mainframe Tango: Save 80% civilian buildings (optional) (UEF)"] = rule
    rule = ((((((((Has("Scorcher")) & (Has("Cyclone") | Has("Archer") | Has("DA1 Railgun"))) & (Has("MA12 Striker"))) & (Has("Mongoose") | Has("Pillar") | Has("Riptide") | Has("Sparky") | Has("Triad"))) & (Has("Triad") | Has("Tigershark") | Has("Thunderhead Class") | Has("Stork") | Has("DN1"))) & (Has("Valiant Class") | Has("Governor Class") | Has("Stinger") | Has("C-6 Courier") | Has("Klink Hammer") | Has("Aloha"))) & (Has("UEF T2 Mass Extractor") & Has("EG - 200 Fusion Reactor"))) & (Has("Air Cleaner") | Has("Sky Boxer"))) & (Has("Valiant Class") | Has("Governor Class"))
    TheCompleteListOfRulesForEverySingleRegion["Mainframe Tango: Survive attacks (UEF)"] = rule
    rule = ((((((((Has("Scorcher")) & (Has("Cyclone") | Has("Archer") | Has("DA1 Railgun"))) & (Has("MA12 Striker"))) & (Has("Mongoose") | Has("Pillar") | Has("Riptide") | Has("Sparky") | Has("Triad"))) & (Has("Triad") | Has("Tigershark") | Has("Thunderhead Class") | Has("Stork") | Has("DN1"))) & (Has("Valiant Class") | Has("Governor Class") | Has("Stinger") | Has("C-6 Courier") | Has("Klink Hammer") | Has("Aloha"))) & (Has("UEF T2 Mass Extractor") & Has("EG - 200 Fusion Reactor"))) & (Has("Air Cleaner") | Has("Sky Boxer"))) & (Has("Valiant Class") | Has("Governor Class"))
    TheCompleteListOfRulesForEverySingleRegion["Mainframe Tango: Capture northeast node (UEF)"] = rule
    rule = ((((((((Has("Scorcher")) & (Has("Cyclone") | Has("Archer") | Has("DA1 Railgun"))) & (Has("MA12 Striker"))) & (Has("Mongoose") | Has("Pillar") | Has("Riptide") | Has("Sparky") | Has("Triad"))) & (Has("Triad") | Has("Tigershark") | Has("Thunderhead Class") | Has("Stork") | Has("DN1"))) & (Has("Valiant Class") | Has("Governor Class") | Has("Stinger") | Has("C-6 Courier") | Has("Klink Hammer") | Has("Aloha"))) & (Has("UEF T2 Mass Extractor") & Has("EG - 200 Fusion Reactor"))) & (Has("Air Cleaner") | Has("Sky Boxer"))) & (Has("Valiant Class") | Has("Governor Class"))
    TheCompleteListOfRulesForEverySingleRegion["Mainframe Tango: Capture northwest node (UEF)"] = rule
    rule = ((((((((Has("Scorcher")) & (Has("Cyclone") | Has("Archer") | Has("DA1 Railgun"))) & (Has("MA12 Striker"))) & (Has("Mongoose") | Has("Pillar") | Has("Riptide") | Has("Sparky") | Has("Triad"))) & (Has("Triad") | Has("Tigershark") | Has("Thunderhead Class") | Has("Stork") | Has("DN1"))) & (Has("Valiant Class") | Has("Governor Class") | Has("Stinger") | Has("C-6 Courier") | Has("Klink Hammer") | Has("Aloha"))) & (Has("UEF T2 Mass Extractor") & Has("EG - 200 Fusion Reactor"))) & (Has("Air Cleaner") | Has("Sky Boxer"))) & (Has("Valiant Class") | Has("Governor Class"))
    TheCompleteListOfRulesForEverySingleRegion["Mainframe Tango: Do not attack main Aeon base (UEF)"] = rule
    rule = ((((((((Has("Scorcher")) & (Has("Cyclone") | Has("Archer") | Has("DA1 Railgun"))) & (Has("MA12 Striker"))) & (Has("Mongoose") | Has("Pillar") | Has("Riptide") | Has("Sparky") | Has("Triad"))) & (Has("Triad") | Has("Tigershark") | Has("Thunderhead Class") | Has("Stork") | Has("DN1"))) & (Has("Valiant Class") | Has("Governor Class") | Has("Stinger") | Has("C-6 Courier") | Has("Klink Hammer") | Has("Aloha"))) & (Has("UEF T2 Mass Extractor") & Has("EG - 200 Fusion Reactor"))) & (Has("Air Cleaner") | Has("Sky Boxer"))) & (Has("Valiant Class") | Has("Governor Class"))
    TheCompleteListOfRulesForEverySingleRegion["Mainframe Tango: Kill Aeon Commander (UEF)"] = rule
    rule = (((((((((Has("Scorcher")) & (Has("Cyclone") | Has("Archer") | Has("DA1 Railgun"))) & (Has("MA12 Striker"))) & (Has("Mongoose") | Has("Pillar") | Has("Riptide") | Has("Sparky") | Has("Triad"))) & (Has("Triad") | Has("Tigershark") | Has("Thunderhead Class") | Has("Stork") | Has("DN1"))) & (Has("Valiant Class") | Has("Governor Class") | Has("Stinger") | Has("C-6 Courier") | Has("Klink Hammer") | Has("Aloha"))) & (Has("UEF T2 Mass Extractor") & Has("EG - 200 Fusion Reactor"))) & (Has("Air Cleaner") | Has("Sky Boxer"))) & (Has("Valiant Class") | Has("Governor Class"))) & (Has("UEF T3 Mass Extractor") & Has("EG 900 Fusion Reactor") & (Has("Titan") | Has("Persival") | Has("Spearhead") | Has("Continental") | Has("Janus") | Has("Mavor") | Has("Novax Center") | Has("Aloha") | Has("Duke") | Has("Stonager") | Has("Broadsword") | Has("Ambassador")))
    TheCompleteListOfRulesForEverySingleRegion["Unlock: Destroy UEF generators (UEF)"] = rule
    rule = ((((((((((Has("Scorcher")) & (Has("Cyclone") | Has("Archer") | Has("DA1 Railgun"))) & (Has("MA12 Striker"))) & (Has("Mongoose") | Has("Pillar") | Has("Riptide") | Has("Sparky") | Has("Triad"))) & (Has("Triad") | Has("Tigershark") | Has("Thunderhead Class") | Has("Stork") | Has("DN1"))) & (Has("Valiant Class") | Has("Governor Class") | Has("Stinger") | Has("C-6 Courier") | Has("Klink Hammer") | Has("Aloha"))) & (Has("UEF T2 Mass Extractor") & Has("EG - 200 Fusion Reactor"))) & (Has("Air Cleaner") | Has("Sky Boxer"))) & (Has("Valiant Class") | Has("Governor Class"))) & (Has("UEF T3 Mass Extractor") & Has("EG 900 Fusion Reactor") & (Has("Titan") | Has("Persival") | Has("Spearhead") | Has("Continental") | Has("Janus") | Has("Mavor") | Has("Novax Center") | Has("Aloha") | Has("Duke") | Has("Stonager") | Has("Broadsword") | Has("Ambassador")))) & (Has("Governor Class"))
    TheCompleteListOfRulesForEverySingleRegion["Unlock: Destroy UEF shipyards (optional) (UEF)"] = rule
    rule = ((((((((((Has("Scorcher")) & (Has("Cyclone") | Has("Archer") | Has("DA1 Railgun"))) & (Has("MA12 Striker"))) & (Has("Mongoose") | Has("Pillar") | Has("Riptide") | Has("Sparky") | Has("Triad"))) & (Has("Triad") | Has("Tigershark") | Has("Thunderhead Class") | Has("Stork") | Has("DN1"))) & (Has("Valiant Class") | Has("Governor Class") | Has("Stinger") | Has("C-6 Courier") | Has("Klink Hammer") | Has("Aloha"))) & (Has("UEF T2 Mass Extractor") & Has("EG - 200 Fusion Reactor"))) & (Has("Air Cleaner") | Has("Sky Boxer"))) & (Has("Valiant Class") | Has("Governor Class"))) & (Has("UEF T3 Mass Extractor") & Has("EG 900 Fusion Reactor") & (Has("Titan") | Has("Persival") | Has("Spearhead") | Has("Continental") | Has("Janus") | Has("Mavor") | Has("Novax Center") | Has("Aloha") | Has("Duke") | Has("Stonager") | Has("Broadsword") | Has("Ambassador")))) & (Has("Governor Class"))
    TheCompleteListOfRulesForEverySingleRegion["Unlock: Destroy UEF radars (UEF)"] = rule
    rule = (((((((((((Has("Scorcher")) & (Has("Cyclone") | Has("Archer") | Has("DA1 Railgun"))) & (Has("MA12 Striker"))) & (Has("Mongoose") | Has("Pillar") | Has("Riptide") | Has("Sparky") | Has("Triad"))) & (Has("Triad") | Has("Tigershark") | Has("Thunderhead Class") | Has("Stork") | Has("DN1"))) & (Has("Valiant Class") | Has("Governor Class") | Has("Stinger") | Has("C-6 Courier") | Has("Klink Hammer") | Has("Aloha"))) & (Has("UEF T2 Mass Extractor") & Has("EG - 200 Fusion Reactor"))) & (Has("Air Cleaner") | Has("Sky Boxer"))) & (Has("Valiant Class") | Has("Governor Class"))) & (Has("UEF T3 Mass Extractor") & Has("EG 900 Fusion Reactor") & (Has("Titan") | Has("Persival") | Has("Spearhead") | Has("Continental") | Has("Janus") | Has("Mavor") | Has("Novax Center") | Has("Aloha") | Has("Duke") | Has("Stonager") | Has("Broadsword") | Has("Ambassador")))) & (Has("Governor Class"))) & (Has("C14 Star Lifter"))
    TheCompleteListOfRulesForEverySingleRegion["Unlock: Go to Hex5 (UEF)"] = rule
    rule = ((((((((((((Has("Scorcher")) & (Has("Cyclone") | Has("Archer") | Has("DA1 Railgun"))) & (Has("MA12 Striker"))) & (Has("Mongoose") | Has("Pillar") | Has("Riptide") | Has("Sparky") | Has("Triad"))) & (Has("Triad") | Has("Tigershark") | Has("Thunderhead Class") | Has("Stork") | Has("DN1"))) & (Has("Valiant Class") | Has("Governor Class") | Has("Stinger") | Has("C-6 Courier") | Has("Klink Hammer") | Has("Aloha"))) & (Has("UEF T2 Mass Extractor") & Has("EG - 200 Fusion Reactor"))) & (Has("Air Cleaner") | Has("Sky Boxer"))) & (Has("Valiant Class") | Has("Governor Class"))) & (Has("UEF T3 Mass Extractor") & Has("EG 900 Fusion Reactor") & (Has("Titan") | Has("Persival") | Has("Spearhead") | Has("Continental") | Has("Janus") | Has("Mavor") | Has("Novax Center") | Has("Aloha") | Has("Duke") | Has("Stonager") | Has("Broadsword") | Has("Ambassador")))) & (Has("Governor Class"))) & (Has("C14 Star Lifter"))) & (Has("Wasp") | Has("Cougar") | Has("Flayer"))
    TheCompleteListOfRulesForEverySingleRegion["Unlock: Defend from heavy gunships (UEF)"] = rule
    rule = ((((((((((((Has("Scorcher")) & (Has("Cyclone") | Has("Archer") | Has("DA1 Railgun"))) & (Has("MA12 Striker"))) & (Has("Mongoose") | Has("Pillar") | Has("Riptide") | Has("Sparky") | Has("Triad"))) & (Has("Triad") | Has("Tigershark") | Has("Thunderhead Class") | Has("Stork") | Has("DN1"))) & (Has("Valiant Class") | Has("Governor Class") | Has("Stinger") | Has("C-6 Courier") | Has("Klink Hammer") | Has("Aloha"))) & (Has("UEF T2 Mass Extractor") & Has("EG - 200 Fusion Reactor"))) & (Has("Air Cleaner") | Has("Sky Boxer"))) & (Has("Valiant Class") | Has("Governor Class"))) & (Has("UEF T3 Mass Extractor") & Has("EG 900 Fusion Reactor") & (Has("Titan") | Has("Persival") | Has("Spearhead") | Has("Continental") | Has("Janus") | Has("Mavor") | Has("Novax Center") | Has("Aloha") | Has("Duke") | Has("Stonager") | Has("Broadsword") | Has("Ambassador")))) & (Has("Governor Class"))) & (Has("C14 Star Lifter"))) & (Has("Wasp") | Has("Cougar") | Has("Flayer"))
    TheCompleteListOfRulesForEverySingleRegion["Unlock: Infect UEF landing pad (optional) (UEF)"] = rule
    rule = ((((((((((((Has("Scorcher")) & (Has("Cyclone") | Has("Archer") | Has("DA1 Railgun"))) & (Has("MA12 Striker"))) & (Has("Mongoose") | Has("Pillar") | Has("Riptide") | Has("Sparky") | Has("Triad"))) & (Has("Triad") | Has("Tigershark") | Has("Thunderhead Class") | Has("Stork") | Has("DN1"))) & (Has("Valiant Class") | Has("Governor Class") | Has("Stinger") | Has("C-6 Courier") | Has("Klink Hammer") | Has("Aloha"))) & (Has("UEF T2 Mass Extractor") & Has("EG - 200 Fusion Reactor"))) & (Has("Air Cleaner") | Has("Sky Boxer"))) & (Has("Valiant Class") | Has("Governor Class"))) & (Has("UEF T3 Mass Extractor") & Has("EG 900 Fusion Reactor") & (Has("Titan") | Has("Persival") | Has("Spearhead") | Has("Continental") | Has("Janus") | Has("Mavor") | Has("Novax Center") | Has("Aloha") | Has("Duke") | Has("Stonager") | Has("Broadsword") | Has("Ambassador")))) & (Has("Governor Class"))) & (Has("C14 Star Lifter"))) & (Has("Wasp") | Has("Cougar") | Has("Flayer"))
    TheCompleteListOfRulesForEverySingleRegion["Unlock: This will be retconned later (UEF)"] = rule
    rule = ((((((((((((Has("Scorcher")) & (Has("Cyclone") | Has("Archer") | Has("DA1 Railgun"))) & (Has("MA12 Striker"))) & (Has("Mongoose") | Has("Pillar") | Has("Riptide") | Has("Sparky") | Has("Triad"))) & (Has("Triad") | Has("Tigershark") | Has("Thunderhead Class") | Has("Stork") | Has("DN1"))) & (Has("Valiant Class") | Has("Governor Class") | Has("Stinger") | Has("C-6 Courier") | Has("Klink Hammer") | Has("Aloha"))) & (Has("UEF T2 Mass Extractor") & Has("EG - 200 Fusion Reactor"))) & (Has("Air Cleaner") | Has("Sky Boxer"))) & (Has("Valiant Class") | Has("Governor Class"))) & (Has("UEF T3 Mass Extractor") & Has("EG 900 Fusion Reactor") & (Has("Titan") | Has("Persival") | Has("Spearhead") | Has("Continental") | Has("Janus") | Has("Mavor") | Has("Novax Center") | Has("Aloha") | Has("Duke") | Has("Stonager") | Has("Broadsword") | Has("Ambassador")))) & (Has("Governor Class"))) & (Has("C14 Star Lifter"))) & (Has("Wasp") | Has("Cougar") | Has("Flayer"))
    TheCompleteListOfRulesForEverySingleRegion["Unlock: Kill UEF Commander (UEF)"] = rule
    rule = ((((((((((((Has("Scorcher")) & (Has("Cyclone") | Has("Archer") | Has("DA1 Railgun"))) & (Has("MA12 Striker"))) & (Has("Mongoose") | Has("Pillar") | Has("Riptide") | Has("Sparky") | Has("Triad"))) & (Has("Triad") | Has("Tigershark") | Has("Thunderhead Class") | Has("Stork") | Has("DN1"))) & (Has("Valiant Class") | Has("Governor Class") | Has("Stinger") | Has("C-6 Courier") | Has("Klink Hammer") | Has("Aloha"))) & (Has("UEF T2 Mass Extractor") & Has("EG - 200 Fusion Reactor"))) & (Has("Air Cleaner") | Has("Sky Boxer"))) & (Has("Valiant Class") | Has("Governor Class"))) & (Has("UEF T3 Mass Extractor") & Has("EG 900 Fusion Reactor") & (Has("Titan") | Has("Persival") | Has("Spearhead") | Has("Continental") | Has("Janus") | Has("Mavor") | Has("Novax Center") | Has("Aloha") | Has("Duke") | Has("Stonager") | Has("Broadsword") | Has("Ambassador")))) & (Has("Governor Class"))) & (Has("C14 Star Lifter"))) & (Has("Wasp") | Has("Cougar") | Has("Flayer"))
    TheCompleteListOfRulesForEverySingleRegion["Freedom: Destroy CZAR (UEF)"] = rule
    rule = (((((((((((((Has("Scorcher")) & (Has("Cyclone") | Has("Archer") | Has("DA1 Railgun"))) & (Has("MA12 Striker"))) & (Has("Mongoose") | Has("Pillar") | Has("Riptide") | Has("Sparky") | Has("Triad"))) & (Has("Triad") | Has("Tigershark") | Has("Thunderhead Class") | Has("Stork") | Has("DN1"))) & (Has("Valiant Class") | Has("Governor Class") | Has("Stinger") | Has("C-6 Courier") | Has("Klink Hammer") | Has("Aloha"))) & (Has("UEF T2 Mass Extractor") & Has("EG - 200 Fusion Reactor"))) & (Has("Air Cleaner") | Has("Sky Boxer"))) & (Has("Valiant Class") | Has("Governor Class"))) & (Has("UEF T3 Mass Extractor") & Has("EG 900 Fusion Reactor") & (Has("Titan") | Has("Persival") | Has("Spearhead") | Has("Continental") | Has("Janus") | Has("Mavor") | Has("Novax Center") | Has("Aloha") | Has("Duke") | Has("Stonager") | Has("Broadsword") | Has("Ambassador")))) & (Has("Governor Class"))) & (Has("C14 Star Lifter"))) & (Has("Wasp") | Has("Cougar") | Has("Flayer"))) & (Has("QGW R-32"))
    TheCompleteListOfRulesForEverySingleRegion["Freedom: Build Quantum Gate (UEF)"] = rule
    rule = ((((((((((((((Has("Scorcher")) & (Has("Cyclone") | Has("Archer") | Has("DA1 Railgun"))) & (Has("MA12 Striker"))) & (Has("Mongoose") | Has("Pillar") | Has("Riptide") | Has("Sparky") | Has("Triad"))) & (Has("Triad") | Has("Tigershark") | Has("Thunderhead Class") | Has("Stork") | Has("DN1"))) & (Has("Valiant Class") | Has("Governor Class") | Has("Stinger") | Has("C-6 Courier") | Has("Klink Hammer") | Has("Aloha"))) & (Has("UEF T2 Mass Extractor") & Has("EG - 200 Fusion Reactor"))) & (Has("Air Cleaner") | Has("Sky Boxer"))) & (Has("Valiant Class") | Has("Governor Class"))) & (Has("UEF T3 Mass Extractor") & Has("EG 900 Fusion Reactor") & (Has("Titan") | Has("Persival") | Has("Spearhead") | Has("Continental") | Has("Janus") | Has("Mavor") | Has("Novax Center") | Has("Aloha") | Has("Duke") | Has("Stonager") | Has("Broadsword") | Has("Ambassador")))) & (Has("Governor Class"))) & (Has("C14 Star Lifter"))) & (Has("Wasp") | Has("Cougar") | Has("Flayer"))) & (Has("QGW R-32"))) & (Has("Titan") | Has("Persival") | Has("Spearhead") | Has("Continental") | Has("Janus") | Has("Broadsword") | Has("Ambassador") | Has("Fatboy"))
    TheCompleteListOfRulesForEverySingleRegion["Freedom: Download Quantum Virus (UEF)"] = rule
    rule = ((((((((((((((Has("Scorcher")) & (Has("Cyclone") | Has("Archer") | Has("DA1 Railgun"))) & (Has("MA12 Striker"))) & (Has("Mongoose") | Has("Pillar") | Has("Riptide") | Has("Sparky") | Has("Triad"))) & (Has("Triad") | Has("Tigershark") | Has("Thunderhead Class") | Has("Stork") | Has("DN1"))) & (Has("Valiant Class") | Has("Governor Class") | Has("Stinger") | Has("C-6 Courier") | Has("Klink Hammer") | Has("Aloha"))) & (Has("UEF T2 Mass Extractor") & Has("EG - 200 Fusion Reactor"))) & (Has("Air Cleaner") | Has("Sky Boxer"))) & (Has("Valiant Class") | Has("Governor Class"))) & (Has("UEF T3 Mass Extractor") & Has("EG 900 Fusion Reactor") & (Has("Titan") | Has("Persival") | Has("Spearhead") | Has("Continental") | Has("Janus") | Has("Mavor") | Has("Novax Center") | Has("Aloha") | Has("Duke") | Has("Stonager") | Has("Broadsword") | Has("Ambassador")))) & (Has("Governor Class"))) & (Has("C14 Star Lifter"))) & (Has("Wasp") | Has("Cougar") | Has("Flayer"))) & (Has("QGW R-32"))) & (Has("Titan") | Has("Persival") | Has("Spearhead") | Has("Continental") | Has("Janus") | Has("Broadsword") | Has("Ambassador") | Has("Fatboy"))
    TheCompleteListOfRulesForEverySingleRegion["Freedom: Capture Black Sun control center (UEF)"] = rule
    rule = ((((((((((((((Has("Scorcher")) & (Has("Cyclone") | Has("Archer") | Has("DA1 Railgun"))) & (Has("MA12 Striker"))) & (Has("Mongoose") | Has("Pillar") | Has("Riptide") | Has("Sparky") | Has("Triad"))) & (Has("Triad") | Has("Tigershark") | Has("Thunderhead Class") | Has("Stork") | Has("DN1"))) & (Has("Valiant Class") | Has("Governor Class") | Has("Stinger") | Has("C-6 Courier") | Has("Klink Hammer") | Has("Aloha"))) & (Has("UEF T2 Mass Extractor") & Has("EG - 200 Fusion Reactor"))) & (Has("Air Cleaner") | Has("Sky Boxer"))) & (Has("Valiant Class") | Has("Governor Class"))) & (Has("UEF T3 Mass Extractor") & Has("EG 900 Fusion Reactor") & (Has("Titan") | Has("Persival") | Has("Spearhead") | Has("Continental") | Has("Janus") | Has("Mavor") | Has("Novax Center") | Has("Aloha") | Has("Duke") | Has("Stonager") | Has("Broadsword") | Has("Ambassador")))) & (Has("Governor Class"))) & (Has("C14 Star Lifter"))) & (Has("Wasp") | Has("Cougar") | Has("Flayer"))) & (Has("QGW R-32"))) & (Has("Titan") | Has("Persival") | Has("Spearhead") | Has("Continental") | Has("Janus") | Has("Broadsword") | Has("Ambassador") | Has("Fatboy"))
    TheCompleteListOfRulesForEverySingleRegion["Freedom: Capture Black Sun (UEF)"] = rule
    rule = ((((((((((((((Has("Scorcher")) & (Has("Cyclone") | Has("Archer") | Has("DA1 Railgun"))) & (Has("MA12 Striker"))) & (Has("Mongoose") | Has("Pillar") | Has("Riptide") | Has("Sparky") | Has("Triad"))) & (Has("Triad") | Has("Tigershark") | Has("Thunderhead Class") | Has("Stork") | Has("DN1"))) & (Has("Valiant Class") | Has("Governor Class") | Has("Stinger") | Has("C-6 Courier") | Has("Klink Hammer") | Has("Aloha"))) & (Has("UEF T2 Mass Extractor") & Has("EG - 200 Fusion Reactor"))) & (Has("Air Cleaner") | Has("Sky Boxer"))) & (Has("Valiant Class") | Has("Governor Class"))) & (Has("UEF T3 Mass Extractor") & Has("EG 900 Fusion Reactor") & (Has("Titan") | Has("Persival") | Has("Spearhead") | Has("Continental") | Has("Janus") | Has("Mavor") | Has("Novax Center") | Has("Aloha") | Has("Duke") | Has("Stonager") | Has("Broadsword") | Has("Ambassador")))) & (Has("Governor Class"))) & (Has("C14 Star Lifter"))) & (Has("Wasp") | Has("Cougar") | Has("Flayer"))) & (Has("QGW R-32"))) & (Has("Titan") | Has("Persival") | Has("Spearhead") | Has("Continental") | Has("Janus") | Has("Broadsword") | Has("Ambassador") | Has("Fatboy"))
    TheCompleteListOfRulesForEverySingleRegion["Freedom: Shoot Black Sun (UEF)"] = rule
    rule = Has("Zeus")
    TheCompleteListOfRulesForEverySingleRegion["Liberation: Build bombers (Cybran)"] = rule
    rule = Has("Zeus")
    TheCompleteListOfRulesForEverySingleRegion["Liberation: Destroy radar defenders (Cybran)"] = rule
    rule = Has("Zeus")
    TheCompleteListOfRulesForEverySingleRegion["Liberation: Capture radars (Cybran)"] = rule
    rule = (Has("Zeus")) & (Has("Prowler") | Has("Sky Slammer") | Has("Tracer"))
    TheCompleteListOfRulesForEverySingleRegion["Liberation: Destroy mex (Cybran)"] = rule
    rule = (Has("Zeus")) & (Has("Prowler") | Has("Sky Slammer") | Has("Tracer"))
    TheCompleteListOfRulesForEverySingleRegion["Liberation: Destroy UEF defences (Cybran)"] = rule
    rule = (Has("Zeus")) & (Has("Prowler") | Has("Sky Slammer") | Has("Tracer"))
    TheCompleteListOfRulesForEverySingleRegion["Liberation: Destroy UEF patrols (Cybran)"] = rule
    rule = (Has("Zeus")) & (Has("Prowler") | Has("Sky Slammer") | Has("Tracer"))
    TheCompleteListOfRulesForEverySingleRegion["Liberation: Destroy UEF base defenders (Cybran)"] = rule
    rule = (Has("Zeus")) & (Has("Prowler") | Has("Sky Slammer") | Has("Tracer"))
    TheCompleteListOfRulesForEverySingleRegion["Liberation: Destroy UEF base (Cybran)"] = rule
    rule = (Has("Zeus")) & (Has("Prowler") | Has("Sky Slammer") | Has("Tracer"))
    TheCompleteListOfRulesForEverySingleRegion["Liberation: Kill Aeon Commander (Cybran)"] = rule
    rule = (Has("Zeus")) & (Has("Prowler") | Has("Sky Slammer") | Has("Tracer"))
    TheCompleteListOfRulesForEverySingleRegion["Artifact: Destroy first village defenders (Cybran)"] = rule
    rule = (Has("Zeus")) & (Has("Prowler") | Has("Sky Slammer") | Has("Tracer"))
    TheCompleteListOfRulesForEverySingleRegion["Artifact: Destroy first temple (Cybran)"] = rule
    rule = (Has("Zeus")) & (Has("Prowler") | Has("Sky Slammer") | Has("Tracer"))
    TheCompleteListOfRulesForEverySingleRegion["Artifact: Protect first artifact (Cybran)"] = rule
    rule = ((Has("Zeus")) & (Has("Prowler") | Has("Sky Slammer") | Has("Tracer"))) & (Has("Mantis"))
    TheCompleteListOfRulesForEverySingleRegion["Artifact: Find second artifact (Cybran)"] = rule
    rule = (((Has("Zeus")) & (Has("Prowler") | Has("Sky Slammer") | Has("Tracer"))) & (Has("Mantis"))) & (Has("Rhino") | Has("Cerberus") | Has("Wagner") | Has("Hoplite"))
    TheCompleteListOfRulesForEverySingleRegion["Artifact: Destroy Aeon reinforcements (Cybran)"] = rule
    rule = ((((Has("Zeus")) & (Has("Prowler") | Has("Sky Slammer") | Has("Tracer"))) & (Has("Mantis"))) & (Has("Rhino") | Has("Cerberus") | Has("Wagner") | Has("Hoplite"))) & (Has("Cerberus") | Has("Sliver") | Has("Trident Class") | Has("Cormorant") | Has("Scuttle"))
    TheCompleteListOfRulesForEverySingleRegion["Artifact: Protect second artifact (Cybran)"] = rule
    rule = ((((Has("Zeus")) & (Has("Prowler") | Has("Sky Slammer") | Has("Tracer"))) & (Has("Mantis"))) & (Has("Rhino") | Has("Cerberus") | Has("Wagner") | Has("Hoplite"))) & (Has("Cerberus") | Has("Sliver") | Has("Trident Class") | Has("Cormorant") | Has("Scuttle"))
    TheCompleteListOfRulesForEverySingleRegion["Artifact: Defend from Aeon attack (Cybran)"] = rule
    rule = ((((Has("Zeus")) & (Has("Prowler") | Has("Sky Slammer") | Has("Tracer"))) & (Has("Mantis"))) & (Has("Rhino") | Has("Cerberus") | Has("Wagner") | Has("Hoplite"))) & (Has("Cerberus") | Has("Sliver") | Has("Trident Class") | Has("Cormorant") | Has("Scuttle"))
    TheCompleteListOfRulesForEverySingleRegion["Artifact: Destroy eastern base (Cybran)"] = rule
    rule = (((((Has("Zeus")) & (Has("Prowler") | Has("Sky Slammer") | Has("Tracer"))) & (Has("Mantis"))) & (Has("Rhino") | Has("Cerberus") | Has("Wagner") | Has("Hoplite"))) & (Has("Cerberus") | Has("Sliver") | Has("Trident Class") | Has("Cormorant") | Has("Scuttle"))) & (Has("Salem Class") | Has("Renegade") | Has("Sky Hook") | Has("Gunther") | Has("TML-4"))
    TheCompleteListOfRulesForEverySingleRegion["Artifact: Destroy navy base (Cybran)"] = rule
    rule = (((((Has("Zeus")) & (Has("Prowler") | Has("Sky Slammer") | Has("Tracer"))) & (Has("Mantis"))) & (Has("Rhino") | Has("Cerberus") | Has("Wagner") | Has("Hoplite"))) & (Has("Cerberus") | Has("Sliver") | Has("Trident Class") | Has("Cormorant") | Has("Scuttle"))) & (Has("Salem Class") | Has("Renegade") | Has("Sky Hook") | Has("Gunther") | Has("TML-4"))
    TheCompleteListOfRulesForEverySingleRegion["Artifact: Protect third artifact (Cybran)"] = rule
    rule = (((((Has("Zeus")) & (Has("Prowler") | Has("Sky Slammer") | Has("Tracer"))) & (Has("Mantis"))) & (Has("Rhino") | Has("Cerberus") | Has("Wagner") | Has("Hoplite"))) & (Has("Cerberus") | Has("Sliver") | Has("Trident Class") | Has("Cormorant") | Has("Scuttle"))) & (Has("Salem Class") | Has("Renegade") | Has("Sky Hook") | Has("Gunther") | Has("TML-4"))
    TheCompleteListOfRulesForEverySingleRegion["Artifact: Kill Aeon Commander (optional) (Cybran)"] = rule
    rule = (((((Has("Zeus")) & (Has("Prowler") | Has("Sky Slammer") | Has("Tracer"))) & (Has("Mantis"))) & (Has("Rhino") | Has("Cerberus") | Has("Wagner") | Has("Hoplite"))) & (Has("Cerberus") | Has("Sliver") | Has("Trident Class") | Has("Cormorant") | Has("Scuttle"))) & (Has("Salem Class") | Has("Renegade") | Has("Sky Hook") | Has("Gunther") | Has("TML-4"))
    TheCompleteListOfRulesForEverySingleRegion["Artifact: Kill Mach (Cybran)"] = rule
    rule = (((((Has("Zeus")) & (Has("Prowler") | Has("Sky Slammer") | Has("Tracer"))) & (Has("Mantis"))) & (Has("Rhino") | Has("Cerberus") | Has("Wagner") | Has("Hoplite"))) & (Has("Cerberus") | Has("Sliver") | Has("Trident Class") | Has("Cormorant") | Has("Scuttle"))) & (Has("Salem Class") | Has("Renegade") | Has("Sky Hook") | Has("Gunther") | Has("TML-4"))
    TheCompleteListOfRulesForEverySingleRegion["Artifact: Go to Gate (Cybran)"] = rule
    rule = ((((((Has("Zeus")) & (Has("Prowler") | Has("Sky Slammer") | Has("Tracer"))) & (Has("Mantis"))) & (Has("Rhino") | Has("Cerberus") | Has("Wagner") | Has("Hoplite"))) & (Has("Cerberus") | Has("Sliver") | Has("Trident Class") | Has("Cormorant") | Has("Scuttle"))) & (Has("Salem Class") | Has("Renegade") | Has("Sky Hook") | Has("Gunther") | Has("TML-4"))) & (Has("Cybran T2 Mass Extractor") & Has("Cybran T2 Generator"))
    TheCompleteListOfRulesForEverySingleRegion["Defrag: Protect York 18 (Cybran)"] = rule
    rule = ((((((Has("Zeus")) & (Has("Prowler") | Has("Sky Slammer") | Has("Tracer"))) & (Has("Mantis"))) & (Has("Rhino") | Has("Cerberus") | Has("Wagner") | Has("Hoplite"))) & (Has("Cerberus") | Has("Sliver") | Has("Trident Class") | Has("Cormorant") | Has("Scuttle"))) & (Has("Salem Class") | Has("Renegade") | Has("Sky Hook") | Has("Gunther") | Has("TML-4"))) & (Has("Cybran T2 Mass Extractor") & Has("Cybran T2 Generator"))
    TheCompleteListOfRulesForEverySingleRegion["Defrag: Destroy western UEF base (Cybran)"] = rule
    rule = ((((((Has("Zeus")) & (Has("Prowler") | Has("Sky Slammer") | Has("Tracer"))) & (Has("Mantis"))) & (Has("Rhino") | Has("Cerberus") | Has("Wagner") | Has("Hoplite"))) & (Has("Cerberus") | Has("Sliver") | Has("Trident Class") | Has("Cormorant") | Has("Scuttle"))) & (Has("Salem Class") | Has("Renegade") | Has("Sky Hook") | Has("Gunther") | Has("TML-4"))) & (Has("Cybran T2 Mass Extractor") & Has("Cybran T2 Generator"))
    TheCompleteListOfRulesForEverySingleRegion["Defrag: Destroy north-western UEF base (Cybran)"] = rule
    rule = ((((((Has("Zeus")) & (Has("Prowler") | Has("Sky Slammer") | Has("Tracer"))) & (Has("Mantis"))) & (Has("Rhino") | Has("Cerberus") | Has("Wagner") | Has("Hoplite"))) & (Has("Cerberus") | Has("Sliver") | Has("Trident Class") | Has("Cormorant") | Has("Scuttle"))) & (Has("Salem Class") | Has("Renegade") | Has("Sky Hook") | Has("Gunther") | Has("TML-4"))) & (Has("Cybran T2 Mass Extractor") & Has("Cybran T2 Generator"))
    TheCompleteListOfRulesForEverySingleRegion["Defrag: Destroy northern UEF base (Cybran)"] = rule
    rule = ((((((Has("Zeus")) & (Has("Prowler") | Has("Sky Slammer") | Has("Tracer"))) & (Has("Mantis"))) & (Has("Rhino") | Has("Cerberus") | Has("Wagner") | Has("Hoplite"))) & (Has("Cerberus") | Has("Sliver") | Has("Trident Class") | Has("Cormorant") | Has("Scuttle"))) & (Has("Salem Class") | Has("Renegade") | Has("Sky Hook") | Has("Gunther") | Has("TML-4"))) & (Has("Cybran T2 Mass Extractor") & Has("Cybran T2 Generator"))
    TheCompleteListOfRulesForEverySingleRegion["Defrag: Sink UEF cruiser (Cybran)"] = rule
    rule = (((((((Has("Zeus")) & (Has("Prowler") | Has("Sky Slammer") | Has("Tracer"))) & (Has("Mantis"))) & (Has("Rhino") | Has("Cerberus") | Has("Wagner") | Has("Hoplite"))) & (Has("Cerberus") | Has("Sliver") | Has("Trident Class") | Has("Cormorant") | Has("Scuttle"))) & (Has("Salem Class") | Has("Renegade") | Has("Sky Hook") | Has("Gunther") | Has("TML-4"))) & (Has("Cybran T2 Mass Extractor") & Has("Cybran T2 Generator"))) & (Has("Burst Master") | Has("Banger"))
    TheCompleteListOfRulesForEverySingleRegion["Defrag: Destroy static artillery (Cybran)"] = rule
    rule = (((((((Has("Zeus")) & (Has("Prowler") | Has("Sky Slammer") | Has("Tracer"))) & (Has("Mantis"))) & (Has("Rhino") | Has("Cerberus") | Has("Wagner") | Has("Hoplite"))) & (Has("Cerberus") | Has("Sliver") | Has("Trident Class") | Has("Cormorant") | Has("Scuttle"))) & (Has("Salem Class") | Has("Renegade") | Has("Sky Hook") | Has("Gunther") | Has("TML-4"))) & (Has("Cybran T2 Mass Extractor") & Has("Cybran T2 Generator"))) & (Has("Burst Master") | Has("Banger"))
    TheCompleteListOfRulesForEverySingleRegion["Defrag: Escort trucks (Cybran)"] = rule
    rule = (((((((Has("Zeus")) & (Has("Prowler") | Has("Sky Slammer") | Has("Tracer"))) & (Has("Mantis"))) & (Has("Rhino") | Has("Cerberus") | Has("Wagner") | Has("Hoplite"))) & (Has("Cerberus") | Has("Sliver") | Has("Trident Class") | Has("Cormorant") | Has("Scuttle"))) & (Has("Salem Class") | Has("Renegade") | Has("Sky Hook") | Has("Gunther") | Has("TML-4"))) & (Has("Cybran T2 Mass Extractor") & Has("Cybran T2 Generator"))) & (Has("Burst Master") | Has("Banger"))
    TheCompleteListOfRulesForEverySingleRegion["Defrag: Escort ALL trucks (optional) (Cybran)"] = rule
    rule = (((((((Has("Zeus")) & (Has("Prowler") | Has("Sky Slammer") | Has("Tracer"))) & (Has("Mantis"))) & (Has("Rhino") | Has("Cerberus") | Has("Wagner") | Has("Hoplite"))) & (Has("Cerberus") | Has("Sliver") | Has("Trident Class") | Has("Cormorant") | Has("Scuttle"))) & (Has("Salem Class") | Has("Renegade") | Has("Sky Hook") | Has("Gunther") | Has("TML-4"))) & (Has("Cybran T2 Mass Extractor") & Has("Cybran T2 Generator"))) & (Has("Burst Master") | Has("Banger"))
    TheCompleteListOfRulesForEverySingleRegion["Defrag: Optional objective  (optional) (Cybran)"] = rule
    rule = (((((((Has("Zeus")) & (Has("Prowler") | Has("Sky Slammer") | Has("Tracer"))) & (Has("Mantis"))) & (Has("Rhino") | Has("Cerberus") | Has("Wagner") | Has("Hoplite"))) & (Has("Cerberus") | Has("Sliver") | Has("Trident Class") | Has("Cormorant") | Has("Scuttle"))) & (Has("Salem Class") | Has("Renegade") | Has("Sky Hook") | Has("Gunther") | Has("TML-4"))) & (Has("Cybran T2 Mass Extractor") & Has("Cybran T2 Generator"))) & (Has("Burst Master") | Has("Banger"))
    TheCompleteListOfRulesForEverySingleRegion["Defrag: Kill UEF Commander (Cybran)"] = rule
    rule = ((((((((Has("Zeus")) & (Has("Prowler") | Has("Sky Slammer") | Has("Tracer"))) & (Has("Mantis"))) & (Has("Rhino") | Has("Cerberus") | Has("Wagner") | Has("Hoplite"))) & (Has("Cerberus") | Has("Sliver") | Has("Trident Class") | Has("Cormorant") | Has("Scuttle"))) & (Has("Salem Class") | Has("Renegade") | Has("Sky Hook") | Has("Gunther") | Has("TML-4"))) & (Has("Cybran T2 Mass Extractor") & Has("Cybran T2 Generator"))) & (Has("Burst Master") | Has("Banger"))) & (Has("Salem Class"))
    TheCompleteListOfRulesForEverySingleRegion["Mainframe Tango: Defeat Aeon Commander (Cybran)"] = rule
    rule = ((((((((Has("Zeus")) & (Has("Prowler") | Has("Sky Slammer") | Has("Tracer"))) & (Has("Mantis"))) & (Has("Rhino") | Has("Cerberus") | Has("Wagner") | Has("Hoplite"))) & (Has("Cerberus") | Has("Sliver") | Has("Trident Class") | Has("Cormorant") | Has("Scuttle"))) & (Has("Salem Class") | Has("Renegade") | Has("Sky Hook") | Has("Gunther") | Has("TML-4"))) & (Has("Cybran T2 Mass Extractor") & Has("Cybran T2 Generator"))) & (Has("Burst Master") | Has("Banger"))) & (Has("Salem Class"))
    TheCompleteListOfRulesForEverySingleRegion["Mainframe Tango: Capture Network Node (Cybran)"] = rule
    rule = ((((((((Has("Zeus")) & (Has("Prowler") | Has("Sky Slammer") | Has("Tracer"))) & (Has("Mantis"))) & (Has("Rhino") | Has("Cerberus") | Has("Wagner") | Has("Hoplite"))) & (Has("Cerberus") | Has("Sliver") | Has("Trident Class") | Has("Cormorant") | Has("Scuttle"))) & (Has("Salem Class") | Has("Renegade") | Has("Sky Hook") | Has("Gunther") | Has("TML-4"))) & (Has("Cybran T2 Mass Extractor") & Has("Cybran T2 Generator"))) & (Has("Burst Master") | Has("Banger"))) & (Has("Salem Class"))
    TheCompleteListOfRulesForEverySingleRegion["Mainframe Tango: Save Network Node (Cybran)"] = rule
    rule = ((((((((Has("Zeus")) & (Has("Prowler") | Has("Sky Slammer") | Has("Tracer"))) & (Has("Mantis"))) & (Has("Rhino") | Has("Cerberus") | Has("Wagner") | Has("Hoplite"))) & (Has("Cerberus") | Has("Sliver") | Has("Trident Class") | Has("Cormorant") | Has("Scuttle"))) & (Has("Salem Class") | Has("Renegade") | Has("Sky Hook") | Has("Gunther") | Has("TML-4"))) & (Has("Cybran T2 Mass Extractor") & Has("Cybran T2 Generator"))) & (Has("Burst Master") | Has("Banger"))) & (Has("Salem Class"))
    TheCompleteListOfRulesForEverySingleRegion["Mainframe Tango: Save 80% civilian buildings (optional) (Cybran)"] = rule
    rule = ((((((((Has("Zeus")) & (Has("Prowler") | Has("Sky Slammer") | Has("Tracer"))) & (Has("Mantis"))) & (Has("Rhino") | Has("Cerberus") | Has("Wagner") | Has("Hoplite"))) & (Has("Cerberus") | Has("Sliver") | Has("Trident Class") | Has("Cormorant") | Has("Scuttle"))) & (Has("Salem Class") | Has("Renegade") | Has("Sky Hook") | Has("Gunther") | Has("TML-4"))) & (Has("Cybran T2 Mass Extractor") & Has("Cybran T2 Generator"))) & (Has("Burst Master") | Has("Banger"))) & (Has("Salem Class"))
    TheCompleteListOfRulesForEverySingleRegion["Mainframe Tango: Survive attacks (Cybran)"] = rule
    rule = ((((((((Has("Zeus")) & (Has("Prowler") | Has("Sky Slammer") | Has("Tracer"))) & (Has("Mantis"))) & (Has("Rhino") | Has("Cerberus") | Has("Wagner") | Has("Hoplite"))) & (Has("Cerberus") | Has("Sliver") | Has("Trident Class") | Has("Cormorant") | Has("Scuttle"))) & (Has("Salem Class") | Has("Renegade") | Has("Sky Hook") | Has("Gunther") | Has("TML-4"))) & (Has("Cybran T2 Mass Extractor") & Has("Cybran T2 Generator"))) & (Has("Burst Master") | Has("Banger"))) & (Has("Salem Class"))
    TheCompleteListOfRulesForEverySingleRegion["Mainframe Tango: Capture northeast node (Cybran)"] = rule
    rule = ((((((((Has("Zeus")) & (Has("Prowler") | Has("Sky Slammer") | Has("Tracer"))) & (Has("Mantis"))) & (Has("Rhino") | Has("Cerberus") | Has("Wagner") | Has("Hoplite"))) & (Has("Cerberus") | Has("Sliver") | Has("Trident Class") | Has("Cormorant") | Has("Scuttle"))) & (Has("Salem Class") | Has("Renegade") | Has("Sky Hook") | Has("Gunther") | Has("TML-4"))) & (Has("Cybran T2 Mass Extractor") & Has("Cybran T2 Generator"))) & (Has("Burst Master") | Has("Banger"))) & (Has("Salem Class"))
    TheCompleteListOfRulesForEverySingleRegion["Mainframe Tango: Capture northwest node (Cybran)"] = rule
    rule = ((((((((Has("Zeus")) & (Has("Prowler") | Has("Sky Slammer") | Has("Tracer"))) & (Has("Mantis"))) & (Has("Rhino") | Has("Cerberus") | Has("Wagner") | Has("Hoplite"))) & (Has("Cerberus") | Has("Sliver") | Has("Trident Class") | Has("Cormorant") | Has("Scuttle"))) & (Has("Salem Class") | Has("Renegade") | Has("Sky Hook") | Has("Gunther") | Has("TML-4"))) & (Has("Cybran T2 Mass Extractor") & Has("Cybran T2 Generator"))) & (Has("Burst Master") | Has("Banger"))) & (Has("Salem Class"))
    TheCompleteListOfRulesForEverySingleRegion["Mainframe Tango: Do not attack main Aeon base (Cybran)"] = rule
    rule = ((((((((Has("Zeus")) & (Has("Prowler") | Has("Sky Slammer") | Has("Tracer"))) & (Has("Mantis"))) & (Has("Rhino") | Has("Cerberus") | Has("Wagner") | Has("Hoplite"))) & (Has("Cerberus") | Has("Sliver") | Has("Trident Class") | Has("Cormorant") | Has("Scuttle"))) & (Has("Salem Class") | Has("Renegade") | Has("Sky Hook") | Has("Gunther") | Has("TML-4"))) & (Has("Cybran T2 Mass Extractor") & Has("Cybran T2 Generator"))) & (Has("Burst Master") | Has("Banger"))) & (Has("Salem Class"))
    TheCompleteListOfRulesForEverySingleRegion["Mainframe Tango: Kill Aeon Commander (Cybran)"] = rule
    rule = (((((((((Has("Zeus")) & (Has("Prowler") | Has("Sky Slammer") | Has("Tracer"))) & (Has("Mantis"))) & (Has("Rhino") | Has("Cerberus") | Has("Wagner") | Has("Hoplite"))) & (Has("Cerberus") | Has("Sliver") | Has("Trident Class") | Has("Cormorant") | Has("Scuttle"))) & (Has("Salem Class") | Has("Renegade") | Has("Sky Hook") | Has("Gunther") | Has("TML-4"))) & (Has("Cybran T2 Mass Extractor") & Has("Cybran T2 Generator"))) & (Has("Burst Master") | Has("Banger"))) & (Has("Salem Class"))) & (Has("Cybran T3 Mass Extractor") & Has("Ion Reactor") & (Has(" Loyalist") | Has("The Brick") | Has("Soul Ripper") | Has("Monkeylord") | Has("Megalith") | Has("Scathis") | Has("TML-4") | Has("Disruptor") | Has("Liberator") | Has("Wailer") | Has("Revenant")))
    TheCompleteListOfRulesForEverySingleRegion["Unlock: Destroy UEF generators (Cybran)"] = rule
    rule = ((((((((((Has("Zeus")) & (Has("Prowler") | Has("Sky Slammer") | Has("Tracer"))) & (Has("Mantis"))) & (Has("Rhino") | Has("Cerberus") | Has("Wagner") | Has("Hoplite"))) & (Has("Cerberus") | Has("Sliver") | Has("Trident Class") | Has("Cormorant") | Has("Scuttle"))) & (Has("Salem Class") | Has("Renegade") | Has("Sky Hook") | Has("Gunther") | Has("TML-4"))) & (Has("Cybran T2 Mass Extractor") & Has("Cybran T2 Generator"))) & (Has("Burst Master") | Has("Banger"))) & (Has("Salem Class"))) & (Has("Cybran T3 Mass Extractor") & Has("Ion Reactor") & (Has(" Loyalist") | Has("The Brick") | Has("Soul Ripper") | Has("Monkeylord") | Has("Megalith") | Has("Scathis") | Has("TML-4") | Has("Disruptor") | Has("Liberator") | Has("Wailer") | Has("Revenant")))) & (Has("Siren Class"))
    TheCompleteListOfRulesForEverySingleRegion["Unlock: Destroy UEF shipyards (optional) (Cybran)"] = rule
    rule = ((((((((((Has("Zeus")) & (Has("Prowler") | Has("Sky Slammer") | Has("Tracer"))) & (Has("Mantis"))) & (Has("Rhino") | Has("Cerberus") | Has("Wagner") | Has("Hoplite"))) & (Has("Cerberus") | Has("Sliver") | Has("Trident Class") | Has("Cormorant") | Has("Scuttle"))) & (Has("Salem Class") | Has("Renegade") | Has("Sky Hook") | Has("Gunther") | Has("TML-4"))) & (Has("Cybran T2 Mass Extractor") & Has("Cybran T2 Generator"))) & (Has("Burst Master") | Has("Banger"))) & (Has("Salem Class"))) & (Has("Cybran T3 Mass Extractor") & Has("Ion Reactor") & (Has(" Loyalist") | Has("The Brick") | Has("Soul Ripper") | Has("Monkeylord") | Has("Megalith") | Has("Scathis") | Has("TML-4") | Has("Disruptor") | Has("Liberator") | Has("Wailer") | Has("Revenant")))) & (Has("Siren Class"))
    TheCompleteListOfRulesForEverySingleRegion["Unlock: Destroy UEF radars (Cybran)"] = rule
    rule = (((((((((((Has("Zeus")) & (Has("Prowler") | Has("Sky Slammer") | Has("Tracer"))) & (Has("Mantis"))) & (Has("Rhino") | Has("Cerberus") | Has("Wagner") | Has("Hoplite"))) & (Has("Cerberus") | Has("Sliver") | Has("Trident Class") | Has("Cormorant") | Has("Scuttle"))) & (Has("Salem Class") | Has("Renegade") | Has("Sky Hook") | Has("Gunther") | Has("TML-4"))) & (Has("Cybran T2 Mass Extractor") & Has("Cybran T2 Generator"))) & (Has("Burst Master") | Has("Banger"))) & (Has("Salem Class"))) & (Has("Cybran T3 Mass Extractor") & Has("Ion Reactor") & (Has(" Loyalist") | Has("The Brick") | Has("Soul Ripper") | Has("Monkeylord") | Has("Megalith") | Has("Scathis") | Has("TML-4") | Has("Disruptor") | Has("Liberator") | Has("Wailer") | Has("Revenant")))) & (Has("Siren Class"))) & (Has("Dragonfly"))
    TheCompleteListOfRulesForEverySingleRegion["Unlock: Go to Hex5 (Cybran)"] = rule
    rule = ((((((((((((Has("Zeus")) & (Has("Prowler") | Has("Sky Slammer") | Has("Tracer"))) & (Has("Mantis"))) & (Has("Rhino") | Has("Cerberus") | Has("Wagner") | Has("Hoplite"))) & (Has("Cerberus") | Has("Sliver") | Has("Trident Class") | Has("Cormorant") | Has("Scuttle"))) & (Has("Salem Class") | Has("Renegade") | Has("Sky Hook") | Has("Gunther") | Has("TML-4"))) & (Has("Cybran T2 Mass Extractor") & Has("Cybran T2 Generator"))) & (Has("Burst Master") | Has("Banger"))) & (Has("Salem Class"))) & (Has("Cybran T3 Mass Extractor") & Has("Ion Reactor") & (Has(" Loyalist") | Has("The Brick") | Has("Soul Ripper") | Has("Monkeylord") | Has("Megalith") | Has("Scathis") | Has("TML-4") | Has("Disruptor") | Has("Liberator") | Has("Wailer") | Has("Revenant")))) & (Has("Siren Class"))) & (Has("Dragonfly"))) & (Has("Gemini") | Has("Bouncer") | Has("Myrmidon"))
    TheCompleteListOfRulesForEverySingleRegion["Unlock: Defend from heavy gunships (Cybran)"] = rule
    rule = ((((((((((((Has("Zeus")) & (Has("Prowler") | Has("Sky Slammer") | Has("Tracer"))) & (Has("Mantis"))) & (Has("Rhino") | Has("Cerberus") | Has("Wagner") | Has("Hoplite"))) & (Has("Cerberus") | Has("Sliver") | Has("Trident Class") | Has("Cormorant") | Has("Scuttle"))) & (Has("Salem Class") | Has("Renegade") | Has("Sky Hook") | Has("Gunther") | Has("TML-4"))) & (Has("Cybran T2 Mass Extractor") & Has("Cybran T2 Generator"))) & (Has("Burst Master") | Has("Banger"))) & (Has("Salem Class"))) & (Has("Cybran T3 Mass Extractor") & Has("Ion Reactor") & (Has(" Loyalist") | Has("The Brick") | Has("Soul Ripper") | Has("Monkeylord") | Has("Megalith") | Has("Scathis") | Has("TML-4") | Has("Disruptor") | Has("Liberator") | Has("Wailer") | Has("Revenant")))) & (Has("Siren Class"))) & (Has("Dragonfly"))) & (Has("Gemini") | Has("Bouncer") | Has("Myrmidon"))
    TheCompleteListOfRulesForEverySingleRegion["Unlock: Infect UEF landing pad (optional) (Cybran)"] = rule
    rule = ((((((((((((Has("Zeus")) & (Has("Prowler") | Has("Sky Slammer") | Has("Tracer"))) & (Has("Mantis"))) & (Has("Rhino") | Has("Cerberus") | Has("Wagner") | Has("Hoplite"))) & (Has("Cerberus") | Has("Sliver") | Has("Trident Class") | Has("Cormorant") | Has("Scuttle"))) & (Has("Salem Class") | Has("Renegade") | Has("Sky Hook") | Has("Gunther") | Has("TML-4"))) & (Has("Cybran T2 Mass Extractor") & Has("Cybran T2 Generator"))) & (Has("Burst Master") | Has("Banger"))) & (Has("Salem Class"))) & (Has("Cybran T3 Mass Extractor") & Has("Ion Reactor") & (Has(" Loyalist") | Has("The Brick") | Has("Soul Ripper") | Has("Monkeylord") | Has("Megalith") | Has("Scathis") | Has("TML-4") | Has("Disruptor") | Has("Liberator") | Has("Wailer") | Has("Revenant")))) & (Has("Siren Class"))) & (Has("Dragonfly"))) & (Has("Gemini") | Has("Bouncer") | Has("Myrmidon"))
    TheCompleteListOfRulesForEverySingleRegion["Unlock: This will be retconned later (Cybran)"] = rule
    rule = ((((((((((((Has("Zeus")) & (Has("Prowler") | Has("Sky Slammer") | Has("Tracer"))) & (Has("Mantis"))) & (Has("Rhino") | Has("Cerberus") | Has("Wagner") | Has("Hoplite"))) & (Has("Cerberus") | Has("Sliver") | Has("Trident Class") | Has("Cormorant") | Has("Scuttle"))) & (Has("Salem Class") | Has("Renegade") | Has("Sky Hook") | Has("Gunther") | Has("TML-4"))) & (Has("Cybran T2 Mass Extractor") & Has("Cybran T2 Generator"))) & (Has("Burst Master") | Has("Banger"))) & (Has("Salem Class"))) & (Has("Cybran T3 Mass Extractor") & Has("Ion Reactor") & (Has(" Loyalist") | Has("The Brick") | Has("Soul Ripper") | Has("Monkeylord") | Has("Megalith") | Has("Scathis") | Has("TML-4") | Has("Disruptor") | Has("Liberator") | Has("Wailer") | Has("Revenant")))) & (Has("Siren Class"))) & (Has("Dragonfly"))) & (Has("Gemini") | Has("Bouncer") | Has("Myrmidon"))
    TheCompleteListOfRulesForEverySingleRegion["Unlock: Kill UEF Commander (Cybran)"] = rule
    rule = ((((((((((((Has("Zeus")) & (Has("Prowler") | Has("Sky Slammer") | Has("Tracer"))) & (Has("Mantis"))) & (Has("Rhino") | Has("Cerberus") | Has("Wagner") | Has("Hoplite"))) & (Has("Cerberus") | Has("Sliver") | Has("Trident Class") | Has("Cormorant") | Has("Scuttle"))) & (Has("Salem Class") | Has("Renegade") | Has("Sky Hook") | Has("Gunther") | Has("TML-4"))) & (Has("Cybran T2 Mass Extractor") & Has("Cybran T2 Generator"))) & (Has("Burst Master") | Has("Banger"))) & (Has("Salem Class"))) & (Has("Cybran T3 Mass Extractor") & Has("Ion Reactor") & (Has(" Loyalist") | Has("The Brick") | Has("Soul Ripper") | Has("Monkeylord") | Has("Megalith") | Has("Scathis") | Has("TML-4") | Has("Disruptor") | Has("Liberator") | Has("Wailer") | Has("Revenant")))) & (Has("Siren Class"))) & (Has("Dragonfly"))) & (Has("Gemini") | Has("Bouncer") | Has("Myrmidon"))
    TheCompleteListOfRulesForEverySingleRegion["Freedom: Destroy CZAR (Cybran)"] = rule
    rule = (((((((((((((Has("Zeus")) & (Has("Prowler") | Has("Sky Slammer") | Has("Tracer"))) & (Has("Mantis"))) & (Has("Rhino") | Has("Cerberus") | Has("Wagner") | Has("Hoplite"))) & (Has("Cerberus") | Has("Sliver") | Has("Trident Class") | Has("Cormorant") | Has("Scuttle"))) & (Has("Salem Class") | Has("Renegade") | Has("Sky Hook") | Has("Gunther") | Has("TML-4"))) & (Has("Cybran T2 Mass Extractor") & Has("Cybran T2 Generator"))) & (Has("Burst Master") | Has("Banger"))) & (Has("Salem Class"))) & (Has("Cybran T3 Mass Extractor") & Has("Ion Reactor") & (Has(" Loyalist") | Has("The Brick") | Has("Soul Ripper") | Has("Monkeylord") | Has("Megalith") | Has("Scathis") | Has("TML-4") | Has("Disruptor") | Has("Liberator") | Has("Wailer") | Has("Revenant")))) & (Has("Siren Class"))) & (Has("Dragonfly"))) & (Has("Gemini") | Has("Bouncer") | Has("Myrmidon"))) & (Has("Summoner"))
    TheCompleteListOfRulesForEverySingleRegion["Freedom: Build Quantum Gate (Cybran)"] = rule
    rule = ((((((((((((((Has("Zeus")) & (Has("Prowler") | Has("Sky Slammer") | Has("Tracer"))) & (Has("Mantis"))) & (Has("Rhino") | Has("Cerberus") | Has("Wagner") | Has("Hoplite"))) & (Has("Cerberus") | Has("Sliver") | Has("Trident Class") | Has("Cormorant") | Has("Scuttle"))) & (Has("Salem Class") | Has("Renegade") | Has("Sky Hook") | Has("Gunther") | Has("TML-4"))) & (Has("Cybran T2 Mass Extractor") & Has("Cybran T2 Generator"))) & (Has("Burst Master") | Has("Banger"))) & (Has("Salem Class"))) & (Has("Cybran T3 Mass Extractor") & Has("Ion Reactor") & (Has(" Loyalist") | Has("The Brick") | Has("Soul Ripper") | Has("Monkeylord") | Has("Megalith") | Has("Scathis") | Has("TML-4") | Has("Disruptor") | Has("Liberator") | Has("Wailer") | Has("Revenant")))) & (Has("Siren Class"))) & (Has("Dragonfly"))) & (Has("Gemini") | Has("Bouncer") | Has("Myrmidon"))) & (Has("Summoner"))) & (Has("Loyalist") | Has("The Brick") | Has("Soul Ripper") | Has("Monkeylord") | Has("Megalith") | Has("Wailer") | Has("Revenant"))
    TheCompleteListOfRulesForEverySingleRegion["Freedom: Download Quantum Virus (Cybran)"] = rule
    rule = ((((((((((((((Has("Zeus")) & (Has("Prowler") | Has("Sky Slammer") | Has("Tracer"))) & (Has("Mantis"))) & (Has("Rhino") | Has("Cerberus") | Has("Wagner") | Has("Hoplite"))) & (Has("Cerberus") | Has("Sliver") | Has("Trident Class") | Has("Cormorant") | Has("Scuttle"))) & (Has("Salem Class") | Has("Renegade") | Has("Sky Hook") | Has("Gunther") | Has("TML-4"))) & (Has("Cybran T2 Mass Extractor") & Has("Cybran T2 Generator"))) & (Has("Burst Master") | Has("Banger"))) & (Has("Salem Class"))) & (Has("Cybran T3 Mass Extractor") & Has("Ion Reactor") & (Has(" Loyalist") | Has("The Brick") | Has("Soul Ripper") | Has("Monkeylord") | Has("Megalith") | Has("Scathis") | Has("TML-4") | Has("Disruptor") | Has("Liberator") | Has("Wailer") | Has("Revenant")))) & (Has("Siren Class"))) & (Has("Dragonfly"))) & (Has("Gemini") | Has("Bouncer") | Has("Myrmidon"))) & (Has("Summoner"))) & (Has("Loyalist") | Has("The Brick") | Has("Soul Ripper") | Has("Monkeylord") | Has("Megalith") | Has("Wailer") | Has("Revenant"))
    TheCompleteListOfRulesForEverySingleRegion["Freedom: Capture Black Sun control center (Cybran)"] = rule
    rule = ((((((((((((((Has("Zeus")) & (Has("Prowler") | Has("Sky Slammer") | Has("Tracer"))) & (Has("Mantis"))) & (Has("Rhino") | Has("Cerberus") | Has("Wagner") | Has("Hoplite"))) & (Has("Cerberus") | Has("Sliver") | Has("Trident Class") | Has("Cormorant") | Has("Scuttle"))) & (Has("Salem Class") | Has("Renegade") | Has("Sky Hook") | Has("Gunther") | Has("TML-4"))) & (Has("Cybran T2 Mass Extractor") & Has("Cybran T2 Generator"))) & (Has("Burst Master") | Has("Banger"))) & (Has("Salem Class"))) & (Has("Cybran T3 Mass Extractor") & Has("Ion Reactor") & (Has(" Loyalist") | Has("The Brick") | Has("Soul Ripper") | Has("Monkeylord") | Has("Megalith") | Has("Scathis") | Has("TML-4") | Has("Disruptor") | Has("Liberator") | Has("Wailer") | Has("Revenant")))) & (Has("Siren Class"))) & (Has("Dragonfly"))) & (Has("Gemini") | Has("Bouncer") | Has("Myrmidon"))) & (Has("Summoner"))) & (Has("Loyalist") | Has("The Brick") | Has("Soul Ripper") | Has("Monkeylord") | Has("Megalith") | Has("Wailer") | Has("Revenant"))
    TheCompleteListOfRulesForEverySingleRegion["Freedom: Capture Black Sun (Cybran)"] = rule
    rule = ((((((((((((((Has("Zeus")) & (Has("Prowler") | Has("Sky Slammer") | Has("Tracer"))) & (Has("Mantis"))) & (Has("Rhino") | Has("Cerberus") | Has("Wagner") | Has("Hoplite"))) & (Has("Cerberus") | Has("Sliver") | Has("Trident Class") | Has("Cormorant") | Has("Scuttle"))) & (Has("Salem Class") | Has("Renegade") | Has("Sky Hook") | Has("Gunther") | Has("TML-4"))) & (Has("Cybran T2 Mass Extractor") & Has("Cybran T2 Generator"))) & (Has("Burst Master") | Has("Banger"))) & (Has("Salem Class"))) & (Has("Cybran T3 Mass Extractor") & Has("Ion Reactor") & (Has(" Loyalist") | Has("The Brick") | Has("Soul Ripper") | Has("Monkeylord") | Has("Megalith") | Has("Scathis") | Has("TML-4") | Has("Disruptor") | Has("Liberator") | Has("Wailer") | Has("Revenant")))) & (Has("Siren Class"))) & (Has("Dragonfly"))) & (Has("Gemini") | Has("Bouncer") | Has("Myrmidon"))) & (Has("Summoner"))) & (Has("Loyalist") | Has("The Brick") | Has("Soul Ripper") | Has("Monkeylord") | Has("Megalith") | Has("Wailer") | Has("Revenant"))
    TheCompleteListOfRulesForEverySingleRegion["Freedom: Shoot Black Sun (Cybran)"] = rule
    rule = Has("Shimmer")
    TheCompleteListOfRulesForEverySingleRegion["Liberation: Build bombers (Aeon)"] = rule
    rule = Has("Shimmer")
    TheCompleteListOfRulesForEverySingleRegion["Liberation: Destroy radar defenders (Aeon)"] = rule
    rule = Has("Shimmer")
    TheCompleteListOfRulesForEverySingleRegion["Liberation: Capture radars (Aeon)"] = rule
    rule = (Has("Shimmer")) & (Has("Conservator") | Has("Thisle") | Has("Seeker"))
    TheCompleteListOfRulesForEverySingleRegion["Liberation: Destroy mex (Aeon)"] = rule
    rule = (Has("Shimmer")) & (Has("Conservator") | Has("Thisle") | Has("Seeker"))
    TheCompleteListOfRulesForEverySingleRegion["Liberation: Destroy UEF defences (Aeon)"] = rule
    rule = (Has("Shimmer")) & (Has("Conservator") | Has("Thisle") | Has("Seeker"))
    TheCompleteListOfRulesForEverySingleRegion["Liberation: Destroy UEF patrols (Aeon)"] = rule
    rule = (Has("Shimmer")) & (Has("Conservator") | Has("Thisle") | Has("Seeker"))
    TheCompleteListOfRulesForEverySingleRegion["Liberation: Destroy UEF base defenders (Aeon)"] = rule
    rule = (Has("Shimmer")) & (Has("Conservator") | Has("Thisle") | Has("Seeker"))
    TheCompleteListOfRulesForEverySingleRegion["Liberation: Destroy UEF base (Aeon)"] = rule
    rule = (Has("Shimmer")) & (Has("Conservator") | Has("Thisle") | Has("Seeker"))
    TheCompleteListOfRulesForEverySingleRegion["Liberation: Kill Aeon Commander (Aeon)"] = rule
    rule = (Has("Shimmer")) & (Has("Conservator") | Has("Thisle") | Has("Seeker"))
    TheCompleteListOfRulesForEverySingleRegion["Artifact: Destroy first village defenders (Aeon)"] = rule
    rule = (Has("Shimmer")) & (Has("Conservator") | Has("Thisle") | Has("Seeker"))
    TheCompleteListOfRulesForEverySingleRegion["Artifact: Destroy first temple (Aeon)"] = rule
    rule = (Has("Shimmer")) & (Has("Conservator") | Has("Thisle") | Has("Seeker"))
    TheCompleteListOfRulesForEverySingleRegion["Artifact: Protect first artifact (Aeon)"] = rule
    rule = ((Has("Shimmer")) & (Has("Conservator") | Has("Thisle") | Has("Seeker"))) & (Has("Aurora"))
    TheCompleteListOfRulesForEverySingleRegion["Artifact: Find second artifact (Aeon)"] = rule
    rule = (((Has("Shimmer")) & (Has("Conservator") | Has("Thisle") | Has("Seeker"))) & (Has("Aurora"))) & (Has("Obsidian") | Has("Oblivion") | Has("Blaze"))
    TheCompleteListOfRulesForEverySingleRegion["Artifact: Destroy Aeon reinforcements (Aeon)"] = rule
    rule = ((((Has("Shimmer")) & (Has("Conservator") | Has("Thisle") | Has("Seeker"))) & (Has("Aurora"))) & (Has("Obsidian") | Has("Oblivion") | Has("Blaze"))) & (Has("Oblivion") | Has("Sylph") | Has("Beacon Class") | Has("Skimmer") | Has("Tide"))
    TheCompleteListOfRulesForEverySingleRegion["Artifact: Protect second artifact (Aeon)"] = rule
    rule = ((((Has("Shimmer")) & (Has("Conservator") | Has("Thisle") | Has("Seeker"))) & (Has("Aurora"))) & (Has("Obsidian") | Has("Oblivion") | Has("Blaze"))) & (Has("Oblivion") | Has("Sylph") | Has("Beacon Class") | Has("Skimmer") | Has("Tide"))
    TheCompleteListOfRulesForEverySingleRegion["Artifact: Defend from Aeon attack (Aeon)"] = rule
    rule = ((((Has("Shimmer")) & (Has("Conservator") | Has("Thisle") | Has("Seeker"))) & (Has("Aurora"))) & (Has("Obsidian") | Has("Oblivion") | Has("Blaze"))) & (Has("Oblivion") | Has("Sylph") | Has("Beacon Class") | Has("Skimmer") | Has("Tide"))
    TheCompleteListOfRulesForEverySingleRegion["Artifact: Destroy eastern base (Aeon)"] = rule
    rule = (((((Has("Shimmer")) & (Has("Conservator") | Has("Thisle") | Has("Seeker"))) & (Has("Aurora"))) & (Has("Obsidian") | Has("Oblivion") | Has("Blaze"))) & (Has("Oblivion") | Has("Sylph") | Has("Beacon Class") | Has("Skimmer") | Has("Tide"))) & (Has("Exodus Class") | Has("Specter") | Has("Mercy") | Has("Chariot") | Has("Miasma") | Has("Serpentine"))
    TheCompleteListOfRulesForEverySingleRegion["Artifact: Destroy navy base (Aeon)"] = rule
    rule = (((((Has("Shimmer")) & (Has("Conservator") | Has("Thisle") | Has("Seeker"))) & (Has("Aurora"))) & (Has("Obsidian") | Has("Oblivion") | Has("Blaze"))) & (Has("Oblivion") | Has("Sylph") | Has("Beacon Class") | Has("Skimmer") | Has("Tide"))) & (Has("Exodus Class") | Has("Specter") | Has("Mercy") | Has("Chariot") | Has("Miasma") | Has("Serpentine"))
    TheCompleteListOfRulesForEverySingleRegion["Artifact: Protect third artifact (Aeon)"] = rule
    rule = (((((Has("Shimmer")) & (Has("Conservator") | Has("Thisle") | Has("Seeker"))) & (Has("Aurora"))) & (Has("Obsidian") | Has("Oblivion") | Has("Blaze"))) & (Has("Oblivion") | Has("Sylph") | Has("Beacon Class") | Has("Skimmer") | Has("Tide"))) & (Has("Exodus Class") | Has("Specter") | Has("Mercy") | Has("Chariot") | Has("Miasma") | Has("Serpentine"))
    TheCompleteListOfRulesForEverySingleRegion["Artifact: Kill Aeon Commander (optional) (Aeon)"] = rule
    rule = (((((Has("Shimmer")) & (Has("Conservator") | Has("Thisle") | Has("Seeker"))) & (Has("Aurora"))) & (Has("Obsidian") | Has("Oblivion") | Has("Blaze"))) & (Has("Oblivion") | Has("Sylph") | Has("Beacon Class") | Has("Skimmer") | Has("Tide"))) & (Has("Exodus Class") | Has("Specter") | Has("Mercy") | Has("Chariot") | Has("Miasma") | Has("Serpentine"))
    TheCompleteListOfRulesForEverySingleRegion["Artifact: Kill Mach (Aeon)"] = rule
    rule = (((((Has("Shimmer")) & (Has("Conservator") | Has("Thisle") | Has("Seeker"))) & (Has("Aurora"))) & (Has("Obsidian") | Has("Oblivion") | Has("Blaze"))) & (Has("Oblivion") | Has("Sylph") | Has("Beacon Class") | Has("Skimmer") | Has("Tide"))) & (Has("Exodus Class") | Has("Specter") | Has("Mercy") | Has("Chariot") | Has("Miasma") | Has("Serpentine"))
    TheCompleteListOfRulesForEverySingleRegion["Artifact: Go to Gate (Aeon)"] = rule
    rule = ((((((Has("Shimmer")) & (Has("Conservator") | Has("Thisle") | Has("Seeker"))) & (Has("Aurora"))) & (Has("Obsidian") | Has("Oblivion") | Has("Blaze"))) & (Has("Oblivion") | Has("Sylph") | Has("Beacon Class") | Has("Skimmer") | Has("Tide"))) & (Has("Exodus Class") | Has("Specter") | Has("Mercy") | Has("Chariot") | Has("Miasma") | Has("Serpentine"))) & (Has("Aeon T2 Mass Extractor") & Has("Aeon T2 Generator"))
    TheCompleteListOfRulesForEverySingleRegion["Defrag: Protect York 18 (Aeon)"] = rule
    rule = ((((((Has("Shimmer")) & (Has("Conservator") | Has("Thisle") | Has("Seeker"))) & (Has("Aurora"))) & (Has("Obsidian") | Has("Oblivion") | Has("Blaze"))) & (Has("Oblivion") | Has("Sylph") | Has("Beacon Class") | Has("Skimmer") | Has("Tide"))) & (Has("Exodus Class") | Has("Specter") | Has("Mercy") | Has("Chariot") | Has("Miasma") | Has("Serpentine"))) & (Has("Aeon T2 Mass Extractor") & Has("Aeon T2 Generator"))
    TheCompleteListOfRulesForEverySingleRegion["Defrag: Destroy western UEF base (Aeon)"] = rule
    rule = ((((((Has("Shimmer")) & (Has("Conservator") | Has("Thisle") | Has("Seeker"))) & (Has("Aurora"))) & (Has("Obsidian") | Has("Oblivion") | Has("Blaze"))) & (Has("Oblivion") | Has("Sylph") | Has("Beacon Class") | Has("Skimmer") | Has("Tide"))) & (Has("Exodus Class") | Has("Specter") | Has("Mercy") | Has("Chariot") | Has("Miasma") | Has("Serpentine"))) & (Has("Aeon T2 Mass Extractor") & Has("Aeon T2 Generator"))
    TheCompleteListOfRulesForEverySingleRegion["Defrag: Destroy north-western UEF base (Aeon)"] = rule
    rule = ((((((Has("Shimmer")) & (Has("Conservator") | Has("Thisle") | Has("Seeker"))) & (Has("Aurora"))) & (Has("Obsidian") | Has("Oblivion") | Has("Blaze"))) & (Has("Oblivion") | Has("Sylph") | Has("Beacon Class") | Has("Skimmer") | Has("Tide"))) & (Has("Exodus Class") | Has("Specter") | Has("Mercy") | Has("Chariot") | Has("Miasma") | Has("Serpentine"))) & (Has("Aeon T2 Mass Extractor") & Has("Aeon T2 Generator"))
    TheCompleteListOfRulesForEverySingleRegion["Defrag: Destroy northern UEF base (Aeon)"] = rule
    rule = ((((((Has("Shimmer")) & (Has("Conservator") | Has("Thisle") | Has("Seeker"))) & (Has("Aurora"))) & (Has("Obsidian") | Has("Oblivion") | Has("Blaze"))) & (Has("Oblivion") | Has("Sylph") | Has("Beacon Class") | Has("Skimmer") | Has("Tide"))) & (Has("Exodus Class") | Has("Specter") | Has("Mercy") | Has("Chariot") | Has("Miasma") | Has("Serpentine"))) & (Has("Aeon T2 Mass Extractor") & Has("Aeon T2 Generator"))
    TheCompleteListOfRulesForEverySingleRegion["Defrag: Sink UEF cruiser (Aeon)"] = rule
    rule = (((((((Has("Shimmer")) & (Has("Conservator") | Has("Thisle") | Has("Seeker"))) & (Has("Aurora"))) & (Has("Obsidian") | Has("Oblivion") | Has("Blaze"))) & (Has("Oblivion") | Has("Sylph") | Has("Beacon Class") | Has("Skimmer") | Has("Tide"))) & (Has("Exodus Class") | Has("Specter") | Has("Mercy") | Has("Chariot") | Has("Miasma") | Has("Serpentine"))) & (Has("Aeon T2 Mass Extractor") & Has("Aeon T2 Generator"))) & (Has("Marr") | Has("Ascendant"))
    TheCompleteListOfRulesForEverySingleRegion["Defrag: Destroy static artillery (Aeon)"] = rule
    rule = (((((((Has("Shimmer")) & (Has("Conservator") | Has("Thisle") | Has("Seeker"))) & (Has("Aurora"))) & (Has("Obsidian") | Has("Oblivion") | Has("Blaze"))) & (Has("Oblivion") | Has("Sylph") | Has("Beacon Class") | Has("Skimmer") | Has("Tide"))) & (Has("Exodus Class") | Has("Specter") | Has("Mercy") | Has("Chariot") | Has("Miasma") | Has("Serpentine"))) & (Has("Aeon T2 Mass Extractor") & Has("Aeon T2 Generator"))) & (Has("Marr") | Has("Ascendant"))
    TheCompleteListOfRulesForEverySingleRegion["Defrag: Escort trucks (Aeon)"] = rule
    rule = (((((((Has("Shimmer")) & (Has("Conservator") | Has("Thisle") | Has("Seeker"))) & (Has("Aurora"))) & (Has("Obsidian") | Has("Oblivion") | Has("Blaze"))) & (Has("Oblivion") | Has("Sylph") | Has("Beacon Class") | Has("Skimmer") | Has("Tide"))) & (Has("Exodus Class") | Has("Specter") | Has("Mercy") | Has("Chariot") | Has("Miasma") | Has("Serpentine"))) & (Has("Aeon T2 Mass Extractor") & Has("Aeon T2 Generator"))) & (Has("Marr") | Has("Ascendant"))
    TheCompleteListOfRulesForEverySingleRegion["Defrag: Escort ALL trucks (optional) (Aeon)"] = rule
    rule = (((((((Has("Shimmer")) & (Has("Conservator") | Has("Thisle") | Has("Seeker"))) & (Has("Aurora"))) & (Has("Obsidian") | Has("Oblivion") | Has("Blaze"))) & (Has("Oblivion") | Has("Sylph") | Has("Beacon Class") | Has("Skimmer") | Has("Tide"))) & (Has("Exodus Class") | Has("Specter") | Has("Mercy") | Has("Chariot") | Has("Miasma") | Has("Serpentine"))) & (Has("Aeon T2 Mass Extractor") & Has("Aeon T2 Generator"))) & (Has("Marr") | Has("Ascendant"))
    TheCompleteListOfRulesForEverySingleRegion["Defrag: Optional objective  (optional) (Aeon)"] = rule
    rule = (((((((Has("Shimmer")) & (Has("Conservator") | Has("Thisle") | Has("Seeker"))) & (Has("Aurora"))) & (Has("Obsidian") | Has("Oblivion") | Has("Blaze"))) & (Has("Oblivion") | Has("Sylph") | Has("Beacon Class") | Has("Skimmer") | Has("Tide"))) & (Has("Exodus Class") | Has("Specter") | Has("Mercy") | Has("Chariot") | Has("Miasma") | Has("Serpentine"))) & (Has("Aeon T2 Mass Extractor") & Has("Aeon T2 Generator"))) & (Has("Marr") | Has("Ascendant"))
    TheCompleteListOfRulesForEverySingleRegion["Defrag: Kill UEF Commander (Aeon)"] = rule
    rule = ((((((((Has("Shimmer")) & (Has("Conservator") | Has("Thisle") | Has("Seeker"))) & (Has("Aurora"))) & (Has("Obsidian") | Has("Oblivion") | Has("Blaze"))) & (Has("Oblivion") | Has("Sylph") | Has("Beacon Class") | Has("Skimmer") | Has("Tide"))) & (Has("Exodus Class") | Has("Specter") | Has("Mercy") | Has("Chariot") | Has("Miasma") | Has("Serpentine"))) & (Has("Aeon T2 Mass Extractor") & Has("Aeon T2 Generator"))) & (Has("Marr") | Has("Ascendant"))) & (Has("Exodus Class"))
    TheCompleteListOfRulesForEverySingleRegion["Mainframe Tango: Defeat Aeon Commander (Aeon)"] = rule
    rule = ((((((((Has("Shimmer")) & (Has("Conservator") | Has("Thisle") | Has("Seeker"))) & (Has("Aurora"))) & (Has("Obsidian") | Has("Oblivion") | Has("Blaze"))) & (Has("Oblivion") | Has("Sylph") | Has("Beacon Class") | Has("Skimmer") | Has("Tide"))) & (Has("Exodus Class") | Has("Specter") | Has("Mercy") | Has("Chariot") | Has("Miasma") | Has("Serpentine"))) & (Has("Aeon T2 Mass Extractor") & Has("Aeon T2 Generator"))) & (Has("Marr") | Has("Ascendant"))) & (Has("Exodus Class"))
    TheCompleteListOfRulesForEverySingleRegion["Mainframe Tango: Capture Network Node (Aeon)"] = rule
    rule = ((((((((Has("Shimmer")) & (Has("Conservator") | Has("Thisle") | Has("Seeker"))) & (Has("Aurora"))) & (Has("Obsidian") | Has("Oblivion") | Has("Blaze"))) & (Has("Oblivion") | Has("Sylph") | Has("Beacon Class") | Has("Skimmer") | Has("Tide"))) & (Has("Exodus Class") | Has("Specter") | Has("Mercy") | Has("Chariot") | Has("Miasma") | Has("Serpentine"))) & (Has("Aeon T2 Mass Extractor") & Has("Aeon T2 Generator"))) & (Has("Marr") | Has("Ascendant"))) & (Has("Exodus Class"))
    TheCompleteListOfRulesForEverySingleRegion["Mainframe Tango: Save Network Node (Aeon)"] = rule
    rule = ((((((((Has("Shimmer")) & (Has("Conservator") | Has("Thisle") | Has("Seeker"))) & (Has("Aurora"))) & (Has("Obsidian") | Has("Oblivion") | Has("Blaze"))) & (Has("Oblivion") | Has("Sylph") | Has("Beacon Class") | Has("Skimmer") | Has("Tide"))) & (Has("Exodus Class") | Has("Specter") | Has("Mercy") | Has("Chariot") | Has("Miasma") | Has("Serpentine"))) & (Has("Aeon T2 Mass Extractor") & Has("Aeon T2 Generator"))) & (Has("Marr") | Has("Ascendant"))) & (Has("Exodus Class"))
    TheCompleteListOfRulesForEverySingleRegion["Mainframe Tango: Save 80% civilian buildings (optional) (Aeon)"] = rule
    rule = ((((((((Has("Shimmer")) & (Has("Conservator") | Has("Thisle") | Has("Seeker"))) & (Has("Aurora"))) & (Has("Obsidian") | Has("Oblivion") | Has("Blaze"))) & (Has("Oblivion") | Has("Sylph") | Has("Beacon Class") | Has("Skimmer") | Has("Tide"))) & (Has("Exodus Class") | Has("Specter") | Has("Mercy") | Has("Chariot") | Has("Miasma") | Has("Serpentine"))) & (Has("Aeon T2 Mass Extractor") & Has("Aeon T2 Generator"))) & (Has("Marr") | Has("Ascendant"))) & (Has("Exodus Class"))
    TheCompleteListOfRulesForEverySingleRegion["Mainframe Tango: Survive attacks (Aeon)"] = rule
    rule = ((((((((Has("Shimmer")) & (Has("Conservator") | Has("Thisle") | Has("Seeker"))) & (Has("Aurora"))) & (Has("Obsidian") | Has("Oblivion") | Has("Blaze"))) & (Has("Oblivion") | Has("Sylph") | Has("Beacon Class") | Has("Skimmer") | Has("Tide"))) & (Has("Exodus Class") | Has("Specter") | Has("Mercy") | Has("Chariot") | Has("Miasma") | Has("Serpentine"))) & (Has("Aeon T2 Mass Extractor") & Has("Aeon T2 Generator"))) & (Has("Marr") | Has("Ascendant"))) & (Has("Exodus Class"))
    TheCompleteListOfRulesForEverySingleRegion["Mainframe Tango: Capture northeast node (Aeon)"] = rule
    rule = ((((((((Has("Shimmer")) & (Has("Conservator") | Has("Thisle") | Has("Seeker"))) & (Has("Aurora"))) & (Has("Obsidian") | Has("Oblivion") | Has("Blaze"))) & (Has("Oblivion") | Has("Sylph") | Has("Beacon Class") | Has("Skimmer") | Has("Tide"))) & (Has("Exodus Class") | Has("Specter") | Has("Mercy") | Has("Chariot") | Has("Miasma") | Has("Serpentine"))) & (Has("Aeon T2 Mass Extractor") & Has("Aeon T2 Generator"))) & (Has("Marr") | Has("Ascendant"))) & (Has("Exodus Class"))
    TheCompleteListOfRulesForEverySingleRegion["Mainframe Tango: Capture northwest node (Aeon)"] = rule
    rule = ((((((((Has("Shimmer")) & (Has("Conservator") | Has("Thisle") | Has("Seeker"))) & (Has("Aurora"))) & (Has("Obsidian") | Has("Oblivion") | Has("Blaze"))) & (Has("Oblivion") | Has("Sylph") | Has("Beacon Class") | Has("Skimmer") | Has("Tide"))) & (Has("Exodus Class") | Has("Specter") | Has("Mercy") | Has("Chariot") | Has("Miasma") | Has("Serpentine"))) & (Has("Aeon T2 Mass Extractor") & Has("Aeon T2 Generator"))) & (Has("Marr") | Has("Ascendant"))) & (Has("Exodus Class"))
    TheCompleteListOfRulesForEverySingleRegion["Mainframe Tango: Do not attack main Aeon base (Aeon)"] = rule
    rule = ((((((((Has("Shimmer")) & (Has("Conservator") | Has("Thisle") | Has("Seeker"))) & (Has("Aurora"))) & (Has("Obsidian") | Has("Oblivion") | Has("Blaze"))) & (Has("Oblivion") | Has("Sylph") | Has("Beacon Class") | Has("Skimmer") | Has("Tide"))) & (Has("Exodus Class") | Has("Specter") | Has("Mercy") | Has("Chariot") | Has("Miasma") | Has("Serpentine"))) & (Has("Aeon T2 Mass Extractor") & Has("Aeon T2 Generator"))) & (Has("Marr") | Has("Ascendant"))) & (Has("Exodus Class"))
    TheCompleteListOfRulesForEverySingleRegion["Mainframe Tango: Kill Aeon Commander (Aeon)"] = rule
    rule = (((((((((Has("Shimmer")) & (Has("Conservator") | Has("Thisle") | Has("Seeker"))) & (Has("Aurora"))) & (Has("Obsidian") | Has("Oblivion") | Has("Blaze"))) & (Has("Oblivion") | Has("Sylph") | Has("Beacon Class") | Has("Skimmer") | Has("Tide"))) & (Has("Exodus Class") | Has("Specter") | Has("Mercy") | Has("Chariot") | Has("Miasma") | Has("Serpentine"))) & (Has("Aeon T2 Mass Extractor") & Has("Aeon T2 Generator"))) & (Has("Marr") | Has("Ascendant"))) & (Has("Exodus Class"))) & (Has("Aeon T3 Mass Extractor") & Has("Quantum Reactor") & (Has("Sprite Striker") | Has("Harbringer Mk4") | Has("Czar") | Has("Galactic Colossus") | Has("Salvation") | Has("Serpentine") | Has("Emissary") | Has("Apocalypse") | Has("Restorer") | Has("Shocker")))
    TheCompleteListOfRulesForEverySingleRegion["Unlock: Destroy UEF generators (Aeon)"] = rule
    rule = ((((((((((Has("Shimmer")) & (Has("Conservator") | Has("Thisle") | Has("Seeker"))) & (Has("Aurora"))) & (Has("Obsidian") | Has("Oblivion") | Has("Blaze"))) & (Has("Oblivion") | Has("Sylph") | Has("Beacon Class") | Has("Skimmer") | Has("Tide"))) & (Has("Exodus Class") | Has("Specter") | Has("Mercy") | Has("Chariot") | Has("Miasma") | Has("Serpentine"))) & (Has("Aeon T2 Mass Extractor") & Has("Aeon T2 Generator"))) & (Has("Marr") | Has("Ascendant"))) & (Has("Exodus Class"))) & (Has("Aeon T3 Mass Extractor") & Has("Quantum Reactor") & (Has("Sprite Striker") | Has("Harbringer Mk4") | Has("Czar") | Has("Galactic Colossus") | Has("Salvation") | Has("Serpentine") | Has("Emissary") | Has("Apocalypse") | Has("Restorer") | Has("Shocker")))) & (Has("Infinity Class"))
    TheCompleteListOfRulesForEverySingleRegion["Unlock: Destroy UEF shipyards (optional) (Aeon)"] = rule
    rule = ((((((((((Has("Shimmer")) & (Has("Conservator") | Has("Thisle") | Has("Seeker"))) & (Has("Aurora"))) & (Has("Obsidian") | Has("Oblivion") | Has("Blaze"))) & (Has("Oblivion") | Has("Sylph") | Has("Beacon Class") | Has("Skimmer") | Has("Tide"))) & (Has("Exodus Class") | Has("Specter") | Has("Mercy") | Has("Chariot") | Has("Miasma") | Has("Serpentine"))) & (Has("Aeon T2 Mass Extractor") & Has("Aeon T2 Generator"))) & (Has("Marr") | Has("Ascendant"))) & (Has("Exodus Class"))) & (Has("Aeon T3 Mass Extractor") & Has("Quantum Reactor") & (Has("Sprite Striker") | Has("Harbringer Mk4") | Has("Czar") | Has("Galactic Colossus") | Has("Salvation") | Has("Serpentine") | Has("Emissary") | Has("Apocalypse") | Has("Restorer") | Has("Shocker")))) & (Has("Infinity Class"))
    TheCompleteListOfRulesForEverySingleRegion["Unlock: Destroy UEF radars (Aeon)"] = rule
    rule = (((((((((((Has("Shimmer")) & (Has("Conservator") | Has("Thisle") | Has("Seeker"))) & (Has("Aurora"))) & (Has("Obsidian") | Has("Oblivion") | Has("Blaze"))) & (Has("Oblivion") | Has("Sylph") | Has("Beacon Class") | Has("Skimmer") | Has("Tide"))) & (Has("Exodus Class") | Has("Specter") | Has("Mercy") | Has("Chariot") | Has("Miasma") | Has("Serpentine"))) & (Has("Aeon T2 Mass Extractor") & Has("Aeon T2 Generator"))) & (Has("Marr") | Has("Ascendant"))) & (Has("Exodus Class"))) & (Has("Aeon T3 Mass Extractor") & Has("Quantum Reactor") & (Has("Sprite Striker") | Has("Harbringer Mk4") | Has("Czar") | Has("Galactic Colossus") | Has("Salvation") | Has("Serpentine") | Has("Emissary") | Has("Apocalypse") | Has("Restorer") | Has("Shocker")))) & (Has("Infinity Class"))) & (Has("Aluminar"))
    TheCompleteListOfRulesForEverySingleRegion["Unlock: Go to Hex5 (Aeon)"] = rule
    rule = ((((((((((((Has("Shimmer")) & (Has("Conservator") | Has("Thisle") | Has("Seeker"))) & (Has("Aurora"))) & (Has("Obsidian") | Has("Oblivion") | Has("Blaze"))) & (Has("Oblivion") | Has("Sylph") | Has("Beacon Class") | Has("Skimmer") | Has("Tide"))) & (Has("Exodus Class") | Has("Specter") | Has("Mercy") | Has("Chariot") | Has("Miasma") | Has("Serpentine"))) & (Has("Aeon T2 Mass Extractor") & Has("Aeon T2 Generator"))) & (Has("Marr") | Has("Ascendant"))) & (Has("Exodus Class"))) & (Has("Aeon T3 Mass Extractor") & Has("Quantum Reactor") & (Has("Sprite Striker") | Has("Harbringer Mk4") | Has("Czar") | Has("Galactic Colossus") | Has("Salvation") | Has("Serpentine") | Has("Emissary") | Has("Apocalypse") | Has("Restorer") | Has("Shocker")))) & (Has("Infinity Class"))) & (Has("Aluminar"))) & (Has("Corona") | Has("Redeemer") | Has("Transcender"))
    TheCompleteListOfRulesForEverySingleRegion["Unlock: Defend from heavy gunships (Aeon)"] = rule
    rule = ((((((((((((Has("Shimmer")) & (Has("Conservator") | Has("Thisle") | Has("Seeker"))) & (Has("Aurora"))) & (Has("Obsidian") | Has("Oblivion") | Has("Blaze"))) & (Has("Oblivion") | Has("Sylph") | Has("Beacon Class") | Has("Skimmer") | Has("Tide"))) & (Has("Exodus Class") | Has("Specter") | Has("Mercy") | Has("Chariot") | Has("Miasma") | Has("Serpentine"))) & (Has("Aeon T2 Mass Extractor") & Has("Aeon T2 Generator"))) & (Has("Marr") | Has("Ascendant"))) & (Has("Exodus Class"))) & (Has("Aeon T3 Mass Extractor") & Has("Quantum Reactor") & (Has("Sprite Striker") | Has("Harbringer Mk4") | Has("Czar") | Has("Galactic Colossus") | Has("Salvation") | Has("Serpentine") | Has("Emissary") | Has("Apocalypse") | Has("Restorer") | Has("Shocker")))) & (Has("Infinity Class"))) & (Has("Aluminar"))) & (Has("Corona") | Has("Redeemer") | Has("Transcender"))
    TheCompleteListOfRulesForEverySingleRegion["Unlock: Infect UEF landing pad (optional) (Aeon)"] = rule
    rule = ((((((((((((Has("Shimmer")) & (Has("Conservator") | Has("Thisle") | Has("Seeker"))) & (Has("Aurora"))) & (Has("Obsidian") | Has("Oblivion") | Has("Blaze"))) & (Has("Oblivion") | Has("Sylph") | Has("Beacon Class") | Has("Skimmer") | Has("Tide"))) & (Has("Exodus Class") | Has("Specter") | Has("Mercy") | Has("Chariot") | Has("Miasma") | Has("Serpentine"))) & (Has("Aeon T2 Mass Extractor") & Has("Aeon T2 Generator"))) & (Has("Marr") | Has("Ascendant"))) & (Has("Exodus Class"))) & (Has("Aeon T3 Mass Extractor") & Has("Quantum Reactor") & (Has("Sprite Striker") | Has("Harbringer Mk4") | Has("Czar") | Has("Galactic Colossus") | Has("Salvation") | Has("Serpentine") | Has("Emissary") | Has("Apocalypse") | Has("Restorer") | Has("Shocker")))) & (Has("Infinity Class"))) & (Has("Aluminar"))) & (Has("Corona") | Has("Redeemer") | Has("Transcender"))
    TheCompleteListOfRulesForEverySingleRegion["Unlock: This will be retconned later (Aeon)"] = rule
    rule = ((((((((((((Has("Shimmer")) & (Has("Conservator") | Has("Thisle") | Has("Seeker"))) & (Has("Aurora"))) & (Has("Obsidian") | Has("Oblivion") | Has("Blaze"))) & (Has("Oblivion") | Has("Sylph") | Has("Beacon Class") | Has("Skimmer") | Has("Tide"))) & (Has("Exodus Class") | Has("Specter") | Has("Mercy") | Has("Chariot") | Has("Miasma") | Has("Serpentine"))) & (Has("Aeon T2 Mass Extractor") & Has("Aeon T2 Generator"))) & (Has("Marr") | Has("Ascendant"))) & (Has("Exodus Class"))) & (Has("Aeon T3 Mass Extractor") & Has("Quantum Reactor") & (Has("Sprite Striker") | Has("Harbringer Mk4") | Has("Czar") | Has("Galactic Colossus") | Has("Salvation") | Has("Serpentine") | Has("Emissary") | Has("Apocalypse") | Has("Restorer") | Has("Shocker")))) & (Has("Infinity Class"))) & (Has("Aluminar"))) & (Has("Corona") | Has("Redeemer") | Has("Transcender"))
    TheCompleteListOfRulesForEverySingleRegion["Unlock: Kill UEF Commander (Aeon)"] = rule
    rule = ((((((((((((Has("Shimmer")) & (Has("Conservator") | Has("Thisle") | Has("Seeker"))) & (Has("Aurora"))) & (Has("Obsidian") | Has("Oblivion") | Has("Blaze"))) & (Has("Oblivion") | Has("Sylph") | Has("Beacon Class") | Has("Skimmer") | Has("Tide"))) & (Has("Exodus Class") | Has("Specter") | Has("Mercy") | Has("Chariot") | Has("Miasma") | Has("Serpentine"))) & (Has("Aeon T2 Mass Extractor") & Has("Aeon T2 Generator"))) & (Has("Marr") | Has("Ascendant"))) & (Has("Exodus Class"))) & (Has("Aeon T3 Mass Extractor") & Has("Quantum Reactor") & (Has("Sprite Striker") | Has("Harbringer Mk4") | Has("Czar") | Has("Galactic Colossus") | Has("Salvation") | Has("Serpentine") | Has("Emissary") | Has("Apocalypse") | Has("Restorer") | Has("Shocker")))) & (Has("Infinity Class"))) & (Has("Aluminar"))) & (Has("Corona") | Has("Redeemer") | Has("Transcender"))
    TheCompleteListOfRulesForEverySingleRegion["Freedom: Destroy CZAR (Aeon)"] = rule
    rule = (((((((((((((Has("Shimmer")) & (Has("Conservator") | Has("Thisle") | Has("Seeker"))) & (Has("Aurora"))) & (Has("Obsidian") | Has("Oblivion") | Has("Blaze"))) & (Has("Oblivion") | Has("Sylph") | Has("Beacon Class") | Has("Skimmer") | Has("Tide"))) & (Has("Exodus Class") | Has("Specter") | Has("Mercy") | Has("Chariot") | Has("Miasma") | Has("Serpentine"))) & (Has("Aeon T2 Mass Extractor") & Has("Aeon T2 Generator"))) & (Has("Marr") | Has("Ascendant"))) & (Has("Exodus Class"))) & (Has("Aeon T3 Mass Extractor") & Has("Quantum Reactor") & (Has("Sprite Striker") | Has("Harbringer Mk4") | Has("Czar") | Has("Galactic Colossus") | Has("Salvation") | Has("Serpentine") | Has("Emissary") | Has("Apocalypse") | Has("Restorer") | Has("Shocker")))) & (Has("Infinity Class"))) & (Has("Aluminar"))) & (Has("Corona") | Has("Redeemer") | Has("Transcender"))) & (Has("Portal"))
    TheCompleteListOfRulesForEverySingleRegion["Freedom: Build Quantum Gate (Aeon)"] = rule
    rule = ((((((((((((((Has("Shimmer")) & (Has("Conservator") | Has("Thisle") | Has("Seeker"))) & (Has("Aurora"))) & (Has("Obsidian") | Has("Oblivion") | Has("Blaze"))) & (Has("Oblivion") | Has("Sylph") | Has("Beacon Class") | Has("Skimmer") | Has("Tide"))) & (Has("Exodus Class") | Has("Specter") | Has("Mercy") | Has("Chariot") | Has("Miasma") | Has("Serpentine"))) & (Has("Aeon T2 Mass Extractor") & Has("Aeon T2 Generator"))) & (Has("Marr") | Has("Ascendant"))) & (Has("Exodus Class"))) & (Has("Aeon T3 Mass Extractor") & Has("Quantum Reactor") & (Has("Sprite Striker") | Has("Harbringer Mk4") | Has("Czar") | Has("Galactic Colossus") | Has("Salvation") | Has("Serpentine") | Has("Emissary") | Has("Apocalypse") | Has("Restorer") | Has("Shocker")))) & (Has("Infinity Class"))) & (Has("Aluminar"))) & (Has("Corona") | Has("Redeemer") | Has("Transcender"))) & (Has("Portal"))) & (Has("Sprite Striker") | Has("Harbringer Mk4") | Has("Czar") | Has("Galactic Colossus") | Has("Restorer") | Has("Shocker"))
    TheCompleteListOfRulesForEverySingleRegion["Freedom: Download Quantum Virus (Aeon)"] = rule
    rule = ((((((((((((((Has("Shimmer")) & (Has("Conservator") | Has("Thisle") | Has("Seeker"))) & (Has("Aurora"))) & (Has("Obsidian") | Has("Oblivion") | Has("Blaze"))) & (Has("Oblivion") | Has("Sylph") | Has("Beacon Class") | Has("Skimmer") | Has("Tide"))) & (Has("Exodus Class") | Has("Specter") | Has("Mercy") | Has("Chariot") | Has("Miasma") | Has("Serpentine"))) & (Has("Aeon T2 Mass Extractor") & Has("Aeon T2 Generator"))) & (Has("Marr") | Has("Ascendant"))) & (Has("Exodus Class"))) & (Has("Aeon T3 Mass Extractor") & Has("Quantum Reactor") & (Has("Sprite Striker") | Has("Harbringer Mk4") | Has("Czar") | Has("Galactic Colossus") | Has("Salvation") | Has("Serpentine") | Has("Emissary") | Has("Apocalypse") | Has("Restorer") | Has("Shocker")))) & (Has("Infinity Class"))) & (Has("Aluminar"))) & (Has("Corona") | Has("Redeemer") | Has("Transcender"))) & (Has("Portal"))) & (Has("Sprite Striker") | Has("Harbringer Mk4") | Has("Czar") | Has("Galactic Colossus") | Has("Restorer") | Has("Shocker"))
    TheCompleteListOfRulesForEverySingleRegion["Freedom: Capture Black Sun control center (Aeon)"] = rule
    rule = ((((((((((((((Has("Shimmer")) & (Has("Conservator") | Has("Thisle") | Has("Seeker"))) & (Has("Aurora"))) & (Has("Obsidian") | Has("Oblivion") | Has("Blaze"))) & (Has("Oblivion") | Has("Sylph") | Has("Beacon Class") | Has("Skimmer") | Has("Tide"))) & (Has("Exodus Class") | Has("Specter") | Has("Mercy") | Has("Chariot") | Has("Miasma") | Has("Serpentine"))) & (Has("Aeon T2 Mass Extractor") & Has("Aeon T2 Generator"))) & (Has("Marr") | Has("Ascendant"))) & (Has("Exodus Class"))) & (Has("Aeon T3 Mass Extractor") & Has("Quantum Reactor") & (Has("Sprite Striker") | Has("Harbringer Mk4") | Has("Czar") | Has("Galactic Colossus") | Has("Salvation") | Has("Serpentine") | Has("Emissary") | Has("Apocalypse") | Has("Restorer") | Has("Shocker")))) & (Has("Infinity Class"))) & (Has("Aluminar"))) & (Has("Corona") | Has("Redeemer") | Has("Transcender"))) & (Has("Portal"))) & (Has("Sprite Striker") | Has("Harbringer Mk4") | Has("Czar") | Has("Galactic Colossus") | Has("Restorer") | Has("Shocker"))
    TheCompleteListOfRulesForEverySingleRegion["Freedom: Capture Black Sun (Aeon)"] = rule
    rule = ((((((((((((((Has("Shimmer")) & (Has("Conservator") | Has("Thisle") | Has("Seeker"))) & (Has("Aurora"))) & (Has("Obsidian") | Has("Oblivion") | Has("Blaze"))) & (Has("Oblivion") | Has("Sylph") | Has("Beacon Class") | Has("Skimmer") | Has("Tide"))) & (Has("Exodus Class") | Has("Specter") | Has("Mercy") | Has("Chariot") | Has("Miasma") | Has("Serpentine"))) & (Has("Aeon T2 Mass Extractor") & Has("Aeon T2 Generator"))) & (Has("Marr") | Has("Ascendant"))) & (Has("Exodus Class"))) & (Has("Aeon T3 Mass Extractor") & Has("Quantum Reactor") & (Has("Sprite Striker") | Has("Harbringer Mk4") | Has("Czar") | Has("Galactic Colossus") | Has("Salvation") | Has("Serpentine") | Has("Emissary") | Has("Apocalypse") | Has("Restorer") | Has("Shocker")))) & (Has("Infinity Class"))) & (Has("Aluminar"))) & (Has("Corona") | Has("Redeemer") | Has("Transcender"))) & (Has("Portal"))) & (Has("Sprite Striker") | Has("Harbringer Mk4") | Has("Czar") | Has("Galactic Colossus") | Has("Restorer") | Has("Shocker"))
    TheCompleteListOfRulesForEverySingleRegion["Freedom: Shoot Black Sun (Aeon)"] = rule
    rule = Has("Sinnve")
    TheCompleteListOfRulesForEverySingleRegion["Liberation: Build bombers (Sera)"] = rule
    rule = Has("Sinnve")
    TheCompleteListOfRulesForEverySingleRegion["Liberation: Destroy radar defenders (Sera)"] = rule
    rule = Has("Sinnve")
    TheCompleteListOfRulesForEverySingleRegion["Liberation: Capture radars (Sera)"] = rule
    rule = (Has("Sinnve")) & (Has("Ia-atha") | Has("Ia-istle") | Has("Ialla"))
    TheCompleteListOfRulesForEverySingleRegion["Liberation: Destroy mex (Sera)"] = rule
    rule = (Has("Sinnve")) & (Has("Ia-atha") | Has("Ia-istle") | Has("Ialla"))
    TheCompleteListOfRulesForEverySingleRegion["Liberation: Destroy UEF defences (Sera)"] = rule
    rule = (Has("Sinnve")) & (Has("Ia-atha") | Has("Ia-istle") | Has("Ialla"))
    TheCompleteListOfRulesForEverySingleRegion["Liberation: Destroy UEF patrols (Sera)"] = rule
    rule = (Has("Sinnve")) & (Has("Ia-atha") | Has("Ia-istle") | Has("Ialla"))
    TheCompleteListOfRulesForEverySingleRegion["Liberation: Destroy UEF base defenders (Sera)"] = rule
    rule = (Has("Sinnve")) & (Has("Ia-atha") | Has("Ia-istle") | Has("Ialla"))
    TheCompleteListOfRulesForEverySingleRegion["Liberation: Destroy UEF base (Sera)"] = rule
    rule = (Has("Sinnve")) & (Has("Ia-atha") | Has("Ia-istle") | Has("Ialla"))
    TheCompleteListOfRulesForEverySingleRegion["Liberation: Kill Aeon Commander (Sera)"] = rule
    rule = (Has("Sinnve")) & (Has("Ia-atha") | Has("Ia-istle") | Has("Ialla"))
    TheCompleteListOfRulesForEverySingleRegion["Artifact: Destroy first village defenders (Sera)"] = rule
    rule = (Has("Sinnve")) & (Has("Ia-atha") | Has("Ia-istle") | Has("Ialla"))
    TheCompleteListOfRulesForEverySingleRegion["Artifact: Destroy first temple (Sera)"] = rule
    rule = (Has("Sinnve")) & (Has("Ia-atha") | Has("Ia-istle") | Has("Ialla"))
    TheCompleteListOfRulesForEverySingleRegion["Artifact: Protect first artifact (Sera)"] = rule
    rule = ((Has("Sinnve")) & (Has("Ia-atha") | Has("Ia-istle") | Has("Ialla"))) & (Has("Thaam"))
    TheCompleteListOfRulesForEverySingleRegion["Artifact: Find second artifact (Sera)"] = rule
    rule = (((Has("Sinnve")) & (Has("Ia-atha") | Has("Ia-istle") | Has("Ialla"))) & (Has("Thaam"))) & (Has("Ilshavoh") | Has("Yenzyne") | Has("Uttaushala"))
    TheCompleteListOfRulesForEverySingleRegion["Artifact: Destroy Aeon reinforcements (Sera)"] = rule
    rule = ((((Has("Sinnve")) & (Has("Ia-atha") | Has("Ia-istle") | Has("Ialla"))) & (Has("Thaam"))) & (Has("Ilshavoh") | Has("Yenzyne") | Has("Uttaushala"))) & (Has("Uttaushala") | Has("Sou-istle") | Has("Hau-esel") | Has("Uosioz") | Has("Sou-atha"))
    TheCompleteListOfRulesForEverySingleRegion["Artifact: Protect second artifact (Sera)"] = rule
    rule = ((((Has("Sinnve")) & (Has("Ia-atha") | Has("Ia-istle") | Has("Ialla"))) & (Has("Thaam"))) & (Has("Ilshavoh") | Has("Yenzyne") | Has("Uttaushala"))) & (Has("Uttaushala") | Has("Sou-istle") | Has("Hau-esel") | Has("Uosioz") | Has("Sou-atha"))
    TheCompleteListOfRulesForEverySingleRegion["Artifact: Defend from Aeon attack (Sera)"] = rule
    rule = ((((Has("Sinnve")) & (Has("Ia-atha") | Has("Ia-istle") | Has("Ialla"))) & (Has("Thaam"))) & (Has("Ilshavoh") | Has("Yenzyne") | Has("Uttaushala"))) & (Has("Uttaushala") | Has("Sou-istle") | Has("Hau-esel") | Has("Uosioz") | Has("Sou-atha"))
    TheCompleteListOfRulesForEverySingleRegion["Artifact: Destroy eastern base (Sera)"] = rule
    rule = (((((Has("Sinnve")) & (Has("Ia-atha") | Has("Ia-istle") | Has("Ialla"))) & (Has("Thaam"))) & (Has("Ilshavoh") | Has("Yenzyne") | Has("Uttaushala"))) & (Has("Uttaushala") | Has("Sou-istle") | Has("Hau-esel") | Has("Uosioz") | Has("Sou-atha"))) & (Has("Uashavoh") | Has("Ithalua") | Has("Vulthoo") | Has("Vish") | Has("Zthuthaam") | Has("Ythis"))
    TheCompleteListOfRulesForEverySingleRegion["Artifact: Destroy navy base (Sera)"] = rule
    rule = (((((Has("Sinnve")) & (Has("Ia-atha") | Has("Ia-istle") | Has("Ialla"))) & (Has("Thaam"))) & (Has("Ilshavoh") | Has("Yenzyne") | Has("Uttaushala"))) & (Has("Uttaushala") | Has("Sou-istle") | Has("Hau-esel") | Has("Uosioz") | Has("Sou-atha"))) & (Has("Uashavoh") | Has("Ithalua") | Has("Vulthoo") | Has("Vish") | Has("Zthuthaam") | Has("Ythis"))
    TheCompleteListOfRulesForEverySingleRegion["Artifact: Protect third artifact (Sera)"] = rule
    rule = (((((Has("Sinnve")) & (Has("Ia-atha") | Has("Ia-istle") | Has("Ialla"))) & (Has("Thaam"))) & (Has("Ilshavoh") | Has("Yenzyne") | Has("Uttaushala"))) & (Has("Uttaushala") | Has("Sou-istle") | Has("Hau-esel") | Has("Uosioz") | Has("Sou-atha"))) & (Has("Uashavoh") | Has("Ithalua") | Has("Vulthoo") | Has("Vish") | Has("Zthuthaam") | Has("Ythis"))
    TheCompleteListOfRulesForEverySingleRegion["Artifact: Kill Aeon Commander (optional) (Sera)"] = rule
    rule = (((((Has("Sinnve")) & (Has("Ia-atha") | Has("Ia-istle") | Has("Ialla"))) & (Has("Thaam"))) & (Has("Ilshavoh") | Has("Yenzyne") | Has("Uttaushala"))) & (Has("Uttaushala") | Has("Sou-istle") | Has("Hau-esel") | Has("Uosioz") | Has("Sou-atha"))) & (Has("Uashavoh") | Has("Ithalua") | Has("Vulthoo") | Has("Vish") | Has("Zthuthaam") | Has("Ythis"))
    TheCompleteListOfRulesForEverySingleRegion["Artifact: Kill Mach (Sera)"] = rule
    rule = (((((Has("Sinnve")) & (Has("Ia-atha") | Has("Ia-istle") | Has("Ialla"))) & (Has("Thaam"))) & (Has("Ilshavoh") | Has("Yenzyne") | Has("Uttaushala"))) & (Has("Uttaushala") | Has("Sou-istle") | Has("Hau-esel") | Has("Uosioz") | Has("Sou-atha"))) & (Has("Uashavoh") | Has("Ithalua") | Has("Vulthoo") | Has("Vish") | Has("Zthuthaam") | Has("Ythis"))
    TheCompleteListOfRulesForEverySingleRegion["Artifact: Go to Gate (Sera)"] = rule
    rule = ((((((Has("Sinnve")) & (Has("Ia-atha") | Has("Ia-istle") | Has("Ialla"))) & (Has("Thaam"))) & (Has("Ilshavoh") | Has("Yenzyne") | Has("Uttaushala"))) & (Has("Uttaushala") | Has("Sou-istle") | Has("Hau-esel") | Has("Uosioz") | Has("Sou-atha"))) & (Has("Uashavoh") | Has("Ithalua") | Has("Vulthoo") | Has("Vish") | Has("Zthuthaam") | Has("Ythis"))) & (Has("Sera T2 Mass Extractor") & Has("Sera T2 Generator"))
    TheCompleteListOfRulesForEverySingleRegion["Defrag: Protect York 18 (Sera)"] = rule
    rule = ((((((Has("Sinnve")) & (Has("Ia-atha") | Has("Ia-istle") | Has("Ialla"))) & (Has("Thaam"))) & (Has("Ilshavoh") | Has("Yenzyne") | Has("Uttaushala"))) & (Has("Uttaushala") | Has("Sou-istle") | Has("Hau-esel") | Has("Uosioz") | Has("Sou-atha"))) & (Has("Uashavoh") | Has("Ithalua") | Has("Vulthoo") | Has("Vish") | Has("Zthuthaam") | Has("Ythis"))) & (Has("Sera T2 Mass Extractor") & Has("Sera T2 Generator"))
    TheCompleteListOfRulesForEverySingleRegion["Defrag: Destroy western UEF base (Sera)"] = rule
    rule = ((((((Has("Sinnve")) & (Has("Ia-atha") | Has("Ia-istle") | Has("Ialla"))) & (Has("Thaam"))) & (Has("Ilshavoh") | Has("Yenzyne") | Has("Uttaushala"))) & (Has("Uttaushala") | Has("Sou-istle") | Has("Hau-esel") | Has("Uosioz") | Has("Sou-atha"))) & (Has("Uashavoh") | Has("Ithalua") | Has("Vulthoo") | Has("Vish") | Has("Zthuthaam") | Has("Ythis"))) & (Has("Sera T2 Mass Extractor") & Has("Sera T2 Generator"))
    TheCompleteListOfRulesForEverySingleRegion["Defrag: Destroy north-western UEF base (Sera)"] = rule
    rule = ((((((Has("Sinnve")) & (Has("Ia-atha") | Has("Ia-istle") | Has("Ialla"))) & (Has("Thaam"))) & (Has("Ilshavoh") | Has("Yenzyne") | Has("Uttaushala"))) & (Has("Uttaushala") | Has("Sou-istle") | Has("Hau-esel") | Has("Uosioz") | Has("Sou-atha"))) & (Has("Uashavoh") | Has("Ithalua") | Has("Vulthoo") | Has("Vish") | Has("Zthuthaam") | Has("Ythis"))) & (Has("Sera T2 Mass Extractor") & Has("Sera T2 Generator"))
    TheCompleteListOfRulesForEverySingleRegion["Defrag: Destroy northern UEF base (Sera)"] = rule
    rule = ((((((Has("Sinnve")) & (Has("Ia-atha") | Has("Ia-istle") | Has("Ialla"))) & (Has("Thaam"))) & (Has("Ilshavoh") | Has("Yenzyne") | Has("Uttaushala"))) & (Has("Uttaushala") | Has("Sou-istle") | Has("Hau-esel") | Has("Uosioz") | Has("Sou-atha"))) & (Has("Uashavoh") | Has("Ithalua") | Has("Vulthoo") | Has("Vish") | Has("Zthuthaam") | Has("Ythis"))) & (Has("Sera T2 Mass Extractor") & Has("Sera T2 Generator"))
    TheCompleteListOfRulesForEverySingleRegion["Defrag: Sink UEF cruiser (Sera)"] = rule
    rule = (((((((Has("Sinnve")) & (Has("Ia-atha") | Has("Ia-istle") | Has("Ialla"))) & (Has("Thaam"))) & (Has("Ilshavoh") | Has("Yenzyne") | Has("Uttaushala"))) & (Has("Uttaushala") | Has("Sou-istle") | Has("Hau-esel") | Has("Uosioz") | Has("Sou-atha"))) & (Has("Uashavoh") | Has("Ithalua") | Has("Vulthoo") | Has("Vish") | Has("Zthuthaam") | Has("Ythis"))) & (Has("Sera T2 Mass Extractor") & Has("Sera T2 Generator"))) & (Has("Iashavoh") | Has("Sinnatha"))
    TheCompleteListOfRulesForEverySingleRegion["Defrag: Destroy static artillery (Sera)"] = rule
    rule = (((((((Has("Sinnve")) & (Has("Ia-atha") | Has("Ia-istle") | Has("Ialla"))) & (Has("Thaam"))) & (Has("Ilshavoh") | Has("Yenzyne") | Has("Uttaushala"))) & (Has("Uttaushala") | Has("Sou-istle") | Has("Hau-esel") | Has("Uosioz") | Has("Sou-atha"))) & (Has("Uashavoh") | Has("Ithalua") | Has("Vulthoo") | Has("Vish") | Has("Zthuthaam") | Has("Ythis"))) & (Has("Sera T2 Mass Extractor") & Has("Sera T2 Generator"))) & (Has("Iashavoh") | Has("Sinnatha"))
    TheCompleteListOfRulesForEverySingleRegion["Defrag: Escort trucks (Sera)"] = rule
    rule = (((((((Has("Sinnve")) & (Has("Ia-atha") | Has("Ia-istle") | Has("Ialla"))) & (Has("Thaam"))) & (Has("Ilshavoh") | Has("Yenzyne") | Has("Uttaushala"))) & (Has("Uttaushala") | Has("Sou-istle") | Has("Hau-esel") | Has("Uosioz") | Has("Sou-atha"))) & (Has("Uashavoh") | Has("Ithalua") | Has("Vulthoo") | Has("Vish") | Has("Zthuthaam") | Has("Ythis"))) & (Has("Sera T2 Mass Extractor") & Has("Sera T2 Generator"))) & (Has("Iashavoh") | Has("Sinnatha"))
    TheCompleteListOfRulesForEverySingleRegion["Defrag: Escort ALL trucks (optional) (Sera)"] = rule
    rule = (((((((Has("Sinnve")) & (Has("Ia-atha") | Has("Ia-istle") | Has("Ialla"))) & (Has("Thaam"))) & (Has("Ilshavoh") | Has("Yenzyne") | Has("Uttaushala"))) & (Has("Uttaushala") | Has("Sou-istle") | Has("Hau-esel") | Has("Uosioz") | Has("Sou-atha"))) & (Has("Uashavoh") | Has("Ithalua") | Has("Vulthoo") | Has("Vish") | Has("Zthuthaam") | Has("Ythis"))) & (Has("Sera T2 Mass Extractor") & Has("Sera T2 Generator"))) & (Has("Iashavoh") | Has("Sinnatha"))
    TheCompleteListOfRulesForEverySingleRegion["Defrag: Optional objective  (optional) (Sera)"] = rule
    rule = (((((((Has("Sinnve")) & (Has("Ia-atha") | Has("Ia-istle") | Has("Ialla"))) & (Has("Thaam"))) & (Has("Ilshavoh") | Has("Yenzyne") | Has("Uttaushala"))) & (Has("Uttaushala") | Has("Sou-istle") | Has("Hau-esel") | Has("Uosioz") | Has("Sou-atha"))) & (Has("Uashavoh") | Has("Ithalua") | Has("Vulthoo") | Has("Vish") | Has("Zthuthaam") | Has("Ythis"))) & (Has("Sera T2 Mass Extractor") & Has("Sera T2 Generator"))) & (Has("Iashavoh") | Has("Sinnatha"))
    TheCompleteListOfRulesForEverySingleRegion["Defrag: Kill UEF Commander (Sera)"] = rule
    rule = ((((((((Has("Sinnve")) & (Has("Ia-atha") | Has("Ia-istle") | Has("Ialla"))) & (Has("Thaam"))) & (Has("Ilshavoh") | Has("Yenzyne") | Has("Uttaushala"))) & (Has("Uttaushala") | Has("Sou-istle") | Has("Hau-esel") | Has("Uosioz") | Has("Sou-atha"))) & (Has("Uashavoh") | Has("Ithalua") | Has("Vulthoo") | Has("Vish") | Has("Zthuthaam") | Has("Ythis"))) & (Has("Sera T2 Mass Extractor") & Has("Sera T2 Generator"))) & (Has("Iashavoh") | Has("Sinnatha"))) & (Has("Uashavoh") | Has("Ithalua"))
    TheCompleteListOfRulesForEverySingleRegion["Mainframe Tango: Defeat Aeon Commander (Sera)"] = rule
    rule = ((((((((Has("Sinnve")) & (Has("Ia-atha") | Has("Ia-istle") | Has("Ialla"))) & (Has("Thaam"))) & (Has("Ilshavoh") | Has("Yenzyne") | Has("Uttaushala"))) & (Has("Uttaushala") | Has("Sou-istle") | Has("Hau-esel") | Has("Uosioz") | Has("Sou-atha"))) & (Has("Uashavoh") | Has("Ithalua") | Has("Vulthoo") | Has("Vish") | Has("Zthuthaam") | Has("Ythis"))) & (Has("Sera T2 Mass Extractor") & Has("Sera T2 Generator"))) & (Has("Iashavoh") | Has("Sinnatha"))) & (Has("Uashavoh") | Has("Ithalua"))
    TheCompleteListOfRulesForEverySingleRegion["Mainframe Tango: Capture Network Node (Sera)"] = rule
    rule = ((((((((Has("Sinnve")) & (Has("Ia-atha") | Has("Ia-istle") | Has("Ialla"))) & (Has("Thaam"))) & (Has("Ilshavoh") | Has("Yenzyne") | Has("Uttaushala"))) & (Has("Uttaushala") | Has("Sou-istle") | Has("Hau-esel") | Has("Uosioz") | Has("Sou-atha"))) & (Has("Uashavoh") | Has("Ithalua") | Has("Vulthoo") | Has("Vish") | Has("Zthuthaam") | Has("Ythis"))) & (Has("Sera T2 Mass Extractor") & Has("Sera T2 Generator"))) & (Has("Iashavoh") | Has("Sinnatha"))) & (Has("Uashavoh") | Has("Ithalua"))
    TheCompleteListOfRulesForEverySingleRegion["Mainframe Tango: Save Network Node (Sera)"] = rule
    rule = ((((((((Has("Sinnve")) & (Has("Ia-atha") | Has("Ia-istle") | Has("Ialla"))) & (Has("Thaam"))) & (Has("Ilshavoh") | Has("Yenzyne") | Has("Uttaushala"))) & (Has("Uttaushala") | Has("Sou-istle") | Has("Hau-esel") | Has("Uosioz") | Has("Sou-atha"))) & (Has("Uashavoh") | Has("Ithalua") | Has("Vulthoo") | Has("Vish") | Has("Zthuthaam") | Has("Ythis"))) & (Has("Sera T2 Mass Extractor") & Has("Sera T2 Generator"))) & (Has("Iashavoh") | Has("Sinnatha"))) & (Has("Uashavoh") | Has("Ithalua"))
    TheCompleteListOfRulesForEverySingleRegion["Mainframe Tango: Save 80% civilian buildings (optional) (Sera)"] = rule
    rule = ((((((((Has("Sinnve")) & (Has("Ia-atha") | Has("Ia-istle") | Has("Ialla"))) & (Has("Thaam"))) & (Has("Ilshavoh") | Has("Yenzyne") | Has("Uttaushala"))) & (Has("Uttaushala") | Has("Sou-istle") | Has("Hau-esel") | Has("Uosioz") | Has("Sou-atha"))) & (Has("Uashavoh") | Has("Ithalua") | Has("Vulthoo") | Has("Vish") | Has("Zthuthaam") | Has("Ythis"))) & (Has("Sera T2 Mass Extractor") & Has("Sera T2 Generator"))) & (Has("Iashavoh") | Has("Sinnatha"))) & (Has("Uashavoh") | Has("Ithalua"))
    TheCompleteListOfRulesForEverySingleRegion["Mainframe Tango: Survive attacks (Sera)"] = rule
    rule = ((((((((Has("Sinnve")) & (Has("Ia-atha") | Has("Ia-istle") | Has("Ialla"))) & (Has("Thaam"))) & (Has("Ilshavoh") | Has("Yenzyne") | Has("Uttaushala"))) & (Has("Uttaushala") | Has("Sou-istle") | Has("Hau-esel") | Has("Uosioz") | Has("Sou-atha"))) & (Has("Uashavoh") | Has("Ithalua") | Has("Vulthoo") | Has("Vish") | Has("Zthuthaam") | Has("Ythis"))) & (Has("Sera T2 Mass Extractor") & Has("Sera T2 Generator"))) & (Has("Iashavoh") | Has("Sinnatha"))) & (Has("Uashavoh") | Has("Ithalua"))
    TheCompleteListOfRulesForEverySingleRegion["Mainframe Tango: Capture northeast node (Sera)"] = rule
    rule = ((((((((Has("Sinnve")) & (Has("Ia-atha") | Has("Ia-istle") | Has("Ialla"))) & (Has("Thaam"))) & (Has("Ilshavoh") | Has("Yenzyne") | Has("Uttaushala"))) & (Has("Uttaushala") | Has("Sou-istle") | Has("Hau-esel") | Has("Uosioz") | Has("Sou-atha"))) & (Has("Uashavoh") | Has("Ithalua") | Has("Vulthoo") | Has("Vish") | Has("Zthuthaam") | Has("Ythis"))) & (Has("Sera T2 Mass Extractor") & Has("Sera T2 Generator"))) & (Has("Iashavoh") | Has("Sinnatha"))) & (Has("Uashavoh") | Has("Ithalua"))
    TheCompleteListOfRulesForEverySingleRegion["Mainframe Tango: Capture northwest node (Sera)"] = rule
    rule = ((((((((Has("Sinnve")) & (Has("Ia-atha") | Has("Ia-istle") | Has("Ialla"))) & (Has("Thaam"))) & (Has("Ilshavoh") | Has("Yenzyne") | Has("Uttaushala"))) & (Has("Uttaushala") | Has("Sou-istle") | Has("Hau-esel") | Has("Uosioz") | Has("Sou-atha"))) & (Has("Uashavoh") | Has("Ithalua") | Has("Vulthoo") | Has("Vish") | Has("Zthuthaam") | Has("Ythis"))) & (Has("Sera T2 Mass Extractor") & Has("Sera T2 Generator"))) & (Has("Iashavoh") | Has("Sinnatha"))) & (Has("Uashavoh") | Has("Ithalua"))
    TheCompleteListOfRulesForEverySingleRegion["Mainframe Tango: Do not attack main Aeon base (Sera)"] = rule
    rule = ((((((((Has("Sinnve")) & (Has("Ia-atha") | Has("Ia-istle") | Has("Ialla"))) & (Has("Thaam"))) & (Has("Ilshavoh") | Has("Yenzyne") | Has("Uttaushala"))) & (Has("Uttaushala") | Has("Sou-istle") | Has("Hau-esel") | Has("Uosioz") | Has("Sou-atha"))) & (Has("Uashavoh") | Has("Ithalua") | Has("Vulthoo") | Has("Vish") | Has("Zthuthaam") | Has("Ythis"))) & (Has("Sera T2 Mass Extractor") & Has("Sera T2 Generator"))) & (Has("Iashavoh") | Has("Sinnatha"))) & (Has("Uashavoh") | Has("Ithalua"))
    TheCompleteListOfRulesForEverySingleRegion["Mainframe Tango: Kill Aeon Commander (Sera)"] = rule
    rule = (((((((((Has("Sinnve")) & (Has("Ia-atha") | Has("Ia-istle") | Has("Ialla"))) & (Has("Thaam"))) & (Has("Ilshavoh") | Has("Yenzyne") | Has("Uttaushala"))) & (Has("Uttaushala") | Has("Sou-istle") | Has("Hau-esel") | Has("Uosioz") | Has("Sou-atha"))) & (Has("Uashavoh") | Has("Ithalua") | Has("Vulthoo") | Has("Vish") | Has("Zthuthaam") | Has("Ythis"))) & (Has("Sera T2 Mass Extractor") & Has("Sera T2 Generator"))) & (Has("Iashavoh") | Has("Sinnatha"))) & (Has("Uashavoh") | Has("Ithalua"))) & (Has("Sera T3 Mass Extractor") & Has("Uya-iya") & (Has("Othuum") | Has("Uyanah") | Has("Ythotha") | Has("Ahwassa") | Has("Yolona Oss") | Has("Ythis") | Has("Hovatham") | Has("Hastue") | Has("Sinntha")))
    TheCompleteListOfRulesForEverySingleRegion["Unlock: Destroy UEF generators (Sera)"] = rule
    rule = ((((((((((Has("Sinnve")) & (Has("Ia-atha") | Has("Ia-istle") | Has("Ialla"))) & (Has("Thaam"))) & (Has("Ilshavoh") | Has("Yenzyne") | Has("Uttaushala"))) & (Has("Uttaushala") | Has("Sou-istle") | Has("Hau-esel") | Has("Uosioz") | Has("Sou-atha"))) & (Has("Uashavoh") | Has("Ithalua") | Has("Vulthoo") | Has("Vish") | Has("Zthuthaam") | Has("Ythis"))) & (Has("Sera T2 Mass Extractor") & Has("Sera T2 Generator"))) & (Has("Iashavoh") | Has("Sinnatha"))) & (Has("Uashavoh") | Has("Ithalua"))) & (Has("Sera T3 Mass Extractor") & Has("Uya-iya") & (Has("Othuum") | Has("Uyanah") | Has("Ythotha") | Has("Ahwassa") | Has("Yolona Oss") | Has("Ythis") | Has("Hovatham") | Has("Hastue") | Has("Sinntha")))) & (Has("Ithalua"))
    TheCompleteListOfRulesForEverySingleRegion["Unlock: Destroy UEF shipyards (optional) (Sera)"] = rule
    rule = ((((((((((Has("Sinnve")) & (Has("Ia-atha") | Has("Ia-istle") | Has("Ialla"))) & (Has("Thaam"))) & (Has("Ilshavoh") | Has("Yenzyne") | Has("Uttaushala"))) & (Has("Uttaushala") | Has("Sou-istle") | Has("Hau-esel") | Has("Uosioz") | Has("Sou-atha"))) & (Has("Uashavoh") | Has("Ithalua") | Has("Vulthoo") | Has("Vish") | Has("Zthuthaam") | Has("Ythis"))) & (Has("Sera T2 Mass Extractor") & Has("Sera T2 Generator"))) & (Has("Iashavoh") | Has("Sinnatha"))) & (Has("Uashavoh") | Has("Ithalua"))) & (Has("Sera T3 Mass Extractor") & Has("Uya-iya") & (Has("Othuum") | Has("Uyanah") | Has("Ythotha") | Has("Ahwassa") | Has("Yolona Oss") | Has("Ythis") | Has("Hovatham") | Has("Hastue") | Has("Sinntha")))) & (Has("Ithalua"))
    TheCompleteListOfRulesForEverySingleRegion["Unlock: Destroy UEF radars (Sera)"] = rule
    rule = (((((((((((Has("Sinnve")) & (Has("Ia-atha") | Has("Ia-istle") | Has("Ialla"))) & (Has("Thaam"))) & (Has("Ilshavoh") | Has("Yenzyne") | Has("Uttaushala"))) & (Has("Uttaushala") | Has("Sou-istle") | Has("Hau-esel") | Has("Uosioz") | Has("Sou-atha"))) & (Has("Uashavoh") | Has("Ithalua") | Has("Vulthoo") | Has("Vish") | Has("Zthuthaam") | Has("Ythis"))) & (Has("Sera T2 Mass Extractor") & Has("Sera T2 Generator"))) & (Has("Iashavoh") | Has("Sinnatha"))) & (Has("Uashavoh") | Has("Ithalua"))) & (Has("Sera T3 Mass Extractor") & Has("Uya-iya") & (Has("Othuum") | Has("Uyanah") | Has("Ythotha") | Has("Ahwassa") | Has("Yolona Oss") | Has("Ythis") | Has("Hovatham") | Has("Hastue") | Has("Sinntha")))) & (Has("Ithalua"))) & (Has("Vishala"))
    TheCompleteListOfRulesForEverySingleRegion["Unlock: Go to Hex5 (Sera)"] = rule
    rule = ((((((((((((Has("Sinnve")) & (Has("Ia-atha") | Has("Ia-istle") | Has("Ialla"))) & (Has("Thaam"))) & (Has("Ilshavoh") | Has("Yenzyne") | Has("Uttaushala"))) & (Has("Uttaushala") | Has("Sou-istle") | Has("Hau-esel") | Has("Uosioz") | Has("Sou-atha"))) & (Has("Uashavoh") | Has("Ithalua") | Has("Vulthoo") | Has("Vish") | Has("Zthuthaam") | Has("Ythis"))) & (Has("Sera T2 Mass Extractor") & Has("Sera T2 Generator"))) & (Has("Iashavoh") | Has("Sinnatha"))) & (Has("Uashavoh") | Has("Ithalua"))) & (Has("Sera T3 Mass Extractor") & Has("Uya-iya") & (Has("Othuum") | Has("Uyanah") | Has("Ythotha") | Has("Ahwassa") | Has("Yolona Oss") | Has("Ythis") | Has("Hovatham") | Has("Hastue") | Has("Sinntha")))) & (Has("Ithalua"))) & (Has("Vishala"))) & (Has("Iazyne") | Has("Uyanah") | Has("Iathu-ioz"))
    TheCompleteListOfRulesForEverySingleRegion["Unlock: Defend from heavy gunships (Sera)"] = rule
    rule = ((((((((((((Has("Sinnve")) & (Has("Ia-atha") | Has("Ia-istle") | Has("Ialla"))) & (Has("Thaam"))) & (Has("Ilshavoh") | Has("Yenzyne") | Has("Uttaushala"))) & (Has("Uttaushala") | Has("Sou-istle") | Has("Hau-esel") | Has("Uosioz") | Has("Sou-atha"))) & (Has("Uashavoh") | Has("Ithalua") | Has("Vulthoo") | Has("Vish") | Has("Zthuthaam") | Has("Ythis"))) & (Has("Sera T2 Mass Extractor") & Has("Sera T2 Generator"))) & (Has("Iashavoh") | Has("Sinnatha"))) & (Has("Uashavoh") | Has("Ithalua"))) & (Has("Sera T3 Mass Extractor") & Has("Uya-iya") & (Has("Othuum") | Has("Uyanah") | Has("Ythotha") | Has("Ahwassa") | Has("Yolona Oss") | Has("Ythis") | Has("Hovatham") | Has("Hastue") | Has("Sinntha")))) & (Has("Ithalua"))) & (Has("Vishala"))) & (Has("Iazyne") | Has("Uyanah") | Has("Iathu-ioz"))
    TheCompleteListOfRulesForEverySingleRegion["Unlock: Infect UEF landing pad (optional) (Sera)"] = rule
    rule = ((((((((((((Has("Sinnve")) & (Has("Ia-atha") | Has("Ia-istle") | Has("Ialla"))) & (Has("Thaam"))) & (Has("Ilshavoh") | Has("Yenzyne") | Has("Uttaushala"))) & (Has("Uttaushala") | Has("Sou-istle") | Has("Hau-esel") | Has("Uosioz") | Has("Sou-atha"))) & (Has("Uashavoh") | Has("Ithalua") | Has("Vulthoo") | Has("Vish") | Has("Zthuthaam") | Has("Ythis"))) & (Has("Sera T2 Mass Extractor") & Has("Sera T2 Generator"))) & (Has("Iashavoh") | Has("Sinnatha"))) & (Has("Uashavoh") | Has("Ithalua"))) & (Has("Sera T3 Mass Extractor") & Has("Uya-iya") & (Has("Othuum") | Has("Uyanah") | Has("Ythotha") | Has("Ahwassa") | Has("Yolona Oss") | Has("Ythis") | Has("Hovatham") | Has("Hastue") | Has("Sinntha")))) & (Has("Ithalua"))) & (Has("Vishala"))) & (Has("Iazyne") | Has("Uyanah") | Has("Iathu-ioz"))
    TheCompleteListOfRulesForEverySingleRegion["Unlock: This will be retconned later (Sera)"] = rule
    rule = ((((((((((((Has("Sinnve")) & (Has("Ia-atha") | Has("Ia-istle") | Has("Ialla"))) & (Has("Thaam"))) & (Has("Ilshavoh") | Has("Yenzyne") | Has("Uttaushala"))) & (Has("Uttaushala") | Has("Sou-istle") | Has("Hau-esel") | Has("Uosioz") | Has("Sou-atha"))) & (Has("Uashavoh") | Has("Ithalua") | Has("Vulthoo") | Has("Vish") | Has("Zthuthaam") | Has("Ythis"))) & (Has("Sera T2 Mass Extractor") & Has("Sera T2 Generator"))) & (Has("Iashavoh") | Has("Sinnatha"))) & (Has("Uashavoh") | Has("Ithalua"))) & (Has("Sera T3 Mass Extractor") & Has("Uya-iya") & (Has("Othuum") | Has("Uyanah") | Has("Ythotha") | Has("Ahwassa") | Has("Yolona Oss") | Has("Ythis") | Has("Hovatham") | Has("Hastue") | Has("Sinntha")))) & (Has("Ithalua"))) & (Has("Vishala"))) & (Has("Iazyne") | Has("Uyanah") | Has("Iathu-ioz"))
    TheCompleteListOfRulesForEverySingleRegion["Unlock: Kill UEF Commander (Sera)"] = rule
    rule = ((((((((((((Has("Sinnve")) & (Has("Ia-atha") | Has("Ia-istle") | Has("Ialla"))) & (Has("Thaam"))) & (Has("Ilshavoh") | Has("Yenzyne") | Has("Uttaushala"))) & (Has("Uttaushala") | Has("Sou-istle") | Has("Hau-esel") | Has("Uosioz") | Has("Sou-atha"))) & (Has("Uashavoh") | Has("Ithalua") | Has("Vulthoo") | Has("Vish") | Has("Zthuthaam") | Has("Ythis"))) & (Has("Sera T2 Mass Extractor") & Has("Sera T2 Generator"))) & (Has("Iashavoh") | Has("Sinnatha"))) & (Has("Uashavoh") | Has("Ithalua"))) & (Has("Sera T3 Mass Extractor") & Has("Uya-iya") & (Has("Othuum") | Has("Uyanah") | Has("Ythotha") | Has("Ahwassa") | Has("Yolona Oss") | Has("Ythis") | Has("Hovatham") | Has("Hastue") | Has("Sinntha")))) & (Has("Ithalua"))) & (Has("Vishala"))) & (Has("Iazyne") | Has("Uyanah") | Has("Iathu-ioz"))
    TheCompleteListOfRulesForEverySingleRegion["Freedom: Destroy CZAR (Sera)"] = rule
    rule = (((((((((((((Has("Sinnve")) & (Has("Ia-atha") | Has("Ia-istle") | Has("Ialla"))) & (Has("Thaam"))) & (Has("Ilshavoh") | Has("Yenzyne") | Has("Uttaushala"))) & (Has("Uttaushala") | Has("Sou-istle") | Has("Hau-esel") | Has("Uosioz") | Has("Sou-atha"))) & (Has("Uashavoh") | Has("Ithalua") | Has("Vulthoo") | Has("Vish") | Has("Zthuthaam") | Has("Ythis"))) & (Has("Sera T2 Mass Extractor") & Has("Sera T2 Generator"))) & (Has("Iashavoh") | Has("Sinnatha"))) & (Has("Uashavoh") | Has("Ithalua"))) & (Has("Sera T3 Mass Extractor") & Has("Uya-iya") & (Has("Othuum") | Has("Uyanah") | Has("Ythotha") | Has("Ahwassa") | Has("Yolona Oss") | Has("Ythis") | Has("Hovatham") | Has("Hastue") | Has("Sinntha")))) & (Has("Ithalua"))) & (Has("Vishala"))) & (Has("Iazyne") | Has("Uyanah") | Has("Iathu-ioz"))) & (Has("Aezthu-uhthe"))
    TheCompleteListOfRulesForEverySingleRegion["Freedom: Build Quantum Gate (Sera)"] = rule
    rule = ((((((((((((((Has("Sinnve")) & (Has("Ia-atha") | Has("Ia-istle") | Has("Ialla"))) & (Has("Thaam"))) & (Has("Ilshavoh") | Has("Yenzyne") | Has("Uttaushala"))) & (Has("Uttaushala") | Has("Sou-istle") | Has("Hau-esel") | Has("Uosioz") | Has("Sou-atha"))) & (Has("Uashavoh") | Has("Ithalua") | Has("Vulthoo") | Has("Vish") | Has("Zthuthaam") | Has("Ythis"))) & (Has("Sera T2 Mass Extractor") & Has("Sera T2 Generator"))) & (Has("Iashavoh") | Has("Sinnatha"))) & (Has("Uashavoh") | Has("Ithalua"))) & (Has("Sera T3 Mass Extractor") & Has("Uya-iya") & (Has("Othuum") | Has("Uyanah") | Has("Ythotha") | Has("Ahwassa") | Has("Yolona Oss") | Has("Ythis") | Has("Hovatham") | Has("Hastue") | Has("Sinntha")))) & (Has("Ithalua"))) & (Has("Vishala"))) & (Has("Iazyne") | Has("Uyanah") | Has("Iathu-ioz"))) & (Has("Aezthu-uhthe"))) & (Has("Othuum") | Has("Othuum") | Has("Uyanah") | Has("Ythotha") | Has("Ahwassa") | Has("Sinntha"))
    TheCompleteListOfRulesForEverySingleRegion["Freedom: Download Quantum Virus (Sera)"] = rule
    rule = ((((((((((((((Has("Sinnve")) & (Has("Ia-atha") | Has("Ia-istle") | Has("Ialla"))) & (Has("Thaam"))) & (Has("Ilshavoh") | Has("Yenzyne") | Has("Uttaushala"))) & (Has("Uttaushala") | Has("Sou-istle") | Has("Hau-esel") | Has("Uosioz") | Has("Sou-atha"))) & (Has("Uashavoh") | Has("Ithalua") | Has("Vulthoo") | Has("Vish") | Has("Zthuthaam") | Has("Ythis"))) & (Has("Sera T2 Mass Extractor") & Has("Sera T2 Generator"))) & (Has("Iashavoh") | Has("Sinnatha"))) & (Has("Uashavoh") | Has("Ithalua"))) & (Has("Sera T3 Mass Extractor") & Has("Uya-iya") & (Has("Othuum") | Has("Uyanah") | Has("Ythotha") | Has("Ahwassa") | Has("Yolona Oss") | Has("Ythis") | Has("Hovatham") | Has("Hastue") | Has("Sinntha")))) & (Has("Ithalua"))) & (Has("Vishala"))) & (Has("Iazyne") | Has("Uyanah") | Has("Iathu-ioz"))) & (Has("Aezthu-uhthe"))) & (Has("Othuum") | Has("Othuum") | Has("Uyanah") | Has("Ythotha") | Has("Ahwassa") | Has("Sinntha"))
    TheCompleteListOfRulesForEverySingleRegion["Freedom: Capture Black Sun control center (Sera)"] = rule
    rule = ((((((((((((((Has("Sinnve")) & (Has("Ia-atha") | Has("Ia-istle") | Has("Ialla"))) & (Has("Thaam"))) & (Has("Ilshavoh") | Has("Yenzyne") | Has("Uttaushala"))) & (Has("Uttaushala") | Has("Sou-istle") | Has("Hau-esel") | Has("Uosioz") | Has("Sou-atha"))) & (Has("Uashavoh") | Has("Ithalua") | Has("Vulthoo") | Has("Vish") | Has("Zthuthaam") | Has("Ythis"))) & (Has("Sera T2 Mass Extractor") & Has("Sera T2 Generator"))) & (Has("Iashavoh") | Has("Sinnatha"))) & (Has("Uashavoh") | Has("Ithalua"))) & (Has("Sera T3 Mass Extractor") & Has("Uya-iya") & (Has("Othuum") | Has("Uyanah") | Has("Ythotha") | Has("Ahwassa") | Has("Yolona Oss") | Has("Ythis") | Has("Hovatham") | Has("Hastue") | Has("Sinntha")))) & (Has("Ithalua"))) & (Has("Vishala"))) & (Has("Iazyne") | Has("Uyanah") | Has("Iathu-ioz"))) & (Has("Aezthu-uhthe"))) & (Has("Othuum") | Has("Othuum") | Has("Uyanah") | Has("Ythotha") | Has("Ahwassa") | Has("Sinntha"))
    TheCompleteListOfRulesForEverySingleRegion["Freedom: Capture Black Sun (Sera)"] = rule
    rule = ((((((((((((((Has("Sinnve")) & (Has("Ia-atha") | Has("Ia-istle") | Has("Ialla"))) & (Has("Thaam"))) & (Has("Ilshavoh") | Has("Yenzyne") | Has("Uttaushala"))) & (Has("Uttaushala") | Has("Sou-istle") | Has("Hau-esel") | Has("Uosioz") | Has("Sou-atha"))) & (Has("Uashavoh") | Has("Ithalua") | Has("Vulthoo") | Has("Vish") | Has("Zthuthaam") | Has("Ythis"))) & (Has("Sera T2 Mass Extractor") & Has("Sera T2 Generator"))) & (Has("Iashavoh") | Has("Sinnatha"))) & (Has("Uashavoh") | Has("Ithalua"))) & (Has("Sera T3 Mass Extractor") & Has("Uya-iya") & (Has("Othuum") | Has("Uyanah") | Has("Ythotha") | Has("Ahwassa") | Has("Yolona Oss") | Has("Ythis") | Has("Hovatham") | Has("Hastue") | Has("Sinntha")))) & (Has("Ithalua"))) & (Has("Vishala"))) & (Has("Iazyne") | Has("Uyanah") | Has("Iathu-ioz"))) & (Has("Aezthu-uhthe"))) & (Has("Othuum") | Has("Othuum") | Has("Uyanah") | Has("Ythotha") | Has("Ahwassa") | Has("Sinntha"))
    TheCompleteListOfRulesForEverySingleRegion["Freedom: Shoot Black Sun (Sera)"] = rule

    ListOfUsedRegions = []
    for i in range(Width):
        for j in range(Height):
            for c in range(len(TotalListOfTtotallyLevels[THE_GRID[i][j]])):
                ListOfUsedRegions.append(DictionaryOfRegions[TotalListOfTtotallyLevels[THE_GRID[i][j]][c]])
    world.multiworld.regions += ListOfUsedRegions

    if "Liberation (UEF)" in AllLevelsListToCheckRegionCreation:
        LiberationUEF0.connect(LiberationUEF1, "e0")
    if "Liberation (UEF)" in AllLevelsListToCheckRegionCreation:
        LiberationUEF1.connect(LiberationUEF2, "e1")
    if "Liberation (UEF)" in AllLevelsListToCheckRegionCreation:
        LiberationUEF2.connect(LiberationUEF3, "e2", TheCompleteListOfRulesForEverySingleRegion["Liberation: Build bombers (UEF)"])
    if "Liberation (UEF)" in AllLevelsListToCheckRegionCreation:
        LiberationUEF3.connect(LiberationUEF4, "e3", TheCompleteListOfRulesForEverySingleRegion["Liberation: Destroy radar defenders (UEF)"])
    if "Liberation (UEF)" in AllLevelsListToCheckRegionCreation:
        LiberationUEF4.connect(LiberationUEF5, "e4", TheCompleteListOfRulesForEverySingleRegion["Liberation: Capture radars (UEF)"])
    if "Liberation (UEF)" in AllLevelsListToCheckRegionCreation:
        LiberationUEF5.connect(LiberationUEF6, "e5", TheCompleteListOfRulesForEverySingleRegion["Liberation: Destroy mex (UEF)"])
    if "Liberation (UEF)" in AllLevelsListToCheckRegionCreation:
        LiberationUEF6.connect(LiberationUEF7, "e6", TheCompleteListOfRulesForEverySingleRegion["Liberation: Destroy UEF defences (UEF)"])
    if "Liberation (UEF)" in AllLevelsListToCheckRegionCreation:
        LiberationUEF7.connect(LiberationUEF8, "e7", TheCompleteListOfRulesForEverySingleRegion["Liberation: Destroy UEF patrols (UEF)"])
    if "Liberation (UEF)" in AllLevelsListToCheckRegionCreation:
        LiberationUEF8.connect(LiberationUEF9, "e8", TheCompleteListOfRulesForEverySingleRegion["Liberation: Destroy UEF base defenders (UEF)"])
    if "Liberation (UEF)" in AllLevelsListToCheckRegionCreation:
        LiberationUEF9.connect(LiberationUEF10, "e9", TheCompleteListOfRulesForEverySingleRegion["Liberation: Destroy UEF base (UEF)"])
    if "Liberation (UEF)" in AllLevelsListToCheckRegionCreation:
        LiberationUEF10.connect(LiberationUEF11, "e10", TheCompleteListOfRulesForEverySingleRegion["Liberation: Kill Aeon Commander (UEF)"])
    if "Artifact (UEF)" in AllLevelsListToCheckRegionCreation:
        ArtifactUEF0.connect(ArtifactUEF1, "e11", TheCompleteListOfRulesForEverySingleRegion["Artifact: Destroy first temple (UEF)"])
    if "Artifact (UEF)" in AllLevelsListToCheckRegionCreation:
        ArtifactUEF1.connect(ArtifactUEF2, "e12", TheCompleteListOfRulesForEverySingleRegion["Artifact: Protect first artifact (UEF)"])
    if "Artifact (UEF)" in AllLevelsListToCheckRegionCreation:
        ArtifactUEF2.connect(ArtifactUEF3, "e13", TheCompleteListOfRulesForEverySingleRegion["Artifact: Find second artifact (UEF)"])
    if "Artifact (UEF)" in AllLevelsListToCheckRegionCreation:
        ArtifactUEF3.connect(ArtifactUEF4, "e14", TheCompleteListOfRulesForEverySingleRegion["Artifact: Destroy Aeon reinforcements (UEF)"])
    if "Artifact (UEF)" in AllLevelsListToCheckRegionCreation:
        ArtifactUEF4.connect(ArtifactUEF5, "e15", TheCompleteListOfRulesForEverySingleRegion["Artifact: Protect second artifact (UEF)"])
    if "Artifact (UEF)" in AllLevelsListToCheckRegionCreation:
        ArtifactUEF5.connect(ArtifactUEF6, "e16", TheCompleteListOfRulesForEverySingleRegion["Artifact: Defend from Aeon attack (UEF)"])
    if "Artifact (UEF)" in AllLevelsListToCheckRegionCreation:
        ArtifactUEF6.connect(ArtifactUEF7, "e17", TheCompleteListOfRulesForEverySingleRegion["Artifact: Destroy eastern base (UEF)"])
    if "Artifact (UEF)" in AllLevelsListToCheckRegionCreation:
        ArtifactUEF7.connect(ArtifactUEF8, "e18", TheCompleteListOfRulesForEverySingleRegion["Artifact: Destroy navy base (UEF)"])
    if "Artifact (UEF)" in AllLevelsListToCheckRegionCreation:
        ArtifactUEF8.connect(ArtifactUEF9, "e19", TheCompleteListOfRulesForEverySingleRegion["Artifact: Protect third artifact (UEF)"])
    if "Artifact (UEF)" in AllLevelsListToCheckRegionCreation:
        ArtifactUEF9.connect(ArtifactUEF10, "e20", TheCompleteListOfRulesForEverySingleRegion["Artifact: Kill Aeon Commander (optional) (UEF)"])
    if "Artifact (UEF)" in AllLevelsListToCheckRegionCreation:
        ArtifactUEF10.connect(ArtifactUEF11, "e21", TheCompleteListOfRulesForEverySingleRegion["Artifact: Kill Mach (UEF)"])
    if "Artifact (UEF)" in AllLevelsListToCheckRegionCreation:
        ArtifactUEF11.connect(ArtifactUEF12, "e22", TheCompleteListOfRulesForEverySingleRegion["Artifact: Go to Gate (UEF)"])
    if "Defrag (UEF)" in AllLevelsListToCheckRegionCreation:
        DefragUEF0.connect(DefragUEF1, "e23", TheCompleteListOfRulesForEverySingleRegion["Defrag: Destroy western UEF base (UEF)"])
    if "Defrag (UEF)" in AllLevelsListToCheckRegionCreation:
        DefragUEF1.connect(DefragUEF2, "e24", TheCompleteListOfRulesForEverySingleRegion["Defrag: Destroy north-western UEF base (UEF)"])
    if "Defrag (UEF)" in AllLevelsListToCheckRegionCreation:
        DefragUEF2.connect(DefragUEF3, "e25", TheCompleteListOfRulesForEverySingleRegion["Defrag: Destroy northern UEF base (UEF)"])
    if "Defrag (UEF)" in AllLevelsListToCheckRegionCreation:
        DefragUEF3.connect(DefragUEF4, "e26", TheCompleteListOfRulesForEverySingleRegion["Defrag: Sink UEF cruiser (UEF)"])
    if "Defrag (UEF)" in AllLevelsListToCheckRegionCreation:
        DefragUEF4.connect(DefragUEF5, "e27", TheCompleteListOfRulesForEverySingleRegion["Defrag: Destroy static artillery (UEF)"])
    if "Defrag (UEF)" in AllLevelsListToCheckRegionCreation:
        DefragUEF5.connect(DefragUEF6, "e28", TheCompleteListOfRulesForEverySingleRegion["Defrag: Escort trucks (UEF)"])
    if "Defrag (UEF)" in AllLevelsListToCheckRegionCreation:
        DefragUEF6.connect(DefragUEF7, "e29", TheCompleteListOfRulesForEverySingleRegion["Defrag: Escort ALL trucks (optional) (UEF)"])
    if "Defrag (UEF)" in AllLevelsListToCheckRegionCreation:
        DefragUEF7.connect(DefragUEF8, "e30", TheCompleteListOfRulesForEverySingleRegion["Defrag: Optional objective  (optional) (UEF)"])
    if "Defrag (UEF)" in AllLevelsListToCheckRegionCreation:
        DefragUEF8.connect(DefragUEF9, "e31", TheCompleteListOfRulesForEverySingleRegion["Defrag: Kill UEF Commander (UEF)"])
    if "Mainframe Tango (UEF)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoUEF0.connect(MainframeTangoUEF1, "e32", TheCompleteListOfRulesForEverySingleRegion["Mainframe Tango: Capture Network Node (UEF)"])
    if "Mainframe Tango (UEF)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoUEF1.connect(MainframeTangoUEF2, "e33", TheCompleteListOfRulesForEverySingleRegion["Mainframe Tango: Save Network Node (UEF)"])
    if "Mainframe Tango (UEF)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoUEF2.connect(MainframeTangoUEF3, "e34", TheCompleteListOfRulesForEverySingleRegion["Mainframe Tango: Save 80% civilian buildings (optional) (UEF)"])
    if "Mainframe Tango (UEF)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoUEF3.connect(MainframeTangoUEF4, "e35", TheCompleteListOfRulesForEverySingleRegion["Mainframe Tango: Survive attacks (UEF)"])
    if "Mainframe Tango (UEF)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoUEF4.connect(MainframeTangoUEF5, "e36", TheCompleteListOfRulesForEverySingleRegion["Mainframe Tango: Capture northeast node (UEF)"])
    if "Mainframe Tango (UEF)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoUEF5.connect(MainframeTangoUEF6, "e37", TheCompleteListOfRulesForEverySingleRegion["Mainframe Tango: Capture northwest node (UEF)"])
    if "Mainframe Tango (UEF)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoUEF6.connect(MainframeTangoUEF7, "e38", TheCompleteListOfRulesForEverySingleRegion["Mainframe Tango: Do not attack main Aeon base (UEF)"])
    if "Mainframe Tango (UEF)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoUEF7.connect(MainframeTangoUEF8, "e39", TheCompleteListOfRulesForEverySingleRegion["Mainframe Tango: Kill Aeon Commander (UEF)"])
    if "Unlock (UEF)" in AllLevelsListToCheckRegionCreation:
        UnlockUEF0.connect(UnlockUEF1, "e40", TheCompleteListOfRulesForEverySingleRegion["Unlock: Destroy UEF shipyards (optional) (UEF)"])
    if "Unlock (UEF)" in AllLevelsListToCheckRegionCreation:
        UnlockUEF1.connect(UnlockUEF2, "e41", TheCompleteListOfRulesForEverySingleRegion["Unlock: Destroy UEF radars (UEF)"])
    if "Unlock (UEF)" in AllLevelsListToCheckRegionCreation:
        UnlockUEF2.connect(UnlockUEF3, "e42", TheCompleteListOfRulesForEverySingleRegion["Unlock: Go to Hex5 (UEF)"])
    if "Unlock (UEF)" in AllLevelsListToCheckRegionCreation:
        UnlockUEF3.connect(UnlockUEF4, "e43", TheCompleteListOfRulesForEverySingleRegion["Unlock: Defend from heavy gunships (UEF)"])
    if "Unlock (UEF)" in AllLevelsListToCheckRegionCreation:
        UnlockUEF4.connect(UnlockUEF5, "e44", TheCompleteListOfRulesForEverySingleRegion["Unlock: Infect UEF landing pad (optional) (UEF)"])
    if "Unlock (UEF)" in AllLevelsListToCheckRegionCreation:
        UnlockUEF5.connect(UnlockUEF6, "e45", TheCompleteListOfRulesForEverySingleRegion["Unlock: This will be retconned later (UEF)"])
    if "Unlock (UEF)" in AllLevelsListToCheckRegionCreation:
        UnlockUEF6.connect(UnlockUEF7, "e46", TheCompleteListOfRulesForEverySingleRegion["Unlock: Kill UEF Commander (UEF)"])
    if "Freedom (UEF)" in AllLevelsListToCheckRegionCreation:
        FreedomUEF0.connect(FreedomUEF1, "e47", TheCompleteListOfRulesForEverySingleRegion["Freedom: Build Quantum Gate (UEF)"])
    if "Freedom (UEF)" in AllLevelsListToCheckRegionCreation:
        FreedomUEF1.connect(FreedomUEF2, "e48", TheCompleteListOfRulesForEverySingleRegion["Freedom: Download Quantum Virus (UEF)"])
    if "Freedom (UEF)" in AllLevelsListToCheckRegionCreation:
        FreedomUEF2.connect(FreedomUEF3, "e49", TheCompleteListOfRulesForEverySingleRegion["Freedom: Capture Black Sun control center (UEF)"])
    if "Freedom (UEF)" in AllLevelsListToCheckRegionCreation:
        FreedomUEF3.connect(FreedomUEF4, "e50", TheCompleteListOfRulesForEverySingleRegion["Freedom: Capture Black Sun (UEF)"])
    if "Freedom (UEF)" in AllLevelsListToCheckRegionCreation:
        FreedomUEF4.connect(FreedomUEF5, "e51", TheCompleteListOfRulesForEverySingleRegion["Freedom: Shoot Black Sun (UEF)"])
    if "Liberation (Cybran)" in AllLevelsListToCheckRegionCreation:
        LiberationCybran0.connect(LiberationCybran1, "e52")
    if "Liberation (Cybran)" in AllLevelsListToCheckRegionCreation:
        LiberationCybran1.connect(LiberationCybran2, "e53")
    if "Liberation (Cybran)" in AllLevelsListToCheckRegionCreation:
        LiberationCybran2.connect(LiberationCybran3, "e54", TheCompleteListOfRulesForEverySingleRegion["Liberation: Build bombers (Cybran)"])
    if "Liberation (Cybran)" in AllLevelsListToCheckRegionCreation:
        LiberationCybran3.connect(LiberationCybran4, "e55", TheCompleteListOfRulesForEverySingleRegion["Liberation: Destroy radar defenders (Cybran)"])
    if "Liberation (Cybran)" in AllLevelsListToCheckRegionCreation:
        LiberationCybran4.connect(LiberationCybran5, "e56", TheCompleteListOfRulesForEverySingleRegion["Liberation: Capture radars (Cybran)"])
    if "Liberation (Cybran)" in AllLevelsListToCheckRegionCreation:
        LiberationCybran5.connect(LiberationCybran6, "e57", TheCompleteListOfRulesForEverySingleRegion["Liberation: Destroy mex (Cybran)"])
    if "Liberation (Cybran)" in AllLevelsListToCheckRegionCreation:
        LiberationCybran6.connect(LiberationCybran7, "e58", TheCompleteListOfRulesForEverySingleRegion["Liberation: Destroy UEF defences (Cybran)"])
    if "Liberation (Cybran)" in AllLevelsListToCheckRegionCreation:
        LiberationCybran7.connect(LiberationCybran8, "e59", TheCompleteListOfRulesForEverySingleRegion["Liberation: Destroy UEF patrols (Cybran)"])
    if "Liberation (Cybran)" in AllLevelsListToCheckRegionCreation:
        LiberationCybran8.connect(LiberationCybran9, "e60", TheCompleteListOfRulesForEverySingleRegion["Liberation: Destroy UEF base defenders (Cybran)"])
    if "Liberation (Cybran)" in AllLevelsListToCheckRegionCreation:
        LiberationCybran9.connect(LiberationCybran10, "e61", TheCompleteListOfRulesForEverySingleRegion["Liberation: Destroy UEF base (Cybran)"])
    if "Liberation (Cybran)" in AllLevelsListToCheckRegionCreation:
        LiberationCybran10.connect(LiberationCybran11, "e62", TheCompleteListOfRulesForEverySingleRegion["Liberation: Kill Aeon Commander (Cybran)"])
    if "Artifact (Cybran)" in AllLevelsListToCheckRegionCreation:
        ArtifactCybran0.connect(ArtifactCybran1, "e63", TheCompleteListOfRulesForEverySingleRegion["Artifact: Destroy first temple (Cybran)"])
    if "Artifact (Cybran)" in AllLevelsListToCheckRegionCreation:
        ArtifactCybran1.connect(ArtifactCybran2, "e64", TheCompleteListOfRulesForEverySingleRegion["Artifact: Protect first artifact (Cybran)"])
    if "Artifact (Cybran)" in AllLevelsListToCheckRegionCreation:
        ArtifactCybran2.connect(ArtifactCybran3, "e65", TheCompleteListOfRulesForEverySingleRegion["Artifact: Find second artifact (Cybran)"])
    if "Artifact (Cybran)" in AllLevelsListToCheckRegionCreation:
        ArtifactCybran3.connect(ArtifactCybran4, "e66", TheCompleteListOfRulesForEverySingleRegion["Artifact: Destroy Aeon reinforcements (Cybran)"])
    if "Artifact (Cybran)" in AllLevelsListToCheckRegionCreation:
        ArtifactCybran4.connect(ArtifactCybran5, "e67", TheCompleteListOfRulesForEverySingleRegion["Artifact: Protect second artifact (Cybran)"])
    if "Artifact (Cybran)" in AllLevelsListToCheckRegionCreation:
        ArtifactCybran5.connect(ArtifactCybran6, "e68", TheCompleteListOfRulesForEverySingleRegion["Artifact: Defend from Aeon attack (Cybran)"])
    if "Artifact (Cybran)" in AllLevelsListToCheckRegionCreation:
        ArtifactCybran6.connect(ArtifactCybran7, "e69", TheCompleteListOfRulesForEverySingleRegion["Artifact: Destroy eastern base (Cybran)"])
    if "Artifact (Cybran)" in AllLevelsListToCheckRegionCreation:
        ArtifactCybran7.connect(ArtifactCybran8, "e70", TheCompleteListOfRulesForEverySingleRegion["Artifact: Destroy navy base (Cybran)"])
    if "Artifact (Cybran)" in AllLevelsListToCheckRegionCreation:
        ArtifactCybran8.connect(ArtifactCybran9, "e71", TheCompleteListOfRulesForEverySingleRegion["Artifact: Protect third artifact (Cybran)"])
    if "Artifact (Cybran)" in AllLevelsListToCheckRegionCreation:
        ArtifactCybran9.connect(ArtifactCybran10, "e72", TheCompleteListOfRulesForEverySingleRegion["Artifact: Kill Aeon Commander (optional) (Cybran)"])
    if "Artifact (Cybran)" in AllLevelsListToCheckRegionCreation:
        ArtifactCybran10.connect(ArtifactCybran11, "e73", TheCompleteListOfRulesForEverySingleRegion["Artifact: Kill Mach (Cybran)"])
    if "Artifact (Cybran)" in AllLevelsListToCheckRegionCreation:
        ArtifactCybran11.connect(ArtifactCybran12, "e74", TheCompleteListOfRulesForEverySingleRegion["Artifact: Go to Gate (Cybran)"])
    if "Defrag (Cybran)" in AllLevelsListToCheckRegionCreation:
        DefragCybran0.connect(DefragCybran1, "e75", TheCompleteListOfRulesForEverySingleRegion["Defrag: Destroy western UEF base (Cybran)"])
    if "Defrag (Cybran)" in AllLevelsListToCheckRegionCreation:
        DefragCybran1.connect(DefragCybran2, "e76", TheCompleteListOfRulesForEverySingleRegion["Defrag: Destroy north-western UEF base (Cybran)"])
    if "Defrag (Cybran)" in AllLevelsListToCheckRegionCreation:
        DefragCybran2.connect(DefragCybran3, "e77", TheCompleteListOfRulesForEverySingleRegion["Defrag: Destroy northern UEF base (Cybran)"])
    if "Defrag (Cybran)" in AllLevelsListToCheckRegionCreation:
        DefragCybran3.connect(DefragCybran4, "e78", TheCompleteListOfRulesForEverySingleRegion["Defrag: Sink UEF cruiser (Cybran)"])
    if "Defrag (Cybran)" in AllLevelsListToCheckRegionCreation:
        DefragCybran4.connect(DefragCybran5, "e79", TheCompleteListOfRulesForEverySingleRegion["Defrag: Destroy static artillery (Cybran)"])
    if "Defrag (Cybran)" in AllLevelsListToCheckRegionCreation:
        DefragCybran5.connect(DefragCybran6, "e80", TheCompleteListOfRulesForEverySingleRegion["Defrag: Escort trucks (Cybran)"])
    if "Defrag (Cybran)" in AllLevelsListToCheckRegionCreation:
        DefragCybran6.connect(DefragCybran7, "e81", TheCompleteListOfRulesForEverySingleRegion["Defrag: Escort ALL trucks (optional) (Cybran)"])
    if "Defrag (Cybran)" in AllLevelsListToCheckRegionCreation:
        DefragCybran7.connect(DefragCybran8, "e82", TheCompleteListOfRulesForEverySingleRegion["Defrag: Optional objective  (optional) (Cybran)"])
    if "Defrag (Cybran)" in AllLevelsListToCheckRegionCreation:
        DefragCybran8.connect(DefragCybran9, "e83", TheCompleteListOfRulesForEverySingleRegion["Defrag: Kill UEF Commander (Cybran)"])
    if "Mainframe Tango (Cybran)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoCybran0.connect(MainframeTangoCybran1, "e84", TheCompleteListOfRulesForEverySingleRegion["Mainframe Tango: Capture Network Node (Cybran)"])
    if "Mainframe Tango (Cybran)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoCybran1.connect(MainframeTangoCybran2, "e85", TheCompleteListOfRulesForEverySingleRegion["Mainframe Tango: Save Network Node (Cybran)"])
    if "Mainframe Tango (Cybran)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoCybran2.connect(MainframeTangoCybran3, "e86", TheCompleteListOfRulesForEverySingleRegion["Mainframe Tango: Save 80% civilian buildings (optional) (Cybran)"])
    if "Mainframe Tango (Cybran)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoCybran3.connect(MainframeTangoCybran4, "e87", TheCompleteListOfRulesForEverySingleRegion["Mainframe Tango: Survive attacks (Cybran)"])
    if "Mainframe Tango (Cybran)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoCybran4.connect(MainframeTangoCybran5, "e88", TheCompleteListOfRulesForEverySingleRegion["Mainframe Tango: Capture northeast node (Cybran)"])
    if "Mainframe Tango (Cybran)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoCybran5.connect(MainframeTangoCybran6, "e89", TheCompleteListOfRulesForEverySingleRegion["Mainframe Tango: Capture northwest node (Cybran)"])
    if "Mainframe Tango (Cybran)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoCybran6.connect(MainframeTangoCybran7, "e90", TheCompleteListOfRulesForEverySingleRegion["Mainframe Tango: Do not attack main Aeon base (Cybran)"])
    if "Mainframe Tango (Cybran)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoCybran7.connect(MainframeTangoCybran8, "e91", TheCompleteListOfRulesForEverySingleRegion["Mainframe Tango: Kill Aeon Commander (Cybran)"])
    if "Unlock (Cybran)" in AllLevelsListToCheckRegionCreation:
        UnlockCybran0.connect(UnlockCybran1, "e92", TheCompleteListOfRulesForEverySingleRegion["Unlock: Destroy UEF shipyards (optional) (Cybran)"])
    if "Unlock (Cybran)" in AllLevelsListToCheckRegionCreation:
        UnlockCybran1.connect(UnlockCybran2, "e93", TheCompleteListOfRulesForEverySingleRegion["Unlock: Destroy UEF radars (Cybran)"])
    if "Unlock (Cybran)" in AllLevelsListToCheckRegionCreation:
        UnlockCybran2.connect(UnlockCybran3, "e94", TheCompleteListOfRulesForEverySingleRegion["Unlock: Go to Hex5 (Cybran)"])
    if "Unlock (Cybran)" in AllLevelsListToCheckRegionCreation:
        UnlockCybran3.connect(UnlockCybran4, "e95", TheCompleteListOfRulesForEverySingleRegion["Unlock: Defend from heavy gunships (Cybran)"])
    if "Unlock (Cybran)" in AllLevelsListToCheckRegionCreation:
        UnlockCybran4.connect(UnlockCybran5, "e96", TheCompleteListOfRulesForEverySingleRegion["Unlock: Infect UEF landing pad (optional) (Cybran)"])
    if "Unlock (Cybran)" in AllLevelsListToCheckRegionCreation:
        UnlockCybran5.connect(UnlockCybran6, "e97", TheCompleteListOfRulesForEverySingleRegion["Unlock: This will be retconned later (Cybran)"])
    if "Unlock (Cybran)" in AllLevelsListToCheckRegionCreation:
        UnlockCybran6.connect(UnlockCybran7, "e98", TheCompleteListOfRulesForEverySingleRegion["Unlock: Kill UEF Commander (Cybran)"])
    if "Freedom (Cybran)" in AllLevelsListToCheckRegionCreation:
        FreedomCybran0.connect(FreedomCybran1, "e99", TheCompleteListOfRulesForEverySingleRegion["Freedom: Build Quantum Gate (Cybran)"])
    if "Freedom (Cybran)" in AllLevelsListToCheckRegionCreation:
        FreedomCybran1.connect(FreedomCybran2, "e100", TheCompleteListOfRulesForEverySingleRegion["Freedom: Download Quantum Virus (Cybran)"])
    if "Freedom (Cybran)" in AllLevelsListToCheckRegionCreation:
        FreedomCybran2.connect(FreedomCybran3, "e101", TheCompleteListOfRulesForEverySingleRegion["Freedom: Capture Black Sun control center (Cybran)"])
    if "Freedom (Cybran)" in AllLevelsListToCheckRegionCreation:
        FreedomCybran3.connect(FreedomCybran4, "e102", TheCompleteListOfRulesForEverySingleRegion["Freedom: Capture Black Sun (Cybran)"])
    if "Freedom (Cybran)" in AllLevelsListToCheckRegionCreation:
        FreedomCybran4.connect(FreedomCybran5, "e103", TheCompleteListOfRulesForEverySingleRegion["Freedom: Shoot Black Sun (Cybran)"])
    if "Liberation (Aeon)" in AllLevelsListToCheckRegionCreation:
        LiberationAeon0.connect(LiberationAeon1, "e104")
    if "Liberation (Aeon)" in AllLevelsListToCheckRegionCreation:
        LiberationAeon1.connect(LiberationAeon2, "e105")
    if "Liberation (Aeon)" in AllLevelsListToCheckRegionCreation:
        LiberationAeon2.connect(LiberationAeon3, "e106", TheCompleteListOfRulesForEverySingleRegion["Liberation: Build bombers (Aeon)"])
    if "Liberation (Aeon)" in AllLevelsListToCheckRegionCreation:
        LiberationAeon3.connect(LiberationAeon4, "e107", TheCompleteListOfRulesForEverySingleRegion["Liberation: Destroy radar defenders (Aeon)"])
    if "Liberation (Aeon)" in AllLevelsListToCheckRegionCreation:
        LiberationAeon4.connect(LiberationAeon5, "e108", TheCompleteListOfRulesForEverySingleRegion["Liberation: Capture radars (Aeon)"])
    if "Liberation (Aeon)" in AllLevelsListToCheckRegionCreation:
        LiberationAeon5.connect(LiberationAeon6, "e109", TheCompleteListOfRulesForEverySingleRegion["Liberation: Destroy mex (Aeon)"])
    if "Liberation (Aeon)" in AllLevelsListToCheckRegionCreation:
        LiberationAeon6.connect(LiberationAeon7, "e110", TheCompleteListOfRulesForEverySingleRegion["Liberation: Destroy UEF defences (Aeon)"])
    if "Liberation (Aeon)" in AllLevelsListToCheckRegionCreation:
        LiberationAeon7.connect(LiberationAeon8, "e111", TheCompleteListOfRulesForEverySingleRegion["Liberation: Destroy UEF patrols (Aeon)"])
    if "Liberation (Aeon)" in AllLevelsListToCheckRegionCreation:
        LiberationAeon8.connect(LiberationAeon9, "e112", TheCompleteListOfRulesForEverySingleRegion["Liberation: Destroy UEF base defenders (Aeon)"])
    if "Liberation (Aeon)" in AllLevelsListToCheckRegionCreation:
        LiberationAeon9.connect(LiberationAeon10, "e113", TheCompleteListOfRulesForEverySingleRegion["Liberation: Destroy UEF base (Aeon)"])
    if "Liberation (Aeon)" in AllLevelsListToCheckRegionCreation:
        LiberationAeon10.connect(LiberationAeon11, "e114", TheCompleteListOfRulesForEverySingleRegion["Liberation: Kill Aeon Commander (Aeon)"])
    if "Artifact (Aeon)" in AllLevelsListToCheckRegionCreation:
        ArtifactAeon0.connect(ArtifactAeon1, "e115", TheCompleteListOfRulesForEverySingleRegion["Artifact: Destroy first temple (Aeon)"])
    if "Artifact (Aeon)" in AllLevelsListToCheckRegionCreation:
        ArtifactAeon1.connect(ArtifactAeon2, "e116", TheCompleteListOfRulesForEverySingleRegion["Artifact: Protect first artifact (Aeon)"])
    if "Artifact (Aeon)" in AllLevelsListToCheckRegionCreation:
        ArtifactAeon2.connect(ArtifactAeon3, "e117", TheCompleteListOfRulesForEverySingleRegion["Artifact: Find second artifact (Aeon)"])
    if "Artifact (Aeon)" in AllLevelsListToCheckRegionCreation:
        ArtifactAeon3.connect(ArtifactAeon4, "e118", TheCompleteListOfRulesForEverySingleRegion["Artifact: Destroy Aeon reinforcements (Aeon)"])
    if "Artifact (Aeon)" in AllLevelsListToCheckRegionCreation:
        ArtifactAeon4.connect(ArtifactAeon5, "e119", TheCompleteListOfRulesForEverySingleRegion["Artifact: Protect second artifact (Aeon)"])
    if "Artifact (Aeon)" in AllLevelsListToCheckRegionCreation:
        ArtifactAeon5.connect(ArtifactAeon6, "e120", TheCompleteListOfRulesForEverySingleRegion["Artifact: Defend from Aeon attack (Aeon)"])
    if "Artifact (Aeon)" in AllLevelsListToCheckRegionCreation:
        ArtifactAeon6.connect(ArtifactAeon7, "e121", TheCompleteListOfRulesForEverySingleRegion["Artifact: Destroy eastern base (Aeon)"])
    if "Artifact (Aeon)" in AllLevelsListToCheckRegionCreation:
        ArtifactAeon7.connect(ArtifactAeon8, "e122", TheCompleteListOfRulesForEverySingleRegion["Artifact: Destroy navy base (Aeon)"])
    if "Artifact (Aeon)" in AllLevelsListToCheckRegionCreation:
        ArtifactAeon8.connect(ArtifactAeon9, "e123", TheCompleteListOfRulesForEverySingleRegion["Artifact: Protect third artifact (Aeon)"])
    if "Artifact (Aeon)" in AllLevelsListToCheckRegionCreation:
        ArtifactAeon9.connect(ArtifactAeon10, "e124", TheCompleteListOfRulesForEverySingleRegion["Artifact: Kill Aeon Commander (optional) (Aeon)"])
    if "Artifact (Aeon)" in AllLevelsListToCheckRegionCreation:
        ArtifactAeon10.connect(ArtifactAeon11, "e125", TheCompleteListOfRulesForEverySingleRegion["Artifact: Kill Mach (Aeon)"])
    if "Artifact (Aeon)" in AllLevelsListToCheckRegionCreation:
        ArtifactAeon11.connect(ArtifactAeon12, "e126", TheCompleteListOfRulesForEverySingleRegion["Artifact: Go to Gate (Aeon)"])
    if "Defrag (Aeon)" in AllLevelsListToCheckRegionCreation:
        DefragAeon0.connect(DefragAeon1, "e127", TheCompleteListOfRulesForEverySingleRegion["Defrag: Destroy western UEF base (Aeon)"])
    if "Defrag (Aeon)" in AllLevelsListToCheckRegionCreation:
        DefragAeon1.connect(DefragAeon2, "e128", TheCompleteListOfRulesForEverySingleRegion["Defrag: Destroy north-western UEF base (Aeon)"])
    if "Defrag (Aeon)" in AllLevelsListToCheckRegionCreation:
        DefragAeon2.connect(DefragAeon3, "e129", TheCompleteListOfRulesForEverySingleRegion["Defrag: Destroy northern UEF base (Aeon)"])
    if "Defrag (Aeon)" in AllLevelsListToCheckRegionCreation:
        DefragAeon3.connect(DefragAeon4, "e130", TheCompleteListOfRulesForEverySingleRegion["Defrag: Sink UEF cruiser (Aeon)"])
    if "Defrag (Aeon)" in AllLevelsListToCheckRegionCreation:
        DefragAeon4.connect(DefragAeon5, "e131", TheCompleteListOfRulesForEverySingleRegion["Defrag: Destroy static artillery (Aeon)"])
    if "Defrag (Aeon)" in AllLevelsListToCheckRegionCreation:
        DefragAeon5.connect(DefragAeon6, "e132", TheCompleteListOfRulesForEverySingleRegion["Defrag: Escort trucks (Aeon)"])
    if "Defrag (Aeon)" in AllLevelsListToCheckRegionCreation:
        DefragAeon6.connect(DefragAeon7, "e133", TheCompleteListOfRulesForEverySingleRegion["Defrag: Escort ALL trucks (optional) (Aeon)"])
    if "Defrag (Aeon)" in AllLevelsListToCheckRegionCreation:
        DefragAeon7.connect(DefragAeon8, "e134", TheCompleteListOfRulesForEverySingleRegion["Defrag: Optional objective  (optional) (Aeon)"])
    if "Defrag (Aeon)" in AllLevelsListToCheckRegionCreation:
        DefragAeon8.connect(DefragAeon9, "e135", TheCompleteListOfRulesForEverySingleRegion["Defrag: Kill UEF Commander (Aeon)"])
    if "Mainframe Tango (Aeon)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoAeon0.connect(MainframeTangoAeon1, "e136", TheCompleteListOfRulesForEverySingleRegion["Mainframe Tango: Capture Network Node (Aeon)"])
    if "Mainframe Tango (Aeon)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoAeon1.connect(MainframeTangoAeon2, "e137", TheCompleteListOfRulesForEverySingleRegion["Mainframe Tango: Save Network Node (Aeon)"])
    if "Mainframe Tango (Aeon)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoAeon2.connect(MainframeTangoAeon3, "e138", TheCompleteListOfRulesForEverySingleRegion["Mainframe Tango: Save 80% civilian buildings (optional) (Aeon)"])
    if "Mainframe Tango (Aeon)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoAeon3.connect(MainframeTangoAeon4, "e139", TheCompleteListOfRulesForEverySingleRegion["Mainframe Tango: Survive attacks (Aeon)"])
    if "Mainframe Tango (Aeon)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoAeon4.connect(MainframeTangoAeon5, "e140", TheCompleteListOfRulesForEverySingleRegion["Mainframe Tango: Capture northeast node (Aeon)"])
    if "Mainframe Tango (Aeon)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoAeon5.connect(MainframeTangoAeon6, "e141", TheCompleteListOfRulesForEverySingleRegion["Mainframe Tango: Capture northwest node (Aeon)"])
    if "Mainframe Tango (Aeon)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoAeon6.connect(MainframeTangoAeon7, "e142", TheCompleteListOfRulesForEverySingleRegion["Mainframe Tango: Do not attack main Aeon base (Aeon)"])
    if "Mainframe Tango (Aeon)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoAeon7.connect(MainframeTangoAeon8, "e143", TheCompleteListOfRulesForEverySingleRegion["Mainframe Tango: Kill Aeon Commander (Aeon)"])
    if "Unlock (Aeon)" in AllLevelsListToCheckRegionCreation:
        UnlockAeon0.connect(UnlockAeon1, "e144", TheCompleteListOfRulesForEverySingleRegion["Unlock: Destroy UEF shipyards (optional) (Aeon)"])
    if "Unlock (Aeon)" in AllLevelsListToCheckRegionCreation:
        UnlockAeon1.connect(UnlockAeon2, "e145", TheCompleteListOfRulesForEverySingleRegion["Unlock: Destroy UEF radars (Aeon)"])
    if "Unlock (Aeon)" in AllLevelsListToCheckRegionCreation:
        UnlockAeon2.connect(UnlockAeon3, "e146", TheCompleteListOfRulesForEverySingleRegion["Unlock: Go to Hex5 (Aeon)"])
    if "Unlock (Aeon)" in AllLevelsListToCheckRegionCreation:
        UnlockAeon3.connect(UnlockAeon4, "e147", TheCompleteListOfRulesForEverySingleRegion["Unlock: Defend from heavy gunships (Aeon)"])
    if "Unlock (Aeon)" in AllLevelsListToCheckRegionCreation:
        UnlockAeon4.connect(UnlockAeon5, "e148", TheCompleteListOfRulesForEverySingleRegion["Unlock: Infect UEF landing pad (optional) (Aeon)"])
    if "Unlock (Aeon)" in AllLevelsListToCheckRegionCreation:
        UnlockAeon5.connect(UnlockAeon6, "e149", TheCompleteListOfRulesForEverySingleRegion["Unlock: This will be retconned later (Aeon)"])
    if "Unlock (Aeon)" in AllLevelsListToCheckRegionCreation:
        UnlockAeon6.connect(UnlockAeon7, "e150", TheCompleteListOfRulesForEverySingleRegion["Unlock: Kill UEF Commander (Aeon)"])
    if "Freedom (Aeon)" in AllLevelsListToCheckRegionCreation:
        FreedomAeon0.connect(FreedomAeon1, "e151", TheCompleteListOfRulesForEverySingleRegion["Freedom: Build Quantum Gate (Aeon)"])
    if "Freedom (Aeon)" in AllLevelsListToCheckRegionCreation:
        FreedomAeon1.connect(FreedomAeon2, "e152", TheCompleteListOfRulesForEverySingleRegion["Freedom: Download Quantum Virus (Aeon)"])
    if "Freedom (Aeon)" in AllLevelsListToCheckRegionCreation:
        FreedomAeon2.connect(FreedomAeon3, "e153", TheCompleteListOfRulesForEverySingleRegion["Freedom: Capture Black Sun control center (Aeon)"])
    if "Freedom (Aeon)" in AllLevelsListToCheckRegionCreation:
        FreedomAeon3.connect(FreedomAeon4, "e154", TheCompleteListOfRulesForEverySingleRegion["Freedom: Capture Black Sun (Aeon)"])
    if "Freedom (Aeon)" in AllLevelsListToCheckRegionCreation:
        FreedomAeon4.connect(FreedomAeon5, "e155", TheCompleteListOfRulesForEverySingleRegion["Freedom: Shoot Black Sun (Aeon)"])
    if "Liberation (Sera)" in AllLevelsListToCheckRegionCreation:
        LiberationSera0.connect(LiberationSera1, "e156")
    if "Liberation (Sera)" in AllLevelsListToCheckRegionCreation:
        LiberationSera1.connect(LiberationSera2, "e157")
    if "Liberation (Sera)" in AllLevelsListToCheckRegionCreation:
        LiberationSera2.connect(LiberationSera3, "e158", TheCompleteListOfRulesForEverySingleRegion["Liberation: Build bombers (Sera)"])
    if "Liberation (Sera)" in AllLevelsListToCheckRegionCreation:
        LiberationSera3.connect(LiberationSera4, "e159", TheCompleteListOfRulesForEverySingleRegion["Liberation: Destroy radar defenders (Sera)"])
    if "Liberation (Sera)" in AllLevelsListToCheckRegionCreation:
        LiberationSera4.connect(LiberationSera5, "e160", TheCompleteListOfRulesForEverySingleRegion["Liberation: Capture radars (Sera)"])
    if "Liberation (Sera)" in AllLevelsListToCheckRegionCreation:
        LiberationSera5.connect(LiberationSera6, "e161", TheCompleteListOfRulesForEverySingleRegion["Liberation: Destroy mex (Sera)"])
    if "Liberation (Sera)" in AllLevelsListToCheckRegionCreation:
        LiberationSera6.connect(LiberationSera7, "e162", TheCompleteListOfRulesForEverySingleRegion["Liberation: Destroy UEF defences (Sera)"])
    if "Liberation (Sera)" in AllLevelsListToCheckRegionCreation:
        LiberationSera7.connect(LiberationSera8, "e163", TheCompleteListOfRulesForEverySingleRegion["Liberation: Destroy UEF patrols (Sera)"])
    if "Liberation (Sera)" in AllLevelsListToCheckRegionCreation:
        LiberationSera8.connect(LiberationSera9, "e164", TheCompleteListOfRulesForEverySingleRegion["Liberation: Destroy UEF base defenders (Sera)"])
    if "Liberation (Sera)" in AllLevelsListToCheckRegionCreation:
        LiberationSera9.connect(LiberationSera10, "e165", TheCompleteListOfRulesForEverySingleRegion["Liberation: Destroy UEF base (Sera)"])
    if "Liberation (Sera)" in AllLevelsListToCheckRegionCreation:
        LiberationSera10.connect(LiberationSera11, "e166", TheCompleteListOfRulesForEverySingleRegion["Liberation: Kill Aeon Commander (Sera)"])
    if "Artifact (Sera)" in AllLevelsListToCheckRegionCreation:
        ArtifactSera0.connect(ArtifactSera1, "e167", TheCompleteListOfRulesForEverySingleRegion["Artifact: Destroy first temple (Sera)"])
    if "Artifact (Sera)" in AllLevelsListToCheckRegionCreation:
        ArtifactSera1.connect(ArtifactSera2, "e168", TheCompleteListOfRulesForEverySingleRegion["Artifact: Protect first artifact (Sera)"])
    if "Artifact (Sera)" in AllLevelsListToCheckRegionCreation:
        ArtifactSera2.connect(ArtifactSera3, "e169", TheCompleteListOfRulesForEverySingleRegion["Artifact: Find second artifact (Sera)"])
    if "Artifact (Sera)" in AllLevelsListToCheckRegionCreation:
        ArtifactSera3.connect(ArtifactSera4, "e170", TheCompleteListOfRulesForEverySingleRegion["Artifact: Destroy Aeon reinforcements (Sera)"])
    if "Artifact (Sera)" in AllLevelsListToCheckRegionCreation:
        ArtifactSera4.connect(ArtifactSera5, "e171", TheCompleteListOfRulesForEverySingleRegion["Artifact: Protect second artifact (Sera)"])
    if "Artifact (Sera)" in AllLevelsListToCheckRegionCreation:
        ArtifactSera5.connect(ArtifactSera6, "e172", TheCompleteListOfRulesForEverySingleRegion["Artifact: Defend from Aeon attack (Sera)"])
    if "Artifact (Sera)" in AllLevelsListToCheckRegionCreation:
        ArtifactSera6.connect(ArtifactSera7, "e173", TheCompleteListOfRulesForEverySingleRegion["Artifact: Destroy eastern base (Sera)"])
    if "Artifact (Sera)" in AllLevelsListToCheckRegionCreation:
        ArtifactSera7.connect(ArtifactSera8, "e174", TheCompleteListOfRulesForEverySingleRegion["Artifact: Destroy navy base (Sera)"])
    if "Artifact (Sera)" in AllLevelsListToCheckRegionCreation:
        ArtifactSera8.connect(ArtifactSera9, "e175", TheCompleteListOfRulesForEverySingleRegion["Artifact: Protect third artifact (Sera)"])
    if "Artifact (Sera)" in AllLevelsListToCheckRegionCreation:
        ArtifactSera9.connect(ArtifactSera10, "e176", TheCompleteListOfRulesForEverySingleRegion["Artifact: Kill Aeon Commander (optional) (Sera)"])
    if "Artifact (Sera)" in AllLevelsListToCheckRegionCreation:
        ArtifactSera10.connect(ArtifactSera11, "e177", TheCompleteListOfRulesForEverySingleRegion["Artifact: Kill Mach (Sera)"])
    if "Artifact (Sera)" in AllLevelsListToCheckRegionCreation:
        ArtifactSera11.connect(ArtifactSera12, "e178", TheCompleteListOfRulesForEverySingleRegion["Artifact: Go to Gate (Sera)"])
    if "Defrag (Sera)" in AllLevelsListToCheckRegionCreation:
        DefragSera0.connect(DefragSera1, "e179", TheCompleteListOfRulesForEverySingleRegion["Defrag: Destroy western UEF base (Sera)"])
    if "Defrag (Sera)" in AllLevelsListToCheckRegionCreation:
        DefragSera1.connect(DefragSera2, "e180", TheCompleteListOfRulesForEverySingleRegion["Defrag: Destroy north-western UEF base (Sera)"])
    if "Defrag (Sera)" in AllLevelsListToCheckRegionCreation:
        DefragSera2.connect(DefragSera3, "e181", TheCompleteListOfRulesForEverySingleRegion["Defrag: Destroy northern UEF base (Sera)"])
    if "Defrag (Sera)" in AllLevelsListToCheckRegionCreation:
        DefragSera3.connect(DefragSera4, "e182", TheCompleteListOfRulesForEverySingleRegion["Defrag: Sink UEF cruiser (Sera)"])
    if "Defrag (Sera)" in AllLevelsListToCheckRegionCreation:
        DefragSera4.connect(DefragSera5, "e183", TheCompleteListOfRulesForEverySingleRegion["Defrag: Destroy static artillery (Sera)"])
    if "Defrag (Sera)" in AllLevelsListToCheckRegionCreation:
        DefragSera5.connect(DefragSera6, "e184", TheCompleteListOfRulesForEverySingleRegion["Defrag: Escort trucks (Sera)"])
    if "Defrag (Sera)" in AllLevelsListToCheckRegionCreation:
        DefragSera6.connect(DefragSera7, "e185", TheCompleteListOfRulesForEverySingleRegion["Defrag: Escort ALL trucks (optional) (Sera)"])
    if "Defrag (Sera)" in AllLevelsListToCheckRegionCreation:
        DefragSera7.connect(DefragSera8, "e186", TheCompleteListOfRulesForEverySingleRegion["Defrag: Optional objective  (optional) (Sera)"])
    if "Defrag (Sera)" in AllLevelsListToCheckRegionCreation:
        DefragSera8.connect(DefragSera9, "e187", TheCompleteListOfRulesForEverySingleRegion["Defrag: Kill UEF Commander (Sera)"])
    if "Mainframe Tango (Sera)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoSera0.connect(MainframeTangoSera1, "e188", TheCompleteListOfRulesForEverySingleRegion["Mainframe Tango: Capture Network Node (Sera)"])
    if "Mainframe Tango (Sera)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoSera1.connect(MainframeTangoSera2, "e189", TheCompleteListOfRulesForEverySingleRegion["Mainframe Tango: Save Network Node (Sera)"])
    if "Mainframe Tango (Sera)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoSera2.connect(MainframeTangoSera3, "e190", TheCompleteListOfRulesForEverySingleRegion["Mainframe Tango: Save 80% civilian buildings (optional) (Sera)"])
    if "Mainframe Tango (Sera)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoSera3.connect(MainframeTangoSera4, "e191", TheCompleteListOfRulesForEverySingleRegion["Mainframe Tango: Survive attacks (Sera)"])
    if "Mainframe Tango (Sera)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoSera4.connect(MainframeTangoSera5, "e192", TheCompleteListOfRulesForEverySingleRegion["Mainframe Tango: Capture northeast node (Sera)"])
    if "Mainframe Tango (Sera)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoSera5.connect(MainframeTangoSera6, "e193", TheCompleteListOfRulesForEverySingleRegion["Mainframe Tango: Capture northwest node (Sera)"])
    if "Mainframe Tango (Sera)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoSera6.connect(MainframeTangoSera7, "e194", TheCompleteListOfRulesForEverySingleRegion["Mainframe Tango: Do not attack main Aeon base (Sera)"])
    if "Mainframe Tango (Sera)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoSera7.connect(MainframeTangoSera8, "e195", TheCompleteListOfRulesForEverySingleRegion["Mainframe Tango: Kill Aeon Commander (Sera)"])
    if "Unlock (Sera)" in AllLevelsListToCheckRegionCreation:
        UnlockSera0.connect(UnlockSera1, "e196", TheCompleteListOfRulesForEverySingleRegion["Unlock: Destroy UEF shipyards (optional) (Sera)"])
    if "Unlock (Sera)" in AllLevelsListToCheckRegionCreation:
        UnlockSera1.connect(UnlockSera2, "e197", TheCompleteListOfRulesForEverySingleRegion["Unlock: Destroy UEF radars (Sera)"])
    if "Unlock (Sera)" in AllLevelsListToCheckRegionCreation:
        UnlockSera2.connect(UnlockSera3, "e198", TheCompleteListOfRulesForEverySingleRegion["Unlock: Go to Hex5 (Sera)"])
    if "Unlock (Sera)" in AllLevelsListToCheckRegionCreation:
        UnlockSera3.connect(UnlockSera4, "e199", TheCompleteListOfRulesForEverySingleRegion["Unlock: Defend from heavy gunships (Sera)"])
    if "Unlock (Sera)" in AllLevelsListToCheckRegionCreation:
        UnlockSera4.connect(UnlockSera5, "e200", TheCompleteListOfRulesForEverySingleRegion["Unlock: Infect UEF landing pad (optional) (Sera)"])
    if "Unlock (Sera)" in AllLevelsListToCheckRegionCreation:
        UnlockSera5.connect(UnlockSera6, "e201", TheCompleteListOfRulesForEverySingleRegion["Unlock: This will be retconned later (Sera)"])
    if "Unlock (Sera)" in AllLevelsListToCheckRegionCreation:
        UnlockSera6.connect(UnlockSera7, "e202", TheCompleteListOfRulesForEverySingleRegion["Unlock: Kill UEF Commander (Sera)"])
    if "Freedom (Sera)" in AllLevelsListToCheckRegionCreation:
        FreedomSera0.connect(FreedomSera1, "e203", TheCompleteListOfRulesForEverySingleRegion["Freedom: Build Quantum Gate (Sera)"])
    if "Freedom (Sera)" in AllLevelsListToCheckRegionCreation:
        FreedomSera1.connect(FreedomSera2, "e204", TheCompleteListOfRulesForEverySingleRegion["Freedom: Download Quantum Virus (Sera)"])
    if "Freedom (Sera)" in AllLevelsListToCheckRegionCreation:
        FreedomSera2.connect(FreedomSera3, "e205", TheCompleteListOfRulesForEverySingleRegion["Freedom: Capture Black Sun control center (Sera)"])
    if "Freedom (Sera)" in AllLevelsListToCheckRegionCreation:
        FreedomSera3.connect(FreedomSera4, "e206", TheCompleteListOfRulesForEverySingleRegion["Freedom: Capture Black Sun (Sera)"])
    if "Freedom (Sera)" in AllLevelsListToCheckRegionCreation:
        FreedomSera4.connect(FreedomSera5, "e207", TheCompleteListOfRulesForEverySingleRegion["Freedom: Shoot Black Sun (Sera)"])

    indexOfEntrance = 208
    for i in range(Width):
        for j in range(Height):
            CheckFilled = bool(not(i == 0 and j == 0))
            if CheckFilled:
                if i > 0:
                    regionLast = world.get_region(TotalListOfTtotallyLevels[THE_GRID[i - 1][j]][len(TotalListOfTtotallyLevels[THE_GRID[i - 1][j]]) - 1])
                    regionFirst = world.get_region(TotalListOfTtotallyLevels[THE_GRID[i][j]][0])
                    tempSTR = "e" + str(indexOfEntrance)
                    if not THE_GRID[i][j] in levelsTier1FOREVER:
                        regionLast.connect(regionFirst, tempSTR, TheCompleteListOfRulesForEverySingleRegion[TotalListOfTtotallyLevels[THE_GRID[i][j]][0]])
                    else:
                        regionLast.connect(regionFirst, tempSTR)
                    indexOfEntrance = 1 + indexOfEntrance
                if j > 0:
                    regionLast = world.get_region(TotalListOfTtotallyLevels[THE_GRID[i][j - 1]][len(TotalListOfTtotallyLevels[THE_GRID[i][j - 1]]) - 1])
                    regionFirst = world.get_region(TotalListOfTtotallyLevels[THE_GRID[i][j]][0])
                    tempSTR = "e" + str(indexOfEntrance)
                    if not THE_GRID[i][j] in levelsTier1FOREVER:
                        regionLast.connect(regionFirst, tempSTR, TheCompleteListOfRulesForEverySingleRegion[TotalListOfTtotallyLevels[THE_GRID[i][j]][0]])
                    else:
                        regionLast.connect(regionFirst, tempSTR)
                    indexOfEntrance = 1 + indexOfEntrance
                if i < Width - 1:
                    regionLast = world.get_region(TotalListOfTtotallyLevels[THE_GRID[i + 1][j]][len(TotalListOfTtotallyLevels[THE_GRID[i + 1][j]]) - 1])
                    regionFirst = world.get_region(TotalListOfTtotallyLevels[THE_GRID[i][j]][0])
                    tempSTR = "e" + str(indexOfEntrance)
                    if not THE_GRID[i][j] in levelsTier1FOREVER:
                        regionLast.connect(regionFirst, tempSTR, TheCompleteListOfRulesForEverySingleRegion[TotalListOfTtotallyLevels[THE_GRID[i][j]][0]])
                    else:
                        regionLast.connect(regionFirst, tempSTR)
                    indexOfEntrance = 1 + indexOfEntrance
                if j < Height - 1:
                    regionLast = world.get_region(TotalListOfTtotallyLevels[THE_GRID[i][j + 1]][len(TotalListOfTtotallyLevels[THE_GRID[i][j + 1]]) - 1])
                    regionFirst = world.get_region(TotalListOfTtotallyLevels[THE_GRID[i][j]][0])
                    tempSTR = "e" + str(indexOfEntrance)
                    if not THE_GRID[i][j] in levelsTier1FOREVER:
                        regionLast.connect(regionFirst, tempSTR, TheCompleteListOfRulesForEverySingleRegion[TotalListOfTtotallyLevels[THE_GRID[i][j]][0]])
                    else:
                        regionLast.connect(regionFirst, tempSTR)
                    indexOfEntrance = 1 + indexOfEntrance

    listOfFactionsThatActuallyExist = []
    for i in range(Width):
        for j in range(Height):
            if ("UEF" in THE_GRID[i][j]) and not "uef" in listOfFactionsThatActuallyExist:
                listOfFactionsThatActuallyExist.append("uef")
            if "Cybran" in THE_GRID[i][j] and not "cybran" in listOfFactionsThatActuallyExist:
                listOfFactionsThatActuallyExist.append("cybran")
            if "Aeon" in THE_GRID[i][j] and not "aeon" in listOfFactionsThatActuallyExist:
                listOfFactionsThatActuallyExist.append("aeon")
            if "Sera" in THE_GRID[i][j] and not "sera" in listOfFactionsThatActuallyExist:
                listOfFactionsThatActuallyExist.append("sera")

    PossibleItemList = []
    if "Liberation (UEF)" in AllLevelsListToCheckRegionCreation:
        LiberationUEFPossibleUnitList = ["Scorcher"]
        temp = world.random.randrange(0, len(LiberationUEFPossibleUnitList))
        if not LiberationUEFPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(LiberationUEFPossibleUnitList[temp])

    if "Artifact (UEF)" in AllLevelsListToCheckRegionCreation:
        ArtifactUEFPossibleUnitList = ["Scorcher"]
        temp = world.random.randrange(0, len(ArtifactUEFPossibleUnitList))
        if not ArtifactUEFPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(ArtifactUEFPossibleUnitList[temp])

    if "Defrag (UEF)" in AllLevelsListToCheckRegionCreation:
        DefragUEFPossibleUnitList = ["Scorcher"]
        temp = world.random.randrange(0, len(DefragUEFPossibleUnitList))
        if not DefragUEFPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(DefragUEFPossibleUnitList[temp])

    if "Mainframe Tango (UEF)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoUEFPossibleUnitList = ["Scorcher"]
        temp = world.random.randrange(0, len(MainframeTangoUEFPossibleUnitList))
        if not MainframeTangoUEFPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(MainframeTangoUEFPossibleUnitList[temp])

    if "Unlock (UEF)" in AllLevelsListToCheckRegionCreation:
        UnlockUEFPossibleUnitList = ["Scorcher"]
        temp = world.random.randrange(0, len(UnlockUEFPossibleUnitList))
        if not UnlockUEFPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(UnlockUEFPossibleUnitList[temp])

    if "Freedom (UEF)" in AllLevelsListToCheckRegionCreation:
        FreedomUEFPossibleUnitList = ["Scorcher"]
        temp = world.random.randrange(0, len(FreedomUEFPossibleUnitList))
        if not FreedomUEFPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomUEFPossibleUnitList[temp])

    if "Liberation (UEF)" in AllLevelsListToCheckRegionCreation:
        LiberationUEFPossibleUnitList = ["Cyclone", "Archer", "DA1 Railgun"]
        temp = world.random.randrange(0, len(LiberationUEFPossibleUnitList))
        if not LiberationUEFPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(LiberationUEFPossibleUnitList[temp])

    if "Artifact (UEF)" in AllLevelsListToCheckRegionCreation:
        ArtifactUEFPossibleUnitList = ["Cyclone", "Archer", "DA1 Railgun"]
        temp = world.random.randrange(0, len(ArtifactUEFPossibleUnitList))
        if not ArtifactUEFPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(ArtifactUEFPossibleUnitList[temp])

    if "Defrag (UEF)" in AllLevelsListToCheckRegionCreation:
        DefragUEFPossibleUnitList = ["Cyclone", "Archer", "DA1 Railgun"]
        temp = world.random.randrange(0, len(DefragUEFPossibleUnitList))
        if not DefragUEFPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(DefragUEFPossibleUnitList[temp])

    if "Mainframe Tango (UEF)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoUEFPossibleUnitList = ["Cyclone", "Archer", "DA1 Railgun"]
        temp = world.random.randrange(0, len(MainframeTangoUEFPossibleUnitList))
        if not MainframeTangoUEFPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(MainframeTangoUEFPossibleUnitList[temp])

    if "Unlock (UEF)" in AllLevelsListToCheckRegionCreation:
        UnlockUEFPossibleUnitList = ["Cyclone", "Archer", "DA1 Railgun"]
        temp = world.random.randrange(0, len(UnlockUEFPossibleUnitList))
        if not UnlockUEFPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(UnlockUEFPossibleUnitList[temp])

    if "Freedom (UEF)" in AllLevelsListToCheckRegionCreation:
        FreedomUEFPossibleUnitList = ["Cyclone", "Archer", "DA1 Railgun"]
        temp = world.random.randrange(0, len(FreedomUEFPossibleUnitList))
        if not FreedomUEFPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomUEFPossibleUnitList[temp])

    if "Artifact (UEF)" in AllLevelsListToCheckRegionCreation:
        ArtifactUEFPossibleUnitList = ["MA12 Striker"]
        temp = world.random.randrange(0, len(ArtifactUEFPossibleUnitList))
        if not ArtifactUEFPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(ArtifactUEFPossibleUnitList[temp])

    if "Defrag (UEF)" in AllLevelsListToCheckRegionCreation:
        DefragUEFPossibleUnitList = ["MA12 Striker"]
        temp = world.random.randrange(0, len(DefragUEFPossibleUnitList))
        if not DefragUEFPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(DefragUEFPossibleUnitList[temp])

    if "Mainframe Tango (UEF)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoUEFPossibleUnitList = ["MA12 Striker"]
        temp = world.random.randrange(0, len(MainframeTangoUEFPossibleUnitList))
        if not MainframeTangoUEFPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(MainframeTangoUEFPossibleUnitList[temp])

    if "Unlock (UEF)" in AllLevelsListToCheckRegionCreation:
        UnlockUEFPossibleUnitList = ["MA12 Striker"]
        temp = world.random.randrange(0, len(UnlockUEFPossibleUnitList))
        if not UnlockUEFPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(UnlockUEFPossibleUnitList[temp])

    if "Freedom (UEF)" in AllLevelsListToCheckRegionCreation:
        FreedomUEFPossibleUnitList = ["MA12 Striker"]
        temp = world.random.randrange(0, len(FreedomUEFPossibleUnitList))
        if not FreedomUEFPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomUEFPossibleUnitList[temp])

    if "Artifact (UEF)" in AllLevelsListToCheckRegionCreation:
        ArtifactUEFPossibleUnitList = ["Mongoose", "Pillar", "Riptide", "Sparky", "Triad"]
        temp = world.random.randrange(0, len(ArtifactUEFPossibleUnitList))
        if not ArtifactUEFPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(ArtifactUEFPossibleUnitList[temp])

    if "Defrag (UEF)" in AllLevelsListToCheckRegionCreation:
        DefragUEFPossibleUnitList = ["Mongoose", "Pillar", "Riptide", "Sparky", "Triad"]
        temp = world.random.randrange(0, len(DefragUEFPossibleUnitList))
        if not DefragUEFPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(DefragUEFPossibleUnitList[temp])

    if "Mainframe Tango (UEF)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoUEFPossibleUnitList = ["Mongoose", "Pillar", "Riptide", "Sparky", "Triad"]
        temp = world.random.randrange(0, len(MainframeTangoUEFPossibleUnitList))
        if not MainframeTangoUEFPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(MainframeTangoUEFPossibleUnitList[temp])

    if "Unlock (UEF)" in AllLevelsListToCheckRegionCreation:
        UnlockUEFPossibleUnitList = ["Mongoose", "Pillar", "Riptide", "Sparky", "Triad"]
        temp = world.random.randrange(0, len(UnlockUEFPossibleUnitList))
        if not UnlockUEFPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(UnlockUEFPossibleUnitList[temp])

    if "Freedom (UEF)" in AllLevelsListToCheckRegionCreation:
        FreedomUEFPossibleUnitList = ["Mongoose", "Pillar", "Riptide", "Sparky", "Triad"]
        temp = world.random.randrange(0, len(FreedomUEFPossibleUnitList))
        if not FreedomUEFPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomUEFPossibleUnitList[temp])

    if "Artifact (UEF)" in AllLevelsListToCheckRegionCreation:
        ArtifactUEFPossibleUnitList = ["Triad", "Tigershark", "Thunderhead Class", "Stork", "DN1"]
        temp = world.random.randrange(0, len(ArtifactUEFPossibleUnitList))
        if not ArtifactUEFPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(ArtifactUEFPossibleUnitList[temp])

    if "Defrag (UEF)" in AllLevelsListToCheckRegionCreation:
        DefragUEFPossibleUnitList = ["Triad", "Tigershark", "Thunderhead Class", "Stork", "DN1"]
        temp = world.random.randrange(0, len(DefragUEFPossibleUnitList))
        if not DefragUEFPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(DefragUEFPossibleUnitList[temp])

    if "Mainframe Tango (UEF)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoUEFPossibleUnitList = ["Triad", "Tigershark", "Thunderhead Class", "Stork", "DN1"]
        temp = world.random.randrange(0, len(MainframeTangoUEFPossibleUnitList))
        if not MainframeTangoUEFPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(MainframeTangoUEFPossibleUnitList[temp])

    if "Unlock (UEF)" in AllLevelsListToCheckRegionCreation:
        UnlockUEFPossibleUnitList = ["Triad", "Tigershark", "Thunderhead Class", "Stork", "DN1"]
        temp = world.random.randrange(0, len(UnlockUEFPossibleUnitList))
        if not UnlockUEFPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(UnlockUEFPossibleUnitList[temp])

    if "Freedom (UEF)" in AllLevelsListToCheckRegionCreation:
        FreedomUEFPossibleUnitList = ["Triad", "Tigershark", "Thunderhead Class", "Stork", "DN1"]
        temp = world.random.randrange(0, len(FreedomUEFPossibleUnitList))
        if not FreedomUEFPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomUEFPossibleUnitList[temp])

    if "Artifact (UEF)" in AllLevelsListToCheckRegionCreation:
        ArtifactUEFPossibleUnitList = ["Valiant Class", "Governor Class", "Stinger", "C-6 Courier", "Klink Hammer", "Aloha"]
        temp = world.random.randrange(0, len(ArtifactUEFPossibleUnitList))
        if not ArtifactUEFPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(ArtifactUEFPossibleUnitList[temp])

    if "Defrag (UEF)" in AllLevelsListToCheckRegionCreation:
        DefragUEFPossibleUnitList = ["Valiant Class", "Governor Class", "Stinger", "C-6 Courier", "Klink Hammer", "Aloha"]
        temp = world.random.randrange(0, len(DefragUEFPossibleUnitList))
        if not DefragUEFPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(DefragUEFPossibleUnitList[temp])

    if "Mainframe Tango (UEF)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoUEFPossibleUnitList = ["Valiant Class", "Governor Class", "Stinger", "C-6 Courier", "Klink Hammer", "Aloha"]
        temp = world.random.randrange(0, len(MainframeTangoUEFPossibleUnitList))
        if not MainframeTangoUEFPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(MainframeTangoUEFPossibleUnitList[temp])

    if "Unlock (UEF)" in AllLevelsListToCheckRegionCreation:
        UnlockUEFPossibleUnitList = ["Valiant Class", "Governor Class", "Stinger", "C-6 Courier", "Klink Hammer", "Aloha"]
        temp = world.random.randrange(0, len(UnlockUEFPossibleUnitList))
        if not UnlockUEFPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(UnlockUEFPossibleUnitList[temp])

    if "Freedom (UEF)" in AllLevelsListToCheckRegionCreation:
        FreedomUEFPossibleUnitList = ["Valiant Class", "Governor Class", "Stinger", "C-6 Courier", "Klink Hammer", "Aloha"]
        temp = world.random.randrange(0, len(FreedomUEFPossibleUnitList))
        if not FreedomUEFPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomUEFPossibleUnitList[temp])

    if "Defrag (UEF)" in AllLevelsListToCheckRegionCreation:
        DefragUEFPossibleUnitList = ["UEF T2 Mass Extractor"]
        temp = world.random.randrange(0, len(DefragUEFPossibleUnitList))
        if not DefragUEFPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(DefragUEFPossibleUnitList[temp])

    if "Mainframe Tango (UEF)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoUEFPossibleUnitList = ["UEF T2 Mass Extractor"]
        temp = world.random.randrange(0, len(MainframeTangoUEFPossibleUnitList))
        if not MainframeTangoUEFPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(MainframeTangoUEFPossibleUnitList[temp])

    if "Unlock (UEF)" in AllLevelsListToCheckRegionCreation:
        UnlockUEFPossibleUnitList = ["UEF T2 Mass Extractor"]
        temp = world.random.randrange(0, len(UnlockUEFPossibleUnitList))
        if not UnlockUEFPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(UnlockUEFPossibleUnitList[temp])

    if "Freedom (UEF)" in AllLevelsListToCheckRegionCreation:
        FreedomUEFPossibleUnitList = ["UEF T2 Mass Extractor"]
        temp = world.random.randrange(0, len(FreedomUEFPossibleUnitList))
        if not FreedomUEFPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomUEFPossibleUnitList[temp])

    if "Defrag (UEF)" in AllLevelsListToCheckRegionCreation:
        DefragUEFPossibleUnitList = ["EG - 200 Fusion Reactor"]
        temp = world.random.randrange(0, len(DefragUEFPossibleUnitList))
        if not DefragUEFPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(DefragUEFPossibleUnitList[temp])

    if "Mainframe Tango (UEF)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoUEFPossibleUnitList = ["EG - 200 Fusion Reactor"]
        temp = world.random.randrange(0, len(MainframeTangoUEFPossibleUnitList))
        if not MainframeTangoUEFPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(MainframeTangoUEFPossibleUnitList[temp])

    if "Unlock (UEF)" in AllLevelsListToCheckRegionCreation:
        UnlockUEFPossibleUnitList = ["EG - 200 Fusion Reactor"]
        temp = world.random.randrange(0, len(UnlockUEFPossibleUnitList))
        if not UnlockUEFPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(UnlockUEFPossibleUnitList[temp])

    if "Freedom (UEF)" in AllLevelsListToCheckRegionCreation:
        FreedomUEFPossibleUnitList = ["EG - 200 Fusion Reactor"]
        temp = world.random.randrange(0, len(FreedomUEFPossibleUnitList))
        if not FreedomUEFPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomUEFPossibleUnitList[temp])

    if "Defrag (UEF)" in AllLevelsListToCheckRegionCreation:
        DefragUEFPossibleUnitList = ["Air Cleaner", "Sky Boxer"]
        temp = world.random.randrange(0, len(DefragUEFPossibleUnitList))
        if not DefragUEFPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(DefragUEFPossibleUnitList[temp])

    if "Mainframe Tango (UEF)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoUEFPossibleUnitList = ["Air Cleaner", "Sky Boxer"]
        temp = world.random.randrange(0, len(MainframeTangoUEFPossibleUnitList))
        if not MainframeTangoUEFPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(MainframeTangoUEFPossibleUnitList[temp])

    if "Unlock (UEF)" in AllLevelsListToCheckRegionCreation:
        UnlockUEFPossibleUnitList = ["Air Cleaner", "Sky Boxer"]
        temp = world.random.randrange(0, len(UnlockUEFPossibleUnitList))
        if not UnlockUEFPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(UnlockUEFPossibleUnitList[temp])

    if "Freedom (UEF)" in AllLevelsListToCheckRegionCreation:
        FreedomUEFPossibleUnitList = ["Air Cleaner", "Sky Boxer"]
        temp = world.random.randrange(0, len(FreedomUEFPossibleUnitList))
        if not FreedomUEFPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomUEFPossibleUnitList[temp])

    if "Mainframe Tango (UEF)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoUEFPossibleUnitList = ["Valiant Class", "Governor Class"]
        temp = world.random.randrange(0, len(MainframeTangoUEFPossibleUnitList))
        if not MainframeTangoUEFPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(MainframeTangoUEFPossibleUnitList[temp])

    if "Unlock (UEF)" in AllLevelsListToCheckRegionCreation:
        UnlockUEFPossibleUnitList = ["Valiant Class", "Governor Class"]
        temp = world.random.randrange(0, len(UnlockUEFPossibleUnitList))
        if not UnlockUEFPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(UnlockUEFPossibleUnitList[temp])

    if "Freedom (UEF)" in AllLevelsListToCheckRegionCreation:
        FreedomUEFPossibleUnitList = ["Valiant Class", "Governor Class"]
        temp = world.random.randrange(0, len(FreedomUEFPossibleUnitList))
        if not FreedomUEFPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomUEFPossibleUnitList[temp])

    if "Unlock (UEF)" in AllLevelsListToCheckRegionCreation:
        UnlockUEFPossibleUnitList = ["UEF T3 Mass Extractor"]
        temp = world.random.randrange(0, len(UnlockUEFPossibleUnitList))
        if not UnlockUEFPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(UnlockUEFPossibleUnitList[temp])

    if "Freedom (UEF)" in AllLevelsListToCheckRegionCreation:
        FreedomUEFPossibleUnitList = ["UEF T3 Mass Extractor"]
        temp = world.random.randrange(0, len(FreedomUEFPossibleUnitList))
        if not FreedomUEFPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomUEFPossibleUnitList[temp])

    if "Unlock (UEF)" in AllLevelsListToCheckRegionCreation:
        UnlockUEFPossibleUnitList = ["EG 900 Fusion Reactor"]
        temp = world.random.randrange(0, len(UnlockUEFPossibleUnitList))
        if not UnlockUEFPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(UnlockUEFPossibleUnitList[temp])

    if "Freedom (UEF)" in AllLevelsListToCheckRegionCreation:
        FreedomUEFPossibleUnitList = ["EG 900 Fusion Reactor"]
        temp = world.random.randrange(0, len(FreedomUEFPossibleUnitList))
        if not FreedomUEFPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomUEFPossibleUnitList[temp])

    if "Unlock (UEF)" in AllLevelsListToCheckRegionCreation:
        UnlockUEFPossibleUnitList = ["Titan", "Persival", "Spearhead", "Continental", "Janus", "Mavor", "Novax Center", "Aloha", "Duke", "Stonager", "Broadsword", "Ambassador"]
        temp = world.random.randrange(0, len(UnlockUEFPossibleUnitList))
        if not UnlockUEFPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(UnlockUEFPossibleUnitList[temp])

    if "Freedom (UEF)" in AllLevelsListToCheckRegionCreation:
        FreedomUEFPossibleUnitList = ["Titan", "Persival", "Spearhead", "Continental", "Janus", "Mavor", "Novax Center", "Aloha", "Duke", "Stonager", "Broadsword", "Ambassador"]
        temp = world.random.randrange(0, len(FreedomUEFPossibleUnitList))
        if not FreedomUEFPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomUEFPossibleUnitList[temp])

    if "Unlock (UEF)" in AllLevelsListToCheckRegionCreation:
        UnlockUEFPossibleUnitList = ["Governor Class"]
        temp = world.random.randrange(0, len(UnlockUEFPossibleUnitList))
        if not UnlockUEFPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(UnlockUEFPossibleUnitList[temp])

    if "Freedom (UEF)" in AllLevelsListToCheckRegionCreation:
        FreedomUEFPossibleUnitList = ["Governor Class"]
        temp = world.random.randrange(0, len(FreedomUEFPossibleUnitList))
        if not FreedomUEFPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomUEFPossibleUnitList[temp])

    if "Unlock (UEF)" in AllLevelsListToCheckRegionCreation:
        UnlockUEFPossibleUnitList = ["C14 Star Lifter"]
        temp = world.random.randrange(0, len(UnlockUEFPossibleUnitList))
        if not UnlockUEFPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(UnlockUEFPossibleUnitList[temp])

    if "Freedom (UEF)" in AllLevelsListToCheckRegionCreation:
        FreedomUEFPossibleUnitList = ["C14 Star Lifter"]
        temp = world.random.randrange(0, len(FreedomUEFPossibleUnitList))
        if not FreedomUEFPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomUEFPossibleUnitList[temp])

    if "Unlock (UEF)" in AllLevelsListToCheckRegionCreation:
        UnlockUEFPossibleUnitList = ["Wasp", "Cougar", "Flayer"]
        temp = world.random.randrange(0, len(UnlockUEFPossibleUnitList))
        if not UnlockUEFPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(UnlockUEFPossibleUnitList[temp])

    if "Freedom (UEF)" in AllLevelsListToCheckRegionCreation:
        FreedomUEFPossibleUnitList = ["Wasp", "Cougar", "Flayer"]
        temp = world.random.randrange(0, len(FreedomUEFPossibleUnitList))
        if not FreedomUEFPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomUEFPossibleUnitList[temp])

    if "Freedom (UEF)" in AllLevelsListToCheckRegionCreation:
        FreedomUEFPossibleUnitList = ["QGW R-32"]
        temp = world.random.randrange(0, len(FreedomUEFPossibleUnitList))
        if not FreedomUEFPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomUEFPossibleUnitList[temp])

    if "Freedom (UEF)" in AllLevelsListToCheckRegionCreation:
        FreedomUEFPossibleUnitList = ["Titan", "Persival", "Spearhead", "Continental", "Janus", "Broadsword", "Ambassador", "Fatboy"]
        temp = world.random.randrange(0, len(FreedomUEFPossibleUnitList))
        if not FreedomUEFPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomUEFPossibleUnitList[temp])

    if "Liberation (Cybran)" in AllLevelsListToCheckRegionCreation:
        LiberationCybranPossibleUnitList = ["Zeus"]
        temp = world.random.randrange(0, len(LiberationCybranPossibleUnitList))
        if not LiberationCybranPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(LiberationCybranPossibleUnitList[temp])

    if "Artifact (Cybran)" in AllLevelsListToCheckRegionCreation:
        ArtifactCybranPossibleUnitList = ["Zeus"]
        temp = world.random.randrange(0, len(ArtifactCybranPossibleUnitList))
        if not ArtifactCybranPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(ArtifactCybranPossibleUnitList[temp])

    if "Defrag (Cybran)" in AllLevelsListToCheckRegionCreation:
        DefragCybranPossibleUnitList = ["Zeus"]
        temp = world.random.randrange(0, len(DefragCybranPossibleUnitList))
        if not DefragCybranPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(DefragCybranPossibleUnitList[temp])

    if "Mainframe Tango (Cybran)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoCybranPossibleUnitList = ["Zeus"]
        temp = world.random.randrange(0, len(MainframeTangoCybranPossibleUnitList))
        if not MainframeTangoCybranPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(MainframeTangoCybranPossibleUnitList[temp])

    if "Unlock (Cybran)" in AllLevelsListToCheckRegionCreation:
        UnlockCybranPossibleUnitList = ["Zeus"]
        temp = world.random.randrange(0, len(UnlockCybranPossibleUnitList))
        if not UnlockCybranPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(UnlockCybranPossibleUnitList[temp])

    if "Freedom (Cybran)" in AllLevelsListToCheckRegionCreation:
        FreedomCybranPossibleUnitList = ["Zeus"]
        temp = world.random.randrange(0, len(FreedomCybranPossibleUnitList))
        if not FreedomCybranPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomCybranPossibleUnitList[temp])

    if "Liberation (Cybran)" in AllLevelsListToCheckRegionCreation:
        LiberationCybranPossibleUnitList = ["Prowler", "Sky Slammer", "Tracer"]
        temp = world.random.randrange(0, len(LiberationCybranPossibleUnitList))
        if not LiberationCybranPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(LiberationCybranPossibleUnitList[temp])

    if "Artifact (Cybran)" in AllLevelsListToCheckRegionCreation:
        ArtifactCybranPossibleUnitList = ["Prowler", "Sky Slammer", "Tracer"]
        temp = world.random.randrange(0, len(ArtifactCybranPossibleUnitList))
        if not ArtifactCybranPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(ArtifactCybranPossibleUnitList[temp])

    if "Defrag (Cybran)" in AllLevelsListToCheckRegionCreation:
        DefragCybranPossibleUnitList = ["Prowler", "Sky Slammer", "Tracer"]
        temp = world.random.randrange(0, len(DefragCybranPossibleUnitList))
        if not DefragCybranPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(DefragCybranPossibleUnitList[temp])

    if "Mainframe Tango (Cybran)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoCybranPossibleUnitList = ["Prowler", "Sky Slammer", "Tracer"]
        temp = world.random.randrange(0, len(MainframeTangoCybranPossibleUnitList))
        if not MainframeTangoCybranPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(MainframeTangoCybranPossibleUnitList[temp])

    if "Unlock (Cybran)" in AllLevelsListToCheckRegionCreation:
        UnlockCybranPossibleUnitList = ["Prowler", "Sky Slammer", "Tracer"]
        temp = world.random.randrange(0, len(UnlockCybranPossibleUnitList))
        if not UnlockCybranPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(UnlockCybranPossibleUnitList[temp])

    if "Freedom (Cybran)" in AllLevelsListToCheckRegionCreation:
        FreedomCybranPossibleUnitList = ["Prowler", "Sky Slammer", "Tracer"]
        temp = world.random.randrange(0, len(FreedomCybranPossibleUnitList))
        if not FreedomCybranPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomCybranPossibleUnitList[temp])

    if "Artifact (Cybran)" in AllLevelsListToCheckRegionCreation:
        ArtifactCybranPossibleUnitList = ["Mantis"]
        temp = world.random.randrange(0, len(ArtifactCybranPossibleUnitList))
        if not ArtifactCybranPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(ArtifactCybranPossibleUnitList[temp])

    if "Defrag (Cybran)" in AllLevelsListToCheckRegionCreation:
        DefragCybranPossibleUnitList = ["Mantis"]
        temp = world.random.randrange(0, len(DefragCybranPossibleUnitList))
        if not DefragCybranPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(DefragCybranPossibleUnitList[temp])

    if "Mainframe Tango (Cybran)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoCybranPossibleUnitList = ["Mantis"]
        temp = world.random.randrange(0, len(MainframeTangoCybranPossibleUnitList))
        if not MainframeTangoCybranPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(MainframeTangoCybranPossibleUnitList[temp])

    if "Unlock (Cybran)" in AllLevelsListToCheckRegionCreation:
        UnlockCybranPossibleUnitList = ["Mantis"]
        temp = world.random.randrange(0, len(UnlockCybranPossibleUnitList))
        if not UnlockCybranPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(UnlockCybranPossibleUnitList[temp])

    if "Freedom (Cybran)" in AllLevelsListToCheckRegionCreation:
        FreedomCybranPossibleUnitList = ["Mantis"]
        temp = world.random.randrange(0, len(FreedomCybranPossibleUnitList))
        if not FreedomCybranPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomCybranPossibleUnitList[temp])

    if "Artifact (Cybran)" in AllLevelsListToCheckRegionCreation:
        ArtifactCybranPossibleUnitList = ["Rhino", "Cerberus", "Wagner", "Hoplite"]
        temp = world.random.randrange(0, len(ArtifactCybranPossibleUnitList))
        if not ArtifactCybranPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(ArtifactCybranPossibleUnitList[temp])

    if "Defrag (Cybran)" in AllLevelsListToCheckRegionCreation:
        DefragCybranPossibleUnitList = ["Rhino", "Cerberus", "Wagner", "Hoplite"]
        temp = world.random.randrange(0, len(DefragCybranPossibleUnitList))
        if not DefragCybranPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(DefragCybranPossibleUnitList[temp])

    if "Mainframe Tango (Cybran)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoCybranPossibleUnitList = ["Rhino", "Cerberus", "Wagner", "Hoplite"]
        temp = world.random.randrange(0, len(MainframeTangoCybranPossibleUnitList))
        if not MainframeTangoCybranPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(MainframeTangoCybranPossibleUnitList[temp])

    if "Unlock (Cybran)" in AllLevelsListToCheckRegionCreation:
        UnlockCybranPossibleUnitList = ["Rhino", "Cerberus", "Wagner", "Hoplite"]
        temp = world.random.randrange(0, len(UnlockCybranPossibleUnitList))
        if not UnlockCybranPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(UnlockCybranPossibleUnitList[temp])

    if "Freedom (Cybran)" in AllLevelsListToCheckRegionCreation:
        FreedomCybranPossibleUnitList = ["Rhino", "Cerberus", "Wagner", "Hoplite"]
        temp = world.random.randrange(0, len(FreedomCybranPossibleUnitList))
        if not FreedomCybranPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomCybranPossibleUnitList[temp])

    if "Artifact (Cybran)" in AllLevelsListToCheckRegionCreation:
        ArtifactCybranPossibleUnitList = ["Cerberus", "Sliver", "Trident Class", "Cormorant", "Scuttle"]
        temp = world.random.randrange(0, len(ArtifactCybranPossibleUnitList))
        if not ArtifactCybranPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(ArtifactCybranPossibleUnitList[temp])

    if "Defrag (Cybran)" in AllLevelsListToCheckRegionCreation:
        DefragCybranPossibleUnitList = ["Cerberus", "Sliver", "Trident Class", "Cormorant", "Scuttle"]
        temp = world.random.randrange(0, len(DefragCybranPossibleUnitList))
        if not DefragCybranPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(DefragCybranPossibleUnitList[temp])

    if "Mainframe Tango (Cybran)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoCybranPossibleUnitList = ["Cerberus", "Sliver", "Trident Class", "Cormorant", "Scuttle"]
        temp = world.random.randrange(0, len(MainframeTangoCybranPossibleUnitList))
        if not MainframeTangoCybranPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(MainframeTangoCybranPossibleUnitList[temp])

    if "Unlock (Cybran)" in AllLevelsListToCheckRegionCreation:
        UnlockCybranPossibleUnitList = ["Cerberus", "Sliver", "Trident Class", "Cormorant", "Scuttle"]
        temp = world.random.randrange(0, len(UnlockCybranPossibleUnitList))
        if not UnlockCybranPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(UnlockCybranPossibleUnitList[temp])

    if "Freedom (Cybran)" in AllLevelsListToCheckRegionCreation:
        FreedomCybranPossibleUnitList = ["Cerberus", "Sliver", "Trident Class", "Cormorant", "Scuttle"]
        temp = world.random.randrange(0, len(FreedomCybranPossibleUnitList))
        if not FreedomCybranPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomCybranPossibleUnitList[temp])

    if "Artifact (Cybran)" in AllLevelsListToCheckRegionCreation:
        ArtifactCybranPossibleUnitList = ["Salem Class", "Renegade", "Sky Hook", "Gunther", "TML-4"]
        temp = world.random.randrange(0, len(ArtifactCybranPossibleUnitList))
        if not ArtifactCybranPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(ArtifactCybranPossibleUnitList[temp])

    if "Defrag (Cybran)" in AllLevelsListToCheckRegionCreation:
        DefragCybranPossibleUnitList = ["Salem Class", "Renegade", "Sky Hook", "Gunther", "TML-4"]
        temp = world.random.randrange(0, len(DefragCybranPossibleUnitList))
        if not DefragCybranPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(DefragCybranPossibleUnitList[temp])

    if "Mainframe Tango (Cybran)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoCybranPossibleUnitList = ["Salem Class", "Renegade", "Sky Hook", "Gunther", "TML-4"]
        temp = world.random.randrange(0, len(MainframeTangoCybranPossibleUnitList))
        if not MainframeTangoCybranPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(MainframeTangoCybranPossibleUnitList[temp])

    if "Unlock (Cybran)" in AllLevelsListToCheckRegionCreation:
        UnlockCybranPossibleUnitList = ["Salem Class", "Renegade", "Sky Hook", "Gunther", "TML-4"]
        temp = world.random.randrange(0, len(UnlockCybranPossibleUnitList))
        if not UnlockCybranPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(UnlockCybranPossibleUnitList[temp])

    if "Freedom (Cybran)" in AllLevelsListToCheckRegionCreation:
        FreedomCybranPossibleUnitList = ["Salem Class", "Renegade", "Sky Hook", "Gunther", "TML-4"]
        temp = world.random.randrange(0, len(FreedomCybranPossibleUnitList))
        if not FreedomCybranPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomCybranPossibleUnitList[temp])

    if "Defrag (Cybran)" in AllLevelsListToCheckRegionCreation:
        DefragCybranPossibleUnitList = ["Cybran T2 Mass Extractor"]
        temp = world.random.randrange(0, len(DefragCybranPossibleUnitList))
        if not DefragCybranPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(DefragCybranPossibleUnitList[temp])

    if "Mainframe Tango (Cybran)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoCybranPossibleUnitList = ["Cybran T2 Mass Extractor"]
        temp = world.random.randrange(0, len(MainframeTangoCybranPossibleUnitList))
        if not MainframeTangoCybranPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(MainframeTangoCybranPossibleUnitList[temp])

    if "Unlock (Cybran)" in AllLevelsListToCheckRegionCreation:
        UnlockCybranPossibleUnitList = ["Cybran T2 Mass Extractor"]
        temp = world.random.randrange(0, len(UnlockCybranPossibleUnitList))
        if not UnlockCybranPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(UnlockCybranPossibleUnitList[temp])

    if "Freedom (Cybran)" in AllLevelsListToCheckRegionCreation:
        FreedomCybranPossibleUnitList = ["Cybran T2 Mass Extractor"]
        temp = world.random.randrange(0, len(FreedomCybranPossibleUnitList))
        if not FreedomCybranPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomCybranPossibleUnitList[temp])

    if "Defrag (Cybran)" in AllLevelsListToCheckRegionCreation:
        DefragCybranPossibleUnitList = ["Cybran T2 Generator"]
        temp = world.random.randrange(0, len(DefragCybranPossibleUnitList))
        if not DefragCybranPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(DefragCybranPossibleUnitList[temp])

    if "Mainframe Tango (Cybran)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoCybranPossibleUnitList = ["Cybran T2 Generator"]
        temp = world.random.randrange(0, len(MainframeTangoCybranPossibleUnitList))
        if not MainframeTangoCybranPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(MainframeTangoCybranPossibleUnitList[temp])

    if "Unlock (Cybran)" in AllLevelsListToCheckRegionCreation:
        UnlockCybranPossibleUnitList = ["Cybran T2 Generator"]
        temp = world.random.randrange(0, len(UnlockCybranPossibleUnitList))
        if not UnlockCybranPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(UnlockCybranPossibleUnitList[temp])

    if "Freedom (Cybran)" in AllLevelsListToCheckRegionCreation:
        FreedomCybranPossibleUnitList = ["Cybran T2 Generator"]
        temp = world.random.randrange(0, len(FreedomCybranPossibleUnitList))
        if not FreedomCybranPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomCybranPossibleUnitList[temp])

    if "Defrag (Cybran)" in AllLevelsListToCheckRegionCreation:
        DefragCybranPossibleUnitList = ["Burst Master", "Banger"]
        temp = world.random.randrange(0, len(DefragCybranPossibleUnitList))
        if not DefragCybranPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(DefragCybranPossibleUnitList[temp])

    if "Mainframe Tango (Cybran)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoCybranPossibleUnitList = ["Burst Master", "Banger"]
        temp = world.random.randrange(0, len(MainframeTangoCybranPossibleUnitList))
        if not MainframeTangoCybranPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(MainframeTangoCybranPossibleUnitList[temp])

    if "Unlock (Cybran)" in AllLevelsListToCheckRegionCreation:
        UnlockCybranPossibleUnitList = ["Burst Master", "Banger"]
        temp = world.random.randrange(0, len(UnlockCybranPossibleUnitList))
        if not UnlockCybranPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(UnlockCybranPossibleUnitList[temp])

    if "Freedom (Cybran)" in AllLevelsListToCheckRegionCreation:
        FreedomCybranPossibleUnitList = ["Burst Master", "Banger"]
        temp = world.random.randrange(0, len(FreedomCybranPossibleUnitList))
        if not FreedomCybranPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomCybranPossibleUnitList[temp])

    if "Mainframe Tango (Cybran)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoCybranPossibleUnitList = ["Salem Class"]
        temp = world.random.randrange(0, len(MainframeTangoCybranPossibleUnitList))
        if not MainframeTangoCybranPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(MainframeTangoCybranPossibleUnitList[temp])

    if "Unlock (Cybran)" in AllLevelsListToCheckRegionCreation:
        UnlockCybranPossibleUnitList = ["Salem Class"]
        temp = world.random.randrange(0, len(UnlockCybranPossibleUnitList))
        if not UnlockCybranPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(UnlockCybranPossibleUnitList[temp])

    if "Freedom (Cybran)" in AllLevelsListToCheckRegionCreation:
        FreedomCybranPossibleUnitList = ["Salem Class"]
        temp = world.random.randrange(0, len(FreedomCybranPossibleUnitList))
        if not FreedomCybranPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomCybranPossibleUnitList[temp])

    if "Unlock (Cybran)" in AllLevelsListToCheckRegionCreation:
        UnlockCybranPossibleUnitList = ["Cybran T3 Mass Extractor"]
        temp = world.random.randrange(0, len(UnlockCybranPossibleUnitList))
        if not UnlockCybranPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(UnlockCybranPossibleUnitList[temp])

    if "Freedom (Cybran)" in AllLevelsListToCheckRegionCreation:
        FreedomCybranPossibleUnitList = ["Cybran T3 Mass Extractor"]
        temp = world.random.randrange(0, len(FreedomCybranPossibleUnitList))
        if not FreedomCybranPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomCybranPossibleUnitList[temp])

    if "Unlock (Cybran)" in AllLevelsListToCheckRegionCreation:
        UnlockCybranPossibleUnitList = ["Ion Reactor"]
        temp = world.random.randrange(0, len(UnlockCybranPossibleUnitList))
        if not UnlockCybranPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(UnlockCybranPossibleUnitList[temp])

    if "Freedom (Cybran)" in AllLevelsListToCheckRegionCreation:
        FreedomCybranPossibleUnitList = ["Ion Reactor"]
        temp = world.random.randrange(0, len(FreedomCybranPossibleUnitList))
        if not FreedomCybranPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomCybranPossibleUnitList[temp])

    if "Unlock (Cybran)" in AllLevelsListToCheckRegionCreation:
        UnlockCybranPossibleUnitList = [" Loyalist", "The Brick", "Soul Ripper", "Monkeylord", "Megalith", "Scathis", "TML-4", "Disruptor", "Liberator", "Wailer", "Revenant"]
        temp = world.random.randrange(0, len(UnlockCybranPossibleUnitList))
        if not UnlockCybranPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(UnlockCybranPossibleUnitList[temp])

    if "Freedom (Cybran)" in AllLevelsListToCheckRegionCreation:
        FreedomCybranPossibleUnitList = [" Loyalist", "The Brick", "Soul Ripper", "Monkeylord", "Megalith", "Scathis", "TML-4", "Disruptor", "Liberator", "Wailer", "Revenant"]
        temp = world.random.randrange(0, len(FreedomCybranPossibleUnitList))
        if not FreedomCybranPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomCybranPossibleUnitList[temp])

    if "Unlock (Cybran)" in AllLevelsListToCheckRegionCreation:
        UnlockCybranPossibleUnitList = ["Siren Class"]
        temp = world.random.randrange(0, len(UnlockCybranPossibleUnitList))
        if not UnlockCybranPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(UnlockCybranPossibleUnitList[temp])

    if "Freedom (Cybran)" in AllLevelsListToCheckRegionCreation:
        FreedomCybranPossibleUnitList = ["Siren Class"]
        temp = world.random.randrange(0, len(FreedomCybranPossibleUnitList))
        if not FreedomCybranPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomCybranPossibleUnitList[temp])

    if "Unlock (Cybran)" in AllLevelsListToCheckRegionCreation:
        UnlockCybranPossibleUnitList = ["Dragonfly"]
        temp = world.random.randrange(0, len(UnlockCybranPossibleUnitList))
        if not UnlockCybranPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(UnlockCybranPossibleUnitList[temp])

    if "Freedom (Cybran)" in AllLevelsListToCheckRegionCreation:
        FreedomCybranPossibleUnitList = ["Dragonfly"]
        temp = world.random.randrange(0, len(FreedomCybranPossibleUnitList))
        if not FreedomCybranPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomCybranPossibleUnitList[temp])

    if "Unlock (Cybran)" in AllLevelsListToCheckRegionCreation:
        UnlockCybranPossibleUnitList = ["Gemini", "Bouncer", "Myrmidon"]
        temp = world.random.randrange(0, len(UnlockCybranPossibleUnitList))
        if not UnlockCybranPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(UnlockCybranPossibleUnitList[temp])

    if "Freedom (Cybran)" in AllLevelsListToCheckRegionCreation:
        FreedomCybranPossibleUnitList = ["Gemini", "Bouncer", "Myrmidon"]
        temp = world.random.randrange(0, len(FreedomCybranPossibleUnitList))
        if not FreedomCybranPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomCybranPossibleUnitList[temp])

    if "Freedom (Cybran)" in AllLevelsListToCheckRegionCreation:
        FreedomCybranPossibleUnitList = ["Summoner"]
        temp = world.random.randrange(0, len(FreedomCybranPossibleUnitList))
        if not FreedomCybranPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomCybranPossibleUnitList[temp])

    if "Freedom (Cybran)" in AllLevelsListToCheckRegionCreation:
        FreedomCybranPossibleUnitList = ["Loyalist", "The Brick", "Soul Ripper", "Monkeylord", "Megalith", "Wailer", "Revenant"]
        temp = world.random.randrange(0, len(FreedomCybranPossibleUnitList))
        if not FreedomCybranPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomCybranPossibleUnitList[temp])

    if "Liberation (Aeon)" in AllLevelsListToCheckRegionCreation:
        LiberationAeonPossibleUnitList = ["Shimmer"]
        temp = world.random.randrange(0, len(LiberationAeonPossibleUnitList))
        if not LiberationAeonPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(LiberationAeonPossibleUnitList[temp])

    if "Artifact (Aeon)" in AllLevelsListToCheckRegionCreation:
        ArtifactAeonPossibleUnitList = ["Shimmer"]
        temp = world.random.randrange(0, len(ArtifactAeonPossibleUnitList))
        if not ArtifactAeonPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(ArtifactAeonPossibleUnitList[temp])

    if "Defrag (Aeon)" in AllLevelsListToCheckRegionCreation:
        DefragAeonPossibleUnitList = ["Shimmer"]
        temp = world.random.randrange(0, len(DefragAeonPossibleUnitList))
        if not DefragAeonPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(DefragAeonPossibleUnitList[temp])

    if "Mainframe Tango (Aeon)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoAeonPossibleUnitList = ["Shimmer"]
        temp = world.random.randrange(0, len(MainframeTangoAeonPossibleUnitList))
        if not MainframeTangoAeonPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(MainframeTangoAeonPossibleUnitList[temp])

    if "Unlock (Aeon)" in AllLevelsListToCheckRegionCreation:
        UnlockAeonPossibleUnitList = ["Shimmer"]
        temp = world.random.randrange(0, len(UnlockAeonPossibleUnitList))
        if not UnlockAeonPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(UnlockAeonPossibleUnitList[temp])

    if "Freedom (Aeon)" in AllLevelsListToCheckRegionCreation:
        FreedomAeonPossibleUnitList = ["Shimmer"]
        temp = world.random.randrange(0, len(FreedomAeonPossibleUnitList))
        if not FreedomAeonPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomAeonPossibleUnitList[temp])

    if "Liberation (Aeon)" in AllLevelsListToCheckRegionCreation:
        LiberationAeonPossibleUnitList = ["Conservator", "Thisle", "Seeker"]
        temp = world.random.randrange(0, len(LiberationAeonPossibleUnitList))
        if not LiberationAeonPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(LiberationAeonPossibleUnitList[temp])

    if "Artifact (Aeon)" in AllLevelsListToCheckRegionCreation:
        ArtifactAeonPossibleUnitList = ["Conservator", "Thisle", "Seeker"]
        temp = world.random.randrange(0, len(ArtifactAeonPossibleUnitList))
        if not ArtifactAeonPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(ArtifactAeonPossibleUnitList[temp])

    if "Defrag (Aeon)" in AllLevelsListToCheckRegionCreation:
        DefragAeonPossibleUnitList = ["Conservator", "Thisle", "Seeker"]
        temp = world.random.randrange(0, len(DefragAeonPossibleUnitList))
        if not DefragAeonPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(DefragAeonPossibleUnitList[temp])

    if "Mainframe Tango (Aeon)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoAeonPossibleUnitList = ["Conservator", "Thisle", "Seeker"]
        temp = world.random.randrange(0, len(MainframeTangoAeonPossibleUnitList))
        if not MainframeTangoAeonPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(MainframeTangoAeonPossibleUnitList[temp])

    if "Unlock (Aeon)" in AllLevelsListToCheckRegionCreation:
        UnlockAeonPossibleUnitList = ["Conservator", "Thisle", "Seeker"]
        temp = world.random.randrange(0, len(UnlockAeonPossibleUnitList))
        if not UnlockAeonPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(UnlockAeonPossibleUnitList[temp])

    if "Freedom (Aeon)" in AllLevelsListToCheckRegionCreation:
        FreedomAeonPossibleUnitList = ["Conservator", "Thisle", "Seeker"]
        temp = world.random.randrange(0, len(FreedomAeonPossibleUnitList))
        if not FreedomAeonPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomAeonPossibleUnitList[temp])

    if "Artifact (Aeon)" in AllLevelsListToCheckRegionCreation:
        ArtifactAeonPossibleUnitList = ["Aurora"]
        temp = world.random.randrange(0, len(ArtifactAeonPossibleUnitList))
        if not ArtifactAeonPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(ArtifactAeonPossibleUnitList[temp])

    if "Defrag (Aeon)" in AllLevelsListToCheckRegionCreation:
        DefragAeonPossibleUnitList = ["Aurora"]
        temp = world.random.randrange(0, len(DefragAeonPossibleUnitList))
        if not DefragAeonPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(DefragAeonPossibleUnitList[temp])

    if "Mainframe Tango (Aeon)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoAeonPossibleUnitList = ["Aurora"]
        temp = world.random.randrange(0, len(MainframeTangoAeonPossibleUnitList))
        if not MainframeTangoAeonPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(MainframeTangoAeonPossibleUnitList[temp])

    if "Unlock (Aeon)" in AllLevelsListToCheckRegionCreation:
        UnlockAeonPossibleUnitList = ["Aurora"]
        temp = world.random.randrange(0, len(UnlockAeonPossibleUnitList))
        if not UnlockAeonPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(UnlockAeonPossibleUnitList[temp])

    if "Freedom (Aeon)" in AllLevelsListToCheckRegionCreation:
        FreedomAeonPossibleUnitList = ["Aurora"]
        temp = world.random.randrange(0, len(FreedomAeonPossibleUnitList))
        if not FreedomAeonPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomAeonPossibleUnitList[temp])

    if "Artifact (Aeon)" in AllLevelsListToCheckRegionCreation:
        ArtifactAeonPossibleUnitList = ["Obsidian", "Oblivion", "Blaze"]
        temp = world.random.randrange(0, len(ArtifactAeonPossibleUnitList))
        if not ArtifactAeonPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(ArtifactAeonPossibleUnitList[temp])

    if "Defrag (Aeon)" in AllLevelsListToCheckRegionCreation:
        DefragAeonPossibleUnitList = ["Obsidian", "Oblivion", "Blaze"]
        temp = world.random.randrange(0, len(DefragAeonPossibleUnitList))
        if not DefragAeonPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(DefragAeonPossibleUnitList[temp])

    if "Mainframe Tango (Aeon)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoAeonPossibleUnitList = ["Obsidian", "Oblivion", "Blaze"]
        temp = world.random.randrange(0, len(MainframeTangoAeonPossibleUnitList))
        if not MainframeTangoAeonPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(MainframeTangoAeonPossibleUnitList[temp])

    if "Unlock (Aeon)" in AllLevelsListToCheckRegionCreation:
        UnlockAeonPossibleUnitList = ["Obsidian", "Oblivion", "Blaze"]
        temp = world.random.randrange(0, len(UnlockAeonPossibleUnitList))
        if not UnlockAeonPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(UnlockAeonPossibleUnitList[temp])

    if "Freedom (Aeon)" in AllLevelsListToCheckRegionCreation:
        FreedomAeonPossibleUnitList = ["Obsidian", "Oblivion", "Blaze"]
        temp = world.random.randrange(0, len(FreedomAeonPossibleUnitList))
        if not FreedomAeonPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomAeonPossibleUnitList[temp])

    if "Artifact (Aeon)" in AllLevelsListToCheckRegionCreation:
        ArtifactAeonPossibleUnitList = ["Oblivion", "Sylph", "Beacon Class", "Skimmer", "Tide"]
        temp = world.random.randrange(0, len(ArtifactAeonPossibleUnitList))
        if not ArtifactAeonPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(ArtifactAeonPossibleUnitList[temp])

    if "Defrag (Aeon)" in AllLevelsListToCheckRegionCreation:
        DefragAeonPossibleUnitList = ["Oblivion", "Sylph", "Beacon Class", "Skimmer", "Tide"]
        temp = world.random.randrange(0, len(DefragAeonPossibleUnitList))
        if not DefragAeonPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(DefragAeonPossibleUnitList[temp])

    if "Mainframe Tango (Aeon)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoAeonPossibleUnitList = ["Oblivion", "Sylph", "Beacon Class", "Skimmer", "Tide"]
        temp = world.random.randrange(0, len(MainframeTangoAeonPossibleUnitList))
        if not MainframeTangoAeonPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(MainframeTangoAeonPossibleUnitList[temp])

    if "Unlock (Aeon)" in AllLevelsListToCheckRegionCreation:
        UnlockAeonPossibleUnitList = ["Oblivion", "Sylph", "Beacon Class", "Skimmer", "Tide"]
        temp = world.random.randrange(0, len(UnlockAeonPossibleUnitList))
        if not UnlockAeonPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(UnlockAeonPossibleUnitList[temp])

    if "Freedom (Aeon)" in AllLevelsListToCheckRegionCreation:
        FreedomAeonPossibleUnitList = ["Oblivion", "Sylph", "Beacon Class", "Skimmer", "Tide"]
        temp = world.random.randrange(0, len(FreedomAeonPossibleUnitList))
        if not FreedomAeonPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomAeonPossibleUnitList[temp])

    if "Artifact (Aeon)" in AllLevelsListToCheckRegionCreation:
        ArtifactAeonPossibleUnitList = ["Exodus Class", "Specter", "Mercy", "Chariot", "Miasma", "Serpentine"]
        temp = world.random.randrange(0, len(ArtifactAeonPossibleUnitList))
        if not ArtifactAeonPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(ArtifactAeonPossibleUnitList[temp])

    if "Defrag (Aeon)" in AllLevelsListToCheckRegionCreation:
        DefragAeonPossibleUnitList = ["Exodus Class", "Specter", "Mercy", "Chariot", "Miasma", "Serpentine"]
        temp = world.random.randrange(0, len(DefragAeonPossibleUnitList))
        if not DefragAeonPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(DefragAeonPossibleUnitList[temp])

    if "Mainframe Tango (Aeon)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoAeonPossibleUnitList = ["Exodus Class", "Specter", "Mercy", "Chariot", "Miasma", "Serpentine"]
        temp = world.random.randrange(0, len(MainframeTangoAeonPossibleUnitList))
        if not MainframeTangoAeonPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(MainframeTangoAeonPossibleUnitList[temp])

    if "Unlock (Aeon)" in AllLevelsListToCheckRegionCreation:
        UnlockAeonPossibleUnitList = ["Exodus Class", "Specter", "Mercy", "Chariot", "Miasma", "Serpentine"]
        temp = world.random.randrange(0, len(UnlockAeonPossibleUnitList))
        if not UnlockAeonPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(UnlockAeonPossibleUnitList[temp])

    if "Freedom (Aeon)" in AllLevelsListToCheckRegionCreation:
        FreedomAeonPossibleUnitList = ["Exodus Class", "Specter", "Mercy", "Chariot", "Miasma", "Serpentine"]
        temp = world.random.randrange(0, len(FreedomAeonPossibleUnitList))
        if not FreedomAeonPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomAeonPossibleUnitList[temp])

    if "Defrag (Aeon)" in AllLevelsListToCheckRegionCreation:
        DefragAeonPossibleUnitList = ["Aeon T2 Mass Extractor"]
        temp = world.random.randrange(0, len(DefragAeonPossibleUnitList))
        if not DefragAeonPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(DefragAeonPossibleUnitList[temp])

    if "Mainframe Tango (Aeon)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoAeonPossibleUnitList = ["Aeon T2 Mass Extractor"]
        temp = world.random.randrange(0, len(MainframeTangoAeonPossibleUnitList))
        if not MainframeTangoAeonPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(MainframeTangoAeonPossibleUnitList[temp])

    if "Unlock (Aeon)" in AllLevelsListToCheckRegionCreation:
        UnlockAeonPossibleUnitList = ["Aeon T2 Mass Extractor"]
        temp = world.random.randrange(0, len(UnlockAeonPossibleUnitList))
        if not UnlockAeonPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(UnlockAeonPossibleUnitList[temp])

    if "Freedom (Aeon)" in AllLevelsListToCheckRegionCreation:
        FreedomAeonPossibleUnitList = ["Aeon T2 Mass Extractor"]
        temp = world.random.randrange(0, len(FreedomAeonPossibleUnitList))
        if not FreedomAeonPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomAeonPossibleUnitList[temp])

    if "Defrag (Aeon)" in AllLevelsListToCheckRegionCreation:
        DefragAeonPossibleUnitList = ["Aeon T2 Generator"]
        temp = world.random.randrange(0, len(DefragAeonPossibleUnitList))
        if not DefragAeonPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(DefragAeonPossibleUnitList[temp])

    if "Mainframe Tango (Aeon)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoAeonPossibleUnitList = ["Aeon T2 Generator"]
        temp = world.random.randrange(0, len(MainframeTangoAeonPossibleUnitList))
        if not MainframeTangoAeonPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(MainframeTangoAeonPossibleUnitList[temp])

    if "Unlock (Aeon)" in AllLevelsListToCheckRegionCreation:
        UnlockAeonPossibleUnitList = ["Aeon T2 Generator"]
        temp = world.random.randrange(0, len(UnlockAeonPossibleUnitList))
        if not UnlockAeonPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(UnlockAeonPossibleUnitList[temp])

    if "Freedom (Aeon)" in AllLevelsListToCheckRegionCreation:
        FreedomAeonPossibleUnitList = ["Aeon T2 Generator"]
        temp = world.random.randrange(0, len(FreedomAeonPossibleUnitList))
        if not FreedomAeonPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomAeonPossibleUnitList[temp])

    if "Defrag (Aeon)" in AllLevelsListToCheckRegionCreation:
        DefragAeonPossibleUnitList = ["Marr", "Ascendant"]
        temp = world.random.randrange(0, len(DefragAeonPossibleUnitList))
        if not DefragAeonPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(DefragAeonPossibleUnitList[temp])

    if "Mainframe Tango (Aeon)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoAeonPossibleUnitList = ["Marr", "Ascendant"]
        temp = world.random.randrange(0, len(MainframeTangoAeonPossibleUnitList))
        if not MainframeTangoAeonPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(MainframeTangoAeonPossibleUnitList[temp])

    if "Unlock (Aeon)" in AllLevelsListToCheckRegionCreation:
        UnlockAeonPossibleUnitList = ["Marr", "Ascendant"]
        temp = world.random.randrange(0, len(UnlockAeonPossibleUnitList))
        if not UnlockAeonPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(UnlockAeonPossibleUnitList[temp])

    if "Freedom (Aeon)" in AllLevelsListToCheckRegionCreation:
        FreedomAeonPossibleUnitList = ["Marr", "Ascendant"]
        temp = world.random.randrange(0, len(FreedomAeonPossibleUnitList))
        if not FreedomAeonPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomAeonPossibleUnitList[temp])

    if "Mainframe Tango (Aeon)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoAeonPossibleUnitList = ["Exodus Class"]
        temp = world.random.randrange(0, len(MainframeTangoAeonPossibleUnitList))
        if not MainframeTangoAeonPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(MainframeTangoAeonPossibleUnitList[temp])

    if "Unlock (Aeon)" in AllLevelsListToCheckRegionCreation:
        UnlockAeonPossibleUnitList = ["Exodus Class"]
        temp = world.random.randrange(0, len(UnlockAeonPossibleUnitList))
        if not UnlockAeonPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(UnlockAeonPossibleUnitList[temp])

    if "Freedom (Aeon)" in AllLevelsListToCheckRegionCreation:
        FreedomAeonPossibleUnitList = ["Exodus Class"]
        temp = world.random.randrange(0, len(FreedomAeonPossibleUnitList))
        if not FreedomAeonPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomAeonPossibleUnitList[temp])

    if "Unlock (Aeon)" in AllLevelsListToCheckRegionCreation:
        UnlockAeonPossibleUnitList = ["Aeon T3 Mass Extractor"]
        temp = world.random.randrange(0, len(UnlockAeonPossibleUnitList))
        if not UnlockAeonPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(UnlockAeonPossibleUnitList[temp])

    if "Freedom (Aeon)" in AllLevelsListToCheckRegionCreation:
        FreedomAeonPossibleUnitList = ["Aeon T3 Mass Extractor"]
        temp = world.random.randrange(0, len(FreedomAeonPossibleUnitList))
        if not FreedomAeonPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomAeonPossibleUnitList[temp])

    if "Unlock (Aeon)" in AllLevelsListToCheckRegionCreation:
        UnlockAeonPossibleUnitList = ["Quantum Reactor"]
        temp = world.random.randrange(0, len(UnlockAeonPossibleUnitList))
        if not UnlockAeonPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(UnlockAeonPossibleUnitList[temp])

    if "Freedom (Aeon)" in AllLevelsListToCheckRegionCreation:
        FreedomAeonPossibleUnitList = ["Quantum Reactor"]
        temp = world.random.randrange(0, len(FreedomAeonPossibleUnitList))
        if not FreedomAeonPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomAeonPossibleUnitList[temp])

    if "Unlock (Aeon)" in AllLevelsListToCheckRegionCreation:
        UnlockAeonPossibleUnitList = ["Sprite Striker", "Harbringer Mk4", "Czar", "Galactic Colossus", "Salvation", "Serpentine", "Emissary", "Apocalypse", "Restorer", "Shocker"]
        temp = world.random.randrange(0, len(UnlockAeonPossibleUnitList))
        if not UnlockAeonPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(UnlockAeonPossibleUnitList[temp])

    if "Freedom (Aeon)" in AllLevelsListToCheckRegionCreation:
        FreedomAeonPossibleUnitList = ["Sprite Striker", "Harbringer Mk4", "Czar", "Galactic Colossus", "Salvation", "Serpentine", "Emissary", "Apocalypse", "Restorer", "Shocker"]
        temp = world.random.randrange(0, len(FreedomAeonPossibleUnitList))
        if not FreedomAeonPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomAeonPossibleUnitList[temp])

    if "Unlock (Aeon)" in AllLevelsListToCheckRegionCreation:
        UnlockAeonPossibleUnitList = ["Infinity Class"]
        temp = world.random.randrange(0, len(UnlockAeonPossibleUnitList))
        if not UnlockAeonPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(UnlockAeonPossibleUnitList[temp])

    if "Freedom (Aeon)" in AllLevelsListToCheckRegionCreation:
        FreedomAeonPossibleUnitList = ["Infinity Class"]
        temp = world.random.randrange(0, len(FreedomAeonPossibleUnitList))
        if not FreedomAeonPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomAeonPossibleUnitList[temp])

    if "Unlock (Aeon)" in AllLevelsListToCheckRegionCreation:
        UnlockAeonPossibleUnitList = ["Aluminar"]
        temp = world.random.randrange(0, len(UnlockAeonPossibleUnitList))
        if not UnlockAeonPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(UnlockAeonPossibleUnitList[temp])

    if "Freedom (Aeon)" in AllLevelsListToCheckRegionCreation:
        FreedomAeonPossibleUnitList = ["Aluminar"]
        temp = world.random.randrange(0, len(FreedomAeonPossibleUnitList))
        if not FreedomAeonPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomAeonPossibleUnitList[temp])

    if "Unlock (Aeon)" in AllLevelsListToCheckRegionCreation:
        UnlockAeonPossibleUnitList = ["Corona", "Redeemer", "Transcender"]
        temp = world.random.randrange(0, len(UnlockAeonPossibleUnitList))
        if not UnlockAeonPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(UnlockAeonPossibleUnitList[temp])

    if "Freedom (Aeon)" in AllLevelsListToCheckRegionCreation:
        FreedomAeonPossibleUnitList = ["Corona", "Redeemer", "Transcender"]
        temp = world.random.randrange(0, len(FreedomAeonPossibleUnitList))
        if not FreedomAeonPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomAeonPossibleUnitList[temp])

    if "Freedom (Aeon)" in AllLevelsListToCheckRegionCreation:
        FreedomAeonPossibleUnitList = ["Portal"]
        temp = world.random.randrange(0, len(FreedomAeonPossibleUnitList))
        if not FreedomAeonPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomAeonPossibleUnitList[temp])

    if "Freedom (Aeon)" in AllLevelsListToCheckRegionCreation:
        FreedomAeonPossibleUnitList = ["Sprite Striker", "Harbringer Mk4", "Czar", "Galactic Colossus", "Restorer", "Shocker"]
        temp = world.random.randrange(0, len(FreedomAeonPossibleUnitList))
        if not FreedomAeonPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomAeonPossibleUnitList[temp])

    if "Liberation (Sera)" in AllLevelsListToCheckRegionCreation:
        LiberationSeraPossibleUnitList = ["Sinnve"]
        temp = world.random.randrange(0, len(LiberationSeraPossibleUnitList))
        if not LiberationSeraPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(LiberationSeraPossibleUnitList[temp])

    if "Artifact (Sera)" in AllLevelsListToCheckRegionCreation:
        ArtifactSeraPossibleUnitList = ["Sinnve"]
        temp = world.random.randrange(0, len(ArtifactSeraPossibleUnitList))
        if not ArtifactSeraPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(ArtifactSeraPossibleUnitList[temp])

    if "Defrag (Sera)" in AllLevelsListToCheckRegionCreation:
        DefragSeraPossibleUnitList = ["Sinnve"]
        temp = world.random.randrange(0, len(DefragSeraPossibleUnitList))
        if not DefragSeraPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(DefragSeraPossibleUnitList[temp])

    if "Mainframe Tango (Sera)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoSeraPossibleUnitList = ["Sinnve"]
        temp = world.random.randrange(0, len(MainframeTangoSeraPossibleUnitList))
        if not MainframeTangoSeraPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(MainframeTangoSeraPossibleUnitList[temp])

    if "Unlock (Sera)" in AllLevelsListToCheckRegionCreation:
        UnlockSeraPossibleUnitList = ["Sinnve"]
        temp = world.random.randrange(0, len(UnlockSeraPossibleUnitList))
        if not UnlockSeraPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(UnlockSeraPossibleUnitList[temp])

    if "Freedom (Sera)" in AllLevelsListToCheckRegionCreation:
        FreedomSeraPossibleUnitList = ["Sinnve"]
        temp = world.random.randrange(0, len(FreedomSeraPossibleUnitList))
        if not FreedomSeraPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomSeraPossibleUnitList[temp])

    if "Liberation (Sera)" in AllLevelsListToCheckRegionCreation:
        LiberationSeraPossibleUnitList = ["Ia-atha", "Ia-istle", "Ialla"]
        temp = world.random.randrange(0, len(LiberationSeraPossibleUnitList))
        if not LiberationSeraPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(LiberationSeraPossibleUnitList[temp])

    if "Artifact (Sera)" in AllLevelsListToCheckRegionCreation:
        ArtifactSeraPossibleUnitList = ["Ia-atha", "Ia-istle", "Ialla"]
        temp = world.random.randrange(0, len(ArtifactSeraPossibleUnitList))
        if not ArtifactSeraPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(ArtifactSeraPossibleUnitList[temp])

    if "Defrag (Sera)" in AllLevelsListToCheckRegionCreation:
        DefragSeraPossibleUnitList = ["Ia-atha", "Ia-istle", "Ialla"]
        temp = world.random.randrange(0, len(DefragSeraPossibleUnitList))
        if not DefragSeraPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(DefragSeraPossibleUnitList[temp])

    if "Mainframe Tango (Sera)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoSeraPossibleUnitList = ["Ia-atha", "Ia-istle", "Ialla"]
        temp = world.random.randrange(0, len(MainframeTangoSeraPossibleUnitList))
        if not MainframeTangoSeraPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(MainframeTangoSeraPossibleUnitList[temp])

    if "Unlock (Sera)" in AllLevelsListToCheckRegionCreation:
        UnlockSeraPossibleUnitList = ["Ia-atha", "Ia-istle", "Ialla"]
        temp = world.random.randrange(0, len(UnlockSeraPossibleUnitList))
        if not UnlockSeraPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(UnlockSeraPossibleUnitList[temp])

    if "Freedom (Sera)" in AllLevelsListToCheckRegionCreation:
        FreedomSeraPossibleUnitList = ["Ia-atha", "Ia-istle", "Ialla"]
        temp = world.random.randrange(0, len(FreedomSeraPossibleUnitList))
        if not FreedomSeraPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomSeraPossibleUnitList[temp])

    if "Artifact (Sera)" in AllLevelsListToCheckRegionCreation:
        ArtifactSeraPossibleUnitList = ["Thaam"]
        temp = world.random.randrange(0, len(ArtifactSeraPossibleUnitList))
        if not ArtifactSeraPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(ArtifactSeraPossibleUnitList[temp])

    if "Defrag (Sera)" in AllLevelsListToCheckRegionCreation:
        DefragSeraPossibleUnitList = ["Thaam"]
        temp = world.random.randrange(0, len(DefragSeraPossibleUnitList))
        if not DefragSeraPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(DefragSeraPossibleUnitList[temp])

    if "Mainframe Tango (Sera)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoSeraPossibleUnitList = ["Thaam"]
        temp = world.random.randrange(0, len(MainframeTangoSeraPossibleUnitList))
        if not MainframeTangoSeraPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(MainframeTangoSeraPossibleUnitList[temp])

    if "Unlock (Sera)" in AllLevelsListToCheckRegionCreation:
        UnlockSeraPossibleUnitList = ["Thaam"]
        temp = world.random.randrange(0, len(UnlockSeraPossibleUnitList))
        if not UnlockSeraPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(UnlockSeraPossibleUnitList[temp])

    if "Freedom (Sera)" in AllLevelsListToCheckRegionCreation:
        FreedomSeraPossibleUnitList = ["Thaam"]
        temp = world.random.randrange(0, len(FreedomSeraPossibleUnitList))
        if not FreedomSeraPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomSeraPossibleUnitList[temp])

    if "Artifact (Sera)" in AllLevelsListToCheckRegionCreation:
        ArtifactSeraPossibleUnitList = ["Ilshavoh", "Yenzyne", "Uttaushala"]
        temp = world.random.randrange(0, len(ArtifactSeraPossibleUnitList))
        if not ArtifactSeraPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(ArtifactSeraPossibleUnitList[temp])

    if "Defrag (Sera)" in AllLevelsListToCheckRegionCreation:
        DefragSeraPossibleUnitList = ["Ilshavoh", "Yenzyne", "Uttaushala"]
        temp = world.random.randrange(0, len(DefragSeraPossibleUnitList))
        if not DefragSeraPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(DefragSeraPossibleUnitList[temp])

    if "Mainframe Tango (Sera)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoSeraPossibleUnitList = ["Ilshavoh", "Yenzyne", "Uttaushala"]
        temp = world.random.randrange(0, len(MainframeTangoSeraPossibleUnitList))
        if not MainframeTangoSeraPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(MainframeTangoSeraPossibleUnitList[temp])

    if "Unlock (Sera)" in AllLevelsListToCheckRegionCreation:
        UnlockSeraPossibleUnitList = ["Ilshavoh", "Yenzyne", "Uttaushala"]
        temp = world.random.randrange(0, len(UnlockSeraPossibleUnitList))
        if not UnlockSeraPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(UnlockSeraPossibleUnitList[temp])

    if "Freedom (Sera)" in AllLevelsListToCheckRegionCreation:
        FreedomSeraPossibleUnitList = ["Ilshavoh", "Yenzyne", "Uttaushala"]
        temp = world.random.randrange(0, len(FreedomSeraPossibleUnitList))
        if not FreedomSeraPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomSeraPossibleUnitList[temp])

    if "Artifact (Sera)" in AllLevelsListToCheckRegionCreation:
        ArtifactSeraPossibleUnitList = ["Uttaushala", "Sou-istle", "Hau-esel", "Uosioz", "Sou-atha"]
        temp = world.random.randrange(0, len(ArtifactSeraPossibleUnitList))
        if not ArtifactSeraPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(ArtifactSeraPossibleUnitList[temp])

    if "Defrag (Sera)" in AllLevelsListToCheckRegionCreation:
        DefragSeraPossibleUnitList = ["Uttaushala", "Sou-istle", "Hau-esel", "Uosioz", "Sou-atha"]
        temp = world.random.randrange(0, len(DefragSeraPossibleUnitList))
        if not DefragSeraPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(DefragSeraPossibleUnitList[temp])

    if "Mainframe Tango (Sera)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoSeraPossibleUnitList = ["Uttaushala", "Sou-istle", "Hau-esel", "Uosioz", "Sou-atha"]
        temp = world.random.randrange(0, len(MainframeTangoSeraPossibleUnitList))
        if not MainframeTangoSeraPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(MainframeTangoSeraPossibleUnitList[temp])

    if "Unlock (Sera)" in AllLevelsListToCheckRegionCreation:
        UnlockSeraPossibleUnitList = ["Uttaushala", "Sou-istle", "Hau-esel", "Uosioz", "Sou-atha"]
        temp = world.random.randrange(0, len(UnlockSeraPossibleUnitList))
        if not UnlockSeraPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(UnlockSeraPossibleUnitList[temp])

    if "Freedom (Sera)" in AllLevelsListToCheckRegionCreation:
        FreedomSeraPossibleUnitList = ["Uttaushala", "Sou-istle", "Hau-esel", "Uosioz", "Sou-atha"]
        temp = world.random.randrange(0, len(FreedomSeraPossibleUnitList))
        if not FreedomSeraPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomSeraPossibleUnitList[temp])

    if "Artifact (Sera)" in AllLevelsListToCheckRegionCreation:
        ArtifactSeraPossibleUnitList = ["Uashavoh", "Ithalua", "Vulthoo", "Vish", "Zthuthaam", "Ythis"]
        temp = world.random.randrange(0, len(ArtifactSeraPossibleUnitList))
        if not ArtifactSeraPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(ArtifactSeraPossibleUnitList[temp])

    if "Defrag (Sera)" in AllLevelsListToCheckRegionCreation:
        DefragSeraPossibleUnitList = ["Uashavoh", "Ithalua", "Vulthoo", "Vish", "Zthuthaam", "Ythis"]
        temp = world.random.randrange(0, len(DefragSeraPossibleUnitList))
        if not DefragSeraPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(DefragSeraPossibleUnitList[temp])

    if "Mainframe Tango (Sera)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoSeraPossibleUnitList = ["Uashavoh", "Ithalua", "Vulthoo", "Vish", "Zthuthaam", "Ythis"]
        temp = world.random.randrange(0, len(MainframeTangoSeraPossibleUnitList))
        if not MainframeTangoSeraPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(MainframeTangoSeraPossibleUnitList[temp])

    if "Unlock (Sera)" in AllLevelsListToCheckRegionCreation:
        UnlockSeraPossibleUnitList = ["Uashavoh", "Ithalua", "Vulthoo", "Vish", "Zthuthaam", "Ythis"]
        temp = world.random.randrange(0, len(UnlockSeraPossibleUnitList))
        if not UnlockSeraPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(UnlockSeraPossibleUnitList[temp])

    if "Freedom (Sera)" in AllLevelsListToCheckRegionCreation:
        FreedomSeraPossibleUnitList = ["Uashavoh", "Ithalua", "Vulthoo", "Vish", "Zthuthaam", "Ythis"]
        temp = world.random.randrange(0, len(FreedomSeraPossibleUnitList))
        if not FreedomSeraPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomSeraPossibleUnitList[temp])

    if "Defrag (Sera)" in AllLevelsListToCheckRegionCreation:
        DefragSeraPossibleUnitList = ["Sera T2 Mass Extractor"]
        temp = world.random.randrange(0, len(DefragSeraPossibleUnitList))
        if not DefragSeraPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(DefragSeraPossibleUnitList[temp])

    if "Mainframe Tango (Sera)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoSeraPossibleUnitList = ["Sera T2 Mass Extractor"]
        temp = world.random.randrange(0, len(MainframeTangoSeraPossibleUnitList))
        if not MainframeTangoSeraPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(MainframeTangoSeraPossibleUnitList[temp])

    if "Unlock (Sera)" in AllLevelsListToCheckRegionCreation:
        UnlockSeraPossibleUnitList = ["Sera T2 Mass Extractor"]
        temp = world.random.randrange(0, len(UnlockSeraPossibleUnitList))
        if not UnlockSeraPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(UnlockSeraPossibleUnitList[temp])

    if "Freedom (Sera)" in AllLevelsListToCheckRegionCreation:
        FreedomSeraPossibleUnitList = ["Sera T2 Mass Extractor"]
        temp = world.random.randrange(0, len(FreedomSeraPossibleUnitList))
        if not FreedomSeraPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomSeraPossibleUnitList[temp])

    if "Defrag (Sera)" in AllLevelsListToCheckRegionCreation:
        DefragSeraPossibleUnitList = ["Sera T2 Generator"]
        temp = world.random.randrange(0, len(DefragSeraPossibleUnitList))
        if not DefragSeraPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(DefragSeraPossibleUnitList[temp])

    if "Mainframe Tango (Sera)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoSeraPossibleUnitList = ["Sera T2 Generator"]
        temp = world.random.randrange(0, len(MainframeTangoSeraPossibleUnitList))
        if not MainframeTangoSeraPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(MainframeTangoSeraPossibleUnitList[temp])

    if "Unlock (Sera)" in AllLevelsListToCheckRegionCreation:
        UnlockSeraPossibleUnitList = ["Sera T2 Generator"]
        temp = world.random.randrange(0, len(UnlockSeraPossibleUnitList))
        if not UnlockSeraPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(UnlockSeraPossibleUnitList[temp])

    if "Freedom (Sera)" in AllLevelsListToCheckRegionCreation:
        FreedomSeraPossibleUnitList = ["Sera T2 Generator"]
        temp = world.random.randrange(0, len(FreedomSeraPossibleUnitList))
        if not FreedomSeraPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomSeraPossibleUnitList[temp])

    if "Defrag (Sera)" in AllLevelsListToCheckRegionCreation:
        DefragSeraPossibleUnitList = ["Iashavoh", "Sinnatha"]
        temp = world.random.randrange(0, len(DefragSeraPossibleUnitList))
        if not DefragSeraPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(DefragSeraPossibleUnitList[temp])

    if "Mainframe Tango (Sera)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoSeraPossibleUnitList = ["Iashavoh", "Sinnatha"]
        temp = world.random.randrange(0, len(MainframeTangoSeraPossibleUnitList))
        if not MainframeTangoSeraPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(MainframeTangoSeraPossibleUnitList[temp])

    if "Unlock (Sera)" in AllLevelsListToCheckRegionCreation:
        UnlockSeraPossibleUnitList = ["Iashavoh", "Sinnatha"]
        temp = world.random.randrange(0, len(UnlockSeraPossibleUnitList))
        if not UnlockSeraPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(UnlockSeraPossibleUnitList[temp])

    if "Freedom (Sera)" in AllLevelsListToCheckRegionCreation:
        FreedomSeraPossibleUnitList = ["Iashavoh", "Sinnatha"]
        temp = world.random.randrange(0, len(FreedomSeraPossibleUnitList))
        if not FreedomSeraPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomSeraPossibleUnitList[temp])

    if "Mainframe Tango (Sera)" in AllLevelsListToCheckRegionCreation:
        MainframeTangoSeraPossibleUnitList = ["Uashavoh", "Ithalua"]
        temp = world.random.randrange(0, len(MainframeTangoSeraPossibleUnitList))
        if not MainframeTangoSeraPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(MainframeTangoSeraPossibleUnitList[temp])

    if "Unlock (Sera)" in AllLevelsListToCheckRegionCreation:
        UnlockSeraPossibleUnitList = ["Uashavoh", "Ithalua"]
        temp = world.random.randrange(0, len(UnlockSeraPossibleUnitList))
        if not UnlockSeraPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(UnlockSeraPossibleUnitList[temp])

    if "Freedom (Sera)" in AllLevelsListToCheckRegionCreation:
        FreedomSeraPossibleUnitList = ["Uashavoh", "Ithalua"]
        temp = world.random.randrange(0, len(FreedomSeraPossibleUnitList))
        if not FreedomSeraPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomSeraPossibleUnitList[temp])

    if "Unlock (Sera)" in AllLevelsListToCheckRegionCreation:
        UnlockSeraPossibleUnitList = ["Sera T3 Mass Extractor"]
        temp = world.random.randrange(0, len(UnlockSeraPossibleUnitList))
        if not UnlockSeraPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(UnlockSeraPossibleUnitList[temp])

    if "Freedom (Sera)" in AllLevelsListToCheckRegionCreation:
        FreedomSeraPossibleUnitList = ["Sera T3 Mass Extractor"]
        temp = world.random.randrange(0, len(FreedomSeraPossibleUnitList))
        if not FreedomSeraPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomSeraPossibleUnitList[temp])

    if "Unlock (Sera)" in AllLevelsListToCheckRegionCreation:
        UnlockSeraPossibleUnitList = ["Uya-iya"]
        temp = world.random.randrange(0, len(UnlockSeraPossibleUnitList))
        if not UnlockSeraPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(UnlockSeraPossibleUnitList[temp])

    if "Freedom (Sera)" in AllLevelsListToCheckRegionCreation:
        FreedomSeraPossibleUnitList = ["Uya-iya"]
        temp = world.random.randrange(0, len(FreedomSeraPossibleUnitList))
        if not FreedomSeraPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomSeraPossibleUnitList[temp])

    if "Unlock (Sera)" in AllLevelsListToCheckRegionCreation:
        UnlockSeraPossibleUnitList = ["Othuum", "Uyanah", "Ythotha", "Ahwassa", "Yolona Oss", "Ythis", "Hovatham", "Hastue", "Sinntha"]
        temp = world.random.randrange(0, len(UnlockSeraPossibleUnitList))
        if not UnlockSeraPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(UnlockSeraPossibleUnitList[temp])

    if "Freedom (Sera)" in AllLevelsListToCheckRegionCreation:
        FreedomSeraPossibleUnitList = ["Othuum", "Uyanah", "Ythotha", "Ahwassa", "Yolona Oss", "Ythis", "Hovatham", "Hastue", "Sinntha"]
        temp = world.random.randrange(0, len(FreedomSeraPossibleUnitList))
        if not FreedomSeraPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomSeraPossibleUnitList[temp])

    if "Unlock (Sera)" in AllLevelsListToCheckRegionCreation:
        UnlockSeraPossibleUnitList = ["Ithalua"]
        temp = world.random.randrange(0, len(UnlockSeraPossibleUnitList))
        if not UnlockSeraPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(UnlockSeraPossibleUnitList[temp])

    if "Freedom (Sera)" in AllLevelsListToCheckRegionCreation:
        FreedomSeraPossibleUnitList = ["Ithalua"]
        temp = world.random.randrange(0, len(FreedomSeraPossibleUnitList))
        if not FreedomSeraPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomSeraPossibleUnitList[temp])

    if "Unlock (Sera)" in AllLevelsListToCheckRegionCreation:
        UnlockSeraPossibleUnitList = ["Vishala"]
        temp = world.random.randrange(0, len(UnlockSeraPossibleUnitList))
        if not UnlockSeraPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(UnlockSeraPossibleUnitList[temp])

    if "Freedom (Sera)" in AllLevelsListToCheckRegionCreation:
        FreedomSeraPossibleUnitList = ["Vishala"]
        temp = world.random.randrange(0, len(FreedomSeraPossibleUnitList))
        if not FreedomSeraPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomSeraPossibleUnitList[temp])

    if "Unlock (Sera)" in AllLevelsListToCheckRegionCreation:
        UnlockSeraPossibleUnitList = ["Iazyne", "Uyanah", "Iathu-ioz"]
        temp = world.random.randrange(0, len(UnlockSeraPossibleUnitList))
        if not UnlockSeraPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(UnlockSeraPossibleUnitList[temp])

    if "Freedom (Sera)" in AllLevelsListToCheckRegionCreation:
        FreedomSeraPossibleUnitList = ["Iazyne", "Uyanah", "Iathu-ioz"]
        temp = world.random.randrange(0, len(FreedomSeraPossibleUnitList))
        if not FreedomSeraPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomSeraPossibleUnitList[temp])

    if "Freedom (Sera)" in AllLevelsListToCheckRegionCreation:
        FreedomSeraPossibleUnitList = ["Aezthu-uhthe"]
        temp = world.random.randrange(0, len(FreedomSeraPossibleUnitList))
        if not FreedomSeraPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomSeraPossibleUnitList[temp])

    if "Freedom (Sera)" in AllLevelsListToCheckRegionCreation:
        FreedomSeraPossibleUnitList = ["Othuum", "Othuum", "Uyanah", "Ythotha", "Ahwassa", "Sinntha"]
        temp = world.random.randrange(0, len(FreedomSeraPossibleUnitList))
        if not FreedomSeraPossibleUnitList[temp] in PossibleItemList:
            PossibleItemList.append(FreedomSeraPossibleUnitList[temp])

    print(PossibleItemList)

    number_of_unfilled_locations = len(ListOfUsedRegions) * world.options.locamount - len(PossibleItemList)
    ItemsFromFactions = []
    if "uef" in listOfFactionsThatActuallyExist:
        ItemsFromFactions.extend(uef_items)
    if "cybran" in listOfFactionsThatActuallyExist:
        ItemsFromFactions.extend(cybran_items)
    if "aeon" in listOfFactionsThatActuallyExist:
        ItemsFromFactions.extend(aeon_items)
    if "sera" in listOfFactionsThatActuallyExist:
        ItemsFromFactions.extend(sera_items)

    for i in range(len(PossibleItemList)):
        if PossibleItemList[i] in ItemsFromFactions:
            ItemsFromFactions.remove(PossibleItemList[i])

    if len(ItemsFromFactions) >= number_of_unfilled_locations:
        PossibleItemList.extend(world.random.sample(ItemsFromFactions, number_of_unfilled_locations))
    else:
        PossibleItemList.extend(ItemsFromFactions)
        for i in range(number_of_unfilled_locations - len(ItemsFromFactions)):
            PossibleItemList.append("Nothing")

    itempoolREAL = []
    for i in range(len(PossibleItemList)):
        itempoolREAL.append(world.create_item(PossibleItemList[i]))

    world.multiworld.itempool += itempoolREAL

    world.origin_region_name = TotalListOfTtotallyLevels[THE_GRID[0][0]][0]

    print(len(ListOfUsedRegions) * world.options.locamount)
    print(len(PossibleItemList))

    final_boss_room = world.get_region(TotalListOfTtotallyLevels[THE_GRID[Width - 1][Height - 1]][len(TotalListOfTtotallyLevels[THE_GRID[Width - 1][Height - 1]]) - 1])
    final_boss_room.add_event("Final Boss Defeated", "Victory", location_type=SupComLocation, item_type=SupComItem)
    world.set_completion_rule(Has("Victory"))
def create_item_with_correct_classification(world: SupComWorld, name: str) -> SupComItem:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]
    return SupComItem(name, classification, ITEM_NAME_TO_ID[name], world.player)
