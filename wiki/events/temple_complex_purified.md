#Information
 - Title: Temple Complex Purified
 - ID: spirits.008
#Description
Temple Complex Purified
#Options

___
##Brilliant!

###Efects:<ul><li>goto = ROOT</li><li>If has province flag is [was_temple_complex](../flags/was_temple_complex.md):</li><ul><li>hidden effect:</li><ul><li>purify temple wards = yes</li><li>clr province flag [was_temple_complex](../flags/was_temple_complex.md)</li></ul><li>remove province triggered modifier = corrupted_temple_complex</li><li>add permanent province modifier:</li><ul><li>name = temple_complex</li><li>duration = -1</li></ul></ul><li>Else if has province flag is [was_damaged_temple_complex](../flags/was_damaged_temple_complex.md):</li><ul><li>hidden effect:</li><ul><li>purify temple wards = yes</li><li>clr province flag [was_damaged_temple_complex](../flags/was_damaged_temple_complex.md)</li></ul><li>remove province triggered modifier = corrupted_temple_complex</li><li>add permanent province modifier:</li><ul><li>name = damaged_temple_complex</li><li>duration = -1</li></ul></ul><li>Else if has province flag is [was_derelict_temple_complex](../flags/was_derelict_temple_complex.md):</li><ul><li>hidden effect:</li><ul><li>purify temple wards = yes</li><li>clr province flag [was_derelict_temple_complex](../flags/was_derelict_temple_complex.md)</li></ul><li>remove province triggered modifier = corrupted_temple_complex</li><li>add permanent province modifier:</li><ul><li>name = derelict_temple_complex</li><li>duration = -1</li></ul></ul></ul>
