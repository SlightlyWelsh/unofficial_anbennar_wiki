This page has the same name as others. For full listing see bottom of [the base page](the_100_years.md).

#Information
 - Title: The 100 Years' Loan
 - ID: venail.7
#Description
The 100 Years' Loan
#Options

___
##Keep it in our chests, now and forever!

###Available if:
<li>None of the following:</li><ul><li>has country flag [repayment_denied](../flags/repayment_denied.md)</li></ul>

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>add prestige = 25</li></ul>

___
##We should reinvest everything.

###Available if:
<li>None of the following:</li><ul><li>has country flag [repayment_denied](../flags/repayment_denied.md)</li></ul><li>NOT:</li><ul><li>has country flag [repayment_with_port](../flags/repayment_with_port.md)</li></ul>

###AI weighting:
AI weights this option at 5


###Efects:<ul><li>If has country modifier is venail damescrown receive loan:</li><ul><li>remove country modifier = venail_damescrown_receive_loan</li></ul><li>else:</li><ul><li>add treasury = -3000</li></ul><li>add prestige = 25</li><li>capital scope:</li><ul><li>add base manpower = 2</li><li>add base production = 2</li><li>add base tax = 2</li><li>area:</li><ul><li>add base manpower = 1</li><li>add base production = 1</li><li>add base tax = 1</li></ul></ul></ul>

___
##Let's build an exclusive trade center with Aelnar!

###Available if:
<li>None of the following:</li><ul><li>has country flag [repayment_denied](../flags/repayment_denied.md)</li></ul><li>NOT:</li><ul><li>has country flag [repayment_with_port](../flags/repayment_with_port.md)</li></ul>

###AI weighting:
AI weights this option at 95


###Efects:<ul><li>If has country modifier is venail damescrown receive loan:</li><ul><li>remove country modifier = venail_damescrown_receive_loan</li></ul><li>else:</li><ul><li>add treasury = -3000</li></ul><li>add prestige = 25</li><li>capital scope:</li><ul><li>add base manpower = 2</li><li>add base production = 2</li><li>add base tax = 2</li><li>change trade goods = precursor_relics</li><li>add province modifier:</li><ul><li>name = aelnar_exclusive_trade</li><li>duration = -1</li></ul></ul></ul>

___
##Those bastards!

###Available if:
<li>has country flag [repayment_denied](../flags/repayment_denied.md)</li>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>clr country flag [repayment_denied](../flags/repayment_denied.md)</li><li>add prestige = -25</li><li>If random province has province modifier is venail cestircel:</li><ul><li>add permanent claim = ROOT</li></ul><li>add historical rival = A21</li><li>add historical rival = Z43</li></ul>
