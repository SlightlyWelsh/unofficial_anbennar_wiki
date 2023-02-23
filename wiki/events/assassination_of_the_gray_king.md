#Information
 - Title: Assassination of the Gray King
 - ID: flavor_grombar.103
#Description
Assassination of the Gray King
#Options

___
##Korz ascends to the throne.

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>If has heir:</li><ul><li>kill heir:</li><ul><li>allow new heir = no</li></ul></ul><li>kill ruler = yes</li><li>reduce stability or adm power = yes</li><li>define ruler:</li><ul><li>name = "Korz"</li><li>dynasty = "Frozenmaw"</li><li>age = 23</li><li>adm = 2</li><li>dip = 6</li><li>mil = 4</li><li>culture = half_orc</li><li>religion = corinite</li></ul><li>If does not have religion is corinite:</li><ul><li>reduce stability or adm power = yes</li><li>change religion = corinite</li><li>remove country modifier = grombar_weak_religion</li><li>country gets the modifier grombar_conversion_zeal until otherwise removed</li></ul><li>set ruler flag [grombar_corinite_ruler](../flags/grombar_corinite_ruler.md)</li><li>If random owned province has superregion is gerudia superregion:</li><ul><li>spawn rebels:</li><ul><li>type = pretender_rebels</li><li>leader = "Gunk"</li><li>leader dynasty = "Doombringer"</li><li>size = 3</li></ul></ul></ul>

___
##Gunk seizes the kingdom.

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>If has heir:</li><ul><li>kill heir:</li><ul><li>allow new heir = no</li></ul></ul><li>kill ruler = yes</li><li>reduce stability or adm power = yes</li><li>define ruler:</li><ul><li>name = "Gunk"</li><li>dynasty = "Doombringer"</li><li>religion = old_dookan</li><li>culture = half_orc</li><li>adm = 4</li><li>dip = 2</li><li>mil = 6</li></ul><li>set ruler flag [grombar_old_dookan_ruler](../flags/grombar_old_dookan_ruler.md)</li><li>If does not have religion is old dookan:</li><ul><li>reduce stability or adm power = yes</li><li>change religion = old_dookan</li><li>remove historical friend = B02</li><li>remove country modifier = grombar_conversion_zeal</li><li>country gets the modifier grombar_weak_religion until otherwise removed</li></ul><li>If random owned province has superregion is gerudia superregion:</li><ul><li>spawn rebels:</li><ul><li>type = pretender_rebels</li><li>leader = "Korz"</li><li>leader dynasty = "Frozenmaw"</li><li>size = 3</li></ul></ul></ul>
