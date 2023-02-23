#Information
 - Title: Disloyal Iosahar Declare War
 - ID: ynn_debate.19
#Description
Disloyal Iosahar Declare War
#Options

___
##Fetch me a blade!

###AI weighting:
AI weights this option at 3


###Efects:<ul><li>If random subject country has liberty desire is 50, and  is subject of type is ynnic iosahar, and  does not have AND has liberty desire is 50, and AND is subject of type is ynnic iosahar, and AND is subject of is ROOT, and AND has total development is PREV:</li><ul><li>set country flag [ynn_iosahar_is_revolting](../flags/ynn_iosahar_is_revolting.md)</li><li>save event target as = ynn_civil_war_leader</li><li>grant independence = yes</li></ul><li>If every subject country has liberty desire is 50, and  is subject of type is ynnic iosahar:</li><ul><li>set country flag [ynn_iosahar_is_revolting](../flags/ynn_iosahar_is_revolting.md)</li><li>event target:ynn civil war leader:</li><ul><li>create subject:</li><ul><li>subject type = ynnic_iosahar</li><li>subject = PREV</li></ul></ul></ul><li>event target:ynn civil war leader:</li><ul><li>declare war with cb:</li><ul><li>who = ROOT</li><li>casus belli = cb_iosahar_annex</li></ul></ul></ul>
