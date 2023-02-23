#Information
 - Title: Dominant in Escann
 - ID: escanni_wars.10
#Description
Dominant in Escann
#Options

___
##Our throne is nice. The Dove Throne of Anbennar shall be even nicer, and is our due.

###Available if:
<li>religion group is cannorian</li><li>government is monarchy</li><li>hre size is at least 1</li><li>is not the emperor</li><li>None of the following:</li><ul><li>Country is Rogieria</li></ul>

###Efects:<ul><li>If has tag is B50:</li><ul><li>set country flag [newshire_won_consolidation](../flags/newshire_won_consolidation.md)</li><li>custom tooltip = newshire_won_consolidation_tooltip</li></ul><li>custom tooltip = usurp_emperorship_choice_tt</li><li>set country flag [escanni_wars_usurp_emperorship](../flags/escanni_wars_usurp_emperorship.md)</li></ul>

___
##We must recast ourselves in the image of the first and greatest human empire, Castanor!

###Available if:
<li>has estate estate_castonath_patricians</li><li>Any of the following:</li><ul><li>culture group is escanni</li><li>culture group  is dostanorian_g</li><li>culture is marrodic</li></ul><li>None of the following:</li><ul><li>has country flag [formed_castanor_flag](../flags/formed_castanor_flag.md)</li></ul><li>NOT:</li><ul><li>has adventurer reform yes</li></ul><li>NOT:</li><ul><li>exists is Castanor</li></ul><li>NOT:</li><ul><li>Country is Black Castanor</li></ul><li>NOT:</li><ul><li>has country flag [orc_nation_formed](../flags/orc_nation_formed.md)</li></ul><li>OR:</li><ul><li>is not controlled by the AI</li><li>is not playing custom nation</li></ul><li>is not colonial nation</li><li>OR:</li><ul><li>is not former colonial nation</li><li>All of the following:</li><ul><li>is former colonial nation</li><li>is not controlled by the AI</li></ul></ul><li>is using normal or historical nations</li>

###Efects:<ul><li>If has tag is B33:</li><ul><li>custom tooltip = no_more_blademarches_blade_tt</li></ul><li>If has tag is B50:</li><ul><li>set country flag [newshire_won_consolidation](../flags/newshire_won_consolidation.md)</li><li>custom tooltip = newshire_won_consolidation_tooltip</li></ul><li>the event [A Crisis of Identity](../events/a_crisis_of_identity.md) happens</li></ul>

___
##Declare a new infernal empire in Escann, the Great Land - Moredhal!

###Available if:
<li>never</li><li>has reform secret_societies_inf</li>

###Efects:<ul><li>set country flag [form_moredhal](../flags/form_moredhal.md)</li><li>custom tooltip = moredhal_decision_tt</li></ul>

___
##The time of magic has come. Proclaim the Black Demesne!

###Available if:
<li>Any of the following:</li><ul><li>Country is Esthil</li><li>tag  is Covenblad</li><li>tag   is Ravenmarch</li><li>has ruler modifier witch_king_modifier</li></ul><li>None of the following:</li><ul><li>exists is Black Demense</li></ul>

###Efects:<ul><li>If has tag is B50:</li><ul><li>set country flag [newshire_won_consolidation](../flags/newshire_won_consolidation.md)</li><li>custom tooltip = newshire_won_consolidation_tooltip</li></ul><li>custom tooltip = escanni_wars_black_demesne_tooltip</li><li>hidden effect:</li><ul><li>set country flag [can_form_bd](../flags/can_form_bd.md)</li></ul></ul>

___
##So long as a corner on Halann does not see Corin's light, there is a shadow for evil to hide. Our work is not finished.

###Available if:
<li>religion is corinite</li><li>mission completed is corintar_escann_restored</li><li>mission completed  is corintar_the_reconciliation</li><li>mission completed   is corintar_escann_defended</li>

###AI weighting:
AI weights this option at 1000


###Efects:<ul><li>override country name = CORINTAR_HOLY_EMPIRE</li><li>hidden effect:</li><ul><li>remove country modifier = corintar_holy_empire_i</li></ul><li>country gets the modifier corintar_holy_empire_ii until otherwise removed</li></ul>

___
##As our power is absolute in Escann, so shall it be in Anbennar

###Available if:
<li>Country is Rogieria</li><li>hre size is at least 1</li>

###Efects:<ul><li>custom tooltip = rogieria_escanni_wars_bypass</li><li>set country flag [rogieria_escanni_wars_bypass_flag](../flags/rogieria_escanni_wars_bypass_flag.md)</li></ul>

___
##Assemble the armies, sharpen the blades, let Halann cower before us!

###Efects:<ul><li>country gets the modifier escanni_wars_escanni_imperialism until otherwise removed</li><li>If has tag is B50:</li><ul><li>set country flag [newshire_won_consolidation](../flags/newshire_won_consolidation.md)</li><li>custom tooltip = newshire_won_consolidation_tooltip</li></ul></ul>

___
##We have reclaimed Escann's shattered glory. Now we must see it prosper beneath us.

###Efects:<ul><li>country gets the modifier escanni_wars_escanni_peace until otherwise removed</li><li>If has tag is B50:</li><ul><li>set country flag [newshire_won_consolidation](../flags/newshire_won_consolidation.md)</li><li>custom tooltip = newshire_won_consolidation_tooltip</li></ul></ul>
