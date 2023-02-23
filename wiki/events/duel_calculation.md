#Information
 - Title: Duel Calculation
 - ID: flavor_ravenmarch.9
#Description
Duel Calculation
#Options

___
##Win

###AI weighting:
AI weights this option at 50
 - Multiplied by 3 if has mil is 6
 - Multiplied by 2 if has mil is 4
 - Multiplied by 2 if has ruler has personality is bold fighter personality
 - Multiplied by 2 if has ruler has personality is inspiring leader personality


###Efects:<ul><li>the event ˻flavor_ravenmarch.10˼ happens</li></ul>

___
##Lose

###AI weighting:
AI weights this option at 40
 - Multiplied by 2 if does not have mil is 3
 - Multiplied by 3 if does not have mil is 1
 - Multiplied by 2 if has ruler has personality is craven personality
 - Multiplied by 2 if has ruler has personality is naive personality


###Efects:<ul><li>set country flag [ravenmarch_duel_lost](../flags/ravenmarch_duel_lost.md)</li><li>the event ˻flavor_ravenmarch.11˼ happens</li></ul>

___
##Unnamed Option

###AI weighting:
AI weights this option at 10
 - Multiplied by 2 if does not have mil is 3
 - Multiplied by 3 if does not have mil is 1
 - Multiplied by 2 if has ruler has personality is craven personality
 - Multiplied by 2 if has ruler has personality is bold fighter personality
 - Multiplied by 0.5 if has ruler has personality is careful personality


###Efects:<ul><li>set country flag [ravenmarch_duel_crit_fail](../flags/ravenmarch_duel_crit_fail.md)</li><li>the event ˻flavor_ravenmarch.11˼ happens</li></ul>
