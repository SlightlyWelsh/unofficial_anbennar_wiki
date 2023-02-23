#Information
 - Title: An Invitation to the Sharaajaghal Games
 - ID: ghavaanaj.100
#Description
An Invitation to the Sharaajaghal Games
#Options

___
##Anyone can represent us

###AI weighting:
AI weights this option at 2
 - Multiplied by 0 if does not have prestige is 0
 - Multiplied by 0.8 if does not have prestige is 40
 - Multiplied by 0.8 if does not have prestige is 80


###Efects:<ul><li>add prestige = -5</li><li>If has estate is estate lowercastes:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_lowercastes</li><li>loyalty = 5</li></ul></ul><li>If has estate is estate middlecastes:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_middlecastes</li><li>loyalty = 5</li></ul></ul><li>If has estate is estate uppercastes:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_uppercastes</li><li>loyalty = -10</li></ul></ul><li>If has estate is estate church:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_church</li><li>loyalty = 5</li></ul></ul><li>If has estate is estate burghers:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_burghers</li><li>loyalty = 5</li></ul></ul><li>If has estate is estate nobles:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_nobles</li><li>loyalty = -10</li></ul></ul><li>hidden effect:</li><ul><li>set country flag [sharaajaghal_games_joined](../flags/sharaajaghal_games_joined.md)</li><li>set country flag [sharaajaghal_games_anyone_can_go](../flags/sharaajaghal_games_anyone_can_go.md)</li><li>4485:</li><ul><li>change variable:</li><ul><li>which = sharaajaghal_games_participants_count</li><li>value = 1</li></ul></ul></ul></ul>

___
##Send our best athletes

###AI weighting:
AI weights this option at 1
 - Multiplied by 1.5 if has army tradition is 40
 - Multiplied by 1.2 if has army tradition is 60
 - Multiplied by 1.2 if has army tradition is 80
 - Multiplied by 1.5 if has mil power is 400


###Efects:<ul><li>add mil power = -25</li><li>add estate loyalty:</li><ul><li>estate = estate_uppercastes</li><li>loyalty = 10</li></ul><li>hidden effect:</li><ul><li>set country flag [sharaajaghal_games_joined](../flags/sharaajaghal_games_joined.md)</li><li>set country flag [sharaajaghal_games_best_athletes_sent](../flags/sharaajaghal_games_best_athletes_sent.md)</li><li>4485:</li><ul><li>change variable:</li><ul><li>which = sharaajaghal_games_participants_count</li><li>value = 1</li></ul></ul></ul></ul>

___
##I will join myself

###AI weighting:
AI weights this option at 1
 - Multiplied by 5 if has ruler culture is ghavaanaj
 - Multiplied by 0.5 if has ruler age is 30
 - Multiplied by 0.5 if has ruler age is 35
 - Multiplied by 0.5 if has ruler age is 40
 - Multiplied by 0.5 if has ruler age is 45


###Efects:<ul><li>add mil power = -10</li><li>add estate loyalty:</li><ul><li>estate = estate_uppercastes</li><li>loyalty = 5</li></ul><li>hidden effect:</li><ul><li>set country flag [sharaajaghal_games_joined](../flags/sharaajaghal_games_joined.md)</li><li>set country flag [sharaajaghal_games_best_athletes_sent](../flags/sharaajaghal_games_best_athletes_sent.md)</li><li>4485:</li><ul><li>change variable:</li><ul><li>which = sharaajaghal_games_participants_count</li><li>value = 1</li></ul></ul></ul><li>the event [What Games Shall $MONARCH$ Join](../events/what_games_shall_monarch_join.md) happens</li></ul>

___
##We won't go

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>add prestige = -5</li></ul>
