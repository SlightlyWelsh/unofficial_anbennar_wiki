#Information
 - Title: Adventurers Seek Support
 - ID: new_sun_cult.149
#Description
Adventurers Seek Support
#Options

___
##Fund their enterprise.

###AI weighting:
AI weights this option at 33
 - Multiplied by 5 if has ruler has personality is entrepreneur personality
 - Multiplied by 5 if has ruler has personality is expansionist personality
 - Multiplied by 5 if has ruler has personality is navigator personality
 - Multiplied by 5 if has ruler has personality is careful personality
 - Multiplied by 0 if does not have years of income is 0.2


###Efects:<ul><li>custom tooltip = nsc_chosen_role_down_tt</li><li>custom tooltip = nsc_improve_change_of_success_tt</li><li>add incident variable value:</li><ul><li>incident = incident_call_of_aelantir</li><li>value = 1</li></ul><li>add years of income = -0.25</li><li>add estate loyalty:</li><ul><li>estate = estate_adventurers</li><li>loyalty = 5</li></ul><li>hidden effect:</li><ul><li>random list:</li><ul><li>15:</li><ul><li>the event ˻new_sun_cult.150˼ happens</li></ul><li>55:</li><ul><li>the event ˻new_sun_cult.151˼ happens</li></ul><li>30:</li><ul><li>the event ˻new_sun_cult.152˼ happens</li></ul></ul></ul></ul>

___
##Fund their enterprise and lend them some ships!

###Available if:
<li>sailors is at least 200</li>

###AI weighting:
AI weights this option at 33
 - Multiplied by 100 if has personality is ai colonialist
 - Multiplied by 10 if has ruler has personality is entrepreneur personality
 - Multiplied by 10 if has ruler has personality is expansionist personality
 - Multiplied by 10 if has ruler has personality is navigator personality
 - Multiplied by 0 if does not have years of income is 0.4


###Efects:<ul><li>custom tooltip = nsc_much_chosen_role_down_tt</li><li>custom tooltip = nsc_much_improve_change_of_success_tt</li><li>add incident variable value:</li><ul><li>incident = incident_call_of_aelantir</li><li>value = 2</li></ul><li>add years of income = -0.5</li><li>add estate loyalty:</li><ul><li>estate = estate_adventurers</li><li>loyalty = 15</li></ul><li>add sailors = -250</li><li>hidden effect:</li><ul><li>random list:</li><ul><li>55:</li><ul><li>the event ˻new_sun_cult.150˼ happens</li></ul><li>35:</li><ul><li>the event ˻new_sun_cult.151˼ happens</li></ul><li>10:</li><ul><li>the event ˻new_sun_cult.152˼ happens</li></ul></ul></ul></ul>

___
##Let them find funds themselves.

###AI weighting:
AI weights this option at 33
 - Multiplied by 10 if has ruler has personality is careful personality
 - Multiplied by 10 if has ruler has personality is free thinker personality


###Efects:<ul><li>add estate loyalty:</li><ul><li>estate = estate_adventurers</li><li>loyalty = -5</li></ul><li>hidden effect:</li><ul><li>random list:</li><ul><li>25:</li><ul><li>the event ˻new_sun_cult.151˼ happens</li></ul><li>75:</li><ul><li>the event ˻new_sun_cult.152˼ happens</li></ul></ul></ul></ul>

___
##Don't fund them and forbid them from leaving!

###AI weighting:
AI weights this option at 33
 - Multiplied by 10 if has ruler has personality is zealot personality
 - Multiplied by 5 if has ruler has personality is strict personality
 - Multiplied by 10 if has ruler has personality is greedy personality


###Efects:<ul><li>custom tooltip = nsc_chosen_role_up_tt</li><li>custom tooltip = nsc_no_expedition_tt</li><li>add incident variable value:</li><ul><li>incident = incident_call_of_aelantir</li><li>value = -1</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_adventurers</li><li>loyalty = -15</li></ul><li>hidden effect:</li><ul><li>the event ˻new_sun_cult.153˼ happens</li></ul></ul>
