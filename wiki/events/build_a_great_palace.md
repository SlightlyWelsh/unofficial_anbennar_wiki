#Information
 - Title: Build a Great Palace
 - ID: 5085
#Description
Build a Great Palace
#Mean Time to Happen:
Base time = 1 days
 - Multiplied by 2.0 if has artist is 3
 - Multiplied by 0.5 if is lucky
 - Multiplied by 0.66 if does not have advisor is artist

#Options

___
##Build the palace.

###AI weighting:
AI weights this option at 40
 - Multiplied by 0.5 if does not have years of income is 0.3
 - Multiplied by 1.5 if does not have legitimacy or horde unity is 60


###Efects:<ul><li>add prestige = 10</li><li>add legitimacy = 20</li><li>add horde unity = 20</li><li>add mandate effect = yes</li><li>add years of income = -0.25</li></ul>

___
##Don't build it.

###AI weighting:
AI weights this option at 60
 - Multiplied by 0.5 if has prestige is 90
 - Multiplied by 0.5 if does not have legitimacy is 40


###Efects:<ul><li>add prestige = -10</li></ul>

___
##It must be even grander!

###Available if:
<li>ruler has personality is obsessive_perfectionist_personality</li>

###Efects:<ul><li>highlight = yes</li><li>add prestige = 15</li><li>add legitimacy = 25</li><li>add horde unity = 25</li><li>add mandate large effect = yes</li><li>add years of income = -0.35</li></ul>

___
##Let [Root.Monarch.GetName] oversee the project personally.

###Available if:
<li>ruler has personality ancestor:</li><ul><li>key is architectural_visionary</li></ul>

###Efects:<ul><li>highlight = yes</li><li>add prestige = 10</li><li>add legitimacy = 20</li><li>add horde unity = 20</li><li>add mandate large effect = yes</li><li>add years of income = -0.15</li></ul>
