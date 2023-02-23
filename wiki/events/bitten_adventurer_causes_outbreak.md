#Information
 - Title: Bitten Adventurer Causes Outbreak
 - ID: aw_zombies.110
#Description
Bitten Adventurer Causes Outbreak
#Options

___
##One problem dealt with, another one takes its place...

###Available if:
<li>event target:aw zombies migration target:</li><ul><li>owned by is event_target:aw_zombies_migration_origin_owner</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>goto = aw_zombies_migration_target</li><li>tooltip:</li><ul><li>remove province modifier = aw_zombies_1</li><li>remove province modifier = aw_zombies_2</li><li>remove province modifier = aw_zombies_3</li></ul><li>event target:aw zombies migration target:</li><ul><li>If has ROOT has province modifier is aw zombies 1:</li><ul><li>add permanent province modifier:</li><ul><li>name = aw_zombies_1</li><li>duration = -1</li></ul></ul><li>Else if has ROOT has province modifier is aw zombies 2:</li><ul><li>add permanent province modifier:</li><ul><li>name = aw_zombies_2</li><li>duration = -1</li></ul></ul><li>Else if has ROOT has province modifier is aw zombies 3:</li><ul><li>add permanent province modifier:</li><ul><li>name = aw_zombies_3</li><li>duration = -1</li></ul></ul><li>hidden effect:</li><ul><li>ROOT:</li><ul><li>remove province modifier = aw_zombies_1</li><li>remove province modifier = aw_zombies_2</li><li>remove province modifier = aw_zombies_3</li></ul></ul></ul></ul>

___
##Thankfully this happened abroad in [aw_zombies_migration_target.GetName]...

###Available if:
<li>event target:aw zombies migration target:</li><ul><li>None of the following:</li><ul><li>owned by is event_target:aw_zombies_migration_origin_owner</li></ul></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>goto = aw_zombies_migration_target</li><li>tooltip:</li><ul><li>remove province modifier = aw_zombies_1</li><li>remove province modifier = aw_zombies_2</li><li>remove province modifier = aw_zombies_3</li></ul><li>custom tooltip = aw_zombies_migrate_to_other_country_tt</li><li>hidden effect:</li><ul><li>event target:aw zombies migration target:</li><ul><li>fire province event [aw_zombies.111](aw_zombies.111_slug) immediately </li></ul></ul></ul>
