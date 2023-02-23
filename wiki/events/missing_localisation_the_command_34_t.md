#Information
 - Title: Missing localisation: the_command_34_t
 - ID: the_command.34
#Description

#Mean Time to Happen:
Base time = 18 months
 - Multiplied by 0.5 if has culture group is wuhyun
 - Multiplied by 0.5 if has religion is godlost
 - Multiplied by 100 if has owner is controlled by the AI

#Options

___
##Missing localisation: the_command_34_a

###Available if:
<li>None of the following:</li><ul><li>culture group is wuhyun</li></ul>

###AI weighting:
AI weights this option at 1


###One of the following randomly happens:
Outcome 1:

Available if <li>None of the following:</li><ul><li>has orcish majority trigger yes</li></ul>

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>If has superregion is rahen superregion:</li><ul><li>change culture = kusonin</li></ul><li>Else if has superregion is yanshen superregion, and has superregion is north haless superregion:</li><ul><li>change culture = ikaniwagain</li></ul><li>Else if has superregion is south haless superregion:</li><ul><li>change culture = kintonan</li></ul><li>else:</li><ul><li>change culture = rinonokegyun</li></ul></ul>
Outcome 2:

Available if <li>owner:</li><ul><li>has country flag [R62_honourable_half_orcs_flag](../flags/r62_honourable_half_orcs_flag.md)</li></ul><li>Any of the following:</li><ul><li>has orcish majority trigger yes</li><li>has any half orcish pop trigger yes</li></ul>

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>change culture = wuhyun_half_orc</li></ul>

###Efects:<ul><li>hidden effect:</li><ul><li>on province culture converted estate privilges effect = yes</li></ul></ul>

___
##Missing localisation: the_command_34_b

###Available if:
<li>None of the following:</li><ul><li>religion is godlost</li></ul>

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>change religion = godlost</li></ul>
