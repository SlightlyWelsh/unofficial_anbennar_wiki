#Information
 - Title: Imprisoned Countryman in [From.GetUsableName]
 - ID: new_court_flavour_events.15
#Description
Imprisoned Countryman in [From.GetUsableName]
#Options

___
##We cannot abandon them.

###Efects:<ul><li>add prestige = 20</li><li>from:</li><ul><li>add opinion:</li><ul><li>modifier = opinion_court_events_interfered</li><li>who = root</li></ul><li>hidden effect:</li><ul><li>the event [[From.GetAdjective] Demands](../events/from_getadjective_demands.md) happens</li></ul></ul></ul>

___
##We will not interfere.

###AI weighting:
AI weights this option at 1
 - Multiplied by 0.5 if does not have opinion has who is from, and has opinion has value is -50
 - Multiplied by 0.5 if does not have opinion has who is from, and has opinion has value is -25
 - Multiplied by 1.5 if has opinion has who is from, and has opinion has value is 20
 - Multiplied by 1.5 if has opinion has who is from, and has opinion has value is 35
 - Multiplied by 1.5 if has opinion has who is from, and has opinion has value is 50
 - Multiplied by 2 if does not have army strength has who is from, and army strength has value is 0.75
 - Multiplied by 2 if does not have army strength has who is from, and army strength has value is 0.5


###Efects:<ul><li>add prestige = -20</li><li>hidden effect:</li><ul><li>clear saved name = advisor_traitor</li><li>from:</li><ul><li>trigger switch:</li><ul><li>on trigger = has_country_flag</li><li>advisor events adm:</li><ul><li>clr country flag [advisor_events_adm](../flags/advisor_events_adm.md)</li></ul><li>advisor events dip:</li><ul><li>clr country flag [advisor_events_dip](../flags/advisor_events_dip.md)</li></ul><li>advisor events mil:</li><ul><li>clr country flag [advisor_events_mil](../flags/advisor_events_mil.md)</li></ul></ul><li>trigger switch:</li><ul><li>on trigger = has_country_flag</li><li>advisor events adm:</li><ul><li>clr country flag [new_court_flavour_events_2adm](../flags/new_court_flavour_events_2adm.md)</li></ul><li>advisor events dip:</li><ul><li>clr country flag [new_court_flavour_events_2dip](../flags/new_court_flavour_events_2dip.md)</li></ul><li>advisor events mil:</li><ul><li>clr country flag [new_court_flavour_events_2mil](../flags/new_court_flavour_events_2mil.md)</li></ul></ul></ul></ul></ul>
