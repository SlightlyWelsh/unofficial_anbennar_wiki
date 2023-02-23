#Information
 - Title: Diocese of the Deep\n[DungeonOverlayBackground]
 - ID: diggy_dungeons.835
#Description
Diocese of the Deep\n[DungeonOverlayBackground]
#Options

___
##Break the door open

###Available if:
<li>always</li>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>dungeon encounter effect:</li><ul><li>base success = 40</li><li>success id = 841</li><li>base failure = 60</li><li>failure id = 842</li></ul></ul>

___
##Drill through the wall

###Available if:
<li>check variable:</li><ul><li>partySupplies is at least 4</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>change party supplies:</li><ul><li>remove tooltip = yes</li><li>loss = 4</li></ul><li>set province flag [ofralglarf_2_drill](../flags/ofralglarf_2_drill.md)</li><li>dungeon encounter effect:</li><ul><li>base success = 60</li><li>success id = 841</li><li>base failure = 40</li><li>failure id = 842</li></ul></ul>
