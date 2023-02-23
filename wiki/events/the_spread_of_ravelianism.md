#Information
 - Title: The Spread of Ravelianism
 - ID: new_sun_cult.210
#Description
The Spread of Ravelianism
#Options

___
##Preposterous! They have no place here!

###AI weighting:
AI weights this option at 45
 - Multiplied by 5 if isolationism is 3


###Efects:<ul><li>custom tooltip = nsc_incident_ravelianism_start_tt</li><li>custom tooltip = nsc_chosen_role_up_tt</li><li>add incident variable value:</li><ul><li>incident = incident_spread_of_ravelianism</li><li>value = 1</li></ul><li>add legitimacy = 10</li></ul>

___
##We will allow them to stay as long as they behave.

###AI weighting:
AI weights this option at 45


###Efects:<ul><li>custom tooltip = nsc_incident_ravelianism_start_tt</li><li>add prestige = 5</li></ul>

___
##Let us hear what they have to say.

###AI weighting:
AI weights this option at 10
 - Multiplied by 5 if does not haveolationism is 2
 - Multiplied by 5 if does not haveolationism is 1
 - Multiplied by 0 if is vassal, and  has overlord has religion is bulwari sun cult; and does not have liberty desire is 50


###Efects:<ul><li>custom tooltip = nsc_incident_ravelianism_start_tt</li><li>custom tooltip = nsc_chosen_role_down_tt</li><li>add incident variable value:</li><ul><li>incident = incident_spread_of_ravelianism</li><li>value = -1</li></ul><li>If has country flag is [nsc_lucian_carter_in_our_lands](../flags/nsc_lucian_carter_in_our_lands.md):</li><ul><li>define advisor:</li><ul><li>type = theologian</li><li>name = "Lucian Carter"</li><li>skill = 3</li><li>culture = anbenncoster</li><li>religion = ravelian</li><li>discount = yes</li></ul></ul><li>else:</li><ul><li>define advisor:</li><ul><li>type = theologian</li><li>skill = 2</li><li>culture = anbenncoster</li><li>religion = ravelian</li><li>discount = yes</li></ul></ul><li>country gets the modifier nsc_ravelian_at_court for 10 years</li></ul>
