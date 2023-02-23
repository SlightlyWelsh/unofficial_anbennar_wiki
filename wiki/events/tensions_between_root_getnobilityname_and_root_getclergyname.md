#Information
 - Title: Tensions between [Root.GetNobilityName] and [Root.GetClergyName]
 - ID: 874
#Description
Tensions between [Root.GetNobilityName] and [Root.GetClergyName]
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Jesus lived among beggars and fishermen, why don't you?

###AI weighting:
AI weights this option at 20
 - Multiplied by 2 if does not have num of cities is 5
 - Multiplied by 2 if does not have num of cities is 10
 - Multiplied by 2 if does not have num of cities is 15
 - Multiplied by 2 if does not have num of cities is 20
 - Multiplied by 0.25 if has estate is estate church, and does not have estate loyalty has estate is estate church, and estate loyalty has loyalty is 30


###Efects:<ul><li>event target:rebel province:</li><ul><li>spawn large scaled rebels:</li><ul><li>type = corinite_rebels</li><li>no defined leader = yes</li></ul></ul><li>reverse add opinion:</li><ul><li>who = PAP</li><li>modifier = opinion_upset_pope</li></ul><li>reduce estate church loyalty effect = yes</li><li>add estate nobles loyalty effect = yes</li></ul>

___
##Surely we do not wish to anger his holiness.

###AI weighting:
AI weights this option at 80
 - Multiplied by 0.25 if has estate is estate nobles, and does not have estate loyalty has estate is estate nobles, and estate loyalty has loyalty is 30


###Efects:<ul><li>event target:rebel province:</li><ul><li>spawn large scaled rebels:</li><ul><li>type = noble_rebels</li><li>no defined leader = yes</li></ul></ul><li>reduce estate nobles loyalty effect = yes</li><li>add estate church loyalty effect = yes</li></ul>
