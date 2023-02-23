#Information
 - Title: [From.Country.GetName] Responds to Upkeep Demand
 - ID: subject_interaction_events.13
#Description
[From.Country.GetName] Responds to Upkeep Demand
#Options

___
##[From.Country.GetName] sent a general.

###Available if:
<li>has country flag [si_sent_general_flag](../flags/si_sent_general_flag.md)</li>

###Efects:<ul><li>create general:</li><ul><li>tradition = 50</li></ul><li>tooltip:</li><ul><li>add opinion:</li><ul><li>who = FROM</li><li>modifier = opinion_sent_general</li></ul></ul><li>clr country flag [si_sent_general_flag](../flags/si_sent_general_flag.md)</li></ul>

___
##[From.Country.GetName] sent an advisor.

###Available if:
<li>has country flag [si_sent_advisor_flag](../flags/si_sent_advisor_flag.md)</li>

###Efects:<ul><li>define advisor:</li><ul><li>type = army_reformer</li><li>skill = 2</li><li>discount = yes</li><li>culture = FROM</li><li>religion = FROM</li></ul><li>tooltip:</li><ul><li>add opinion:</li><ul><li>who = FROM</li><li>modifier = opinion_sent_advisor</li></ul></ul><li>clr country flag [si_sent_advisor_flag](../flags/si_sent_advisor_flag.md)</li></ul>

___
##[From.Country.GetName] sent gold and manpower.

###Available if:
<li>has country flag [si_sent_gold_flag](../flags/si_sent_gold_flag.md)</li>

###Efects:<ul><li>add years of income = 0.1</li><li>add yearly manpower = 2.5</li><li>tooltip:</li><ul><li>add opinion:</li><ul><li>who = FROM</li><li>modifier = opinion_sent_gold_manpower</li></ul></ul><li>clr country flag [si_sent_gold_flag](../flags/si_sent_gold_flag.md)</li></ul>

___
##[From.Country.GetName] sent nothing.

###Available if:
<li>has country flag [si_sent_nothing_flag](../flags/si_sent_nothing_flag.md)</li>

###Efects:<ul><li>tooltip:</li><ul><li>add opinion:</li><ul><li>who = FROM</li><li>modifier = opinion_sent_nothing</li></ul></ul><li>clr country flag [si_sent_nothing_flag](../flags/si_sent_nothing_flag.md)</li></ul>
