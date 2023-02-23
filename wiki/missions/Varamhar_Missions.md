This is a list of all [missions](missions.md) of [Varamhar](Varamhar.md)

| Mission | Completion requirements | Effects | Prerequisites |
| ----- | ------ | ----- | ------ |
| <a name="varamhar_winged_victory">Winged Victory</a><br />*The harpies have terrorized our people as long as we can remember. But in recent years they waged wars on our neighbours to spread their realm. If we want our country to prosper and trade to flourish we need to put a stop to their expansion. These foul beasts only understand violence. So we will raise the banner of war and drive them out.* | <li>army size is Harpylen</li> | <li>If frenyantlen area does not have owned by is ROOT, and does not have core is ROOT:</li><ul><li>add permanent claim = ROOT</li></ul><li>If harpylen area does not have owned by is ROOT, and does not have core is ROOT:</li><ul><li>add permanent claim = ROOT</li></ul><li>If invaders pass area does not have owned by is ROOT, and does not have core is ROOT:</li><ul><li>add permanent claim = ROOT</li></ul> |  |
| <a name="varamhar_a_secure_northern_flank">A Secure Northern Flank</a><br />*We drove off the Harpies and embattled the territory so they’ll never be able to return. Finally we can focus on things that actually deserve our attention.* | <li>667:</li><ul><li>country or non sovereign subject holds is this nation</li></ul><li>666:</li><ul><li>country or non sovereign subject holds is this nation</li><li>fort level is at least 2</li></ul> | <li>add stability or adm power = yes</li><li>If bulwar area does not have owned by is ROOT, and does not have core is ROOT:</li><ul><li>add permanent claim = ROOT</li></ul> | [Winged Victory](#varamhar_winged_victory)<br /> |
| <a name="varamhar_protector_of_bulwar">Protector of Bulwar</a><br />*Bulwar is the heart of these lands and only if you control it you’ll be able to spread your influence. With Bulwar as a centre of operation we can start campaigns along the Suran and Buranun rivers, the veins to this heart.* | <li>601:</li><ul><li>country or non sovereign subject holds is this nation</li></ul> | <li>If south naza area does not have owned by is ROOT, and does not have core is ROOT:</li><ul><li>add permanent claim = ROOT</li></ul><li>If east naza area does not have owned by is ROOT, and does not have core is ROOT:</li><ul><li>add permanent claim = ROOT</li></ul><li>If avamezan area does not have owned by is ROOT, and does not have core is ROOT:</li><ul><li>add permanent claim = ROOT</li></ul><li>If sareyand area does not have owned by is ROOT, and does not have core is ROOT:</li><ul><li>add permanent claim = ROOT</li></ul><li>If bulwar area does not have owned by is ROOT, and does not have core is ROOT:</li><ul><li>add permanent claim = ROOT</li></ul><li>If harklum area does not have owned by is ROOT, and does not have core is ROOT:</li><ul><li>add permanent claim = ROOT</li></ul><li>If zansap area does not have owned by is ROOT, and does not have core is ROOT:</li><ul><li>add permanent claim = ROOT</li></ul> | [A Secure Northern Flank](#varamhar_a_secure_northern_flank)<br /> |
| <a name="varamhar_control_over_the_plain">Control over the Plains</a><br />*Under our rule Bulwar prospered and greedy eyes set sight onto it and its wealthy merchants. We need to expand our borders to protect the city from our neighbours and the trade-routes from highwaymen, gnolls and what else may threaten the goods for Bulwar.* | <li>bulwar area:</li><ul><li>type is all</li><li>country or non sovereign subject holds is this nation</li></ul><li>harklum area:</li><ul><li>type is all</li><li>country or non sovereign subject holds is this nation</li></ul><li>zansap area:</li><ul><li>type is all</li><li>country or non sovereign subject holds is this nation</li></ul> | <li>If bulwar proper region does not have owned by is ROOT, and does not have core is ROOT:</li><ul><li>add permanent claim = ROOT</li></ul> | [Protector of Bulwar](#varamhar_protector_of_bulwar)<br /> |
| <a name="varamhar_the_white_phoenix_ascendant">White Phoenix Ascendant</a><br />*We now control large parts of Bulwar. With every expansion people said: “The White Phoenix seeks to become the Great Phoenix.” In the beginning it was merely a snide comment, they thought us weak. But now it’s proudly spoken by our people and with fear by our foes. We truly are ascendant and nothing will stop us.* | <li>num of owned provinces with:</li><ul><li>value is at least 50</li><li>superregion is bulwar_superregion</li></ul> | <li>country gets the modifier varamhar_the_white_phoenix_ascendant for 25 years</li> | [Control over the Plains](#varamhar_control_over_the_plain)<br />[Secure the East](#varamhar_secure_the_east)<br /> |

| Mission | Completion requirements | Effects | Prerequisites |
| ----- | ------ | ----- | ------ |
| <a name="varamhar_found_the_academy">Found the Academy</a><br />*Varamhar has always been the home to the greatest of minds of Bulwar, loathe our brethren in Sareyand and Irrliam are to admit it. However they won’t stay the greatest if we stagnate. We should give these minds space to develop. They’ll need a place to prosper and move the boundaries of our understanding of the world: The Academy* | <li>owns core province 609</li><li>adm power is at least 100</li><li>dip power is at least 100</li><li>mil power is at least 100</li><li>treasury is at least 100</li> | <li>add adm power = -100</li><li>add dip power = -100</li><li>add mil power = -100</li><li>add treasury = -100</li><li>609:</li><ul><li>add building construction:</li><ul><li>building = university</li><li>speed = 1</li><li>cost = 0</li></ul><li>add permanent province modifier:</li><ul><li>name = varamhar_the_varamhar_academy</li><li>duration = -1</li></ul></ul> |  |
| <a name="varamhar_expand_the_academy">Expand the Academy</a><br />*Our Academy is ever growing and so are its needs. Even now the first ideas and concepts promise great advances for our nation. Imagine what could be achieved if we support them.* | <li>owns core province 609</li><li>609:</li><ul><li>has building university</li><li>has building  mage_tower</li></ul> | <li>country gets the modifier varamhar_influx_of_magical_talent for 20 years</li> | [Found the Academy](#varamhar_found_the_academy)<br /> |
| <a name="varamhar_the_brightest_of_minds">The Brightest of Minds</a><br />*Over the years our Academy attracted numerous great minds. Some of them are so magnificent we need them in our government. The influence of our advisors will shape our realm for decades and with this decision we will make sure it will be into the best possible direction.* | <li>court mage is at least 3</li><li>estate loyalty:</li><ul><li>estate is estate_mages</li><li>loyalty is at least 60</li></ul> | <li>country gets the modifier varamhar_light_shed_on_issues for 20 years</li> | [Expand the Academy](#varamhar_expand_the_academy)<br /> |
| <a name="varamhar_secure_the_east">Secure the East</a><br />*The larger our project grows, the greater becomes the chance of its discovery. We need to be wary of the Monks of the Blazing Sun in Sareyand. They are zealous and too backward to understand what we are doing. They would probably use their influence in the state to urge their King to attack us and we can’t have that now. A preemptive strike would get rid of this thread and protect our great project and at the same time give us access to the sheltered fields between the mountains and Lake Naza.* | <li>south naza area:</li><ul><li>type is all</li><li>country or non sovereign subject holds is this nation</li></ul><li>east naza area:</li><ul><li>type is all</li><li>country or non sovereign subject holds is this nation</li></ul><li>north naza area:</li><ul><li>type is all</li><li>country or non sovereign subject holds is this nation</li></ul><li>Any of the following:</li><ul><li>625:</li><ul><li>country or non sovereign subject holds is this nation</li></ul><li>625:</li><ul><li>owner:</li><ul><li>None of the following:</li><ul><li>army size is this nation</li></ul></ul></ul></ul> | <li>If far bulwar region does not have owned by is ROOT, and does not have core is ROOT:</li><ul><li>add permanent claim = ROOT</li></ul> | [Protector of Bulwar](#varamhar_protector_of_bulwar)<br /> |

| Mission | Completion requirements | Effects | Prerequisites |
| ----- | ------ | ----- | ------ |
| <a name="varamhar_centralize_mage_organisation">Centralize the Magi</a><br />*We need to take control of the mages from the clerics into our own hand. Many of the priests may not understand what we want to achieve and would want to hinder our ambitions. The mages need to be free to follow our directive over any other. No priest, even one of Surael, shall take precedence over the demands of the state.* | <li>has estate privilege estate_mages_organization_state</li><li>custom trigger tooltip:</li><ul><li>tooltip is varamhar_rekindle_the_flame_happened_tt</li><li>has country flag [varamhar_rekindle_the_flame_flag](../flags/varamhar_rekindle_the_flame_flag.md)</li></ul> | <li>define advisor:</li><ul><li>type = court_mage</li><li>skill = 1</li><li>culture = sun_elf</li><li>religion = bulwari_sun_cult</li><li>discount = yes</li></ul><li>add stability = 1</li> |  |
| <a name="varamhar_initiate_project_divinity">Initiate Project Divinity</a><br />*We have gathered the resources for the most ambitious project ever attempted to our knowledge. We have the funding, now all we need is to send the invitations and the research can begin. We will initiate Project Divinity and it will be completed, no matter the cost.* | <li>adm power is at least 150</li><li>dip power is at least 150</li><li>mil power is at least 150</li><li>owns core province 609</li> | <li>add adm power = -150</li><li>add dip power = -150</li><li>add mil power = -150</li><li>the event [Project Briefing](../events/project_briefing.md) happens</li><li>custom tooltip = varamhar_estate_loyalty_tt</li> | [Centralize the Magi](#varamhar_centralize_mage_organisation)<br />[Found the Academy](#varamhar_found_the_academy)<br />[Find Relics of Power](#varamhar_find_relics_of_power)<br /> |
| <a name="varamhar_hypothesis_testing">Hypothesis Testing</a><br />*The basic research is done. Now it is time to test our hypotheses. Our mages warn that the experiments may prove difficult and dangerous, but those are mere footnotes. This work is simply too important.* | <li>ruler has mage personality is yes</li><li>adm power is at least 150</li><li>dip power is at least 150</li><li>mil power is at least 150</li><li>has country modifier varamhar_project_divinity_hypotheses_established</li><li>owns core province 609</li> | <li>add adm power = -150</li><li>add dip power = -150</li><li>add mil power = -150</li><li>the event [Animal Testing](../events/animal_testing.md) happens</li><li>custom tooltip = varamhar_estate_loyalty_tt</li> | [Initiate Project Divinity](#varamhar_initiate_project_divinity)<br />[Expand the Academy](#varamhar_expand_the_academy)<br /> |
| <a name="varamhar_refine_theories">Refine Theories</a><br />*There is no test the mages think useful that hasn’t been done. We have gathered all possible information. Now it’s time to evaluate theses and data. And to compile our research into a final theory.* | <li>adm power is at least 150</li><li>dip power is at least 150</li><li>mil power is at least 150</li><li>has country modifier varamhar_project_divinity_infusion_testing_completed</li><li>owns core province 609</li> | <li>add adm power = -150</li><li>add dip power = -150</li><li>add mil power = -150</li><li>the event [Analysing Test Results](../events/analysing_test_results.md) happens</li><li>custom tooltip = varamhar_estate_loyalty_tt</li> | [Hypothesis Testing](#varamhar_hypothesis_testing)<br />[The Brightest of Minds](#varamhar_the_brightest_of_minds)<br /> |
| <a name="varamhar_the_creation_of_a_god">The Creation of a God</a><br />*Project Divinity is almost complete, all that remains is for [Root.Monarch.GetName] to strengthen [Root.Monarch.GetHerHis] mind, for only the most strong-willed will be able to succesfully complete what has been dubbed the 'Sunmaker' procedure. With a strong mind and a strong will, we will finally be able to complete Project Divinity and achieve the creation of a god.* | <li>adm is at least 6</li><li>dip is at least 6</li><li>mil is at least 6</li><li>adm power is at least 150</li><li>dip power is at least 150</li><li>mil power is at least 150</li><li>has country modifier varamhar_project_divinity_the_compendium</li><li>owns core province 609</li> | <li>add adm power = -150</li><li>add dip power = -150</li><li>add mil power = -150</li><li>the event [A Final Test](../events/a_final_test.md) happens</li><li>custom tooltip = varamhar_estate_loyalty_tt</li> | [Refine Theories](#varamhar_refine_theories)<br />[Distill Divine Magic](#varamhar_distil_divine_magic)<br />[Secrets of the Cult](#varamhar_secrets_of_the_cult)<br /> |

| Mission | Completion requirements | Effects | Prerequisites |
| ----- | ------ | ----- | ------ |
| <a name="varamhar_find_relics_of_power">Find Relics of Power</a><br />*We have an idea, a concept, but no idea whether it is even possible? Maybe there is an answer in powerful relics of old. We need to get our hands on as many as possible, or at least as many as we need, to get proof.* | <li>Any of the following:</li><ul><li>any owned province:</li><ul><li>trade goods is precursor_relics</li></ul><li>All of the following:</li><ul><li>adm power is at least 50</li><li>dip power is at least 50</li><li>years of income is at least 1</li></ul></ul><li>custom trigger tooltip:</li><ul><li>tooltip is varamhar_rekindle_the_flame_happened_tt</li><li>has country flag [varamhar_rekindle_the_flame_flag](../flags/varamhar_rekindle_the_flame_flag.md)</li></ul> | <li>If has any owned province has trade goods is precursor relics:</li><ul><li>add adm power = 100</li><li>add dip power = 100</li></ul><li>else:</li><ul><li>add adm power = -50</li><li>add dip power = -50</li><li>the event [A Quest for Relics of Power](../events/a_quest_for_relics_of_power.md) happens</li></ul> |  |
| <a name="varamhar_elemental_energy_storage">Elemental Energy Storage</a><br />*The relics not only gave us what we were looking for but many other things too. One of the more important and with a direct application is a method to absorb and store the magical power of primal elements, including the light of the sun, and make it usable as a supplementary source of power for our magi.* | <li>natural scientist is at least 1</li><li>estate loyalty:</li><ul><li>estate is estate_mages</li><li>loyalty is at least 50</li></ul> | <li>capital scope:</li><ul><li>add permanent province modifier:</li><ul><li>name = varamhar_magical_infrastructure_development</li><li>duration = 9125</li></ul></ul><li>custom tooltip = varamhar_properly_advised_tt</li><li>hidden effect:</li><ul><li>If has natural scientist is 2:</li><ul><li>change variable:</li><ul><li>which = varamharProjectDivinityCounter</li><li>value = 1</li></ul></ul></ul> | [Find Relics of Power](#varamhar_find_relics_of_power)<br /> |
| <a name="varamhar_concentrate_light">Concentrate Light</a><br />*Project Divinity will need a lot of magical power. The storage of elemental energy we have developed is a first step, but its slow loading is a major obstacle. It may be worth looking into lens making technology from Cannor or the Dwarovar, as supposedly they are able to distort and concentrate light. This could greatly enhance the capabilities of our mages and provide just the energy we need to complete our great project.* | <li>Any of the following:</li><ul><li>any owned province:</li><ul><li>trade goods is glass</li></ul><li>any subject country:</li><ul><li>any owned province:</li><ul><li>trade goods is glass</li></ul></ul></ul><li>natural scientist is at least 2</li><li>treasury is at least 200</li> | <li>add treasury = -200</li><li>609:</li><ul><li>add permanent province modifier:</li><ul><li>name = varamhar_light_research</li><li>duration = 7300</li></ul></ul> | [Initiate Project Divinity](#varamhar_initiate_project_divinity)<br />[Elemental Energy Storage](#varamhar_elemental_energy_storage)<br /> |
| <a name="varamhar_distil_divine_magic">Distill Divine Magic</a><br />*We don’t want [Root.Monarch.GetName] to suffer the same fate as all those others that couldn’t contain the power they were granted. Through the special 'divine' flavour of magic we are able to allow them to be imbued with magic but not suffer the negative consequences. Our tests showed promise, now the [Root.Monarch.GetTitle] can finally see the results.* | <li>Any of the following:</li><ul><li>any owned province:</li><ul><li>trade goods is chinaware</li></ul><li>any subject country:</li><ul><li>any owned province:</li><ul><li>trade goods is chinaware</li></ul></ul><li>has country modifier varamhar_porcelain_stockpile</li></ul><li>adm power is at least 50</li><li>dip power is at least 50</li><li>mil power is at least 50</li> | <li>add adm power = -50</li><li>add dip power = -50</li><li>add mil power = -50</li><li>the event [Nectar](../events/nectar.md) happens</li><li>custom tooltip = varamhar_estate_loyalty_tt</li><li>hidden effect:</li><ul><li>If has estate loyalty has estate is estate church, and estate loyalty has loyalty is 50:</li><ul><li>change variable:</li><ul><li>which = varamharProjectDivinityCounter</li><li>value = 1</li></ul></ul></ul> | [Concentrate Light](#varamhar_concentrate_light)<br />[Ascend the Ranks](#varamhar_ascend_the_ranks)<br /> |
| <a name="varamhar_bottled_sunlight">Bottled Sunlight</a><br />*Further improvements in the distillation of divine magic allowed us to mass produce a potion that temporarily boosts the physical and magical capabilities of the consumer. It’s not documented if it was an accident, a joke or someone put a meaningful thought into it, however someone decided to mix it with our famous wine, which seemed to enhance the effect. Considering this we have decided to ration it out selectively to distinguished soldiers and officers to enhance their units with magical support.* | <li>owns core province 614</li><li>614:</li><ul><li>has building farm_estate</li><li>trade goods is wine</li></ul><li>mil power is at least 100</li> | <li>add mil power = -100</li><li>country gets the modifier varamhar_bottled_sunlight until otherwise removed</li> | [Distill Divine Magic](#varamhar_distil_divine_magic)<br /> |

| Mission | Completion requirements | Effects | Prerequisites |
| ----- | ------ | ----- | ------ |
| <a name="varamhar_appease_the_priests">Appease the Priests</a><br />*We have always had strenuous relations with the priesthood. However with our great ambition we will need their support, their knowledge and their secrets. So we better keep them on our side if we wish for this to end well.* | <li>estate loyalty:</li><ul><li>estate is estate_church</li><li>loyalty is at least 60</li></ul><li>custom trigger tooltip:</li><ul><li>tooltip is varamhar_rekindle_the_flame_happened_tt</li><li>has country flag [varamhar_rekindle_the_flame_flag](../flags/varamhar_rekindle_the_flame_flag.md)</li></ul> | <li>country gets the modifier varamhar_pleasedhood for 25 years</li> |  |
| <a name="varamhar_initiation">Initiation</a><br />*Over the past years we spent time and resources to appease the clergy. It was easy for [Root.Monarch.GetName] to take notice of the power of the high priests over everyone in the cult. It only seems reasonable for them to become one as well. From that position they can start to reform the cult into a shape where it would accept our ambition. And make it so that the transition to a god-king seems only natural. Beyond that, their knowledge of divine magic may be crucial in the success of our project.* | <li>theologian is at least 1</li><li>estate loyalty:</li><ul><li>estate is estate_church</li><li>loyalty is at least 40</li></ul> | <li>add ruler modifier:</li><ul><li>name = varamhar_sun_cult_acolyte</li><li>duration = -1</li></ul> | [Appease the Priests](#varamhar_appease_the_priests)<br /> |
| <a name="varamhar_ascend_the_ranks">Ascend the Ranks</a><br />*Every rank [Root.Monarch.GetName] ascends leaves them in control of more priests and gives them access to more powers of the priesthood. Soon our control over the cult will be unimpeachable and we will be able to unlock secrets no elf has previously had access to.* | <li>num of owned provinces with:</li><ul><li>value is at least 10</li><li>has tax building trigger yes</li></ul><li>dip is at least 5</li> | <li>remove country modifier = varamhar_sun_cult_acolyte</li><li>add ruler modifier:</li><ul><li>name = varamhar_magic_of_the_cult</li><li>duration = -1</li></ul><li>custom tooltip = varamhar_estate_loyalty_tt</li><li>hidden effect:</li><ul><li>If has estate loyalty has estate is estate church, and estate loyalty has loyalty is 50:</li><ul><li>change variable:</li><ul><li>which = varamharProjectDivinityCounter</li><li>value = 1</li></ul></ul></ul> | [Initiation](#varamhar_initiation)<br /> |
| <a name="varamhar_secrets_of_the_cult">Secrets of the Cult</a><br />*Now that [Root.Monarch.GetName] is the head of our clergy it’s time to inform his loyalists in the key positions about our plan so they can align their teaching with our goals and fight every subversive element in our cult. * | <li>estate loyalty:</li><ul><li>estate is estate_church</li><li>loyalty is at least 60</li></ul><li>dip is at least 6</li><li>has estate privilege estate_church_religious_state</li> | <li>remove country modifier = varamhar_magic_of_the_cult</li><li>add ruler modifier:</li><ul><li>name = varamhar_secrets_of_the_cult</li><li>duration = -1</li></ul> | [Ascend the Ranks](#varamhar_ascend_the_ranks)<br /> |
| <a name="varamhar_import_porcelain">Import Porcelain</a><br />*Small tests with Porcelain have shown that we could use porcelain to create something like a magical capacitor with our relics of power. Sadly we have no way to create any and for our project we need to acquire a large amount. We need to directly import from the source and can’t wait for the natural reaction of the trade about our demands.* | <li>treasury is at least 100</li><li>any known country:</li><ul><li>any owned province:</li><ul><li>province group is porcelain_cities</li></ul><li>has opinion:</li><ul><li>this nation</li><li>value is at least 50</li></ul></ul><li>custom trigger tooltip:</li><ul><li>tooltip is varamhar_rekindle_the_flame_happened_tt</li><li>has country flag [varamhar_rekindle_the_flame_flag](../flags/varamhar_rekindle_the_flame_flag.md)</li></ul> | <li>add treasury = -100</li><li>If random known country has any owned province has province group is porcelain cities; and  has opinion has who is ROOT, and has opinion has value is 50:</li><ul><li>the event [A Large Order of Porcelain!](../events/a_large_order_of_porcelain.md) happens</li></ul> |  |