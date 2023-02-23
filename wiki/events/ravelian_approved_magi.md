#Information
 - Title: Ravelian-Approved Magi?
 - ID: estate_organization.7
#Description
Ravelian-Approved Magi?
#Mean Time to Happen:
Base time = 3650 days

#Options

___
##Magic is holy, and they must be bound by faith.

###AI weighting:
AI weights this option at 75


###Efects:<ul><li>clear mages organization effect = yes</li><li>set estate privilege = estate_mages_organization_religious</li></ul>

___
##The Magisterium must remain.

###Available if:
<li>has estate privilege estate_mages_organization_magisterium</li>

###AI weighting:
AI weights this option at 75
 - Multiplied by 0 if has government is theocracy


###Efects:<ul><li>reverse add casus belli:</li><ul><li>target = Z97</li><li>type = cb_insult</li><li>months = 120</li></ul><li>reverse add opinion:</li><ul><li>who = Z97</li><li>modifier = refused_ravelian_org</li><li>years = 50</li></ul><li>add opinion:</li><ul><li>who = A85</li><li>modifier = maintained_magisterium_org</li><li>years = 50</li></ul></ul>

___
##Leave it as it is.

###Available if:
<li>None of the following:</li><ul><li>has estate privilege estate_mages_organization_magisterium</li></ul>

###AI weighting:
AI weights this option at 25
 - Multiplied by 0 if has government is theocracy


###Efects:<ul><li>reverse add casus belli:</li><ul><li>target = Z97</li><li>type = cb_insult</li><li>months = 120</li></ul><li>reverse add opinion:</li><ul><li>who = Z97</li><li>modifier = refused_ravelian_org</li><li>years = 50</li></ul></ul>
