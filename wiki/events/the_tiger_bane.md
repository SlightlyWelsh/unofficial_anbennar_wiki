#Information
 - Title: The Tiger Bane
 - ID: salgae.5
#Description
The Tiger Bane
#Options

___
##The jungle will burn with the Caehn's fury

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>reduce stability or adm power = yes</li><li>custom tooltip = tiger_bane_rebellion_tooltip</li><li>hidden effect:</li><ul><li>If has country flag is [tiger_bane_flag](../flags/tiger_bane_flag.md):</li><ul><li>If every owned province has province modifier is centaur tiger bane territory:</li><ul><li>add core = I93</li></ul><li>release = I93</li></ul><li>else:</li><ul><li>If every owned province has province flag is [tiger_bane_region](../flags/tiger_bane_region.md):</li><ul><li>clr province flag [tiger_bane_region](../flags/tiger_bane_region.md)</li><li>clr province flag [marked_region](../flags/marked_region.md)</li><li>add core = I93</li></ul><li>release = I93</li><li>I93:</li><ul><li>If random owned province has any neighbor province has owned by is I89, and does not have province flag is [capital_region](../flags/capital_region.md):</li><ul><li>If random neighbor province has owned by is I89, and does not have province flag is [capital_region](../flags/capital_region.md):</li><ul><li>If region has owned by is I89:</li><ul><li>add core = I93</li><li>cede province = I93</li></ul></ul></ul></ul></ul><li>I93:</li><ul><li>change technology group = tech_centaur</li><li>change religion = ik_magthaal</li><li>change government = tribal</li><li>add government reform = centaur_settled</li><li>the event [Missing localisation: salgae_100_t](../events/missing_localisation_salgae_100_t.md) happens</li><li>declare war with cb:</li><ul><li>who = I91</li><li>casus belli = cb_salgae</li></ul><li>declare war with cb:</li><ul><li>who = I92</li><li>casus belli = cb_salgae</li></ul><li>add yearly manpower = 10</li><li>add years of income = 15</li><li>set country flag [centaur_breakaway](../flags/centaur_breakaway.md)</li></ul><li>declare war with cb:</li><ul><li>who = I93</li><li>casus belli = cb_salgae</li></ul><li>set country flag [tiger_bane_revolt](../flags/tiger_bane_revolt.md)</li><li>remove faction = tiger_bane</li></ul></ul>

___
##The monsoon begins to pour

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>reduce stability or adm power = yes</li><li>custom tooltip = centaur_switch_country_tooltip</li><li>hidden effect:</li><ul><li>If has country flag is [tiger_bane_flag](../flags/tiger_bane_flag.md):</li><ul><li>If every owned province has province modifier is centaur tiger bane territory:</li><ul><li>add core = I93</li></ul><li>release = I93</li></ul><li>else:</li><ul><li>If every owned province has province flag is [tiger_bane_region](../flags/tiger_bane_region.md):</li><ul><li>clr province flag [tiger_bane_region](../flags/tiger_bane_region.md)</li><li>clr province flag [marked_region](../flags/marked_region.md)</li><li>add core = I93</li></ul><li>release = I93</li><li>I93:</li><ul><li>If random owned province has any neighbor province has owned by is I89, and does not have province flag is [capital_region](../flags/capital_region.md):</li><ul><li>If random neighbor province has owned by is I89, and does not have province flag is [capital_region](../flags/capital_region.md):</li><ul><li>If region has owned by is I89:</li><ul><li>add core = I93</li><li>cede province = I93</li></ul></ul></ul></ul></ul><li>I93:</li><ul><li>change technology group = tech_centaur</li><li>change religion = ik_magthaal</li><li>change government = tribal</li><li>add government reform = centaur_settled</li><li>the event [Missing localisation: salgae_100_t](../events/missing_localisation_salgae_100_t.md) happens</li><li>declare war with cb:</li><ul><li>who = I91</li><li>casus belli = cb_salgae</li></ul><li>declare war with cb:</li><ul><li>who = I92</li><li>casus belli = cb_salgae</li></ul><li>set country flag [centaur_breakaway](../flags/centaur_breakaway.md)</li></ul><li>declare war with cb:</li><ul><li>who = I93</li><li>casus belli = cb_salgae</li></ul><li>set country flag [tiger_bane_revolt](../flags/tiger_bane_revolt.md)</li><li>remove faction = tiger_bane</li></ul><li>switch tag = I93</li></ul>
