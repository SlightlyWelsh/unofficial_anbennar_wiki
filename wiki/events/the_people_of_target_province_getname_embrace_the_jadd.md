#Information
 - Title: The People of [target_province.GetName] Embrace the Jadd
 - ID: bulwar_flavour.11
#Description
The People of [target_province.GetName] Embrace the Jadd
#Options

___
##That's not what I wanted! Kick them out!

###AI weighting:
AI weights this option at 2
 - Multiplied by 5 if has culture is sun elf, and  has religion is bulwari sun cult
 - Multiplied by 0.5 if does not have culture is sun elf; and  has religion is bulwari sun cult
 - Multiplied by 3 if has ruler has personality is malevolent personality
 - Multiplied by 3 if has ruler has personality is strict personality
 - Multiplied by 20 if has ruler has personality is zealot personality
 - Multiplied by 20 if has ruler has personality is pious personality


###Efects:<ul><li>event target:target province:</li><ul><li>change religion = the_jadd</li><li>add permanent province modifier:</li><ul><li>name = religious_zeal_at_conv</li><li>duration = 3650</li></ul></ul><li>remove country modifier = jaddari_visiting_jaddari_missionaries</li></ul>

___
##This was to be expected

###AI weighting:
AI weights this option at 5
 - Multiplied by 3 if has ruler has personality is tolerant personality
 - Multiplied by 3 if has ruler has personality is free thinker personality
 - Multiplied by 2 if has ruler has personality is sinner personality
 - Multiplied by 0 if has num of religion has religion is the jadd, and num of religion has value is 0.9


###Efects:<ul><li>event target:target province:</li><ul><li>change religion = the_jadd</li><li>add permanent province modifier:</li><ul><li>name = religious_zeal_at_conv</li><li>duration = 3650</li></ul></ul></ul>

___
##They're really onto something!

###Available if:
<li>dominant religion is the_jadd</li>

###AI weighting:
AI weights this option at 1
 - Multiplied by 0 if has ruler has personality is zealot personality
 - Multiplied by 0 if has ruler has personality is pious personality
 - Multiplied by 40 if has num of religion has religion is the jadd, and num of religion has value is 0.9


###Efects:<ul><li>event target:target province:</li><ul><li>change religion = the_jadd</li><li>add permanent province modifier:</li><ul><li>name = religious_zeal_at_conv</li><li>duration = 3650</li></ul></ul><li>change religion = the_jadd</li><li>reduce stability or adm power = yes</li></ul>
