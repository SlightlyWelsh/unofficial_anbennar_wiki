#Information
 - Title: [Root.Monarch.GetName] Triumphs!
 - ID: magic_duel.4
#Description
[Root.Monarch.GetName] Triumphs!
#Options

___
##Glory to the victor!

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>If has country flag is [blackpurgis_happening](../flags/blackpurgis_happening.md), and has overlord has country flag is [blackpurgis_happening](../flags/blackpurgis_happening.md):</li><ul><li>hidden effect:</li><ul><li>change variable:</li><ul><li>currentBlack = 1</li></ul><li>change variable:</li><ul><li>winBlack = 1</li></ul></ul><li>add ruler modifier:</li><ul><li>name = recent_blackpurgis_duel</li><li>duration = 90</li></ul><li>If has event target:attacker has tag is Z99; and does not have tag is Z99:</li><ul><li>add liberty desire = 15</li><li>increase acolyte influence 15 = yes</li></ul><li>Else if is subject of type is acolyte dominion:</li><ul><li>increase acolyte influence 5 = yes</li></ul><li>add prestige excess to splendour effect:</li><ul><li>VAL = 3</li></ul><li>update blackpurgis = yes</li></ul><li>Else if has country flag is [tluukt_the_challenge](../flags/tluukt_the_challenge.md):</li><ul><li>hidden effect:</li><ul><li>set country flag [tluukt_challenge_won](../flags/tluukt_challenge_won.md)</li></ul><li>the event ˻flavour_tluukt.55˼ happens</li></ul><li>Else if has country flag is [tluukt_vs_carodir](../flags/tluukt_vs_carodir.md):</li><ul><li>clr country flag [tluukt_vs_carodir](../flags/tluukt_vs_carodir.md)</li><li>add prestige excess to splendour effect:</li><ul><li>VAL = 10</li></ul><li>If has tag is F28:</li><ul><li>add ruler modifier:</li><ul><li>name = tluukt_wins_carodir</li><li>duration = 1825</li></ul><li>tooltip:</li><ul><li>F42:</li><ul><li>kill ruler = yes</li><li>capital scope:</li><ul><li>change controller = ROOT</li><li>If every neighbor province has country or non sovereign subject holds is F42:</li><ul><li>change controller = ROOT</li></ul></ul></ul></ul></ul><li>Else if has tag is F42:</li><ul><li>capital scope:</li><ul><li>change controller = ROOT</li><li>kill units:</li><ul><li>who = F28</li><li>type = infantry</li><li>amount = 5</li></ul><li>If every neighbor province has controlled by is F28, and  has country or non sovereign subject holds is F42:</li><ul><li>change controller = ROOT</li></ul></ul><li>tooltip:</li><ul><li>F28:</li><ul><li>kill ruler = yes</li><li>country gets the modifier tluukt_loses_carodir for 5 years</li></ul></ul></ul></ul><li>else:</li><ul><li>add prestige excess to splendour effect:</li><ul><li>VAL = 10</li></ul></ul></ul>
