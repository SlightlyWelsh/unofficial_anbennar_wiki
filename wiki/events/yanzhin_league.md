#Information
 - Title: Yanzhin League
 - ID: flavor_azjakuma.2655
#Description
Yanzhin League
#Options

___
##We shall directly control the temple complexes. The rest shall belong to a Rethagi...

###Efects:<ul><li>If has alliance with is Y10, and has Y10 is subject of is Y01:</li><ul><li>create subject:</li><ul><li>subject type = oni_governorship</li><li>subject = Y10</li></ul><li>If every owned province has area is anjiang area, and has area is linyuan area, and has area is yanzhong area; and does not have province modifier is temple complex; and does not have province modifier is damaged temple complex; and does not have province modifier is derelict temple complex; and does not have province modifier is ruined temple complex; and does not have province modifier is corrupted temple complex:</li><ul><li>cede province = Y10</li></ul><li>Y10:</li><ul><li>change religion = lefthand_path</li><li>country gets the modifier azjakuma_rethagi until otherwise removed</li><li>If anjiang area does not have core is PREV, and does not have permanent claim is PREV, and does not have province group is temple province group:</li><ul><li>add permanent claim = PREV</li></ul><li>If linyuan area does not have core is PREV, and does not have permanent claim is PREV, and does not have province group is temple province group:</li><ul><li>add permanent claim = PREV</li></ul><li>If yanzhong area does not have core is PREV, and does not have permanent claim is PREV, and does not have province group is temple province group:</li><ul><li>add permanent claim = PREV</li></ul></ul><li>If while does not have check variable has which is provinceCountIncrementY, and check variable has which is provinceCountY:</li><ul><li>add adm power = 80</li><li>change variable:</li><ul><li>which = provinceCountIncrementY</li><li>value = 1</li></ul></ul><li>custom tooltip = azjakuma_returned_80_adm_tooltip</li></ul><li>else:</li><ul><li>If every owned province has area is anjiang area, and has area is linyuan area, and has area is yanzhong area; and does not have province modifier is temple complex; and does not have province modifier is damaged temple complex; and does not have province modifier is derelict temple complex; and does not have province modifier is ruined temple complex; and does not have province modifier is corrupted temple complex:</li><ul><li>cede province = Y10</li></ul><li>create subject:</li><ul><li>subject type = oni_governorship</li><li>subject = Y10</li></ul><li>Y10:</li><ul><li>change religion = lefthand_path</li><li>country gets the modifier azjakuma_rethagi until otherwise removed</li><li>If anjiang area does not have core is PREV, and does not have permanent claim is PREV, and does not have province group is temple province group:</li><ul><li>add permanent claim = PREV</li></ul><li>If linyuan area does not have core is PREV, and does not have permanent claim is PREV, and does not have province group is temple province group:</li><ul><li>add permanent claim = PREV</li></ul><li>If yanzhong area does not have core is PREV, and does not have permanent claim is PREV, and does not have province group is temple province group:</li><ul><li>add permanent claim = PREV</li></ul></ul><li>add opinion:</li><ul><li>who = Y10</li><li>modifier = loyal_servants</li></ul><li>reverse add opinion:</li><ul><li>who = Y10</li><li>modifier = noble_oni</li></ul><li>If while does not have check variable has which is provinceCountIncrementY, and check variable has which is provinceCountY:</li><ul><li>add adm power = 80</li><li>change variable:</li><ul><li>which = provinceCountIncrementY</li><li>value = 1</li></ul></ul></ul><li>custom tooltip = rethagi_grant_tooltip</li><li>custom tooltip = azjakuma_returned_80_adm_tooltip</li></ul>

___
##The government of Yingshi will be easy to reconfigure into a Rethagi...

###Available if:
<li>Any of the following:</li><ul><li>alliance with is Y10</li><li>Y10:</li><ul><li>is subject of is Y01</li><li>is controlled by the AI</li></ul></ul>

###Efects:<ul><li>create subject:</li><ul><li>subject type = oni_governorship</li><li>subject = Y10</li></ul><li>Y10:</li><ul><li>change religion = lefthand_path</li><li>country gets the modifier azjakuma_rethagi until otherwise removed</li></ul><li>custom tooltip = rethagi_grant_tooltip</li></ul>

___
##Why would I give away land that will be perfectly usable in only a few decades at most?
