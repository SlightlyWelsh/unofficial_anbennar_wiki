#Information
 - Title: Defiance of Vels Domfan
 - ID: flavor_arverynn.19
#Description
Defiance of Vels Domfan
#Options

___
##Relocate the Mint, and be grateful your town remains standing

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>1134:</li><ul><li>add devastation = 20</li><li>add base production = -2</li></ul><li>1139:</li><ul><li>add base production = 1</li><li>add province modifier:</li><ul><li>name = G35_imperial_mint</li><li>duration = -1</li></ul></ul><li>add inflation = 2</li><li>add prestige = 10</li><li>H26:</li><ul><li>add trust:</li><ul><li>who = ROOT</li><li>value = -10</li><li>mutual = no</li></ul></ul></ul>

___
##The Mint is staying, but so are we

###Available if:
<li>1134:</li><ul><li>country or non sovereign subject holds is this nation</li></ul>

###AI weighting:
AI weights this option at 2


###Efects:<ul><li>1134:</li><ul><li>If does not have owned by is ROOT:</li><ul><li>cede province = ROOT</li></ul><li>add permanent province modifier:</li><ul><li>name = G35_imperial_mint</li><li>duration = -1</li></ul></ul><li>add prestige = 10</li></ul>

___
##Let us absolve their crime. Live and let live

###Available if:
<li>Any of the following:</li><ul><li>All of the following:</li><ul><li>H26:</li><ul><li>is subject of is this nation</li></ul><li>Any of the following:</li><ul><li>owns core province 1134</li><li>H26:</li><ul><li>owns core province 1134</li></ul></ul></ul><li>AND:</li><ul><li>H26:</li><ul><li>does not exist</li></ul><li>owns core province 1134</li></ul></ul>

###AI weighting:
AI weights this option at 1
 - Multiplied by 2 if has opinion has who is H26, and has opinion has value is 50
 - Multiplied by 2 if has opinion has who is H26, and has opinion has value is 100
 - Multiplied by 2 if has opinion has who is H26, and has opinion has value is 150


###Efects:<ul><li>If has H26 has does not exist:</li><ul><li>release = H26</li><li>H26:</li><ul><li>the event ˻ynn_events.20˼ happens</li></ul><li>hidden effect:</li><ul><li>H26:</li><ul><li>change religion = ROOT</li></ul></ul></ul><li>1134:</li><ul><li>If has H26 has exists; and  does not have owned by is H26:</li><ul><li>cede province = H26</li><li>H26:</li><ul><li>set capital = 1134</li></ul></ul><li>add permanent province modifier:</li><ul><li>name = G35_imperial_mint</li><li>duration = -1</li></ul></ul><li>add historical friend = H26</li><li>H26:</li><ul><li>add historical friend = ROOT</li></ul></ul>
