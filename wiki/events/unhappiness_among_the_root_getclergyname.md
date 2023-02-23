#Information
 - Title: Unhappiness Among the [Root.GetClergyName]
 - ID: 5050
#Description
Unhappiness Among the [Root.GetClergyName]
#Mean Time to Happen:
Base time = 1 days
 - Multiplied by 2.0 if does not have advisor is theologian
 - Multiplied by 0.5 if is lucky
 - Multiplied by 0.66 if has theologian is 3

#Options

___
##Ignore their demands.

###AI weighting:
AI weights this option at 55
 - Multiplied by 0.5 if has prestige is 90
 - Multiplied by 0 if has estate is estate church, and does not have estate loyalty has estate is estate church, and estate loyalty has loyalty is 30


###Efects:<ul><li>reduce estate church loyalty effect = yes</li><li>If has religion group is muslim:</li><ul><li>add piety = -0.1</li></ul><li>If has religion is ravelian:</li><ul><li>add papal influence = -10</li></ul><li>If has religion is orthodox:</li><ul><li>add patriarch authority = -0.1</li></ul><li>add prestige = 10</li></ul>

___
##Agree to their demands.

###AI weighting:
AI weights this option at 45
 - Multiplied by 0.5 if does not have prestige is 0


###Efects:<ul><li>add estate church loyalty effect = yes</li><li>If has religion group is muslim:</li><ul><li>add piety = 0.2</li></ul><li>If has religion is ravelian:</li><ul><li>add papal influence = 10</li></ul><li>If has religion is orthodox:</li><ul><li>add patriarch authority = 0.05</li></ul><li>add prestige = -15</li></ul>

___
##Let our [Root.Monarch.GetTitle] attempt to placate them.

###Available if:
<li>ruler has personality ancestor:</li><ul><li>key is zealot</li></ul>

###Efects:<ul><li>highlight = yes</li><li>add estate church loyalty effect = yes</li><li>If has religion group is muslim:</li><ul><li>add piety = 0.1</li></ul><li>If has religion is ravelian:</li><ul><li>add papal influence = 5</li></ul><li>If has religion is orthodox:</li><ul><li>add patriarch authority = 0.025</li></ul></ul>

___
##Let our [Root.Monarch.GetTitle] personally take the blame.

###Available if:
<li>ruler has personality ancestor:</li><ul><li>key is pious</li></ul>

###Efects:<ul><li>highlight = yes</li><li>add devotion = -5</li></ul>
