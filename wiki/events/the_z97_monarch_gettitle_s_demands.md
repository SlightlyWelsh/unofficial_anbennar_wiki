#Information
 - Title: The [Z97.Monarch.GetTitle]'s Demands
 - ID: new_court_flavour_events.40
#Description
The [Z97.Monarch.GetTitle]'s Demands
#Options

___
##Hand [Root.GetEventAdvisorHerHim] over.

###AI weighting:
AI weights this option at 2
 - Multiplied by 2 if has opinion has who is PAP, and has opinion has value is 50
 - Multiplied by 2 if has opinion has who is PAP, and has opinion has value is 100
 - Multiplied by 0.5 if does not have opinion has who is PAP, and has opinion has value is -50
 - Multiplied by 0.5 if has num of owned provinces with has value is 5, and num of owned provinces with has religion group is root, and does not have religion is root


###Efects:<ul><li>trigger switch:</li><ul><li>on trigger = has_country_flag</li><li>advisor events adm:</li><ul><li>remove advisor by category = ADM</li></ul><li>advisor events dip:</li><ul><li>remove advisor by category = DIP</li></ul><li>advisor events mil:</li><ul><li>remove advisor by category = MIL</li></ul></ul><li>country gets the modifier handed_over_heretic for 15 years</li><li>PAP:</li><ul><li>add opinion:</li><ul><li>who = root</li><li>modifier = opinion_bowed_to_papal_demand_advisor</li></ul><li>hidden effect:</li><ul><li>the event [[heathen_advisor_country.GetUsableName] Complies with our Demands](../events/heathen_advisor_country_getusablename_complies_with_our_demands.md) happens</li></ul></ul><li>add estate influence modifier:</li><ul><li>estate = estate_church</li><li>desc = EST_VAL_ACCEPTED_POPE_DEMANDS</li><li>influence = 10</li><li>duration = 5475</li></ul></ul>

___
##We will not bow to Rectorate pressure.

###Efects:<ul><li>PAP:</li><ul><li>add opinion:</li><ul><li>who = root</li><li>modifier = opinion_rejected_papal_demand_advisor</li></ul><li>hidden effect:</li><ul><li>the event [[heathen_advisor_country.GetUsableName] Defies our Authority](../events/heathen_advisor_country_getusablename_defies_our_authority.md) happens</li></ul></ul><li>add papal influence = -20</li><li>reduce estate church loyalty effect = yes</li></ul>
