#Information
 - Title: Ice Fields
 - ID: flavor_krak.104
#Description
Ice Fields
#Options

___
##Go back

###AI weighting:
AI weights this option at 5


###Efects:<ul><li>custom tooltip = opens_magic_estate_menu_tt</li><li>hidden effect:</li><ul><li>the event [    Ice Smithing\n£estate_magic_icesmith_bg£\n\n\n\n[Root.GetSpellStrengthIndicator]                                   ](../events/ice_smithing_npsestate_magic_icesmith_bgps_n_n_n_n_root_getspellstrengthindicator.md) happens</li></ul></ul>

___
##Northern Pass

###Available if:
<li>4175:</li><ul><li>has building mage_tower</li><li>owned by is this nation</li></ul><li>4181:</li><ul><li>has building mage_tower</li><li>owned by is this nation</li></ul><li>4194:</li><ul><li>has building mage_tower</li><li>owned by is this nation</li></ul><li>4197:</li><ul><li>has building mage_tower</li><li>owned by is this nation</li></ul><li>4200:</li><ul><li>has building mage_tower</li><li>owned by is this nation</li></ul><li>4190:</li><ul><li>has building mage_tower</li><li>owned by is this nation</li></ul><li>4184:</li><ul><li>has building mage_tower</li><li>owned by is this nation</li></ul>

###AI weighting:
AI weights this option at 10
 - Multiplied by 100 if has any owned province has region is northern pass region, and any owned province has owned by is ROOT, and does not have controlled by is ROOT


###Efects:<ul><li>If has check variable has which is krak discount spell, and check variable has value is 1:</li><ul><li>change variable:</li><ul><li>which = krak_discount_spell</li><li>value = -1</li></ul></ul><li>else:</li><ul><li>add years of income = -0.75</li></ul><li>If northern pass region has owned by is ROOT:</li><ul><li>add province modifier:</li><ul><li>name = krak_icefield</li><li>duration = 3650</li></ul></ul></ul>

___
##West Dwarovar

###Available if:
<li>num of owned provinces with:</li><ul><li>region is west_dwarovar_region</li><li>has building mage_tower</li><li>value is at least 12</li></ul>

###AI weighting:
AI weights this option at 10
 - Multiplied by 100 if has any owned province has region is west dwarovar region, and any owned province has owned by is ROOT, and does not have controlled by is ROOT


###Efects:<ul><li>If has check variable has which is krak discount spell, and check variable has value is 1:</li><ul><li>change variable:</li><ul><li>which = krak_discount_spell</li><li>value = -1</li></ul></ul><li>else:</li><ul><li>add years of income = -0.75</li></ul><li>If west dwarovar region has owned by is ROOT:</li><ul><li>add province modifier:</li><ul><li>name = krak_icefield</li><li>duration = 3650</li></ul></ul></ul>

___
##Serpentreach

###Available if:
<li>num of owned provinces with:</li><ul><li>region is serpentreach_region</li><li>has building mage_tower</li><li>value is at least 8</li></ul>

###AI weighting:
AI weights this option at 10
 - Multiplied by 100 if has any owned province has region is serpentreach region, and any owned province has owned by is ROOT, and does not have controlled by is ROOT


###Efects:<ul><li>If has check variable has which is krak discount spell, and check variable has value is 1:</li><ul><li>change variable:</li><ul><li>which = krak_discount_spell</li><li>value = -1</li></ul></ul><li>else:</li><ul><li>add years of income = -0.75</li></ul><li>If serpentreach region has owned by is ROOT:</li><ul><li>add province modifier:</li><ul><li>name = krak_icefield</li><li>duration = 3650</li></ul></ul></ul>

___
##Middle Dwarovar

###Available if:
<li>num of owned provinces with:</li><ul><li>region is middle_dwarovar_region</li><li>has building mage_tower</li><li>value is at least 9</li></ul>

###AI weighting:
AI weights this option at 10
 - Multiplied by 100 if has any owned province has region is middle dwarovar region, and any owned province has owned by is ROOT, and does not have controlled by is ROOT


###Efects:<ul><li>If has check variable has which is krak discount spell, and check variable has value is 1:</li><ul><li>change variable:</li><ul><li>which = krak_discount_spell</li><li>value = -1</li></ul></ul><li>else:</li><ul><li>add years of income = -0.75</li></ul><li>If middle dwarovar region has owned by is ROOT:</li><ul><li>add province modifier:</li><ul><li>name = krak_icefield</li><li>duration = 3650</li></ul></ul></ul>

___
##Tree of Stone

###Available if:
<li>num of owned provinces with:</li><ul><li>region is tree_of_stone_region</li><li>has building mage_tower</li><li>value is at least 7</li></ul>

###AI weighting:
AI weights this option at 10
 - Multiplied by 100 if has any owned province has region is tree of stone region, and does not have controlled by is ROOT


###Efects:<ul><li>If has check variable has which is krak discount spell, and check variable has value is 1:</li><ul><li>change variable:</li><ul><li>which = krak_discount_spell</li><li>value = -1</li></ul></ul><li>else:</li><ul><li>add years of income = -0.75</li></ul><li>If tree of stone region has owned by is ROOT:</li><ul><li>add province modifier:</li><ul><li>name = krak_icefield</li><li>duration = 3650</li></ul></ul></ul>

___
##Jade Mines

###Available if:
<li>num of owned provinces with:</li><ul><li>region is jade_mines_region</li><li>has building mage_tower</li><li>value is at least 6</li></ul>

###AI weighting:
AI weights this option at 10
 - Multiplied by 100 if has any owned province has region is jade mines region, and any owned province has owned by is ROOT, and does not have controlled by is ROOT


###Efects:<ul><li>If has check variable has which is krak discount spell, and check variable has value is 1:</li><ul><li>change variable:</li><ul><li>which = krak_discount_spell</li><li>value = -1</li></ul></ul><li>else:</li><ul><li>add years of income = -0.75</li></ul><li>If jade mines region has owned by is ROOT:</li><ul><li>add province modifier:</li><ul><li>name = krak_icefield</li><li>duration = 3650</li></ul></ul></ul>
