#Information
 - Title: An Offer for Marrhold
 - ID: flavor_mithradhum.103
#Description
An Offer for Marrhold
#Options

___
##Let them seize the hold, for a price.

###Available if:
<li>None of the following:</li><ul><li>capital is at least 4097</li></ul>

###AI weighting:
AI weights this option at 99


###Efects:<ul><li>add treasury = 2000</li><li>4097:</li><ul><li>cede province = FROM</li><li>add core = FROM</li></ul><li>FROM:</li><ul><li>the event [Offer for Marrhold Accepted](../events/offer_for_marrhold_accepted.md) happens</li></ul></ul>

___
##Allow them to fund an excavation.

###Available if:
<li>owns 4097</li>

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>set country flag [marrhold_tunnel_decision_taken](../flags/marrhold_tunnel_decision_taken.md)</li><li>4097:</li><ul><li>add great project:</li><ul><li>type = marrhold_tunnel</li><li>instant = yes</li></ul></ul><li>FROM:</li><ul><li>the event [[From.GetName] Makes Tunnel Instead](../events/from_getname_makes_tunnel_instead.md) happens</li></ul></ul>

___
##Tell the Dwarves to get lost!

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>FROM:</li><ul><li>the event [Offer for Marrhold Declined](../events/offer_for_marrhold_declined.md) happens</li></ul></ul>
