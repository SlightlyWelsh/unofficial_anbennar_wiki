#Information
 - Title: An Empty Crib
 - ID: consort_events.103
#Description
An Empty Crib
#Mean Time to Happen:
Base time = 600 months
 - Multiplied by 0.5 if has religion group is cannorian
 - Multiplied by 0.5 if has ruler has personality is infertile personality, and has consort has personality is infertile personality

#Options

___
##[Root.Monarch.GetTitle] [Root.Monarch.GetName] has a distant cousin who might be a decent option.

###AI weighting:
AI weights this option at 1
 - Multiplied by 2 if has ruler has personality is infertile personality


###Efects:<ul><li>custom tooltip = consort_events.103.b.tt</li><li>If has ruler flag is [male_cousin](../flags/male_cousin.md):</li><ul><li>define heir:</li><ul><li>claim = 60</li><li>male = yes</li><li>age = 30</li></ul></ul><li>If has ruler flag is [female_cousin](../flags/female_cousin.md):</li><ul><li>define heir:</li><ul><li>claim = 60</li><li>female = yes</li><li>age = 30</li></ul></ul><li>clr ruler flag [male_cousin](../flags/male_cousin.md)</li><li>clr ruler flag [female_cousin](../flags/female_cousin.md)</li></ul>

___
##We must be patient. It will happen, eventually.

###AI weighting:
AI weights this option at 1
 - Multiplied by 0.5 if has consort has personality is infertile personality


###Efects:<ul><li>custom tooltip = consort_events.103.c.tt</li><li>add prestige = -10</li><li>clr ruler flag [male_cousin](../flags/male_cousin.md)</li><li>clr ruler flag [female_cousin](../flags/female_cousin.md)</li></ul>

___
##It is obviously [Root.Consort.GetName]'s fault. The [Root.Monarch.GetTitle] needs another [Root.Consort.GetTitle].

###AI weighting:
AI weights this option at 1
 - Multiplied by 2 if has consort has personality is infertile personality


###Efects:<ul><li>divorce consort effect = yes</li><li>clr ruler flag [male_cousin](../flags/male_cousin.md)</li><li>clr ruler flag [female_cousin](../flags/female_cousin.md)</li></ul>
