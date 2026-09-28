#****************************************************************************
#**
#**  File     : /maps/X1CA_006/X1CA_006_m2rhizaai.lua
#**  Author(s): Jessica St. Croix
#**
#**  Summary  : Rhiza army AI for Mission 2 - X1CA_006
#**
#**  Copyright © 2007 Gas Powered Games, Inc.  All rights reserved.
#****************************************************************************
local BaseManager = import('/lua/ai/opai/basemanager.lua')

local SPAIFileName = '/lua/ScenarioPlatoonAI.lua'

# ------
# Locals
# ------
local Rhiza = 2

# -------------
# Base Managers
# -------------
local RhizaM2Base = BaseManager.CreateBaseManager()

function RhizaM2BaseAI()

    # -------------
    # Rhiza M2 Base
    # -------------
    RhizaM2Base:InitializeDifficultyTables(ArmyBrains[Rhiza], 'M2_Rhiza_Base', 'M2_Rhiza_Base_Marker', 100, {M2_Rhiza_Base = 100})
    RhizaM2Base:StartNonZeroBase({{4, 4, 4}, {4, 4, 4}})
    RhizaM2Base:SetActive('AirScouting', true)

    RhizaM2BaseAirAttacks()
    RhizaM2BaseLandAttacks()
    RhizaM2BaseNavalAttacks()
end

function RhizaM2BaseAirAttacks()
    local opai = nil

    # ---------------------------------
    # Rhiza M2 Base Op AI - Air Attacks
    # ---------------------------------

    # sends [gunships]
    opai = RhizaM2Base:AddOpAI('AirAttacks', 'M2_RhizaAirAttacks1',
        {
            MasterPlatoonFunction = {SPAIFileName, 'PatrolThread'},
            PlatoonData = {
                PatrolChain = 'M2_Rhiza_AirAttack_Chain',
            },
            Priority = 100,
        }
    )
    opai:SetChildQuantity('Gunships', 8)
    opai:SetLockingStyle('None')

    # sends [gunships, combat fighters]
    opai = RhizaM2Base:AddOpAI('AirAttacks', 'M2_RhizaAirAttacks2',
        {
            MasterPlatoonFunction = {SPAIFileName, 'PatrolThread'},
            PlatoonData = {
                PatrolChain = 'M2_Rhiza_AirAttack_Chain',
            },
            Priority = 100,
        }
    )
    opai:SetChildQuantity({'Gunships', 'CombatFighters'}, 8)
    opai:SetLockingStyle('None')

    # sends [bombers]
    opai = RhizaM2Base:AddOpAI('AirAttacks', 'M2_RhizaAirAttacks3',
        {
            MasterPlatoonFunction = {SPAIFileName, 'PatrolThread'},
            PlatoonData = {
                PatrolChain = 'M2_Rhiza_AirAttack_Chain',
            },
            Priority = 110,
        }
    )
    opai:SetChildQuantity('Bombers', 24)

    # Air Defense
    opai = RhizaM2Base:AddOpAI('AirAttacks', 'M2_RhizaAirDefense1',
        {
            MasterPlatoonFunction = {SPAIFileName, 'RandomDefensePatrolThread'},
            PlatoonData = {
                PatrolChain = 'M2_Rhiza_AirDef_Chain',
            },
            Priority = 100,
        }
    )
    opai:SetChildQuantity('AirSuperiority', 4)

    opai = RhizaM2Base:AddOpAI('AirAttacks', 'M2_RhizaAirDefense2',
        {
            MasterPlatoonFunction = {SPAIFileName, 'RandomDefensePatrolThread'},
            PlatoonData = {
                PatrolChain = 'M2_Rhiza_AirDef_Chain',
            },
            Priority = 100,
        }
    )
    opai:SetChildQuantity('Gunships', 4)
end

function RhizaM2BaseLandAttacks()
    local opai = nil

    # ----------------------------------
    # Rhiza M2 Base Op AI - Land Attacks
    # ----------------------------------

    # Land Defense
    opai = RhizaM2Base:AddOpAI('BasicLandAttack', 'M2_RhizaLandDefense1',
        {
            MasterPlatoonFunction = {SPAIFileName, 'PatrolThread'},
            PlatoonData = {
                PatrolChain = 'M2_Rhiza_LandDef_Chain',
            },
            Priority = 100,
        }
    )
    opai:SetChildQuantity('MobileMissiles', 3)

    opai = RhizaM2Base:AddOpAI('BasicLandAttack', 'M2_RhizaLandDefense2',
        {
            MasterPlatoonFunction = {SPAIFileName, 'PatrolThread'},
            PlatoonData = {
                PatrolChain = 'M2_Rhiza_LandDef_Chain',
            },
            Priority = 100,
        }
    )
    opai:SetChildQuantity('MobileFlak', 3)
end

function RhizaM2BaseNavalAttacks()

    # -----------------------------------
    # Rhiza M2 Base Op AI - Naval Attacks
    # -----------------------------------

    # sends 10 - 30 frigate power of [all but T3]
    local opai = RhizaM2Base:AddNavalAI('M2_RhizaNavalAttack1',
        {
            MasterPlatoonFunction = {SPAIFileName, 'PatrolThread'},
            PlatoonData = {
                PatrolChain = 'M2_Rhiza_NavalAttack_Chain',
            },
            MaxFrigates = 30,
            MinFrigates = 10,
            Priority = 100,
        }
    )
    opai:SetChildActive('T3', false)

    # Naval Defense
    opai = RhizaM2Base:AddNavalAI('M2_RhizaNavalDefense1',
        {
            MasterPlatoonFunction = {SPAIFileName, 'PatrolThread'},
            PlatoonData = {
                PatrolChain = 'M2_Rhiza_NavalDef_Chain',
            },
            MaxFrigates = 30,
            MinFrigates = 10,
            Priority = 110,
        }
    )
    opai:SetChildActive('T3', false)
end

function DisableBase()
    if(RhizaM2Base) then
        RhizaM2Base:BaseActive(false)
    end
end