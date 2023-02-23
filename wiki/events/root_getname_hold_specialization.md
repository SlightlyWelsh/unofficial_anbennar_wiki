#Information
 - Title: [Root.GetName] Hold Specialization
 - ID: diggy.27
#Description
[Root.GetName] Hold Specialization
#Mean Time to Happen:
Base time = 10 years

#Options

___
##Foundry Infrastructure

###Available if:
<li>Any of the following:</li><ul><li>trade goods is iron</li><li>trade goods  is damestear</li><li>trade goods   is mithril</li><li>trade goods    is copper</li><li>trade goods     is coal</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>goto = ROOT</li><li>add permanent province modifier:</li><ul><li>name = hold_foundry</li><li>duration = -1</li></ul></ul>

___
##Metropolis Infrastructure

###Available if:
<li>Any of the following:</li><ul><li>trade goods is glass</li><li>trade goods  is cloth</li><li>trade goods   is mithril</li><li>trade goods    is gold</li><li>trade goods     is paper</li><li>trade goods      is wine</li><li>trade goods       is precursor_relics</li><li>trade goods        is gems</li><li>trade goods         is incense</li><li>trade goods          is salt</li><li>base tax is at least 30</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>goto = ROOT</li><li>add permanent province modifier:</li><ul><li>name = hold_city</li><li>duration = -1</li></ul></ul>

___
##Artisan Infrastructure

###Available if:
<li>Any of the following:</li><ul><li>trade goods is gems</li><li>trade goods  is glass</li><li>trade goods   is wine</li><li>trade goods    is gold</li><li>trade goods     is mithril</li><li>trade goods      is precursor_relics</li><li>trade goods       is incense</li><li>trade goods        is tropical_wood</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>goto = ROOT</li><li>add permanent province modifier:</li><ul><li>name = hold_artisan</li><li>duration = -1</li></ul></ul>

___
##Vertical Farm Infrastructure

###Available if:
<li>Any of the following:</li><ul><li>trade goods is fungi</li><li>trade goods  is serpentbloom</li><li>trade goods   is livestock</li><li>trade goods    is salt</li><li>trade goods     is slaves</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>goto = ROOT</li><li>add permanent province modifier:</li><ul><li>name = hold_farm</li><li>duration = -1</li></ul></ul>

___
##Military Infrastructure

###Available if:
<li>Any of the following:</li><ul><li>trade goods is iron</li><li>trade goods  is copper</li><li>trade goods   is paper</li><li>trade goods    is mithril</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>goto = ROOT</li><li>add permanent province modifier:</li><ul><li>name = hold_military</li><li>duration = -1</li></ul></ul>
