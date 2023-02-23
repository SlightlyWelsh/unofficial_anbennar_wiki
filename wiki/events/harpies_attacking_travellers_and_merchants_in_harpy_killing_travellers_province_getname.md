#Information
 - Title: Harpies Attacking Travellers and Merchants in [harpy_killing_travellers_province.GetName]
 - ID: harpy_tolerance_events.8
#Description
Harpies Attacking Travellers and Merchants in [harpy_killing_travellers_province.GetName]
#Options

___
##Appeasement must work

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.5 if does not have years of income is 0.4
 - Multiplied by 0.8 if does not have years of income is 0.8
 - Multiplied by 0.5 if has wants to decrease tolerance harpy is yes


###Efects:<ul><li>add years of income = -0.4</li><li>small increase of harpy tolerance effect = yes</li><li>event target:harpy killing travellers province:</li><ul><li>add province modifier:</li><ul><li>name = harpy_killing_travellers</li><li>duration = 365</li></ul></ul></ul>

___
##Some patrols will discourage them

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.8 if has wants to increase tolerance harpy is yes


###Efects:<ul><li>add mil power = -25</li><li>small decrease of harpy tolerance effect = yes</li><li>event target:harpy killing travellers province:</li><ul><li>add province modifier:</li><ul><li>name = harpy_killing_travellers</li><li>duration = 1825</li></ul></ul></ul>

___
##Build watchtowers along the roads

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.5 if has wants to increase tolerance harpy is yes
 - Multiplied by 0.5 if does not have years of income is 0.4
 - Multiplied by 0.8 if does not have years of income is 0.8


###Efects:<ul><li>add mil power = -50</li><li>add years of income = -0.4</li><li>medium decrease of harpy tolerance effect = yes</li></ul>

___
##We must avenge all those who were attacked

###Available if:
<li>Any of the following:</li><ul><li>ruler has personality is malevolent_personality</li><li>ruler has personality  is cruel_personality</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.1 if has wants to increase tolerance harpy is yes
 - Multiplied by 0.5 if does not have years of income is 0.4
 - Multiplied by 0.8 if does not have years of income is 0.8
 - Multiplied by 0.5 if does not have manpower percentage is 0.8


###Efects:<ul><li>highlight = yes</li><li>add mil power = -50</li><li>If has max manpower is 10:</li><ul><li>add manpower = -1</li></ul><li>else:</li><ul><li>add yearly manpower = -1</li></ul><li>add years of income = 0.4</li><li>largest decrease of harpy tolerance effect = yes</li><li>event target:harpy killing travellers province:</li><ul><li>remove harpy minority size effect = yes</li></ul></ul>
