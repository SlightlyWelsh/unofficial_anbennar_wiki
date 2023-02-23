#Information
 - Title: Infighting in [fightingProv.GetName]
 - ID: flavor_castanor.216
#Description
Infighting in [fightingProv.GetName]
#Options

___
##Let them fight it out...

###One of the following randomly happens:
Outcome 1:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>If has tag is B61:</li><ul><li>add prestige = 10</li><li>add yearly manpower = 0.5</li></ul><li>else:</li><ul><li>add prestige = -5</li><li>event target:fightingProv:</li><ul><li>add base tax = -1</li></ul></ul></ul>
Outcome 2:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>If has tag is B61:</li><ul><li>add prestige = -5</li><li>event target:fightingProv:</li><ul><li>add base tax = -1</li></ul></ul><li>else:</li><ul><li>add prestige = 10</li><li>add yearly manpower = 0.5</li></ul></ul>
Outcome 3:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>event target:fightingProv:</li><ul><li>add unrest = 10</li><li>add devastation = 20</li></ul></ul>

___
##Enough - put them down.

###Efects:<ul><li>add mil power = -33</li></ul>
