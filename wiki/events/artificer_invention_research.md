#Information
 - Title: Artificer Invention Research
 - ID: artifice_events.1
#Description
Artificer Invention Research
#Options

___
##The Philosophy of Brilliant Inventions

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>set country flag [artifice_research_brilliance](../flags/artifice_research_brilliance.md)</li><li>add faction influence:</li><ul><li>faction = tec_brilliance</li><li>influence = 10</li></ul><li>If has estate privilege is estate artificers organization international gommo:</li><ul><li>custom tooltip = begin_invention_research_brilliance_5_years_tt</li><li>hidden effect:</li><ul><li>the event [Eureka!](../events/eureka.md) happens</li></ul></ul><li>else:</li><ul><li>custom tooltip = begin_invention_research_brilliance_10_years_tt</li><li>hidden effect:</li><ul><li>the event [Eureka!](../events/eureka.md) happens</li></ul></ul></ul>

___
##The Philosophy of Techno-Thaumaturgy

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>set country flag [artifice_research_technomancy](../flags/artifice_research_technomancy.md)</li><li>add faction influence:</li><ul><li>faction = tec_technomancy</li><li>influence = 10</li></ul><li>If has estate privilege is estate artificers organization international gommo:</li><ul><li>custom tooltip = begin_invention_research_technomancy_5_years_tt</li><li>hidden effect:</li><ul><li>the event [Eureka!](../events/eureka.md) happens</li></ul></ul><li>else:</li><ul><li>custom tooltip = begin_invention_research_technomancy_10_years_tt</li><li>hidden effect:</li><ul><li>the event [Eureka!](../events/eureka.md) happens</li></ul></ul></ul>

___
##The Philosophy of Mechanism

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>set country flag [artifice_research_machinery](../flags/artifice_research_machinery.md)</li><li>add faction influence:</li><ul><li>faction = tec_mechanists</li><li>influence = 10</li></ul><li>If has estate privilege is estate artificers organization international gommo:</li><ul><li>custom tooltip = begin_invention_research_machinery_5_years_tt</li><li>hidden effect:</li><ul><li>the event [Eureka!](../events/eureka.md) happens</li></ul></ul><li>else:</li><ul><li>custom tooltip = begin_invention_research_machinery_10_years_tt</li><li>hidden effect:</li><ul><li>the event [Eureka!](../events/eureka.md) happens</li></ul></ul></ul>

___
##On the grafted hand, perhaps we should focus on what we already have..

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>highlight = yes</li><li>If is not controlled by the AI:</li><ul><li>remove estate privilege = artifice_invention_research_privilege</li></ul><li>else:</li><ul><li>set country flag [remove_artifice_invention_research](../flags/remove_artifice_invention_research.md)</li></ul><li>add adm power = 30</li><li>add dip power = 30</li><li>add mil power = 30</li></ul>
