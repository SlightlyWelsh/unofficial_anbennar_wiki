#Information
 - Title: The Magma Below\n[DungeonOverlayBackground]
 - ID: diggy_dungeons.510
#Description
The Magma Below\n[DungeonOverlayBackground]
#Options

___
##You've made it this far, you can do the rest alone.

###Available if:
<li>always</li>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>dungeon encounter effect:</li><ul><li>base success = 40</li><li>success id = 516</li><li>base failure = 60</li><li>failure id = 517</li></ul></ul>

___
##Quickly, throw him whatever he needs to repair the valves!

###Available if:
<li>check variable:</li><ul><li>partySupplies is at least 4</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>change party supplies:</li><ul><li>remove tooltip = yes</li><li>loss = 4</li></ul><li>set province flag [grumhardhum_1_emergencyvalves](../flags/grumhardhum_1_emergencyvalves.md)</li><li>dungeon encounter effect:</li><ul><li>base success = 60</li><li>success id = 516</li><li>base failure = 40</li><li>failure id = 517</li></ul></ul>
