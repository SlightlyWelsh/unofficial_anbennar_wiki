#Information
 - Title: Unification of the Federation
 - ID: lake.27
#Description
Unification of the Federation
#Options

___
##We move forward as one!

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>hidden effect:</li><ul><li>export to variable:</li><ul><li>which = treasuryAvailable</li><li>value = treasury</li><li>who = ROOT</li></ul><li>export to variable:</li><ul><li>which = manpowerAvailable</li><li>value = manpower</li><li>who = ROOT</li></ul><li>currency effect:</li><ul><li>currency = treasury</li><li>takeFrom = ROOT</li><li>addTo = J33</li><li>which = treasuryAvailable</li></ul><li>currency effect:</li><ul><li>currency = manpower</li><li>takeFrom = ROOT</li><li>addTo = J33</li><li>which = manpowerAvailable</li></ul></ul><li>J33:</li><ul><li>inherit = ROOT</li><li>hidden effect:</li><ul><li>change estate land share:</li><ul><li>estate = all</li><li>share = -10</li></ul></ul></ul></ul>

___
##We will not recognize their so-called 'unification'

###Available if:
<li>is lake federation leader is no</li>

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>remove country modifier = lake_federation_member</li><li>every owned province:</li><ul><li>add permanent claim = J33</li></ul><li>swap non generic missions = yes</li></ul>
