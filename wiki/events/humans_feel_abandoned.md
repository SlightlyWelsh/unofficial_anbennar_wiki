#Information
 - Title: Humans Feel Abandoned
 - ID: new_sun_cult.155
#Description
Humans Feel Abandoned
#Options

___
##They can join them and leave for Aelantir too!

###AI weighting:
AI weights this option at 1
 - Multiplied by 100 if has personality is ai colonialist


###Efects:<ul><li>custom tooltip = nsc_chosen_role_down_tt</li><li>add incident variable value:</li><ul><li>incident = incident_call_of_aelantir</li><li>value = 1</li></ul><li>If random owned province does not have province flag is [nsc_lost_dev](../flags/nsc_lost_dev.md); and  has culture is human is yes, and  has religion is bulwari sun cult:</li><ul><li>add base tax = -1</li><li>add base production = -1</li><li>add base manpower = -1</li><li>set province flag [nsc_lost_dev](../flags/nsc_lost_dev.md)</li></ul><li>If random owned province does not have province flag is [nsc_lost_dev](../flags/nsc_lost_dev.md); and  has culture is human is yes, and  has religion is bulwari sun cult:</li><ul><li>add base tax = -1</li><li>add base production = -1</li><li>add base manpower = -1</li><li>set province flag [nsc_lost_dev](../flags/nsc_lost_dev.md)</li></ul></ul>

___
##Unfortunately, there is nothing we can do about that...

###AI weighting:
AI weights this option at 9


###Efects:<ul><li>reduce stability or adm power = yes</li></ul>

___
##The Chosen leaving means that more opportunities are available for those who remain!

###Available if:
<li>None of the following:</li><ul><li>isolationism is at least 2</li></ul>

###AI weighting:
AI weights this option at 90


###Efects:<ul><li>highlight = yes</li><li>custom tooltip = nsc_chosen_role_up_tt</li><li>add incident variable value:</li><ul><li>incident = incident_call_of_aelantir</li><li>value = -1</li></ul><li>country gets the modifier nsc_new_opportunities for 10 years</li></ul>
