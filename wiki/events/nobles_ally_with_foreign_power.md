#Information
 - Title: Nobles Ally with Foreign Power
 - ID: 5064
#Description
Nobles Ally with Foreign Power
#Mean Time to Happen:
Base time = 1 days
 - Multiplied by 2.0 if does not have economic ideas is 2
 - Multiplied by 1.25 if does not have stability is 0
 - Multiplied by 0.8 if has stability is 1
 - Multiplied by 0.5 if is lucky

#Options

___
##They will pay for their treachery.

###AI weighting:
AI weights this option at 55
 - Multiplied by 0 if has estate is estate nobles, and does not have estate loyalty has estate is estate nobles, and estate loyalty has loyalty is 30


###Efects:<ul><li>reduce estate nobles loyalty effect = yes</li><li>event target:neighbour country:</li><ul><li>reverse add casus belli:</li><ul><li>target = ROOT</li><li>type = cb_insult</li><li>months = 12</li></ul></ul><li>add adm power = -33</li></ul>

___
##We'll deal with them later.

###AI weighting:
AI weights this option at 45
 - Multiplied by 1.5 if has prestige is 35


###Efects:<ul><li>add prestige = -15</li><li>add estate nobles loyalty effect = yes</li></ul>

___
##Let [Root.Monarch.GetTitle] Intimidate them.

###Available if:
<li>ruler has personality is malevolent_personality</li>

###Efects:<ul><li>highlight = yes</li><li>add prestige = -5</li><li>add estate nobles loyalty effect = yes</li><li>If has country flag is [tyrant_system_initialized](../flags/tyrant_system_initialized.md):</li><ul><li>increase tyrant ruthless 1 = yes</li></ul></ul>
