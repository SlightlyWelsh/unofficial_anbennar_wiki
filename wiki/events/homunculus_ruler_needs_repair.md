#Information
 - Title: Homunculus Ruler Needs Repair
 - ID: magic_project_homunculus.13
#Description
Homunculus Ruler Needs Repair
#Mean Time to Happen:
Base time = 240 months
 - Multiplied by 0.9 if has ruler age is 70
 - Multiplied by 0.9 if has ruler age is 80
 - Multiplied by 0.9 if has ruler age is 90
 - Multiplied by 0.9 if has ruler age is 100
 - Multiplied by 0.9 if has ruler age is 120
 - Multiplied by 0.9 if has ruler age is 140
 - Multiplied by 0.9 if has ruler age is 160
 - Multiplied by 0.9 if has ruler age is 180
 - Multiplied by 0.9 if has ruler age is 200
 - Multiplied by 0.5 if has ruler age is 250
 - Multiplied by 0.5 if has ruler age is 300

#Options

___
##Repair myself

###Available if:
<li>always</li>

###AI weighting:
AI weights this option at 50
 - Multiplied by 2 if has years of income is 1.0
 - Multiplied by 0.5 if does not have years of income is 0.5


###Efects:<ul><li>add years of income = -0.5</li><li>add adm power = -20</li><li>add dip power = -20</li><li>add mil power = -20</li></ul>

___
##Risk deterioration

###Available if:
<li>adm is at least 1</li><li>dip is at least 1</li><li>mil is at least 1</li>

###AI weighting:
AI weights this option at 50


###One of the following randomly happens:
Outcome 1:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>decrease ruler adm effect = yes</li></ul>
Outcome 2:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>decrease ruler dip effect = yes</li></ul>
Outcome 3:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>decrease ruler mil effect = yes</li></ul>

___
##Die

###Available if:
<li>None of the following:</li><ul><li>All of the following:</li><ul><li>adm is at least 1</li><li>dip is at least 1</li><li>mil is at least 1</li></ul></ul>

###AI weighting:
AI weights this option at 5


###Efects:<ul><li>kill ruler = yes</li></ul>
