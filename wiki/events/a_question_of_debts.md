#Information
 - Title: A Question of Debts
 - ID: flavor_arverynn.29
#Description
A Question of Debts
#Options

___
##We shall pay you in full

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>add treasury = -200</li><li>If has exists is H25:</li><ul><li>H25:</li><ul><li>add treasury = 200</li><li>If is subject of is ROOT:</li><ul><li>country gets the modifier H25_debt_repaid for 20 years</li></ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = opinion_friendliness</li></ul></ul></ul><li>else:</li><ul><li>1135:</li><ul><li>add base tax = 1</li><li>add base production = 1</li><li>add base manpower = 1</li><li>owner:</li><ul><li>If does not have tag is ROOT:</li><ul></ul><li>add liberty desire = -5</li></ul></ul></ul></ul>

___
##Would you be interested in Vels Domfan?

###Available if:
<li>exists is Stenurynn</li><li>mission completed is currency_reform</li><li>1134:</li><ul><li>owned by is this nation</li></ul>

###AI weighting:
AI weights this option at 2


###Efects:<ul><li>1134:</li><ul><li>cede province = H25</li></ul><li>If has 1134 has province modifier is G35 imperial mint:</li><ul><li>H25:</li><ul><li>add trust:</li><ul><li>who = ROOT</li><li>value = 10</li><li>mutual = yes</li></ul></ul></ul><li>H25:</li><ul><li>add prestige = 10</li><li>If is subject of is ROOT:</li><ul><li>country gets the modifier H25_debt_repaid for 20 years</li></ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = opinion_friendliness</li></ul></ul></ul>

___
##Even more debts? That sounds awful

###AI weighting:
AI weights this option at 1
 - Multiplied by 0.5 if has treasury is 200
 - Multiplied by 2 if has ruler has personality is greedy personality


###Efects:<ul><li>country gets the modifier G35_refused_to_pay_debts for 20 years</li><li>If has exists is H25:</li><ul><li>H25:</li><ul><li>remove historical friend = ROOT</li><li>If is subject of is ROOT:</li><ul><li>country gets the modifier H25_furious_about_debts for 20 years</li></ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = opinion_angry</li></ul></ul></ul><li>else:</li><ul><li>If every owned province is core is H25:</li><ul><li>add unrest = 3</li></ul></ul></ul>

___
##Move the mint to Arverynn and give them Vels Domfan

###Available if:
<li>exists is Stenurynn</li><li>mission completed is currency_reform</li><li>1134:</li><ul><li>owned by is this nation</li><li>has province modifier G35_imperial_mint</li></ul>

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>1134:</li><ul><li>add devastation = 30</li><li>add base production = -2</li><li>remove province modifier = G35_imperial_mint</li><li>add unrest = 5</li></ul><li>1139:</li><ul><li>add province modifier:</li><ul><li>name = G35_imperial_mint</li><li>duration = -1</li></ul></ul><li>add inflation = 2</li><li>1134:</li><ul><li>cede province = H25</li></ul><li>H25:</li><ul><li>If is subject of is G35:</li><ul><li>country gets the modifier H25_debt_repaid for 20 years</li></ul><li>add trust:</li><ul><li>who = ROOT</li><li>value = -10</li><li>mutual = yes</li></ul></ul></ul>
