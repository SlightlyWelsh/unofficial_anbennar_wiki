This is a list of all [missions](missions.md) of [Greysheep](Greysheep.md)

| Mission | Completion requirements | Effects | Prerequisites |
| ----- | ------ | ----- | ------ |
| <a name="U13_final_wave">The Final Wave</a><br />*Our clan was the latest among the waves of exodus from the caves of our ancestral homeland. The Bahar we came to find was not the same unbreakable wall that once held our ancestors at bay with their united empires, nor the fragmented - yet powerful - force that our fellow goblin clans crashed upon to break through and conquer in their weakness.\n\nInstead the Bulwar we fight is a scattered mess of what once was, and what remains further of that. Still, glory is a thing that can be earned later. For now we are concerned in the creation of a new home for our kin.* | <li>army size is at least 10</li><li>num of generals is at least 1</li> | <li>If azka evran area does not have core is ROOT; and does not have permanent claim is ROOT:</li><ul><li>add permanent claim = ROOT</li></ul><li>658:</li><ul><li>add permanent claim = ROOT</li></ul><li>657:</li><ul><li>add permanent claim = ROOT</li></ul><li>651:</li><ul><li>add permanent claim = ROOT</li></ul> |  |
| <a name="U13_second_time">Second Times A Charm</a><br />*To say our previous encounters with the knife-eared menaces of the north of Bahar were bloody, punitive affairs is an understatement. They had long-known our kin's tactics thanks to Marblehead's invasion, which meant that they were ready for us.\n\nThough we won, we lost an unspeakable amount of numbers just for measly gains in the hills, lands we suspect they never even really cared for. Goblins, however, are capable of playing that game too, and with the knowledge we gained of their tactics and strategy, it's about time we finish what we started.* | <li>has institution feudalism</li><li>None of the following:</li><ul><li>exists is Azka-Evran</li></ul><li>azka evran area:</li><ul><li>type is all</li><li>owned by is this nation</li><li>is core is this nation</li></ul> | <li>If aqatbahar area does not have core is ROOT; and does not have permanent claim is ROOT:</li><ul><li>add permanent claim = ROOT</li></ul><li>535:</li><ul><li>add permanent claim = ROOT</li></ul><li>534:</li><ul><li>add permanent claim = ROOT</li></ul><li>541:</li><ul><li>add permanent claim = ROOT</li></ul> | [The Final Wave](#U13_final_wave)<br /> |
| <a name="U13_takeover">Take Over The Administration</a><br />*The Marblehead clan are no doubt both great conquerors and great rulers. Under their watchful gaze, they not only managed to establish a foothold into the continent, but managed also to hold onto that land they conquered.\n\nIf we are to ensure we are more than just a blip in the pages of history we need to ensure stability, and we need it fast. Developing a similar system could take decades through research, but with conquest, maybe only a few months.* | <li>is not at war</li><li>None of the following:</li><ul><li>exists is Marble Head Clan</li></ul><li>aqatbahar area:</li><ul><li>type is all</li><li>owned by is this nation</li><li>is core is this nation</li></ul><li>adm power is at least 100</li><li>treasury is at least 75</li> | <li>add adm power = -100</li><li>add treasury = -75</li><li>small increase of human tolerance effect = yes</li><li>change government reform progress = 50</li><li>If every core province is core is U15:</li><ul><li>remove core = U15</li></ul><li>set capital = 536</li> | [Second Times A Charm](#U13_second_time)<br /> |
| <a name="U13_elven_coast">The Elven Coast</a><br />*We may have a home, but what we do not have is respect. Fear is the greatest guarantor of all our desires, and there is no better way to guarantee fear than conquest.\n\nThough we have conquered and brought low the elves of Azka-Evran, they were already weak and battered by their previous run-ins with our kind. With our new might, thanks to our numbers, it is time we show the rest of these lands the power of the goblins, one shattered empire at a time.* | <li>Any of the following:</li><ul><li>has country modifier exodus_goblin_invasion</li><li>has global modifier value:</li><ul><li>which is global_manpower</li><li>value is at least 0.6</li></ul></ul><li>num of generals with traits is at least 1</li><li>army size is at least 30</li> | <li>country gets the modifier U13_coastal_invasion for 30 years</li><li>If birsartenslib area does not have core is ROOT; and does not have permanent claim is ROOT:</li><ul><li>add permanent claim = ROOT</li></ul><li>If imuluses area does not have core is ROOT; and does not have permanent claim is ROOT:</li><ul><li>add permanent claim = ROOT</li></ul><li>If kuz mountains area does not have core is ROOT; and does not have permanent claim is ROOT:</li><ul><li>add permanent claim = ROOT</li></ul> | [Take Over The Administration](#U13_takeover)<br />[Humans Of the Hills](#U13_gelkalis)<br /> |
| <a name="U13_elves_gtfo">End Elven Dominion</a><br />*The once-mighty and ever-annoying elves had it good for far too long, and nothing beats the feeling of bursting the ego of an elf. With the kingdom of the western elves downed, some of our ambitious compatriots have gone on to say that the age of the elves is coming to a close.\n\nSoon Bulwar will see a new age. One where we topple the old regimes, and cast asunder the believers of the false sun... Tell that to the humans, they just might believe it.* | <li>None of the following:</li><ul><li>exists is Birsartanses</li></ul><li>birsartenslib area:</li><ul><li>type is all</li><li>owned by is this nation</li><li>is core is this nation</li></ul><li>imuluses area:</li><ul><li>type is all</li><li>owned by is this nation</li><li>is core is this nation</li></ul><li>kuz mountains area:</li><ul><li>type is all</li><li>owned by is this nation</li><li>is core is this nation</li></ul><li>adm tech is at least 7</li><li>accepted culture is bahari</li><li>accepted culture  is sun_elf</li> | <li>add prestige = 30</li><li>change government reform progress = 75</li><li>small increase of human tolerance effect = yes</li><li>add power projection:</li><ul><li>type = mission_rewards_power_projection</li><li>amount = 15</li></ul> | [The Elven Coast](#U13_elven_coast)<br /> |

| Mission | Completion requirements | Effects | Prerequisites |
| ----- | ------ | ----- | ------ |
| <a name="U13_old_sun">Eclipse Of the Old Sun</a><br />*It's unsure just how it came about, but somehow during the upheaval of the empire of the elves and the establishment of the our new society, the humans saw it fit to prop their claims of being the true sons of Bulwar - claiming their adherence to the old ways of their sun god as proof... as if that means anything to a species born in the darkness.* | <li>owns core province 658</li><li>owns core province  657</li><li>owns core province   651</li> | <li>If bahar szel uak area does not have core is ROOT; and does not have permanent claim is ROOT:</li><ul><li>add permanent claim = ROOT</li></ul><li>the event [Old Sun Cultists Proselytise](../events/old_sun_cultists_proselytise.md) happens</li> | [The Final Wave](#U13_final_wave)<br /> |
| <a name="U13_gelkalis">Humans Of the Hills</a><br />*Who could ever believe that we would find anyone that loves sheep just as much as we do?\n\nIt turns out that our love for sheep is shared by the humans in the hills, who've existed until now as simple herders and ranchers of goats and sheep, high upon the hills that they live in. A fascinating culture like this is best kept within our jurisdiction, in fact, maybe we could trade breeding secrets!* | <li>None of the following:</li><ul><li>exists is Dartaxagerdim</li></ul><li>bahar szel uak area:</li><ul><li>type is all</li><li>owned by is this nation</li><li>is core is this nation</li></ul><li>Any of the following:</li><ul><li>None of the following:</li><ul><li>exists is Birsartanses</li></ul><li>is rival is Birsartanses</li><li>F21:</li><ul><li>None of the following:</li><ul><li>has opinion:</li><ul><li>this nation</li><li>value is at least 0</li></ul></ul></ul></ul> | <li>If has exists is F26:</li><ul><li>add casus belli:</li><ul><li>target = F26</li><li>type = cb_vassalize_mission</li><li>months = 480</li></ul></ul><li>else:</li><ul><li>If upper gelkali area does not have core is ROOT; and does not have permanent claim is ROOT:</li><ul><li>add permanent claim = ROOT</li></ul><li>If gelkalis area does not have core is ROOT; and does not have permanent claim is ROOT:</li><ul><li>add permanent claim = ROOT</li></ul></ul> | [Eclipse Of the Old Sun](#U13_old_sun)<br /> |
| <a name="U13_harpy_deal">Deal With Harpies</a><br />*The humans and their attitudes towards us is frankly unacceptable. It has been some time since our initial annexation of the Gelkali lands and they've been nothing but hostile and condescending, even erupting into fury when we suggest breeding our sheep populations together for stronger strains, the nerve!\n\nThe harpies, on the other hand, are an... interesting race that can offer more than just complaints and sheep. With their razor sharp talons and their aerial nature, they'd be an invaluable asset to our conquests. And in return we should have no issue finding lonely and willing gentlemen for their... purposes.* | <li>F27:</li><ul><li>has opinion:</li><ul><li>this nation</li><li>value is at least 10</li></ul></ul><li>upper gelkali area:</li><ul><li>type is all</li><li>country or non sovereign subject holds is this nation</li></ul><li>gelkalis area:</li><ul><li>type is all</li><li>country or non sovereign subject holds is this nation</li></ul> | <li>F27:</li><ul><li>add trust:</li><ul><li>who = ROOT</li><li>value = 10</li><li>mutual = yes</li></ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = greysheep_deal</li></ul></ul><li>medium increase of harpy tolerance effect = yes</li><li>665:</li><ul><li>add harpy minority size effect = yes</li></ul><li>capital scope:</li><ul><li>add harpy minority size effect = yes</li></ul><li>complete mission = U13_gelkali_deal</li> | [Humans Of the Hills](#U13_gelkalis)<br /> |

| Mission | Completion requirements | Effects | Prerequisites |
| ----- | ------ | ----- | ------ |
| <a name="U13_surface_world">The Surface World</a><br />*Goblins are born in the dark, raised in the dark, and die in the dark. But following our exodus we have come to inhabit the so-called 'surface' world, where walls have to be built by hand and the people worship the strange crystals that move across the endless cave ceiling. It is a strange and unfamiliar place, one that understands us just about as much as we understand it. And though it is our new home, it does not hurt to seek solace from those who know us best and are experiencing the same.* | <li>650:</li><ul><li>has merchant this nation</li></ul><li>Any of the following:</li><ul><li>U11:</li><ul><li>has opinion:</li><ul><li>this nation</li><li>value is at least 100</li></ul></ul><li>U14:</li><ul><li>has opinion:</li><ul><li>this nation</li><li>value is at least 100</li></ul></ul><li>U15:</li><ul><li>has opinion:</li><ul><li>this nation</li><li>value is at least 100</li></ul></ul></ul> | <li>add mercantilism = 3</li><li>define advisor:</li><ul><li>type = trader</li><li>skill = 1</li><li>discount = yes</li><li>culture = exodus_goblin</li></ul> |  |
| <a name="U13_sheep_grazing">Expand Sheep Grazing Lands</a><br />*Though we Graysheep goblins are lovers of sheep and all they provide for us, their needs are far more demanding than the people they are meant to clothe and feed. For one thing, they need space and lots of it!\n\nIf you want sheep to make good meat, good wool, or grow to a good size they need massive tracts of land to fuel their stomachs, land that more often than not comes from conquering new cities and turning them into new grasslands to fill the bellies of our hungry sheep, and the gods know that we are always breeding more sheep.* | <li>treasury is at least 75</li><li>if:</li><ul><li>limit:</li><ul><li>Country is Greysheep Clan</li></ul><li>U13 ideas is at least 2</li></ul><li>num of owned provinces with:</li><ul><li>value is at least 3</li><li>trade goods is wool</li><li>has production building trigger yes</li></ul> | <li>add treasury = -75</li><li>custom tooltip = sheep_grazing_greysheep_tt</li><li>hidden effect:</li><ul><li>If every owned province has trade goods is wool:</li><ul><li>add base production = 1</li><li>add province modifier:</li><ul><li>name = U13_sheep_grazing</li><li>duration = 7300</li></ul></ul></ul> | [The Surface World](#U13_surface_world)<br /> |
| <a name="U13_volt_sedovco_mission">Volt Sedovco Cavalry</a><br />*With advents in sheep breeding methods, in large part thanks to the hardy strains of the Gelkali hillfolk, as well as the new lands now allocated for grazing and ranching, we have developed a new breed of sheep that is larger, hardier, and far meaner than any the world has ever seen.\n\nDecked out in an almost metallic coat of wool thick enough to match gambeson, these sheep are tempered enough to ride into battle, acting as living bunkers that can charge into enemy lines while two goblins latch onto their sides, lances or spears in hand.* | <li>if:</li><ul><li>limit:</li><ul><li>Country is Greysheep Clan</li></ul><li>U13 ideas is at least 5</li></ul><li>mil tech is at least 8</li><li>mil power is at least 100</li><li>treasury is at least 100</li><li>num of owned provinces with:</li><ul><li>value is at least 5</li><li>trade goods is wool</li></ul> | <li>add mil power = -100</li><li>add treasury = -100</li><li>country gets the modifier U13_volt_sedovco_cavalry until otherwise removed</li> | [Expand Sheep Grazing Lands](#U13_sheep_grazing)<br />[Eclipse Of the Old Sun](#U13_old_sun)<br /> |
| <a name="U13_gelkali_deal">Deal With Humans</a><br />*Harpies are a banditrous and conniving race of monsters that claim descent from the fey of the deepwoods, and are known for their raids on their neighbors where they regularly steal men, gold, and whatever valuables they can get their razor sharp talons on. What we know of what happens to our men when they are kidnapped is limited, but awesome... for a while, afterwards they get eaten which is much less awesome.\n\nIf we are going to get ahead of this issue we need to make a deal with their quarry - the humans. Though they are a mouthy sort, humans are antagonistic in ways that are far less directly harmful to our productivity. Humans are builders and innovators, they breed almost as fast as we do, and are able to work jobs that a goblin cannot. Though they may not be immediately effective in our endeavors, the future we can potentially build with them could be worth it.* | <li>Any of the following:</li><ul><li>None of the following:</li><ul><li>exists is Harpylen</li></ul><li>F27:</li><ul><li>None of the following:</li><ul><li>has opinion:</li><ul><li>this nation</li><li>value is at least 0</li></ul></ul></ul></ul><li>upper gelkali area:</li><ul><li>type is all</li><li>country or non sovereign subject holds is this nation</li></ul><li>gelkalis area:</li><ul><li>type is all</li><li>country or non sovereign subject holds is this nation</li></ul> | <li>small increase of human tolerance effect = yes</li><li>small decrease of harpy tolerance effect = yes</li><li>decrease monstrous 3 = yes</li><li>665:</li><ul><li>add goblin minority size effect = yes</li></ul><li>capital scope:</li><ul><li>add human minority size effect = yes</li></ul><li>complete mission = U13_harpy_deal</li> | [Humans Of the Hills](#U13_gelkalis)<br /> |
| <a name="U13_highland_goblins">Highland Goblins</a><br />*Though we may have, long in our past, have been destined to be born in caves, be raised in caves, and eventually die in caves, we are no longer limited to the dimness of the caverns and find ourselves out in the open. Now entire generations are born warmed and nourished by the light of the sky-crystals, building atop the mounds that once hid our people from the outside, and exploring what the outside world has to offer before inevitably returning to the hills they were born in to be laid to rest.\n\nSome have even gone to calling ourselves a new kin, a sort of 'highland goblin' so to say. Isn't that peculiar?* | <li>manpower percentage is at least 0.75</li><li>treasury is at least 200</li><li>total development is at least 100</li><li>all owned province:</li><ul><li>None of the following:</li><ul><li>devastation is at least 1</li></ul></ul> | <li>add treasury = -200</li><li>add yearly manpower = -0.25</li><li>decrease monstrous 2 = yes</li><li>custom tooltip = highland_goblin_tt</li><li>hidden effect:</li><ul><li>If every owned province has superregion is bulwar superregion, and has terrain is mountain, and has terrain is highlands:</li><ul><li>add province modifier:</li><ul><li>name = U13_highland_goblins</li><li>duration = -1</li></ul></ul></ul> | [Deal With Humans](#U13_gelkali_deal)<br />[Deal With Harpies](#U13_harpy_deal)<br />[Settle the Newcomers](#U13_newcomers)<br /> |

| Mission | Completion requirements | Effects | Prerequisites |
| ----- | ------ | ----- | ------ |
| <a name="U13_our_new_home">Protect Our New Home</a><br />*The world has long been at odds with our people, perhaps since the moment they were born into this world, and though we have tried hard to assert ourselves as being in control of our own fate, we are surrounded at all sides by those who'd wish nothing more than to take our lands and destroy what we have worked tirelessly to build.\n\nWell if they want our lands, they will have to take them over our cold, dead hands! In the tens of thousands we were expelled from our homes by the orcs, and in the tens of thousands we will defend it to the very last.* | <li>treasury is at least 100</li><li>649:</li><ul><li>base manpower is at least 3</li></ul><li>652:</li><ul><li>base manpower is at least 3</li></ul><li>650:</li><ul><li>base manpower is at least 3</li></ul> | <li>650:</li><ul><li>add province modifier:</li><ul><li>name = U13_gorihradin_defence</li><li>duration = 12775</li></ul><li>add building construction:</li><ul><li>building = fort_15th</li><li>speed = 0.5</li><li>cost = 0.5</li></ul></ul> |  |
| <a name="U13_greysheep_style">The Greysheep Style</a><br />*The style of clothing famous in our great clan was developed when our first queen-clanboss learned of how to sew clothing from wool and taught it to the many family masters of our clan. It is distinct for its emphasis on form, with notably wealthy members of society sporting large and distinct coats that look warm but actually are expert insulators against the heat of the Bulwari sun.\n\nRecently, in part due to our successful and conquests and campaigns, goblins from other clans and even Harpies have taken interest in our unique sense of style and have sought to import our clothes and dresses, no doubt to emulate the sophistication and prestige that comes with dressing like us.* | <li>treasury is at least 75</li><li>Have an advisor of type trader</li><li>Any of the following:</li><ul><li>has ruler "Guklo"</li><li>monthly dip is at least 9</li></ul><li>num of owned provinces with:</li><ul><li>value is at least 3</li><li>trade goods is wool</li><li>has trade building trigger yes</li></ul> | <li>add treasury = -75</li><li>country gets the modifier U13_style for 20 years</li> | [Protect Our New Home](#U13_our_new_home)<br />[The Two Queens](#U13_queen_slay)<br /> |
| <a name="U13_mining">Reinvigorate Mining</a><br />*The sale of our trademark products has never been more successful. However, a successful society such as ours is fueled by gold. Our labourers do not run out of sheer obligation after all, in Greysheep all men are guaranteed their rightful pay. A large chunk of our expenditures come in the form of the import of metals and valuable tools thanks to our shortage of the fruits of the underground; iron, gold, and other such metals.\n\nTo even admit that we are in shortage of these goods is beyond ridiculous! We are goblins, born in the dark and nestled on a teat of stone and iron. Whether the mine be shallow or deep, we are still men of the stone and masters of the earth! We must never allow ourselves to forget that.* | <li>num of owned provinces with:</li><ul><li>value is at least 4</li><li>Any of the following:</li><ul><li>trade goods is iron</li><li>trade goods  is copper</li></ul><li>has production building trigger yes</li><li>has tax building trigger yes</li><li>num of times improved is at least 5</li></ul><li>Any of the following:</li><ul><li>treasury is at least 100</li><li>has country modifier U13_style</li></ul> | <li>add mercantilism = 3</li><li>country gets the modifier U13_mining_expansion for 20 years</li> | [The Greysheep Style](#U13_greysheep_style)<br /> |
| <a name="U13_newcomers">Settle the Newcomers</a><br />*Word has no doubt come around to our brothers in the depths of our successes in the surface, and faced with the option to either stay and die or seek opportunities elsewhere, thousands and more goblins have emerged from the Serpentspine to make a new home for themselves in our great society.\n\nWhat would we be if not great hypocrites if we did not accept this new wave of migrants, this new exodus of our kind? Thankfully we won't have to, we have more than enough freshly-taken land to go around after all.* | <li>Any of the following:</li><ul><li>any known country:</li><ul><li>capital scope:</li><ul><li>region is serpentreach_region</li></ul><li>Any of the following:</li><ul><li>culture group is goblin</li><li>has country modifier racial_pop_goblin_purge</li><li>has country modifier  racial_pop_goblin_expulsion</li></ul></ul><li>any owned province:</li><ul><li>region is serpentreach_region</li></ul></ul><li>if:</li><ul><li>limit:</li><ul><li>Country is Greysheep Clan</li></ul><li>U13 ideas is at least 3</li></ul><li>adm power is at least 75</li><li>dip power is at least 75</li> | <li>add adm power = -75</li><li>add dip power = -75</li><li>custom tooltip = newcomer_settlement_tt</li><li>hidden effect:</li><ul><li>If every owned province has trade goods is iron, and has trade goods is copper, and has trade goods is wool:</li><ul><li>add base production = 1</li><li>add goblin minority size effect = yes</li></ul></ul> | [Reinvigorate Mining](#U13_mining)<br /> |

| Mission | Completion requirements | Effects | Prerequisites |
| ----- | ------ | ----- | ------ |
| <a name="U13_queen_slay">The Two Queens</a><br />*The first true ruler of the Greysheep clan was a queen not unlike those in the harpy queendoms, this was by design. She was a domineering woman, but though she was as harsh as the harpies to her enemies, she was fair and beloved to her people, and she built a legacy that would far outlast her, and potentially even the harpies that she once modeled herself after.\n\nToday we must deal with queens again, those of the harpies and what role they play in our new society. Do we have space for more than one queen?* | <li>is female</li><li>Any of the following:</li><ul><li>alliance with is Harpylen</li><li>is rival is Harpylen</li><li>F27:</li><ul><li>is rival is this nation</li></ul><li>None of the following:</li><ul><li>exists is Harpylen</li></ul></ul> | <li>If has alliance with is F27:</li><ul><li>650:</li><ul><li>add trade modifier:</li><ul><li>who = ROOT</li><li>duration = 3650</li><li>power = 10</li><li>key = STRONG_MERCHANTS</li></ul></ul><li>F27:</li><ul><li>add trust:</li><ul><li>who = ROOT</li><li>value = 10</li><li>mutual = yes</li></ul></ul></ul><li>else:</li><ul><li>add power projection:</li><ul><li>type = mission_rewards_power_projection</li><li>amount = 10</li></ul></ul> |  |
| <a name="U13_emulate_harpies">Feathers Are the New Fluff</a><br />*Harpies are ruthless, cruel, and vicious she-devils that are known for few things beyond that. One of the things that has been criminally overlooked however is their absolutely fabulous sense of style. Frills, feathers, and all sorts of barecloth coverings and leather bodices to tempt the observer, the only issue was always their craftsmanship, hard to sew when your hands are either wings or talons after all.\n\nBut with their style married with our quality production methods... well, in the words of a great goblin seamsmaster 'it's absolutely fabulous, dahling!'* | <li>Any of the following:</li><ul><li>F27:</li><ul><li>has opinion:</li><ul><li>this nation</li><li>value is at least 175</li></ul></ul><li>custom trigger tooltip:</li><ul><li>tooltip is harpy_trade_building_tt</li><li>any owned province:</li><ul><li>has any harpy pop trigger yes</li><li>has trade building trigger yes</li></ul></ul></ul> | <li>small increase of harpy tolerance effect = yes</li><li>custom tooltip = harpy_style_emulation_tt</li><li>hidden effect:</li><ul><li>If every owned province has trade goods is wool:</li><ul><li>add province modifier:</li><ul><li>name = U13_emulating_harpies</li><li>duration = 7300</li></ul></ul></ul> | [The Two Queens](#U13_queen_slay)<br /> |
| <a name="U13_export">Exporting Our Style</a><br />*So far it's been easy selling to the exodus goblins and cave goblin migrants our wares, but true growth doesn't come from selling to your own people and the occasional harpy. To sell to foreign markets is the dream for any aspiring business, whether it be selling propaganda, clothes, or propaganda in the form of clothes!\n\nAs we speak our seamsmasters have already begun designs for Greysheep style clothing fit for any and all occupations; Snazzlewax's Down and Under line for the hard-working miners, Murkwort's Furious Flyter's set for the boys in Escann, and Gallytrot's  Hidden and Dangerous for fellows in the forest.* | <li>num of owned provinces with:</li><ul><li>value is at least 3</li><li>trade goods is wool</li><li>base production is at least 5</li></ul><li>any owned province:</li><ul><li>trade goods is cloth</li><li>base production is at least 10</li></ul><li>any known country:</li><ul><li>culture group is goblin</li><li>has opinion:</li><ul><li>this nation</li><li>value is at least 75</li></ul></ul> | <li>add mercantilism = 3</li><li>country gets the modifier U13_trade_export for 25 years</li> | [Feathers Are the New Fluff](#U13_emulate_harpies)<br />[The Greysheep Style](#U13_greysheep_style)<br /> |
| <a name="U13_expand_market">Out-Styling the Ancients</a><br />*For far too long we've been looked down upon as warriors, statesmen, and just in general. But if there's one thing we goblins know how to do great is looking our damn best. All around the world we've been getting reports that foreign cultures and races have begun eyeing our goods with more than just a passing interest. Even the hacky elf-emulating Cannorians have begun looking towards us for inspiration, and those guys wouldn't know fashion if it was shot through their chest by a cannon!\n\nWe've already taken the initiative and have sent the commissions to the best and brightest seamsmasters and fashion innovators throughout the country to come up with a lineup fitting for the tallfolk. Once summer rolls around the world is gonna see what real fashion looks like!* | <li>custom trigger tooltip:</li><ul><li>tooltip is semi_or_non_monstrous_tt</li><li>Any of the following:</li><ul><li>has country flag [semi_monstrous](../flags/semi_monstrous.md)</li><li>has country flag  no_longer_monstrous</li><li>None of the following:</li><ul><li>has country modifier monstrous_nation</li></ul></ul></ul><li>any known country:</li><ul><li>capital scope:</li><ul><li>superregion is bulwar_superregion</li></ul><li>None of the following:</li><ul><li>has country modifier monstrous_nation</li></ul><li>has opinion:</li><ul><li>this nation</li><li>value is at least 100</li></ul></ul> | <li>decrease monstrous 5 = yes</li><li>add mercantilism = 3</li><li>add years of income = 0.5</li> | [Exporting Our Style](#U13_export)<br /> |
| <a name="U13_gobchi_fashion">Gobchi Fashion</a><br />*Snotwort and Sneedwort Gobchi are by far the most acclaimed seamsmasters of our time, a pair of twins born and raised by their father - who was the acclaimed master of his time, who was raised by his mother - the acclaimed master of her time, and her mother - who was the acclaimed master of her time, who was raised by her father who was taught how to sew by the first queen herself.\n\nWith the reveal of their most recent summer line the world has been clamoring for Gobchi more than ever, with even Anbennar electors being present during the last unveiling. The twins realized they would forever be stuck to selling to the richest of the rich if they continued with the old ways, so they devised a system of regional branches that could source materials locally from whatever region the seamsmasters under their employ were living in at the time to greatly expand their production. With the news of such successes, it's only a matter of time until their competitors do the same and all men will know what is hot and what is not.* | <li>mercantilism is at least 35</li><li>Any of the following:</li><ul><li>has institution global_trade</li><li>any owned province:</li><ul><li>province has center of trade of level is at least 3</li></ul></ul><li>num of owned provinces with:</li><ul><li>value is at least 7</li><li>Any of the following:</li><ul><li>trade goods is wool</li><li>trade goods  is cloth</li></ul><li>has manufactory trigger yes</li></ul><li>if:</li><ul><li>limit:</li><ul><li>Country is Greysheep Clan</li></ul><li>U13 ideas is at least 7</li></ul> | <li>country gets the modifier U13_fashion_is_my_passion until otherwise removed</li> | [Out-Styling the Ancients](#U13_expand_market)<br />[Settle the Newcomers](#U13_newcomers)<br /> |