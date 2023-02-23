#Information
 - Title: Vampires Migrate to [aw_vampires_migration_target.GetName]
 - ID: aw_vampires.10
#Description
Vampires Migrate to [aw_vampires_migration_target.GetName]
#Options

___
##Direct the adventurers to [aw_vampires_migration_target.GetName]!

###Available if:
<li>event target:aw vampires migration target:</li><ul><li>owned by is event_target:aw_vampires_migration_origin_owner</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>goto = aw_vampires_migration_target</li><li>tooltip:</li><ul><li>remove province modifier = aw_vampires_1</li><li>remove province modifier = aw_vampires_2</li><li>remove province modifier = aw_vampires_3</li></ul><li>event target:aw vampires migration target:</li><ul><li>If has ROOT has province modifier is aw vampires 1:</li><ul><li>add permanent province modifier:</li><ul><li>name = aw_vampires_1</li><li>duration = -1</li></ul></ul><li>Else if has ROOT has province modifier is aw vampires 2:</li><ul><li>add permanent province modifier:</li><ul><li>name = aw_vampires_2</li><li>duration = -1</li></ul></ul><li>Else if has ROOT has province modifier is aw vampires 3:</li><ul><li>add permanent province modifier:</li><ul><li>name = aw_vampires_3</li><li>duration = -1</li></ul></ul><li>hidden effect:</li><ul><li>ROOT:</li><ul><li>remove province modifier = aw_vampires_1</li><li>remove province modifier = aw_vampires_2</li><li>remove province modifier = aw_vampires_3</li></ul></ul></ul></ul>

___
##They are no longer our problem, then.

###Available if:
<li>event target:aw vampires migration target:</li><ul><li>None of the following:</li><ul><li>owned by is event_target:aw_vampires_migration_origin_owner</li></ul></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>goto = aw_vampires_migration_target</li><li>tooltip:</li><ul><li>remove province modifier = aw_vampires_1</li><li>remove province modifier = aw_vampires_2</li><li>remove province modifier = aw_vampires_3</li></ul><li>custom tooltip = aw_vampire_migrate_to_other_country_tt</li><li>hidden effect:</li><ul><li>event target:aw vampires migration target:</li><ul><li>fire province event [aw_vampires.11](aw_vampires.11_slug) immediately </li></ul></ul></ul>
