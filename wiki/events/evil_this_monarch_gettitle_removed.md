#Information
 - Title: Evil [This.Monarch.GetTitle] Removed
 - ID: witch_king.2
#Description
Evil [This.Monarch.GetTitle] Removed
#Options

___
##We must retain control of what still remains

###Efects:<ul><li>If has country flag is [witch_king_flag](../flags/witch_king_flag.md):</li><ul><li>If has heir flag is [heir_consort_mage_personality](../flags/heir_consort_mage_personality.md), and has heir has mage personality is yes:</li><ul><li>exile heir as = exiled_evil_heir_@ROOT</li></ul><li>country gets the modifier witch_king_death for 10 years</li><li>hidden effect:</li><ul><li>the event ˻anbennar_setup.8˼ happens</li></ul></ul><li>If has country flag is [lich_ruler](../flags/lich_ruler.md):</li><ul><li>hidden effect:</li><ul><li>the event ˻magic_project_lichdom.16˼ happens</li></ul></ul><li>If has country flag is [vampire_heir](../flags/vampire_heir.md):</li><ul><li>clr country flag [vampire_heir](../flags/vampire_heir.md)</li></ul><li>If has religion is infernal court:</li><ul><li>change religion = FROM</li></ul><li>hidden effect:</li><ul><li>clr country flag [witch_king_flag](../flags/witch_king_flag.md)</li><li>clear ruler vampire flags = yes</li><li>clr country flag [vampire_heir](../flags/vampire_heir.md)</li><li>clr country flag [lich_ruler](../flags/lich_ruler.md)</li><li>clr country flag [lich_ruler_has_phylactery](../flags/lich_ruler_has_phylactery.md)</li><li>clr country flag [lich_ruler_female](../flags/lich_ruler_female.md)</li><li>clr country flag [lich_ruler_male](../flags/lich_ruler_male.md)</li><li>clr country flag [exposed_lich_ruler](../flags/exposed_lich_ruler.md)</li><li>ruler clear saved spell schools = yes</li></ul><li>exile ruler as:</li><ul><li>name = exiled_evil_ruler_@ROOT</li></ul><li>add stability = -3</li><li>add prestige = -50</li></ul>
