#Information
 - Title: The [iron_province.GetName] Metalworks
 - ID: industrialization_events.14
#Description
The [iron_province.GetName] Metalworks
#Mean Time to Happen:
Base time = 1 days
 - Multiplied by 1.5 if has calc true if has country flag is [atmospheric_engine_flag](../flags/atmospheric_engine_flag.md), and calc true if has country flag is coke blast furnaces flag, and calc true if has country flag is watt steam engine flag, and calc true if has amount is 2
 - Multiplied by 1.5 if has calc true if has country flag is [atmospheric_engine_flag](../flags/atmospheric_engine_flag.md), and calc true if has country flag is coke blast furnaces flag, and calc true if has country flag is watt steam engine flag, and calc true if has amount is 3
 - Multiplied by 1.25 if has coal is 3, and does not have furnace is 3
 - Multiplied by 1.5 if has furnace is 3
 - Multiplied by 1.25 if has coal is 5, and does not have furnace is 5
 - Multiplied by 1.5 if has furnace is 5
 - Multiplied by 1.5 if does not have any owned province has province flag is [metalwork_center](../flags/metalwork_center.md)
 - Multiplied by 0.5 if has num of owned provinces with has province flag is [metalwork_center](../flags/metalwork_center.md), and num of owned provinces with has value is 4
 - Multiplied by 0.25 if has num of owned provinces with has province flag is [metalwork_center](../flags/metalwork_center.md), and num of owned provinces with has value is 6
 - Multiplied by 0.25 if has num of owned provinces with has province flag is [metalwork_center](../flags/metalwork_center.md), and num of owned provinces with has value is 8
 - Multiplied by 0.25 if has num of owned provinces with has province flag is [metalwork_center](../flags/metalwork_center.md), and num of owned provinces with has value is 10
 - Multiplied by 0.25 if has num of owned provinces with has province flag is [metalwork_center](../flags/metalwork_center.md), and num of owned provinces with has value is 12
 - Multiplied by 0.25 if has num of owned provinces with has province flag is [metalwork_center](../flags/metalwork_center.md), and num of owned provinces with has value is 14
 - Multiplied by 0.25 if has num of owned provinces with has province flag is [metalwork_center](../flags/metalwork_center.md), and num of owned provinces with has value is 15

#Options

___
##This is the dawn of a new era.

###Efects:<ul><li>event target:iron province:</li><ul><li>add base production = 4</li><li>add province modifier:</li><ul><li>name = "metalworks_modifier"</li><li>duration = 7300</li></ul><li>add quarter industrialization effect = yes</li></ul><li>If random owned province has unindustrialized province trigger is yes, and  has base tax is 2, and  has base manpower is 2:</li><ul><li>add base manpower = -1</li><li>add base tax = -1</li></ul></ul>
