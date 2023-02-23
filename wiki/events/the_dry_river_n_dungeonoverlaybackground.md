#Information
 - Title: The Dry River\n[DungeonOverlayBackground]
 - ID: diggy_dungeons.538
#Description
The Dry River\n[DungeonOverlayBackground]
#Options

___
##Everyone, grab something heavy and get started.

###Available if:
<li>always</li>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>dungeon encounter effect:</li><ul><li>base success = 60</li><li>success id = 543</li><li>base failure = 40</li><li>failure id = 544</li></ul></ul>

___
##This calls for a little explosive persuasion.

###Available if:
<li>check variable:</li><ul><li>partySupplies is at least 4</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>change party supplies:</li><ul><li>remove tooltip = yes</li><li>loss = 4</li></ul><li>set province flag [grumhardhum_2_blowup](../flags/grumhardhum_2_blowup.md)</li><li>dungeon encounter effect:</li><ul><li>base success = 80</li><li>success id = 543</li><li>base failure = 20</li><li>failure id = 544</li></ul></ul>
