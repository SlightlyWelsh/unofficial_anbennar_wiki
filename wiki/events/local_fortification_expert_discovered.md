#Information
 - Title: Local fortification expert discovered
 - ID: 737
#Description
Local fortification expert discovered
#Mean Time to Happen:
Base time = 1 days

#Options

___
##The entire country needs him.

###AI weighting:
AI weights this option at 35
 - Multiplied by 0.5 if has advisor is fortification expert


###Efects:<ul><li>add meritocracy effect = yes</li><li>define advisor:</li><ul><li>type = fortification_expert</li><li>name = local_fortification_expert</li><li>skill = 2</li><li>culture = event_target:local_fortification_expert_province</li><li>religion = event_target:local_fortification_expert_province</li><li>discount = yes</li></ul></ul>

___
##Let him stay home.

###AI weighting:
AI weights this option at 65


###Efects:<ul><li>event target:local fortification expert province:</li><ul><li>add province modifier:</li><ul><li>name = "local_fortress"</li><li>duration = -1</li></ul></ul></ul>

___
##This will be an excellent opportunity, for him.

###Available if:
<li>ruler has personality ancestor:</li><ul><li>key is well_connected</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>highlight = yes</li><li>add meritocracy effect = yes</li><li>define advisor:</li><ul><li>type = fortification_expert</li><li>name = local_fortification_expert</li><li>culture = event_target:local_fortification_expert_province</li><li>religion = event_target:local_fortification_expert_province</li><li>discount = yes</li><li>skill = 3</li></ul></ul>
