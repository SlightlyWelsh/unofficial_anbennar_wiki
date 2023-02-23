#Information
 - Title: The Decision of the Council
 - ID: flavor_gawed.5
#Description
The Decision of the Council
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Fantastic!

###Available if:
<li>has country flag [council_support_ruler](../flags/council_support_ruler.md)</li>

###AI weighting:
AI weights this option at 3


###Efects:<ul><li>add ruler modifier:</li><ul><li>name = magnate_council_support</li><li>duration = -1</li></ul></ul>

___
##I do not need their help.

###Available if:
<li>has country flag [council_support_ruler](../flags/council_support_ruler.md)</li>

###AI weighting:
AI weights this option at 3


###Efects:<ul><li>add prestige = 10</li><li>add ruler modifier:</li><ul><li>name = magnate_council_rejected</li><li>duration = -1</li></ul></ul>

___
##Damnation!

###Available if:
<li>has country flag [council_oppose_ruler](../flags/council_oppose_ruler.md)</li>

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>add ruler modifier:</li><ul><li>name = magnate_council_opposition</li><li>duration = -1</li></ul></ul>

___
##Perhaps we could persuade them to change their minds...

###Available if:
<li>has country flag [council_oppose_ruler](../flags/council_oppose_ruler.md)</li>

###AI weighting:
AI weights this option at 3


###Efects:<ul><li>If is not controlled by the AI:</li><ul><li>change estate land share:</li><ul><li>estate = estate_burghers</li><li>share = 5</li></ul></ul><li>add years of income = -0.25</li><li>add ruler modifier:</li><ul><li>name = magnate_council_support</li><li>duration = -1</li></ul></ul>
