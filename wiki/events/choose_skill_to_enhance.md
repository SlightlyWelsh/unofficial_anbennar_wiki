#Information
 - Title: Choose Skill to Enhance
 - ID: magic_ruler.18
#Description
Choose Skill to Enhance
#Options

___
##Cast Permanent Dame's Wisdom

###Available if:
<li>None of the following:</li><ul><li>adm is at least 6</li></ul><li>enhance ability cost adm trigger is yes</li>

###AI weighting:
AI weights this option at 50
 - Multiplied by 2 if does not have adm is 4


###Efects:<ul><li>If does not have adm is 3; and does not have adm is 4; and AND has ruler flag is [transmutation_3](../flags/transmutation_3.md):</li><ul><li>add adm power = -100</li></ul><li>Else if does not have adm is 4; and does not have adm is 5; and AND has ruler flag is [transmutation_3](../flags/transmutation_3.md):</li><ul><li>add adm power = -200</li></ul><li>Else if does not have adm is 5; and does not have adm is 6; and AND has ruler flag is [transmutation_3](../flags/transmutation_3.md):</li><ul><li>add adm power = -300</li></ul><li>Else if does not have adm is 6; and has ruler flag is [transmutation_3](../flags/transmutation_3.md):</li><ul><li>add adm power = -400</li></ul><li>else:</li><ul><li>add adm power = -500</li></ul><li>magic casted spell = yes</li><li>add ruler modifier:</li><ul><li>name = magic_enhance_cooldown</li><li>duration = 1825</li><li>hidden = yes</li></ul><li>If has ruler flag is [transmutation_3](../flags/transmutation_3.md):</li><ul><li>random list:</li><ul><li>70:</li><ul><li>increase ruler adm effect = yes</li></ul><li>25:</li><ul></ul><li>5:</li><ul><li>decrease ruler adm effect = yes</li></ul></ul></ul><li>else:</li><ul><li>random list:</li><ul><li>50:</li><ul><li>increase ruler adm effect = yes</li></ul><li>40:</li><ul></ul><li>10:</li><ul><li>decrease ruler adm effect = yes</li></ul></ul></ul><li>set country flag [spell_1](../flags/spell_1.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_14_t](../events/missing_localisation_magic_ruler_14_t.md) happens</li></ul></ul>

___
##§RCast Permanent Dame's Wisdom (Unavailable)§!

###Available if:
<li>None of the following:</li><ul><li>enhance ability cost adm trigger is yes</li></ul><li>NOT:</li><ul><li>adm is at least 6</li></ul>

###Efects:<ul><li>If has ruler flag is [transmutation_3](../flags/transmutation_3.md):</li><ul><li>If has adm is 5:</li><ul><li>custom tooltip = magic_need_500_adm_tt</li></ul><li>Else if has adm is 4:</li><ul><li>custom tooltip = magic_need_400_adm_tt</li></ul><li>Else if has adm is 3:</li><ul><li>custom tooltip = magic_need_300_adm_tt</li></ul><li>Else if has adm is 2:</li><ul><li>custom tooltip = magic_need_200_adm_tt</li></ul><li>else:</li><ul><li>custom tooltip = magic_need_100_adm_tt</li></ul></ul><li>else:</li><ul><li>If has adm is 5:</li><ul><li>custom tooltip = magic_need_400_adm_tt</li></ul><li>Else if has adm is 4:</li><ul><li>custom tooltip = magic_need_300_adm_tt</li></ul><li>Else if has adm is 3:</li><ul><li>custom tooltip = magic_need_200_adm_tt</li></ul><li>else:</li><ul><li>custom tooltip = magic_need_100_adm_tt</li></ul></ul></ul>

___
##Cast Permanent Minara's Tongue

###Available if:
<li>None of the following:</li><ul><li>dip is at least 6</li></ul><li>enhance ability cost dip trigger is yes</li>

###AI weighting:
AI weights this option at 50
 - Multiplied by 2 if does not have dip is 4


###Efects:<ul><li>If does not have dip is 3; and does not have dip is 4; and AND has ruler flag is [transmutation_3](../flags/transmutation_3.md):</li><ul><li>add dip power = -100</li></ul><li>Else if does not have dip is 4; and does not have dip is 5; and AND has ruler flag is [transmutation_3](../flags/transmutation_3.md):</li><ul><li>add dip power = -200</li></ul><li>Else if does not have dip is 5; and does not have dip is 6; and AND has ruler flag is [transmutation_3](../flags/transmutation_3.md):</li><ul><li>add dip power = -300</li></ul><li>Else if does not have dip is 6; and has ruler flag is [transmutation_3](../flags/transmutation_3.md):</li><ul><li>add dip power = -400</li></ul><li>else:</li><ul><li>add dip power = -500</li></ul><li>magic casted spell = yes</li><li>add ruler modifier:</li><ul><li>name = magic_enhance_cooldown</li><li>duration = 1825</li><li>hidden = yes</li></ul><li>If has ruler flag is [transmutation_3](../flags/transmutation_3.md):</li><ul><li>random list:</li><ul><li>70:</li><ul><li>increase ruler dip effect = yes</li></ul><li>25:</li><ul></ul><li>5:</li><ul><li>decrease ruler dip effect = yes</li></ul></ul></ul><li>else:</li><ul><li>random list:</li><ul><li>50:</li><ul><li>increase ruler dip effect = yes</li></ul><li>40:</li><ul></ul><li>10:</li><ul><li>decrease ruler dip effect = yes</li></ul></ul></ul><li>set country flag [spell_2](../flags/spell_2.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_14_t](../events/missing_localisation_magic_ruler_14_t.md) happens</li></ul></ul>

___
##Cast Permanent Minara's Tongue

###Available if:
<li>None of the following:</li><ul><li>enhance ability cost dip trigger is yes</li></ul><li>NOT:</li><ul><li>dip is at least 6</li></ul>

###Efects:<ul><li>If has ruler flag is [transmutation_3](../flags/transmutation_3.md):</li><ul><li>If has dip is 5:</li><ul><li>custom tooltip = magic_need_500_dip_tt</li></ul><li>Else if has dip is 4:</li><ul><li>custom tooltip = magic_need_400_dip_tt</li></ul><li>Else if has dip is 3:</li><ul><li>custom tooltip = magic_need_300_dip_tt</li></ul><li>Else if has dip is 2:</li><ul><li>custom tooltip = magic_need_200_dip_tt</li></ul><li>else:</li><ul><li>custom tooltip = magic_need_100_dip_tt</li></ul></ul><li>else:</li><ul><li>If has dip is 5:</li><ul><li>custom tooltip = magic_need_400_dip_tt</li></ul><li>Else if has dip is 4:</li><ul><li>custom tooltip = magic_need_300_dip_tt</li></ul><li>Else if has dip is 3:</li><ul><li>custom tooltip = magic_need_200_dip_tt</li></ul><li>else:</li><ul><li>custom tooltip = magic_need_100_dip_tt</li></ul></ul></ul>

___
##Cast Permanent Adean's Might

###Available if:
<li>None of the following:</li><ul><li>mil is at least 6</li></ul><li>enhance ability cost mil trigger is yes</li>

###Efects:<ul><li>If does not have mil is 3; and does not have mil is 4; and AND has ruler flag is [transmutation_3](../flags/transmutation_3.md):</li><ul><li>add mil power = -100</li></ul><li>Else if does not have mil is 4; and does not have mil is 5; and AND has ruler flag is [transmutation_3](../flags/transmutation_3.md):</li><ul><li>add mil power = -200</li></ul><li>Else if does not have mil is 5; and does not have mil is 6; and AND has ruler flag is [transmutation_3](../flags/transmutation_3.md):</li><ul><li>add mil power = -300</li></ul><li>Else if does not have mil is 6; and has ruler flag is [transmutation_3](../flags/transmutation_3.md):</li><ul><li>add mil power = -400</li></ul><li>else:</li><ul><li>add mil power = -500</li></ul><li>magic casted spell = yes</li><li>add ruler modifier:</li><ul><li>name = magic_enhance_cooldown</li><li>duration = 1825</li><li>hidden = yes</li></ul><li>If has ruler flag is [transmutation_3](../flags/transmutation_3.md):</li><ul><li>random list:</li><ul><li>70:</li><ul><li>increase ruler mil effect = yes</li></ul><li>25:</li><ul></ul><li>5:</li><ul><li>decrease ruler mil effect = yes</li></ul></ul></ul><li>else:</li><ul><li>random list:</li><ul><li>50:</li><ul><li>increase ruler mil effect = yes</li></ul><li>40:</li><ul></ul><li>10:</li><ul><li>decrease ruler mil effect = yes</li></ul></ul></ul><li>set country flag [spell_3](../flags/spell_3.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_14_t](../events/missing_localisation_magic_ruler_14_t.md) happens</li></ul></ul>

___
##§RCast Permanent Adean's Might (Unavailable)§!

###Available if:
<li>None of the following:</li><ul><li>enhance ability cost mil trigger is yes</li></ul><li>NOT:</li><ul><li>mil is at least 6</li></ul>

###Efects:<ul><li>If has ruler flag is [transmutation_3](../flags/transmutation_3.md):</li><ul><li>If has mil is 5:</li><ul><li>custom tooltip = magic_need_500_mil_tt</li></ul><li>Else if has mil is 4:</li><ul><li>custom tooltip = magic_need_400_mil_tt</li></ul><li>Else if has mil is 3:</li><ul><li>custom tooltip = magic_need_300_mil_tt</li></ul><li>Else if has mil is 2:</li><ul><li>custom tooltip = magic_need_200_mil_tt</li></ul><li>else:</li><ul><li>custom tooltip = magic_need_100_mil_tt</li></ul></ul><li>else:</li><ul><li>If has mil is 5:</li><ul><li>custom tooltip = magic_need_400_mil_tt</li></ul><li>Else if has mil is 4:</li><ul><li>custom tooltip = magic_need_300_mil_tt</li></ul><li>Else if has mil is 3:</li><ul><li>custom tooltip = magic_need_200_mil_tt</li></ul><li>else:</li><ul><li>custom tooltip = magic_need_100_mil_tt</li></ul></ul></ul>

___
##Go back

###AI weighting:
AI weights this option at 5

