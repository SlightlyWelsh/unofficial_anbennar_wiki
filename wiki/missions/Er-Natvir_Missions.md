This is a list of all [missions](missions.md) of [Er-Natvir](Er-Natvir.md)

| Mission | Completion requirements | Effects | Prerequisites |
| ----- | ------ | ----- | ------ |
| <a name="ernatvir_dagrite_repair">Dagrite Repair Shops</a><br />*Dagrite, a metal prized for its ability to repair itself when in the presence of an electric current, was used in the construction of all dwarven rails. We must build manufacturing plants dedicated to restoring dagrite.* | <li>num of owned provinces with:</li><ul><li>value is at least 3</li><li>trade goods is copper</li><li>has building weapons</li></ul> | <li>custom tooltip = ernatvir_dagrite_repair_tooltip</li><li>hidden effect:</li><ul><li>If random owned province does not have province flag is [applied_effect](../flags/applied_effect.md); and  has trade goods is copper, and  has building is weapons:</li><ul><li>add base tax = 1</li><li>add base production = 1</li><li>add base manpower = 1</li><li>set province flag [applied_effect](../flags/applied_effect.md)</li></ul><li>If random owned province does not have province flag is [applied_effect](../flags/applied_effect.md); and  has trade goods is copper, and  has building is weapons:</li><ul><li>add base tax = 1</li><li>add base production = 1</li><li>add base manpower = 1</li><li>set province flag [applied_effect](../flags/applied_effect.md)</li></ul><li>If random owned province does not have province flag is [applied_effect](../flags/applied_effect.md); and  has trade goods is copper, and  has building is weapons:</li><ul><li>add base tax = 1</li><li>add base production = 1</li><li>add base manpower = 1</li><li>set province flag [applied_effect](../flags/applied_effect.md)</li></ul><li>If every owned province has province flag is [applied_effect](../flags/applied_effect.md):</li><ul><li>clr province flag [applied_effect](../flags/applied_effect.md)</li></ul></ul> |  |
| <a name="ernatvir_lighting_dwarovar">Lighting the Dwarovar</a><br />*High quality gems are candidates to be enchanted with runes, enabling them to produce light while requiring little maintenance in the deep tunnels of the Dwarovar. We must set up a grand workshop to produce these runelights.* | <li>any owned province:</li><ul><li>has building mills</li><li>base production is at least 15</li><li>trade goods is gems</li></ul> | <li>If random owned province has building is mills, and  has base production is 15, and  has trade goods is gems:</li><ul><li>add permanent province modifier:</li><ul><li>name = ernatvir_runelight_factory</li><li>duration = -1</li></ul></ul> | [Dagrite Repair Shops](#ernatvir_dagrite_repair)<br /> |
| <a name="ernatvir_advanced_vehicles">Advanced Vehicles</a><br />*We now have secured all the resources we need to produce more sophisticated vehicles, such as powered mine carts, wagons, and diggers. This will greatly help us transport dwarves and supplies across our entire country.* | <li>any owned province:</li><ul><li>has building university</li><li>base production is at least 25</li><li>Any of the following:</li><ul><li>trade goods is damestear</li><li>trade goods  is coal</li></ul></ul> | <li>country gets the modifier ernatvir_transportation_boom for 20 years</li> | [Superior Materials](#ernatvir_superior_materials)<br />[Lighting the Dwarovar](#ernatvir_lighting_dwarovar)<br /> |

| Mission | Completion requirements | Effects | Prerequisites |
| ----- | ------ | ----- | ------ |
| <a name="ernatvir_new_foundries">New Foundries</a><br />*Er-Natvir's prodigious steel output once made our ancestors a powerful economic force. We must rekindle the foundries of Er-Natvir!* | <li>num of owned provinces with:</li><ul><li>value is at least 4</li><li>trade goods is iron</li><li>has production building trigger yes</li></ul> | <li>custom tooltip = ernatvir_new_foundries_tooltip</li><li>hidden effect:</li><ul><li>If random owned province has trade goods is iron, and  has production building trigger is yes, and does not have province flag is [applied_effect](../flags/applied_effect.md):</li><ul><li>add base production = 2</li><li>set province flag [applied_effect](../flags/applied_effect.md)</li></ul><li>If random owned province has trade goods is iron, and  has production building trigger is yes, and does not have province flag is [applied_effect](../flags/applied_effect.md):</li><ul><li>add base production = 2</li><li>set province flag [applied_effect](../flags/applied_effect.md)</li></ul><li>If random owned province has trade goods is iron, and  has production building trigger is yes, and does not have province flag is [applied_effect](../flags/applied_effect.md):</li><ul><li>add base production = 2</li><li>set province flag [applied_effect](../flags/applied_effect.md)</li></ul><li>If random owned province has trade goods is iron, and  has production building trigger is yes, and does not have province flag is [applied_effect](../flags/applied_effect.md):</li><ul><li>add base production = 2</li><li>set province flag [applied_effect](../flags/applied_effect.md)</li></ul><li>If every owned province has province flag is [applied_effect](../flags/applied_effect.md):</li><ul><li>clr province flag [applied_effect](../flags/applied_effect.md)</li></ul></ul> |  |
| <a name="ernatvir_superior_materials">Superior Materials</a><br />*Mithril, a rare, lightweight and strong metal, is highly prized for its superior qualities compared to iron or steel. We must secure a source of this metal to give us an edge over our competition!* | <li>any owned province:</li><ul><li>has building weapons</li><li>base production is at least 20</li><li>trade goods is mithril</li></ul> | <li>country gets the modifier ernatvir_advanced_alloys until otherwise removed</li> | [New Foundries](#ernatvir_new_foundries)<br /> |
| <a name="ernatvir_depths_of_trade">Depths of Trade</a><br />*Er-Natvir was once one of the busiest trading holds in the Dwarovar. We must restore our hold to its former glory!* | <li>2931:</li><ul><li>has dwarven hold 6 yes</li><li>owned by is this nation</li></ul> | <li>country gets the modifier ernatvir_revitalized_economy for 25 years</li> |  |
| <a name="ernatvir_the_train_hub">The Train Hub</a><br />*As the central station to many trains travelling the Dwarovar, Er-Natvir offers us a perfect location to begin the construction of a massive train hub, capable of providing greater service across our entire empire! We must build it!* | <li>2931:</li><ul><li>has dwarven hold 8 yes</li><li>owned by is this nation</li></ul><li>treasury is at least 10000</li><li>adm power is at least 200</li><li>dip power is at least 200</li><li>mil power is at least 200</li><li>num of owned provinces with:</li><ul><li>value is at least 30</li><li>has terrain dwarven_road</li><li>None of the following:</li><ul><li>has province modifier dwarovar_rail</li></ul></ul> | <li>add treasury = -10000</li><li>add adm power = -200</li><li>add dip power = -200</li><li>add mil power = -200</li><li>2931:</li><ul><li>add permanent province modifier:</li><ul><li>name = ernatvir_constructing_hub</li><li>duration = -1</li></ul></ul><li>custom tooltip = ernatvir_begin_construction_tooltip</li><li>hidden effect:</li><ul><li>2931:</li><ul><li>fire province event [ernatvir.1](ernatvir.1_slug) in 1460 to 730 days</li></ul></ul> | [Depths of Trade](#ernatvir_depths_of_trade)<br /> |

| Mission | Completion requirements | Effects | Prerequisites |
| ----- | ------ | ----- | ------ |
| <a name="ernatvir_branching_out">Branching Out</a><br />*We must reclaim the roads as they branch out across the Dwarovar. This will surely bring settlers to our lands!* | <li>num of owned provinces with:</li><ul><li>value is at least 16</li><li>has terrain dwarven_road</li></ul> | <li>custom tooltip = ernatvir_claim_serpentreach_tooltip</li><li>hidden effect:</li><ul><li>If serpentreach region does not have core is ROOT; and does not have permanent claim is ROOT; and  has terrain is dwarven road:</li><ul><li>add permanent claim = ROOT</li></ul></ul><li>country gets the modifier ernatvir_resettlement_enthusiasm for 30 years</li> | [Rebuilding Lines](#ernatvir_rebuilding_lines)<br /> |
| <a name="ernatvir_on_the_road_again">On the Road Again</a><br />*We must claim an even larger number of roads. Many more dwarves will surely flock to our new mines!* | <li>num of owned provinces with:</li><ul><li>value is at least 25</li><li>has terrain dwarven_road</li></ul> | <li>custom tooltip = ernatvir_claim_middle_dwarovar_tooltip</li><li>hidden effect:</li><ul><li>If middle dwarovar region does not have core is ROOT; and does not have permanent claim is ROOT; and  has terrain is dwarven road:</li><ul><li>add permanent claim = ROOT</li></ul></ul><li>country gets the modifier ernatvir_transportation_boom_early for 50 years</li> | [Branching Out](#ernatvir_branching_out)<br /> |
| <a name="ernatvir_er-natvir_transcontinental">Er-Natvir Transcontinental</a><br />*We must not only retake our roads, but also develop the industry alongside it. Then we will be able to provide proper transportation across an entire continent!* | <li>num of owned provinces with:</li><ul><li>value is at least 40</li><li>has terrain dwarven_road</li><li>development is at least 10</li></ul> | <li>custom tooltip = ernatvir_claim_jade_mines_tooltip</li><li>hidden effect:</li><ul><li>If jade mines region does not have core is ROOT; and does not have permanent claim is ROOT; and  has terrain is dwarven road:</li><ul><li>add permanent claim = ROOT</li></ul></ul><li>custom tooltip = ernatvir_claim_tree_of_stone_tooltip</li><li>hidden effect:</li><ul><li>If tree of stone region does not have core is ROOT; and does not have permanent claim is ROOT; and  has terrain is dwarven road:</li><ul><li>add permanent claim = ROOT</li></ul></ul><li>country gets the modifier ernatvir_dwarovrod_reclaimers for 50 years</li> | [On the Road Again](#ernatvir_on_the_road_again)<br /> |

| Mission | Completion requirements | Effects | Prerequisites |
| ----- | ------ | ----- | ------ |
| <a name="ernatvir_rebuilding_lines">Rebuilding Lines</a><br />*Before the fall, we controlled many of the busiest dwarven roads. We must retake some of these roads to begin the path toward reclaiming our former glory.* | <li>num of owned provinces with:</li><ul><li>value is at least 8</li><li>has terrain dwarven_road</li></ul> | <li>custom tooltip = ernatvir_claim_west_dwarovar_tooltip</li><li>hidden effect:</li><ul><li>If west dwarovar region does not have core is ROOT; and does not have permanent claim is ROOT; and  has terrain is dwarven road:</li><ul><li>add permanent claim = ROOT</li></ul></ul><li>country gets the modifier ernatvir_rebuilders for 20 years</li> |  |
| <a name="ernatvir_the_dagrinrod_line">The Dagrinrod Line</a><br />*The Dagrinrod Line once ran from Dûr-Vazhatun down past Er-Natvir, connecting back to the main Dwarovrod line. It carried the latest publications from Dûr-Vazhatun to the rest of the Dwarovar. We must restore it!* | <li>custom trigger tooltip:</li><ul><li>tooltip is ernatvir_dagrinrod_line_tooltip</li><li>4104:</li><ul><li>owned by is this nation</li><li>None of the following:</li><ul><li>has province modifier dwarovar_rail</li></ul></ul><li>2876:</li><ul><li>owned by is this nation</li><li>None of the following:</li><ul><li>has province modifier dwarovar_rail</li></ul></ul><li>2988:</li><ul><li>owned by is this nation</li><li>None of the following:</li><ul><li>has province modifier dwarovar_rail</li></ul></ul><li>2989:</li><ul><li>owned by is this nation</li><li>None of the following:</li><ul><li>has province modifier dwarovar_rail</li></ul></ul><li>2990:</li><ul><li>owned by is this nation</li><li>None of the following:</li><ul><li>has province modifier dwarovar_rail</li></ul></ul><li>2991:</li><ul><li>owned by is this nation</li><li>None of the following:</li><ul><li>has province modifier dwarovar_rail</li></ul></ul><li>2992:</li><ul><li>owned by is this nation</li><li>None of the following:</li><ul><li>has province modifier dwarovar_rail</li></ul></ul><li>2993:</li><ul><li>owned by is this nation</li><li>None of the following:</li><ul><li>has province modifier dwarovar_rail</li></ul></ul><li>2994:</li><ul><li>owned by is this nation</li><li>None of the following:</li><ul><li>has province modifier dwarovar_rail</li></ul></ul><li>2996:</li><ul><li>owned by is this nation</li><li>None of the following:</li><ul><li>has province modifier dwarovar_rail</li></ul></ul><li>2997:</li><ul><li>owned by is this nation</li><li>None of the following:</li><ul><li>has province modifier dwarovar_rail</li></ul></ul><li>2998:</li><ul><li>owned by is this nation</li><li>None of the following:</li><ul><li>has province modifier dwarovar_rail</li></ul></ul><li>2999:</li><ul><li>owned by is this nation</li><li>None of the following:</li><ul><li>has province modifier dwarovar_rail</li></ul></ul><li>3000:</li><ul><li>owned by is this nation</li><li>None of the following:</li><ul><li>has province modifier dwarovar_rail</li></ul></ul><li>3001:</li><ul><li>owned by is this nation</li><li>None of the following:</li><ul><li>has province modifier dwarovar_rail</li></ul></ul><li>3002:</li><ul><li>owned by is this nation</li><li>None of the following:</li><ul><li>has province modifier dwarovar_rail</li></ul></ul><li>3003:</li><ul><li>owned by is this nation</li><li>None of the following:</li><ul><li>has province modifier dwarovar_rail</li></ul></ul></ul> | <li>country gets the modifier ernatvir_message_system until otherwise removed</li> | [Rebuilding Lines](#ernatvir_rebuilding_lines)<br /> |
| <a name="ernatvir_the_argrod_line">The Argrod Line</a><br />*The Argrod Line once spanned the entire Serpentreach, transporting many dwarves to the far reaches of Aul-Dwarov. Rebuilding it will show the world that we are truly on our way to restoring the lost rails!* | <li>custom trigger tooltip:</li><ul><li>tooltip is ernatvir_argrod_line_tooltip</li><li>2987:</li><ul><li>owned by is this nation</li><li>None of the following:</li><ul><li>has province modifier dwarovar_rail</li></ul></ul><li>2957:</li><ul><li>owned by is this nation</li><li>None of the following:</li><ul><li>has province modifier dwarovar_rail</li></ul></ul><li>2956:</li><ul><li>owned by is this nation</li><li>None of the following:</li><ul><li>has province modifier dwarovar_rail</li></ul></ul><li>2955:</li><ul><li>owned by is this nation</li><li>None of the following:</li><ul><li>has province modifier dwarovar_rail</li></ul></ul><li>2954:</li><ul><li>owned by is this nation</li><li>None of the following:</li><ul><li>has province modifier dwarovar_rail</li></ul></ul><li>2943:</li><ul><li>owned by is this nation</li><li>None of the following:</li><ul><li>has province modifier dwarovar_rail</li></ul></ul><li>2944:</li><ul><li>owned by is this nation</li><li>None of the following:</li><ul><li>has province modifier dwarovar_rail</li></ul></ul><li>2945:</li><ul><li>owned by is this nation</li><li>None of the following:</li><ul><li>has province modifier dwarovar_rail</li></ul></ul><li>2946:</li><ul><li>owned by is this nation</li><li>None of the following:</li><ul><li>has province modifier dwarovar_rail</li></ul></ul><li>2962:</li><ul><li>owned by is this nation</li><li>None of the following:</li><ul><li>has province modifier dwarovar_rail</li></ul></ul><li>4240:</li><ul><li>owned by is this nation</li><li>None of the following:</li><ul><li>has province modifier dwarovar_rail</li></ul></ul><li>2968:</li><ul><li>owned by is this nation</li><li>None of the following:</li><ul><li>has province modifier dwarovar_rail</li></ul></ul><li>2969:</li><ul><li>owned by is this nation</li><li>None of the following:</li><ul><li>has province modifier dwarovar_rail</li></ul></ul><li>2970:</li><ul><li>owned by is this nation</li><li>None of the following:</li><ul><li>has province modifier dwarovar_rail</li></ul></ul><li>2979:</li><ul><li>owned by is this nation</li><li>None of the following:</li><ul><li>has province modifier dwarovar_rail</li></ul></ul><li>2980:</li><ul><li>owned by is this nation</li><li>None of the following:</li><ul><li>has province modifier dwarovar_rail</li></ul></ul><li>2984:</li><ul><li>owned by is this nation</li><li>None of the following:</li><ul><li>has province modifier dwarovar_rail</li></ul></ul><li>2985:</li><ul><li>owned by is this nation</li><li>None of the following:</li><ul><li>has province modifier dwarovar_rail</li></ul></ul><li>4036:</li><ul><li>owned by is this nation</li><li>None of the following:</li><ul><li>has province modifier dwarovar_rail</li></ul></ul><li>4037:</li><ul><li>owned by is this nation</li><li>None of the following:</li><ul><li>has province modifier dwarovar_rail</li></ul></ul><li>4038:</li><ul><li>owned by is this nation</li><li>None of the following:</li><ul><li>has province modifier dwarovar_rail</li></ul></ul></ul> | <li>country gets the modifier ernatvir_passenger_line until otherwise removed</li> | [The Dagrinrod Line](#ernatvir_the_dagrinrod_line)<br /> |
| <a name="ernatvir_widespread_industry">Widespread Industry</a><br />*It is not enough to only build up our holds. We must restore the grand crafting halls that used to provide work for our craftsdwarves.* | <li>num of owned provinces with:</li><ul><li>value is at least 40</li><li>has terrain dwarven_road</li><li>development is at least 20</li></ul> | <li>country gets the modifier ernatvir_widespread_industry until otherwise removed</li> | [Toll Stations](#ernatvir_toll_stations)<br /> |
| <a name="ernatvir_ernatvir_intercontinental">Er-Natvir Intercontinental</a><br />*We must rise to the challenge given to us by our ancestors, and restore the rail system of the entire Dwarovar! We must make our ancestors proud!* | <li>num of owned provinces with:</li><ul><li>value is at least 110</li><li>has terrain dwarven_road</li><li>has province modifier advanced_rail</li></ul> | <li>country gets the modifier ernatvir_intercontinental until otherwise removed</li> | [Widespread Industry](#ernatvir_widespread_industry)<br />[Er-Natvir Transcontinental](#ernatvir_er-natvir_transcontinental)<br />[Widespread Recruitment](#ernatvir_widespread_recruitment)<br /> |

| Mission | Completion requirements | Effects | Prerequisites |
| ----- | ------ | ----- | ------ |
| <a name="ernatvir_secured_south_junction">Secured South Junction</a><br />*To our south lies Er-Natvir's connection to the Dwarovrod. By revitalizing that area, we can provide an economic boost in our capital.* | <li>2932:</li><ul><li>owned by is this nation</li><li>development is at least 10</li></ul><li>2934:</li><ul><li>owned by is this nation</li><li>development is at least 10</li></ul> | <li>capital scope:</li><ul><li>add base tax = 1</li><li>add base production = 1</li><li>add base manpower = 1</li><li>If area has owned by is ROOT:</li><ul><li>add province modifier:</li><ul><li>name = "growth_of_capital"</li><li>duration = 9125</li></ul></ul></ul> |  |
| <a name="ernatvir_southern_tunnels">The Southern Tunnels</a><br />*The two great tunnels to our south have fallen into disrepair. While still functional, restoring these tunnels will allow us a greater influx of supplies and settlers.* | <li>4103:</li><ul><li>owned by is this nation</li><li>development is at least 15</li></ul><li>2981:</li><ul><li>owned by is this nation</li><li>development is at least 15</li></ul><li>2884:</li><ul><li>owned by is this nation</li><li>development is at least 15</li></ul><li>2885:</li><ul><li>owned by is this nation</li><li>development is at least 15</li></ul> | <li>country gets the modifier ernatvir_reopened_tunnels for 30 years</li> | [Secured South Junction](#ernatvir_secured_south_junction)<br /> |
| <a name="ernatvir_toll_stations">Toll Stations</a><br />*While we own one of the greatest transportation networks in the world, we don't offer our services for free! We must create places where we can profit from a toll levied on goods that pass through our lands. These locations may also serve as vital strongpoints in case of war.* | <li>num of owned provinces with:</li><ul><li>value is at least 8</li><li>has terrain dwarven_road</li><li>fort level is at least 2</li></ul> | <li>If random owned province has terrain is dwarven road, and  has fort level is 2, and does not have province modifier is ernatvir toll station:</li><ul><li>add permanent province modifier:</li><ul><li>name = ernatvir_toll_station</li><li>duration = -1</li></ul></ul><li>If random owned province has terrain is dwarven road, and  has fort level is 2, and does not have province modifier is ernatvir toll station:</li><ul><li>add permanent province modifier:</li><ul><li>name = ernatvir_toll_station</li><li>duration = -1</li></ul></ul><li>If random owned province has terrain is dwarven road, and  has fort level is 2, and does not have province modifier is ernatvir toll station:</li><ul><li>add permanent province modifier:</li><ul><li>name = ernatvir_toll_station</li><li>duration = -1</li></ul></ul><li>If random owned province has terrain is dwarven road, and  has fort level is 2, and does not have province modifier is ernatvir toll station:</li><ul><li>add permanent province modifier:</li><ul><li>name = ernatvir_toll_station</li><li>duration = -1</li></ul></ul><li>If random owned province has terrain is dwarven road, and  has fort level is 2, and does not have province modifier is ernatvir toll station:</li><ul><li>add permanent province modifier:</li><ul><li>name = ernatvir_toll_station</li><li>duration = -1</li></ul></ul><li>If random owned province has terrain is dwarven road, and  has fort level is 2, and does not have province modifier is ernatvir toll station:</li><ul><li>add permanent province modifier:</li><ul><li>name = ernatvir_toll_station</li><li>duration = -1</li></ul></ul><li>If random owned province has terrain is dwarven road, and  has fort level is 2, and does not have province modifier is ernatvir toll station:</li><ul><li>add permanent province modifier:</li><ul><li>name = ernatvir_toll_station</li><li>duration = -1</li></ul></ul><li>If random owned province has terrain is dwarven road, and  has fort level is 2, and does not have province modifier is ernatvir toll station:</li><ul><li>add permanent province modifier:</li><ul><li>name = ernatvir_toll_station</li><li>duration = -1</li></ul></ul> | [The Southern Tunnels](#ernatvir_southern_tunnels)<br /> |
| <a name="ernatvir_widespread_recruitment">Widespread Recruitment</a><br />*Now that we own land across many places in the Dwarovar, we must recruit from many different locations to acquire the best deals and brightest minds.* | <li>custom trigger tooltip:</li><ul><li>tooltip is ernatvir_provinces_in_areas_tooltip</li><li>calc true if:</li><ul><li>any owned province:</li><ul><li>region is west_dwarovar_region</li><li>development is at least 60</li></ul><li>any owned province:</li><ul><li>region is middle_dwarovar_region</li><li>development is at least 60</li></ul><li>any owned province:</li><ul><li>region is serpentreach_region</li><li>development is at least 60</li></ul><li>any owned province:</li><ul><li>region is serpents_vale_region</li><li>development is at least 60</li></ul><li>any owned province:</li><ul><li>region is northern_pass_region</li><li>development is at least 60</li></ul><li>any owned province:</li><ul><li>region is tree_of_stone_region</li><li>development is at least 60</li></ul><li>any owned province:</li><ul><li>region is jade_mines_region</li><li>development is at least 60</li></ul><li>amount is at least 4</li></ul></ul> | <li>country gets the modifier ernatvir_widespread_options until otherwise removed</li> | [Toll Stations](#ernatvir_toll_stations)<br /> |