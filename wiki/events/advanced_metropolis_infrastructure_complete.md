#Information
 - Title: Advanced Metropolis Infrastructure Complete
 - ID: diggy_project.4
#Description
Advanced Metropolis Infrastructure Complete
#Mean Time to Happen:
Base time = 30 years
 - Multiplied by 0.9 if has any owned province has province modifier is developing advanced infrastructure, and any owned province has province modifier is hold city, and any owned province has coexisting dwarven pop trigger is yes
 - Multiplied by 0.8 if has any owned province has province modifier is developing advanced infrastructure, and any owned province has province modifier is hold city, and any owned province has integrated dwarven pop trigger is yes
 - Multiplied by 0.9 if has any owned province has province modifier is developing advanced infrastructure, and any owned province has province modifier is hold city, and any owned province has base tax is 25
 - Multiplied by 0.9 if has any owned province has province modifier is developing advanced infrastructure, and any owned province has province modifier is hold city, and any owned province has base tax is 30
 - Multiplied by 0.9 if has any owned province has province modifier is developing advanced infrastructure, and any owned province has province modifier is hold city, and any owned province has base tax is 35
 - Multiplied by 0.8 if has any owned province has province modifier is developing advanced infrastructure, and any owned province has province modifier is hold city, and any owned province has base tax is 40
 - Multiplied by 0.01 if has had country flag is [building_artificier_hall](../flags/building_artificier_hall.md) for 10950 days

#Options

___
##Good work!

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>hidden effect:</li><ul><li>clr country flag [building_artificier_hall](../flags/building_artificier_hall.md)</li></ul><li>hidden effect:</li><ul><li>clr country flag [building_diggy](../flags/building_diggy.md)</li></ul><li>add prestige = 15</li><li>If does not have global flag is [artificier_hall_build](../flags/artificier_hall_build.md):</li><ul><li>hidden effect:</li><ul><li>set global flag [artificier_hall_build](../flags/artificier_hall_build.md)</li></ul><li>custom tooltip = first_artificier_tooltip</li><li>event target:advanced infrastructure province:</li><ul><li>remove province modifier = hold_city</li><li>add permanent province modifier:</li><ul><li>name = hold_city_2</li><li>duration = -1</li></ul><li>add permanent province modifier:</li><ul><li>name = artificier_hall</li><li>duration = -1</li></ul></ul></ul><li>else:</li><ul><li>event target:advanced infrastructure province:</li><ul><li>remove province modifier = hold_city</li><li>add permanent province modifier:</li><ul><li>name = hold_city_2</li><li>duration = -1</li></ul></ul></ul></ul>
