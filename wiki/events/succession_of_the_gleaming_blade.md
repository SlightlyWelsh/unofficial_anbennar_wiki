#Information
 - Title: Succession of the Gleaming Blade
 - ID: flavor_blademarches.3
#Description
Succession of the Gleaming Blade
#Options

___
##Take the Test

###Available if:
<li>None of the following:</li><ul><li>has country flag [calindal_revolt_success](../flags/calindal_revolt_success.md)</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 2 if has mil is 3, and does not have mil is 4
 - Multiplied by 4 if has mil is 4, and does not have mil is 5
 - Multiplied by 6 if has mil is 5, and does not have mil is 6
 - Multiplied by 100 if has mil is 6
 - Multiplied by 1.5 if has ruler has personality is righteous personality
 - Multiplied by 1.5 if has ruler has personality is inspiring leader personality
 - Multiplied by 1.5 if has ruler has personality is conqueror personality
 - Multiplied by 5 if has ruler has personality is obsessive perfectionist personality


###Efects:<ul><li>hidden effect:</li><ul><li>the event ˻flavor_blademarches.4˼ happens</li></ul><li>custom tooltip = wield_the_blade_tooltip</li></ul>

___
##Find a Bladechosen

###Available if:
<li>None of the following:</li><ul><li>has country flag [calindal_revolt_success](../flags/calindal_revolt_success.md)</li></ul>

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>hidden effect:</li><ul><li>the event ˻flavor_blademarches.8˼ happens</li></ul><li>custom tooltip = nominate_bladechosen_tooltip</li></ul>

___
##Train with the Blade Stewards

###Available if:
<li>None of the following:</li><ul><li>mil is at least 6</li></ul><li>NOT:</li><ul><li>has ruler flag [trained_calindal](../flags/trained_calindal.md)</li></ul><li>NOT:</li><ul><li>has country flag [calindal_revolt_success](../flags/calindal_revolt_success.md)</li></ul>

###AI weighting:
AI weights this option at 10
 - Multiplied by 20 if has mil is 1, and does not have mil is 2
 - Multiplied by 10 if has mil is 2, and does not have mil is 3
 - Multiplied by 5 if has mil is 3, and does not have mil is 4


###Efects:<ul><li>the event ˻flavor_blademarches.6˼ happens</li><li>hidden effect:</li><ul><li>set ruler flag [trained_calindal](../flags/trained_calindal.md)</li></ul></ul>

___
##As a former Bladechosen, [Root.Monarch.GetName] is already worthy.

###Available if:
<li>has country flag [calindal_revolt_success](../flags/calindal_revolt_success.md)</li>

###AI weighting:
AI weights this option at 10


###Efects:<ul><li>add ruler modifier:</li><ul><li>name = wielding_calindal</li><li>duration = -1</li></ul><li>increase legitimacy large effect = yes</li><li>reduce stability or adm power = yes</li><li>hidden effect:</li><ul><li>set ruler flag [wield_the_sword](../flags/wield_the_sword.md)</li></ul><li>hidden effect:</li><ul><li>clr country flag [calindal_revolt_success](../flags/calindal_revolt_success.md)</li></ul></ul>
