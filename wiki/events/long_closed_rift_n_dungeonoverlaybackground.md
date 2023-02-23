#Information
 - Title: Long-Closed Rift\n[DungeonOverlayBackground]
 - ID: diggy_dungeons.233
#Description
Long-Closed Rift\n[DungeonOverlayBackground]
#Options

___
##Wield the magic.

###Available if:
<li>always</li>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>dungeon progress advancement:</li><ul><li>id = 235</li></ul></ul>

___
##Explosives will do.

###Available if:
<li>check variable:</li><ul><li>partySupplies is at least 4</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>change party supplies:</li><ul><li>remove tooltip = yes</li><li>loss = 4</li></ul><li>set province flag [stunveigryorth_2_explosives](../flags/stunveigryorth_2_explosives.md)</li><li>dungeon encounter effect:</li><ul><li>base success = 80</li><li>success id = 234</li><li>base failure = 20</li><li>failure id = 235</li></ul></ul>
