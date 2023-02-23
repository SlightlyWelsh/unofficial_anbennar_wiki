#Information
 - Title: Heretic Advisor
 - ID: 5094
#Description
Heretic Advisor
#Mean Time to Happen:
Base time = 1 days
 - Multiplied by 2.0 if does not have statesman is 1; and does not have innovativeness ideas is 2
 - Multiplied by 0.5 if is lucky
 - Multiplied by 0.66 if has statesman is 3

#Options

___
##Fire [Root.GetEventAdvisorHerHim]!

###AI weighting:
AI weights this option at 40


###Efects:<ul><li>reduce meritocracy effect = yes</li><li>trigger switch:</li><ul><li>on trigger = has_country_flag</li><li>advisor events adm:</li><ul><li>remove advisor by category = ADM</li></ul><li>advisor events dip:</li><ul><li>remove advisor by category = DIP</li></ul><li>advisor events mil:</li><ul><li>remove advisor by category = MIL</li></ul></ul><li>add estate church loyalty effect = yes</li></ul>

___
##We have faith in [Root.GetEventAdvisorHerHim].

###AI weighting:
AI weights this option at 60
 - Multiplied by 0 if has estate is estate church, and does not have estate loyalty has estate is estate church, and estate loyalty has loyalty is 30


###Efects:<ul><li>add prestige = -10</li><li>reduce estate church loyalty effect = yes</li><li>If has country flag is [tyrant_system_initialized](../flags/tyrant_system_initialized.md):</li><ul><li>increase tyrant benevolent 1 = yes</li></ul></ul>
