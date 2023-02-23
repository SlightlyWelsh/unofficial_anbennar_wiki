#Information
 - Title: An Elephantine Issue
 - ID: rahenraj.2114
#Description
An Elephantine Issue
#Options

___
##Execute the elephants!

###AI weighting:
AI weights this option at 10
 - Multiplied by 0.01 if does not have opinion has who is FROM, and has opinion has value is 0
 - Multiplied by 2 if has opinion has who is FROM, and has opinion has value is 50
 - Multiplied by 2 if has opinion has who is FROM, and has opinion has value is 100
 - Multiplied by 2 if has opinion has who is FROM, and has opinion has value is 150
 - Multiplied by 2 if has FROM has army strength has who is ROOT, and army strength has value is 0.2
 - Multiplied by 2 if has FROM has total development is 100
 - Multiplied by 2 if has FROM has total development is 200
 - Multiplied by 0.5 if has 4411 has check variable has which is vizierSway, and check variable has value is 60
 - Multiplied by 0.5 if has 4411 has check variable has which is vizierSway, and check variable has value is 80
 - Multiplied by 0.5 if has FROM has country flag is [raj_vizier_risky_option](../flags/raj_vizier_risky_option.md)


###Efects:<ul><li>raj vizier sway change:</li><ul><li>amount = 5</li></ul><li>reverse add opinion:</li><ul><li>who = FROM</li><li>modifier = raj_granted_vizier_demands</li></ul><li>If every known country has culture is ghavaanaj:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = raj_executed_elephant</li></ul></ul><li>country gets the modifier raj_angered_elephant_riders for 10 years</li></ul>

___
##Banish the trainers!

###AI weighting:
AI weights this option at 80
 - Multiplied by 0 if does not have check variable has which is raj cohesion, and check variable has value is 40
 - Multiplied by 0 if has 4411 has check variable has which is vizierSway, and check variable has value is 80


###Efects:<ul><li>raj cohesion change absolute:</li><ul><li>amount = -10</li></ul></ul>

___
##Reject the request

###AI weighting:
AI weights this option at 10
 - Multiplied by 0.5 if does not have check variable has which is raj cohesion, and check variable has value is 30
 - Multiplied by 0 if does not have check variable has which is raj cohesion, and check variable has value is 20
 - Multiplied by 8 if has 4411 has check variable has which is vizierSway, and check variable has value is 80


###Efects:<ul><li>raj vizier sway change:</li><ul><li>amount = -5</li></ul><li>raj cohesion change absolute:</li><ul><li>amount = -15</li></ul><li>reverse add opinion:</li><ul><li>who = FROM</li><li>modifier = raj_rejected_vizier_demands</li></ul></ul>
