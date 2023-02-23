#Information
 - Title: Treasure Fleet Seeks Repairs
 - ID: treasurefleet.21
#Description
Treasure Fleet Seeks Repairs
#Options

___
##Very well, let us repair their ships!

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.1 if has owner has num of loans is 1


###Efects:<ul><li>owner:</li><ul><li>add treasury = -15</li><li>add prestige = 10</li><li>add dip power = 10</li></ul><li>custom tooltip = JY_LF_fix</li><li>If has global flag is [JY_LF_damage_5](../flags/jy_lf_damage_5.md):</li><ul><li>clr global flag [JY_LF_damage_5](../flags/jy_lf_damage_5.md)</li></ul><li>Else if has global flag is [JY_LF_damage_4](../flags/jy_lf_damage_4.md):</li><ul><li>clr global flag [JY_LF_damage_4](../flags/jy_lf_damage_4.md)</li></ul><li>Else if has global flag is [JY_LF_damage_3](../flags/jy_lf_damage_3.md):</li><ul><li>clr global flag [JY_LF_damage_3](../flags/jy_lf_damage_3.md)</li></ul><li>Else if has global flag is [JY_LF_damage_2](../flags/jy_lf_damage_2.md):</li><ul><li>clr global flag [JY_LF_damage_2](../flags/jy_lf_damage_2.md)</li></ul><li>else:</li><ul><li>clr global flag [JY_LF_damage_1](../flags/jy_lf_damage_1.md)</li></ul><li>JY LF trade = yes</li></ul>

___
##We unfortunately cannot afford the expense.

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>owner:</li><ul><li>add prestige = -5</li></ul><li>JY LF trade = yes</li></ul>

___
##We have the supplies to help!

###Available if:
<li>owner:</li><ul><li>any owned province:</li><ul><li>trade goods is naval_supplies</li></ul></ul>

###AI weighting:
AI weights this option at 500


###Efects:<ul><li>highlight = yes</li><li>owner:</li><ul><li>add prestige = 5</li><li>add dip power = 10</li></ul><li>JY LF trade = yes</li></ul>
