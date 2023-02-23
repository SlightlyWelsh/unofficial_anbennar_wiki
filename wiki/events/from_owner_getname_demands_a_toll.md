#Information
 - Title: [From.Owner.GetName] Demands a Toll
 - ID: ynn_barges.3
#Description
[From.Owner.GetName] Demands a Toll
#Options

___
##We'll just open up the dam ourselves

###Available if:
<li>FROM:</li><ul><li>controlled by is this nation</li></ul>

###AI weighting:
AI weights this option at 1000


###Efects:<ul><li>highlight = yes</li><li>add prestige = 5</li><li>hidden effect:</li><ul><li>the event [Missing localisation: ynn_barges_100_t](../events/missing_localisation_ynn_barges_100_t.md) happens</li></ul><li>hidden effect:</li><ul><li>If does not have FROM has owned by is ROOT:</li><ul><li>FROM:</li><ul><li>owner:</li><ul><li>the event [[From.GetName] Forces their Way Through](../events/from_getname_forces_their_way_through.md) happens</li></ul></ul></ul></ul></ul>

___
##Very well

###AI weighting:
AI weights this option at 80
 - Multiplied by 2 if has country flag is [big_barges](../flags/big_barges.md)
 - Multiplied by 0.5 if has num of loans is 2
 - Multiplied by 0.5 if has num of loans is 4
 - Multiplied by 0.25 if is bankrupt
 - Multiplied by 0.1 if has ruler has personality is greedy personality


###Efects:<ul><li>add treasury = -50</li><li>hidden effect:</li><ul><li>FROM:</li><ul><li>fire province event [ynn_barges.4](ynn_barges.4_slug) in 10 to 5 days</li></ul></ul></ul>

___
##Sink the barge

###AI weighting:
AI weights this option at 20


###Efects:<ul><li>add prestige = -5</li><li>hidden effect:</li><ul><li>FROM:</li><ul><li>fire province event [ynn_barges.5](ynn_barges.5_slug) in 10 to 5 days</li></ul></ul></ul>
