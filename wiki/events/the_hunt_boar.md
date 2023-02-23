#Information
 - Title: The Hunt: Boar
 - ID: flavor_adenica.3
#Description
The Hunt: Boar
#Options

___
##Spring the trap

###Available if:
<li>has country flag [hunt_nobles](../flags/hunt_nobles.md)</li>

###Efects:<ul><li>highlight = yes</li><li>set country flag [hunt_nobles_save](../flags/hunt_nobles_save.md)</li></ul>

___
##My steel shall taste flesh, today

###Efects:<ul><li>If has country modifier is adenica adenican courser, and has country modifier is adenica alenic rouncey, and has country modifier is adenica arbarani destrier, and has country modifier is adenica elikhandi courser:</li><ul><li>set country flag [hunt_boar_horse_saved](../flags/hunt_boar_horse_saved.md)</li></ul><li>Else if has mil is 4, and does not have mil is 5:</li><ul><li>random:</li><ul><li>chance = 15</li><li>add ruler modifier:</li><ul><li>name = adenica_injured</li><li>duration = 1825</li></ul><li>set country flag [hunt_boar_injured](../flags/hunt_boar_injured.md)</li></ul><li>set country flag [hunt_boar_success](../flags/hunt_boar_success.md)</li></ul><li>Else if has mil is 5, and does not have mil is 6:</li><ul><li>random:</li><ul><li>chance = 5</li><li>add ruler modifier:</li><ul><li>name = adenica_injured</li><li>duration = 1825</li></ul><li>set country flag [hunt_boar_injured](../flags/hunt_boar_injured.md)</li></ul><li>set country flag [hunt_boar_success](../flags/hunt_boar_success.md)</li></ul><li>Else if has mil is 6:</li><ul></ul><li>else:</li><ul><li>random:</li><ul><li>chance = 25</li><li>add ruler modifier:</li><ul><li>name = adenica_injured</li><li>duration = 1825</li></ul><li>set country flag [hunt_boar_injured](../flags/hunt_boar_injured.md)</li></ul><li>set country flag [hunt_boar_success](../flags/hunt_boar_success.md)</li></ul></ul>

___
##Turn around and run

###Efects:<ul><li>If does not have ruler has max personalities is yes; and does not have ruler has personality is inspiring leader personality; and does not have ruler has personality is craven personality:</li><ul><li>random:</li><ul><li>chance = 50</li><li>add ruler personality = craven_personality</li></ul></ul><li>set country flag [hunt_boar_ran](../flags/hunt_boar_ran.md)</li></ul>
