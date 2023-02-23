#Information
 - Title: Relics Dwindling
 - ID: precursor_relics.2
#Description
Relics Dwindling
#Mean Time to Happen:
Base time = 30 years
 - Multiplied by 2 if has REB has check variable has which is num precursor relics, and check variable has value is 40; and does not have province flag is [small_temple_relics](../flags/small_temple_relics.md)
 - Multiplied by 1.5 if does not have check variable has which is num precursor relics, and check variable has value is 20; and REB has check variable has which is num precursor relics, and check variable has value is 10; and does not have province flag is [small_temple_relics](../flags/small_temple_relics.md)
 - Multiplied by 2 if does not have check variable has which is num precursor relics, and check variable has value is 10; and does not have province flag is [small_temple_relics](../flags/small_temple_relics.md)
 - Multiplied by 0.25 if has province flag is [small_temple_relics](../flags/small_temple_relics.md)
 - Multiplied by 3 if has province modifier is eordan expedition site

#Options

___
##Make hay while the sun shines.

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>add permanent province modifier:</li><ul><li>name = dwindling_resources</li><li>duration = -1</li></ul><li>hidden effect:</li><ul><li>fire province event [precursor_relics.3](precursor_relics.3_slug) in 1825 to 3650 days</li></ul></ul>
