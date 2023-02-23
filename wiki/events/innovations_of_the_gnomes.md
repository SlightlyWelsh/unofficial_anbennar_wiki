#Information
 - Title: Innovations of the Gnomes
 - ID: gnomish_tolerance_events.1
#Description
Innovations of the Gnomes
#Options

___
##We need to exploit this, NOW!

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>add adm power = 10</li><li>add dip power = 10</li><li>event target:innovations gnomish province:</li><ul><li>If area does not have province modifier is gnomish exploiting inventions prov; and does not have province modifier is gnomish respect of innovations prov; and does not have province modifier is gnomish stopped innovations prov; and  has owned by is ROOT, and has gnomish minority trigger is yes, and has culture group is gnomish:</li><ul><li>add province modifier:</li><ul><li>name = gnomish_exploiting_inventions_prov</li><li>duration = 1825</li></ul></ul></ul></ul>

___
##Respect their wishes

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.5 if has wants to maintain tolerance gnomish is yes
 - Multiplied by 0.1 if has wants to decrease tolerance gnomish is yes


###Efects:<ul><li>small increase of gnomish tolerance effect = yes</li><li>event target:innovations gnomish province:</li><ul><li>If area does not have province modifier is gnomish exploiting inventions prov; and does not have province modifier is gnomish respect of innovations prov; and does not have province modifier is gnomish stopped innovations prov; and  has owned by is ROOT, and has gnomish minority trigger is yes, and has culture group is gnomish:</li><ul><li>add province modifier:</li><ul><li>name = gnomish_respect_of_innovations_prov</li><li>duration = 1825</li></ul></ul></ul></ul>

___
##Confiscate their machines

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.5 if has wants to maintain tolerance gnomish is yes
 - Multiplied by 0.1 if has wants to increase tolerance gnomish is yes


###Efects:<ul><li>add prestige = 5</li><li>add mil power = -10</li><li>add dip power = -10</li><li>If has max manpower is 20:</li><ul><li>add manpower = -1</li></ul><li>If does not have max manpower is 20:</li><ul><li>add yearly manpower = -0.5</li></ul><li>add years of income = 0.4</li><li>small decrease of gnomish tolerance effect = yes</li><li>event target:innovations gnomish province:</li><ul><li>add province modifier:</li><ul><li>name = gnomish_stopped_innovations_prov</li><li>duration = 1825</li></ul></ul></ul>

___
##A great innovation, lets make use of it with their help!

###Available if:
<li>Any of the following:</li><ul><li>ruler has personality is scholar_personality</li><li>ruler has personality  is free_thinker_personality</li></ul>

###AI weighting:
AI weights this option at 100
 - Multiplied by 0.5 if has wants to maintain tolerance gnomish is yes
 - Multiplied by 0.1 if has wants to decrease tolerance gnomish is yes


###Efects:<ul><li>highlight = yes</li><li>add adm power = 10</li><li>add dip power = 10</li><li>small increase of gnomish tolerance effect = yes</li><li>event target:innovations gnomish province:</li><ul><li>If area does not have province modifier is gnomish exploiting inventions prov; and does not have province modifier is gnomish respect of innovations prov; and does not have province modifier is gnomish stopped innovations prov; and  has owned by is ROOT, and has gnomish minority trigger is yes, and has culture group is gnomish:</li><ul><li>add province modifier:</li><ul><li>name = gnomish_respect_of_innovations_prov</li><li>duration = 3650</li></ul></ul></ul></ul>
