#Information
 - Title: Tensions between Nomads and Sedentary Population
 - ID: tribal_estate_events.1
#Description
Tensions between Nomads and Sedentary Population
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Reprimand the Chiefs.

###AI weighting:
AI weights this option at 75
 - Multiplied by 0.5 if does not have estate loyalty has estate is estate nomadic tribes, and estate loyalty has loyalty is 40
 - Multiplied by 1.5 if has estate influence has estate is estate nomadic tribes, and estate influence has influence is 65


###Efects:<ul><li>add estate loyalty:</li><ul><li>estate = estate_nomadic_tribes</li><li>loyalty = -15</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_nomadic_tribes</li><li>desc = EST_VAL_TRIBES_REPRIMANDED</li><li>influence = -10</li><li>duration = 5475</li></ul></ul>

___
##Support the Chiefs.

###AI weighting:
AI weights this option at 25
 - Multiplied by 1.5 if does not have estate loyalty has estate is estate nomadic tribes, and estate loyalty has loyalty is 40
 - Multiplied by 0.5 if has estate influence has estate is estate nomadic tribes, and estate influence has influence is 65


###Efects:<ul><li>If random owned province has province flag is [conflict_regarding_tax_collection](../flags/conflict_regarding_tax_collection.md):</li><ul><li>spawn rebels:</li><ul><li>size = 1</li><li>type = nationalist_rebels</li></ul><li>clr province flag [conflict_regarding_tax_collection](../flags/conflict_regarding_tax_collection.md)</li></ul><li>If random owned province has province flag is [conflict_regarding_tax_collection](../flags/conflict_regarding_tax_collection.md), and  has owner has num of cities is 10:</li><ul><li>spawn rebels:</li><ul><li>size = 1</li><li>type = nationalist_rebels</li></ul><li>clr province flag [conflict_regarding_tax_collection](../flags/conflict_regarding_tax_collection.md)</li></ul><li>If random owned province has province flag is [conflict_regarding_tax_collection](../flags/conflict_regarding_tax_collection.md), and  has owner has num of cities is 15:</li><ul><li>spawn rebels:</li><ul><li>size = 1</li><li>type = nationalist_rebels</li></ul><li>clr province flag [conflict_regarding_tax_collection](../flags/conflict_regarding_tax_collection.md)</li></ul><li>every owned province:</li><ul><li>clr province flag [conflict_regarding_tax_collection](../flags/conflict_regarding_tax_collection.md)</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_nomadic_tribes</li><li>loyalty = 15</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_nomadic_tribes</li><li>desc = EST_VAL_TRIBES_ALLOWED_FREE_REIGN</li><li>influence = 10</li><li>duration = 5475</li></ul></ul>
