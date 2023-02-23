#Information
 - Title: [Root.Overlord.GetAdjective] Factions Meddle in [Root.GetAdjective] Politics
 - ID: tributary_events.25
#Description
[Root.Overlord.GetAdjective] Factions Meddle in [Root.GetAdjective] Politics
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Rebels do not frighten us.

###Efects:<ul><li>If has government is monarchy:</li><ul><li>If random owned province has province flag is [tributary_supported_pretenders_here](../flags/tributary_supported_pretenders_here.md):</li><ul><li>spawn rebels:</li><ul><li>type = pretender_rebels</li><li>size = 2</li></ul><li>clr province flag [tributary_supported_pretenders_here](../flags/tributary_supported_pretenders_here.md)</li></ul></ul><li>If has government is theocracy:</li><ul><li>If random owned province has province flag is [tributary_supported_pretenders_here](../flags/tributary_supported_pretenders_here.md):</li><ul><li>spawn rebels:</li><ul><li>type = particularist_rebels</li><li>size = 1</li></ul><li>clr province flag [tributary_supported_pretenders_here](../flags/tributary_supported_pretenders_here.md)</li></ul></ul><li>If has government is republic:</li><ul><li>If random owned province has province flag is [tributary_supported_pretenders_here](../flags/tributary_supported_pretenders_here.md):</li><ul><li>spawn rebels:</li><ul><li>type = revolutionary_rebels</li><li>size = 1</li></ul><li>clr province flag [tributary_supported_pretenders_here](../flags/tributary_supported_pretenders_here.md)</li></ul></ul></ul>

___
##And a princely gift [Root.Overlord.Monarch.GetSheHe] will have!

###Efects:<ul><li>add years of income = -1</li><li>overlord:</li><ul><li>add trust:</li><ul><li>who = ROOT</li><li>value = 10</li></ul></ul><li>hidden effect:</li><ul><li>If random owned province has province flag is [tributary_supported_pretenders_here](../flags/tributary_supported_pretenders_here.md):</li><ul><li>clr province flag [tributary_supported_pretenders_here](../flags/tributary_supported_pretenders_here.md)</li></ul></ul></ul>
