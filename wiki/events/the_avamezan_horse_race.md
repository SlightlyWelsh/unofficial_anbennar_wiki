#Information
 - Title: The Avamezan Horse Race
 - ID: bulwar_flavour.36
#Description
The Avamezan Horse Race
#Options

___
##That was hippique! Nothing escapes the eye of a expert like me!

###Available if:
<li>has country flag [horce_race_win](../flags/horce_race_win.md)</li>

###Efects:<ul><li>If has monthly income is 10:</li><ul><li>trigger switch:</li><ul><li>on trigger = has_country_flag</li><li>horse race small bet:</li><ul><li>add treasury = 90</li></ul><li>horse race medium bet:</li><ul><li>add treasury = 180</li></ul><li>horse race big bet:</li><ul><li>add treasury = 360</li></ul><li>horse race massive bet:</li><ul><li>add treasury = 720</li></ul></ul></ul><li>else:</li><ul><li>trigger switch:</li><ul><li>on trigger = has_country_flag</li><li>horse race small bet:</li><ul><li>add years of income = 0.75</li></ul><li>horse race medium bet:</li><ul><li>add years of income = 1.5</li></ul><li>horse race big bet:</li><ul><li>add years of income = 3</li></ul><li>horse race massive bet:</li><ul><li>add years of income = 6</li></ul></ul></ul></ul>

___
##That's rotten luck, I was certain [jockey_origin.GetHorseRaceColour] was going to win...

###Available if:
<li>None of the following:</li><ul><li>has country flag [horce_race_win](../flags/horce_race_win.md)</li></ul>

###Efects:<ul><li>add prestige = -5</li></ul>
