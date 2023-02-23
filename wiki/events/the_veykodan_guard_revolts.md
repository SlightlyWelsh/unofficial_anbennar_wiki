#Information
 - Title: The Veykodan Guard Revolts!
 - ID: flavor_arverynn.2
#Description
The Veykodan Guard Revolts!
#Mean Time to Happen:
Base time = 8 months

#Options

___
##In its desperation to reclaim the empire, House Vyrekynn delivered it to barbarians.

###Available if:
<li>never</li>

###AI weighting:
AI weights this option at 2


###Efects:<ul><li>kill ruler = yes</li><li>kill heir:</li><ul><li>allow new heir = no</li></ul><li>hidden effect:</li><ul><li>random owned province:</li><ul><li>add core = U21</li><li>cede province = U21</li></ul></ul><li>tooltip:</li><ul><li>every owned province:</li><ul><li>add core = U21</li><li>cede province = U21</li></ul></ul><li>switch tag = U21</li><li>ROOT:</li><ul><li>If random hired mercenary company has template is veykodan guard merc:</li><ul><li>disband mercenary company = THIS</li></ul></ul><li>hidden effect:</li><ul><li>ROOT:</li><ul><li>clr country flag [G35_veykodan_mercs_available_flag](../flags/g35_veykodan_mercs_available_flag.md)</li></ul></ul></ul>

___
##Loot everything and pack it into carts, we're out!

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>kill ruler = yes</li><li>kill heir:</li><ul><li>allow new heir = no</li></ul><li>If has owns core province is 1139:</li><ul><li>1139:</li><ul><li>add devastation = 50</li><li>add base tax = -2</li><li>add base production = -2</li><li>add base manpower = -2</li><li>If has great project has type is ynnic teal keep, and has great project has tier is 2; and has great project has type is ynnic teal keep, and has great project has tier is 3:</li><ul><li>1139:</li><ul><li>add great project tier:</li><ul><li>type = ynnic_teal_keep</li><li>tier = -1</li></ul></ul></ul><li>else:</li><ul><li>1139:</li><ul><li>destroy great project:</li><ul><li>type = ynnic_teal_keep</li></ul></ul></ul></ul></ul><li>else:</li><ul><li>capital scope:</li><ul><li>add devastation = 50</li><li>add base tax = -2</li><li>add base production = -2</li><li>add base manpower = -2</li></ul></ul><li>If random hired mercenary company has template is veykodan guard merc:</li><ul><li>disband mercenary company = THIS</li></ul><li>If north america has region is sarda region, and has region is dolindha region, and has region is rzenta region; and  has culture is veykodan, and  is city:</li><ul><li>remove province modifier = ynn_pomentere_estates</li><li>If has owned by is ROOT:</li><ul><li>add devastation = 20</li><li>add base tax = -1</li><li>add base production = -1</li><li>add base manpower = -1</li></ul><li>If has region is sarda region:</li><ul><li>change culture = sarda</li></ul><li>Else if has region is dolindha region:</li><ul><li>change culture = dolindhan</li></ul><li>Else if has region is rzenta region:</li><ul><li>change culture = rzentur</li></ul></ul><li>hidden effect:</li><ul><li>clr country flag [G35_veykodan_mercs_available_flag](../flags/g35_veykodan_mercs_available_flag.md)</li></ul><li>add years of income = -5</li><li>complete mission = pomentere_estates</li><li>complete mission = buycev_policy</li><li>complete mission = veykodan_guard</li></ul>
