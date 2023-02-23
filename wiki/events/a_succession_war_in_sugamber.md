#Information
 - Title: A Succession War in Sugamber
 - ID: flavor_sugamber.10
#Description
A Succession War in Sugamber
#Mean Time to Happen:
Base time = 18 months

#Options

___
##Send some unruly subjects to the rebels as 'volunteers'.

###AI weighting:
AI weights this option at 30


###Efects:<ul><li>set country flag [support_rebels](../flags/support_rebels.md)</li><li>add manpower = -2</li><li>hidden effect:</li><ul><li>A48:</li><ul><li>the event ˻flavor_sugamber.12˼ happens</li></ul></ul><li>reverse add opinion:</li><ul><li>who = A48</li><li>modifier = A48_supported_rebels</li></ul></ul>

___
##Give the rebels some monetary aid.

###AI weighting:
AI weights this option at 20


###Efects:<ul><li>set country flag [support_rebels](../flags/support_rebels.md)</li><li>add years of income = -0.4</li><li>hidden effect:</li><ul><li>A48:</li><ul><li>the event ˻flavor_sugamber.12˼ happens</li></ul></ul><li>reverse add opinion:</li><ul><li>who = A48</li><li>modifier = A48_supported_rebels</li></ul></ul>

___
##We don't help rebel scum.

###AI weighting:
AI weights this option at 50
 - Multiplied by 3 if has opinion has who is A48, and has opinion has value is 30
 - Multiplied by 2 if does not have tag is A56; and does not have tag is A34
 - Multiplied by 0.3 if does not have opinion has who is A48, and has opinion has value is -30


###Efects:<ul><li>set country flag [no_support_for_rebels](../flags/no_support_for_rebels.md)</li><li>add prestige = 5</li><li>reverse add opinion:</li><ul><li>who = A48</li><li>modifier = A48_didnt_support_rebels</li></ul></ul>
