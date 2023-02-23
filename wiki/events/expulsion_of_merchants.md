#Information
 - Title: Expulsion of Merchants
 - ID: trade.3
#Description
Expulsion of Merchants
#Mean Time to Happen:
Base time = 1 days

#Options

___
##They stay!

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>If random active trade node has merchant is PREV, and does not have most province trade power has tag is ROOT:</li><ul><li>most province trade power:</li><ul><li>add opinion:</li><ul><li>who = root</li><li>modifier = merchants_too_succesful</li></ul></ul><li>add trade modifier:</li><ul><li>who = root</li><li>duration = 365</li><li>power = 5</li><li>key = merchants_too_succesful</li></ul></ul></ul>

___
##The merchants will keep a lower profile

###Efects:<ul><li>If random active trade node does not have most province trade power has tag is ROOT; and  has merchant is PREV:</li><ul><li>most province trade power:</li><ul><li>add opinion:</li><ul><li>who = root</li><li>modifier = merchants_standing_down</li></ul></ul><li>add trade modifier:</li><ul><li>who = root</li><li>duration = 365</li><li>power = -5</li><li>key = merchants_standing_down</li></ul></ul></ul>
