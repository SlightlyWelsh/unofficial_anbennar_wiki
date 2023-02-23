#Information
 - Title: The Pyre Burns!
 - ID: xhazobkult_events.1102
#Description
The Pyre Burns!
#Options

___
##Death, blood and pain in the name of Xhazob!

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>custom tooltip = xhazobkult_execute_sacrifice_effect_tt</li><li>If every owned province has building is xhazobkult pyre, and has province modifier is xhazobkult everpyre:</li><ul><li>remove building = xhazobkult_pyre</li><li>hidden effect:</li><ul><li>random:</li><ul><li>chance = 20</li><li>fire province event [xhazobkult_events.19](xhazobkult_events.19_slug) immediately </li></ul></ul></ul><li>hidden effect:</li><ul><li>If while has check variable has which is total gathered sacrifices, and check variable has value is 1:</li><ul><li>add patriarch authority = 0.01</li><li>change variable:</li><ul><li>which = total_gathered_sacrifices</li><li>value = -1</li></ul><li>If has faction is mykx xhazobkult:</li><ul><li>add faction influence:</li><ul><li>faction = mykx_xhazobkult</li><li>influence = 1</li></ul></ul></ul><li>set variable:</li><ul><li>which = total_gathered_sacrifices</li><li>value = 0</li></ul><li>clr country flag [xhazobkult_hide_sacrifice_gathering_events_flag](../flags/xhazobkult_hide_sacrifice_gathering_events_flag.md)</li></ul></ul>
