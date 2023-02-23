#Information
 - Title: Age Draws Suspicion
 - ID: vampire_ruler.1
#Description
Age Draws Suspicion
#Mean Time to Happen:
Base time = 10 years

#Options

___
##Fortunately I already have an heir

###Available if:
<li>has country flag [vampire_heir](../flags/vampire_heir.md)</li>

###AI weighting:
AI weights this option at 10


###Efects:<ul><li>clr country flag [vampire_heir](../flags/vampire_heir.md)</li><li>clr country flag [vampire_ruler](../flags/vampire_ruler.md)</li><li>exile ruler as:</li><ul><li>name = cannot_return</li></ul><li>If does not have heir:</li><ul><li>define ruler:</li><ul><li>dynasty = ROOT</li><li>age = 17</li><li>change adm = 1</li><li>change dip = 1</li><li>change mil = 1</li><li>hide skills = yes</li><li>claim = 80</li></ul></ul><li>set country flag [new_vampire](../flags/new_vampire.md)</li><li>ruler become vampire = yes</li></ul>

___
##I grow tired of ruling, perhaps I should step down.

###Available if:
<li>None of the following:</li><ul><li>has country flag [vampire_heir](../flags/vampire_heir.md)</li></ul>

###Efects:<ul><li>hidden effect:</li><ul><li>clear ruler vampire flags = yes</li></ul><li>If does not have heir:</li><ul><li>define heir:</li><ul><li>dynasty = ROOT</li><li>age = 17</li><li>hide skills = yes</li><li>claim = 80</li></ul></ul><li>exile ruler as:</li><ul><li>name = cannot_return</li></ul></ul>

___
##I will fake my own death!

###AI weighting:
AI weights this option at 10


###Efects:<ul><li>hidden effect:</li><ul><li>If does not have heir:</li><ul><li>define heir:</li><ul><li>dynasty = ROOT</li><li>age = 17</li><li>hide skills = yes</li><li>claim = 80</li></ul><li>define ruler:</li><ul><li>dynasty = ROOT</li><li>age = 17</li><li>change adm = 1</li><li>change dip = 1</li><li>change mil = 1</li><li>hide skills = yes</li><li>claim = 80</li></ul></ul></ul><li>facade suspicion decrease 10 = yes</li><li>If has ruler flag is [transmutation_3](../flags/transmutation_3.md), and has ruler flag is illusion 3:</li><ul><li>facade suspicion decrease 10 = yes</li></ul><li>Else if has ruler flag is [transmutation_2](../flags/transmutation_2.md), and has ruler flag is illusion 2:</li><ul><li>facade suspicion decrease 5 = yes</li></ul><li>Else if has ruler flag is [transmutation_1](../flags/transmutation_1.md), and has ruler flag is illusion 1:</li><ul><li>facade suspicion decrease 2 = yes</li></ul><li>add adm power = -100</li><li>save ruler stats = yes</li><li>kill ruler = yes</li><li>reset vampire age = yes</li></ul>

___
##I will never step down!

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>facade suspicion increase 10 = yes</li></ul>

___
##Perhaps I should adjust their memories of me

###Available if:
<li>has ruler flag [enchantment_3](../flags/enchantment_3.md)</li>

###AI weighting:
AI weights this option at 10


###Efects:<ul><li>facade suspicion increase 1 = yes</li></ul>
