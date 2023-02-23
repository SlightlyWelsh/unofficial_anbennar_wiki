#Information
 - Title: Girl in the Forest: The Prodigal Daughter
 - ID: girl_in_the_forest.4
#Description
Girl in the Forest: The Prodigal Daughter
#Options

___
##We must back [Root.Heir.GetName]

###Available if:
<li>has heir</li><li>has ruler flag [girl_in_the_forest_parent](../flags/girl_in_the_forest_parent.md)</li>

###Efects:<ul><li>add heir claim = 20</li><li>clr country flag [girl_in_the_forest](../flags/girl_in_the_forest.md)</li></ul>

___
##The prodigal daughter returns!

###Available if:
<li>has ruler flag [girl_in_the_forest_parent](../flags/girl_in_the_forest_parent.md)</li>

###Efects:<ul><li>define heir:</li><ul><li>name = girl_in_the_forest_name</li><li>dynasty = ROOT</li><li>female = yes</li><li>age = 17</li><li>change adm = 2</li><li>change dip = 2</li><li>change mil = 2</li><li>claim = 70</li></ul><li>set heir flag [girl_in_the_forest](../flags/girl_in_the_forest.md)</li><li>hidden effect:</li><ul><li>the event [Girl in the Forest: An Imposter?](../events/girl_in_the_forest_an_imposter.md) happens</li></ul></ul>

___
##[Root.girl_in_the_forest_name.GetName] is a pretender!

###Available if:
<li>None of the following:</li><ul><li>has ruler flag [girl_in_the_forest_parent](../flags/girl_in_the_forest_parent.md)</li></ul>

###Efects:<ul><li>random owned province:</li><ul><li>spawn rebels:</li><ul><li>type = pretender_rebels</li><li>size = 3</li><li>female = yes</li><li>leader = girl_in_the_forest_name</li></ul></ul><li>set country flag [girl_in_the_forest_rebels](../flags/girl_in_the_forest_rebels.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: girl_in_the_forest_9_t](../events/missing_localisation_girl_in_the_forest_9_t.md) happens</li></ul></ul>

___
##[Root.girl_in_the_forest_name.GetName] is the rightful ruler!

###Available if:
<li>None of the following:</li><ul><li>ruler has personality is immortal_personality</li></ul><li>has ruler flag [girl_in_the_forest_parent](../flags/girl_in_the_forest_parent.md)</li>

###Efects:<ul><li>add prestige = -50</li><li>reduce stability or adm power = yes</li><li>remove heir:</li><ul></ul><li>define ruler:</li><ul><li>name = girl_in_the_forest_name</li><li>dynasty = ROOT</li><li>female = yes</li><li>age = 17</li><li>change adm = 2</li><li>change dip = 2</li><li>change mil = 2</li><li>claim = 70</li></ul><li>set ruler flag [girl_in_the_forest](../flags/girl_in_the_forest.md)</li></ul>
