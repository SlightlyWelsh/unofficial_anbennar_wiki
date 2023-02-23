#Information
 - Title: The Council of Medurubar Comes to a Close
 - ID: new_sun_cult.142
#Description
The Council of Medurubar Comes to a Close
#Options

___
##Keep those fires burning all night! For we celebrate Surael's Glory!

###Available if:
<li>REB:</li><ul><li>check variable:</li><ul><li>which is nscUnityVar</li><li>value is at least 600</li></ul></ul>

###Efects:<ul><li>remove country modifier = nsc_divided_cult</li><li>remove country modifier = nsc_big_council</li><li>remove country modifier = nsc_medium_council</li><li>remove country modifier = nsc_small_council</li><li>If has tag is F37:</li><ul><li>country gets the modifier nsc_unified_cult for 50 years</li></ul></ul>

___
##This is what we expected. Let the celebrations begin.

###Available if:
<li>REB:</li><ul><li>None of the following:</li><ul><li>check variable:</li><ul><li>which is nscUnityVar</li><li>value is at least 600</li></ul></ul><li>check variable:</li><ul><li>which is nscUnityVar</li><li>value is at least 300</li></ul></ul>

###Efects:<ul><li>remove country modifier = nsc_divided_cult</li><li>remove country modifier = nsc_big_council</li><li>remove country modifier = nsc_medium_council</li><li>remove country modifier = nsc_small_council</li><li>country gets the modifier nsc_restructuring_cult for 25 years</li></ul>

___
##This is a dark day for us all. But with faith in Surael, we shall make it through the night.

###Available if:
<li>REB:</li><ul><li>None of the following:</li><ul><li>check variable:</li><ul><li>which is nscUnityVar</li><li>value is at least 300</li></ul></ul></ul>

###Efects:<ul><li>hidden effect:</li><ul><li>remove country modifier = nsc_divided_cult</li></ul><li>country gets the modifier nsc_divided_cult for 25 years</li><li>remove country modifier = nsc_big_council</li><li>remove country modifier = nsc_medium_council</li><li>remove country modifier = nsc_small_council</li><li>country gets the modifier nsc_autonomous_clergy for 25 years</li></ul>
