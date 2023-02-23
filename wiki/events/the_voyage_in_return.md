#Information
 - Title: The Voyage: In Return
 - ID: flavor_feiten.97
#Description
The Voyage: In Return
#Options

___
##The world suddenly seems much smaller

###Efects:<ul><li>custom tooltip = feiten_voyage_return_tt</li><li>If while has check variable has which is feiten voyage light ships left, and check variable has value is 1:</li><ul><li>subtract variable:</li><ul><li>which = feiten_voyage_light_ships_left</li><li>value = 1</li></ul><li>4879:</li><ul><li>light ship = ROOT</li></ul><li>add treasury = 50</li><li>If has country flag is [feiten_voyage_sramaya_markets](../flags/feiten_voyage_sramaya_markets.md):</li><ul><li>add treasury = 25</li></ul></ul><li>set country flag [feiten_voyage_concluded](../flags/feiten_voyage_concluded.md)</li><li>set country flag [feiten_skyposts_unlocked](../flags/feiten_skyposts_unlocked.md)</li><li>If has check variable has which is feiten voyage mythos, and check variable has value is 6:</li><ul><li>country gets the modifier feiten_mythos_of_the_voyage_max for 100 years</li></ul><li>Else if has check variable has which is feiten voyage mythos, and check variable has value is 4:</li><ul><li>country gets the modifier feiten_mythos_of_the_voyage_mid for 100 years</li></ul><li>else:</li><ul><li>country gets the modifier feiten_mythos_of_the_voyage_min for 100 years</li></ul><li>custom tooltip = feiten_the_world_our_oyster_tt</li><li>If has country flag is [feiten_davharral_skypost](../flags/feiten_davharral_skypost.md):</li><ul><li>2913:</li><ul><li>add province triggered modifier = feiten_skyport_handler_mod</li></ul></ul><li>Else if has country flag is [feiten_murdkather_skypost](../flags/feiten_murdkather_skypost.md):</li><ul><li>2037:</li><ul><li>add province triggered modifier = feiten_skyport_handler_mod</li></ul></ul><li>Else if has country flag is [feiten_bagcatir_skypost](../flags/feiten_bagcatir_skypost.md):</li><ul><li>2022:</li><ul><li>add province triggered modifier = feiten_skyport_handler_mod</li></ul></ul></ul>
