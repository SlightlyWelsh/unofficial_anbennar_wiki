#Information
 - Title: Bandit King's Demesne Expands
 - ID: aw_bandits.13
#Description
Bandit King's Demesne Expands
#Options

___
##Damn the king!

###Available if:
<li>event target:aw bandits migration target:</li><ul><li>owned by is event_target:aw_bandits_migration_origin_owner</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>goto = aw_bandits_migration_target</li><li>event target:aw bandits migration target:</li><ul><li>add permanent province modifier:</li><ul><li>name = aw_bandits_1</li><li>duration = -1</li></ul></ul></ul>

___
##Good luck and good riddance!

###Available if:
<li>event target:aw bandits migration target:</li><ul><li>None of the following:</li><ul><li>owned by is event_target:aw_bandits_migration_origin_owner</li></ul></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>goto = aw_bandits_migration_target</li><li>custom tooltip = aw_bandits_migrate_to_other_country_tt</li><li>hidden effect:</li><ul><li>event target:aw bandits migration target:</li><ul><li>fire province event [aw_bandits.14](aw_bandits.14_slug) immediately </li></ul></ul></ul>
