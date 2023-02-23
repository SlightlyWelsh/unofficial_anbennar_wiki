#Information
 - Title: Returning Territory to Bisan?
 - ID: flavor_sugamber.20
#Description
Returning Territory to Bisan?
#Options

___
##They can have Gnollsgate, the gnolls only make trouble anyway.

###Available if:
<li>owns 913</li>

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>913:</li><ul><li>cede province = A34</li><li>remove core = A48</li></ul></ul>

___
##Give them Countsbridge.

###Available if:
<li>owns 315</li>

###AI weighting:
AI weights this option at 20


###Efects:<ul><li>315:</li><ul><li>cede province = A34</li><li>remove core = A48</li></ul><li>A34:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = A48_gave_important_province</li></ul></ul></ul>

___
##Fullfill all their claims.

###Available if:
<li>owns 913</li><li>owns  315</li>

###AI weighting:
AI weights this option at 10


###Efects:<ul><li>913:</li><ul><li>cede province = A34</li><li>remove core = A48</li></ul><li>315:</li><ul><li>cede province = A34</li><li>remove core = A48</li></ul><li>A34:</li><ul><li>add historical friend = A48</li><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = A48_gave_important_province</li></ul></ul></ul>

___
##Pay them in cash.

###AI weighting:
AI weights this option at 10
 - Multiplied by 0.1 if has num of loans is 2
 - Multiplied by 3 if does not have owns is 913
 - Multiplied by 3 if does not have owns is 315


###Efects:<ul><li>add years of income = -1</li><li>A34:</li><ul><li>the event ˻flavor_sugamber.22˼ happens</li></ul></ul>

___
##Haha! Did they really think we'd pay them back.

###AI weighting:
AI weights this option at 20


###Efects:<ul><li>A34:</li><ul><li>add historical rival = A48</li><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = A48_didnt_paid_us_back</li></ul></ul></ul>
