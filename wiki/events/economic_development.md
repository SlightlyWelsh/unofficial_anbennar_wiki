#Information
 - Title: Economic Development
 - ID: industrialization_events.9
#Description
Economic Development
#Mean Time to Happen:
Base time = 1 days
 - Multiplied by 2 if has calc true if has country flag is [atmospheric_engine_flag](../flags/atmospheric_engine_flag.md), and calc true if has country flag is coke blast furnaces flag, and calc true if has country flag is watt steam engine flag, and calc true if has country flag is rotherham plough flag, and calc true if has country flag is flying shuttle flag, and calc true if has country flag is spinning jenny flag, and calc true if has amount is 3
 - Multiplied by 1.5 if has calc true if has country flag is [atmospheric_engine_flag](../flags/atmospheric_engine_flag.md), and calc true if has country flag is coke blast furnaces flag, and calc true if has country flag is watt steam engine flag, and calc true if has country flag is rotherham plough flag, and calc true if has country flag is flying shuttle flag, and calc true if has country flag is spinning jenny flag, and calc true if has amount is 6
 - Multiplied by 1.25 if has any owned province has latent trade goods is coal
 - Multiplied by 1.5 if does not have any owned province has province flag is [had_economic_urbanization](../flags/had_economic_urbanization.md)
 - Multiplied by 0.5 if has num of owned provinces with has province flag is [had_economic_urbanization](../flags/had_economic_urbanization.md), and num of owned provinces with has value is 15
 - Multiplied by 0.5 if has num of owned provinces with has province flag is [had_economic_urbanization](../flags/had_economic_urbanization.md), and num of owned provinces with has value is 20
 - Multiplied by 0.5 if has num of owned provinces with has province flag is [had_economic_urbanization](../flags/had_economic_urbanization.md), and num of owned provinces with has value is 25
 - Multiplied by 0.5 if has num of owned provinces with has province flag is [had_economic_urbanization](../flags/had_economic_urbanization.md), and num of owned provinces with has value is 30

#Options

___
##[industrialization_province.GetName] will be a great home for them.

###Efects:<ul><li>event target:industrialization province:</li><ul><li>add base production = 1</li><li>add base tax = 1</li><li>add quarter industrialization effect = yes</li><li>If area has owned by is ROOT, and does not have province flag is [had_economic_urbanization](../flags/had_economic_urbanization.md):</li><ul><li>add province modifier:</li><ul><li>name = "economic_urbanization_modifier"</li><li>duration = 3650</li></ul><li>set province flag [had_economic_urbanization](../flags/had_economic_urbanization.md)</li></ul></ul><li>If random owned province has unindustrialized province trigger is yes, and  has base manpower is 3:</li><ul><li>add base manpower = -2</li></ul></ul>
