#Information
 - Title: Orcish Warband Migrates
 - ID: aw_orcs.10
#Description
Orcish Warband Migrates
#Options

___
##We will have to move our efforts.

###Available if:
<li>event target:aw orcs migration target:</li><ul><li>owned by is event_target:aw_orcs_migration_origin_owner</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>goto = aw_orcs_migration_target</li><li>tooltip:</li><ul><li>remove province modifier = aw_orcs_1</li><li>remove province modifier = aw_orcs_2</li><li>remove province modifier = aw_orcs_3</li></ul><li>event target:aw orcs migration target:</li><ul><li>If has ROOT has province modifier is aw orcs 1:</li><ul><li>add permanent province modifier:</li><ul><li>name = aw_orcs_1</li><li>duration = -1</li></ul></ul><li>Else if has ROOT has province modifier is aw orcs 2:</li><ul><li>add permanent province modifier:</li><ul><li>name = aw_orcs_2</li><li>duration = -1</li></ul></ul><li>Else if has ROOT has province modifier is aw orcs 3:</li><ul><li>add permanent province modifier:</li><ul><li>name = aw_orcs_3</li><li>duration = -1</li></ul></ul><li>hidden effect:</li><ul><li>ROOT:</li><ul><li>remove province modifier = aw_orcs_1</li><li>remove province modifier = aw_orcs_2</li><li>remove province modifier = aw_orcs_3</li></ul></ul></ul></ul>

___
##They are someone else's problem now.

###Available if:
<li>event target:aw orcs migration target:</li><ul><li>None of the following:</li><ul><li>owned by is event_target:aw_orcs_migration_origin_owner</li></ul></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>goto = aw_orcs_migration_target</li><li>tooltip:</li><ul><li>remove province modifier = aw_orcs_1</li><li>remove province modifier = aw_orcs_2</li><li>remove province modifier = aw_orcs_3</li></ul><li>custom tooltip = aw_orcs_migrate_to_other_country_tt</li><li>hidden effect:</li><ul><li>event target:aw orcs migration target:</li><ul><li>fire province event [aw_orcs.11](aw_orcs.11_slug) immediately </li></ul></ul></ul>
