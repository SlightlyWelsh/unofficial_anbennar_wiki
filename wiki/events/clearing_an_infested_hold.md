#Information
 - Title: Clearing an Infested Hold
 - ID: diggy.48
#Description
Clearing an Infested Hold
#Options

___
##Clear §O[infested1.GetName]§!

###Available if:
<li>any owned province:</li><ul><li>has province flag [option_infested_1_@ROOT](../flags/option_infested_1_root.md)</li><li>is city</li></ul>

###AI weighting:
AI weights this option at 5


###Efects:<ul><li>goto = infested1</li><li>If random owned province has province flag is [option_infested_1_@ROOT](../flags/option_infested_1_root.md), and  is city:</li><ul><li>infested hold clearing = yes</li></ul></ul>

___
##Clear §O[infested2.GetName]§!

###Available if:
<li>any owned province:</li><ul><li>has province flag [option_infested_2_@ROOT](../flags/option_infested_2_root.md)</li><li>is city</li></ul>

###AI weighting:
AI weights this option at 5


###Efects:<ul><li>goto = infested2</li><li>If random owned province has province flag is [option_infested_2_@ROOT](../flags/option_infested_2_root.md), and  is city:</li><ul><li>infested hold clearing = yes</li></ul></ul>

___
##Clear §O[infested3.GetName]§!

###Available if:
<li>any owned province:</li><ul><li>has province flag [option_infested_3_@ROOT](../flags/option_infested_3_root.md)</li><li>is city</li></ul>

###AI weighting:
AI weights this option at 5


###Efects:<ul><li>goto = infested3</li><li>If random owned province has province flag is [option_infested_3_@ROOT](../flags/option_infested_3_root.md), and  is city:</li><ul><li>infested hold clearing = yes</li></ul></ul>

___
##Clear §O[infested4.GetName]§!

###Available if:
<li>any owned province:</li><ul><li>has province flag [option_infested_4_@ROOT](../flags/option_infested_4_root.md)</li><li>is city</li></ul>

###AI weighting:
AI weights this option at 5


###Efects:<ul><li>goto = infested4</li><li>If random owned province has province flag is [option_infested_4_@ROOT](../flags/option_infested_4_root.md), and  is city:</li><ul><li>infested hold clearing = yes</li></ul></ul>

___
##Go Back

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>hidden effect:</li><ul><li>If every owned province has province flag is [infested_@ROOT](../flags/infested_root.md):</li><ul><li>clr province flag [infested_@ROOT](../flags/infested_root.md)</li><li>clr province flag [option_infested_1_@ROOT](../flags/option_infested_1_root.md)</li><li>clr province flag [option_infested_2_@ROOT](../flags/option_infested_2_root.md)</li><li>clr province flag [option_infested_3_@ROOT](../flags/option_infested_3_root.md)</li><li>clr province flag [option_infested_4_@ROOT](../flags/option_infested_4_root.md)</li></ul><li>clr country flag [open_infested_hold_menu](../flags/open_infested_hold_menu.md)</li></ul></ul>
