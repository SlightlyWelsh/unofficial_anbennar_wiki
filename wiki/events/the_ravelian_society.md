#Information
 - Title: The Ravelian Society
 - ID: ravelian.1
#Description
The Ravelian Society
#Mean Time to Happen:
Base time = 480 months
 - Multiplied by 0.8 if has terrain is city terrain
 - Multiplied by 0.8 if has development is 30
 - Multiplied by 1.5 if has religion is regent court
 - Multiplied by 0.8 if has printing press is 100
 - Multiplied by 0.8 if has province id is 8
 - Multiplied by 0.7 if has global flag is [ravelians_have_god_fragment](../flags/ravelians_have_god_fragment.md), and has continent is north america, and has continent is south america
 - Multiplied by 0.8 if has region is businor region, and has area is konwell area, and has area is middle luna area, and has area is upper luna area
 - Multiplied by 0.9 if has culture is busilari, and has culture is pearlsedger, and has culture is arannese, and has culture is sorncosti, and has culture is anbenncoster
 - Multiplied by 1.5 if does not have year is 1600

#Options

___
##Welcome the Ravelians to [Root.GetName]

###AI weighting:
AI weights this option at 70
 - Multiplied by 2 if has owner has innovativeness ideas is 7
 - Multiplied by 1.1 if has owner has innovativeness ideas is 1
 - Multiplied by 1.5 if has owner has humanist ideas is 7
 - Multiplied by 1.1 if has owner has humanist ideas is 1
 - Multiplied by 1.4 if has owner is lacking institutions


###Efects:<ul><li>add permanent province modifier:</li><ul><li>name = ravelian_society</li><li>duration = -1</li></ul></ul>

___
##They can find somewhere else to congregate.

###AI weighting:
AI weights this option at 30
 - Multiplied by 2 if has owner has religious ideas is 7
 - Multiplied by 1.2 if has owner has religious ideas is 1


###Efects:<ul><li>hidden effect:</li><ul><li>set province flag [denied_ravelian_society](../flags/denied_ravelian_society.md)</li></ul></ul>

___
##Ban any future Ravelian society formation in the whole country.

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>owner:</li><ul><li>hidden effect:</li><ul><li>set country flag [no_ravelian_societies](../flags/no_ravelian_societies.md)</li></ul></ul></ul>
