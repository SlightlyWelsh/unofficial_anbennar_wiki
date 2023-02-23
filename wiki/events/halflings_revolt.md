#Information
 - Title: Halflings Revolt!
 - ID: flavor_smallcountry.1
#Description
Halflings Revolt!
#Options

___
##Suppress the rebels!

###Efects:<ul><li>add stability = -2</li><li>If random owned province has region is small country region, and has culture is bluefoot halfling, and has culture is redfoot halfling, and has culture is imperial halfling, and has culture is visfoot halfling:</li><ul><li>spawn rebels:</li><ul><li>type = nationalist_rebels</li><li>size = 3</li><li>friend = A97</li></ul><li>set province flag [A97_rebels_start_flag](../flags/a97_rebels_start_flag.md)</li></ul><li>If random owned province does not have province flag is [A97_rebels_start_flag](../flags/a97_rebels_start_flag.md); and  has region is small country region, and has culture is bluefoot halfling, and has culture is redfoot halfling, and has culture is imperial halfling, and has culture is visfoot halfling:</li><ul><li>spawn rebels:</li><ul><li>type = nationalist_rebels</li><li>size = 3</li><li>friend = A97</li></ul><li>set province flag [A97_rebels_start_flag](../flags/a97_rebels_start_flag.md)</li><li>set province flag [halfling_revolt](../flags/halfling_revolt.md)</li></ul><li>custom tooltip = halfling_revolt_tt</li><li>hidden effect:</li><ul><li>If small country region has owned by is ROOT, and has culture is bluefoot halfling, and has culture is redfoot halfling, and has culture is imperial halfling, and has culture is visfoot halfling:</li><ul><li>add province modifier:</li><ul><li>name = "halfling_revolt_modifier"</li><li>duration = -1</li></ul></ul></ul></ul>
