#Information
 - Title: Sympathizers in [negotiating_sympathizers.GetName] want to negotiate
 - ID: blood_lotus_rebellion.5
#Description
Sympathizers in [negotiating_sympathizers.GetName] want to negotiate
#Options

___
##Grant them their request

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>goto = negotiating_sympathizers</li><li>event target:negotiating sympathizers:</li><ul><li>add local autonomy = 25</li><li>remove province modifier = blood_lotus_sympathizers</li><li>hidden effect:</li><ul><li>remove province modifier = blood_lotus_guerrillas_hidden</li><li>remove province modifier = blood_lotus_guerrillas</li></ul><li>add province modifier:</li><ul><li>name = blood_lotus_dissuaded_sympathizers</li><li>duration = 730</li></ul></ul><li>blood lotus hardline stance change small:</li><ul><li>humanhardline = yes</li></ul></ul>

___
##We don't talk to traitors

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>increase legitimacy small effect = yes</li><li>hidden effect:</li><ul><li>event target:negotiating sympathizers:</li><ul><li>add province modifier:</li><ul><li>name = blood_lotus_guerrillas_hidden</li><li>duration = -1</li><li>hidden = yes</li></ul></ul></ul><li>blood lotus hardline stance change small:</li><ul><li>harimarihardline = yes</li></ul></ul>
