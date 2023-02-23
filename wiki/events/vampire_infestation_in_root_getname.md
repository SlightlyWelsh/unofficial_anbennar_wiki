#Information
 - Title: Vampire Infestation in [Root.GetName]
 - ID: aw_vampires.13
#Description
Vampire Infestation in [Root.GetName]
#Options

___
##We're going to need more hunters.

###Available if:
<li>event target:aw vampires migration target:</li><ul><li>owned by is event_target:aw_vampires_migration_origin_owner</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>goto = aw_vampires_migration_target</li><li>event target:aw vampires migration target:</li><ul><li>add permanent province modifier:</li><ul><li>name = aw_vampires_1</li><li>duration = -1</li></ul></ul></ul>

___
##Doesn't seem to be our problem.

###Available if:
<li>event target:aw vampires migration target:</li><ul><li>None of the following:</li><ul><li>owned by is event_target:aw_vampires_migration_origin_owner</li></ul></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>goto = aw_vampires_migration_target</li><li>custom tooltip = aw_vampire_migrate_to_other_country_tt</li><li>hidden effect:</li><ul><li>event target:aw vampires migration target:</li><ul><li>fire province event [aw_vampires.14](aw_vampires.14_slug) immediately </li></ul></ul></ul>
