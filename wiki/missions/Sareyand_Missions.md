This is a list of all [missions](missions.md) of [Sareyand](Sareyand.md)

| Mission | Completion requirements | Effects | Prerequisites |
| ----- | ------ | ----- | ------ |
| <a name="sareyand_0_patronage_of_the_landlords">Patronage of the Landlords</a><br />*Our lands are dotted with the massive estates of our Sun Elven brethren. It is those landlords that are the foundation of our rule and it is with their support that we can gain and maintain our greatness.* | <li>estate loyalty:</li><ul><li>estate is estate_nobles</li><li>loyalty is at least 60</li></ul> | <li>If north naza area does not have owned by is ROOT, and does not have core is ROOT:</li><ul><li>add permanent claim = ROOT</li></ul><li>country gets the modifier sareyand_cooperative_landlords for 20 years</li> |  |
| <a name="sareyand_0_sunshine_manors">Sunshine Manors</a><br />*The manors of the landlords are the motor of our economy. Their massive farm estates provide the taxes and the resources that maintain our politics, infrastructure and army. So naturally more developed estates mean more money.* | <li>development in provinces:</li><ul><li>value is at least 110</li><li>Any of the following:</li><ul><li>area is east_naza_area</li><li>area  is south_naza_area</li><li>area   is sareyand_area</li><li>area    is avamezan_area</li></ul></ul> | <li>country gets the modifier sareyand_new_manors for 25 years</li> | [Patronage of the Landlords](#sareyand_0_patronage_of_the_landlords)<br /> |
| <a name="sareyand_0_rebuild_the_ash_palace">Rebuild the Ash Palace</a><br />*Since the palace of Sareyand was burned down during Jexis' youth its husk has sat there like a great carcass, black and empty. It is time we restore this relic of Jaher's days to its former glory, and possibly even embellish it further. That will show we truly are the worthy successors of the great conqueror.* | <li>625:</li><ul><li>development is at least 40</li></ul><li>treasury is at least 500</li> | <li>add treasury = -500</li><li>625:</li><ul><li>add province triggered modifier = sareyand_the_ash_palace</li><li>add province modifier:</li><ul><li>name = sareyand_rebuilding_the_ash_palace</li><li>duration = 730</li></ul><li>tooltip:</li><ul><li>add permanent province modifier:</li><ul><li>name = sareyand_the_ash_palace_dummy</li><li>duration = -1</li></ul></ul></ul> | [Sunshine Manors](#sareyand_0_sunshine_manors)<br /> |
| <a name="sareyand_0_the_bulwark_of_the_sun">Bulwark of the Sun</a><br />*The Mountains of the Sun guard the western approach of Bulwar from the Salahad. The construction of a great fort there can be exactly the protection we need against new gnollish incursions and will safeguard our lands.* | <li>682:</li><ul><li>owned by is this nation</li><li>fort level is at least 4</li><li>base manpower is at least 5</li></ul> | <li>682:</li><ul><li>add permanent province modifier:</li><ul><li>name = sareyand_bulwark_of_the_sun</li><li>duration = -1</li></ul></ul> | [The Šad Sur](#sareyand_1_the_mountains_of_the_sun)<br /> |
| <a name="sareyand_0_the_phoenix_citadel">The Phoenix Citadel</a><br />*The Bulwark of the Sun has attracted a great deal of military interest due to its ingenuity. We should expand its construction and turn it into the largest citadel of our nation that can watch over all of the Suran plain and the Divenhal.* | <li>682:</li><ul><li>owned by is this nation</li><li>fort level is at least 6</li><li>has building training_fields</li><li>base manpower is at least 10</li></ul> | <li>682:</li><ul><li>remove province modifier = sareyand_bulwark_of_the_sun</li><li>add permanent province modifier:</li><ul><li>name = sareyand_the_phoenix_citadel</li><li>duration = -1</li></ul></ul> | [Bulwark of the Sun](#sareyand_0_the_bulwark_of_the_sun)<br /> |

| Mission | Completion requirements | Effects | Prerequisites |
| ----- | ------ | ----- | ------ |
| <a name="sareyand_1_around_lake_naza">Around Lake Naza</a><br />*The Naza estates house some of the wealthiest landlords of our nation and some of the royal family's most avid supporters. They have long looked out across the lake to potential new grounds to expand their manors into. It would mean a great deal to them and so to the nation if we were to incorporate the entire circumference of the lake into our administration.* | <li>north naza area:</li><ul><li>type is all</li><li>country or non sovereign subject holds is this nation</li></ul> | <li>country gets the modifier sareyand_food_surplus for 25 years</li> | [Patronage of the Landlords](#sareyand_0_patronage_of_the_landlords)<br /> |
| <a name="sareyand_1_the_mountains_of_the_sun">The Šad Sur</a><br />*The Mountains of the Sun have been infested with gnolls since time immemorial. It was the outpost of many gnoll raids during Jaher's time and still under his successors. Let us bring them under our rule and ensure that such a thing never happens again.* | <li>sur mountains area:</li><ul><li>type is all</li><li>country or non sovereign subject holds is this nation</li></ul><li>jixobix area:</li><ul><li>type is all</li><li>country or non sovereign subject holds is this nation</li></ul><li>garpix tluukt area:</li><ul><li>type is all</li><li>country or non sovereign subject holds is this nation</li></ul><li>grixekyr area:</li><ul><li>type is all</li><li>country or non sovereign subject holds is this nation</li></ul><li>691:</li><ul><li>country or non sovereign subject holds is this nation</li></ul> | <li>682:</li><ul><li>change religion = bulwari_sun_cult</li><li>change culture = sun_elf</li><li>add province modifier:</li><ul><li>name = sareyand_military_colony</li><li>duration = 3650</li></ul></ul><li>If zansap area does not have owned by is ROOT, and does not have core is ROOT:</li><ul><li>add claim = ROOT</li></ul><li>If bulwar area does not have owned by is ROOT, and does not have core is ROOT:</li><ul><li>add claim = ROOT</li></ul><li>604:</li><ul><li>If does not have owned by is ROOT, and does not have core is ROOT:</li><ul><li>add claim = ROOT</li></ul></ul><li>611:</li><ul><li>If does not have owned by is ROOT, and does not have core is ROOT:</li><ul><li>add claim = ROOT</li></ul></ul> | [Sun Elven Protection](#sareyand_2_sun_elven_protection)<br /> |
| <a name="sareyand_1_the_heart_of_bulwar">The Heart of Bulwar</a><br />*Bulwar is a land of city-states and a land of city-states is at its heart. Independently they have stood for centuries, only united under the greatest conquerors. We should step into the footsteps of Jaher and Jexis and unite the city-states of Bulwar under our rule.* | <li>zansap area:</li><ul><li>type is all</li><li>country or non sovereign subject holds is this nation</li></ul><li>bulwar area:</li><ul><li>type is all</li><li>country or non sovereign subject holds is this nation</li></ul><li>604:</li><ul><li>country or non sovereign subject holds is this nation</li></ul><li>611:</li><ul><li>country or non sovereign subject holds is this nation</li></ul> | <li>If medurubar area does not have owned by is ROOT, and does not have core is ROOT:</li><ul><li>add claim = ROOT</li></ul><li>If lower brasan area does not have owned by is ROOT, and does not have core is ROOT:</li><ul><li>add claim = ROOT</li></ul><li>If upper brasan area does not have owned by is ROOT, and does not have core is ROOT:</li><ul><li>add claim = ROOT</li></ul> | [The Šad Sur](#sareyand_1_the_mountains_of_the_sun)<br /> |
| <a name="sareyand_1_the_length_of_the_suran">The Length of the Suran</a><br />*The Suran is the lifeblood of Bulwar, it flows from beyond Azka-Sur to Sareyand, Bulwar and all the way down to Brasan. Obviously, its importance to region cannot be overstated. And so, we should control it, from the source all the way down to the lands where in mythical times the Djinn were first broken.* | <li>medurubar area:</li><ul><li>type is all</li><li>country or non sovereign subject holds is this nation</li></ul><li>lower brasan area:</li><ul><li>type is all</li><li>country or non sovereign subject holds is this nation</li></ul><li>upper brasan area:</li><ul><li>type is all</li><li>country or non sovereign subject holds is this nation</li></ul> | <li>country gets the modifier sareyand_control_over_the_suran for 15 years</li> | [The Heart of Bulwar](#sareyand_1_the_heart_of_bulwar)<br /> |

| Mission | Completion requirements | Effects | Prerequisites |
| ----- | ------ | ----- | ------ |
| <a name="sareyand_2_recover_the_suran_plain">Recover the Suran Plain</a><br />*Zokka was a great adversary and the monster dealt us many defeats. But his life is short while we live long and it is time for us to reclaim what we have lost so that all can be well again.* | <li>690:</li><ul><li>country or non sovereign subject holds is this nation</li></ul><li>636:</li><ul><li>country or non sovereign subject holds is this nation</li></ul><li>637:</li><ul><li>country or non sovereign subject holds is this nation</li></ul><li>641:</li><ul><li>country or non sovereign subject holds is this nation</li></ul><li>F45:</li><ul><li>exists</li><li>is subject of is this nation</li><li>owns 638</li><li>owns  639</li><li>owns   640</li></ul> | <li>country gets the modifier sareyand_slayer_of_beasts for 10 years</li> |  |
| <a name="sareyand_2_sun_elven_protection">Sun Elven Protection</a><br />*It is our role and duty to protect the world against the Malevolent Dark. And so, it is our obligation to take those weaker than us under our wing, even if they don't know that they need the protection.* | <li>calc true if:</li><ul><li>all subject country:</li><ul><li>is subject of is this nation</li><li>culture group is bulwari</li><li>None of the following:</li><ul><li>liberty desire is at least 30</li></ul><li>NOT:</li><ul><li>num of cities is at least 4</li></ul></ul><li>amount is at least 4</li></ul> | <li>country gets the modifier sareyand_protector_of_the_light for 100 years</li> | [Recover the Suran Plain](#sareyand_2_recover_the_suran_plain)<br /> |
| <a name="sareyand_2_gno_more_gnolls">Gno More Gnolls</a><br />*We have pushed Zokka's pack back, but that is not enough. We can't rest until any gnoll remains to threaten our homes. We will start by pushing them out of the deserts of Bulwar.* | <li>None of the following:</li><ul><li>far bulwar region:</li><ul><li>owner:</li><ul><li>culture group is gnollish</li></ul></ul></ul> | <li>custom tooltip = sareyand_claims_on_jaddari_tt</li><li>hidden effect:</li><ul><li>If far salahad region has owned by is F46, and has culture is desert elf:</li><ul><li>add permanent claim = ROOT</li></ul></ul> | [Sun Elven Protection](#sareyand_2_sun_elven_protection)<br /> |
| <a name="sareyand_2_the_gate_of_the_east">The Gate of the East</a><br />*Sareyand is the great eastern facing city of Bulwar and through its gates flows all the trade with Rahen. We should ensure that this trade is firmly in our grasp so that we force our will upon traders from the lands of the elephants and tigers.* | <li>638:</li><ul><li>trade share:</li><ul><li>country is this nation</li><li>share is at least 70</li></ul></ul> | <li>country gets the modifier sareyand_the_gate_of_the_east for 25 years</li> | [Gno More Gnolls](#sareyand_2_gno_more_gnolls)<br /> |
| <a name="sareyand_2_trade_with_rahen">Trade with Rahen</a><br />*The trade with Rahen is one of the most lucrative sources of income since the days of old Castanor and the Damerian Republic. Even the first gnolls in the region saw its value. Now it is our turn to take control of this trade so that we can earn the maximum profit possible.* | <li>2901:</li><ul><li>is strongest trade power is this nation</li></ul><li>1350:</li><ul><li>is strongest trade power is this nation</li></ul> | <li>country gets the modifier sareyand_the_riches_of_the_east for 25 years</li> | [The Gate of the East](#sareyand_2_the_gate_of_the_east)<br /> |

| Mission | Completion requirements | Effects | Prerequisites |
| ----- | ------ | ----- | ------ |
| <a name="sareyand_3_restore_the_akalate_of_azka_sur">Restore Azka-Sur</a><br />*Azka-Sur was once one of the major Kingdoms of Bulwar, but under repeated onslaught from gnollish attacks it lost both its land and its sun elven rulership. It is time we take responsibility and reestablish the Kingdom to its former glory. This time under better leadership.* | <li>U20:</li><ul><li>is subject of is this nation</li><li>None of the following:</li><ul><li>liberty desire is at least 30</li></ul></ul> | <li>create march = U20</li><li>U20:</li><ul><li>change primary culture = sun_elf</li><li>add accepted culture = surani</li><li>define ruler:</li><ul><li>dynasty = ROOT</li><li>culture = ROOT</li><li>religion = ROOT</li></ul><li>jikarzax area:</li><ul><li>add core = PREV</li></ul><li>grixek area:</li><ul><li>add core = PREV</li></ul></ul> | [Recover the Suran Plain](#sareyand_2_recover_the_suran_plain)<br /> |
| <a name="sareyand_3_the_true_lords_of_bulwar">True Lords of Bulwar</a><br />*Many peoples have disputed who are the lords of Bulwar. There have been human priests and kings, harpy matriarchs and gnollish warlords. But since the Landing it has been clear that elves are the true lords of this land and we will prove that time and again.* | <li>is not at war</li><li>calc true if:</li><ul><li>all subject country:</li><ul><li>is subject of is this nation</li><li>culture group is bulwari</li><li>None of the following:</li><ul><li>liberty desire is at least 1</li></ul></ul><li>amount is at least 4</li></ul> | <li>If every subject country has culture group is bulwari, and does not have liberty desire is 1:</li><ul><li>ROOT:</li><ul><li>create march = PREV</li></ul><li>change primary culture = sun_elf</li><li>define ruler:</li><ul><li>dynasty = ROOT</li><li>culture = ROOT</li><li>religion = ROOT</li></ul><li>kill heir:</li><ul></ul></ul><li>country gets the modifier sareyand_the_true_lord_of_bulwar until otherwise removed</li> | [Sun Elven Protection](#sareyand_2_sun_elven_protection)<br />[Restore Azka-Sur](#sareyand_3_restore_the_akalate_of_azka_sur)<br /> |
| <a name="sareyand_3_the_rogue_legion">The Rogue Legion</a><br />*Since their return from Haless the old phoenix legions have gone rogue and become an unbridled horde with no civilisation or structure. Now they even went astray in their faith. We must bring these warriors back to the right path so that they can be a support to the cause instead of a threat.* | <li>custom trigger tooltip:</li><ul><li>tooltip is sareyand_3_the_rogue_legion_tt</li><li>None of the following:</li><ul><li>any province:</li><ul><li>culture is desert_elf</li><li>None of the following:</li><ul><li>religion is bulwari_sun_cult</li></ul></ul></ul></ul> | <li>custom tooltip = sareyand_desert_elves_become_sun_elves_tt</li><li>hidden effect:</li><ul><li>If every province has culture is desert elf:</li><ul><li>change culture = sun_elf</li></ul></ul><li>add mil power = 100</li> | [Gno More Gnolls](#sareyand_2_gno_more_gnolls)<br /> |
| <a name="sareyand_3_the_great_ash_legion">The Great Ash Legion</a><br />*Too long have we relied on human auxiliaries and legionaries to fuel our war machine. They are good only for support. It is the elves that conquered Bulwar and Haless and so the Ash Legion must also be an elven legion at the core. We now finally have the numbers once more to make this vision a reality.* | <li>num of owned provinces with:</li><ul><li>value is at least 15</li><li>has manpower building trigger yes</li><li>culture is sun_elf</li></ul> | <li>If does not have country modifier is elven military:</li><ul><li>clear racial military = yes</li><li>country gets the modifier restructuring_military for 5 years</li><li>country gets the modifier elven_military until otherwise removed</li><li>change unit type = tech_east_elven</li></ul><li>country gets the modifier sareyand_the_great_ash_legion until otherwise removed</li> | [The Rogue Legion](#sareyand_3_the_rogue_legion)<br />[Ashes to Iron](#sareyand_4_ashes_to_iron)<br /> |

| Mission | Completion requirements | Effects | Prerequisites |
| ----- | ------ | ----- | ------ |
| <a name="sareyand_4_found_the_shining_monastery">The Shining Monastery</a><br />*The monks of the Blazing Sun have been a great support in our campaigns and in our administration. It is time we give them a home where they can practise their work. It will be a library, school and barrack for all those wishing to pursue their special art.* | <li>625:</li><ul><li>development is at least 30</li><li>renaissance is at least 100</li><li>owned by is this nation</li></ul> | <li>625:</li><ul><li>add permanent province modifier:</li><ul><li>name = sareyand_the_shining_monastery</li><li>duration = -1</li></ul></ul> |  |
| <a name="sareyand_4_build_the_blazing_temple">Build the Blazing Temple</a><br />*While the Shining Monastery serves a great purpose within our country, its residents have been talking about the need for a larger religious structure that is not just for them. We will heed their words and the Blazing Temple will arise next to their complex. This great structure shall honour Surael and surely will impress the gullible masses.* | <li>treasury is at least 400</li><li>625:</li><ul><li>has tax building trigger yes</li><li>religion is bulwari_sun_cult</li></ul> | <li>add treasury = -400</li><li>625:</li><ul><li>add building = cathedral</li><li>add province triggered modifier = sareyand_the_blazing_temple</li><li>tooltip:</li><ul><li>add permanent province modifier:</li><ul><li>name = sareyand_the_blazing_temple_dummy</li><li>duration = -1</li></ul></ul></ul> | [The Shining Monastery](#sareyand_4_found_the_shining_monastery)<br /> |
| <a name="sareyand_4_rekindle_the_ashes">Rekindle the Ashes</a><br />*Too long have our armies sat idle and failed to produce results. It is time we turn to the attack and rekindle the ashes, so that in time they may birth a new Phoenix.* | <li>is in war:</li><ul><li>attacker leader is this nation</li></ul> | <li>define general:</li><ul><li>name = "Nuzarien Szel-Orean"</li><li>fire = 2</li><li>shock = 6</li><li>manuever = 0</li><li>siege = 4</li></ul> |  |
| <a name="sareyand_4_ashes_to_iron">Ashes to Iron</a><br />*We have resumed the attack, but attacking on its own won't let us gain the heights of a Phoenix. We must harden our armies and beat them into shape. Our Ash Legion will be a blade of the strongest steel to cut down our enemies.* | <li>army tradition is at least 60</li> | <li>country gets the modifier sareyand_ash_and_iron for 20 years</li> | [Rekindle the Ashes](#sareyand_4_rekindle_the_ashes)<br /> |