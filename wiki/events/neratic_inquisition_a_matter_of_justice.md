#Information
 - Title: Neratic Inquisition: A Matter of Justice
 - ID: vampires_estate_events.501
#Description
Neratic Inquisition: A Matter of Justice
#Mean Time to Happen:
Base time = 20 years
 - Multiplied by 0.75 if does not have estate loyalty has estate is estate church, and estate loyalty has loyalty is 30
 - Multiplied by 0.5 if does not have estate loyalty has estate is estate church, and estate loyalty has loyalty is 20
 - Multiplied by 0.75 if has any owned province has province modifier is aw vampires 1
 - Multiplied by 0.5 if has any owned province has province modifier is aw vampires 2
 - Multiplied by 0.25 if has any owned province has province modifier is aw vampires 3
 - Multiplied by 2 if has estate loyalty has estate is estate church, and estate loyalty has loyalty is 60
 - Multiplied by 4 if has estate loyalty has estate is estate church, and estate loyalty has loyalty is 80

#Options

___
##Allow the execution of the accused.

###Efects:<ul><li>add estate loyalty:</li><ul><li>estate = estate_vampires</li><li>loyalty = -10</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_church</li><li>influence = 5</li><li>desc = EST_VAMPIRES_PURGING_THE_SHADOWS</li><li>duration = 3650</li></ul></ul>

___
##We must stop this overreach!

###Efects:<ul><li>add estate loyalty:</li><ul><li>estate = estate_church</li><li>loyalty = -10</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_church</li><li>influence = -5</li><li>desc = EST_VAMPIRES_DENIED_OVERSIGHT</li><li>duration = 3650</li></ul></ul>

___
##Under my reign, the law is administered to all.

###Available if:
<li>Any of the following:</li><ul><li>ruler has personality is just_personality</li><li>ruler has personality  is lawgiver_personality</li><li>ruler has personality   is incorruptible_personality</li></ul>

###One of the following randomly happens:
Outcome 1:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>custom tooltip = ravenmarch_inquisition_trial_guilty</li><li>hidden effect:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_vampires</li><li>loyalty = 5</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_church</li><li>loyalty = 5</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_church</li><li>influence = 5</li><li>desc = EST_VAMPIRES_PURGING_THE_SHADOWS</li><li>duration = 3650</li></ul></ul></ul>
Outcome 2:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>custom tooltip = ravenmarch_inquisition_found_not_guilty</li><li>hidden effect:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_vampires</li><li>loyalty = 5</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_church</li><li>influence = 5</li><li>desc = EST_VAMPIRES_PURGING_THE_SHADOWS</li><li>duration = 3650</li></ul></ul></ul>
Outcome 3:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>custom tooltip = ravenmarch_inquisition_found_guilty_is_not_guilty</li><li>hidden effect:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_vampires</li><li>loyalty = -5</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_church</li><li>influence = 5</li><li>desc = EST_VAMPIRES_PURGING_THE_SHADOWS</li><li>duration = 3650</li></ul></ul></ul>
Outcome 4:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>custom tooltip = ravenmarch_inquisition_found_not_guilty_is_guilty</li><li>hidden effect:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_church</li><li>loyalty = -5</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_church</li><li>influence = -5</li><li>desc = EST_VAMPIRES_DENIED_OVERSIGHT</li><li>duration = 3650</li></ul></ul></ul>

###Efects:<ul><li>highlight = yes</li></ul>
