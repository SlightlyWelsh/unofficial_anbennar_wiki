#Information
 - Title: Elven Refugees From [From.GetName]
 - ID: racial_pop_events_elven.10
#Description
Elven Refugees From [From.GetName]
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Let them in

###Available if:


###AI weighting:
AI weights this option at 50
 - Multiplied by 1.5 if has wants to increase tolerance elven is yes
 - Multiplied by 2 if has high tolerance elven race trigger is yes
 - Multiplied by 2 if is colonial nation, and is subject of is ROOT
 - Multiplied by 2 if has ruler has personality is tolerant personality, and has ruler has personality is kind hearted personality, and has ruler has personality is benevolent personality
 - Multiplied by 3 if has idea group is humanist ideas


###Efects:<ul><li>event target:racial pop province target:</li><ul><li>add elven minority size effect = yes</li><li>add local autonomy = 10</li></ul><li>If has has large elven minority trigger is yes, and has elven majority trigger is yes:</li><ul><li>event target:racial pop province target:</li><ul><li>random:</li><ul><li>chance = 50</li><li>add base production = 1</li></ul></ul></ul><li>small increase of elven tolerance effect = yes</li></ul>

___
##Confiscate their valuables in return

###Available if:


###AI weighting:
AI weights this option at 50
 - Multiplied by 1.5 if has wants to decrease tolerance elven is yes
 - Multiplied by 1.5 if is bankrupt
 - Multiplied by 2 if has ruler has personality is greedy personality
 - Multiplied by 1.5 if has personal deity is ara


###Efects:<ul><li>add years of income = 0.2</li><li>event target:racial pop province target:</li><ul><li>add elven minority size effect = yes</li><li>add local autonomy = 10</li></ul><li>If has has large elven minority trigger is yes, and has elven majority trigger is yes:</li><ul><li>event target:racial pop province target:</li><ul><li>random:</li><ul><li>chance = 50</li><li>add base production = 1</li></ul></ul></ul><li>medium decrease of elven tolerance effect = yes</li></ul>

___
##There's no room for you here!

###Available if:


###AI weighting:
AI weights this option at 50
 - Multiplied by 1.5 if has wants to decrease tolerance elven is yes
 - Multiplied by 2 if has low tolerance elven race trigger is yes
 - Multiplied by 2 if has ruler has personality is malevolent personality, and has ruler has personality is cruel personality
 - Multiplied by 1.5 if has ruler has personality is careful personality
 - Multiplied by 3 if has country modifier is racial pop elven purge, and has country modifier is racial pop elven expulsion


###Efects:<ul><li>If does not have country modifier is racial pop elven purge; and does not have country modifier is racial pop elven expulsion:</li><ul><li>event target:racial pop migration country:</li><ul><li>the event [Elven Refugees From [From.From.GetName]](../events/elven_refugees_from_from_from_getname.md) happens</li></ul></ul><li>add mil power = -20</li><li>medium decrease of elven tolerance effect = yes</li></ul>
