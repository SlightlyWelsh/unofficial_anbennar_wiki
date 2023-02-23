#Information
 - Title: Missing localisation: magic_duel_3_t
 - ID: magic_duel.3
#Description

#Options

___
##Missing localisation: magic_duel_3_a

###Available if:
<li>event target:defender:</li><ul><li>check variable:</li><ul><li>current hp is at least 0</li></ul></ul><li>event target:attacker:</li><ul><li>check variable:</li><ul><li>current hp is at least 0</li></ul></ul>

###AI weighting:
AI weights this option at 10


###Efects:<ul><li>If has event target:attacker is not controlled by the AI; and  has event target:defender is controlled by the AI:</li><ul><li>event target:attacker:</li><ul><li>the event ˻magic_duel.1˼ happens</li></ul></ul><li>Else if has event target:attacker is controlled by the AI; and  has event target:defender is not controlled by the AI:</li><ul><li>event target:defender:</li><ul><li>the event ˻magic_duel.1˼ happens</li></ul></ul><li>else:</li><ul><li>event target:attacker:</li><ul><li>the event ˻magic_duel.1˼ happens</li></ul><li>event target:defender:</li><ul><li>the event ˻magic_duel.1˼ happens</li></ul></ul></ul>

___
##Missing localisation: magic_duel_3_b

###Available if:
<li>event target:attacker:</li><ul><li>check variable:</li><ul><li>current hp is at least 0</li></ul></ul><li>event target:defender:</li><ul><li>None of the following:</li><ul><li>check variable:</li><ul><li>current hp is at least 0</li></ul></ul></ul>

###AI weighting:
AI weights this option at 10


###Efects:<ul><li>If has event target:attacker has ruler flag is [fighting_NPC](../flags/fighting_npc.md):</li><ul><li>trigger switch:</li><ul><li>on trigger = has_ruler_flag</li><li>npc jorgurem:</li><ul><li>event target:attacker:</li><ul><li>the event ˻black_demesne.8˼ happens</li><li>clr ruler flag [npc_jorgurem](../flags/npc_jorgurem.md)</li><li>clr ruler flag [fighting_NPC](../flags/fighting_npc.md)</li></ul></ul></ul><li>event target:defender:</li><ul><li>magic duel npc clear magical flag = yes</li></ul></ul><li>else:</li><ul><li>event target:attacker:</li><ul><li>the event ˻magic_duel.4˼ happens</li></ul><li>event target:defender:</li><ul><li>the event ˻magic_duel.6˼ happens</li></ul></ul><li>event target:attacker:</li><ul><li>clr ruler flag [in_magic_duel](../flags/in_magic_duel.md)</li><li>clr magic duel printing flag = yes</li></ul><li>event target:defender:</li><ul><li>clr ruler flag [in_magic_duel](../flags/in_magic_duel.md)</li><li>clr magic duel printing flag = yes</li></ul></ul>

___
##Missing localisation: magic_duel_3_c

###Available if:
<li>event target:defender:</li><ul><li>check variable:</li><ul><li>current hp is at least 0</li></ul></ul><li>event target:attacker:</li><ul><li>None of the following:</li><ul><li>check variable:</li><ul><li>current hp is at least 0</li></ul></ul></ul>

###AI weighting:
AI weights this option at 10


###Efects:<ul><li>event target:attacker:</li><ul><li>clr ruler flag [in_magic_duel](../flags/in_magic_duel.md)</li><li>clr magic duel printing flag = yes</li></ul><li>event target:defender:</li><ul><li>clr ruler flag [in_magic_duel](../flags/in_magic_duel.md)</li><li>clr magic duel printing flag = yes</li></ul><li>If has event target:attacker has ruler flag is [fighting_NPC](../flags/fighting_npc.md):</li><ul><li>trigger switch:</li><ul><li>on trigger = has_ruler_flag</li><li>npc jorgurem:</li><ul><li>event target:attacker:</li><ul><li>the event ˻black_demesne.9˼ happens</li><li>clr ruler flag [npc_jorgurem](../flags/npc_jorgurem.md)</li><li>clr ruler flag [fighting_NPC](../flags/fighting_npc.md)</li></ul></ul></ul><li>event target:defender:</li><ul><li>magic duel npc clear magical flag = yes</li></ul></ul><li>else:</li><ul><li>event target:defender:</li><ul><li>the event ˻magic_duel.4˼ happens</li></ul><li>event target:attacker:</li><ul><li>the event ˻magic_duel.6˼ happens</li></ul></ul></ul>

___
##Missing localisation: magic_duel_3_e

###Available if:
<li>event target:attacker:</li><ul><li>None of the following:</li><ul><li>check variable:</li><ul><li>current hp is at least 0</li></ul></ul></ul><li>event target:defender:</li><ul><li>None of the following:</li><ul><li>check variable:</li><ul><li>current hp is at least 0</li></ul></ul></ul>

###AI weighting:
AI weights this option at 10


###Efects:<ul><li>event target:attacker:</li><ul><li>the event ˻magic_duel.5˼ happens</li></ul><li>event target:defender:</li><ul><li>the event ˻magic_duel.5˼ happens</li></ul><li>event target:attacker:</li><ul><li>clr ruler flag [in_magic_duel](../flags/in_magic_duel.md)</li><li>clr magic duel printing flag = yes</li></ul><li>event target:defender:</li><ul><li>clr ruler flag [in_magic_duel](../flags/in_magic_duel.md)</li><li>clr magic duel printing flag = yes</li></ul></ul>
