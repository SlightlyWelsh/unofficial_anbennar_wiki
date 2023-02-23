#Information
 - Title: Influenza!
 - ID: random_event.23
#Description
Influenza!
#Mean Time to Happen:
Base time = 600 months
 - Multiplied by 0.9 if has terrain is marsh

#Options

___
##Quarantine the port and let them die!

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>owner:</li><ul><li>add adm power = -50</li></ul><li>add province modifier:</li><ul><li>name = "quarantined_influenza"</li><li>duration = 3650</li></ul></ul>

___
##This is not the first flu in our country, I don't care!

###AI weighting:
AI weights this option at 50
 - Multiplied by 0 if has calc true if has all neighbor province has owned by is ROOT, and all neighbor province has development is 12; and calc true if has amount is 3


###Efects:<ul><li>add province modifier:</li><ul><li>name = "influenza"</li><li>duration = 3650</li></ul><li>If does not have province modifier is quarantined influenza; and does not have province modifier is influenza; and does not have province flag is [province_had_influenza](../flags/province_had_influenza.md):</li><ul><li>custom tooltip = random_events.23.b.tt</li></ul></ul>
