#Information
 - Title: Unhappiness Among the Artisans
 - ID: 5051
#Description
Unhappiness Among the Artisans
#Mean Time to Happen:
Base time = 1 days
 - Multiplied by 2.0 if has aristocracy ideas is 7
 - Multiplied by 0.5 if is lucky
 - Multiplied by 0.66 if has stability is 3

#Options

___
##Execute the troublemakers.

###AI weighting:
AI weights this option at 55
 - Multiplied by 0.5 if does not have stability is 1
 - Multiplied by 0 if has estate is estate burghers, and does not have estate loyalty has estate is estate burghers, and estate loyalty has loyalty is 30
 - Multiplied by 0 if has estate is estate vaisyas, and does not have estate loyalty has estate is estate burghers, and estate loyalty has loyalty is 30


###Efects:<ul><li>reduce estate burghers loyalty effect = yes</li><li>If does not have stability is -2:</li><ul><li>add adm power = -100</li></ul><li>If has stability is -2:</li><ul><li>add stability = -1</li></ul><li>If has country flag is [tyrant_system_initialized](../flags/tyrant_system_initialized.md):</li><ul><li>increase tyrant ruthless 1 = yes</li></ul></ul>

___
##Abolish a tax.

###AI weighting:
AI weights this option at 45
 - Multiplied by 0.5 if does not have num of cities is 15
 - Multiplied by 0.5 if does not have years of income is 0.5


###Efects:<ul><li>add years of income = -0.50</li><li>add estate burghers loyalty effect = yes</li><li>If has country flag is [tyrant_system_initialized](../flags/tyrant_system_initialized.md):</li><ul><li>increase tyrant benevolent 1 = yes</li></ul></ul>

___
##Crush these troublemakers!

###Available if:
<li>ruler has personality is cruel_personality</li>

###Efects:<ul><li>highlight = yes</li><li>add years of income = 0.1</li><li>event target:uppity artisans province:</li><ul><li>spawn small scaled rebels:</li><ul><li>type = anti_tax_rebels</li><li>no defined leader = yes</li></ul></ul><li>If has country flag is [tyrant_system_initialized](../flags/tyrant_system_initialized.md):</li><ul><li>increase tyrant ruthless 1 = yes</li></ul></ul>

___
##Encourage them to go into other businesses.

###Available if:
<li>ruler has personality ancestor:</li><ul><li>key is entrepreneur</li></ul>

###Efects:<ul><li>highlight = yes</li><li>add prestige = -10</li><li>reduce estate burghers loyalty effect = yes</li></ul>

___
##Complaints indicate a lack of devotion to their work.

###Available if:
<li>ruler has personality is obsessive_perfectionist_personality</li>

###Efects:<ul><li>highlight = yes</li><li>add prestige = -5</li><li>reduce estate burghers loyalty effect = yes</li></ul>
