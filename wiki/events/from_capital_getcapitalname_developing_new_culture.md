#Information
 - Title: [From.Capital.GetCapitalName] Developing New Culture
 - ID: diggy.119
#Description
[From.Capital.GetCapitalName] Developing New Culture
#Mean Time to Happen:
Base time = 30 years
 - Multiplied by 1.5 if has seat in parliament
 - Multiplied by 0.9 if has dwarven hold 6 is yes
 - Multiplied by 0.9 if has dwarven hold 7 is yes
 - Multiplied by 0.9 if has dwarven hold 8 is yes
 - Multiplied by 0.9 if has dwarven hold 9 is yes
 - Multiplied by 0.8 if has dwarven hold 10 is yes
 - Multiplied by 0.7 if has dwarven hold 11 is yes
 - Multiplied by 1.5 if has has province modifier is restored rail, and has province modifier is advanced rail
 - Multiplied by 2 if has any neighbor province has province modifier is advanced rail
 - Multiplied by 0.35 if has province modifier is hold foundry 2, and has province modifier is hold city 2, and has province modifier is hold artisan 2, and has province modifier is hold farm 2, and has province modifier is hold military 2
 - Multiplied by 0.25 if has province modifier is magma forge, and has province modifier is artificier hall, and has province modifier is engineer manufactory, and has province modifier is high gardens, and has province modifier is military academy
 - Multiplied by 1.5 if is state core is owner
 - Multiplied by 2 if has owner has stability is 3
 - Multiplied by 1.5 if has owner has stability is 1
 - Multiplied by 0.75 if does not have stability is 0
 - Multiplied by 0.5 if does not have stability is -2

#Options

___
##It was to be expected. Give the hold the respect it is deserved.

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>If area has culture group is dwarven:</li><ul><li>set province historical culture = yes</li><li>add local autonomy = 10</li></ul><li>add province modifier:</li><ul><li>name = diggy_autonomy_concessions</li><li>duration = 7300</li></ul></ul>

___
##Suppress them by force. Tear down their halls if you have to!

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>custom tooltip = diggy_dangerous_path_tt</li><li>If area has culture group is dwarven:</li><ul><li>add unrest = 5</li><li>set province historical culture = yes</li></ul><li>add province modifier:</li><ul><li>name = diggy_suppressed_populace</li><li>duration = 7300</li></ul><li>add province modifier:</li><ul><li>name = diggy_cultural_integration_initiative</li><li>duration = 1825</li></ul><li>hidden effect:</li><ul><li>fire province event [diggy.120](diggy.120_slug) in 1825 to 730 days</li></ul></ul>
