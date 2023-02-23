#Information
 - Title: Acolyte Interactions
 - ID: black_demesne.6
#Description
Acolyte Interactions
#Options

___
##Go Back

###AI weighting:
AI weights this option at 40


___
##Damnation

###Available if:
<li>event target:country:</li><ul><li>None of the following:</li><ul><li>has ruler flag [damned_acolyte](../flags/damned_acolyte.md)</li></ul></ul>

###AI weighting:
AI weights this option at 40


###Efects:<ul><li>event target:country:</li><ul><li>hidden effect:</li><ul><li>set ruler flag [damned_acolyte](../flags/damned_acolyte.md)</li></ul><li>add liberty desire = 33</li></ul><li>custom tooltip = acolyte_damnation_tooltip</li></ul>

___
##Remove Damnation

###Available if:
<li>event target:country:</li><ul><li>has ruler flag [damned_acolyte](../flags/damned_acolyte.md)</li></ul>

###AI weighting:
AI weights this option at 40


###Efects:<ul><li>event target:country:</li><ul><li>hidden effect:</li><ul><li>clr ruler flag [damned_acolyte](../flags/damned_acolyte.md)</li></ul><li>add liberty desire = -5</li></ul><li>custom tooltip = acolyte_damnation_remove_tooltip</li></ul>

___
##Shun [country.GetName]

###Available if:
<li>adm power is at least 50</li><li>mil power is at least 50</li><li>dip power is at least 50</li>

###AI weighting:
AI weights this option at 40


###Efects:<ul><li>event target:country:</li><ul><li>hidden effect:</li><ul><li>multiply variable:</li><ul><li>aInfluence = 0.9</li></ul></ul><li>add liberty desire = 20</li></ul><li>add adm power = -75</li><li>add mil power = -75</li><li>add dip power = -75</li><li>custom tooltip = acolyte_shun_tooltip</li></ul>

___
##Favour [country.GetName]

###Available if:
<li>adm power is at least 50</li><li>mil power is at least 50</li><li>dip power is at least 50</li>

###AI weighting:
AI weights this option at 40


###Efects:<ul><li>event target:country:</li><ul><li>hidden effect:</li><ul><li>multiply variable:</li><ul><li>aInfluence = 1.1</li></ul></ul><li>add liberty desire = -5</li></ul><li>add adm power = -75</li><li>add mil power = -75</li><li>add dip power = -75</li><li>custom tooltip = acolyte_favour_tooltip</li></ul>
