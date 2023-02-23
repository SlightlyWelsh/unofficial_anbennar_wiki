#Information
 - Title: Advanced Foundry Infrastructure Complete
 - ID: diggy_project.2
#Description
Advanced Foundry Infrastructure Complete
#Mean Time to Happen:
Base time = 30 years
 - Multiplied by 0.9 if has any owned province has province modifier is developing advanced infrastructure, and any owned province has province modifier is hold foundry, and any owned province has coexisting dwarven pop trigger is yes
 - Multiplied by 0.8 if has any owned province has province modifier is developing advanced infrastructure, and any owned province has province modifier is hold foundry, and any owned province has integrated dwarven pop trigger is yes
 - Multiplied by 0.9 if has any owned province has province modifier is developing advanced infrastructure, and any owned province has province modifier is hold foundry, and any owned province has base production is 25
 - Multiplied by 0.9 if has any owned province has province modifier is developing advanced infrastructure, and any owned province has province modifier is hold foundry, and any owned province has base production is 30
 - Multiplied by 0.9 if has any owned province has province modifier is developing advanced infrastructure, and any owned province has province modifier is hold foundry, and any owned province has base production is 35
 - Multiplied by 0.8 if has any owned province has province modifier is developing advanced infrastructure, and any owned province has province modifier is hold foundry, and any owned province has base production is 40
 - Multiplied by 0.01 if has had country flag is [building_magma_forge](../flags/building_magma_forge.md) for 10950 days

#Options

___
##Good work!

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>hidden effect:</li><ul><li>clr country flag [building_magma_forge](../flags/building_magma_forge.md)</li></ul><li>hidden effect:</li><ul><li>clr country flag [building_diggy](../flags/building_diggy.md)</li></ul><li>hidden effect:</li><ul><li>set country flag [builded_magma_forge](../flags/builded_magma_forge.md)</li></ul><li>add prestige = 15</li><li>If does not have global flag is [magma_forge_build](../flags/magma_forge_build.md):</li><ul><li>hidden effect:</li><ul><li>set global flag [magma_forge_build](../flags/magma_forge_build.md)</li></ul><li>custom tooltip = first_magma_forge_tooltip</li><li>event target:advanced infrastructure province:</li><ul><li>remove province modifier = hold_foundry</li><li>add permanent province modifier:</li><ul><li>name = hold_foundry_2</li><li>duration = -1</li></ul><li>add permanent province modifier:</li><ul><li>name = magma_forge</li><li>duration = -1</li></ul></ul></ul><li>else:</li><ul><li>event target:advanced infrastructure province:</li><ul><li>remove province modifier = hold_foundry</li><li>add permanent province modifier:</li><ul><li>name = hold_foundry_2</li><li>duration = -1</li></ul></ul></ul></ul>
