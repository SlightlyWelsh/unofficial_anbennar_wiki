This page has the same name as others. For full listing see bottom of [the base page](the_sirtan_offer_a_deal.md).

#Information
 - Title: The Sirtan Offer A Deal
 - ID: khom_civilwar.24
#Description
The Sirtan Offer A Deal
#Options

___
##Accept the deal

###AI weighting:
AI weights this option at 75


###Efects:<ul><li>custom tooltip = khom_civilwar_accept_sirtan_offer_tt</li><li>set global flag [khom_civilwar_sirtan_joins_honsai](../flags/khom_civilwar_sirtan_joins_honsai.md)</li><li>country gets the modifier khom_civilwar_friendly_raiders for 25 years</li><li>add opinion:</li><ul><li>who = Y73</li><li>modifier = khom_civilwar_struck_a_deal</li></ul><li>reverse add opinion:</li><ul><li>who = Y73</li><li>modifier = khom_civilwar_struck_a_deal</li></ul><li>hidden effect:</li><ul><li>Y73:</li><ul><li>the event [Hon Sai Accepts](../events/hon_sai_accepts.md) happens</li></ul></ul></ul>

___
##We refuse to work with savages

###AI weighting:
AI weights this option at 25


###Efects:<ul><li>Y73:</li><ul><li>set country flag [khom_civilwar_honsai_refuses_sirtan](../flags/khom_civilwar_honsai_refuses_sirtan.md)</li></ul><li>reverse add opinion:</li><ul><li>who = Y73</li><li>modifier = khom_civilwar_spurned_offer</li></ul><li>hidden effect:</li><ul><li>Y73:</li><ul><li>the event [Our Offer Was Spurned](../events/our_offer_was_spurned.md) happens</li></ul></ul></ul>
