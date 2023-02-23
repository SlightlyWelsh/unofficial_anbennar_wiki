#Information
 - Title: The Hunt: Cockatrice
 - ID: flavor_adenica.6
#Description
The Hunt: Cockatrice
#Options

___
##Do something, mages!

###Available if:
<li>has country flag [hunt_mages](../flags/hunt_mages.md)</li>

###Efects:<ul><li>highlight = yes</li><li>set country flag [hunt_cockatrice_mages_save](../flags/hunt_cockatrice_mages_save.md)</li></ul>

___
##Try and break free of the spell

###Efects:<ul><li>If does not have ruler has max personalities is yes; and does not have ruler has personality is craven personality:</li><ul><li>random:</li><ul><li>chance = 75</li><li>add ruler personality = bold_fighter_personality</li></ul></ul><li>If has mil is 4, and does not have mil is 5:</li><ul><li>random list:</li><ul><li>25:</li><ul><li>add ruler modifier:</li><ul><li>name = adenica_injured</li><li>duration = 1825</li></ul><li>set country flag [hunt_cockatrice_injured](../flags/hunt_cockatrice_injured.md)</li></ul><li>75:</li><ul><li>set country flag [hunt_cockatrice_distracted](../flags/hunt_cockatrice_distracted.md)</li></ul></ul></ul><li>Else if has mil is 5, and does not have mil is 6:</li><ul><li>random list:</li><ul><li>15:</li><ul><li>add ruler modifier:</li><ul><li>name = adenica_injured</li><li>duration = 1825</li></ul><li>set country flag [hunt_cockatrice_injured](../flags/hunt_cockatrice_injured.md)</li></ul><li>85:</li><ul><li>set country flag [hunt_cockatrice_distracted](../flags/hunt_cockatrice_distracted.md)</li></ul></ul></ul><li>Else if has mil is 6:</li><ul><li>random list:</li><ul><li>5:</li><ul><li>add ruler modifier:</li><ul><li>name = adenica_injured</li><li>duration = 1825</li></ul><li>set country flag [hunt_cockatrice_injured](../flags/hunt_cockatrice_injured.md)</li></ul><li>95:</li><ul><li>set country flag [hunt_cockatrice_distracted](../flags/hunt_cockatrice_distracted.md)</li></ul></ul></ul><li>else:</li><ul><li>random list:</li><ul><li>50:</li><ul><li>add ruler modifier:</li><ul><li>name = adenica_injured</li><li>duration = 1825</li></ul><li>set country flag [hunt_cockatrice_injured](../flags/hunt_cockatrice_injured.md)</li></ul><li>50:</li><ul><li>set country flag [hunt_cockatrice_distracted](../flags/hunt_cockatrice_distracted.md)</li></ul></ul></ul></ul>

___
##The end is near...

###Efects:<ul><li>If does not have ruler has max personalities is yes; and does not have ruler has personality is inspiring leader personality; and does not have ruler has personality is craven personality:</li><ul><li>random:</li><ul><li>chance = 50</li><li>add ruler personality = craven_personality</li></ul></ul><li>set country flag [hunt_cockatrice_fear](../flags/hunt_cockatrice_fear.md)</li></ul>
