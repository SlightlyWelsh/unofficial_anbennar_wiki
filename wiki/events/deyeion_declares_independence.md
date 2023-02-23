#Information
 - Title: Deyeion Declares Independence
 - ID: flavor_ameion.13
#Description
Deyeion Declares Independence
#Options

___
##To arms!

###Efects:<ul><li>If has country flag is [G52_G62_ally](../flags/g52_g62_ally.md):</li><ul><li>create alliance = G56</li><li>G62:</li><ul><li>create alliance = G56</li></ul><li>event target:G52 G56 overlord:</li><ul><li>declare war with cb:</li><ul><li>who = G56</li><li>casus belli = cb_disloyal_vassal</li></ul></ul><li>join all defensive wars of = G56</li><li>G62:</li><ul><li>join all defensive wars of = G56</li></ul></ul><li>else:</li><ul><li>G56:</li><ul><li>declare war with cb:</li><ul><li>who = event_target:G52_G56_overlord</li><li>casus belli = cb_independence_war</li></ul></ul><li>join all offensive wars of = G56</li><li>create alliance = G56</li><li>G62:</li><ul><li>join all offensive wars of = G56</li><li>create alliance = G56</li></ul></ul></ul>
