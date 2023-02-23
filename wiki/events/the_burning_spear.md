#Information
 - Title: The Burning Spear
 - ID: salgae.3
#Description
The Burning Spear
#Options

___
##The sand will be crushed underhoof

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>reduce stability or adm power = yes</li><li>custom tooltip = burning_spear_rebellion_tooltip</li><li>hidden effect:</li><ul><li>If has country flag is [burning_spear_flag](../flags/burning_spear_flag.md):</li><ul><li>If every owned province has province modifier is centaur burning spear territory:</li><ul><li>add core = I91</li></ul><li>release = I91</li></ul><li>else:</li><ul><li>If every owned province has province flag is [burning_spear_region](../flags/burning_spear_region.md):</li><ul><li>clr province flag [burning_spear_region](../flags/burning_spear_region.md)</li><li>clr province flag [marked_region](../flags/marked_region.md)</li><li>add core = I91</li></ul><li>release = I91</li><li>I91:</li><ul><li>If random owned province has any neighbor province has owned by is I89, and does not have province flag is [capital_region](../flags/capital_region.md):</li><ul><li>If random neighbor province has owned by is I89, and does not have province flag is [capital_region](../flags/capital_region.md):</li><ul><li>If region has owned by is I89:</li><ul><li>add core = I91</li><li>cede province = I91</li></ul></ul></ul></ul></ul><li>I91:</li><ul><li>change technology group = tech_centaur</li><li>change religion = ik_magthaal</li><li>change government = tribal</li><li>add government reform = centaur_settled</li><li>the event [Missing localisation: salgae_100_t](../events/missing_localisation_salgae_100_t.md) happens</li><li>add yearly manpower = 10</li><li>add years of income = 15</li><li>set country flag [centaur_breakaway](../flags/centaur_breakaway.md)</li></ul><li>declare war with cb:</li><ul><li>who = I91</li><li>casus belli = cb_salgae</li></ul><li>the event [The Verdant Bliss](../events/the_verdant_bliss.md) happens</li><li>set country flag [burning_spear_revolt](../flags/burning_spear_revolt.md)</li><li>remove faction = burning_spear</li></ul></ul>

___
##The sandstorm begins to blow

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>reduce stability or adm power = yes</li><li>custom tooltip = centaur_switch_country_tooltip</li><li>hidden effect:</li><ul><li>If has country flag is [burning_spear_flag](../flags/burning_spear_flag.md):</li><ul><li>If every owned province has province modifier is centaur burning spear territory:</li><ul><li>add core = I91</li></ul><li>release = I91</li></ul><li>else:</li><ul><li>If every owned province has province flag is [burning_spear_region](../flags/burning_spear_region.md):</li><ul><li>clr province flag [burning_spear_region](../flags/burning_spear_region.md)</li><li>clr province flag [marked_region](../flags/marked_region.md)</li><li>add core = I91</li></ul><li>release = I91</li><li>I91:</li><ul><li>If random owned province has any neighbor province has owned by is I89, and does not have province flag is [capital_region](../flags/capital_region.md):</li><ul><li>If random neighbor province has owned by is I89, and does not have province flag is [capital_region](../flags/capital_region.md):</li><ul><li>If region has owned by is I89:</li><ul><li>add core = I91</li><li>cede province = I91</li></ul></ul></ul></ul></ul><li>I91:</li><ul><li>change technology group = tech_centaur</li><li>change religion = ik_magthaal</li><li>change government = tribal</li><li>add government reform = centaur_settled</li><li>the event [Missing localisation: salgae_100_t](../events/missing_localisation_salgae_100_t.md) happens</li><li>add yearly manpower = 10</li><li>add years of income = 15</li><li>set country flag [centaur_breakaway](../flags/centaur_breakaway.md)</li></ul><li>declare war with cb:</li><ul><li>who = I91</li><li>casus belli = cb_salgae</li></ul><li>the event [The Verdant Bliss](../events/the_verdant_bliss.md) happens</li><li>set country flag [burning_spear_revolt](../flags/burning_spear_revolt.md)</li><li>remove faction = burning_spear</li></ul><li>switch tag = I91</li></ul>
