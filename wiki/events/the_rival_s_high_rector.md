#Information
 - Title: The Rival's High Rector
 - ID: papacy_events.29
#Description
The Rival's High Rector
#Mean Time to Happen:
Base time = 200 months

#Options

___
##Then we will erase his deeds.

###Efects:<ul><li>add devotion = -10</li><li>If random known country does not have tag is Z97; and  is papal controller, and  does not have tag is Z97; and any rival country is previous papal controller:</li><ul><li>set country flag [pap_erased_rival_pope_flag](../flags/pap_erased_rival_pope_flag.md)</li><li>the event ˻papacy_events.30˼ happens</li><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = opinion_erased_rival_pope</li></ul><li>If random rival country does not have tag is Z97; and  is previous papal controller:</li><ul><li>set country flag [pap_erased_pope_flag](../flags/pap_erased_pope_flag.md)</li><li>the event ˻papacy_events.31˼ happens</li><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = opinion_erased_pope</li></ul></ul></ul></ul>

___
##Every High Rector should be respected, even the bad ones.

###Efects:<ul><li>add devotion = 10</li><li>If random known country does not have tag is Z97; and  is papal controller, and  does not have tag is Z97; and any rival country is previous papal controller:</li><ul><li>set country flag [pap_not_erased_rival_pope_flag](../flags/pap_not_erased_rival_pope_flag.md)</li><li>the event ˻papacy_events.30˼ happens</li><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = opinion_not_erased_rival_pope</li></ul><li>If random rival country does not have tag is Z97; and  is previous papal controller:</li><ul><li>set country flag [pap_not_erased_pope_flag](../flags/pap_not_erased_pope_flag.md)</li><li>the event ˻papacy_events.31˼ happens</li><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = opinion_not_erased_pope</li></ul></ul></ul></ul>
