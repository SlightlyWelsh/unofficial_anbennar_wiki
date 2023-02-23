#Information
 - Title: The Remnant Awakening
 - ID: diggy_remnant_stagnation.2
#Description
The Remnant Awakening
#Options

___
##We will be able to dig deeper than ever before!

###Available if:
<li>check variable:</li><ul><li>awakeningDig is at least 100</li></ul>

###AI weighting:
AI weights this option at 10


###Efects:<ul><li>add prestige = 10</li><li>If has capital scope has province modifier is dig 1:</li><ul><li>capital scope:</li><ul><li>add permanent province modifier:</li><ul><li>name = dig_2</li><li>duration = -1</li></ul><li>hidden effect:</li><ul><li>remove province modifier = dig_1</li></ul></ul></ul><li>Else if has capital scope has province modifier is dig 2:</li><ul><li>capital scope:</li><ul><li>add permanent province modifier:</li><ul><li>name = dig_3</li><li>duration = -1</li></ul><li>hidden effect:</li><ul><li>remove province modifier = dig_2</li></ul></ul></ul><li>Else if has capital scope has province modifier is dig 3:</li><ul><li>capital scope:</li><ul><li>add permanent province modifier:</li><ul><li>name = dig_4</li><li>duration = -1</li></ul><li>hidden effect:</li><ul><li>remove province modifier = dig_3</li></ul></ul></ul><li>Else if has capital scope has province modifier is dig 4:</li><ul><li>capital scope:</li><ul><li>add permanent province modifier:</li><ul><li>name = dig_5</li><li>duration = -1</li></ul><li>hidden effect:</li><ul><li>remove province modifier = dig_4</li></ul></ul></ul><li>Else if has capital scope has province modifier is dig 5:</li><ul><li>capital scope:</li><ul><li>add permanent province modifier:</li><ul><li>name = dig_6</li><li>duration = -1</li></ul><li>hidden effect:</li><ul><li>remove province modifier = dig_5</li></ul></ul></ul><li>Else if has capital scope has province modifier is dig 6:</li><ul><li>capital scope:</li><ul><li>add permanent province modifier:</li><ul><li>name = dig_7</li><li>duration = -1</li></ul><li>hidden effect:</li><ul><li>remove province modifier = dig_6</li></ul></ul></ul><li>Else if has capital scope has province modifier is dig 7:</li><ul><li>capital scope:</li><ul><li>add permanent province modifier:</li><ul><li>name = dig_8</li><li>duration = -1</li></ul><li>hidden effect:</li><ul><li>remove province modifier = dig_7</li></ul></ul></ul><li>Else if has capital scope has province modifier is dig 8:</li><ul><li>capital scope:</li><ul><li>add permanent province modifier:</li><ul><li>name = dig_9</li><li>duration = -1</li></ul><li>hidden effect:</li><ul><li>remove province modifier = dig_8</li></ul></ul></ul><li>Else if has capital scope has province modifier is dig 9:</li><ul><li>capital scope:</li><ul><li>add permanent province modifier:</li><ul><li>name = dig_10</li><li>duration = -1</li></ul><li>hidden effect:</li><ul><li>remove province modifier = dig_9</li></ul></ul></ul><li>country gets the modifier remnant_dig for 50 years</li><li>If has check variable has awakeningColonial is 100:</li><ul><li>country gets the modifier remnant_colonial_small for 50 years</li></ul><li>If has check variable has awakeningArmy is 100:</li><ul><li>country gets the modifier remnant_army_small for 50 years</li></ul><li>raise stability to neutral = yes</li></ul>

___
##We are ready to send settlers out once again

###Available if:
<li>check variable:</li><ul><li>awakeningColonial is at least 100</li></ul>

###AI weighting:
AI weights this option at 80


###Efects:<ul><li>add prestige = 10</li><li>country gets the modifier remnant_colonial for 50 years</li><li>If has check variable has awakeningDig is 100:</li><ul><li>country gets the modifier remnant_dig_small for 50 years</li></ul><li>If has check variable has awakeningArmy is 100:</li><ul><li>country gets the modifier remnant_army_small for 50 years</li></ul><li>raise stability to neutral = yes</li></ul>

___
##Our army shall be equipped with the finest weapons

###Available if:
<li>check variable:</li><ul><li>awakeningArmy is at least 100</li></ul>

###AI weighting:
AI weights this option at 10


###Efects:<ul><li>add prestige = 10</li><li>country gets the modifier remnant_army for 50 years</li><li>If has check variable has awakeningDig is 100:</li><ul><li>country gets the modifier remnant_dig_small for 50 years</li></ul><li>If has check variable has awakeningColonial is 100:</li><ul><li>country gets the modifier remnant_colonial_small for 50 years</li></ul><li>raise stability to neutral = yes</li></ul>
