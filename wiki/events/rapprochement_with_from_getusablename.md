#Information
 - Title: Rapprochement with [From.GetUsableName]?
 - ID: new_court_flavour_events.2
#Description
Rapprochement with [From.GetUsableName]?
#Options

___
##Better relations could indeed be of benefit to us.

###AI weighting:
AI weights this option at 1
 - Multiplied by 0.5 if does not have opinion has who is from, and has opinion has value is -50
 - Multiplied by 0.5 if does not have opinion has who is from, and has opinion has value is -25
 - Multiplied by 1.5 if has opinion has who is from, and has opinion has value is 20
 - Multiplied by 1.5 if has opinion has who is from, and has opinion has value is 35
 - Multiplied by 1.5 if has opinion has who is from, and has opinion has value is 50
 - Multiplied by 2 if does not have army strength has who is from, and army strength has value is 0.75
 - Multiplied by 2 if does not have army strength has who is from, and army strength has value is 0.5


###Efects:<ul><li>from:</li><ul><li>add opinion:</li><ul><li>who = root</li><li>modifier = opinion_court_events_accept</li></ul><li>hidden effect:</li><ul><li>the event [Rapprochement Successful](../events/rapprochement_successful.md) happens</li></ul></ul></ul>

___
##Better relations are not in our interest.

###AI weighting:
AI weights this option at 1
 - Multiplied by 1.5 if does not have opinion has who is from, and has opinion has value is -50
 - Multiplied by 1.5 if does not have opinion has who is from, and has opinion has value is -25
 - Multiplied by 0.75 if has opinion has who is from, and has opinion has value is 25
 - Multiplied by 0.75 if has opinion has who is from, and has opinion has value is 50


###Efects:<ul><li>from:</li><ul><li>add opinion:</li><ul><li>who = root</li><li>modifier = opinion_court_events_rebuke_1</li></ul><li>hidden effect:</li><ul><li>the event [Rapprochement Unsuccessful](../events/rapprochement_unsuccessful.md) happens</li></ul></ul></ul>

___
##Friendship? Get out of my sight!

###Available if:
<li>employed advisor:</li><ul><li>category is DIP</li></ul>

###AI weighting:
AI weights this option at 1
 - Multiplied by 2 if does not have opinion has who is from, and has opinion has value is -50
 - Multiplied by 2 if does not have opinion has who is from, and has opinion has value is -25
 - Multiplied by 0.5 if has opinion has who is from, and has opinion has value is 25
 - Multiplied by 0.5 if has opinion has who is from, and has opinion has value is 50
 - Multiplied by 0.5 if does not have army strength has who is from, and army strength has value is 0.9
 - Multiplied by 0.5 if does not have army strength has who is from, and army strength has value is 0.65
 - Multiplied by 0 if has religion is catholic, and  has from has tag is PAP


###Efects:<ul><li>add prestige = 15</li><li>remove advisor by category = DIP</li><li>from:</li><ul><li>add opinion:</li><ul><li>who = root</li><li>modifier = opinion_court_events_rebuke</li></ul><li>hidden effect:</li><ul><li>the event [Rapprochement Forcefully Rebuffed](../events/rapprochement_forcefully_rebuffed.md) happens</li></ul></ul></ul>
