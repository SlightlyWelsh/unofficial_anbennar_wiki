#Information
 - Title: Hunting the Surge
 - ID: black_demesne.7
#Description
Hunting the Surge
#Options

___
##We found him!

###Available if:
<li>event target:province:</li><ul><li>has province flag [jorgurem_the_frozen](../flags/jorgurem_the_frozen.md)</li></ul>

###AI weighting:
AI weights this option at 40


###One of the following randomly happens:
Outcome 1:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>change dip = -1</li></ul>
Outcome 2:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>change mil = -1</li></ul>
Outcome 3:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>change adm = -1</li></ul>

###Efects:<ul><li>add prestige excess to splendour effect:</li><ul><li>VAL = 20</li></ul><li>event target:province:</li><ul><li>add permanent province modifier:</li><ul><li>name = jorgurem_the_frozen</li><li>duration = -1</li></ul><li>tooltip:</li><ul><li>kill units:</li><ul><li>who = ROOT</li><li>amount = 10</li></ul></ul></ul><li>hidden effect:</li><ul><li>set global flag [jorgurem_alive](../flags/jorgurem_alive.md)</li><li>If gerudia superregion has province flag is [frozen_surge](../flags/frozen_surge.md):</li><ul><li>clr province flag [frozen_surge](../flags/frozen_surge.md)</li><li>clr province flag [jorgurem_the_frozen](../flags/jorgurem_the_frozen.md)</li></ul><li>If random province has region is alenic reach region:</li><ul><li>fire province event [black_demesne.12](black_demesne.12_slug) in 265 to 100 days</li></ul></ul></ul>

___
##Curses!

###Available if:
<li>event target:province:</li><ul><li>None of the following:</li><ul><li>has province flag [jorgurem_the_frozen](../flags/jorgurem_the_frozen.md)</li></ul></ul>

###AI weighting:
AI weights this option at 40


###Efects:<ul><li>add prestige = -5</li></ul>
