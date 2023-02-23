#Information
 - Title: The Samartal Ball is Approaching
 - ID: new_sun_cult.171
#Description
The Samartal Ball is Approaching
#Options

___
##[Root.Monarch.GetTitle] [Root.Monarch.GetName] will represent us.

###AI weighting:
AI weights this option at 1
 - Multiplied by 100 if has variable arithmetic trigger has export to variable has which is rulerAdmVar, and export to variable has value is ADM; and variable arithmetic trigger has export to variable has which is rulerDipVar, and export to variable has value is DIP; and variable arithmetic trigger has export to variable has which is rulerMilVar, and export to variable has value is MIL; and variable arithmetic trigger has change variable has which is rulerAdmVar, and change variable has which is rulerDipVar; and variable arithmetic trigger has change variable has which is rulerAdmVar, and change variable has which is rulerMilVar; and does not have check variable has which is rulerAdmVar, and check variable has value is 9


###Efects:<ul><li>custom tooltip = nsc_wars_are_disabled_tt</li><li>If every known country has defensive war with is ROOT, and  has religion is bulwari sun cult:</li><ul><li>white peace = ROOT</li></ul><li>set country flag [nsc_sent_ruler](../flags/nsc_sent_ruler.md)</li><li>set ruler flag [nsc_is_at_samartal](../flags/nsc_is_at_samartal.md)</li></ul>

___
##[Root.Heir.GetTitle] [Root.Heir.GetName] will represent us.

###Available if:
<li>has heir</li><li>heir age is at least 15</li>

###AI weighting:
AI weights this option at 1
 - Multiplied by 100 if has variable arithmetic trigger has export to variable has which is heirAdmVar, and export to variable has value is heir adm; and variable arithmetic trigger has export to variable has which is heirDipVar, and export to variable has value is heir dip; and variable arithmetic trigger has export to variable has which is heirMilVar, and export to variable has value is heir mil; and variable arithmetic trigger has change variable has which is heirAdmVar, and change variable has which is heirDipVar; and variable arithmetic trigger has change variable has which is heirAdmVar, and change variable has which is heirMilVar; and does not have check variable has which is heirAdmVar, and check variable has value is 9


###Efects:<ul><li>custom tooltip = nsc_wars_are_disabled_tt</li><li>If every known country has defensive war with is ROOT, and  has religion is bulwari sun cult:</li><ul><li>white peace = ROOT</li></ul><li>set country flag [nsc_sent_heir](../flags/nsc_sent_heir.md)</li><li>set heir flag [nsc_is_at_samartal](../flags/nsc_is_at_samartal.md)</li></ul>
