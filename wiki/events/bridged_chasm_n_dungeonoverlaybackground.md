#Information
 - Title: Bridged Chasm\n[DungeonOverlayBackground]
 - ID: diggy_dungeons.236
#Description
Bridged Chasm\n[DungeonOverlayBackground]
#Options

___
##Just cross over the tree.

###Available if:
<li>always</li>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>dungeon encounter effect:</li><ul><li>base success = 80</li><li>success id = 239</li><li>base failure = 20</li><li>failure id = 237</li></ul></ul>

___
##Descend the chasm.

###Available if:
<li>check variable:</li><ul><li>partySupplies is at least 4</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>change party supplies:</li><ul><li>remove tooltip = yes</li><li>loss = 4</li></ul><li>set province flag [stunveigryorth_2_descend](../flags/stunveigryorth_2_descend.md)</li><li>dungeon encounter effect:</li><ul><li>base success = 60</li><li>success id = 238</li><li>base failure = 40</li><li>failure id = 237</li></ul></ul>
