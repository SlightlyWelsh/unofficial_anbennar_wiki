#Information
 - Title: Elections in Marlliande
 - ID: marlliande.1
#Description
Elections in Marlliande
#Options

___
##The current $MONARCHTITLE$ has served us well.

###Available if:
<li>does not have regency</li><li>None of the following:</li><ul><li>has ruler flag [leader_has_been_pushed_out](../flags/leader_has_been_pushed_out.md)</li></ul>

###AI weighting:
AI weights this option at 60
 - Multiplied by 0 if does not have republican tradition is 25
 - Multiplied by 0.5 if does not have republican tradition is 50
 - Multiplied by 0.5 if does not have republican tradition is 75
 - Multiplied by 2.0 if has republican tradition is 90
 - Multiplied by 2.0 if has ruler has mage personality is yes


###One of the following randomly happens:
Outcome 1:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>change adm = 1</li></ul>
Outcome 2:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>change dip = 1</li></ul>
Outcome 3:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>change mil = 1</li></ul>

###Efects:<ul><li>custom tooltip = remains_ruler</li><li>If has country flag is [vilaechi_lord](../flags/vilaechi_lord.md):</li><ul><li>add faction influence:</li><ul><li>faction = vilaechi</li><li>influence = 10</li></ul></ul><li>Else if has country flag is [rosrholych_lord](../flags/rosrholych_lord.md):</li><ul><li>add faction influence:</li><ul><li>faction = rosrholych</li><li>influence = 10</li></ul></ul><li>Else if has country flag is [drominar_lord](../flags/drominar_lord.md):</li><ul><li>add faction influence:</li><ul><li>faction = drominar</li><li>influence = 10</li></ul></ul><li>add scaled republican tradition = -10</li><li>hidden effect:</li><ul><li>clr country flag [in_marlliande_election](../flags/in_marlliande_election.md)</li></ul></ul>

___
##The Vilaéchi noble.

###Available if:
<li>does not have regency</li><li>None of the following:</li><ul><li>has country flag [vilaechi_lord](../flags/vilaechi_lord.md)</li></ul>

###AI weighting:
AI weights this option at 60


###Efects:<ul><li>define ruler:</li><ul><li>change adm = 2</li><li>change dip = 0</li><li>change mil = 0</li><li>max random adm = 4</li><li>max random dip = 4</li><li>max random mil = 4</li><li>random gender = yes</li></ul><li>add faction influence:</li><ul><li>faction = vilaechi</li><li>influence = 25</li></ul><li>add adm power = 50</li><li>hidden effect:</li><ul><li>clear ruler vampire flags = yes</li><li>set country flag [new_vampire](../flags/new_vampire.md)</li><li>ruler become vampire = yes</li><li>clr country flag [rosrholych_lord](../flags/rosrholych_lord.md)</li><li>clr country flag [drominar_lord](../flags/drominar_lord.md)</li><li>set country flag [vilaechi_lord](../flags/vilaechi_lord.md)</li><li>clr country flag [in_marlliande_election](../flags/in_marlliande_election.md)</li></ul></ul>

___
##The Rósrholych emissary.

###Available if:
<li>does not have regency</li><li>None of the following:</li><ul><li>has country flag [rosrholych_lord](../flags/rosrholych_lord.md)</li></ul>

###AI weighting:
AI weights this option at 60


###Efects:<ul><li>define ruler:</li><ul><li>change adm = 0</li><li>change dip = 2</li><li>change mil = 0</li><li>max random adm = 4</li><li>max random dip = 4</li><li>max random mil = 4</li><li>random gender = yes</li></ul><li>add faction influence:</li><ul><li>faction = rosrholych</li><li>influence = 25</li></ul><li>add dip power = 50</li><li>hidden effect:</li><ul><li>clear ruler vampire flags = yes</li><li>set country flag [new_vampire](../flags/new_vampire.md)</li><li>ruler become vampire = yes</li><li>clr country flag [vilaechi_lord](../flags/vilaechi_lord.md)</li><li>clr country flag [drominar_lord](../flags/drominar_lord.md)</li><li>set country flag [rosrholych_lord](../flags/rosrholych_lord.md)</li><li>clr country flag [in_marlliande_election](../flags/in_marlliande_election.md)</li></ul></ul>

___
##The Drominar pioneer.

###Available if:
<li>does not have regency</li><li>None of the following:</li><ul><li>has country flag [drominar_lord](../flags/drominar_lord.md)</li></ul>

###AI weighting:
AI weights this option at 60


###Efects:<ul><li>define ruler:</li><ul><li>change adm = 0</li><li>change dip = 0</li><li>change mil = 2</li><li>max random adm = 4</li><li>max random dip = 4</li><li>max random mil = 4</li><li>random gender = yes</li></ul><li>add faction influence:</li><ul><li>faction = drominar</li><li>influence = 25</li></ul><li>add mil power = 50</li><li>hidden effect:</li><ul><li>clear ruler vampire flags = yes</li><li>set country flag [new_vampire](../flags/new_vampire.md)</li><li>ruler become vampire = yes</li><li>clr country flag [vilaechi_lord](../flags/vilaechi_lord.md)</li><li>clr country flag [rosrholych_lord](../flags/rosrholych_lord.md)</li><li>set country flag [drominar_lord](../flags/drominar_lord.md)</li><li>clr country flag [in_marlliande_election](../flags/in_marlliande_election.md)</li></ul></ul>


#Pages with same name:
The following pages have the same name as this page:
 - [elections_in_marlliande_1](elections_in_marlliande_1.md)


#Pages with same name:
The following pages have the same name as this page:
 - [elections_in_marlliande_1](elections_in_marlliande_1.md)
