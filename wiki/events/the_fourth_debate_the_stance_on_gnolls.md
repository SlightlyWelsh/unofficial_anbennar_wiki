#Information
 - Title: The Fourth Debate: The Stance on Gnolls
 - ID: new_sun_cult.134
#Description
The Fourth Debate: The Stance on Gnolls
#Options

___
##They are the spawn of demons who enslaved this land for centuries! All must die!

###AI weighting:
AI weights this option at 50
 - Multiplied by 0 if is vassal, and does not have liberty desire is 50; and does not have overlord has country flag is [nsc_choice_a](../flags/nsc_choice_a.md)
 - Multiplied by 3 if has F37 has country flag is [nsc_choice_a](../flags/nsc_choice_a.md); and  has alliance with is F37
 - Multiplied by 2 if has F37 has country flag is [nsc_choice_a](../flags/nsc_choice_a.md); and  has opinion has who is F37, and has opinion has value is 100
 - Multiplied by 0.5 if has F37 has country flag is [nsc_choice_a](../flags/nsc_choice_a.md); and  is rival is F37
 - Multiplied by 0 if has F37 has country flag is [nsc_choice_a](../flags/nsc_choice_a.md); and  has tag is U05


###Efects:<ul><li>If has F37 has country flag is [nsc_choice_a](../flags/nsc_choice_a.md):</li><ul><li>custom tooltip = nsc_irrliam_option_tt</li><li>hidden effect:</li><ul><li>If is chosen country is yes:</li><ul><li>REB:</li><ul><li>change variable:</li><ul><li>which = nscIrrliamChoicesVar</li><li>value = 2</li></ul></ul></ul><li>else:</li><ul><li>REB:</li><ul><li>change variable:</li><ul><li>which = nscIrrliamChoicesVar</li><li>value = 1</li></ul></ul></ul></ul></ul><li>hidden effect:</li><ul><li>If is chosen country is yes:</li><ul><li>REB:</li><ul><li>change variable:</li><ul><li>which = nscChoiceAVar</li><li>value = 2</li></ul></ul></ul><li>else:</li><ul><li>REB:</li><ul><li>change variable:</li><ul><li>which = nscChoiceAVar</li><li>value = 1</li></ul></ul></ul><li>set country flag [nsc_choice_a](../flags/nsc_choice_a.md)</li></ul><li>custom tooltip = nsc_chosen_role_up_tt</li><li>add incident variable value:</li><ul><li>incident = incident_death_of_taelarios</li><li>value = 1</li></ul><li>large decrease of gnollish tolerance effect = yes</li></ul>

___
##They are beasts that must be driven from Bulwar back below the Salahad!

###AI weighting:
AI weights this option at 50
 - Multiplied by 0 if is vassal, and does not have liberty desire is 50; and does not have overlord has country flag is [nsc_choice_b](../flags/nsc_choice_b.md)
 - Multiplied by 3 if has F37 has country flag is [nsc_choice_b](../flags/nsc_choice_b.md); and  has alliance with is F37
 - Multiplied by 2 if has F37 has country flag is [nsc_choice_b](../flags/nsc_choice_b.md); and  has opinion has who is F37, and has opinion has value is 100
 - Multiplied by 0.5 if has F37 has country flag is [nsc_choice_b](../flags/nsc_choice_b.md); and  is rival is F37
 - Multiplied by 0 if has F37 has country flag is [nsc_choice_b](../flags/nsc_choice_b.md); and  has tag is U05


###Efects:<ul><li>If has F37 has country flag is [nsc_choice_b](../flags/nsc_choice_b.md):</li><ul><li>custom tooltip = nsc_irrliam_option_tt</li><li>hidden effect:</li><ul><li>If is chosen country is yes:</li><ul><li>REB:</li><ul><li>change variable:</li><ul><li>which = nscIrrliamChoicesVar</li><li>value = 2</li></ul></ul></ul><li>else:</li><ul><li>REB:</li><ul><li>change variable:</li><ul><li>which = nscIrrliamChoicesVar</li><li>value = 1</li></ul></ul></ul></ul></ul><li>hidden effect:</li><ul><li>If is chosen country is yes:</li><ul><li>REB:</li><ul><li>change variable:</li><ul><li>which = nscChoiceBVar</li><li>value = 2</li></ul></ul></ul><li>else:</li><ul><li>REB:</li><ul><li>change variable:</li><ul><li>which = nscChoiceBVar</li><li>value = 1</li></ul></ul></ul><li>set country flag [nsc_choice_b](../flags/nsc_choice_b.md)</li></ul><li>medium decrease of gnollish tolerance effect = yes</li></ul>

___
##They are misguided creatures that must be shown the path to the Light.

###AI weighting:
AI weights this option at 50
 - Multiplied by 0 if is vassal, and does not have liberty desire is 50; and does not have overlord has country flag is [nsc_choice_c](../flags/nsc_choice_c.md)
 - Multiplied by 3 if has F37 has country flag is [nsc_choice_c](../flags/nsc_choice_c.md); and  has alliance with is F37
 - Multiplied by 2 if has F37 has country flag is [nsc_choice_c](../flags/nsc_choice_c.md); and  has opinion has who is F37, and has opinion has value is 100
 - Multiplied by 0.5 if has F37 has country flag is [nsc_choice_c](../flags/nsc_choice_c.md); and  is rival is F37
 - Multiplied by 0 if has F37 has country flag is [nsc_choice_c](../flags/nsc_choice_c.md); and  has tag is U05
 - Multiplied by 0 if has low tolerance gnollish race trigger is yes
 - Multiplied by 10 if has high tolerance gnollish race trigger is yes


###Efects:<ul><li>If has F37 has country flag is [nsc_choice_c](../flags/nsc_choice_c.md):</li><ul><li>custom tooltip = nsc_irrliam_option_tt</li><li>hidden effect:</li><ul><li>If is chosen country is yes:</li><ul><li>REB:</li><ul><li>change variable:</li><ul><li>which = nscIrrliamChoicesVar</li><li>value = 2</li></ul></ul></ul><li>else:</li><ul><li>REB:</li><ul><li>change variable:</li><ul><li>which = nscIrrliamChoicesVar</li><li>value = 1</li></ul></ul></ul></ul></ul><li>hidden effect:</li><ul><li>If is chosen country is yes:</li><ul><li>REB:</li><ul><li>change variable:</li><ul><li>which = nscChoiceCVar</li><li>value = 2</li></ul></ul></ul><li>else:</li><ul><li>REB:</li><ul><li>change variable:</li><ul><li>which = nscChoiceCVar</li><li>value = 1</li></ul></ul></ul><li>set country flag [nsc_choice_c](../flags/nsc_choice_c.md)</li></ul><li>custom tooltip = nsc_much_chosen_role_down_tt</li><li>add incident variable value:</li><ul><li>incident = incident_death_of_taelarios</li><li>value = -2</li></ul><li>largest increase of gnollish tolerance effect = yes</li></ul>
