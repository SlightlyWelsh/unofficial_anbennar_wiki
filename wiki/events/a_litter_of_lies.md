#Information
 - Title: A Litter Of Lies
 - ID: estate_castes_events.117
#Description
A Litter Of Lies
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Keep it a secret, it would be a shame for the state as well!

###Efects:<ul><li>caste fluidity decrease small = yes</li><li>add adm power = -25</li><li>add estate loyalty:</li><ul><li>estate = estate_uppercastes</li><li>loyalty = 5</li></ul></ul>

___
##Even a low caste person can climb to greatness, he is proof of it!

###Efects:<ul><li>caste fluidity increase small = yes</li><li>If has country flag is [target_human_advisor](../flags/target_human_advisor.md):</li><ul><li>small increase of human tolerance effect = yes</li></ul><li>Else if has country flag is [target_harimari_advisor](../flags/target_harimari_advisor.md):</li><ul><li>small increase of harimari tolerance effect = yes</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_uppercastes</li><li>loyalty = -10</li></ul></ul>

___
##Fire the fool and condemn him harshly for his lies!

###Efects:<ul><li>caste fluidity decrease medium = yes</li><li>add legitimacy = 10</li><li>trigger switch:</li><ul><li>on trigger = has_country_flag</li><li>target adm advisor:</li><ul><li>remove advisor by category = ADM</li></ul><li>target dip advisor:</li><ul><li>remove advisor by category = DIP</li></ul><li>target mil advisor:</li><ul><li>remove advisor by category = MIL</li></ul></ul><li>If has country flag is [target_human_advisor](../flags/target_human_advisor.md):</li><ul><li>small decrease of human tolerance effect = yes</li></ul><li>Else if has country flag is [target_harimari_advisor](../flags/target_harimari_advisor.md):</li><ul><li>small decrease of harimari tolerance effect = yes</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_uppercastes</li><li>desc = EST_VAL_CASTES_ADVISOR_FROM_LOWER_CASTE</li><li>influence = -10</li><li>duration = 3650</li></ul></ul>
