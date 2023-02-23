#Information
 - Title: The Immovable Sun
 - ID: jaddari_missions.21
#Description
The Immovable Sun
#Options

___
##Damn them!

###Efects:<ul><li>change religion = the_jadd</li><li>add base tax = 3</li><li>add base manpower = 5</li><li>add province modifier:</li><ul><li>name = religious_fanatics</li><li>duration = 9125</li></ul><li>spawn rebels:</li><ul><li>type = the_jadd_rebels</li><li>size = 3</li><li>religion = the_jadd</li><li>win = yes</li><li>unrest = 10</li></ul><li>hidden effect:</li><ul><li>1:</li><ul><li>subtract variable:</li><ul><li>which = jaddari_eulos_expedition</li><li>value = 1</li></ul><li>If while has check variable has which is jaddari eulos expedition, and check variable has value is 0:</li><ul><li>ROOT:</li><ul><li>spawn rebels:</li><ul><li>type = the_jadd_rebels</li><li>size = 3</li><li>religion = the_jadd</li><li>win = yes</li><li>unrest = 10</li></ul></ul><li>subtract variable:</li><ul><li>which = jaddari_eulos_expedition</li><li>value = 1</li></ul></ul></ul></ul></ul>
