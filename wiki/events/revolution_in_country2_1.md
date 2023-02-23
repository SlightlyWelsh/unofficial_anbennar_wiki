This page has the same name as others. For full listing see bottom of [the base page](revolution_in_country2.md).

#Information
 - Title: Revolution in $COUNTRY$
 - ID: republic_factions.103
#Description
Revolution in $COUNTRY$
#Mean Time to Happen:
Base time = 400 months
 - Multiplied by 0.9 if has faction influence has faction is mr aristocrats, and faction influence has influence is 90
 - Multiplied by 0.9 if has faction influence has faction is mr aristocrats, and faction influence has influence is 95
 - Multiplied by 0.9 if has faction influence has faction is mr aristocrats, and faction influence has influence is 100
 - Multiplied by 0.9 if does not have faction influence has faction is mr guilds, and faction influence has influence is 5
 - Multiplied by 0.9 if does not have faction influence has faction is mr traders, and faction influence has influence is 5
 - Multiplied by 0.95 if does not have stability is 2
 - Multiplied by 0.95 if does not have stability is 1
 - Multiplied by 0.95 if does not have stability is 0
 - Multiplied by 0.8 if does not have stability is 2
 - Multiplied by 0.9 if does not have republican tradition is 80
 - Multiplied by 0.9 if does not have republican tradition is 60
 - Multiplied by 0.9 if does not have republican tradition is 40

#Options

___
##We cannot possibly surrender to grocers!

###Efects:<ul><li>add stability = -1</li><li>add prestige = -15</li><li>add republican tradition = -20</li><li>If has num of cities is 2, and  has any owned province is not a capital, and any owned province is in capital area:</li><ul><li>If random owned province is not a capital, and  is in capital area, and  has owner has adm tech is 22:</li><ul><li>spawn rebels:</li><ul><li>type = revolutionary_rebels</li><li>size = 2</li></ul></ul><li>If random owned province is not a capital, and  is in capital area, and  does not have adm tech is 22:</li><ul><li>spawn rebels:</li><ul><li>type = anti_tax_rebels</li><li>size = 2</li></ul></ul></ul><li>If does not have num of cities is 2; and does not have any owned province is not a capital, and any owned province is in capital area; and  does not have province modifier is wrecked by factional riots:</li><ul><li>capital scope:</li><ul><li>add province modifier:</li><ul><li>name = "wrecked_by_factional_riots"</li><li>duration = 1825</li></ul></ul></ul></ul>

___
##Give in to their demands.

###Efects:<ul><li>custom tooltip = republic_factions.103.b.tt</li><li>add stability = -1</li><li>add years of income = -0.25</li><li>add republican tradition = 5</li><li>add faction influence:</li><ul><li>faction = mr_aristocrats</li><li>influence = -60</li></ul><li>set ruler flag [leader_has_been_pushed_out](../flags/leader_has_been_pushed_out.md)</li><li>the event [Election!](../events/election.md) happens</li></ul>
