#Information
 - Title: A Heathen [Root.Monarch.GetTitle]
 - ID: culture_religion_events.5
#Description
A Heathen [Root.Monarch.GetTitle]
#Mean Time to Happen:
Base time = 1 days
 - Multiplied by 2 if has piety is 0.5
 - Multiplied by 1.5 if has piety is 0.01

#Options

___
##Extensive use of force is only fitting.

###Efects:<ul><li>event target:rebelprovince:</li><ul><li>If has religion is ROOT:</li><ul><li>spawn rebels:</li><ul><li>type = religious_rebels</li><li>religion = ROOT</li><li>size = 1</li><li>leader = antimonarchistpriest</li></ul></ul><li>else:</li><ul><li>spawn rebels:</li><ul><li>type = pretender_rebels</li><li>religion = ROOT</li><li>size = 1</li><li>leader = antimonarchistpriest</li></ul></ul><li>If area has owned by is ROOT:</li><ul><li>add province modifier:</li><ul><li>name = "heathen_ruler_religious_tensions"</li><li>duration = 3650</li></ul></ul></ul></ul>

___
##Let us not escalate the situation.

###Efects:<ul><li>add dip power = -25</li><li>event target:rebelprovince:</li><ul><li>If area has owned by is ROOT:</li><ul><li>add province modifier:</li><ul><li>name = "heathen_ruler_religious_tensions"</li><li>duration = 1825</li></ul></ul></ul></ul>
