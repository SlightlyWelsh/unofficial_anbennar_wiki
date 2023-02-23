#Information
 - Title: Growth of the [industrialization_province.GetName] Textile Industry
 - ID: industrialization_events.10
#Description
Growth of the [industrialization_province.GetName] Textile Industry
#Mean Time to Happen:
Base time = 1 days
 - Multiplied by 2 if has country flag is [spinning_jenny_flag](../flags/spinning_jenny_flag.md)
 - Multiplied by 2 if has calc true if has country flag is [atmospheric_engine_flag](../flags/atmospheric_engine_flag.md), and calc true if has country flag is coke blast furnaces flag, and calc true if has country flag is watt steam engine flag, and calc true if has country flag is rotherham plough flag, and calc true if has amount is 2
 - Multiplied by 1.5 if has calc true if has country flag is [atmospheric_engine_flag](../flags/atmospheric_engine_flag.md), and calc true if has country flag is coke blast furnaces flag, and calc true if has country flag is watt steam engine flag, and calc true if has country flag is rotherham plough flag, and calc true if has amount is 4
 - Multiplied by 1.5 if does not have any owned province has province flag is [swapped_to_cloth](../flags/swapped_to_cloth.md)
 - Multiplied by 0.5 if has num of owned provinces with has province flag is [swapped_to_cloth](../flags/swapped_to_cloth.md), and num of owned provinces with has value is 3
 - Multiplied by 0.5 if has num of owned provinces with has province flag is [swapped_to_cloth](../flags/swapped_to_cloth.md), and num of owned provinces with has value is 5
 - Multiplied by 0.5 if has num of owned provinces with has province flag is [swapped_to_cloth](../flags/swapped_to_cloth.md), and num of owned provinces with has value is 8
 - Multiplied by 0.5 if has num of owned provinces with has province flag is [swapped_to_cloth](../flags/swapped_to_cloth.md), and num of owned provinces with has value is 10
 - Multiplied by 0.5 if has num of owned provinces with has province flag is [swapped_to_cloth](../flags/swapped_to_cloth.md), and num of owned provinces with has value is 12

#Options

___
##Time waits for no man.

###Efects:<ul><li>event target:industrialization province:</li><ul><li>change trade goods = cloth</li><li>add base manpower = -1</li><li>set province flag [swapped_to_cloth](../flags/swapped_to_cloth.md)</li><li>add quarter industrialization effect = yes</li></ul></ul>
