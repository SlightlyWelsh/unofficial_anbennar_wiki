#Information
 - Title: Stolen [fancy_trade_caravan_origin.GetFancyTradeGood]
 - ID: tribal_federation_events.8
#Description
Stolen [fancy_trade_caravan_origin.GetFancyTradeGood]
#Mean Time to Happen:
Base time = 1 days

#Options

___
##We must root out the raiders.

###AI weighting:
AI weights this option at 25


###Efects:<ul><li>event target:ambush province:</li><ul><li>If area has owned by is ROOT:</li><ul><li>add province modifier:</li><ul><li>name = "rooting_out_raiders"</li><li>duration = 3650</li></ul></ul></ul><li>event target:fancy trade caravan origin:</li><ul><li>If has owned by is ROOT:</li><ul><li>add province modifier:</li><ul><li>name = "unsafe_roads_hurting_demand"</li><li>duration = 3650</li></ul></ul><li>else:</li><ul><li>owner:</li><ul><li>the event [Stolen [fancy_trade_caravan_origin.GetFancyTradeGood]](../events/stolen_fancy_trade_caravan_origin_getfancytradegood_1.md) happens</li><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = unsafe_caravans</li></ul></ul></ul></ul></ul>

___
##Pay the protection money.

###AI weighting:
AI weights this option at 75


###Efects:<ul><li>add years of income = -0.05</li><li>event target:ambush province:</li><ul><li>If area has owned by is ROOT:</li><ul><li>add local autonomy = 20</li><li>add province modifier:</li><ul><li>name = "caravans_protected_by_raiders"</li><li>duration = 3650</li></ul></ul></ul></ul>


#Pages with same name:
The following pages have the same name as this page:
 - [stolen_fancy_trade_caravan_origin_getfancytradegood_1](stolen_fancy_trade_caravan_origin_getfancytradegood_1.md)
