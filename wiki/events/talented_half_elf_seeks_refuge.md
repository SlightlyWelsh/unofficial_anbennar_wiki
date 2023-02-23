#Information
 - Title: Talented Half-Elf Seeks Refuge
 - ID: bulwar_flavour.40
#Description
Talented Half-Elf Seeks Refuge
#Options

___
##Half-elves are welcome in [Root.GetName]! Offer them refuge.

###AI weighting:
AI weights this option at 75


###Efects:<ul><li>If has country flag is [bulwar_flavour_helf_artist](../flags/bulwar_flavour_helf_artist.md):</li><ul><li>define advisor:</li><ul><li>type = artist</li><li>name = half_elf_advisor</li><li>skill = 2</li><li>culture = half_elf</li><li>religion = old_bulwari_sun_cult</li><li>discount = yes</li></ul></ul><li>Else if has country flag is [bulwar_flavour_helf_statesman](../flags/bulwar_flavour_helf_statesman.md):</li><ul><li>define advisor:</li><ul><li>type = statesman</li><li>name = half_elf_advisor</li><li>skill = 2</li><li>culture = half_elf</li><li>religion = old_bulwari_sun_cult</li><li>discount = yes</li></ul></ul><li>else:</li><ul><li>define advisor:</li><ul><li>type = army_reformer</li><li>name = half_elf_advisor</li><li>skill = 2</li><li>culture = half_elf</li><li>religion = old_bulwari_sun_cult</li><li>discount = yes</li></ul></ul><li>small increase of half elven tolerance effect = yes</li></ul>

___
##Half-elves are not welcome here. Get them out of my sight!

###AI weighting:
AI weights this option at 25


###Efects:<ul><li>country gets the modifier bulwar_flavour_no_helf for 10 years</li><li>small decrease of half elven tolerance effect = yes</li></ul>

___
##This will be the half-breed's last mistake! Off with their head!

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>country gets the modifier bulwar_flavour_executed_helf for 10 years</li><li>large decrease of half elven tolerance effect = yes</li></ul>
