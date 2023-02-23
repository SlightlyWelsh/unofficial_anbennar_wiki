#Information
 - Title: [Root.GetName] Expedition
 - ID: diggy_expedition.2
#Description
[Root.GetName] Expedition
#Options

___
##Go back

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>owner:</li><ul><li>hidden effect:</li><ul><li>If every owned province has province flag is [expedition_@ROOT](../flags/expedition_root.md):</li><ul><li>clr province flag [expedition_@ROOT](../flags/expedition_root.md)</li></ul></ul><li>the event [Expedition Menu](../events/expedition_menu.md) happens</li></ul></ul>

___
##Organise the expedition

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>custom tooltip = prepare_expedition_tooltip</li><li>hidden effect:</li><ul><li>set province flag [sent_expedition_@ROOT](../flags/sent_expedition_root.md)</li><li>owner:</li><ul><li>set country flag [expedition_happening](../flags/expedition_happening.md)</li></ul><li>If has owner is not controlled by the AI:</li><ul><li>generate party stats = yes</li><li>fire province event [diggy_expedition.3](diggy_expedition.3_slug) immediately </li></ul><li>else:</li><ul><li>owner:</li><ul><li>clr country flag [debug_menu](../flags/debug_menu.md)</li></ul></ul></ul></ul>
