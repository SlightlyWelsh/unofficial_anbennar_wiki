#Information
 - Title: Draining the Heart
 - ID: spirits.606
#Description
Draining the Heart
#Options

___
##Cast a Sinister Ritual

###Efects:<ul><li>the event ˻spirits.608˼ happens</li><li>hidden effect:</li><ul><li>set country flag [in_deeper_heart_drain_menu](../flags/in_deeper_heart_drain_menu.md)</li></ul></ul>

___
##Consume the Chi for yourself

###Available if:
<li>does not have regency</li><li>does not have consort regency</li>

###Efects:<ul><li>the event ˻spirits.609˼ happens</li><li>hidden effect:</li><ul><li>set country flag [in_deeper_heart_drain_menu](../flags/in_deeper_heart_drain_menu.md)</li></ul></ul>

___
##Empower a General

###Available if:
<li>None of the following:</li><ul><li>has country modifier spirits_war_wizard_cooldown</li></ul>

###Efects:<ul><li>create war wizard effect = yes</li><li>lhp heart drain choose option = yes</li><li>custom tooltip = spirits_war_wizard_cooldown_tooltip</li><li>hidden effect:</li><ul><li>country gets the modifier spirits_war_wizard_cooldown for 50 years</li></ul></ul>

___
##Empower a prominent Court Sorceror

###Efects:<ul><li>define advisor:</li><ul><li>type = court_mage</li><li>skill = 4</li><li>cost multiplier = 0.25</li></ul><li>If does not have tag is Y01:</li><ul><li>add estate loyalty modifier:</li><ul><li>estate = estate_mages</li><li>desc = EST_VAL_LEFTHAND_EMPOWERED_COURT_SORCEROR_LOY</li><li>loyalty = 5</li><li>duration = 7300</li></ul></ul><li>Else if has tag is Y01:</li><ul><li>random list:</li><ul><li>20:</li><ul><li>trigger:</li><ul><li>has estate = estate_shinukhorchi</li></ul><li>add estate loyalty modifier:</li><ul><li>estate = estate_shinukhorchi</li><li>desc = EST_VAL_LEFTHAND_EMPOWERED_COURT_SORCEROR_LOY</li><li>loyalty = 5</li><li>duration = 7300</li></ul></ul><li>20:</li><ul><li>trigger:</li><ul><li>has estate = estate_chumijemoya</li></ul><li>add estate loyalty modifier:</li><ul><li>estate = estate_chumijemoya</li><li>desc = EST_VAL_LEFTHAND_EMPOWERED_COURT_SORCEROR_LOY</li><li>loyalty = 5</li><li>duration = 7300</li></ul></ul><li>20:</li><ul><li>trigger:</li><ul><li>has estate = estate_ajgriijarul</li></ul><li>add estate loyalty modifier:</li><ul><li>estate = estate_ajgriijarul</li><li>desc = EST_VAL_LEFTHAND_EMPOWERED_COURT_SORCEROR_LOY</li><li>loyalty = 5</li><li>duration = 7300</li></ul></ul><li>20:</li><ul><li>trigger:</li><ul><li>has estate = estate_kabiurgarko</li></ul><li>add estate loyalty modifier:</li><ul><li>estate = estate_kabiurgarko</li><li>desc = EST_VAL_LEFTHAND_EMPOWERED_COURT_SORCEROR_LOY</li><li>loyalty = 5</li><li>duration = 7300</li></ul></ul><li>20:</li><ul><li>trigger:</li><ul><li>has estate = estate_khelorvalshi</li></ul><li>add estate loyalty modifier:</li><ul><li>estate = estate_khelorvalshi</li><li>desc = EST_VAL_LEFTHAND_EMPOWERED_COURT_SORCEROR_LOY</li><li>loyalty = 5</li><li>duration = 7300</li></ul></ul></ul></ul><li>lhp heart drain choose option = yes</li></ul>

___
##Let the §YSorcerers§! drink to their heart's content!

###Available if:
<li>None of the following:</li><ul><li>Country is Y01</li></ul>

###Efects:<ul><li>add estate loyalty modifier:</li><ul><li>estate = estate_mages</li><li>desc = EST_VAL_LEFTHAND_EMPOWERED_SORCERERS_LOY</li><li>loyalty = 15</li><li>duration = 7300</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_mages</li><li>desc = EST_VAL_LEFTHAND_EMPOWERED_SORCERERS</li><li>influence = 33</li><li>duration = 730</li></ul><li>country gets the modifier lefthand_empowered_sorcerers for 5 years</li><li>lhp heart drain choose option = yes</li></ul>

___
##Let the §YShirgrii§! drink to their heart's content!

###Available if:
<li>Country is Y01</li>

###Efects:<ul><li>the event ˻spirits.610˼ happens</li><li>hidden effect:</li><ul><li>set country flag [in_deeper_heart_drain_menu](../flags/in_deeper_heart_drain_menu.md)</li></ul></ul>


#Pages with same name:
The following pages have the same name as this page:
 - [draining_the_heart_1](draining_the_heart_1.md)
