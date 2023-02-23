#Information
 - Title: [Root.NativeCulture.GetName] People Enter Our Colony
 - ID: 3071
#Description
[Root.NativeCulture.GetName] People Enter Our Colony
#Mean Time to Happen:
Base time = 1 months

#Options

___
##Erase these savages from [Root.GetName]!

###AI weighting:
AI weights this option at 40


###Efects:<ul><li>owner:</li><ul><li>set country flag [NF_colony](../flags/nf_colony.md)</li><li>set country flag [NF_ruthless](../flags/nf_ruthless.md)</li></ul><li>add colonysize = 200</li><li>change native size = -3</li><li>custom tooltip = native_ruthless_tt</li></ul>

___
##Just pay them to stop hissing at us.

###AI weighting:
AI weights this option at 20


###Efects:<ul><li>owner:</li><ul><li>add treasury = 50</li><li>set country flag [NF_colony](../flags/nf_colony.md)</li><li>set country flag [NF_trader](../flags/nf_trader.md)</li></ul><li>add base tax = 1</li><li>custom tooltip = native_trader_tt</li></ul>

___
##Offer them whatever they desire, we should live in peace.

###AI weighting:
AI weights this option at 20


###Efects:<ul><li>owner:</li><ul><li>add prestige = 5</li><li>set country flag [NF_colony](../flags/nf_colony.md)</li><li>set country flag [NF_peacenik](../flags/nf_peacenik.md)</li></ul><li>add province modifier:</li><ul><li>name = colonial_accommodation_mod</li><li>duration = 3650</li></ul><li>custom tooltip = native_peace_tt</li></ul>
