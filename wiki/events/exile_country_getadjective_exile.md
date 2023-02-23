#Information
 - Title: [exile_country.GetAdjective] Exile
 - ID: new_court_flavour_events.35
#Description
[exile_country.GetAdjective] Exile
#Mean Time to Happen:
Base time = 900 months
 - Multiplied by 1.5 if does not have current age is age of reformation

#Options

___
##His services will be useful.

###AI weighting:
AI weights this option at 2


###Efects:<ul><li>add prestige = 10</li><li>trigger switch:</li><ul><li>on trigger = has_country_flag</li><li>court flavour philosopher:</li><ul><li>generate exile advisor effect:</li><ul><li>advisor type = philosopher</li></ul></ul><li>court flavour natural scientist:</li><ul><li>generate exile advisor effect:</li><ul><li>advisor type = natural_scientist</li></ul></ul><li>court flavour artist:</li><ul><li>generate exile advisor effect:</li><ul><li>advisor type = artist</li></ul></ul><li>court flavour treasurer:</li><ul><li>generate exile advisor effect:</li><ul><li>advisor type = treasurer</li></ul></ul><li>court flavour theologian:</li><ul><li>generate exile advisor effect:</li><ul><li>advisor type = theologian</li></ul></ul><li>court flavour master of mint:</li><ul><li>generate exile advisor effect:</li><ul><li>advisor type = master_of_mint</li></ul></ul><li>court flavour inquisitor:</li><ul><li>generate exile advisor effect:</li><ul><li>advisor type = inquisitor</li></ul></ul><li>court flavour statesman:</li><ul><li>generate exile advisor effect:</li><ul><li>advisor type = statesman</li></ul></ul><li>court flavour naval reformer:</li><ul><li>generate exile advisor effect:</li><ul><li>advisor type = naval_reformer</li></ul></ul><li>court flavour trader:</li><ul><li>generate exile advisor effect:</li><ul><li>advisor type = trader</li></ul></ul><li>court flavour spymaster:</li><ul><li>generate exile advisor effect:</li><ul><li>advisor type = spymaster</li></ul></ul><li>court flavour diplomat:</li><ul><li>generate exile advisor effect:</li><ul><li>advisor type = diplomat</li></ul></ul><li>court flavour army reformer:</li><ul><li>generate exile advisor effect:</li><ul><li>advisor type = army_reformer</li></ul></ul><li>court flavour army organiser:</li><ul><li>generate exile advisor effect:</li><ul><li>advisor type = army_organiser</li></ul></ul><li>court flavour commandant:</li><ul><li>generate exile advisor effect:</li><ul><li>advisor type = commandant</li></ul></ul><li>court flavour quartermaster:</li><ul><li>generate exile advisor effect:</li><ul><li>advisor type = quartermaster</li></ul></ul><li>court flavour recruitmaster:</li><ul><li>generate exile advisor effect:</li><ul><li>advisor type = recruitmaster</li></ul></ul><li>court flavour fortification expert:</li><ul><li>generate exile advisor effect:</li><ul><li>advisor type = fortification_expert</li></ul></ul><li>court flavour grand captain:</li><ul><li>generate exile advisor effect:</li><ul><li>advisor type = grand_captain</li></ul></ul><li>court flavour colonial governor:</li><ul><li>generate exile advisor effect:</li><ul><li>advisor type = colonial_governor</li></ul></ul><li>court flavour navigator:</li><ul><li>generate exile advisor effect:</li><ul><li>advisor type = navigator</li></ul></ul></ul><li>reverse add opinion:</li><ul><li>who = event_target:exile_country</li><li>modifier = opinion_took_in_exiles</li></ul><li>hidden effect:</li><ul><li>random list:</li><ul><li>2:</li><ul><li>hidden effect:</li><ul><li>clear saved name = fleeing_advisor</li></ul></ul><li>1:</li><ul><li>the event [[exile_country.GetAdjective] Exiles](../events/exile_country_getadjective_exiles.md) happens</li></ul></ul></ul></ul>

___
##We have no room for him.

###Efects:<ul><li>reverse add opinion:</li><ul><li>who = event_target:exile_country</li><li>modifier = opinion_turned_away_exiles</li></ul><li>hidden effect:</li><ul><li>clear saved name = fleeing_advisor</li></ul></ul>
