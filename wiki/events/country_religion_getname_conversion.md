#Information
 - Title: [country.Religion.GetName] Conversion
 - ID: monstrous.22
#Description
[country.Religion.GetName] Conversion
#Mean Time to Happen:
Base time = 1 days

#Options

___
##I convert!

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>decrease monstrous 10 = yes</li><li>change government reform progress = 25</li><li>add stability = -2</li><li>change religion = event_target:country</li><li>capital scope:</li><ul><li>If area has owned by is ROOT:</li><ul><li>change religion = event_target:country</li></ul></ul><li>set ruler religion = event_target:country</li><li>If has heir:</li><ul><li>set heir religion = event_target:country</li></ul><li>If has consort:</li><ul><li>set consort religion = event_target:country</li></ul><li>hidden effect:</li><ul><li>set country flag [monstrous_converted_religion](../flags/monstrous_converted_religion.md)</li></ul></ul>

___
##We stick to the old ways.

###AI weighting:
AI weights this option at 100
 - Multiplied by 0 if has want to decrease monstrous is yes


###Efects:<ul><li>increase monstrous 1 = yes</li><li>change government reform progress = -10</li></ul>
