#Information
 - Title: The Gold Dwarves
 - ID: flavor_greedy_grin.2
#Description
The Gold Dwarves
#Options

___
##Kill any that resist

###Available if:
<li>2914:</li><ul><li>None of the following:</li><ul><li>culture is cave_goblin</li></ul><li>NOT:</li><ul><li>religion is goblinic_shamanism</li></ul></ul>

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>2914:</li><ul><li>change culture = cave_goblin</li><li>change religion = goblinic_shamanism</li><li>add devastation = 30</li><li>add base tax = -2</li><li>add base production = -2</li><li>add base manpower = -2</li></ul><li>hidden effect:</li><ul><li>the event [Missing localisation: race_setup_events_4_t](../events/missing_localisation_race_setup_events_4_t.md) happens</li></ul></ul>

___
##Enslave them

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>2914:</li><ul><li>If does not have culture is cave goblin:</li><ul><li>add goblin minority size effect = yes</li><li>add goblin minority size effect = yes</li></ul><li>else:</li><ul></ul><li>add province modifier:</li><ul><li>name = greedy_grin_gold_dwarven_slaves</li><li>duration = 3650</li></ul></ul><li>add dip power = 50</li></ul>
