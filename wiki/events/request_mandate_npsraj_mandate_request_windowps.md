#Information
 - Title: Request Mandate\n£raj_mandate_request_window£
 - ID: rahenraj.1002
#Description
Request Mandate\n£raj_mandate_request_window£
#Options

___
##£event_button_mandate_back_rajmenu£

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>add dip power = 50</li><li>hidden effect:</li><ul><li>clr country flag [raj_requested_mandate](../flags/raj_requested_mandate.md)</li><li>If is not controlled by the AI:</li><ul><li>the event [The Raj\n£raj_menu_window£\n\n\n\n[raja_global_target.GetFlag] \n[4411.GetRajCohesion]\n[raj_vizier_global_target.GetFlag]                                                               \n\n[raja_global_target.GetName] \n[raj_vizier_global_target.GetName]                                                               \n\n\n[4411.GetRajVizierBar]                                                               \n[Root.GetVizierRanking] ](../events/the_raj_npsraj_menu_windowps_n_n_n_n_raja_global_target_getflag_n_4411_getrajcohesion_n_raj_vizier_global_target_getflag_n_n_raja_global_target_getname_n_raj_vizier_global_target_getname) happens</li></ul></ul></ul>

___
##£event_button_mandate_protection£

###Available if:
<li>Any of the following:</li><ul><li>check variable:</li><ul><li>which is rajMandateReasonsProtectionDiff</li><li>value is at least 1</li></ul><li>All of the following:</li><ul><li>overlord:</li><ul><li>is not controlled by the AI</li></ul><li>4411:</li><ul><li>is variable equal:</li><ul><li>which is rajProtectionSetting</li><li>value is at least 0</li></ul></ul></ul></ul>

###AI weighting:
AI weights this option at 5
 - Multiplied by 0 if has total development is 60
 - Multiplied by 4 if does not have num of cities is 2
 - Multiplied by 2 if has any neighbor country has overlord has overlord of is ROOT; and does not have alliance with is ROOT; and any neighbor country has army strength has who is ROOT, and army strength has value is 2


###Efects:<ul><li>raj cohesion change:</li><ul><li>amount = 10</li><li>mandate = yes</li></ul><li>custom tooltip = request_raj_mandate_tt</li><li>tooltip:</li><ul><li>country gets the modifier raj_mandate_raja_protection for 15 years</li><li>custom tooltip = desc_raj_mandate_raja_protection</li></ul><li>hidden effect:</li><ul><li>set country flag [requested_raj_mandate_raja_protection](../flags/requested_raj_mandate_raja_protection.md)</li><li>overlord:</li><ul><li>If is not controlled by the AI, and  has 4411 is variable equal has which is rajProtectionSetting, and is variable equal has value is 0:</li><ul><li>the event [[From.GetName] requests a Mandate of the Raj](../events/from_getname_requests_a_mandate_of_the_raj.md) happens</li></ul><li>else:</li><ul><li>the event [[From.GetName] requests a Mandate of the Raj](../events/from_getname_requests_a_mandate_of_the_raj_1.md) happens</li></ul></ul><li>clr country flag [raj_requested_mandate](../flags/raj_requested_mandate.md)</li><li>If is not controlled by the AI:</li><ul><li>the event [The Raj\n£raj_menu_window£\n\n\n\n[raja_global_target.GetFlag] \n[4411.GetRajCohesion]\n[raj_vizier_global_target.GetFlag]                                                               \n\n[raja_global_target.GetName] \n[raj_vizier_global_target.GetName]                                                               \n\n\n[4411.GetRajVizierBar]                                                               \n[Root.GetVizierRanking] ](../events/the_raj_npsraj_menu_windowps_n_n_n_n_raja_global_target_getflag_n_4411_getrajcohesion_n_raj_vizier_global_target_getflag_n_n_raja_global_target_getname_n_raj_vizier_global_target_getname) happens</li></ul></ul><li>custom tooltip = raj_mandate_reasons_accept_tt</li><li>custom tooltip = raj_mandate_reasons_protection_tt</li></ul>

___
##£event_button_mandate_protection_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>check variable:</li><ul><li>which is rajMandateReasonsProtectionDiff</li><li>value is at least 1</li></ul></ul><li>Any of the following:</li><ul><li>overlord:</li><ul><li>is controlled by the AI</li></ul><li>4411:</li><ul><li>None of the following:</li><ul><li>is variable equal:</li><ul><li>which is rajProtectionSetting</li><li>value is at least 0</li></ul></ul></ul></ul>

###Efects:<ul><li>custom tooltip = request_raj_mandate_tt</li><li>tooltip:</li><ul><li>country gets the modifier raj_mandate_raja_protection for 15 years</li><li>custom tooltip = desc_raj_mandate_raja_protection</li></ul><li>custom tooltip = raj_mandate_reasons_refuse_tt</li><li>custom tooltip = raj_mandate_reasons_protection_tt</li><li>If has 4411 has check variable has which is raj cohesion, and check variable has value is 80:</li><ul><li>custom tooltip = raj_mandate_reasons_80_cohesion_tt</li></ul><li>hidden effect:</li><ul><li>the event [Missing localisation: rahenraj_3007_t](../events/missing_localisation_rahenraj_3007_t.md) happens</li></ul></ul>

___
##£event_button_mandate_expansion£

###Available if:
<li>Any of the following:</li><ul><li>check variable:</li><ul><li>which is rajMandateReasonsExpansionDiff</li><li>value is at least 1</li></ul><li>All of the following:</li><ul><li>overlord:</li><ul><li>is not controlled by the AI</li></ul><li>4411:</li><ul><li>is variable equal:</li><ul><li>which is rajExpansionSetting</li><li>value is at least 0</li></ul></ul></ul></ul><li>None of the following:</li><ul><li>has country flag [raj_vizier](../flags/raj_vizier.md)</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 2 if has any neighbor country has overlord has overlord of is ROOT; and does not have alliance with is ROOT; and any neighbor country has ROOT has army strength has who is PREV, and army strength has value is 2
 - Multiplied by 0 if does not have 4411 has check variable has which is raj cohesion, and check variable has value is 80; and does not have total development is 100


###Efects:<ul><li>raj cohesion change:</li><ul><li>amount = 10</li><li>mandate = yes</li></ul><li>custom tooltip = request_raj_mandate_tt</li><li>tooltip:</li><ul><li>country gets the modifier raj_mandate_right_to_expansion for 15 years</li><li>custom tooltip = desc_raj_mandate_right_to_expansion</li></ul><li>hidden effect:</li><ul><li>set country flag [requested_raj_mandate_right_to_expansion](../flags/requested_raj_mandate_right_to_expansion.md)</li><li>overlord:</li><ul><li>If is not controlled by the AI, and  has 4411 is variable equal has which is rajExpansionSetting, and is variable equal has value is 0:</li><ul><li>the event [[From.GetName] requests a Mandate of the Raj](../events/from_getname_requests_a_mandate_of_the_raj.md) happens</li></ul><li>else:</li><ul><li>the event [[From.GetName] requests a Mandate of the Raj](../events/from_getname_requests_a_mandate_of_the_raj_1.md) happens</li></ul></ul><li>clr country flag [raj_requested_mandate](../flags/raj_requested_mandate.md)</li><li>If is not controlled by the AI:</li><ul><li>the event [The Raj\n£raj_menu_window£\n\n\n\n[raja_global_target.GetFlag] \n[4411.GetRajCohesion]\n[raj_vizier_global_target.GetFlag]                                                               \n\n[raja_global_target.GetName] \n[raj_vizier_global_target.GetName]                                                               \n\n\n[4411.GetRajVizierBar]                                                               \n[Root.GetVizierRanking] ](../events/the_raj_npsraj_menu_windowps_n_n_n_n_raja_global_target_getflag_n_4411_getrajcohesion_n_raj_vizier_global_target_getflag_n_n_raja_global_target_getname_n_raj_vizier_global_target_getname) happens</li></ul></ul><li>custom tooltip = raj_mandate_reasons_accept_tt</li><li>custom tooltip = raj_mandate_reasons_expansion_tt</li><li>custom tooltip = raj_mandate_reasons_num_cities_tt</li></ul>

___
##£event_button_mandate_expansion_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>check variable:</li><ul><li>which is rajMandateReasonsExpansionDiff</li><li>value is at least 1</li></ul></ul><li>Any of the following:</li><ul><li>overlord:</li><ul><li>is controlled by the AI</li></ul><li>4411:</li><ul><li>None of the following:</li><ul><li>is variable equal:</li><ul><li>which is rajExpansionSetting</li><li>value is at least 0</li></ul></ul></ul></ul>

###Efects:<ul><li>custom tooltip = request_raj_mandate_tt</li><li>tooltip:</li><ul><li>country gets the modifier raj_mandate_right_to_expansion for 15 years</li><li>custom tooltip = desc_raj_mandate_right_to_expansion</li></ul><li>custom tooltip = raj_mandate_reasons_refuse_tt</li><li>custom tooltip = raj_mandate_reasons_expansion_tt</li><li>custom tooltip = raj_mandate_reasons_num_cities_tt</li><li>hidden effect:</li><ul><li>the event [Missing localisation: rahenraj_3007_t](../events/missing_localisation_rahenraj_3007_t.md) happens</li></ul></ul>

___
##£event_button_mandate_autonomy£

###Available if:
<li>Any of the following:</li><ul><li>check variable:</li><ul><li>which is rajMandateReasonsAutonomyDiff</li><li>value is at least 1</li></ul><li>All of the following:</li><ul><li>overlord:</li><ul><li>is not controlled by the AI</li></ul><li>4411:</li><ul><li>is variable equal:</li><ul><li>which is rajAutonomySetting</li><li>value is at least 0</li></ul></ul></ul></ul>

###AI weighting:
AI weights this option at 10
 - Multiplied by 0 if has overlord has disaster is rahen corrupt court
 - Multiplied by 0 if does not have 4411 has check variable has which is raj cohesion, and check variable has value is 80


###Efects:<ul><li>raj cohesion change:</li><ul><li>amount = 10</li><li>mandate = yes</li></ul><li>custom tooltip = request_raj_mandate_tt</li><li>tooltip:</li><ul><li>country gets the modifier raj_mandate_guaranteed_autonomy for 15 years</li><li>custom tooltip = desc_raj_mandate_guaranteed_autonomy</li></ul><li>hidden effect:</li><ul><li>set country flag [requested_raj_mandate_guaranteed_autonomy](../flags/requested_raj_mandate_guaranteed_autonomy.md)</li><li>overlord:</li><ul><li>If is not controlled by the AI, and  has 4411 is variable equal has which is rajAutonomySetting, and is variable equal has value is 0:</li><ul><li>the event [[From.GetName] requests a Mandate of the Raj](../events/from_getname_requests_a_mandate_of_the_raj.md) happens</li></ul><li>else:</li><ul><li>the event [[From.GetName] requests a Mandate of the Raj](../events/from_getname_requests_a_mandate_of_the_raj_1.md) happens</li></ul></ul><li>clr country flag [raj_requested_mandate](../flags/raj_requested_mandate.md)</li><li>If is not controlled by the AI:</li><ul><li>the event [The Raj\n£raj_menu_window£\n\n\n\n[raja_global_target.GetFlag] \n[4411.GetRajCohesion]\n[raj_vizier_global_target.GetFlag]                                                               \n\n[raja_global_target.GetName] \n[raj_vizier_global_target.GetName]                                                               \n\n\n[4411.GetRajVizierBar]                                                               \n[Root.GetVizierRanking] ](../events/the_raj_npsraj_menu_windowps_n_n_n_n_raja_global_target_getflag_n_4411_getrajcohesion_n_raj_vizier_global_target_getflag_n_n_raja_global_target_getname_n_raj_vizier_global_target_getname) happens</li></ul></ul><li>custom tooltip = raj_mandate_reasons_accept_tt</li><li>custom tooltip = raj_mandate_reasons_autonomy_tt</li></ul>

___
##£event_button_mandate_autonomy_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>check variable:</li><ul><li>which is rajMandateReasonsAutonomyDiff</li><li>value is at least 1</li></ul></ul><li>Any of the following:</li><ul><li>overlord:</li><ul><li>is controlled by the AI</li></ul><li>4411:</li><ul><li>None of the following:</li><ul><li>is variable equal:</li><ul><li>which is rajAutonomySetting</li><li>value is at least 0</li></ul></ul></ul></ul>

###Efects:<ul><li>custom tooltip = request_raj_mandate_tt</li><li>tooltip:</li><ul><li>country gets the modifier raj_mandate_guaranteed_autonomy for 15 years</li><li>custom tooltip = desc_raj_mandate_guaranteed_autonomy</li></ul><li>hidden effect:</li><ul><li>the event [Missing localisation: rahenraj_3007_t](../events/missing_localisation_rahenraj_3007_t.md) happens</li></ul><li>custom tooltip = raj_mandate_reasons_refuse_tt</li><li>custom tooltip = raj_mandate_reasons_autonomy_tt</li><li>If does not have liberty desire is 30:</li><ul><li>custom tooltip = raj_mandate_reasons_low_LD_tt</li></ul></ul>

___
##£event_button_mandate_trading£

###Available if:
<li>Any of the following:</li><ul><li>check variable:</li><ul><li>which is rajMandateReasonsTradingDiff</li><li>value is at least 1</li></ul><li>All of the following:</li><ul><li>overlord:</li><ul><li>is not controlled by the AI</li></ul><li>4411:</li><ul><li>is variable equal:</li><ul><li>which is rajTradingSetting</li><li>value is at least 0</li></ul></ul></ul></ul>

###AI weighting:
AI weights this option at 10


###Efects:<ul><li>raj cohesion change:</li><ul><li>amount = 10</li><li>mandate = yes</li></ul><li>custom tooltip = request_raj_mandate_tt</li><li>add years of income = -0.5</li><li>tooltip:</li><ul><li>country gets the modifier raj_mandate_mercantile_preference for 15 years</li></ul><li>hidden effect:</li><ul><li>set country flag [requested_raj_mandate_mercantile_preference](../flags/requested_raj_mandate_mercantile_preference.md)</li><li>overlord:</li><ul><li>If is not controlled by the AI, and  has 4411 is variable equal has which is rajTradingSetting, and is variable equal has value is 0:</li><ul><li>the event [[From.GetName] requests a Mandate of the Raj](../events/from_getname_requests_a_mandate_of_the_raj.md) happens</li></ul><li>else:</li><ul><li>the event [[From.GetName] requests a Mandate of the Raj](../events/from_getname_requests_a_mandate_of_the_raj_1.md) happens</li></ul></ul><li>clr country flag [raj_requested_mandate](../flags/raj_requested_mandate.md)</li><li>If is not controlled by the AI:</li><ul><li>the event [The Raj\n£raj_menu_window£\n\n\n\n[raja_global_target.GetFlag] \n[4411.GetRajCohesion]\n[raj_vizier_global_target.GetFlag]                                                               \n\n[raja_global_target.GetName] \n[raj_vizier_global_target.GetName]                                                               \n\n\n[4411.GetRajVizierBar]                                                               \n[Root.GetVizierRanking] ](../events/the_raj_npsraj_menu_windowps_n_n_n_n_raja_global_target_getflag_n_4411_getrajcohesion_n_raj_vizier_global_target_getflag_n_n_raja_global_target_getname_n_raj_vizier_global_target_getname) happens</li></ul></ul><li>custom tooltip = raj_mandate_reasons_accept_tt</li><li>custom tooltip = raj_mandate_reasons_trading_tt</li></ul>

___
##£event_button_mandate_trading_g£

###Available if:
<li>Any of the following:</li><ul><li>check variable:</li><ul><li>which is rajMandateReasonsTradingDiff</li><li>value is at least 1</li></ul><li>All of the following:</li><ul><li>overlord:</li><ul><li>is not controlled by the AI</li></ul><li>4411:</li><ul><li>is variable equal:</li><ul><li>which is rajTradingSetting</li><li>value is at least 0</li></ul></ul></ul></ul>

###Efects:<ul><li>custom tooltip = request_raj_mandate_tt</li><li>tooltip:</li><ul><li>add years of income = -0.5</li><li>country gets the modifier raj_mandate_mercantile_preference for 15 years</li></ul><li>hidden effect:</li><ul><li>the event [Missing localisation: rahenraj_3007_t](../events/missing_localisation_rahenraj_3007_t.md) happens</li></ul><li>custom tooltip = raj_mandate_reasons_refuse_tt</li><li>custom tooltip = raj_mandate_reasons_trading_tt</li></ul>

___
##£event_button_mandate_armoury£

###Available if:
<li>has reform senapti_reform</li><li>Any of the following:</li><ul><li>check variable:</li><ul><li>which is rajMandateReasonsArmouryDiff</li><li>value is at least 1</li></ul><li>All of the following:</li><ul><li>overlord:</li><ul><li>is not controlled by the AI</li></ul><li>4411:</li><ul><li>is variable equal:</li><ul><li>which is rajArmourySetting</li><li>value is at least 0</li></ul></ul></ul></ul>

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>raj cohesion change:</li><ul><li>amount = 10</li><li>mandate = yes</li></ul><li>custom tooltip = request_raj_mandate_tt</li><li>add years of income = -0.5</li><li>tooltip:</li><ul><li>country gets the modifier raj_mandate_sanctioned_armoury for 15 years</li></ul><li>hidden effect:</li><ul><li>set country flag [requested_raj_mandate_sanctioned_armoury](../flags/requested_raj_mandate_sanctioned_armoury.md)</li><li>overlord:</li><ul><li>If is not controlled by the AI, and  has 4411 is variable equal has which is rajArmourySetting, and is variable equal has value is 0:</li><ul><li>the event [[From.GetName] requests a Mandate of the Raj](../events/from_getname_requests_a_mandate_of_the_raj.md) happens</li></ul><li>else:</li><ul><li>the event [[From.GetName] requests a Mandate of the Raj](../events/from_getname_requests_a_mandate_of_the_raj_1.md) happens</li></ul></ul><li>clr country flag [raj_requested_mandate](../flags/raj_requested_mandate.md)</li><li>If is not controlled by the AI:</li><ul><li>the event [The Raj\n£raj_menu_window£\n\n\n\n[raja_global_target.GetFlag] \n[4411.GetRajCohesion]\n[raj_vizier_global_target.GetFlag]                                                               \n\n[raja_global_target.GetName] \n[raj_vizier_global_target.GetName]                                                               \n\n\n[4411.GetRajVizierBar]                                                               \n[Root.GetVizierRanking] ](../events/the_raj_npsraj_menu_windowps_n_n_n_n_raja_global_target_getflag_n_4411_getrajcohesion_n_raj_vizier_global_target_getflag_n_n_raja_global_target_getname_n_raj_vizier_global_target_getname) happens</li></ul></ul><li>custom tooltip = raj_mandate_reasons_accept_tt</li><li>custom tooltip = raj_mandate_reasons_armoury_tt</li></ul>

___
##£event_button_mandate_armoury_g£

###Available if:
<li>Any of the following:</li><ul><li>check variable:</li><ul><li>which is rajMandateReasonsArmouryDiff</li><li>value is at least 1</li></ul><li>All of the following:</li><ul><li>overlord:</li><ul><li>is not controlled by the AI</li></ul><li>4411:</li><ul><li>is variable equal:</li><ul><li>which is rajArmourySetting</li><li>value is at least 0</li></ul></ul></ul></ul>

###Efects:<ul><li>custom tooltip = request_raj_mandate_tt</li><li>tooltip:</li><ul><li>add years of income = -0.5</li><li>country gets the modifier raj_mandate_sanctioned_armoury for 15 years</li></ul><li>hidden effect:</li><ul><li>the event [Missing localisation: rahenraj_3007_t](../events/missing_localisation_rahenraj_3007_t.md) happens</li></ul><li>custom tooltip = raj_mandate_reasons_refuse_tt</li><li>custom tooltip = raj_mandate_reasons_armoury_tt</li></ul>

___
##£event_button_mandate_education£

###Available if:
<li>Any of the following:</li><ul><li>check variable:</li><ul><li>which is rajMandateReasonsEducationDiff</li><li>value is at least 1</li></ul><li>All of the following:</li><ul><li>overlord:</li><ul><li>is not controlled by the AI</li></ul><li>4411:</li><ul><li>is variable equal:</li><ul><li>which is rajEducationSetting</li><li>value is at least 0</li></ul></ul></ul></ul>

###AI weighting:
AI weights this option at 10
 - Multiplied by 0 if does not have adm tech is 5


###Efects:<ul><li>raj cohesion change:</li><ul><li>amount = 10</li><li>mandate = yes</li></ul><li>custom tooltip = request_raj_mandate_tt</li><li>add years of income = -0.5</li><li>tooltip:</li><ul><li>country gets the modifier raj_mandate_ministry_lectures for 15 years</li></ul><li>hidden effect:</li><ul><li>set country flag [requested_raj_mandate_ministry_lectures](../flags/requested_raj_mandate_ministry_lectures.md)</li><li>overlord:</li><ul><li>If is not controlled by the AI, and  has 4411 is variable equal has which is rajEducationSetting, and is variable equal has value is 0:</li><ul><li>the event [[From.GetName] requests a Mandate of the Raj](../events/from_getname_requests_a_mandate_of_the_raj.md) happens</li></ul><li>else:</li><ul><li>the event [[From.GetName] requests a Mandate of the Raj](../events/from_getname_requests_a_mandate_of_the_raj_1.md) happens</li></ul></ul><li>clr country flag [raj_requested_mandate](../flags/raj_requested_mandate.md)</li><li>If is not controlled by the AI:</li><ul><li>the event [The Raj\n£raj_menu_window£\n\n\n\n[raja_global_target.GetFlag] \n[4411.GetRajCohesion]\n[raj_vizier_global_target.GetFlag]                                                               \n\n[raja_global_target.GetName] \n[raj_vizier_global_target.GetName]                                                               \n\n\n[4411.GetRajVizierBar]                                                               \n[Root.GetVizierRanking] ](../events/the_raj_npsraj_menu_windowps_n_n_n_n_raja_global_target_getflag_n_4411_getrajcohesion_n_raj_vizier_global_target_getflag_n_n_raja_global_target_getname_n_raj_vizier_global_target_getname) happens</li></ul></ul><li>custom tooltip = raj_mandate_reasons_accept_tt</li><li>custom tooltip = raj_mandate_reasons_education_tt</li></ul>

___
##£event_button_mandate_education_g£

###Available if:
<li>Any of the following:</li><ul><li>check variable:</li><ul><li>which is rajMandateEducationEducationDiff</li><li>value is at least 1</li></ul><li>All of the following:</li><ul><li>overlord:</li><ul><li>is not controlled by the AI</li></ul><li>4411:</li><ul><li>is variable equal:</li><ul><li>which is rajEducationSetting</li><li>value is at least 0</li></ul></ul></ul></ul>

###Efects:<ul><li>custom tooltip = request_raj_mandate_tt</li><li>tooltip:</li><ul><li>add years of income = -0.5</li><li>country gets the modifier raj_mandate_ministry_lectures for 15 years</li></ul><li>hidden effect:</li><ul><li>the event [Missing localisation: rahenraj_3007_t](../events/missing_localisation_rahenraj_3007_t.md) happens</li></ul><li>custom tooltip = raj_mandate_reasons_refuse_tt</li><li>custom tooltip = raj_mandate_reasons_education_tt</li></ul>

___
##£event_button_mandate_senapti£

###Available if:
<li>has reform senapti_reform</li><li>Any of the following:</li><ul><li>check variable:</li><ul><li>which is rajMandateReasonsSenaptiDiff</li><li>value is at least 1</li></ul><li>All of the following:</li><ul><li>overlord:</li><ul><li>is not controlled by the AI</li></ul><li>4411:</li><ul><li>is variable equal:</li><ul><li>which is rajSenaptiSetting</li><li>value is at least 0</li></ul></ul></ul></ul>

###AI weighting:
AI weights this option at 10
 - Multiplied by 10 if does not have overlord has any subject country is subject of type is great daimyo vassal, and does not have country modifier is prabhi recently promoted; and does not have country modifier is raj mandate senapti primacy; and does not have country modifier is rajiya senapti; and does not have tag is ROOT; and does not have total development is ROOT


###Efects:<ul><li>raj cohesion change:</li><ul><li>amount = 10</li><li>mandate = yes</li></ul><li>custom tooltip = request_raj_mandate_tt</li><li>tooltip:</li><ul><li>country gets the modifier raj_mandate_senapti_primacy for 15 years</li><li>custom tooltip = desc_raj_mandate_senapti_primacy</li></ul><li>hidden effect:</li><ul><li>set country flag [requested_raj_mandate_senapti_primacy](../flags/requested_raj_mandate_senapti_primacy.md)</li><li>overlord:</li><ul><li>If is not controlled by the AI, and  has 4411 is variable equal has which is rajSenaptiSetting, and is variable equal has value is 0:</li><ul><li>the event [[From.GetName] requests a Mandate of the Raj](../events/from_getname_requests_a_mandate_of_the_raj.md) happens</li></ul><li>else:</li><ul><li>the event [[From.GetName] requests a Mandate of the Raj](../events/from_getname_requests_a_mandate_of_the_raj_1.md) happens</li></ul></ul><li>clr country flag [raj_requested_mandate](../flags/raj_requested_mandate.md)</li><li>If is not controlled by the AI:</li><ul><li>the event [The Raj\n£raj_menu_window£\n\n\n\n[raja_global_target.GetFlag] \n[4411.GetRajCohesion]\n[raj_vizier_global_target.GetFlag]                                                               \n\n[raja_global_target.GetName] \n[raj_vizier_global_target.GetName]                                                               \n\n\n[4411.GetRajVizierBar]                                                               \n[Root.GetVizierRanking] ](../events/the_raj_npsraj_menu_windowps_n_n_n_n_raja_global_target_getflag_n_4411_getrajcohesion_n_raj_vizier_global_target_getflag_n_n_raja_global_target_getname_n_raj_vizier_global_target_getname) happens</li></ul></ul><li>custom tooltip = raj_mandate_reasons_accept_tt</li><li>custom tooltip = raj_mandate_reasons_senapti_tt</li></ul>

___
##£event_button_mandate_senapti_g£

###Available if:
<li>is not controlled by the AI</li><li>has reform senapti_reform</li><li>None of the following:</li><ul><li>check variable:</li><ul><li>which is rajMandateReasonsSenaptiDiff</li><li>value is at least 1</li></ul></ul><li>Any of the following:</li><ul><li>overlord:</li><ul><li>is controlled by the AI</li></ul><li>4411:</li><ul><li>None of the following:</li><ul><li>is variable equal:</li><ul><li>which is rajSenaptiSetting</li><li>value is at least 0</li></ul></ul></ul></ul>

###Efects:<ul><li>raj cohesion change:</li><ul><li>amount = 10</li><li>mandate = yes</li></ul><li>custom tooltip = request_raj_mandate_tt</li><li>tooltip:</li><ul><li>country gets the modifier raj_mandate_senapti_primacy for 15 years</li><li>custom tooltip = desc_raj_mandate_senapti_primacy</li></ul><li>hidden effect:</li><ul><li>the event [Missing localisation: rahenraj_3007_t](../events/missing_localisation_rahenraj_3007_t.md) happens</li></ul><li>custom tooltip = raj_mandate_reasons_refuse_tt</li><li>custom tooltip = raj_mandate_reasons_senapti_tt</li></ul>

___
##£event_button_mandate_prabhi£

###Available if:
<li>has reform prabhi_reform</li><li>Any of the following:</li><ul><li>check variable:</li><ul><li>which is rajMandateReasonsPrabhiDiff</li><li>value is at least 1</li></ul><li>All of the following:</li><ul><li>overlord:</li><ul><li>is not controlled by the AI</li></ul><li>4411:</li><ul><li>is variable equal:</li><ul><li>which is rajPrabhiSetting</li><li>value is at least 0</li></ul></ul></ul></ul>

###AI weighting:
AI weights this option at 20


###Efects:<ul><li>raj cohesion change:</li><ul><li>amount = 10</li><li>mandate = yes</li></ul><li>custom tooltip = request_raj_mandate_tt</li><li>tooltip:</li><ul><li>country gets the modifier raj_mandate_extended_prabhi_privileges for 15 years</li><li>custom tooltip = desc_raj_mandate_extended_prabhi_privileges</li></ul><li>hidden effect:</li><ul><li>set country flag [requested_raj_mandate_extended_prabhi_privileges](../flags/requested_raj_mandate_extended_prabhi_privileges.md)</li><li>overlord:</li><ul><li>If is not controlled by the AI, and  has 4411 is variable equal has which is rajPrabhiSetting, and is variable equal has value is 0:</li><ul><li>the event [[From.GetName] requests a Mandate of the Raj](../events/from_getname_requests_a_mandate_of_the_raj.md) happens</li></ul><li>else:</li><ul><li>the event [[From.GetName] requests a Mandate of the Raj](../events/from_getname_requests_a_mandate_of_the_raj_1.md) happens</li></ul></ul><li>clr country flag [raj_requested_mandate](../flags/raj_requested_mandate.md)</li><li>If is not controlled by the AI:</li><ul><li>the event [The Raj\n£raj_menu_window£\n\n\n\n[raja_global_target.GetFlag] \n[4411.GetRajCohesion]\n[raj_vizier_global_target.GetFlag]                                                               \n\n[raja_global_target.GetName] \n[raj_vizier_global_target.GetName]                                                               \n\n\n[4411.GetRajVizierBar]                                                               \n[Root.GetVizierRanking] ](../events/the_raj_npsraj_menu_windowps_n_n_n_n_raja_global_target_getflag_n_4411_getrajcohesion_n_raj_vizier_global_target_getflag_n_n_raja_global_target_getname_n_raj_vizier_global_target_getname) happens</li></ul></ul><li>custom tooltip = raj_mandate_reasons_accept_tt</li><li>custom tooltip = raj_mandate_reasons_prabhi_tt</li></ul>

___
##£event_button_mandate_prabhi_g£

###Available if:
<li>is not controlled by the AI</li><li>has reform prabhi_reform</li><li>None of the following:</li><ul><li>check variable:</li><ul><li>which is rajMandateReasonsPrabhiDiff</li><li>value is at least 1</li></ul></ul><li>Any of the following:</li><ul><li>overlord:</li><ul><li>is controlled by the AI</li></ul><li>4411:</li><ul><li>None of the following:</li><ul><li>is variable equal:</li><ul><li>which is rajPrabhiSetting</li><li>value is at least 0</li></ul></ul></ul></ul>

###Efects:<ul><li>raj cohesion change:</li><ul><li>amount = 10</li><li>mandate = yes</li></ul><li>custom tooltip = request_raj_mandate_tt</li><li>tooltip:</li><ul><li>country gets the modifier raj_mandate_extended_prabhi_privileges for 15 years</li><li>custom tooltip = desc_raj_mandate_extended_prabhi_privileges</li></ul><li>hidden effect:</li><ul><li>the event [Missing localisation: rahenraj_3007_t](../events/missing_localisation_rahenraj_3007_t.md) happens</li></ul><li>custom tooltip = raj_mandate_reasons_refuse_tt</li><li>custom tooltip = raj_mandate_reasons_prabhi_tt</li></ul>

___
##£event_button_mandate_back_rajmenu£

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>add dip power = 50</li><li>hidden effect:</li><ul><li>clr country flag [raj_requested_mandate](../flags/raj_requested_mandate.md)</li><li>If is not controlled by the AI:</li><ul><li>the event [The Raj\n£raj_menu_window£\n\n\n\n[raja_global_target.GetFlag] \n[4411.GetRajCohesion]\n[raj_vizier_global_target.GetFlag]                                                               \n\n[raja_global_target.GetName] \n[raj_vizier_global_target.GetName]                                                               \n\n\n[4411.GetRajVizierBar]                                                               \n[Root.GetVizierRanking] ](../events/the_raj_npsraj_menu_windowps_n_n_n_n_raja_global_target_getflag_n_4411_getrajcohesion_n_raj_vizier_global_target_getflag_n_n_raja_global_target_getname_n_raj_vizier_global_target_getname) happens</li></ul></ul></ul>
