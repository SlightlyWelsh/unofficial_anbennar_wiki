#Information
 - Title: The Death of Raja Indranayar the Idle
 - ID: rahenraj.90
#Description
The Death of Raja Indranayar the Idle
#Options

___
##Indrapalar is the rightful heir, and legitimacy still matters, even in times such as these.

###Available if:
<li>has regency</li>

###Efects:<ul><li>define ruler:</li><ul><li>name = "Manava"</li><li>dynasty = "of the Bloody Claw"</li><li>age = 37</li><li>adm = 6</li><li>dip = 3</li><li>mil = 4</li><li>regency = yes</li><li>culture = royal_harimari</li></ul><li>set heir flag [manava_as_regent](../flags/manava_as_regent.md)</li><li>raj vizier sway change:</li><ul><li>amount = 25</li></ul></ul>

___
##[R53.Monarch.GetName]'s military expertise is needed if the Raj is to endure this period of crisis.

###Available if:
<li>R53:</li><ul><li>exists</li><li>dynasty is this nation</li></ul>

###Efects:<ul><li>goto = dhenijansar_capital</li><li>add legitimacy = -10</li><li>hidden effect:</li><ul><li>R53:</li><ul><li>exile ruler as:</li><ul><li>name = ganyakanar</li></ul><li>If has heir:</li><ul><li>exile heir as = ganyakanar_heir</li></ul></ul></ul><li>inherit = R53</li><li>set ruler = ganyakanar</li><li>set heir = ganyakanar_heir</li><li>custom tooltip = raj_ganyakanar_becomes_ruler_tt</li></ul>

___
##Ganjina is the blood of Amanapurna Peacemaker - perhaps she too can bring peace.

###Available if:
<li>R10:</li><ul><li>exists</li><li>dynasty is this nation</li></ul>

###Efects:<ul><li>goto = sarnavan_capital</li><li>add legitimacy = -40</li><li>create alliance = R10</li><li>create marriage = R10</li><li>define ruler:</li><ul><li>name = "Ganjina"</li><li>dynasty = "of the Bloody Claw"</li><li>age = 27</li><li>adm = 4</li><li>dip = 2</li><li>mil = 2</li><li>female = yes</li><li>culture = royal_harimari</li></ul><li>set country flag [raj_married_ganjina](../flags/raj_married_ganjina.md)</li></ul>
