#****************************************************************************
#**
#**  File     : /maps/X1CA_003/X1CA_003_m3princessai.lua
#**  Author(s): Jessica St. Croix
#**
#**  Summary  : Princess army AI for Mission 3 - X1CA_003
#**
#**  Copyright © 2007 Gas Powered Games, Inc.  All rights reserved.
#****************************************************************************
local BaseManager = import('/lua/ai/opai/basemanager.lua')

local SPAIFileName = '/lua/ScenarioPlatoonAI.lua'

# ------
# Locals
# ------
local Princess = 4
local Difficulty = ScenarioInfo.Options.Difficulty

# -------------
# Base Managers
# -------------
local PrincessBase = BaseManager.CreateBaseManager()

function PrincessBaseAI()

    # -------------
    # Princess Base
    # -------------
    PrincessBase:InitializeDifficultyTables(ArmyBrains[Princess], 'M3_Princess_Base', 'Princess_Base', 150, {M3_Princess_Base = 100})
    PrincessBase:StartNonZeroBase({3,2,1})

    PrincessBaseAirAttacks()
end

function PrincessBaseAirAttacks()
    local opai = nil
    local quantity = {}

    # Air Defense
    quantity = {8, 6, 4}
    opai = PrincessBase:AddOpAI('AirAttacks', 'PrincessBase_AirDefense1',
        {
            MasterPlatoonFunction = {SPAIFileName, 'RandomDefensePatrolThread'},
            PlatoonData = {
                PatrolChain = 'M3_Princess_AirDef_Chain',
            },
            Priority = 100,
        }
    )
    opai:SetChildQuantity('AirSuperiority', quantity[Difficulty])

    quantity = {8, 6, 4}
    opai = PrincessBase:AddOpAI('AirAttacks', 'PrincessBase_AirDefense2',
        {
            MasterPlatoonFunction = {SPAIFileName, 'RandomDefensePatrolThread'},
            PlatoonData = {
                PatrolChain = 'M3_Princess_AirDef_Chain',
            },
            Priority = 100,
        }
    )
    opai:SetChildQuantity('Gunships', quantity[Difficulty])
end