This page has the same name as others. For full listing see bottom of [the base page](election_in_the_root.md).

#Information
 - Title: Election in the [Root.GovernmentName]
 - ID: elections.800
#Description
Election in the [Root.GovernmentName]
#Options

___
##Have [lottery_candidate_a_@ROOT.GetName] elected.

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>set ruler = lottery_candidate_a_@ROOT</li><li>add republican tradition = -25</li><li>If has faction is mr guilds:</li><ul><li>add faction influence:</li><ul><li>faction = mr_guilds</li><li>influence = 20</li></ul></ul><li>custom tooltip = lottery_candidate_bonus_one</li><li>If has government attribute is bonus stats for elected ruler:</li><ul><li>custom tooltip = bonus_stats_for_elected_ruler_tt</li></ul><li>If has government attribute is elections influence estates:</li><ul><li>add estate loyalty by class adm:</li><ul><li>loyalty = 10</li></ul></ul></ul>

___
##Have [lottery_candidate_b_@ROOT.GetName] elected.

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>set ruler = lottery_candidate_b_@ROOT</li><li>add republican tradition = -25</li><li>If has faction is mr traders:</li><ul><li>add faction influence:</li><ul><li>faction = mr_traders</li><li>influence = 20</li></ul></ul><li>custom tooltip = lottery_candidate_bonus_one</li><li>If has government attribute is bonus stats for elected ruler:</li><ul><li>custom tooltip = bonus_stats_for_elected_ruler_tt</li></ul><li>If has government attribute is elections influence estates:</li><ul><li>add estate loyalty by class dip:</li><ul><li>loyalty = 10</li></ul></ul></ul>

___
##Have [lottery_candidate_c_@ROOT.GetName] elected.

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>set ruler = lottery_candidate_c_@ROOT</li><li>add republican tradition = -25</li><li>If has faction is mr aristocrats:</li><ul><li>add faction influence:</li><ul><li>faction = mr_aristocrats</li><li>influence = 20</li></ul></ul><li>custom tooltip = lottery_candidate_bonus_one</li><li>If has government attribute is bonus stats for elected ruler:</li><ul><li>custom tooltip = bonus_stats_for_elected_ruler_tt</li></ul><li>If has government attribute is elections influence estates:</li><ul><li>add estate loyalty by class mil:</li><ul><li>loyalty = 10</li></ul></ul></ul>

___
##Let the Lottery decide.

###AI weighting:
AI weights this option at 90


###One of the following randomly happens:
Outcome 1:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>set ruler = lottery_candidate_a_@ROOT</li><li>If has faction is mr guilds:</li><ul><li>add faction influence:</li><ul><li>faction = mr_guilds</li><li>influence = 20</li></ul></ul><li>If has faction is rr jacobins:</li><ul><li>add faction influence:</li><ul><li>faction = rr_jacobins</li><li>influence = 20</li></ul></ul><li>If has government attribute is elections influence estates:</li><ul><li>add estate loyalty by class adm:</li><ul><li>loyalty = 10</li></ul></ul></ul>
Outcome 2:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>set ruler = lottery_candidate_b_@ROOT</li><li>If has faction is mr traders:</li><ul><li>add faction influence:</li><ul><li>faction = mr_traders</li><li>influence = 20</li></ul></ul><li>If has faction is rr royalists:</li><ul><li>add faction influence:</li><ul><li>faction = rr_royalists</li><li>influence = 20</li></ul></ul><li>If has government attribute is elections influence estates:</li><ul><li>add estate loyalty by class dip:</li><ul><li>loyalty = 10</li></ul></ul></ul>
Outcome 3:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>set ruler = lottery_candidate_c_@ROOT</li><li>If has faction is mr aristocrats:</li><ul><li>add faction influence:</li><ul><li>faction = mr_aristocrats</li><li>influence = 20</li></ul></ul><li>If has faction is rr girondists:</li><ul><li>add faction influence:</li><ul><li>faction = rr_girondists</li><li>influence = 20</li></ul></ul><li>If has government attribute is elections influence estates:</li><ul><li>add estate loyalty by class mil:</li><ul><li>loyalty = 10</li></ul></ul></ul>

###Efects:<ul><li>custom tooltip = lottery_candidate_bonus_plural</li><li>If has government attribute is bonus stats for elected ruler:</li><ul><li>custom tooltip = bonus_stats_for_elected_ruler_tt</li></ul></ul>

___
##Elect the beloved relative of [Root.Monarch.GetName].

###Available if:
<li>has government attribute enables_nepotism</li>

###AI weighting:
AI weights this option at 10


###Efects:<ul><li>If has country flag is [strengthened_signoria_flag](../flags/strengthened_signoria_flag.md):</li><ul><li>custom tooltip = strengthened_signoria_election_tt</li><li>clr country flag [strengthened_signoria_flag](../flags/strengthened_signoria_flag.md)</li></ul><li>else:</li><ul><li>add republican tradition = -15</li></ul><li>If has country modifier is harpy administration, and does not have reform is signoria reform:</li><ul><li>define ruler:</li><ul><li>min age = 30</li><li>max age = 50</li><li>change mil = -1</li><li>change adm = -1</li><li>change dip = -1</li><li>name = "lastname"</li><li>female = yes</li></ul></ul><li>Else if has republic with female rulers trigger is yes, and does not have reform is signoria reform:</li><ul><li>define ruler:</li><ul><li>min age = 30</li><li>max age = 50</li><li>change mil = -1</li><li>change adm = -1</li><li>change dip = -1</li><li>name = "lastname"</li><li>random gender = yes</li></ul></ul><li>Else if has country modifier is harpy administration, and  has reform is signoria reform:</li><ul><li>define ruler:</li><ul><li>min age = 30</li><li>max age = 50</li><li>name = "lastname"</li><li>female = yes</li></ul></ul><li>Else if has republic with female rulers trigger is yes, and  has reform is signoria reform:</li><ul><li>define ruler:</li><ul><li>min age = 30</li><li>max age = 50</li><li>name = "lastname"</li><li>random gender = yes</li></ul></ul><li>Else if does not have republic with female rulers trigger is yes; and  has reform is signoria reform:</li><ul><li>define ruler:</li><ul><li>min age = 30</li><li>max age = 50</li><li>name = "lastname"</li></ul></ul><li>else:</li><ul><li>define ruler:</li><ul><li>min age = 30</li><li>max age = 50</li><li>change mil = -1</li><li>change adm = -1</li><li>change dip = -1</li><li>name = "lastname"</li></ul></ul><li>If has faction is mr aristocrats:</li><ul><li>add faction influence:</li><ul><li>faction = mr_aristocrats</li><li>influence = 10</li></ul></ul><li>If has government attribute is elections influence estates:</li><ul><li>add estate loyalty:</li><ul><li>estate = all</li><li>loyalty = 10</li></ul></ul><li>If has government attribute is bonus stats for elected ruler:</li><ul><li>custom tooltip = bonus_stats_for_elected_ruler_tt</li></ul></ul>
