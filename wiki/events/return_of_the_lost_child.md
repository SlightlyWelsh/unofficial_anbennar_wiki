#Information
 - Title: Return of the Lost Child
 - ID: fey_alignment.13
#Description
Return of the Lost Child
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Welcome back! Of course I know who you are!

###Efects:<ul><li>set heir = fey_alignment_abductedheir</li><li>add legitimacy = -20</li><li>add devotion = -10</li><li>add republican tradition = -5</li><li>add prestige = -20</li><li>add piety = 0.1</li></ul>

___
##I will never let some runaway cur take my nation!

###One of the following randomly happens:
Outcome 1:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>increase heir adm effect = yes</li></ul>
Outcome 2:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>increase heir dip effect = yes</li></ul>
Outcome 3:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>increase heir mil effect = yes</li></ul>

###Efects:<ul><li>If random owned province has province flag is [fey_returned_heir](../flags/fey_returned_heir.md):</li><ul><li>spawn rebels:</li><ul><li>type = pretender_rebels</li><li>size = 3</li><li>leader = fey_alignment_heirpretender</li></ul></ul><li>add piety = -0.1</li></ul>
