#Information
 - Title: Fate of Dahvar
 - ID: aelnar.55
#Description
Fate of Dahvar
#Mean Time to Happen:
Base time = 1 months

#Options

___
##Death shall come for our enemies!

###Available if:
<li>has country flag [dahvar_dead](../flags/dahvar_dead.md)</li>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>random:</li><ul><li>chance = 30</li><li>reduce stability or adm power = yes</li></ul><li>add adm power = 50</li></ul>

___
##The verdict shall be death

###Available if:
<li>has country flag [dahvar_alive](../flags/dahvar_alive.md)</li>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>reduce stability or adm power = yes</li><li>add adm power = 150</li></ul>

___
##The verdict shall be incarceration

###Available if:
<li>has country flag [dahvar_alive](../flags/dahvar_alive.md)</li>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>country gets the modifier dahvar_in_prison for 50 years</li><li>add stability or adm power = yes</li></ul>

___
##The verdict shall be exile

###Available if:
<li>has country flag [dahvar_alive](../flags/dahvar_alive.md)</li>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>add mil power = 50</li><li>add dip power = 50</li><li>add adm power = 50</li><li>hidden effect:</li><ul><li>set global flag [dahvar_exiled](../flags/dahvar_exiled.md)</li></ul></ul>
