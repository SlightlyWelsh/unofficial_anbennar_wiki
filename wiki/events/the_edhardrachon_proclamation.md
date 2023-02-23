#Information
 - Title: The Edhardrachon Proclamation
 - ID: flavor_castanor.213
#Description
The Edhardrachon Proclamation
#Options

___
##Now, our attention can turn outward.

###Available if:
<li>Any of the following:</li><ul><li>has global flag [edhar_castan_victory](../flags/edhar_castan_victory.md)</li><li>B32:</li><ul><li>None of the following:</li><ul><li>check variable:</li><ul><li>which is castanLegitimacy</li><li>value is at least 0</li></ul></ul></ul></ul>

###Efects:<ul><li>If has tag is B61:</li><ul><li>exile ruler as:</li><ul><li>name = new_castan</li></ul><li>B32:</li><ul><li>set country flag [trials_of_castan_one_time_bypass](../flags/trials_of_castan_one_time_bypass.md)</li></ul><li>switch tag = B32</li><li>B32:</li><ul><li>set ruler = new_castan</li><li>add dip power = 100</li><li>add adm power = 100</li><li>add mil power = 100</li></ul><li>custom tooltip = edhardrachon_inherit_tt</li></ul><li>Else if has tag is B32:</li><ul><li>reduce stability or adm power = yes</li></ul><li>tooltip:</li><ul><li>B32:</li><ul><li>set country flag [patrician_castanor](../flags/patrician_castanor.md)</li><li>add government reform = castanor_succession_war_reward_edhar_castan</li><li>inherit = B61</li><li>add government reform = original_castanor_trials_reform</li></ul></ul></ul>

___
##Now, our attention can turn outward.

###Available if:
<li>Any of the following:</li><ul><li>has global flag [original_castan_victory](../flags/original_castan_victory.md)</li><li>B32:</li><ul><li>check variable:</li><ul><li>which is castanLegitimacy</li><li>value is at least 10</li></ul></ul></ul>

###Efects:<ul><li>If has tag is B61:</li><ul><li>switch tag = B32</li><li>B32:</li><ul><li>reduce stability or adm power = yes</li></ul></ul><li>Else if has tag is B32:</li><ul><li>add dip power = 100</li><li>add adm power = 100</li><li>add mil power = 100</li></ul><li>B32:</li><ul><li>add government reform = castanor_succession_war_reward_original_castan</li><li>inherit = B61</li></ul></ul>
