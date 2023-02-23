#Information
 - Title: An Invitation to the Court of Blood
 - ID: corvuria.4
#Description
An Invitation to the Court of Blood
#Options

___
##We gladly accept.

###AI weighting:
AI weights this option at 100
 - Multiplied by 4 if has alliance with is FROM
 - Multiplied by 0.25 if is rival is FROM
 - Multiplied by 0.10 if has war with is FROM
 - Multiplied by 0.75 if does not have opinion has who is FROM, and has opinion has value is 0
 - Multiplied by 0.75 if does not have opinion has who is FROM, and has opinion has value is -50
 - Multiplied by 0.50 if does not have opinion has who is FROM, and has opinion has value is -100
 - Multiplied by 1.25 if has opinion has who is FROM, and has opinion has value is 0
 - Multiplied by 1.5 if has opinion has who is FROM, and has opinion has value is 50
 - Multiplied by 1.5 if has opinion has who is FROM, and has opinion has value is 100
 - Multiplied by 1.5 if has opinion has who is FROM, and has opinion has value is 150
 - Multiplied by 0.1 if has estate privilege is estate vampires organization vampiric emigres
 - Multiplied by 2 if has estate privilege is estate vampires organization bloody aristocracy
 - Multiplied by 0.8 if has estate privilege is estate vampires organization vampires lord
 - Multiplied by 2 if has estate privilege is estate vampires law traditional masquerade
 - Multiplied by 5 if has estate privilege is estate vampires law state collusion masquerade
 - Multiplied by 0.25 if has estate privilege is estate vampires law open rule


###Efects:<ul><li>If has estate privilege is estate vampires law open rule:</li><ul><li>remove estate privilege = estate_vampires_law_open_rule</li><li>set estate privilege = estate_vampires_law_traditional_masquerade</li></ul><li>set estate privilege = estate_vampires_organization_the_blood_court</li><li>event target:blood court founder:</li><ul><li>the event [A New Member](../events/a_new_member.md) happens</li></ul></ul>

___
##We will decline.

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>add prestige = 5</li><li>event target:blood court founder:</li><ul><li>the event [Failure](../events/failure.md) happens</li></ul></ul>
