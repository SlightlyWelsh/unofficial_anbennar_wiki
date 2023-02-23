#Information
 - Title: The Plague of the Dead Spreads to [Root.GetName]
 - ID: aw_zombies.13
#Description
The Plague of the Dead Spreads to [Root.GetName]
#Options

___
##Can nothing be done to bring this situation under control?

###Available if:
<li>event target:aw zombies migration target:</li><ul><li>owned by is event_target:aw_zombies_migration_origin_owner</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>goto = aw_zombies_migration_target</li><li>event target:aw zombies migration target:</li><ul><li>If has ROOT has province modifier is aw zombies 1:</li><ul><li>add permanent province modifier:</li><ul><li>name = aw_zombies_1</li><li>duration = -1</li></ul></ul><li>Else if has ROOT has province modifier is aw zombies 2:</li><ul><li>add permanent province modifier:</li><ul><li>name = aw_zombies_1</li><li>duration = -1</li></ul></ul><li>Else if has ROOT has province modifier is aw zombies 3:</li><ul><li>add permanent province modifier:</li><ul><li>name = aw_zombies_1</li><li>duration = -1</li></ul></ul></ul></ul>

___
##How unfortunate for them.

###Available if:
<li>event target:aw zombies migration target:</li><ul><li>None of the following:</li><ul><li>owned by is event_target:aw_zombies_migration_origin_owner</li></ul></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>goto = aw_zombies_migration_target</li><li>custom tooltip = aw_zombies_migrate_to_other_country_tt</li><li>hidden effect:</li><ul><li>event target:aw zombies migration target:</li><ul><li>fire province event [aw_zombies.14](aw_zombies.14_slug) immediately </li></ul></ul></ul>


#Pages with same name:
The following pages have the same name as this page:
 - [the_plague_of_the_dead_spreads_to_root_getname_1](the_plague_of_the_dead_spreads_to_root_getname_1.md)
