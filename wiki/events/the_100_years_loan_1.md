This page has the same name as others. For full listing see bottom of [the base page](the_100_years_loan.md).

#Information
 - Title: The 100 Years' Loan
 - ID: venail.6
#Description
The 100 Years' Loan
#Options

___
##Pay them now in full!

###AI weighting:
AI weights this option at 25


###Efects:<ul><li>add treasury = -3000</li><li>A25:</li><ul><li>add treasury = 3000</li></ul><li>A25:</li><ul><li>the event [The 100 Years' Loan](../events/the_100_years_loan.md) happens</li></ul></ul>

___
##Offer them a deferred payment

###AI weighting:
AI weights this option at 65


###Efects:<ul><li>country gets the modifier venail_repay_loan for 75 years</li><li>A25:</li><ul><li>country gets the modifier venail_damescrown_receive_loan for 27357 days</li><li>the event [The 100 Years' Loan](../events/the_100_years_loan.md) happens</li></ul></ul>

___
##Give them a big trading port

###Available if:
<li>any owned province:</li><ul><li>has province modifier venail_cestircel</li></ul>

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>If random province has province modifier is venail cestircel:</li><ul><li>cede province = A25</li><li>add core = A25</li><li>remove core = ROOT</li></ul><li>A25:</li><ul><li>the event [The 100 Years' Loan](../events/the_100_years_loan.md) happens</li><li>set country flag [repayment_with_port](../flags/repayment_with_port.md)</li></ul></ul>

___
##Refuse. What could they do anyway?

###AI weighting:
AI weights this option at 10


###Efects:<ul><li>If every country has capital scope has superregion is western cannor superregion:</li><ul><li>add trust:</li><ul><li>who = ROOT</li><li>value = -45</li></ul></ul><li>add historical rival = A25</li><li>A25:</li><ul><li>set country flag [repayment_denied](../flags/repayment_denied.md)</li><li>the event [The 100 Years' Loan](../events/the_100_years_loan.md) happens</li></ul><li>country gets the modifier mischievious_elf until otherwise removed</li></ul>
