#Information
 - Title: Vampire Ruler is Revealed
 - ID: vampire_ruler.0
#Description
Vampire Ruler is Revealed
#Mean Time to Happen:
Base time = 100 years
 - Multiplied by 0.5 if has check variable has which is suspicionPoints, and check variable has value is 30
 - Multiplied by 0.5 if has check variable has which is suspicionPoints, and check variable has value is 35
 - Multiplied by 0.5 if has check variable has which is suspicionPoints, and check variable has value is 40
 - Multiplied by 0 if has estate privilege is estate vampires law open rule
 - Multiplied by 1.5 if has estate privilege is estate vampires organization the blood court
 - Multiplied by 1.1 if has estate privilege is estate vampires cover vampires action
 - Multiplied by 1.1 if has estate privilege is estate vampires vampires in the administration

#Options

___
##I must step down.

###AI weighting:
AI weights this option at 10


###Efects:<ul><li>reduce stability or adm power = yes</li><li>hidden effect:</li><ul><li>clear ruler vampire flags = yes</li></ul><li>exile ruler as:</li><ul><li>name = cannot_return</li></ul><li>exile heir as = cannot_return_heir</li><li>custom tooltip = human_heir</li><li>country gets the modifier outed_vampire for 5 years</li></ul>

___
##This is MY realm!

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>add stability = -3</li><li>add legitimacy = -10</li><li>add prestige = -20</li><li>clr country flag [hidden_ruler_vampire](../flags/hidden_ruler_vampire.md)</li><li>set country flag [exposed_vampire_ruler](../flags/exposed_vampire_ruler.md)</li><li>clear vampire law = yes</li><li>set estate privilege = estate_vampires_law_open_rule</li><li>If has reform is ar callein reform:</li><ul><li>remove government reform = ar_callein_reform</li><li>change government = monarchy</li></ul><li>country gets the modifier ruler_broken_masquerade for 10 years</li><li>country gets the modifier outed_vampire for 5 years</li></ul>
