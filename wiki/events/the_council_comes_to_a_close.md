#Information
 - Title: The Council Comes to a Close
 - ID: bulwar_flavour.48
#Description
The Council Comes to a Close
#Options

___
##The Cult is united, let the celebrations begin.

###Efects:<ul><li>If has country flag is [osc_centralization_synod_flag](../flags/osc_centralization_synod_flag.md):</li><ul><li>set estate privilege = estate_clergy_osc_centralization_synod</li></ul><li>Else if has country flag is [osc_centralization_high_coucil_flag](../flags/osc_centralization_high_coucil_flag.md):</li><ul><li>set estate privilege = estate_clergy_osc_centralization_high_council</li></ul><li>Else if has country flag is [osc_centralization_elected_kasra_flag](../flags/osc_centralization_elected_kasra_flag.md):</li><ul><li>set estate privilege = estate_clergy_osc_centralization_elected_kasra</li></ul><li>else:</li><ul><li>set estate privilege = estate_clergy_osc_centralization_nominated_kasra</li></ul><li>hidden effect:</li><ul><li>set country flag [osc_centralization_completed](../flags/osc_centralization_completed.md)</li><li>clr country flag [osc_centralization_started](../flags/osc_centralization_started.md)</li></ul></ul>
