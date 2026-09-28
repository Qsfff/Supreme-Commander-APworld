#****************************************************************************
#**
#**  File     : /maps/X1CA_001/X1CA_001_m4uefai.lua
#**  Author(s): Jessica St. Croix
#**
#**  Summary  : UEF army AI for Mission 4 - X1CA_001
#**
#**  Copyright © 2007 Gas Powered Games, Inc.  All rights reserved.
#****************************************************************************
local BaseManager = import('/lua/ai/opai/basemanager.lua')
local ScenarioUtils = import('/lua/sim/ScenarioUtilities.lua')

local SPAIFileName = '/lua/scenarioplatoonai.lua'

# ------
# Locals
# ------
local UEF = 4
local Difficulty = ScenarioInfo.Options.Difficulty

# -------------
# Base Managers
# -------------
local FortClarke = BaseManager.CreateBaseManager()
local UEFM4ForwardOne = BaseManager.CreateBaseManager()
local UEFM4ForwardTwo = BaseManager.CreateBaseManager()

function FortClarkeAI()

    # -----------
    # Fort Clarke
    # -----------
    ScenarioUtils.CreateArmyGroup('UEF', 'M4_UEF_Clarke_Init_Eng_D' .. Difficulty)
    FortClarke:InitializeDifficultyTables(ArmyBrains[UEF], 'UEF_Fort_Clarke_Base', 'UEF_Fort_Clarke_Marker', 100, {UEF_Fort_Clarke_Base = 100,})
    FortClarke:StartNonZeroBase({{5, 5, 2}, {4, 4, 2}})
    FortClarke:SetActive('AirScouting', true)
    FortClarke:SetActive('LandScouting', true)

    FortClarkeLandAttacks()
    FortClarkeAirAttacks()
end

function FortClarkeLandAttacks()
    local opai = nil

    # -------------------------------
    # Fort Clarke Op AI, Land Attacks
    # -------------------------------

    # sends [siege bots, heavy tanks, light tanks]
    opai = FortClarke:AddOpAI('BasicLandAttack', 'M4_LandAttack1',
        {
            MasterPlatoonFunction = {SPAIFileName, 'PatrolThread'},
            PlatoonData = {
                PatrolChain = 'M4_UEF_LandAttack_Mid_Chain',
            },
            Priority = 100,
        }
    )
    opai:SetChildQuantity({'SiegeBots', 'HeavyTanks', 'LightTanks'}, 9)
    opai:SetLockingStyle('None')

    # sends [heavy tanks, heavy bots]
    opai = FortClarke:AddOpAI('BasicLandAttack', 'M4_LandAttack2',
        {
            MasterPlatoonFunction = {SPAIFileName, 'PatrolThread'},
            PlatoonData = {
                PatrolChain = 'M4_UEF_LandAttack_Mid_Chain',
            },
            Priority = 100,
        }
    )
    opai:SetChildQuantity({'HeavyTanks', 'HeavyBots'}, 8)
    opai:SetLockingStyle('None')

    # sends [mobile missiles, light artillery]
    opai = FortClarke:AddOpAI('BasicLandAttack', 'M4_LandAttack3',
        {
            MasterPlatoonFunction = {SPAIFileName, 'PatrolThread'},
            PlatoonData = {
                PatrolChain = 'M4_UEF_LandAttack_Mid_Chain',
            },
            Priority = 100,
        }
    )
    opai:SetChildQuantity({'MobileMissiles', 'LightArtillery'}, 8)
    opai:SetLockingStyle('None')

    # sends [mobile flak, light bots]
    opai = FortClarke:AddOpAI('BasicLandAttack', 'M4_LandAttack4',
        {
            MasterPlatoonFunction = {SPAIFileName, 'PatrolThread'},
            PlatoonData = {
                PatrolChain = 'M4_UEF_LandAttack_Mid_Chain',
            },
            Priority = 100,
        }
    )
    opai:SetChildQuantity({'MobileFlak', 'LightBots'}, 8)
    opai:SetLockingStyle('None')

    # [mobile flak, mobile aa] patrols
    for i = 1, 2 do
        opai = FortClarke:AddOpAI('BasicLandAttack', 'FortClarkeLandBasePatrol' .. i,
            {
                MasterPlatoonFunction = {SPAIFileName, 'PatrolThread'},
                PlatoonData = {
                    PatrolChain = 'UEF_M4_BasePatrol' .. i .. '_Chain',
                },
                Priority = 110,
            }
        )
        opai:SetChildQuantity({'MobileFlak', 'MobileAntiAir'}, 8)
    end

    # [siege bots, heavy tanks, heavy bots] patrols
    for i = 1, 2 do
        opai = FortClarke:AddOpAI('BasicLandAttack', 'FortClarkeFrontLandBasePatrol' .. i,
            {
                MasterPlatoonFunction = {SPAIFileName, 'RandomPatrolThread'},
                PlatoonData = {
                    PatrolChain = 'M4_UEF_BaseFrontPatrol_Chain',
                },
                Priority = 120,
            }
        )
        opai:SetChildQuantity({'SiegeBots', 'HeavyTanks', 'HeavyBots'}, 9)
    end
end

function FortClarkeAirAttacks()
    local opai = nil

    # ------------------------------
    # Fort Clarke Op AI, Air Attacks
    # ------------------------------

    # sends [heavy gunships, gunships, interceptors]
    opai = FortClarke:AddOpAI('AirAttacks', 'M4_AirAttack1',
        {
            MasterPlatoonFunction = {SPAIFileName, 'PatrolThread'},
            PlatoonData = {
                PatrolChain = 'M4_UEF_AirAttack1_Chain',
            },
            Priority = 100,
        }
    )
    opai:SetChildQuantity({'HeavyGunships', 'Gunships', 'Interceptors'}, 9)
    opai:SetLockingStyle('None')

    # sends [bombers]
    opai = FortClarke:AddOpAI('AirAttacks', 'M4_AirAttack2',
        {
            MasterPlatoonFunction = {SPAIFileName, 'PatrolThread'},
            PlatoonData = {
                PatrolChain = 'M4_UEF_AirAttack1_Chain',
            },
            Priority = 100,
        }
    )
    opai:SetChildQuantity('Bombers', 8)
    opai:SetLockingStyle('None')

    # Air Defense
    opai = FortClarke:AddOpAI('AirAttacks', 'M4_AirDefense1',
        {
            MasterPlatoonFunction = {SPAIFileName, 'RandomDefensePatrolThread'},
            PlatoonData = {
                PatrolChain = 'M4_UEF_AirPatrol1_Chain',
            },
            Priority = 110,
        }
    )
    opai:SetChildQuantity('AirSuperiority', 8)

    opai = FortClarke:AddOpAI('AirAttacks', 'M4_AirDefense2',
        {
            MasterPlatoonFunction = {SPAIFileName, 'RandomDefensePatrolThread'},
            PlatoonData = {
                PatrolChain = 'M4_UEF_AirPatrol1_Chain',
            },
            Priority = 110,
        }
    )
    opai:SetChildQuantity('HeavyGunships', 8)

    opai = FortClarke:AddOpAI('AirAttacks', 'M4_AirDefense3',
        {
            MasterPlatoonFunction = {SPAIFileName, 'RandomDefensePatrolThread'},
            PlatoonData = {
                PatrolChain = 'M4_UEF_AirPatrol1_Chain',
            },
            Priority = 110,
        }
    )
    opai:SetChildQuantity('Interceptors', 8)
end

function UEFM4ForwardOneAI()

    # ------------------
    # UEF Forward Base 1
    # ------------------
    UEFM4ForwardOne:InitializeDifficultyTables(ArmyBrains[UEF], 'M3_Forward_One', 'UEF_M3_Forward_One_Base_Marker', 20, {M3_Forward_One = 100,})
    UEFM4ForwardOne:StartNonZeroBase({{3, 3, 1}, {3, 3, 1}})

    UEFM4ForwardOneLandAttacks()
end

function UEFM4ForwardOneLandAttacks()
    local opai = nil

    # --------------------------------------
    # UEF M4 Forward One Op AI, Land Attacks
    # --------------------------------------

    # sends [heavy tanks, heavy bots]
    opai = UEFM4ForwardOne:AddOpAI('BasicLandAttack', 'UEF_ForwardOne_LandAttack1',
        {
            MasterPlatoonFunction = {SPAIFileName, 'PatrolThread'},
            PlatoonData = {
                PatrolChain = 'M4_UEF_LandAttack_South_Chain',
            },
            Priority = 100,
        }
    )
    opai:SetChildQuantity({'HeavyTanks', 'HeavyBots'}, 4)
    opai:SetLockingStyle('None')

    # sends [mobile missiles, light artillery]
    opai = UEFM4ForwardOne:AddOpAI('BasicLandAttack', 'UEF_ForwardOne_LandAttack2',
        {
            MasterPlatoonFunction = {SPAIFileName, 'PatrolThread'},
            PlatoonData = {
                PatrolChain = 'M4_UEF_LandAttack_South_Chain',
            },
            Priority = 100,
        }
    )
    opai:SetChildQuantity({'MobileMissiles', 'LightArtillery'}, 4)
    opai:SetLockingStyle('None')

    # sends [mobile flak, light bots]
    opai = UEFM4ForwardOne:AddOpAI('BasicLandAttack', 'UEF_ForwardOne_LandAttack3',
        {
            MasterPlatoonFunction = {SPAIFileName, 'PatrolThread'},
            PlatoonData = {
                PatrolChain = 'M4_UEF_LandAttack_South_Chain',
            },
            Priority = 100,
        }
    )
    opai:SetChildQuantity({'MobileFlak', 'LightBots'}, 4)
    opai:SetLockingStyle('None')
end

function UEFM4ForwardTwoAI()

    # ------------------
    # UEF Forward Base 2
    # ------------------
    UEFM4ForwardTwo:InitializeDifficultyTables(ArmyBrains[UEF], 'M3_Forward_Two', 'UEF_M3_Forward_Two_Base_Marker', 20, {M3_Forward_Two = 100,})
    UEFM4ForwardTwo:StartNonZeroBase(0)

    UEFM4ForwardTwoLandAttacks()
end

function UEFM4ForwardTwoLandAttacks()
    local opai = nil

    # --------------------------------------
    # UEF M4 Forward Two Op AI, Land Attacks
    # --------------------------------------

    # sends [heavy tanks, heavy bots]
    opai = UEFM4ForwardTwo:AddOpAI('BasicLandAttack', 'UEF_ForwardTwo_LandAttack1',
        {
            MasterPlatoonFunction = {SPAIFileName, 'PatrolThread'},
            PlatoonData = {
                PatrolChain = 'M4_UEF_LandAttack_North_Chain',
            },
            Priority = 100,
        }
    )
    opai:SetChildQuantity({'HeavyTanks', 'HeavyBots'}, 4)
    opai:SetLockingStyle('None')

    # sends [mobile missiles, light artillery]
    opai = UEFM4ForwardTwo:AddOpAI('BasicLandAttack', 'UEF_ForwardTwo_LandAttack2',
        {
            MasterPlatoonFunction = {SPAIFileName, 'PatrolThread'},
            PlatoonData = {
                PatrolChain = 'M4_UEF_LandAttack_North_Chain',
            },
            Priority = 100,
        }
    )
    opai:SetChildQuantity({'MobileMissiles', 'LightArtillery'}, 4)
    opai:SetLockingStyle('None')

    # sends [mobile flak, light bots]
    opai = UEFM4ForwardTwo:AddOpAI('BasicLandAttack', 'UEF_ForwardTwo_LandAttack3',
        {
            MasterPlatoonFunction = {SPAIFileName, 'PatrolThread'},
            PlatoonData = {
                PatrolChain = 'M4_UEF_LandAttack_North_Chain',
            },
            Priority = 100,
        }
    )
    opai:SetChildQuantity({'MobileFlak', 'LightBots'}, 4)
    opai:SetLockingStyle('None')
end