#Information
 - Title: Encroachment of the $ESTATE_NOBLES$ in [noble_encroachment.GetName]
 - ID: nobles_estate_events.3
#Description
Encroachment of the $ESTATE_NOBLES$ in [noble_encroachment.GetName]
#Mean Time to Happen:
Base time = 1 days
 - Multiplied by 2.0 if has estate influence has estate is estate nobles, and estate influence has influence is 80; and does not have estate loyalty has estate is estate nobles, and estate loyalty has loyalty is 80

#Options

___
##Let it slide.

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.25 if has estate territory has estate is estate nobles, and estate territory has territory is 12
 - Multiplied by 0.25 if has estate influence has estate is estate nobles, and estate influence has influence is 60
 - Multiplied by 1.5 if does not have estate loyalty has estate is estate nobles, and estate loyalty has loyalty is 30


###Efects:<ul><li>event target:noble encroachment:</li><ul><li>add local autonomy = 25</li></ul><li>give estate land share small:</li><ul><li>estate = estate_nobles</li></ul></ul>

___
##Demand that the land be returned.

###AI weighting:
AI weights this option at 50
 - Multiplied by 1.1 if does not have estate territory has estate is estate nobles, and estate territory has territory is 15
 - Multiplied by 0.25 if does not have estate loyalty has estate is estate nobles, and estate loyalty has loyalty is 35


###Efects:<ul><li>event target:noble encroachment:</li><ul><li>random list:</li><ul><li>50:</li><ul><li>spawn rebels:</li><ul><li>type = noble_rebels</li><li>size = 1</li></ul></ul><li>50:</li><ul></ul></ul></ul><li>add estate loyalty:</li><ul><li>estate = estate_nobles</li><li>loyalty = -15</li></ul></ul>
