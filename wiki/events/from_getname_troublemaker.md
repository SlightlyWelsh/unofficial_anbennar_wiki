#Information
 - Title: [From.GetName] troublemaker!
 - ID: lake.51
#Description
[From.GetName] troublemaker!
#Options

___
##Conscript part of it, let the other join the Joglik Uts

###AI weighting:
AI weights this option at 100
 - Multiplied by 0 if is rival is FROM
 - Multiplied by 0 if has 5284 has unrest is 5
 - Multiplied by 10 if is at war


###Efects:<ul><li>If has FROM has country flag is [manpower_1](../flags/manpower_1.md):</li><ul><li>add manpower = 0.5</li></ul><li>Else if has FROM has country flag is [manpower_2](../flags/manpower_2.md):</li><ul><li>add manpower = 1</li><li>5284:</li><ul><li>add unrest = 1</li></ul></ul><li>Else if has FROM has country flag is [manpower_3](../flags/manpower_3.md):</li><ul><li>add manpower = 1.5</li><li>5284:</li><ul><li>add unrest = 1</li></ul></ul><li>Else if has FROM has country flag is [manpower_4](../flags/manpower_4.md):</li><ul><li>add manpower = 2</li><li>5284:</li><ul><li>add unrest = 2</li><li>area:</li><ul><li>add unrest = 1</li></ul></ul></ul></ul>

___
##Send them all to die in the forbidden plains

###AI weighting:
AI weights this option at 10
 - Multiplied by 10 if is at war
 - Multiplied by 5 if has war exhaustion is 8
 - Multiplied by 50 if does not have stability is 0

