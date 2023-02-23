This page has the same name as others. For full listing see bottom of [the base page](petition_for_membership.md).

#Information
 - Title: Petition for Membership
 - ID: incident_generic.2
#Description
Petition for Membership
#Options

___
##[current_pu_incident_target.GetName] shall join the Empire.

###AI weighting:
AI weights this option at 10
 - Multiplied by 0 if is rival is FROM, and has FROM is rival is ROOT


###Efects:<ul><li>event target:current pu incident target:</li><ul><li>set in empire = yes</li><li>overlord:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = opinion_added_pu_subject_hre</li></ul></ul></ul></ul>

___
##We do not accept this application.

###AI weighting:
AI weights this option at 1
 - Multiplied by 1000 if is rival is FROM, and has FROM is rival is ROOT


###Efects:<ul><li>event target:current pu incident target:</li><ul><li>set country flag [pu_hre_rejected_flag](../flags/pu_hre_rejected_flag.md)</li><li>overlord:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = opinion_denied_pu_subject_hre</li></ul></ul></ul></ul>
