#Information
 - Title: Aspiring Hero on Potraga
 - ID: ynn_events.207
#Description
Aspiring Hero on Potraga
#Options

___
##This hero could instruct our whole army!

###AI weighting:
AI weights this option at 50
 - Multiplied by 0 if is bankrupt


###Efects:<ul><li>add treasury = -40</li><li>define advisor:</li><ul><li>type = army_reformer</li><li>skill = 3</li><li>discount = yes</li><li>culture = event_target:potraga_origins</li><li>religion = event_target:potraga_origins</li></ul></ul>

___
##He would best serve us by vanquishing our enemies on the battlefield.

###AI weighting:
AI weights this option at 50
 - Multiplied by 0 if is bankrupt


###Efects:<ul><li>add treasury = -40</li><li>create general:</li><ul><li>tradition = 60</li><li>culture = event_target:potraga_origins</li></ul></ul>

___
##Serve? He should marry one of our princesses instead!

###Available if:
<li>Any of the following:</li><ul><li>has female heir</li><li>does not have heir</li></ul><li>None of the following:</li><ul><li>All of the following:</li><ul><li>is female</li><li>does not have consort</li></ul></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 2 if has ruler has personality is infertile personality
 - Multiplied by 2 if has ruler age is 45
 - Multiplied by 0.5 if has ruler has personality is fertile personality
 - Multiplied by 0.5 if does not have ruler age is 25


###Efects:<ul><li>define heir:</li><ul><li>dynasty = ROOT</li><li>age = 16</li><li>claim = 50</li><li>adm = 2</li><li>dip = 2</li><li>mil = 3</li><li>hide skills = yes</li><li>no consort with heir = yes</li><li>male = yes</li><li>culture = event_target:potraga_origins</li><li>religion = event_target:potraga_origins</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_adventurers</li><li>desc = ynn_promoted_hero_to_prince</li><li>influence = 15</li><li>duration = 7200</li></ul></ul>

___
##Marry me!

###Available if:
<li>is female</li><li>does not have consort</li><li>does not have regency</li>

###AI weighting:
AI weights this option at 50
 - Multiplied by 100 if has ruler has personality is fertile personality, and has ruler has personality is sinner personality


###Efects:<ul><li>define consort:</li><ul><li>age = 16</li><li>adm = 4</li><li>dip = 5</li><li>mil = 5</li><li>hide skills = yes</li><li>male = yes</li><li>culture = event_target:potraga_origins</li><li>religion = event_target:potraga_origins</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_adventurers</li><li>desc = ynn_promoted_hero_to_prince</li><li>influence = 15</li><li>duration = 7200</li></ul></ul>

___
##You may have the peasants' favour, but war and rulership are not a thing for boys.

###AI weighting:
AI weights this option at 25


###Efects:<ul><li>add estate loyalty:</li><ul><li>estate = estate_adventurers</li><li>loyalty = -5</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_adventurers</li><li>desc = ynn_turned_away_promising_hero</li><li>influence = -10</li><li>duration = 3600</li></ul></ul>
