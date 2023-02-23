#Information
 - Title: Refusal to Pay Taxes
 - ID: court_and_country_events.2
#Description
Refusal to Pay Taxes
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Arrest their leaders!

###Efects:<ul><li>add absolutism = 5</li><li>event target:local court location:</li><ul><li>spawn rebels:</li><ul><li>type = particularist_rebels</li><li>size = 1.5</li></ul></ul><li>If every owned province has province flag is [local_courts_refuse_to_pay_tax](../flags/local_courts_refuse_to_pay_tax.md):</li><ul><li>add province modifier:</li><ul><li>name = "cnc_local_authority_asserted"</li><li>duration = 1825</li></ul><li>set province flag [had_local_courts_refused](../flags/had_local_courts_refused.md)</li><li>clr province flag [local_courts_refuse_to_pay_tax](../flags/local_courts_refuse_to_pay_tax.md)</li></ul></ul>

___
##Send a negotiator to the [local_court_location.GetName] [Root.GetLocalPowerStructure].

###Efects:<ul><li>If every owned province has province flag is [local_courts_refuse_to_pay_tax](../flags/local_courts_refuse_to_pay_tax.md):</li><ul><li>add province modifier:</li><ul><li>name = "cnc_refused_to_pay_taxes"</li><li>duration = 3650</li></ul><li>set province flag [had_local_courts_refused](../flags/had_local_courts_refused.md)</li><li>clr province flag [local_courts_refuse_to_pay_tax](../flags/local_courts_refuse_to_pay_tax.md)</li></ul></ul>
