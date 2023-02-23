#Information
 - Title: The First Debate: The Role of the Chosen in Society
 - ID: new_sun_cult.128
#Description
The First Debate: The Role of the Chosen in Society
#Options

___
##God-Kings who allow lesser beings a glimpse of the Light.

###AI weighting:
AI weights this option at 20
 - Multiplied by 0.1 if does not haveolationism is 4
 - Multiplied by 0 if is vassal, and does not have liberty desire is 50; and does not have overlord has country flag is [nsc_choice_a](../flags/nsc_choice_a.md)
 - Multiplied by 3 if has F37 has country flag is [nsc_choice_a](../flags/nsc_choice_a.md); and  has alliance with is F37
 - Multiplied by 2 if has F37 has country flag is [nsc_choice_a](../flags/nsc_choice_a.md); and  has opinion has who is F37, and has opinion has value is 100
 - Multiplied by 0 if has F37 has country flag is [nsc_choice_a](../flags/nsc_choice_a.md); and  has tag is U05


###Efects:<ul><li>If has F37 has country flag is [nsc_choice_a](../flags/nsc_choice_a.md):</li><ul><li>custom tooltip = nsc_irrliam_option_tt</li><li>hidden effect:</li><ul><li>If is chosen country is yes:</li><ul><li>REB:</li><ul><li>change variable:</li><ul><li>which = nscIrrliamChoicesVar</li><li>value = 2</li></ul></ul></ul><li>else:</li><ul><li>REB:</li><ul><li>change variable:</li><ul><li>which = nscIrrliamChoicesVar</li><li>value = 1</li></ul></ul></ul></ul></ul><li>hidden effect:</li><ul><li>If is chosen country is yes:</li><ul><li>REB:</li><ul><li>change variable:</li><ul><li>which = nscChoiceAVar</li><li>value = 2</li></ul></ul></ul><li>else:</li><ul><li>REB:</li><ul><li>change variable:</li><ul><li>which = nscChoiceAVar</li><li>value = 1</li></ul></ul></ul><li>set country flag [nsc_choice_a](../flags/nsc_choice_a.md)</li></ul><li>If does not haveolationism is 4:</li><ul><li>If isolationism is 3:</li><ul><li>custom tooltip = nsc_chosen_role_up_tt</li><li>add incident variable value:</li><ul><li>incident = incident_death_of_taelarios</li><li>value = 1</li></ul><li>country gets the modifier nsc_differing_opinion for 10 years</li></ul><li>else:</li><ul><li>custom tooltip = nsc_much_chosen_role_up_tt</li><li>add incident variable value:</li><ul><li>incident = incident_death_of_taelarios</li><li>value = 2</li></ul><li>country gets the modifier nsc_big_differing_opinion for 10 years</li></ul></ul><li>else:</li><ul><li>country gets the modifier nsc_congruent_opinion for 10 years</li></ul></ul>

___
##Unquestionable rulers who will carve our way to salvation.

###AI weighting:
AI weights this option at 20
 - Multiplied by 0.1 if does not haveolationism is 3; and  isolationism is 4
 - Multiplied by 0 if is vassal, and does not have liberty desire is 50; and does not have overlord has country flag is [nsc_choice_b](../flags/nsc_choice_b.md)
 - Multiplied by 3 if has F37 has country flag is [nsc_choice_b](../flags/nsc_choice_b.md); and  has alliance with is F37
 - Multiplied by 2 if has F37 has country flag is [nsc_choice_b](../flags/nsc_choice_b.md); and  has opinion has who is F37, and has opinion has value is 100
 - Multiplied by 0 if has F37 has country flag is [nsc_choice_a](../flags/nsc_choice_a.md); and  has tag is U05


###Efects:<ul><li>If has F37 has country flag is [nsc_choice_b](../flags/nsc_choice_b.md):</li><ul><li>custom tooltip = nsc_irrliam_option_tt</li><li>hidden effect:</li><ul><li>If is chosen country is yes:</li><ul><li>REB:</li><ul><li>change variable:</li><ul><li>which = nscIrrliamChoicesVar</li><li>value = 2</li></ul></ul></ul><li>else:</li><ul><li>REB:</li><ul><li>change variable:</li><ul><li>which = nscIrrliamChoicesVar</li><li>value = 1</li></ul></ul></ul></ul></ul><li>hidden effect:</li><ul><li>If is chosen country is yes:</li><ul><li>REB:</li><ul><li>change variable:</li><ul><li>which = nscChoiceBVar</li><li>value = 2</li></ul></ul></ul><li>else:</li><ul><li>REB:</li><ul><li>change variable:</li><ul><li>which = nscChoiceBVar</li><li>value = 1</li></ul></ul></ul><li>set country flag [nsc_choice_b](../flags/nsc_choice_b.md)</li></ul><li>If does not haveolationism is 3:</li><ul><li>If isolationism is 2:</li><ul><li>custom tooltip = nsc_chosen_role_up_tt</li><li>add incident variable value:</li><ul><li>incident = incident_death_of_taelarios</li><li>value = 1</li></ul><li>country gets the modifier nsc_differing_opinion for 10 years</li></ul><li>else:</li><ul><li>custom tooltip = nsc_much_chosen_role_up_tt</li><li>add incident variable value:</li><ul><li>incident = incident_death_of_taelarios</li><li>value = 2</li></ul><li>country gets the modifier nsc_big_differing_opinion for 10 years</li></ul></ul><li>Else if isolationism is 4:</li><ul><li>custom tooltip = nsc_chosen_role_down_tt</li><li>add incident variable value:</li><ul><li>incident = incident_death_of_taelarios</li><li>value = -1</li></ul><li>country gets the modifier nsc_differing_opinion for 10 years</li></ul><li>else:</li><ul><li>country gets the modifier nsc_congruent_opinion for 10 years</li></ul></ul>

___
##Leaders who will help us find the path.

###AI weighting:
AI weights this option at 20
 - Multiplied by 0.1 if does not haveolationism is 2; and  isolationism is 3
 - Multiplied by 0 if is vassal, and does not have liberty desire is 50; and does not have overlord has country flag is [nsc_choice_c](../flags/nsc_choice_c.md)
 - Multiplied by 3 if has F37 has country flag is [nsc_choice_c](../flags/nsc_choice_c.md); and  has alliance with is F37
 - Multiplied by 2 if has F37 has country flag is [nsc_choice_c](../flags/nsc_choice_c.md); and  has opinion has who is F37, and has opinion has value is 100
 - Multiplied by 0 if has F37 has country flag is [nsc_choice_a](../flags/nsc_choice_a.md); and  has tag is U05


###Efects:<ul><li>If has F37 has country flag is [nsc_choice_c](../flags/nsc_choice_c.md):</li><ul><li>custom tooltip = nsc_irrliam_option_tt</li><li>hidden effect:</li><ul><li>If is chosen country is yes:</li><ul><li>REB:</li><ul><li>change variable:</li><ul><li>which = nscIrrliamChoicesVar</li><li>value = 2</li></ul></ul></ul><li>else:</li><ul><li>REB:</li><ul><li>change variable:</li><ul><li>which = nscIrrliamChoicesVar</li><li>value = 1</li></ul></ul></ul></ul></ul><li>hidden effect:</li><ul><li>If is chosen country is yes:</li><ul><li>REB:</li><ul><li>change variable:</li><ul><li>which = nscChoiceCVar</li><li>value = 2</li></ul></ul></ul><li>else:</li><ul><li>REB:</li><ul><li>change variable:</li><ul><li>which = nscChoiceCVar</li><li>value = 1</li></ul></ul></ul><li>set country flag [nsc_choice_c](../flags/nsc_choice_c.md)</li></ul><li>If does not haveolationism is 2:</li><ul><li>If isolationism is 1:</li><ul><li>custom tooltip = nsc_chosen_role_up_tt</li><li>add incident variable value:</li><ul><li>incident = incident_death_of_taelarios</li><li>value = 1</li></ul><li>country gets the modifier nsc_differing_opinion for 10 years</li></ul><li>else:</li><ul><li>custom tooltip = nsc_much_chosen_role_up_tt</li><li>add incident variable value:</li><ul><li>incident = incident_death_of_taelarios</li><li>value = 2</li></ul><li>country gets the modifier nsc_big_differing_opinion for 10 years</li></ul></ul><li>Else if isolationism is 3:</li><ul><li>If isolationism is 4:</li><ul><li>custom tooltip = nsc_much_chosen_role_down_tt</li><li>add incident variable value:</li><ul><li>incident = incident_death_of_taelarios</li><li>value = -2</li></ul><li>country gets the modifier nsc_big_differing_opinion for 10 years</li></ul><li>else:</li><ul><li>custom tooltip = nsc_chosen_role_down_tt</li><li>add incident variable value:</li><ul><li>incident = incident_death_of_taelarios</li><li>value = -1</li></ul><li>country gets the modifier nsc_differing_opinion for 10 years</li></ul></ul><li>else:</li><ul><li>country gets the modifier nsc_congruent_opinion for 10 years</li></ul></ul>

___
##Guides and shepherds on the journey to Surael's Light.

###AI weighting:
AI weights this option at 20
 - Multiplied by 0.1 if does not haveolationism is 1; and  isolationism is 2
 - Multiplied by 0 if is vassal, and does not have liberty desire is 50; and does not have overlord has country flag is [nsc_choice_e](../flags/nsc_choice_e.md)
 - Multiplied by 3 if has F37 has country flag is [nsc_choice_e](../flags/nsc_choice_e.md); and  has alliance with is F37
 - Multiplied by 2 if has F37 has country flag is [nsc_choice_e](../flags/nsc_choice_e.md); and  has opinion has who is F37, and has opinion has value is 100
 - Multiplied by 0 if has F37 has country flag is [nsc_choice_a](../flags/nsc_choice_a.md); and  has tag is U05


###Efects:<ul><li>If has F37 has country flag is [nsc_choice_e](../flags/nsc_choice_e.md):</li><ul><li>custom tooltip = nsc_irrliam_option_tt</li><li>hidden effect:</li><ul><li>If is chosen country is yes:</li><ul><li>REB:</li><ul><li>change variable:</li><ul><li>which = nscIrrliamChoicesVar</li><li>value = 2</li></ul></ul></ul><li>else:</li><ul><li>REB:</li><ul><li>change variable:</li><ul><li>which = nscIrrliamChoicesVar</li><li>value = 1</li></ul></ul></ul></ul></ul><li>hidden effect:</li><ul><li>If is chosen country is yes:</li><ul><li>REB:</li><ul><li>change variable:</li><ul><li>which = nscChoiceEVar</li><li>value = 2</li></ul></ul></ul><li>else:</li><ul><li>REB:</li><ul><li>change variable:</li><ul><li>which = nscChoiceEVar</li><li>value = 1</li></ul></ul></ul><li>set country flag [nsc_choice_e](../flags/nsc_choice_e.md)</li></ul><li>If does not haveolationism is 1:</li><ul><li>custom tooltip = nsc_chosen_role_up_tt</li><li>add incident variable value:</li><ul><li>incident = incident_death_of_taelarios</li><li>value = 1</li></ul><li>country gets the modifier nsc_differing_opinion for 10 years</li></ul><li>Else if isolationism is 2:</li><ul><li>If isolationism is 3:</li><ul><li>custom tooltip = nsc_much_chosen_role_down_tt</li><li>add incident variable value:</li><ul><li>incident = incident_death_of_taelarios</li><li>value = -2</li></ul><li>country gets the modifier nsc_big_differing_opinion for 10 years</li></ul><li>else:</li><ul><li>custom tooltip = nsc_chosen_role_down_tt</li><li>add incident variable value:</li><ul><li>incident = incident_death_of_taelarios</li><li>value = -1</li></ul><li>country gets the modifier nsc_differing_opinion for 10 years</li></ul></ul><li>else:</li><ul><li>country gets the modifier nsc_congruent_opinion for 10 years</li></ul></ul>

___
##Priestly servants of Surael, here to help us find salvation.

###AI weighting:
AI weights this option at 20
 - Multiplied by 0.1 if isolationism is 1
 - Multiplied by 0 if is vassal, and does not have liberty desire is 50; and does not have overlord has country flag is [nsc_choice_f](../flags/nsc_choice_f.md)
 - Multiplied by 3 if has F37 has country flag is [nsc_choice_f](../flags/nsc_choice_f.md); and  has alliance with is F37
 - Multiplied by 2 if has F37 has country flag is [nsc_choice_f](../flags/nsc_choice_f.md); and  has opinion has who is F37, and has opinion has value is 100
 - Multiplied by 0 if has F37 has country flag is [nsc_choice_a](../flags/nsc_choice_a.md); and  has tag is U05


###Efects:<ul><li>If has F37 has country flag is [nsc_choice_f](../flags/nsc_choice_f.md):</li><ul><li>custom tooltip = nsc_irrliam_option_tt</li><li>hidden effect:</li><ul><li>If is chosen country is yes:</li><ul><li>REB:</li><ul><li>change variable:</li><ul><li>which = nscIrrliamChoicesVar</li><li>value = 2</li></ul></ul></ul><li>else:</li><ul><li>REB:</li><ul><li>change variable:</li><ul><li>which = nscIrrliamChoicesVar</li><li>value = 1</li></ul></ul></ul></ul></ul><li>hidden effect:</li><ul><li>If is chosen country is yes:</li><ul><li>REB:</li><ul><li>change variable:</li><ul><li>which = nscChoiceFVar</li><li>value = 2</li></ul></ul></ul><li>else:</li><ul><li>REB:</li><ul><li>change variable:</li><ul><li>which = nscChoiceFVar</li><li>value = 1</li></ul></ul></ul><li>set country flag [nsc_choice_f](../flags/nsc_choice_f.md)</li></ul><li>If isolationism is 1:</li><ul><li>If isolationism is 2:</li><ul><li>custom tooltip = nsc_much_chosen_role_down_tt</li><li>add incident variable value:</li><ul><li>incident = incident_death_of_taelarios</li><li>value = -2</li></ul><li>country gets the modifier nsc_big_differing_opinion for 10 years</li></ul><li>else:</li><ul><li>custom tooltip = nsc_chosen_role_down_tt</li><li>add incident variable value:</li><ul><li>incident = incident_death_of_taelarios</li><li>value = -1</li></ul><li>country gets the modifier nsc_differing_opinion for 10 years</li></ul></ul><li>else:</li><ul><li>country gets the modifier nsc_congruent_opinion for 10 years</li></ul></ul>
