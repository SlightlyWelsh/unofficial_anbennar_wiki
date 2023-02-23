#Information
 - Title: Old Noblewoman Founds Colony!
 - ID: aelantirspawnables.12
#Description
Old Noblewoman Founds Colony!
#Mean Time to Happen:
Base time = 360 months
 - Multiplied by 0.05 if has trollsbay region is a colony
 - Multiplied by 0.5 if is year is 1550
 - Multiplied by 0.5 if is not controlled by the AI

#Options

___
##Another competitor in Aelantir.

###Efects:<ul><li>G91:</li><ul><li>event target:spawn province:</li><ul><li>create colony = 1000</li><li>add core = G91</li></ul></ul><li>hidden effect:</li><ul><li>If does not have event target:spawn province has province id is 1035; and  has 1035 has owner has culture is ruinborn is yes:</li><ul><li>1035:</li><ul><li>save event target as = nativebuy_prov</li></ul><li>G91:</li><ul><li>the event [Acquiring New Land](../events/acquiring_new_land.md) happens</li></ul></ul><li>Else if has event target:spawn province has province id is 1035; and  has 1036 has owner has culture is ruinborn is yes:</li><ul><li>1036:</li><ul><li>save event target as = nativebuy_prov</li></ul><li>G91:</li><ul><li>the event [Acquiring New Land](../events/acquiring_new_land.md) happens</li></ul></ul><li>G91:</li><ul><li>the event [Colonial Ambitions](../events/colonial_ambitions.md) happens</li><li>define ruler:</li><ul><li>name = "Isobel síl Isobelin"</li><li>adm = 5</li><li>dip = 6</li><li>mil = 2</li><li>age = 48</li><li>claim = 95</li><li>female = yes</li><li>culture = roilsardi</li></ul></ul></ul><li>adventurer spawnable starting bonus:</li><ul><li>tag = G91</li></ul></ul>

___
##Play as the new country

###Available if:
<li>is not controlled by the AI</li>

###Efects:<ul><li>G91:</li><ul><li>event target:spawn province:</li><ul><li>create colony = 1000</li><li>add core = G91</li></ul></ul><li>hidden effect:</li><ul><li>If does not have event target:spawn province has province id is 1035; and  has 1035 has owner has culture is ruinborn is yes:</li><ul><li>1035:</li><ul><li>save event target as = nativebuy_prov</li></ul><li>G91:</li><ul><li>the event [Acquiring New Land](../events/acquiring_new_land.md) happens</li></ul></ul><li>Else if has event target:spawn province has province id is 1035; and  has 1036 has owner has culture is ruinborn is yes:</li><ul><li>1036:</li><ul><li>save event target as = nativebuy_prov</li></ul><li>G91:</li><ul><li>the event [Acquiring New Land](../events/acquiring_new_land.md) happens</li></ul></ul><li>G91:</li><ul><li>the event [Colonial Ambitions](../events/colonial_ambitions.md) happens</li><li>define ruler:</li><ul><li>name = "Isobel síl Isobelin"</li><li>adm = 5</li><li>dip = 6</li><li>mil = 2</li><li>age = 48</li><li>claim = 95</li><li>female = yes</li><li>culture = roilsardi</li></ul></ul></ul><li>adventurer spawnable starting bonus:</li><ul><li>tag = G91</li></ul><li>switch tag = G91</li></ul>
