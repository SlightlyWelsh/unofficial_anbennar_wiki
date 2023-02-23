#Information
 - Title: Great Expectations
 - ID: consort_events.3
#Description
Great Expectations
#Mean Time to Happen:
Base time = 800 months
 - Multiplied by 0.9 if has AND has estate is estate nobles, and AND has estate influence has estate is estate nobles, and estate influence has influence is 60; and does not have estate is estate nobles; and does not have legitimacy is 60
 - Multiplied by 0.65 if has ruler flag is [accepted_help_from_spouses_family](../flags/accepted_help_from_spouses_family.md)
 - Multiplied by 1.5 if has ruler flag is [helped_spouses_family](../flags/helped_spouses_family.md)

#Options

___
##Anything for our dear [Root.Consort.GetTitle].

###Efects:<ul><li>If has ruler flag is [accepted_help_from_spouses_family](../flags/accepted_help_from_spouses_family.md):</li><ul><li>clr ruler flag [accepted_help_from_spouses_family](../flags/accepted_help_from_spouses_family.md)</li></ul><li>set ruler flag [helped_spouses_family](../flags/helped_spouses_family.md)</li><li>trigger switch:</li><ul><li>on trigger = has_country_flag</li><li>develop seat province:</li><ul><li>custom tooltip = consort_events.3.a.tt.1</li><li>If random owned province has province modifier is domain of spouses family:</li><ul><li>add base tax = 1</li></ul><li>add adm power = -100</li><li>clr country flag [develop_seat_province](../flags/develop_seat_province.md)</li></ul><li>pay money:</li><ul><li>custom tooltip = consort_events.3.a.tt.2</li><li>add years of income = -0.25</li><li>clr country flag [pay_money](../flags/pay_money.md)</li></ul><li>pay legitimacy or give noble influence:</li><ul><li>custom tooltip = consort_events.3.a.tt.3</li><li>If has estate is estate nobles:</li><ul><li>add estate influence modifier:</li><ul><li>estate = estate_nobles</li><li>desc = EST_VAL_FURTHERED_SPOUSES_FAMILY_NOBLES</li><li>influence = 10</li><li>duration = 7300</li></ul></ul><li>If does not have estate is estate nobles:</li><ul><li>add legitimacy = -10</li><li>add horde unity = -10</li></ul><li>clr country flag [pay_legitimacy_or_give_noble_influence](../flags/pay_legitimacy_or_give_noble_influence.md)</li></ul><li>kick advisor:</li><ul><li>custom tooltip = consort_events.3.a.tt.4</li><li>kill advisor = random</li><li>add adm power = -50</li><li>clr country flag [kick_advisor](../flags/kick_advisor.md)</li><li>reduce meritocracy effect = yes</li></ul><li>pay mil trad:</li><ul><li>If has army tradition is 50:</li><ul><li>custom tooltip = consort_events.3.a.tt.5</li><li>add army tradition = -20</li></ul><li>If does not have army tradition is 50:</li><ul><li>custom tooltip = consort_events.3.a.tt.6b</li><li>add corruption = 1</li></ul><li>clr country flag [pay_mil_trad](../flags/pay_mil_trad.md)</li></ul><li>pay nav trad:</li><ul><li>If has num of ports is 5, and has navy tradition is 50:</li><ul><li>custom tooltip = consort_events.3.a.tt.6</li><li>add navy tradition = -20</li></ul><li>If does not have num of ports is 5; and does not have navy tradition is 50:</li><ul><li>custom tooltip = consort_events.3.a.tt.6b</li><li>add corruption = 1</li></ul><li>clr country flag [pay_nav_trad](../flags/pay_nav_trad.md)</li></ul></ul><li>custom tooltip = consort_events.3.a.tt.0</li></ul>

___
##Sorry, no special favors.

###Efects:<ul><li>custom tooltip = consort_events.3.b.tt</li><li>set ruler flag [refused_to_help_spouses_family](../flags/refused_to_help_spouses_family.md)</li><li>add prestige = -10</li><li>If random owned province has province modifier is domain of spouses family:</li><ul><li>add local autonomy = 25</li></ul><li>clr country flag [develop_seat_province](../flags/develop_seat_province.md)</li><li>clr country flag [pay_money](../flags/pay_money.md)</li><li>clr country flag [pay_legitimacy_or_give_noble_influence](../flags/pay_legitimacy_or_give_noble_influence.md)</li><li>clr country flag [kick_advisor](../flags/kick_advisor.md)</li><li>clr country flag [pay_mil_trad](../flags/pay_mil_trad.md)</li><li>clr country flag [pay_nav_trad](../flags/pay_nav_trad.md)</li></ul>
