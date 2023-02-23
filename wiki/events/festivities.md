#Information
 - Title: Festivities
 - ID: 6015
#Description
Festivities
#Mean Time to Happen:
Base time = 1 days
 - Multiplied by 2.0 if has adm is 5
 - Multiplied by 2.0 if is lucky
 - Multiplied by 0.66 if does not have production efficiency is 0.5

#Options

___
##Arrange festivities.

###Available if:
<li>None of the following:</li><ul><li>stability is at least 3</li></ul>

###AI weighting:
AI weights this option at 30
 - Multiplied by 0 if has stability is 2


###Efects:<ul><li>add stability or adm power = yes</li></ul>

___
##Such nonsense, wasting money like that!

###AI weighting:
AI weights this option at 70


###Efects:<ul><li>goto = random_province</li><li>event target:random province:</li><ul><li>add base tax = 1</li></ul></ul>

___
##The [Root.Monarch.GetTitle] wishes to combine this with an opulent feast.

###Available if:
<li>ruler has personality is drunkard_personality</li>

###Efects:<ul><li>highlight = yes</li><li>add stability or adm power = yes</li><li>If random neighbor country does not have war with is ROOT:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = indulgent_feast</li></ul></ul><li>If random neighbor country does not have war with is ROOT:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = indulgent_feast</li></ul></ul></ul>
