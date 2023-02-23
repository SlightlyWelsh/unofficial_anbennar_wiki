#Information
 - Title: Trompolere Leader Slain
 - ID: flavor_trompolere.1
#Description
Trompolere Leader Slain
#Options

___
##That is the fate of any who would threaten our peace

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>add prestige = 10</li><li>G36:</li><ul><li>the event ˻flavor_trompolere.4˼ happens</li></ul><li>If has core claim is G36:</li><ul><li>G36:</li><ul><li>If every owned province is core is ROOT:</li><ul><li>cede province = ROOT</li></ul></ul></ul><li>custom tooltip = trompolere_restore_tooltip</li><li>If every country has core claim is G36, and  has exists:</li><ul><li>the event ˻flavor_trompolere.2˼ happens</li><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = opinion_grateful</li></ul></ul><li>If has G36 has any owned province does not have tag is ROOT; and any core country has does not exist:</li><ul><li>G36:</li><ul><li>the event ˻flavor_trompolere.5˼ happens</li></ul></ul><li>ynn superregion:</li><ul><li>clr province flag [trompolere_seize_flag](../flags/trompolere_seize_flag.md)</li></ul></ul>

___
##Seize their land on our border

###Available if:
<li>Any of the following:</li><ul><li>G36:</li><ul><li>any owned province:</li><ul><li>has province flag [trompolere_seize_flag](../flags/trompolere_seize_flag.md)</li></ul></ul><li>has saved event target trompolere_subject_target</li></ul>

###AI weighting:
AI weights this option at 3
 - Multiplied by 0.5 if has any country has any core province has province flag is [trompolere_seize_flag](../flags/trompolere_seize_flag.md); and any country has reverse has opinion has who is ROOT, and reverse has opinion has value is 50
 - Multiplied by 0.5 if has any country has any core province has province flag is [trompolere_seize_flag](../flags/trompolere_seize_flag.md); and any country has reverse has opinion has who is ROOT, and reverse has opinion has value is 100


###Efects:<ul><li>G36:</li><ul><li>If every owned province has province flag is [trompolere_seize_flag](../flags/trompolere_seize_flag.md):</li><ul><li>cede province = ROOT</li></ul></ul><li>If has core claim is G36:</li><ul><li>G36:</li><ul><li>If every owned province is core is ROOT:</li><ul><li>cede province = ROOT</li></ul></ul></ul><li>custom tooltip = trompolere_restore_tooltip</li><li>If has saved event target is trompolere subject target:</li><ul><li>event target:trompolere subject target:</li><ul><li>the event ˻flavor_trompolere.7˼ happens</li></ul></ul><li>add prestige = 10</li><li>G36:</li><ul><li>the event ˻flavor_trompolere.4˼ happens</li></ul><li>If every country has core claim is G36, and  has exists, and does not have tag is ROOT:</li><ul><li>If has any core province has province flag is [trompolere_seize_flag](../flags/trompolere_seize_flag.md):</li><ul><li>the event ˻flavor_trompolere.3˼ happens</li><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = opinion_disappointed</li></ul></ul><li>else:</li><ul><li>the event ˻flavor_trompolere.2˼ happens</li><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = opinion_grateful</li></ul></ul></ul><li>If has G36 has any owned province does not have tag is ROOT; and any core country has does not exist:</li><ul><li>G36:</li><ul><li>the event ˻flavor_trompolere.5˼ happens</li></ul></ul><li>ynn superregion:</li><ul><li>clr province flag [trompolere_seize_flag](../flags/trompolere_seize_flag.md)</li></ul></ul>


#Pages with same name:
The following pages have the same name as this page:
 - [trompolere_leader_slain_1](trompolere_leader_slain_1.md)
