#Information
 - Title: On The Walls\n[DungeonOverlayBackground]
 - ID: diggy_dungeons.833
#Description
On The Walls\n[DungeonOverlayBackground]
#Options

___
##Through the window

###Available if:
<li>always</li>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>dungeon encounter effect:</li><ul><li>base success = 60</li><li>success id = 838</li><li>base failure = 40</li><li>failure id = 836</li></ul></ul>

___
##Pick the lock

###Available if:
<li>check variable:</li><ul><li>partySupplies is at least 4</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>change party supplies:</li><ul><li>remove tooltip = yes</li><li>loss = 4</li></ul><li>set province flag [ofralglarf_2_lock](../flags/ofralglarf_2_lock.md)</li><li>dungeon encounter effect:</li><ul><li>base success = 80</li><li>success id = 838</li><li>base failure = 20</li><li>failure id = 837</li></ul></ul>
