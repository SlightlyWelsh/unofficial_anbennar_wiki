#Information
 - Title: Wyvern Disrupts Caravans
 - ID: aw_wyvern.201
#Description
Wyvern Disrupts Caravans
#Options

___
##Watch the skies.

###Available if:
<li>event target:nested wyvern target:</li><ul><li>owned by is event_target:nested_wyvern_origin_country</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>event target:nested wyvern target:</li><ul><li>add devastation = 25</li><li>add province modifier:</li><ul><li>name = aw_wyvern_attacks_on_caravans</li><li>duration = 1825</li></ul></ul></ul>

___
##Unfortunate for their trade.

###Available if:
<li>event target:nested wyvern target:</li><ul><li>None of the following:</li><ul><li>owned by is event_target:nested_wyvern_origin_country</li></ul></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>event target:nested wyvern target:</li><ul><li>fire province event [aw_wyvern.2001](aw_wyvern.2001_slug) in 7 days</li></ul></ul>
