#Information
 - Title: Tradition of Service
 - ID: nobles_estate_events.11
#Description
Tradition of Service
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Great!

###Efects:<ul><li>add meritocracy effect = yes</li><li>trigger switch:</li><ul><li>on trigger = has_country_flag</li><li>noble general:</li><ul><li>create general:</li><ul><li>tradition = 50</li></ul><li>clr country flag [noble_general](../flags/noble_general.md)</li></ul><li>noble admiral:</li><ul><li>create admiral:</li><ul><li>tradition = 50</li></ul><li>clr country flag [noble_admiral](../flags/noble_admiral.md)</li></ul><li>noble statesman:</li><ul><li>If has monthly income is 25:</li><ul><li>define advisor:</li><ul><li>type = statesman</li><li>culture = event_target:noble_province</li><li>religion = event_target:noble_province</li><li>skill = 3</li><li>discount = yes</li></ul></ul><li>If does not have monthly income is 25:</li><ul><li>define advisor:</li><ul><li>type = statesman</li><li>culture = event_target:noble_province</li><li>religion = event_target:noble_province</li><li>skill = 2</li><li>discount = yes</li></ul></ul><li>clr country flag [noble_statesman](../flags/noble_statesman.md)</li></ul><li>noble army reformer:</li><ul><li>If has monthly income is 25:</li><ul><li>define advisor:</li><ul><li>type = army_reformer</li><li>culture = event_target:noble_province</li><li>religion = event_target:noble_province</li><li>skill = 3</li><li>discount = yes</li></ul></ul><li>If does not have monthly income is 25:</li><ul><li>define advisor:</li><ul><li>type = army_reformer</li><li>culture = event_target:noble_province</li><li>religion = event_target:noble_province</li><li>skill = 2</li><li>discount = yes</li></ul></ul><li>clr country flag [noble_army_reformer](../flags/noble_army_reformer.md)</li></ul></ul></ul>
