This page has the same name as others. For full listing see bottom of [the base page](the_harpylen_dam.md).

#Information
 - Title: The Harpylen Dam
 - ID: diggy_project.12
#Description
The Harpylen Dam
#Mean Time to Happen:
Base time = 10 years
 - Multiplied by 0.01 if has had country flag is [constructing_dam](../flags/constructing_dam.md) for 1825 days
 - Multiplied by 0.5 if has global flag is [dd_dimlherd](../flags/dd_dimlherd.md), and  has any owned province has great project has type is dd dimlherd, and has great project has tier is 3

#Options

___
##Excellent!

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>If does not have province flag is [dam_1](../flags/dam_1.md):</li><ul><li>676:</li><ul><li>hidden effect:</li><ul><li>set province flag [dam_1](../flags/dam_1.md)</li></ul><li>add permanent province modifier:</li><ul><li>name = dam_stage_1</li><li>duration = -1</li></ul></ul></ul><li>Else if has 676 has province flag is [dam_1](../flags/dam_1.md); and  does not have province flag is [dam_2](../flags/dam_2.md):</li><ul><li>676:</li><ul><li>hidden effect:</li><ul><li>set province flag [dam_2](../flags/dam_2.md)</li></ul><li>remove province modifier = dam_stage_1</li><li>add permanent province modifier:</li><ul><li>name = dam_stage_2</li><li>duration = -1</li></ul></ul></ul><li>Else if has 676 has province flag is [dam_2](../flags/dam_2.md); and  does not have province flag is [dam_3](../flags/dam_3.md):</li><ul><li>676:</li><ul><li>hidden effect:</li><ul><li>set province flag [dam_3](../flags/dam_3.md)</li></ul><li>remove province modifier = dam_stage_2</li><li>add permanent province modifier:</li><ul><li>name = dam_stage_3</li><li>duration = -1</li></ul></ul></ul><li>Else if has 676 has province flag is [dam_3](../flags/dam_3.md); and  does not have province flag is [dam_4](../flags/dam_4.md):</li><ul><li>676:</li><ul><li>hidden effect:</li><ul><li>set province flag [dam_4](../flags/dam_4.md)</li></ul><li>remove province modifier = dam_stage_3</li><li>add permanent province modifier:</li><ul><li>name = dam_stage_4</li><li>duration = -1</li></ul></ul></ul><li>Else if has 676 has province flag is [dam_4](../flags/dam_4.md):</li><ul><li>676:</li><ul><li>remove province modifier = dam_stage_4</li><li>add permanent province modifier:</li><ul><li>name = the_harpylen_dam</li><li>duration = -1</li></ul><li>hidden effect:</li><ul><li>clr province flag [dam_4](../flags/dam_4.md)</li></ul><li>hidden effect:</li><ul><li>clr province flag [dam_3](../flags/dam_3.md)</li></ul><li>hidden effect:</li><ul><li>clr province flag [dam_2](../flags/dam_2.md)</li></ul><li>hidden effect:</li><ul><li>clr province flag [dam_1](../flags/dam_1.md)</li></ul></ul><li>add prestige = 50</li><li>add splendor = 100</li><li>custom tooltip = the_harpylen_dam_tooltip</li><li>hidden effect:</li><ul><li>set global flag [harpylen_dam_build](../flags/harpylen_dam_build.md)</li></ul></ul><li>676:</li><ul><li>remove province modifier = dam_construction</li></ul></ul>
