#Information
 - Title: A Promise of Protection
 - ID: flavour_tluukt.43
#Description
A Promise of Protection
#Options

___
##It is better to pay a modest tribute than to lose everything at the hands of gnolls.

###AI weighting:
AI weights this option at 100
 - Multiplied by 0 if has total development is 101


###Efects:<ul><li>If has FROM has country flag is [tluukt_jaddari](../flags/tluukt_jaddari.md):</li><ul><li>add treasury = 250</li></ul><li>Else if has FROM has country flag is [tluukt_zokka](../flags/tluukt_zokka.md):</li><ul><li>kill ruler = yes</li></ul><li>FROM:</li><ul><li>vassalize = ROOT</li></ul><li>jikarzax area:</li><ul><li>cede province = ROOT</li></ul><li>grixek area:</li><ul><li>cede province = ROOT</li></ul></ul>

___
##Never! We would rather die than bow before those demonspawn!

###AI weighting:
AI weights this option at 100
 - Multiplied by 0 if does not have total development is 101


###Efects:<ul><li>add prestige = 5</li><li>If has FROM has country flag is [tluukt_jaddari](../flags/tluukt_jaddari.md):</li><ul><li>FROM:</li><ul><li>add treasury = 250</li><li>add casus belli:</li><ul><li>target = ROOT</li><li>type = cb_vassalize_mission</li><li>months = 240</li></ul></ul></ul><li>Else if has FROM has country flag is [tluukt_zokka](../flags/tluukt_zokka.md):</li><ul><li>kill ruler = yes</li><li>FROM:</li><ul><li>add casus belli:</li><ul><li>target = ROOT</li><li>type = cb_vassalize_mission</li><li>months = 240</li></ul></ul><li>random owned province:</li><ul><li>spawn rebels:</li><ul><li>type = noble_rebels</li><li>size = 1</li><li>culture = ROOT</li><li>religion = ROOT</li><li>win = yes</li><li>friend = FROM</li></ul></ul></ul></ul>
