#Information
 - Title: [Root.Monarch.GetName]'s Ascension
 - ID: flavor_malacnar.4
#Description
[Root.Monarch.GetName]'s Ascension
#Options

___
##Bojna Zovech Malacnar

###Available if:
<li>is not female</li><li>None of the following:</li><ul><li>primary culture is malacnari</li></ul>

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>hidden effect:</li><ul><li>remove country modifier = g32_battleking_grace_period</li></ul><li>If is not controlled by the AI:</li><ul><li>add ruler modifier:</li><ul><li>name = g32_battleking_grace_period</li><li>duration = 912</li><li>hidden = yes</li></ul></ul><li>else:</li><ul><li>add ruler modifier:</li><ul><li>name = g32_battleking_grace_period</li><li>duration = 3650</li><li>hidden = yes</li></ul></ul><li>add ruler modifier:</li><ul><li>name = g32_untested_battleking</li></ul><li>hidden effect:</li><ul><li>set ai personality:</li><ul><li>personality = ai_militarist</li><li>locked = no</li></ul></ul><li>custom tooltip = malacnar_battleking_rep_tooltip</li></ul>

___
##Botka Zovigni Malacnar

###Available if:
<li>is not female</li><li>primary culture is malacnari</li>

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>hidden effect:</li><ul><li>remove country modifier = g32_battleking_grace_period</li></ul><li>If is not controlled by the AI:</li><ul><li>add ruler modifier:</li><ul><li>name = g32_battleking_grace_period</li><li>duration = 912</li><li>hidden = yes</li></ul></ul><li>else:</li><ul><li>add ruler modifier:</li><ul><li>name = g32_battleking_grace_period</li><li>duration = 3650</li><li>hidden = yes</li></ul></ul><li>add ruler modifier:</li><ul><li>name = g32_untested_battleking</li></ul><li>hidden effect:</li><ul><li>set ai personality:</li><ul><li>personality = ai_militarist</li><li>locked = no</li></ul></ul><li>custom tooltip = malacnar_battleking_rep_tooltip</li></ul>

___
##[Root.Monarch.GetName] will prove [Root.Monarch.GetHerHim]self to be on par with the Battlekings of old

###Available if:
<li>is female</li><li>Any of the following:</li><ul><li>has country modifier g32_legacy_battlequeen</li><li>stability is at least 1</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>hidden effect:</li><ul><li>remove country modifier = g32_battleking_grace_period</li></ul><li>add ruler modifier:</li><ul><li>name = g32_battlequeen</li><li>hidden = yes</li></ul><li>set country flag [g32_past_queen](../flags/g32_past_queen.md)</li><li>If is not controlled by the AI:</li><ul><li>add ruler modifier:</li><ul><li>name = g32_battleking_grace_period</li><li>duration = 600</li><li>hidden = yes</li></ul></ul><li>else:</li><ul><li>add ruler modifier:</li><ul><li>name = g32_battleking_grace_period</li><li>duration = 1825</li><li>hidden = yes</li></ul></ul><li>add ruler modifier:</li><ul><li>name = g32_untested_battleking</li></ul><li>hidden effect:</li><ul><li>set ai personality:</li><ul><li>personality = ai_militarist</li><li>locked = no</li></ul></ul><li>custom tooltip = malacnar_battleking_rep_tooltip</li></ul>

___
##No woman can be Battleking

###Available if:
<li>is female</li><li>None of the following:</li><ul><li>has country modifier g32_legacy_battlequeen</li></ul>

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>hidden effect:</li><ul><li>remove country modifier = g32_battleking_grace_period</li></ul><li>If random province has area is malacnar area:</li><ul><li>spawn rebels:</li><ul><li>type = pretender_rebels</li><li>size = 2</li></ul></ul><li>add ruler modifier:</li><ul><li>name = g32_battlequeen</li><li>hidden = yes</li></ul><li>set country flag [g32_past_queen](../flags/g32_past_queen.md)</li><li>If is not controlled by the AI:</li><ul><li>add ruler modifier:</li><ul><li>name = g32_battleking_grace_period</li><li>duration = 600</li><li>hidden = yes</li></ul></ul><li>else:</li><ul><li>add ruler modifier:</li><ul><li>name = g32_battleking_grace_period</li><li>duration = 1825</li><li>hidden = yes</li></ul></ul><li>add ruler modifier:</li><ul><li>name = g32_untested_battleking</li></ul><li>hidden effect:</li><ul><li>set ai personality:</li><ul><li>personality = ai_militarist</li><li>locked = no</li></ul></ul><li>custom tooltip = malacnar_battleking_rep_tooltip</li></ul>
