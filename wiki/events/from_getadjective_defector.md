#Information
 - Title: [From.GetAdjective] Defector!
 - ID: new_court_flavour_events.12
#Description
[From.GetAdjective] Defector!
#Options

___
##His services will be remembered - and rewarded.

###AI weighting:
AI weights this option at 2
 - Multiplied by 0.25 if does not have army strength has who is from, and army strength has value is 0.75
 - Multiplied by 0.25 if has opinion has who is from, and has opinion has value is 50


###Efects:<ul><li>hidden effect:</li><ul><li>from:</li><ul><li>the event [Betrayal](../events/betrayal.md) happens</li></ul></ul><li>If has from has country flag is [advisor_events_adm](../flags/advisor_events_adm.md):</li><ul><li>add adm power = 100</li><li>custom tooltip = new_court_flavour_events_add_traitor_tooltip_adm</li></ul><li>Else if has from has country flag is [advisor_events_dip](../flags/advisor_events_dip.md):</li><ul><li>add dip power = 100</li><li>custom tooltip = new_court_flavour_events_add_traitor_tooltip_dip</li></ul><li>else:</li><ul><li>add mil power = 100</li><li>custom tooltip = new_court_flavour_events_add_traitor_tooltip_mil</li></ul><li>hidden effect:</li><ul><li>If does not have monthly income is 15:</li><ul><li>generate traitor advisor effect:</li><ul><li>skill level = 1</li></ul></ul><li>Else if does not have monthly income is 25:</li><ul><li>generate traitor advisor effect:</li><ul><li>skill level = 2</li></ul></ul><li>else:</li><ul><li>generate traitor advisor effect:</li><ul><li>skill level = 3</li></ul></ul></ul><li>from:</li><ul><li>add opinion:</li><ul><li>modifier = opinion_court_events_annoyed</li><li>who = root</li></ul></ul></ul>

___
##We have no need of traitors.

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>add prestige = 20</li><li>from:</li><ul><li>add opinion:</li><ul><li>modifier = opinion_court_events_grateful</li><li>who = root</li></ul></ul><li>hidden effect:</li><ul><li>from:</li><ul><li>the event [Caught in the Act](../events/caught_in_the_act.md) happens</li></ul></ul></ul>


#Pages with same name:
The following pages have the same name as this page:
 - [from_getadjective_defector_1](from_getadjective_defector_1.md)
