#Information
 - Title: Orcish Revolt
 - ID: orcish_tolerance_events.4
#Description
Orcish Revolt
#Options

___
##The Savages!

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.1 if has wants to increase tolerance orcish is yes


###Efects:<ul><li>event target:orcish revolt province:</li><ul><li>If has orcish minority trigger is yes:</li><ul><li>spawn rebels:</li><ul><li>size = 1</li><li>type = anti_tax_rebels</li></ul></ul><li>else:</li><ul><li>spawn rebels:</li><ul><li>size = 1</li><li>type = nationalist_rebels</li></ul></ul></ul><li>medium decrease of orcish tolerance effect = yes</li></ul>

___
##Grant them some autonomy.

###Available if:
<li>None of the following:</li><ul><li>has country modifier racial_pop_orcish_purge</li><li>has country modifier  racial_pop_orcish_expulsion</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.5 if has wants to maintain tolerance orcish is yes
 - Multiplied by 0.1 if has wants to decrease tolerance orcish is yes


###Efects:<ul><li>event target:orcish revolt province:</li><ul><li>add local autonomy = 50</li></ul><li>small increase of orcish tolerance effect = yes</li></ul>
