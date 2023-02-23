#Information
 - Title: Orenkoraim Seeks Aid against Ameion
 - ID: flavor_ameion.42
#Description
Orenkoraim Seeks Aid against Ameion
#Options

___
##They shall have our aid, empires are a Cannorian buisness.

###AI weighting:
AI weights this option at 20
 - Multiplied by 5 if is enemy is FROM
 - Multiplied by 5 if is rival is FROM
 - Multiplied by 0 if is bankrupt


###Efects:<ul><li>add treasury = -400</li><li>If has global flag is [ameion_G52_c](../flags/ameion_g52_c.md):</li><ul><li>G52:</li><ul><li>the event [[From.GetName] Aid to Orenkoraim](../events/from_getname_aid_to_orenkoraim.md) happens</li></ul></ul><li>else:</li><ul><li>G00:</li><ul><li>the event [[From.GetName] Aid to Orenkoraim](../events/from_getname_aid_to_orenkoraim.md) happens</li></ul></ul></ul>

___
##Demand Concessions from Ameion.

###AI weighting:
AI weights this option at 60
 - Multiplied by 0 if is bankrupt


###Efects:<ul><li>If has global flag is [ameion_G52_c](../flags/ameion_g52_c.md):</li><ul><li>G52:</li><ul><li>the event [[From.GetName] Makes Threats](../events/from_getname_makes_threats.md) happens</li></ul></ul><li>else:</li><ul><li>G00:</li><ul><li>the event [[From.GetName] Makes Threats](../events/from_getname_makes_threats.md) happens</li></ul></ul></ul>

___
##This is not our venture.

###AI weighting:
AI weights this option at 20
 - Multiplied by 2 if has num of loans is 3
 - Multiplied by 0.25 if has 1544 has trade share has country is ROOT, and trade share has share is 3


###Efects:<ul><li>add prestige = -15</li></ul>
