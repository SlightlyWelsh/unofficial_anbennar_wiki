#Information
 - Title: The Prejudices of Rulers
 - ID: diggy.758
#Description
The Prejudices of Rulers
#Options

___
##Long are our memories as well. We will brook no tolerance to these squatters.

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>If has estate is estate nobles:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_nobles</li><li>loyalty = 10</li></ul></ul><li>Else if has estate is estate burghers:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_burghers</li><li>loyalty = 10</li></ul></ul><li>else:</li><ul><li>add prestige = 10</li></ul><li>event target:province:</li><ul><li>add unrest = 5</li><li>If has goblin minority trigger is yes:</li><ul><li>ROOT:</li><ul><li>medium decrease of goblin tolerance effect = yes</li></ul></ul><li>If has orcish minority trigger is yes:</li><ul><li>ROOT:</li><ul><li>medium decrease of orcish tolerance effect = yes</li></ul></ul></ul></ul>

___
##And how did such things aid Aul Dwarov? We must carve a new path.

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>If has estate is estate nobles:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_nobles</li><li>loyalty = -10</li></ul><li>If has estate influence has estate is estate nobles, and estate influence has influence is 50:</li><ul><li>reduce stability or adm power = yes</li></ul></ul><li>Else if has estate is estate burghers:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_burghers</li><li>loyalty = -10</li></ul><li>If has estate influence has estate is estate burghers, and estate influence has influence is 50:</li><ul><li>reduce stability or adm power = yes</li></ul></ul><li>else:</li><ul><li>add prestige = -10</li><li>reduce stability or adm power = yes</li></ul></ul>
