#Information
 - Title: Centaur Minority Migrates to Colony
 - ID: racial_pop_events_centaur.8
#Description
Centaur Minority Migrates to Colony
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


###Efects:<ul><li>event target:racial pop province origin:</li><ul><li>remove centaur minority size effect = yes</li></ul><li>event target:racial pop migration country:</li><ul><li>the event [Centaur Migrants From [From.GetName]](../events/centaur_migrants_from_from_getname.md) happens</li></ul></ul>

___
##Prevent them from leaving, they belong at home

###Available if:


###AI weighting:
AI weights this option at 30
 - Multiplied by 2 if has ruler has personality is careful personality
 - Multiplied by 3 if has country modifier is racial pop centaur purge, and has country modifier is racial pop centaur expulsion


###Efects:<ul><li>add dip power = -10</li><li>small decrease of centaur tolerance effect = yes</li></ul>
