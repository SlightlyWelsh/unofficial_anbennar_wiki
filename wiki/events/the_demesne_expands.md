#Information
 - Title: The Demesne Expands
 - ID: black_demesne.2
#Description
The Demesne Expands
#Options

___
##Share the land between the Throne and the Acolytes

###Available if:
<li>calc true if:</li><ul><li>all subject country:</li><ul><li>is subject of type is acolyte_dominion</li></ul><li>amount is at least 1</li></ul>

###AI weighting:
AI weights this option at 40


###Efects:<ul><li>hidden effect:</li><ul><li>set variable:</li><ul><li>nbProvBlack = 0</li></ul><li>REB:</li><ul><li>set variable:</li><ul><li>nbProvBlack = 0</li></ul></ul><li>event target:country:</li><ul><li>every subject country:</li><ul><li>grant independence = yes</li></ul><li>every owned province:</li><ul><li>REB:</li><ul><li>change variable:</li><ul><li>nbProvBlack = 1</li></ul></ul></ul></ul><li>REB:</li><ul><li>ROOT:</li><ul><li>set variable:</li><ul><li>which = nbProvBlack</li><li>which = PREV</li></ul></ul></ul><li>If has estate privilege is estate acolytes land share 10:</li><ul><li>multiply variable:</li><ul><li>nbProvBlack = 0.1</li></ul></ul><li>Else if has estate privilege is estate acolytes land share 20:</li><ul><li>multiply variable:</li><ul><li>nbProvBlack = 0.2</li></ul></ul><li>Else if has estate privilege is estate acolytes land share 30:</li><ul><li>multiply variable:</li><ul><li>nbProvBlack = 0.3</li></ul></ul><li>Else if has estate privilege is estate acolytes land share 40:</li><ul><li>multiply variable:</li><ul><li>nbProvBlack = 0.4</li></ul></ul><li>Else if has estate privilege is estate acolytes land share 50:</li><ul><li>multiply variable:</li><ul><li>nbProvBlack = 0.5</li></ul></ul><li>REB:</li><ul><li>subtract variable:</li><ul><li>which = nbProvBlack</li><li>which = ROOT</li></ul></ul><li>If while has check variable has nbProvBlack is 0:</li><ul><li>subtract variable:</li><ul><li>nbProvBlack = 1</li></ul><li>event target:country:</li><ul><li>random owned province:</li><ul><li>cede province = ROOT</li><li>remove loot:</li><ul><li>who = ROOT</li><li>amount = 100</li></ul></ul></ul></ul><li>acolytes land distribution effect = yes</li><li>event target:country:</li><ul><li>every owned province:</li><ul><li>cede province = ROOT</li><li>remove loot:</li><ul><li>who = ROOT</li><li>amount = 100</li></ul></ul></ul></ul><li>custom tooltip = share_the_land_acolyte_and_us_toolip</li></ul>

___
##Split the land between the Acolytes

###Available if:
<li>calc true if:</li><ul><li>all subject country:</li><ul><li>is subject of type is acolyte_dominion</li></ul><li>amount is at least 1</li></ul>

###AI weighting:
AI weights this option at 40


###Efects:<ul><li>hidden effect:</li><ul><li>set variable:</li><ul><li>nbProvBlack = 0</li></ul><li>REB:</li><ul><li>set variable:</li><ul><li>nbProvBlack = 0</li></ul></ul><li>event target:country:</li><ul><li>every subject country:</li><ul><li>grant independence = yes</li></ul><li>every owned province:</li><ul><li>REB:</li><ul><li>change variable:</li><ul><li>nbProvBlack = 1</li></ul></ul></ul></ul><li>acolytes land distribution effect = yes</li><li>event target:country:</li><ul><li>every owned province:</li><ul><li>cede province = ROOT</li><li>remove loot:</li><ul><li>who = ROOT</li><li>amount = 100</li></ul></ul></ul></ul><li>custom tooltip = share_the_land_acolyte_toolip</li></ul>

___
##Place it under direct control

###AI weighting:
AI weights this option at 40


###Efects:<ul><li>If has event target:country has total development is 1000:</li><ul><li>If every subject country is subject of type is acolyte dominion:</li><ul><li>add liberty desire = 100</li></ul></ul><li>Else if has event target:country has total development is 900:</li><ul><li>If every subject country is subject of type is acolyte dominion:</li><ul><li>add liberty desire = 90</li></ul></ul><li>Else if has event target:country has total development is 800:</li><ul><li>If every subject country is subject of type is acolyte dominion:</li><ul><li>add liberty desire = 80</li></ul></ul><li>Else if has event target:country has total development is 700:</li><ul><li>If every subject country is subject of type is acolyte dominion:</li><ul><li>add liberty desire = 70</li></ul></ul><li>Else if has event target:country has total development is 600:</li><ul><li>If every subject country is subject of type is acolyte dominion:</li><ul><li>add liberty desire = 60</li></ul></ul><li>Else if has event target:country has total development is 500:</li><ul><li>If every subject country is subject of type is acolyte dominion:</li><ul><li>add liberty desire = 50</li></ul></ul><li>Else if has event target:country has total development is 400:</li><ul><li>If every subject country is subject of type is acolyte dominion:</li><ul><li>add liberty desire = 40</li></ul></ul><li>Else if has event target:country has total development is 300:</li><ul><li>If every subject country is subject of type is acolyte dominion:</li><ul><li>add liberty desire = 30</li></ul></ul><li>Else if has event target:country has total development is 200:</li><ul><li>If every subject country is subject of type is acolyte dominion:</li><ul><li>add liberty desire = 20</li></ul></ul><li>Else if has event target:country has total development is 100:</li><ul><li>If every subject country is subject of type is acolyte dominion:</li><ul><li>add liberty desire = 10</li></ul></ul><li>Else if has event target:country has total development is 0:</li><ul><li>If every subject country is subject of type is acolyte dominion:</li><ul><li>add liberty desire = 5</li></ul></ul><li>custom tooltip = annex_everything_no_core_tooltip</li><li>hidden effect:</li><ul><li>event target:country:</li><ul><li>every owned province:</li><ul><li>cede province = ROOT</li></ul></ul></ul></ul>

___
##Create a new Dominion

###Available if:
<li>custom trigger tooltip:</li><ul><li>tooltip is create_new_acolyte_tooltip</li><li>black demesne has available acolyte is yes</li><li>black demesne can have another acolyte is yes</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>highlight = yes</li><li>custom tooltip = create_new_acolyte_effect_tooltip</li><li>hidden effect:</li><ul><li>set variable:</li><ul><li>nbProvBlack = 0</li></ul><li>REB:</li><ul><li>set variable:</li><ul><li>nbProvBlack = 0</li></ul></ul><li>event target:country:</li><ul><li>every subject country:</li><ul><li>grant independence = yes</li></ul><li>every owned province:</li><ul><li>REB:</li><ul><li>change variable:</li><ul><li>nbProvBlack = 1</li></ul></ul></ul></ul><li>REB:</li><ul><li>ROOT:</li><ul><li>set variable:</li><ul><li>which = nbProvBlack</li><li>which = PREV</li></ul></ul></ul><li>If has estate privilege is estate acolytes land share 10:</li><ul><li>multiply variable:</li><ul><li>nbProvBlack = 0.1</li></ul></ul><li>Else if has estate privilege is estate acolytes land share 20:</li><ul><li>multiply variable:</li><ul><li>nbProvBlack = 0.2</li></ul></ul><li>Else if has estate privilege is estate acolytes land share 30:</li><ul><li>multiply variable:</li><ul><li>nbProvBlack = 0.3</li></ul></ul><li>Else if has estate privilege is estate acolytes land share 40:</li><ul><li>multiply variable:</li><ul><li>nbProvBlack = 0.4</li></ul></ul><li>Else if has estate privilege is estate acolytes land share 50:</li><ul><li>multiply variable:</li><ul><li>nbProvBlack = 0.5</li></ul></ul><li>REB:</li><ul><li>subtract variable:</li><ul><li>which = nbProvBlack</li><li>which = ROOT</li></ul></ul><li>If while has check variable has nbProvBlack is 0:</li><ul><li>subtract variable:</li><ul><li>nbProvBlack = 1</li></ul><li>event target:country:</li><ul><li>random owned province:</li><ul><li>cede province = ROOT</li><li>remove loot:</li><ul><li>who = ROOT</li><li>amount = 100</li></ul></ul></ul></ul><li>REB:</li><ul><li>multiply variable:</li><ul><li>nbProvBlack = 0.7</li></ul></ul><li>new acolyte after conquest effect = yes</li></ul></ul>
