#Information
 - Title: Ravelian Sailors
 - ID: propagate_religion_events.3
#Description
Ravelian Sailors
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Let us encourage these sailors to seek out our ports!

###Efects:<ul><li>goto = sailor_province</li><li>custom tooltip = explain_conversion_strength_in_true_religion_provinces</li><li>event target:sailor province:</li><ul><li>add province modifier:</li><ul><li>name = "muslim_sailor_community"</li><li>duration = 3650</li></ul></ul><li>trigger switch:</li><ul><li>on trigger = has_country_flag</li><li>sailors flag:</li><ul><li>clr country flag [sailors_flag](../flags/sailors_flag.md)</li><li>add yearly sailors = 2</li></ul><li>captain flag:</li><ul><li>clr country flag [captain_flag](../flags/captain_flag.md)</li><li>define advisor:</li><ul><li>name = sailor_person</li><li>type = trader</li><li>religion = event_target:converter_country</li><li>culture = event_target:converter_country</li><li>skill = 2</li><li>discount = yes</li></ul></ul></ul><li>add years of income = -0.75</li></ul>

___
##We have no need of foreign faiths on our ships.

###Efects:<ul><li>add legitimacy = 5</li></ul>
