#Information
 - Title: Orcs Destroying Property in [orcish_causing_havoc_province.GetName]
 - ID: orcish_tolerance_events.1
#Description
Orcs Destroying Property in [orcish_causing_havoc_province.GetName]
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Punish them harshly

###AI weighting:
AI weights this option at 50
 - Multiplied by 1.5 if has country flag is [orc_loot_church](../flags/orc_loot_church.md), and  has dlc is "The Cossacks", and does not have estate loyalty has estate is estate church, and estate loyalty has loyalty is 40
 - Multiplied by 1.5 if has country flag is [orc_loot_nobles](../flags/orc_loot_nobles.md), and  has dlc is "The Cossacks", and does not have estate loyalty has estate is estate nobles, and estate loyalty has loyalty is 40
 - Multiplied by 1.5 if has country flag is [orc_loot_burghers](../flags/orc_loot_burghers.md), and  has dlc is "The Cossacks", and does not have estate loyalty has estate is estate burghers, and estate loyalty has loyalty is 40
 - Multiplied by 0.5 if has wants to maintain tolerance orcish is yes
 - Multiplied by 0.1 if has wants to increase tolerance orcish is yes


###Efects:<ul><li>add prestige = 5</li><li>add mil power = -20</li><li>small decrease of orcish tolerance effect = yes</li><li>event target:orcish causing havoc province:</li><ul><li>add province modifier:</li><ul><li>name = orcish_harsh_punishment_prov</li><li>duration = 3650</li></ul></ul><li>trigger switch:</li><ul><li>on trigger = has_country_flag</li><li>orc loot burghers:</li><ul><li>If has estate is estate burghers:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_burghers</li><li>loyalty = 5</li></ul></ul></ul><li>orc loot church:</li><ul><li>If has estate is estate church:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_church</li><li>loyalty = 5</li></ul></ul></ul><li>orc loot nobles:</li><ul><li>If has estate is estate nobles:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_nobles</li><li>loyalty = 5</li></ul></ul></ul></ul></ul>

___
##Just punish them moderately

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>add mil power = -10</li><li>event target:orcish causing havoc province:</li><ul><li>add province modifier:</li><ul><li>name = orcish_normal_punishment_prov</li><li>duration = 3650</li></ul></ul></ul>

___
##We have to forgive for which is out of their control

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.5 if has country flag is [orc_loot_church](../flags/orc_loot_church.md), and  has dlc is "The Cossacks", and does not have estate loyalty has estate is estate church, and estate loyalty has loyalty is 40
 - Multiplied by 0.5 if has country flag is [orc_loot_nobles](../flags/orc_loot_nobles.md), and  has dlc is "The Cossacks", and does not have estate loyalty has estate is estate nobles, and estate loyalty has loyalty is 40
 - Multiplied by 0.5 if has country flag is [orc_loot_burghers](../flags/orc_loot_burghers.md), and  has dlc is "The Cossacks", and does not have estate loyalty has estate is estate burghers, and estate loyalty has loyalty is 40
 - Multiplied by 0.5 if has wants to maintain tolerance orcish is yes
 - Multiplied by 0.1 if has wants to decrease tolerance orcish is yes


###Efects:<ul><li>add prestige = -10</li><li>small increase of orcish tolerance effect = yes</li><li>trigger switch:</li><ul><li>on trigger = has_country_flag</li><li>orc loot burghers:</li><ul><li>reduce estate burghers loyalty effect = yes</li></ul><li>orc loot church:</li><ul><li>reduce estate church loyalty effect = yes</li></ul><li>orc loot nobles:</li><ul><li>reduce estate nobles loyalty effect = yes</li></ul></ul></ul>

___
##Punish them and their families!

###Available if:
<li>ruler has personality is cruel_personality</li>

###AI weighting:
AI weights this option at 100
 - Multiplied by 1.5 if has country flag is [orc_loot_church](../flags/orc_loot_church.md), and  has dlc is "The Cossacks", and does not have estate loyalty has estate is estate church, and estate loyalty has loyalty is 40
 - Multiplied by 1.5 if has country flag is [orc_loot_nobles](../flags/orc_loot_nobles.md), and  has dlc is "The Cossacks", and does not have estate loyalty has estate is estate nobles, and estate loyalty has loyalty is 40
 - Multiplied by 1.5 if has country flag is [orc_loot_burghers](../flags/orc_loot_burghers.md), and  has dlc is "The Cossacks", and does not have estate loyalty has estate is estate burghers, and estate loyalty has loyalty is 40
 - Multiplied by 0.5 if has wants to maintain tolerance orcish is yes
 - Multiplied by 0.1 if has wants to increase tolerance orcish is yes


###Efects:<ul><li>highlight = yes</li><li>add prestige = 10</li><li>add mil power = -25</li><li>small decrease of orcish tolerance effect = yes</li><li>event target:orcish causing havoc province:</li><ul><li>If area does not have province modifier is orcish harsh punishment prov; and does not have province modifier is orcish normal punishment prov; and has orcish minority trigger is yes, and has culture group is orcish:</li><ul><li>add province modifier:</li><ul><li>name = orcish_harsh_punishment_prov</li><li>duration = 1825</li></ul></ul></ul><li>trigger switch:</li><ul><li>on trigger = has_country_flag</li><li>orc loot burghers:</li><ul><li>add estate burghers loyalty effect = yes</li></ul><li>orc loot church:</li><ul><li>add estate church loyalty effect = yes</li></ul><li>orc loot nobles:</li><ul><li>add estate nobles loyalty effect = yes</li></ul></ul></ul>
