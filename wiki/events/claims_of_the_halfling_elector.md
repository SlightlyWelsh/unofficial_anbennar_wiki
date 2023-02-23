#Information
 - Title: Claims of the Halfling Elector
 - ID: flavor_beepeck.2
#Description
Claims of the Halfling Elector
#Options

___
##Of course not. The land is de jure Exwes.

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>reverse add opinion:</li><ul><li>who = A12</li><li>modifier = refused_our_right_as_elector</li></ul><li>reverse add opinion:</li><ul><li>who = A40</li><li>modifier = forced_other_to_give_up_claim_on_us</li></ul><li>hidden effect:</li><ul><li>A12:</li><ul><li>set country flag [claims_rejected](../flags/claims_rejected.md)</li><li>the event [Result of the Petition](../events/result_of_the_petition.md) happens</li></ul></ul></ul>

___
##They do have a right to it. But we will not force Exwes on the issue

###AI weighting:
AI weights this option at 10


###Efects:<ul><li>157:</li><ul><li>add core = A12</li></ul><li>reverse add opinion:</li><ul><li>who = A12</li><li>modifier = accepted_claim_on_neighbor</li></ul><li>hidden effect:</li><ul><li>A12:</li><ul><li>set country flag [claims_acknowledged](../flags/claims_acknowledged.md)</li><li>the event [Result of the Petition](../events/result_of_the_petition.md) happens</li></ul></ul></ul>

___
##Their right is acknowledged. Exwes must give them the land.

###AI weighting:
AI weights this option at 1
 - Multiplied by 1.2 if has opinion has who is A12, and has opinion has value is 125
 - Multiplied by 1.2 if has opinion has who is A12, and has opinion has value is 150
 - Multiplied by 1.2 if has opinion has who is A12, and has opinion has value is 175
 - Multiplied by 1.2 if has opinion has who is A12, and has opinion has value is 199
 - Multiplied by 1.5 if has opinion modifier has who is A12, and has opinion modifier has modifier is sent gift
 - Multiplied by 2 if has alliance with is A12


###Efects:<ul><li>157:</li><ul><li>add core = A12</li><li>cede province = A12</li></ul><li>reverse add opinion:</li><ul><li>who = A12</li><li>modifier = enforced_our_right_as_elector</li></ul><li>reverse add opinion:</li><ul><li>who = A40</li><li>modifier = opinion_took_province</li></ul><li>hidden effect:</li><ul><li>A12:</li><ul><li>set country flag [claims_enforced](../flags/claims_enforced.md)</li><li>the event [Result of the Petition](../events/result_of_the_petition.md) happens</li></ul></ul></ul>
