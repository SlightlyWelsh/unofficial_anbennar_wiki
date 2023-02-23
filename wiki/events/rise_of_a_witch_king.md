#Information
 - Title: Rise of a Witch-King
 - ID: witch_king.0
#Description
Rise of a Witch-King
#Mean Time to Happen:
Base time = 600 months
 - Multiplied by 0.75 if has check variable has which is pointsWitchKing, and check variable has value is 26
 - Multiplied by 0.5 if has check variable has which is pointsWitchKing, and check variable has value is 39
 - Multiplied by 0.7 if has ruler flag is [necromancy_1](../flags/necromancy_1.md)
 - Multiplied by 0.5 if has ruler flag is [necromancy_2](../flags/necromancy_2.md)
 - Multiplied by 0.2 if has ruler flag is [necromancy_3](../flags/necromancy_3.md)
 - Multiplied by 0.8 if has ruler modifier is magic witch king drain life
 - Multiplied by 0.001 if has country modifier is undead military
 - Multiplied by 0.7 if has ruler flag is [magic_project_lichdom_started](../flags/magic_project_lichdom_started.md)
 - Multiplied by 0.5 if has ruler flag is [is_a_lich](../flags/is_a_lich.md)
 - Multiplied by 0.8 if has ruler modifier is magic realm enchantment modify memories overlook national blunders
 - Multiplied by 0.8 if has ruler modifier is magic realm enchantment modify memories encourage subservience
 - Multiplied by 0.8 if has ruler modifier is magic realm enchantment modify memories forget atrocities
 - Multiplied by 0.5 if has country modifier is magic enchantment hysteria
 - Multiplied by 0.9 if has ruler flag is [magic_project_homunculus_started](../flags/magic_project_homunculus_started.md)
 - Multiplied by 0.9 if has ruler modifier is magic witch king thunderstorm
 - Multiplied by 0.7 if has ruler modifier is magic witch king dominate surrender
 - Multiplied by 0.8 if has ruler modifier is magic witch king earthquake
 - Multiplied by 0.7 if has ruler modifier is magic witch king meteor strike
 - Multiplied by 0.9 if has ruler flag is [ruler_studying_necromancy](../flags/ruler_studying_necromancy.md)
 - Multiplied by 0.9 if has ruler flag is [ruler_studying_unregulated_research](../flags/ruler_studying_unregulated_research.md)
 - Multiplied by 0.9 if has ruler flag is [ruler_studying_unsafe_experiments](../flags/ruler_studying_unsafe_experiments.md)
 - Multiplied by 0.8 if has ruler flag is [ruler_studying_live_experiments](../flags/ruler_studying_live_experiments.md)
 - Multiplied by 0.8 if has ruler modifier is ruler studying live experiments
 - Multiplied by 0.9 if has estate privilege is estate mages reduced research regulations
 - Multiplied by 0.001 if has government attribute is always witch king

#Options

___
##Kneel before me!

###Efects:<ul><li>add ruler modifier:</li><ul><li>name = witch_king_modifier</li><li>duration = -1</li></ul><li>set country flag [witch_king_flag](../flags/witch_king_flag.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: anbennar_setup_7_t](../events/missing_localisation_anbennar_setup_7_t.md) happens</li><li>If has government attribute is always witch king:</li><ul><li>change variable:</li><ul><li>pointsWitchKing = 50</li></ul></ul><li>If is part of hre, and  is not the emperor, and does not have global flag is [imperial_witch_king_active](../flags/imperial_witch_king_active.md):</li><ul><li>save global event target as = imperial_witch_king</li><li>set global flag [imperial_witch_king_active](../flags/imperial_witch_king_active.md)</li><li>If has dlc is "Emperor":</li><ul><li>set imperial incident = incident_witch_prince</li></ul><li>else:</li><ul><li>emperor:</li><ul><li>the event [Rise of a Witch-Prince](../events/rise_of_a_witch_prince.md) happens</li></ul></ul></ul></ul></ul>
