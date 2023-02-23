#Information
 - Title: Trap-filled Hall\n[DungeonOverlayBackground]
 - ID: diggy_dungeons.704
#Description
Trap-filled Hall\n[DungeonOverlayBackground]
#Options

___
##Just close your eyes.

###Available if:
<li>always</li>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>set province flag [runeshop_1_traps](../flags/runeshop_1_traps.md)</li><li>dungeon encounter effect:</li><ul><li>base success = 60</li><li>success id = 706</li><li>base failure = 40</li><li>failure id = 705</li></ul></ul>

___
##Use the bandages.

###Available if:
<li>check variable:</li><ul><li>partySupplies is at least 4</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>change party supplies:</li><ul><li>remove tooltip = yes</li><li>loss = 4</li></ul><li>dungeon progress advancement:</li><ul><li>id = 706</li></ul></ul>
