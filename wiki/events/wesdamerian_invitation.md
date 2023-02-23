#Information
 - Title: Wesdamerian Invitation
 - ID: flavor_wesdam.5
#Description
Wesdamerian Invitation
#Options

___
##Accept the union.

###AI weighting:
AI weights this option at 100
 - Multiplied by 0 if has ROOT is an elector; and has ROOT is the emperor
 - Multiplied by 1.5 if has FROM is a great power
 - Multiplied by 5 if has dynasty is FROM
 - Multiplied by 3 if has regency
 - Multiplied by 3 if has FROM is lucky
 - Multiplied by 1.2 if has trust has who is FROM, and trust has value is 60
 - Multiplied by 1.2 if has trust has who is FROM, and trust has value is 70
 - Multiplied by 1.2 if has trust has who is FROM, and trust has value is 85


###Efects:<ul><li>hidden effect:</li><ul><li>FROM:</li><ul><li>set country flag [accepted_pu](../flags/accepted_pu.md)</li></ul></ul><li>FROM:</li><ul><li>the event [[Root.WesdamUnion]](../events/root_wesdamunion.md) happens</li></ul></ul>

___
##Reject the union.

###AI weighting:
AI weights this option at 100
 - Multiplied by 0.5 if has army strength has who is FROM, and army strength has value is 0.5
 - Multiplied by 1.5 if is a great power
 - Multiplied by 8 if has total development is FROM
 - Multiplied by 1.2 if does not have trust has who is FROM, and trust has value is 20
 - Multiplied by 1.2 if does not have trust has who is FROM, and trust has value is 40


###Efects:<ul><li>hidden effect:</li><ul><li>FROM:</li><ul><li>set country flag [refused_pu](../flags/refused_pu.md)</li></ul></ul><li>FROM:</li><ul><li>the event [[Root.WesdamUnion]](../events/root_wesdamunion.md) happens</li></ul></ul>
