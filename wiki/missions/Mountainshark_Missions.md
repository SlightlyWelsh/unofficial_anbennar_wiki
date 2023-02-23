This is a list of all [missions](missions.md) of [Mountainshark](Mountainshark.md)

| Mission | Completion requirements | Effects | Prerequisites |
| ----- | ------ | ----- | ------ |
| <a name="g_an_unexpected_journey">Unexpected Journey</a><br />*We’ve always been conquerors and raiders rather than colonizers and empire builders. But all that changed when an old friend of the Clanboss showed up and told him of the riches that we could get from expanding into the tunnels.* | <li>adm power is at least 100</li> | <li>add adm power = -100</li><li>country gets the modifier cave_goblin_hobbit_journey for 25 years</li> |  |
| <a name="g_the_plans_of_tolzheen">Tolzheen's Plans</a><br />*The great military mind of Jararar Tolzheen has formulated a plan. He intends to facilitate an enormous battle between all the different races of the Dwarovar and its valleys and in doing so prove that goblins (specifically our goblins) are the most fit to be kings under the mountain.  Now we just have to find all the races.* | <li>Any of the following:</li><ul><li>theologian is at least 2</li><li>philosopher is at least 2</li></ul><li>mil power is at least 150</li> | <li>add mil power = -150</li><li>define general:</li><ul><li>shock = 7</li><li>fire = 4</li><li>manuever = 1</li><li>siege = 3</li><li>name = "Jararar Tolzheen"</li><li>trait = war_wizard_personality</li></ul> | [Unexpected Journey](#g_an_unexpected_journey)<br /> |
| <a name="g_the_battle_of_five_armies">Battle of the Five Armies</a><br />*Dwarves, Orcs, Kobolds, Ogres, and of course Goblins have all been subjugated under our banner. General Tolzheen’s plan has nearly come to fruition. All that remains is to actually have the final battle. Five armies will gather in the Serpent’s Vale to fight, and one army will emerge victorious. Goblins will sing of this day.* | <li>any core province:</li><ul><li>culture group is orcish</li></ul><li>any core province:</li><ul><li>culture group is goblin</li></ul><li>any core province:</li><ul><li>culture group is dwarven</li></ul><li>any core province:</li><ul><li>culture group is ogre</li></ul><li>any core province:</li><ul><li>culture group is kobold</li></ul> | <li>add prestige = 25</li><li>add splendor = 100</li><li>add treasury = 100</li> | [Tolzheen's Plans](#g_the_plans_of_tolzheen)<br /> |
| <a name="g_the_reforms_of_pether_jakzon">Pether Jakzon's Additions</a><br />*'Drums. Drums in the deep. That's what it's missing.'\n\nAs overheard by one of Pether Jakzon's subordinates one day while en route to his post. General Jakzon always did have a flair for the dramatic.* | <li>if:</li><ul><li>limit:</li><ul><li>None of the following:</li><ul><li>has dlc "Cradle of Civilization"</li></ul></ul><li>artist is at least 3</li><li>prestige is at least 100</li></ul><li>else:</li><ul><li>artist is at least 4</li></ul> | <li>country gets the modifier cave_goblin_peter_jackson for 25 years</li><li>define general:</li><ul><li>shock = 3</li><li>fire = 3</li><li>manuever = 8</li><li>siege = 1</li><li>name = "Pether Jakzon"</li><li>trait = glory_seeker_personality</li></ul> | [Battle of the Five Armies](#g_the_battle_of_five_armies)<br /> |
| <a name="g_goblins_of_the_mithril_mountains">The Mithril Mountains</a><br />*We have bested all those around us, and our enemies have shattered against our mighty armies. It has become common among our people to refer to this part of the Serpentspine as the Mithril Mountains after the fine metal that we mine in our capital. Truly our people can now call themselves the Divlklan, Free Clan.* | <li>calc true if:</li><ul><li>all known country:</li><ul><li>truce with is FROM</li></ul><li>amount is at least 6</li></ul> | <li>country gets the modifier cave_goblin_mountainshark until otherwise removed</li><li>override country name = DIVLKLAN</li> | [Pether Jakzon's Additions](#g_the_reforms_of_pether_jakzon)<br /> |

| Mission | Completion requirements | Effects | Prerequisites |
| ----- | ------ | ----- | ------ |
| <a name="g_the_lord_of_the_guns">The Lord of the Guns</a><br />*As with all goblins, those of the Divlklan love guns. The bigger the boom the better. Well one of our advisors, Gazdalk the White, has come up some clever ways to enhance that boom with some good old-fashioned magic. Originally something he thought up to amuse goblin children during festivals, he later realized its military uses when two young goblin lads found his stash at a party and set off the biggest one they could find, resulting in a catastrophic display.* | <li>mil tech is at least 14</li> | <li>define advisor:</li><ul><li>type = court_mage</li><li>name = "Gazdalk the Gray"</li><li>skill = 1</li><li>culture = cave_goblin</li><li>religion = goblinic_shamanism</li><li>discount = yes</li></ul> | [The Mithril Mountains](#g_goblins_of_the_mithril_mountains)<br /> |
| <a name="g_the_fellowship_of_the_gun">Fellowship of the Gun</a><br />*Our generals have come together for the council of Ezrolnd, a semi-regular meeting of our greatest military and magical minds. They are discussing ways to improve upon the magical enhancements of Gazdalk and ideally how to scale them down to use with our infantry’s firearms.* | <li>has leader with:</li><ul><li>fire is at least 5</li><li>shock is at least 0</li><li>manuever is at least 0</li><li>siege is at least 0</li></ul> | <li>country gets the modifier cave_goblin_fellowship_of_the_gun for 20 years</li> | [The Lord of the Guns](#g_the_lord_of_the_guns)<br /> |
| <a name="g_gazdalk_the_white">Gazdalk the White</a><br />*After many years of studying and researching, Gazdalk the White has decided that the best way to improve upon his formulas is to test them in the field. For that purpose, he has been given command of an army to do with as he pleases.* | <li>Any of the following:</li><ul><li>court mage is at least 5</li><li>All of the following:</li><ul><li>court mage is at least 3</li><li>estate influence:</li><ul><li>estate is estate_mages</li><li>influence is at least 40</li></ul></ul></ul> | <li>define general:</li><ul><li>shock = 8</li><li>fire = 2</li><li>manuever = 4</li><li>siege = 2</li><li>name = "Gazdalk the White"</li><li>trait = war_wizard_personality</li></ul> | [Fellowship of the Gun](#g_the_fellowship_of_the_gun)<br /> |
| <a name="g_the_return_of_the_clanboss">The Return of the Clanboss</a><br />*With a fine company of advisors behind him and strong generals leading the way, the true king has emerged, Arzorn Mountainshark. Hiding for many years under the guise of Arzorn the Strider, he has served in our armies and advised our rulers. But now it is time for him to take his rightful place as heir to the throne.* | <li>government is monarchy</li><li>if:</li><ul><li>limit:</li><ul><li>has dlc "Cradle of Civilization"</li></ul><li>philosopher is at least 5</li><li>statesman is at least 5</li><li>army organiser is at least 5</li></ul><li>else:</li><ul><li>philosopher is at least 3</li><li>statesman is at least 3</li><li>army organiser is at least 3</li></ul> | <li>add adm power = 100</li><li>add mil power = 100</li><li>add dip power = 100</li><li>define ruler:</li><ul><li>name = "Arzorn"</li><li>dynasty = "Mountainshark"</li><li>adm = 6</li><li>dip = 6</li><li>mil = 6</li><li>age = 24</li><li>claim = 100</li></ul> | [Gazdalk the White](#g_gazdalk_the_white)<br /> |