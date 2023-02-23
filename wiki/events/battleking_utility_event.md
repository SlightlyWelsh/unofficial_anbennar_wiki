#Information
 - Title: Battleking Utility Event
 - ID: flavor_malacnar.6
#Description
Battleking Utility Event
#Options

___
##Grind, grind, grind at the enemy armies like they're mobs

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>If is not controlled by the AI:</li><ul><li>add ruler modifier:</li><ul><li>name = g32_battleking_fought_recently</li><li>duration = 1825</li></ul></ul><li>else:</li><ul><li>add ruler modifier:</li><ul><li>name = g32_battleking_fought_recently</li><li>duration = 3650</li></ul></ul><li>If has ruler modifier is g32 untested battleking, and has ruler modifier is g32 cowardly battleking:</li><ul><li>random:</li><ul><li>chance = 50</li><li>the event [A [Root.Monarch.GetTitle]'s Progression](../events/a_root_monarch_gettitle_s_progression.md) happens</li></ul></ul><li>Else if has ruler modifier is g32 tested battleking, and has ruler modifier is g32 legendary battleking:</li><ul><li>random:</li><ul><li>chance = 20</li><li>the event [A [Root.Monarch.GetTitle]'s Progression](../events/a_root_monarch_gettitle_s_progression.md) happens</li></ul></ul><li>Else if has ruler modifier is g32 bloodied battleking:</li><ul><li>random:</li><ul><li>chance = 10</li><li>the event [A [Root.Monarch.GetTitle]'s Progression](../events/a_root_monarch_gettitle_s_progression.md) happens</li></ul></ul><li>Else if has ruler modifier is g32 veteran battleking:</li><ul><li>random:</li><ul><li>chance = 5</li><li>the event [A [Root.Monarch.GetTitle]'s Progression](../events/a_root_monarch_gettitle_s_progression.md) happens</li></ul></ul><li>If is female:</li><ul><li>If has ruler modifier is g32 tested battleking:</li><ul><li>random:</li><ul><li>chance = 20</li><li>the event [The Battlequeen Triumphant](../events/the_battlequeen_triumphant.md) happens</li></ul></ul><li>Else if has ruler modifier is g32 bloodied battleking:</li><ul><li>random:</li><ul><li>chance = 50</li><li>the event [The Battlequeen Triumphant](../events/the_battlequeen_triumphant.md) happens</li></ul></ul><li>Else if has ruler modifier is g32 veteran battleking, and has ruler modifier is g32 legendary battleking:</li><ul><li>the event [The Battlequeen Triumphant](../events/the_battlequeen_triumphant.md) happens</li></ul></ul></ul>
