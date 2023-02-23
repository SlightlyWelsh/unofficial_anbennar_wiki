#Information
 - Title: Unhappiness Among the Peasantry
 - ID: 5052
#Description
Unhappiness Among the Peasantry
#Mean Time to Happen:
Base time = 1 days
 - Multiplied by 2.0 if has wartaxes
 - Multiplied by 0.5 if is lucky
 - Multiplied by 0.66 if has stability is 3, and  has revolt percentage is 0

#Options

___
##We rule as we see fit!

###AI weighting:
AI weights this option at 55
 - Multiplied by 0.5 if does not have stability is 1


###Efects:<ul><li>add prestige = 10</li><li>If does not have stability is -2:</li><ul><li>add adm power = -100</li></ul><li>If has stability is -2:</li><ul><li>add stability = -1</li></ul></ul>

___
##Try to improve their situation.

###AI weighting:
AI weights this option at 45
 - Multiplied by 0.5 if does not have years of income is 0.3


###Efects:<ul><li>add years of income = -0.25</li><li>If has country flag is [tyrant_system_initialized](../flags/tyrant_system_initialized.md):</li><ul><li>increase tyrant benevolent 1 = yes</li></ul></ul>

___
##Crush these troublemakers!

###Available if:
<li>ruler has personality is cruel_personality</li>

###Efects:<ul><li>goto = uppity_peasants_province</li><li>highlight = yes</li><li>event target:uppity peasants province:</li><ul><li>spawn small scaled rebels:</li><ul><li>type = anti_tax_rebels</li><li>no defined leader = yes</li></ul></ul><li>If has country flag is [tyrant_system_initialized](../flags/tyrant_system_initialized.md):</li><ul><li>increase tyrant ruthless 1 = yes</li></ul></ul>
