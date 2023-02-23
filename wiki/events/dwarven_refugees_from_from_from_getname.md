#Information
 - Title: Dwarven Refugees From [From.From.GetName]
 - ID: racial_pop_events_dwarven.11
#Description
Dwarven Refugees From [From.From.GetName]
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Let those poor souls in!

###Available if:


###AI weighting:
AI weights this option at 50
 - Multiplied by 1.5 if has wants to increase tolerance dwarven is yes
 - Multiplied by 2 if has high tolerance dwarven race trigger is yes
 - Multiplied by 2 if is colonial nation, and is subject of is ROOT
 - Multiplied by 2 if has ruler has personality is tolerant personality, and has ruler has personality is kind hearted personality, and has ruler has personality is benevolent personality
 - Multiplied by 3 if has idea group is humanist ideas


###Efects:<ul><li>event target:racial pop province target:</li><ul><li>add dwarven minority size effect = yes</li><li>add local autonomy = 10</li></ul><li>If has has large dwarven minority trigger is yes, and has dwarven majority trigger is yes:</li><ul><li>event target:racial pop province target:</li><ul><li>random:</li><ul><li>chance = 50</li><li>add base production = 1</li></ul></ul></ul><li>small increase of dwarven tolerance effect = yes</li></ul>

___
##Confiscate what they have in return

###Available if:


###AI weighting:
AI weights this option at 50
 - Multiplied by 1.5 if has wants to decrease tolerance dwarven is yes
 - Multiplied by 1.5 if is bankrupt
 - Multiplied by 2 if has ruler has personality is greedy personality
 - Multiplied by 1.5 if has personal deity is ara


###Efects:<ul><li>add years of income = 0.15</li><li>event target:racial pop province target:</li><ul><li>add dwarven minority size effect = yes</li><li>add local autonomy = 10</li></ul><li>If has has large dwarven minority trigger is yes, and has dwarven majority trigger is yes:</li><ul><li>event target:racial pop province target:</li><ul><li>random:</li><ul><li>chance = 50</li><li>add base production = 1</li></ul></ul></ul><li>medium decrease of dwarven tolerance effect = yes</li></ul>

___
##Prevent entry with force, if necessary

###Available if:


###AI weighting:
AI weights this option at 50
 - Multiplied by 1.5 if has wants to decrease tolerance dwarven is yes
 - Multiplied by 2 if has low tolerance dwarven race trigger is yes
 - Multiplied by 2 if has ruler has personality is malevolent personality, and has ruler has personality is cruel personality
 - Multiplied by 1.5 if has ruler has personality is careful personality
 - Multiplied by 3 if has country modifier is racial pop dwarven purge, and has country modifier is racial pop dwarven expulsion


###Efects:<ul><li>random:</li><ul><li>chance = 50</li><li>event target:racial pop province target:</li><ul><li>add dwarven minority size effect = yes</li><li>add local autonomy = 10</li></ul><li>If has has large dwarven minority trigger is yes, and has dwarven majority trigger is yes:</li><ul><li>event target:racial pop province target:</li><ul><li>random:</li><ul><li>chance = 50</li><li>add base production = 1</li></ul></ul></ul></ul><li>add mil power = -30</li><li>large decrease of dwarven tolerance effect = yes</li></ul>
