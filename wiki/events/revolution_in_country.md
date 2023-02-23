#Information
 - Title: Revolution in $COUNTRY$
 - ID: revolution.1
#Description
Revolution in $COUNTRY$
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Dire times are ahead of us.

###Available if:
<li>None of the following:</li><ul><li>has dlc "Emperor"</li></ul>

###Efects:<ul><li>add prestige = -10</li></ul>

___
##We must show these upstarts their place!

###Available if:
<li>has dlc "Emperor"</li>

###AI weighting:
AI weights this option at 3
 - Multiplied by 0 if has tag is J33, and  has Y15 has mission completed is Y15 enlist kin


###Efects:<ul><li>set country flag [revolution_disaster_reactionary](../flags/revolution_disaster_reactionary.md)</li><li>If random owned province has province flag is [revolution_spawn_rebels_here](../flags/revolution_spawn_rebels_here.md):</li><ul><li>clr province flag [revolution_spawn_rebels_here](../flags/revolution_spawn_rebels_here.md)</li><li>spawn rebels:</li><ul><li>type = revolutionary_rebels</li><li>size = 3</li><li>win = yes</li><li>unrest = 10</li></ul><li>If has any neighbor province has owned by is root:</li><ul><li>If random neighbor province has owned by is root:</li><ul><li>spawn rebels:</li><ul><li>type = revolutionary_rebels</li><li>size = 3</li><li>win = yes</li><li>unrest = 10</li></ul></ul></ul><li>else:</li><ul><li>owner:</li><ul><li>If random owned province is a capital:</li><ul><li>spawn rebels:</li><ul><li>type = revolutionary_rebels</li><li>size = 2</li></ul></ul></ul></ul></ul></ul>

___
##Perhaps they are right...

###Available if:
<li>has dlc "Emperor"</li>

###AI weighting:
AI weights this option at 2
 - Multiplied by 2 if has revolution target does not exist
 - Multiplied by 0 if is the emperor


###Efects:<ul><li>custom tooltip = revolution_disaster_go_for_it_tooltip</li><li>If random owned province has province flag is [revolution_spawn_rebels_here](../flags/revolution_spawn_rebels_here.md):</li><ul><li>clr province flag [revolution_spawn_rebels_here](../flags/revolution_spawn_rebels_here.md)</li><li>spawn rebels:</li><ul><li>type = pretender_rebels</li><li>size = 3</li><li>win = yes</li><li>unrest = 10</li></ul><li>If has any neighbor province has owned by is root:</li><ul><li>If random neighbor province has owned by is root:</li><ul><li>spawn rebels:</li><ul><li>type = pretender_rebels</li><li>size = 2</li><li>win = yes</li><li>unrest = 10</li></ul></ul></ul></ul><li>set country flag [revolution_disaster_revolutionary](../flags/revolution_disaster_revolutionary.md)</li><li>set country flag [revolution_disaster_immediate_revolution](../flags/revolution_disaster_immediate_revolution.md)</li><li>hidden effect:</li><ul><li>the event [The Revolution is Here](../events/the_revolution_is_here.md) happens</li></ul></ul>


#Pages with same name:
The following pages have the same name as this page:
 - [revolution_in_country_1](revolution_in_country_1.md)


#Pages with same name:
The following pages have the same name as this page:
 - [revolution_in_country_1](revolution_in_country_1.md)


#Pages with same name:
The following pages have the same name as this page:
 - [revolution_in_country_1](revolution_in_country_1.md)
