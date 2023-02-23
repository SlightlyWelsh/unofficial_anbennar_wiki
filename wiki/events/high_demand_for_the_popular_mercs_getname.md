#Information
 - Title: High Demand for the [popular_mercs.GetName]
 - ID: mercs.7
#Description
High Demand for the [popular_mercs.GetName]
#Options

___
##Encourage recruitment in [popular_mercs_origin.GetName].

###Efects:<ul><li>goto = popular_mercs_origin</li><li>event target:popular mercs origin:</li><ul><li>add base manpower = 1</li></ul></ul>

___
##Let the wealth flow.

###Available if:
<li>None of the following:</li><ul><li>event target:popular mercs origin:</li><ul><li>has province modifier popular_mercs_prosperity</li></ul></ul>

###Efects:<ul><li>goto = popular_mercs_origin</li><li>event target:popular mercs origin:</li><ul><li>add province modifier:</li><ul><li>name = "popular_mercs_prosperity"</li><li>duration = 7300</li></ul></ul></ul>
