#Information
 - Title: Battle Results
 - ID: flavor_malacnar.116
#Description
Battle Results
#Options

___
##Puah. Is this all a gunner can do? Get out of our country!

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>If has country flag is [yrw_3a](../flags/yrw_3a.md):</li><ul><li>custom tooltip = malacnar_gun_debate_switch_b</li><li>clr country flag [yrw_3a](../flags/yrw_3a.md)</li><li>set country flag [yrw_3b](../flags/yrw_3b.md)</li><li>add prestige = -5</li></ul><li>Else if has country flag is [yrw_3a_reform](../flags/yrw_3a_reform.md), and has country modifier is yrw 3a:</li><ul><li>reduce stability or adm power = yes</li></ul><li>Else if has country flag is [yrw_3b](../flags/yrw_3b.md), and has country flag is yrw 3b reform, and has country modifier is yrw 3b:</li><ul><li>trigger switch:</li><ul><li>on trigger = stability</li><li>3:</li><ul><li>add adm power = 100</li></ul><li>2:</li><ul><li>add adm power = 50</li><li>add stability = 1</li></ul><li>-3:</li><ul><li>add stability = 2</li></ul></ul></ul><li>else:</li><ul><li>add stability or adm power = yes</li></ul><li>malacnar battleking rankup = yes</li></ul>

___
##It was a good fight. You may stay in Bosancovac.

###AI weighting:
AI weights this option at 99


###Efects:<ul><li>If has country flag is [yrw_3b](../flags/yrw_3b.md):</li><ul><li>custom tooltip = malacnar_gun_debate_switch_a</li><li>clr country flag [yrw_3b](../flags/yrw_3b.md)</li><li>set country flag [yrw_3a](../flags/yrw_3a.md)</li><li>add prestige = -5</li></ul><li>Else if has country flag is [yrw_3b_reform](../flags/yrw_3b_reform.md), and has country modifier is yrw 3b:</li><ul><li>reduce stability or adm power = yes</li></ul><li>1165:</li><ul><li>add province modifier:</li><ul><li>name = malacnar_meeting</li><li>duration = -1</li></ul><li>add institution embracement:</li><ul><li>which = new_world_i</li><li>value = 30</li></ul><li>add province modifier:</li><ul><li>name = malacnar_rush</li><li>duration = 3650</li></ul><li>add base tax = 2</li><li>add base production = 2</li><li>add base manpower = 2</li><li>add human minority size effect = yes</li><li>add dwarven minority size effect = yes</li></ul><li>If has 2837 has owned by companion is yes:</li><ul><li>2837:</li><ul><li>add province modifier:</li><ul><li>name = malacnar_meeting</li><li>duration = -1</li></ul><li>add institution embracement:</li><ul><li>which = new_world_i</li><li>value = 20</li></ul><li>add human minority size effect = yes</li></ul></ul><li>If has 2839 has owned by companion is yes:</li><ul><li>2839:</li><ul><li>add province modifier:</li><ul><li>name = malacnar_meeting</li><li>duration = -1</li></ul><li>add institution embracement:</li><ul><li>which = new_world_i</li><li>value = 20</li></ul><li>add human minority size effect = yes</li></ul></ul></ul>


#Pages with same name:
The following pages have the same name as this page:
 - [battle_results_1](battle_results_1.md)
