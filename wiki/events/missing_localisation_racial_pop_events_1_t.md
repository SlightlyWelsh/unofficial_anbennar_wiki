#Information
 - Title: Missing localisation: racial_pop_events_1_t
 - ID: racial_pop_events.1
#Description

#Mean Time to Happen:
Base time = 1 days

#Options

___
##Missing localisation: racial_pop_events_1_b

###One of the following randomly happens:
Outcome 1:

Available if <li>event target:racial province:</li><ul><li>has dwarven minority trigger yes</li></ul>

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>event target:racial province:</li><ul><li>remove dwarven minority size effect = yes</li></ul></ul>
Outcome 2:

Available if <li>event target:racial province:</li><ul><li>has elven minority trigger yes</li></ul>

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>event target:racial province:</li><ul><li>remove elven minority size effect = yes</li></ul></ul>
Outcome 3:

Available if <li>event target:racial province:</li><ul><li>has halfling minority trigger yes</li></ul>

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>event target:racial province:</li><ul><li>remove halfling minority size effect = yes</li></ul></ul>

___
##Missing localisation: racial_pop_events_1_c

###AI weighting:
AI weights this option at 50
 - Multiplied by 1.2 if has dlc is "The Cossacks", and  has estate is estate nobles, and does not have estate loyalty has estate is estate nobles, and estate loyalty has loyalty is 40
 - Multiplied by 0.5 if has wants to maintain tolerance elven is yes
 - Multiplied by 0.1 if has wants to increase tolerance elven is yes


###Efects:<ul><li>add mil power = -10</li><li>If has estate is estate nobles:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_nobles</li><li>loyalty = 5</li></ul></ul><li>small decrease of elven tolerance effect = yes</li><li>event target:elven lords province:</li><ul><li>If area has owned by is ROOT, and does not have province modifier is elven local lords; and does not have province modifier is elven local lords punished; and  has elven minority trigger is yes:</li><ul><li>add province modifier:</li><ul><li>name = elven_local_lords_punished</li><li>duration = 3650</li></ul></ul></ul></ul>

___
##Missing localisation: racial_pop_events_1_e

###Available if:
<li>ruler has personality is calm_personality</li>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>highlight = yes</li><li>custom tooltip = racial_pop_events_2_e_tooltip</li></ul>

___
##Missing localisation: racial_pop_events_1_f

###Available if:
<li>Any of the following:</li><ul><li>ruler has personality is embezzler_personality</li><li>ruler has personality  is intricate_web_weaver_personality</li></ul>

###AI weighting:
AI weights this option at 100
 - Multiplied by 1.2 if has dlc is "The Cossacks", and  has estate is estate nobles, and does not have estate loyalty has estate is estate nobles, and estate loyalty has loyalty is 40
 - Multiplied by 0.5 if has wants to maintain tolerance elven is yes
 - Multiplied by 0.1 if has wants to increase tolerance elven is yes


###Efects:<ul><li>highlight = yes</li><li>custom tooltip = racial_pop_events_2_f_tooltip</li><li>add estate nobles loyalty effect = yes</li><li>small decrease of elven tolerance effect = yes</li><li>event target:elven lords province:</li><ul><li>If area has owned by is ROOT, and does not have province modifier is elven local lords; and does not have province modifier is elven local lords punished; and  has elven minority trigger is yes:</li><ul><li>add unrest = -1</li><li>add province modifier:</li><ul><li>name = elven_local_lords_punished</li><li>duration = 1825</li></ul></ul></ul></ul>
