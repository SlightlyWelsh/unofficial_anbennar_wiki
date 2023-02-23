#Information
 - Title: The Serpent's Cure
 - ID: serpent_rot.16
#Description
The Serpent's Cure
#Options

___
##Distribute it to everyone in the capital!

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>add prestige = 50</li><li>add stability = 3</li><li>custom tooltip = serpent_cure_tooltip</li><li>If has capital scope has continent is serpentspine, and has province modifier is serpent rot 1, and has province modifier is serpent rot 2:</li><ul><li>capital scope:</li><ul><li>add permanent province modifier:</li><ul><li>name = serpent_cure</li><li>duration = 3650</li></ul></ul></ul><li>else:</li><ul><li>If random owned province has continent is serpentspine, and has province modifier is serpent rot 1, and has province modifier is serpent rot 2:</li><ul><li>add permanent province modifier:</li><ul><li>name = serpent_cure</li><li>duration = 3650</li></ul></ul></ul><li>hidden effect:</li><ul><li>clr country flag [burn_the_corpse](../flags/burn_the_corpse.md)</li><li>clr country flag [quarantine_zone](../flags/quarantine_zone.md)</li><li>clr country flag [fight_it_with_fire](../flags/fight_it_with_fire.md)</li></ul></ul>

___
##Spread it through the ventilation system!

###Available if:
<li>any owned province:</li><ul><li>Any of the following:</li><ul><li>has terrain dwarven_hold</li><li>has terrain  dwarven_hold_surface</li></ul></ul>

###AI weighting:
AI weights this option at 100
 - Multiplied by 0 if has ruler has personality is malevolent personality, and has ruler has personality is cruel personality


###Efects:<ul><li>add prestige = 50</li><li>add stability = 3</li><li>custom tooltip = serpent_cure_ventilation_tooltip</li><li>country gets the modifier cure_bringer for 100 years</li><li>If serpentspine has terrain is dwarven hold, and has terrain is dwarven hold surface, and has terrain is dwarven road:</li><ul><li>add permanent province modifier:</li><ul><li>name = serpent_cure</li><li>duration = 3650</li></ul></ul><li>hidden effect:</li><ul><li>clr country flag [burn_the_corpse](../flags/burn_the_corpse.md)</li><li>clr country flag [quarantine_zone](../flags/quarantine_zone.md)</li><li>clr country flag [fight_it_with_fire](../flags/fight_it_with_fire.md)</li></ul></ul>
