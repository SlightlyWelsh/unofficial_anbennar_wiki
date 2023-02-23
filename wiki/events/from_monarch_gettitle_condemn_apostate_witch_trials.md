#Information
 - Title: [From.Monarch.GetTitle]: Condemn Apostate Witch Trials
 - ID: papacy_events.27
#Description
[From.Monarch.GetTitle]: Condemn Apostate Witch Trials
#Options

___
##We obey.

###Efects:<ul><li>add papal influence = 5</li><li>If has any owned province has province modifier is local witch hunts:</li><ul><li>If every owned province has province modifier is local witch hunts:</li><ul><li>remove province modifier = local_witch_hunts</li></ul></ul><li>If has country modifier is nationwide witch hunts:</li><ul><li>remove country modifier = nationwide_witch_hunts</li></ul><li>Z97:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = opinion_condemn_witchtrials_good</li></ul><li>set global flag [pap_condemn_witchtrials_good_flag](../flags/pap_condemn_witchtrials_good_flag.md)</li><li>the event [$FROMCOUNTRY$ Stops the Apostate Witch Trials](../events/fromcountry_stops_the_apostate_witch_trials.md) happens</li></ul></ul>

___
##We decline.

###Efects:<ul><li>Z97:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = opinion_allows_witchtrials_bad</li></ul><li>set global flag [pap_allows_witchtrials_bad_flag](../flags/pap_allows_witchtrials_bad_flag.md)</li><li>the event [$FROMCOUNTRY$ Allows Witch Trials](../events/fromcountry_allows_witch_trials.md) happens</li></ul></ul>
