#Information
 - Title: A Political Marriage - Accepted or Not?
 - ID: dynastic_events.7
#Description
A Political Marriage - Accepted or Not?
#Options

___
##[From.Monarch.GetTitle] [From.Monarch.GetName] accepted!

###Available if:
<li>has country flag [dyn_pu_accepted_flag](../flags/dyn_pu_accepted_flag.md)</li>

###Efects:<ul><li>add legitimacy = 20</li><li>define consort:</li><ul><li>country of origin = FROM</li><li>dynasty = FROM</li><li>culture = FROM</li><li>religion = FROM</li></ul><li>create union = FROM</li></ul>

___
##[From.Monarch.GetTitle] [From.Monarch.GetName] refused!

###Available if:
<li>has country flag [dyn_pu_refused_flag](../flags/dyn_pu_refused_flag.md)</li>

###Efects:<ul><li>tooltip:</li><ul><li>add opinion:</li><ul><li>modifier = opinion_spurned_pu</li><li>who = FROM</li></ul><li>add casus belli:</li><ul><li>target = FROM</li><li>type = cb_insult</li><li>months = 12</li></ul></ul></ul>
