#Information
 - Title: The Sun's Fleet
 - ID: jaddari_missions.20
#Description
The Sun's Fleet
#Options

___
##Send them on their way!

###AI weighting:
AI weights this option at 0


###One of the following randomly happens:
Outcome 1:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>hidden effect:</li><ul><li>1:</li><ul><li>If has check variable has which is jaddari eulos expedition, and check variable has value is 0:</li><ul><li>If random country has continent is north america, and has continent is south america; and does not have religion is the jadd; and  has any owned province has port:</li><ul><li>the event [The Sun's Fleet](../events/the_sun_s_fleet.md) happens</li></ul></ul></ul></ul></ul>
Outcome 2:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>event target:the suns fleet landing:</li><ul><li>fire province event [jaddari_missions.21](jaddari_missions.21_slug) in 1 days</li></ul></ul>

###Efects:<ul><li>add estate loyalty:</li><ul><li>estate = estate_church</li><li>loyalty = 10</li></ul></ul>

___
##Take their gifts

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>change religion = the_jadd</li><li>country gets the modifier "conversion_zeal" for 10 years</li><li>add manpower = 10</li><li>add treasury = 1000</li><li>event target:the suns fleet landing:</li><ul><li>custom tooltip = jaddari_spawn_10_light_ship_tt</li><li>spawn units for:</li><ul><li>amount = 10</li><li>type = light_ship</li><li>who = ROOT</li></ul></ul><li>hidden effect:</li><ul><li>1:</li><ul><li>subtract variable:</li><ul><li>which = jaddari_eulos_expedition</li><li>value = 1</li></ul><li>If has check variable has which is jaddari eulos expedition, and check variable has value is 0:</li><ul><li>If random country has continent is north america, and has continent is south america; and does not have religion is the jadd; and  has any owned province has port:</li><ul><li>the event [The Sun's Fleet](../events/the_sun_s_fleet.md) happens</li></ul></ul></ul><li>If has country modifier is ruinborn administration:</li><ul><li>F51:</li><ul><li>medium increase of ruinborn tolerance effect = yes</li><li>capital scope:</li><ul><li>add ruinborn minority size effect = yes</li></ul></ul></ul></ul></ul>
