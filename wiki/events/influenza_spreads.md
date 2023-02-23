#Information
 - Title: Influenza Spreads
 - ID: random_event.24
#Description
Influenza Spreads
#Mean Time to Happen:
Base time = 120 months

#Options

___
##Quarantine the province!

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>add province modifier:</li><ul><li>name = "quarantined_influenza"</li><li>duration = 3650</li></ul><li>If every neighbor province has owned by is ROOT, and does not have province modifier is quarantined influenza:</li><ul><li>add province modifier:</li><ul><li>name = "quarantined_influenza"</li><li>duration = 3650</li></ul></ul><li>owner:</li><ul><li>If has any owned province has province modifier is influenza:</li><ul><li>If every owned province has province modifier is influenza:</li><ul><li>remove province modifier = influenza</li><li>add province modifier:</li><ul><li>name = "quarantined_influenza"</li><li>duration = 3650</li></ul></ul></ul></ul></ul>

___
##It will soon go away

###AI weighting:
AI weights this option at 50
 - Multiplied by 0 if has calc true if has all neighbor province has owned by is ROOT, and all neighbor province has development is 12; and calc true if has amount is 3


###Efects:<ul><li>add province modifier:</li><ul><li>name = "influenza"</li><li>duration = 3650</li></ul><li>If does not have province modifier is quarantined influenza; and does not have province modifier is influenza; and does not have province flag is [province_had_influenza](../flags/province_had_influenza.md):</li><ul><li>custom tooltip = random_events.23.b.tt</li></ul></ul>
