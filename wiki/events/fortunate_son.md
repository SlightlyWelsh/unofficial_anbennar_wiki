#Information
 - Title: Fortunate Son
 - ID: estate_castes_events.107
#Description
Fortunate Son
#Mean Time to Happen:
Base time = 1 days

#Options

___
##The ones showing the most promise can be introduced to the warrior caste

###Efects:<ul><li>caste fluidity increase medium = yes</li><li>add estate loyalty:</li><ul><li>estate = estate_lowercastes</li><li>loyalty = 15</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_uppercastes</li><li>loyalty = -15</li></ul><li>add yearly manpower = 0.25</li></ul>

___
##Let merchants hire them as bodyguards

###Efects:<ul><li>caste fluidity increase small = yes</li><li>add estate loyalty:</li><ul><li>estate = estate_lowercastes</li><li>loyalty = 5</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_middlecastes</li><li>loyalty = 5</li></ul><li>If random owned province does not have province flag is [modifier_province_flag](../flags/modifier_province_flag.md):</li><ul><li>add province modifier:</li><ul><li>name = estate_castes_events_hired_bodyguards_mod</li><li>duration = 3650</li></ul><li>set province flag [modifier_province_flag](../flags/modifier_province_flag.md)</li></ul><li>If random owned province does not have province flag is [modifier_province_flag](../flags/modifier_province_flag.md):</li><ul><li>add province modifier:</li><ul><li>name = estate_castes_events_hired_bodyguards_mod</li><li>duration = 3650</li></ul><li>set province flag [modifier_province_flag](../flags/modifier_province_flag.md)</li></ul><li>If random owned province does not have province flag is [modifier_province_flag](../flags/modifier_province_flag.md):</li><ul><li>add province modifier:</li><ul><li>name = estate_castes_events_hired_bodyguards_mod</li><li>duration = 3650</li></ul><li>set province flag [modifier_province_flag](../flags/modifier_province_flag.md)</li></ul><li>hidden effect:</li><ul><li>every owned province:</li><ul><li>clr province flag [modifier_province_flag](../flags/modifier_province_flag.md)</li></ul></ul></ul>

___
##Lower Castes work is honourable too. Show these men where they belong

###Efects:<ul><li>caste fluidity decrease small = yes</li><li>add estate loyalty:</li><ul><li>estate = estate_lowercastes</li><li>loyalty = -10</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_uppercastes</li><li>loyalty = 10</li></ul><li>country gets the modifier estate_castes_events_enforced_status_quo_mod for 10 years</li></ul>
