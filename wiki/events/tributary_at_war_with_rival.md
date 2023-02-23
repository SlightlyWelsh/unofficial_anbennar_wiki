#Information
 - Title: Tributary at War With Rival
 - ID: tributary_events.30
#Description
Tributary at War With Rival
#Mean Time to Happen:
Base time = 300 months
 - Multiplied by 0.66 if does not have at war
 - Multiplied by 0.5 if has any subject country is subject of type is tributary state, and does not have country modifier is overlord military mission; and any subject country has any country is enemy is ROOT, and any country has defensive war with is PREV; and does not have manpower is 1

#Options

___
##We must send everything we can spare!

###AI weighting:
AI weights this option at 20
 - Multiplied by 0 if does not have manpower is 0.2, and does not have years of income is 0.3
 - Multiplied by 0 if has num of loans is 1
 - Multiplied by 0 if is at war, and does not have war score is -15
 - Multiplied by 0.5 if is at war
 - Multiplied by 0.5 if does not have manpower is 0.4; and  has years of income is 0.3
 - Multiplied by 2 if has manpower is 0.6, and  has years of income is 0.3
 - Multiplied by 2 if has manpower is 0.8, and  has years of income is 0.3
 - Multiplied by 1.5 if has manpower is 0.6, and  has years of income is 0.5
 - Multiplied by 2 if has manpower is 0.8, and  has years of income is 1


###Efects:<ul><li>hidden effect:</li><ul><li>event target:tributary warring rival:</li><ul><li>set country flag [overlord_all_the_support](../flags/overlord_all_the_support.md)</li><li>the event [Overlord Sends Military Mission](../events/overlord_sends_military_mission.md) happens</li></ul></ul><li>add mil power = -50</li><li>add yearly manpower = -1</li><li>add years of income = -0.5</li><li>event target:tributary warring rival:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = overlord_military_aid</li></ul></ul><li>tooltip:</li><ul><li>event target:tributary warring rival:</li><ul><li>add yearly manpower = 2</li><li>add years of income = 1</li><li>overlord:</li><ul><li>add trust:</li><ul><li>who = ROOT</li><li>value = 10</li><li>mutual = yes</li></ul></ul><li>country gets the modifier overlord_military_mission for 20 years</li></ul></ul></ul>

___
##Apparently [overlord_rival.Capital.GetCapitalName] is a wonderful holiday destination...

###AI weighting:
AI weights this option at 25
 - Multiplied by 0 if does not have manpower is 0.2
 - Multiplied by 0 if has AND is at war, and does not have war score is -15
 - Multiplied by 0.5 if is at war
 - Multiplied by 0.5 if does not have manpower is 0.4
 - Multiplied by 2 if has AND has manpower is 0.6, and does not have years of income is 0.3
 - Multiplied by 2 if has AND has manpower is 0.8, and does not have years of income is 0.3


###Efects:<ul><li>hidden effect:</li><ul><li>event target:tributary warring rival:</li><ul><li>set country flag [overlord_manpower_support](../flags/overlord_manpower_support.md)</li><li>the event [Overlord Sends Military Mission](../events/overlord_sends_military_mission.md) happens</li></ul></ul><li>add mil power = -50</li><li>add yearly manpower = -1</li><li>event target:tributary warring rival:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = overlord_military_aid</li></ul></ul><li>tooltip:</li><ul><li>event target:tributary warring rival:</li><ul><li>add yearly manpower = 2</li><li>overlord:</li><ul><li>add trust:</li><ul><li>who = ROOT</li><li>value = 10</li><li>mutual = yes</li></ul></ul><li>country gets the modifier overlord_military_mission for 20 years</li></ul></ul></ul>

___
##They could well do with some additional funding.

###AI weighting:
AI weights this option at 25
 - Multiplied by 0 if does not have years of income is 0.3
 - Multiplied by 0 if has num of loans is 1
 - Multiplied by 0 if has AND is at war, and does not have war score is -15
 - Multiplied by 0.5 if is at war
 - Multiplied by 0.5 if does not have years of income is 0.5
 - Multiplied by 2 if has years of income is 1


###Efects:<ul><li>hidden effect:</li><ul><li>event target:tributary warring rival:</li><ul><li>set country flag [overlord_funding_support](../flags/overlord_funding_support.md)</li><li>the event [Overlord Sends Military Mission](../events/overlord_sends_military_mission.md) happens</li></ul></ul><li>add mil power = -50</li><li>add years of income = -0.5</li><li>event target:tributary warring rival:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = overlord_military_aid</li></ul></ul><li>tooltip:</li><ul><li>event target:tributary warring rival:</li><ul><li>add years of income = 1</li><li>overlord:</li><ul><li>add trust:</li><ul><li>who = ROOT</li><li>value = 10</li><li>mutual = yes</li></ul></ul><li>country gets the modifier overlord_military_mission for 20 years</li></ul></ul></ul>

___
##Just the mission is enough.

###AI weighting:
AI weights this option at 25


###Efects:<ul><li>hidden effect:</li><ul><li>event target:tributary warring rival:</li><ul><li>set country flag [overlord_military_mission](../flags/overlord_military_mission.md)</li><li>the event [Overlord Sends Military Mission](../events/overlord_sends_military_mission.md) happens</li></ul></ul><li>add mil power = -50</li><li>event target:tributary warring rival:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = overlord_military_aid</li></ul></ul><li>tooltip:</li><ul><li>event target:tributary warring rival:</li><ul><li>overlord:</li><ul><li>add trust:</li><ul><li>who = ROOT</li><li>value = 10</li><li>mutual = yes</li></ul></ul><li>country gets the modifier overlord_military_mission for 20 years</li></ul></ul></ul>

___
##Unfortunately we cannot afford to send any help right now.

###AI weighting:
AI weights this option at 5


###Efects:<ul><li>add prestige = -5</li></ul>
