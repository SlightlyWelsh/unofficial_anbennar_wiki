#Information
 - Title: Reactionaries!
 - ID: diggy_remnant_stagnation.3
#Description
Reactionaries!
#Options

___
##Follow their demands

###Available if:
<li>is controlled by the AI</li>

###AI weighting:
AI weights this option at 500


###One of the following randomly happens:
Outcome 1:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>subtract variable:</li><ul><li>awakeningArmy = 20</li></ul></ul>
Outcome 2:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>subtract variable:</li><ul><li>awakeningDig = 20</li></ul></ul>
Outcome 3:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>subtract variable:</li><ul><li>awakeningColonial = 20</li></ul></ul>

###Efects:<ul><li>set variable:</li><ul><li>awakeningReact = 20</li></ul><li>random:</li><ul><li>chance = 50</li><li>add stability or adm power = yes</li></ul></ul>

___
##Follow their demands

###Available if:
<li>is not controlled by the AI</li>

###AI weighting:
AI weights this option at 5


###Efects:<ul><li>custom tooltip = remnant_react_follow_demand_tooltip</li><li>capital scope:</li><ul><li>random list:</li><ul><li>25:</li><ul><li>add base tax = 1</li></ul><li>25:</li><ul><li>add base production = 1</li></ul><li>25:</li><ul><li>add base manpower = 1</li></ul><li>25:</li><ul><li>modifier:</li><ul><li>factor = 2</li><li>development = 30</li></ul><li>modifier:</li><ul><li>factor = 3</li><li>development = 40</li></ul></ul></ul></ul><li>hidden effect:</li><ul><li>subtract variable:</li><ul><li>awakeningReact = 30</li></ul><li>subtract variable:</li><ul><li>awakeningArmy = 40</li></ul><li>subtract variable:</li><ul><li>awakeningDig = 40</li></ul><li>subtract variable:</li><ul><li>awakeningColonial = 40</li></ul></ul></ul>

___
##Pretend to oblige

###Available if:
<li>is not controlled by the AI</li>

###AI weighting:
AI weights this option at 50


###One of the following randomly happens:
Outcome 1:

Available if <li>Any of the following:</li><ul><li>has country modifier remnant_appeasement_tax</li><li>has country modifier  remnant_appeasement_production</li><li>has country modifier   remnant_appeasement_manpower</li></ul>

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>reduce stability or adm power = yes</li><li>add adm power = -25</li><li>add dip power = -25</li><li>add mil power = -25</li></ul>
Outcome 2:

Available if <li>None of the following:</li><ul><li>has country modifier remnant_appeasement_tax</li></ul>

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>country gets the modifier remnant_appeasement_tax for 10 years</li></ul>
Outcome 3:

Available if <li>None of the following:</li><ul><li>has country modifier remnant_appeasement_production</li></ul>

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>country gets the modifier remnant_appeasement_production for 10 years</li></ul>
Outcome 4:

Available if <li>None of the following:</li><ul><li>has country modifier remnant_appeasement_manpower</li></ul>

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>country gets the modifier remnant_appeasement_manpower for 10 years</li></ul>
Outcome 5:

Available if <li>None of the following:</li><ul><li>has country modifier remnant_appeasement_buildspeed</li></ul>

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>country gets the modifier remnant_appeasement_buildspeed for 10 years</li></ul>
Outcome 6:

Available if <li>capital scope:</li><ul><li>infantry in province is at least 2</li></ul>

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>capital scope:</li><ul><li>kill units:</li><ul><li>who = ROOT</li><li>type = infantry</li><li>amount = 2</li></ul></ul></ul>
Outcome 7:

Available if <li>None of the following:</li><ul><li>has country modifier remnant_appeasement_colonization</li></ul>

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>country gets the modifier remnant_appeasement_colonization for 25 years</li></ul>
Outcome 8:

Available if <li>None of the following:</li><ul><li>has country modifier remnant_appeasement_morale</li></ul>

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>country gets the modifier remnant_appeasement_morale for 25 years</li></ul>
Outcome 9:

Available if <li>None of the following:</li><ul><li>has country modifier remnant_appeasement_dev</li></ul>

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>country gets the modifier remnant_appeasement_dev for 25 years</li></ul>

###Efects:<ul><li>custom tooltip = remnant_react_appease_tooltip</li><li>hidden effect:</li><ul><li>subtract variable:</li><ul><li>awakeningReact = 40</li></ul></ul></ul>

___
##Purge them!

###Available if:
<li>is not controlled by the AI</li>

###AI weighting:
AI weights this option at 20


###Efects:<ul><li>reduce stability or adm power = yes</li><li>capital scope:</li><ul><li>spawn rebels:</li><ul><li>type = noble_rebels</li><li>size = 0.5</li></ul><li>random:</li><ul><li>chance = 50</li><li>spawn rebels:</li><ul><li>type = noble_rebels</li><li>size = 0.25</li></ul></ul></ul><li>custom tooltip = remnant_react_purge_tooltip</li><li>hidden effect:</li><ul><li>set variable:</li><ul><li>awakeningReact = 0</li></ul></ul></ul>
