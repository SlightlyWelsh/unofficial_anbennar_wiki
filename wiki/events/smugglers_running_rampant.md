#Information
 - Title: Smugglers running rampant
 - ID: 740
#Description
Smugglers running rampant
#Mean Time to Happen:
Base time = 1 days
 - Multiplied by 0.5 if is lucky

#Options

___
##Stop them!

###AI weighting:
AI weights this option at 35
 - Multiplied by 0.5 if does not have years of income is 0.5


###Efects:<ul><li>add years of income = -0.35</li></ul>

___
##It is too expensive

###AI weighting:
AI weights this option at 65


###Efects:<ul><li>country gets the modifier "smugglers_dominating" for 10 years</li></ul>

___
##Our [Root.Monarch.GetTitle] knows ways to close off some of the worst ways to exploit the system.

###Available if:
<li>ruler has personality ancestor:</li><ul><li>key is entrepreneur</li></ul>

###AI weighting:
AI weights this option at 100
 - Multiplied by 0.5 if does not have years of income is 0.5


###Efects:<ul><li>highlight = yes</li><li>add years of income = -0.2</li></ul>

___
##As long as they don't hurt our interests directly...

###Available if:
<li>ruler has personality is embezzler_personality</li>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>highlight = yes</li><li>country gets the modifier "smugglers_dominating" for 5 years</li><li>If has country flag is [tyrant_system_initialized](../flags/tyrant_system_initialized.md):</li><ul><li>increase tyrant ruthless 1 = yes</li></ul></ul>
