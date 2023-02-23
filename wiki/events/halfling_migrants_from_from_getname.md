#Information
 - Title: Halfling Migrants From [From.GetName]
 - ID: racial_pop_events_halfling.9
#Description
Halfling Migrants From [From.GetName]
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Welcome to [racial_pop_province_target.GetName]!

###Available if:


###AI weighting:
AI weights this option at 50
 - Multiplied by 1.5 if has wants to increase tolerance halfling is yes
 - Multiplied by 2 if has high tolerance halfling race trigger is yes
 - Multiplied by 2 if is colonial nation, and is subject of is ROOT
 - Multiplied by 2 if has ruler has personality is tolerant personality, and has ruler has personality is kind hearted personality, and has ruler has personality is benevolent personality
 - Multiplied by 3 if has idea group is humanist ideas


###Efects:<ul><li>event target:racial pop province target:</li><ul><li>add halfling minority size effect = yes</li></ul><li>If has has large halfling minority trigger is yes, and has halfling majority trigger is yes:</li><ul><li>event target:racial pop province target:</li><ul><li>random:</li><ul><li>chance = 50</li><li>add base production = 1</li></ul></ul></ul></ul>

___
##They can settle... for a price

###Available if:


###AI weighting:
AI weights this option at 50
 - Multiplied by 1.5 if has wants to decrease tolerance halfling is yes
 - Multiplied by 1.5 if is bankrupt
 - Multiplied by 2 if has ruler has personality is greedy personality
 - Multiplied by 1.5 if has personal deity is ara


###Efects:<ul><li>add years of income = 0.1</li><li>event target:racial pop province target:</li><ul><li>add halfling minority size effect = yes</li></ul><li>If has has large halfling minority trigger is yes, and has halfling majority trigger is yes:</li><ul><li>event target:racial pop province target:</li><ul><li>random:</li><ul><li>chance = 50</li><li>add base production = 1</li></ul></ul></ul><li>small decrease of halfling tolerance effect = yes</li></ul>

___
##Get out of here!

###Available if:


###AI weighting:
AI weights this option at 50
 - Multiplied by 1.5 if has wants to decrease tolerance halfling is yes
 - Multiplied by 2 if has low tolerance halfling race trigger is yes
 - Multiplied by 2 if has ruler has personality is malevolent personality, and has ruler has personality is cruel personality
 - Multiplied by 1.5 if has ruler has personality is careful personality
 - Multiplied by 3 if has country modifier is racial pop halfling purge, and has country modifier is racial pop halfling expulsion


###Efects:<ul><li>add mil power = -10</li><li>small decrease of halfling tolerance effect = yes</li></ul>
