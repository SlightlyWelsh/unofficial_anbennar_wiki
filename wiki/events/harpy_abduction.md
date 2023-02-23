#Information
 - Title: Harpy Abduction!
 - ID: harpy_tolerance_events.4
#Description
Harpy Abduction!
#Options

___
##Well... not a huge loss to be honest

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.8 if has wants to decrease tolerance harpy is yes


###Efects:<ul><li>small increase of harpy tolerance effect = yes</li><li>add prestige = -10</li><li>trigger switch:</li><ul><li>on trigger = has_country_flag</li><li>advisor events adm:</li><ul><li>remove advisor by category = ADM</li></ul><li>advisor events dip:</li><ul><li>remove advisor by category = DIP</li></ul><li>advisor events mil:</li><ul><li>remove advisor by category = MIL</li></ul></ul></ul>

___
##Send out a massive rescue party

###AI weighting:
AI weights this option at 50
 - Multiplied by 2 if has wants to maintain tolerance harpy is yes


###Efects:<ul><li>add mil power = -25</li></ul>

___
##Interrogate the local harpies for information

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.1 if has wants to increase tolerance harpy is yes


###Efects:<ul><li>small decrease of harpy tolerance effect = yes</li><li>random:</li><ul><li>chance = 50</li><li>trigger switch:</li><ul><li>on trigger = has_country_flag</li><li>advisor events adm:</li><ul><li>remove advisor by category = ADM</li></ul><li>advisor events dip:</li><ul><li>remove advisor by category = DIP</li></ul><li>advisor events mil:</li><ul><li>remove advisor by category = MIL</li></ul></ul></ul></ul>

___
##Cut a deal for the advisor's release

###Available if:
<li>Any of the following:</li><ul><li>ruler has personality is charismatic_negotiator_personality</li><li>ruler has personality  is silver_tongue_personality</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.1 if has wants to decrease tolerance harpy is yes
 - Multiplied by 0.1 if does not have years of income is 0.3
 - Multiplied by 0.8 if does not have years of income is 0.6


###Efects:<ul><li>highlight = yes</li><li>small increase of harpy tolerance effect = yes</li><li>add years of income = -0.3</li></ul>
