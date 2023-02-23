#Information
 - Title: Eunuch Attempt on [Root.Heir.GetTitle]’s Life Thwarted
 - ID: bianfang.34
#Description
Eunuch Attempt on [Root.Heir.GetTitle]’s Life Thwarted
#Options

___
##We still have need of the eunuchs. Spare them.

###Efects:<ul><li>add prestige = -25</li><li>add estate influence modifier:</li><ul><li>estate = estate_eunuchs</li><li>desc = EST_BIANFANG_EUNUCH_ASSASSINATION_ATTEMPT_ROYAL_FAMILY</li><li>influence = -20</li><li>duration = 5475</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_eunuchs</li><li>loyalty = 15</li></ul><li>increase tyrant benevolent 1 = yes</li></ul>

___
##Their mutilation is not yet complete. Off with their heads.

###Efects:<ul><li>If has estate influence has estate is estate eunuchs, and estate influence has influence is 80:</li><ul><li>random owned province:</li><ul><li>spawn rebels:</li><ul><li>type = noble_rebels</li><li>size = 3</li></ul></ul></ul><li>Else if has estate influence has estate is estate eunuchs, and estate influence has influence is 60:</li><ul><li>random owned province:</li><ul><li>spawn rebels:</li><ul><li>type = noble_rebels</li><li>size = 2</li></ul></ul></ul><li>else:</li><ul><li>random owned province:</li><ul><li>spawn rebels:</li><ul><li>type = noble_rebels</li><li>size = 1</li></ul></ul></ul><li>set country flag [anti_eunuch_country](../flags/anti_eunuch_country.md)</li><li>add ruler modifier:</li><ul><li>name = eunuchs_purged</li><li>duration = -1</li></ul><li>increase tyrant ruthless 2 = yes</li></ul>
