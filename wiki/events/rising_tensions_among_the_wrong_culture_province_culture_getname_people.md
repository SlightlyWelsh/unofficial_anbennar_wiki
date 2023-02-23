#Information
 - Title: Rising Tensions among the [wrong_culture_province.Culture.GetName] People
 - ID: culture_religion_events.17
#Description
Rising Tensions among the [wrong_culture_province.Culture.GetName] People
#Mean Time to Happen:
Base time = 1 days

#Options

___
##We have ministers who can communicate with these Barbarians.

###Available if:
<li>employed advisor:</li><ul><li>culture is event_target:wrong_culture_province</li></ul>

###Efects:<ul><li>If has employed advisor has category is ADM, and employed advisor has culture is event target:wrong culture province:</li><ul><li>add adm power = -10</li></ul><li>Else if has employed advisor has category is DIP:</li><ul><li>add dip power = -10</li></ul><li>else:</li><ul><li>add mil power = -10</li></ul></ul>

___
##[Root.Monarch.GetName] [Root.Monarch.GetHerselfHimself] might be able to sway them.

###Available if:
<li>ruler culture is event_target:wrong_culture_province</li>

###Efects:<ul><li>add prestige = -5</li></ul>

___
##[Root.Heir.GetName] has always had a way with these people.

###Available if:
<li>heir culture is event_target:wrong_culture_province</li><li>None of the following:</li><ul><li>ruler culture is event_target:wrong_culture_province</li></ul>

###Efects:<ul><li>add prestige = -5</li></ul>

___
##Perhaps [Root.Consort.GetName] can convince them of our good will?

###Available if:
<li>consort culture is event_target:wrong_culture_province</li><li>None of the following:</li><ul><li>heir culture is event_target:wrong_culture_province</li></ul><li>NOT:</li><ul><li>ruler culture is event_target:wrong_culture_province</li></ul>

###Efects:<ul><li>add prestige = -5</li></ul>

___
##Best send in soldiers before this escalates.

###Efects:<ul><li>event target:wrong culture province:</li><ul><li>spawn rebels:</li><ul><li>type = nationalist_rebels</li><li>size = 2</li></ul></ul></ul>

___
##Perhaps some tax exemptions could ease their burden.

###Efects:<ul><li>add years of income = -0.15</li></ul>
