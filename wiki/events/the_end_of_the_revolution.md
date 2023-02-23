#Information
 - Title: The End of the Revolution
 - ID: revolution.9
#Description
The End of the Revolution
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Order is restored.

###Available if:
<li>None of the following:</li><ul><li>has dlc "Emperor"</li></ul>

###Efects:<ul><li>add stability or adm power = yes</li><li>increase legitimacy large effect = yes</li><li>clear standard revolution elements effect = yes</li></ul>

___
##At least the conflict is over...

###Available if:
<li>has dlc "Emperor"</li><li>Any of the following:</li><ul><li>All of the following:</li><ul><li>is revolutionary is no</li><li>has country flag [revolution_disaster_revolutionary](../flags/revolution_disaster_revolutionary.md)</li></ul><li>AND:</li><ul><li>is revolutionary is yes</li><li>has country flag [revolution_disaster_reactionary](../flags/revolution_disaster_reactionary.md)</li></ul></ul>

###Efects:<ul><li>add stability or adm power = yes</li><li>If is revolutionary is no:</li><ul><li>capital scope:</li><ul><li>If region has revolution in province, and  has owned by is root, and  is center of revolution is no:</li><ul><li>remove revolution from province effect = yes</li></ul></ul><li>hidden effect:</li><ul><li>log = "[Root.GetName] lost the Revolution as the Revolutionaries."</li></ul></ul><li>else:</li><ul><li>hidden effect:</li><ul><li>log = "[Root.GetName] lost the Revolution as the Reactionaries."</li></ul></ul><li>clear standard revolution elements effect = yes</li></ul>

___
##Let us rejoice in victory!

###Available if:
<li>has dlc "Emperor"</li><li>Any of the following:</li><ul><li>All of the following:</li><ul><li>is revolutionary is yes</li><li>has country flag [revolution_disaster_revolutionary](../flags/revolution_disaster_revolutionary.md)</li></ul><li>AND:</li><ul><li>is revolutionary is no</li><li>has country flag [revolution_disaster_reactionary](../flags/revolution_disaster_reactionary.md)</li></ul></ul>

###Efects:<ul><li>add stability or adm power = yes</li><li>If is revolutionary is no:</li><ul><li>tooltip:</li><ul><li>country gets the modifier no_revolution_here_country_dummy until otherwise removed</li><li>If has any owned province is center of revolution is yes:</li><ul><li>remove center of revolution = yes</li></ul><li>custom tooltip = remove_revolution_from_all_provinces</li><li>hidden effect:</li><ul><li>If every owned province has revolution in province:</li><ul><li>remove revolution from province effect = yes</li></ul></ul><li>increase legitimacy large effect = yes</li><li>hidden effect:</li><ul><li>log = "[Root.GetName] won the Revolution as the Reactionaries."</li></ul></ul></ul><li>else:</li><ul><li>custom tooltip = add_as_much_revolutionary_zeal_as_you_can_take</li><li>hidden effect:</li><ul><li>add revolutionary zeal = 1000</li></ul><li>hidden effect:</li><ul><li>log = "[Root.GetName] won the Revolution as the Revolutionaries."</li></ul></ul><li>clear standard revolution elements effect = yes</li></ul>
