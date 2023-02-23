#Information
 - Title: Gift to the State
 - ID: 5008
#Description
Gift to the State
#Mean Time to Happen:
Base time = 1 days
 - Multiplied by 2.0 if has adm is 4
 - Multiplied by 2.0 if is lucky

#Options

___
##Put into the treasury.

###AI weighting:
AI weights this option at 55
 - Multiplied by 0 if does not have num of cities is 5


###Efects:<ul><li>add years of income = 0.2</li></ul>

___
##Spend it generously.

###AI weighting:
AI weights this option at 45


###Efects:<ul><li>add prestige = 10</li></ul>

___
##I'm sure I know some more people who can contribute.

###Available if:
<li>ruler has personality ancestor:</li><ul><li>key is well_connected</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>highlight = yes</li><li>add years of income = 0.2</li><li>add prestige = 10</li></ul>

___
##I know just where to put those funds...

###Available if:
<li>ruler has personality is embezzler_personality</li>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>highlight = yes</li><li>add years of income = 0.35</li><li>If has country flag is [tyrant_system_initialized](../flags/tyrant_system_initialized.md):</li><ul><li>increase tyrant ruthless 1 = yes</li></ul></ul>

___
##We must donate this to the poor.

###Available if:
<li>Any of the following:</li><ul><li>ruler has personality ancestor:</li><ul><li>key is righteous</li></ul><li>ruler has personality ancestor:</li><ul><li>key is kind_hearted</li></ul></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>highlight = yes</li><li>add prestige = 15</li><li>If has country flag is [tyrant_system_initialized](../flags/tyrant_system_initialized.md):</li><ul><li>increase tyrant benevolent 1 = yes</li></ul></ul>
