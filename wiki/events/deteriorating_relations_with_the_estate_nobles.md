#Information
 - Title: Deteriorating Relations with the $ESTATE_NOBLES$
 - ID: nobles_estate_events.8
#Description
Deteriorating Relations with the $ESTATE_NOBLES$
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Leave them be.

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>add estate influence modifier:</li><ul><li>estate = estate_nobles</li><li>desc = EST_VAL_NOBLES_EXTORTED_RIGHTS</li><li>influence = 10</li><li>duration = 5475</li></ul><li>If every owned province has province flag is [noble_estate_revolt](../flags/noble_estate_revolt.md):</li><ul><li>add local autonomy = 33</li></ul><li>hidden effect:</li><ul><li>If every owned province has province flag is [noble_estate_revolt](../flags/noble_estate_revolt.md):</li><ul><li>clr province flag [noble_estate_revolt](../flags/noble_estate_revolt.md)</li></ul></ul></ul>

___
##Force them to accept state authority.

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>add estate influence modifier:</li><ul><li>estate = estate_nobles</li><li>desc = EST_VAL_NOBLES_DENIED_RIGHTS</li><li>influence = -10</li><li>duration = 5475</li></ul><li>If every owned province has province flag is [noble_estate_revolt](../flags/noble_estate_revolt.md):</li><ul><li>clr province flag [noble_estate_revolt](../flags/noble_estate_revolt.md)</li><li>spawn rebels:</li><ul><li>type = noble_rebels</li><li>size = 1</li></ul></ul></ul>
