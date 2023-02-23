#Information
 - Title: $ESTATE_NOBLES$ demand Stricter Sumptuary Laws
 - ID: nobles_estate_events.6
#Description
$ESTATE_NOBLES$ demand Stricter Sumptuary Laws
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Bend to the wishes of the $ESTATE_NOBLES$.

###AI weighting:
AI weights this option at 25
 - Multiplied by 2.0 if does not have estate loyalty has estate is estate nobles, and estate loyalty has loyalty is 35
 - Multiplied by 0.5 if has estate loyalty has estate is estate nobles, and estate loyalty has loyalty is 45


###Efects:<ul><li>country gets the modifier "nobility_sumptuary_restrictions" for 15 years</li><li>add estate influence modifier:</li><ul><li>estate = estate_nobles</li><li>desc = EST_VAL_NOBILITY_SUMPTUARY_RESTRICTIONS</li><li>influence = 10</li><li>duration = 5475</li></ul><li>If has estate is estate burghers:</li><ul><li>add estate influence modifier:</li><ul><li>estate = estate_burghers</li><li>desc = EST_VAL_BURGHERS_SUMPTUARY_RESTRICTIONS</li><li>influence = -10</li><li>duration = 5475</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_burghers</li><li>loyalty = -20</li></ul></ul><li>If has estate is estate vaisyas:</li><ul><li>add estate influence modifier:</li><ul><li>estate = estate_vaisyas</li><li>desc = EST_VAL_BURGHERS_SUMPTUARY_RESTRICTIONS</li><li>influence = -10</li><li>duration = 5475</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_vaisyas</li><li>loyalty = -20</li></ul></ul></ul>

___
##Refuse to obey the $ESTATE_NOBLES$.

###AI weighting:
AI weights this option at 75
 - Multiplied by 0.3 if does not have estate loyalty has estate is estate nobles, and estate loyalty has loyalty is 35
 - Multiplied by 1.25 if has estate loyalty has estate is estate nobles, and estate loyalty has loyalty is 45


###Efects:<ul><li>add estate loyalty:</li><ul><li>estate = estate_nobles</li><li>loyalty = -20</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_nobles</li><li>desc = EST_VAL_BURGHERS_NO_SUMPTUARY_RESTRICTIONS</li><li>influence = -10</li><li>duration = 5475</li></ul><li>If has estate is estate burghers:</li><ul><li>add estate influence modifier:</li><ul><li>estate = estate_burghers</li><li>desc = EST_VAL_NOBILITY_NO_SUMPTUARY_RESTRICTIONS</li><li>influence = 10</li><li>duration = 5475</li></ul></ul><li>If has estate is estate vaisyas:</li><ul><li>add estate influence modifier:</li><ul><li>estate = estate_vaisyas</li><li>desc = EST_VAL_NOBILITY_NO_SUMPTUARY_RESTRICTIONS</li><li>influence = 10</li><li>duration = 5475</li></ul></ul></ul>
