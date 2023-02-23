#Information
 - Title: Nobles Demand Privileges
 - ID: 5058
#Description
Nobles Demand Privileges
#Mean Time to Happen:
Base time = 1 days
 - Multiplied by 2.0 if has adm is 4
 - Multiplied by 0.5 if is lucky
 - Multiplied by 0.66 if has government attribute is is merchant republic, and has government is theocracy, and has reform is tribal federation

#Options

___
##Accept their rightful claims.

###AI weighting:
AI weights this option at 55
 - Multiplied by 1.5 if has prestige is 20


###Efects:<ul><li>add prestige = -10</li></ul>

___
##Ignore their demands.

###AI weighting:
AI weights this option at 45
 - Multiplied by 0.5 if has unrest is 5
 - Multiplied by 0 if has estate is estate nobles, and  has estate influence has estate is estate nobles, and estate influence has influence is 80


###Efects:<ul><li>reduce estate nobles loyalty effect = yes</li><li>country gets the modifier "disorder" for 10 years</li></ul>

___
##Crush them!

###Available if:
<li>ruler has personality is cruel_personality</li>

###Efects:<ul><li>highlight = yes</li><li>add prestige = 10</li><li>If random owned province is core is ROOT, and  is state, and  is in capital area, and  has highest supply  in area is yes:</li><ul><li>spawn rebels:</li><ul><li>type = noble_rebels</li><li>size = 1</li></ul></ul><li>If has country flag is [tyrant_system_initialized](../flags/tyrant_system_initialized.md):</li><ul><li>increase tyrant ruthless 1 = yes</li></ul></ul>

___
##Let the [Root.Monarch.GetTitle] explain why they never had those rights to begin with.

###Available if:
<li>ruler has personality ancestor:</li><ul><li>key is lawgiver</li></ul>

###Efects:<ul><li>highlight = yes</li><li>add prestige = -5</li><li>add legitimacy = 5</li></ul>
