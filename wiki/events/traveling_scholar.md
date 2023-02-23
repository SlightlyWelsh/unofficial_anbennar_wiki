#Information
 - Title: Traveling Scholar
 - ID: propagate_religion_events.8
#Description
Traveling Scholar
#Mean Time to Happen:
Base time = 1 days

#Options

___
##We have use of this man. Let us offer him a place at our court!

###Efects:<ul><li>trigger switch:</li><ul><li>on trigger = has_country_flag</li><li>qadi:</li><ul><li>clr country flag [qadi](../flags/qadi.md)</li><li>define advisor:</li><ul><li>type = natural_scientist</li><li>name = qadi_person</li><li>skill = 2</li><li>culture = event_target:converter_country</li><li>religion = event_target:converter_country</li><li>discount = yes</li></ul></ul><li>mufti:</li><ul><li>clr country flag [mufti](../flags/mufti.md)</li><li>define advisor:</li><ul><li>type = theologian</li><li>skill = 2</li><li>name = qadi_person</li><li>culture = event_target:converter_country</li><li>religion = event_target:converter_country</li><li>discount = yes</li></ul></ul><li>sufi:</li><ul><li>clr country flag [sufi](../flags/sufi.md)</li><li>define advisor:</li><ul><li>type = philosopher</li><li>name = qadi_person</li><li>skill = 2</li><li>culture = event_target:converter_country</li><li>religion = event_target:converter_country</li><li>discount = yes</li></ul></ul></ul></ul>

___
##Let us learn as much as we can about the state of things abroad.

###Efects:<ul><li>add dip power = 15</li><li>add mil power = 15</li><li>event target:converter country:</li><ul><li>add spy network from:</li><ul><li>who = ROOT</li><li>value = 75</li></ul></ul></ul>
