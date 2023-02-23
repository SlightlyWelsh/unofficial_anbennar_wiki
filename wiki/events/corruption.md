#Information
 - Title: Corruption
 - ID: 5055
#Description
Corruption
#Mean Time to Happen:
Base time = 1 days
 - Multiplied by 2.0 if has num of loans is 1
 - Multiplied by 0.5 if is lucky
 - Multiplied by 0.5 if does not have corruption is 0.5
 - Multiplied by 2 if has corruption is 4
 - Multiplied by 0.66 if has advisor is treasurer

#Options

___
##Try to eradicate the problems.

###AI weighting:
AI weights this option at 55
 - Multiplied by 0.5 if does not have stability is 1


###Efects:<ul><li>If does not have stability is -2:</li><ul><li>add adm power = -100</li></ul><li>If has stability is -2:</li><ul><li>add stability = -1</li></ul></ul>

___
##Ignore them.

###AI weighting:
AI weights this option at 45
 - Multiplied by 0.5 if has corruption is 10


###Efects:<ul><li>If has completed all reforms trigger is yes:</li><ul><li>add corruption = 2</li></ul><li>else:</li><ul><li>add corruption = 1</li><li>reduce reform progress small effect = yes</li></ul><li>If has country flag is [tyrant_system_initialized](../flags/tyrant_system_initialized.md):</li><ul><li>increase tyrant ruthless 1 = yes</li></ul></ul>

___
##Allow our [Root.Monarch.GetTitle] to deal with any visible signs of corruption.

###Available if:
<li>ruler has personality is embezzler_personality</li>

###Efects:<ul><li>highlight = yes</li><li>add prestige = 5</li></ul>

___
##Let our [Root.Monarch.GetTitle] replace certain high-ranking officials.

###Available if:
<li>ruler has personality ancestor:</li><ul><li>key is incorruptible</li></ul>

###Efects:<ul><li>highlight = yes</li><li>add adm power = -25</li><li>If has country flag is [tyrant_system_initialized](../flags/tyrant_system_initialized.md):</li><ul><li>increase tyrant benevolent 1 = yes</li></ul></ul>
