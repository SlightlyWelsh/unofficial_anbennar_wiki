#Information
 - Title: Complex Controls\n[DungeonOverlayBackground]
 - ID: diggy_dungeons.526
#Description
Complex Controls\n[DungeonOverlayBackground]
#Options

___
##Pull the red lever.

###Available if:
<li>None of the following:</li><ul><li>has province flag [grumhardhum_2_lever](../flags/grumhardhum_2_lever.md)</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>set province flag [grumhardhum_2_lever](../flags/grumhardhum_2_lever.md)</li><li>If has province flag is [grumhardhum_2_control_correct1](../flags/grumhardhum_2_control_correct1.md):</li><ul><li>set province flag [grumhardhum_2_control_correct2](../flags/grumhardhum_2_control_correct2.md)</li></ul><li>dungeon encounter effect:</li><ul><li>base success = 60</li><li>success id = 529</li><li>base failure = 40</li><li>failure id = 530</li></ul></ul>

___
##Turn the green valve on the left.

###Available if:
<li>None of the following:</li><ul><li>has province flag [grumhardhum_2_leftvalve](../flags/grumhardhum_2_leftvalve.md)</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>set province flag [grumhardhum_2_leftvalve](../flags/grumhardhum_2_leftvalve.md)</li><li>dungeon encounter effect:</li><ul><li>base success = 80</li><li>success id = 529</li><li>base failure = 20</li><li>failure id = 530</li></ul></ul>

___
##Turn the yellow valve on the right.

###Available if:
<li>None of the following:</li><ul><li>has province flag [grumhardhum_2_rightvalve](../flags/grumhardhum_2_rightvalve.md)</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>set province flag [grumhardhum_2_rightvalve](../flags/grumhardhum_2_rightvalve.md)</li><li>If has province flag is [grumhardhum_2_leftvalve](../flags/grumhardhum_2_leftvalve.md), and does not have province flag is [grumhardhum_2_lever](../flags/grumhardhum_2_lever.md):</li><ul><li>set province flag [grumhardhum_2_control_correct1](../flags/grumhardhum_2_control_correct1.md)</li></ul><li>dungeon encounter effect:</li><ul><li>base success = 60</li><li>success id = 529</li><li>base failure = 40</li><li>failure id = 530</li></ul></ul>

___
##Search for instructions in the control room.

###Available if:
<li>None of the following:</li><ul><li>has province flag [grumhardhum_2_labels](../flags/grumhardhum_2_labels.md)</li></ul><li>NOT:</li><ul><li>All of the following:</li><ul><li>has province flag [grumhardhum_2_lever](../flags/grumhardhum_2_lever.md)</li><li>has province flag  grumhardhum_2_leftvalve</li><li>has province flag   grumhardhum_2_rightvalve</li></ul></ul><li>check variable:</li><ul><li>partySupplies is at least 4</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>change party supplies:</li><ul><li>remove tooltip = yes</li><li>loss = 4</li></ul><li>set province flag [grumhardhum_2_labels](../flags/grumhardhum_2_labels.md)</li><li>dungeon encounter effect:</li><ul><li>base success = 60</li><li>success id = 532</li><li>base failure = 40</li><li>failure id = 531</li></ul></ul>

___
##Let's move on, we've done what we can.

###Available if:
<li>has province flag [grumhardhum_2_lever](../flags/grumhardhum_2_lever.md)</li><li>has province flag  grumhardhum_2_leftvalve</li><li>has province flag   grumhardhum_2_rightvalve</li>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>dungeon progress advancement:</li><ul><li>id = 525</li></ul></ul>
