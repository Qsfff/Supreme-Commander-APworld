local VariablesAP = import('/maps/SCCA_R02/Variables.lua')
local RestrictionsBase = import('/maps/SCCA_R02/BasicRestriction.lua')
local RestrictionsUnlock = nil

function BuildCategoriesS()
    -- Start by restricting all
    ScenarioFramework.AddRestriction( Player, categories.ALLUNITS )
	--Unrestrict Basic
	for i = 1, RestrictionsBase.Elements do
		ScenarioFramework.RemoveRestriction( Player, RestrictionsBase.Unlock[i] )
	end
	--Unrestrict Unlocked
	RestrictionsUnlock = nil
	RestrictionsUnlock = import('/maps/SCCA_R02/UnlockRestriction.lua')
	for i = 1, RestrictionsUnlock.Elements do
		ScenarioFramework.RemoveRestriction( Player, RestrictionsUnlock.Unlock[i] )
	end
	--Set Unlocked Enchancements
	if VariablesAP.Faction == 0 then
		RestrictionsUnlock.EnchanceUEF()
    elseif VariablesAP.Faction == 1 then
		RestrictionsUnlock.EnchanceCYB()
	elseif VariablesAP.Faction == 2 then
		RestrictionsUnlock.EnchanceAEON()
	else
		RestrictionsUnlock.EnchanceSERA()
	end
    
end
function SuperReminder()
    if(true) then
        BuildCategoriesS()
		LOG('THIS IS REMINDER')
        ScenarioFramework.CreateTimerTrigger(SuperReminder, 60)
    end
end

-----------------------COPY THIS------------------------
    BuildCategoriesS()
	ScenarioFramework.CreateTimerTrigger(SuperReminder, 60)
	SetArmyColor(1, VariablesAP.Red, VariablesAP.Green, VariablesAP.Blue)
	
    if(VariablesAP.Faction == 0) then
        ScenarioInfo.PlayerCDR = ScenarioUtils.CreateArmyUnit('Player', 'Player_CommanderUEF')
		Faction = 'uef'
    elseif(VariablesAP.Faction == 1) then
        ScenarioInfo.PlayerCDR = ScenarioUtils.CreateArmyUnit('Player', 'Player_CommanderCyb')
		Faction = 'cybran'
    elseif(VariablesAP.Faction == 2) then
        ScenarioInfo.PlayerCDR = ScenarioUtils.CreateArmyUnit('Player', 'Player_CommanderAeon')
		Faction = 'aeon'
	else
        ScenarioInfo.PlayerCDR = ScenarioUtils.CreateArmyUnit('Player', 'Player_CommanderSera')
		Faction = 'aeon'
    end
	ScenarioInfo.PlayerCDR:SetCustomName(VariablesAP.Name)
	--------------------------------------------------------
	
	
			LOG('APLOG-A1Mass')