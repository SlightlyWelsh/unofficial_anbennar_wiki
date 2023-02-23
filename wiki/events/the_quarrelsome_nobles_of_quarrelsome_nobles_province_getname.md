#Information
 - Title: The Quarrelsome Nobles of [quarrelsome_nobles_province.GetName]
 - ID: court_and_country_events.5
#Description
The Quarrelsome Nobles of [quarrelsome_nobles_province.GetName]
#Mean Time to Happen:
Base time = 1 days

#Options

___
##We will meet them with sword in hand.

###AI weighting:
AI weights this option at 80
 - Multiplied by 0.2 if is at war


###Efects:<ul><li>add absolutism = 5</li><li>event target:quarrelsome nobles province:</li><ul><li>set province flag [cnc_quarrelsome_nobles](../flags/cnc_quarrelsome_nobles.md)</li><li>spawn rebels:</li><ul><li>type = noble_rebels</li><li>size = 2</li></ul></ul><li>If has num of cities is 30:</li><ul><li>If random owned province does not have province flag is [cnc_quarrelsome_nobles](../flags/cnc_quarrelsome_nobles.md); and  is not a capital, and  is in capital area:</li><ul><li>spawn rebels:</li><ul><li>type = noble_rebels</li><li>size = 1</li></ul></ul></ul><li>If has num of cities is 40:</li><ul><li>If random owned province does not have province flag is [cnc_quarrelsome_nobles](../flags/cnc_quarrelsome_nobles.md); and  is not a capital, and  is in capital area:</li><ul><li>spawn rebels:</li><ul><li>type = noble_rebels</li><li>size = 1</li></ul></ul></ul><li>If has num of cities is 60:</li><ul><li>If random owned province does not have province flag is [cnc_quarrelsome_nobles](../flags/cnc_quarrelsome_nobles.md); and  is not a capital, and  is in capital area:</li><ul><li>spawn rebels:</li><ul><li>type = noble_rebels</li><li>size = 1</li></ul></ul></ul></ul>

___
##Let us see try to meet their demands.

###AI weighting:
AI weights this option at 20


###Efects:<ul><li>add absolutism = -5</li><li>add legitimacy = -10</li><li>add devotion = -10</li><li>add horde unity = -10</li><li>add republican tradition = -5</li><li>event target:quarrelsome nobles province:</li><ul><li>add local autonomy = 40</li><li>set province flag [cnc_quarrelsome_nobles](../flags/cnc_quarrelsome_nobles.md)</li></ul></ul>
