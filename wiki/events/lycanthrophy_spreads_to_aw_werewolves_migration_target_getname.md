#Information
 - Title: Lycanthrophy Spreads to [aw_werewolves_migration_target.GetName]
 - ID: aw_werewolves.13
#Description
Lycanthrophy Spreads to [aw_werewolves_migration_target.GetName]
#Options

___
##We must contain them!

###Available if:
<li>event target:aw werewolves migration target:</li><ul><li>owned by is event_target:aw_werewolves_migration_origin_owner</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>goto = aw_werewolves_migration_target</li><li>event target:aw werewolves migration target:</li><ul><li>add permanent province modifier:</li><ul><li>name = aw_werewolves_2</li><li>duration = -1</li></ul></ul></ul>

___
##Not my wolf, not my problem.

###Available if:
<li>event target:aw werewolves migration target:</li><ul><li>None of the following:</li><ul><li>owned by is event_target:aw_werewolves_migration_origin_owner</li></ul></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>goto = aw_werewolves_migration_target</li><li>custom tooltip = aw_werewolves_migrate_to_other_country_tt</li><li>hidden effect:</li><ul><li>event target:aw werewolves migration target:</li><ul><li>fire province event [aw_werewolves.14](aw_werewolves.14_slug) in 14 days</li></ul></ul></ul>
