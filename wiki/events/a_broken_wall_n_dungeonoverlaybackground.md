#Information
 - Title: A Broken Wall\n[DungeonOverlayBackground]
 - ID: diggy_dungeons.608
#Description
A Broken Wall\n[DungeonOverlayBackground]
#Options

___
##It is fine as it is. Just walk through without taking extra precautions.

###Available if:
<li>always</li>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>dungeon encounter effect:</li><ul><li>base success = 40</li><li>success id = 611</li><li>base failure = 60</li><li>failure id = 610</li></ul></ul>

___
##Better safe than sorry. Let us spend some time stabilizing the passage.

###Available if:
<li>check variable:</li><ul><li>partySupplies is at least 4</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>change party supplies:</li><ul><li>remove tooltip = yes</li><li>loss = 4</li></ul><li>set province flag [leforn_1_stabilize](../flags/leforn_1_stabilize.md)</li><li>dungeon encounter effect:</li><ul><li>base success = 60</li><li>success id = 611</li><li>base failure = 40</li><li>failure id = 610</li></ul></ul>
