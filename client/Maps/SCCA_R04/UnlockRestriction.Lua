local ScenarioFramework = import('/lua/scenarioframework.lua')
Unlock = {}
Unlock[1] = categories.uea0103
Unlock[2] = categories.ura0103
Unlock[3] = categories.uaa0103
Unlock[4] = categories.xsa0103
Elements = 4

function EnchanceUEF()
    ScenarioFramework.RestrictEnhancements({'AdvancedEngineering', --1
                                            'T3Engineering',
                                            'DamageStabilization',
                                            'HeavyAntiMatterCannon',
                                            'LeftPod',
                                            'RightPod',
                                            'Shield',
                                            'ShieldGeneratorField',
                                            'TacticalMissile',
                                            'TacticalNukeMissile',
                                            'ResourceAllocation',
                                            'Teleporter'})
end
function EnchanceCYB()
    ScenarioFramework.RestrictEnhancements({'AdvancedEngineering', --1
                                            'T3Engineering',
                                            'CloakingGenerator',
                                            'CoolingUpgrade',
                                            'MicrowaveLaserGenerator',
											'NaniteTorpedoTube',
                                            'StealthGenerator',
                                            'ResourceAllocation',
                                            'StealthGenerator',
                                            'Teleporter'})
end
function EnchanceAEON()
    ScenarioFramework.RestrictEnhancements({'AdvancedEngineering', --1
                                            'T3Engineering',
                                            'ChronoDampener',
                                            'CrysalisBeam',
                                            'EnhancedSensors',
                                            'HeatSink',
                                            'Shield',
                                            'ShieldHeavy',
                                            'ResourceAllocationAdvanced',
                                            'ResourceAllocation',
                                            'Teleporter'})
end
function EnchanceSERA()
    ScenarioFramework.RestrictEnhancements({'AdvancedEngineering', --1
                                            'T3Engineering',
											'AdvancedRegenAura', --1
                                            'BlastAttack',
                                            'DamageStabilization',
                                            'DamageStabilizationAdvanced',
                                            'Missile',
                                            'RateOfFire',
                                            'RegenAura',
                                            'ResourceAllocation',
                                            'ResourceAllocationAdvanced',
                                            'Teleporter'})
end