#Information
 - Title: Massacre on the Dagrinrod!
 - ID: flavor_krak.7
#Description
Massacre on the Dagrinrod!
#Options

___
##This tragedy could've been avoided with proper preparation.

###AI weighting:
AI weights this option at 5


###Efects:<ul><li>add republican tradition = -20</li><li>add manpower = -0.2</li><li>add prestige = -40</li><li>3001:</li><ul><li>If is city:</li><ul><li>add devastation = 100</li></ul><li>else:</li><ul><li>custom tooltip = flavor_krak.7.tooltip</li><li>destroy province = yes</li><li>add permanent province modifier:</li><ul><li>name = krak_fearful_colonization</li><li>duration = 3650</li></ul></ul></ul><li>If dagrinrod 13 15 area does not have province id is 3001:</li><ul><li>remove claim = ROOT</li></ul><li>If orlazam area does not have province id is 4147:</li><ul><li>remove claim = ROOT</li></ul><li>dagrinrod 7 9 area:</li><ul><li>remove claim = ROOT</li></ul><li>the event [Clan Council Election!](../events/clan_council_election.md) happens</li><li>hidden effect:</li><ul><li>If has country flag is [krak_unsteady_road_happened](../flags/krak_unsteady_road_happened.md):</li><ul><li>set country flag [krak_disaster_can_start](../flags/krak_disaster_can_start.md)</li></ul></ul></ul>
