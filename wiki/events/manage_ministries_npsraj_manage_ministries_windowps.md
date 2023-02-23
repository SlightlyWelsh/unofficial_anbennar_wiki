#Information
 - Title: Manage Ministries\n£raj_manage_ministries_window£
 - ID: rahenraj.3002
#Description
Manage Ministries\n£raj_manage_ministries_window£
#Options

___
##£event_button_mandate_back_rajmenu£

###Efects:<ul><li>hidden effect:</li><ul><li>the event ˻rahenraj.3000˼ happens</li></ul></ul>

___
##£event_button_ministries_increase_controls£

###Available if:
<li>None of the following:</li><ul><li>has country modifier raj_increased_ministries_controls</li></ul>

###AI weighting:
AI weights this option at 1
 - Multiplied by 100 if has disaster is rahen corrupt court
 - Multiplied by 50 if does not have 4411 has check variable has which is rajCohesionMonthy low liberty desire, and check variable has value is -0.25
 - Multiplied by 2 if does not have 4411 has check variable has which is rajCohesionMonthy low liberty desire, and check variable has value is -0.5
 - Multiplied by 3 if does not have 4411 has check variable has which is rajCohesionMonthy low liberty desire, and check variable has value is -1
 - Multiplied by 0.5 if has 4411 has check variable has which is rajCohesionMonthy high liberty desire, and check variable has value is 0.5
 - Multiplied by 0.5 if has 4411 has check variable has which is rajCohesionMonthy high liberty desire, and check variable has value is 1


###Efects:<ul><li>country gets the modifier raj_increased_ministries_controls for 10 years</li><li>custom tooltip = raj_vassals_get_increased_controls_privilege_tt</li><li>hidden effect:</li><ul><li>If every subject country is subject of type is daimyo vassal, and is subject of type is great daimyo vassal:</li><ul><li>set estate privilege = estate_raj_ministries_increased_controls</li><li>the event ˻rahenraj.3011˼ happens</li></ul><li>the event ˻rahenraj.3008˼ happens</li></ul></ul>

___
##£event_button_ministries_increase_controls_g£

###Available if:
<li>is not controlled by the AI</li><li>has country modifier raj_increased_ministries_controls</li>

###Efects:<ul><li>custom tooltip = raj_ministries_actions_only_every_10_years_tt</li><li>custom tooltip = raj_separator_tt</li><li>tooltip:</li><ul><li>country gets the modifier raj_increased_ministries_controls for 10 years</li></ul><li>custom tooltip = raj_vassals_get_increased_controls_privilege_tt</li><li>hidden effect:</li><ul><li>the event ˻rahenraj.3008˼ happens</li></ul></ul>

___
##£event_button_ministries_demand_introspection£

###Available if:
<li>None of the following:</li><ul><li>has country modifier raj_demanded_introspection</li></ul>

###AI weighting:
AI weights this option at 1
 - Multiplied by 50 if does not have 4411 has check variable has which is rajCohesionMonthy internal wars, and check variable has value is -0.1
 - Multiplied by 2 if does not have 4411 has check variable has which is rajCohesionMonthy internal wars, and check variable has value is -0.25
 - Multiplied by 3 if does not have 4411 has check variable has which is rajCohesionMonthy internal wars, and check variable has value is -0.5


###Efects:<ul><li>country gets the modifier raj_raja_introspecting for 3 years</li><li>custom tooltip = raj_vassals_get_introspection_privilege_tt</li><li>hidden effect:</li><ul><li>country gets the modifier raj_demanded_introspection for 10 years</li><li>If every subject country is subject of type is daimyo vassal, and is subject of type is great daimyo vassal:</li><ul><li>set estate privilege = estate_raj_ministries_demand_of_introspection</li><li>the event ˻rahenraj.3010˼ happens</li></ul><li>the event ˻rahenraj.3008˼ happens</li></ul></ul>

___
##£event_button_ministries_demand_introspection_g£

###Available if:
<li>is not controlled by the AI</li><li>has country modifier raj_demanded_introspection</li>

###Efects:<ul><li>custom tooltip = raj_ministries_actions_only_every_10_years_tt</li><li>custom tooltip = raj_separator_tt</li><li>tooltip:</li><ul><li>country gets the modifier raj_raja_introspecting for 3 years</li></ul><li>custom tooltip = raj_vassals_get_introspection_privilege_tt</li><li>hidden effect:</li><ul><li>the event ˻rahenraj.3008˼ happens</li></ul></ul>

___
##£event_button_ministries_agressive_policies£

###Available if:
<li>None of the following:</li><ul><li>has country modifier raj_raja_aggressive_policies</li></ul><li>4411:</li><ul><li>check variable:</li><ul><li>which is raj_cohesion</li><li>value is at least 75</li></ul></ul>

###AI weighting:
AI weights this option at 25
 - Multiplied by 2 if is at war
 - Multiplied by 20 if is at war, and does not have war score is -10


###Efects:<ul><li>country gets the modifier raj_raja_aggressive_policies for 10 years</li><li>custom tooltip = raj_vassals_get_aggressive_policies_privilege_tt</li><li>hidden effect:</li><ul><li>If every subject country is subject of type is great daimyo vassal:</li><ul><li>set estate privilege = estate_raj_ministries_aggressive_policies</li><li>the event ˻rahenraj.3012˼ happens</li></ul><li>the event ˻rahenraj.3008˼ happens</li></ul></ul>

___
##£event_button_ministries_agressive_policies_g£

###Available if:
<li>is not controlled by the AI</li><li>Any of the following:</li><ul><li>has country modifier raj_raja_aggressive_policies</li><li>4411:</li><ul><li>None of the following:</li><ul><li>check variable:</li><ul><li>which is raj_cohesion</li><li>value is at least 75</li></ul></ul></ul></ul>

###Efects:<ul><li>If has country modifier is raj raja aggressive policies:</li><ul><li>custom tooltip = raj_ministries_actions_only_every_10_years_tt</li></ul><li>If does not have check variable has which is raj cohesion, and check variable has value is 70:</li><ul><li>custom tooltip = raj_need_cohesion_75_tt</li></ul><li>custom tooltip = raj_separator_tt</li><li>tooltip:</li><ul><li>country gets the modifier raj_raja_aggressive_policies for 10 years</li></ul><li>custom tooltip = raj_vassals_get_aggressive_policies_privilege_tt</li><li>hidden effect:</li><ul><li>the event ˻rahenraj.3008˼ happens</li></ul></ul>

___
##£event_button_ministries_tutor_heir£

###Available if:
<li>has heir</li><li>None of the following:</li><ul><li>heir age is at least 15</li></ul><li>NOT:</li><ul><li>has country modifier raj_tutoring_heir</li></ul><li>NOT:</li><ul><li>has heir flag [raj_tutored_adm](../flags/raj_tutored_adm.md)</li><li>has heir flag  raj_tutored_dip</li><li>has heir flag   raj_tutored_mil</li></ul>

###AI weighting:
AI weights this option at 5
 - Multiplied by 3 if does not have heir adm is 3
 - Multiplied by 3 if does not have heir dip is 3
 - Multiplied by 3 if does not have heir mil is 3
 - Multiplied by 3 if does not have heir adm is 2
 - Multiplied by 3 if does not have heir dip is 2
 - Multiplied by 3 if does not have heir mil is 2


###Efects:<ul><li>custom tooltip = raj_heir_tutoring_effect_in_3_years_tt</li><li>add years of income = -0.25</li><li>tooltip:</li><ul><li>If does not have heir flag is [raj_tutored_adm](../flags/raj_tutored_adm.md):</li><ul><li>random list:</li><ul><li>1:</li><ul><li>modifier:</li><ul><li>factor = 2</li><li>has heir flag [raj_tutored_dip](../flags/raj_tutored_dip.md)</li></ul><li>modifier:</li><ul><li>factor = 2</li><li>has heir flag [raj_tutored_mil](../flags/raj_tutored_mil.md)</li></ul><li>change heir adm = 1</li></ul><li>2:</li><ul></ul></ul></ul><li>If does not have heir flag is [raj_tutored_dip](../flags/raj_tutored_dip.md):</li><ul><li>random list:</li><ul><li>1:</li><ul><li>modifier:</li><ul><li>factor = 2</li><li>has heir flag [raj_tutored_adm](../flags/raj_tutored_adm.md)</li></ul><li>modifier:</li><ul><li>factor = 2</li><li>has heir flag [raj_tutored_mil](../flags/raj_tutored_mil.md)</li></ul><li>change heir dip = 1</li></ul><li>2:</li><ul></ul></ul></ul><li>If does not have heir flag is [raj_tutored_mil](../flags/raj_tutored_mil.md):</li><ul><li>random list:</li><ul><li>1:</li><ul><li>modifier:</li><ul><li>factor = 2</li><li>has heir flag [raj_tutored_dip](../flags/raj_tutored_dip.md)</li></ul><li>modifier:</li><ul><li>factor = 2</li><li>has heir flag [raj_tutored_adm](../flags/raj_tutored_adm.md)</li></ul><li>change heir mil = 1</li></ul><li>2:</li><ul></ul></ul></ul></ul><li>hidden effect:</li><ul><li>country gets the modifier raj_tutoring_heir for 1115 days</li><li>set heir flag [raj_ministries_tutoring](../flags/raj_ministries_tutoring.md)</li><li>the event ˻rahenraj.3008˼ happens</li><li>the event ˻rahenraj.3013˼ happens</li></ul></ul>

___
##£event_button_ministries_tutor_heir_g£

###Available if:
<li>is not controlled by the AI</li><li>Any of the following:</li><ul><li>None of the following:</li><ul><li>has heir</li></ul><li>heir age is at least 15</li><li>has country modifier raj_tutoring_heir</li><li>All of the following:</li><ul><li>has heir flag [raj_tutored_adm](../flags/raj_tutored_adm.md)</li><li>has heir flag  raj_tutored_dip</li><li>has heir flag   raj_tutored_mil</li></ul></ul>

###Efects:<ul><li>If does not have heir, and has heir age is 15:</li><ul><li>custom tooltip = raj_has_an_heir_younger_than_15_tt</li></ul><li>If has country modifier is raj tutoring heir:</li><ul><li>custom tooltip = raj_ministries_actions_only_every_3_years_tt</li></ul><li>If has heir flag is [raj_tutored_adm](../flags/raj_tutored_adm.md), and  has heir flag is raj tutored dip, and  has heir flag is raj tutored mil:</li><ul><li>custom tooltip = raj_ministries_actions_only_every_3_years_tt</li></ul><li>custom tooltip = raj_separator_tt</li><li>custom tooltip = raj_heir_tutoring_effect_in_3_years_tt</li><li>tooltip:</li><ul><li>add years of income = -0.25</li><li>If does not have heir flag is [raj_tutored_adm](../flags/raj_tutored_adm.md):</li><ul><li>random list:</li><ul><li>1:</li><ul><li>modifier:</li><ul><li>factor = 2</li><li>has heir flag [raj_tutored_dip](../flags/raj_tutored_dip.md)</li></ul><li>modifier:</li><ul><li>factor = 2</li><li>has heir flag [raj_tutored_mil](../flags/raj_tutored_mil.md)</li></ul><li>change heir adm = 1</li></ul><li>2:</li><ul></ul></ul></ul><li>If does not have heir flag is [raj_tutored_dip](../flags/raj_tutored_dip.md):</li><ul><li>random list:</li><ul><li>1:</li><ul><li>modifier:</li><ul><li>factor = 2</li><li>has heir flag [raj_tutored_adm](../flags/raj_tutored_adm.md)</li></ul><li>modifier:</li><ul><li>factor = 2</li><li>has heir flag [raj_tutored_mil](../flags/raj_tutored_mil.md)</li></ul><li>change heir dip = 1</li></ul><li>2:</li><ul></ul></ul></ul><li>If does not have heir flag is [raj_tutored_mil](../flags/raj_tutored_mil.md):</li><ul><li>random list:</li><ul><li>1:</li><ul><li>modifier:</li><ul><li>factor = 2</li><li>has heir flag [raj_tutored_dip](../flags/raj_tutored_dip.md)</li></ul><li>modifier:</li><ul><li>factor = 2</li><li>has heir flag [raj_tutored_adm](../flags/raj_tutored_adm.md)</li></ul><li>change heir mil = 1</li></ul><li>2:</li><ul></ul></ul></ul></ul><li>hidden effect:</li><ul><li>the event ˻rahenraj.3008˼ happens</li></ul></ul>

___
##£event_button_ministries_census£

###Available if:
<li>None of the following:</li><ul><li>has country modifier raj_ministerial_census</li></ul><li>adm power is at least 50</li><li>dip power is at least 50</li><li>mil power is at least 50</li>

###AI weighting:
AI weights this option at 1
 - Multiplied by 50 if does not have 4411 has check variable has which is rajCohesionMonthy ministries influence, and check variable has value is 0.5
 - Multiplied by 2 if does not have 4411 has check variable has which is rajCohesionMonthy ministries influence, and check variable has value is 0.25
 - Multiplied by 10 if does not have 4411 has check variable has which is rajCohesionMonthy ministries influence, and check variable has value is 0


###Efects:<ul><li>raj cohesion change absolute:</li><ul><li>amount = 5</li></ul><li>add adm power = -50</li><li>add dip power = -50</li><li>add mil power = -50</li><li>custom tooltip = raj_ministries_ministerial_census_tt</li><li>hidden effect:</li><ul><li>country gets the modifier raj_ministerial_census for 10 years</li><li>If every subject country is subject of type is daimyo vassal, and is subject of type is great daimyo vassal:</li><ul><li>the event ˻rahenraj.1200˼ happens</li></ul><li>the event ˻rahenraj.3008˼ happens</li></ul></ul>

___
##£event_button_ministries_census_g£

###Available if:
<li>is not controlled by the AI</li><li>Any of the following:</li><ul><li>has country modifier raj_ministerial_census</li><li>None of the following:</li><ul><li>adm power is at least 50</li><li>dip power is at least 50</li><li>mil power is at least 50</li></ul></ul>

###Efects:<ul><li>If has country modifier is raj ministerial census:</li><ul><li>custom tooltip = raj_ministries_actions_only_every_10_years_tt</li></ul><li>If does not have adm power is 50:</li><ul><li>custom tooltip = raj_need_50_adm_tt</li></ul><li>If does not have dip power is 50:</li><ul><li>custom tooltip = raj_need_50_dip_tt</li></ul><li>If does not have mil power is 50:</li><ul><li>custom tooltip = raj_need_50_mil_tt</li></ul><li>custom tooltip = raj_separator_tt</li><li>tooltip:</li><ul><li>raj cohesion change absolute:</li><ul><li>amount = 5</li></ul><li>add adm power = -50</li><li>add dip power = -50</li><li>add mil power = -50</li></ul><li>custom tooltip = raj_ministries_ministerial_census_tt</li><li>hidden effect:</li><ul><li>the event ˻rahenraj.3008˼ happens</li></ul></ul>

___
##£event_button_ministries_crack_on_decadence£

###Available if:
<li>4411:</li><ul><li>None of the following:</li><ul><li>check variable:</li><ul><li>which is raj_cohesion</li><li>value is at least 30</li></ul></ul></ul><li>None of the following:</li><ul><li>has country modifier raj_cracking_on_decadence</li></ul><li>dip power is at least 50</li><li>treasury is at least 350</li>

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>raj cohesion change absolute:</li><ul><li>amount = 15</li></ul><li>add dip power = -50</li><li>add treasury = -350</li><li>custom tooltip = raj_cracking_on_decadence_tt</li><li>hidden effect:</li><ul><li>country gets the modifier raj_cracking_on_decadence for 10 years</li><li>If every subject country is subject of type is daimyo vassal, and is subject of type is great daimyo vassal:</li><ul><li>the event ˻rahenraj.3016˼ happens</li><li>add liberty desire = 15</li><li>set estate privilege = estate_raj_ministries_cracking_on_decadence</li></ul><li>the event ˻rahenraj.3008˼ happens</li></ul></ul>

___
##£event_button_ministries_crack_on_decadence_g£

###Available if:
<li>is not controlled by the AI</li><li>Any of the following:</li><ul><li>4411:</li><ul><li>check variable:</li><ul><li>which is raj_cohesion</li><li>value is at least 30</li></ul></ul><li>has country modifier raj_cracking_on_decadence</li><li>None of the following:</li><ul><li>dip power is at least 50</li><li>treasury is at least 350</li></ul></ul>

###Efects:<ul><li>If has country modifier is raj cracking on decadence:</li><ul><li>custom tooltip = raj_ministries_actions_only_every_10_years_tt</li></ul><li>If has 4411 has check variable has which is raj cohesion, and check variable has value is 30:</li><ul><li>custom tooltip = raj_need_less_cohesion_30_tt</li></ul><li>If does not have dip power is 50:</li><ul><li>custom tooltip = raj_need_50_dip_tt</li></ul><li>If does not have treasury is 350:</li><ul><li>custom tooltip = raj_need_350_cash_tt</li></ul><li>custom tooltip = raj_separator_tt</li><li>tooltip:</li><ul><li>raj cohesion change absolute:</li><ul><li>amount = 15</li></ul><li>add dip power = -50</li><li>add treasury = -350</li></ul><li>custom tooltip = raj_cracking_on_decadence_tt</li><li>hidden effect:</li><ul><li>the event ˻rahenraj.3008˼ happens</li></ul></ul>

___
##£event_button_ministries_regulate_vizier£

###Available if:
<li>4411:</li><ul><li>check variable:</li><ul><li>which is raj_cohesion</li><li>value is at least 60</li></ul></ul><li>None of the following:</li><ul><li>has country modifier raj_regulating_vizier</li></ul><li>adm power is at least 50</li>

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>add adm power = -50</li><li>raj cohesion change absolute:</li><ul><li>amount = -10</li></ul><li>raj vizier sway change:</li><ul><li>amount = -10</li></ul><li>If random subject country has country flag is [raj_vizier](../flags/raj_vizier.md):</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = raj_regulated_vizier</li></ul><li>hidden effect:</li><ul><li>the event ˻rahenraj.3017˼ happens</li></ul></ul><li>hidden effect:</li><ul><li>country gets the modifier raj_regulating_vizier for 10 years</li><li>the event ˻rahenraj.3008˼ happens</li></ul></ul>

___
##£event_button_ministries_regulate_vizier_g£

###Available if:
<li>is not controlled by the AI</li><li>Any of the following:</li><ul><li>has country modifier raj_regulating_vizier</li><li>4411:</li><ul><li>None of the following:</li><ul><li>check variable:</li><ul><li>which is raj_cohesion</li><li>value is at least 60</li></ul></ul></ul><li>None of the following:</li><ul><li>adm power is at least 50</li></ul></ul>

###Efects:<ul><li>If has country modifier is raj regulating vizier:</li><ul><li>custom tooltip = raj_ministries_actions_only_every_10_years_tt</li></ul><li>If does not have check variable has which is raj cohesion, and check variable has value is 60:</li><ul><li>custom tooltip = raj_need_cohesion_60_tt</li></ul><li>If does not have adm power is 50:</li><ul><li>custom tooltip = raj_need_50_adm_tt</li></ul><li>custom tooltip = raj_separator_tt</li><li>tooltip:</li><ul><li>add adm power = -50</li><li>raj cohesion change absolute:</li><ul><li>amount = -10</li></ul><li>raj vizier sway change:</li><ul><li>amount = -10</li></ul><li>If random subject country has country flag is [raj_vizier](../flags/raj_vizier.md):</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = raj_regulated_vizier</li></ul></ul></ul><li>hidden effect:</li><ul><li>the event ˻rahenraj.3008˼ happens</li></ul></ul>

___
##£event_button_ministries_tax_policies£

###Available if:
<li>4411:</li><ul><li>check variable:</li><ul><li>which is raj_cohesion</li><li>value is at least 60</li></ul></ul><li>None of the following:</li><ul><li>has country modifier raj_new_tax_policies</li></ul><li>dip power is at least 50</li>

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>raj cohesion change absolute:</li><ul><li>amount = -10</li></ul><li>add dip power = 50</li><li>country gets the modifier raj_new_tax_policies for 10 years</li><li>hidden effect:</li><ul><li>the event ˻rahenraj.3008˼ happens</li></ul></ul>

___
##£event_button_ministries_tax_policies_g£

###Available if:
<li>is not controlled by the AI</li><li>Any of the following:</li><ul><li>has country modifier raj_new_tax_policies</li><li>4411:</li><ul><li>None of the following:</li><ul><li>check variable:</li><ul><li>which is raj_cohesion</li><li>value is at least 60</li></ul></ul></ul><li>None of the following:</li><ul><li>dip power is at least 50</li></ul></ul>

###Efects:<ul><li>If has country modifier is raj new tax policies:</li><ul><li>custom tooltip = raj_ministries_actions_only_every_10_years_tt</li></ul><li>If does not have check variable has which is raj cohesion, and check variable has value is 60:</li><ul><li>custom tooltip = raj_need_cohesion_60_tt</li></ul><li>If does not have dip power is 50:</li><ul><li>custom tooltip = raj_need_50_dip_tt</li></ul><li>custom tooltip = raj_separator_tt</li><li>tooltip:</li><ul><li>raj cohesion change absolute:</li><ul><li>amount = -10</li></ul><li>add dip power = -50</li><li>country gets the modifier raj_new_tax_policies for 10 years</li></ul><li>hidden effect:</li><ul><li>the event ˻rahenraj.3008˼ happens</li></ul></ul>

___
##£event_button_mandate_back_rajmenu£

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.1 if does not have 4411 has check variable has which is raj cohesion, and check variable has value is 40


###Efects:<ul><li>If is not controlled by the AI:</li><ul><li>hidden effect:</li><ul><li>the event ˻rahenraj.3000˼ happens</li></ul></ul></ul>
