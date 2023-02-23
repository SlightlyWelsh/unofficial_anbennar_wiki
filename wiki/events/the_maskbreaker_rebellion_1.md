This page has the same name as others. For full listing see bottom of [the base page](the_maskbreaker_rebellion.md).

#Information
 - Title: The Maskbreaker Rebellion
 - ID: flavor_nuugdan_tsarai.34
#Description
The Maskbreaker Rebellion
#Mean Time to Happen:
Base time = 18 months

#Options

___
##Send some unruly subjects to the rebels as 'volunteers'.

###AI weighting:
AI weights this option at 30


###Efects:<ul><li>set country flag [Y91_support_rebels](../flags/y91_support_rebels.md)</li><li>add manpower = -2</li><li>hidden effect:</li><ul><li>Y98:</li><ul><li>the event [[From.GetAdjective] Intervention](../events/from_getadjective_intervention.md) happens</li></ul></ul><li>reverse add opinion:</li><ul><li>who = Y98</li><li>modifier = A48_supported_rebels</li></ul></ul>

___
##Give the rebels some monetary aid.

###AI weighting:
AI weights this option at 20


###Efects:<ul><li>set country flag [Y91_support_rebels](../flags/y91_support_rebels.md)</li><li>add years of income = -0.4</li><li>hidden effect:</li><ul><li>Y98:</li><ul><li>the event [[From.GetAdjective] Intervention](../events/from_getadjective_intervention.md) happens</li></ul></ul><li>reverse add opinion:</li><ul><li>who = Y98</li><li>modifier = A48_supported_rebels</li></ul></ul>

___
##We don't help rebel scum.

###AI weighting:
AI weights this option at 50
 - Multiplied by 3 if has opinion has who is Y98, and has opinion has value is 30
 - Multiplied by 2 if does not have tag is R62; and does not have tag is Y28
 - Multiplied by 0.3 if does not have opinion has who is Y98, and has opinion has value is -30


###Efects:<ul><li>set country flag [Y91_no_support_for_rebels](../flags/y91_no_support_for_rebels.md)</li><li>add prestige = 5</li><li>reverse add opinion:</li><ul><li>who = Y98</li><li>modifier = A48_didnt_support_rebels</li></ul></ul>
