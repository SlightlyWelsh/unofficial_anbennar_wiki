#Information
 - Title: Human Minorities Emigrate Elsewhere
 - ID: racial_pop_events_human.7
#Description
Human Minorities Emigrate Elsewhere
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Good luck in [racial_pop_migration_country.GetName]!

###Available if:


###AI weighting:
AI weights this option at 50
 - Multiplied by 1.5 if has wants to increase tolerance human is yes
 - Multiplied by 2 if does not have stability is 1
 - Multiplied by 1.5 if is at war
 - Multiplied by 3 if has country modifier is racial pop human expulsion


###Efects:<ul><li>event target:racial pop province origin:</li><ul><li>remove human minority size effect = yes</li></ul><li>event target:racial pop migration country:</li><ul><li>the event [Human Migrants From [From.GetName]](../events/human_migrants_from_from_getname.md) happens</li></ul></ul>

___
##Stop them! They are subjects of [Root.GetName]!

###Available if:


###AI weighting:
AI weights this option at 50
 - Multiplied by 1.5 if has wants to decrease tolerance human is yes
 - Multiplied by 2 if has stability is 2
 - Multiplied by 1.5 if has high tolerance human race trigger is yes
 - Multiplied by 3 if has country modifier is racial pop human purge


###Efects:<ul><li>add dip power = -10</li><li>small decrease of human tolerance effect = yes</li></ul>
