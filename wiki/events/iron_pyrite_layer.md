#Information
 - Title: Iron Pyrite Layer
 - ID: diggy.7
#Description
Iron Pyrite Layer
#Mean Time to Happen:
Base time = 5 years

#Options

___
##No Pyrite shall block our way!

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>custom tooltip = dig_through_tooltip</li><li>add adm power = -50</li><li>If has global flag is [dd_grumhardhum](../flags/dd_grumhardhum.md), and  has any owned province has great project has type is dd grumhardhum, and has great project has tier is 3:</li><ul><li>add treasury = -1125</li></ul><li>Else if is not controlled by the AI:</li><ul><li>add treasury = -2250</li></ul><li>hidden effect:</li><ul><li>set country flag [dig_through](../flags/dig_through.md)</li><li>clr country flag [not_dig_through](../flags/not_dig_through.md)</li></ul><li>hidden effect:</li><ul><li>capital scope:</li><ul><li>change variable:</li><ul><li>cons prog = 0.075</li></ul></ul></ul><li>tooltip:</li><ul><li>capital scope:</li><ul><li>change variable:</li><ul><li>cons prog = 0.15</li></ul></ul></ul></ul>

___
##Try to dig through another path

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>custom tooltip = not_dig_through_tooltip</li><li>add stability or adm power = yes</li><li>hidden effect:</li><ul><li>set country flag [not_dig_through](../flags/not_dig_through.md)</li><li>clr country flag [dig_through](../flags/dig_through.md)</li></ul><li>hidden effect:</li><ul><li>capital scope:</li><ul><li>change variable:</li><ul><li>cons prog = -0.075</li></ul></ul></ul><li>tooltip:</li><ul><li>capital scope:</li><ul><li>change variable:</li><ul><li>cons prog = -0.15</li></ul></ul></ul></ul>
