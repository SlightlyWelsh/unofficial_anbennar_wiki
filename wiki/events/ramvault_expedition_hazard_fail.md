#Information
 - Title: Ramvault Expedition: Hazard Fail
 - ID: ramsteel.16
#Description
Ramvault Expedition: Hazard Fail
#Options

___
##Ask the mages for expertise

###Available if:
<li>has estate estate_mages</li>

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>add estate influence modifier:</li><ul><li>estate = estate_mages</li><li>desc = ramsteel_asked_estate_help</li><li>duration = 7300</li><li>influence = 5</li></ul><li>add prestige = -10</li><li>hidden effect:</li><ul><li>If has country flag is [ramsteel_ancient_curse](../flags/ramsteel_ancient_curse.md):</li><ul><li>set country flag [ramsteel_success](../flags/ramsteel_success.md)</li></ul></ul></ul>

___
##Ask the dwarven clans for equipment

###Available if:
<li>has estate estate_nobles</li>

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>add estate influence modifier:</li><ul><li>estate = estate_nobles</li><li>desc = ramsteel_asked_estate_help</li><li>duration = 7300</li><li>influence = 5</li></ul><li>add legitimacy = -10</li><li>hidden effect:</li><ul><li>If has country flag is [ramsteel_cave_collapse](../flags/ramsteel_cave_collapse.md):</li><ul><li>set country flag [ramsteel_success](../flags/ramsteel_success.md)</li></ul></ul></ul>

___
##Ask the adventurers for manpower

###Available if:
<li>has estate estate_adventurers</li>

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>add estate influence modifier:</li><ul><li>estate = estate_adventurers</li><li>desc = ramsteel_asked_estate_help</li><li>duration = 7300</li><li>influence = 5</li></ul><li>add years of income = -0.25</li><li>hidden effect:</li><ul><li>If has country flag is [ramsteel_goblin_ambush](../flags/ramsteel_goblin_ambush.md):</li><ul><li>set country flag [ramsteel_success](../flags/ramsteel_success.md)</li></ul></ul></ul>

___
##Use our crown resources to figure out a solution

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>add years of income = -0.33</li><li>hidden effect:</li><ul><li>set country flag [ramsteel_success](../flags/ramsteel_success.md)</li></ul></ul>

___
##They can figure it out themselves

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>set country flag [ramsteel_left_alone](../flags/ramsteel_left_alone.md)</li><li>add prestige = -15</li></ul>
