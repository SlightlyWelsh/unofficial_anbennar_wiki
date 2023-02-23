#Information
 - Title: [Root.foreign_leader.GetName] and the [foreign_culture_province.Culture.GetName] People
 - ID: culture_religion_events.15
#Description
[Root.foreign_leader.GetName] and the [foreign_culture_province.Culture.GetName] People
#Mean Time to Happen:
Base time = 1 days

#Options

___
##[Root.foreign_leader.GetName] will be a welcome addition to the cabinet.

###Efects:<ul><li>add prestige = -10</li><li>If does not have monthly income is 30:</li><ul><li>define advisor:</li><ul><li>name = foreign_leader</li><li>skill = 2</li><li>type = statesman</li><li>discount = yes</li><li>culture = event_target:foreign_culture_province</li><li>religion = event_target:foreign_culture_province</li></ul></ul><li>else:</li><ul><li>define advisor:</li><ul><li>name = foreign_leader</li><li>skill = 3</li><li>type = statesman</li><li>discount = yes</li><li>culture = event_target:foreign_culture_province</li><li>religion = event_target:foreign_culture_province</li></ul></ul></ul>

___
##He serves us better as a local leader of our [foreign_culture_province.Culture.GetName] subjects.

###Efects:<ul><li>event target:foreign culture province:</li><ul><li>If area does not have province modifier is influential power holder; and  has owned by is ROOT:</li><ul><li>add province modifier:</li><ul><li>name = "influential_power_holder"</li><li>duration = 3650</li></ul></ul></ul></ul>
