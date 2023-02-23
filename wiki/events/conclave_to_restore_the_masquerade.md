#Information
 - Title: Conclave to Restore the Masquerade
 - ID: disaster_vampire_masquerade.11
#Description
Conclave to Restore the Masquerade
#Options

___
##I can only accept...

###Available if:
<li>None of the following:</li><ul><li>has ruler flag [is_a_vampire](../flags/is_a_vampire.md)</li></ul>

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>change dip = -2</li><li>change adm = -2</li><li>change mil = -2</li><li>add ruler modifier:</li><ul><li>name = vampire_thrall</li><li>duration = -1</li></ul><li>add stability or adm power = yes</li><li>clear vampire organization = yes</li><li>clear vampire law = yes</li><li>set estate privilege = estate_vampires_organization_bloody_aristocracy</li><li>set estate privilege = estate_vampires_law_traditional_masquerade</li><li>end disaster = estate_vampires_restore_masquerade_disaster</li></ul>

___
##Fight them off!

###AI weighting:
AI weights this option at 10


###One of the following randomly happens:
Outcome 1:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>change dip = -1</li></ul>
Outcome 2:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>change adm = -1</li></ul>
Outcome 3:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>change mil = -1</li></ul>

###Efects:<ul><li>add ruler modifier:</li><ul><li>name = wounded_ruler</li><li>duration = 1095</li></ul><li>the event [To Choke an Unborn Rebellion](../events/to_choke_an_unborn_rebellion.md) happens</li></ul>

___
##I will return to the shadows

###Available if:
<li>has ruler flag [is_a_vampire](../flags/is_a_vampire.md)</li>

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>hidden effect:</li><ul><li>clear ruler vampire flags = yes</li></ul><li>exile ruler as:</li><ul><li>name = my_exiled_ruler</li></ul><li>add stability or adm power = yes</li><li>clear vampire organization = yes</li><li>clear vampire law = yes</li><li>set estate privilege = estate_vampires_organization_bloody_aristocracy</li><li>set estate privilege = estate_vampires_law_traditional_masquerade</li><li>end disaster = estate_vampires_restore_masquerade_disaster</li><li>define ruler:</li><ul><li>culture = ROOT</li><li>religion = ROOT</li></ul><li>add ruler modifier:</li><ul><li>name = vampire_thrall</li><li>duration = -1</li></ul></ul>
