#Information
 - Title: [separatist_province.Culture.GetName] Revolt
 - ID: court_and_country_events.3
#Description
[separatist_province.Culture.GetName] Revolt
#Mean Time to Happen:
Base time = 1 days

#Options

___
##This rebellion must be crushed!

###AI weighting:
AI weights this option at 80
 - Multiplied by 0.2 if is at war


###Efects:<ul><li>add absolutism = 10</li><li>event target:separatist province:</li><ul><li>spawn rebels:</li><ul><li>type = nationalist_rebels</li><li>size = 2</li></ul><li>clr province flag [separatist_province_set_here](../flags/separatist_province_set_here.md)</li><li>add nationalism = 10</li><li>add province modifier:</li><ul><li>name = "court_and_country_hardline_vs_separatists"</li><li>duration = 1825</li></ul></ul><li>If has calc true if has all owned province has province flag is [separatist_province_set_here](../flags/separatist_province_set_here.md); and calc true if has amount is 7:</li><ul><li>custom tooltip = court_and_country_events.3.a.tt</li><li>hidden effect:</li><ul><li>If every owned province has province flag is [separatist_province_set_here](../flags/separatist_province_set_here.md):</li><ul><li>clr province flag [separatist_province_set_here](../flags/separatist_province_set_here.md)</li><li>add nationalism = 10</li><li>add province modifier:</li><ul><li>name = "court_and_country_hardline_vs_separatists"</li><li>duration = 1825</li></ul></ul></ul><li>else:</li><ul><li>If every owned province has province flag is [separatist_province_set_here](../flags/separatist_province_set_here.md):</li><ul><li>clr province flag [separatist_province_set_here](../flags/separatist_province_set_here.md)</li><li>add nationalism = 10</li><li>add province modifier:</li><ul><li>name = "court_and_country_hardline_vs_separatists"</li><li>duration = 1825</li></ul></ul></ul></ul></ul>

___
##We will buy their loyalty.

###AI weighting:
AI weights this option at 20


###Efects:<ul><li>add absolutism = 5</li><li>event target:separatist province:</li><ul><li>clr province flag [separatist_province_set_here](../flags/separatist_province_set_here.md)</li><li>add local autonomy = 40</li><li>add nationalism = -5</li><li>add province modifier:</li><ul><li>name = "court_and_country_concessions_to_separatists"</li><li>duration = 3650</li></ul></ul><li>If has calc true if has all owned province has province flag is [separatist_province_set_here](../flags/separatist_province_set_here.md); and calc true if has amount is 7:</li><ul><li>custom tooltip = court_and_country_events.3.b.tt</li><li>hidden effect:</li><ul><li>If every owned province has province flag is [separatist_province_set_here](../flags/separatist_province_set_here.md):</li><ul><li>add local autonomy = 40</li><li>add nationalism = -5</li><li>add province modifier:</li><ul><li>name = "court_and_country_concessions_to_separatists"</li><li>duration = 3650</li></ul></ul></ul><li>else:</li><ul><li>If every owned province has province flag is [separatist_province_set_here](../flags/separatist_province_set_here.md):</li><ul><li>add local autonomy = 40</li><li>add nationalism = -5</li><li>add province modifier:</li><ul><li>name = "court_and_country_concessions_to_separatists"</li><li>duration = 3650</li></ul></ul></ul></ul></ul>
