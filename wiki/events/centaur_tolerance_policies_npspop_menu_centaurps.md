#Information
 - Title: Centaur Tolerance & Policies\n£pop_menu_centaur£
 - ID: racial_pop_events_centaur.12
#Description
Centaur Tolerance & Policies\n£pop_menu_centaur£
#Options

___
##Missing localisation: racial_pop_events_all_races_12_y

###Available if:
<li>is controlled by the AI</li>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>country gets the modifier racial_pop_menu_cooldown for 10 years</li><li>clr country flag [racial_pop_menu_opened](../flags/racial_pop_menu_opened.md)</li></ul>

___
##£event_button_enact_policy_purge£

###Available if:
<li>can purge race:</li><ul><li>RACE is centaur</li></ul>

###AI weighting:
AI weights this option at 5
 - Multiplied by 1.25 if has wants to decrease tolerance centaur is yes
 - Multiplied by 1.5 if has low tolerance centaur race trigger is yes, and  has calc true if has all owned province has oppressed centaur pop trigger is yes; and calc true if has amount is 20
 - Multiplied by 1.25 if has stability is -3, and does not have stability is 0
 - Multiplied by 1.5 if has average unrest is 10
 - Multiplied by 2 if has ruler has personality is malevolent personality, and has ruler has personality is cruel personality
 - Multiplied by 2 if has ROOT is subject, and does not have liberty desire is 50; and  has overlord has country modifier is racial pop centaur purge
 - Multiplied by 1.25 if has corruption is 3
 - Multiplied by 1.5 if has country modifier is evil nation, and has country modifier is lich ruler
 - Multiplied by 1.25 if has any enemy country has country modifier is centaur administration; and has any rival country has country modifier is centaur administration
 - Multiplied by 3 if has country modifier is monstrous nation
 - Multiplied by 2 if does not have country modifier is centaur administration; and  has any known country has country modifier is centaur administration, and any known country has country modifier is monstrous nation; and does not have year is 1700
 - Multiplied by 0.1 if has num of rebel armies is 3, and has num of rebel controlled provinces is 5
 - Multiplied by 0.25 if is part of hre
 - Multiplied by 0.25 if does not have diplomatic reputation is 1
 - Multiplied by 0.25 if does not have liberty desire is 50
 - Multiplied by 0.8 if does not have a great power
 - Multiplied by 0.1 if has any known country has country modifier is centaur administration, and does not have country modifier is monstrous nation
 - Multiplied by 0.1 if has any ally has country modifier is centaur administration
 - Multiplied by 0.75 if does not have adm power is 150
 - Multiplied by 0 if has country modifier is centaur administration, and has country modifier is centaur military
 - Multiplied by 0.1 if has ruler has personality is tolerant personality, and has ruler has personality is kind hearted personality, and has ruler has personality is benevolent personality, and has ruler has personality is careful personality, and has ruler has personality is just personality
 - Multiplied by 0 if has idea group is humanist ideas
 - Multiplied by 0 if has personality is ai diplomat
 - Multiplied by 0.25 if has medium tolerance centaur race trigger is yes
 - Multiplied by 0 if has high tolerance centaur race trigger is yes
 - Multiplied by 0 if has ROOT is subject, and does not have liberty desire is 50; and  has overlord has country modifier is centaur administration
 - Multiplied by 0.5 if has check variable has which is centaur race tolerance ai, and check variable has value is 50
 - Multiplied by 0 if has check variable has which is centaur race tolerance ai, and check variable has value is 71


###Efects:<ul><li>hidden effect:</li><ul><li>If is not controlled by the AI:</li><ul><li>the event [Missing localisation: racial_pop_events_centaur_24_t](../events/missing_localisation_racial_pop_events_centaur_24_t.md) happens</li></ul><li>else:</li><ul><li>clr country flag [racial_pop_menu_opened](../flags/racial_pop_menu_opened.md)</li></ul><li>the event [The Purge of Centaurkind](../events/the_purge_of_centaurkind.md) happens</li></ul><li>custom tooltip = pop_menu_purge_desc_tt</li><li>add adm power = -100</li><li>largest decrease of centaur tolerance effect = yes</li><li>country gets the modifier racial_pop_centaur_purge until otherwise removed</li><li>custom tooltip = racial_pop_events_debug.3.tooltip</li><li>custom tooltip = pop_menu_purge_effect_unrest_tt</li><li>hidden effect:</li><ul><li>If every owned province has small centaur minority trigger is yes:</li><ul><li>add unrest = 5</li></ul><li>If every owned province has large centaur minority trigger is yes:</li><ul><li>add unrest = 7</li></ul><li>If every owned province has centaur majority trigger is yes:</li><ul><li>add unrest = 15</li></ul></ul></ul>

___
##£event_button_cant_enact_purge£

###Available if:
<li>None of the following:</li><ul><li>can purge race:</li><ul><li>RACE is centaur</li></ul><li>has country modifier racial_pop_centaur_purge</li></ul>

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>custom tooltip = pop_menu_purge_desc_tt</li><li>racial purge disabled tt:</li><ul><li>RACE = centaur</li></ul></ul>

___
##£event_button_cancel_policy_purge£

###Available if:
<li>has country modifier racial_pop_centaur_purge</li><li>adm power is at least 100</li>

###AI weighting:
AI weights this option at 20
 - Multiplied by 0 if has country modifier is racial pop menu cooldown
 - Multiplied by 1.5 if does not have diplomatic reputation is -3
 - Multiplied by 10 if has country modifier is centaur administration, and has country modifier is centaur military
 - Multiplied by 2 if has wants to increase tolerance centaur is yes
 - Multiplied by 10 if has medium tolerance centaur race trigger is yes
 - Multiplied by 20 if has high tolerance centaur race trigger is yes
 - Multiplied by 2 if does not have liberty desire is 50
 - Multiplied by 5 if has any ally has country modifier is centaur administration
 - Multiplied by 2 if has ruler has personality is tolerant personality, and has ruler has personality is kind hearted personality, and has ruler has personality is benevolent personality, and has ruler has personality is careful personality, and has ruler has personality is just personality
 - Multiplied by 10 if has idea group is humanist ideas
 - Multiplied by 5 if is bankrupt
 - Multiplied by 10 if has ROOT is subject, and does not have liberty desire is 50; and  does not have country modifier is racial pop centaur expulsion


###Efects:<ul><li>custom tooltip = pop_menu_purge_desc_tt</li><li>remove country modifier = racial_pop_centaur_purge</li><li>add adm power = -100</li><li>hidden effect:</li><ul><li>If is not controlled by the AI:</li><ul><li>set country flag [just_stopped_purging](../flags/just_stopped_purging.md)</li><li>the event [Missing localisation: racial_pop_events_centaur_24_t](../events/missing_localisation_racial_pop_events_centaur_24_t.md) happens</li></ul><li>else:</li><ul><li>clr country flag [racial_pop_menu_opened](../flags/racial_pop_menu_opened.md)</li></ul><li>the event [End of the Centaur Purge](../events/end_of_the_centaur_purge.md) happens</li></ul></ul>

___
##£event_button_cant_cancel_purge£

###Available if:
<li>has country modifier racial_pop_centaur_purge</li><li>None of the following:</li><ul><li>adm power is at least 100</li></ul>

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>custom tooltip = pop_menu_purge_desc_tt</li><li>custom tooltip = pop_menu_cannot_stop_purge_not_enough_adm_tt</li><li>hidden effect:</li><ul><li>the event [Missing localisation: racial_pop_events_centaur_24_t](../events/missing_localisation_racial_pop_events_centaur_24_t.md) happens</li></ul></ul>

___
##£event_button_enact_policy_expel£

###Available if:
<li>can expel race:</li><ul><li>RACE is centaur</li></ul>

###AI weighting:
AI weights this option at 10
 - Multiplied by 1.25 if has wants to decrease tolerance centaur is yes
 - Multiplied by 1.25 if has wants to decrease tolerance centaur is yes
 - Multiplied by 1.5 if has low tolerance centaur race trigger is yes, and  has calc true if has all owned province has oppressed centaur pop trigger is yes; and calc true if has amount is 20
 - Multiplied by 1.25 if has stability is -3, and does not have stability is 0
 - Multiplied by 1.5 if has average unrest is 10
 - Multiplied by 2 if has ruler has personality is malevolent personality, and has ruler has personality is cruel personality
 - Multiplied by 2 if has ROOT is subject, and does not have liberty desire is 50; and  has overlord has country modifier is racial pop centaur purge
 - Multiplied by 1.25 if has country modifier is evil nation, and has country modifier is lich ruler
 - Multiplied by 1.25 if has any enemy country has country modifier is centaur administration; and has any rival country has country modifier is centaur administration
 - Multiplied by 2 if has country modifier is monstrous nation
 - Multiplied by 1.5 if does not have country modifier is centaur administration; and  has any known country has country modifier is centaur administration, and any known country has country modifier is monstrous nation; and does not have year is 1700
 - Multiplied by 0.1 if has num of rebel armies is 3, and has num of rebel controlled provinces is 5
 - Multiplied by 0.25 if is part of hre
 - Multiplied by 0.25 if does not have liberty desire is 50
 - Multiplied by 0.75 if has any known country has country modifier is centaur administration, and does not have country modifier is monstrous nation
 - Multiplied by 0.1 if has any ally has country modifier is centaur administration
 - Multiplied by 0.75 if does not have adm power is 100
 - Multiplied by 0 if has country modifier is centaur administration, and has country modifier is centaur military
 - Multiplied by 0.1 if has ruler has personality is tolerant personality, and has ruler has personality is kind hearted personality, and has ruler has personality is benevolent personality, and has ruler has personality is careful personality, and has ruler has personality is just personality
 - Multiplied by 0.25 if has medium tolerance centaur race trigger is yes
 - Multiplied by 0 if has high tolerance centaur race trigger is yes
 - Multiplied by 0 if has ROOT is subject, and does not have liberty desire is 50; and  has overlord has country modifier is centaur administration
 - Multiplied by 0.5 if has check variable has which is centaur race tolerance ai, and check variable has value is 50
 - Multiplied by 0 if has check variable has which is centaur race tolerance ai, and check variable has value is 71
 - Multiplied by 0 if has idea group is humanist ideas, and has personality is ai diplomat


###Efects:<ul><li>hidden effect:</li><ul><li>If is not controlled by the AI:</li><ul><li>the event [Missing localisation: racial_pop_events_centaur_24_t](../events/missing_localisation_racial_pop_events_centaur_24_t.md) happens</li></ul><li>else:</li><ul><li>clr country flag [racial_pop_menu_opened](../flags/racial_pop_menu_opened.md)</li></ul><li>the event [The Expulsion of Centaurkind](../events/the_expulsion_of_centaurkind.md) happens</li></ul><li>custom tooltip = pop_menu_expel_desc_tt</li><li>add adm power = -50</li><li>large decrease of centaur tolerance effect = yes</li><li>country gets the modifier racial_pop_centaur_expulsion until otherwise removed</li><li>custom tooltip = racial_pop_events_debug.2.tooltip</li><li>custom tooltip = pop_menu_expel_effect_unrest_tt</li><li>hidden effect:</li><ul><li>If every owned province has small centaur minority trigger is yes:</li><ul><li>add unrest = 2</li></ul><li>If every owned province has large centaur minority trigger is yes:</li><ul><li>add unrest = 5</li></ul><li>If every owned province has centaur majority trigger is yes:</li><ul><li>add unrest = 10</li></ul></ul></ul>

___
##£event_button_cant_enact_expel£

###Available if:
<li>None of the following:</li><ul><li>can expel race:</li><ul><li>RACE is centaur</li></ul><li>has country modifier racial_pop_centaur_expulsion</li></ul>

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>custom tooltip = pop_menu_expel_desc_tt</li><li>racial expel disabled tt:</li><ul><li>RACE = centaur</li></ul></ul>

___
##£event_button_cancel_policy_expel£

###Available if:
<li>has country modifier racial_pop_centaur_expulsion</li><li>adm power is at least 50</li>

###AI weighting:
AI weights this option at 20
 - Multiplied by 0 if has country modifier is racial pop menu cooldown
 - Multiplied by 1.5 if does not have diplomatic reputation is -3
 - Multiplied by 10 if has country modifier is centaur administration, and has country modifier is centaur military
 - Multiplied by 2 if has wants to increase tolerance centaur is yes
 - Multiplied by 10 if has medium tolerance centaur race trigger is yes
 - Multiplied by 20 if has high tolerance centaur race trigger is yes
 - Multiplied by 2 if does not have liberty desire is 50
 - Multiplied by 5 if has any ally has country modifier is centaur administration
 - Multiplied by 2 if has ruler has personality is tolerant personality, and has ruler has personality is kind hearted personality, and has ruler has personality is benevolent personality, and has ruler has personality is careful personality, and has ruler has personality is just personality
 - Multiplied by 10 if has idea group is humanist ideas
 - Multiplied by 5 if is bankrupt
 - Multiplied by 10 if has ROOT is subject, and does not have liberty desire is 50; and  does not have country modifier is racial pop centaur expulsion


###Efects:<ul><li>custom tooltip = pop_menu_expel_desc_tt</li><li>remove country modifier = racial_pop_centaur_expulsion</li><li>add adm power = -50</li><li>hidden effect:</li><ul><li>If is not controlled by the AI:</li><ul><li>the event [Missing localisation: racial_pop_events_centaur_24_t](../events/missing_localisation_racial_pop_events_centaur_24_t.md) happens</li></ul><li>else:</li><ul><li>clr country flag [racial_pop_menu_opened](../flags/racial_pop_menu_opened.md)</li></ul><li>the event [Revocation of Expulsion of Centaurkind](../events/revocation_of_expulsion_of_centaurkind.md) happens</li></ul></ul>

___
##£event_button_cant_cancel_expel£

###Available if:
<li>has country modifier racial_pop_centaur_expulsion</li><li>None of the following:</li><ul><li>adm power is at least 50</li></ul>

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>custom tooltip = pop_menu_expel_desc_tt</li><li>custom tooltip = pop_menu_cannot_stop_expel_not_enough_adm_tt</li><li>hidden effect:</li><ul><li>the event [Missing localisation: racial_pop_events_centaur_24_t](../events/missing_localisation_racial_pop_events_centaur_24_t.md) happens</li></ul></ul>

___
##£event_button_enact_policy_focus£

###Available if:
<li>None of the following:</li><ul><li>has racial focus yes</li></ul><li>dip power is at least 50</li>

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>custom tooltip = pop_menu_focus_desc_tt</li><li>add dip power = -50</li><li>country gets the modifier racial_focus_centaur until otherwise removed</li><li>hidden effect:</li><ul><li>the event [Missing localisation: racial_pop_events_centaur_24_t](../events/missing_localisation_racial_pop_events_centaur_24_t.md) happens</li></ul></ul>

___
##£event_button_cant_enact_focus£

###Available if:
<li>None of the following:</li><ul><li>has country modifier racial_focus_centaur</li></ul><li>Any of the following:</li><ul><li>None of the following:</li><ul><li>dip power is at least 50</li></ul><li>has racial focus yes</li></ul>

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>custom tooltip = pop_menu_focus_desc_tt</li><li>If has racial focus is yes:</li><ul><li>custom tooltip = pop_menu_focus_already_active_tt</li></ul><li>If does not have dip power is 50:</li><ul><li>custom tooltip = pop_menu_cannot_focus_not_enough_dip_tt</li></ul><li>hidden effect:</li><ul><li>the event [Missing localisation: racial_pop_events_centaur_24_t](../events/missing_localisation_racial_pop_events_centaur_24_t.md) happens</li></ul></ul>

___
##£event_button_cancel_policy_focus£

###Available if:
<li>has country modifier racial_focus_centaur</li>

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>custom tooltip = pop_menu_focus_desc_tt</li><li>remove country modifier = racial_focus_centaur</li><li>hidden effect:</li><ul><li>the event [Missing localisation: racial_pop_events_centaur_24_t](../events/missing_localisation_racial_pop_events_centaur_24_t.md) happens</li></ul></ul>

___
##£event_button_back_to_menu£

###Available if:
<li>is not controlled by the AI</li>

###Efects:<ul><li>hidden effect:</li><ul><li>the event [Racial Tolerances & Policies\n£pop_menu_window£](../events/racial_tolerances_policies_npspop_menu_windowps.md) happens</li></ul></ul>
