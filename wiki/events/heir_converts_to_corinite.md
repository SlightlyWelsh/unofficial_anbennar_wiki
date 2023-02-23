#Information
 - Title: Heir Converts to Corinite
 - ID: deluge.5
#Description
Heir Converts to Corinite
#Mean Time to Happen:
Base time = 150 months
 - Multiplied by 0.8 if has region is west castanor region, and has region is inner castanor region, and has region is south castanor region, and has region is the borders region
 - Multiplied by 3 if does not have religion group is cannorian
 - Multiplied by 4 if has heir culture is moon elf, and has heir culture is wood elf, and has heir culture is sun elf, and has heir culture is imperial gnome
 - Multiplied by 2 if has heir culture is high lorentish, and has heir culture is low lorentish, and has heir culture is sorncosti, and has heir culture is roilsardi, and has heir culture is crownsman, and has heir culture is esmari
 - Multiplied by 0.5 if has personal deity is corin
 - Multiplied by 10 if has personal deity is adean
 - Multiplied by 5 if has personal deity is ara
 - Multiplied by 0.77 if has heir culture is vernman, and has heir culture is arbarani

#Options

___
##[Root.Heir.GetSheHeCap] is still our heir.

###Available if:
<li>religion is regent_court</li>

###Efects:<ul><li>add prestige = -10</li><li>add legitimacy = -10</li><li>set heir religion = corinite</li></ul>

___
##We can't allow [Root.Heir.GetHerHim] to inherit.

###Available if:
<li>religion is regent_court</li>

###Efects:<ul><li>add prestige = -60</li><li>add legitimacy = -10</li><li>remove heir:</li><ul></ul></ul>

___
##Why would [Root.Heir.GetSheHe] abandon our ancestors for this?

###Available if:
<li>None of the following:</li><ul><li>religion group is cannorian</li></ul>

###Efects:<ul><li>add prestige = -10</li><li>add legitimacy = -10</li><li>set heir religion = corinite</li></ul>

___
##We can't allow [Root.Heir.GetHerHim] to inherit.

###Available if:
<li>None of the following:</li><ul><li>religion group is cannorian</li></ul>

###Efects:<ul><li>add prestige = -60</li><li>add legitimacy = -10</li><li>remove heir:</li><ul></ul></ul>
