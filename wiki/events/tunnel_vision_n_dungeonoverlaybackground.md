#Information
 - Title: Tunnel Vision\n[DungeonOverlayBackground]
 - ID: diggy_dungeons.527
#Description
Tunnel Vision\n[DungeonOverlayBackground]
#Options

___
##I want soldiers, armoured and bearing shields.

###Available if:
<li>always</li>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>dungeon encounter effect:</li><ul><li>base success = 60</li><li>success id = 534</li><li>base failure = 40</li><li>failure id = 533</li></ul></ul>

___
##I want water mages and armoured soldiers.

###Available if:
<li>check variable:</li><ul><li>partySupplies is at least 4</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>change party supplies:</li><ul><li>remove tooltip = yes</li><li>loss = 4</li></ul><li>set province flag [grumhardhum_2_throwwater](../flags/grumhardhum_2_throwwater.md)</li><li>dungeon encounter effect:</li><ul><li>base success = 80</li><li>success id = 534</li><li>base failure = 20</li><li>failure id = 533</li></ul></ul>
