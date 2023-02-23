#Information
 - Title: The Beast Inside
 - ID: vampire_ruler.11
#Description
The Beast Inside
#Mean Time to Happen:
Base time = 1 days

#Options

___
##A beast I am, lest a beast I become

###Available if:
<li>dip is at least 1</li><li>None of the following:</li><ul><li>has country flag [vampire_missed_hunt](../flags/vampire_missed_hunt.md)</li></ul>

###AI weighting:
AI weights this option at 10


###Efects:<ul><li>the event ˻vampire_ruler.13˼ happens</li><li>change dip = -2</li><li>set country flag [vampire_missed_hunt](../flags/vampire_missed_hunt.md)</li></ul>

___
##I will control myself

###Available if:
<li>dip is at least 1</li><li>None of the following:</li><ul><li>has country flag [vampire_missed_hunt](../flags/vampire_missed_hunt.md)</li></ul>

###AI weighting:
AI weights this option at 10
 - Multiplied by 0 if does not have country flag is [exposed_vampire_ruler](../flags/exposed_vampire_ruler.md)


###One of the following randomly happens:
Outcome 1:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>change dip = -2</li></ul>
Outcome 2:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>add legitimacy = -10</li></ul>

###Efects:<ul><li>set country flag [vampire_missed_hunt](../flags/vampire_missed_hunt.md)</li></ul>

___
##I... Must... §RFEED§!

###AI weighting:
AI weights this option at 10
 - Multiplied by 0 if does not have country flag is [exposed_vampire_ruler](../flags/exposed_vampire_ruler.md)


###One of the following randomly happens:
Outcome 1:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>increase ruler adm effect = yes</li></ul>
Outcome 2:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>increase ruler dip effect = yes</li></ul>
Outcome 3:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>increase ruler mil effect = yes</li></ul>

###Efects:<ul><li>facade suspicion increase 10 = yes</li><li>random owned province:</li><ul><li>add devastation = 10</li><li>add province modifier:</li><ul><li>name = vampire_ruler_rampage</li><li>duration = 1850</li></ul></ul><li>clr country flag [vampire_missed_hunt](../flags/vampire_missed_hunt.md)</li></ul>
