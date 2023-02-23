#Information
 - Title: $ESTATE_ADVENTURERS$ Refuse to Hand Artifact to $ESTATE_ARTIFICERS$
 - ID: adventurers_estate_events.7
#Description
$ESTATE_ADVENTURERS$ Refuse to Hand Artifact to $ESTATE_ARTIFICERS$
#Mean Time to Happen:
Base time = 1 days

#Options

___
##It belongs in a museum!

###AI weighting:
AI weights this option at 50
 - Multiplied by 1.5 if does not have estate loyalty has estate is estate adventurers, and estate loyalty has loyalty is 60


###Efects:<ul><li>add estate loyalty:</li><ul><li>estate = estate_adventurers</li><li>loyalty = 10</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_artificers</li><li>loyalty = -15</li></ul></ul>

___
##Take the artifact by force.

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.5 if does not have estate loyalty has estate is estate adventurers, and estate loyalty has loyalty is 40
 - Multiplied by 1.5 if does not have estate influence has estate is estate artificers, and estate influence has influence is 30


###Efects:<ul><li>add mil power = -25</li><li>add estate loyalty:</li><ul><li>estate = estate_adventurers</li><li>loyalty = -15</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_artificers</li><li>loyalty = 10</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_artificers</li><li>desc = EST_VAL_EXPLOITING_ARTIFACTS</li><li>influence = 10</li><li>duration = 5475</li></ul></ul>
