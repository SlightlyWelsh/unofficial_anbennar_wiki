#Information
 - Title: Eduz-Ammanu, the Seat of the Magi
 - ID: new_sun_cult.246
#Description
Eduz-Ammanu, the Seat of the Magi
#Options

___
##In a Sun Elven province, in our Crownland.

###Available if:
<li>None of the following:</li><ul><li>has country flag [nsc_bulwari_organization](../flags/nsc_bulwari_organization.md)</li></ul><li>any owned province:</li><ul><li>culture is sun_elf</li><li>None of the following:</li><ul><li>province has center of trade of level is at least 1</li></ul><li>NOT:</li><ul><li>has terrain farmlands</li></ul><li>has saved event target nsc_elven_mage_hogwarts_target</li></ul>

###Efects:<ul><li>custom tooltip = nsc_chosen_role_up_tt</li><li>custom tooltip = nsc_increase_magi_influence</li><li>country gets the modifier nsc_magi_supported_magi for 10 years</li><li>event target:nsc elven mage hogwarts target:</li><ul><li>add building construction:</li><ul><li>building = mage_tower</li><li>speed = 0.5</li><li>cost = 0.5</li></ul><li>add province modifier:</li><ul><li>name = nsc_bulwari_hogwarts</li><li>duration = -1</li></ul></ul><li>set country flag [nsc_privilege_magi_influence](../flags/nsc_privilege_magi_influence.md)</li></ul>

___
##In a Sun Elven province, under the control of the nobles.

###Available if:
<li>None of the following:</li><ul><li>has country flag [nsc_bulwari_organization](../flags/nsc_bulwari_organization.md)</li></ul><li>any owned province:</li><ul><li>culture is sun_elf</li><li>has terrain farmlands</li><li>None of the following:</li><ul><li>province has center of trade of level is at least 1</li></ul><li>has saved event target nsc_elven_nobility_hogwarts_target</li></ul>

###Efects:<ul><li>custom tooltip = nsc_chosen_role_up_tt</li><li>custom tooltip = nsc_increase_noble_influence</li><li>country gets the modifier nsc_magi_supported_nobles for 10 years</li><li>add estate influence modifier:</li><ul><li>estate = estate_nobles</li><li>desc = nsc_hogwarts_in_elven_nobles_prov</li><li>influence = 10</li><li>duration = 20</li></ul><li>event target:nsc elven nobility hogwarts target:</li><ul><li>add building construction:</li><ul><li>building = mage_tower</li><li>speed = 0.5</li><li>cost = 0.5</li></ul><li>add province modifier:</li><ul><li>name = nsc_bulwari_hogwarts</li><li>duration = -1</li></ul></ul><li>set country flag [nsc_privilege_noble_influence](../flags/nsc_privilege_noble_influence.md)</li></ul>

___
##In a Center of Trade

###Available if:
<li>any owned province:</li><ul><li>province has center of trade of level is at least 1</li></ul>

###Efects:<ul><li>custom tooltip = nsc_increase_both_influence</li><li>country gets the modifier nsc_magi_supported_both for 10 years</li><li>add estate influence modifier:</li><ul><li>estate = estate_nobles</li><li>desc = nsc_hogwarts_in_cot_mage_prov</li><li>influence = 5</li><li>duration = 20</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_burghers</li><li>desc = nsc_hogwarts_in_cot_mage_prov</li><li>influence = 5</li><li>duration = 20</li></ul><li>event target:nsc cot mage hogwarts target:</li><ul><li>add building construction:</li><ul><li>building = mage_tower</li><li>speed = 0.5</li><li>cost = 0.5</li></ul><li>add province modifier:</li><ul><li>name = nsc_bulwari_hogwarts</li><li>duration = -1</li></ul></ul><li>set country flag [nsc_privilege_both_influence](../flags/nsc_privilege_both_influence.md)</li></ul>

___
##In a Bulwari province, under the control of the burghers.

###Available if:
<li>None of the following:</li><ul><li>has country flag [nsc_tutelage_organization](../flags/nsc_tutelage_organization.md)</li></ul><li>any owned province:</li><ul><li>culture group is bulwari</li><li>development is at least 15</li><li>None of the following:</li><ul><li>province has center of trade of level is at least 1</li></ul></ul><li>has saved event target nsc_human_burgher_hogwarts_target</li>

###Efects:<ul><li>custom tooltip = nsc_chosen_role_down_tt</li><li>custom tooltip = nsc_increase_burgher_influence</li><li>country gets the modifier nsc_magi_supported_burghers for 10 years</li><li>add estate influence modifier:</li><ul><li>estate = estate_burghers</li><li>desc = nsc_hogwarts_in_human_burgher_prov</li><li>influence = 10</li><li>duration = 20</li></ul><li>event target:nsc human burgher hogwarts target:</li><ul><li>add building construction:</li><ul><li>building = mage_tower</li><li>speed = 0.5</li><li>cost = 0.5</li></ul><li>add province modifier:</li><ul><li>name = nsc_bulwari_hogwarts</li><li>duration = -1</li></ul></ul><li>set country flag [nsc_privilege_burgher_influence](../flags/nsc_privilege_burgher_influence.md)</li><li>clr province flag [nsc_nsc_human_burgher_hogwarts_province](../flags/nsc_nsc_human_burgher_hogwarts_province.md)</li></ul>

___
##In a Bulwari province, in our Crownland.

###Available if:
<li>None of the following:</li><ul><li>has country flag [nsc_tutelage_organization](../flags/nsc_tutelage_organization.md)</li></ul><li>any owned province:</li><ul><li>culture group is bulwari</li><li>has terrain drylands</li><li>None of the following:</li><ul><li>province has center of trade of level is at least 1</li></ul></ul><li>has saved event target nsc_human_mage_hogwarts_target</li>

###Efects:<ul><li>custom tooltip = nsc_chosen_role_down_tt</li><li>custom tooltip = nsc_increase_magi_influence</li><li>country gets the modifier nsc_magi_supported_magi for 10 years</li><li>event target:nsc human mage hogwarts target:</li><ul><li>add building construction:</li><ul><li>building = mage_tower</li><li>speed = 0.5</li><li>cost = 0.5</li></ul><li>add province modifier:</li><ul><li>name = nsc_bulwari_hogwarts</li><li>duration = -1</li></ul></ul><li>set country flag [nsc_privilege_magi_influence](../flags/nsc_privilege_magi_influence.md)</li></ul>
