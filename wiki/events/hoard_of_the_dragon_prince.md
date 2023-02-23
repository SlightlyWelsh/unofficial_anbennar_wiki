#Information
 - Title: Hoard of the Dragon Prince
 - ID: eordand.23
#Description
Hoard of the Dragon Prince
#Options

___
##His hoard, however meagre, is ours to claim!

###Efects:<ul><li>add treasury = 1000</li><li>add war exhaustion = -2</li><li>1991:</li><ul><li>add devastation = 75</li></ul><li>custom tooltip = eord_dragon_looted_tt</li><li>hidden effect:</li><ul><li>If every owned province has culture is rzentur:</li><ul><li>add province modifier:</li><ul><li>name = eord_dragon_hoard_looted</li><li>duration = 36500</li></ul></ul></ul></ul>

___
##Let us make a gift to Varlengeilt to appease his adherents.

###Efects:<ul><li>add treasury = -500</li><li>add prestige = -5</li><li>add dip power = 50</li><li>custom tooltip = eord_dragon_appeased_tt</li><li>hidden effect:</li><ul><li>If every owned province has culture is rzentur:</li><ul><li>add province modifier:</li><ul><li>name = eord_dragon_hoard_appeased</li><li>duration = 36500</li></ul></ul></ul></ul>

___
##Dragons are fearsome beasts: let us ignore them so they may ignore us.

###Efects:<ul><li>add prestige = -10</li><li>add legitimacy = -10</li><li>add devotion = -10</li><li>add republican tradition = -5</li></ul>

___
##Perhaps a skilled burglar may steal us the most prized artifacts undetected?

###Available if:
<li>Any of the following:</li><ul><li>has idea group spy_ideas</li><li>spymaster is at least 1</li></ul>

###Efects:<ul><li>random:</li><ul><li>chance = 70</li><li>add prestige = 10</li><li>add treasury = 1500</li><li>add adm power = 50</li><li>add dip power = 50</li><li>add mil power = 50</li></ul><li>random:</li><ul><li>chance = 30</li></ul></ul>

___
##As the Rzentur have for generations, let us send Varlengeilt a bride.

###Available if:


###Efects:<ul><li>random:</li><ul><li>chance = 75</li><li>add prestige = 25</li><li>add adm power = 50</li><li>add dip power = 50</li><li>add mil power = 50</li><li>If has government is monarchy, and has government is theocracy:</li><ul><li>define heir:</li><ul><li>name = "Barrsac"</li><li>change adm = 5</li><li>change dip = 5</li><li>change mil = 6</li></ul><li>add heir personality = mage_personality</li></ul><li>else:</li><ul><li>define advisor:</li><ul><li>type = commandant</li><li>name = "Barrsac"</li><li>skill = 3</li><li>location = 1191</li><li>discount = yes</li></ul></ul><li>custom tooltip = eord_dragon_appeased_tt</li><li>hidden effect:</li><ul><li>If every owned province has culture is rzentur:</li><ul><li>add province modifier:</li><ul><li>name = eord_dragon_hoard_appeased</li><li>duration = 36500</li></ul></ul></ul></ul><li>random:</li><ul><li>chance = 25</li></ul></ul>
