#Information
 - Title: Provincial Feud
 - ID: personality_events.10
#Description
Provincial Feud
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Try to settle the issue justly.

###AI weighting:
AI weights this option at 40


###Efects:<ul><li>add estate nobles loyalty effect = yes</li><li>add prestige = 10</li><li>add ruler modifier:</li><ul><li>name = "just_settlement_modifier"</li><li>duration = 1825</li></ul><li>If has country flag is [tyrant_system_initialized](../flags/tyrant_system_initialized.md):</li><ul><li>increase tyrant benevolent 1 = yes</li></ul></ul>

___
##We must exploit this situation!

###Available if:
<li>None of the following:</li><ul><li>ruler has personality is greedy_personality</li></ul>

###AI weighting:
AI weights this option at 40


###Efects:<ul><li>If random owned province has local autonomy is 50, and  is core is ROOT, and  is state, and  has controlled by is owner, and does not have province modifier is increasing local authority:</li><ul><li>If area is not a capital, and  has owned by is ROOT:</li><ul><li>custom tooltip = personality_events.10.b.tt</li><li>hidden effect:</li><ul><li>add local autonomy = -15</li><li>add province modifier:</li><ul><li>name = "increasing_local_authority"</li><li>duration = 10950</li></ul></ul></ul></ul><li>If does not have religion is totemism:</li><ul><li>random list:</li><ul><li>20:</li><ul><li>remove ruler personality = just_personality</li><li>add ruler personality = greedy_personality</li></ul><li>80:</li><ul></ul></ul></ul><li>If has country flag is [tyrant_system_initialized](../flags/tyrant_system_initialized.md):</li><ul><li>increase tyrant ruthless 1 = yes</li></ul></ul>
