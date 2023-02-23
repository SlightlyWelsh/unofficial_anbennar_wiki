#Information
 - Title: Eldritch Cult Migrates to [aw_eldritch_cultists_migration_target.GetName]
 - ID: aw_eldritch_cultists.10
#Description
Eldritch Cult Migrates to [aw_eldritch_cultists_migration_target.GetName]
#Options

___
##They'll just end up stirring trouble somewhere else.

###Available if:
<li>event target:aw eldritch cultists migration target:</li><ul><li>owned by is event_target:aw_eldritch_cultists_migration_origin_owner</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>goto = aw_eldritch_cultists_migration_target</li><li>tooltip:</li><ul><li>remove province modifier = aw_eldritch_cultists_1</li><li>remove province modifier = aw_eldritch_cultists_2</li><li>remove province modifier = aw_eldritch_cultists_3</li></ul><li>event target:aw eldritch cultists migration target:</li><ul><li>If has ROOT has province modifier is aw eldritch cultists 1:</li><ul><li>add permanent province modifier:</li><ul><li>name = aw_eldritch_cultists_1</li><li>duration = -1</li></ul></ul><li>Else if has ROOT has province modifier is aw eldritch cultists 2:</li><ul><li>add permanent province modifier:</li><ul><li>name = aw_eldritch_cultists_2</li><li>duration = -1</li></ul></ul><li>Else if has ROOT has province modifier is aw eldritch cultists 3:</li><ul><li>add permanent province modifier:</li><ul><li>name = aw_eldritch_cultists_3</li><li>duration = -1</li></ul></ul><li>hidden effect:</li><ul><li>ROOT:</li><ul><li>remove province modifier = aw_eldritch_cultists_1</li><li>remove province modifier = aw_eldritch_cultists_2</li><li>remove province modifier = aw_eldritch_cultists_3</li></ul></ul></ul></ul>

___
##That's not our problem anymore.

###Available if:
<li>event target:aw eldritch cultists migration target:</li><ul><li>None of the following:</li><ul><li>owned by is event_target:aw_eldritch_cultists_migration_origin_owner</li></ul></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>goto = aw_eldritch_cultists_migration_target</li><li>tooltip:</li><ul><li>remove province modifier = aw_eldritch_cultists_1</li><li>remove province modifier = aw_eldritch_cultists_2</li><li>remove province modifier = aw_eldritch_cultists_3</li></ul><li>custom tooltip = aw_eldritch_cultists_migrate_to_other_country_tt</li><li>hidden effect:</li><ul><li>event target:aw eldritch cultists migration target:</li><ul><li>fire province event [aw_eldritch_cultists.11](aw_eldritch_cultists.11_slug) immediately </li></ul></ul></ul>
