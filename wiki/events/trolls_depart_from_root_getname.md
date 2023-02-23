#Information
 - Title: Trolls Depart from [Root.GetName]
 - ID: aw_trolls.10
#Description
Trolls Depart from [Root.GetName]
#Options

___
##Finally they're leaving

###Available if:
<li>event target:aw trolls migration target:</li><ul><li>owned by is event_target:aw_trolls_migration_origin_owner</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>goto = aw_trolls_migration_target</li><li>tooltip:</li><ul><li>remove province modifier = aw_trolls_1</li><li>remove province modifier = aw_trolls_2</li><li>remove province modifier = aw_trolls_3</li></ul><li>event target:aw trolls migration target:</li><ul><li>If has ROOT has province modifier is aw trolls 1:</li><ul><li>add permanent province modifier:</li><ul><li>name = aw_trolls_1</li><li>duration = -1</li></ul></ul><li>Else if has ROOT has province modifier is aw trolls 2:</li><ul><li>add permanent province modifier:</li><ul><li>name = aw_trolls_2</li><li>duration = -1</li></ul></ul><li>Else if has ROOT has province modifier is aw trolls 3:</li><ul><li>add permanent province modifier:</li><ul><li>name = aw_trolls_3</li><li>duration = -1</li></ul></ul><li>hidden effect:</li><ul><li>ROOT:</li><ul><li>remove province modifier = aw_trolls_1</li><li>remove province modifier = aw_trolls_2</li><li>remove province modifier = aw_trolls_3</li></ul></ul></ul></ul>

___
##Thoughts and prayers for [aw_trolls_migration_target.GetName].

###Available if:
<li>event target:aw trolls migration target:</li><ul><li>None of the following:</li><ul><li>owned by is event_target:aw_trolls_migration_origin_owner</li></ul></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>goto = aw_trolls_migration_target</li><li>tooltip:</li><ul><li>remove province modifier = aw_trolls_1</li><li>remove province modifier = aw_trolls_2</li><li>remove province modifier = aw_trolls_3</li></ul><li>custom tooltip = aw_trolls_migrate_to_other_country_tt</li><li>hidden effect:</li><ul><li>event target:aw trolls migration target:</li><ul><li>fire province event [aw_trolls.11](aw_trolls.11_slug) immediately </li></ul></ul></ul>
