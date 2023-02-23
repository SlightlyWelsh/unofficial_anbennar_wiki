#Information
 - Title: [Root.Monarch.GetName]'s Laws
 - ID: flavor_malacnar.5
#Description
[Root.Monarch.GetName]'s Laws
#Options

___
##…And you, my companions, I entrust you'll uphold these laws once I'm gone.

###AI weighting:
AI weights this option at 3


###Efects:<ul><li>change government to republic = yes</li><li>add government reform = malacnar_republic_reform</li><li>If has reform is states general reform:</li><ul><li>remove government reform = states_general_reform</li></ul></ul>

___
##…Furthermore, I am introducing you to my heir, who will rule Malacnar after my death.

###Available if:
<li>government is monarchy</li>

###AI weighting:
AI weights this option at 0
 - Multiplied by 10 if has ruler has personality is lawgiver personality, and has ruler has personality is cruel personality, and has ruler has personality is greedy personality, and has ruler has personality is malevolent personality
 - Multiplied by 0.5 if has reform is enforce privileges reform, and has reform is decentralize reform, and has reform is states general reform, and does not have legitimacy is 80


###Efects:<ul><li>If does not have ruler modifier is g32 legendary battleking; and  has calc true if has reform is enforce privileges reform, and calc true if has reform is decentralize reform, and calc true if has reform is states general reform, and calc true if has country modifier is yrw 2b, and does not have legitimacy is 80; and does not have ruler modifier is g32 bloodied battleking, and does not have ruler modifier is g32 veteran battleking; and calc true if has amount is 1:</li><ul><li>add stability = -1</li></ul><li>If does not have ruler modifier is g32 veteran battleking, and does not have ruler modifier is g32 legendary battleking; and  has calc true if has reform is enforce privileges reform, and calc true if has reform is decentralize reform, and calc true if has reform is states general reform, and calc true if has country modifier is yrw 2b, and does not have legitimacy is 80; and does not have ruler modifier is g32 bloodied battleking; and calc true if has amount is 2:</li><ul><li>custom tooltip = malacnar_really_good_idea_tooltip</li><li>hidden effect:</li><ul><li>malacnar area:</li><ul><li>spawn rebels:</li><ul><li>type = pretender_rebels</li><li>size = 2</li></ul></ul><li>add manpower = -27</li></ul></ul><li>change government to monarchy = yes</li><li>add government reform = malacnar_monarchy_reformed</li><li>define heir:</li><ul><li>age = 12</li><li>dynasty = ROOT</li><li>claim = 50</li></ul><li>If has reform is states general reform:</li><ul><li>remove government reform = states_general_reform</li></ul></ul>
