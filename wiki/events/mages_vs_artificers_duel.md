#Information
 - Title: Mages vs Artificers Duel
 - ID: new_sun_cult.202
#Description
Mages vs Artificers Duel
#Options

___
##Mages will strike first!

###Efects:<ul><li>custom tooltip = nsc_duel_mages_first_tt</li><li>set province flag [nsc_duel](../flags/nsc_duel.md)</li><li>If has units in province is 1:</li><ul><li>set province flag [nsc_duel_null](../flags/nsc_duel_null.md)</li></ul><li>spawn rebels:</li><ul><li>type = mage_duelists_rebels</li><li>size = 2</li></ul><li>spawn rebels:</li><ul><li>type = artificer_duelists_rebels</li><li>size = 2</li></ul></ul>

___
##Artificers will strike first!

###Efects:<ul><li>custom tooltip = nsc_duel_artificer_first_tt</li><li>set province flag [nsc_duel](../flags/nsc_duel.md)</li><li>If has units in province is 1:</li><ul><li>set province flag [nsc_duel_null](../flags/nsc_duel_null.md)</li></ul><li>spawn rebels:</li><ul><li>type = artificer_duelists_rebels</li><li>size = 2</li></ul><li>spawn rebels:</li><ul><li>type = mage_duelists_rebels</li><li>size = 2</li></ul></ul>

___
##Toss a coin. Then no one can complain.

###One of the following randomly happens:
Outcome 1:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>spawn rebels:</li><ul><li>type = mage_duelists_rebels</li><li>size = 2</li></ul><li>spawn rebels:</li><ul><li>type = artificer_duelists_rebels</li><li>size = 2</li></ul></ul>
Outcome 2:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>spawn rebels:</li><ul><li>type = artificer_duelists_rebels</li><li>size = 2</li></ul><li>spawn rebels:</li><ul><li>type = mage_duelists_rebels</li><li>size = 2</li></ul></ul>

###Efects:<ul><li>set province flag [nsc_duel](../flags/nsc_duel.md)</li><li>If has units in province is 1:</li><ul><li>set province flag [nsc_duel_null](../flags/nsc_duel_null.md)</li></ul></ul>
