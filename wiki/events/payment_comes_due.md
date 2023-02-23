#Information
 - Title: Payment Comes Due
 - ID: flavor_castanor.222
#Description
Payment Comes Due
#Options

___
##The patricians always settle their debts.

###Efects:<ul><li>every country:</li><ul><li>If has country flag is [patrician_castanor_hostile_ally](../flags/patrician_castanor_hostile_ally.md):</li><ul><li>ROOT:</li><ul><li>add manpower = -7.5</li></ul></ul><li>Else if has country flag is [patrician_castanor_rivalled_ally](../flags/patrician_castanor_rivalled_ally.md):</li><ul><li>ROOT:</li><ul><li>add treasury = -750</li></ul></ul><li>Else if has country flag is [patrician_castanor_threatened_ally](../flags/patrician_castanor_threatened_ally.md):</li><ul><li>add truce with = ROOT</li></ul></ul></ul>

___
##Are you crazy? They ask for too much.

###Efects:<ul><li>If every country has country flag is [patrician_castanor_hostile_ally](../flags/patrician_castanor_hostile_ally.md), and has country flag is patrician castanor rivalled ally, and has country flag is patrician castanor threatened ally:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = castanor_reneged_on_support</li></ul></ul><li>country gets the modifier castanor_reneged_on_support_mod for 10 years</li></ul>
