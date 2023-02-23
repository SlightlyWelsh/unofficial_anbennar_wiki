#Information
 - Title: Good Government Policies
 - ID: 5040
#Description
Good Government Policies
#Mean Time to Happen:
Base time = 1 days
 - Multiplied by 2.0 if has advisor is statesman
 - Multiplied by 2.0 if is lucky

#Options

___
##Use the money to increase stability.

###AI weighting:
AI weights this option at 40
 - Multiplied by 2 if does not have stability is 0


###Efects:<ul><li>add stability or adm power = yes</li></ul>

___
##Invest the money in our government.

###AI weighting:
AI weights this option at 30


###Efects:<ul><li>If has completed all reforms trigger is yes, and is primitives:</li><ul><li>add adm power = 25</li><li>add dip power = 25</li><li>add mil power = 25</li></ul><li>else:</li><ul><li>add reform progress small effect = yes</li></ul></ul>

___
##Let's fill our treasury.

###AI weighting:
AI weights this option at 30
 - Multiplied by 2 if has num of cities is 30


###Efects:<ul><li>add years of income = 0.20</li></ul>

___
##Root out the corruption in our government.

###Available if:
<li>ruler has personality ancestor:</li><ul><li>key is incorruptible</li></ul><li>corruption is at least 1</li>

###Efects:<ul><li>highlight = yes</li><li>add corruption = -1</li></ul>

___
##Improve the officer training curriculum.

###Available if:
<li>ruler has personality ancestor:</li><ul><li>key is martial_educator</li></ul>

###Efects:<ul><li>highlight = yes</li><li>add army tradition = 10</li></ul>

___
##The [Root.Monarch.GetTitle] wishes to hold an opulent feast...

###Available if:
<li>ruler has personality is drunkard_personality</li><li>any neighbor country:</li><ul><li>None of the following:</li><ul><li>war with is this nation</li></ul></ul>

###Efects:<ul><li>highlight = yes</li><li>If random neighbor country does not have war with is ROOT:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = indulgent_feast</li></ul><li>If random neighbor country does not have war with is ROOT; and does not have tag is ROOT:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = indulgent_feast</li></ul></ul></ul></ul>

___
##Allow the [Root.Monarch.GetTitle] to personally oversee the diverting of funds.

###Available if:
<li>ruler has personality is embezzler_personality</li>

###Efects:<ul><li>highlight = yes</li><li>add years of income = 0.25</li></ul>

___
##This is a perfect time for one of our [Root.Monarch.GetTitle]'s little projects.

###Available if:
<li>ruler has personality is obsessive_perfectionist_personality</li>

###Efects:<ul><li>highlight = yes</li><li>add prestige = 10</li></ul>
