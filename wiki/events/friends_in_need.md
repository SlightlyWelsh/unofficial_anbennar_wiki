#Information
 - Title: Friends in Need
 - ID: consort_events.57
#Description
Friends in Need
#Options

___
##We can surely spare some coin for our [From.GetAdjective] friends.

###Available if:
<li>FROM:</li><ul><li>has country flag [asked_consort_for_money](../flags/asked_consort_for_money.md)</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 1.25 if has opinion has who is FROM, and has opinion has value is 150
 - Multiplied by 0.5 if does not have opinion has who is FROM, and has opinion has value is 100
 - Multiplied by 0 if does not have opinion has who is FROM, and has opinion has value is 50


###Efects:<ul><li>If does not have check variable has which is money to give, and check variable has value is 25:</li><ul><li>add treasury = -10</li></ul><li>If has check variable has which is money to give, and check variable has value is 25; and does not have check variable has which is money to give, and check variable has value is 50:</li><ul><li>add treasury = -25</li></ul><li>If has check variable has which is money to give, and check variable has value is 50; and does not have check variable has which is money to give, and check variable has value is 100:</li><ul><li>add treasury = -50</li></ul><li>If has check variable has which is money to give, and check variable has value is 100; and does not have check variable has which is money to give, and check variable has value is 250:</li><ul><li>add treasury = -100</li></ul><li>If has check variable has which is money to give, and check variable has value is 250:</li><ul><li>add treasury = -250</li></ul><li>FROM:</li><ul><li>the event [A Helping Hand](../events/a_helping_hand.md) happens</li></ul><li>reverse add opinion:</li><ul><li>who = FROM</li><li>modifier = grateful_for_aid</li></ul></ul>

___
##We will send some of our best administrators to help them.

###Available if:
<li>FROM:</li><ul><li>has country flag [asked_consort_for_adm](../flags/asked_consort_for_adm.md)</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 1.25 if has opinion has who is FROM, and has opinion has value is 150
 - Multiplied by 0.5 if does not have opinion has who is FROM, and has opinion has value is 100
 - Multiplied by 0 if does not have opinion has who is FROM, and has opinion has value is 50


###Efects:<ul><li>add adm power = -25</li><li>FROM:</li><ul><li>the event [A Helping Hand](../events/a_helping_hand.md) happens</li></ul><li>reverse add opinion:</li><ul><li>who = FROM</li><li>modifier = grateful_for_aid</li></ul></ul>

___
##A couple of our most talented diplomats will be sent to aid them.

###Available if:
<li>FROM:</li><ul><li>has country flag [asked_consort_for_dip](../flags/asked_consort_for_dip.md)</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 1.25 if has opinion has who is FROM, and has opinion has value is 150
 - Multiplied by 0.5 if does not have opinion has who is FROM, and has opinion has value is 100
 - Multiplied by 0 if does not have opinion has who is FROM, and has opinion has value is 50


###Efects:<ul><li>add dip power = -25</li><li>FROM:</li><ul><li>the event [A Helping Hand](../events/a_helping_hand.md) happens</li></ul><li>reverse add opinion:</li><ul><li>who = FROM</li><li>modifier = grateful_for_aid</li></ul></ul>

___
##One of our best generals will be sent to teach them about our methods.

###Available if:
<li>FROM:</li><ul><li>has country flag [asked_consort_for_mil](../flags/asked_consort_for_mil.md)</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 1.25 if has opinion has who is FROM, and has opinion has value is 150
 - Multiplied by 0.5 if does not have opinion has who is FROM, and has opinion has value is 100
 - Multiplied by 0 if does not have opinion has who is FROM, and has opinion has value is 50


###Efects:<ul><li>add mil power = -25</li><li>FROM:</li><ul><li>the event [A Helping Hand](../events/a_helping_hand.md) happens</li></ul><li>reverse add opinion:</li><ul><li>who = FROM</li><li>modifier = grateful_for_aid</li></ul></ul>

___
##Some able-bodied men shall be sent to [From.GetName] in their time of need.

###Available if:
<li>FROM:</li><ul><li>has country flag [asked_consort_for_manpower](../flags/asked_consort_for_manpower.md)</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 1.25 if has opinion has who is FROM, and has opinion has value is 150
 - Multiplied by 0.5 if does not have opinion has who is FROM, and has opinion has value is 100
 - Multiplied by 0 if does not have opinion has who is FROM, and has opinion has value is 50
 - Multiplied by 0 if does not have max manpower is 10


###Efects:<ul><li>If does not have check variable has which is manpower to send, and check variable has value is 0.5:</li><ul><li>add manpower = -0.1</li></ul><li>If has check variable has which is manpower to send, and check variable has value is 0.5; and does not have check variable has which is manpower to send, and check variable has value is 1:</li><ul><li>add manpower = -0.5</li></ul><li>If has check variable has which is manpower to send, and check variable has value is 1; and does not have check variable has which is manpower to send, and check variable has value is 2.5:</li><ul><li>add manpower = -1</li></ul><li>If has check variable has which is manpower to send, and check variable has value is 2.5; and does not have check variable has which is manpower to send, and check variable has value is 5:</li><ul><li>add manpower = -2.5</li></ul><li>If has check variable has which is manpower to send, and check variable has value is 5:</li><ul><li>add manpower = -5</li></ul><li>FROM:</li><ul><li>the event [A Helping Hand](../events/a_helping_hand.md) happens</li></ul><li>reverse add opinion:</li><ul><li>who = FROM</li><li>modifier = grateful_for_aid</li></ul></ul>

___
##And what would we get in return? No, never!

###AI weighting:
AI weights this option at 50
 - Multiplied by 10.0 if does not have opinion has who is FROM, and has opinion has value is -50
 - Multiplied by 0.5 if does not have opinion has who is FROM, and has opinion has value is 100
 - Multiplied by 0 if has opinion has who is FROM, and has opinion has value is 150


###Efects:<ul><li>reverse add opinion:</li><ul><li>who = FROM</li><li>modifier = denied_aid</li></ul><li>add opinion:</li><ul><li>who = FROM</li><li>modifier = outrageous_demands</li></ul><li>FROM:</li><ul><li>the event [Broken Promises](../events/broken_promises.md) happens</li></ul></ul>
