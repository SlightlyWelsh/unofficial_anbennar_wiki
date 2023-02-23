#Information
 - Title: Miracle?
 - ID: propagate_religion_events.4
#Description
Miracle?
#Mean Time to Happen:
Base time = 1 days

#Options

___
##This is a good sign.

###Efects:<ul><li>add stability or adm power = yes</li><li>event target:cured province:</li><ul><li>change religion = event_target:converter_country</li></ul></ul>

___
##Let us invite this man to [Root.Capital.GetName], where he can be put to good use.

###Efects:<ul><li>event target:cured province:</li><ul><li>change religion = event_target:converter_country</li></ul><li>trigger switch:</li><ul><li>on trigger = has_country_flag</li><li>philosopher flag:</li><ul><li>clr country flag [philosopher_flag](../flags/philosopher_flag.md)</li><li>define advisor:</li><ul><li>name = miracle_person</li><li>type = philosopher</li><li>culture = event_target:converter_country</li><li>religion = event_target:converter_country</li><li>skill = 2</li><li>discount = yes</li></ul></ul><li>theologian flag:</li><ul><li>clr country flag [theologian_flag](../flags/theologian_flag.md)</li><li>define advisor:</li><ul><li>name = miracle_person</li><li>type = natural_scientist</li><li>culture = event_target:converter_country</li><li>religion = event_target:converter_country</li><li>skill = 2</li><li>discount = yes</li></ul></ul></ul></ul>
