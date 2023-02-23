#Information
 - Title: Bandits On the Move
 - ID: aw_bandits.10
#Description
Bandits On the Move
#Options

___
##Curses!

###Available if:
<li>event target:aw bandits migration target:</li><ul><li>owned by is event_target:aw_bandits_migration_origin_owner</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>goto = aw_bandits_migration_target</li><li>tooltip:</li><ul><li>remove province modifier = aw_bandits_1</li><li>remove province modifier = aw_bandits_2</li><li>remove province modifier = aw_bandits_3</li></ul><li>event target:aw bandits migration target:</li><ul><li>If has ROOT has province modifier is aw bandits 1:</li><ul><li>add permanent province modifier:</li><ul><li>name = aw_bandits_1</li><li>duration = -1</li></ul></ul><li>Else if has ROOT has province modifier is aw bandits 2:</li><ul><li>add permanent province modifier:</li><ul><li>name = aw_bandits_2</li><li>duration = -1</li></ul></ul><li>Else if has ROOT has province modifier is aw bandits 3:</li><ul><li>add permanent province modifier:</li><ul><li>name = aw_bandits_3</li><li>duration = -1</li></ul></ul><li>hidden effect:</li><ul><li>ROOT:</li><ul><li>remove province modifier = aw_bandits_1</li><li>remove province modifier = aw_bandits_2</li><li>remove province modifier = aw_bandits_3</li></ul></ul></ul></ul>

___
##Good luck to them!

###Available if:
<li>event target:aw bandits migration target:</li><ul><li>None of the following:</li><ul><li>owned by is event_target:aw_bandits_migration_origin_owner</li></ul></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>goto = aw_bandits_migration_target</li><li>tooltip:</li><ul><li>remove province modifier = aw_bandits_1</li><li>remove province modifier = aw_bandits_2</li><li>remove province modifier = aw_bandits_3</li></ul><li>custom tooltip = aw_bandits_migrate_to_other_country_tt</li><li>hidden effect:</li><ul><li>event target:aw bandits migration target:</li><ul><li>fire province event [aw_bandits.11](aw_bandits.11_slug) immediately </li></ul></ul></ul>
