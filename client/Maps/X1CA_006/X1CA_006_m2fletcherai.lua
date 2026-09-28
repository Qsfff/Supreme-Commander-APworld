#****************************************************************************
#**
#**  File     : /maps/X1CA_006/X1CA_006_m2fletcherai.lua
#**  Author(s): Jessica St. Croix
#**
#**  Summary  : Fletcher army AI for Mission 2 - X1CA_006
#**
#**  Copyright © 2007 Gas Powered Games, Inc.  All rights reserved.
#****************************************************************************
local BaseManager = import('/lua/ai/opai/basemanager.lua')

local SPAIFileName = '/lua/ScenarioPlatoonAI.lua'

# ------
# Locals
# ------
local Fletcher = 3
local Difficulty = ScenarioInfo.Options.Difficulty

# -------------
# Base Managers
# -------------
local FletcherM2Base = BaseManager.CreateBaseManager()
local FletcherM2ExpBase = BaseManager.CreateBaseManager()

function FletcherM2BaseAI()

    # ----------------
    # Fletcher M2 Base
    # ----------------
    FletcherM2Base:InitializeDifficultyTables(ArmyBrains[Fletcher], 'M2_Fletcher_Base', 'M2_Fletcher_Base_Marker', 100, {M2_Fletcher_Base = 100})
    FletcherM2Base:StartNonZeroBase({{5, 9, 14}, {5, 8, 12}})
    FletcherM2Base:SetActive('AirScouting', true)

    FletcherM2BaseAirAttacks()
    FletcherM2BaseLandAttacks()
end

function FletcherM2BaseAirAttacks()
    local opai = nil
    local quantity = {}
    local trigger = {}

    # -----------------------------------
    # Fletcher M2 Base Op AI, Air Attacks
    # -----------------------------------

    # sends 9, 18, 27 [bombers], ([gunships] on hard)
    quantity = {9, 18, 27}
    opai = FletcherM2Base:AddOpAI('AirAttacks', 'M2_FletcherAirAttacks1',
        {
            MasterPlatoonFunction = {SPAIFileName, 'PatrolChainPickerThread'},
            PlatoonData = {
                PatrolChains = {'M2_Fletcher_AirAttack1_Chain', 'M2_Fletcher_AirAttack1_Chain'},
            },
            Priority = 100,
        }
    )
    opai:SetChildActive('All', false)
    if(Difficulty < 3) then
        opai:SetChildQuantity('Bombers', quantity[Difficulty])
    else
        opai:SetChildQuantity('Gunships', quantity[Difficulty])
    end
    opai:SetLockingStyle('None')

    # sends 9, 18, 27 [gunships], ([heavy gunships] on hard)
    quantity = {9, 18, 27}
    opai = FletcherM2Base:AddOpAI('AirAttacks', 'M2_FletcherAirAttacks2',
        {
            MasterPlatoonFunction = {SPAIFileName, 'PatrolChainPickerThread'},
            PlatoonData = {
                PatrolChains = {'M2_Fletcher_AirAttack1_Chain', 'M2_Fletcher_AirAttack1_Chain'},
            },
            Priority = 100,
        }
    )
    opai:SetChildActive('All', false)
    if(Difficulty < 3) then
        opai:SetChildQuantity('Gunships', quantity[Difficulty])
    else
        opai:SetChildQuantity('HeavyGunships', quantity[Difficulty])
    end
    opai:SetLockingStyle('None')

    # sends 4, 8, 18 [gunships, combat fighters]
    quantity = {4, 8, 18}
    opai = FletcherM2Base:AddOpAI('AirAttacks', 'M2_FletcherAirAttacks3',
        {
            MasterPlatoonFunction = {SPAIFileName, 'PatrolChainPickerThread'},
            PlatoonData = {
                PatrolChains = {'M2_Fletcher_AirAttack1_Chain', 'M2_Fletcher_AirAttack1_Chain'},
            },
            Priority = 100,
        }
    )
    opai:SetChildQuantity({'Gunships', 'CombatFighters'}, quantity[Difficulty])
    opai:SetLockingStyle('None')

    # sends 9, 18, 27 [gunships] if player has >= 100, 80, 60 mobile land
    quantity = {9, 18, 27}
    trigger = {100, 80, 60}
    opai = FletcherM2Base:AddOpAI('AirAttacks', 'M2_FletcherAirAttacks4',
        {
            MasterPlatoonFunction = {SPAIFileName, 'PatrolChainPickerThread'},
            PlatoonData = {
                PatrolChains = {'M2_Fletcher_AirAttack1_Chain', 'M2_Fletcher_AirAttack1_Chain'},
            },
            Priority = 110,
        }
    )
    opai:SetChildQuantity('Gunships', quantity[Difficulty])
    opai:AddBuildCondition('/lua/editor/otherarmyunitcountbuildconditions.lua', 'BrainGreaterThanOrEqualNumCategory',
        {'default_brain', 'Player', trigger[Difficulty], (categories.MOBILE * categories.LAND) - categories.CONSTRUCTION})

    # sends 9, 18, 27 [air superiority] if player has >= 80, 60, 60 mobile air
    quantity = {9, 18, 27}
    trigger = {80, 60, 60}
    opai = FletcherM2Base:AddOpAI('AirAttacks', 'M2_FletcherAirAttacks5',
        {
            MasterPlatoonFunction = {SPAIFileName, 'PatrolChainPickerThread'},
            PlatoonData = {
                PatrolChains = {'M2_Fletcher_AirAttack1_Chain', 'M2_Fletcher_AirAttack1_Chain'},
            },
            Priority = 120,
        }
    )
    opai:SetChildQuantity('AirSuperiority', quantity[Difficulty])
    opai:AddBuildCondition('/lua/editor/otherarmyunitcountbuildconditions.lua', 'BrainGreaterThanOrEqualNumCategory',
        {'default_brain', 'Player', trigger[Difficulty], categories.MOBILE * categories.AIR})

    # sends 9, 18, 27 [air superiority] if player has >= 60, 40, 40 gunships
    quantity = {9, 18, 27}
    trigger = {60, 40, 40}
    opai = FletcherM2Base:AddOpAI('AirAttacks', 'M2_FletcherAirAttacks6',
        {
            MasterPlatoonFunction = {SPAIFileName, 'PatrolChainPickerThread'},
            PlatoonData = {
                PatrolChains = {'M2_Fletcher_AirAttack1_Chain', 'M2_Fletcher_AirAttack1_Chain'},
            },
            Priority = 120,
        }
    )
    opai:SetChildQuantity('AirSuperiority', quantity[Difficulty])
    opai:AddBuildCondition('/lua/editor/otherarmyunitcountbuildconditions.lua', 'BrainGreaterThanOrEqualNumCategory',
        {'default_brain', 'Player', trigger[Difficulty], categories.uaa0203 + categories.uea0203 + categories.ura0203})

    # sends 6, 12, 18 [combat fighters, gunships] if player has >= 60, 40, 20 T3 units
    quantity = {6, 12, 18}
    trigger = {60, 40, 20}
    opai = FletcherM2Base:AddOpAI('AirAttacks', 'M2_FletcherAirAttacks7',
        {
            MasterPlatoonFunction = {SPAIFileName, 'PatrolChainPickerThread'},
            PlatoonData = {
                PatrolChains = {'M2_Fletcher_AirAttack1_Chain', 'M2_Fletcher_AirAttack1_Chain'},
            },
            Priority = 130,
        }
    )
    opai:SetChildQuantity({'Gunships', 'CombatFighters'}, quantity[Difficulty])
    opai:AddBuildCondition('/lua/editor/otherarmyunitcountbuildconditions.lua',
        'BrainGreaterThanOrEqualNumCategory', {'default_brain', 'Player', trigger[Difficulty], categories.TECH3})

    # sends 9, 18, 27 [air superiority] if player has >= 1 strat bomber
    quantity = {9, 18, 27}
    opai = FletcherM2Base:AddOpAI('AirAttacks', 'M2_FletcherAirAttacks8',
        {
            MasterPlatoonFunction = {SPAIFileName, 'PatrolChainPickerThread'},
            PlatoonData = {
                PatrolChains = {'M2_Fletcher_AirAttack1_Chain', 'M2_Fletcher_AirAttack1_Chain'},
            },
            Priority = 140,
        }
    )
    opai:SetChildQuantity('AirSuperiority', quantity[Difficulty])
    opai:AddBuildCondition('/lua/editor/otherarmyunitcountbuildconditions.lua',
        'BrainGreaterThanOrEqualNumCategory', {'default_brain', 'Player', 1, categories.uaa0304 + categories.uea0304 + categories.ura0304})

    # sends 8, 16, 26 [bombers, gunships] if player has >= 450, 400, 300 units
    quantity = {8, 16, 26}
    trigger = {450, 400, 300}
    opai = FletcherM2Base:AddOpAI('AirAttacks', 'M2_FletcherAirAttacks9',
        {
            MasterPlatoonFunction = {SPAIFileName, 'PatrolChainPickerThread'},
            PlatoonData = {
                PatrolChains = {'M2_Fletcher_AirAttack1_Chain', 'M2_Fletcher_AirAttack1_Chain'},
            },
            Priority = 150,
        }
    )
    opai:SetChildQuantity({'Bombers', 'Gunships'}, quantity[Difficulty])
    opai:AddBuildCondition('/lua/editor/otherarmyunitcountbuildconditions.lua',
        'BrainGreaterThanOrEqualNumCategory', {'default_brain', 'Player', trigger[Difficulty], categories.ALLUNITS - categories.WALL})

    # Air Defense
    quantity = {3, 6, 9}
    for i = 1, 3 do
        opai = FletcherM2Base:AddOpAI('AirAttacks', 'M2_FletcherAirDefense1_' .. i,
            {
                MasterPlatoonFunction = {SPAIFileName, 'RandomDefensePatrolThread'},
                PlatoonData = {
                    PatrolChain = 'M2_Fletcher_AirDef_Chain',
                },
                Priority = 100,
            }
        )
        opai:SetChildQuantity('Gunships', quantity[Difficulty])
    end

    quantity = {3, 6, 9}
    for i = 1, 3 do
        opai = FletcherM2Base:AddOpAI('AirAttacks', 'M2_FletcherAirDefense2_' .. i,
            {
                MasterPlatoonFunction = {SPAIFileName, 'RandomDefensePatrolThread'},
                PlatoonData = {
                    PatrolChain = 'M2_Fletcher_AirDef_Chain',
                },
                Priority = 100,
            }
        )
        opai:SetChildQuantity('TorpedoBombers', quantity[Difficulty])
    end
end

function FletcherM2BaseLandAttacks()
    local opai = nil
    local quantity = {}

    # ----------------------
    # Fletcher M2 Base Op AI
    # ----------------------

    quantity = {1, 3, 5}
    opai = FletcherM2Base:AddOpAI('M2_Fletcher_Main_Fatboy',
        {
            Amount = 1,
            KeepAlive = true,
            PlatoonAIFunction = {SPAIFileName, 'PatrolThread'},
            PlatoonData = {
                PatrolChain = 'M2_Fletcher_ExpAttack_Chain',
            },
            MaxAssist = quantity[Difficulty],
            Retry = true,
        }
    )

    # Land Defense
    quantity = {5, 10, 15}
    for i = 1, quantity[Difficulty] do
        opai = FletcherM2Base:AddOpAI('BasicLandAttack', 'M2_FletcherLandDefense1_' .. i,
            {
                MasterPlatoonFunction = {SPAIFileName, 'PatrolThread'},
                PlatoonData = {
                    PatrolChain = 'M2_Fletcher_LandDef_Chain',
                },
                Priority = 100,
            }
        )
        opai:SetChildQuantity('MobileShields', 1)
    end

    quantity = {5, 10, 15}
    for i = 1, quantity[Difficulty] do
        opai = FletcherM2Base:AddOpAI('BasicLandAttack', 'M2_FletcherLandDefense2_' .. i,
            {
                MasterPlatoonFunction = {SPAIFileName, 'PatrolThread'},
                PlatoonData = {
                    PatrolChain = 'M2_Fletcher_LandDef_Chain',
                },
                Priority = 100,
            }
        )
        opai:SetChildQuantity('MobileMissiles', 1)
    end

    quantity = {5, 10, 15}
    for i = 1, quantity[Difficulty] do
        opai = FletcherM2Base:AddOpAI('BasicLandAttack', 'M2_FletcherLandDefense3_' .. i,
            {
                MasterPlatoonFunction = {SPAIFileName, 'PatrolThread'},
                PlatoonData = {
                    PatrolChain = 'M2_Fletcher_LandDef_Chain',
                },
                Priority = 100,
            }
        )
        opai:SetChildQuantity('MobileMissilePlatforms', 1)
    end
end

function FletcherCaptureControlCenter()
    # sends engineers
    opai = FletcherM2Base:AddOpAI('EngineerAttack', 'M2_FletcherEngAttack1',
    {
        MasterPlatoonFunction = {'/lua/ScenarioPlatoonAI.lua', 'LandAssaultWithTransports'},
        PlatoonData = {
            AttackChain = 'M2_OptionZero_Capture_Chain',
            LandingChain = 'M2_OptionZero_Landing_Chain',
            TransportReturn = 'M2_Fletcher_Base_Marker',
            Categories = {'uec1902'},
        },
        Priority = 1000,
    })
    opai:SetChildActive('T1Transports', false)
    opai:AddBuildCondition('/lua/editor/unitcountbuildconditions.lua',
        'HaveLessThanUnitsWithCategory', {'default_brain', 3, categories.uea0104 + categories.xea0306})
end

function FletcherM2ExpBaseAI()

    # --------------------
    # Fletcher M2 Exp Base
    # --------------------
    FletcherM2ExpBase:InitializeDifficultyTables(ArmyBrains[Fletcher], 'M2_Fletcher_EastExp_Group', 'M2_Fletcher_Exp_Base', 30, {M2_Fletcher_EastExp_Group = 100})
    FletcherM2ExpBase:StartNonZeroBase({0, 1, 2})

    FletcherM2ExpBaseLandAttacks()
end

function FletcherM2ExpBaseLandAttacks()
    local opai = nil

    # ----------------------------------------
    # Fletcher M2 Exp Base Op AI, Land Attacks
    # ----------------------------------------

    opai = FletcherM2ExpBase:AddOpAI('M2_Fletcher_East_Fatboy',
        {
            Amount = 1,
            KeepAlive = true,
            PlatoonAIFunction = {SPAIFileName, 'PatrolThread'},
            PlatoonData = {
                PatrolChain = 'M2_Fletcher_EasternExp_Chain',
            },

            MaxAssist = 3,
            Retry = true,
        }
    )
end