This page has the same name as others. For full listing see bottom of [the base page](the_ningbo_province_getcapitalname_incident.md).

#Information
 - Title: The [ningbo_province.GetCapitalName] Incident
 - ID: tributary_events.11
#Description
The [ningbo_province.GetCapitalName] Incident
#Options

___
##Unfortunate.

###Efects:<ul><li>FROM:</li><ul><li>If random active trade node does not have trade modifier has who is ROOT, and has trade modifier has name is tributary soured relations:</li><ul><li>add trade modifier:</li><ul><li>who = ROOT</li><li>duration = 5475</li><li>power = -10</li><li>key = tributary_soured_relations</li></ul></ul></ul><li>reduce estate burghers loyalty effect = yes</li><li>add estate nobles loyalty effect = yes</li></ul>

___
##Compensate [Root.Overlord.GetName] for the inconvenience.

###Efects:<ul><li>add years of income = -1</li><li>hidden effect:</li><ul><li>export to variable:</li><ul><li>which = money_to_give</li><li>value = years_of_income</li><li>who = ROOT</li></ul></ul><li>FROM:</li><ul><li>the event [Tribute from [ningbo_country.GetName]](../events/tribute_from_ningbo_country_getname.md) happens</li></ul><li>add estate burghers loyalty effect = yes</li><li>reduce estate nobles loyalty effect = yes</li></ul>
