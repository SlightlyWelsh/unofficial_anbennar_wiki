#Information
 - Title: Choose Feast Target
 - ID: magic_ruler.11
#Description
Choose Feast Target
#Options

___
##Hold a Magical Feast with [magic_ally_1.GetName]

###Available if:
<li>has ruler flag [conjuration_1](../flags/conjuration_1.md)</li>

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>goto = magic_ally_1</li><li>magic casted spell = yes</li><li>add ruler modifier:</li><ul><li>name = magic_feast_cooldown</li><li>duration = 30</li><li>hidden = yes</li></ul><li>If has ruler flag is [conjuration_2](../flags/conjuration_2.md):</li><ul><li>event target:magic ally 1:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = opinion_magical_feast_greater</li><li>years = 5</li></ul></ul></ul><li>else:</li><ul><li>event target:magic ally 1:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = opinion_magical_feast</li><li>years = 5</li></ul></ul></ul></ul>

___
##Hold a Magical Feast with [magic_ally_2.GetName]

###Available if:
<li>num of allies is at least 2</li>

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>goto = magic_ally_2</li><li>magic casted spell = yes</li><li>add ruler modifier:</li><ul><li>name = magic_feast_cooldown</li><li>duration = 30</li><li>hidden = yes</li></ul><li>If has ruler flag is [conjuration_2](../flags/conjuration_2.md):</li><ul><li>event target:magic ally 2:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = opinion_magical_feast_greater</li><li>years = 5</li></ul></ul></ul><li>else:</li><ul><li>event target:magic ally 2:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = opinion_magical_feast</li><li>years = 5</li></ul></ul></ul></ul>

___
##Hold a Magical Feast with [magic_ally_3.GetName]

###Available if:
<li>num of allies is at least 3</li>

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>goto = magic_ally_3</li><li>magic casted spell = yes</li><li>add ruler modifier:</li><ul><li>name = magic_feast_cooldown</li><li>duration = 30</li><li>hidden = yes</li></ul><li>If has ruler flag is [conjuration_2](../flags/conjuration_2.md):</li><ul><li>event target:magic ally 3:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = opinion_magical_feast_greater</li><li>years = 5</li></ul></ul></ul><li>else:</li><ul><li>event target:magic ally 3:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = opinion_magical_feast</li><li>years = 5</li></ul></ul></ul></ul>

___
##Hold a Magical Feast with [magic_ally_4.GetName]

###Available if:
<li>num of allies is at least 4</li>

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>goto = magic_ally_4</li><li>magic casted spell = yes</li><li>add ruler modifier:</li><ul><li>name = magic_feast_cooldown</li><li>duration = 30</li><li>hidden = yes</li></ul><li>If has ruler flag is [conjuration_2](../flags/conjuration_2.md):</li><ul><li>event target:magic ally 4:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = opinion_magical_feast_greater</li><li>years = 5</li></ul></ul></ul><li>else:</li><ul><li>event target:magic ally 4:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = opinion_magical_feast</li><li>years = 5</li></ul></ul></ul></ul>

___
##Go back

###AI weighting:
AI weights this option at 5


###Efects:<ul><li>add dip power = 15</li></ul>
