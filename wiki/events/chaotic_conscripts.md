#Information
 - Title: Chaotic Conscripts
 - ID: subject_interaction_events.19
#Description
Chaotic Conscripts
#Mean Time to Happen:
Base time = 1 days
 - Multiplied by 0.5 if has country modifier is bad discipline

#Options

___
##If we close our eyes, maybe they will go away.

###Efects:<ul><li>If random owned province has any neighbor province has province flag is [si_province_rebels_flag](../flags/si_province_rebels_flag.md):</li><ul><li>spawn rebels:</li><ul><li>type = noble_rebels</li><li>size = 1</li></ul></ul><li>If random subject country has country flag is [si_vassal_rebels_flag](../flags/si_vassal_rebels_flag.md):</li><ul><li>If random owned province has province flag is [si_province_rebels_flag](../flags/si_province_rebels_flag.md):</li><ul><li>clr province flag [si_province_rebels_flag](../flags/si_province_rebels_flag.md)</li><li>spawn rebels:</li><ul><li>type = noble_rebels</li><li>size = 1</li></ul></ul><li>clr country flag [si_vassal_rebels_flag](../flags/si_vassal_rebels_flag.md)</li></ul></ul>

___
##Try to soothe these turbulent forces, let them come home if that is what they wish.

###Efects:<ul><li>hidden effect:</li><ul><li>If random subject country has country flag is [si_vassal_rebels_flag](../flags/si_vassal_rebels_flag.md):</li><ul><li>clr country flag [si_vassal_rebels_flag](../flags/si_vassal_rebels_flag.md)</li><li>If random owned province has province flag is [si_province_rebels_flag](../flags/si_province_rebels_flag.md):</li><ul><li>clr province flag [si_province_rebels_flag](../flags/si_province_rebels_flag.md)</li></ul></ul></ul><li>add mil power = -25</li><li>add army tradition = -5</li></ul>
