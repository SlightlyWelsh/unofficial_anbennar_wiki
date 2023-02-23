This page has the same name as others. For full listing see bottom of [the base page](election_in_the_root_governmentname.md).

#Information
 - Title: Election in the [Root.GovernmentName]
 - ID: elections.721
#Description
Election in the [Root.GovernmentName]
#Options

___
##A Statist Candidate

###Available if:
<li>None of the following:</li><ul><li>has reform monastic_elections_reform</li></ul><li>NOT:</li><ul><li>has reform feuillant_reform</li></ul><li>NOT:</li><ul><li>has reform damescrown_republic_reform</li></ul><li>NOT:</li><ul><li>has reform feiten_reformist_movement</li></ul>

###Efects:<ul><li>define ruler:</li><ul></ul><li>change statists vs orangists = -0.33</li></ul>

___
##A Republican Candidate

###Available if:
<li>has reform damescrown_republic_reform</li>

###Efects:<ul><li>define ruler:</li><ul></ul><li>change statists vs orangists = -0.33</li></ul>

___
##A Jacobin candidate.

###Available if:
<li>has reform feuillant_reform</li>

###Efects:<ul><li>define ruler:</li><ul></ul><li>add faction influence:</li><ul><li>faction = rr_jacobins</li><li>influence = 20</li></ul><li>change statists vs orangists = -0.33</li></ul>

___
##A Girondist candidate.

###Available if:
<li>has reform feuillant_reform</li>

###Efects:<ul><li>define ruler:</li><ul></ul><li>add faction influence:</li><ul><li>faction = rr_girondists</li><li>influence = 20</li></ul><li>change statists vs orangists = -0.33</li></ul>

___
##A Calasanni Candidate

###Available if:
<li>has reform damescrown_republic_reform</li>

###Efects:<ul><li>define ruler:</li><ul><li>dynasty = "Silcalas"</li></ul><li>change statists vs orangists = 0.33</li></ul>

___
##A Monarchist Candidate

###Available if:
<li>None of the following:</li><ul><li>Any of the following:</li><ul><li>has reform monastic_elections_reform</li><li>has reform  damescrown_republic_reform</li><li>has reform   feiten_reformist_movement</li></ul></ul>

###Efects:<ul><li>If has reform is feuillant reform:</li><ul><li>define ruler:</li><ul></ul></ul><li>Else if has tag is A62, and has tag is G97:</li><ul><li>define ruler:</li><ul><li>dynasty = "of Vanbury"</li></ul></ul><li>else:</li><ul><li>define ruler:</li><ul><li>dynasty = historic_dynasty</li></ul></ul><li>If has reform is feuillant reform:</li><ul><li>add faction influence:</li><ul><li>faction = rr_royalists</li><li>influence = 20</li></ul></ul><li>change statists vs orangists = 0.33</li></ul>

___
##A Militarist candidate.

###Available if:
<li>has reform monastic_elections_reform</li>

###Efects:<ul><li>define ruler:</li><ul></ul><li>change statists vs orangists = -0.33</li></ul>

___
##A Theocratic candidate.

###Available if:
<li>has reform monastic_elections_reform</li>

###Efects:<ul><li>define ruler:</li><ul></ul><li>change statists vs orangists = 0.33</li></ul>

___
##A Reformist Candidate

###Available if:
<li>has reform feiten_reformist_movement</li>

###Efects:<ul><li>define ruler:</li><ul><li>change adm = 1</li></ul><li>change statists vs orangists = -0.33</li><li>change innovativeness = 2</li><li>add estate loyalty:</li><ul><li>estate = estate_burghers</li><li>loyalty = -5</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_eunuchs</li><li>loyalty = -5</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_church</li><li>loyalty = -5</li></ul></ul>

___
##An Old Guard Candidate

###Available if:
<li>has reform feiten_reformist_movement</li>

###Efects:<ul><li>define ruler:</li><ul><li>change dip = 1</li><li>dynasty = ""</li></ul><li>change statists vs orangists = 0.33</li><li>change innovativeness = -2</li><li>add mercantilism excess to diplo power effect:</li><ul><li>VAL = 2</li></ul></ul>
