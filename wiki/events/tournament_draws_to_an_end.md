#Information
 - Title: Tournament Draws To An End
 - ID: flavor_nuugdan_tsarai.70
#Description
Tournament Draws To An End
#Options

___
##[From.GetRulerTitleAndNameOrRegencyCap] of [From.GetName]!

###Available if:
<li>has global flag [Y91_tournament_won_by_ruler](../flags/y91_tournament_won_by_ruler.md)</li>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>If has event target:Y91 tournament winner has tag is ROOT:</li><ul><li>add prestige = 20</li><li>add legitimacy = 20</li><li>add years of income = 0.5</li><li>add army tradition = 5</li><li>add yearly manpower = 0.5</li><li>If does not have mil is 6:</li><ul><li>change mil = 1</li></ul><li>else:</li><ul><li>add mil power = 50</li></ul></ul><li>If has event target:Y91 tournament winner has tag is ROOT, and event target:Y91 tournament winner has country modifier is Y91 propaganda reform modifier:</li><ul><li>event target:Y91 tournament winner:</li><ul><li>the event ˻flavor_nuugdan_tsarai.80˼ happens</li></ul></ul><li>If has country flag is [Y91_ruler_participating](../flags/y91_ruler_participating.md), and does not have event target:Y91 tournament winner has tag is ROOT:</li><ul><li>random list:</li><ul><li>5:</li><ul><li>kill ruler = yes</li></ul><li>95:</li><ul></ul></ul></ul><li>If has country flag is [Y91_heir_participating](../flags/y91_heir_participating.md), and does not have event target:Y91 tournament winner has tag is ROOT:</li><ul><li>random list:</li><ul><li>5:</li><ul><li>kill heir:</li><ul></ul></ul><li>95:</li><ul></ul></ul></ul></ul>

___
##[From.Heir.GetName] of [From.GetName]!

###Available if:
<li>has global flag [Y91_tournament_won_by_heir](../flags/y91_tournament_won_by_heir.md)</li>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>If has event target:Y91 tournament winner has tag is ROOT:</li><ul><li>add prestige = 10</li><li>add legitimacy = 5</li><li>add heir claim = 50</li><li>add years of income = 0.25</li><li>add army tradition = 2.5</li><li>add manpower = 1</li><li>If does not have heir mil is 6:</li><ul><li>change heir mil = 1</li></ul><li>else:</li><ul><li>add mil power = 50</li></ul></ul><li>If has event target:Y91 tournament winner has tag is ROOT, and event target:Y91 tournament winner has country modifier is Y91 propaganda reform modifier:</li><ul><li>event target:Y91 tournament winner:</li><ul><li>the event ˻flavor_nuugdan_tsarai.81˼ happens</li></ul></ul><li>If has country flag is [Y91_ruler_participating](../flags/y91_ruler_participating.md), and does not have event target:Y91 tournament winner has tag is ROOT:</li><ul><li>random list:</li><ul><li>5:</li><ul><li>kill ruler = yes</li></ul><li>95:</li><ul></ul></ul></ul><li>If has country flag is [Y91_heir_participating](../flags/y91_heir_participating.md), and does not have event target:Y91 tournament winner has tag is ROOT:</li><ul><li>random list:</li><ul><li>5:</li><ul><li>kill heir:</li><ul></ul></ul><li>95:</li><ul></ul></ul></ul></ul>

___
##One of the many clan leaders

###Available if:
<li>has global flag [Y91_tournament_won_by_random_dude](../flags/y91_tournament_won_by_random_dude.md)</li>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>If has country flag is [Y91_ruler_participating](../flags/y91_ruler_participating.md):</li><ul><li>random list:</li><ul><li>5:</li><ul><li>kill ruler = yes</li></ul><li>95:</li><ul></ul></ul></ul><li>If has country flag is [Y91_heir_participating](../flags/y91_heir_participating.md):</li><ul><li>random list:</li><ul><li>5:</li><ul><li>kill heir:</li><ul></ul></ul><li>95:</li><ul></ul></ul></ul></ul>
