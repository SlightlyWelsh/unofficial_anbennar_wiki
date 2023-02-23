#Information
 - Title: A Call to Crusade
 - ID: black_demesne.250
#Description
A Call to Crusade
#Options

___
##ALDRESIA WILLS IT!

###AI weighting:
AI weights this option at 75


###Efects:<ul><li>add ruler modifier:</li><ul><li>name = black_against_the_dark</li><li>duration = -1</li></ul><li>add opinion:</li><ul><li>who = Z99</li><li>modifier = opinion_second_aldresian_crusade_target</li></ul><li>hidden effect:</li><ul><li>set country flag [second_aldresian_crusade_participant](../flags/second_aldresian_crusade_participant.md)</li></ul><li>add stability or adm power = yes</li><li>custom tooltip = join_second_aldresian_crusade_tooltip</li></ul>

___
##We must leave the empire... for our own sakes.

###AI weighting:
AI weights this option at 10
 - Multiplied by 5 if is at war
 - Multiplied by 3 if does not have total development is 30
 - Multiplied by 5 if has ruler has personality is craven personality
 - Multiplied by 5 if has alliance with is Z99
 - Multiplied by 2 if is bankrupt
 - Multiplied by 2 if does not have stability is 1
 - Multiplied by 10 if is subject of is Z99
 - Multiplied by 2 if has religion is regent court
 - Multiplied by 0 if is an elector
 - Multiplied by 0 if has tag is A77
 - Multiplied by 2 if does not have opinion has who is emperor, and has opinion has value is 50


###Efects:<ul><li>add ruler modifier:</li><ul><li>name = black_falling_hopes</li><li>duration = -1</li></ul><li>If every owned province is part of hre:</li><ul><li>add claim = emperor</li></ul><li>every owned province:</li><ul><li>set in empire = no</li></ul><li>emperor:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = opinion_left_empire</li></ul></ul><li>add opinion:</li><ul><li>who = emperor</li><li>modifier = opinion_united_empire</li></ul><li>elector = no</li></ul>
