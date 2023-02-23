#Information
 - Title: Support from [Root.Overlord.GetAdjective] Factions
 - ID: tributary_events.27
#Description
Support from [Root.Overlord.GetAdjective] Factions
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Excellent!

###Efects:<ul><li>custom tooltip = tributary_events.27.a.tt</li><li>trigger switch:</li><ul><li>on trigger = has_country_flag</li><li>extra men:</li><ul><li>add yearly manpower = 1</li><li>clr country flag [extra_men](../flags/extra_men.md)</li></ul><li>extra tradition:</li><ul><li>add army tradition = 20</li><li>clr country flag [extra_tradition](../flags/extra_tradition.md)</li></ul><li>extra money:</li><ul><li>add years of income = 1</li><li>clr country flag [extra_money](../flags/extra_money.md)</li></ul></ul><li>overlord:</li><ul><li>the event [[From.GetName] Meddles in Politics](../events/from_getname_meddles_in_politics.md) happens</li><li>tooltip:</li><ul><li>add trust:</li><ul><li>who = ROOT</li><li>value = -5</li><li>mutual = yes</li></ul></ul></ul><li>event target:other tributary country:</li><ul><li>the event [[Root.Overlord.GetAdjective] Groups Support [From.GetName]!](../events/root_overlord_getadjective_groups_support_from_getname.md) happens</li></ul></ul>

___
##We will not meddle in the politics of the [Root.Overlord.GetAdjective] [Root.Overlord.GovernmentName].

###Efects:<ul><li>hidden effect:</li><ul><li>trigger switch:</li><ul><li>on trigger = has_country_flag</li><li>extra men:</li><ul><li>clr country flag [extra_men](../flags/extra_men.md)</li></ul><li>extra tradition:</li><ul><li>clr country flag [extra_tradition](../flags/extra_tradition.md)</li></ul><li>extra money:</li><ul><li>clr country flag [extra_money](../flags/extra_money.md)</li></ul></ul></ul><li>add prestige = 10</li></ul>
