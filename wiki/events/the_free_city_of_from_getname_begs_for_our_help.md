#Information
 - Title: The Free City of [From.GetName] Begs for Our Help
 - ID: free_cities.4
#Description
The Free City of [From.GetName] Begs for Our Help
#Options

___
##It's a reasonable request, and one we will honor.

###AI weighting:
AI weights this option at 75
 - Multiplied by 2 if has opinion has who is FROM, and has opinion has value is 50


###Efects:<ul><li>add manpower = -1</li><li>add years of income = -0.1</li><li>add imperial influence = 10</li><li>FROM:</li><ul><li>set country flag [fc_help_flag](../flags/fc_help_flag.md)</li><li>the event [The [Emperor.Monarch.GetTitle]’s Response](../events/the_emperor_monarch_gettitle_s_response.md) happens</li><li>tooltip:</li><ul><li>add manpower = 1</li><li>add years of income = 0.1</li></ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = opinion_sent_help</li></ul></ul></ul>

___
##The problem is deeper within [From.Country.GetName] and until they realize that, we will not send help.

###AI weighting:
AI weights this option at 25
 - Multiplied by 2 if does not have opinion has who is FROM, and has opinion has value is 0
 - Multiplied by 0 if has opinion has who is FROM, and has opinion has value is 50


###Efects:<ul><li>FROM:</li><ul><li>set country flag [fc_nohelp_flag](../flags/fc_nohelp_flag.md)</li><li>the event [The [Emperor.Monarch.GetTitle]’s Response](../events/the_emperor_monarch_gettitle_s_response.md) happens</li><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = opinion_refused_send_help</li></ul></ul></ul>
