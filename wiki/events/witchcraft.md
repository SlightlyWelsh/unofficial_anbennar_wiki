#Information
 - Title: Witchcraft
 - ID: aow_events.16
#Description
Witchcraft
#Mean Time to Happen:
Base time = 480 months
 - Multiplied by 0.75 if has owner has government is theocracy
 - Multiplied by 0.75 if has current age is age of discovery, and has current age is age of reformation
 - Multiplied by 2 if has current age is age of revolutions

#Options

___
##Allow them to proceed with the local trials.

###Efects:<ul><li>add province modifier:</li><ul><li>name = "local_witch_hunts"</li><li>duration = 3650</li></ul><li>hidden effect:</li><ul><li>fire province event [aow_events.17](aow_events.17_slug) in 1080 to 4800 days</li><li>fire province event [aow_events.18](aow_events.18_slug) in 1080 to 4800 days</li></ul></ul>

___
##$INQUISITOR$ can see to these matters in a more organized fashion.

###Available if:
<li>owner:</li><ul><li>Have an advisor of type inquisitor</li></ul>

###Efects:<ul><li>owner:</li><ul><li>country gets the modifier "nationwide_witch_hunts" for 10 years</li></ul></ul>

___
##Such foolish superstitions have no place in [Root.Owner.GetName]!

###Efects:<ul><li>owner:</li><ul><li>country gets the modifier "forbade_witch_hunts" for 10 years</li></ul></ul>
