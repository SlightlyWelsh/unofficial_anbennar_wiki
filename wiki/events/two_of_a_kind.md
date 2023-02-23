#Information
 - Title: Two of a Kind
 - ID: consort_events.312
#Description
Two of a Kind
#Mean Time to Happen:
Base time = 460 months

#Options

___
##[Root.Consort.GetTitle] [Root.Consort.GetName] has a point! We shall invite [Root.Consort.GetHerHis] acquaintance to stay.

###Efects:<ul><li>custom tooltip = consort_events.312.a.tt</li><li>trigger switch:</li><ul><li>on trigger = has_ruler_flag</li><li>consort adm advisor:</li><ul><li>add meritocracy effect = yes</li><li>trigger switch:</li><ul><li>on trigger = has_country_flag</li><li>foreign advisor origin:</li><ul><li>If does not have monthly income is 25:</li><ul><li>define advisor:</li><ul><li>type = natural_scientist</li><li>skill = 2</li><li>discount = yes</li><li>female = yes</li><li>culture = event_target:consort_from_here</li><li>religion = event_target:consort_from_here</li></ul></ul><li>else:</li><ul><li>define advisor:</li><ul><li>type = natural_scientist</li><li>skill = 3</li><li>discount = yes</li><li>female = yes</li><li>culture = event_target:consort_from_here</li><li>religion = event_target:consort_from_here</li></ul></ul></ul><li>internal advisor origin:</li><ul><li>If does not have monthly income is 25:</li><ul><li>define advisor:</li><ul><li>type = natural_scientist</li><li>skill = 2</li><li>discount = yes</li><li>female = yes</li><li>culture = event_target:internal_origin_province</li><li>religion = event_target:internal_origin_province</li></ul></ul><li>else:</li><ul><li>define advisor:</li><ul><li>type = natural_scientist</li><li>skill = 3</li><li>discount = yes</li><li>female = yes</li><li>culture = event_target:internal_origin_province</li><li>religion = event_target:internal_origin_province</li></ul></ul></ul><li>no foreign advisor origin:</li><ul><li>If does not have monthly income is 25:</li><ul><li>define advisor:</li><ul><li>type = natural_scientist</li><li>skill = 2</li><li>discount = yes</li><li>female = yes</li></ul></ul><li>else:</li><ul><li>define advisor:</li><ul><li>type = natural_scientist</li><li>skill = 3</li><li>discount = yes</li><li>female = yes</li></ul></ul></ul></ul></ul><li>consort dip advisor:</li><ul><li>add meritocracy effect = yes</li><li>trigger switch:</li><ul><li>on trigger = has_country_flag</li><li>foreign advisor origin:</li><ul><li>If does not have monthly income is 25:</li><ul><li>define advisor:</li><ul><li>type = statesman</li><li>skill = 2</li><li>discount = yes</li><li>female = yes</li><li>culture = event_target:consort_from_here</li><li>religion = event_target:consort_from_here</li></ul></ul><li>else:</li><ul><li>define advisor:</li><ul><li>type = statesman</li><li>skill = 3</li><li>discount = yes</li><li>female = yes</li><li>culture = event_target:consort_from_here</li><li>religion = event_target:consort_from_here</li></ul></ul></ul><li>internal advisor origin:</li><ul><li>If does not have monthly income is 25:</li><ul><li>define advisor:</li><ul><li>type = statesman</li><li>skill = 2</li><li>discount = yes</li><li>female = yes</li><li>culture = event_target:internal_origin_province</li><li>religion = event_target:internal_origin_province</li></ul></ul><li>else:</li><ul><li>define advisor:</li><ul><li>type = statesman</li><li>skill = 3</li><li>discount = yes</li><li>female = yes</li><li>culture = event_target:internal_origin_province</li><li>religion = event_target:internal_origin_province</li></ul></ul></ul><li>no foreign advisor origin:</li><ul><li>If does not have monthly income is 25:</li><ul><li>define advisor:</li><ul><li>type = statesman</li><li>skill = 2</li><li>discount = yes</li><li>female = yes</li></ul></ul><li>else:</li><ul><li>define advisor:</li><ul><li>type = statesman</li><li>skill = 3</li><li>discount = yes</li><li>female = yes</li></ul></ul></ul></ul></ul><li>consort mil advisor:</li><ul><li>add meritocracy effect = yes</li><li>trigger switch:</li><ul><li>on trigger = has_country_flag</li><li>foreign advisor origin:</li><ul><li>If does not have monthly income is 25:</li><ul><li>define advisor:</li><ul><li>type = commandant</li><li>skill = 2</li><li>discount = yes</li><li>female = yes</li><li>culture = event_target:consort_from_here</li><li>religion = event_target:consort_from_here</li></ul></ul><li>else:</li><ul><li>define advisor:</li><ul><li>type = commandant</li><li>skill = 3</li><li>discount = yes</li><li>female = yes</li><li>culture = event_target:consort_from_here</li><li>religion = event_target:consort_from_here</li></ul></ul></ul><li>internal advisor origin:</li><ul><li>If does not have monthly income is 25:</li><ul><li>define advisor:</li><ul><li>type = commandant</li><li>skill = 2</li><li>discount = yes</li><li>female = yes</li><li>culture = event_target:internal_origin_province</li><li>religion = event_target:internal_origin_province</li></ul></ul><li>else:</li><ul><li>define advisor:</li><ul><li>type = commandant</li><li>skill = 3</li><li>discount = yes</li><li>female = yes</li><li>culture = event_target:internal_origin_province</li><li>religion = event_target:internal_origin_province</li></ul></ul></ul><li>no foreign advisor origin:</li><ul><li>If does not have monthly income is 25:</li><ul><li>define advisor:</li><ul><li>type = commandant</li><li>skill = 2</li><li>discount = yes</li><li>female = yes</li></ul></ul><li>else:</li><ul><li>define advisor:</li><ul><li>type = commandant</li><li>skill = 3</li><li>discount = yes</li><li>female = yes</li></ul></ul></ul></ul></ul></ul></ul>

___
##No, we will just ask [Root.Adm_Advisor.GetTitle] [Root.Adm_Advisor.GetName] to work harder.

###Available if:
<li>has ruler flag [consort_adm_advisor](../flags/consort_adm_advisor.md)</li>

###Efects:<ul><li>custom tooltip = consort_events.312.b.tt</li><li>add adm power = 50</li></ul>

___
##No, we will just ask [Root.Dip_Advisor.GetTitle] [Root.Dip_Advisor.GetName] to work harder.

###Available if:
<li>has ruler flag [consort_dip_advisor](../flags/consort_dip_advisor.md)</li>

###Efects:<ul><li>custom tooltip = consort_events.312.c.tt</li><li>add dip power = 50</li></ul>

___
##No, we will just ask [Root.Mil_Advisor.GetTitle] [Root.Mil_Advisor.GetName] to work harder.

###Available if:
<li>has ruler flag [consort_mil_advisor](../flags/consort_mil_advisor.md)</li>

###Efects:<ul><li>custom tooltip = consort_events.312.d.tt</li><li>add mil power = 50</li></ul>
