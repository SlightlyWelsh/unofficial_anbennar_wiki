#Information
 - Title: Submit to Cyranvar
 - ID: cyranvar.4
#Description
Submit to Cyranvar
#Options

___
##Accept

###AI weighting:
AI weights this option at 50
 - Multiplied by 1.2 if has opinion has who is FROM, and has opinion has value is 120
 - Multiplied by 1.2 if has opinion has who is FROM, and has opinion has value is 150
 - Multiplied by 1.2 if has opinion has who is FROM, and has opinion has value is 180
 - Multiplied by 1.2 if has opinion has who is FROM, and has opinion has value is 200
 - Multiplied by 1.5 if has FROM has alliance with is ROOT
 - Multiplied by 1.2 if has FROM has marriage with is ROOT
 - Multiplied by 1.1 if has guaranteed by is FROM


###Efects:<ul><li>FROM:</li><ul><li>the event [[From.GetName] submitted!](../events/from_getname_submitted.md) happens</li></ul></ul>

___
##Never!

###AI weighting:
AI weights this option at 50
 - Multiplied by 1.2 if does not have opinion has who is FROM, and has opinion has value is 100
 - Multiplied by 1.5 if does not have opinion has who is FROM, and has opinion has value is 50
 - Multiplied by 1.8 if does not have opinion has who is FROM, and has opinion has value is 0
 - Multiplied by 2.5 if does not have opinion has who is FROM, and has opinion has value is -50
 - Multiplied by 1000 if is rival is FROM


###Efects:<ul><li>FROM:</li><ul><li>the event [[From.GetName] refused our offer!](../events/from_getname_refused_our_offer.md) happens</li></ul></ul>
