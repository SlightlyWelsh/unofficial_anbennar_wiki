#Information
 - Title: Hostility to New Production Techniques
 - ID: industrialization_events.17
#Description
Hostility to New Production Techniques
#Mean Time to Happen:
Base time = 1 days
 - Multiplied by 1.5 if has calc true if has country flag is [atmospheric_engine_flag](../flags/atmospheric_engine_flag.md), and calc true if has country flag is coke blast furnaces flag, and calc true if has country flag is watt steam engine flag, and calc true if has country flag is rotherham plough flag, and calc true if has country flag is flying shuttle flag, and calc true if has country flag is spinning jenny flag, and calc true if has amount is 3
 - Multiplied by 1.5 if has calc true if has country flag is [atmospheric_engine_flag](../flags/atmospheric_engine_flag.md), and calc true if has country flag is coke blast furnaces flag, and calc true if has country flag is watt steam engine flag, and calc true if has country flag is rotherham plough flag, and calc true if has country flag is flying shuttle flag, and calc true if has country flag is spinning jenny flag, and calc true if has amount is 6
 - Multiplied by 1.25 if has coal is 3, and does not have furnace is 3
 - Multiplied by 1.5 if has furnace is 3
 - Multiplied by 1.25 if has coal is 5, and does not have furnace is 5
 - Multiplied by 1.5 if has furnace is 5
 - Multiplied by 0.5 if has num of owned provinces with has province flag is [luddite_protests](../flags/luddite_protests.md), and num of owned provinces with has value is 10
 - Multiplied by 0.5 if has num of owned provinces with has province flag is [luddite_protests](../flags/luddite_protests.md), and num of owned provinces with has value is 12
 - Multiplied by 0.5 if has num of owned provinces with has province flag is [luddite_protests](../flags/luddite_protests.md), and num of owned provinces with has value is 14
 - Multiplied by 0.25 if has num of owned provinces with has province flag is [luddite_protests](../flags/luddite_protests.md), and num of owned provinces with has value is 16
 - Multiplied by 0.25 if has num of owned provinces with has province flag is [luddite_protests](../flags/luddite_protests.md), and num of owned provinces with has value is 18
 - Multiplied by 0.25 if has num of owned provinces with has province flag is [luddite_protests](../flags/luddite_protests.md), and num of owned provinces with has value is 20
 - Multiplied by 0.25 if has num of owned provinces with has province flag is [luddite_protests](../flags/luddite_protests.md), and num of owned provinces with has value is 22

#Options

___
##Luddites!

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>event target:luddite province:</li><ul><li>add devastation = 25</li><li>spawn rebels:</li><ul><li>type = anti_tax_rebels</li><li>size = 2</li></ul></ul></ul>

___
##We will have to negotiate.

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>event target:luddite province:</li><ul><li>add devastation = 10</li><li>add province modifier:</li><ul><li>name = "gave_in_to_luddite_protests"</li><li>duration = 3650</li></ul></ul></ul>
