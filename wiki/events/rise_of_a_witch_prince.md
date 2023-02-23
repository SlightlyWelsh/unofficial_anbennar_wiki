#Information
 - Title: Rise of a Witch-Prince
 - ID: witch_king.4
#Description
Rise of a Witch-Prince
#Options

___
##They have forfeited the right to rule.

###AI weighting:
AI weights this option at 10
 - Multiplied by 2 if has ai attitude has who is event target:imperial witch king, and ai attitude has attitude is attitude rivalry; and has ai attitude has who is event target:imperial witch king, and ai attitude has attitude is attitude hostile; and has ai attitude has who is event target:imperial witch king, and ai attitude has attitude is attitude threatened; and has ai attitude has who is event target:imperial witch king, and ai attitude has attitude is attitude outraged; and has ai attitude has who is event target:imperial witch king, and ai attitude has attitude is attitude rebellious


###Efects:<ul><li>emperor:</li><ul><li>declare war with cb:</li><ul><li>who = event_target:imperial_witch_king</li><li>casus belli = cb_evil_ruler</li></ul></ul><li>If does not have event target:imperial witch king has tag is A85; and  has exists is A85:</li><ul><li>custom tooltip = magisterium_may_join_war_tt</li><li>hidden effect:</li><ul><li>A85:</li><ul><li>the event [Rise of a Witch-Prince in [imperial_witch_king.GetName]](../events/rise_of_a_witch_prince_in_imperial_witch_king_getname.md) happens</li></ul></ul></ul><li>event target:imperial witch king:</li><ul><li>add ruler modifier:</li><ul><li>name = denounced_witch_king</li><li>duration = 3650</li></ul></ul></ul>

___
##We will simply denounce them.

###AI weighting:
AI weights this option at 5
 - Multiplied by 2 if has opinion has who is event target:imperial witch king, and has opinion has value is 100; and has ai attitude has who is event target:imperial witch king, and ai attitude has attitude is attitude friendly; and has ai attitude has who is event target:imperial witch king, and ai attitude has attitude is attitude loyal; and has ai attitude has who is event target:imperial witch king, and ai attitude has attitude is attitude allied


###Efects:<ul><li>add imperial influence = -20</li><li>add ruler modifier:</li><ul><li>name = cowardly_emperor</li><li>duration = -1</li></ul><li>event target:imperial witch king:</li><ul><li>add ruler modifier:</li><ul><li>name = denounced_witch_king</li><li>duration = 3650</li></ul></ul></ul>
