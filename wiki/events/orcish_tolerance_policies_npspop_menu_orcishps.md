#Information
 - Title: Orcish Tolerance & Policies\n£pop_menu_orcish£
 - ID: racial_pop_events_orcish.12
#Description
Orcish Tolerance & Policies\n£pop_menu_orcish£
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
<li>can purge race:</li><ul><li>RACE is orcish</li></ul>

###AI weighting:
AI weights this option at 5
 - Multiplied by 1.25 if has wants to decrease tolerance orcish is yes
 - Multiplied by 1.5 if has low tolerance orcish race trigger is yes, and  has calc true if has all owned province has oppressed orcish pop trigger is yes; and calc true if has amount is 20
 - Multiplied by 1.25 if has stability is -3, and does not have stability is 0
 - Multiplied by 1.5 if has average unrest is 10
 - Multiplied by 2 if has ruler has personality is malevolent personality, and has ruler has personality is cruel personality
 - Multiplied by 2 if has ROOT is subject, and does not have liberty desire is 50; and  has overlord has country modifier is racial pop orcish purge
 - Multiplied by 1.25 if has corruption is 3
 - Multiplied by 1.5 if has country modifier is evil nation, and has country modifier is lich ruler
 - Multiplied by 1.25 if has any enemy country has country modifier is orcish administration; and has any rival country has country modifier is orcish administration
 - Multiplied by 3 if has country modifier is monstrous nation
 - Multiplied by 2 if does not have country modifier is orcish administration; and  has any known country has country modifier is orcish administration, and any known country has country modifier is monstrous nation; and does not have year is 1700
 - Multiplied by 0.1 if has num of rebel armies is 3, and has num of rebel controlled provinces is 5
 - Multiplied by 0.25 if is part of hre
 - Multiplied by 0.25 if does not have diplomatic reputation is 1
 - Multiplied by 0.25 if does not have liberty desire is 50
 - Multiplied by 0.8 if does not have a great power
 - Multiplied by 0.1 if has any known country has country modifier is orcish administration, and does not have country modifier is monstrous nation
 - Multiplied by 0.1 if has any ally has country modifier is orcish administration
 - Multiplied by 0.75 if does not have adm power is 150
 - Multiplied by 0 if has country modifier is orcish administration, and has country modifier is orcish military
 - Multiplied by 0.1 if has ruler has personality is tolerant personality, and has ruler has personality is kind hearted personality, and has ruler has personality is benevolent personality, and has ruler has personality is careful personality, and has ruler has personality is just personality
 - Multiplied by 0 if has idea group is humanist ideas
 - Multiplied by 0 if has personality is ai diplomat
 - Multiplied by 0.25 if has medium tolerance orcish race trigger is yes
 - Multiplied by 0 if has high tolerance orcish race trigger is yes
 - Multiplied by 0 if has ROOT is subject, and does not have liberty desire is 50; and  has overlord has country modifier is orcish administration
 - Multiplied by 0.5 if has check variable has which is orcish race tolerance ai, and check variable has value is 50
 - Multiplied by 0 if has check variable has which is orcish race tolerance ai, and check variable has value is 71
 - Multiplied by 3 if has reform is adventurer reform, and  has current age is age of discovery
 - Multiplied by 0.1 if has country modifier is orcish slaves in colonies
 - Multiplied by 10 if has country modifier is dwarven administration


###Efects:<ul><li>hidden effect:</li><ul><li>If is not controlled by the AI:</li><ul><li>the event ˻racial_pop_events_orcish.24˼ happens</li></ul><li>else:</li><ul><li>clr country flag [racial_pop_menu_opened](../flags/racial_pop_menu_opened.md)</li></ul><li>the event ˻racial_pop_events_orcish.14˼ happens</li></ul><li>custom tooltip = pop_menu_purge_desc_tt</li><li>add adm power = -100</li><li>largest decrease of orcish tolerance effect = yes</li><li>country gets the modifier racial_pop_orcish_purge until otherwise removed</li><li>custom tooltip = racial_pop_events_debug.3.tooltip</li><li>custom tooltip = pop_menu_purge_effect_unrest_tt</li><li>hidden effect:</li><ul><li>If every owned province has small orcish minority trigger is yes:</li><ul><li>add unrest = 5</li></ul><li>If every owned province has large orcish minority trigger is yes:</li><ul><li>add unrest = 7</li></ul><li>If every owned province has orcish majority trigger is yes:</li><ul><li>add unrest = 15</li></ul></ul></ul>

___
##£event_button_cant_enact_purge£

###Available if:
<li>None of the following:</li><ul><li>can purge race:</li><ul><li>RACE is orcish</li></ul><li>has country modifier racial_pop_orcish_purge</li></ul>

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>custom tooltip = pop_menu_purge_desc_tt</li><li>racial purge disabled tt:</li><ul><li>RACE = orcish</li></ul></ul>

___
##£event_button_cancel_policy_purge£

###Available if:
<li>has country modifier racial_pop_orcish_purge</li><li>adm power is at least 100</li>

###AI weighting:
AI weights this option at 20
 - Multiplied by 0 if has country modifier is racial pop menu cooldown
 - Multiplied by 1.5 if does not have diplomatic reputation is -3
 - Multiplied by 10 if has country modifier is orcish administration, and has country modifier is orcish military
 - Multiplied by 2 if has wants to increase tolerance orcish is yes
 - Multiplied by 10 if has medium tolerance orcish race trigger is yes
 - Multiplied by 20 if has high tolerance orcish race trigger is yes
 - Multiplied by 2 if does not have liberty desire is 50
 - Multiplied by 5 if has any ally has country modifier is orcish administration
 - Multiplied by 2 if has ruler has personality is tolerant personality, and has ruler has personality is kind hearted personality, and has ruler has personality is benevolent personality, and has ruler has personality is careful personality, and has ruler has personality is just personality
 - Multiplied by 10 if has idea group is humanist ideas
 - Multiplied by 5 if is bankrupt
 - Multiplied by 10 if has ROOT is subject, and does not have liberty desire is 50; and  does not have country modifier is racial pop orcish expulsion
 - Multiplied by 0 if has reform is adventurer reform, and  has current age is age of discovery


###Efects:<ul><li>custom tooltip = pop_menu_purge_desc_tt</li><li>remove country modifier = racial_pop_orcish_purge</li><li>add adm power = -100</li><li>hidden effect:</li><ul><li>If is not controlled by the AI:</li><ul><li>set country flag [just_stopped_purging](../flags/just_stopped_purging.md)</li><li>the event ˻racial_pop_events_orcish.24˼ happens</li></ul><li>else:</li><ul><li>clr country flag [racial_pop_menu_opened](../flags/racial_pop_menu_opened.md)</li></ul><li>the event ˻racial_pop_events_orcish.16˼ happens</li></ul></ul>

___
##£event_button_cant_cancel_purge£

###Available if:
<li>has country modifier racial_pop_orcish_purge</li><li>None of the following:</li><ul><li>adm power is at least 100</li></ul>

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>custom tooltip = pop_menu_purge_desc_tt</li><li>custom tooltip = pop_menu_cannot_stop_purge_not_enough_adm_tt</li><li>hidden effect:</li><ul><li>the event ˻racial_pop_events_orcish.24˼ happens</li></ul></ul>

___
##£event_button_enact_policy_expel£

###Available if:
<li>can expel race:</li><ul><li>RACE is orcish</li></ul>

###AI weighting:
AI weights this option at 10
 - Multiplied by 1.25 if has wants to decrease tolerance orcish is yes
 - Multiplied by 1.25 if has wants to decrease tolerance orcish is yes
 - Multiplied by 1.5 if has low tolerance orcish race trigger is yes, and  has calc true if has all owned province has oppressed orcish pop trigger is yes; and calc true if has amount is 20
 - Multiplied by 1.25 if has stability is -3, and does not have stability is 0
 - Multiplied by 1.5 if has average unrest is 10
 - Multiplied by 2 if has ruler has personality is malevolent personality, and has ruler has personality is cruel personality
 - Multiplied by 2 if has ROOT is subject, and does not have liberty desire is 50; and  has overlord has country modifier is racial pop orcish purge
 - Multiplied by 1.25 if has country modifier is evil nation, and has country modifier is lich ruler
 - Multiplied by 1.25 if has any enemy country has country modifier is orcish administration; and has any rival country has country modifier is orcish administration
 - Multiplied by 2 if has country modifier is monstrous nation
 - Multiplied by 1.5 if does not have country modifier is orcish administration; and  has any known country has country modifier is orcish administration, and any known country has country modifier is monstrous nation; and does not have year is 1700
 - Multiplied by 0.1 if has num of rebel armies is 3, and has num of rebel controlled provinces is 5
 - Multiplied by 0.25 if is part of hre
 - Multiplied by 0.25 if does not have liberty desire is 50
 - Multiplied by 0.75 if has any known country has country modifier is orcish administration, and does not have country modifier is monstrous nation
 - Multiplied by 0.1 if has any ally has country modifier is orcish administration
 - Multiplied by 0.75 if does not have adm power is 100
 - Multiplied by 0 if has country modifier is orcish administration, and has country modifier is orcish military
 - Multiplied by 0.1 if has ruler has personality is tolerant personality, and has ruler has personality is kind hearted personality, and has ruler has personality is benevolent personality, and has ruler has personality is careful personality, and has ruler has personality is just personality
 - Multiplied by 0.25 if has medium tolerance orcish race trigger is yes
 - Multiplied by 0 if has high tolerance orcish race trigger is yes
 - Multiplied by 0 if has ROOT is subject, and does not have liberty desire is 50; and  has overlord has country modifier is orcish administration
 - Multiplied by 0.5 if has check variable has which is orcish race tolerance ai, and check variable has value is 50
 - Multiplied by 0 if has check variable has which is orcish race tolerance ai, and check variable has value is 71
 - Multiplied by 0.1 if has country modifier is orcish slaves in colonies
 - Multiplied by 0 if has tag is A73
 - Multiplied by 0 if has idea group is humanist ideas, and has personality is ai diplomat; and does not have country modifier is dwarven administration
 - Multiplied by 10 if has country modifier is dwarven administration


###Efects:<ul><li>hidden effect:</li><ul><li>If is not controlled by the AI:</li><ul><li>the event ˻racial_pop_events_orcish.24˼ happens</li></ul><li>else:</li><ul><li>clr country flag [racial_pop_menu_opened](../flags/racial_pop_menu_opened.md)</li></ul><li>the event ˻racial_pop_events_orcish.13˼ happens</li></ul><li>custom tooltip = pop_menu_expel_desc_tt</li><li>add adm power = -50</li><li>large decrease of orcish tolerance effect = yes</li><li>country gets the modifier racial_pop_orcish_expulsion until otherwise removed</li><li>custom tooltip = racial_pop_events_debug.2.tooltip</li><li>custom tooltip = pop_menu_expel_effect_unrest_tt</li><li>hidden effect:</li><ul><li>If every owned province has small orcish minority trigger is yes:</li><ul><li>add unrest = 2</li></ul><li>If every owned province has large orcish minority trigger is yes:</li><ul><li>add unrest = 5</li></ul><li>If every owned province has orcish majority trigger is yes:</li><ul><li>add unrest = 10</li></ul></ul></ul>

___
##£event_button_cant_enact_expel£

###Available if:
<li>None of the following:</li><ul><li>can expel race:</li><ul><li>RACE is orcish</li></ul><li>has country modifier racial_pop_orcish_expulsion</li></ul>

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>custom tooltip = pop_menu_expel_desc_tt</li><li>racial expel disabled tt:</li><ul><li>RACE = orcish</li></ul></ul>

___
##£event_button_cancel_policy_expel£

###Available if:
<li>has country modifier racial_pop_orcish_expulsion</li><li>adm power is at least 50</li>

###AI weighting:
AI weights this option at 20
 - Multiplied by 0 if has country modifier is racial pop menu cooldown
 - Multiplied by 1.5 if does not have diplomatic reputation is -3
 - Multiplied by 10 if has country modifier is orcish administration, and has country modifier is orcish military
 - Multiplied by 2 if has wants to increase tolerance orcish is yes
 - Multiplied by 10 if has medium tolerance orcish race trigger is yes
 - Multiplied by 20 if has high tolerance orcish race trigger is yes
 - Multiplied by 2 if does not have liberty desire is 50
 - Multiplied by 5 if has any ally has country modifier is orcish administration
 - Multiplied by 2 if has ruler has personality is tolerant personality, and has ruler has personality is kind hearted personality, and has ruler has personality is benevolent personality, and has ruler has personality is careful personality, and has ruler has personality is just personality
 - Multiplied by 10 if has idea group is humanist ideas
 - Multiplied by 5 if is bankrupt
 - Multiplied by 10 if has ROOT is subject, and does not have liberty desire is 50; and  does not have country modifier is racial pop orcish expulsion
 - Multiplied by 0 if has reform is adventurer reform, and  has current age is age of discovery


###Efects:<ul><li>custom tooltip = pop_menu_expel_desc_tt</li><li>remove country modifier = racial_pop_orcish_expulsion</li><li>add adm power = -50</li><li>hidden effect:</li><ul><li>If is not controlled by the AI:</li><ul><li>the event ˻racial_pop_events_orcish.24˼ happens</li></ul><li>else:</li><ul><li>clr country flag [racial_pop_menu_opened](../flags/racial_pop_menu_opened.md)</li></ul><li>the event ˻racial_pop_events_orcish.15˼ happens</li></ul></ul>

___
##£event_button_cant_cancel_expel£

###Available if:
<li>has country modifier racial_pop_orcish_expulsion</li><li>None of the following:</li><ul><li>adm power is at least 50</li></ul>

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>custom tooltip = pop_menu_expel_desc_tt</li><li>custom tooltip = pop_menu_cannot_stop_expel_not_enough_adm_tt</li><li>hidden effect:</li><ul><li>the event ˻racial_pop_events_orcish.24˼ happens</li></ul></ul>

___
##£event_button_enact_policy_focus£

###Available if:
<li>None of the following:</li><ul><li>has racial focus yes</li></ul><li>dip power is at least 50</li>

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>custom tooltip = pop_menu_focus_desc_tt</li><li>add dip power = -50</li><li>country gets the modifier racial_focus_orcish until otherwise removed</li><li>hidden effect:</li><ul><li>the event ˻racial_pop_events_orcish.24˼ happens</li></ul></ul>

___
##£event_button_cant_enact_focus£

###Available if:
<li>None of the following:</li><ul><li>has country modifier racial_focus_orcish</li></ul><li>Any of the following:</li><ul><li>None of the following:</li><ul><li>dip power is at least 50</li></ul><li>has racial focus yes</li></ul>

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>custom tooltip = pop_menu_focus_desc_tt</li><li>custom tooltip = pop_menu_unavailable_tt</li><li>If has racial focus is yes:</li><ul><li>custom tooltip = pop_menu_focus_already_active_tt</li></ul><li>If does not have dip power is 50:</li><ul><li>custom tooltip = pop_menu_cannot_focus_not_enough_dip_tt</li></ul><li>hidden effect:</li><ul><li>the event ˻racial_pop_events_orcish.24˼ happens</li></ul></ul>

___
##£event_button_cancel_policy_focus£

###Available if:
<li>has country modifier racial_focus_orcish</li>

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>custom tooltip = pop_menu_focus_desc_tt</li><li>remove country modifier = racial_focus_orcish</li><li>hidden effect:</li><ul><li>the event ˻racial_pop_events_orcish.24˼ happens</li></ul></ul>

___
##£event_button_back_to_menu£

###Available if:
<li>is not controlled by the AI</li>

###Efects:<ul><li>hidden effect:</li><ul><li>the event ˻racial_pop_misc.3˼ happens</li></ul></ul>
