#Information
 - Title: [Root.Monarch.GetName]'s Stance on the Cult
 - ID: new_sun_cult.143
#Description
[Root.Monarch.GetName]'s Stance on the Cult
#Options

___
##They shall tremble before the Light of Surael!

###Available if:
<li>incident variable value:</li><ul><li>incident is incident_death_of_taelarios</li><li>value is at least 2</li></ul>

###Efects:<ul><li>country gets the modifier nsc_zealous_stance for 25 years</li><li>increase nsc isolation level = yes</li><li>end incident = incident_death_of_taelarios</li></ul>

___
##They will come around in time, and we will be waiting for them in the Light.

###Available if:
<li>None of the following:</li><ul><li>incident variable value:</li><ul><li>incident is incident_death_of_taelarios</li><li>value is at least 2</li></ul></ul><li>incident variable value:</li><ul><li>incident is incident_death_of_taelarios</li><li>value is -2</li></ul>

###Efects:<ul><li>country gets the modifier nsc_moderate_stance for 25 years</li><li>end incident = incident_death_of_taelarios</li></ul>

___
##We do not need to bother with them - their fates will be decided by Surael.

###Available if:
<li>None of the following:</li><ul><li>incident variable value:</li><ul><li>incident is incident_death_of_taelarios</li><li>value is -2</li></ul></ul>

###Efects:<ul><li>country gets the modifier nsc_tolerant_stance for 25 years</li><li>decrease nsc isolation level = yes</li><li>end incident = incident_death_of_taelarios</li></ul>
