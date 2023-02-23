#Information
 - Title: Filth And Beauty\n[DungeonOverlayBackground]
 - ID: diggy_dungeons.367
#Description
Filth And Beauty\n[DungeonOverlayBackground]
#Options

___
##Let us kill it before it gets out of the hole!

###Available if:
<li>always</li>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>dungeon progress advancement:</li><ul><li>id = 368</li></ul></ul>

___
##Quick! Re-arm the trap!

###Available if:
<li>check variable:</li><ul><li>partySupplies is at least 4</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>change party supplies:</li><ul><li>remove tooltip = yes</li><li>loss = 4</li></ul><li>set province flag [wytlramvar_3_trap](../flags/wytlramvar_3_trap.md)</li><li>dungeon progress advancement:</li><ul><li>id = 368</li></ul></ul>
