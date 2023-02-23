#Information
 - Title: Marital Bliss
 - ID: consort_events.4
#Description
Marital Bliss
#Mean Time to Happen:
Base time = 600 months
 - Multiplied by 1.5 if has ruler flag is [accepted_help_from_spouses_family](../flags/accepted_help_from_spouses_family.md)
 - Multiplied by 0.95 if has consort dip is 4
 - Multiplied by 0.95 if has consort dip is 5
 - Multiplied by 0.9 if has consort dip is 6
 - Multiplied by 0.5 if has ruler flag is [helped_spouses_family](../flags/helped_spouses_family.md)

#Options

___
##May this union bring benefits to us both.

###Efects:<ul><li>set ruler flag [accepted_help_from_spouses_family](../flags/accepted_help_from_spouses_family.md)</li><li>trigger switch:</li><ul><li>on trigger = has_country_flag</li><li>in laws fund development:</li><ul><li>custom tooltip = consort_events.4.a.tt.1</li><li>If random owned province is state:</li><ul><li>add base tax = 1</li></ul><li>clr country flag [in_laws_fund_development](../flags/in_laws_fund_development.md)</li></ul><li>in laws provide money:</li><ul><li>custom tooltip = consort_events.4.a.tt.2</li><li>add years of income = 0.15</li><li>clr country flag [in_laws_provide_money](../flags/in_laws_provide_money.md)</li></ul><li>in laws provide mil advisor:</li><ul><li>custom tooltip = consort_events.4.a.tt.3</li><li>If has monthly income is 35:</li><ul><li>define advisor:</li><ul><li>type = recruitmaster</li><li>skill = 3</li><li>culture = event_target:domain_of_spouses_family_province</li><li>religion = event_target:domain_of_spouses_family_province</li><li>discount = yes</li></ul><li>add meritocracy effect = yes</li></ul><li>If does not have monthly income is 35:</li><ul><li>define advisor:</li><ul><li>type = recruitmaster</li><li>culture = event_target:domain_of_spouses_family_province</li><li>religion = event_target:domain_of_spouses_family_province</li><li>skill = 2</li><li>discount = yes</li></ul><li>add meritocracy effect = yes</li></ul><li>clr country flag [in_laws_provide_mil_advisor](../flags/in_laws_provide_mil_advisor.md)</li></ul><li>in laws provide dip advisor:</li><ul><li>custom tooltip = consort_events.4.a.tt.4</li><li>If has monthly income is 35:</li><ul><li>define advisor:</li><ul><li>type = trader</li><li>culture = event_target:domain_of_spouses_family_province</li><li>religion = event_target:domain_of_spouses_family_province</li><li>skill = 3</li><li>discount = yes</li></ul><li>add meritocracy effect = yes</li></ul><li>If does not have monthly income is 35:</li><ul><li>define advisor:</li><ul><li>type = trader</li><li>culture = event_target:domain_of_spouses_family_province</li><li>religion = event_target:domain_of_spouses_family_province</li><li>skill = 2</li><li>discount = yes</li></ul><li>add meritocracy effect = yes</li></ul></ul><li>in laws provide help with nobility:</li><ul><li>custom tooltip = consort_events.4.a.tt.5</li><li>If has estate is estate nobles:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_nobles</li><li>loyalty = 10</li></ul></ul><li>If does not have estate is estate nobles:</li><ul><li>add legitimacy = 10</li><li>add horde unity = 10</li></ul><li>clr country flag [in_laws_provide_help_with_nobility](../flags/in_laws_provide_help_with_nobility.md)</li></ul><li>in laws provide adm advisor:</li><ul><li>custom tooltip = consort_events.4.a.tt.6</li><li>If has monthly income is 35:</li><ul><li>define advisor:</li><ul><li>type = natural_scientist</li><li>culture = event_target:domain_of_spouses_family_province</li><li>religion = event_target:domain_of_spouses_family_province</li><li>skill = 3</li><li>discount = yes</li></ul><li>add meritocracy effect = yes</li></ul><li>If does not have monthly income is 35:</li><ul><li>define advisor:</li><ul><li>type = natural_scientist</li><li>culture = event_target:domain_of_spouses_family_province</li><li>religion = event_target:domain_of_spouses_family_province</li><li>skill = 2</li><li>discount = yes</li></ul><li>add meritocracy effect = yes</li></ul><li>clr country flag [pay_nav_trad](../flags/pay_nav_trad.md)</li></ul></ul><li>custom tooltip = consort_events.4.a.tt.0</li></ul>

___
##We must avoid indebting ourselves to the [Root.Consort.Dynasty.GetName] family.

###Efects:<ul><li>add prestige = 5</li><li>custom tooltip = consort_events.4.b.tt</li></ul>
