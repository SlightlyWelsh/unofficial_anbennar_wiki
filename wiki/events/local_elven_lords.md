#Information
 - Title: Local Elven Lords
 - ID: elven_tolerance_events.2
#Description
Local Elven Lords
#Mean Time to Happen:
Base time = 1 days

#Options

___
##A lord is a lord

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.5 if has dlc is "The Cossacks", and  has estate is estate nobles, and does not have estate loyalty has estate is estate nobles, and estate loyalty has loyalty is 40
 - Multiplied by 0.5 if has wants to maintain tolerance elven is yes
 - Multiplied by 0.1 if has wants to decrease tolerance elven is yes


###Efects:<ul><li>add prestige = 10</li><li>reduce legitimacy small effect = yes</li><li>reduce estate nobles loyalty effect = yes</li><li>small increase of elven tolerance effect = yes</li><li>event target:elven lords province:</li><ul><li>If area has owned by is ROOT, and does not have province modifier is elven local lords; and does not have province modifier is elven local lords punished; and  has elven minority trigger is yes:</li><ul><li>add province modifier:</li><ul><li>name = elven_local_lords</li><li>duration = 3650</li></ul></ul></ul></ul>

___
##Obviously these claims are fake

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.8 if has legitimacy is 75


###Efects:<ul><li>add prestige = -10</li><li>increase legitimacy small effect = yes</li></ul>

___
##Punish them for these lies

###AI weighting:
AI weights this option at 50
 - Multiplied by 1.2 if has dlc is "The Cossacks", and  has estate is estate nobles, and does not have estate loyalty has estate is estate nobles, and estate loyalty has loyalty is 40
 - Multiplied by 0.5 if has wants to maintain tolerance elven is yes
 - Multiplied by 0.1 if has wants to increase tolerance elven is yes


###Efects:<ul><li>add mil power = -10</li><li>If has estate is estate nobles:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_nobles</li><li>loyalty = 5</li></ul></ul><li>small decrease of elven tolerance effect = yes</li><li>event target:elven lords province:</li><ul><li>If area has owned by is ROOT, and does not have province modifier is elven local lords; and does not have province modifier is elven local lords punished; and  has elven minority trigger is yes:</li><ul><li>add province modifier:</li><ul><li>name = elven_local_lords_punished</li><li>duration = 3650</li></ul></ul></ul></ul>

___
##Explain their duties

###Available if:
<li>ruler has personality is calm_personality</li>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>highlight = yes</li><li>custom tooltip = elven_tolerance_events_2_e_tooltip</li></ul>

___
##These documents are fake!

###Available if:
<li>Any of the following:</li><ul><li>ruler has personality is embezzler_personality</li><li>ruler has personality  is intricate_web_weaver_personality</li></ul>

###AI weighting:
AI weights this option at 100
 - Multiplied by 1.2 if has dlc is "The Cossacks", and  has estate is estate nobles, and does not have estate loyalty has estate is estate nobles, and estate loyalty has loyalty is 40
 - Multiplied by 0.5 if has wants to maintain tolerance elven is yes
 - Multiplied by 0.1 if has wants to increase tolerance elven is yes


###Efects:<ul><li>highlight = yes</li><li>custom tooltip = elven_tolerance_events_2_f_tooltip</li><li>add estate nobles loyalty effect = yes</li><li>small decrease of elven tolerance effect = yes</li><li>event target:elven lords province:</li><ul><li>If area has owned by is ROOT, and does not have province modifier is elven local lords; and does not have province modifier is elven local lords punished; and  has elven minority trigger is yes:</li><ul><li>add unrest = -1</li><li>add province modifier:</li><ul><li>name = elven_local_lords_punished</li><li>duration = 1825</li></ul></ul></ul></ul>
