This page has the same name as others. For full listing see bottom of [the base page](unlimited_power.md).

#Information
 - Title: Unlimited Power!
 - ID: spirits.609
#Description
Unlimited Power!
#Options

___
##an Expanded Mind

###Available if:
<li>None of the following:</li><ul><li>adm is at least 6</li></ul>

###Efects:<ul><li>change adm = 1</li><li>lhp heart drain choose option = yes</li></ul>

___
##an Enthralling Soul

###Available if:
<li>None of the following:</li><ul><li>dip is at least 6</li></ul>

###Efects:<ul><li>change dip = 1</li><li>lhp heart drain choose option = yes</li></ul>

___
##a Mighty Will

###Available if:
<li>None of the following:</li><ul><li>mil is at least 6</li></ul>

###Efects:<ul><li>change mil = 1</li><li>lhp heart drain choose option = yes</li></ul>

___
##an Infusion of Chi

###Available if:
<li>ruler has mage personality is yes</li>

###Efects:<ul><li>add adm power = 75</li><li>add dip power = 75</li><li>add mil power = 75</li><li>lhp heart drain choose option = yes</li></ul>

___
##an Infusion of Power

###Available if:
<li>None of the following:</li><ul><li>ruler has mage personality is yes</li></ul>

###Efects:<ul><li>If has ruler has max personalities is yes:</li><ul><li>hidden effect:</li><ul><li>clear ruler personalities = yes</li><li>If has ruler flag is [spirits_immortal_ruler](../flags/spirits_immortal_ruler.md):</li><ul><li>add ruler personality = immortal_personality</li></ul></ul></ul><li>add ruler personality = mage_personality</li><li>lhp heart drain choose option = yes</li></ul>

___
##an Unnatural Life

###Available if:
<li>ruler has mage personality is yes</li><li>has country flag [lefthand_life_extension_unlocked](../flags/lefthand_life_extension_unlocked.md)</li><li>None of the following:</li><ul><li>has ruler flag [is_a_lich](../flags/is_a_lich.md)</li></ul><li>NOT:</li><ul><li>has ruler flag [is_a_vampire](../flags/is_a_vampire.md)</li></ul><li>NOT:</li><ul><li>is variable equal:</li><ul><li>which is lefthand_life_extension_max_age_var</li><li>value is at least 190</li></ul></ul>

###Efects:<ul><li>If has ruler has max personalities is yes, and does not have ruler has personality is immortal personality:</li><ul><li>hidden effect:</li><ul><li>clear ruler personalities = yes</li><li>add ruler personality = mage_personality</li></ul><li>add ruler personality = immortal_personality</li></ul><li>else:</li><ul><li>add ruler personality = immortal_personality</li></ul><li>custom tooltip = spirits_life_extension_option_tooltip</li><li>hidden effect:</li><ul><li>If does not have ruler flag is [lefthand_life_extension](../flags/lefthand_life_extension.md):</li><ul><li>set variable:</li><ul><li>which = lefthand_life_extension_max_age_var</li><li>value = 110</li></ul><li>set ruler flag [lefthand_life_extension](../flags/lefthand_life_extension.md)</li></ul><li>Else if has ruler flag is [lefthand_life_extension](../flags/lefthand_life_extension.md), and  is variable equal has which is lefthand life extension max age var, and is variable equal has value is 110:</li><ul><li>change variable:</li><ul><li>which = lefthand_life_extension_max_age_var</li><li>value = 30</li></ul></ul><li>Else if has ruler flag is [lefthand_life_extension](../flags/lefthand_life_extension.md), and  is variable equal has which is lefthand life extension max age var, and is variable equal has value is 140:</li><ul><li>change variable:</li><ul><li>which = lefthand_life_extension_max_age_var</li><li>value = 20</li></ul></ul><li>Else if has ruler flag is [lefthand_life_extension](../flags/lefthand_life_extension.md), and  is variable equal has which is lefthand life extension max age var, and is variable equal has value is 160:</li><ul><li>change variable:</li><ul><li>which = lefthand_life_extension_max_age_var</li><li>value = 15</li></ul></ul><li>Else if has ruler flag is [lefthand_life_extension](../flags/lefthand_life_extension.md), and  is variable equal has which is lefthand life extension max age var, and is variable equal has value is 175:</li><ul><li>change variable:</li><ul><li>which = lefthand_life_extension_max_age_var</li><li>value = 10</li></ul></ul><li>Else if has ruler flag is [lefthand_life_extension](../flags/lefthand_life_extension.md), and  is variable equal has which is lefthand life extension max age var, and is variable equal has value is 185:</li><ul><li>change variable:</li><ul><li>which = lefthand_life_extension_max_age_var</li><li>value = 5</li></ul></ul></ul><li>lhp heart drain choose option = yes</li></ul>

___
##Go Back

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>the event [Draining the Heart](../events/draining_the_heart.md) happens</li></ul>
