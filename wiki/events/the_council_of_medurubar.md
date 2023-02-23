#Information
 - Title: The Council of Medurubar
 - ID: new_sun_cult.126
#Description
The Council of Medurubar
#Options

___
##Send a massive delegation. Let them see our power and wealth!

###AI weighting:
AI weights this option at 25
 - Multiplied by 1.5 if has opinion has who is F37, and has opinion has value is 50
 - Multiplied by 1.5 if has opinion has who is F37, and has opinion has value is 100
 - Multiplied by 2 if has alliance with is F37
 - Multiplied by 100 if has vassal of is F37
 - Multiplied by 0 if is rival is F37
 - Multiplied by 0 if has tag is U05


###Efects:<ul><li>custom tooltip = nsc_increase_unity_tt</li><li>add years of income = -0.3</li><li>add prestige = 10</li><li>hidden effect:</li><ul><li>If is chosen country is yes:</li><ul><li>REB:</li><ul><li>change variable:</li><ul><li>which = nscTempUnityVar</li><li>value = 2</li></ul><li>change variable:</li><ul><li>which = nscTotalChoicesVar</li><li>value = 2</li></ul></ul></ul><li>else:</li><ul><li>REB:</li><ul><li>change variable:</li><ul><li>which = nscTempUnityVar</li><li>value = 1</li></ul><li>change variable:</li><ul><li>which = nscTotalChoicesVar</li><li>value = 1</li></ul></ul></ul></ul></ul>

___
##No need to spend too much. Send an appropriate delegation.

###AI weighting:
AI weights this option at 50
 - Multiplied by 0 if has tag is U05


###Efects:<ul><li>add years of income = -0.2</li><li>add prestige = 5</li><li>hidden effect:</li><ul><li>If is chosen country is yes:</li><ul><li>REB:</li><ul><li>change variable:</li><ul><li>which = nscTotalChoicesVar</li><li>value = 2</li></ul></ul></ul><li>else:</li><ul><li>REB:</li><ul><li>change variable:</li><ul><li>which = nscTotalChoicesVar</li><li>value = 1</li></ul></ul></ul></ul></ul>

___
##We don't care, send the bare minimum!

###AI weighting:
AI weights this option at 25
 - Multiplied by 0.75 if has opinion has who is F37, and has opinion has value is 50
 - Multiplied by 0.75 if has opinion has who is F37, and has opinion has value is 100
 - Multiplied by 0.5 if has alliance with is F37
 - Multiplied by 0 if has vassal of is F37
 - Multiplied by 5 if is rival is F37


###Efects:<ul><li>custom tooltip = nsc_decrease_unity_tt</li><li>add years of income = -0.1</li><li>hidden effect:</li><ul><li>If is chosen country is yes:</li><ul><li>REB:</li><ul><li>change variable:</li><ul><li>which = nscTempUnityVar</li><li>value = -2</li></ul><li>change variable:</li><ul><li>which = nscTotalChoicesVar</li><li>value = 2</li></ul></ul></ul><li>else:</li><ul><li>REB:</li><ul><li>change variable:</li><ul><li>which = nscTempUnityVar</li><li>value = -1</li></ul><li>change variable:</li><ul><li>which = nscTotalChoicesVar</li><li>value = 1</li></ul></ul></ul></ul></ul>
