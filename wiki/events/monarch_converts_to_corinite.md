#Information
 - Title: $MONARCH$ converts to Corinite
 - ID: deluge.7
#Description
$MONARCH$ converts to Corinite
#Mean Time to Happen:
Base time = 150 months
 - Multiplied by 0.8 if has region is west castanor region, and has region is inner castanor region, and has region is south castanor region, and has region is the borders region
 - Multiplied by 4 if does not have religion group is cannorian
 - Multiplied by 4 if has ruler culture is moon elf, and has ruler culture is wood elf, and has ruler culture is sun elf, and has ruler culture is imperial gnome
 - Multiplied by 2 if has ruler culture is high lorentish, and has ruler culture is low lorentish, and has ruler culture is sorncosti, and has ruler culture is roilsardi, and has ruler culture is crownsman, and has ruler culture is esmari
 - Multiplied by 0.5 if has personal deity is corin
 - Multiplied by 10 if has personal deity is adean
 - Multiplied by 5 if has personal deity is ara
 - Multiplied by 3 if has ruler has personality is zealot personality
 - Multiplied by 0.77 if has ruler culture is vernman, and has ruler culture is arbarani

#Options

___
##This will bring trouble.

###Available if:
<li>religion is regent_court</li>

###AI weighting:
AI weights this option at 70
 - Multiplied by 10 if has personal deity is adean
 - Multiplied by 5 if has personal deity is ara
 - Multiplied by 0.5 if has ruler has personality is zealot personality
 - Multiplied by 1.5 if has capital scope has region is lencenor region; and has capital scope has region is west dameshead region; and has capital scope has region is small country region; and has capital scope has region is dragon coast region; and has capital scope has region is damescrown region; and has capital scope has region is esmaria region


###Efects:<ul><li>add prestige = -5</li><li>add legitimacy = -10</li><li>add devotion = -10</li><li>reduce stability or adm power = yes</li><li>set ruler religion = corinite</li></ul>

___
##$MONARCH$ seeks to bring the rest of the country with [Root.Monarch.GetHerHim].

###Available if:
<li>religion is regent_court</li>

###AI weighting:
AI weights this option at 30
 - Multiplied by 5 if has tag is B33, and has tag is B35, and has tag is A45, and has tag is U16
 - Multiplied by 3 if has capital scope has region is the borders region; and has capital scope has region is east dameshead region
 - Multiplied by 3 if has capital scope has region is west castanor region; and has capital scope has region is inner castanor region; and has capital scope has region is south castanor region; and has capital scope has region is the borders region; and does not have culture group is orcish; and does not have culture group is goblin
 - Multiplied by 0.25 if has culture group is elven, and has culture group is gnomish
 - Multiplied by 0.5 if has culture group is lencori, and has primary culture is crownsman, and has primary culture is esmari
 - Multiplied by 1.3 if has primary culture is vernman, and has primary culture is derannic, and has primary culture is arbarani, and has culture group is alenic
 - Multiplied by 2 if has personality is ai militarist
 - Multiplied by 1.5 if does not have religious unity is 0.5
 - Multiplied by 1.5 if does not have religious unity is 0.7
 - Multiplied by 1.5 if does not have religious unity is 0.9


###Efects:<ul><li>add prestige = -50</li><li>country gets the modifier "conversion_zeal" for 10 years</li><li>change religion = corinite</li><li>set ruler religion = corinite</li><li>set consort religion = corinite</li><li>set heir religion = corinite</li><li>capital scope:</li><ul><li>change religion = corinite</li></ul></ul>

___
##This will bring trouble.

###Available if:
<li>None of the following:</li><ul><li>religion group is cannorian</li></ul>

###AI weighting:
AI weights this option at 80


###Efects:<ul><li>add prestige = -15</li><li>add legitimacy = -10</li><li>add devotion = -15</li><li>reduce stability or adm power = yes</li><li>set ruler religion = corinite</li></ul>

___
##$MONARCH$ brings the rest of the country with [Root.Monarch.GetHerHim].

###Available if:
<li>None of the following:</li><ul><li>religion group is cannorian</li></ul>

###AI weighting:
AI weights this option at 20
 - Multiplied by 1.5 if does not have religious unity is 0.5
 - Multiplied by 1.5 if does not have religious unity is 0.7
 - Multiplied by 1.5 if does not have religious unity is 0.9


###Efects:<ul><li>add prestige = -50</li><li>reduce stability or adm power = yes</li><li>country gets the modifier "conversion_zeal" for 10 years</li><li>change religion = corinite</li><li>set ruler religion = corinite</li><li>set consort religion = corinite</li><li>set heir religion = corinite</li><li>capital scope:</li><ul><li>change religion = corinite</li></ul></ul>
