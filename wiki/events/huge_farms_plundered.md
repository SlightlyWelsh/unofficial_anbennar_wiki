#Information
 - Title: Huge Farms Plundered!
 - ID: blorc.112
#Description
Huge Farms Plundered!
#Options

___
##This is for our capital!

###Available if:
<li>capital scope:</li><ul><li>province group is hold_province</li><li>Any of the following:</li><ul><li>trade goods is fungi</li><li>trade goods  is livestock</li><li>trade goods   is salt</li></ul><li>None of the following:</li><ul><li>has province modifier blorc_hold_farm</li></ul></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>event target:blorc military academy hold event target:</li><ul><li>remove province modifier = hold_farm_2</li><li>remove province modifier = hold_farm</li></ul><li>capital scope:</li><ul><li>add permanent province modifier:</li><ul><li>name = blorc_hold_farm</li><li>duration = -1</li></ul></ul><li>add adm power = -100</li><li>add treasury = -500</li></ul>

___
##Good news!

###Available if:
<li>event target:blorc military academy hold event target:</li><ul><li>has province modifier hold_farm</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>event target:blorc military academy hold event target:</li><ul><li>remove province modifier = hold_farm</li></ul><li>add yearly manpower = 0.5</li><li>add treasury = 500</li></ul>

___
##Good news!

###Available if:
<li>event target:blorc military academy hold event target:</li><ul><li>has province modifier hold_farm_2</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>event target:blorc military academy hold event target:</li><ul><li>remove province modifier = hold_farm_2</li></ul><li>add yearly manpower = 1</li><li>add treasury = 1000</li></ul>
