#Information
 - Title: Ravages of War
 - ID: personality_events.14
#Description
Ravages of War
#Mean Time to Happen:
Base time = 1 days

#Options

___
##We must help these poor people rebuild their lives!

###Efects:<ul><li>If random owned province has nationalism is 1, and  is state, and does not have province modifier is kind hearted healing ravages of war; and does not have province modifier is not so kind hearted:</li><ul><li>If area has nationalism is 1, and  has owned by is ROOT, and does not have province modifier is kind hearted healing ravages of war; and does not have province modifier is not so kind hearted:</li><ul><li>custom tooltip = personality_events.14.a.tt</li><li>hidden effect:</li><ul><li>add province modifier:</li><ul><li>name = "kind_hearted_healing_ravages_of_war"</li><li>duration = 5475</li></ul></ul></ul></ul><li>If has country flag is [tyrant_system_initialized](../flags/tyrant_system_initialized.md):</li><ul><li>increase tyrant benevolent 1 = yes</li></ul></ul>

___
##Let us instead use the devastation to our advantage!

###Available if:
<li>None of the following:</li><ul><li>ruler has personality is cruel_personality</li></ul>

###Efects:<ul><li>add mil power = -50</li><li>If random owned province has nationalism is 1, and  is state, and does not have province modifier is kind hearted healing ravages of war; and does not have province modifier is not so kind hearted:</li><ul><li>If area has nationalism is 1, and  has owned by is ROOT, and does not have province modifier is kind hearted healing ravages of war; and does not have province modifier is not so kind hearted:</li><ul><li>custom tooltip = personality_events.14.b.tt</li><li>hidden effect:</li><ul><li>add local autonomy = -25</li><li>add province modifier:</li><ul><li>name = "not_so_kind_hearted"</li><li>duration = 5475</li></ul></ul></ul></ul><li>If does not have religion is totemism:</li><ul><li>random list:</li><ul><li>10:</li><ul><li>remove ruler personality = kind_hearted_personality</li><li>add ruler personality = cruel_personality</li></ul><li>90:</li><ul><li>add prestige = -10</li></ul></ul></ul><li>If has country flag is [tyrant_system_initialized](../flags/tyrant_system_initialized.md):</li><ul><li>increase tyrant ruthless 1 = yes</li></ul></ul>

___
##Local authorities are handling it.

###Efects:<ul><li>add prestige = -10</li></ul>
