#Information
 - Title: Golem Assembler\n[DungeonOverlayBackground]
 - ID: diggy_dungeons.728
#Description
Golem Assembler\n[DungeonOverlayBackground]
#Options

___
##Can we just turn it off?

###Available if:
<li>check variable:</li><ul><li>partySupplies is at least 4</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>change party supplies:</li><ul><li>remove tooltip = yes</li><li>loss = 4</li></ul><li>set province flag [runeshop_2_assembly](../flags/runeshop_2_assembly.md)</li><li>set province flag [runeshop_2_shutdown](../flags/runeshop_2_shutdown.md)</li><li>dungeon progress advancement:</li><ul><li>id = 730</li></ul></ul>

___
##Risk nothing, destroy it.!

###Available if:
<li>always</li>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>set province flag [runeshop_2_assembly](../flags/runeshop_2_assembly.md)</li><li>set province flag [runeshop_2_violence](../flags/runeshop_2_violence.md)</li><li>dungeon encounter effect:</li><ul><li>base success = 40</li><li>success id = 730</li><li>base failure = 60</li><li>failure id = 731</li></ul></ul>

___
##Send the Mages!

###Available if:
<li>always</li>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>set province flag [runeshop_2_assembly](../flags/runeshop_2_assembly.md)</li><li>set province flag [runeshop_2_magic](../flags/runeshop_2_magic.md)</li><li>dungeon encounter effect:</li><ul><li>base success = 80</li><li>success id = 730</li><li>base failure = 20</li><li>failure id = 731</li></ul></ul>
