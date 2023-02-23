#Information
 - Title: Straggler Zombies from the Army
 - ID: aw_zombies.100
#Description
Straggler Zombies from the Army
#Options

___
##Ashen skies. Hopefully they'll be dealt with.

###Available if:
<li>event target:aw zombies target:</li><ul><li>owned by is this nation</li></ul>

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>goto = aw_zombies_target</li><li>event target:aw zombies target:</li><ul><li>add permanent province modifier:</li><ul><li>name = aw_zombies_1</li><li>duration = -1</li></ul></ul></ul>

___
##Hah! Good luck to them!

###Available if:
<li>event target:aw zombies target:</li><ul><li>None of the following:</li><ul><li>owned by is this nation</li></ul></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>goto = aw_zombies_target</li><li>custom tooltip = aw_zombies_migrate_to_other_country_tt</li><li>hidden effect:</li><ul><li>event target:aw zombies target:</li><ul><li>fire province event [aw_zombies.101](aw_zombies.101_slug) immediately </li></ul></ul></ul>

___
##No, you will obey me!

###Available if:
<li>ruler is legendary in necromancy</li><li>mil power is at least 20</li>

###AI weighting:
AI weights this option at 1000


###Efects:<ul><li>highlight = yes</li><li>add mil power = -20</li><li>custom tooltip = is_necromancy_3_tt</li></ul>
