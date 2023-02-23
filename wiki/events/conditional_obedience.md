#Information
 - Title: Conditional Obedience
 - ID: flavour_zongji.4
#Description
Conditional Obedience
#Options

___
##Become their vassal

###AI weighting:
AI weights this option at 50
 - Multiplied by 2 if has any neighbor country has tag is R62
 - Multiplied by 2 if has any neighbor country has country flag is [great_conqueror_flag](../flags/great_conqueror_flag.md)


###Efects:<ul><li>custom tooltip = Y25_hubao_claim_tt</li><li>FROM:</li><ul><li>the event [Offer Accepted](../events/offer_accepted.md) happens</li></ul><li>hidden effect:</li><ul><li>FROM:</li><ul><li>vassalize = ROOT</li></ul><li>ROOT:</li><ul><li>If yanshen superregion has culture is hill yan, and  has religion is lefthand path:</li><ul><li>add permanent claim = ROOT</li></ul></ul></ul></ul>

___
##Remain Free

###AI weighting:
AI weights this option at 20
 - Multiplied by 0 if has total development is 80


###Efects:<ul><li>FROM:</li><ul><li>the event [Offer Declined](../events/offer_declined.md) happens</li></ul><li>hidden effect:</li><ul><li>FROM:</li><ul><li>If yanshen superregion is core is ROOT:</li><ul><li>add permanent claim = ROOT</li></ul></ul></ul><li>custom tooltip = y25_hubao_alt_tt</li><li>FROM:</li><ul><li>add casus belli:</li><ul><li>target = Y03</li><li>type = cb_vassalize_mission</li><li>months = 300</li></ul></ul></ul>
