#Information
 - Title: [Emperor.GetName] Rejects Ravelian Demands!
 - ID: reformer_dissension.2
#Description
[Emperor.GetName] Rejects Ravelian Demands!
#Options

___
##Our future is still in the Empire.

###AI weighting:
AI weights this option at 1
 - Multiplied by 0.5 if has global flag is [incident_reformer_dissension_high_chance](../flags/incident_reformer_dissension_high_chance.md)


###Efects:<ul><li>add stability = -1</li><li>add imperial influence = 10</li></ul>

___
##We are better off outside of it.

###AI weighting:
AI weights this option at 2
 - Multiplied by 0 if has reform is free city
 - Multiplied by 0.75 if does not have num of cities is 10
 - Multiplied by 0.5 if does not have num of cities is 4
 - Multiplied by 0.5 if does not have num of cities is 2
 - Multiplied by 0.5 if does not have num of cities is 2
 - Multiplied by 0.25 if has alliance with is event target:Emperor
 - Multiplied by 2 if is rival is event target:Emperor, and has event target:Emperor is rival is root
 - Multiplied by 10 if has total own and non tributary subject development is event target:Emperor, and has army size is event target:Emperor


###Efects:<ul><li>event target:Emperor:</li><ul><li>add opinion:</li><ul><li>who = root</li><li>modifier = opinion_abandoned_hre</li></ul></ul><li>set in empire = no</li><li>If every subject country is part of hre, and  is free or tributary trigger is no:</li><ul><li>set in empire = no</li></ul></ul>
