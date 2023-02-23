#Information
 - Title: [halfling_rebels_target.GetName] Revolts!
 - ID: flavor_smallcountry.2
#Description
[halfling_rebels_target.GetName] Revolts!
#Options

___
##Suppress the rebels!

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>event target:halfling rebels target:</li><ul><li>set province flag [halfling_revolt](../flags/halfling_revolt.md)</li><li>spawn rebels:</li><ul><li>type = nationalist_rebels</li><li>size = 1</li><li>friend = A97</li></ul></ul></ul>

___
##Give local concessions

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>event target:halfling rebels target:</li><ul><li>add local autonomy = 100</li><li>set province flag [no_halfling_revolt](../flags/no_halfling_revolt.md)</li></ul></ul>
