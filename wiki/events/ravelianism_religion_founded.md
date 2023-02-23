#Information
 - Title: Ravelianism Religion Founded!
 - ID: ravelian.5
#Description
Ravelianism Religion Founded!
#Mean Time to Happen:
Base time = 1 days

#Options

___
##The Truth Shall Set You Free

###Available if:
<li>Any of the following:</li><ul><li>All of the following:</li><ul><li>religion group is cannorian</li><li>Any of the following:</li><ul><li>capital scope:</li><ul><li>continent is north_america</li></ul><li>capital scope:</li><ul><li>continent is south_america</li></ul></ul></ul><li>any owned province:</li><ul><li>Any of the following:</li><ul><li>has province modifier ravelian_society</li><li>has province modifier  ravelian_lodge</li></ul></ul></ul>

###AI weighting:
AI weights this option at 20
 - Multiplied by 2 if has any owned province has province modifier is ravelian lodge
 - Multiplied by 2 if has innovativeness ideas is 7
 - Multiplied by 1.1 if has innovativeness ideas is 1
 - Multiplied by 1.5 if has humanist ideas is 7
 - Multiplied by 1.1 if has humanist ideas is 1
 - Multiplied by 0.1 if does not have religion group is cannorian
 - Multiplied by 0 if has country modifier is monstrous nation
 - Multiplied by 0 if has religion group is bulwari
 - Multiplied by 0 if has tag is A21, and has tag is Z43
 - Multiplied by 0.1 if has tag is B02, and has tag is G95, and has tag is H44, and has tag is H45, and has tag is H42, and has tag is H43, and has tag is H46, and has tag is H47, and has tag is H35, and has tag is G94, and has tag is H36
 - Multiplied by 0.75 if has tag is A10, and has tag is A41, and has tag is A43, and has tag is A53
 - Multiplied by 0.25 if has primary culture is vernman, and has tag is A45, and has tag is A34
 - Multiplied by 0.5 if has capital scope has superregion is escann superregion
 - Multiplied by 2 if has primary culture is busilari, and has primary culture is pearlsedger, and has primary culture is arannese, and has primary culture is sorncosti, and has primary culture is anbenncoster, and has tag is A11, and has tag is A23
 - Multiplied by 1000 if has tag is A35, and has tag is A29, and has tag is H33
 - Multiplied by 1.2 if has capital scope has region is the borders region
 - Multiplied by 5 if has religion is regent court, and has capital scope has continent is north america; and has capital scope has continent is south america


###Efects:<ul><li>If random owned province has can have center of reformation trigger has RELIGION is ravelian; and  has province modifier is ravelian lodge:</li><ul><li>change religion = ravelian</li><li>add reform center = ravelian</li><li>add cardinal = yes</li><li>add permanent province modifier:</li><ul><li>name = "religious_zeal_at_conv"</li><li>duration = 9000</li></ul></ul><li>custom tooltip = ravelian_chapter_lodge_convert_tt</li><li>hidden effect:</li><ul><li>If every owned province has province modifier is ravelian lodge:</li><ul><li>change religion = ravelian</li><li>add permanent province modifier:</li><ul><li>name = "religious_zeal_at_conv"</li><li>duration = 9000</li></ul><li>add cardinal = yes</li><li>remove province modifier = ravelian_lodge</li></ul><li>If every owned province has province modifier is ravelian society:</li><ul><li>change religion = ravelian</li><li>add permanent province modifier:</li><ul><li>name = "religious_zeal_at_conv"</li><li>duration = 9000</li></ul><li>remove province modifier = ravelian_society</li></ul></ul><li>capital scope:</li><ul><li>If area does not have province modifier is religious zeal at conv:</li><ul><li>change religion = ravelian</li><li>add permanent province modifier:</li><ul><li>name = "religious_zeal_at_conv"</li><li>duration = 9000</li></ul></ul></ul><li>If has continent is north america, and has continent is south america:</li><ul><li>country gets the modifier "decline_of_cannor_centric_scripture" for 20 years</li><li>If every owned province is core is ROOT, and  has culture is ROOT, and does not have province modifier is religious zeal at conv:</li><ul><li>change religion = ravelian</li></ul></ul><li>change religion = ravelian</li><li>country gets the modifier "conversion_zeal" for 10 years</li></ul>

___
##Interesting

###AI weighting:
AI weights this option at 70
 - Multiplied by 1.5 if has personal deity is adean


###Efects:<ul><li>If random owned province has can have center of reformation trigger has RELIGION is ravelian; and  has province modifier is ravelian lodge:</li><ul><li>change religion = ravelian</li><li>add reform center = ravelian</li><li>add permanent province modifier:</li><ul><li>name = "religious_zeal_at_conv"</li><li>duration = 9000</li></ul></ul><li>custom tooltip = ravelian_chapter_lodge_convert_nc_tt</li><li>hidden effect:</li><ul><li>If every owned province has province modifier is ravelian lodge:</li><ul><li>change religion = ravelian</li><li>add permanent province modifier:</li><ul><li>name = "religious_zeal_at_conv"</li><li>duration = 9000</li></ul><li>remove province modifier = ravelian_lodge</li></ul><li>If every owned province has province modifier is ravelian society:</li><ul><li>change religion = ravelian</li><li>add permanent province modifier:</li><ul><li>name = "religious_zeal_at_conv"</li><li>duration = 9000</li></ul><li>remove province modifier = ravelian_society</li></ul></ul></ul>
