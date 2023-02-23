#Information
 - Title: Future of our Dominion
 - ID: black_demesne.4
#Description
Future of our Dominion
#Options

___
##Share it between the Acolytes and the Throne

###Available if:
<li>calc true if:</li><ul><li>all subject country:</li><ul><li>is subject of type is acolyte_dominion</li></ul><li>amount is at least 2</li></ul><li>None of the following:</li><ul><li>FROM:</li><ul><li>has country flag [newly_formed_dominion](../flags/newly_formed_dominion.md)</li></ul></ul>

###AI weighting:
AI weights this option at 40


###Efects:<ul><li>hidden effect:</li><ul><li>set variable:</li><ul><li>nbProvBlack = 0</li></ul><li>REB:</li><ul><li>set variable:</li><ul><li>nbProvBlack = 0</li></ul></ul><li>event target:country:</li><ul><li>every owned province:</li><ul><li>remove core = event_target:country</li><li>REB:</li><ul><li>change variable:</li><ul><li>nbProvBlack = 1</li></ul></ul></ul></ul><li>REB:</li><ul><li>ROOT:</li><ul><li>set variable:</li><ul><li>which = nbProvBlack</li><li>which = PREV</li></ul></ul></ul><li>If has estate privilege is estate acolytes land share 10:</li><ul><li>multiply variable:</li><ul><li>nbProvBlack = 0.1</li></ul></ul><li>Else if has estate privilege is estate acolytes land share 20:</li><ul><li>multiply variable:</li><ul><li>nbProvBlack = 0.2</li></ul></ul><li>Else if has estate privilege is estate acolytes land share 30:</li><ul><li>multiply variable:</li><ul><li>nbProvBlack = 0.3</li></ul></ul><li>Else if has estate privilege is estate acolytes land share 40:</li><ul><li>multiply variable:</li><ul><li>nbProvBlack = 0.4</li></ul></ul><li>Else if has estate privilege is estate acolytes land share 50:</li><ul><li>multiply variable:</li><ul><li>nbProvBlack = 0.5</li></ul></ul><li>REB:</li><ul><li>subtract variable:</li><ul><li>which = nbProvBlack</li><li>which = ROOT</li></ul></ul><li>If while has check variable has nbProvBlack is 0:</li><ul><li>subtract variable:</li><ul><li>nbProvBlack = 1</li></ul><li>event target:country:</li><ul><li>random owned province:</li><ul><li>cede province = ROOT</li><li>remove loot:</li><ul><li>who = ROOT</li><li>amount = 100</li></ul><li>add core = ROOT</li></ul></ul></ul><li>acolytes land distribution with core effect = yes</li><li>event target:country:</li><ul><li>every owned province:</li><ul><li>cede province = ROOT</li><li>add core = ROOT</li><li>remove loot:</li><ul><li>who = ROOT</li><li>amount = 100</li></ul></ul></ul></ul></ul>

___
##Split it between the Acolytes

###Available if:
<li>calc true if:</li><ul><li>all subject country:</li><ul><li>is subject of type is acolyte_dominion</li></ul><li>amount is at least 2</li></ul><li>None of the following:</li><ul><li>FROM:</li><ul><li>has country flag [newly_formed_dominion](../flags/newly_formed_dominion.md)</li></ul></ul>

###AI weighting:
AI weights this option at 40


###Efects:<ul><li>hidden effect:</li><ul><li>set variable:</li><ul><li>nbProvBlack = 0</li></ul><li>REB:</li><ul><li>set variable:</li><ul><li>nbProvBlack = 0</li></ul></ul><li>event target:country:</li><ul><li>every subject country:</li><ul><li>grant independence = yes</li></ul><li>every owned province:</li><ul><li>remove core = event_target:country</li><li>REB:</li><ul><li>change variable:</li><ul><li>nbProvBlack = 1</li></ul></ul></ul></ul><li>acolytes land distribution with core effect = yes</li><li>event target:country:</li><ul><li>every owned province:</li><ul><li>cede province = ROOT</li><li>add core = ROOT</li><li>remove loot:</li><ul><li>who = ROOT</li><li>amount = 100</li></ul></ul></ul></ul></ul>

___
##Place it all directly under the Throne

###Available if:
<li>None of the following:</li><ul><li>FROM:</li><ul><li>has country flag [newly_formed_dominion](../flags/newly_formed_dominion.md)</li></ul></ul>

###AI weighting:
AI weights this option at 40


###Efects:<ul><li>If has FROM has total development is 1000:</li><ul><li>If every subject country is subject of type is acolyte dominion:</li><ul><li>add liberty desire = 100</li></ul></ul><li>Else if has FROM has total development is 900:</li><ul><li>If every subject country is subject of type is acolyte dominion:</li><ul><li>add liberty desire = 90</li></ul></ul><li>Else if has FROM has total development is 800:</li><ul><li>If every subject country is subject of type is acolyte dominion:</li><ul><li>add liberty desire = 80</li></ul></ul><li>Else if has FROM has total development is 700:</li><ul><li>If every subject country is subject of type is acolyte dominion:</li><ul><li>add liberty desire = 70</li></ul></ul><li>Else if has FROM has total development is 600:</li><ul><li>If every subject country is subject of type is acolyte dominion:</li><ul><li>add liberty desire = 60</li></ul></ul><li>Else if has FROM has total development is 500:</li><ul><li>If every subject country is subject of type is acolyte dominion:</li><ul><li>add liberty desire = 50</li></ul></ul><li>Else if has FROM has total development is 400:</li><ul><li>If every subject country is subject of type is acolyte dominion:</li><ul><li>add liberty desire = 40</li></ul></ul><li>Else if has FROM has total development is 300:</li><ul><li>If every subject country is subject of type is acolyte dominion:</li><ul><li>add liberty desire = 30</li></ul></ul><li>Else if has FROM has total development is 200:</li><ul><li>If every subject country is subject of type is acolyte dominion:</li><ul><li>add liberty desire = 20</li></ul></ul><li>Else if has FROM has total development is 100:</li><ul><li>If every subject country is subject of type is acolyte dominion:</li><ul><li>add liberty desire = 10</li></ul></ul><li>Else if has FROM has total development is 0:</li><ul><li>If every subject country is subject of type is acolyte dominion:</li><ul><li>add liberty desire = 5</li></ul></ul><li>hidden effect:</li><ul><li>FROM:</li><ul><li>every owned province:</li><ul><li>remove core = event_target:country</li></ul></ul></ul><li>FROM:</li><ul><li>ROOT:</li><ul><li>inherit = PREV</li></ul></ul></ul>

___
##Choose a new Acolyte to rule over it

###AI weighting:
AI weights this option at 150


###Efects:<ul><li>tooltip:</li><ul><li>FROM:</li><ul><li>define ruler:</li><ul><li>culture = black_demesner</li><li>min age = 18</li><li>max age = 25</li><li>hide skills = yes</li></ul></ul></ul><li>hidden effect:</li><ul><li>FROM:</li><ul><li>random list:</li><ul><li>50:</li><ul><li>define ruler:</li><ul><li>culture = black_demesner</li><li>min age = 18</li><li>max age = 25</li><li>hide skills = yes</li><li>female = yes</li></ul></ul><li>50:</li><ul><li>define ruler:</li><ul><li>culture = black_demesner</li><li>min age = 18</li><li>max age = 25</li><li>hide skills = yes</li></ul></ul></ul></ul></ul><li>If has FROM has country flag is [newly_formed_dominion](../flags/newly_formed_dominion.md):</li><ul><li>hidden effect:</li><ul><li>FROM:</li><ul><li>clr country flag [newly_formed_dominion](../flags/newly_formed_dominion.md)</li></ul></ul></ul><li>else:</li><ul><li>custom tooltip = divide_influence_by_two_tooltip</li><li>hidden effect:</li><ul><li>FROM:</li><ul><li>divide variable:</li><ul><li>aInfluence = 2</li></ul></ul></ul></ul></ul>
