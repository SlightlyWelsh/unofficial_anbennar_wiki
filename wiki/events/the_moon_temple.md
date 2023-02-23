#Information
 - Title: The Moon Temple
 - ID: flavor_arverynn.23
#Description
The Moon Temple
#Options

___
##Wall off the temple and claim the area

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>If has 2841 is empty, and 2841 has infantry in province is 1, and 2841 has infantry in province is ROOT:</li><ul><li>2841:</li><ul><li>cede province = ROOT</li><li>add core = ROOT</li><li>hidden effect:</li><ul><li>change culture = veykodan</li></ul><li>add unrest = 5</li><li>add province modifier:</li><ul><li>name = ynn_pomentere_estates</li><li>duration = -1</li></ul></ul></ul><li>2841:</li><ul><li>kill units:</li><ul><li>who = ROOT</li><li>type = infantry</li><li>amount = 1</li></ul></ul><li>custom tooltip = g35_never_know_tt</li><li>hidden effect:</li><ul><li>the event ˻flavor_arverynn.27˼ happens</li></ul></ul>

___
##The field won't be truly secured until we clear out this temple

###Available if:
<li>dynasty is "Vyrekynn"</li>

###AI weighting:
AI weights this option at 3


###Efects:<ul><li>If has 2841 is empty, and 2841 has infantry in province is 3, and 2841 has infantry in province is ROOT, and 2841 has cavalry in province is 2, and 2841 has cavalry in province is ROOT:</li><ul><li>2841:</li><ul><li>cede province = FROM</li><li>add core = FROM</li><li>hidden effect:</li><ul><li>change culture = veykodan</li></ul><li>add unrest = 5</li><li>add province modifier:</li><ul><li>name = ynn_pomentere_estates</li><li>duration = -1</li></ul></ul></ul><li>2841:</li><ul><li>kill units:</li><ul><li>who = ROOT</li><li>type = infantry</li><li>amount = 3</li></ul><li>kill units:</li><ul><li>who = ROOT</li><li>type = cavalry</li><li>amount = 2</li></ul></ul><li>the event ˻flavor_arverynn.24˼ happens</li></ul>
