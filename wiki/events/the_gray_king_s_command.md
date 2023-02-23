#Information
 - Title: The Gray King's Command
 - ID: flavor_grombar.3
#Description
The Gray King's Command
#Options

___
##We shall accept integration (this will end your game).

###Available if:
<li>Z50:</li><ul><li>has country flag [half_orc_grombar](../flags/half_orc_grombar.md)</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 2 if has opinion has who is Z50, and has opinion has value is 200
 - Multiplied by 2 if has ruler is half orcish is yes
 - Multiplied by 0.5 if has ruler is half orcish is no
 - Multiplied by 0.1 if does not have opinion has who is Z50, and has opinion has value is 0


###Efects:<ul><li>Z50:</li><ul><li>inherit = ROOT</li></ul></ul>

___
##We shall protect our freedom.

###Available if:
<li>Z50:</li><ul><li>has country flag [half_orc_grombar](../flags/half_orc_grombar.md)</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 0 if has opinion has who is Z50, and has opinion has value is 200
 - Multiplied by 0 if has ruler is half orcish is yes
 - Multiplied by 1.9 if does not have opinion has who is Z50, and has opinion has value is 100


###Efects:<ul><li>add prestige = 10</li><li>grant independence = yes</li><li>every owned province:</li><ul><li>add permanent claim = Z50</li></ul></ul>

___
##We shall live on our knees (this will end your game).

###Available if:
<li>Z50:</li><ul><li>has country flag [orc_grombar](../flags/orc_grombar.md)</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 2 if has opinion has who is Z50, and has opinion has value is 200
 - Multiplied by 2 if has ruler is half orcish is yes
 - Multiplied by 0.5 if has ruler is half orcish is no
 - Multiplied by 0.1 if does not have opinion has who is Z50, and has opinion has value is 0


###Efects:<ul><li>Z50:</li><ul><li>inherit = ROOT</li></ul></ul>

___
##We shall die standing tall!

###Available if:
<li>Z50:</li><ul><li>has country flag [orc_grombar](../flags/orc_grombar.md)</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 0 if has opinion has who is Z50, and has opinion has value is 200
 - Multiplied by 0 if has ruler is half orcish is yes
 - Multiplied by 1.9 if does not have opinion has who is Z50, and has opinion has value is 100


###Efects:<ul><li>add prestige = 10</li><li>grant independence = yes</li><li>every owned province:</li><ul><li>add permanent claim = Z50</li></ul></ul>
