#Information
 - Title: The Raja condemns our expansion
 - ID: rahenraj.1008
#Description
The Raja condemns our expansion
#Options

___
##We are but subjects of the throne

###AI weighting:
AI weights this option at 2


###Efects:<ul><li>remove raj mandate = yes</li><li>country gets the modifier raj_mandate_territorial_limits for 10 years</li><li>custom tooltip = desc_raj_mandate_territorial_limits</li><li>return all uncored provinces:</li><ul><li>release nations = yes</li></ul><li>add opinion:</li><ul><li>who = FROM</li><li>modifier = rahen_raja_pronounced_undesired_mandate</li></ul></ul>

___
##Perhaps a deal can be struck

###AI weighting:
AI weights this option at 2
 - Multiplied by 0 if has num of loans is 1


###Efects:<ul><li>transfer uncored province value to overlord = yes</li><li>add adm power = -10</li><li>add dip power = -10</li><li>add mil power = -10</li><li>remove raj mandate = yes</li><li>country gets the modifier raj_mandate_territorial_limits for 10 years</li><li>custom tooltip = desc_raj_mandate_territorial_limits</li><li>add opinion:</li><ul><li>who = FROM</li><li>modifier = rahen_raja_pronounced_undesired_mandate</li></ul><li>hidden effect:</li><ul><li>FROM:</li><ul><li>add adm power = 10</li><li>add dip power = 10</li><li>add mil power = 10</li></ul></ul></ul>

___
##We clearly need a new Raja

###AI weighting:
AI weights this option at 1
 - Multiplied by 0 if has opinion has who is FROM, and has opinion has value is 100
 - Multiplied by 5 if has army size is FROM


###Efects:<ul><li>If does not have range is ROOT; and does not have core is ROOT:</li><ul><li>4411:</li><ul><li>add core = ROOT</li></ul></ul><li>declare war with cb:</li><ul><li>who = FROM</li><li>casus belli = cb_prabhi_claim_raj</li></ul><li>add stability = -3</li></ul>
