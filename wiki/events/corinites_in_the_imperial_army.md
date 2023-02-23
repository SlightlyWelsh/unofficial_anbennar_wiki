#Information
 - Title: Corinites in the Imperial Army
 - ID: flavor_istralore.1
#Description
Corinites in the Imperial Army
#Mean Time to Happen:
Base time = 100 months
 - Multiplied by 0.5 if has any owned province has religion is corinite
 - Multiplied by 0.1 if has any owned province has religion is corinite, and any owned province is reformation center

#Options

___
##The Corinites present a just and righteous cause. I will join you, brothers!

###AI weighting:
AI weights this option at 60
 - Multiplied by 10000 if has personal deity is corin
 - Multiplied by 2 if has ruler has personality is zealot personality
 - Multiplied by 2 if has mil is 3
 - Multiplied by 0.8 if is the emperor, and  has hre does not have religion treaty
 - Multiplied by 2 if has personality is ai militarist
 - Multiplied by 1.5 if has ruler has personality is free thinker personality


###Efects:<ul><li>change religion = corinite</li><li>capital scope:</li><ul><li>change religion = corinite</li><li>add reform center = corinite</li><li>add permanent province modifier:</li><ul><li>name = "religious_zeal_at_conv"</li><li>duration = 9000</li></ul></ul><li>country gets the modifier "conversion_zeal" for 10 years</li><li>add ruler modifier:</li><ul><li>name = istralore_support_of_the_corinite_military</li><li>duration = -1</li></ul></ul>

___
##Reject the petition.

###AI weighting:
AI weights this option at 40
 - Multiplied by 10000 if has personal deity is adean
 - Multiplied by 1.5 if has ruler has personality is calm personality
 - Multiplied by 1.5 if has ruler has personality is careful personality


###Efects:<ul><li>If random owned province has religion group is cannorian, and  is core is ROOT, and  has development is 10, and  is not a capital:</li><ul><li>change religion = corinite</li><li>spawn rebels:</li><ul><li>type = corinite_rebels</li><li>size = 3</li><li>win = yes</li></ul></ul></ul>
