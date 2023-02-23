#Information
 - Title: The Wounded Elf
 - ID: flavor_lodhum.10
#Description
The Wounded Elf
#Options

___
##We will not allow our ancestral enemy to wipe out another civilization!

###Available if:
<li>I33:</li><ul><li>exists</li></ul><li>None of the following:</li><ul><li>exists is Cyranvar</li></ul>

###AI weighting:
AI weights this option at 5


###Efects:<ul><li>hidden effect:</li><ul><li>I33:</li><ul><li>If is at war, and  is controlled by the AI:</li><ul><li>If every known country has war with is I33, and  is controlled by the AI:</li><ul><li>white peace = I33</li></ul></ul></ul></ul><li>I33:</li><ul><li>every owned province:</li><ul><li>discover country = ROOT</li></ul></ul><li>hidden effect:</li><ul><li>every owned province:</li><ul><li>discover country = I33</li></ul></ul></ul>

___
##His vengeance is our vengeance, these monsters will know our anger!

###Available if:
<li>I33:</li><ul><li>does not exist</li></ul><li>None of the following:</li><ul><li>exists is Cyranvar</li></ul><li>NOT:</li><ul><li>Any of the following:</li><ul><li>lonfarch area:</li><ul><li>owner:</li><ul><li>culture is elven is yes</li></ul></ul><li>ayeth area:</li><ul><li>owner:</li><ul><li>culture is elven is yes</li></ul></ul></ul></ul>

###AI weighting:
AI weights this option at 5


###Efects:<ul><li>lonfarch area:</li><ul><li>add core = ROOT</li><li>discover country = ROOT</li></ul><li>ayeth area:</li><ul><li>add core = ROOT</li><li>discover country = ROOT</li></ul><li>custom tooltip = lodhum_no_keep_lands_tooltip</li></ul>

___
##Then we'll have to convince them to give it back to your people.

###Available if:
<li>I33:</li><ul><li>does not exist</li></ul><li>None of the following:</li><ul><li>exists is Cyranvar</li></ul><li>Any of the following:</li><ul><li>lonfarch area:</li><ul><li>owner:</li><ul><li>culture is elven is yes</li></ul></ul><li>ayeth area:</li><ul><li>owner:</li><ul><li>culture is elven is yes</li></ul></ul></ul>

###AI weighting:
AI weights this option at 5


###Efects:<ul><li>custom tooltip = flavor_lodhum.10.tooltip</li><li>If lonfarch area has owner has culture is elven is yes:</li><ul><li>add core = I33</li><li>cede province = I33</li></ul><li>If ayeth area has owner has culture is elven is yes:</li><ul><li>add core = I33</li><li>cede province = I33</li></ul></ul>

___
##So they have united against the orcish threat?

###Available if:
<li>exists is Cyranvar</li>

###AI weighting:
AI weights this option at 5


###Efects:<ul><li>hidden effect:</li><ul><li>I45:</li><ul><li>every owned province:</li><ul><li>discover country = ROOT</li></ul></ul></ul><li>hidden effect:</li><ul><li>every owned province:</li><ul><li>discover country = I45</li></ul></ul></ul>
