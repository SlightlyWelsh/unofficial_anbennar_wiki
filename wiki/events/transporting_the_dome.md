#Information
 - Title: Transporting the Dome
 - ID: reveria.23
#Description
Transporting the Dome
#Options

___
##[Root.GetRulerTitleAndNameOrRegencyCap]: "I will go there and move it myself

###Available if:
<li>ruler has mage personality is yes</li><li>Any of the following:</li><ul><li>has ruler flag [conjuration_2](../flags/conjuration_2.md)</li><li>has ruler flag  conjuration_3</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>the event [Selling the dome?](../events/selling_the_dome.md) happens</li><li>add prestige = 20</li></ul>

___
##Our artificers are both capable and willing to move it, let them handle it.

###Available if:
<li>has estate estate_artificers</li><li>estate loyalty:</li><ul><li>estate is estate_artificers</li><li>loyalty is at least 40</li></ul><li>estate influence:</li><ul><li>estate is estate_artificers</li><li>influence is at least 50</li></ul>

###AI weighting:
AI weights this option at 99


###Efects:<ul><li>add treasury = -150</li><li>the event [Selling the dome?](../events/selling_the_dome.md) happens</li></ul>

___
##We own can send it downstream on the Ynn and tow it from Ynnsmouth to [Root.Capital.GetName] by ship.

###Available if:
<li>owns or non sovereign subject of 1028</li><li>owns or non sovereign subject of  1873</li><li>owns or non sovereign subject of   1031</li><li>owns or non sovereign subject of    1133</li>

###AI weighting:
AI weights this option at 99


###Efects:<ul><li>add treasury = -50</li><li>the event [Selling the dome?](../events/selling_the_dome.md) happens</li></ul>

___
##Let the mages teleport it

###Available if:
<li>has estate estate_mages</li><li>estate loyalty:</li><ul><li>estate is estate_mages</li><li>loyalty is at least 40</li></ul><li>estate influence:</li><ul><li>estate is estate_mages</li><li>influence is at least 50</li></ul>

###AI weighting:
AI weights this option at 99


###Efects:<ul><li>add treasury = -200</li><li>the event [Selling the dome?](../events/selling_the_dome.md) happens</li></ul>

___
##We'll have to tow it up the Ynn and cart it back to Verencel and then tow it to [Root.Capital.GetName] by ship.

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>add treasury = -400</li><li>the event [Selling the dome?](../events/selling_the_dome.md) happens</li></ul>
