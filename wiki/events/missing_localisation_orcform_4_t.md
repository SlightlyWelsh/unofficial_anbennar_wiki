#Information
 - Title: Missing localisation: orcform_4_t
 - ID: orcform.4
#Description

#Options

___
##Missing localisation: orcform_4_a

###Efects:<ul><li>hidden effect:</li><ul><li>If every owned province has continent is serpentspine:</li><ul><li>export to variable:</li><ul><li>which = TotalDev</li><li>value = development</li></ul><li>ROOT:</li><ul><li>change variable:</li><ul><li>which = TotalDev</li><li>which = PREV</li></ul></ul></ul></ul><li>hidden effect:</li><ul><li>If every owned province has continent is serpentspine:</li><ul><li>add base manpower = -20</li><li>add base tax = -20</li><li>add base production = -20</li><li>remove core = ROOT</li><li>destroy province = yes</li></ul><li>If while has check variable has TotalDev is 1:</li><ul><li>subtract variable:</li><ul><li>TotalDev = 3</li></ul><li>If has any owned province has culture group is ROOT, and has AND is a capital, and does not have development is 40; and does not have development is 20:</li><ul><li>If random owned province has culture group is ROOT, and has AND is a capital, and does not have development is 40; and does not have development is 20:</li><ul><li>add base production = 1</li><li>add base tax = 1</li><li>add base manpower = 1</li></ul></ul><li>else:</li><ul><li>If random owned province does not have development is 20:</li><ul><li>add base production = 1</li><li>add base tax = 1</li><li>add base manpower = 1</li><li>If has large orcish minority trigger is yes, and has terrain is hills, and has terrain is highlands, and has terrain is mountain, and has terrain is desert:</li><ul><li>change culture = karashari_orc</li><li>change religion = old_bulwari_sun_cult</li></ul><li>else:</li><ul><li>add orcish minority size effect = yes</li></ul></ul></ul></ul></ul></ul>
