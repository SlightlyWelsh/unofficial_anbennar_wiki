#Information
 - Title: Foreign Inventor
 - ID: innovativeness_events.4
#Description
Foreign Inventor
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Let us take [Root.inventor.GetName] in!

###AI weighting:
AI weights this option at 40


###Efects:<ul><li>If does not have government is native:</li><ul><li>add innovativeness small effect = yes</li></ul><li>Else if has government is native:</li><ul><li>add adm power = 50</li></ul><li>event target:inventor country:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = harbored_inventor</li></ul><li>If every ally does not have tag is ROOT:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = harbored_inventor</li></ul></ul></ul></ul>

___
##We would not risk the anger of [inventor_country.GetDefiniteArticleBeforePluralCountry][inventor_country.GetName].

###AI weighting:
AI weights this option at 60


###Efects:<ul><li>add prestige = 10</li><li>event target:inventor country:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = turned_away_inventor</li></ul></ul></ul>
