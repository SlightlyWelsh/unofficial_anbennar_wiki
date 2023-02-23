#Information
 - Title: Assassination Attempt on the szal-Fazil
 - ID: new_sun_cult.250
#Description
Assassination Attempt on the szal-Fazil
#Options

___
##Send soldiers to help the priests and disband the mob.

###Efects:<ul><li>add stability = -1</li><li>add legitimacy = -5</li><li>If has saved event target is nsc temple mob:</li><ul><li>event target:nsc temple mob:</li><ul><li>spawn rebels:</li><ul><li>type = leadered_peasant_rebels</li><li>size = 2</li></ul></ul></ul><li>else:</li><ul><li>capital scope:</li><ul><li>spawn rebels:</li><ul><li>type = leadered_peasant_rebels</li><li>size = 2</li></ul></ul></ul></ul>

___
##The clergy must take responsibility for their actions.

###Efects:<ul><li>If has saved event target is nsc temple mob:</li><ul><li>event target:nsc temple mob:</li><ul><li>If has building is temple:</li><ul><li>remove building = temple</li></ul><li>else:</li><ul><li>remove building = cathedral</li></ul><li>add devastation = 15</li></ul></ul><li>else:</li><ul><li>capital scope:</li><ul><li>add devastation = 15</li></ul></ul><li>add estate loyalty:</li><ul><li>estate = estate_church</li><li>loyalty = -10</li></ul></ul>
