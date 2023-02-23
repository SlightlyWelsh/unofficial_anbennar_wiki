This is a list of all [missions](missions.md) of [CountsLeague](CountsLeague.md)

| Mission | Completion requirements | Effects | Prerequisites |
| ----- | ------ | ----- | ------ |
| <a name="CL_escanni_military_traditions">Greentide Survivors</a><br />*We survived the Greentide by fortifying and holding out in the Oldhaven, a highly defensible position from which our allies and us could rally. The fortifications still remain strong and will remain important to our survival into the future.* | <li>manpower percentage is at least 0.75</li> | <li>country gets the modifier "CL_escanni_traditions" for 25 years</li> |  |
| <a name="CL_rebuilding_our_army">Rebuilding Our Army</a><br />*It is vital that we rebuild our army if we are to survive the chaos that grips Escann. With a rebuilt army, we can begin to establish a new officer corps taught by our Greentide veterans.* | <li>army size is at least 20</li> | <li>country gets the modifier "army_enthusiasm" for 25 years</li> | [Greentide Survivors](#CL_escanni_military_traditions)<br /> |
| <a name="CL_gate_to_the_south">Gate to the South</a><br />*The Southgate is an important stronghold to control passage into the former Kingdom of Castellyr. If we are to rebuild it, we must control this area.* | <li>southgate area:</li><ul><li>type is all</li><li>country or non sovereign subject holds is this nation</li></ul> | <li>country gets the modifier counts_league_colonial_enthusiasm for 5 years</li><li>If nortmere area does not have core is ROOT; and does not have owned by is ROOT:</li><ul><li>add permanent claim = ROOT</li></ul> | [Retaking The Nath](#CL_retaking_the_nath)<br /> |
| <a name="CL_equipping_our_army">Equipping Our Army</a><br />*The opening of new iron mines is vital to any growing army. We have discovered new, largely untapped sources of iron and can put it to good use.* | <li>num of provinces in states is at least 3</li><li>iron is at least 1</li> | <li>add years of income = -0.5</li><li>If random owned province has trade goods is iron:</li><ul><li>add base production = 3</li><li>add permanent province modifier:</li><ul><li>name = adv_big_forge</li><li>duration = 18250</li></ul></ul> |  |

| Mission | Completion requirements | Effects | Prerequisites |
| ----- | ------ | ----- | ------ |
| <a name="CL_retaking_the_nath">Retaking The Nath</a><br />*The Nath is a large river that runs through Castonath itself, providing the city with much of its water as well as a riverine trade route connecting it to the western and eastern lands of Castellyr.* | <li>upper nath area:</li><ul><li>type is all</li><li>country or non sovereign subject holds is this nation</li></ul> | <li>country gets the modifier counts_league_colonial_enthusiasm for 5 years</li><li>If castonath area does not have core is ROOT; and does not have owned by is ROOT:</li><ul><li>add permanent claim = ROOT</li></ul><li>If southgate area does not have core is ROOT; and does not have owned by is ROOT:</li><ul><li>add permanent claim = ROOT</li></ul> | [Reclamation](#CL_reclamation)<br /> |
| <a name="CL_city_of_castan">City of Castan</a><br />*Castonath was once the greatest city of all Cannor. While this time had since passed by the Greentide, it is still vital to reclaiming our legacy to hold this most ancient of cities. * | <li>castonath area:</li><ul><li>type is all</li><li>country or non sovereign subject holds is this nation</li></ul> | <li>country gets the modifier counts_league_colonial_enthusiasm for 5 years</li><li>If trialmount area does not have core is ROOT; and does not have owned by is ROOT:</li><ul><li>add permanent claim = ROOT</li></ul> | [Retaking The Nath](#CL_retaking_the_nath)<br /> |
| <a name="CL_feeding_our_people">Feeding Our People</a><br />*We are a country of embattled survivors, yes, but even we cannot fight off starvation. The creation of new farmlands will help us feed our people and attract more refugees to our lands.* | <li>num of provinces in states is at least 5</li><li>grain is at least 3</li> | <li>add years of income = -0.5</li><li>If random owned province has trade goods is grain:</li><ul><li>add base manpower = 1</li><li>add base production = 2</li><li>add permanent province modifier:</li><ul><li>name = adv_grain_production</li><li>duration = 18250</li></ul></ul><li>If random owned province has trade goods is grain:</li><ul><li>add base manpower = 1</li><li>add base production = 2</li><li>add permanent province modifier:</li><ul><li>name = adv_grain_production</li><li>duration = 18250</li></ul></ul><li>If random owned province has trade goods is grain:</li><ul><li>add base manpower = 1</li><li>add base production = 2</li><li>add permanent province modifier:</li><ul><li>name = adv_grain_production</li><li>duration = 18250</li></ul></ul> |  |

| Mission | Completion requirements | Effects | Prerequisites |
| ----- | ------ | ----- | ------ |
| <a name="CL_reclamation">Reclamation</a><br />*We are the last remnant of the Kingdom of Castellyr, saved by the wise leadership of Carleon Blacktower and the sheer defensibility of his holdings. As such, we are the natural birthplace of the new Castellyr. We must, and shall, reclaim all that has been lost.* | <li>stability is at least 1</li><li>oldhaven area:</li><ul><li>type is all</li><li>country or non sovereign subject holds is this nation</li></ul> | <li>country gets the modifier counts_league_colonial_enthusiasm for 5 years</li><li>If upper nath area does not have core is ROOT; and does not have owned by is ROOT:</li><ul><li>add permanent claim = ROOT</li></ul><li>If ardent glade area does not have core is ROOT; and does not have owned by is ROOT:</li><ul><li>add permanent claim = ROOT</li></ul><li>If sarwood area does not have core is ROOT; and does not have owned by is ROOT:</li><ul><li>add permanent claim = ROOT</li></ul> |  |
| <a name="CL_ardent_glade">The Ardent Glade</a><br />*While the Oldhaven is an excellent defensive region, it isn't well-suited for growth or trade. The Ardent Glade is much better placed; more fertile and with its local capital, the Ardent Keep, placed upon the Nath river allowing for easy access to the river trade.* | <li>ardent glade area:</li><ul><li>type is all</li><li>country or non sovereign subject holds is this nation</li></ul> | <li>country gets the modifier counts_league_colonial_enthusiasm for 5 years</li><li>If coalwoud area does not have core is ROOT; and does not have owned by is ROOT:</li><ul><li>add permanent claim = ROOT</li></ul> | [Reclamation](#CL_reclamation)<br /> |
| <a name="CL_coalwoud">Forts of Coalwoud</a><br />*The Coalwoud is one of the region most securely held by the orcish invaders. It gives them a position to directly threaten the city of Castonath and so, to defend our holdings both current and future, we must take it for ourselves.* | <li>coalwoud area:</li><ul><li>type is all</li><li>country or non sovereign subject holds is this nation</li></ul> | <li>country gets the modifier counts_league_colonial_enthusiasm for 5 years</li><li>If serpentsmarck area does not have core is ROOT; and does not have owned by is ROOT:</li><ul><li>add permanent claim = ROOT</li></ul> | [The Ardent Glade](#CL_ardent_glade)<br /> |
| <a name="CL_ardent_capital">A New Capital</a><br />*With our control of the Ardent Keep, we can establish it as a temporary capital pending the reclaimation of the North Citadel. It would be best for us to move our artisans and merchants into this keep. where they would be much better placed to sell their goods.* | <li>owns core province 865</li> | <li>add dip power = -150</li><li>865:</li><ul><li>move capital effect = yes</li><li>add province modifier:</li><ul><li>name = adv_administration</li><li>duration = 18250</li></ul></ul><li>If does not have trade goods is gold, and does not have trade goods is gems, and does not have trade goods is mithril, and does not have trade goods is damestear:</li><ul><li>random list:</li><ul><li>40:</li><ul><li>865:</li><ul><li>change trade goods = cloth</li></ul></ul><li>30:</li><ul><li>865:</li><ul><li>change trade goods = glass</li></ul></ul><li>30:</li><ul><li>865:</li><ul><li>change trade goods = paper</li></ul></ul></ul></ul> |  |
| <a name="CL_developing_the_glade">Developing the Glade</a><br />*With our new interim capital, the Ardent Glade is now the most appealing region for the refugees flocking to us. It would be best to resettle as many of them as we can here, increasing the region's utility while also firmly establishing the Glade as our territory.* | <li>ardent glade area:</li><ul><li>type is all</li><li>country or non sovereign subject holds is this nation</li></ul><li>865:</li><ul><li>development is at least 18</li></ul> | <li>865:</li><ul><li>add base tax = 2</li><li>add base manpower = 2</li><li>add base production = 2</li><li>change culture = castellyrian</li><li>change religion = ROOT</li></ul><li>864:</li><ul><li>add base tax = 2</li><li>add base manpower = 2</li><li>add base production = 2</li><li>change culture = castellyrian</li><li>change religion = ROOT</li></ul><li>869:</li><ul><li>add base tax = 2</li><li>add base manpower = 2</li><li>add base production = 2</li><li>change culture = castellyrian</li><li>change religion = ROOT</li></ul> | [A New Capital](#CL_ardent_capital)<br /> |

| Mission | Completion requirements | Effects | Prerequisites |
| ----- | ------ | ----- | ------ |
| <a name="CL_into_the_woods">Into the Woods</a><br />*The Sarwood is directly to our east and full of orcs. If we are to survive this chaos, we need to conquer this region, or else we ourselves will be the conquered.* | <li>sarwood area:</li><ul><li>type is all</li><li>country or non sovereign subject holds is this nation</li></ul> | <li>country gets the modifier counts_league_colonial_enthusiasm for 5 years</li><li>If clouded wood area does not have core is ROOT; and does not have owned by is ROOT:</li><ul><li>add permanent claim = ROOT</li></ul><li>If nortessord area does not have core is ROOT; and does not have owned by is ROOT:</li><ul><li>add permanent claim = ROOT</li></ul> | [Reclamation](#CL_reclamation)<br /> |
| <a name="CL_highland_forests">Highland Forests</a><br />*The Sarwood is ours but yet more forest remains under orcish rule. While not as pressing, it would still be best to take the Clouded Woods for ourselves.* | <li>clouded wood area:</li><ul><li>type is all</li><li>country or non sovereign subject holds is this nation</li></ul> | <li>country gets the modifier counts_league_colonial_enthusiasm for 5 years</li><li>If steelhyl area does not have core is ROOT; and does not have owned by is ROOT:</li><ul><li>add permanent claim = ROOT</li></ul> | [Into the Woods](#CL_into_the_woods)<br /> |
| <a name="CL_putting_invaders_to_work">Putting Orcs to Work</a><br />*With the invading orcs defeated, it is best that we put them to work rebuilding the land they destroyed. Some may call it slavery, and they may be right, but we call it restitution and justice.* | <li>num of provinces in states is at least 3</li><li>slaves is at least 1</li> | <li>add years of income = -0.5</li><li>If random owned province has trade goods is slaves:</li><ul><li>add base tax = 3</li></ul> |  |

| Mission | Completion requirements | Effects | Prerequisites |
| ----- | ------ | ----- | ------ |
| <a name="CL_negotiating_with_adventurers">Treating with Adventurers</a><br />*Many of the adventurer bands who fought alongside us against the orcs remain in our territory. While some work to protect refugees, for which we thank them, all seem distinctly uninterested in ceding our land back to us. Nevertheless, despite this insult, we remain in need of allies and they are our best bet.* | <li>any ally:</li><ul><li>has reform adventurer_reform</li></ul> | <li>If random ally has reform is adventurer reform:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = opinion_adv_ally</li><li>years = 75</li></ul><li>reverse add opinion:</li><ul><li>who = ROOT</li><li>modifier = opinion_adv_ally</li><li>years = 75</li></ul></ul> |  |
| <a name="CL_fighting_orcs">Fighting the Orcs</a><br />*Yet again, we fight the green invaders. We have much experience in this and it can be expected that every one of our soldiers will give this fight everything they have. We shall not falter.* | <li>is in war:</li><ul><li>casus belli is cb_civ_vs_monster</li></ul> | <li>country gets the modifier adv_war_ork_modifier for 25 years</li> |  |
| <a name="CL_eastern_hills">Eastern Hills</a><br />*To our east lays the Nortessord hills, including the gold mines of Gulenhyl. Currently, this land is under occupation by the orcs. For the sake of justice and economic growth, we must take this land for ourselves.* | <li>nortessord area:</li><ul><li>type is all</li><li>country or non sovereign subject holds is this nation</li></ul> | <li>country gets the modifier counts_league_colonial_enthusiasm for 5 years</li><li>If esshyl area does not have core is ROOT; and does not have owned by is ROOT:</li><ul><li>add permanent claim = ROOT</li></ul> | [Into the Woods](#CL_into_the_woods)<br /> |
| <a name="CL_riches_of_escann">Riches of Escann</a><br />*We have gained control over a gold mine and begun operations. This will surely be of great benefit to our economy and a small gold rush has already begun among our people.* | <li>num of provinces in states is at least 3</li><li>gold is at least 1</li> | <li>add years of income = -0.5</li><li>If random owned province has trade goods is gold:</li><ul><li>add base tax = 2</li><li>add base production = 2</li><li>add permanent province modifier:</li><ul><li>name = adv_bank</li><li>duration = 18250</li></ul></ul> |  |