#Information
 - Title: Training under the Blade Stewards
 - ID: flavor_blademarches.6
#Description
Training under the Blade Stewards
#Options

___
##A few sword lessons a day should help!

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>add mil power = -50</li><li>add dip power = -50</li><li>add adm power = -50</li><li>add ruler modifier:</li><ul><li>name = in_training_calindal_casual</li><li>duration = -1</li></ul><li>custom tooltip = calindal_training_tooltip</li><li>hidden effect:</li><ul><li>set ruler flag [easy_training_calindal](../flags/easy_training_calindal.md)</li></ul></ul>

___
##A balance of train and rule

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>add mil power = -100</li><li>add dip power = -100</li><li>add adm power = -100</li><li>add ruler modifier:</li><ul><li>name = in_training_calindal_normal</li><li>duration = -1</li></ul><li>custom tooltip = calindal_training_tooltip</li><li>hidden effect:</li><ul><li>set ruler flag [normal_training_calindal](../flags/normal_training_calindal.md)</li></ul></ul>

___
##I must train and live as a Blade Steward.

###AI weighting:
AI weights this option at 50


###One of the following randomly happens:
Outcome 1:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>decrease ruler dip effect = yes</li></ul>
Outcome 2:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>decrease ruler adm effect = yes</li></ul>

###Efects:<ul><li>add mil power = -100</li><li>add dip power = -100</li><li>add adm power = -100</li><li>add ruler modifier:</li><ul><li>name = in_training_calindal_monastic</li><li>duration = -1</li></ul><li>custom tooltip = calindal_training_tooltip</li><li>hidden effect:</li><ul><li>set ruler flag [hard_training_calindal](../flags/hard_training_calindal.md)</li></ul></ul>

___
##Only complete adherance will do.

###Available if:
<li>ruler has personality is strict_personality</li>

###AI weighting:
AI weights this option at 5000


###Efects:<ul><li>highlight = yes</li><li>add ruler modifier:</li><ul><li>name = in_training_calindal_monastic</li><li>duration = -1</li></ul><li>add mil power = -150</li><li>add dip power = -150</li><li>add adm power = -150</li><li>custom tooltip = calindal_training_tooltip</li><li>hidden effect:</li><ul><li>set ruler flag [super_training_calindal](../flags/super_training_calindal.md)</li></ul></ul>
