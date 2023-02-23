#Information
 - Title: Orc Slaves Sold Due to Purge Edict
 - ID: orc_slavery.72
#Description
Orc Slaves Sold Due to Purge Edict
#Mean Time to Happen:
Base time = 3 months
 - Multiplied by 0.75 if has owner has num of owned provinces with has value is 10, and num of owned provinces with has trade goods is slaves
 - Multiplied by 0.25 if has owner has num of owned provinces with has value is 20, and num of owned provinces with has trade goods is slaves

#Options

___
##Good riddance.

###AI weighting:
AI weights this option at 5
 - Multiplied by 10 if has ruler has personality is cruel personality, and has ruler has personality is malevolent personality, and has ruler has personality is sinner personality


###Efects:<ul><li>owner:</li><ul><li>add years of income = 0.1</li></ul><li>change trade goods = unknown</li><li>add unrest = 5</li><li>If has orcish majority trigger is yes:</li><ul><li>change culture = ROOT</li><li>change religion = ROOT</li></ul><li>Else if has orcish minority trigger is yes:</li><ul><li>remove orcish minority size effect = yes</li><li>remove orcish minority size effect = yes</li></ul><li>hidden effect:</li><ul><li>REB:</li><ul><li>subtract variable:</li><ul><li>which = num_orc_slaves</li><li>value = 1</li></ul></ul></ul></ul>
