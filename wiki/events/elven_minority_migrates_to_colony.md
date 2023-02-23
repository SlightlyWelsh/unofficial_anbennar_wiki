#Information
 - Title: Elven Minority Migrates to Colony
 - ID: racial_pop_events_elven.8
#Description
Elven Minority Migrates to Colony
#Mean Time to Happen:
Base time = 1 days

#Options

___
##[racial_pop_migration_country.GetName] could use the help!

###Available if:


###AI weighting:
AI weights this option at 50
 - Multiplied by 2 if has personality is ai colonialist
 - Multiplied by 2 if has idea group is expansion ideas


###Efects:<ul><li>event target:racial pop province origin:</li><ul><li>remove elven minority size effect = yes</li></ul><li>event target:racial pop migration country:</li><ul><li>the event [Elven Migrants From [From.GetName]](../events/elven_migrants_from_from_getname.md) happens</li></ul></ul>

___
##Prevent them from leaving, they belong at home

###Available if:


###AI weighting:
AI weights this option at 30
 - Multiplied by 2 if has ruler has personality is careful personality
 - Multiplied by 3 if has country modifier is racial pop elven purge, and has country modifier is racial pop elven expulsion


###Efects:<ul><li>add dip power = -10</li><li>small decrease of elven tolerance effect = yes</li></ul>
