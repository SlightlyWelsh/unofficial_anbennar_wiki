#Information
 - Title: The Regency's Abuses
 - ID: estate_regency_events.2
#Description
The Regency's Abuses
#Mean Time to Happen:
Base time = 1 days

#Options

___
##We will accept their demands. For now.

###AI weighting:
AI weights this option at 33
 - Multiplied by 2 if does not have estate led regency loyalty is 30
 - Multiplied by 0 if has AND has estate led regency has estate is estate burghers; and AND has num of estate privileges has estate is estate burghers, and num of estate privileges has value is 2; and has AND has estate led regency has estate is estate church; and AND has num of estate privileges has estate is estate church, and num of estate privileges has value is 2; and has AND has estate led regency has estate is estate nobles; and AND has num of estate privileges has estate is estate nobles, and num of estate privileges has value is 2


###Efects:<ul><li>set estate led regency privilege = random</li></ul>

___
##Perhaps we can bribe them and hope they forget the matter.

###AI weighting:
AI weights this option at 33
 - Multiplied by 0 if does not have treasury is 100; and has corruption is 20
 - Multiplied by 0.5 if has estate led regency loyalty is 70
 - Multiplied by 2 if has AND has estate led regency has estate is estate burghers; and AND has num of estate privileges has estate is estate burghers, and num of estate privileges has value is 2; and has AND has estate led regency has estate is estate church; and AND has num of estate privileges has estate is estate church, and num of estate privileges has value is 2; and has AND has estate led regency has estate is estate nobles; and AND has num of estate privileges has estate is estate nobles, and num of estate privileges has value is 2


###Efects:<ul><li>add treasury = -100</li><li>add corruption = 10</li></ul>

___
##They get nothing. They must serve the nation, not their interests.

###AI weighting:
AI weights this option at 34
 - Multiplied by 0 if does not have stability is 2
 - Multiplied by 0.5 if does not have estate led regency loyalty is 70
 - Multiplied by 2 if has AND has estate led regency has estate is estate burghers; and AND has num of estate privileges has estate is estate burghers, and num of estate privileges has value is 2; and has AND has estate led regency has estate is estate church; and AND has num of estate privileges has estate is estate church, and num of estate privileges has value is 2; and has AND has estate led regency has estate is estate nobles; and AND has num of estate privileges has estate is estate nobles, and num of estate privileges has value is 2


###Efects:<ul><li>add stability = -1</li><li>If has estate led regency has estate is estate burghers:</li><ul><li>add estate loyalty modifier:</li><ul><li>estate = estate_burghers</li><li>loyalty = -10</li><li>desc = REFUSED_PRIVILEGE</li><li>duration = 7300</li></ul></ul><li>Else if has estate led regency has estate is estate church:</li><ul><li>add estate loyalty modifier:</li><ul><li>estate = estate_church</li><li>loyalty = -10</li><li>desc = REFUSED_PRIVILEGE</li><li>duration = 7300</li></ul></ul><li>Else if has estate led regency has estate is estate nobles:</li><ul><li>add estate loyalty modifier:</li><ul><li>estate = estate_nobles</li><li>loyalty = -10</li><li>desc = REFUSED_PRIVILEGE</li><li>duration = 7300</li></ul></ul></ul>
