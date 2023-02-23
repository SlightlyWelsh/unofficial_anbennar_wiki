#Information
 - Title: The Second Debate: The Place of Humans in the Clergy
 - ID: new_sun_cult.130
#Description
The Second Debate: The Place of Humans in the Clergy
#Options

___
##The top positions should be occupied by the Chosen.

###AI weighting:
AI weights this option at 50
 - Multiplied by 0 if is vassal, and does not have liberty desire is 50; and does not have overlord has country flag is [nsc_choice_a](../flags/nsc_choice_a.md)
 - Multiplied by 3 if has F37 has country flag is [nsc_choice_a](../flags/nsc_choice_a.md); and  has alliance with is F37
 - Multiplied by 2 if has F37 has country flag is [nsc_choice_a](../flags/nsc_choice_a.md); and  has opinion has who is F37, and has opinion has value is 100
 - Multiplied by 0.5 if has F37 has country flag is [nsc_choice_a](../flags/nsc_choice_a.md); and  is rival is F37
 - Multiplied by 0 if has F37 has country flag is [nsc_choice_a](../flags/nsc_choice_a.md); and  has tag is U05
 - Multiplied by 0 if is not vassal, and has liberty desire is 50; and  is chosen country is no


###Efects:<ul><li>If has F37 has country flag is [nsc_choice_a](../flags/nsc_choice_a.md):</li><ul><li>custom tooltip = nsc_irrliam_option_tt</li><li>hidden effect:</li><ul><li>If is chosen country is yes:</li><ul><li>REB:</li><ul><li>change variable:</li><ul><li>which = nscIrrliamChoicesVar</li><li>value = 2</li></ul></ul></ul><li>else:</li><ul><li>REB:</li><ul><li>change variable:</li><ul><li>which = nscIrrliamChoicesVar</li><li>value = 1</li></ul></ul></ul></ul></ul><li>hidden effect:</li><ul><li>If is chosen country is yes:</li><ul><li>REB:</li><ul><li>change variable:</li><ul><li>which = nscChoiceAVar</li><li>value = 2</li></ul></ul></ul><li>else:</li><ul><li>REB:</li><ul><li>change variable:</li><ul><li>which = nscChoiceAVar</li><li>value = 1</li></ul></ul></ul><li>set country flag [nsc_choice_a](../flags/nsc_choice_a.md)</li></ul><li>custom tooltip = nsc_chosen_role_up_tt</li><li>add incident variable value:</li><ul><li>incident = incident_death_of_taelarios</li><li>value = 1</li></ul><li>country gets the modifier nsc_elven_clergy_support for 25 years</li></ul>

___
##No need to change anything.

###AI weighting:
AI weights this option at 50
 - Multiplied by 0 if is vassal, and does not have liberty desire is 50; and does not have overlord has country flag is [nsc_choice_b](../flags/nsc_choice_b.md)
 - Multiplied by 3 if has F37 has country flag is [nsc_choice_b](../flags/nsc_choice_b.md); and  has alliance with is F37
 - Multiplied by 2 if has F37 has country flag is [nsc_choice_b](../flags/nsc_choice_b.md); and  has opinion has who is F37, and has opinion has value is 100
 - Multiplied by 0.5 if has F37 has country flag is [nsc_choice_b](../flags/nsc_choice_b.md); and  is rival is F37
 - Multiplied by 0 if has F37 has country flag is [nsc_choice_b](../flags/nsc_choice_b.md); and  has tag is U05


###Efects:<ul><li>If has F37 has country flag is [nsc_choice_b](../flags/nsc_choice_b.md):</li><ul><li>custom tooltip = nsc_irrliam_option_tt</li><li>hidden effect:</li><ul><li>If is chosen country is yes:</li><ul><li>REB:</li><ul><li>change variable:</li><ul><li>which = nscIrrliamChoicesVar</li><li>value = 2</li></ul></ul></ul><li>else:</li><ul><li>REB:</li><ul><li>change variable:</li><ul><li>which = nscIrrliamChoicesVar</li><li>value = 1</li></ul></ul></ul></ul></ul><li>hidden effect:</li><ul><li>If is chosen country is yes:</li><ul><li>REB:</li><ul><li>change variable:</li><ul><li>which = nscChoiceBVar</li><li>value = 2</li></ul></ul></ul><li>else:</li><ul><li>REB:</li><ul><li>change variable:</li><ul><li>which = nscChoiceBVar</li><li>value = 1</li></ul></ul></ul><li>set country flag [nsc_choice_b](../flags/nsc_choice_b.md)</li></ul><li>country gets the modifier nsc_human_clergy_support for 25 years</li></ul>
