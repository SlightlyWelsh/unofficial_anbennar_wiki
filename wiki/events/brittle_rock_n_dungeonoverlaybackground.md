#Information
 - Title: Brittle Rock\n[DungeonOverlayBackground]
 - ID: diggy_dungeons.250
#Description
Brittle Rock\n[DungeonOverlayBackground]
#Options

___
##Chance it.

###Available if:
<li>always</li>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>dungeon encounter effect:</li><ul><li>base success = 60</li><li>success id = 253</li><li>base failure = 40</li><li>failure id = 252</li></ul></ul>

___
##Play it safe.

###Available if:
<li>check variable:</li><ul><li>partySupplies is at least 4</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>change party supplies:</li><ul><li>remove tooltip = yes</li><li>loss = 4</li></ul><li>set province flag [stunveigryorth_3_hammer](../flags/stunveigryorth_3_hammer.md)</li><li>dungeon encounter effect:</li><ul><li>base success = 80</li><li>success id = 253</li><li>base failure = 20</li><li>failure id = 252</li></ul></ul>
