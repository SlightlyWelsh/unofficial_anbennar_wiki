#Information
 - Title: Deputize the vizier to [vizier_destination.GetName]
 - ID: rahenraj.2117
#Description
Deputize the vizier to [vizier_destination.GetName]
#Options

___
##Tell the vizier to pack his bags

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>raj vizier sway change:</li><ul><li>amount = 5</li></ul><li>If random subject country has country flag is [raj_vizier](../flags/raj_vizier.md):</li><ul><li>the event [Deputized to [vizier_destination.GetName]](../events/deputized_to_vizier_destination_getname.md) happens</li></ul></ul>

___
##Send a delegation of advisors instead

###Available if:
<li>Any of the following:</li><ul><li>All of the following:</li><ul><li>employed advisor:</li><ul><li>category is ADM</li></ul><li>employed advisor:</li><ul><li>category is DIP</li></ul></ul><li>AND:</li><ul><li>employed advisor:</li><ul><li>category is DIP</li></ul><li>employed advisor:</li><ul><li>category is MIL</li></ul></ul><li>AND:</li><ul><li>employed advisor:</li><ul><li>category is MIL</li></ul><li>employed advisor:</li><ul><li>category is ADM</li></ul></ul></ul>

###AI weighting:
AI weights this option at 0


###One of the following randomly happens:
Outcome 1:

Available if <li>employed advisor:</li><ul><li>category is ADM</li></ul><li>employed advisor:</li><ul><li>category is DIP</li></ul>

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>remove advisor by category = ADM</li><li>remove advisor by category = DIP</li></ul>
Outcome 2:

Available if <li>employed advisor:</li><ul><li>category is DIP</li></ul><li>employed advisor:</li><ul><li>category is MIL</li></ul>

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>remove advisor by category = DIP</li><li>remove advisor by category = MIL</li></ul>
Outcome 3:

Available if <li>employed advisor:</li><ul><li>category is MIL</li></ul><li>employed advisor:</li><ul><li>category is ADM</li></ul>

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>remove advisor by category = MIL</li><li>remove advisor by category = ADM</li></ul>

###Efects:<ul><li>raj cohesion change absolute:</li><ul><li>amount = -5</li></ul><li>event target:vizier destination:</li><ul><li>country gets the modifier raj_raja_delegation for 5 years</li><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = raj_raja_delegation_opinion</li></ul><li>hidden effect:</li><ul><li>the event [A Delegation from the Raja](../events/a_delegation_from_the_raja.md) happens</li></ul></ul></ul>

___
##The Lotus Court cannot be bothered to care about such a minor area

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>raj cohesion change absolute:</li><ul><li>amount = -10</li></ul><li>event target:vizier destination:</li><ul><li>country gets the modifier raj_raja_neglected for 5 years</li><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = raj_raja_neglected_opinion</li></ul><li>hidden effect:</li><ul><li>the event [Neglected by the Raja](../events/neglected_by_the_raja.md) happens</li></ul></ul></ul>
