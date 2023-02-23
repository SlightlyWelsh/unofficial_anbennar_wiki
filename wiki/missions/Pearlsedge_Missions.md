This is a list of all [missions](missions.md) of [Pearlsedge](Pearlsedge.md)

| Mission | Completion requirements | Effects | Prerequisites |
| ----- | ------ | ----- | ------ |
| <a name="A11_wine_classic">Wine, Classic</a><br />*Ah, Pearl Vintage. One of the most popular white wines, excellent with seafood of all kinds and appreciated by many for its light and dry taste. By establishing new production facilities, we can produce more of this wine - and, with its rising popularity, we will surely profit.* | <li>49:</li><ul><li>owned by is this nation</li><li>has production building trigger yes</li></ul> | <li>49:</li><ul><li>add base production = 2</li><li>add province modifier:</li><ul><li>name = "pearlywine_vintage"</li><li>duration = 7300</li></ul></ul> |  |
| <a name="A11_wine_modern">Wine, Contemporary</a><br />*With a younger but no less impressive record than its sister wine, Pearl Modern is also quite profitable. Known for its sweet, vanilla-like aroma, Pearl Modern is frequently paired with fruit and citrus based desserts. With the introduction of a new production facility, we can increase how much of this wine we provide to our thirsty customers.* | <li>41:</li><ul><li>owned by is this nation</li><li>has production building trigger yes</li></ul> | <li>41:</li><ul><li>add base production = 2</li><li>add province modifier:</li><ul><li>name = "pearlywine_modern"</li><li>duration = 7300</li></ul></ul> | [Wine, Classic](#A11_wine_classic)<br /> |
| <a name="A11_wine_perfect">Wine, Perfected</a><br />*In a bizarre event, one of our vintners forgot about one of his vineyards! While it laid forgotten, it rained quite heavily over this vineyard and his grapes were afflicted with an unfamiliar grey rot. Peculiarly, he then made wine with these grapes anyway! Even more bizarrely, this wine has been excellently received! It appears the rot dries out the grapes but leaves them otherwise intact, concentrating their sugars and producing an exquisitely sweet wine. While we will need more samples to study, this offers an excellent opportunity for us to enhance our sweet wines and perhaps even outcompete the venerable Jaherian Sunlight dessert wine. We will tell no one why these vintages are particularly sweet, of course.* | <li>Any of the following:</li><ul><li>trading bonus:</li><ul><li>trade goods is fungi</li><li>country has this</li></ul><li>fungi is at least 1</li><li>any subject country:</li><ul><li>fungi is at least 1</li></ul></ul> | <li>41:</li><ul><li>add base production = 2</li><li>add province modifier:</li><ul><li>name = "noble_wine"</li><li>duration = -1</li></ul></ul><li>49:</li><ul><li>add base production = 2</li><li>add province modifier:</li><ul><li>name = "noble_wine"</li><li>duration = -1</li></ul></ul> | [Wine, Contemporary](#A11_wine_modern)<br /> |
| <a name="A11_dominate_eordand">Dominate Eordand</a><br />*To the west, the land of Eordand is rich in artifacts from the old elven empire that the local inhabitants clearly cannot properly utilize. If we were to establish control over the trade in these artifacts, we could make quite the tidy profit selling the odder ones to enthusiastic nobles and providing the more viable designs to our own manufacturers.* | <li>1720:</li><ul><li>is strongest trade power is this nation</li></ul><li>1690:</li><ul><li>is strongest trade power is this nation</li></ul><li>1693:</li><ul><li>is strongest trade power is this nation</li></ul><li>1683:</li><ul><li>is strongest trade power is this nation</li></ul><li>1681:</li><ul><li>is strongest trade power is this nation</li></ul> | <li>country gets the modifier "pearlsedge_eordand" for 25 years</li> | [West Pearls](#A11_western_pearls)<br /> |

| Mission | Completion requirements | Effects | Prerequisites |
| ----- | ------ | ----- | ------ |
| <a name="A11_siloriel_friends">Siloriel-Trísfer Friendship</a><br />*During the Lilac Wars, we aligned with House Siloriel of the Kingdom of Lorent against our supposed sovereigns, the House of Silmuna, Grand Dukes of Dameria and Emperors of Anbennar - in truth, little more than oppressors who corrupted the Empire into little more than an extension of their Grand Duchy. With the Grand Duchy of Dameria destroyed in the Lilac Wars, we have an unprecedented opportunity for imperial influence, and it is all thanks to our 'friends' in Lorent! We must truly make sure to repay them.* | <li>Any of the following:</li><ul><li>A01:</li><ul><li>alliance with is this nation</li></ul><li>None of the following:</li><ul><li>exists is Lorent</li></ul></ul> | <li>If tretunica area does not have core is ROOT; and does not have owned by is ROOT:</li><ul><li>add permanent claim = ROOT</li></ul> |  |
| <a name="A11_fall_of_tretun">Fall of Tretun</a><br />*The Duchy of Tretun is the rightful land of Pearlsedge, by right of conquest from our founder Henrik Divenscourge, just like the rest of the supposedly once-great Tretunic Kingdom. We must bring these glorified rebels under the aegis of our duchy and end this last, sad remnant of the Tretunic people.* | <li>tretunica area:</li><ul><li>type is all</li><li>country or non sovereign subject holds is this nation</li></ul> | <li>If eastern winebay area does not have core is ROOT; and does not have owned by is ROOT:</li><ul><li>add permanent claim = ROOT</li></ul> | [Siloriel-Trísfer Friendship](#A11_siloriel_friends)<br /> |
| <a name="A11_conquest_of_roilsard">Conquest of Roilsard</a><br />*The Duchy of Roilsard is a failed state - they are truly like the thorns of their sigil, rising, falling, but always returning, something not even the Lorentish could ever get rid of. As its strongest neighbor, it is our duty to restore order and stability to its remains - and, additionally, acquire control over its profitable vineyards.* | <li>eastern winebay area:</li><ul><li>type is all</li><li>country or non sovereign subject holds is this nation</li></ul> | <li>add accepted culture = roilsardi</li><li>country gets the modifier "army_enthusiasm" for 25 years</li> | [Fall of Tretun](#A11_fall_of_tretun)<br /> |
| <a name="A11_defenders_of_the_dameshead_mission">Defenders of the Dameshead</a><br />*Since conquering this land, we have had a role in regulating what enters or exits the Dameshead. This role has become ever-more important, and ever-more difficult, with the emergence of the Aelantir to Cannor trade. If we are to continue, we must seize control of those islands in the Diven an enemy navy could use as mooring. Their current owners - the obnoxious Vernmen, weak Akani, and peculiar elven reclamationists - are foolish and undeserving of such strategically valuable islands.* | <li>navy size is at least 30</li><li>navy size percentage is at least 0.9</li> | <li>If akan isles area does not have core is ROOT; and does not have owned by is ROOT:</li><ul><li>add permanent claim = ROOT</li></ul><li>If venail area does not have core is ROOT; and does not have owned by is ROOT:</li><ul><li>add permanent claim = ROOT</li></ul><li>376:</li><ul><li>add permanent claim = ROOT</li></ul><li>51:</li><ul><li>add permanent claim = ROOT</li></ul> | [A New, Yet Old, World](#A11_a_new_world)<br /> |
| <a name="A11_western_pearls">West Pearls</a><br />*We have found an island chain to the far west well situated for control of future trade routes. We must establish a sufficient colony to control these islands, as we have heard great tales about the ancient treasures found further north and the great mineral wealth to their immediate south.* | <li>custom trigger tooltip:</li><ul><li>tooltip is pearl_west_colony</li><li>any subject country:</li><ul><li>is colonial nation of is Pearlsedge</li><li>capital scope:</li><ul><li>colonial region is colonial_haraf</li></ul><li>num of cities is at least 10</li></ul></ul> | <li>1681:</li><ul><li>add trade modifier:</li><ul><li>who = A11</li><li>duration = 5475</li><li>power = 15</li><li>key = STRONG_MERCHANTS</li></ul></ul> | [Breadbasket-to-be](#A11_new_breadbasket)<br /> |
| <a name="A11_dominate_kheionai">Dominate Kheionai</a><br />*To the south of the West Pearls, the land of Kheionai is home to its own traders who deal in such things as cocoa, coffee and sugar. They are unlikely to be much of a competitor and if we seize control of this region's trade, we could supply such goods to our colonies on the cheap and attract more settlers.* | <li>1731:</li><ul><li>is strongest trade power is this nation</li></ul><li>1741:</li><ul><li>is strongest trade power is this nation</li></ul><li>1553:</li><ul><li>is strongest trade power is this nation</li></ul> | <li>country gets the modifier "pearlsedge_kheionai" for 25 years</li> | [West Pearls](#A11_western_pearls)<br /> |

| Mission | Completion requirements | Effects | Prerequisites |
| ----- | ------ | ----- | ------ |
| <a name="A11_nation_of_traders">Nation of Traders</a><br />*We are a nation built by trade; from the beginning, Pearlsedge was born of Gerudian reavers conquering a land to settle down in and embrace trading over raiding. Since then, we have maintained a strong presence in any trade going in or out of the Dameshead, and are naturally placed to expand our trade routes even further in the future.* | <li>1270:</li><ul><li>trade share:</li><ul><li>country is Pearlsedge</li><li>share is at least 25</li></ul></ul> | <li>country gets the modifier "merchant_navy" for 25 years</li> |  |
| <a name="A11_on_the_seas">On the Seas</a><br />*We must increase our presence on the seas to take advantage of how trade routes are rapidly shifting in the aftermath of the Lilac Wars and Greentide. New facilities should be built to train more of our people in sailing and navigation, so that they can ply the new trade routes that are sure to open up.* | <li>43:</li><ul><li>owned by is this nation</li><li>has shipyard building trigger yes</li><li>has dock building trigger yes</li></ul><li>num of light ship is at least 10</li> | <li>country gets the modifier "A11_people_of_the_seas" for 25 years</li> | [Nation of Traders](#A11_nation_of_traders)<br /> |
| <a name="A11_a_new_world">A New, Yet Old, World</a><br />*While new trade routes were expected, we did not anticipate the rediscovery of the elven homeland. We must take an early lead in its exploration so we can get a proper slice of the pie, or else our rivals will claim the ancient treasures of this land instead.* | <li>has idea group exploration_ideas</li><li>exploration ideas is at least 1</li><li>colonial endralliande:</li><ul><li>has discovered this nation</li></ul> | <li>country gets the modifier "lorent_rediscovery_of_aelantir" for 25 years</li> | [On the Seas](#A11_on_the_seas)<br /> |
| <a name="A11_new_breadbasket">Breadbasket-to-be</a><br />*Far to our west is a large island akin to our own homeland, particularly the province of Erngrove, though much larger. It could provide the necessary food, timber, and other resources to fuel our future empire and so we shall claim it for ourselves.* | <li>custom trigger tooltip:</li><ul><li>tooltip is pearl_endralliande_colony</li><li>any subject country:</li><ul><li>is colonial nation of is Pearlsedge</li><li>capital scope:</li><ul><li>colonial region is colonial_endralliande</li></ul><li>num of cities is at least 10</li></ul></ul> | <li>1504:</li><ul><li>add trade modifier:</li><ul><li>who = A11</li><li>duration = 5475</li><li>power = 15</li><li>key = STRONG_MERCHANTS</li></ul></ul> | [A New, Yet Old, World](#A11_a_new_world)<br /> |
| <a name="A11_central_pearls">Central Pearls</a><br />*West of the great island we have taken to calling 'New Erngrove' lies a wide variety of lesser islands, placed perfectly between the two main continents. Any future trade will surely go through these islands and so we must make taking control of these islands our foremost goal!* | <li>custom trigger tooltip:</li><ul><li>tooltip is pearl_central_colony</li><li>any subject country:</li><ul><li>is colonial nation of is Pearlsedge</li><li>capital scope:</li><ul><li>colonial region is colonial_isles</li></ul><li>num of cities is at least 10</li></ul></ul> | <li>1527:</li><ul><li>add trade modifier:</li><ul><li>who = A11</li><li>duration = 5475</li><li>power = 15</li><li>key = STRONG_MERCHANTS</li></ul></ul> | [Breadbasket-to-be](#A11_new_breadbasket)<br /> |
| <a name="A11_dominate_the_bay">Dominate the Ruined Sea</a><br />*With control over many of its islands, we are well on the way to dominate trade in the heart of Aelantir. We must complete our local dominance and make sure our traders are favored throughout the region.* | <li>1504:</li><ul><li>is strongest trade power is this nation</li></ul><li>1527:</li><ul><li>is strongest trade power is this nation</li></ul> | <li>country gets the modifier "pearlsedge_ruined_sea" for 25 years</li> | [Central Pearls](#A11_central_pearls)<br /> |

| Mission | Completion requirements | Effects | Prerequisites |
| ----- | ------ | ----- | ------ |
| <a name="A11_pearl_white_army">Pearl White Army</a><br />*With the fall of Dameria, the Dameshead has fallen into division between petty states. Only the persistence of the Empire of Anbennar has prevented total chaos. While dangerous, this also offers a chance to reclaim those lands that are rightfully ours - of course, doing so will require a suitable army.* | <li>army size percentage is at least 1.0</li> | <li>If woodwell area does not have core is ROOT; and does not have owned by is ROOT:</li><ul><li>add permanent claim = ROOT</li></ul> |  |
| <a name="A11_claim_the_woods">Claim the Woods</a><br />*The duchy of Woodwell is the obvious first target for our expansion. It is weak and forgettable, yet offers two resources we greatly desire: lumber and an excellent staging area for future expansion.* | <li>woodwell area:</li><ul><li>type is all</li><li>country or non sovereign subject holds is this nation</li></ul> | <li>If carneteria area does not have core is ROOT; and does not have owned by is ROOT:</li><ul><li>add permanent claim = ROOT</li></ul><li>If neckcliffe area does not have core is ROOT; and does not have owned by is ROOT:</li><ul><li>add permanent claim = ROOT</li></ul> | [Pearl White Army](#A11_pearl_white_army)<br /> |
| <a name="A11_the_old_rivals">The Old Rivals</a><br />*The Trísferian dynasty, and the House of Pearlman before them, have had two notable rivals throughout our history: the kings of Carneter and the mayors of Neckcliffe. With the fall of their protector, Dameria, we can finally conquer the remnants of these enemies. We shall consign the Kingdom of Carneter to the dustbin of history where it belongs and seize the city of Neckcliffe for ourselves.* | <li>carneteria area:</li><ul><li>type is all</li><li>country or non sovereign subject holds is this nation</li></ul><li>neckcliffe area:</li><ul><li>type is all</li><li>country or non sovereign subject holds is this nation</li></ul> | <li>If windtower area does not have core is ROOT; and does not have owned by is ROOT:</li><ul><li>add permanent claim = ROOT</li></ul><li>If wesdam area does not have core is ROOT; and does not have owned by is ROOT:</li><ul><li>add permanent claim = ROOT</li></ul> | [Claim the Woods](#A11_claim_the_woods)<br /> |
| <a name="A11_wesdameric_ambitions">Wesdameric Ambitions</a><br />*Though they sided with us in the Lilac Wars, the rulers of Wesdam remain members of the House of Silmuna - particularly treacherous ones, at that. They will inevitably seek to restore Dameria and return us to subjugation! We must destroy them before they get the chance and consolidate our dominion over the Western Dameshead.* | <li>windtower area:</li><ul><li>type is all</li><li>country or non sovereign subject holds is this nation</li></ul><li>wesdam area:</li><ul><li>type is all</li><li>country or non sovereign subject holds is this nation</li></ul> | <li>country gets the modifier "A11_wesdameric_hegemony" until otherwise removed</li> | [The Old Rivals](#A11_the_old_rivals)<br /> |
| <a name="A11_southern_pearls">South Pearls</a><br />*To our south, we have found yet another group of useful islands, as well as a nearby peninsula. It seems to have had very little native population before its discovery, and so could make for an excellent colony of ours - it is also quite close to the land of Taychend, an apparently wealthy land of warring kingdoms in need of some intervention by their betters.* | <li>custom trigger tooltip:</li><ul><li>tooltip is pearl_south_colony</li><li>any subject country:</li><ul><li>is colonial nation of is Pearlsedge</li><li>capital scope:</li><ul><li>colonial region is colonial_lai_peninsula</li></ul><li>num of cities is at least 10</li></ul></ul> | <li>1607:</li><ul><li>add trade modifier:</li><ul><li>who = A11</li><li>duration = 5475</li><li>power = 15</li><li>key = STRONG_MERCHANTS</li></ul></ul> | [Breadbasket-to-be](#A11_new_breadbasket)<br /> |
| <a name="A11_dominate_taychend">Dominate Taychend</a><br />*Perhaps the most valuable territory we have yet to find, Taychend is nevertheless a primarily non-coastal land - as such, it may be better for us to focus on controlling their trade with the rest of the world and make them a captive market rather than direct intervention. Or perhaps not, and we shall indeed take them for ourselves. Either way, extending our trade network to the region can only have benefits.* | <li>1544:</li><ul><li>is strongest trade power is this nation</li></ul><li>1607:</li><ul><li>is strongest trade power is this nation</li></ul><li>1539:</li><ul><li>is strongest trade power is this nation</li></ul> | <li>country gets the modifier "pearlsedge_taychend" for 25 years</li> | [South Pearls](#A11_southern_pearls)<br /> |

| Mission | Completion requirements | Effects | Prerequisites |
| ----- | ------ | ----- | ------ |
| <a name="A11_imperial_ambitions">Imperial Ambitions</a><br />*With the fall of the House Silmuna, our position as the defenders of the Dameshead places us as the obvious choice for a truly deserving emperor. We are far less decadent than the Damerians, reliant on magic as they are, we are far more virtuous than the degenerates of Esmaria, we are far more cultured than the primitive Arannese and the adventurer-spawned Arbarani, we are not Alenic savages like the Wexonards, and we have an ability to plan for the long-term quite lacking in the Damescrowners. We are sure there are some other peoples in the Empire, but they're too irrelevant to bother remembering. With such obviously inferior competition, our ascent to imperial glory is surely inevitable.* | <li>calc true if:</li><ul><li>all elector:</li><ul><li>preferred emperor is this nation</li></ul><li>amount is at least 3</li></ul> | <li>add prestige = 10</li><li>country gets the modifier "pearlsedge_support" for 15 years</li> |  |
| <a name="A11_imperial_glory">Imperial Glory</a><br />*With many of the electors of the empire showing their intellect and now favoring our candidacy, the time has come to more aggressively court the rest. Only when we have taken the Dove Throne for ourselves, and find no challengers to our authority left standing, can we truly say we have saved the empire from its own inhabitants.* | <li>is the emperor</li><li>calc true if:</li><ul><li>all elector:</li><ul><li>preferred emperor is this nation</li></ul><li>amount is at least 5</li></ul> | <li>country gets the modifier "pearlsedge_emperor" for 15 years</li> | [Imperial Ambitions](#A11_imperial_ambitions)<br /> |
| <a name="A11_imperial_faith">Imperial Faith</a><br />*The rise of the Corinite heresy poses many problems for our authority in the Empire; many of the princes are too busy fighting each other over it to pause and recognize our superiority. We must crush this heresy without mercy - or, at least, bend it to our interests should eradication prove impossible.* | <li>is the emperor</li><li>hre is religion locked</li> | <li>If has religion is regent court:</li><ul><li>country gets the modifier pearl_adean_empire until otherwise removed</li></ul><li>Else if has religion is corinite:</li><ul><li>country gets the modifier pearl_corin_empire until otherwise removed</li></ul> | [Imperial Glory](#A11_imperial_glory)<br /> |
| <a name="A11_imperial_unity">Imperial Unity</a><br />*With the empire united under our dynasty, the time has come to push our borders further. The Kingdoms of Lorent and Gawed have existed for long enough, holding their back from the future. We must crush these barbarian kingdoms and incorporate their lands into our most enlightened empire.* | <li>is the emperor</li><li>Any of the following:</li><ul><li>hre reform passed is emperor_reichskrieg</li><li>Country is Empire of Anbennar</li></ul> | <li>country gets the modifier trisferian_empire until otherwise removed</li><li>If western cannor superregion does not have core is ROOT; and does not have owned by is ROOT:</li><ul><li>add permanent claim = ROOT</li></ul><li>If akan region does not have core is ROOT; and does not have owned by is ROOT:</li><ul><li>add permanent claim = ROOT</li></ul> | [Imperial Faith](#A11_imperial_faith)<br /> |