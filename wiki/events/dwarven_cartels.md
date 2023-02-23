#Information
 - Title: Dwarven Cartels
 - ID: dwarven_tolerance_events.3
#Description
Dwarven Cartels
#Options

___
##Their competence shall be rewarded

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.8 if does not have prestige is 0
 - Multiplied by 0.5 if does not have estate loyalty has estate is estate burghers, and estate loyalty has loyalty is 40
 - Multiplied by 0.5 if has wants to maintain tolerance dwarven is yes
 - Multiplied by 0.1 if has wants to decrease tolerance dwarven is yes


###Efects:<ul><li>add prestige = -5</li><li>small increase of dwarven tolerance effect = yes</li><li>reduce estate burghers loyalty effect = yes</li><li>event target:dwarven guild province:</li><ul><li>If area does not have province modifier is dwarven guilds upset; and does not have province modifier is dwarven guilds given privileges; and  has dwarven minority trigger is yes:</li><ul><li>add province modifier:</li><ul><li>name = dwarven_guilds_given_privileges</li><li>duration = 3650</li></ul></ul></ul></ul>

___
##We sadly cannot agree to this

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>event target:dwarven guild province:</li><ul><li>If area does not have province modifier is dwarven guilds upset; and does not have province modifier is dwarven guilds given privileges; and  has dwarven minority trigger is yes:</li><ul><li>add province modifier:</li><ul><li>name = dwarven_guilds_upset</li><li>duration = 1825</li></ul></ul></ul></ul>

___
##Outrageous! No dwarf deserves such privileges

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.5 if has wants to maintain tolerance dwarven is yes
 - Multiplied by 0.1 if has wants to increase tolerance dwarven is yes


###Efects:<ul><li>add prestige = 5</li><li>small decrease of dwarven tolerance effect = yes</li><li>event target:dwarven guild province:</li><ul><li>If area does not have province modifier is dwarven guilds upset; and does not have province modifier is dwarven guilds given privileges; and  has dwarven minority trigger is yes:</li><ul><li>add province modifier:</li><ul><li>name = dwarven_guilds_upset</li><li>duration = 3650</li></ul></ul></ul></ul>
