#Information
 - Title: The Final Journey
 - ID: ynn_barges.1
#Description
The Final Journey
#Options

___
##Build an opulent barge

###AI weighting:
AI weights this option at 10
 - Multiplied by 0.01 if has num of loans is 1
 - Multiplied by 0.01 if is bankrupt
 - Multiplied by 0.1 if has ruler has personality is greedy personality


###Efects:<ul><li>add years of income = -0.95</li><li>add prestige = 10</li><li>add stability or adm power = yes</li><li>hidden effect:</li><ul><li>set country flag [big_barges](../flags/big_barges.md)</li></ul><li>hidden effect:</li><ul><li>the event [Missing localisation: ynn_barges_101_t](../events/missing_localisation_ynn_barges_101_t.md) happens</li></ul></ul>

___
##Build an elegant barge

###AI weighting:
AI weights this option at 7
 - Multiplied by 0.01 if has num of loans is 3
 - Multiplied by 0.01 if is bankrupt
 - Multiplied by 0.5 if has ruler has personality is greedy personality


###Efects:<ul><li>add years of income = -0.5</li><li>add prestige = 5</li><li>random:</li><ul><li>chance = 30</li><li>add stability or adm power = yes</li></ul><li>hidden effect:</li><ul><li>set country flag [normal_barges](../flags/normal_barges.md)</li></ul><li>hidden effect:</li><ul><li>the event [Missing localisation: ynn_barges_101_t](../events/missing_localisation_ynn_barges_101_t.md) happens</li></ul></ul>

___
##Build a simple barge

###AI weighting:
AI weights this option at 5
 - Multiplied by 0.2 if is bankrupt


###Efects:<ul><li>add years of income = -0.2</li><li>hidden effect:</li><ul><li>set country flag [little_barges](../flags/little_barges.md)</li></ul><li>hidden effect:</li><ul><li>the event [Missing localisation: ynn_barges_101_t](../events/missing_localisation_ynn_barges_101_t.md) happens</li></ul></ul>

___
##Just dump them in the River

###Available if:
<li>None of the following:</li><ul><li>government is republic</li></ul>

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>add prestige = -10</li><li>random:</li><ul><li>chance = 50</li><li>reduce stability or adm power = yes</li></ul></ul>

___
##Their family shall organize their funeral like any other

###Available if:
<li>government is republic</li>

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>add prestige = -10</li><li>add scaled republican tradition = -5</li><li>hidden effect:</li><ul><li>clr country flag [ynn_mayor_death](../flags/ynn_mayor_death.md)</li></ul></ul>
