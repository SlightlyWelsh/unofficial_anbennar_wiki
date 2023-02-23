#Information
 - Title: Ozarm'Chadash - Ruler is challenged
 - ID: orc_flavor.1
#Description
Ozarm'Chadash - Ruler is challenged
#Mean Time to Happen:
Base time = 240 months
 - Multiplied by 0.9 if does not have stability is 0
 - Multiplied by 0.8 if does not have stability is -1
 - Multiplied by 0.7 if does not have stability is -2
 - Multiplied by 0.8 if does not have mil is 3
 - Multiplied by 0.7 if does not have mil is 2
 - Multiplied by 0.5 if does not have mil is 1
 - Multiplied by 0.8 if does not have prestige is -25
 - Multiplied by 0.8 if does not have prestige is -50
 - Multiplied by 0.8 if does not have prestige is -75
 - Multiplied by 0.5 if does not have legitimacy is 50
 - Multiplied by 0.9 if has reform is orcish kingdom reform
 - Multiplied by 0.8 if has full idea group is aristocracy ideas
 - Multiplied by 1.25 if is year is 1600
 - Multiplied by 1.25 if is year is 1700
 - Multiplied by 1.25 if has mil is 4
 - Multiplied by 1.25 if has mil is 5
 - Multiplied by 1.5 if has mil is 6
 - Multiplied by 2 if has full idea group is innovativeness ideas
 - Multiplied by 2 if has full idea group is administrative ideas
 - Multiplied by 2 if has full idea group is diplomatic ideas
 - Multiplied by 2 if has full idea group is spy ideas
 - Multiplied by 2 if does not have religion group is orcish
 - Multiplied by 2 if has tag is Z50
 - Multiplied by 2 if has government is monarchy
 - Multiplied by 2 if has government is republic
 - Multiplied by 2.5 if has ruler modifier is ozarm chadash without fight
 - Multiplied by 2.5 if has ruler modifier is ozarm chadash outraged by dishonor
 - Multiplied by 5 if has government is theocracy
 - Multiplied by 5 if has ruler flag is [orc_winner_of_ozarmchadash](../flags/orc_winner_of_ozarmchadash.md)

#Options

___
##[Root.Monarch.GetSheHeCap] will just step down.

###AI weighting:
AI weights this option at 30
 - Multiplied by 0 if has ruler has personality is intricate web weaver personality, and has ruler has personality is charismatic negotiator personality, and has full idea group is diplomatic ideas, and has full idea group is spy ideas, and has dip is 5


###Efects:<ul><li>reduce stability or adm power = yes</li><li>add prestige = -25</li><li>define ruler:</li><ul><li>claim = 50</li><li>culture = ROOT</li></ul><li>kill consort = yes</li><li>kill heir:</li><ul><li>allow new heir = no</li></ul><li>add ruler modifier:</li><ul><li>name = ozarm_chadash_without_fight</li><li>duration = 1825</li></ul></ul>

___
##We can solve this without any duel...

###Available if:
<li>Any of the following:</li><ul><li>ruler has personality is intricate_web_weaver_personality</li><li>ruler has personality  is charismatic_negotiator_personality</li><li>full idea group is diplomatic_ideas</li><li>full idea group  is spy_ideas</li><li>dip is at least 5</li></ul>

###AI weighting:
AI weights this option at 65


###One of the following randomly happens:
Outcome 1:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>add prestige = -10</li><li>reduce stability or adm power = yes</li><li>add ruler modifier:</li><ul><li>name = ozarm_chadash_outraged_by_dishonor</li><li>duration = 1825</li></ul><li>custom tooltip = lets_fight_tooltip</li><li>hidden effect:</li><ul><li>If does not have mil is 1:</li><ul><li>random list:</li><ul><li>90:</li><ul><li>the event ˻orc_flavor.2˼ happens</li></ul><li>10:</li><ul><li>the event ˻orc_flavor.3˼ happens</li></ul></ul></ul><li>If has mil is 1, and does not have mil is 2:</li><ul><li>random list:</li><ul><li>75:</li><ul><li>the event ˻orc_flavor.2˼ happens</li></ul><li>25:</li><ul><li>the event ˻orc_flavor.3˼ happens</li></ul></ul></ul><li>If has mil is 2, and does not have mil is 3:</li><ul><li>random list:</li><ul><li>66:</li><ul><li>the event ˻orc_flavor.2˼ happens</li></ul><li>33:</li><ul><li>the event ˻orc_flavor.3˼ happens</li></ul></ul></ul><li>If has mil is 3, and does not have mil is 4:</li><ul><li>random list:</li><ul><li>50:</li><ul><li>the event ˻orc_flavor.2˼ happens</li></ul><li>50:</li><ul><li>the event ˻orc_flavor.3˼ happens</li></ul></ul></ul><li>If has mil is 4, and does not have mil is 5:</li><ul><li>random list:</li><ul><li>33:</li><ul><li>the event ˻orc_flavor.2˼ happens</li></ul><li>66:</li><ul><li>the event ˻orc_flavor.3˼ happens</li></ul></ul></ul><li>If has mil is 5, and does not have mil is 6:</li><ul><li>random list:</li><ul><li>25:</li><ul><li>the event ˻orc_flavor.2˼ happens</li></ul><li>75:</li><ul><li>the event ˻orc_flavor.3˼ happens</li></ul></ul></ul><li>If has mil is 6:</li><ul><li>random list:</li><ul><li>5:</li><ul><li>the event ˻orc_flavor.2˼ happens</li></ul><li>95:</li><ul><li>the event ˻orc_flavor.3˼ happens</li></ul></ul></ul></ul></ul>
Outcome 2:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>add stability or adm power = yes</li><li>increase ruler dip effect = yes</li></ul>

___
##[Root.Monarch.GetSheHeCap] will defend [Root.Monarch.GetHerHis] honor and title!

###AI weighting:
AI weights this option at 70
 - Multiplied by 0.5 if has ruler has personality is intricate web weaver personality, and has ruler has personality is charismatic negotiator personality, and has full idea group is diplomatic ideas, and has full idea group is spy ideas, and has dip is 5


###Efects:<ul><li>custom tooltip = lets_fight_tooltip</li><li>hidden effect:</li><ul><li>If does not have mil is 1:</li><ul><li>random list:</li><ul><li>90:</li><ul><li>the event ˻orc_flavor.2˼ happens</li></ul><li>10:</li><ul><li>the event ˻orc_flavor.3˼ happens</li></ul></ul></ul><li>If has mil is 1, and does not have mil is 2:</li><ul><li>random list:</li><ul><li>75:</li><ul><li>the event ˻orc_flavor.2˼ happens</li></ul><li>25:</li><ul><li>the event ˻orc_flavor.3˼ happens</li></ul></ul></ul><li>If has mil is 2, and does not have mil is 3:</li><ul><li>random list:</li><ul><li>66:</li><ul><li>the event ˻orc_flavor.2˼ happens</li></ul><li>33:</li><ul><li>the event ˻orc_flavor.3˼ happens</li></ul></ul></ul><li>If has mil is 3, and does not have mil is 4:</li><ul><li>random list:</li><ul><li>50:</li><ul><li>the event ˻orc_flavor.2˼ happens</li></ul><li>50:</li><ul><li>the event ˻orc_flavor.3˼ happens</li></ul></ul></ul><li>If has mil is 4, and does not have mil is 5:</li><ul><li>random list:</li><ul><li>33:</li><ul><li>the event ˻orc_flavor.2˼ happens</li></ul><li>66:</li><ul><li>the event ˻orc_flavor.3˼ happens</li></ul></ul></ul><li>If has mil is 5, and does not have mil is 6:</li><ul><li>random list:</li><ul><li>25:</li><ul><li>the event ˻orc_flavor.2˼ happens</li></ul><li>75:</li><ul><li>the event ˻orc_flavor.3˼ happens</li></ul></ul></ul><li>If has mil is 6:</li><ul><li>random list:</li><ul><li>10:</li><ul><li>the event ˻orc_flavor.2˼ happens</li></ul><li>90:</li><ul><li>the event ˻orc_flavor.3˼ happens</li></ul></ul></ul></ul></ul>
