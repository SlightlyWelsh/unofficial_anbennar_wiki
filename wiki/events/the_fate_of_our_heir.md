#Information
 - Title: The Fate of our Heir
 - ID: new_sun_cult.165
#Description
The Fate of our Heir
#Options

___
##Praise be Surael!

###Available if:
<li>None of the following:</li><ul><li>has country flag [nsc_heir_will_die](../flags/nsc_heir_will_die.md)</li></ul>

###Efects:<ul><li>set heir = kidnapped_heir_@ROOT</li><li>If does not have ruler flag is [was_ruler_when_kidnapping_happened](../flags/was_ruler_when_kidnapping_happened.md); and  does not have regency:</li><ul><li>custom tooltip = nsc_ruler_will_step_down_tt</li><li>hidden effect:</li><ul><li>set country flag [nsc_no_level_loss](../flags/nsc_no_level_loss.md)</li><li>kill ruler = yes</li><li>add stability or adm power = yes</li></ul></ul><li>clr ruler flag [was_ruler_when_kidnapping_happened](../flags/was_ruler_when_kidnapping_happened.md)</li><li>add trust:</li><ul><li>who = event_target:nsc_target_country</li><li>value = -25</li><li>mutual = no</li></ul><li>add opinion:</li><ul><li>who = event_target:nsc_target_country</li><li>modifier = nsc_suspicious_behaviour_big</li></ul></ul>

___
##Nooooo!!

###Available if:
<li>has country flag [nsc_heir_will_die](../flags/nsc_heir_will_die.md)</li>

###Efects:<ul><li>add prestige = -5</li><li>clr country flag [nsc_heir_will_die](../flags/nsc_heir_will_die.md)</li><li>clr ruler flag [was_ruler_when_kidnapping_happened](../flags/was_ruler_when_kidnapping_happened.md)</li><li>add trust:</li><ul><li>who = event_target:nsc_target_country</li><li>value = -25</li><li>mutual = no</li></ul><li>add opinion:</li><ul><li>who = event_target:nsc_target_country</li><li>modifier = nsc_suspicious_behaviour_big</li></ul></ul>
