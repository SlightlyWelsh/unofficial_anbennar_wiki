#Information
 - Title: Times of Need
 - ID: consort_events.56
#Description
Times of Need
#Mean Time to Happen:
Base time = 250 months

#Options

___
##Our coffers are getting worryingly light.

###Available if:
<li>Any of the following:</li><ul><li>num of loans is at least 1</li><li>None of the following:</li><ul><li>treasury is at least 100</li></ul></ul>

###Efects:<ul><li>custom tooltip = consort_events.56.a.tt</li><li>set ruler flag [asked_foreign_in_laws_for_help](../flags/asked_foreign_in_laws_for_help.md)</li><li>set country flag [asked_consort_for_money](../flags/asked_consort_for_money.md)</li><li>event target:marriage partner:</li><ul><li>the event [Friends in Need](../events/friends_in_need.md) happens</li></ul></ul>

___
##We do need some help managing our administration.

###Available if:
<li>None of the following:</li><ul><li>adm power is at least 500</li></ul>

###Efects:<ul><li>custom tooltip = consort_events.56.b.tt</li><li>set ruler flag [asked_foreign_in_laws_for_help](../flags/asked_foreign_in_laws_for_help.md)</li><li>set country flag [asked_consort_for_adm](../flags/asked_consort_for_adm.md)</li><li>event target:marriage partner:</li><ul><li>the event [Friends in Need](../events/friends_in_need.md) happens</li></ul></ul>

___
##Our diplomats could surely learn from those of [marriage_partner.GetName].

###Available if:
<li>None of the following:</li><ul><li>dip power is at least 500</li></ul>

###Efects:<ul><li>custom tooltip = consort_events.56.c.tt</li><li>set ruler flag [asked_foreign_in_laws_for_help](../flags/asked_foreign_in_laws_for_help.md)</li><li>set country flag [asked_consort_for_dip](../flags/asked_consort_for_dip.md)</li><li>event target:marriage partner:</li><ul><li>the event [Friends in Need](../events/friends_in_need.md) happens</li></ul></ul>

___
##Perhaps we can borrow one of [marriage_partner.Monarch.GetTitle] [marriage_partner.Monarch.GetName]'s generals?

###Available if:
<li>None of the following:</li><ul><li>mil power is at least 500</li></ul>

###Efects:<ul><li>custom tooltip = consort_events.56.e.tt</li><li>set ruler flag [asked_foreign_in_laws_for_help](../flags/asked_foreign_in_laws_for_help.md)</li><li>set country flag [asked_consort_for_mil](../flags/asked_consort_for_mil.md)</li><li>event target:marriage partner:</li><ul><li>the event [Friends in Need](../events/friends_in_need.md) happens</li></ul></ul>

___
##We are in need of more men for our army.

###Available if:
<li>None of the following:</li><ul><li>manpower percentage is at least 0.7</li></ul><li>event target:marriage partner:</li><ul><li>manpower percentage is at least 0.1</li><li>manpower is at least 1</li></ul>

###Efects:<ul><li>custom tooltip = consort_events.56.f.tt</li><li>set ruler flag [asked_foreign_in_laws_for_help](../flags/asked_foreign_in_laws_for_help.md)</li><li>set country flag [asked_consort_for_manpower](../flags/asked_consort_for_manpower.md)</li><li>event target:marriage partner:</li><ul><li>the event [Friends in Need](../events/friends_in_need.md) happens</li></ul></ul>

___
##We do not need any help from [marriage_partner.GetName] or house [marriage_partner.Monarch.Dynasty.GetName]!

###Efects:<ul><li>add prestige = 10</li></ul>
