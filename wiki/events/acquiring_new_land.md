#Information
 - Title: Acquiring New Land
 - ID: nativebuyout.1
#Description
Acquiring New Land
#Options

___
##Send the natives a generous offer

###AI weighting:
AI weights this option at 100
 - Multiplied by 5 if has wants to increase tolerance ruinborn is yes


###Efects:<ul><li>add treasury = -200</li><li>event target:nativebuy owner:</li><ul><li>the event [An Offer from the Outsiders](../events/an_offer_from_the_outsiders.md) happens</li></ul><li>small increase of ruinborn tolerance effect = yes</li></ul>

___
##Send them some trinkets and a few of our older weapons

###AI weighting:
AI weights this option at 30
 - Multiplied by 5 if has wants to decrease tolerance ruinborn is yes
 - Multiplied by 10 if has ruler has personality is greedy personality


###Efects:<ul><li>set country flag [nativebuy_greedy](../flags/nativebuy_greedy.md)</li><li>add treasury = -20</li><li>event target:nativebuy owner:</li><ul><li>the event [An Offer from the Outsiders](../events/an_offer_from_the_outsiders.md) happens</li></ul><li>small decrease of ruinborn tolerance effect = yes</li></ul>

___
##We'll just take the place by force

###AI weighting:
AI weights this option at 10
 - Multiplied by 5 if has wants to decrease tolerance ruinborn is yes
 - Multiplied by 5 if is enemy is event target:nativebuy owner
 - Multiplied by 10 if has ruler has personality is conqueror personality


###Efects:<ul><li>hidden effect:</li><ul><li>set ai personality:</li><ul><li>personality = ai_militarist</li><li>locked = no</li></ul><li>If has event target:nativebuy owner is controlled by the AI, and does not have num of cities is 2; and event target:nativebuy owner has capital scope has empty adjacent province:</li><ul><li>event target:nativebuy owner:</li><ul><li>capital scope:</li><ul><li>random empty neighbor province:</li><ul><li>cede province = event_target:nativebuy_owner</li><li>add core = event_target:nativebuy_owner</li><li>change culture = event_target:nativebuy_owner</li><li>change religion = event_target:nativebuy_owner</li></ul></ul></ul></ul></ul><li>If has event target:nativebuy owner is controlled by the AI, and has num of cities is 2, and has capital scope has empty adjacent province:</li><ul><li>event target:nativebuy prov2:</li><ul><li>cede province = ROOT</li><li>add core = ROOT</li><li>change culture = ROOT</li><li>change religion = ROOT</li><li>add devastation = 5</li></ul><li>set capital = event_target:nativebuy_prov2</li><li>hidden effect:</li><ul><li>event target:nativebuy owner:</li><ul><li>the event [Attack on our Lands](../events/attack_on_our_lands.md) happens</li></ul></ul></ul><li>else:</li><ul><li>event target:nativebuy prov2:</li><ul><li>add core = ROOT</li></ul></ul><li>large decrease of ruinborn tolerance effect = yes</li></ul>

___
##Our current spot in [Root.Capital.GetName] is good enough

###AI weighting:
AI weights this option at 0

