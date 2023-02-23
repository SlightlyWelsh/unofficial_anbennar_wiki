#Information
 - Title: Crovis Adshaw, Prince of Vrorenmarch
 - ID: flavor_grombar.17
#Description
Crovis Adshaw, Prince of Vrorenmarch
#Options

___
##Hail King Crovis, Lord of the Vroren!

###AI weighting:
AI weights this option at 95
 - Multiplied by 0.5 if has ruler is half orcish is yes


###Efects:<ul><li>grant independence = yes</li><li>reduce stability or adm power = yes</li><li>change tag = Z45</li><li>hidden effect:</li><ul><li>restore country name = yes</li></ul><li>define ruler:</li><ul><li>name = "Crovis I"</li><li>dynasty = "Adshaw"</li><li>adm = 2</li><li>dip = 4</li><li>mil = 5</li><li>age = 23</li><li>claim = 50</li><li>culture = Z26</li><li>religion = Z26</li></ul><li>kill heir:</li><ul></ul><li>add ruler modifier:</li><ul><li>name = crovis_invasion_mod</li><li>duration = 3650</li></ul><li>add years of income = 1</li><li>add yearly manpower = 1</li><li>hidden effect:</li><ul><li>Z45:</li><ul><li>If europe has region is alenic reach region, and  has owned by is Z18, and does not have core is ROOT:</li><ul><li>add core = Z45</li></ul></ul><li>701:</li><ul><li>add core = Z18</li></ul><li>709:</li><ul><li>add core = Z18</li></ul><li>712:</li><ul><li>add core = Z18</li></ul><li>713:</li><ul><li>add core = Z18</li></ul><li>Z18:</li><ul><li>the event [Crovis' Invasion'](../events/crovis_invasion.md) happens</li></ul><li>Z26:</li><ul><li>the event [Crovis' Adventure](../events/crovis_adventure.md) happens</li></ul><li>Z48:</li><ul><li>the event [A Chance for Freedom](../events/a_chance_for_freedom.md) happens</li></ul><li>Z49:</li><ul><li>the event [A Chance for Freedom](../events/a_chance_for_freedom.md) happens</li></ul></ul><li>capital scope:</li><ul><li>ROOT:</li><ul><li>infantry = PREV</li><li>infantry = PREV</li><li>infantry = PREV</li><li>infantry = PREV</li><li>infantry = PREV</li><li>infantry = PREV</li><li>infantry = PREV</li><li>infantry = PREV</li><li>infantry = PREV</li><li>infantry = PREV</li><li>infantry = PREV</li><li>infantry = PREV</li><li>infantry = PREV</li><li>infantry = PREV</li><li>cavalry = PREV</li><li>cavalry = PREV</li></ul></ul><li>If does not have custom ideas:</li><ul><li>the event [New Traditions & Ambitions](../events/new_traditions_ambitions.md) happens</li></ul><li>set global flag [crovis_invasion](../flags/crovis_invasion.md)</li></ul>

___
##Send him away, the days of Vrorenmarch are no more.

###AI weighting:
AI weights this option at 5
 - Multiplied by 20 if has ruler is half orcish is yes


###Efects:<ul><li>hidden effect:</li><ul><li>set country flag [crovis_rebellion](../flags/crovis_rebellion.md)</li></ul><li>capital scope:</li><ul><li>spawn rebels:</li><ul><li>type = pretender_rebels</li><li>size = 2</li><li>culture = old_alenic</li><li>religion = regent_court</li><li>leader = "Crovis"</li><li>leader dynasty = "Adshaw"</li><li>win = yes</li></ul></ul></ul>
