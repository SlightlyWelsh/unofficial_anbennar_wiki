#Information
 - Title: The Hunt: Werebear
 - ID: flavor_adenica.5
#Description
The Hunt: Werebear
#Options

___
##Wait! Let the adventurers have a word. Maybe they can provide a solution?

###Available if:
<li>has country flag [hunt_adventurers](../flags/hunt_adventurers.md)</li>

###Efects:<ul><li>highlight = yes</li><li>set country flag [hunt_werebear_adventurer_negotiated](../flags/hunt_werebear_adventurer_negotiated.md)</li></ul>

___
##Put it out of its misery

###Efects:<ul><li>add prestige = -5</li><li>set country flag [hunt_werebear_dead](../flags/hunt_werebear_dead.md)</li></ul>

___
##Try and talk it out

###Available if:


###Efects:<ul><li>If has ruler has personality is charismatic negotiator personality:</li><ul><li>set country flag [hunt_werebear_negotiated](../flags/hunt_werebear_negotiated.md)</li></ul><li>Else if has ruler has personality is silver tongue personality:</li><ul><li>set country flag [hunt_werebear_negotiated](../flags/hunt_werebear_negotiated.md)</li></ul><li>Else if has dip is 4, and does not have dip is 5:</li><ul><li>random:</li><ul><li>chance = 50</li><li>set country flag [hunt_werebear_negotiated](../flags/hunt_werebear_negotiated.md)</li></ul></ul><li>Else if has dip is 5, and does not have dip is 6:</li><ul><li>random:</li><ul><li>chance = 75</li><li>set country flag [hunt_werebear_negotiated](../flags/hunt_werebear_negotiated.md)</li></ul></ul><li>Else if has dip is 6:</li><ul><li>random:</li><ul><li>chance = 100</li><li>set country flag [hunt_werebear_negotiated](../flags/hunt_werebear_negotiated.md)</li></ul></ul><li>else:</li><ul><li>random:</li><ul><li>chance = 25</li><li>set country flag [hunt_werebear_negotiated](../flags/hunt_werebear_negotiated.md)</li></ul></ul><li>If does not have country flag is [hunt_werebear_negotiated](../flags/hunt_werebear_negotiated.md):</li><ul><li>set country flag [hunt_werebear_negotiations_failed](../flags/hunt_werebear_negotiations_failed.md)</li></ul></ul>
