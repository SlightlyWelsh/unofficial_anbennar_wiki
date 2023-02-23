#Information
 - Title: Precursor Ruins Discovered
 - ID: precursor_relics.1
#Description
Precursor Ruins Discovered
#Mean Time to Happen:
Base time = 800 years
 - Multiplied by 0.3 if has continent is north america, and has continent is south america
 - Multiplied by 0.8 if has port, and has continent is europe, and has continent is africa
 - Multiplied by 1.6 if does not have port, and has continent is europe, and has continent is africa

#Options

___
##Send them in, and secure the site!

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>save trade goods = yes</li><li>change trade goods = precursor_relics</li><li>add devastation = 10</li><li>If does not have province modifier is eordan expedition site; and does not have province modifier is pr great ruin; and does not have province flag is [no_precursor_ruin](../flags/no_precursor_ruin.md); and does not have REB has check variable has num ruin is 5:</li><ul><li>random:</li><ul><li>chance = 10</li><li>add permanent province modifier:</li><ul><li>name = pr_great_ruin</li><li>duration = -1</li></ul><li>set add ruin count = yes</li></ul></ul><li>set add relics count = yes</li><li>If has REB has check variable has num precursor relics is 55:</li><ul><li>hidden effect:</li><ul><li>set global flag [max_precursor_relics](../flags/max_precursor_relics.md)</li></ul></ul></ul>

___
##Just throw the dirt back over it; it's too much trouble.

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>owner:</li><ul><li>add prestige = 10</li></ul></ul>
