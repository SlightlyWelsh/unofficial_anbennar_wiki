#Information
 - Title: A Righteous [Root.Monarch.GetTitle]
 - ID: personality_events.11
#Description
A Righteous [Root.Monarch.GetTitle]
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Chastise the Governor.

###AI weighting:
AI weights this option at 40


###Efects:<ul><li>add legitimacy = 10</li><li>If random owned province is not a capital, and does not have province modifier is chastised governor; and does not have province modifier is defended governor; and  is core is ROOT, and  is state:</li><ul><li>If area is not a capital, and  has owned by is ROOT, and does not have province modifier is chastised governor; and does not have province modifier is defended governor:</li><ul><li>custom tooltip = personality_events.11.a.tt</li><li>hidden effect:</li><ul><li>add province modifier:</li><ul><li>name = "chastised_governor"</li><li>duration = 10950</li></ul></ul></ul></ul><li>If has country flag is [tyrant_system_initialized](../flags/tyrant_system_initialized.md):</li><ul><li>increase tyrant benevolent 1 = yes</li></ul></ul>

___
##Attempt to defend the governor.

###Available if:
<li>None of the following:</li><ul><li>ruler has personality is greedy_personality</li></ul>

###AI weighting:
AI weights this option at 40
 - Multiplied by 0 if has ruler has personality is malevolent personality, and has ruler has personality is obsessive perfectionist personality, and has ruler has personality is loose lips personality, and has ruler has personality is craven personality, and has ruler has personality is naive personality, and has ruler has personality is cruel personality, and has ruler has personality is sinner personality, and has ruler has personality is drunkard personality, and has ruler has personality is infertile personality, and has ruler has personality is embezzler personality, and has ruler has personality is babbling buffoon personality


###Efects:<ul><li>If random owned province is not a capital, and does not have province modifier is chastised governor; and does not have province modifier is defended governor; and  is core is ROOT, and  is state:</li><ul><li>If area is not a capital, and  has owned by is ROOT, and does not have province modifier is chastised governor; and does not have province modifier is defended governor:</li><ul><li>custom tooltip = personality_events.11.b.tt</li><li>hidden effect:</li><ul><li>add province modifier:</li><ul><li>name = "defended_governor"</li><li>duration = 10950</li></ul></ul></ul></ul><li>If does not have religion is totemism:</li><ul><li>random list:</li><ul><li>10:</li><ul><li>remove ruler personality = righteous_personality</li><li>add ruler personality = greedy_personality</li></ul><li>90:</li><ul><li>add prestige = 10</li></ul></ul></ul><li>If has country flag is [tyrant_system_initialized](../flags/tyrant_system_initialized.md):</li><ul><li>increase tyrant ruthless 1 = yes</li></ul></ul>

___
##Leave it to the locals to handle.

###AI weighting:
AI weights this option at 20


###Efects:<ul><li>add legitimacy = -10</li></ul>
