#Information
 - Title: Of Pistons and Flames: Local Suspicions
 - ID: flavor_feiten.231
#Description
Of Pistons and Flames: Local Suspicions
#Options

___
##Perhaps an injection into their treasury will help them look the other way?

###Efects:<ul><li>add treasury = -5000</li><li>event target:feiten of pistons and flames owner province:</li><ul><li>add treasury = 5000</li></ul><li>set country flag [feiten_of_pistons_and_flames_bribed](../flags/feiten_of_pistons_and_flames_bribed.md)</li><li>event target:feiten of pistons and flames owner province:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = sent_gift</li></ul></ul><li>custom tooltip = flavor_feiten.231.parameters</li></ul>

___
##We must send an envoy to smooth things over

###Efects:<ul><li>add dip power = -100</li><li>event target:feiten of pistons and flames owner province:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = feiten_of_pistons_and_steam_sent_envoy_op_mod</li></ul></ul><li>set country flag [feiten_of_pistons_and_flames_envoy](../flags/feiten_of_pistons_and_flames_envoy.md)</li><li>country gets the modifier feiten_the_steam_engine_sent_envoy for 2 years</li><li>custom tooltip = flavor_feiten.231.parameters</li></ul>

___
##What do we care what they think?

###Efects:<ul><li>custom tooltip = flavor_feiten.231.parameters</li><li>event target:feiten of pistons and flames owner province:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = opinion_confront_spies</li></ul></ul></ul>
