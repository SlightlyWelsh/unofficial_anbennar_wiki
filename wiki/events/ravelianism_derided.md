#Information
 - Title: Ravelianism Derided
 - ID: new_sun_cult.219
#Description
Ravelianism Derided
#Options

___
##We need no mere lightshow when we have Surael's sun in the sky above!

###AI weighting:
AI weights this option at 90
 - Multiplied by 2 if isolationism is 3
 - Multiplied by 5 if isolationism is 4


###Efects:<ul><li>custom tooltip = nsc_much_chosen_role_up_tt</li><li>add incident variable value:</li><ul><li>incident = incident_spread_of_ravelianism</li><li>value = 3</li></ul><li>add prestige = 25</li><li>If has country flag is [nsc_sent_heir](../flags/nsc_sent_heir.md):</li><ul><li>set heir = exiled_heir_@ROOT</li><li>If does not have ruler flag is [was_ruler_when_heir_left](../flags/was_ruler_when_heir_left.md); and  does not have regency:</li><ul><li>custom tooltip = nsc_ruler_will_step_down_tt</li><li>hidden effect:</li><ul><li>set country flag [nsc_no_level_loss](../flags/nsc_no_level_loss.md)</li><li>kill ruler = yes</li><li>add stability or adm power = yes</li></ul></ul></ul></ul>

___
##Perhaps it was mere bad luck, tell me more of what you saw in that chamber...

###AI weighting:
AI weights this option at 10
 - Multiplied by 0.5 if does not have stability is 0
 - Multiplied by 2 if does not haveolationism is 2
 - Multiplied by 5 if does not haveolationism is 1
 - Multiplied by 0 if is vassal, and  has overlord has religion is bulwari sun cult; and does not have liberty desire is 50


###Efects:<ul><li>custom tooltip = nsc_much_chosen_role_down_tt</li><li>add incident variable value:</li><ul><li>incident = incident_spread_of_ravelianism</li><li>value = -2</li></ul><li>reduce stability or adm power = yes</li><li>If has country flag is [nsc_sent_heir](../flags/nsc_sent_heir.md):</li><ul><li>set heir = exiled_heir_@ROOT</li><li>If does not have ruler flag is [was_ruler_when_heir_left](../flags/was_ruler_when_heir_left.md); and  does not have regency:</li><ul><li>custom tooltip = nsc_ruler_will_step_down_tt</li><li>hidden effect:</li><ul><li>set country flag [nsc_no_level_loss](../flags/nsc_no_level_loss.md)</li><li>kill ruler = yes</li><li>add stability or adm power = yes</li></ul></ul></ul></ul>
