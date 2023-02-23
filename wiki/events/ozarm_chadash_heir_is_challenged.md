#Information
 - Title: Ozarm'Chadash - Heir is challenged
 - ID: orc_flavor.4
#Description
Ozarm'Chadash - Heir is challenged
#Mean Time to Happen:
Base time = 600 months
 - Multiplied by 0.9 if does not have stability is 0
 - Multiplied by 0.8 if does not have stability is -1
 - Multiplied by 0.8 if does not have stability is -2
 - Multiplied by 0.8 if does not have heir mil is 3
 - Multiplied by 0.8 if does not have heir mil is 2
 - Multiplied by 0.5 if does not have heir mil is 1
 - Multiplied by 0.8 if does not have prestige is -25
 - Multiplied by 0.8 if does not have prestige is -50
 - Multiplied by 0.8 if does not have prestige is -75
 - Multiplied by 0.5 if does not have legitimacy is 50
 - Multiplied by 0.9 if has reform is orcish kingdom reform
 - Multiplied by 0.8 if has full idea group is aristocracy ideas
 - Multiplied by 1.25 if is year is 1600
 - Multiplied by 1.25 if is year is 1700
 - Multiplied by 1.25 if has heir mil is 4
 - Multiplied by 1.25 if has heir mil is 5
 - Multiplied by 1.5 if has heir mil is 6
 - Multiplied by 2 if has full idea group is innovativeness ideas
 - Multiplied by 2 if has full idea group is administrative ideas
 - Multiplied by 2 if has full idea group is diplomatic ideas
 - Multiplied by 2 if has full idea group is spy ideas
 - Multiplied by 2 if does not have religion group is orcish
 - Multiplied by 2 if has tag is Z50
 - Multiplied by 2 if has government is monarchy
 - Multiplied by 2.5 if has ruler modifier is ozarm chadash without fight
 - Multiplied by 2.5 if has ruler modifier is ozarm chadash outraged by dishonor
 - Multiplied by 5 if has ruler flag is [orc_winner_of_ozarmchadash](../flags/orc_winner_of_ozarmchadash.md)

#Options

___
##Stop, you fools!

###AI weighting:
AI weights this option at 10


###Efects:<ul><li>If has government is tribal:</li><ul><li>add prestige = -10</li><li>reduce stability or adm power = yes</li><li>add estate loyalty:</li><ul><li>estate = estate_monstrous_tribes</li><li>loyalty = -15</li></ul></ul><li>add ruler modifier:</li><ul><li>name = orc_stopped_heir_duel</li><li>duration = 1825</li></ul></ul>

___
##Orcs must fight to prove themselves worthy.

###AI weighting:
AI weights this option at 70


###Efects:<ul><li>custom tooltip = orc_heir_duel_tooltip</li><li>hidden effect:</li><ul><li>If does not have heir mil is 1:</li><ul><li>random list:</li><ul><li>90:</li><ul><li>the event [Heir Lost!](../events/heir_lost.md) happens</li></ul><li>10:</li><ul><li>the event [Heir Won!](../events/heir_won.md) happens</li></ul></ul></ul><li>If has heir mil is 1, and does not have heir mil is 2:</li><ul><li>random list:</li><ul><li>75:</li><ul><li>the event [Heir Lost!](../events/heir_lost.md) happens</li></ul><li>25:</li><ul><li>the event [Heir Won!](../events/heir_won.md) happens</li></ul></ul></ul><li>If has heir mil is 2, and does not have heir mil is 3:</li><ul><li>random list:</li><ul><li>66:</li><ul><li>the event [Heir Lost!](../events/heir_lost.md) happens</li></ul><li>33:</li><ul><li>the event [Heir Won!](../events/heir_won.md) happens</li></ul></ul></ul><li>If has heir mil is 3, and does not have heir mil is 4:</li><ul><li>random list:</li><ul><li>50:</li><ul><li>the event [Heir Lost!](../events/heir_lost.md) happens</li></ul><li>50:</li><ul><li>the event [Heir Won!](../events/heir_won.md) happens</li></ul></ul></ul><li>If has heir mil is 4, and does not have heir mil is 5:</li><ul><li>random list:</li><ul><li>33:</li><ul><li>the event [Heir Lost!](../events/heir_lost.md) happens</li></ul><li>66:</li><ul><li>the event [Heir Won!](../events/heir_won.md) happens</li></ul></ul></ul><li>If has heir mil is 5, and does not have heir mil is 6:</li><ul><li>random list:</li><ul><li>25:</li><ul><li>the event [Heir Lost!](../events/heir_lost.md) happens</li></ul><li>75:</li><ul><li>the event [Heir Won!](../events/heir_won.md) happens</li></ul></ul></ul><li>If has heir mil is 6:</li><ul><li>random list:</li><ul><li>95:</li><ul><li>the event [Heir Won!](../events/heir_won.md) happens</li></ul><li>5:</li><ul><li>the event [Heir Lost!](../events/heir_lost.md) happens</li></ul></ul></ul></ul></ul>

___
##We can try to settle it peacefully... more or less.

###Available if:
<li>Any of the following:</li><ul><li>ruler has personality is intricate_web_weaver_personality</li><li>ruler has personality  is charismatic_negotiator_personality</li><li>full idea group is diplomatic_ideas</li><li>full idea group  is spy_ideas</li><li>dip is at least 5</li></ul>

###AI weighting:
AI weights this option at 60


###One of the following randomly happens:
Outcome 1:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>add prestige = -10</li><li>reduce stability or adm power = yes</li><li>add ruler modifier:</li><ul><li>name = ozarm_chadash_outraged_by_dishonor</li><li>duration = 1825</li></ul><li>custom tooltip = orc_heir_duel_tooltip</li><li>hidden effect:</li><ul><li>If does not have heir mil is 1:</li><ul><li>random list:</li><ul><li>90:</li><ul><li>the event [Heir Lost!](../events/heir_lost.md) happens</li></ul><li>10:</li><ul><li>the event [Heir Won!](../events/heir_won.md) happens</li></ul></ul></ul><li>If has heir mil is 1, and does not have heir mil is 2:</li><ul><li>random list:</li><ul><li>75:</li><ul><li>the event [Heir Lost!](../events/heir_lost.md) happens</li></ul><li>25:</li><ul><li>the event [Heir Won!](../events/heir_won.md) happens</li></ul></ul></ul><li>If has heir mil is 2, and does not have heir mil is 3:</li><ul><li>random list:</li><ul><li>66:</li><ul><li>the event [Heir Lost!](../events/heir_lost.md) happens</li></ul><li>33:</li><ul><li>the event [Heir Won!](../events/heir_won.md) happens</li></ul></ul></ul><li>If has heir mil is 3, and does not have heir mil is 4:</li><ul><li>random list:</li><ul><li>50:</li><ul><li>the event [Heir Lost!](../events/heir_lost.md) happens</li></ul><li>50:</li><ul><li>the event [Heir Won!](../events/heir_won.md) happens</li></ul></ul></ul><li>If has heir mil is 4, and does not have heir mil is 5:</li><ul><li>random list:</li><ul><li>33:</li><ul><li>the event [Heir Lost!](../events/heir_lost.md) happens</li></ul><li>66:</li><ul><li>the event [Heir Won!](../events/heir_won.md) happens</li></ul></ul></ul><li>If has heir mil is 5, and does not have heir mil is 6:</li><ul><li>random list:</li><ul><li>25:</li><ul><li>the event [Heir Lost!](../events/heir_lost.md) happens</li></ul><li>75:</li><ul><li>the event [Heir Won!](../events/heir_won.md) happens</li></ul></ul></ul><li>If has heir mil is 6:</li><ul><li>random list:</li><ul><li>95:</li><ul><li>the event [Heir Won!](../events/heir_won.md) happens</li></ul><li>5:</li><ul><li>the event [Heir Lost!](../events/heir_lost.md) happens</li></ul></ul></ul></ul></ul>
Outcome 2:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>add stability or adm power = yes</li><li>increase ruler dip effect = yes</li></ul>

___
##I never liked [Root.Heir.GetHerHim] anyway.

###AI weighting:
AI weights this option at 10


###Efects:<ul><li>If has government is tribal:</li><ul><li>add prestige = -20</li><li>reduce stability or adm power = yes</li><li>kill heir:</li><ul><li>allow new heir = no</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_monstrous_tribes</li><li>loyalty = 15</li></ul><li>define heir:</li><ul><li>change adm = 0</li><li>change dip = 0</li><li>change mil = 1</li><li>claim = 90</li><li>age = 15</li></ul></ul></ul>
