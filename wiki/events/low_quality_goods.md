#Information
 - Title: Low Quality Goods
 - ID: halfling_tolerance_events.1
#Description
Low Quality Goods
#Options

___
##The merchants are right

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.5 if has wants to maintain tolerance halfling is yes
 - Multiplied by 0.1 if has wants to increase tolerance halfling is yes


###Efects:<ul><li>add dip power = -40</li><li>small decrease of halfling tolerance effect = yes</li><li>event target:poor wares halfling province:</li><ul><li>If area has owned by is ROOT, and does not have province modifier is halfling not allowed to trade; and does not have province modifier is halfling low quality wares:</li><ul><li>add province modifier:</li><ul><li>name = halfling_not_allowed_to_trade</li><li>duration = 730</li></ul></ul></ul><li>If has estate is estate burghers:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_burghers</li><li>loyalty = 5</li></ul></ul><li>Else if has estate is estate castonath patricians:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_castonath_patricians</li><li>loyalty = 5</li></ul></ul></ul>

___
##Let them trade

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.5 if has dlc is "The Cossacks", and  has estate is estate burghers, and does not have estate loyalty has estate is estate burghers, and estate loyalty has loyalty is 40
 - Multiplied by 0.5 if has wants to maintain tolerance halfling is yes
 - Multiplied by 0.1 if has wants to decrease tolerance halfling is yes


###Efects:<ul><li>add prestige = -5</li><li>small increase of halfling tolerance effect = yes</li><li>event target:poor wares halfling province:</li><ul><li>If area has owned by is ROOT, and does not have province modifier is halfling not allowed to trade; and does not have province modifier is halfling low quality wares:</li><ul><li>add province modifier:</li><ul><li>name = halfling_low_quality_wares</li><li>duration = 730</li></ul></ul></ul><li>reduce estate burghers loyalty effect = yes</li></ul>

___
##We need to confiscate their goods

###Available if:
<li>Any of the following:</li><ul><li>ruler has personality is embezzler_personality</li><li>ruler has personality  is greedy_personality</li></ul>

###AI weighting:
AI weights this option at 100
 - Multiplied by 0.5 if has wants to maintain tolerance halfling is yes
 - Multiplied by 0.01 if has wants to increase tolerance halfling is yes


###Efects:<ul><li>highlight = yes</li><li>add years of income = 0.05</li><li>medium decrease of halfling tolerance effect = yes</li><li>event target:poor wares halfling province:</li><ul><li>add unrest = 2</li><li>If area has owned by is ROOT, and does not have province modifier is halfling not allowed to trade; and does not have province modifier is halfling low quality wares:</li><ul><li>add province modifier:</li><ul><li>name = halfling_not_allowed_to_trade</li><li>duration = 730</li></ul></ul></ul><li>If has estate is estate burghers:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_burghers</li><li>loyalty = 5</li></ul></ul><li>Else if has estate is estate castonath patricians:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_castonath_patricians</li><li>loyalty = 5</li></ul></ul></ul>

___
##Compesensate both parties

###Available if:
<li>Any of the following:</li><ul><li>ruler has personality is just_personality</li><li>ruler has personality  is kind_hearted_personality</li></ul>

###AI weighting:
AI weights this option at 100
 - Multiplied by 0.5 if has dlc is "The Cossacks", and  has estate is estate burghers, and does not have estate loyalty has estate is estate burghers, and estate loyalty has loyalty is 40
 - Multiplied by 0.5 if has wants to maintain tolerance halfling is yes
 - Multiplied by 0.1 if has wants to decrease tolerance halfling is yes


###Efects:<ul><li>highlight = yes</li><li>add years of income = -0.15</li><li>small increase of halfling tolerance effect = yes</li><li>If has estate is estate burghers:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_burghers</li><li>loyalty = 5</li></ul></ul><li>Else if has estate is estate castonath patricians:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_castonath_patricians</li><li>loyalty = 5</li></ul></ul></ul>

___
##Get rid of the complainers

###Available if:
<li>Any of the following:</li><ul><li>ruler has personality is cruel_personality</li><li>ruler has personality  is malevolent_personality</li></ul>

###AI weighting:
AI weights this option at 100
 - Multiplied by 0.5 if has dlc is "The Cossacks", and  has estate is estate burghers, and does not have estate loyalty has estate is estate burghers, and estate loyalty has loyalty is 40


###Efects:<ul><li>highlight = yes</li><li>add mil power = -60</li><li>reduce estate burghers loyalty effect = yes</li></ul>
