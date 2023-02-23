#Information
 - Title: Trouble in Kalib
 - ID: flavour_bulwar_tag.32
#Description
Trouble in Kalib
#Options

___
##Give them our full support!

###Efects:<ul><li>If has exists is F44:</li><ul><li>F44:</li><ul><li>the event [An offer from the Naqtazan](../events/an_offer_from_the_naqtazan.md) happens</li></ul><li>custom tooltip = bulwar_accept_offer_tt</li><li>tooltip:</li><ul><li>If is subject:</li><ul><li>F44:</li><ul><li>grant independence = yes</li></ul><li>vassalize = F44</li><li>event target:kalib overlord:</li><ul><li>declare war with cb:</li><ul><li>who = F44</li><li>casus belli = cb_vassalize_mission</li></ul></ul></ul><li>else:</li><ul><li>vassalize = F44</li></ul></ul></ul><li>else:</li><ul><li>add treasury = -50</li><li>600:</li><ul><li>add core = F44</li></ul><li>599:</li><ul><li>add core = F44</li><li>owner:</li><ul><li>If every owned province is core is F44:</li><ul><li>cede province = F44</li></ul></ul></ul><li>vassalize = F44</li><li>event target:kalib overlord:</li><ul><li>declare war with cb:</li><ul><li>who = F44</li><li>casus belli = cb_vassalize_mission</li></ul></ul><li>hidden effect:</li><ul><li>remove opinion:</li><ul><li>who = F44</li><li>modifier = nsc_suspicious_behaviour</li></ul><li>remove opinion:</li><ul><li>who = F44</li><li>modifier = nsc_suspicious_behaviour_big</li></ul><li>reverse remove opinion:</li><ul><li>who = F44</li><li>modifier = nsc_suspicious_behaviour</li></ul><li>reverse remove opinion:</li><ul><li>who = F44</li><li>modifier = nsc_suspicious_behaviour_big</li></ul></ul></ul></ul>

___
##Just give the a nudge.

###Available if:
<li>F44:</li><ul><li>exists</li><li>is subject</li></ul>

###Efects:<ul><li>F44:</li><ul><li>add liberty desire = 50</li></ul></ul>

___
##It's too risky...

###Available if:
<li>F44:</li><ul><li>None of the following:</li><ul><li>exists</li></ul></ul>

###Efects:<ul><li>add prestige = -5</li></ul>
