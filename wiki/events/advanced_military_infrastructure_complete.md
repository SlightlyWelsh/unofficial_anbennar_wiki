#Information
 - Title: Advanced Military Infrastructure Complete
 - ID: diggy_project.10
#Description
Advanced Military Infrastructure Complete
#Mean Time to Happen:
Base time = 30 years
 - Multiplied by 0.9 if has any owned province has province modifier is developing advanced infrastructure, and any owned province has province modifier is hold military, and any owned province has coexisting dwarven pop trigger is yes
 - Multiplied by 0.8 if has any owned province has province modifier is developing advanced infrastructure, and any owned province has province modifier is hold military, and any owned province has integrated dwarven pop trigger is yes
 - Multiplied by 0.9 if has any owned province has province modifier is developing advanced infrastructure, and any owned province has province modifier is hold military, and any owned province has base manpower is 25
 - Multiplied by 0.9 if has any owned province has province modifier is developing advanced infrastructure, and any owned province has province modifier is hold military, and any owned province has base manpower is 30
 - Multiplied by 0.9 if has any owned province has province modifier is developing advanced infrastructure, and any owned province has province modifier is hold military, and any owned province has base manpower is 35
 - Multiplied by 0.8 if has any owned province has province modifier is developing advanced infrastructure, and any owned province has province modifier is hold military, and any owned province has base manpower is 40
 - Multiplied by 0.01 if has had country flag is [building_military_academy](../flags/building_military_academy.md) for 10950 days

#Options

___
##Good work!

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>hidden effect:</li><ul><li>clr country flag [building_military_academy](../flags/building_military_academy.md)</li></ul><li>hidden effect:</li><ul><li>clr country flag [building_diggy](../flags/building_diggy.md)</li></ul><li>add prestige = 15</li><li>If does not have global flag is [military_academy_build](../flags/military_academy_build.md):</li><ul><li>hidden effect:</li><ul><li>set global flag [military_academy_build](../flags/military_academy_build.md)</li></ul><li>custom tooltip = first_military_tooltip</li><li>event target:advanced infrastructure province:</li><ul><li>remove province modifier = hold_military</li><li>add permanent province modifier:</li><ul><li>name = hold_military_2</li><li>duration = -1</li></ul><li>add permanent province modifier:</li><ul><li>name = military_academy</li><li>duration = -1</li></ul></ul></ul><li>else:</li><ul><li>event target:advanced infrastructure province:</li><ul><li>remove province modifier = hold_military</li><li>add permanent province modifier:</li><ul><li>name = hold_military_2</li><li>duration = -1</li></ul></ul></ul></ul>
