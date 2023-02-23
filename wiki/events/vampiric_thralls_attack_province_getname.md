#Information
 - Title: Vampiric Thralls attack [province.GetName]!
 - ID: disaster_vampire_masquerade.2
#Description
Vampiric Thralls attack [province.GetName]!
#Mean Time to Happen:
Base time = 1 days
 - Multiplied by 2.5 if has country flag is [wipe_vampire_out](../flags/wipe_vampire_out.md)

#Options

___
##Damn them!

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>goto = province</li><li>If has total development is 500:</li><ul><li>event target:province:</li><ul><li>spawn rebels:</li><ul><li>type = vampires_thralls</li><li>size = 2</li></ul></ul></ul><li>else:</li><ul><li>event target:province:</li><ul><li>spawn rebels:</li><ul><li>type = vampires_thralls</li><li>size = 1</li></ul></ul></ul></ul>
