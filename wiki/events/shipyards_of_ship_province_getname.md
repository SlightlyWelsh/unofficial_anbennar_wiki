#Information
 - Title: Shipyards of [ship_province.GetName]
 - ID: industrialization_events.16
#Description
Shipyards of [ship_province.GetName]
#Mean Time to Happen:
Base time = 1 days
 - Multiplied by 1.5 if has country flag is [atmospheric_engine_flag](../flags/atmospheric_engine_flag.md)
 - Multiplied by 1.5 if has country flag is [watt_steam_engine_flag](../flags/watt_steam_engine_flag.md)
 - Multiplied by 1.25 if has coal is 3, and does not have furnace is 3
 - Multiplied by 1.5 if has furnace is 3
 - Multiplied by 1.25 if has coal is 5, and does not have furnace is 5
 - Multiplied by 1.5 if has furnace is 5
 - Multiplied by 1.5 if does not have any owned province has province flag is [shipyards_of_x](../flags/shipyards_of_x.md)
 - Multiplied by 0.5 if has num of owned provinces with has province flag is [shipyards_of_x](../flags/shipyards_of_x.md), and num of owned provinces with has value is 4
 - Multiplied by 0.5 if has num of owned provinces with has province flag is [shipyards_of_x](../flags/shipyards_of_x.md), and num of owned provinces with has value is 5
 - Multiplied by 0.25 if has num of owned provinces with has province flag is [shipyards_of_x](../flags/shipyards_of_x.md), and num of owned provinces with has value is 7
 - Multiplied by 0.25 if has num of owned provinces with has province flag is [shipyards_of_x](../flags/shipyards_of_x.md), and num of owned provinces with has value is 9
 - Multiplied by 0.25 if has num of owned provinces with has province flag is [shipyards_of_x](../flags/shipyards_of_x.md), and num of owned provinces with has value is 11
 - Multiplied by 0.25 if has num of owned provinces with has province flag is [shipyards_of_x](../flags/shipyards_of_x.md), and num of owned provinces with has value is 13
 - Multiplied by 0.25 if has num of owned provinces with has province flag is [shipyards_of_x](../flags/shipyards_of_x.md), and num of owned provinces with has value is 15

#Options

___
##[Root.GetName] rules the waves.

###Efects:<ul><li>event target:ship province:</li><ul><li>add base production = 4</li><li>add province modifier:</li><ul><li>name = "shipyards_of_x_modifier"</li><li>duration = 7300</li></ul><li>add quarter industrialization effect = yes</li></ul><li>If random owned province has unindustrialized province trigger is yes, and  has base tax is 2, and  has base manpower is 2:</li><ul><li>add base manpower = -1</li><li>add base tax = -1</li></ul></ul>
