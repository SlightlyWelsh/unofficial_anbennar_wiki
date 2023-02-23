#Information
 - Title: Vampiric Emigres Arrive
 - ID: vampires_estate_events.11
#Description
Vampiric Emigres Arrive
#Options

___
##Mutually beneficial? More like parasitic. Guards!

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>add prestige = 5</li><li>hidden effect:</li><ul><li>ROOT:</li><ul><li>save event target as = emigres_landing</li></ul><li>event target:vampire origin:</li><ul><li>the event ˻flavor_asheniande.10˼ happens</li></ul></ul><li>event target:aw vampires migration target:</li><ul><li>If does not have province modifier is aw vampires 1; and does not have province modifier is aw vampires 2; and does not have province modifier is aw vampires 3:</li><ul><li>random:</li><ul><li>chance = 33</li><li>add province modifier:</li><ul><li>name = aw_vampires_1</li><li>duration = -1</li></ul></ul></ul></ul></ul>

___
##Let the seeds of darkness fester

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.1 if does not have culture is human is yes
 - Multiplied by 1.25 if has capital scope has region is the borders region


###Efects:<ul><li>add stability = -1</li><li>hidden effect:</li><ul><li>ROOT:</li><ul><li>save event target as = emigres_landing</li></ul><li>set country flag [has_vampires_estate](../flags/has_vampires_estate.md)</li><li>the event ˻vampires_estate_events.12˼ happens</li><li>event target:vampire origin:</li><ul><li>the event ˻flavor_asheniande.8˼ happens</li></ul></ul><li>custom tooltip = estate_vampies_gain_tooltip</li><li>event target:aw vampires migration target:</li><ul><li>If does not have province modifier is aw vampires 1; and does not have province modifier is aw vampires 2; and does not have province modifier is aw vampires 3:</li><ul><li>random:</li><ul><li>chance = 33</li><li>add province modifier:</li><ul><li>name = aw_vampires_2</li><li>duration = -1</li></ul></ul></ul></ul></ul>
