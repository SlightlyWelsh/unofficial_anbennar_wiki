#Information
 - Title: The Temple of Ma Hoang got severely damaged during the war
 - ID: flavor_honsai.25
#Description
The Temple of Ma Hoang got severely damaged during the war
#Options

___
##Unfortunately.

###Efects:<ul><li>goto = ROOT</li><li>add devastation = 15</li><li>If has province modifier is temple complex:</li><ul><li>remove province modifier = temple_complex</li><li>add permanent province modifier:</li><ul><li>name = derelict_temple_complex</li><li>duration = -1</li></ul><li>downgrade temple wards = yes</li></ul><li>Else if has province modifier is damaged temple complex:</li><ul><li>remove province modifier = damaged_temple_complex</li><li>add permanent province modifier:</li><ul><li>name = derelict_temple_complex</li><li>duration = -1</li></ul><li>downgrade temple wards = yes</li></ul></ul>
