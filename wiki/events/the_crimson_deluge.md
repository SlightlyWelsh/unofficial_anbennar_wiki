#Information
 - Title: The Crimson Deluge
 - ID: corinite.2
#Description
The Crimson Deluge
#Mean Time to Happen:
Base time = 1 days

#Options

___
##A dark omen of the usurper Corin attempting to do what Agrados once did!

###Available if:
<li>religion is regent_court</li><li>None of the following:</li><ul><li>Country is Corintar</li></ul>

###AI weighting:
AI weights this option at 70
 - Multiplied by 10 if has personal deity is adean
 - Multiplied by 5 if has personal deity is ara
 - Multiplied by 1.5 if has ruler has personality is calm personality
 - Multiplied by 1.5 if has ruler has personality is careful personality
 - Multiplied by 2 if has ruler has personality is zealot personality
 - Multiplied by 5 if has tag is A74, and has tag is B09, and has tag is B49
 - Multiplied by 1.5 if has capital scope has region is lencenor region; and has capital scope has region is west dameshead region; and has capital scope has region is small country region; and has capital scope has region is dragon coast region; and has capital scope has region is damescrown region; and has capital scope has region is esmaria region


###Efects:<ul><li>add stability = -2</li><li>custom tooltip = tooltip_remove_corin_personal_deity</li><li>custom tooltip = crimson_deluge_start_tooltip</li></ul>

___
##We must convert to Corin's faith to prevent more cataclysms!

###Available if:
<li>religion is regent_court</li>

###AI weighting:
AI weights this option at 30
 - Multiplied by 10 if has personal deity is corin
 - Multiplied by 100 if has tag is B02
 - Multiplied by 5 if has tag is B33, and has tag is B35, and has tag is A45, and has tag is U16
 - Multiplied by 0 if has tag is B58
 - Multiplied by 0 if has government is theocracy, and does not have reform is magocracy reform
 - Multiplied by 0 if is the emperor, and  has hre does not have religion treaty
 - Multiplied by 3 if has capital scope has region is the borders region; and has capital scope has region is east dameshead region
 - Multiplied by 3 if has capital scope has region is west castanor region; and has capital scope has region is inner castanor region; and has capital scope has region is south castanor region; and does not have culture group is orcish; and does not have culture group is goblin
 - Multiplied by 0.25 if has culture group is elven, and has culture group is gnomish
 - Multiplied by 0.5 if has culture group is lencori, and has primary culture is crownsman, and has primary culture is esmari
 - Multiplied by 1.3 if has primary culture is vernman, and has primary culture is derannic, and has primary culture is arbarani, and has culture group is alenic
 - Multiplied by 2 if has personality is ai militarist
 - Multiplied by 1.5 if has ruler has personality is free thinker personality
 - Multiplied by 1.5 if has ruler has personality is naive personality
 - Multiplied by 2 if has ruler has personality is sinner personality
 - Multiplied by 2 if has ruler has personality is tolerant personality
 - Multiplied by 2 if has ruler has personality is pious personality


###Efects:<ul><li>change religion = corinite</li><li>If random owned province has can have center of reformation trigger has RELIGION is corinite:</li><ul><li>change religion = corinite</li><li>add reform center = corinite</li><li>add permanent province modifier:</li><ul><li>name = "religious_zeal_at_conv"</li><li>duration = 9000</li></ul></ul><li>capital scope:</li><ul><li>change religion = corinite</li><li>add permanent province modifier:</li><ul><li>name = "religious_zeal_at_conv"</li><li>duration = 9000</li></ul></ul><li>country gets the modifier "conversion_zeal" for 10 years</li><li>reduce stability or adm power = yes</li><li>custom tooltip = crimson_deluge_start_tooltip</li></ul>

___
##It's the end of the world!

###Available if:
<li>None of the following:</li><ul><li>religion group is cannorian</li></ul>

###Efects:<ul><li>reduce stability or adm power = yes</li><li>custom tooltip = crimson_deluge_start_tooltip</li></ul>

___
##A sign of Corin's truth!

###Available if:
<li>religion is corinite</li>

###AI weighting:
AI weights this option at 1000


###Efects:<ul><li>add stability or adm power = yes</li><li>custom tooltip = crimson_deluge_start_tooltip</li></ul>


#Pages with same name:
The following pages have the same name as this page:
 - [the_crimson_deluge_1](the_crimson_deluge_1.md)
