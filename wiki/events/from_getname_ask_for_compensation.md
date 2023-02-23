#Information
 - Title: [From.GetName] ask for compensation
 - ID: goldisland.6
#Description
[From.GetName] ask for compensation
#Options

___
##Give them more than they asked!

###Available if:
<li>if:</li><ul><li>limit:</li><ul><li>FROM:</li><ul><li>has country flag [asked_manpower](../flags/asked_manpower.md)</li></ul></ul><li>manpower is at least 3</li></ul>

###AI weighting:
AI weights this option at 20
 - Multiplied by 0 if is rival is FROM
 - Multiplied by 0 if has FROM has country flag is [asked_money](../flags/asked_money.md); and  has num of loans is 3


###Efects:<ul><li>If has FROM has country flag is [asked_money](../flags/asked_money.md):</li><ul><li>add treasury = -150</li></ul><li>Else if has FROM has country flag is [asked_mana](../flags/asked_mana.md):</li><ul><li>add dip power = -60</li><li>add mil power = -60</li><li>add adm power = -60</li></ul><li>Else if has FROM has country flag is [asked_manpower](../flags/asked_manpower.md):</li><ul><li>add manpower = -3</li></ul><li>FROM:</li><ul><li>hidden effect:</li><ul><li>set country flag [given_big](../flags/given_big.md)</li></ul><li>add opinion:</li><ul><li>modifier = federation_pos_intrigue</li><li>who = ROOT</li></ul><li>add opinion:</li><ul><li>modifier = federation_pos_intrigue</li><li>who = ROOT</li></ul><li>add opinion:</li><ul><li>modifier = federation_pos_intrigue</li><li>who = ROOT</li></ul><li>the event [[From.GetName] response](../events/from_getname_response.md) happens</li></ul></ul>

___
##They ask, they receive

###Available if:
<li>if:</li><ul><li>limit:</li><ul><li>FROM:</li><ul><li>has country flag [asked_manpower](../flags/asked_manpower.md)</li></ul></ul><li>manpower is at least 2</li></ul>

###AI weighting:
AI weights this option at 30
 - Multiplied by 0 if is rival is FROM
 - Multiplied by 0 if has FROM has country flag is [asked_money](../flags/asked_money.md); and  has num of loans is 4


###Efects:<ul><li>If has FROM has country flag is [asked_money](../flags/asked_money.md):</li><ul><li>add treasury = -100</li></ul><li>Else if has FROM has country flag is [asked_mana](../flags/asked_mana.md):</li><ul><li>add dip power = -40</li><li>add mil power = -40</li><li>add adm power = -40</li></ul><li>Else if has FROM has country flag is [asked_manpower](../flags/asked_manpower.md):</li><ul><li>add manpower = -2</li></ul><li>FROM:</li><ul><li>hidden effect:</li><ul><li>set country flag [given_medium](../flags/given_medium.md)</li></ul><li>add opinion:</li><ul><li>modifier = federation_pos_intrigue</li><li>who = ROOT</li></ul><li>add opinion:</li><ul><li>modifier = federation_pos_intrigue</li><li>who = ROOT</li></ul><li>the event [[From.GetName] response](../events/from_getname_response.md) happens</li></ul></ul>

___
##We can spare some...

###Available if:
<li>if:</li><ul><li>limit:</li><ul><li>FROM:</li><ul><li>has country flag [asked_manpower](../flags/asked_manpower.md)</li></ul></ul><li>manpower is at least 1</li></ul>

###AI weighting:
AI weights this option at 40
 - Multiplied by 0 if is rival is FROM
 - Multiplied by 0 if has FROM has country flag is [asked_money](../flags/asked_money.md); and  has num of loans is 5


###Efects:<ul><li>If has FROM has country flag is [asked_money](../flags/asked_money.md):</li><ul><li>add treasury = -50</li></ul><li>Else if has FROM has country flag is [asked_mana](../flags/asked_mana.md):</li><ul><li>add dip power = -20</li><li>add mil power = -20</li><li>add adm power = -20</li></ul><li>Else if has FROM has country flag is [asked_manpower](../flags/asked_manpower.md):</li><ul><li>add manpower = -1</li></ul><li>FROM:</li><ul><li>hidden effect:</li><ul><li>set country flag [given_low](../flags/given_low.md)</li></ul><li>add opinion:</li><ul><li>modifier = federation_pos_intrigue</li><li>who = ROOT</li></ul><li>the event [[From.GetName] response](../events/from_getname_response.md) happens</li></ul></ul>

___
##Nothing for them

###AI weighting:
AI weights this option at 20
 - Multiplied by 100 if has FROM has country flag is [asked_mana](../flags/asked_mana.md); and  has any known country has tech difference is 3
 - Multiplied by 100 if has FROM has country flag is [asked_money](../flags/asked_money.md); and  has num of loans is 10


###Efects:<ul><li>FROM:</li><ul><li>hidden effect:</li><ul><li>set country flag [given_nothing](../flags/given_nothing.md)</li></ul><li>add opinion:</li><ul><li>modifier = federation_neg_intrigue</li><li>who = ROOT</li></ul><li>add opinion:</li><ul><li>modifier = federation_neg_intrigue</li><li>who = ROOT</li></ul><li>the event [[From.GetName] response](../events/from_getname_response.md) happens</li></ul></ul>
