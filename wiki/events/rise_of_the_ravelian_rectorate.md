#Information
 - Title: Rise of the Ravelian Rectorate
 - ID: ravelian.3
#Description
Rise of the Ravelian Rectorate
#Mean Time to Happen:
Base time = 60 months
 - Multiplied by 2 if does not have culture is human is yes
 - Multiplied by 0.5 if is year is 1650
 - Multiplied by 0.75 if has ruler has personality is free thinker personality
 - Multiplied by 2 if has ruler has personality is righteous personality
 - Multiplied by 0.75 if has ruler has personality is scholar personality
 - Multiplied by 0.75 if does not have num of cities is 2
 - Multiplied by 1.5 if has religion is regent court
 - Multiplied by 0.5 if has tag is A38
 - Multiplied by 0.5 if has num of owned provinces with has value is 1, and num of owned provinces with has development is 30
 - Multiplied by 0.5 if has religion years has corinite is 125
 - Multiplied by 0.5 if has religion years has corinite is 150
 - Multiplied by 0.9 if has innovativeness ideas is 5
 - Multiplied by 0.9 if has innovativeness ideas is 6
 - Multiplied by 0.9 if has innovativeness ideas is 7
 - Multiplied by 1.5 if does not have innovativeness ideas is 3
 - Multiplied by 2 if does not have innovativeness ideas is 2
 - Multiplied by 2 if does not have innovativeness ideas is 1
 - Multiplied by 0.8 if has idea is humanist tolerance
 - Multiplied by 0.5 if has num of rebel controlled provinces is 1
 - Multiplied by 0.8 if has total development is 100
 - Multiplied by 0.75 if has region is east dameshead region, and has region is the borders region, and has area is konwell area

#Options

___
##Become the Rectorate

###AI weighting:
AI weights this option at 70


###Efects:<ul><li>enable religion = ravelian</li><li>If random owned province has can have center of reformation trigger has RELIGION is ravelian; and  has province modifier is ravelian lodge:</li><ul><li>change religion = ravelian</li><li>add reform center = ravelian</li><li>add permanent province modifier:</li><ul><li>name = "religious_zeal_at_conv"</li><li>duration = 9000</li></ul></ul><li>capital scope:</li><ul><li>change religion = ravelian</li><li>set province flag [ravelian_state_capital](../flags/ravelian_state_capital.md)</li><li>add permanent province modifier:</li><ul><li>name = "religious_zeal_at_conv"</li><li>duration = 9000</li></ul><li>save global event target as = ravelian_state_spawned_capital</li></ul><li>country gets the modifier "conversion_zeal" for 10 years</li><li>custom tooltip = ravelian_chapter_lodge_convert_tt</li><li>hidden effect:</li><ul><li>If every owned province has province modifier is ravelian lodge:</li><ul><li>change religion = ravelian</li><li>add permanent province modifier:</li><ul><li>name = "religious_zeal_at_conv"</li><li>duration = 9000</li></ul><li>add cardinal = yes</li><li>remove province modifier = ravelian_lodge</li></ul><li>If every owned province has province modifier is ravelian society:</li><ul><li>change religion = ravelian</li><li>add permanent province modifier:</li><ul><li>name = "religious_zeal_at_conv"</li><li>duration = 9000</li></ul><li>remove province modifier = ravelian_society</li></ul></ul><li>change religion = ravelian</li><li>hidden effect:</li><ul><li>add reform desire = -10</li></ul><li>change tag = Z97</li><li>hidden effect:</li><ul><li>restore country name = yes</li></ul><li>swap non generic missions = yes</li><li>change government = theocracy</li><li>add government reform = papacy_reform</li><li>add curia treasury = 1000</li><li>If does not have custom ideas:</li><ul><li>the event [New Traditions & Ambitions](../events/new_traditions_ambitions.md) happens</li></ul><li>hidden effect:</li><ul><li>set ruler = torrieth</li></ul><li>hidden effect:</li><ul><li>If every country has capital scope has continent is europe; and has capital scope has continent is north america; and has capital scope has continent is south america; and has has province modifier is ravelian society, and has province modifier is ravelian lodge; and does not have tag is Z97:</li><ul><li>the event [Ravelianism Religion Founded!](../events/ravelianism_religion_founded.md) happens</li></ul><li>577:</li><ul><li>fire province event [new_sun_cult.8](new_sun_cult.8_slug) in 3650 to 3650 days</li></ul></ul></ul>

___
##Politely decline

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>hidden effect:</li><ul><li>If random known country is not defender of faith, and  has religion group is cannorian, and does not have reform is papacy reform; and  has capital scope has continent is europe; and does not have num of cities is 6; and  has any owned province has can have center of reformation trigger has RELIGION is ravelian; and any owned province has province modifier is ravelian lodge:</li><ul><li>the event [Rise of the Ravelian Rectorate](../events/rise_of_the_ravelian_rectorate.md) happens</li></ul><li>set global flag [allow_non_ideal_rectorate_candidate](../flags/allow_non_ideal_rectorate_candidate.md)</li></ul></ul>


#Pages with same name:
The following pages have the same name as this page:
 - [rise_of_the_ravelian_rectorate_1](rise_of_the_ravelian_rectorate_1.md)
