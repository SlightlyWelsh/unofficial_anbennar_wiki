#Information
 - Title: The Mercenary [ROOT.GetRulerTitleOrRegency]
 - ID: lotdekkhang.3
#Description
The Mercenary [ROOT.GetRulerTitleOrRegency]
#Options

___
##A Swallow Hobgoblin

###Available if:
<li>ruler culture is swallow_command</li>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>add ruler modifier:</li><ul><li>name = Y58_lot_dekkhang_swallow_ruler</li><li>duration = -1</li></ul></ul>

___
##An Azkare Sun Elf

###Available if:
<li>ruler culture is sun_elf</li>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>add ruler modifier:</li><ul><li>name = Y58_lot_dekkhang_sun_ruler</li><li>duration = -1</li></ul></ul>

___
##A Nephrite dwarf

###Available if:
<li>ruler culture is nephrite_dwarf</li>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>add ruler modifier:</li><ul><li>name = Y58_lot_dekkhang_nephrite_ruler</li><li>duration = -1</li></ul></ul>

___
##An Eastern Harimari

###Available if:
<li>ruler culture is east_harimari</li>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>add ruler modifier:</li><ul><li>name = Y58_lot_dekkhang_harimari_ruler</li><li>duration = -1</li></ul></ul>

___
##A Feng Harpy

###Available if:
<li>ruler culture is feng_harpy</li>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>add ruler modifier:</li><ul><li>name = Y58_lot_dekkhang_feng_ruler</li><li>duration = -1</li></ul></ul>

___
##A Goldscale Kobold

###Available if:
<li>ruler culture is goldscale_kobold</li>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>add ruler modifier:</li><ul><li>name = Y58_lot_dekkhang_goldbold_ruler</li><li>duration = -1</li></ul></ul>

___
##An Oni

###Available if:
<li>ruler culture is horned_ogre</li>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>add ruler modifier:</li><ul><li>name = Y58_lot_dekkhang_oni_ruler</li><li>duration = -1</li></ul></ul>

___
##A brown Orc

###Available if:
<li>ruler culture is brown_orc</li>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>add ruler modifier:</li><ul><li>name = Y58_lot_dekkhang_orc_ruler</li><li>duration = -1</li></ul></ul>

___
##A Cave Goblin

###Available if:
<li>ruler culture is undergrowth_goblin</li>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>add ruler modifier:</li><ul><li>name = Y58_lot_dekkhang_goblin_ruler</li><li>duration = -1</li></ul></ul>

___
##A Half-Orc

###Available if:
<li>ruler culture is half_orc</li>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>add ruler modifier:</li><ul><li>name = Y58_lot_dekkhang_horc_ruler</li><li>duration = -1</li></ul></ul>

___
##A Half Elf

###Available if:
<li>ruler culture is half_elf</li>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>add ruler modifier:</li><ul><li>name = Y58_lot_dekkhang_helf_ruler</li><li>duration = -1</li></ul></ul>

___
##A relative of the previous ruler

###Available if:
<li>has country flag [Y58_relative_won](../flags/y58_relative_won.md)</li><li>None of the following:</li><ul><li>ruler culture is half_elf</li><li>ruler culture  is half_orc</li><li>ruler culture   is undergrowth_goblin</li><li>ruler culture    is brown_orc</li><li>ruler culture     is horned_ogre</li><li>ruler culture      is goldscale_kobold</li><li>ruler culture       is feng_harpy</li><li>ruler culture        is east_harimari</li><li>ruler culture         is nephrite_dwarf</li><li>ruler culture          is sun_elf</li><li>ruler culture           is swallow_command</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>clr country flag [Y58_relative_won](../flags/y58_relative_won.md)</li><li>add ruler modifier:</li><ul><li>name = Y58_lot_dekkhang_relative_ruler</li><li>duration = -1</li></ul></ul>

___
##A prominent Dauloph

###Available if:
<li>has country flag [Y58_prominent_dauloph_won](../flags/y58_prominent_dauloph_won.md)</li>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>clr country flag [Y58_prominent_dauloph_won](../flags/y58_prominent_dauloph_won.md)</li><li>add ruler modifier:</li><ul><li>name = Y58_lot_dekkhang_dauloph_ruler</li><li>duration = -1</li></ul></ul>

___
##A local fighter

###Available if:
<li>Any of the following:</li><ul><li>has country flag [Y58_local_fighter_won](../flags/y58_local_fighter_won.md)</li><li>None of the following:</li><ul><li>ruler culture is half_elf</li><li>ruler culture  is half_orc</li><li>ruler culture   is undergrowth_goblin</li><li>ruler culture    is brown_orc</li><li>ruler culture     is horned_ogre</li><li>ruler culture      is goldscale_kobold</li><li>ruler culture       is feng_harpy</li><li>ruler culture        is east_harimari</li><li>ruler culture         is nephrite_dwarf</li><li>ruler culture          is sun_elf</li><li>ruler culture           is swallow_command</li><li>has country flag [Y58_local_fighter_won](../flags/y58_local_fighter_won.md)</li><li>has country flag  Y58_allied_noble_won</li><li>has country flag   Y58_prominent_dauloph_won</li><li>has country flag    Y58_relative_won</li></ul></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>clr country flag [Y58_local_fighter_won](../flags/y58_local_fighter_won.md)</li><li>clr country flag [Y58_allied_noble_won](../flags/y58_allied_noble_won.md)</li><li>clr country flag [Y58_prominent_dauloph_won](../flags/y58_prominent_dauloph_won.md)</li><li>clr country flag [Y58_relative_won](../flags/y58_relative_won.md)</li><li>add ruler modifier:</li><ul><li>name = Y58_lot_dekkhang_fighter_ruler</li><li>duration = -1</li></ul></ul>

___
##An allied noble

###Available if:
<li>has country flag [Y58_allied_noble_won](../flags/y58_allied_noble_won.md)</li>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>clr country flag [Y58_allied_noble_won](../flags/y58_allied_noble_won.md)</li><li>add ruler modifier:</li><ul><li>name = Y58_lot_dekkhang_allied_ruler</li><li>duration = -1</li></ul></ul>
