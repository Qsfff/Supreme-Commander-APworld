#****************************************************************************
#**
#**  File     : /maps/X1CA_005/X1CA_005_m2fletcherai.lua
#**  Author(s): Jessica St. Croix
#**
#**  Summary  : Fletcher army AI for Mission 2 - X1CA_005
#**
#**  Copyright © 2007 Gas Powered Games, Inc.  All rights reserved.
#****************************************************************************
local BaseManager = import('/lua/ai/opai/basemanager.lua')
local ScenarioFramework = import('/lua/ScenarioFramework.lua')

local SPAIFileName = '/lua/ScenarioPlatoonAI.lua'

# ------
# Locals
# ------
local Fletcher = 2
local Difficulty = ScenarioInfo.Options.Difficulty

# -------------
# Base Managers
# -------------
local FletcherBase = BaseManager.CreateBaseManager()

function FletcherBaseAI()

    # -------------
    # Fletcher Base
    # -------------
    FletcherBase:Initialize(ArmyBrains[Fletcher], 'M1_Fletcher_Base', 'M1_Fletcher_Base_Marker', 150,
        {
             M1_Fletcher_MEX1 = 1000,
             M1_Fletcher_FACT1 = 980,
             M1_Fletcher_MEX2 = 970,
             M1_Fletcher_PWR2 = 960,
             M1_Fletcher_MEX3 = 950,
             M1_Fletcher_DEF1 = 930,
             M1_Fletcher_PWFAB1_1 = 910,
             M1_Fletcher_PWFAB1_2 = 900,
             M1_Fletcher_PWFAB1_3 = 890,
             M1_Fletcher_PWFAB1_4 = 880,
             M1_Fletcher_PWFAB2_1 = 820,
             M1_Fletcher_PWFAB2_2 = 810,
             M1_Fletcher_PWFAB2_3 = 800,
             M1_Fletcher_PWFAB2_4 = 790,
             M1_Fletcher_PWFAB3_1 = 730,
             M1_Fletcher_PWFAB3_2 = 720,
             M1_Fletcher_PWFAB3_3 = 710,
             M1_Fletcher_PWFAB3_4 = 700,
             M1_Fletcher_MSTOR4 = 650,
             M1_Fletcher_PWFAB4_1 = 640,
             M1_Fletcher_PWFAB4_2 = 630,
             M1_Fletcher_PWFAB4_3 = 620,
             M1_Fletcher_PWFAB4_4 = 610,
             M1_Fletcher_DEF2 = 560,
             M1_Fletcher_RDR1 = 550,
             M1_Fletcher_SHLD1 = 540,
             M1_Fletcher_FACT2 = 530,
             M1_Fletcher_FACT3 = 520,
             M1_Fletcher_DEF3 = 510,
             M1_Fletcher_SHLD2 = 500,
             M1_Fletcher_DEF4 = 490,
             M1_Fletcher_WALL1 = 480,
             M1_Fletcher_WALL2 = 470,
             M1_Fletcher_WALL3 = 460,
             M1_Fletcher_WALL4 = 450,
             M1_Fletcher_WALL5 = 440,
             M1_Fletcher_WALL6 = 430,
             M1_Fletcher_WALL7 = 420,
             M1_Fletcher_WALL8 = 410,
             M1_Fletcher_WALL9 = 400,
             M1_Fletcher_WALL10 = 390,
             M1_Fletcher_WALL11 = 380,
             M1_Fletcher_WALL12 = 370,
             M1_Fletcher_PWR1 = 10,
             M1_Fletcher_PWR3 = 10,
             M1_Fletcher_MEX4 = 10,
             M1_Fletcher_MSTOR1 = 10,
             M1_Fletcher_MSTOR2 = 10,
             M1_Fletcher_MSTOR3 = 10,
         }
    )
    FletcherBase:StartEmptyBase(35)
    FletcherBase:SetConstructionAlwaysAssist(true)
    FletcherBase:SetMaximumConstructionEngineers(5)

    FletcherBase:SetActive('AirScouting', true)
    FletcherBase:SetActive('LandScouting', true)

    FletcherBaseLandAttacks()
end

function FletcherBaseLandAttacks()
    local opai = nil
    local quantity = {}

    # ---------------------------------
    # Fletcher Base Op AI, Land Attacks
    # ---------------------------------

    opai = FletcherBase:AddOpAI('Fatboy_1',
        {
            Amount = 3,
            KeepAlive = true,
            BuildCondition = {
                {'/lua/editor/unitcountbuildconditions.lua', 'HaveGreaterThanUnitsWithCategory', {8, categories.ueb1301, false}}
            },
            PlatoonAIFunction = {'/maps/X1CA_005/X1CA_005_m2fletcherai.lua', 'FletcherLandPlatoonThread'},
            MaxAssist = 15,
            Retry = true,
        }
    )

    # sends [heavy tanks]
    opai = FletcherBase:AddOpAI('BasicLandAttack', 'M2_LandAttack1',
        {
            MasterPlatoonFunction = {'/maps/X1CA_005/X1CA_005_m2fletcherai.lua', 'FletcherLandPlatoonThread'},
            Priority = 100,
        }
    )
    opai:SetChildQuantity('HeavyTanks', 8)

    # sends [mobile missiles]
    opai = FletcherBase:AddOpAI('BasicLandAttack', 'M2_LandAttack2',
        {
            MasterPlatoonFunction = {'/maps/X1CA_005/X1CA_005_m2fletcherai.lua', 'FletcherLandPlatoonThread'},
            Priority = 100,
        }
    )
    opai:SetChildQuantity('MobileMissiles', 6)

    # sends [siege bots]
    opai = FletcherBase:AddOpAI('BasicLandAttack', 'M2_LandAttack3',
        {
            MasterPlatoonFunction = {'/maps/X1CA_005/X1CA_005_m2fletcherai.lua', 'FletcherLandPlatoonThread'},
            Priority = 100,
        }
    )
    opai:SetChildQuantity('SiegeBots', 4)

    # sends [heavy bots] (mission 3)
    opai = FletcherBase:AddOpAI('BasicLandAttack', 'M2_LandAttack4',
        {
            MasterPlatoonFunction = {'/maps/X1CA_005/X1CA_005_m2fletcherai.lua', 'FletcherLandPlatoonThread'},
            Priority = 100,
        }
    )
    opai:SetChildQuantity('HeavyBots', 4)
    opai:AddBuildCondition('/lua/editor/miscbuildconditions.lua', 'MissionNumber', {'default_brain', 3})

    # Land Defense

    # maintains 8, 6, 4 [heavy tanks]
    quantity = {8, 6, 4}
    opai = FletcherBase:AddOpAI('BasicLandAttack', 'M2_LandDefense1',
        {
            MasterPlatoonFunction = {SPAIFileName, 'PatrolChainPickerThread'},
            PlatoonData = {
                PatrolChains = {'M1_Hex5_Main_LandDefEast_Chain', 'M1_Hex5_Main_LandDefWest_Chain'},
            },
            Priority = 110,
        }
    )
    opai:SetChildQuantity('HeavyTanks', quantity[Difficulty])

    # maintains 6, 4, 2 [mobile missiles]
    quantity = {6, 4, 2}
    opai = FletcherBase:AddOpAI('BasicLandAttack', 'M2_LandDefense2',
        {
            MasterPlatoonFunction = {SPAIFileName, 'PatrolChainPickerThread'},
            PlatoonData = {
                PatrolChains = {'M1_Hex5_Main_LandDefEast_Chain', 'M1_Hex5_Main_LandDefWest_Chain'},
            },
            Priority = 110,
        }
    )
    opai:SetChildQuantity('MobileMissiles', quantity[Difficulty])

    # maintains 8, 6, 4 [mobile flak]
    quantity = {8, 6, 4}
    opai = FletcherBase:AddOpAI('BasicLandAttack', 'M2_LandDefense3',
        {
            MasterPlatoonFunction = {SPAIFileName, 'PatrolChainPickerThread'},
            PlatoonData = {
                PatrolChains = {'M1_Hex5_Main_LandDefEast_Chain', 'M1_Hex5_Main_LandDefWest_Chain'},
            },
            Priority = 110,
        }
    )
    opai:SetChildQuantity('MobileFlak', quantity[Difficulty])

    # maintains 6, 4, 2 [siege bots]
    quantity = {6, 4, 2}
    opai = FletcherBase:AddOpAI('BasicLandAttack', 'M2_LandDefense4',
        {
            MasterPlatoonFunction = {SPAIFileName, 'PatrolChainPickerThread'},
            PlatoonData = {
                PatrolChains = {'M1_Hex5_Main_LandDefEast_Chain', 'M1_Hex5_Main_LandDefWest_Chain'},
            },
            Priority = 110,
        }
    )
    opai:SetChildQuantity('SiegeBots', quantity[Difficulty])
end

function FletcherLandPlatoonThread(platoon)
    local moveNum = false

    while(ArmyBrains[Fletcher]:PlatoonExists(platoon)) do
        if(ScenarioInfo.MissionNumber == 2) then
            if(not moveNum) then
                moveNum = 2
                IssueStop(platoon:GetPlatoonUnits())
                IssueClearCommands(platoon:GetPlatoonUnits())
                for k,v in platoon:GetPlatoonUnits() do
                    if(v and not v:IsDead()) then
                        ScenarioFramework.GroupPatrolChain({v}, 'M2_Fletcher_LandAttack_Chain')
                    end
                end
            end
        elseif(ScenarioInfo.MissionNumber == 3) then
            if(not moveNum or moveNum ~= 3) then
                moveNum = 3
                IssueStop(platoon:GetPlatoonUnits())
                IssueClearCommands(platoon:GetPlatoonUnits())
                for k,v in platoon:GetPlatoonUnits() do
                    if(v and not v:IsDead()) then
                        ScenarioFramework.GroupPatrolChain({v}, 'M3_Fletcher_Fatboy_Attack_Chain')
                    end
                end
            end
        end
        WaitSeconds(10)
    end
end

function M2FletcherBaseAirAttacks()
    local opai = nil
    local quantity = {}

    # --------------------------------
    # Fletcher Base Op AI, Air Attacks
    # --------------------------------

    # sends 12, 10, 8 [bombers]
    quantity = {12, 10, 8}
    opai = FletcherBase:AddOpAI('AirAttacks', 'M2_AirAttack1',
        {
            MasterPlatoonFunction = {'/maps/X1CA_005/X1CA_005_m2fletcherai.lua', 'FletcherAirPlatoonThread'},
            Priority = 100,
        }
    )
    opai:SetChildQuantity('Bombers', quantity[Difficulty])

    # sends 8, 6, 4 [gunships]
    quantity = {8, 6, 4}
    opai = FletcherBase:AddOpAI('AirAttacks', 'M2_AirAttack2',
        {
            MasterPlatoonFunction = {'/maps/X1CA_005/X1CA_005_m2fletcherai.lua', 'FletcherAirPlatoonThread'},
            Priority = 100,
        }
    )
    opai:SetChildQuantity('Gunships', quantity[Difficulty])

    # sends 8, 6, 4 [heavy gunships] (mission 3)
    quantity = {8, 6, 4}
    opai = FletcherBase:AddOpAI('AirAttacks', 'M2_AirAttack3',
        {
            MasterPlatoonFunction = {'/maps/X1CA_005/X1CA_005_m2fletcherai.lua', 'FletcherAirPlatoonThread'},
            Priority = 100,
        }
    )
    opai:SetChildQuantity('Gunships', quantity[Difficulty])
    opai:AddBuildCondition('/lua/editor/miscbuildconditions.lua', 'MissionNumber', {'default_brain', 3})

    # Air Defense

    # maintains 12, 10, 8 [interceptors]
    quantity = {6, 5, 4}
    for i = 1, 2 do
        opai = FletcherBase:AddOpAI('AirAttacks', 'M2_AirDefense' .. i,
            {
                MasterPlatoonFunction = {SPAIFileName, 'RandomDefensePatrolThread'},
                PlatoonData = {
                    PatrolChain = 'M1_Hex5_Main_AirDef_Chain',
                },
                Priority = 110,
            }
        )
        opai:SetChildQuantity('Interceptors', quantity[Difficulty])
    end

    # maintains 8, 6, 4 [air superiority]
    quantity = {4, 3, 2}
    for i = 3, 4 do
        opai = FletcherBase:AddOpAI('AirAttacks', 'M2_AirDefense' .. i,
            {
                MasterPlatoonFunction = {SPAIFileName, 'RandomDefensePatrolThread'},
                PlatoonData = {
                    PatrolChain = 'M1_Hex5_Main_AirDef_Chain',
                },
                Priority = 110,
            }
        )
        opai:SetChildQuantity('AirSuperiority', quantity[Difficulty])
    end
end

function FletcherAirPlatoonThread(platoon)
    local moveNum = false

    while(ArmyBrains[Fletcher]:PlatoonExists(platoon)) do
        if(ScenarioInfo.MissionNumber == 2) then
            if(not moveNum) then
                moveNum = 2
                IssueStop(platoon:GetPlatoonUnits())
                IssueClearCommands(platoon:GetPlatoonUnits())
                ScenarioFramework.PlatoonPatrolChain(platoon, 'M2_Fletcher_AirAttack_Chain')
            end
        elseif(ScenarioInfo.MissionNumber == 3) then
            if(not moveNum or moveNum ~= 3) then
                moveNum = 3
                IssueStop(platoon:GetPlatoonUnits())
                IssueClearCommands(platoon:GetPlatoonUnits())
                ScenarioFramework.PlatoonPatrolChain(platoon, 'M3_Fletcher_Air_Attack_Chain')
            end
        end
        WaitSeconds(10)
    end
end

function DisableBase()
    if(FletcherBase) then
        FletcherBase:SetBuild('Engineers', false)
        FletcherBase:SetBuildAllStructures(false)
        FletcherBase:SetActive('AirScouting', false)
        FletcherBase:SetActive('LandScouting', false)
        FletcherBase:BaseActive(false)
    end
end