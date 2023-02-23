#Information
 - Title: Anti Half-Elves Pogroms
 - ID: flavor_azka_sur.17
#Description
Anti Half-Elves Pogroms
#Options

___
##We could turn a blind eye

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>custom tooltip = nsc_much_chosen_role_up_tt</li><li>add incident variable value:</li><ul><li>incident = incident_half_a_king</li><li>value = 2</li></ul><li>medium decrease of half elven tolerance effect = yes</li></ul>

___
##We have to protect them!

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>custom tooltip = nsc_chosen_role_down_tt</li><li>add incident variable value:</li><ul><li>incident = incident_half_a_king</li><li>value = -1</li></ul><li>event target:target province 1:</li><ul><li>spawn rebels:</li><ul><li>size = 1</li><li>type = religious_rebels</li></ul></ul><li>event target:target province 2:</li><ul><li>spawn rebels:</li><ul><li>size = 1</li><li>type = religious_rebels</li></ul></ul><li>event target:target province 3:</li><ul><li>spawn rebels:</li><ul><li>size = 1</li><li>type = religious_rebels</li></ul></ul><li>custom tooltip = azka_sur_clergy_angered_tt</li><li>hidden effect:</li><ul><li>change variable:</li><ul><li>clergyPissiness = 1</li></ul></ul></ul>
