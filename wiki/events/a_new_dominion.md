#Information
 - Title: A New Dominion
 - ID: black_demesne.5
#Description
A New Dominion
#Mean Time to Happen:
Base time = 60 months

#Options

___
##There is wisdom in their words

###Available if:
<li>is controlled by the AI</li>

###AI weighting:
AI weights this option at 40


###Efects:<ul><li>hidden effect:</li><ul><li>event target:province:</li><ul><li>set province flag [new_acolyte](../flags/new_acolyte.md)</li><li>If every neighbor province is not a capital:</li><ul><li>set province flag [new_acolyte](../flags/new_acolyte.md)</li><li>If every neighbor province is not a capital:</li><ul><li>set province flag [new_acolyte](../flags/new_acolyte.md)</li></ul></ul></ul></ul></ul>

___
##Go Back

###Available if:
<li>has country flag [acolyte_decision](../flags/acolyte_decision.md)</li><li>is not controlled by the AI</li>

###AI weighting:
AI weights this option at 40


___
##There is wisdom in their words

###Available if:
<li>is not controlled by the AI</li>

###AI weighting:
AI weights this option at 40


###Efects:<ul><li>If does not have any owned province has state edict is acolyte territory edict:</li><ul><li>add absolutism = 5</li><li>add dip power = -25</li><li>add adm power = -25</li><li>add mil power = -25</li><li>If every subject country is subject of type is acolyte dominion:</li><ul><li>add liberty desire = 25</li></ul><li>custom tooltip = new_acolyte_no_edict_tooltip</li></ul><li>else:</li><ul><li>custom tooltip = new_acolyte_tooltip</li><li>hidden effect:</li><ul><li>new acolyte mtth effect = yes</li></ul></ul></ul>

___
##They dare challenge my authority?

###Available if:
<li>None of the following:</li><ul><li>has country flag [special_acolyte_creation](../flags/special_acolyte_creation.md)</li></ul>

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>add absolutism = 5</li><li>add dip power = -25</li><li>add adm power = -25</li><li>add mil power = -25</li><li>If every subject country is subject of type is acolyte dominion:</li><ul><li>add liberty desire = 25</li></ul></ul>
