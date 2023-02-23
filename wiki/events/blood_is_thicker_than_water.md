#Information
 - Title: Blood is Thicker than Water?
 - ID: new_court_flavour_events.25
#Description
Blood is Thicker than Water?
#Options

___
##They are right - banish [Root.GetEventAdvisorHerHim]!

###AI weighting:
AI weights this option at 1
 - Multiplied by 0.5 if has AND has country flag is [advisor_events_adm](../flags/advisor_events_adm.md), and AND has adm advisor 3 is yes; and has AND has country flag is [advisor_events_dip](../flags/advisor_events_dip.md), and AND has dip advisor 3 is yes; and has AND has country flag is [advisor_events_mil](../flags/advisor_events_mil.md), and AND has mil advisor 3 is yes


###Efects:<ul><li>trigger switch:</li><ul><li>on trigger = has_country_flag</li><li>advisor events adm:</li><ul><li>remove advisor by category = ADM</li></ul><li>advisor events dip:</li><ul><li>remove advisor by category = DIP</li></ul><li>advisor events mil:</li><ul><li>remove advisor by category = MIL</li></ul></ul><li>hidden effect:</li><ul><li>trigger switch:</li><ul><li>on trigger = has_country_flag</li><li>advisor events adm:</li><ul><li>clr country flag [advisor_events_adm](../flags/advisor_events_adm.md)</li></ul><li>advisor events dip:</li><ul><li>clr country flag [advisor_events_dip](../flags/advisor_events_dip.md)</li></ul><li>advisor events mil:</li><ul><li>clr country flag [advisor_events_mil](../flags/advisor_events_mil.md)</li></ul></ul><li>set variable:</li><ul><li>which = advisor_culture</li><li>value = -1</li></ul></ul></ul>

___
##Keep [Root.GetEventAdvisorHerHim] - [Root.GetEventAdvisorHerHis] information will be useful.

###One of the following randomly happens:
Outcome 1:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>custom tooltip = tooltip_in_30_days</li><li>custom tooltip = new_court_flavour_events.10.A.tt2</li><li>tooltip:</li><ul><li>event target:advisor enemy country:</li><ul><li>root:</li><ul><li>remove fow = 6</li></ul></ul><li>add prestige = -15</li></ul><li>hidden effect:</li><ul><li>event target:advisor enemy country:</li><ul><li>the event ˻new_court_flavour_events.27˼ happens</li></ul></ul></ul>
Outcome 2:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>custom tooltip = tooltip_in_30_days</li><li>custom tooltip = new_court_flavour_events.10.A.tt1</li><li>tooltip:</li><ul><li>event target:advisor enemy country:</li><ul><li>remove fow = 6</li></ul></ul><li>hidden effect:</li><ul><li>the event ˻new_court_flavour_events.26˼ happens</li></ul></ul>

###Efects:<ul><li>reduce estate nobles loyalty effect = yes</li></ul>
