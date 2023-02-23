#Information
 - Title: Bladechosen Revolt
 - ID: flavor_blademarches.9
#Description
Bladechosen Revolt
#Mean Time to Happen:
Base time = 100 years
 - Multiplied by 0.5 if has ruler modifier is blinded by the sword
 - Multiplied by 0.2 if has mil is 0, and does not have mil is 1
 - Multiplied by 0.35 if has mil is 1, and does not have mil is 2
 - Multiplied by 0.55 if has mil is 2, and does not have mil is 3
 - Multiplied by 0.75 if has mil is 3, and does not have mil is 4
 - Multiplied by 0.9 if has mil is 4, and does not have mil is 5
 - Multiplied by 0.9 if does not have legitimacy is 50
 - Multiplied by 0.8 if does not have legitimacy is 20
 - Multiplied by 2 if has ruler has personality is just personality
 - Multiplied by 2 if has ruler has personality is righteous personality
 - Multiplied by 0.5 if has ruler has personality is malevolent personality
 - Multiplied by 0.5 if has ruler has personality is cruel personality
 - Multiplied by 0.5 if has ruler has personality is craven personality

#Options

___
##Bladechosen or not, you are not worthy of the blade!

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>remove country modifier = has_bladechosen</li><li>reduce stability or adm power = yes</li><li>capital scope:</li><ul><li>If has owner has land force is 150:</li><ul><li>spawn rebels:</li><ul><li>type = pretender_rebels</li><li>size = 7</li></ul></ul><li>Else if has owner has land force is 130:</li><ul><li>spawn rebels:</li><ul><li>type = pretender_rebels</li><li>size = 6</li></ul></ul><li>Else if has owner has land force is 100:</li><ul><li>spawn rebels:</li><ul><li>type = pretender_rebels</li><li>size = 5</li></ul></ul><li>Else if has owner has land force is 70:</li><ul><li>spawn rebels:</li><ul><li>type = pretender_rebels</li><li>size = 4</li></ul></ul><li>Else if has owner has land force is 50:</li><ul><li>spawn rebels:</li><ul><li>type = pretender_rebels</li><li>size = 3</li></ul></ul><li>else:</li><ul><li>spawn rebels:</li><ul><li>type = pretender_rebels</li><li>size = 2</li></ul></ul></ul><li>hidden effect:</li><ul><li>set ruler flag [calindal_revolt](../flags/calindal_revolt.md)</li></ul></ul>
