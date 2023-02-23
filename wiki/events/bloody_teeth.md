#Information
 - Title: Bloody Teeth
 - ID: flavour_wineport.2
#Description
Bloody Teeth
#Options

___
##End the Toll!

###Available if:
<li>None of the following:</li><ul><li>has country flag [kept_toll](../flags/kept_toll.md)</li></ul>

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>11:</li><ul><li>add province modifier:</li><ul><li>name = ended_teeth_toll</li><li>duration = -1</li></ul></ul></ul>

___
##Perhaps we should reconsider...

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>add treasury = 200</li><li>event target:wineport sponsor:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = renegaded_sponsorship</li><li>years = 50</li></ul></ul><li>set country flag [kept_toll](../flags/kept_toll.md)</li></ul>
