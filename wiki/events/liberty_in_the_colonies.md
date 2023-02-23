#Information
 - Title: Liberty in the Colonies
 - ID: center_of_revolution.4
#Description
Liberty in the Colonies
#Mean Time to Happen:
Base time = 3650 days
 - Multiplied by 0.5 if has treasury is 1000, and does not have num of loans is 1

#Options

___
##Send them some financial aid.

###AI weighting:
AI weights this option at 1
 - Multiplied by 0 if does not have treasury is 500
 - Multiplied by 0 if is at war, and does not have war with is event target:rival country


###Efects:<ul><li>add treasury = -500</li><li>event target:colonial country:</li><ul><li>set country flag [financial_aid](../flags/financial_aid.md)</li></ul><li>event target:rival country:</li><ul><li>the event ˻center_of_revolution.6˼ happens</li></ul><li>event target:colonial country:</li><ul><li>tooltip:</li><ul><li>add treasury = 500</li><li>add liberty desire = 50</li></ul><li>add opinion:</li><ul><li>who = root</li><li>modifier = opinion_funded_independence_war</li></ul><li>hidden effect:</li><ul><li>the event ˻center_of_revolution.5˼ happens</li></ul></ul><li>add revolutionary zeal = 5</li></ul>

___
##Send them other forms of aid.

###AI weighting:
AI weights this option at 1
 - Multiplied by 0 if does not have adm power is 100; and does not have dip power is 100; and does not have mil power is 100
 - Multiplied by 0 if is at war, and does not have war with is event target:rival country


###Efects:<ul><li>add adm power = -100</li><li>add dip power = -100</li><li>add mil power = -100</li><li>event target:colonial country:</li><ul><li>set country flag [mana_aid](../flags/mana_aid.md)</li></ul><li>event target:rival country:</li><ul><li>the event ˻center_of_revolution.6˼ happens</li></ul><li>event target:colonial country:</li><ul><li>tooltip:</li><ul><li>add adm power = 100</li><li>add dip power = 100</li><li>add mil power = 100</li><li>add liberty desire = 50</li></ul><li>add opinion:</li><ul><li>who = root</li><li>modifier = opinion_funded_independence_war</li></ul><li>hidden effect:</li><ul><li>the event ˻center_of_revolution.5˼ happens</li></ul></ul><li>add revolutionary zeal = 5</li></ul>

___
##We are better off focusing our energies elsewhere.

###AI weighting:
AI weights this option at 2


###Efects:<ul><li>add adm power = 35</li><li>add dip power = 35</li><li>add mil power = 35</li><li>event target:colonial country:</li><ul><li>add opinion:</li><ul><li>who = root</li><li>modifier = opinion_refused_to_fund_independence_war</li></ul></ul></ul>
