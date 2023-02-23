#Information
 - Title: An Offer from the Outsiders
 - ID: nativebuyout.2
#Description
An Offer from the Outsiders
#Options

___
##We accept the deal

###Available if:
<li>Any of the following:</li><ul><li>num of cities is at least 2</li><li>capital scope:</li><ul><li>has empty adjacent province</li></ul></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>If does not have num of cities is 2:</li><ul><li>custom tooltip = nativebuy_migrate_tt</li><li>hidden effect:</li><ul><li>event target:nativebuy migration:</li><ul><li>cede province = ROOT</li><li>add core = ROOT</li><li>change culture = ROOT</li><li>change religion = ROOT</li></ul></ul></ul><li>If has FROM has country flag is [nativebuy_greedy](../flags/nativebuy_greedy.md):</li><ul><li>add treasury = 20</li></ul><li>else:</li><ul><li>add treasury = 200</li></ul><li>add adm power = 15</li><li>add dip power = 15</li><li>add mil power = 15</li><li>event target:nativebuy prov3:</li><ul><li>cede province = FROM</li><li>remove core = ROOT</li></ul><li>FROM:</li><ul><li>the event [The Natives Accept!](../events/the_natives_accept.md) happens</li></ul><li>add truce with = FROM</li><li>FROM:</li><ul><li>clr country flag [nativebuy_greedy](../flags/nativebuy_greedy.md)</li></ul></ul>

___
##The land of [nativebuy_prov3.GetName] is not for sale

###AI weighting:
AI weights this option at 10
 - Multiplied by 0 if has FROM is controlled by the AI
 - Multiplied by 0.1 if has FROM is not controlled by the AI, and FROM has tag is G96
 - Multiplied by 10 if has FROM is not controlled by the AI; and  has FROM has country flag is [nativebuy_greedy](../flags/nativebuy_greedy.md)
 - Multiplied by 100 if has FROM is not controlled by the AI; and  has FROM has country flag is [nativebuy_greedy](../flags/nativebuy_greedy.md); and  has ruler has personality is well advised personality
 - Multiplied by 100 if has FROM is not controlled by the AI; and  has ruler has personality is incorruptible personality
 - Multiplied by 100 if has FROM is not controlled by the AI; and  is enemy is FROM


###Efects:<ul><li>hidden effect:</li><ul><li>If has FROM has country flag is [nativebuy_greedy](../flags/nativebuy_greedy.md):</li><ul><li>FROM:</li><ul><li>add treasury = 20</li></ul></ul><li>else:</li><ul><li>FROM:</li><ul><li>add treasury = 200</li></ul></ul></ul><li>FROM:</li><ul><li>the event [The Natives Refuse](../events/the_natives_refuse.md) happens</li></ul><li>FROM:</li><ul><li>clr country flag [nativebuy_greedy](../flags/nativebuy_greedy.md)</li></ul></ul>
