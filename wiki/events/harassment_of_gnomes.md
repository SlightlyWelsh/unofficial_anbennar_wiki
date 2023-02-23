#Information
 - Title: Harassment of Gnomes
 - ID: gnomish_tolerance_events.2
#Description
Harassment of Gnomes
#Options

___
##Well, we could ignore the issue

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>add prestige = -5</li><li>add corruption = 1</li><li>event target:gnomish treated poorly province:</li><ul><li>add province modifier:</li><ul><li>name = gnomes_treated_poorly_prov</li><li>duration = 1825</li></ul></ul></ul>

___
##Something could be done about this

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.5 if has wants to maintain tolerance gnomish is yes
 - Multiplied by 0.1 if has wants to decrease tolerance gnomish is yes


###Efects:<ul><li>add prestige = 5</li><li>add mil power = -20</li><li>small increase of gnomish tolerance effect = yes</li><li>event target:gnomish treated poorly province:</li><ul><li>add province modifier:</li><ul><li>name = gnomes_protected_from_danger_prov</li><li>duration = 1825</li></ul></ul></ul>

___
##This seem just, support the trend!

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.5 if has wants to maintain tolerance gnomish is yes
 - Multiplied by 0.1 if has wants to increase tolerance gnomish is yes


###Efects:<ul><li>add prestige = -5</li><li>increase legitimacy small effect = yes</li><li>small decrease of gnomish tolerance effect = yes</li><li>event target:gnomish treated poorly province:</li><ul><li>add province modifier:</li><ul><li>name = gnomes_treated_poorly_prov</li><li>duration = 3650</li></ul></ul></ul>

___
##Those poor souls, we need to help them

###Available if:
<li>ruler has personality is kind_hearted_personality</li>

###AI weighting:
AI weights this option at 100
 - Multiplied by 0.5 if has wants to maintain tolerance gnomish is yes
 - Multiplied by 0.1 if has wants to decrease tolerance gnomish is yes


###Efects:<ul><li>highlight = yes</li><li>add prestige = 5</li><li>add dip power = -10</li><li>add mil power = -10</li><li>small increase of gnomish tolerance effect = yes</li><li>event target:gnomish treated poorly province:</li><ul><li>add province modifier:</li><ul><li>name = gnomes_protected_from_danger_prov</li><li>duration = 3650</li></ul></ul></ul>

___
##Make an example out of the troublemakers

###Available if:
<li>ruler has personality is cruel_personality</li>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>highlight = yes</li><li>add mil power = -10</li><li>If has corruption is 0.01:</li><ul><li>add corruption = -0.5</li></ul><li>medium increase of gnomish tolerance effect = yes</li><li>event target:gnomish treated poorly province:</li><ul><li>add unrest = 0.5</li></ul></ul>

___
##They should know better

###Available if:
<li>ruler has personality is strict_personality</li>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>highlight = yes</li><li>small increase of gnomish tolerance effect = yes</li><li>increase legitimacy small effect = yes</li><li>add mil power = -15</li><li>If has corruption is 0.01:</li><ul><li>add corruption = -0.75</li></ul><li>event target:gnomish treated poorly province:</li><ul><li>add unrest = -1</li></ul></ul>
