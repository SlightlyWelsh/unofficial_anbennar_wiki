#Information
 - Title: Petition for Membership
 - ID: incident_generic.1
#Description
Petition for Membership
#Mean Time to Happen:
Base time = 120 months

#Options

___
##We shall take this to the Imperial Diet.

###AI weighting:
AI weights this option at 10


###Efects:<ul><li>set imperial incident = incident_pu_subject_joins_empire</li><li>event target:pu hre country:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = petitioned_for_hre_membership</li></ul></ul></ul>

___
##Thre is no need to include [pu_hre_country.GetName].

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>event target:pu hre country:</li><ul><li>set country flag [pu_hre_rejected_flag](../flags/pu_hre_rejected_flag.md)</li></ul><li>add prestige = -5</li><li>custom tooltip = reject_hre_pu_tt</li><li>event target:pu hre country:</li><ul><li>clr country flag [current_pu_incident_target_flag](../flags/current_pu_incident_target_flag.md)</li><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = no_petition_for_hre_membership</li></ul></ul></ul>


#Pages with same name:
The following pages have the same name as this page:
 - [petition_for_membership_1](petition_for_membership_1.md)
