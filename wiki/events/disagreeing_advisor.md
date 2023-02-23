#Information
 - Title: Disagreeing Advisor
 - ID: 878
#Description
Disagreeing Advisor
#Mean Time to Happen:
Base time = 1 days

#Options

___
##But it was a good point...

###Efects:<ul><li>add prestige = -10</li><li>trigger switch:</li><ul><li>on trigger = has_country_flag</li><li>advisor events adm:</li><ul><li>add adm power = 25</li></ul><li>advisor events dip:</li><ul><li>add dip power = 25</li></ul><li>advisor events mil:</li><ul><li>add mil power = 25</li></ul></ul></ul>

___
##Off with [Root.GetEventAdvisorHerHis] head!

###Efects:<ul><li>reduce meritocracy effect = yes</li><li>trigger switch:</li><ul><li>on trigger = has_country_flag</li><li>advisor events adm:</li><ul><li>kill advisor by category effect:</li><ul><li>ADM = yes</li></ul></ul><li>advisor events dip:</li><ul><li>kill advisor by category effect:</li><ul><li>DIP = yes</li></ul></ul><li>advisor events mil:</li><ul><li>kill advisor by category effect:</li><ul><li>MIL = yes</li></ul></ul></ul><li>If has country flag is [tyrant_system_initialized](../flags/tyrant_system_initialized.md):</li><ul><li>increase tyrant ruthless 1 = yes</li></ul></ul>
