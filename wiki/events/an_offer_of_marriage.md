#Information
 - Title: An Offer of Marriage
 - ID: consort_events.1
#Description
An Offer of Marriage
#Mean Time to Happen:
Base time = 360 months

#Options

___
##Accept the offer.

###Efects:<ul><li>goto = origin_of_queens_family</li><li>custom tooltip = consort_events.1.a.tt</li><li>add years of income = 0.15</li><li>event target:origin of queens family:</li><ul><li>add province modifier:</li><ul><li>name = "domain_of_spouses_family"</li><li>duration = -1</li></ul></ul><li>give estate land share small:</li><ul><li>estate = estate_nobles</li></ul><li>define consort:</li><ul><li>female = yes</li></ul></ul>

___
##[Root.Monarch.GetName] must save [Root.Monarch.GetHerselfHimself] for a better offer.

###Efects:<ul><li>add prestige = 10</li><li>If has estate is estate nobles:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_nobles</li><li>loyalty = -5</li></ul></ul></ul>
