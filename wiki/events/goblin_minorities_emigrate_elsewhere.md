#Information
 - Title: Goblin Minorities Emigrate Elsewhere
 - ID: racial_pop_events_goblin.7
#Description
Goblin Minorities Emigrate Elsewhere
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Good luck in [racial_pop_migration_country.GetName]!

###Available if:


###AI weighting:
AI weights this option at 50
 - Multiplied by 1.5 if has wants to increase tolerance goblin is yes
 - Multiplied by 2 if does not have stability is 1
 - Multiplied by 1.5 if is at war
 - Multiplied by 3 if has country modifier is racial pop goblin expulsion


###Efects:<ul><li>event target:racial pop province origin:</li><ul><li>remove goblin minority size effect = yes</li></ul><li>event target:racial pop migration country:</li><ul><li>the event [Goblin Migrants From [From.GetName]](../events/goblin_migrants_from_from_getname.md) happens</li></ul></ul>

___
##Stop them! They are subjects of [Root.GetName]!

###Available if:


###AI weighting:
AI weights this option at 50
 - Multiplied by 1.5 if has wants to decrease tolerance goblin is yes
 - Multiplied by 2 if has stability is 2
 - Multiplied by 1.5 if has high tolerance goblin race trigger is yes
 - Multiplied by 3 if has country modifier is racial pop goblin purge


###Efects:<ul><li>add dip power = -10</li><li>small decrease of goblin tolerance effect = yes</li></ul>
