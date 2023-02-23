#Information
 - Title: Secure the Coastline
 - ID: flavor_honsai.18
#Description
Secure the Coastline
#Options

___
##To Prukakhin!

###Available if:
<li>exists is Prukakhin</li>

###Efects:<ul><li>set country flag [pruhakin_chosen](../flags/pruhakin_chosen.md)</li><li>add casus belli:</li><ul><li>target = Y53</li><li>type = cb_vassalize_mission</li><li>months = 120</li></ul></ul>

___
##Pinghoi shall repay all that is due, and more.

###Available if:
<li>exists is Y64</li>

###Efects:<ul><li>set country flag [pinghoi_chosen](../flags/pinghoi_chosen.md)</li><li>add casus belli:</li><ul><li>target = Y64</li><li>type = cb_vassalize_mission</li><li>months = 120</li></ul></ul>

___
##Perhaps we should take a different path...

###Available if:
<li>None of the following:</li><ul><li>exists is Prukakhin</li></ul><li>NOT:</li><ul><li>exists is Y64</li></ul>

###Efects:<ul><li>If khindi area does not have core is ROOT; and does not have permanent claim is ROOT:</li><ul><li>add permanent claim = ROOT</li></ul><li>set country flag [pruhakin_chosen](../flags/pruhakin_chosen.md)</li></ul>
