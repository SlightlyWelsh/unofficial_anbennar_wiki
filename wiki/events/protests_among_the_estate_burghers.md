#Information
 - Title: Protests among the $ESTATE_BURGHERS$
 - ID: burghers_estate_events.15
#Description
Protests among the $ESTATE_BURGHERS$
#Mean Time to Happen:
Base time = 1 days
 - Multiplied by 2.0 if does not have estate loyalty has estate is estate burghers, and estate loyalty has loyalty is 15

#Options

___
##They must be joking!

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>If every owned province has province flag is [city_protests](../flags/city_protests.md):</li><ul><li>clr province flag [city_protests](../flags/city_protests.md)</li><li>spawn rebels:</li><ul><li>type = particularist_rebels</li><li>size = 1</li></ul></ul></ul>

___
##Give in to their demands.

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>If every owned province has province flag is [city_protests](../flags/city_protests.md):</li><ul><li>clr province flag [city_protests](../flags/city_protests.md)</li><li>add local autonomy = 33</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_burghers</li><li>loyalty = 15</li></ul></ul>
