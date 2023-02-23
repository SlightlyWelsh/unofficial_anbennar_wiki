#Information
 - Title: Forgotten Ropes And Woods\n[DungeonOverlayBackground]
 - ID: diggy_dungeons.314
#Description
Forgotten Ropes And Woods\n[DungeonOverlayBackground]
#Options

___
##It is fine, we will just sprint across it.

###Available if:
<li>always</li>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>set province flag [wytlramvar_1_bridge](../flags/wytlramvar_1_bridge.md)</li><li>dungeon encounter effect:</li><ul><li>base success = 60</li><li>success id = 311</li><li>base failure = 40</li><li>failure id = 310</li></ul></ul>

___
##Make the bridge safe again.

###Available if:
<li>check variable:</li><ul><li>partySupplies is at least 4</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>change party supplies:</li><ul><li>remove tooltip = yes</li><li>loss = 4</li></ul><li>set province flag [wytlramvar_1_bridge](../flags/wytlramvar_1_bridge.md)</li><li>dungeon encounter effect:</li><ul><li>base success = 80</li><li>success id = 311</li><li>base failure = 20</li><li>failure id = 310</li></ul></ul>
