#Information
 - Title: The Elven Response
 - ID: flavor_lodhum.15
#Description
The Elven Response
#Options

___
##Then they shall feel the fury of the mountain on their heads!

###Available if:
<li>Any of the following:</li><ul><li>event target:global lodhum elf enemy 1:</li><ul><li>has country flag [denied_lodhum_friendship](../flags/denied_lodhum_friendship.md)</li></ul><li>event target:global lodhum elf enemy 2:</li><ul><li>has country flag [denied_lodhum_friendship](../flags/denied_lodhum_friendship.md)</li></ul></ul>

###AI weighting:
AI weights this option at 5


###Efects:<ul><li>If has event target:global lodhum elf enemy 1 has country flag is [denied_lodhum_friendship](../flags/denied_lodhum_friendship.md):</li><ul><li>declare war with cb:</li><ul><li>casus belli = cb_lodhum_elf_war</li><li>who = event_target:global_lodhum_elf_enemy_1</li></ul><li>custom tooltip = flavor_lodhum.15.tooltip</li></ul><li>If has event target:global lodhum elf enemy 2 has country flag is [denied_lodhum_friendship](../flags/denied_lodhum_friendship.md):</li><ul><li>declare war with cb:</li><ul><li>casus belli = cb_lodhum_elf_war</li><li>who = event_target:global_lodhum_elf_enemy_2</li></ul><li>custom tooltip = flavor_lodhum.15.tooltip</li></ul><li>set country flag [lodhum_part3_bulwar_war](../flags/lodhum_part3_bulwar_war.md)</li><li>hidden effect:</li><ul><li>F26:</li><ul><li>join all offensive wars of = ROOT</li></ul></ul></ul>

___
##Love prevails.

###Available if:
<li>event target:global lodhum elf enemy 1:</li><ul><li>has country flag [accepted_lodhum_friendship](../flags/accepted_lodhum_friendship.md)</li></ul><li>event target:global lodhum elf enemy 2:</li><ul><li>has country flag [accepted_lodhum_friendship](../flags/accepted_lodhum_friendship.md)</li></ul>

###AI weighting:
AI weights this option at 5


###Efects:<ul><li>set country flag [lodhum_part3_bulwar_peace](../flags/lodhum_part3_bulwar_peace.md)</li></ul>
