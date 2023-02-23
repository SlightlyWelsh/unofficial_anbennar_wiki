#Information
 - Title: Goblins Leave to Raid [aw_goblins_migration_target.GetName]
 - ID: aw_goblins.10
#Description
Goblins Leave to Raid [aw_goblins_migration_target.GetName]
#Options

___
##Best to check on [aw_goblins_migration_target.GetName].

###Available if:
<li>event target:aw goblins migration target:</li><ul><li>owned by is event_target:aw_goblins_migration_origin_owner</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>goto = aw_goblins_migration_target</li><li>tooltip:</li><ul><li>remove province modifier = aw_goblins_1</li><li>remove province modifier = aw_goblins_2</li><li>remove province modifier = aw_goblins_3</li></ul><li>event target:aw goblins migration target:</li><ul><li>If has ROOT has province modifier is aw goblins 1:</li><ul><li>add permanent province modifier:</li><ul><li>name = aw_goblins_1</li><li>duration = -1</li></ul></ul><li>Else if has ROOT has province modifier is aw goblins 2:</li><ul><li>add permanent province modifier:</li><ul><li>name = aw_goblins_2</li><li>duration = -1</li></ul></ul><li>Else if has ROOT has province modifier is aw goblins 3:</li><ul><li>add permanent province modifier:</li><ul><li>name = aw_goblins_3</li><li>duration = -1</li></ul></ul><li>hidden effect:</li><ul><li>ROOT:</li><ul><li>remove province modifier = aw_goblins_1</li><li>remove province modifier = aw_goblins_2</li><li>remove province modifier = aw_goblins_3</li></ul></ul></ul></ul>

___
##We'll see how they handle it.

###Available if:
<li>event target:aw goblins migration target:</li><ul><li>None of the following:</li><ul><li>owned by is event_target:aw_goblins_migration_origin_owner</li></ul></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>goto = aw_goblins_migration_target</li><li>tooltip:</li><ul><li>remove province modifier = aw_goblins_1</li><li>remove province modifier = aw_goblins_2</li><li>remove province modifier = aw_goblins_3</li></ul><li>custom tooltip = aw_goblins_migrate_to_other_country_tt</li><li>hidden effect:</li><ul><li>event target:aw goblins migration target:</li><ul><li>fire province event [aw_goblins.11](aw_goblins.11_slug) immediately </li></ul></ul></ul>
