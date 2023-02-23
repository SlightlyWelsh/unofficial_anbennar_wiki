#Information
 - Title: Goblin Horde Splits Up
 - ID: aw_goblins.13
#Description
Goblin Horde Splits Up
#Options

___
##At least they are divided now

###Available if:
<li>event target:aw goblins migration target:</li><ul><li>owned by is event_target:aw_goblins_migration_origin_owner</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>goto = aw_goblins_migration_target</li><li>remove province modifier = aw_goblins_3</li><li>add permanent province modifier:</li><ul><li>name = aw_goblins_2</li><li>duration = -1</li></ul><li>event target:aw goblins migration target:</li><ul><li>add permanent province modifier:</li><ul><li>name = aw_goblins_1</li><li>duration = -1</li></ul></ul></ul>

___
##Good riddance!

###Available if:
<li>event target:aw goblins migration target:</li><ul><li>None of the following:</li><ul><li>owned by is event_target:aw_goblins_migration_origin_owner</li></ul></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>goto = aw_goblins_migration_target</li><li>remove province modifier = aw_goblins_3</li><li>add permanent province modifier:</li><ul><li>name = aw_goblins_2</li><li>duration = -1</li></ul><li>custom tooltip = aw_goblins_migrate_to_other_country_tt</li><li>hidden effect:</li><ul><li>event target:aw goblins migration target:</li><ul><li>fire province event [aw_goblins.14](aw_goblins.14_slug) immediately </li></ul></ul></ul>
