#Information
 - Title: Actions...\n[DungeonOverlayBackground]
 - ID: diggy_dungeons.749
#Description
Actions...\n[DungeonOverlayBackground]
#Options

___
##Perhaps we can Divine them with magic.

###Available if:
<li>check variable:</li><ul><li>partySupplies is at least 4</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>change party supplies:</li><ul><li>remove tooltip = yes</li><li>loss = 4</li></ul><li>dungeon encounter effect:</li><ul><li>base success = 60</li><li>success id = 750</li><li>base failure = 40</li><li>failure id = 751</li></ul></ul>

___
##Split up and search for it.

###Available if:
<li>always</li>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>set province flag [runeshop_3_search](../flags/runeshop_3_search.md)</li><li>dungeon encounter effect:</li><ul><li>base success = 40</li><li>success id = 750</li><li>base failure = 60</li><li>failure id = 752</li></ul></ul>

___
##An ambush may work.

###Available if:
<li>check variable:</li><ul><li>partySupplies is at least 4</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>change party supplies:</li><ul><li>remove tooltip = yes</li><li>loss = 4</li></ul><li>dungeon encounter effect:</li><ul><li>base success = 60</li><li>success id = 750</li><li>base failure = 40</li><li>failure id = 752</li></ul></ul>
