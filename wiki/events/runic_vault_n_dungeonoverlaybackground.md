#Information
 - Title: Runic Vault\n[DungeonOverlayBackground]
 - ID: diggy_dungeons.701
#Description
Runic Vault\n[DungeonOverlayBackground]
#Options

___
##We'll force our way inside.

###Available if:
<li>always</li>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>set province flag [runeshop_1_entry](../flags/runeshop_1_entry.md)</li><li>dungeon encounter effect:</li><ul><li>base success = 40</li><li>success id = 702</li><li>base failure = 60</li><li>failure id = 703</li></ul></ul>

___
##Try to solve the puzzle...

###Available if:
<li>check variable:</li><ul><li>partySupplies is at least 4</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>change party supplies:</li><ul><li>remove tooltip = yes</li><li>loss = 4</li></ul><li>dungeon encounter effect:</li><ul><li>base success = 80</li><li>success id = 702</li><li>base failure = 20</li><li>failure id = 703</li></ul></ul>
