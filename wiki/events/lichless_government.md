#Information
 - Title: Lichless Government
 - ID: magic_project_lichdom.16
#Description
Lichless Government
#Options

___
##The lich had a worthy apprentice to take the mantle

###Available if:
<li>ruler has mage personality is yes</li>

###AI weighting:
AI weights this option at 75


###Efects:<ul><li>add prestige = 10</li></ul>

___
##The dark acolytes of the realm solidified their magocratic control

###AI weighting:
AI weights this option at 33
 - Multiplied by 100 if has estate influence has estate is estate mages, and estate influence has influence is 60; and has estate influence has estate is estate acolytes, and estate influence has influence is 60


###Efects:<ul><li>add prestige = -10</li></ul>

___
##The realm reverted back to its old form, before the dark times

###AI weighting:
AI weights this option at 66


###Efects:<ul><li>If has country flag is [original_gov_monarchy](../flags/original_gov_monarchy.md):</li><ul><li>change government = monarchy</li><li>exile ruler as:</li><ul><li>name = old_lich_gov_ruler</li></ul></ul><li>Else if has country flag is [original_gov_republic](../flags/original_gov_republic.md):</li><ul><li>change government = republic</li><li>exile ruler as:</li><ul><li>name = old_lich_gov_ruler</li></ul></ul><li>Else if has country flag is [original_gov_theocracy](../flags/original_gov_theocracy.md):</li><ul><li>If has country flag is [original_gov_clergy](../flags/original_gov_clergy.md):</li><ul><li>add government reform = leading_clergy_reform</li></ul><li>Else if has country flag is [original_gov_monastic](../flags/original_gov_monastic.md):</li><ul><li>add government reform = monastic_order_reform</li></ul><li>Else if has country flag is [original_gov_secular](../flags/original_gov_secular.md):</li><ul><li>add government reform = secular_order_reform</li></ul><li>Else if has country flag is [original_gov_adventurer](../flags/original_gov_adventurer.md):</li><ul><li>add government reform = adventurer_reform</li></ul><li>Else if has country flag is [original_gov_rezankand](../flags/original_gov_rezankand.md):</li><ul><li>add government reform = rezankand_reform</li></ul><li>Else if has country flag is [original_gov_oracular](../flags/original_gov_oracular.md):</li><ul><li>add government reform = oracular_order_reform</li></ul><li>exile ruler as:</li><ul><li>name = old_lich_gov_ruler</li></ul></ul><li>Else if has country flag is [original_gov_tribal](../flags/original_gov_tribal.md):</li><ul><li>change government = tribal</li><li>If has primary culture is emerald orc:</li><ul><li>add government reform = emerald_horde</li></ul><li>Else if has culture group is goblin, and has culture group is orcish; and does not have capital scope has continent is serpentspine:</li><ul><li>add government reform = greentide_horde</li></ul><li>Else if has culture group is goblin, and has culture group is orcish; and  has capital scope has continent is serpentspine, and has terrain is dwarven hold, and has terrain is dwarven hold surface:</li><ul><li>add government reform = dwarovar_squatter</li></ul><li>Else if has culture group is goblin, and has culture group is orcish; and  has capital scope has continent is serpentspine, and does not have terrain is dwarven hold, and does not have terrain is dwarven hold surface:</li><ul><li>add government reform = dwarovar_warband</li></ul><li>Else if has culture is troll is yes, and has culture group is kobold:</li><ul><li>add government reform = settled_horde</li></ul><li>Else if has culture group is harpy, and has culture group is gnollish:</li><ul><li>add government reform = roaming_horde</li></ul><li>Else if has primary culture is desert elf:</li><ul><li>add government reform = desert_legion</li></ul><li>exile ruler as:</li><ul><li>name = old_lich_gov_ruler</li></ul></ul><li>magic project clear lichdom government flags = yes</li><li>add stability or adm power = yes</li></ul>
