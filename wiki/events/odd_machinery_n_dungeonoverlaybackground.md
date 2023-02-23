#Information
 - Title: Odd Machinery\n[DungeonOverlayBackground]
 - ID: diggy_dungeons.729
#Description
Odd Machinery\n[DungeonOverlayBackground]
#Options

___
##Clearly, smashing it is the only option.

###Available if:
<li>always</li>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>set province flag [runeshop_2_destroy](../flags/runeshop_2_destroy.md)</li><li>dungeon encounter effect:</li><ul><li>base success = 40</li><li>success id = 732</li><li>base failure = 60</li><li>failure id = 733</li></ul></ul>

___
##Maybe we can turn it off?

###Available if:
<li>check variable:</li><ul><li>partySupplies is at least 4</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>change party supplies:</li><ul><li>remove tooltip = yes</li><li>loss = 4</li></ul><li>dungeon encounter effect:</li><ul><li>base success = 80</li><li>success id = 732</li><li>base failure = 20</li><li>failure id = 733</li></ul></ul>
