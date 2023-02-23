#Information
 - Title: Samartal Investigation: Leader Reveals Everything
 - ID: new_sun_cult.182
#Description
Samartal Investigation: Leader Reveals Everything
#Options

___
##Make amends

###Available if:
<li>check variable:</li><ul><li>which is PersonallyInvestigatedCountriesVar</li><li>value is at least 1</li></ul>

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>If has check variable has which is PersonallyInvestigatedCountriesVar, and check variable has value is 5:</li><ul><li>add years of income = -1</li></ul><li>Else if has check variable has which is PersonallyInvestigatedCountriesVar, and check variable has value is 4:</li><ul><li>add years of income = -0.8</li></ul><li>Else if has check variable has which is PersonallyInvestigatedCountriesVar, and check variable has value is 3:</li><ul><li>add years of income = -0.6</li></ul><li>Else if has check variable has which is PersonallyInvestigatedCountriesVar, and check variable has value is 2:</li><ul><li>add years of income = -0.4</li></ul><li>Else if has check variable has which is PersonallyInvestigatedCountriesVar, and check variable has value is 1:</li><ul><li>add years of income = -0.2</li></ul><li>If every known country has country flag is [nsc_was_investigated_by_@ROOT](../flags/nsc_was_investigated_by_root.md):</li><ul><li>reverse add opinion:</li><ul><li>who = FROM</li><li>modifier = nsc_paid_reparations</li></ul><li>remove opinion:</li><ul><li>who = ROOT</li><li>modifier = nsc_tragedy_of_samartal</li></ul></ul><li>If every country is in war has attacker leader is ROOT, and is in war has casus belli is cb nsc investigation:</li><ul><li>white peace = ROOT</li></ul><li>set incident variable value:</li><ul><li>incident = incident_summit_of_samartal</li><li>value = 0</li></ul></ul>

___
##Don't make amends

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>If every country is in war has attacker leader is ROOT, and is in war has casus belli is cb nsc investigation:</li><ul><li>white peace = ROOT</li></ul></ul>
