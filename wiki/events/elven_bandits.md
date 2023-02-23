#Information
 - Title: Elven Bandits
 - ID: elven_tolerance_events.3
#Description
Elven Bandits
#Mean Time to Happen:
Base time = 1 days

#Options

___
##This is an issue we can ignore

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.8 if does not have prestige is 0
 - Multiplied by 0.5 if has dlc is "The Cossacks", and  has estate is estate nobles, and does not have estate loyalty has estate is estate nobles, and estate loyalty has loyalty is 40
 - Multiplied by 0.5 if has dlc is "The Cossacks", and  has estate is estate burghers, and does not have estate loyalty has estate is estate burghers, and estate loyalty has loyalty is 40


###Efects:<ul><li>add prestige = -5</li><li>reduce estate nobles loyalty effect = yes</li><li>reduce estate burghers loyalty effect = yes</li><li>event target:elven bandit province:</li><ul><li>If area has owned by is ROOT, and does not have province modifier is elven bandits punished; and does not have province modifier is elven bandits run free; and does not have province modifier is elven bandits run free gov support; and  has elven minority trigger is yes:</li><ul><li>add province modifier:</li><ul><li>name = elven_bandits_run_free</li><li>duration = 1825</li></ul></ul></ul></ul>

___
##We need to punish them!

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.5 if has wants to maintain tolerance elven is yes
 - Multiplied by 0.1 if has wants to increase tolerance elven is yes


###Efects:<ul><li>add mil power = -10</li><li>If has estate is estate nobles:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_nobles</li><li>loyalty = 5</li></ul></ul><li>If has estate is estate burghers:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_burghers</li><li>loyalty = 5</li></ul></ul><li>small decrease of elven tolerance effect = yes</li><li>event target:elven bandit province:</li><ul><li>If area has owned by is ROOT, and does not have province modifier is elven bandits punished; and does not have province modifier is elven bandits run free; and does not have province modifier is elven bandits run free gov support; and  has elven minority trigger is yes:</li><ul><li>add province modifier:</li><ul><li>name = elven_bandits_punished</li><li>duration = 1825</li></ul></ul></ul></ul>

___
##They could collect our taxes

###Available if:
<li>None of the following:</li><ul><li>has country modifier minority_bandits_run_free_gov_support_global</li></ul><li>ruler has personality is embezzler_personality</li>

###AI weighting:
AI weights this option at 100
 - Multiplied by 0.8 if does not have prestige is 0
 - Multiplied by 0.5 if has dlc is "The Cossacks", and  has estate is estate nobles, and does not have estate loyalty has estate is estate nobles, and estate loyalty has loyalty is 45
 - Multiplied by 0.5 if has dlc is "The Cossacks", and  has estate is estate burghers, and does not have estate loyalty has estate is estate burghers, and estate loyalty has loyalty is 45


###Efects:<ul><li>highlight = yes</li><li>add prestige = -10</li><li>If has estate is estate nobles:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_nobles</li><li>loyalty = -15</li></ul></ul><li>If has estate is estate burghers:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_burghers</li><li>loyalty = -15</li></ul></ul><li>country gets the modifier minority_bandits_run_free_gov_support_global for 3 years</li><li>event target:elven bandit province:</li><ul><li>If area has owned by is ROOT, and does not have province modifier is elven bandits punished; and does not have province modifier is elven bandits run free; and does not have province modifier is elven bandits run free gov support:</li><ul><li>add province modifier:</li><ul><li>name = elven_bandits_run_free_gov_support</li><li>duration = 1825</li></ul></ul></ul></ul>
