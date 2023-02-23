#Information
 - Title: The End of the Deioderan
 - ID: jaddari_missions.202
#Description
The End of the Deioderan
#Options

___
##Well, so be it

###Available if:
<li>had country flag [deioderan_started_flag](../flags/deioderan_started_flag.md) for 3650 days</li>

###Efects:<ul><li>add stability or adm power = yes</li><li>If has capital scope has continent is asia:</li><ul><li>override country name = POST_EAST_JADD_EMPIRE</li><li>F99:</li><ul><li>override country name = POST_WEST_JADD_EMPIRE</li></ul></ul><li>else:</li><ul><li>override country name = POST_WEST_JADD_EMPIRE</li><li>F99:</li><ul><li>override country name = POST_EAST_JADD_EMPIRE</li></ul></ul><li>hidden effect:</li><ul><li>set country flag [had_deioderan](../flags/had_deioderan.md)</li><li>clr country flag [jaddari_static_court](../flags/jaddari_static_court.md)</li><li>clr country flag [deioderan_started_flag](../flags/deioderan_started_flag.md)</li><li>F99:</li><ul><li>clr country flag [jaddari_static_court](../flags/jaddari_static_court.md)</li></ul></ul></ul>

___
##The bond will be stronger than ever.

###Available if:
<li>has country flag [jaddari_empire_united_by_diplomacy](../flags/jaddari_empire_united_by_diplomacy.md)</li>

###Efects:<ul><li>restore country name = yes</li><li>country gets the modifier jaddari_empire_of_harmony for 100 years</li><li>add stability = 2</li><li>inherit = F99</li><li>hidden effect:</li><ul><li>set country flag [had_deioderan](../flags/had_deioderan.md)</li><li>clr country flag [jaddari_static_court](../flags/jaddari_static_court.md)</li><li>clr country flag [deioderan_started_flag](../flags/deioderan_started_flag.md)</li><li>F99:</li><ul><li>clr country flag [jaddari_static_court](../flags/jaddari_static_court.md)</li></ul></ul><li>the event ˻jadd_empire.1˼ happens</li></ul>

___
##There is only one Sun.

###Available if:
<li>None of the following:</li><ul><li>had country flag [deioderan_started_flag](../flags/deioderan_started_flag.md) for 3650 days</li><li>has country flag [jaddari_empire_united_by_diplomacy](../flags/jaddari_empire_united_by_diplomacy.md)</li></ul>

###Efects:<ul><li>restore country name = yes</li><li>country gets the modifier jaddari_one_divine_herald for 100 years</li><li>add absolutism = 10</li><li>add stability or adm power = yes</li><li>inherit = F99</li><li>hidden effect:</li><ul><li>set country flag [had_deioderan](../flags/had_deioderan.md)</li><li>clr country flag [jaddari_static_court](../flags/jaddari_static_court.md)</li><li>clr country flag [deioderan_started_flag](../flags/deioderan_started_flag.md)</li><li>F99:</li><ul><li>clr country flag [jaddari_static_court](../flags/jaddari_static_court.md)</li></ul></ul><li>the event ˻jadd_empire.1˼ happens</li></ul>
