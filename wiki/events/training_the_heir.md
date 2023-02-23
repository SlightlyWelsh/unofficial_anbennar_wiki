#Information
 - Title: Training The Heir
 - ID: flavor_blademarches.11
#Description
Training The Heir
#Mean Time to Happen:
Base time = 1 years

#Options

___
##They're fine, don't bother

###AI weighting:
AI weights this option at 50
 - Multiplied by 2 if has heir mil is 5
 - Multiplied by 0 if does not have legitimacy is 90


###Efects:<ul><li>reduce legitimacy medium effect = yes</li><li>hidden effect:</li><ul><li>set heir flag [not_trained_heir_calindal](../flags/not_trained_heir_calindal.md)</li></ul></ul>

___
##Occasionally train with the Blade Stewards

###AI weighting:
AI weights this option at 50
 - Multiplied by 2 if does not have heir mil is 3


###One of the following randomly happens:
Outcome 1:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>decrease heir adm effect = yes</li></ul>
Outcome 2:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>decrease heir dip effect = yes</li></ul>

###Efects:<ul><li>random:</li><ul><li>chance = 66</li><li>increase heir mil effect = yes</li></ul><li>hidden effect:</li><ul><li>set heir flag [trained_heir_calindal](../flags/trained_heir_calindal.md)</li></ul><li>custom tooltip = training_heir_tooltip</li></ul>

___
##Dedicate our heir's education with the Blade Stewards

###AI weighting:
AI weights this option at 50
 - Multiplied by 2 if does not have heir mil is 2


###One of the following randomly happens:
Outcome 1:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>decrease heir adm effect = yes</li></ul>
Outcome 2:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>decrease heir dip effect = yes</li></ul>
Outcome 3:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>If has heir adm is 2:</li><ul><li>change heir adm = -2</li></ul><li>Else if has heir adm is 1:</li><ul><li>change heir adm = -1</li><li>add adm power = -50</li></ul><li>else:</li><ul><li>add adm power = -100</li></ul></ul>
Outcome 4:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>If has heir dip is 2:</li><ul><li>change heir dip = -2</li></ul><li>Else if has heir dip is 1:</li><ul><li>change heir dip = -1</li><li>add dip power = -50</li></ul><li>else:</li><ul><li>add dip power = -100</li></ul></ul>

###Efects:<ul><li>random:</li><ul><li>chance = 75</li><li>If has heir mil is 6:</li><ul><li>add mil power = 100</li></ul><li>Else if has heir mil is 5:</li><ul><li>change heir mil = 1</li><li>add mil power = 50</li></ul><li>else:</li><ul><li>change heir mil = 2</li></ul></ul><li>hidden effect:</li><ul><li>set heir flag [trained_heir_calindal](../flags/trained_heir_calindal.md)</li></ul><li>custom tooltip = training_heir_tooltip</li></ul>
