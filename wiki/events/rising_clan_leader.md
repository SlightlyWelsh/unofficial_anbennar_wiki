#Information
 - Title: Rising Clan Leader
 - ID: tribal_federation_events.3
#Description
Rising Clan Leader
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Let us make room for this man!

###AI weighting:
AI weights this option at 25


###Efects:<ul><li>add tribal allegiance = -7</li><li>event target:clan area:</li><ul><li>If area has owned by is ROOT:</li><ul><li>add local autonomy = 25</li><li>add province modifier:</li><ul><li>name = "favored_clan"</li><li>duration = 3650</li></ul></ul></ul><li>trigger switch:</li><ul><li>on trigger = has_country_flag</li><li>adm advisor:</li><ul><li>clr country flag [adm_advisor](../flags/adm_advisor.md)</li><li>define advisor:</li><ul><li>type = treasurer</li><li>culture = event_target:clan_area</li><li>religion = event_target:clan_area</li><li>skill = 2</li><li>discount = yes</li></ul></ul><li>dip advisor:</li><ul><li>clr country flag [dip_advisor](../flags/dip_advisor.md)</li><li>define advisor:</li><ul><li>type = spymaster</li><li>culture = event_target:clan_area</li><li>religion = event_target:clan_area</li><li>skill = 2</li><li>discount = yes</li></ul></ul><li>mil advisor:</li><ul><li>clr country flag [mil_advisor](../flags/mil_advisor.md)</li><li>define advisor:</li><ul><li>type = recruitmaster</li><li>culture = event_target:clan_area</li><li>religion = event_target:clan_area</li><li>skill = 2</li><li>discount = yes</li></ul></ul></ul></ul>

___
##He can serve us better in the field.

###AI weighting:
AI weights this option at 25


###Efects:<ul><li>add tribal allegiance = -10</li><li>event target:clan area:</li><ul><li>If area has owned by is ROOT:</li><ul><li>add local autonomy = 25</li><li>add province modifier:</li><ul><li>name = "favored_clan"</li><li>duration = 3650</li></ul></ul></ul><li>create general:</li><ul><li>tradition = 30</li></ul><li>trigger switch:</li><ul><li>on trigger = has_country_flag</li><li>adm advisor:</li><ul><li>clr country flag [adm_advisor](../flags/adm_advisor.md)</li></ul><li>dip advisor:</li><ul><li>clr country flag [dip_advisor](../flags/dip_advisor.md)</li></ul><li>mil advisor:</li><ul><li>clr country flag [mil_advisor](../flags/mil_advisor.md)</li></ul></ul></ul>

___
##We must protect the privileges of the traditional leading clans.

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>add tribal allegiance = 15</li><li>event target:clan area:</li><ul><li>If area has owned by is ROOT:</li><ul><li>add province modifier:</li><ul><li>name = "disfavored_clan"</li><li>duration = 3650</li></ul></ul></ul><li>trigger switch:</li><ul><li>on trigger = has_country_flag</li><li>adm advisor:</li><ul><li>clr country flag [adm_advisor](../flags/adm_advisor.md)</li></ul><li>dip advisor:</li><ul><li>clr country flag [dip_advisor](../flags/dip_advisor.md)</li></ul><li>mil advisor:</li><ul><li>clr country flag [mil_advisor](../flags/mil_advisor.md)</li></ul></ul></ul>
