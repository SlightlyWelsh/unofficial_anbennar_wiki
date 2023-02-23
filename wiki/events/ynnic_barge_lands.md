#Information
 - Title: Ynnic Barge Lands
 - ID: ynn_barges.11
#Description
Ynnic Barge Lands
#Options

___
##A tribute from the heavens! Seize it and bury the body

###Available if:
<li>event target:venaine owner:</li><ul><li>Country is Inek</li></ul>

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>If has event target:venaine owner has capital scope has discovered is FROM:</li><ul><li>random:</li><ul><li>chance = 50</li><li>FROM:</li><ul><li>add trust:</li><ul><li>who = event_target:venaine_owner</li><li>value = -20</li></ul><li>add opinion:</li><ul><li>who = event_target:venaine_owner</li><li>modifier = ynn_barge_looted</li></ul></ul></ul></ul><li>If has FROM has monthly income is 15:</li><ul><li>If has FROM has country flag is [big_barges](../flags/big_barges.md):</li><ul><li>event target:venaine owner:</li><ul><li>add treasury = 150</li></ul></ul><li>Else if has FROM has country flag is [normal_barges](../flags/normal_barges.md):</li><ul><li>event target:venaine owner:</li><ul><li>add treasury = 75</li></ul></ul><li>else:</li><ul><li>event target:venaine owner:</li><ul><li>add treasury = 27</li></ul></ul></ul><li>Else if has FROM has monthly income is 10:</li><ul><li>If has FROM has country flag is [big_barges](../flags/big_barges.md):</li><ul><li>event target:venaine owner:</li><ul><li>add treasury = 100</li></ul></ul><li>Else if has FROM has country flag is [normal_barges](../flags/normal_barges.md):</li><ul><li>event target:venaine owner:</li><ul><li>add treasury = 50</li></ul></ul><li>else:</li><ul><li>event target:venaine owner:</li><ul><li>add treasury = 18</li></ul></ul></ul><li>Else if has FROM has monthly income is 7.5:</li><ul><li>If has FROM has country flag is [big_barges](../flags/big_barges.md):</li><ul><li>event target:venaine owner:</li><ul><li>add treasury = 70</li></ul></ul><li>Else if has FROM has country flag is [normal_barges](../flags/normal_barges.md):</li><ul><li>event target:venaine owner:</li><ul><li>add treasury = 35</li></ul></ul><li>else:</li><ul><li>event target:venaine owner:</li><ul><li>add treasury = 13.5</li></ul></ul></ul><li>Else if has FROM has monthly income is 5:</li><ul><li>If has FROM has country flag is [big_barges](../flags/big_barges.md):</li><ul><li>event target:venaine owner:</li><ul><li>add treasury = 50</li></ul></ul><li>Else if has FROM has country flag is [normal_barges](../flags/normal_barges.md):</li><ul><li>event target:venaine owner:</li><ul><li>add treasury = 25</li></ul></ul><li>else:</li><ul><li>event target:venaine owner:</li><ul><li>add treasury = 9</li></ul></ul></ul><li>Else if has FROM has monthly income is 2.5:</li><ul><li>If has FROM has country flag is [big_barges](../flags/big_barges.md):</li><ul><li>event target:venaine owner:</li><ul><li>add treasury = 24</li></ul></ul><li>Else if has FROM has country flag is [normal_barges](../flags/normal_barges.md):</li><ul><li>event target:venaine owner:</li><ul><li>add treasury = 12</li></ul></ul><li>else:</li><ul><li>event target:venaine owner:</li><ul><li>add treasury = 4.5</li></ul></ul></ul><li>else:</li><ul><li>If has FROM has country flag is [big_barges](../flags/big_barges.md):</li><ul><li>event target:venaine owner:</li><ul><li>add treasury = 10</li></ul></ul><li>Else if has FROM has country flag is [normal_barges](../flags/normal_barges.md):</li><ul><li>event target:venaine owner:</li><ul><li>add treasury = 5</li></ul></ul><li>else:</li><ul><li>event target:venaine owner:</li><ul><li>add treasury = 1.8</li></ul></ul></ul></ul>

___
##Loot the contents of the vessel

###Available if:
<li>None of the following:</li><ul><li>event target:venaine owner:</li><ul><li>Country is Inek</li></ul></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.5 if does not have FROM has monthly income is 2.5
 - Multiplied by 0.5 if has FROM has country flag is [little_barges](../flags/little_barges.md)
 - Multiplied by 5 if has event target:venaine owner is rival is FROM
 - Multiplied by 2 if has event target:venaine owner has num of loans is 2
 - Multiplied by 4 if has event target:venaine owner is bankrupt
 - Multiplied by 10 if has event target:venaine owner has ruler has personality is greedy personality
 - Multiplied by 10 if has event target:venaine owner has ruler has personality is malevolent personality


###Efects:<ul><li>random:</li><ul><li>chance = 50</li><li>FROM:</li><ul><li>add trust:</li><ul><li>who = event_target:venaine_owner</li><li>value = -20</li></ul><li>add opinion:</li><ul><li>who = event_target:venaine_owner</li><li>modifier = ynn_barge_looted</li></ul></ul></ul><li>If has FROM has monthly income is 15:</li><ul><li>If has FROM has country flag is [big_barges](../flags/big_barges.md):</li><ul><li>event target:venaine owner:</li><ul><li>add treasury = 150</li></ul></ul><li>Else if has FROM has country flag is [normal_barges](../flags/normal_barges.md):</li><ul><li>event target:venaine owner:</li><ul><li>add treasury = 75</li></ul></ul><li>else:</li><ul><li>event target:venaine owner:</li><ul><li>add treasury = 27</li></ul></ul></ul><li>Else if has FROM has monthly income is 10:</li><ul><li>If has FROM has country flag is [big_barges](../flags/big_barges.md):</li><ul><li>event target:venaine owner:</li><ul><li>add treasury = 100</li></ul></ul><li>Else if has FROM has country flag is [normal_barges](../flags/normal_barges.md):</li><ul><li>event target:venaine owner:</li><ul><li>add treasury = 50</li></ul></ul><li>else:</li><ul><li>event target:venaine owner:</li><ul><li>add treasury = 18</li></ul></ul></ul><li>Else if has FROM has monthly income is 7.5:</li><ul><li>If has FROM has country flag is [big_barges](../flags/big_barges.md):</li><ul><li>event target:venaine owner:</li><ul><li>add treasury = 70</li></ul></ul><li>Else if has FROM has country flag is [normal_barges](../flags/normal_barges.md):</li><ul><li>event target:venaine owner:</li><ul><li>add treasury = 35</li></ul></ul><li>else:</li><ul><li>event target:venaine owner:</li><ul><li>add treasury = 13.5</li></ul></ul></ul><li>Else if has FROM has monthly income is 5:</li><ul><li>If has FROM has country flag is [big_barges](../flags/big_barges.md):</li><ul><li>event target:venaine owner:</li><ul><li>add treasury = 50</li></ul></ul><li>Else if has FROM has country flag is [normal_barges](../flags/normal_barges.md):</li><ul><li>event target:venaine owner:</li><ul><li>add treasury = 25</li></ul></ul><li>else:</li><ul><li>event target:venaine owner:</li><ul><li>add treasury = 9</li></ul></ul></ul><li>Else if has FROM has monthly income is 2.5:</li><ul><li>If has FROM has country flag is [big_barges](../flags/big_barges.md):</li><ul><li>event target:venaine owner:</li><ul><li>add treasury = 24</li></ul></ul><li>Else if has FROM has country flag is [normal_barges](../flags/normal_barges.md):</li><ul><li>event target:venaine owner:</li><ul><li>add treasury = 12</li></ul></ul><li>else:</li><ul><li>event target:venaine owner:</li><ul><li>add treasury = 4.5</li></ul></ul></ul><li>else:</li><ul><li>If has FROM has country flag is [big_barges](../flags/big_barges.md):</li><ul><li>event target:venaine owner:</li><ul><li>add treasury = 10</li></ul></ul><li>Else if has FROM has country flag is [normal_barges](../flags/normal_barges.md):</li><ul><li>event target:venaine owner:</li><ul><li>add treasury = 5</li></ul></ul><li>else:</li><ul><li>event target:venaine owner:</li><ul><li>add treasury = 1.8</li></ul></ul></ul></ul>

___
##Bury these valuables along with the coffin

###Available if:
<li>None of the following:</li><ul><li>event target:venaine owner:</li><ul><li>Country is Inek</li></ul></ul>

###AI weighting:
AI weights this option at 10
 - Multiplied by 2 if has event target:venaine owner has opinion has who is FROM, and has opinion has value is 50
 - Multiplied by 2 if has event target:venaine owner has opinion has who is FROM, and has opinion has value is 100
 - Multiplied by 2 if has event target:venaine owner has opinion has who is FROM, and has opinion has value is 150
 - Multiplied by 10 if has event target:venaine owner has ruler has personality is pious personality
 - Multiplied by 10 if has event target:venaine owner has ruler has personality is righteous personality


###Efects:<ul><li>FROM:</li><ul><li>add trust:</li><ul><li>who = event_target:venaine_owner</li><li>value = 5</li><li>mutual = yes</li></ul></ul></ul>
