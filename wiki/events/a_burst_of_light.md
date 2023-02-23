#Information
 - Title: A Burst of Light
 - ID: varamhar_flavour.13
#Description
A Burst of Light
#Options

___
##A new power has come to this land.

###Available if:
<li>None of the following:</li><ul><li>check variable:</li><ul><li>which is varamharProjectDivinityCounter</li><li>value is at least 5</li></ul></ul>

###Efects:<ul><li>remove country modifier = varamhar_temporary_absence_of_the_monarch</li><li>country gets the modifier varamhar_loss_of_magical_talent for 20 years</li><li>add ruler modifier:</li><ul><li>name = varamhar_the_sun_reborn</li><li>duration = -1</li></ul><li>hidden effect:</li><ul><li>the event [Too Bright a Sun](../events/too_bright_a_sun.md) happens</li></ul><li>hidden effect:</li><ul><li>If does not have ruler has mage personality is yes:</li><ul><li>clear ruler personalities = yes</li><li>add ruler personality = immortal_personality</li><li>add ruler personality = mage_personality</li><li>add ruler personality = conqueror_personality</li><li>magic ruler give random spell school = yes</li><li>magic ruler give random spell school = yes</li><li>magic ruler give random spell school = yes</li><li>magic ruler give random spell school = yes</li><li>magic ruler give random spell school = yes</li><li>magic ruler give random spell school = yes</li><li>magic ruler give random spell school = yes</li><li>magic ruler give random spell school = yes</li><li>magic study level up evocation = yes</li><li>magic study level up evocation = yes</li><li>magic study level up evocation = yes</li><li>magic study level up divination = yes</li><li>magic study level up divination = yes</li><li>magic study level up divination = yes</li><li>magic study level up abjuration = yes</li><li>magic study level up abjuration = yes</li></ul><li>else:</li><ul><li>magic study level up evocation = yes</li><li>magic study level up evocation = yes</li><li>magic study level up evocation = yes</li><li>magic study level up divination = yes</li><li>magic study level up divination = yes</li><li>magic study level up divination = yes</li><li>magic study level up abjuration = yes</li><li>magic study level up abjuration = yes</li></ul></ul></ul>

___
##[Root.Monarch.GetName]... ascended?

###Available if:
<li>check variable:</li><ul><li>which is varamharProjectDivinityCounter</li><li>value is at least 5</li></ul><li>None of the following:</li><ul><li>check variable:</li><ul><li>which is varamharProjectDivinityCounter</li><li>value is at least 9</li></ul></ul>

###Efects:<ul><li>kill ruler = yes</li><li>country gets the modifier varamhar_loss_of_magical_talent for 20 years</li><li>add prestige = 10</li><li>country gets the modifier varamhar_ascended_ruler until otherwise removed</li></ul>

___
##Good times have come.

###Available if:
<li>check variable:</li><ul><li>which is varamharProjectDivinityCounter</li><li>value is at least 9</li></ul>

###Efects:<ul><li>remove country modifier = varamhar_temporary_absence_of_the_monarch</li><li>country gets the modifier varamhar_loss_of_magical_talent for 20 years</li><li>add ruler modifier:</li><ul><li>name = varamhar_blessed_of_surael</li><li>duration = -1</li></ul><li>hidden effect:</li><ul><li>If does not have ruler has mage personality is yes:</li><ul><li>clear ruler personalities = yes</li><li>add ruler personality = immortal_personality</li><li>add ruler personality = mage_personality</li><li>add ruler personality = just_personality</li><li>magic ruler give random spell school = yes</li><li>magic ruler give random spell school = yes</li><li>magic ruler give random spell school = yes</li><li>magic ruler give random spell school = yes</li><li>magic ruler give random spell school = yes</li><li>magic ruler give random spell school = yes</li><li>magic study level up evocation = yes</li><li>magic study level up evocation = yes</li><li>magic study level up divination = yes</li><li>magic study level up divination = yes</li><li>magic study level up abjuration = yes</li></ul><li>else:</li><ul><li>magic study level up evocation = yes</li><li>magic study level up evocation = yes</li><li>magic study level up divination = yes</li><li>magic study level up divination = yes</li><li>magic study level up abjuration = yes</li></ul></ul></ul>
