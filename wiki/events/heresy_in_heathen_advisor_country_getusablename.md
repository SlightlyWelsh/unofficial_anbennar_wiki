#Information
 - Title: Heresy in [heathen_advisor_country.GetUsableName]
 - ID: new_court_flavour_events.39
#Description
Heresy in [heathen_advisor_country.GetUsableName]
#Mean Time to Happen:
Base time = 5475 days

#Options

___
##Intolerable! We must lodge a protest.

###AI weighting:
AI weights this option at 1
 - Multiplied by 0 if has alliance with is root, and has reverse has opinion has who is root, and reverse has opinion has value is 100
 - Multiplied by 2 if does not have reverse has opinion has who is root, and reverse has opinion has value is -50


###Efects:<ul><li>add devotion = 5</li><li>event target:heathen advisor country:</li><ul><li>the event [The [Z97.Monarch.GetTitle]'s Demands](../events/the_z97_monarch_gettitle_s_demands.md) happens</li><li>add opinion:</li><ul><li>who = root</li><li>modifier = opinion_interfering_pope</li></ul></ul><li>add estate loyalty:</li><ul><li>estate = estate_church</li><li>loyalty = 10</li></ul></ul>

___
##We shall turn a blind eye.

###AI weighting:
AI weights this option at 1
 - Multiplied by 0.5 if does not have devotion is 50
 - Multiplied by 0 if does not have devotion is 30


###Efects:<ul><li>add devotion = -10</li><li>add estate loyalty:</li><ul><li>estate = estate_church</li><li>loyalty = -10</li></ul></ul>
