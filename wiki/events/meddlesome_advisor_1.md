This page has the same name as others. For full listing see bottom of [the base page](meddlesome_advisor.md).

#Information
 - Title: Meddlesome Advisor
 - ID: new_court_flavour_events.32
#Description
Meddlesome Advisor
#Options

___
##Maybe [Root.GetEventAdvisorSheHe] is right after all.

###AI weighting:
AI weights this option at 2
 - Multiplied by 1.5 if has event target:advisor antiliaisons target country is not controlled by the AI
 - Multiplied by 0.75 if has opinion has who is event target:advisor antiliaisons target country, and has opinion has value is 50
 - Multiplied by 0.67 if does not have army strength has who is event target:advisor antiliaisons target country, and army strength has value is 0.75
 - Multiplied by 0.5 if does not have army strength has who is event target:advisor antiliaisons target country, and army strength has value is 0.5


###Efects:<ul><li>add opinion:</li><ul><li>who = event_target:advisor_antiliaisons_target_country</li><li>modifier = advisor_antiliaisons</li></ul><li>reverse add opinion:</li><ul><li>who = event_target:advisor_antiliaisons_target_country</li><li>modifier = advisor_spurious_accusations</li></ul><li>hidden effect:</li><ul><li>event target:advisor antiliaisons target country:</li><ul><li>country gets the modifier recent_liaising_advisor_timer for 50 years</li><li>the event [Meddlesome Advisor](../events/meddlesome_advisor.md) happens</li></ul></ul></ul>

___
##No means no.

###Efects:<ul><li>add stability = -1</li><li>reduce estate nobles loyalty effect = yes</li><li>hidden effect:</li><ul><li>trigger switch:</li><ul><li>on trigger = has_country_flag</li><li>advisor events adm:</li><ul><li>clr country flag [advisor_events_adm](../flags/advisor_events_adm.md)</li></ul><li>advisor events dip:</li><ul><li>clr country flag [advisor_events_dip](../flags/advisor_events_dip.md)</li></ul><li>advisor events mil:</li><ul><li>clr country flag [advisor_events_mil](../flags/advisor_events_mil.md)</li></ul></ul></ul></ul>
