#****************************************************************************
#**
#**  File     : /maps/X1CA_001/X1CA_001_m2uefai.lua
#**  Author(s): Jessica St. Croix
#**
#**  Summary  : UEF army AI for Mission 2 - X1CA_001
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
local UEFM2WesternTown = BaseManager.CreateBaseManager()

function UEFM2WesternTownAI()

    # ----------------
    # UEF Western Town
    # ----------------
    ScenarioUtils.CreateArmyGroup('UEF', 'M2_Town_Init_Eng_D' .. Difficulty)
    ScenarioUtils.CreateArmyGroup('UEF', 'M2_Town_Turrets_D' .. Difficulty)
    UEFM2WesternTown:Initialize(ArmyBrains[UEF], 'M2_Town_Defenses', 'UEF_M2_Base_Marker', 50, {M2_Town_Defenses = 100})
    UEFM2WesternTown:StartNonZeroBase({{1, 3, 5}, {1, 3, 5}})
    UEFM2WesternTown:SetBuild('Engineers', false)

    UEFM2WesternTownLandAttacks()
end

function UEFM2WesternTownLandAttacks()
    local opai = nil

    # ---------------------------------------
    # UEF M2 Western Town Op AI, Land Attacks
    # ---------------------------------------

    # sends [mobile missiles]
    opai = UEFM2WesternTown:AddOpAI('BasicLandAttack', 'M2_LandAttack1',
        {
            MasterPlatoonFunction = {SPAIFileName, 'PatrolThread'},
            PlatoonData = {
                PatrolChain = 'UEF_M2_West_Town_Patrol_Chain',
            },
        }
    )
    opai:SetChildQuantity('MobileMissiles', 4)

    # sends [heavy tanks]
    opai = UEFM2WesternTown:AddOpAI('BasicLandAttack', 'M2_LandAttack2',
        {
            MasterPlatoonFunction = {SPAIFileName, 'PatrolThread'},
            PlatoonData = {
                PatrolChain = 'UEF_M2_West_Town_Patrol_Chain',
            },
        }
    )
    opai:SetChildQuantity('HeavyTanks', 4)

    # sends [light bots]
    opai = UEFM2WesternTown:AddOpAI('BasicLandAttack', 'M2_LandAttack3',
        {
            MasterPlatoonFunction = {SPAIFileName, 'PatrolThread'},
            PlatoonData = {
                PatrolChain = 'UEF_M2_West_Town_Patrol_Chain',
            },
        }
    )
    opai:SetChildQuantity('LightBots', 4)

    # sends [light artillery]
    opai = UEFM2WesternTown:AddOpAI('BasicLandAttack', 'M2_LandAttack4',
        {
            MasterPlatoonFunction = {SPAIFileName, 'PatrolThread'},
            PlatoonData = {
                PatrolChain = 'UEF_M2_West_Town_Patrol_Chain',
            },
        }
    )
    opai:SetChildQuantity('LightArtillery', 4)
end


function DisableBase()
    if(UEFM2WesternTown) then
        UEFM2WesternTown:BaseActive(false)
    end
end