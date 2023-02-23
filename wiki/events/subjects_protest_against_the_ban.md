#Information
 - Title: Subjects Protest Against the Ban
 - ID: new_sun_cult.200
#Description
Subjects Protest Against the Ban
#Options

___
##Nonsense, let's put down this foolish rebellion at once! The ban stays.

###AI weighting:
AI weights this option at 20
 - Multiplied by 0 if does not have manpower percentage is 0.1
 - Multiplied by 10 if has ruler has personality is cruel personality
 - Multiplied by 100 if has ruler has personality is mage personality


###Efects:<ul><li>custom tooltip = nsc_chosen_role_up_tt</li><li>add incident variable value:</li><ul><li>incident = incident_rise_of_artificery</li><li>value = -1</li></ul><li>If does not have culture is sun elf; and num of owned provinces with has value is 3:</li><ul><li>If random owned province does not have culture is sun elf; and does not have province flag is [nsc_rebel_spawned](../flags/nsc_rebel_spawned.md):</li><ul><li>spawn rebels:</li><ul><li>type = particularist_rebels</li><li>size = 1</li></ul><li>set province flag [nsc_rebel_spawned](../flags/nsc_rebel_spawned.md)</li></ul><li>If random owned province does not have culture is sun elf; and does not have province flag is [nsc_rebel_spawned](../flags/nsc_rebel_spawned.md):</li><ul><li>spawn rebels:</li><ul><li>type = particularist_rebels</li><li>size = 1</li></ul><li>set province flag [nsc_rebel_spawned](../flags/nsc_rebel_spawned.md)</li></ul><li>If random owned province does not have culture is sun elf; and does not have province flag is [nsc_rebel_spawned](../flags/nsc_rebel_spawned.md):</li><ul><li>spawn rebels:</li><ul><li>type = particularist_rebels</li><li>size = 1</li></ul><li>set province flag [nsc_rebel_spawned](../flags/nsc_rebel_spawned.md)</li></ul></ul><li>else:</li><ul><li>If random owned province does not have province flag is [nsc_rebel_spawned](../flags/nsc_rebel_spawned.md):</li><ul><li>spawn rebels:</li><ul><li>type = particularist_rebels</li><li>size = 1</li></ul><li>set province flag [nsc_rebel_spawned](../flags/nsc_rebel_spawned.md)</li></ul><li>If random owned province does not have province flag is [nsc_rebel_spawned](../flags/nsc_rebel_spawned.md):</li><ul><li>spawn rebels:</li><ul><li>type = particularist_rebels</li><li>size = 1</li></ul><li>set province flag [nsc_rebel_spawned](../flags/nsc_rebel_spawned.md)</li></ul><li>If random owned province does not have province flag is [nsc_rebel_spawned](../flags/nsc_rebel_spawned.md):</li><ul><li>spawn rebels:</li><ul><li>type = particularist_rebels</li><li>size = 1</li></ul><li>set province flag [nsc_rebel_spawned](../flags/nsc_rebel_spawned.md)</li></ul></ul></ul>

___
##I guess we could loosen the ban a little bit...

###AI weighting:
AI weights this option at 20
 - Multiplied by 5 if has ruler has personality is free thinker personality
 - Multiplied by 5 if has ruler has personality is scholar personality
 - Multiplied by 0 if has ruler has personality is mage personality


###Efects:<ul><li>custom tooltip = nsc_chosen_role_down_tt</li><li>add incident variable value:</li><ul><li>incident = incident_rise_of_artificery</li><li>value = 1</li></ul><li>If has country modifier is nsc hard ban on artificery:</li><ul><li>remove country modifier = nsc_hard_ban_on_artificery</li><li>country gets the modifier nsc_ban_on_artificery until otherwise removed</li><li>add estate loyalty:</li><ul><li>estate = estate_mages</li><li>loyalty = -10</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_nobles</li><li>loyalty = -10</li></ul></ul><li>Else if has country modifier is nsc ban on artificery:</li><ul><li>remove country modifier = nsc_ban_on_artificery</li><li>country gets the modifier nsc_light_ban_on_artificery until otherwise removed</li><li>add estate loyalty:</li><ul><li>estate = estate_mages</li><li>loyalty = -10</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_nobles</li><li>loyalty = -10</li></ul></ul><li>Else if has country modifier is nsc light ban on artificery:</li><ul><li>remove country modifier = nsc_light_ban_on_artificery</li><li>country gets the modifier nsc_no_ban_on_artificery until otherwise removed</li><li>add estate loyalty:</li><ul><li>estate = estate_mages</li><li>loyalty = -10</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_nobles</li><li>loyalty = -10</li></ul></ul><li>If random owned province does not have province flag is [nsc_rebel_spawned](../flags/nsc_rebel_spawned.md):</li><ul><li>spawn rebels:</li><ul><li>type = noble_rebels</li><li>size = 1</li></ul><li>set province flag [nsc_rebel_spawned](../flags/nsc_rebel_spawned.md)</li></ul></ul>

___
##They are right, let's loosen the ban to just artifice weapons.

###Available if:
<li>None of the following:</li><ul><li>has country modifier nsc_light_ban_on_artificery</li></ul>

###AI weighting:
AI weights this option at 10
 - Multiplied by 10 if has ruler has personality is free thinker personality
 - Multiplied by 10 if has ruler has personality is scholar personality
 - Multiplied by 0 if has ruler has personality is mage personality


###Efects:<ul><li>custom tooltip = nsc_much_chosen_role_down_tt</li><li>add incident variable value:</li><ul><li>incident = incident_rise_of_artificery</li><li>value = 2</li></ul><li>If has country modifier is nsc hard ban on artificery:</li><ul><li>remove country modifier = nsc_hard_ban_on_artificery</li><li>country gets the modifier nsc_light_ban_on_artificery until otherwise removed</li><li>add estate loyalty:</li><ul><li>estate = estate_mages</li><li>loyalty = -20</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_nobles</li><li>loyalty = -20</li></ul></ul><li>Else if has country modifier is nsc ban on artificery:</li><ul><li>remove country modifier = nsc_ban_on_artificery</li><li>country gets the modifier nsc_no_ban_on_artificery until otherwise removed</li><li>add estate loyalty:</li><ul><li>estate = estate_mages</li><li>loyalty = -20</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_nobles</li><li>loyalty = -20</li></ul></ul><li>If random owned province does not have province flag is [nsc_rebel_spawned](../flags/nsc_rebel_spawned.md):</li><ul><li>spawn rebels:</li><ul><li>type = noble_rebels</li><li>size = 1</li></ul><li>set province flag [nsc_rebel_spawned](../flags/nsc_rebel_spawned.md)</li></ul><li>If random owned province does not have province flag is [nsc_rebel_spawned](../flags/nsc_rebel_spawned.md):</li><ul><li>spawn rebels:</li><ul><li>type = noble_rebels</li><li>size = 1</li></ul><li>set province flag [nsc_rebel_spawned](../flags/nsc_rebel_spawned.md)</li></ul></ul>

___
##Have [Root.Monarch.GetName] convince them to wait for the end of the investigation.

###Available if:
<li>Any of the following:</li><ul><li>ruler has personality is charismatic_negotiator_personality</li><li>ruler has personality  is silver_tongue_personality</li><li>is controlled by the AI</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 10 if has ruler has personality is mage personality
 - Multiplied by 5 if has ruler has personality is calm personality
 - Multiplied by 5 if has ruler has personality is careful personality


###Efects:<ul><li>highlight = yes</li><li>reduce legitimacy medium effect = yes</li></ul>
