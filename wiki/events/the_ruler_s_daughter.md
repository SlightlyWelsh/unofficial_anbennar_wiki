#Information
 - Title: The Ruler's Daughter
 - ID: dynastic_events.4
#Description
The Ruler's Daughter
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Crown the former ruler's daughter.

###Efects:<ul><li>If has religion is catholic:</li><ul><li>add papal influence = -10</li></ul><li>define ruler:</li><ul><li>dynasty = ROOT</li><li>age = 20</li><li>adm = 3</li><li>dip = 3</li><li>mil = 3</li><li>claim = 50</li><li>female = yes</li></ul><li>If has states general mechanic is yes:</li><ul><li>change statists vs orangists = 1</li></ul><li>If random known country has country flag is [dyn_woman_pretender_flag](../flags/dyn_woman_pretender_flag.md):</li><ul><li>add casus belli:</li><ul><li>target = ROOT</li><li>type = cb_restore_personal_union</li><li>months = 12</li></ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = opinion_spurned_heir</li></ul><li>clr country flag [dyn_woman_pretender_flag](../flags/dyn_woman_pretender_flag.md)</li></ul></ul>

___
##Choose the foreign noble.

###Efects:<ul><li>If random known country has country flag is [dyn_woman_pretender_flag](../flags/dyn_woman_pretender_flag.md):</li><ul><li>clr country flag [dyn_woman_pretender_flag](../flags/dyn_woman_pretender_flag.md)</li><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = opinion_choose_heir</li></ul><li>ROOT:</li><ul><li>define ruler:</li><ul><li>dynasty = PREV</li><li>age = 20</li></ul><li>If has states general mechanic is yes:</li><ul><li>change statists vs orangists = 1</li></ul></ul></ul><li>If random owned province is not a capital:</li><ul><li>spawn rebels:</li><ul><li>type = pretender_rebels</li><li>size = 2</li><li>female = yes</li></ul></ul></ul>
