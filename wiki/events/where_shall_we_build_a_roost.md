#Information
 - Title: Where shall we build a roost?
 - ID: harpy_events.1
#Description
Where shall we build a roost?
#Options

___
##In the capital

###Available if:
<li>can build roost is yes</li><li>capital scope:</li><ul><li>fort level is at least 1</li><li>has harpy majority trigger yes</li><li>is city</li><li>Any of the following:</li><ul><li>has terrain mountain</li><li>has terrain  highlands</li><li>has terrain   hills</li></ul><li>None of the following:</li><ul><li>has province modifier harpy_roost</li></ul></ul>

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>goto = capital_scope</li><li>capital scope:</li><ul><li>add province triggered modifier = harpy_roost</li><li>add province modifier:</li><ul><li>name = harpy_roost_under_construction</li><li>duration = 365</li></ul><li>add province modifier:</li><ul><li>name = same_roost_owner</li><li>duration = -1</li><li>hidden = yes</li></ul></ul><li>update roost count = yes</li></ul>

___
##In the [harpy_roost_region1.GetRegionName] Region

###Available if:
<li>can build roost is yes</li><li>has saved event target harpy_roost_region1</li>

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>goto = harpy_roost_region1</li><li>hidden effect:</li><ul><li>event target:harpy roost region1:</li><ul><li>fire province event [harpy_events.2](harpy_events.2_slug) immediately </li></ul></ul></ul>

___
##In the [harpy_roost_region2.GetRegionName] Region

###Available if:
<li>can build roost is yes</li><li>has saved event target harpy_roost_region2</li>

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>goto = harpy_roost_region2</li><li>hidden effect:</li><ul><li>event target:harpy roost region2:</li><ul><li>fire province event [harpy_events.2](harpy_events.2_slug) immediately </li></ul></ul></ul>

___
##In the [harpy_roost_region3.GetRegionName] Region

###Available if:
<li>can build roost is yes</li><li>has saved event target harpy_roost_region3</li>

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>goto = harpy_roost_region3</li><li>hidden effect:</li><ul><li>event target:harpy roost region3:</li><ul><li>fire province event [harpy_events.2](harpy_events.2_slug) immediately </li></ul></ul></ul>

___
##In the [harpy_roost_region4.GetRegionName] Region

###Available if:
<li>can build roost is yes</li><li>has saved event target harpy_roost_region4</li>

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>goto = harpy_roost_region4</li><li>hidden effect:</li><ul><li>event target:harpy roost region4:</li><ul><li>fire province event [harpy_events.2](harpy_events.2_slug) immediately </li></ul></ul></ul>

___
##In the [harpy_roost_region5.GetRegionName] Region

###Available if:
<li>can build roost is yes</li><li>has saved event target harpy_roost_region5</li>

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>goto = harpy_roost_region5</li><li>hidden effect:</li><ul><li>event target:harpy roost region5:</li><ul><li>fire province event [harpy_events.2](harpy_events.2_slug) immediately </li></ul></ul></ul>

___
##In the [harpy_roost_region6.GetRegionName] Region

###Available if:
<li>can build roost is yes</li><li>has saved event target harpy_roost_region6</li>

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>goto = harpy_roost_region6</li><li>hidden effect:</li><ul><li>event target:harpy roost region6:</li><ul><li>fire province event [harpy_events.2](harpy_events.2_slug) immediately </li></ul></ul></ul>

___
##In the [harpy_roost_region7.GetRegionName] Region

###Available if:
<li>can build roost is yes</li><li>has saved event target harpy_roost_region7</li>

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>goto = harpy_roost_region7</li><li>hidden effect:</li><ul><li>event target:harpy roost region7:</li><ul><li>fire province event [harpy_events.2](harpy_events.2_slug) immediately </li></ul></ul></ul>

___
##In the [harpy_roost_region8.GetRegionName] Region

###Available if:
<li>can build roost is yes</li><li>has saved event target harpy_roost_region8</li>

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>goto = harpy_roost_region8</li><li>hidden effect:</li><ul><li>event target:harpy roost region8:</li><ul><li>fire province event [harpy_events.2](harpy_events.2_slug) immediately </li></ul></ul></ul>

___
##In the [harpy_roost_region9.GetRegionName] Region

###Available if:
<li>can build roost is yes</li><li>has saved event target harpy_roost_region9</li>

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>goto = harpy_roost_region9</li><li>hidden effect:</li><ul><li>event target:harpy roost region9:</li><ul><li>fire province event [harpy_events.2](harpy_events.2_slug) immediately </li></ul></ul></ul>

___
##In the [harpy_roost_region10.GetRegionName] Region

###Available if:
<li>can build roost is yes</li><li>has saved event target harpy_roost_region10</li>

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>goto = harpy_roost_region10</li><li>hidden effect:</li><ul><li>event target:harpy roost region10:</li><ul><li>fire province event [harpy_events.2](harpy_events.2_slug) immediately </li></ul></ul></ul>

___
##Nevermind

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>add adm power = 50</li><li>clr country flag [open_harpy_roost_menu](../flags/open_harpy_roost_menu.md)</li></ul>


#Pages with same name:
The following pages have the same name as this page:
 - [where_shall_we_build_a_roost_1](where_shall_we_build_a_roost_1.md)
