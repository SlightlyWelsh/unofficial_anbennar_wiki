#Information
 - Title: Sack of [From.GetName]
 - ID: army_professionalism_events.1
#Description
Sack of [From.GetName]
#Mean Time to Happen:
Base time = 1 days
 - Multiplied by 0.5 if has army professionalism is 0.30
 - Multiplied by 0.5 if has FROM has owned by is Z47, and FROM is a capital

#Options

___
##We need better payment routines and harder discipline!

###AI weighting:
AI weights this option at 25
 - Multiplied by 2 if has years of income is 0.5


###Efects:<ul><li>add army professionalism = 0.05</li><li>add years of income = -0.25</li><li>FROM:</li><ul><li>fire province event [army_professionalism_events.2](army_professionalism_events.2_slug) immediately </li><li>tooltip:</li><ul><li>add devastation = 50</li></ul></ul><li>decrease monstrous 2 = yes</li></ul>

___
##We must punish the perpetrators!

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>add prestige = -5</li><li>FROM:</li><ul><li>fire province event [army_professionalism_events.18](army_professionalism_events.18_slug) immediately </li><li>tooltip:</li><ul><li>add devastation = 75</li></ul></ul><li>tooltip:</li><ul><li>event target:attacked country:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = sack_of_x</li></ul></ul></ul><li>decrease monstrous 1 = yes</li></ul>

___
##Such are the rules of warfare.

###Available if:
<li>None of the following:</li><ul><li>FROM:</li><ul><li>is a capital</li><li>None of the following:</li><ul><li>owned by is Doombringer Clan</li></ul></ul></ul>

###AI weighting:
AI weights this option at 25
 - Multiplied by 0 if is core is FROM
 - Multiplied by 0 if has primary culture is FROM
 - Multiplied by 5 if has reform is steppe horde


###Efects:<ul><li>add army professionalism = -0.05</li><li>add prestige = -10</li><li>add horde unity = 5</li><li>add loot from province effect = yes</li><li>FROM:</li><ul><li>fire province event [army_professionalism_events.3](army_professionalism_events.3_slug) immediately </li><li>tooltip:</li><ul><li>add devastation = 100</li><li>add base production = -2</li></ul></ul><li>tooltip:</li><ul><li>event target:attacked country:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = sack_of_x</li></ul><li>country gets the modifier "enemies_sacked_city" for 10 years</li></ul></ul><li>increase monstrous 2 = yes</li></ul>

___
##Plunder the Rectorate Treasury!

###Available if:
<li>has dlc "Emperor"</li><li>FROM:</li><ul><li>is a capital</li><li>owned by is Ravelian State</li></ul>

###AI weighting:
AI weights this option at 25
 - Multiplied by 0 if is core is FROM
 - Multiplied by 0 if has primary culture is FROM
 - Multiplied by 5 if has reform is steppe horde
 - Multiplied by 100 if does not have religion is catholic
 - Multiplied by 100 if has religion is catholic, and has ruler has personality is sinner personality, and has ruler has personality is malevolent personality


###Efects:<ul><li>highlight = yes</li><li>add treasury = 1000</li><li>add army professionalism = -0.05</li><li>add prestige = -10</li><li>add horde unity = 5</li><li>add loot from province effect = yes</li><li>FROM:</li><ul><li>fire province event [army_professionalism_events.3](army_professionalism_events.3_slug) immediately </li><li>tooltip:</li><ul><li>add devastation = 100</li><li>add base production = -2</li></ul></ul><li>tooltip:</li><ul><li>reduce curia treasury big effect = yes</li><li>event target:attacked country:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = sack_of_x</li></ul><li>country gets the modifier "enemies_sacked_city" for 10 years</li></ul></ul></ul>
