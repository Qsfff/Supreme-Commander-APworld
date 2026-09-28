#****************************************************************************
#**
#**  File     : /maps/X1CA_003/X1CA_003_m1rhizaai.lua
#**  Author(s): Jessica St. Croix
#**
#**  Summary  : Rhiza army AI for Mission 1 - X1CA_003
#**
#**  Copyright © 2007 Gas Powered Games, Inc.  All rights reserved.
#****************************************************************************
local BaseManager = import('/lua/ai/opai/basemanager.lua')
local ScenarioFramework = import('/lua/ScenarioFramework.lua')
local ScenarioPlatoonAI = import('/lua/ScenarioPlatoonAI.lua')
local ScenarioUtils = import('/lua/sim/ScenarioUtilities.lua')

local SPAIFileName = '/lua/ScenarioPlatoonAI.lua'

# ------
# Locals
# ------
local Rhiza = 3

# -------------
# Base Managers
# -------------
local M1RhizaBase = BaseManager.CreateBaseManager()

function M1RhizaBaseAI()

    # -------------
    # M1 Rhiza Base
    # -------------
    M1RhizaBase:InitializeDifficultyTables(ArmyBrains[Rhiza], 'M1_Rhiza_Base', 'Rhiza_M1_Base', 100, {M1_Rhiza_Base = 100})
    M1RhizaBase:StartNonZeroBase({{3, 2, 1}, {3, 2, 1}})
    M1RhizaBase:SetActive('AirScouting', true)

    M1RhizaBaseAirAttacks()
    M1RhizaBaseNavalAttacks()
end

function M1RhizaBaseAirAttacks()
    local opai = nil

    # --------------------------------
    # M1 Rhiza Base Op AI, Air Attacks
    # --------------------------------

    # sends all but [strat bombers]
    opai = M1RhizaBase:AddOpAI('AirAttacks', 'M1_AirAttacks1',
        {
            MasterPlatoonFunction = {'/maps/X1CA_003/X1CA_003_m1rhizaai.lua', 'M1RhizaAirAttackAI'},
            Priority = 100,
        }
    )
    opai:SetChildActive('StratBombers', false)

    # Air Defense
    for i = 1, 2 do
        opai = M1RhizaBase:AddOpAI('AirAttacks', 'M1_AirDefense' .. i,
            {
                MasterPlatoonFunction = {SPAIFileName, 'RandomDefensePatrolThread'},
                PlatoonData = {
                    PatrolChain = 'M1_Rhiza_AirDef_Chain',
                },
                Priority = 100,
            }
        )
        opai:SetChildActive('All', false)
        opai:SetChildActive('AirSuperiority', true)
        opai:SetChildCount(1)
    end
end

function M1RhizaBaseNavalAttacks()
    local opai = nil

    # ----------------------------------
    # M1 Rhiza Base Op AI, Naval Attacks
    # ----------------------------------

    # sends 15 frigate power of all but T3
    opai = M1RhizaBase:AddNavalAI('M1_NavalAttack1',
        {
            MasterPlatoonFunction = {'/maps/X1CA_003/X1CA_003_m1rhizaai.lua', 'M1RhizaNavalAttackAI'},
            MaxFrigates = 15,
            MinFrigates = 15,
            Priority = 100,
        }
    )
    opai:SetChildActive('T3', false)

    # Naval Defense
    for i = 1, 2 do
        opai = M1RhizaBase:AddNavalAI('M1_NavalDefense' .. i,
            {
                MasterPlatoonFunction = {SPAIFileName, 'PatrolThread'},
                PlatoonData = {
                    PatrolChain = 'M1_Rhiza_NavalDef_Chain',
                },
                MaxFrigates = 15,
                MinFrigates = 15,
                Priority = 110,
            }
        )
        opai:SetChildActive('T3', false)
    end
end

function M1RhizaAirAttackAI(platoon)
    local moveNum = false
    while(ArmyBrains[Rhiza]:PlatoonExists(platoon)) do
        if(ScenarioInfo.MissionNumber == 1) then
            if(not moveNum) then
                moveNum = 1
                IssueStop(platoon:GetPlatoonUnits())
                IssueClearCommands(platoon:GetPlatoonUnits())
                for k, v in platoon:GetPlatoonUnits() do
                    if(v and not v:IsDead()) then
                        ScenarioFramework.GroupPatrolRoute({v}, ScenarioPlatoonAI.GetRandomPatrolRoute(ScenarioUtils.ChainToPositions('M1_Rhiza_Air_Attack' .. Random(1,2) .. '_Chain')))
                    end
                end
            end
        elseif(ScenarioInfo.MissionNumber == 2) then
            if(not moveNum or moveNum ~= 2) then
                moveNum = 2
                IssueStop(platoon:GetPlatoonUnits())
                IssueClearCommands(platoon:GetPlatoonUnits())
                for k, v in platoon:GetPlatoonUnits() do
                    if(v and not v:IsDead()) then
                        ScenarioFramework.GroupPatrolRoute({v}, ScenarioPlatoonAI.GetRandomPatrolRoute(ScenarioUtils.ChainToPositions('M2_Rhiza_Air_Attack_Chain')))
                    end
                end
            end
        elseif(ScenarioInfo.MissionNumber == 3) then
            if(not moveNum or moveNum ~= 3) then
                moveNum = 3
                IssueStop(platoon:GetPlatoonUnits())
                IssueClearCommands(platoon:GetPlatoonUnits())
                for k, v in platoon:GetPlatoonUnits() do
                    if(v and not v:IsDead()) then
                        ScenarioFramework.GroupPatrolRoute({v}, ScenarioPlatoonAI.GetRandomPatrolRoute(ScenarioUtils.ChainToPositions('M3_Rhiza_AirAttack_Chain')))
                    end
                end
            end
        end
        WaitSeconds(10)
    end
end

function M1RhizaNavalAttackAI(platoon)
    local moveNum = false
    while(ArmyBrains[Rhiza]:PlatoonExists(platoon)) do
        if(ScenarioInfo.MissionNumber == 1) then
            if(not moveNum) then
                moveNum = 1
                IssueStop(platoon:GetPlatoonUnits())
                IssueClearCommands(platoon:GetPlatoonUnits())
                for k, v in platoon:GetPlatoonUnits() do
                    if(v and not v:IsDead()) then
                        ScenarioFramework.GroupPatrolChain({v}, 'M1_Rhiza_Naval_Attack' .. Random(1,2) .. '_Chain')
                    end
                end
            end
        elseif(ScenarioInfo.MissionNumber == 2) then
            if(not moveNum or moveNum ~= 2) then
                moveNum = 2
                IssueStop(platoon:GetPlatoonUnits())
                IssueClearCommands(platoon:GetPlatoonUnits())
                for k, v in platoon:GetPlatoonUnits() do
                    if(v and not v:IsDead()) then
                        ScenarioFramework.GroupPatrolChain({v}, 'M2_Rhiza_Naval_Attack_Chain')
                    end
                end
            end
        elseif(ScenarioInfo.MissionNumber == 3) then
            if(not moveNum or moveNum ~= 3) then
                moveNum = 3
                IssueStop(platoon:GetPlatoonUnits())
                IssueClearCommands(platoon:GetPlatoonUnits())
                for k, v in platoon:GetPlatoonUnits() do
                    if(v and not v:IsDead()) then
                        ScenarioFramework.GroupPatrolChain({v}, 'M3_Rhiza_NavalAttack_Chain')
                    end
                end
            end
        end
        WaitSeconds(10)
    end
end

function DisableBase()
    if(M1RhizaBase) then
        M1RhizaBase:BaseActive(false)
    end
end