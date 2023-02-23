#Information
 - Title: Eldritch Cult spreads to [aw_eldritch_cultists_migration_target.GetName]
 - ID: aw_eldritch_cultists.13
#Description
Eldritch Cult spreads to [aw_eldritch_cultists_migration_target.GetName]
#Options

___
##Oh no.

###Available if:
<li>event target:aw eldritch cultists migration target:</li><ul><li>owned by is event_target:aw_eldritch_cultists_migration_origin_owner</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>goto = aw_eldritch_cultists_migration_target</li><li>event target:aw eldritch cultists migration target:</li><ul><li>add permanent province modifier:</li><ul><li>name = aw_eldritch_cultists_1</li><li>duration = -1</li></ul></ul></ul>

___
##At least that's not our problem.

###Available if:
<li>event target:aw eldritch cultists migration target:</li><ul><li>None of the following:</li><ul><li>owned by is event_target:aw_eldritch_cultists_migration_origin_owner</li></ul></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>goto = aw_eldritch_cultists_migration_target</li><li>custom tooltip = aw_eldritch_cultists_migrate_to_other_country_tt</li><li>hidden effect:</li><ul><li>event target:aw eldritch cultists migration target:</li><ul><li>fire province event [aw_eldritch_cultists.14](aw_eldritch_cultists.14_slug) immediately </li></ul></ul></ul>
