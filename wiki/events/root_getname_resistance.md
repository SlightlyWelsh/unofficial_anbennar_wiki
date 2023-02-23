#Information
 - Title: [Root.GetName] Resistance
 - ID: ibevar.4
#Description
[Root.GetName] Resistance
#Options

___
##Send Starwatcher's finest missionaries.

###Available if:
<li>None of the following:</li><ul><li>has province flag [ibe_option_1](../flags/ibe_option_1.md)</li></ul>

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>hidden effect:</li><ul><li>ibevar province flag = yes</li></ul><li>hidden effect:</li><ul><li>set province flag [ibe_option_1](../flags/ibe_option_1.md)</li></ul><li>fire province event [ibevar.100](ibevar.100_slug) immediately </li><li>owner:</li><ul><li>tooltip:</li><ul><li>random list:</li><ul><li>50:</li><ul><li>add treasury = -15</li></ul><li>35:</li><ul><li>add treasury = -30</li></ul><li>15:</li><ul><li>add treasury = -50</li></ul></ul></ul><li>hidden effect:</li><ul><li>the event [Missing localisation: ibevar_104_t](../events/missing_localisation_ibevar_104_t.md) happens</li></ul></ul></ul>

___
##Send aid to the local officials.

###Available if:
<li>None of the following:</li><ul><li>has province flag [ibe_option_2](../flags/ibe_option_2.md)</li></ul>

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>hidden effect:</li><ul><li>ibevar province flag = yes</li></ul><li>hidden effect:</li><ul><li>set province flag [ibe_option_2](../flags/ibe_option_2.md)</li></ul><li>fire province event [ibevar.100](ibevar.100_slug) immediately </li><li>owner:</li><ul><li>tooltip:</li><ul><li>random list:</li><ul><li>33:</li><ul><li>add adm power = -15</li></ul><li>33:</li><ul><li>add dip power = -15</li></ul><li>33:</li><ul><li>add mil power = -15</li></ul></ul></ul><li>hidden effect:</li><ul><li>the event [Missing localisation: ibevar_104_t](../events/missing_localisation_ibevar_104_t.md) happens</li></ul></ul></ul>

___
##Send soldiers to keep the peace.

###Available if:
<li>None of the following:</li><ul><li>has province flag [ibe_option_3](../flags/ibe_option_3.md)</li></ul><li>owner:</li><ul><li>manpower is at least 1.5</li></ul>

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>hidden effect:</li><ul><li>ibevar province flag = yes</li></ul><li>hidden effect:</li><ul><li>set province flag [ibe_option_3](../flags/ibe_option_3.md)</li></ul><li>fire province event [ibevar.100](ibevar.100_slug) immediately </li><li>owner:</li><ul><li>tooltip:</li><ul><li>random list:</li><ul><li>50:</li><ul><li>add manpower = -0.5</li></ul><li>35:</li><ul><li>add manpower = -1</li></ul><li>15:</li><ul><li>add manpower = -1.5</li></ul></ul></ul><li>hidden effect:</li><ul><li>the event [Missing localisation: ibevar_104_t](../events/missing_localisation_ibevar_104_t.md) happens</li></ul></ul></ul>

___
##Start Operations

###Available if:
<li>custom trigger tooltip:</li><ul><li>tooltip is ibevar4_option_tooltip</li><li>Any of the following:</li><ul><li>has province flag [ibe_1](../flags/ibe_1.md)</li><li>has province flag  ibe_2</li><li>has province flag   ibe_3</li></ul></ul>

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>highlight = yes</li><li>owner:</li><ul><li>country gets the modifier ibevar_reformation_work until otherwise removed</li></ul><li>If has owner is controlled by the AI:</li><ul><li>fire province event [ibevar.103](ibevar.103_slug) in 30 to 90 days</li></ul><li>else:</li><ul><li>fire province event [ibevar.103](ibevar.103_slug) in 60 to 120 days</li></ul><li>hidden effect:</li><ul><li>owner:</li><ul><li>clr country flag [ibevar_reformation_menu_debug_flag](../flags/ibevar_reformation_menu_debug_flag.md)</li></ul><li>set province flag [ibevar_reformation_work_flag](../flags/ibevar_reformation_work_flag.md)</li></ul><li>custom tooltip = ibevar4_option_tooltip2</li></ul>

___
##Go Back

###Available if:
<li>None of the following:</li><ul><li>Any of the following:</li><ul><li>has province flag [ibe_1](../flags/ibe_1.md)</li><li>has province flag  ibe_2</li><li>has province flag   ibe_3</li></ul></ul>

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>owner:</li><ul><li>the event [[A32.Monarch.GetName]'s Reformation Efforts](../events/a32_monarch_getname_s_reformation_efforts.md) happens</li></ul></ul>


#Pages with same name:
The following pages have the same name as this page:
 - [root_getname_resistance_1](root_getname_resistance_1.md)
