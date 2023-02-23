#Information
 - Title: The Faith of [Root.Monarch.GetName]
 - ID: culture_religion_events.3
#Description
The Faith of [Root.Monarch.GetName]
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Wonderful!

###AI weighting:
AI weights this option at 10


###Efects:<ul><li>add ruler modifier:</li><ul><li>name = "increased_tolerance_of_heretics"</li></ul><li>event target:conversion province:</li><ul><li>change religion = variable:From:new_ruler_religion</li><li>add province modifier:</li><ul><li>name = "religious_zeal_at_conv"</li><li>duration = 7300</li></ul></ul></ul>

___
##We must attempt to stem the subversive powers of the [Root.Monarch.GetTitle].

###AI weighting:
AI weights this option at 90


###Efects:<ul><li>add ruler modifier:</li><ul><li>name = "supressing_personal_faith"</li></ul><li>event target:conversion province:</li><ul><li>add province modifier:</li><ul><li>name = "supressed_religious_minority"</li><li>duration = 7300</li></ul></ul></ul>
