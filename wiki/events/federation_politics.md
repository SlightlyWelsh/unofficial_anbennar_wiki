#Information
 - Title: Federation Politics
 - ID: fed_politics.1
#Description
Federation Politics
#Options

___
##Request Federation Aid

###AI weighting:
AI weights this option at 50
 - Multiplied by 0 if does not have federation has high standing is yes
 - Multiplied by 0 if has stability is 2


###Efects:<ul><li>lake federation lose 2 points = yes</li><li>lake federation lose 1 politics = yes</li><li>add adm power = 25</li><li>add dip power = 25</li><li>add mil power = 25</li><li>tooltip:</li><ul><li>random:</li><ul><li>chance = 20</li><li>add stability or adm power = yes</li></ul></ul><li>hidden effect:</li><ul><li>the event [Missing localisation: fed_politics_100_t](../events/missing_localisation_fed_politics_100_t.md) happens</li></ul><li>If is controlled by the AI:</li><ul><li>add stability or adm power = yes</li></ul><li>hidden effect:</li><ul><li>set country flag [recent_federation_politic](../flags/recent_federation_politic.md)</li></ul></ul>

___
##Share Granaries

###Available if:
<li>None of the following:</li><ul><li>has country modifier federation_shared_granaries</li></ul><li>any neighbor country:</li><ul><li>has country modifier lake_federation_member</li><li>None of the following:</li><ul><li>is rival is this nation</li></ul></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>lake federation lose 1 politics = yes</li><li>lake federation gain 1 points = yes</li><li>country gets the modifier federation_shared_granaries for 5 years</li><li>If random neighbor country has country modifier is lake federation member, and does not have rival is ROOT:</li><ul><li>hidden effect:</li><ul><li>add yearly manpower = 1</li></ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = federation_pos_intrigue</li></ul></ul><li>hidden effect:</li><ul><li>set country flag [recent_federation_politic](../flags/recent_federation_politic.md)</li></ul></ul>

___
##Scholarly Cooperation

###Available if:
<li>any neighbor country:</li><ul><li>has country modifier lake_federation_member</li><li>None of the following:</li><ul><li>has country modifier federation_shared_institution</li></ul><li>ROOT:</li><ul><li>institution difference:</li><ul><li>PREV</li><li>value is at least 1</li></ul></ul></ul>

###AI weighting:
AI weights this option at 1000


###Efects:<ul><li>lake federation lose 1 politics = yes</li><li>lake federation gain 2 points = yes</li><li>add dip power = -75</li><li>If random neighbor country has country modifier is lake federation member, and does not have country modifier is federation shared institution; and  has ROOT has institution difference has who is PREV, and institution difference has value is 1:</li><ul><li>country gets the modifier federation_shared_institution for 10 years</li><li>capital scope:</li><ul><li>add next institution embracement = 50</li></ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = federation_pos_intrigue</li></ul></ul><li>hidden effect:</li><ul><li>set country flag [recent_federation_politic](../flags/recent_federation_politic.md)</li></ul></ul>

___
##Exile Troublemaker

###Available if:
<li>Any of the following:</li><ul><li>average unrest is at least 1</li><li>None of the following:</li><ul><li>stability is at least 0</li></ul></ul><li>manpower is at least 4</li><li>None of the following:</li><ul><li>has country modifier federation_exiled_troublemaker</li></ul><li>5284:</li><ul><li>owner:</li><ul><li>has country modifier lake_federation_member</li></ul></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 0 if has stability is 2
 - Multiplied by 0 if does not have manpower percentage is 0.5


###Efects:<ul><li>lake federation lose 1 politics = yes</li><li>country gets the modifier federation_exiled_troublemaker for 10 years</li><li>hidden effect:</li><ul><li>the event [Missing localisation: fed_politics_101_t](../events/missing_localisation_fed_politics_101_t.md) happens</li></ul><li>tooltip:</li><ul><li>random list:</li><ul><li>40:</li><ul><li>add manpower = -1</li><li>hidden effect:</li><ul><li>set country flag [manpower_1](../flags/manpower_1.md)</li></ul><li>5284:</li><ul><li>owner:</li><ul><li>the event [[From.GetName] troublemaker!](../events/from_getname_troublemaker.md) happens</li></ul></ul></ul><li>30:</li><ul><li>add manpower = -2</li><li>hidden effect:</li><ul><li>set country flag [manpower_2](../flags/manpower_2.md)</li></ul><li>5284:</li><ul><li>owner:</li><ul><li>the event [[From.GetName] troublemaker!](../events/from_getname_troublemaker.md) happens</li></ul></ul></ul><li>20:</li><ul><li>add manpower = -3</li><li>hidden effect:</li><ul><li>set country flag [manpower_3](../flags/manpower_3.md)</li></ul><li>5284:</li><ul><li>owner:</li><ul><li>the event [[From.GetName] troublemaker!](../events/from_getname_troublemaker.md) happens</li></ul></ul></ul><li>10:</li><ul><li>add manpower = -4</li><li>hidden effect:</li><ul><li>set country flag [manpower_4](../flags/manpower_4.md)</li></ul><li>5284:</li><ul><li>owner:</li><ul><li>the event [[From.GetName] troublemaker!](../events/from_getname_troublemaker.md) happens</li></ul></ul></ul></ul></ul><li>hidden effect:</li><ul><li>the event [Missing localisation: fed_politics_102_t](../events/missing_localisation_fed_politics_102_t.md) happens</li></ul><li>tooltip:</li><ul><li>random list:</li><ul><li>40:</li><ul><li>add stability or adm power = yes</li></ul><li>55:</li><ul></ul><li>5:</li><ul><li>trigger:</li><ul><li>ai = no</li></ul><li>reduce stability or adm power = yes</li></ul></ul></ul><li>hidden effect:</li><ul><li>set country flag [recent_federation_politic](../flags/recent_federation_politic.md)</li></ul></ul>

___
##Go Back

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>If is controlled by the AI:</li><ul><li>country gets the modifier fed_assembly_house_cooldown for 180 days</li></ul></ul>
