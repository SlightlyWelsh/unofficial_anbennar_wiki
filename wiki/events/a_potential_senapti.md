#Information
 - Title: A Potential Senapti
 - ID: rahenraj.4
#Description
A Potential Senapti
#Options

___
##Their strength shall be recognised

###AI weighting:
AI weights this option at 100
 - Multiplied by 0 if has FROM has check variable has which is senaptiCandidateScore, and check variable has value is 1


###Efects:<ul><li>event target:next ai senapti:</li><ul><li>overlord:</li><ul><li>create subject:</li><ul><li>subject type = great_daimyo_vassal</li><li>subject = event_target:next_ai_senapti</li></ul></ul><li>add government reform = senapti_reform</li><li>hidden effect:</li><ul><li>clr country flag [potential_senapti](../flags/potential_senapti.md)</li><li>the event [Raja Promotes [Root.GetName] to Senapti](../events/raja_promotes_root_getname_to_senapti.md) happens</li></ul></ul><li>hidden effect:</li><ul><li>4411:</li><ul><li>change variable:</li><ul><li>rajNbSenapti = 1</li></ul></ul></ul></ul>

___
##We have enough Senaptia already!

###AI weighting:
AI weights this option at 100
 - Multiplied by 0 if does not have check variable has which is senaptiCandidateScore, and check variable has value is 1


###Efects:<ul><li>event target:next ai senapti:</li><ul><li>country gets the modifier prabhi_promotion_rejected for 180 days</li><li>hidden effect:</li><ul><li>clr country flag [potential_senapti](../flags/potential_senapti.md)</li><li>the event [Raja Denies Our Request](../events/raja_denies_our_request.md) happens</li></ul></ul></ul>
