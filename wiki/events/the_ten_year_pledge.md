#Information
 - Title: The Ten-Year Pledge
 - ID: new_sun_cult.77
#Description
The Ten-Year Pledge
#Options

___
##Our realm is finally back on track, let [Root.GetName] prosper until the end of days!

###Available if:
<li>check variable:</li><ul><li>which is ScoreVar</li><li>value is at least 100</li></ul>

###Efects:<ul><li>end incident = incident_bulwar_under_threat</li><li>country gets the modifier nsc_pledge_great_success for 25 years</li><li>remove country modifier = nsc_bulwar_under_threat</li><li>remove country modifier = nsc_bulwar_under_threat_ai</li><li>If has incident variable value has incident is incident bulwar under threat, and incident variable value has value is 3:</li><ul><li>custom tooltip = nsc_choices_impact_level_tt</li><li>increase nsc isolation level = yes</li></ul><li>Else if does not have incident variable value has incident is incident bulwar under threat, and incident variable value has value is -2:</li><ul><li>custom tooltip = nsc_choices_impact_level_tt</li><li>decrease nsc isolation level = yes</li></ul><li>set country flag [birsartanses_pledge_good](../flags/birsartanses_pledge_good.md)</li></ul>

___
##The situation has certainly improved.

###Available if:
<li>None of the following:</li><ul><li>check variable:</li><ul><li>which is ScoreVar</li><li>value is at least 100</li></ul></ul><li>Any of the following:</li><ul><li>check variable:</li><ul><li>which is ScoreVar</li><li>value is at least 66</li></ul><li>is controlled by the AI</li></ul>

###Efects:<ul><li>end incident = incident_bulwar_under_threat</li><li>country gets the modifier nsc_pledge_successful for 10 years</li><li>remove country modifier = nsc_bulwar_under_threat</li><li>remove country modifier = nsc_bulwar_under_threat_ai</li><li>If has incident variable value has incident is incident bulwar under threat, and incident variable value has value is 3:</li><ul><li>custom tooltip = nsc_choices_impact_level_tt</li><li>increase nsc isolation level = yes</li></ul><li>Else if does not have incident variable value has incident is incident bulwar under threat, and incident variable value has value is -2:</li><ul><li>custom tooltip = nsc_choices_impact_level_tt</li><li>decrease nsc isolation level = yes</li></ul><li>set country flag [birsartanses_pledge_good](../flags/birsartanses_pledge_good.md)</li></ul>

___
##At least things are not as bad as they could be.

###Available if:
<li>None of the following:</li><ul><li>check variable:</li><ul><li>which is ScoreVar</li><li>value is at least 66</li></ul></ul><li>check variable:</li><ul><li>which is ScoreVar</li><li>value is at least 33</li></ul><li>is not controlled by the AI</li>

###Efects:<ul><li>end incident = incident_bulwar_under_threat</li><li>remove country modifier = nsc_bulwar_under_threat</li><li>country gets the modifier nsc_semi_successful for 10 years</li><li>If has incident variable value has incident is incident bulwar under threat, and incident variable value has value is 3:</li><ul><li>custom tooltip = nsc_choices_impact_level_tt</li><li>increase nsc isolation level = yes</li></ul><li>Else if does not have incident variable value has incident is incident bulwar under threat, and incident variable value has value is -2:</li><ul><li>custom tooltip = nsc_choices_impact_level_tt</li><li>decrease nsc isolation level = yes</li></ul><li>set country flag [birsartanses_pledge_good](../flags/birsartanses_pledge_good.md)</li></ul>

___
##This is a catastrophe...

###Available if:
<li>None of the following:</li><ul><li>check variable:</li><ul><li>which is ScoreVar</li><li>value is at least 33</li></ul></ul><li>is not controlled by the AI</li>

###Efects:<ul><li>end incident = incident_bulwar_under_threat</li><li>hidden effect:</li><ul><li>remove country modifier = nsc_bulwar_under_threat</li></ul><li>country gets the modifier nsc_bulwar_under_threat for 10 years</li><li>If has incident variable value has incident is incident bulwar under threat, and incident variable value has value is 3:</li><ul><li>custom tooltip = nsc_choices_impact_level_tt</li><li>increase nsc isolation level = yes</li></ul><li>Else if does not have incident variable value has incident is incident bulwar under threat, and incident variable value has value is -2:</li><ul><li>custom tooltip = nsc_choices_impact_level_tt</li><li>decrease nsc isolation level = yes</li></ul></ul>
