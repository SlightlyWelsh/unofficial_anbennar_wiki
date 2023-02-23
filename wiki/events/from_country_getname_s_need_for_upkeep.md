#Information
 - Title: [From.Country.GetName]'s Need for Upkeep
 - ID: subject_interaction_events.12
#Description
[From.Country.GetName]'s Need for Upkeep
#Options

___
##Send them a general.

###Efects:<ul><li>add army tradition = -5</li><li>FROM:</li><ul><li>tooltip:</li><ul><li>create general:</li><ul><li>tradition = 50</li></ul></ul><li>set country flag [si_sent_general_flag](../flags/si_sent_general_flag.md)</li><li>the event [[From.Country.GetName] Responds to Upkeep Demand](../events/from_country_getname_responds_to_upkeep_demand.md) happens</li><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = opinion_sent_general</li></ul></ul></ul>

___
##They need a good advisor.

###Efects:<ul><li>add treasury = -25</li><li>FROM:</li><ul><li>tooltip:</li><ul><li>define advisor:</li><ul><li>type = army_reformer</li><li>skill = 2</li><li>discount = yes</li></ul></ul><li>set country flag [si_sent_advisor_flag](../flags/si_sent_advisor_flag.md)</li><li>the event [[From.Country.GetName] Responds to Upkeep Demand](../events/from_country_getname_responds_to_upkeep_demand.md) happens</li><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = opinion_sent_advisor</li></ul></ul></ul>

___
##Send more soldiers and gold.

###Efects:<ul><li>add treasury = -50</li><li>add manpower = -5</li><li>FROM:</li><ul><li>tooltip:</li><ul><li>add treasury = 50</li><li>add manpower = 5</li></ul><li>set country flag [si_sent_gold_flag](../flags/si_sent_gold_flag.md)</li><li>the event [[From.Country.GetName] Responds to Upkeep Demand](../events/from_country_getname_responds_to_upkeep_demand.md) happens</li><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = opinion_sent_gold_manpower</li></ul></ul></ul>

___
##They have all that they need, we will give them no more.

###Efects:<ul><li>FROM:</li><ul><li>set country flag [si_sent_nothing_flag](../flags/si_sent_nothing_flag.md)</li><li>the event [[From.Country.GetName] Responds to Upkeep Demand](../events/from_country_getname_responds_to_upkeep_demand.md) happens</li><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = opinion_sent_nothing</li></ul></ul></ul>
