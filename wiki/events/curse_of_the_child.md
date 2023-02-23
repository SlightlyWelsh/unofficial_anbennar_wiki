#Information
 - Title: Curse of the Child
 - ID: fey_alignment.12
#Description
Curse of the Child
#Mean Time to Happen:
Base time = 1 days

#Options

___
##What has happened to you!

###Efects:<ul><li>If has country flag is [fey_alignment_heir_disfigure](../flags/fey_alignment_heir_disfigure.md):</li><ul><li>random list:</li><ul><li>1:</li><ul><li>decrease heir adm effect = yes</li></ul><li>1:</li><ul><li>decrease heir dip effect = yes</li></ul><li>1:</li><ul><li>decrease heir mil effect = yes</li></ul></ul></ul><li>If has country flag is [fey_alignment_heir_abducted](../flags/fey_alignment_heir_abducted.md):</li><ul><li>hidden effect:</li><ul><li>root:</li><ul><li>set saved name:</li><ul><li>key = fey_alignment_heirpretender</li><li>type = simple</li><li>name = "[ROOT.Heir.GetName]"</li><li>scope = ROOT</li></ul></ul></ul><li>custom tooltip = fey_alignment_abductedheirtooltip</li><li>exile heir as = fey_alignment_abductedheir@ROOT</li></ul><li>If has country flag is [fey_alignment_heir_race](../flags/fey_alignment_heir_race.md):</li><ul><li>random list:</li><ul><li>1:</li><ul><li>trigger:</li><ul><li>NOT:</li><ul><li>heir is orcish = yes</li></ul></ul><li>random list:</li><ul><li>1:</li><ul><li>set heir culture = green_orc</li></ul><li>1:</li><ul><li>set heir culture = gray_orc</li></ul><li>1:</li><ul><li>set heir culture = black_orc</li></ul></ul><li>decrease heir adm effect = yes</li><li>decrease heir dip effect = yes</li><li>change heir mil = 2</li></ul><li>1:</li><ul><li>trigger:</li><ul><li>NOT:</li><ul><li>heir is goblin = yes</li></ul></ul><li>random list:</li><ul><li>1:</li><ul><li>set heir culture = forest_goblin</li></ul><li>1:</li><ul><li>set heir culture = cave_goblin</li></ul><li>1:</li><ul><li>set heir culture = undergrowth_goblin</li></ul><li>1:</li><ul><li>set heir culture = exodus_goblin</li></ul></ul><li>decrease heir adm effect = yes</li><li>decrease heir dip effect = yes</li><li>change heir mil = 2</li></ul><li>1:</li><ul><li>trigger:</li><ul><li>NOT:</li><ul><li>heir is troll = yes</li></ul></ul><li>random list:</li><ul><li>1:</li><ul><li>set heir culture = fjord_troll</li></ul><li>1:</li><ul><li>set heir culture = forest_troll</li></ul></ul><li>decrease heir adm effect = yes</li><li>decrease heir dip effect = yes</li><li>change heir mil = 2</li></ul><li>1:</li><ul><li>trigger:</li><ul><li>NOT:</li><ul><li>heir is elven = yes</li></ul></ul><li>random list:</li><ul><li>1:</li><ul><li>set heir culture = moon_elf</li></ul><li>1:</li><ul><li>set heir culture = sun_elf</li></ul><li>1:</li><ul><li>set heir culture = wood_elf</li></ul></ul><li>add heir personality = immortal_personality</li><li>increase heir adm effect = yes</li><li>increase heir dip effect = yes</li></ul></ul></ul></ul>

___
##Quick, drink this!

###Available if:
<li>has country flag [fey_alignment_mead](../flags/fey_alignment_mead.md)</li>

###Efects:<ul><li>hidden effect:</li><ul><li>clr country flag [fey_alignment_mead](../flags/fey_alignment_mead.md)</li></ul></ul>
