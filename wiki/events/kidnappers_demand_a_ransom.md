#Information
 - Title: Kidnappers Demand a Ransom
 - ID: new_sun_cult.164
#Description
Kidnappers Demand a Ransom
#Options

___
##Pay the ransom.

###AI weighting:
AI weights this option at 1
 - Multiplied by 100 if has variable arithmetic trigger has export to variable has which is heirAdmVar, and export to variable has value is heir adm; and variable arithmetic trigger has export to variable has which is heirDipVar, and export to variable has value is heir dip; and variable arithmetic trigger has export to variable has which is heirMilVar, and export to variable has value is heir mil; and variable arithmetic trigger has change variable has which is heirAdmVar, and change variable has which is heirDipVar; and variable arithmetic trigger has change variable has which is heirAdmVar, and change variable has which is heirMilVar; and variable arithmetic trigger has check variable has which is heirAdmVar, and check variable has value is 9
 - Multiplied by 0 if has num of loans is 5


###Efects:<ul><li>add treasury = -100</li><li>the event [The Fate of our Heir](../events/the_fate_of_our_heir.md) happens</li></ul>

___
##Try to locate the kidnappers.

###AI weighting:
AI weights this option at 1
 - Multiplied by 100 if has variable arithmetic trigger has export to variable has which is heirAdmVar, and export to variable has value is heir adm; and variable arithmetic trigger has export to variable has which is heirDipVar, and export to variable has value is heir dip; and variable arithmetic trigger has export to variable has which is heirMilVar, and export to variable has value is heir mil; and variable arithmetic trigger has change variable has which is heirAdmVar, and change variable has which is heirDipVar; and variable arithmetic trigger has change variable has which is heirAdmVar, and change variable has which is heirMilVar; and does not have check variable has which is heirAdmVar, and check variable has value is 9


###Efects:<ul><li>set country flag [nsc_heir_will_die](../flags/nsc_heir_will_die.md)</li><li>the event [The Fate of our Heir](../events/the_fate_of_our_heir.md) happens</li></ul>
