#Information
 - Title: The Outcome of the Expeditions
 - ID: new_sun_cult.158
#Description
The Outcome of the Expeditions
#Options

___
##Aelantir awaits us! Praise the Sun!

###Available if:
<li>incident variable value:</li><ul><li>incident is incident_call_of_aelantir</li><li>value is at least 4</li></ul>

###Efects:<ul><li>country gets the modifier nsc_high_aelantir_enthusiasm for 50 years</li><li>decrease nsc isolation level = yes</li><li>end incident = incident_call_of_aelantir</li></ul>

___
##At least something good came of all this, in the end

###Available if:
<li>None of the following:</li><ul><li>incident variable value:</li><ul><li>incident is incident_call_of_aelantir</li><li>value is at least 4</li></ul></ul><li>incident variable value:</li><ul><li>incident is incident_call_of_aelantir</li><li>value is -2</li></ul>

###Efects:<ul><li>country gets the modifier nsc_moderate_aelantir_enthusiasm for 50 years</li><li>end incident = incident_call_of_aelantir</li></ul>

___
##The adventurers will calm down. The elves that are left will have to pick up the pieces

###Available if:
<li>None of the following:</li><ul><li>incident variable value:</li><ul><li>incident is incident_call_of_aelantir</li><li>value is -2</li></ul></ul>

###Efects:<ul><li>country gets the modifier nsc_low_aelantir_enthusiasm for 50 years</li><li>increase nsc isolation level = yes</li><li>end incident = incident_call_of_aelantir</li></ul>
