#Information
 - Title: Wyvern Attacks Peasantry
 - ID: aw_wyvern.200
#Description
Wyvern Attacks Peasantry
#Options

___
##Damn that wyvern!

###Available if:
<li>event target:nested wyvern target:</li><ul><li>owned by is event_target:nested_wyvern_origin_country</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>goto = nested_wyvern_target</li><li>event target:nested wyvern target:</li><ul><li>add devastation = 50</li></ul></ul>

___
##Send our regards

###Available if:
<li>event target:nested wyvern target:</li><ul><li>None of the following:</li><ul><li>owned by is event_target:nested_wyvern_origin_country</li></ul></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>goto = nested_wyvern_target</li><li>event target:nested wyvern target:</li><ul><li>fire province event [aw_wyvern.2000](aw_wyvern.2000_slug) in 7 days</li></ul></ul>
