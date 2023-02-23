#Information
 - Title: Across the Portal, a Familiar Forest
 - ID: eordand.39
#Description
Across the Portal, a Familiar Forest
#Options

___
##The Fey Lords promised us the Domandrod, and with their grace the Deepwoods are ours!

###Efects:<ul><li>If every known country has culture is wood elf:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = eordand_familiar_forest_conquest</li></ul></ul><li>3049:</li><ul><li>add permanent claim = ROOT</li></ul><li>3050:</li><ul><li>add permanent claim = ROOT</li></ul><li>3063:</li><ul><li>add permanent claim = ROOT</li></ul><li>3053:</li><ul><li>add permanent claim = ROOT</li></ul><li>3059:</li><ul><li>add permanent claim = ROOT</li></ul><li>hidden effect:</li><ul><li>set country flag [eordand_deepwoods_conquer](../flags/eordand_deepwoods_conquer.md)</li><li>swap non generic missions = yes</li></ul></ul>

___
##Let us work with the Wood Elves to protect our forests from the outside world.

###Efects:<ul><li>largest increase of elven tolerance effect = yes</li><li>If every known country has culture is wood elf:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = eordand_familiar_forest_ally</li></ul></ul><li>If does not have any country has primary culture is wood elf:</li><ul><li>If has calc true if has deepwoods superregion has culture is wood elf; and calc true if has amount is 10:</li><ul><li>If deepwoods superregion has culture is wood elf, and  does not have owner culture:</li><ul><li>add permanent claim = ROOT</li></ul></ul><li>else:</li><ul><li>deepwoods superregion:</li><ul><li>add permanent claim = ROOT</li></ul></ul></ul><li>hidden effect:</li><ul><li>set country flag [eordand_deepwoods_ally](../flags/eordand_deepwoods_ally.md)</li><li>swap non generic missions = yes</li></ul></ul>
