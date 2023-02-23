#Information
 - Title: Tales of Battle
 - ID: centaur_tournament.4
#Description
Tales of Battle
#Options

___
##[Root.Monarch.GetName] emerges victorious!

###Available if:
<li>has country flag [win_round](../flags/win_round.md)</li><li>None of the following:</li><ul><li>has country flag [last_round](../flags/last_round.md)</li></ul>

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>trigger switch:</li><ul><li>on trigger = has_country_flag</li><li>grandiose tournament:</li><ul><li>add prestige = 5</li><li>random list:</li><ul><li>33:</li><ul><li>add mil power = 10</li></ul><li>33:</li><ul><li>add adm power = 10</li></ul><li>33:</li><ul><li>add dip power = 10</li></ul></ul></ul><li>big tournament:</li><ul><li>add prestige = 5</li></ul><li>normal tournament:</li><ul><li>add prestige = 2</li></ul></ul><li>hidden effect:</li><ul><li>clr country flag [win_round](../flags/win_round.md)</li><li>trigger switch:</li><ul><li>on trigger = has_country_flag</li><li>second round:</li><ul><li>clr country flag [second_round](../flags/second_round.md)</li><li>set country flag [last_round](../flags/last_round.md)</li></ul><li>first round:</li><ul><li>clr country flag [first_round](../flags/first_round.md)</li><li>set country flag [second_round](../flags/second_round.md)</li></ul></ul></ul><li>If has num of generals is 1:</li><ul><li>hidden effect:</li><ul><li>the event ˻centaur_tournament.102˼ happens</li></ul><li>tooltip:</li><ul><li>random:</li><ul><li>chance = 50</li><li>kill leader:</li><ul><li>type = random</li></ul></ul></ul></ul><li>the event ˻centaur_tournament.3˼ happens</li></ul>

___
##[Root.Monarch.GetName] emerges defeated!

###Available if:
<li>has country flag [lost_round](../flags/lost_round.md)</li>

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>hidden effect:</li><ul><li>clr country flag [first_round](../flags/first_round.md)</li><li>clr country flag [second_round](../flags/second_round.md)</li><li>clr country flag [last_round](../flags/last_round.md)</li><li>clr country flag [normal_tournament](../flags/normal_tournament.md)</li><li>clr country flag [big_tournament](../flags/big_tournament.md)</li><li>clr country flag [grandiose_tournament](../flags/grandiose_tournament.md)</li><li>clr country flag [lost_round](../flags/lost_round.md)</li></ul><li>hidden effect:</li><ul><li>the event ˻centaur_tournament.101˼ happens</li></ul><li>tooltip:</li><ul><li>random:</li><ul><li>chance = 50</li><li>kill ruler = yes</li></ul></ul><li>If has check variable has centaur zeal is 0:</li><ul><li>custom tooltip = centaur_zeal_minus_5_tooltip</li><li>hidden effect:</li><ul><li>subtract variable:</li><ul><li>centaur zeal = 5</li></ul></ul></ul></ul>

___
##[Root.Monarch.GetName] has won the tournament!

###Available if:
<li>has country flag [win_round](../flags/win_round.md)</li><li>has country flag  last_round</li>

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>trigger switch:</li><ul><li>on trigger = has_country_flag</li><li>grandiose tournament:</li><ul><li>add prestige = 5</li><li>random list:</li><ul><li>33:</li><ul><li>add mil power = 10</li></ul><li>33:</li><ul><li>add adm power = 10</li></ul><li>33:</li><ul><li>add dip power = 10</li></ul></ul></ul><li>big tournament:</li><ul><li>add prestige = 5</li></ul><li>normal tournament:</li><ul><li>add prestige = 2</li></ul></ul><li>hidden effect:</li><ul><li>the event ˻centaur_tournament.102˼ happens</li></ul><li>tooltip:</li><ul><li>random:</li><ul><li>chance = 50</li><li>kill leader:</li><ul><li>type = random</li></ul></ul></ul><li>the event ˻centaur_tournament.5˼ happens</li></ul>
