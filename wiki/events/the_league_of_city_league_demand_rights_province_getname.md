#Information
 - Title: The League of [city_league_demand_rights_province.GetName]
 - ID: court_and_country_events.4
#Description
The League of [city_league_demand_rights_province.GetName]
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Let us crush these troublemakers!

###AI weighting:
AI weights this option at 80
 - Multiplied by 0.2 if is at war


###Efects:<ul><li>add absolutism = 5</li><li>event target:city league demand rights province:</li><ul><li>set province flag [cnc_rights_demanded](../flags/cnc_rights_demanded.md)</li><li>spawn rebels:</li><ul><li>type = particularist_rebels</li><li>size = 2</li><li>win = yes</li></ul></ul></ul>

___
##We can make exceptions for the cities of [city_league_demand_rights_province.GetName].

###AI weighting:
AI weights this option at 20


###Efects:<ul><li>add absolutism = -5</li><li>event target:city league demand rights province:</li><ul><li>If area has owned by is ROOT, and  is not a capital:</li><ul><li>add local autonomy = 40</li></ul><li>set province flag [cnc_rights_demanded](../flags/cnc_rights_demanded.md)</li></ul></ul>
