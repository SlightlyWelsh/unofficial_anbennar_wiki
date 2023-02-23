#Information
 - Title: Delegation Insulted
 - ID: xia_summit.10
#Description
Delegation Insulted
#Mean Time to Happen:
Base time = 72 months

#Options

___
##Let it go.

###AI weighting:
AI weights this option at 50
 - Multiplied by 5 if has ruler has personality is calm personality, and has ruler has personality is benevolent personality, and has ruler has personality is careful personality, and has ruler has personality is craven personality
 - Multiplied by 0 if has ruler has personality is malevolent personality, and has ruler has personality is naive personality, and has ruler has personality is bold fighter personality


###Efects:<ul><li>add prestige = -5</li></ul>

___
##This insult will not go unanswered. Demand a duel!

###AI weighting:
AI weights this option at 50
 - Multiplied by 5 if has ruler has personality is righteous personality, and has ruler has personality is just personality, and has ruler has personality is inspiring leader personality


###Efects:<ul><li>add prestige = 5</li><li>custom tooltip = xia_duel_choice_tt</li><li>save event target as = xia_duel_instigator</li><li>event target:xia duel target:</li><ul><li>the event [[xia_duel_instigator.GetName] Demands a Duel!](../events/xia_duel_instigator_getname_demands_a_duel.md) happens</li></ul></ul>

___
##Our First Master ought to smooth things over with [xia_duel_target.GetName]

###Available if:
<li>Any of the following:</li><ul><li>ruler has personality is charismatic_negotiator_personality</li><li>ruler has personality  is silver_tongue_personality</li></ul>

###Efects:<ul><li>add prestige = 10</li></ul>
