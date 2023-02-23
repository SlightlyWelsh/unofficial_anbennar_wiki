#Information
 - Title: Frozen Gems
 - ID: flavor_krak.103
#Description
Frozen Gems
#Options

___
##Go back

###AI weighting:
AI weights this option at 5


###Efects:<ul><li>custom tooltip = opens_magic_estate_menu_tt</li><li>hidden effect:</li><ul><li>the event [    Ice Smithing\n£estate_magic_icesmith_bg£\n\n\n\n[Root.GetSpellStrengthIndicator]                                   ](../events/ice_smithing_npsestate_magic_icesmith_bgps_n_n_n_n_root_getspellstrengthindicator.md) happens</li></ul></ul>

___
##Such beautiful pieces!

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>If has country flag is [icecraft_gems_upgrade](../flags/icecraft_gems_upgrade.md):</li><ul><li>If has estate influence has estate is estate mages, and estate influence has influence is 66:</li><ul><li>country gets the modifier krak_frozengems_6 for 10 years</li></ul><li>Else if has estate influence has estate is estate mages, and estate influence has influence is 33:</li><ul><li>country gets the modifier krak_frozengems_5 for 10 years</li></ul><li>else:</li><ul><li>country gets the modifier krak_frozengems_4 for 10 years</li></ul></ul><li>If has estate influence has estate is estate mages, and estate influence has influence is 66:</li><ul><li>add dip power = -150</li><li>If has check variable has which is krak discount spell, and check variable has value is 1:</li><ul><li>change variable:</li><ul><li>which = krak_discount_spell</li><li>value = -1</li></ul></ul><li>else:</li><ul><li>add years of income = -0.8</li></ul><li>If every owned province is core is ROOT, and  has trade goods is gems:</li><ul><li>add province modifier:</li><ul><li>name = krak_frozengems_3</li><li>duration = 3650</li></ul></ul></ul><li>Else if has estate influence has estate is estate mages, and estate influence has influence is 33:</li><ul><li>add dip power = -100</li><li>If has check variable has which is krak discount spell, and check variable has value is 1:</li><ul><li>change variable:</li><ul><li>which = krak_discount_spell</li><li>value = -1</li></ul></ul><li>else:</li><ul><li>add years of income = -0.55</li></ul><li>If every owned province is core is ROOT, and  has trade goods is gems:</li><ul><li>add province modifier:</li><ul><li>name = krak_frozengems_2</li><li>duration = 3650</li></ul></ul></ul><li>else:</li><ul><li>add dip power = -50</li><li>If has check variable has which is krak discount spell, and check variable has value is 1:</li><ul><li>change variable:</li><ul><li>which = krak_discount_spell</li><li>value = -1</li></ul></ul><li>else:</li><ul><li>add years of income = -0.5</li></ul><li>If every owned province is core is ROOT, and  has trade goods is gems:</li><ul><li>add province modifier:</li><ul><li>name = krak_frozengems_1</li><li>duration = 3650</li></ul></ul></ul></ul>
