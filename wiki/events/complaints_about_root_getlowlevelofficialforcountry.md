#Information
 - Title: Complaints about [Root.GetLowLevelOfficialForCountry]
 - ID: 710
#Description
Complaints about [Root.GetLowLevelOfficialForCountry]
#Mean Time to Happen:
Base time = 1 days
 - Multiplied by 0.5 if is lucky

#Options

___
##Execute the [Root.GetLowLevelOfficialForCountry]!

###Available if:
<li>is not emperor of china</li><li>is not lesser in union</li><li>None of the following:</li><ul><li>government is republic</li></ul>

###AI weighting:
AI weights this option at 55
 - Multiplied by 0 if does not have legitimacy equivalent is 20
 - Multiplied by 0.5 if does not have legitimacy equivalent is 60
 - Multiplied by 1.5 if has legitimacy equivalent is 100


###Efects:<ul><li>add legitimacy = -10</li><li>add devotion = -10</li></ul>

___
##Execute the [Root.GetLowLevelOfficialForCountry]!

###Available if:
<li>Any of the following:</li><ul><li>government is republic</li><li>is emperor of china</li><li>is lesser in union</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>add meritocracy effect = yes</li><li>If has government is republic:</li><ul><li>add republican tradition = 5</li><li>add corruption = -2</li></ul><li>If is lesser in union:</li><ul><li>add liberty desire = 10</li></ul></ul>

___
##Ignore Complaints

###AI weighting:
AI weights this option at 45
 - Multiplied by 0.5 if does not have stability is 1
 - Multiplied by 1.5 if has stability is 2


###Efects:<ul><li>add stability = -1</li></ul>

___
##Strike down any who would oppose our [Root.GetLowLevelOfficialForCountry].

###Available if:
<li>ruler has personality is cruel_personality</li>

###Efects:<ul><li>highlight = yes</li><li>event target:bailiff province:</li><ul><li>spawn small scaled rebels:</li><ul><li>type = anti_tax_rebels</li><li>no defined leader = yes</li></ul></ul><li>If has country flag is [tyrant_system_initialized](../flags/tyrant_system_initialized.md):</li><ul><li>increase tyrant ruthless 1 = yes</li></ul></ul>
