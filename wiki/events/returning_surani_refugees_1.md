This page has the same name as others. For full listing see bottom of [the base page](returning_surani_refugees.md).

#Information
 - Title: Returning Surani Refugees
 - ID: bulwar_flavour.100
#Description
Returning Surani Refugees
#Options

___
##Welcome them back!

###AI weighting:
AI weights this option at 1


###One of the following randomly happens:
Outcome 1:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>add base tax = 1</li></ul>
Outcome 2:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>add base production = 1</li></ul>
Outcome 3:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>add base manpower = 1</li></ul>

###Efects:<ul><li>If does not have culture group is bulwari; and  has large human minority trigger is no:</li><ul><li>add human minority size effect = yes</li><li>add devastation = 1</li></ul><li>Else if does not have culture group is bulwari; and  has large human minority trigger is yes:</li><ul><li>If has area is jikarzax area:</li><ul><li>change culture = masnsih</li><li>add core = F79</li></ul><li>else:</li><ul><li>change culture = surani</li></ul><li>add province modifier:</li><ul><li>name = add_unrest_5_modifier</li><li>duration = 730</li></ul><li>add devastation = 10</li><li>If has owner has religion is the jadd:</li><ul><li>change religion = the_jadd</li></ul><li>Else if has owner has religion is old bulwari sun cult:</li><ul><li>change religion = old_bulwari_sun_cult</li></ul><li>else:</li><ul><li>change religion = bulwari_sun_cult</li></ul></ul><li>If random province has superregion is bulwar superregion, and  has or has province modifier is surani refugee large, and or has province modifier is surani refugee medium, and or has province modifier is surani refugee small:</li><ul><li>fire province event [bulwar_flavour.29](bulwar_flavour.29_slug) in 10 days</li></ul><li>If random province has culture group is bulwari, and  has or has area is azka sur area, and or has area is upper suran area, and or has area is eduz vacyn area:</li><ul><li>random list:</li><ul><li>55:</li><ul></ul><li>15:</li><ul><li>add base tax = 1</li></ul><li>15:</li><ul><li>add base production = 1</li></ul><li>15:</li><ul><li>add base manpower = 1</li></ul></ul></ul></ul>
