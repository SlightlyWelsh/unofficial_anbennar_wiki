#Information
 - Title: The Xia is Beaten!
 - ID: flavor_azjakuma.2701
#Description
The Xia is Beaten!
#Options

___
##The [Root.Monarch.GetTitle] will personally oversee the Xia.

###Efects:<ul><li>set country flag [xia_subjugated_oni](../flags/xia_subjugated_oni.md)</li><li>If has any owned province has province flag is [azjakuma_was_territorial_core](../flags/azjakuma_was_territorial_core.md):</li><ul><li>custom tooltip = azjakuma_add_territorial_core_tooltip</li></ul><li>hidden effect:</li><ul><li>If every owned province has province flag is [azjakuma_was_territorial_core](../flags/azjakuma_was_territorial_core.md):</li><ul><li>add territorial core = ROOT</li><li>clr province flag [azjakuma_was_territorial_core](../flags/azjakuma_was_territorial_core.md)</li></ul></ul></ul>

___
##The Yuanszi will be a better fit for integrating the populace

###Efects:<ul><li>If every owned province has region is xianjie region, and does not have province modifier is temple complex, and does not have province modifier is damaged temple complex, and does not have province modifier is ruined temple complex, and does not have province modifier is corrupted temple complex:</li><ul><li>cede province = Y89</li></ul><li>set country flag [xia_subjugated_oni](../flags/xia_subjugated_oni.md)</li><li>Y01:</li><ul><li>create subject:</li><ul><li>subject type = oni_governorship</li><li>subject = Y89</li></ul></ul><li>Y89:</li><ul><li>change religion = lefthand_path</li><li>country gets the modifier azjakuma_rethagi until otherwise removed</li></ul><li>hidden effect:</li><ul><li>add opinion:</li><ul><li>who = Y89</li><li>modifier = loyal_servants</li></ul><li>reverse add opinion:</li><ul><li>who = Y89</li><li>modifier = noble_oni</li></ul></ul><li>custom tooltip = rethagi_grant_tooltip</li></ul>
