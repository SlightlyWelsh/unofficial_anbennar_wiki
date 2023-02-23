#Information
 - Title: Fire of [fire_province.GetName]
 - ID: industrialization_events.21
#Description
Fire of [fire_province.GetName]
#Mean Time to Happen:
Base time = 1 days
 - Multiplied by 0.5 if has num of owned provinces with has province flag is [great_fire](../flags/great_fire.md), and num of owned provinces with has value is 20

#Options

___
##Factory owners must contribute to rebuilding the city.

###Efects:<ul><li>event target:fire province:</li><ul><li>add devastation = 50</li><li>If area has owned by is ROOT, and does not have province modifier is fire compensation:</li><ul><li>add province modifier:</li><ul><li>name = "fire_compensation"</li><li>duration = 3650</li></ul></ul></ul></ul>

___
##We must help these poor people.

###Efects:<ul><li>add years of income = -0.15</li><li>event target:fire province:</li><ul><li>add devastation = 50</li></ul></ul>
