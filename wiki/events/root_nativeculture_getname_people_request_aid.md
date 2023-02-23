#Information
 - Title: [Root.NativeCulture.GetName] People Request Aid
 - ID: 3076
#Description
[Root.NativeCulture.GetName] People Request Aid
#Mean Time to Happen:
Base time = 240 months
 - Multiplied by 0.8 if does not have colonysize is 150
 - Multiplied by 0.8 if has any neighbor province is a colony, and any neighbor province has owned by is ROOT
 - Multiplied by 1.5 if has owner has num of colonies is 5
 - Multiplied by 2.0 if has owner has num of colonies is 10
 - Multiplied by 3.0 if has owner has num of colonies is 20

#Options

___
##Can the treasury bear such an expense?

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>change native size = -5</li><li>owner:</li><ul><li>If random owned province is a colony, and  has native size is 2:</li><ul><li>change native size = -2</li></ul><li>country gets the modifier "disregard_natives" for 2 years</li></ul></ul>

___
##Give them everything they need and more!

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>owner:</li><ul><li>add treasury = -40</li><li>country gets the modifier "aid_natives" for 2 years</li></ul></ul>
