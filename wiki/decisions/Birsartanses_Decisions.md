This is a list of all [decisions](decisions.md) in the category "Birsartanses_Decisions"

| Decision | Completion requirements | Effects | Requirements to appear |
| ----- | ------ | ----- | ------ |
| <a name="birsartanses_25_year_plans">Enact 25-Year Plan</a><br />*Successfully enacting a 25-Year plan will require a sophisticated and efficient administration. Highly skilled advisors, wise rulers, and even a focus on administrative endeavours might ensure our success, while a failure could have debilitating effects on the nation.* | <li>has reform birsartanses_central_administration_2</li> | <li>hidden effect:</li><ul><li>multiply variable:</li><ul><li>which = BirsartansesExaminationSuccess</li><li>value = 3</li></ul><li>set variable:</li><ul><li>which = BirsartansesPlanFailChance</li><li>which = BirsartansesExaminationSuccess</li></ul><li>If does not have ADM is 3:</li><ul><li>change variable:</li><ul><li>which = BirsartansesPlanFailChance</li><li>value = 5</li></ul></ul><li>Else if does not have ADM is 2:</li><ul><li>change variable:</li><ul><li>which = BirsartansesPlanFailChance</li><li>value = 10</li></ul></ul><li>Else if does not have ADM is 1:</li><ul><li>change variable:</li><ul><li>which = BirsartansesPlanFailChance</li><li>value = 15</li></ul></ul><li>If does not have monthly adm is 8:</li><ul><li>change variable:</li><ul><li>which = BirsartansesPlanFailChance</li><li>value = 5</li></ul></ul><li>Else if does not have monthly adm is 6:</li><ul><li>change variable:</li><ul><li>which = BirsartansesPlanFailChance</li><li>value = 10</li></ul></ul><li>If does not have adm advisor 3 is yes, and does not have dip advisor 3 is yes, and does not have mil advisor 3 is yes:</li><ul><li>change variable:</li><ul><li>which = BirsartansesPlanSuccessChance</li><li>value = 5</li></ul></ul><li>Else if does not have adm advisor 2 is yes, and does not have dip advisor 2 is yes, and does not have mil advisor 2 is yes:</li><ul><li>change variable:</li><ul><li>which = BirsartansesPlanSuccessChance</li><li>value = 10</li></ul></ul><li>If has ADM is 6:</li><ul><li>change variable:</li><ul><li>which = BirsartansesPlanSuccessChance</li><li>value = 25</li></ul></ul><li>Else if has ADM is 5:</li><ul><li>change variable:</li><ul><li>which = BirsartansesPlanSuccessChance</li><li>value = 20</li></ul></ul><li>Else if has ADM is 4:</li><ul><li>change variable:</li><ul><li>which = BirsartansesPlanSuccessChance</li><li>value = 10</li></ul></ul><li>Else if has ADM is 3:</li><ul><li>change variable:</li><ul><li>which = BirsartansesPlanSuccessChance</li><li>value = 5</li></ul></ul><li>If has monthly adm is 14:</li><ul><li>change variable:</li><ul><li>which = BirsartansesPlanSuccessChance</li><li>value = 15</li></ul></ul><li>Else if has monthly adm is 12:</li><ul><li>change variable:</li><ul><li>which = BirsartansesPlanSuccessChance</li><li>value = 10</li></ul></ul><li>Else if has monthly adm is 10:</li><ul><li>change variable:</li><ul><li>which = BirsartansesPlanSuccessChance</li><li>value = 5</li></ul></ul><li>If has adm advisor 5 is yes, and  has dip advisor 5 is yes, and  has mil advisor 5 is yes:</li><ul><li>change variable:</li><ul><li>which = BirsartansesPlanSuccessChance</li><li>value = 20</li></ul></ul><li>Else if has adm advisor 4 is yes, and  has dip advisor 4 is yes, and  has mil advisor 4 is yes:</li><ul><li>change variable:</li><ul><li>which = BirsartansesPlanSuccessChance</li><li>value = 10</li></ul></ul><li>set country flag [birsartanses_taking_test](../flags/birsartanses_taking_test.md)</li><li>capital scope:</li><ul><li>add province triggered modifier = birsartanses_25_year_plan_mod</li></ul></ul><li>set country flag [birsartanses_preparing_plan](../flags/birsartanses_preparing_plan.md)</li><li>custom tooltip = It will take a few days to prepare.</li> | <li>Any of the following:</li><ul><li>Country is Birsartanses</li><li>Country was Birsartanses</li></ul><li>has country flag [birsartanses_plans_enacted](../flags/birsartanses_plans_enacted.md)</li><li>None of the following:</li><ul><li>has country modifier F21_admin_plan</li><li>has country modifier  F21_diplo_plan</li><li>has country modifier   F21_milit_plan</li><li>has country modifier    F21_admin_plan_upgrade</li><li>has country modifier     F21_diplo_plan_upgrade</li><li>has country modifier      F21_milit_plan_upgrade</li><li>has country modifier       F21_plan_failure</li><li>has country flag [birsartanses_taking_test](../flags/birsartanses_taking_test.md)</li></ul> |
| <a name="birsartanses_integrate_goblins">Integrate Goblins</a><br />*In order to effectively use goblins and their peculiar advantages, we will need to invest in their societal acceptance and try to reduce friction with other races. Only then will we be able to make use of them efficiently.* | <li>any owned province:</li><ul><li>culture group is goblin</li><li>has owner accepted culture</li></ul><li>employed advisor:</li><ul><li>culture is exodus_goblin</li></ul><li>high tolerance goblin race trigger is yes</li> | <li>custom tooltip = Upgrade the cultural efficiency of the nation.</li><li>If has country modifier is F21 cultural efficiency 3:</li><ul><li>remove country modifier = F21_cultural_efficiency_3</li><li>country gets the modifier F21_cultural_efficiency_4 until otherwise removed</li></ul><li>Else if has country modifier is F21 cultural efficiency 2:</li><ul><li>remove country modifier = F21_cultural_efficiency_2</li><li>country gets the modifier F21_cultural_efficiency_3 until otherwise removed</li></ul><li>Else if has country modifier is F21 cultural efficiency 1:</li><ul><li>remove country modifier = F21_cultural_efficiency_1</li><li>country gets the modifier F21_cultural_efficiency_2 until otherwise removed</li></ul><li>Else if does not have country modifier is F21 cultural efficiency 1, and does not have country modifier is F21 cultural efficiency 2, and does not have country modifier is F21 cultural efficiency 3, and does not have country modifier is F21 cultural efficiency 4:</li><ul><li>country gets the modifier F21_cultural_efficiency_1 until otherwise removed</li></ul><li>hidden effect:</li><ul><li>set country flag [birsartanses_goblins_integrated](../flags/birsartanses_goblins_integrated.md)</li></ul> | <li>Any of the following:</li><ul><li>Country is Birsartanses</li><li>Country was Birsartanses</li></ul><li>accepted culture is exodus_goblin</li><li>None of the following:</li><ul><li>has country flag [birsartanses_goblins_integrated](../flags/birsartanses_goblins_integrated.md)</li></ul> |