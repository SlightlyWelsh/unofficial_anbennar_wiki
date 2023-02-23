#Information
 - Title: [Root.Monarch.GetName] Lost!
 - ID: magic_duel.6
#Description
[Root.Monarch.GetName] Lost!
#Options

___
##Terrible!

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>If has country flag is [blackpurgis_happening](../flags/blackpurgis_happening.md), and has overlord has country flag is [blackpurgis_happening](../flags/blackpurgis_happening.md):</li><ul><li>hidden effect:</li><ul><li>change variable:</li><ul><li>currentBlack = 1</li></ul><li>change variable:</li><ul><li>loseBlack = 1</li></ul></ul><li>add ruler modifier:</li><ul><li>name = recent_blackpurgis_duel</li><li>duration = 180</li></ul><li>If has event target:attacker has tag is Z99; and does not have tag is Z99:</li><ul><li>add liberty desire = -5</li><li>decrease acolyte influence 5 = yes</li></ul><li>Else if is subject of type is acolyte dominion:</li><ul><li>decrease acolyte influence 10 = yes</li></ul><li>add prestige = -5</li><li>update blackpurgis = yes</li></ul><li>Else if has country flag is [tluukt_the_challenge](../flags/tluukt_the_challenge.md):</li><ul><li>hidden effect:</li><ul><li>set country flag [tluukt_challenge_lost](../flags/tluukt_challenge_lost.md)</li></ul><li>the event [The Spoils](../events/the_spoils.md) happens</li></ul><li>Else if has country flag is [tluukt_vs_carodir](../flags/tluukt_vs_carodir.md):</li><ul><li>clr country flag [tluukt_vs_carodir](../flags/tluukt_vs_carodir.md)</li><li>add prestige = -10</li><li>If has tag is F42:</li><ul><li>kill ruler = yes</li><li>capital scope:</li><ul><li>change controller = F28</li><li>If every neighbor province has country or non sovereign subject holds is ROOT:</li><ul><li>change controller = F28</li></ul></ul><li>tooltip:</li><ul><li>F28:</li><ul><li>add ruler modifier:</li><ul><li>name = tluukt_wins_carodir</li><li>duration = 1825</li></ul></ul></ul></ul><li>Else if has tag is F28:</li><ul><li>kill ruler = yes</li><li>country gets the modifier tluukt_loses_carodir for 5 years</li><li>tooltip:</li><ul><li>F42:</li><ul><li>capital scope:</li><ul><li>change controller = F42</li><li>kill units:</li><ul><li>who = ROOT</li><li>type = infantry</li><li>amount = 5</li></ul><li>If every neighbor province has controlled by is ROOT, and  has country or non sovereign subject holds is F42:</li><ul><li>change controller = F42</li></ul></ul></ul></ul></ul></ul><li>else:</li><ul><li>add prestige = -10</li></ul></ul>
