#Information
 - Title: [From.GetName] Demands Fealty
 - ID: flavor_ameion.36
#Description
[From.GetName] Demands Fealty
#Options

___
##Kneel, there is little shame in being ruled by our kin.

###AI weighting:
AI weights this option at 100
 - Multiplied by 0.75 if has num of owned provinces with has value is 7
 - Multiplied by 0.666 if has num of owned provinces with has value is 12
 - Multiplied by 0.5 if has num of owned provinces with has value is 20
 - Multiplied by 0 if is a great power, and has tag is H22


###Efects:<ul><li>If has global flag is [ameion_G52_s](../flags/ameion_g52_s.md):</li><ul><li>G52:</li><ul><li>the event [[From.GetName] Accepts Fealty](../events/from_getname_accepts_fealty.md) happens</li></ul></ul><li>else:</li><ul><li>G00:</li><ul><li>the event [[From.GetName] Accepts Fealty](../events/from_getname_accepts_fealty.md) happens</li></ul></ul></ul>

___
##We may fall, but we shall fall standing.

###AI weighting:
AI weights this option at 1
 - Multiplied by 0 if does not have num of owned provinces with has value is 7; and does not have tag is H22
 - Multiplied by 25 if has num of owned provinces with has value is 7
 - Multiplied by 2 if has num of owned provinces with has value is 12
 - Multiplied by 1.333 if has num of owned provinces with has value is 20


###Efects:<ul><li>If has global flag is [ameion_G52_s](../flags/ameion_g52_s.md):</li><ul><li>G52:</li><ul><li>the event [[From.GetName] Rejects Fealty](../events/from_getname_rejects_fealty.md) happens</li></ul></ul><li>else:</li><ul><li>G00:</li><ul><li>the event [[From.GetName] Rejects Fealty](../events/from_getname_rejects_fealty.md) happens</li></ul></ul></ul>
