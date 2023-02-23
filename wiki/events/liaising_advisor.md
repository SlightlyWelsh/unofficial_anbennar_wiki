#Information
 - Title: Liaising Advisor
 - ID: new_court_flavour_events.1
#Description
Liaising Advisor
#Mean Time to Happen:
Base time = 75 years

#Options

___
##Let's do it.

###AI weighting:
AI weights this option at 1
 - Multiplied by 1.5 if has event target:advisor liaisons target country is not controlled by the AI
 - Multiplied by 0.5 if does not have opinion has who is event target:advisor liaisons target country, and has opinion has value is -100
 - Multiplied by 0.5 if does not have opinion has who is event target:advisor liaisons target country, and has opinion has value is -50
 - Multiplied by 1.5 if has opinion has who is event target:advisor liaisons target country, and has opinion has value is 25
 - Multiplied by 2 if has opinion has who is event target:advisor liaisons target country, and has opinion has value is 50
 - Multiplied by 2 if does not have army strength has who is event target:advisor liaisons target country, and army strength has value is 0.75
 - Multiplied by 2 if does not have army strength has who is event target:advisor liaisons target country, and army strength has value is 0.5
 - Multiplied by 0.75 if has army strength has who is event target:advisor liaisons target country, and army strength has value is 1.5


###Efects:<ul><li>custom tooltip = new_court_flavour_events.1.A.tooltip</li><li>hidden effect:</li><ul><li>event target:advisor liaisons target country:</li><ul><li>country gets the modifier recent_liaising_advisor_timer for 50 years</li></ul><li>If does not have event target:advisor liaisons target country has opinion has who is root, and has opinion has value is 25; and has AND has country flag is [advisor_events_adm](../flags/advisor_events_adm.md), and has employed advisor has category is DIP; and has employed advisor has category is MIL; and has AND has country flag is [advisor_events_dip](../flags/advisor_events_dip.md), and has employed advisor has category is ADM; and has employed advisor has category is MIL; and has AND has country flag is [advisor_events_mil](../flags/advisor_events_mil.md), and has employed advisor has category is DIP; and has employed advisor has category is ADM:</li><ul><li>random list:</li><ul><li>2:</li><ul><li>event target:advisor liaisons target country:</li><ul><li>the event [Rapprochement with [From.GetUsableName]?](../events/rapprochement_with_from_getusablename.md) happens</li></ul></ul><li>1:</li><ul><li>the event [Allegations of Disloyalty](../events/allegations_of_disloyalty.md) happens</li></ul></ul></ul><li>else:</li><ul><li>event target:advisor liaisons target country:</li><ul><li>the event [Rapprochement with [From.GetUsableName]?](../events/rapprochement_with_from_getusablename.md) happens</li></ul></ul></ul></ul>

___
##We have no need for better relations with them.

###Efects:<ul><li>add prestige = 15</li><li>hidden effect:</li><ul><li>trigger switch:</li><ul><li>on trigger = has_country_flag</li><li>advisor events adm:</li><ul><li>clr country flag [advisor_events_adm](../flags/advisor_events_adm.md)</li></ul><li>advisor events dip:</li><ul><li>clr country flag [advisor_events_dip](../flags/advisor_events_dip.md)</li></ul><li>advisor events mil:</li><ul><li>clr country flag [advisor_events_mil](../flags/advisor_events_mil.md)</li></ul></ul></ul></ul>
