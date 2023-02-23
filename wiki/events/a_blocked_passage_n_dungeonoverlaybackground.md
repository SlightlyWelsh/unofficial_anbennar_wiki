#Information
 - Title: A Blocked Passage\n[DungeonOverlayBackground]
 - ID: diggy_dungeons.603
#Description
A Blocked Passage\n[DungeonOverlayBackground]
#Options

___
##Heave ho!

###Available if:
<li>always</li>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>dungeon encounter effect:</li><ul><li>base success = 60</li><li>success id = 607</li><li>base failure = 40</li><li>failure id = 606</li></ul></ul>

___
##Clear the path with the explosives!

###Available if:
<li>check variable:</li><ul><li>partySupplies is at least 4</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>change party supplies:</li><ul><li>remove tooltip = yes</li><li>loss = 4</li></ul><li>set province flag [leforn_1_bomb](../flags/leforn_1_bomb.md)</li><li>dungeon encounter effect:</li><ul><li>base success = 80</li><li>success id = 607</li><li>base failure = 20</li><li>failure id = 606</li></ul></ul>
