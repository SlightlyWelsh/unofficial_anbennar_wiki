#Information
 - Title: Religious Fanatics
 - ID: flavor_grombar.102
#Description
Religious Fanatics
#Mean Time to Happen:
Base time = 120 months
 - Multiplied by 1.25 if has province flag is [religious_fanatics](../flags/religious_fanatics.md)
 - Multiplied by 2.0 if does not have any neighbor province has owned by is Z50, and any neighbor province has owner religion
 - Multiplied by 0.95 if has any neighbor province has owned by is Z50, and any neighbor province has owner religion
 - Multiplied by 0.95 if has unrest is 3
 - Multiplied by 0.95 if has unrest is 5
 - Multiplied by 0.95 if has unrest is 7
 - Multiplied by 0.95 if has unrest is 9
 - Multiplied by 0.95 if has unrest is 11
 - Multiplied by 0.95 if does not have stability is 0
 - Multiplied by 0.95 if does not have stability is -1
 - Multiplied by 0.95 if does not have stability is -2

#Options

___
##The ends justify the means.

###AI weighting:
AI weights this option at 100
 - Multiplied by 0 if has owner has religion is ROOT


###Efects:<ul><li>add devastation = 25</li><li>add province modifier:</li><ul><li>name = "grombar_religious_violence"</li><li>duration = 7300</li></ul></ul>

___
##Regardless of faith, they are our people.

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>spawn rebels:</li><ul><li>type = religious_rebels</li><li>size = 3</li></ul></ul>
