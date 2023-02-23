#Information
 - Title: Gnollish Minorities Emigrate Elsewhere
 - ID: racial_pop_events_gnollish.7
#Description
Gnollish Minorities Emigrate Elsewhere
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Good luck in [racial_pop_migration_country.GetName]!

###Available if:


###AI weighting:
AI weights this option at 50
 - Multiplied by 1.5 if has wants to increase tolerance gnollish is yes
 - Multiplied by 2 if does not have stability is 1
 - Multiplied by 1.5 if is at war
 - Multiplied by 3 if has country modifier is racial pop gnollish expulsion


###Efects:<ul><li>event target:racial pop province origin:</li><ul><li>remove gnollish minority size effect = yes</li></ul><li>event target:racial pop migration country:</li><ul><li>the event [Gnollish Migrants From [From.GetName]](../events/gnollish_migrants_from_from_getname.md) happens</li></ul></ul>

___
##Stop them! They are subjects of [Root.GetName]!

###Available if:


###AI weighting:
AI weights this option at 50
 - Multiplied by 1.5 if has wants to decrease tolerance gnollish is yes
 - Multiplied by 2 if has stability is 2
 - Multiplied by 1.5 if has high tolerance gnollish race trigger is yes
 - Multiplied by 3 if has country modifier is racial pop gnollish purge


###Efects:<ul><li>add dip power = -10</li><li>small decrease of gnollish tolerance effect = yes</li></ul>
