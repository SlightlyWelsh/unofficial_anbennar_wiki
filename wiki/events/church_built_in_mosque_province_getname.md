#Information
 - Title: Church built in [mosque_province.GetName]
 - ID: propagate_religion_events.5
#Description
Church built in [mosque_province.GetName]
#Mean Time to Happen:
Base time = 1 days

#Options

___
##We cannot allow this.

###Efects:<ul><li>event target:mosque province:</li><ul><li>add province modifier:</li><ul><li>name = "religious_community_isolated"</li><li>duration = 3650</li></ul></ul><li>event target:converter country:</li><ul><li>add opinion:</li><ul><li>modifier = discriminated_our_countrymen</li><li>who = ROOT</li></ul></ul></ul>

___
##Let us provide them with the support they need to build a better community.

###Efects:<ul><li>custom tooltip = explain_conversion_strength_in_true_religion_provinces</li><li>event target:mosque province:</li><ul><li>If does not have building is temple; and does not have building is cathedral; and  has num free building slots is 1:</li><ul><li>add building = temple</li></ul><li>add base tax = 1</li><li>If area has owned by is ROOT, and does not have province id is PREV; and does not have religion is PREV:</li><ul><li>add local autonomy = 15</li><li>add province modifier:</li><ul><li>name = "mosque_of_x"</li><li>duration = 3650</li></ul></ul></ul></ul>
