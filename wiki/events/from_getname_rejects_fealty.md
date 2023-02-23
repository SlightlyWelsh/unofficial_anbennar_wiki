#Information
 - Title: [From.GetName] Rejects Fealty
 - ID: flavor_ameion.38
#Description
[From.GetName] Rejects Fealty
#Options

___
##We will make them kneel.

###Available if:
<li>None of the following:</li><ul><li>war with is event_target:G52_kheion</li></ul>

###Efects:<ul><li>declare war with cb:</li><ul><li>who = FROM</li><li>casus belli = cb_vassalize_mission</li></ul></ul>

___
##We will topple them, then raise them to their knees.

###Efects:<ul><li>custom tooltip = ameion_kheion_claims</li><li>hidden effect:</li><ul><li>FROM:</li><ul><li>every owned province:</li><ul><li>add claim = ROOT</li></ul></ul></ul><li>If does not have war with is FROM:</li><ul><li>declare war with cb:</li><ul><li>who = FROM</li><li>casus belli = cb_imperial</li></ul></ul></ul>
