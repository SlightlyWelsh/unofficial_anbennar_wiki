#Information
 - Title: Foreign Talent
 - ID: army_professionalism_events.6
#Description
Foreign Talent
#Options

___
##Hire [professional_country.GetAdjective] officers

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>If has monthly income is 10:</li><ul><li>add years of income = -0.5</li></ul><li>else:</li><ul><li>add treasury = -60</li></ul><li>add army professionalism = 0.05</li><li>event target:professional country:</li><ul><li>add opinion:</li><ul><li>modifier = hired_defectors</li><li>who = ROOT</li></ul><li>hidden effect:</li><ul><li>random list:</li><ul><li>25:</li><ul><li>the event [Infiltration of [From.GetName]](../events/infiltration_of_from_getname.md) happens</li></ul><li>75:</li><ul></ul></ul></ul></ul></ul>

___
##Let us continue to rely on our own people.

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>event target:professional country:</li><ul><li>add opinion:</li><ul><li>modifier = refused_to_hire_defectors</li><li>who = ROOT</li></ul></ul></ul>
