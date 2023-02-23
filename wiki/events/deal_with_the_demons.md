#Information
 - Title: Deal With the Demons
 - ID: bianfang.200
#Description
Deal With the Demons
#Options

___
##Their foul presence shall be cleansed from the land!

###Efects:<ul><li>custom tooltip = bianfang_hunt_oni_tt</li><li>hidden effect:</li><ul><li>If every owned province has religion is lefthand path, and does not have culture is horned ogre:</li><ul><li>add province modifier:</li><ul><li>name = bianfang_lhp_outraged</li><li>duration = 3650</li></ul></ul><li>If every owned province has culture is horned ogre:</li><ul><li>add province modifier:</li><ul><li>name = bianfang_oni_hunted_modifier</li><li>duration = 3650</li></ul><li>add nationalism = 10</li></ul><li>If every owned province has religion is righteous path:</li><ul><li>add province modifier:</li><ul><li>name = bianfang_righteous_path_pleased</li><li>duration = 3650</li></ul></ul></ul><li>add stability or adm power = yes</li><li>large decrease of ogre tolerance effect = yes</li><li>increase tyrant benevolent 3 = yes</li><li>4842:</li><ul><li>If has province modifier is bianfang working with jiangshi:</li><ul><li>remove province modifier = bianfang_working_with_jiangshi</li></ul></ul><li>hidden effect:</li><ul><li>clr country flag [bianfang_lhp_tolerated](../flags/bianfang_lhp_tolerated.md)</li><li>set country flag [bianfang_lhp_hunted](../flags/bianfang_lhp_hunted.md)</li><li>set country flag [bianfang_oni_hunted](../flags/bianfang_oni_hunted.md)</li></ul></ul>

___
##We will use their knowledge and teachings to crush the enemies of [Root.GetName]

###Available if:
<li>None of the following:</li><ul><li>All of the following:</li><ul><li>Any of the following:</li><ul><li>ruler has personality is malevolent_personality</li><li>ruler has personality  is cruel_personality</li></ul><li>has country modifier bianfang_tyrant_modifier_ruthless</li></ul></ul>

###Efects:<ul><li>custom tooltip = bianfang_tolerate_oni_tt</li><li>hidden effect:</li><ul><li>If every owned province has religion is righteous path:</li><ul><li>add province modifier:</li><ul><li>name = bianfang_righteous_path_outraged</li><li>duration = 3650</li></ul></ul><li>If every owned province has culture is horned ogre:</li><ul><li>add province modifier:</li><ul><li>name = bianfang_oni_left_alone</li><li>duration = 3650</li></ul></ul><li>If every country has superregion is yanshen superregion, and has superregion is south haless superregion, and has superregion is north haless superregion, and has superregion is rahen superregion; and does not have religion is lefthand path:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = bianfang_oni_tolerated_opinion</li></ul></ul></ul><li>reduce stability or adm power = yes</li><li>medium increase of ogre tolerance effect = yes</li><li>capital scope:</li><ul><li>add ogre minority size effect = yes</li></ul><li>country gets the modifier bianfang_oni_secrets until otherwise removed</li><li>increase tyrant ruthless 2 = yes</li><li>hidden effect:</li><ul><li>set country flag [bianfang_oni_tolerated](../flags/bianfang_oni_tolerated.md)</li></ul></ul>

___
##Our persecution of the Lefthand Path was unwise. Spare the Oni and their human followers.

###Available if:
<li>has country flag [bianfang_lhp_hunted](../flags/bianfang_lhp_hunted.md)</li><li>has country modifier bianfang_tyrant_modifier_ruthless</li><li>Any of the following:</li><ul><li>ruler has personality is malevolent_personality</li><li>ruler has personality  is cruel_personality</li></ul><li>None of the following:</li><ul><li>ruler has personality is zealot_personality</li></ul>

###Efects:<ul><li>custom tooltip = bianfang_tolerate_oni_lhp_tt</li><li>hidden effect:</li><ul><li>If every owned province has religion is righteous path:</li><ul><li>add province modifier:</li><ul><li>name = bianfang_righteous_path_outraged</li><li>duration = 3650</li></ul></ul><li>If every owned province has culture is horned ogre:</li><ul><li>add province modifier:</li><ul><li>name = bianfang_oni_left_alone</li><li>duration = 3650</li></ul></ul><li>If every country has superregion is yanshen superregion, and has superregion is south haless superregion, and has superregion is north haless superregion, and has superregion is rahen superregion; and does not have religion is lefthand path:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = bianfang_oni_tolerated_opinion</li></ul></ul></ul><li>add stability = -4</li><li>medium increase of ogre tolerance effect = yes</li><li>capital scope:</li><ul><li>add ogre minority size effect = yes</li></ul><li>increase tyrant ruthless 3 = yes</li><li>hidden effect:</li><ul><li>clr country flag [bianfang_lhp_hunted](../flags/bianfang_lhp_hunted.md)</li><li>set country flag [bianfang_oni_tolerated](../flags/bianfang_oni_tolerated.md)</li><li>set country flag [bianfang_lhp_tolerated](../flags/bianfang_lhp_tolerated.md)</li></ul></ul>
