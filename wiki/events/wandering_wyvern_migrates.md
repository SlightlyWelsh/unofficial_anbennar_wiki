#Information
 - Title: Wandering Wyvern Migrates
 - ID: aw_wyvern.10
#Description
Wandering Wyvern Migrates
#Options

___
##Thank the gods!

###Available if:
<li>event target:aw wyvern migration target:</li><ul><li>owned by is event_target:aw_wyvern_migration_origin_owner</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>goto = aw_wyvern_migration_target</li><li>tooltip:</li><ul><li>remove province modifier = aw_wyvern_1</li><li>remove province modifier = aw_wyvern_2</li></ul><li>event target:aw wyvern migration target:</li><ul><li>tooltip:</li><ul><li>remove province modifier = aw_wyvern_1</li><li>remove province modifier = aw_wyvern_2</li></ul><li>If has ROOT has province modifier is aw wyvern 1:</li><ul><li>add permanent province modifier:</li><ul><li>name = aw_wyvern_1</li><li>duration = -1</li></ul></ul><li>Else if has ROOT has province modifier is aw wyvern 2:</li><ul><li>add permanent province modifier:</li><ul><li>name = aw_wyvern_2</li><li>duration = -1</li></ul></ul><li>hidden effect:</li><ul><li>ROOT:</li><ul><li>remove province modifier = aw_wyvern_1</li><li>remove province modifier = aw_wyvern_2</li></ul></ul></ul></ul>

___
##Let us hope it stays away for good.

###Available if:
<li>event target:aw wyvern migration target:</li><ul><li>None of the following:</li><ul><li>owned by is event_target:aw_wyvern_migration_origin_owner</li></ul></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>goto = aw_wyvern_migration_target</li><li>tooltip:</li><ul><li>remove province modifier = aw_wyvern_1</li><li>remove province modifier = aw_wyvern_2</li></ul><li>custom tooltip = aw_wyvern_migrate_to_other_country_tt</li><li>hidden effect:</li><ul><li>event target:aw wyvern migration target:</li><ul><li>fire province event [aw_wyvern.11](aw_wyvern.11_slug) immediately </li></ul></ul></ul>
