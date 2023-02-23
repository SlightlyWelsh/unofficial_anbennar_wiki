#Information
 - Title: Heathens in High Places
 - ID: culture_religion_events.13
#Description
Heathens in High Places
#Mean Time to Happen:
Base time = 1 days

#Options

___
##It is time we let [Root.Adm_Advisor.GetName] go.

###Available if:
<li>has country flag [adm_advisor_heathen](../flags/adm_advisor_heathen.md)</li>

###Efects:<ul><li>remove advisor by category = ADM</li><li>add adm power = -25</li></ul>

___
##It is time we let [Root.Dip_Advisor.GetName] go.

###Available if:
<li>has country flag [dip_advisor_heathen](../flags/dip_advisor_heathen.md)</li>

###Efects:<ul><li>remove advisor by category = DIP</li><li>add dip power = -25</li></ul>

___
##It is time we let [Root.Mil_Advisor.GetName] go.

###Available if:
<li>has country flag [mil_advisor_heathen](../flags/mil_advisor_heathen.md)</li>

###Efects:<ul><li>remove advisor by category = MIL</li><li>add mil power = -25</li></ul>

___
##We do not bow to the demands of petty dilettantes.

###Efects:<ul><li>If has calc true if has all known country has religion group is ROOT; and calc true if has amount is 12:</li><ul><li>custom tooltip = culture_religion_events.13.e.tt</li><li>hidden effect:</li><ul><li>If every known country has religion group is ROOT:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = entertaining_heathens</li></ul></ul></ul></ul><li>else:</li><ul><li>If every known country has religion group is ROOT:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = entertaining_heathens</li></ul></ul></ul></ul>
