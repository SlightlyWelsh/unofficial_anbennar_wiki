#Information
 - Title: Siring an Heir
 - ID: vampire_ruler.7
#Description
Siring an Heir
#Mean Time to Happen:
Base time = 30 years
 - Multiplied by 0.75 if has ruler age is 100
 - Multiplied by 0.5 if has country flag is [exposed_vampire_ruler](../flags/exposed_vampire_ruler.md)

#Options

___
##They shall succeed me

###Available if:
<li>None of the following:</li><ul><li>has country flag [vampire_heir](../flags/vampire_heir.md)</li></ul><li>has government attribute heir</li>

###AI weighting:
AI weights this option at 10


###Efects:<ul><li>custom tooltip = add_vampire_heir</li><li>set country flag [vampire_heir](../flags/vampire_heir.md)</li></ul>

___
##They shall serve me as an advisor

###AI weighting:
AI weights this option at 10


###Efects:<ul><li>define advisor:</li><ul><li>type = treasurer</li><li>skill = 3</li><li>cost multiplier = 0.25</li></ul></ul>

___
##They shall lead our armies

###AI weighting:
AI weights this option at 10


###Efects:<ul><li>define general:</li><ul><li>fire = 4</li><li>shock = 6</li><li>manuever = 2</li><li>siege = 4</li></ul></ul>

___
##This would draw attentions

###AI weighting:
AI weights this option at 5


###Efects:<ul><li>facade suspicion decrease 1 = yes</li><li>hidden effect:</li><ul><li>remove country modifier = sired_heir</li></ul></ul>
