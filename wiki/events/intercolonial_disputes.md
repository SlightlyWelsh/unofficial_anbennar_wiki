#Information
 - Title: Intercolonial Disputes
 - ID: pretty_colonial_borders.3
#Description
Intercolonial Disputes
#Options

___
##Side with [colonial_country_1.GetName].

###AI weighting:
AI weights this option at 1
 - Multiplied by 1.5 if has event target:colonial country 1 has liberty desire is 35
 - Multiplied by 1.5 if has event target:colonial country 1 has liberty desire is 45
 - Multiplied by 1.5 if does not have liberty desire is 15
 - Multiplied by 0.75 if has event target:colonial country 2 has liberty desire is 35
 - Multiplied by 0.75 if has event target:colonial country 2 has liberty desire is 45


###Efects:<ul><li>event target:colonial country 1:</li><ul><li>add liberty desire = -15</li></ul><li>event target:colonial country 2:</li><ul><li>add liberty desire = 15</li></ul></ul>

___
##Side with [colonial_country_2.GetName].

###AI weighting:
AI weights this option at 1
 - Multiplied by 1.5 if has event target:colonial country 2 has liberty desire is 35
 - Multiplied by 1.5 if has event target:colonial country 2 has liberty desire is 45
 - Multiplied by 1.5 if does not have liberty desire is 15
 - Multiplied by 0.75 if has event target:colonial country 1 has liberty desire is 35
 - Multiplied by 0.75 if has event target:colonial country 1 has liberty desire is 45


###Efects:<ul><li>custom tooltip = pretty_colonial_borders.3.B.tooltip</li><li>hidden effect:</li><ul><li>event target:pretty colonial province:</li><ul><li>add core = event_target:colonial_country_2</li><li>remove core = event_target:colonial_country_1</li><li>cede province = event_target:colonial_country_2</li><li>If has any neighbor province has colonial region is prev, and any neighbor province has owned by is event target:colonial country 1:</li><ul><li>If every neighbor province has colonial region is prev, and  has owned by is event target:colonial country 1:</li><ul><li>add core = event_target:colonial_country_2</li><li>remove core = event_target:colonial_country_1</li><li>cede province = event_target:colonial_country_2</li><li>If has any neighbor province has colonial region is prev, and any neighbor province has owned by is event target:colonial country 1, and does not have province id is event target:pretty colonial province; and does not have any neighbor province has owned by is event target:colonial country 1, and does not have province id is prev, and does not have province id is event target:pretty colonial province:</li><ul><li>If every neighbor province has colonial region is prev, and  has owned by is event target:colonial country 1, and does not have province id is event target:pretty colonial province; and does not have any neighbor province has owned by is event target:colonial country 1, and does not have province id is prev, and does not have province id is event target:pretty colonial province:</li><ul><li>add core = event_target:colonial_country_2</li><li>remove core = event_target:colonial_country_1</li><li>cede province = event_target:colonial_country_2</li></ul></ul></ul></ul></ul></ul><li>event target:colonial country 1:</li><ul><li>add liberty desire = 15</li></ul><li>event target:colonial country 2:</li><ul><li>add liberty desire = -15</li></ul></ul>
