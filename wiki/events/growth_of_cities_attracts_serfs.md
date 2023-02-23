#Information
 - Title: Growth of Cities attracts Serfs
 - ID: 725
#Description
Growth of Cities attracts Serfs
#Mean Time to Happen:
Base time = 1 days
 - Multiplied by 0.5 if is lucky

#Options

___
##We have to accept this.

###AI weighting:
AI weights this option at 50
 - Multiplied by 0 if has estate is estate nobles, and does not have estate loyalty has estate is estate nobles, and estate loyalty has loyalty is 30


###Efects:<ul><li>goto = rural_province</li><li>event target:rural province:</li><ul><li>add base tax = -1</li><li>add local autonomy = 25</li></ul><li>capital scope:</li><ul><li>add base tax = 1</li></ul><li>reduce estate nobles loyalty effect = yes</li></ul>

___
##The serfs belong on their turf.

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>add estate nobles loyalty effect = yes</li><li>country gets the modifier serfdom_modifier for 20 years</li><li>If has country flag is [tyrant_system_initialized](../flags/tyrant_system_initialized.md):</li><ul><li>increase tyrant ruthless 1 = yes</li></ul></ul>

___
##Let's keep calm and ensure no damage is done.

###Available if:
<li>ruler has personality ancestor:</li><ul><li>key is calm</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>highlight = yes</li><li>goto = rural_province</li><li>event target:rural province:</li><ul><li>add local autonomy = 25</li></ul><li>capital scope:</li><ul><li>add base tax = 1</li></ul><li>If has country flag is [tyrant_system_initialized](../flags/tyrant_system_initialized.md):</li><ul><li>increase tyrant benevolent 1 = yes</li></ul></ul>
