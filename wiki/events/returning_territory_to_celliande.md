#Information
 - Title: Returning Territory to Celliande?
 - ID: flavor_sugamber.21
#Description
Returning Territory to Celliande?
#Options

___
##They can have Hawkshot, we still have a coastline without it.

###Available if:
<li>owns 410</li>

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>410:</li><ul><li>cede province = A56</li><li>remove core = A48</li></ul></ul>

___
##Give them Irmathmas, if we don't have any ports we can't get raided by pirates.

###Available if:
<li>owns 411</li>

###AI weighting:
AI weights this option at 21


###Efects:<ul><li>411:</li><ul><li>cede province = A56</li><li>remove core = A48</li></ul><li>A56:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = A48_gave_important_province</li></ul></ul></ul>

___
##Fulfill all their claims.

###Available if:
<li>owns 410</li><li>owns  411</li>

###AI weighting:
AI weights this option at 10


###Efects:<ul><li>410:</li><ul><li>cede province = A56</li><li>remove core = A48</li></ul><li>411:</li><ul><li>cede province = A56</li><li>remove core = A48</li></ul><li>A56:</li><ul><li>add historical friend = A48</li><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = A48_gave_important_province</li></ul></ul></ul>

___
##Pay them in cash.

###AI weighting:
AI weights this option at 10
 - Multiplied by 0.1 if has num of loans is 2
 - Multiplied by 3 if does not have owns is 410
 - Multiplied by 3 if does not have owns is 411


###Efects:<ul><li>add years of income = -1</li><li>A56:</li><ul><li>the event ˻flavor_sugamber.22˼ happens</li></ul></ul>

___
##Haha! Did they really think we'd pay them back.

###AI weighting:
AI weights this option at 21


###Efects:<ul><li>A56:</li><ul><li>add historical rival = A48</li><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = A48_didnt_paid_us_back</li></ul></ul></ul>
