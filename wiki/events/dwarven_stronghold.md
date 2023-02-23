#Information
 - Title: Dwarven Stronghold
 - ID: dwarven_tolerance_events.2
#Description
Dwarven Stronghold
#Options

___
##They can have the land for now

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.8 if does not have prestige is 0
 - Multiplied by 0.5 if has wants to maintain tolerance dwarven is yes
 - Multiplied by 0.1 if has wants to decrease tolerance dwarven is yes


###Efects:<ul><li>add prestige = -10</li><li>small increase of dwarven tolerance effect = yes</li><li>event target:dwarven stronghold province:</li><ul><li>add local autonomy = 5</li><li>add province modifier:</li><ul><li>name = dwarven_independent_stronghold_prov</li><li>duration = 3650</li></ul></ul></ul>

___
##Buy the land back immediately

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.8 if does not have years of income is 0.2
 - Multiplied by 0.8 if does not have years of income is 0.4


###Efects:<ul><li>add years of income = -0.2</li></ul>

___
##Send in the military, that land is rightfully ours

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.8 if does not have manpower percentage is 0.33
 - Multiplied by 0.5 if has wants to maintain tolerance dwarven is yes
 - Multiplied by 0.1 if has wants to increase tolerance dwarven is yes


###Efects:<ul><li>add mil power = -50</li><li>If has max manpower is 20:</li><ul><li>add manpower = -1</li></ul><li>If does not have max manpower is 20:</li><ul><li>add yearly manpower = -0.5</li></ul><li>small decrease of dwarven tolerance effect = yes</li><li>event target:dwarven stronghold province:</li><ul><li>add province modifier:</li><ul><li>name = dwarven_independent_stronghold_attacked_prov</li><li>duration = 1825</li></ul></ul></ul>

___
##This is an opportunity in disguise

###Available if:
<li>ruler has personality is entrepreneur_personality</li>

###AI weighting:
AI weights this option at 100
 - Multiplied by 0.8 if does not have years of income is 0.1
 - Multiplied by 0.8 if does not have years of income is 0.2
 - Multiplied by 0.5 if has wants to maintain tolerance dwarven is yes
 - Multiplied by 0.1 if has wants to decrease tolerance dwarven is yes


###Efects:<ul><li>highlight = yes</li><li>add years of income = -0.1</li><li>small increase of dwarven tolerance effect = yes</li><li>event target:dwarven stronghold province:</li><ul><li>add local autonomy = 3</li><li>add province modifier:</li><ul><li>name = dwarven_independent_stronghold_deal_prov</li><li>duration = 3650</li></ul></ul></ul>
