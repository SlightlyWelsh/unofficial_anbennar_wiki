#Information
 - Title: Rotten Boroughs
 - ID: parlaments.2
#Description
Rotten Boroughs
#Mean Time to Happen:
Base time = 200 months
 - Multiplied by 0.8 if does not have development is 6
 - Multiplied by 0.7 if does not have development is 4

#Options

___
##Rotten!

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>owner:</li><ul><li>add corruption = 0.5</li></ul><li>custom tooltip = "parlaments.2.a.tt"</li><li>add province modifier:</li><ul><li>name = "rotten_borough"</li><li>duration = -1</li></ul></ul>

___
##We must reassign the seat.

###AI weighting:
AI weights this option at 50
 - Multiplied by 4 if has owner has num of owned provinces with has value is 2, and num of owned provinces with has province modifier is "rotten borough"


###Efects:<ul><li>goto = envious_province</li><li>set seat in parliament = no</li><li>event target:envious province:</li><ul><li>set seat in parliament = yes</li></ul><li>owner:</li><ul><li>add stability = -1</li></ul><li>add province modifier:</li><ul><li>name = "withdrawn_parliamentary_seat"</li><li>duration = 3650</li></ul></ul>


#Pages with same name:
The following pages have the same name as this page:
 - [rotten_boroughs_1](rotten_boroughs_1.md)
