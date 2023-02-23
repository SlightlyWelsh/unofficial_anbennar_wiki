#Information
 - Title: Fate of the Homunculus
 - ID: magic_project_homunculus.6
#Description
Fate of the Homunculus
#Mean Time to Happen:
Base time = 12 months
 - Multiplied by 2 if has ruler flag is [homunculus_current_humanlike](../flags/homunculus_current_humanlike.md)
 - Multiplied by 0.05 if has had ruler flag is [magic_project_homunculus_5](../flags/magic_project_homunculus_5.md) for 1095 days

#Options

___
##...a familiar to aid in my magical study

###Available if:
<li>None of the following:</li><ul><li>has country flag [ruler_studying_homunculus_familiar](../flags/ruler_studying_homunculus_familiar.md)</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 2 if has ruler has personality is scholar personality, and has ruler has personality is careful personality, and has ruler has personality is cruel personality


###Efects:<ul><li>set country flag [ruler_studying_homunculus_familiar](../flags/ruler_studying_homunculus_familiar.md)</li><li>custom tooltip = tooltip_homunculus_familiar</li><li>set ruler flag [magic_project_homunculus_complete](../flags/magic_project_homunculus_complete.md)</li><li>custom tooltip = tooltip_magic_project_complete</li><li>magic project clear homunculus flags = yes</li></ul>

___
##...a General

###AI weighting:
AI weights this option at 50
 - Multiplied by 2 if is at war
 - Multiplied by 2 if has personality is ai militarist
 - Multiplied by 0.25 if has num of generals is 3


###Efects:<ul><li>create general:</li><ul><li>tradition = 75</li></ul><li>set ruler flag [magic_project_homunculus_complete](../flags/magic_project_homunculus_complete.md)</li><li>custom tooltip = tooltip_magic_project_complete</li><li>magic project clear homunculus flags = yes</li></ul>

___
##...a Admiral

###AI weighting:
AI weights this option at 50
 - Multiplied by 2 if is at war
 - Multiplied by 2 if has personality is ai militarist
 - Multiplied by 0 if does not have navy size is 10
 - Multiplied by 0.25 if has num of admirals is 3


###Efects:<ul><li>create admiral:</li><ul><li>tradition = 75</li></ul><li>magic project clear homunculus flags = yes</li><li>set ruler flag [magic_project_homunculus_complete](../flags/magic_project_homunculus_complete.md)</li><li>custom tooltip = tooltip_magic_project_complete</li></ul>

___
##...a 'long lost' heir of my house

###Available if:
<li>has ruler flag [homunculus_current_humanlike](../flags/homunculus_current_humanlike.md)</li><li>has government attribute heir</li><li>None of the following:</li><ul><li>has reform magocracy_reform</li></ul><li>NOT:</li><ul><li>has reform magisterium_reform</li></ul><li>NOT:</li><ul><li>has reform states_general_reform</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.25 if has heir adm is 3, and has heir dip is 3, and has heir mil is 3


###Efects:<ul><li>remove heir:</li><ul></ul><li>If has ruler flag is [homunculus_current_male](../flags/homunculus_current_male.md), and has ruler flag is homunculus current androgyne:</li><ul><li>define heir:</li><ul><li>dynasty = ROOT</li><li>age = 18</li><li>change adm = 4</li><li>change dip = 4</li><li>change mil = 4</li><li>claim = 25</li><li>no consort with heir = yes</li><li>male = yes</li></ul></ul><li>If has ruler flag is [homunculus_current_female](../flags/homunculus_current_female.md):</li><ul><li>define heir:</li><ul><li>dynasty = ROOT</li><li>age = 18</li><li>change adm = 4</li><li>change dip = 4</li><li>change mil = 4</li><li>claim = 25</li><li>no consort with heir = yes</li><li>female = yes</li></ul></ul><li>hidden effect:</li><ul><li>add heir personality = immortal_personality</li></ul><li>set heir flag [is_a_secret_homunculus](../flags/is_a_secret_homunculus.md)</li><li>set ruler flag [magic_project_homunculus_complete](../flags/magic_project_homunculus_complete.md)</li><li>custom tooltip = tooltip_magic_project_complete</li><li>magic project clear homunculus flags = yes</li></ul>

___
##...my lover and consort

###Available if:
<li>has ruler flag [homunculus_current_humanlike](../flags/homunculus_current_humanlike.md)</li><li>does not have consort</li><li>government is monarchy</li><li>None of the following:</li><ul><li>has reform states_general_reform</li></ul><li>Any of the following:</li><ul><li>All of the following:</li><ul><li>is female</li><li>Any of the following:</li><ul><li>has ruler flag [homunculus_current_male](../flags/homunculus_current_male.md)</li><li>has ruler flag  homunculus_current_androgyne</li></ul></ul><li>AND:</li><ul><li>is not female</li><li>Any of the following:</li><ul><li>has ruler flag [homunculus_current_female](../flags/homunculus_current_female.md)</li><li>has ruler flag  homunculus_current_androgyne</li></ul></ul></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.25 if has consort adm is 3, and has consort dip is 3, and has consort mil is 3


###Efects:<ul><li>remove consort = yes</li><li>If is not female:</li><ul><li>define consort:</li><ul><li>age = 18</li><li>adm = 4</li><li>dip = 4</li><li>mil = 4</li><li>female = yes</li></ul></ul><li>Else if is female:</li><ul><li>define consort:</li><ul><li>dynasty = ROOT</li><li>age = 18</li><li>adm = 4</li><li>dip = 4</li><li>mil = 4</li><li>male = yes</li></ul></ul><li>hidden effect:</li><ul><li>add queen personality = immortal_personality</li></ul><li>set consort flag [is_a_secret_homunculus](../flags/is_a_secret_homunculus.md)</li><li>set ruler flag [magic_project_homunculus_complete](../flags/magic_project_homunculus_complete.md)</li><li>custom tooltip = tooltip_magic_project_complete</li><li>magic project clear homunculus flags = yes</li></ul>

___
##...an Advisor

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>the event [Homunculus Advisor](../events/homunculus_advisor.md) happens</li><li>set ruler flag [magic_project_homunculus_complete](../flags/magic_project_homunculus_complete.md)</li><li>custom tooltip = tooltip_magic_project_complete</li></ul>
