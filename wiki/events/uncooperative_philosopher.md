#Information
 - Title: Uncooperative Philosopher
 - ID: 5086
#Description
Uncooperative Philosopher
#Mean Time to Happen:
Base time = 1 days
 - Multiplied by 2.0 if does not have innovativeness ideas is 3
 - Multiplied by 0.5 if is lucky
 - Multiplied by 0.66 if has innovativeness ideas is 4

#Options

___
##Imprison $PHILOSOPHER_O_PRONOUN$.

###AI weighting:
AI weights this option at 60
 - Multiplied by 0.5 if does not have stability is 1


###Efects:<ul><li>If does not have stability is -2:</li><ul><li>add adm power = -100</li></ul><li>If has stability is -2:</li><ul><li>add stability = -1</li></ul><li>add estate church loyalty effect = yes</li><li>remove advisor by category = ADM</li></ul>

___
##Allow $PHILOSOPHER_O_PRONOUN$ to remain free.

###AI weighting:
AI weights this option at 40
 - Multiplied by 0.5 if does not have prestige is 50
 - Multiplied by 0 if has estate is estate church, and does not have estate loyalty has estate is estate church, and estate loyalty has loyalty is 30


###Efects:<ul><li>add prestige = -10</li><li>reduce estate church loyalty effect = yes</li><li>If has exists is Z97:</li><ul><li>Z97:</li><ul><li>add opinion:</li><ul><li>who = root</li><li>modifier = opinion_heretical_philosopher</li></ul></ul></ul></ul>

___
##[Root.Adm_Advisor.GetSheHeCap]'s got some interesting ideas actually!

###Available if:
<li>ruler has personality ancestor:</li><ul><li>key is free_thinker</li></ul>

###Efects:<ul><li>highlight = yes</li><li>add adm power = 25</li><li>add prestige = -10</li><li>reduce estate church loyalty effect = yes</li><li>If has exists is Z97:</li><ul><li>Z97:</li><ul><li>add opinion:</li><ul><li>who = root</li><li>modifier = opinion_heretical_philosopher</li></ul></ul></ul></ul>
