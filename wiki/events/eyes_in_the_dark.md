#Information
 - Title: Eyes in the Dark
 - ID: flavor_seghdihr.51
#Description
Eyes in the Dark
#Options

___
##This may affect things…

###AI weighting:
AI weights this option at 5


###Efects:<ul><li>If does not have event target:incursion target has province id is 4218:</li><ul><li>event target:incursion target:</li><ul><li>add devastation = 10</li><li>add province modifier:</li><ul><li>name = seghdihr_incursion_fear</li><li>duration = 3650</li></ul><li>If every neighbor province has country or subject holds is ROOT, and  is city:</li><ul><li>add devastation = 5</li><li>add province modifier:</li><ul><li>name = seghdihr_incursion_fear</li><li>duration = 1825</li></ul></ul></ul></ul><li>else:</li><ul><li>ozumbrog area:</li><ul><li>add devastation = 10</li><li>add unrest = 2</li><li>add province modifier:</li><ul><li>name = seghdihr_incursion_fear</li><li>duration = 3650</li></ul></ul></ul><li>custom tooltip = seghdihr_incursion_strength_gathered</li><li>hidden effect:</li><ul><li>change variable:</li><ul><li>which = incursion_gathering_strength</li><li>value = 200</li></ul><li>If has check variable has which is incursion gathering strength, and check variable has value is 1100:</li><ul><li>set variable:</li><ul><li>which = incursion_gathering_strength</li><li>value = 1000</li></ul></ul><li>seghdihr calculate incursion strength = yes</li><li>If has H74 has exists, and H74 is controlled by the AI:</li><ul><li>H74:</li><ul><li>add adm power = 100</li><li>add dip power = 100</li><li>add mil power = 100</li></ul></ul></ul></ul>
