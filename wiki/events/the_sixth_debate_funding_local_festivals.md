#Information
 - Title: The Sixth Debate: Funding Local Festivals
 - ID: new_sun_cult.138
#Description
The Sixth Debate: Funding Local Festivals
#Options

___
##Festivals warm our hearts and help us fight the Darkness; they should be funded by the church.

###AI weighting:
AI weights this option at 50
 - Multiplied by 0 if is vassal, and does not have liberty desire is 50; and does not have overlord has country flag is [nsc_choice_a](../flags/nsc_choice_a.md)
 - Multiplied by 3 if has F37 has country flag is [nsc_choice_a](../flags/nsc_choice_a.md); and  has alliance with is F37
 - Multiplied by 2 if has F37 has country flag is [nsc_choice_a](../flags/nsc_choice_a.md); and  has opinion has who is F37, and has opinion has value is 100
 - Multiplied by 0.5 if has F37 has country flag is [nsc_choice_a](../flags/nsc_choice_a.md); and  is rival is F37
 - Multiplied by 0 if has F37 has country flag is [nsc_choice_a](../flags/nsc_choice_a.md); and  has tag is U05


###Efects:<ul><li>If has F37 has country flag is [nsc_choice_a](../flags/nsc_choice_a.md):</li><ul><li>custom tooltip = nsc_irrliam_option_tt</li><li>hidden effect:</li><ul><li>If is chosen country is yes:</li><ul><li>REB:</li><ul><li>change variable:</li><ul><li>which = nscIrrliamChoicesVar</li><li>value = 2</li></ul></ul></ul><li>else:</li><ul><li>REB:</li><ul><li>change variable:</li><ul><li>which = nscIrrliamChoicesVar</li><li>value = 1</li></ul></ul></ul></ul></ul><li>hidden effect:</li><ul><li>If is chosen country is yes:</li><ul><li>REB:</li><ul><li>change variable:</li><ul><li>which = nscChoiceAVar</li><li>value = 2</li></ul></ul></ul><li>else:</li><ul><li>REB:</li><ul><li>change variable:</li><ul><li>which = nscChoiceAVar</li><li>value = 1</li></ul></ul></ul><li>set country flag [nsc_choice_a](../flags/nsc_choice_a.md)</li></ul><li>custom tooltip = nsc_chosen_role_up_tt</li><li>add incident variable value:</li><ul><li>incident = incident_death_of_taelarios</li><li>value = 1</li></ul><li>set country flag [nsc_sponsored_festivals_flag](../flags/nsc_sponsored_festivals_flag.md)</li><li>set estate privilege = estate_church_sponsored_festivals</li></ul>

___
##Buying them some equipment should be enough.

###AI weighting:
AI weights this option at 50
 - Multiplied by 0 if is vassal, and does not have liberty desire is 50; and does not have overlord has country flag is [nsc_choice_b](../flags/nsc_choice_b.md)
 - Multiplied by 3 if has F37 has country flag is [nsc_choice_b](../flags/nsc_choice_b.md); and  has alliance with is F37
 - Multiplied by 2 if has F37 has country flag is [nsc_choice_b](../flags/nsc_choice_b.md); and  has opinion has who is F37, and has opinion has value is 100
 - Multiplied by 0.5 if has F37 has country flag is [nsc_choice_b](../flags/nsc_choice_b.md); and  is rival is F37
 - Multiplied by 0 if has F37 has country flag is [nsc_choice_b](../flags/nsc_choice_b.md); and  has tag is U05


###Efects:<ul><li>If has F37 has country flag is [nsc_choice_b](../flags/nsc_choice_b.md):</li><ul><li>custom tooltip = nsc_irrliam_option_tt</li><li>hidden effect:</li><ul><li>If is chosen country is yes:</li><ul><li>REB:</li><ul><li>change variable:</li><ul><li>which = nscIrrliamChoicesVar</li><li>value = 2</li></ul></ul></ul><li>else:</li><ul><li>REB:</li><ul><li>change variable:</li><ul><li>which = nscIrrliamChoicesVar</li><li>value = 1</li></ul></ul></ul></ul></ul><li>hidden effect:</li><ul><li>If is chosen country is yes:</li><ul><li>REB:</li><ul><li>change variable:</li><ul><li>which = nscChoiceBVar</li><li>value = 2</li></ul></ul></ul><li>else:</li><ul><li>REB:</li><ul><li>change variable:</li><ul><li>which = nscChoiceBVar</li><li>value = 1</li></ul></ul></ul><li>set country flag [nsc_choice_b](../flags/nsc_choice_b.md)</li></ul><li>add treasury = -50</li><li>country gets the modifier nsc_equipped_festivals for 10 years</li></ul>

___
##Actually, festivals could become a good source of revenue for the church.

###AI weighting:
AI weights this option at 50
 - Multiplied by 0 if is vassal, and does not have liberty desire is 50; and does not have overlord has country flag is [nsc_choice_c](../flags/nsc_choice_c.md)
 - Multiplied by 3 if has F37 has country flag is [nsc_choice_c](../flags/nsc_choice_c.md); and  has alliance with is F37
 - Multiplied by 2 if has F37 has country flag is [nsc_choice_c](../flags/nsc_choice_c.md); and  has opinion has who is F37, and has opinion has value is 100
 - Multiplied by 0.5 if has F37 has country flag is [nsc_choice_c](../flags/nsc_choice_c.md); and  is rival is F37
 - Multiplied by 0 if has F37 has country flag is [nsc_choice_c](../flags/nsc_choice_c.md); and  has tag is U05


###Efects:<ul><li>If has F37 has country flag is [nsc_choice_c](../flags/nsc_choice_c.md):</li><ul><li>custom tooltip = nsc_irrliam_option_tt</li><li>hidden effect:</li><ul><li>If is chosen country is yes:</li><ul><li>REB:</li><ul><li>change variable:</li><ul><li>which = nscIrrliamChoicesVar</li><li>value = 2</li></ul></ul></ul><li>else:</li><ul><li>REB:</li><ul><li>change variable:</li><ul><li>which = nscIrrliamChoicesVar</li><li>value = 1</li></ul></ul></ul></ul></ul><li>hidden effect:</li><ul><li>If is chosen country is yes:</li><ul><li>REB:</li><ul><li>change variable:</li><ul><li>which = nscChoiceCVar</li><li>value = 2</li></ul></ul></ul><li>else:</li><ul><li>REB:</li><ul><li>change variable:</li><ul><li>which = nscChoiceCVar</li><li>value = 1</li></ul></ul></ul><li>set country flag [nsc_choice_c](../flags/nsc_choice_c.md)</li></ul><li>custom tooltip = nsc_chosen_role_down_tt</li><li>add incident variable value:</li><ul><li>incident = incident_death_of_taelarios</li><li>value = -1</li></ul><li>set country flag [nsc_church_tax_on_festivals](../flags/nsc_church_tax_on_festivals.md)</li><li>set estate privilege = estate_church_tax_on_local_festivals</li></ul>
