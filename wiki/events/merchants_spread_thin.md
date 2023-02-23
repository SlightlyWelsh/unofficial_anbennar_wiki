#Information
 - Title: Merchants Spread Thin
 - ID: 863
#Description
Merchants Spread Thin
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Haless is not as important.

###Available if:
<li>any active trade node:</li><ul><li>continent is asia</li><li>has merchant PREV</li><li>None of the following:</li><ul><li>has trade modifier:</li><ul><li>this nation</li><li>name is merchant_recalled</li></ul></ul></ul>

###AI weighting:
AI weights this option at 33


###Efects:<ul><li>goto = asia_node</li><li>If random active trade node has continent is asia, and  has merchant is PREV, and does not have trade modifier has who is ROOT, and has trade modifier has name is merchant recalled:</li><ul><li>add trade modifier:</li><ul><li>who = root</li><li>duration = 3650</li><li>power = -10</li><li>key = merchant_recalled</li></ul></ul></ul>

___
##We can ignore Cannor.

###Available if:
<li>any active trade node:</li><ul><li>continent is europe</li><li>has merchant PREV</li><li>None of the following:</li><ul><li>has trade modifier:</li><ul><li>this nation</li><li>name is merchant_recalled</li></ul></ul></ul>

###AI weighting:
AI weights this option at 33


###Efects:<ul><li>goto = europe_node</li><li>If random active trade node has continent is europe, and  has merchant is PREV, and does not have trade modifier has who is ROOT, and has trade modifier has name is merchant recalled:</li><ul><li>add trade modifier:</li><ul><li>who = root</li><li>duration = 3650</li><li>power = -10</li><li>key = merchant_recalled</li></ul></ul></ul>

___
##Support them anyway!

###AI weighting:
AI weights this option at 33
 - Multiplied by 1.5 if has estate is estate burghers, and does not have estate loyalty has estate is estate burghers, and estate loyalty has loyalty is 30


###Efects:<ul><li>add dip power = -20</li><li>add estate burghers loyalty effect = yes</li></ul>
