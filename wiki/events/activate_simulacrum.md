#Information
 - Title: Activate Simulacrum?
 - ID: magic_ruler.21
#Description
Activate Simulacrum?
#Options

___
##Summon Simulacrum

###Available if:
<li>has ruler flag [illusion_3](../flags/illusion_3.md)</li><li>has ruler flag  magic_project_simulacrum_complete</li><li>has ruler modifier ruler_studying_magic</li>

###AI weighting:
AI weights this option at 50
 - Multiplied by 0 if does not have adm power is 20; and does not have dip power is 20


###Efects:<ul><li>add adm power = -20</li><li>add dip power = -20</li><li>magic casted spell = yes</li><li>If has ruler flag is [magic_realm_simulacrum_exposed](../flags/magic_realm_simulacrum_exposed.md):</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_illusion_simulacrum_exposed</li><li>duration = 3650</li></ul></ul><li>else:</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_illusion_simulacrum</li><li>duration = 3650</li></ul></ul></ul>

___
##No thanks

###AI weighting:
AI weights this option at 10


###Efects:<ul><li>add ruler modifier:</li><ul><li>name = ruler_cooldown_10yr</li><li>duration = 3650</li><li>hidden = yes</li></ul></ul>
