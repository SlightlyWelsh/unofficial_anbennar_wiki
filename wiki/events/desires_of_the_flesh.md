#Information
 - Title: Desires of the Flesh
 - ID: consort_events.314
#Description
Desires of the Flesh
#Mean Time to Happen:
Base time = 1000 months
 - Multiplied by 0.75 if has ruler has personality is cruel personality, and has ruler has personality is infertile personality, and has ruler has personality is babbling buffoon personality, and has ruler has personality is naive personality
 - Multiplied by 0.75 if has consort has personality is sinner personality, and has consort has personality is drunkard personality, and has consort has personality is fertile personality

#Options

___
##Now we know, at least. We can take measures to keep this quiet.

###Efects:<ul><li>custom tooltip = consort_events.314.a.tt</li><li>If has heir can be child of consort, and  has female consort:</li><ul><li>random:</li><ul><li>chance = 50</li><li>the event [A Royal Bastard](../events/a_royal_bastard.md) happens</li></ul></ul><li>If has heir can not be child of consort, and does not have female consort:</li><ul><li>add prestige = -10</li></ul></ul>

___
##This cannot continue. Find out what [Root.Adm_Advisor.GetName] wants for [Root.Adm_Advisor.GetHerHis] silence.

###Efects:<ul><li>custom tooltip = consort_events.314.b.tt</li><li>hidden effect:</li><ul><li>If has advisor is treasurer:</li><ul><li>remove advisor = treasurer</li></ul><li>If has advisor is philosopher:</li><ul><li>remove advisor = philosopher</li></ul><li>If has advisor is artist:</li><ul><li>remove advisor = artist</li></ul><li>If has advisor is master of mint:</li><ul><li>remove advisor = master_of_mint</li></ul><li>If has advisor is natural scientist:</li><ul><li>remove advisor = natural_scientist</li></ul><li>If has advisor is court mage:</li><ul><li>remove advisor = court_mage</li></ul></ul><li>If has monthly income is 30:</li><ul><li>add years of income = -0.25</li></ul><li>If does not have monthly income is 30:</li><ul><li>add treasury = -90</li></ul><li>hidden effect:</li><ul><li>If has heir can be child of consort, and  has female consort:</li><ul><li>random:</li><ul><li>chance = 10</li><li>the event [A Royal Bastard](../events/a_royal_bastard.md) happens</li></ul></ul></ul></ul>

___
##This is high treason, and no less! We shall have [Root.Adm_Advisor.GetName]'s head for this!

###Efects:<ul><li>custom tooltip = consort_events.314.c.tt</li><li>reduce meritocracy effect = yes</li><li>hidden effect:</li><ul><li>If has advisor is treasurer:</li><ul><li>kill advisor = treasurer</li></ul><li>If has advisor is philosopher:</li><ul><li>kill advisor = philosopher</li></ul><li>If has advisor is artist:</li><ul><li>kill advisor = artist</li></ul><li>If has advisor is master of mint:</li><ul><li>kill advisor = master_of_mint</li></ul><li>If has advisor is natural scientist:</li><ul><li>kill advisor = natural_scientist</li></ul><li>If has advisor is court mage:</li><ul><li>kill advisor = court_mage</li></ul></ul><li>capital scope:</li><ul><li>If area has owned by is ROOT:</li><ul><li>add province modifier:</li><ul><li>name = tyrannical_ruler</li><li>duration = 5475</li></ul></ul></ul><li>hidden effect:</li><ul><li>If has heir can be child of consort, and  has female consort:</li><ul><li>random:</li><ul><li>chance = 10</li><li>the event [A Royal Bastard](../events/a_royal_bastard.md) happens</li></ul></ul></ul></ul>

___
##We cannot have an adulteress for a Queen. [Root.Consort.GetName] must go.

###Available if:
<li>has female consort</li>

###Efects:<ul><li>If has religion is catholic, and  has exists is PAP:</li><ul><li>set country flag [desires_of_flesh_divorce](../flags/desires_of_flesh_divorce.md)</li></ul><li>divorce consort effect = yes</li></ul>

___
##We cannot have an adulterer for a Prince-Consort. [Root.Consort.GetName] must go.

###Available if:
<li>does not have female consort</li>

###Efects:<ul><li>If has religion is catholic, and  has exists is PAP:</li><ul><li>set country flag [desires_of_flesh_divorce](../flags/desires_of_flesh_divorce.md)</li></ul><li>divorce consort effect = yes</li></ul>
