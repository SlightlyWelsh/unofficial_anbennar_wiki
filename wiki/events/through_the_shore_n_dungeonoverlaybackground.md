#Information
 - Title: Through The Shore\n[DungeonOverlayBackground]
 - ID: diggy_dungeons.324
#Description
Through The Shore\n[DungeonOverlayBackground]
#Options

___
##Get out of here! Back to the water, crabs!

###Available if:
<li>always</li>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>set province flag [wytlramvar_2_crabs](../flags/wytlramvar_2_crabs.md)</li><li>dungeon progress advancement:</li><ul><li>id = 329</li></ul></ul>

___
##We could try to lure them out with food.

###Available if:
<li>check variable:</li><ul><li>partySupplies is at least 4</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>change party supplies:</li><ul><li>remove tooltip = yes</li><li>loss = 4</li></ul><li>dungeon encounter effect:</li><ul><li>base success = 80</li><li>success id = 330</li><li>base failure = 20</li><li>failure id = 328</li></ul></ul>
