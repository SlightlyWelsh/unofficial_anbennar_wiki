This page has the same name as others. For full listing see bottom of [the base page](privileges_revoked.md).

#Information
 - Title: Privileges Revoked
 - ID: 9074
#Description
Privileges Revoked
#Options

___
##Swear Oath of Loyalty

###AI weighting:
AI weights this option at 10
 - Multiplied by 0 if does not have opinion has who is emperor, and has opinion has value is 0


###Efects:<ul><li>emperor:</li><ul><li>vassalize = ROOT</li></ul></ul>

___
##He may take our lives, but he will never take our freedom.

###AI weighting:
AI weights this option at 10
 - Multiplied by 0 if has opinion has who is emperor, and has opinion has value is 0


###Efects:<ul><li>If every owned province is part of hre:</li><ul><li>add claim = emperor</li></ul><li>every owned province:</li><ul><li>set in empire = no</li></ul><li>emperor:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = opinion_left_empire</li></ul></ul><li>add opinion:</li><ul><li>who = emperor</li><li>modifier = opinion_united_empire</li></ul><li>elector = no</li></ul>
