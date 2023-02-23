#Information
 - Title: Arannese Landlords Found Joint Stock Company
 - ID: aelantirspawnables.16
#Description
Arannese Landlords Found Joint Stock Company
#Mean Time to Happen:
Base time = 360 months
 - Multiplied by 0.05 if has trollsbay region is a colony
 - Multiplied by 0.5 if is year is 1530
 - Multiplied by 0.5 if is not controlled by the AI

#Options

___
##Another competitor in Aelantir.

###Efects:<ul><li>G95:</li><ul><li>event target:spawn province:</li><ul><li>create colony = 1000</li><li>add core = G95</li></ul></ul><li>hidden effect:</li><ul><li>If does not have event target:spawn province has province id is 1024; and  has 1024 has owner has culture is ruinborn is yes:</li><ul><li>1024:</li><ul><li>save event target as = nativebuy_prov</li></ul><li>G95:</li><ul><li>the event [Acquiring New Land](../events/acquiring_new_land.md) happens</li></ul></ul><li>G95:</li><ul><li>the event [Colonial Ambitions](../events/colonial_ambitions.md) happens</li><li>the event [Elections in Marlliande](../events/elections_in_marlliande.md) happens</li><li>define ruler:</li><ul><li>name = "Adeline síl Marllin"</li><li>adm = 6</li><li>dip = 5</li><li>mil = 3</li><li>age = 96</li><li>claim = 95</li><li>female = yes</li><li>culture = arannese</li></ul><li>clear ruler vampire flags = yes</li><li>set country flag [new_vampire](../flags/new_vampire.md)</li><li>ruler become vampire = yes</li><li>add ruler personality = silver_tongue_personality</li><li>set country flag [vilaechi_lord](../flags/vilaechi_lord.md)</li></ul></ul><li>adventurer spawnable starting bonus:</li><ul><li>tag = G95</li></ul></ul>

___
##Play as the new country

###Available if:
<li>is not controlled by the AI</li>

###Efects:<ul><li>G95:</li><ul><li>event target:spawn province:</li><ul><li>create colony = 1000</li><li>add core = G95</li></ul></ul><li>hidden effect:</li><ul><li>If does not have event target:spawn province has province id is 1024; and  has 1024 has owner has culture is ruinborn is yes:</li><ul><li>1024:</li><ul><li>save event target as = nativebuy_prov</li></ul><li>G95:</li><ul><li>the event [Acquiring New Land](../events/acquiring_new_land.md) happens</li></ul></ul><li>G95:</li><ul><li>the event [Colonial Ambitions](../events/colonial_ambitions.md) happens</li><li>the event [Elections in Marlliande](../events/elections_in_marlliande.md) happens</li><li>define ruler:</li><ul><li>name = "Adeline síl Marllin"</li><li>adm = 6</li><li>dip = 5</li><li>mil = 3</li><li>age = 96</li><li>claim = 95</li><li>female = yes</li><li>culture = arannese</li></ul><li>add ruler personality = immortal_personality</li><li>add ruler personality = silver_tongue_personality</li><li>set ruler flag [is_a_vampire](../flags/is_a_vampire.md)</li><li>set country flag [vilaechi_lord](../flags/vilaechi_lord.md)</li></ul></ul><li>adventurer spawnable starting bonus:</li><ul><li>tag = G95</li></ul><li>switch tag = G95</li></ul>
