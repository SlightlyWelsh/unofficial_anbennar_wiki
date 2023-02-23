#Information
 - Title: [xia_duel_instigator.GetName] Demands a Duel!
 - ID: xia_summit.11
#Description
[xia_duel_instigator.GetName] Demands a Duel!
#Options

___
##Make the master apologize.

###AI weighting:
AI weights this option at 20


###Efects:<ul><li>add prestige = -20</li><li>event target:xia duel instigator:</li><ul><li>the event [[xia_duel_target.GetName] Apologizes](../events/xia_duel_target_getname_apologizes.md) happens</li></ul></ul>

___
##Accept the duel.

###AI weighting:
AI weights this option at 80
 - Multiplied by 0 if has ruler has personality is craven personality
 - Multiplied by 5 if has ruler has personality is bold fighter personality, and has ruler has personality is just personality, and has ruler has personality is inspiring leader personality


###Efects:<ul><li>custom tooltip = xia_duel_accept_tt</li><li>overlord:</li><ul><li>the event [Xiaken Request Permission for Righteous Combat](../events/xiaken_request_permission_for_righteous_combat.md) happens</li></ul></ul>
