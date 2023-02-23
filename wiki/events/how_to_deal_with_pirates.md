#Information
 - Title: How To Deal With Pirates
 - ID: treasurefleet.2
#Description
How To Deal With Pirates
#Options

___
##Pay off the pirates.

###AI weighting:
AI weights this option at 25
 - Multiplied by 0.1 if has ruler has personality is greedy personality


###Efects:<ul><li>set global flag [JY_LF_P_bribe](../flags/jy_lf_p_bribe.md)</li><li>add adm power = -1</li><li>custom tooltip = JY_LF_P_bribe_t</li></ul>

___
##Pay them, I have advice...

###Available if:
<li>Any of the following:</li><ul><li>ruler has personality is fierce_negotiator_personality</li><li>ruler has personality  is charismatic_negotiator_personality</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>set global flag [JY_LF_P_bribe](../flags/jy_lf_p_bribe.md)</li><li>set global flag [JY_LF_P_bribe_2](../flags/jy_lf_p_bribe_2.md)</li><li>add adm power = -1</li><li>custom tooltip = JY_LF_P_bribe_t</li><li>highlight = yes</li></ul>

___
##Try to sneak past them.

###AI weighting:
AI weights this option at 25


###Efects:<ul><li>set global flag [JY_LF_P_sneak](../flags/jy_lf_p_sneak.md)</li><li>add dip power = -1</li><li>custom tooltip = JY_LF_P_sneak_t</li></ul>

___
##Sneak past them, I have advice...

###Available if:
<li>ruler has personality is secretive_personality</li>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>set global flag [JY_LF_P_sneak](../flags/jy_lf_p_sneak.md)</li><li>set global flag [JY_LF_P_sneak_2](../flags/jy_lf_p_sneak_2.md)</li><li>add dip power = -1</li><li>custom tooltip = JY_LF_P_sneak_t</li><li>highlight = yes</li></ul>

___
##Try to fight them.

###AI weighting:
AI weights this option at 12
 - Multiplied by 0.25 if has ruler has personality is careful personality
 - Multiplied by 2 if has global flag is [JY_LF_P_weak](../flags/jy_lf_p_weak.md)
 - Multiplied by 4 if has global flag is [JY_LF_P_weaker](../flags/jy_lf_p_weaker.md)


###Efects:<ul><li>set global flag [JY_LF_P_fight](../flags/jy_lf_p_fight.md)</li><li>add mil power = -1</li><li>custom tooltip = JY_LF_P_fight_t</li></ul>

___
##Fight them off, I have advice...

###Available if:
<li>ruler has personality is navigator_personality</li>

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.5 if has ruler has personality is careful personality
 - Multiplied by 2 if has global flag is [JY_LF_P_weak](../flags/jy_lf_p_weak.md)
 - Multiplied by 4 if has global flag is [JY_LF_P_weaker](../flags/jy_lf_p_weaker.md)


###Efects:<ul><li>set global flag [JY_LF_P_fight](../flags/jy_lf_p_fight.md)</li><li>set global flag [JY_LF_P_fight_2](../flags/jy_lf_p_fight_2.md)</li><li>add mil power = -1</li><li>custom tooltip = JY_LF_P_fight_t</li><li>highlight = yes</li></ul>

___
##Don't bother, it is too dangerous.

###AI weighting:
AI weights this option at 25
 - Multiplied by 2 if has ruler has personality is careful personality


###Efects:<ul><li>set global flag [JY_LF_P_nah](../flags/jy_lf_p_nah.md)</li><li>add prestige = -1</li><li>custom tooltip = JY_LF_P_nah_t</li></ul>
