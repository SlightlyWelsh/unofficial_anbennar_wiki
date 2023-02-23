#Information
 - Title: The Dead Seek Passage
 - ID: ynn_barges.2
#Description
The Dead Seek Passage
#Options

___
##Let them pass

###Available if:
<li>None of the following:</li><ul><li>owned by is FROM</li></ul>

###AI weighting:
AI weights this option at 100
 - Multiplied by 2 if has owner has religion is ynn river worship; and has owner has religion is ynn river reformed
 - Multiplied by 2 if has owner has opinion has who is FROM, and has opinion has value is 50
 - Multiplied by 2 if has owner has opinion has who is FROM, and has opinion has value is 100
 - Multiplied by 2 if has owner has opinion has who is FROM, and has opinion has value is 150


###Efects:<ul><li>FROM:</li><ul><li>add prestige = 1</li></ul><li>owner:</li><ul><li>add prestige = 1</li><li>add trust:</li><ul><li>who = FROM</li><li>value = 5</li><li>mutual = yes</li></ul></ul><li>hidden effect:</li><ul><li>FROM:</li><ul><li>the event [Missing localisation: ynn_barges_100_t](../events/missing_localisation_ynn_barges_100_t.md) happens</li></ul></ul></ul>

___
##Charge the toll

###Available if:
<li>None of the following:</li><ul><li>owned by is FROM</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 2 if does not have owner has opinion has who is FROM, and has opinion has value is 50
 - Multiplied by 2 if does not have owner has opinion has who is FROM, and has opinion has value is 0
 - Multiplied by 2 if does not have owner has opinion has who is FROM, and has opinion has value is -50
 - Multiplied by 5 if has owner is rival is FROM
 - Multiplied by 2 if has owner has num of loans is 2
 - Multiplied by 4 if has owner is bankrupt
 - Multiplied by 4 if has owner has ruler has personality is greedy personality
 - Multiplied by 5 if does not have owner has religion is ynn river worship; and does not have owner has religion is ynn river reformed


###Efects:<ul><li>owner:</li><ul><li>add trust:</li><ul><li>who = FROM</li><li>value = -2</li><li>mutual = yes</li></ul></ul><li>FROM:</li><ul><li>the event [[From.Owner.GetName] Demands a Toll](../events/from_owner_getname_demands_a_toll.md) happens</li></ul></ul>

___
##Turn them back

###Available if:
<li>None of the following:</li><ul><li>owned by is FROM</li></ul><li>NOT:</li><ul><li>controlled by is FROM</li></ul>

###AI weighting:
AI weights this option at 10
 - Multiplied by 100 if has owner has ruler has personality is malevolent personality
 - Multiplied by 5 if does not have owner has opinion has who is FROM, and has opinion has value is -50
 - Multiplied by 5 if has owner is rival is FROM


###Efects:<ul><li>owner:</li><ul><li>add trust:</li><ul><li>who = FROM</li><li>value = -7</li><li>mutual = yes</li></ul></ul><li>FROM:</li><ul><li>the event [[From.Owner.GetName] Prevents Passage](../events/from_owner_getname_prevents_passage.md) happens</li></ul></ul>

___
##Let our monarch through

###Available if:
<li>owned by is FROM</li>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>owner:</li><ul><li>add adm power = 10</li><li>add mil power = 10</li><li>add dip power = 10</li></ul><li>hidden effect:</li><ul><li>FROM:</li><ul><li>the event [Missing localisation: ynn_barges_100_t](../events/missing_localisation_ynn_barges_100_t.md) happens</li></ul></ul></ul>
