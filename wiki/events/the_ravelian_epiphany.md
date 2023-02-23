#Information
 - Title: The Ravelian Epiphany
 - ID: reformer_dissension.1
#Description
The Ravelian Epiphany
#Options

___
##The Empire's faith shall not be questioned!

###AI weighting:
AI weights this option at 1000
 - Multiplied by 0.5 if has global flag is [incident_reformer_dissension_high_chance](../flags/incident_reformer_dissension_high_chance.md)
 - Multiplied by 0.5 if is part of hre, and has religion is ravelian; and has total own and non tributary subject development is root, and has army size is root
 - Multiplied by 0.01 if has calc true if has amount is 3, and calc true if is part of hre, and has religion is ravelian; and has total own and non tributary subject development is root, and has army size is root
 - Multiplied by 0 if has religion is ravelian, and does not have num of cities is 2; and has any country is part of hre, and any country has religion is ravelian, and is in war has attacker leader is this, and is in war has defenders is root, and is in war has war score is 50; and is in war has defender leader is this, and is in war has attackers is root, and is in war has war score is 50


###Efects:<ul><li>custom tooltip = reformer_dissension.1.A.tt</li><li>hidden effect:</li><ul><li>If every country is part of hre, and  has religion is ravelian, and  is free or tributary trigger is yes:</li><ul><li>add opinion:</li><ul><li>who = root</li><li>modifier = opinion_annoyed_at_hre_protestant</li></ul><li>the event [[Emperor.GetName] Rejects Ravelian Demands!](../events/emperor_getname_rejects_ravelian_demands.md) happens</li></ul></ul></ul>

___
##Grant them equal rights.

###AI weighting:
AI weights this option at 1000
 - Multiplied by 0.01 if does not have part of hre, and has religion is ravelian; and has total own and non tributary subject development is root, and has army size is root
 - Multiplied by 0 if has religion is ravelian, and does not have num of cities is 2; and has any country is part of hre, and any country has religion is ravelian, and is in war has attacker leader is this, and is in war has defenders is root, and is in war has war score is 50; and is in war has defender leader is this, and is in war has attackers is root, and is in war has war score is 50


###Efects:<ul><li>set hre religion treaty = yes</li><li>add imperial influence = -20</li></ul>

___
##We must concede to all demands.

###AI weighting:
AI weights this option at 1000
 - Multiplied by 0.01 if has num of cities is 2, and does not have any country is part of hre, and any country has religion is ravelian, and is in war has attacker leader is this, and is in war has defenders is root, and is in war has war score is 50; and is in war has defender leader is this, and is in war has attackers is root, and is in war has war score is 50


###Efects:<ul><li>set hre religion = ravelian</li><li>custom tooltip = reformer_dissension.1.C.tt</li></ul>
