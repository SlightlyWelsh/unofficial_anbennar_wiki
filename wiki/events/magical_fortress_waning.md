#Information
 - Title: Magical Fortress Waning
 - ID: magic_misc_events.3
#Description
Magical Fortress Waning
#Mean Time to Happen:
Base time = 2400 months
 - Multiplied by 0.75 if does not have stability is 1
 - Multiplied by 0.75 if is at war
 - Multiplied by 0.5 if has any owned province has building is fort magic, and does not have controlled by is ROOT

#Options

___
##Oh well.

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>add prestige = -1</li><li>event target:fort magic province:</li><ul><li>remove building = fort_magic</li></ul></ul>

___
##Reinforce the spell myself!

###Available if:
<li>has ruler flag [conjuration_2](../flags/conjuration_2.md)</li><li>adm power is at least 50</li><li>dip power is at least 50</li>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>add adm power = -50</li><li>add dip power = -50</li><li>custom tooltip = tooltip_option_conjuration_2</li></ul>

___
##The $ESTATE_MAGES$ can fix it

###Available if:
<li>has estate estate_mages</li><li>estate loyalty:</li><ul><li>estate is estate_mages</li><li>loyalty is at least 60</li></ul><li>estate influence:</li><ul><li>estate is estate_mages</li><li>influence is at least 40</li></ul>

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>add years of income = -2</li><li>custom tooltip = tooltip_loyal_influential_estate</li></ul>
