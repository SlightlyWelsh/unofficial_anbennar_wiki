#Information
 - Title: The szal-Fazil Arrive to [Root.GetName]
 - ID: new_sun_cult.243
#Description
The szal-Fazil Arrive to [Root.GetName]
#Options

___
##The szal-Fazil are no longer welcome in our country.

###Efects:<ul><li>custom tooltip = nsc_chosen_role_up_tt</li><li>add estate loyalty:</li><ul><li>estate = estate_church</li><li>loyalty = 10</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_church</li><li>desc = nsc_expelled_szal_fazil</li><li>influence = 10</li><li>duration = 7300</li></ul><li>add prestige = 10</li></ul>

___
##The szal-Fazil are our guests, and the Amman Magi is now a member of the court.

###Efects:<ul><li>custom tooltip = nsc_chosen_role_down_tt</li><li>set country flag [nsc_protected_amman_magi](../flags/nsc_protected_amman_magi.md)</li><li>define advisor:</li><ul><li>type = court_mage</li><li>name = "Amman Magi"</li><li>skill = 3</li><li>culture = masnsih</li><li>religion = old_bulwari_sun_cult</li><li>discount = yes</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_church</li><li>loyalty = -10</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_church</li><li>desc = nsc_protected_szal_fazil</li><li>influence = -10</li><li>duration = 7300</li></ul><li>add prestige = -10</li><li>hidden effect:</li><ul><li>If has government is monarchy:</li><ul><li>the event [An Offer from the Magi](../events/an_offer_from_the_magi.md) happens</li></ul></ul></ul>

___
##The szal-Fazil are our guests, and the Amman Magi will help our soldiers in battle.

###Efects:<ul><li>custom tooltip = nsc_chosen_role_down_tt</li><li>set country flag [nsc_protected_amman_magi](../flags/nsc_protected_amman_magi.md)</li><li>define general:</li><ul><li>name = "Amman Magi"</li><li>fire = 3</li><li>shock = 9</li><li>manuever = 3</li><li>siege = 3</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_church</li><li>loyalty = -10</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_church</li><li>desc = nsc_protected_szal_fazil</li><li>influence = -10</li><li>duration = 7300</li></ul><li>add prestige = -10</li><li>hidden effect:</li><ul><li>If has government is monarchy, and does not have reform is states general reform:</li><ul><li>the event [An Offer from the Magi](../events/an_offer_from_the_magi.md) happens</li></ul></ul></ul>
