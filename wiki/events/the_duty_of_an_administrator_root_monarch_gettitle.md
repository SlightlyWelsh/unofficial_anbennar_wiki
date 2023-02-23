#Information
 - Title: The Duty of an Administrator-[Root.Monarch.GetTitle]
 - ID: flavour_birsartanses.7
#Description
The Duty of an Administrator-[Root.Monarch.GetTitle]
#Options

___
##There's no need.

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>country gets the modifier F21_not_proving_yourself until otherwise removed</li><li>If has country flag is [birsartanses_plans_improved](../flags/birsartanses_plans_improved.md):</li><ul><li>add stability = -2</li></ul></ul>

___
##Write a treatise.

###AI weighting:
AI weights this option at 99


###Efects:<ul><li>hidden effect:</li><ul><li>multiply variable:</li><ul><li>which = BirsartansesExaminationSuccess</li><li>value = 3</li></ul><li>set variable:</li><ul><li>which = BirsartansesPlanFailChance</li><li>which = BirsartansesExaminationSuccess</li></ul><li>If does not have ADM is 3:</li><ul><li>change variable:</li><ul><li>which = BirsartansesPlanFailChance</li><li>value = 5</li></ul></ul><li>Else if does not have ADM is 2:</li><ul><li>change variable:</li><ul><li>which = BirsartansesPlanFailChance</li><li>value = 10</li></ul></ul><li>Else if does not have ADM is 1:</li><ul><li>change variable:</li><ul><li>which = BirsartansesPlanFailChance</li><li>value = 15</li></ul></ul><li>If does not have monthly adm is 8:</li><ul><li>change variable:</li><ul><li>which = BirsartansesPlanFailChance</li><li>value = 5</li></ul></ul><li>Else if does not have monthly adm is 6:</li><ul><li>change variable:</li><ul><li>which = BirsartansesPlanFailChance</li><li>value = 10</li></ul></ul><li>If does not have adm advisor 3 is yes, and does not have dip advisor 3 is yes, and does not have mil advisor 3 is yes:</li><ul><li>change variable:</li><ul><li>which = BirsartansesPlanFailChance</li><li>value = 5</li></ul></ul><li>Else if does not have adm advisor 2 is yes, and does not have dip advisor 2 is yes, and does not have mil advisor 2 is yes:</li><ul><li>change variable:</li><ul><li>which = BirsartansesPlanFailChance</li><li>value = 10</li></ul></ul><li>If has ADM is 6:</li><ul><li>change variable:</li><ul><li>which = BirsartansesPlanSuccessChance</li><li>value = 25</li></ul></ul><li>Else if has ADM is 5:</li><ul><li>change variable:</li><ul><li>which = BirsartansesPlanSuccessChance</li><li>value = 20</li></ul></ul><li>Else if has ADM is 4:</li><ul><li>change variable:</li><ul><li>which = BirsartansesPlanSuccessChance</li><li>value = 10</li></ul></ul><li>Else if has ADM is 3:</li><ul><li>change variable:</li><ul><li>which = BirsartansesPlanSuccessChance</li><li>value = 5</li></ul></ul><li>If has monthly adm is 14:</li><ul><li>change variable:</li><ul><li>which = BirsartansesPlanSuccessChance</li><li>value = 15</li></ul></ul><li>Else if has monthly adm is 12:</li><ul><li>change variable:</li><ul><li>which = BirsartansesPlanSuccessChance</li><li>value = 10</li></ul></ul><li>Else if has monthly adm is 10:</li><ul><li>change variable:</li><ul><li>which = BirsartansesPlanSuccessChance</li><li>value = 5</li></ul></ul><li>If has adm advisor 5 is yes, and  has dip advisor 5 is yes, and  has mil advisor 5 is yes:</li><ul><li>change variable:</li><ul><li>which = BirsartansesPlanSuccessChance</li><li>value = 20</li></ul></ul><li>Else if has adm advisor 4 is yes, and  has dip advisor 4 is yes, and  has mil advisor 4 is yes:</li><ul><li>change variable:</li><ul><li>which = BirsartansesPlanSuccessChance</li><li>value = 10</li></ul></ul><li>set country flag [birsartanses_taking_test](../flags/birsartanses_taking_test.md)</li><li>capital scope:</li><ul><li>add province triggered modifier = birsartanses_25_year_plan_mod</li></ul></ul><li>set country flag [birsartanses_preparing_plan](../flags/birsartanses_preparing_plan.md)</li><li>custom tooltip = birsartanses_preparing_plan_tt</li></ul>
