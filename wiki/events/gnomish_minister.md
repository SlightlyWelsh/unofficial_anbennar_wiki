#Information
 - Title: Gnomish Minister
 - ID: gnomish_tolerance_events.5
#Description
Gnomish Minister
#Mean Time to Happen:
Base time = 1 days
 - Multiplied by 1.5 if has medium tolerance gnomish race trigger is yes
 - Multiplied by 2 if has high tolerance gnomish race trigger is yes

#Options

___
##Recruit this man, er, gnome!

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.5 if has wants to maintain tolerance gnomish is yes
 - Multiplied by 0.1 if has wants to decrease tolerance gnomish is yes


###Efects:<ul><li>small increase of gnomish tolerance effect = yes</li><li>If has country flag is [gnomish_advisor_culture_set](../flags/gnomish_advisor_culture_set.md):</li><ul><li>If has monthly income is 50:</li><ul><li>random list:</li><ul><li>1:</li><ul><li>define advisor:</li><ul><li>type = natural_scientist</li><li>culture = event_target:gnomish_advisor_culture_province</li><li>religion = event_target:gnomish_advisor_culture_province</li><li>skill = 3</li><li>discount = yes</li></ul></ul><li>1:</li><ul><li>define advisor:</li><ul><li>type = philosopher</li><li>culture = event_target:gnomish_advisor_culture_province</li><li>religion = event_target:gnomish_advisor_culture_province</li><li>skill = 3</li><li>discount = yes</li></ul></ul></ul></ul><li>Else if has monthly income is 25:</li><ul><li>random list:</li><ul><li>1:</li><ul><li>define advisor:</li><ul><li>type = natural_scientist</li><li>culture = event_target:gnomish_advisor_culture_province</li><li>religion = event_target:gnomish_advisor_culture_province</li><li>skill = 2</li><li>discount = yes</li></ul></ul><li>1:</li><ul><li>define advisor:</li><ul><li>type = philosopher</li><li>culture = event_target:gnomish_advisor_culture_province</li><li>religion = event_target:gnomish_advisor_culture_province</li><li>skill = 2</li><li>discount = yes</li></ul></ul></ul></ul><li>else:</li><ul><li>random list:</li><ul><li>1:</li><ul><li>define advisor:</li><ul><li>type = natural_scientist</li><li>culture = event_target:gnomish_advisor_culture_province</li><li>religion = event_target:gnomish_advisor_culture_province</li><li>skill = 1</li><li>discount = yes</li></ul></ul><li>1:</li><ul><li>define advisor:</li><ul><li>type = philosopher</li><li>culture = event_target:gnomish_advisor_culture_province</li><li>religion = event_target:gnomish_advisor_culture_province</li><li>skill = 1</li><li>discount = yes</li></ul></ul></ul></ul></ul><li>Else if has region is lencenor region, and has area is iochand area:</li><ul><li>If has monthly income is 50:</li><ul><li>random list:</li><ul><li>1:</li><ul><li>define advisor:</li><ul><li>type = natural_scientist</li><li>culture = creek_gnome</li><li>skill = 3</li><li>discount = yes</li></ul></ul><li>1:</li><ul><li>define advisor:</li><ul><li>type = philosopher</li><li>culture = creek_gnome</li><li>skill = 3</li><li>discount = yes</li></ul></ul></ul></ul><li>Else if has monthly income is 25:</li><ul><li>random list:</li><ul><li>1:</li><ul><li>define advisor:</li><ul><li>type = natural_scientist</li><li>culture = creek_gnome</li><li>skill = 2</li><li>discount = yes</li></ul></ul><li>1:</li><ul><li>define advisor:</li><ul><li>type = philosopher</li><li>culture = creek_gnome</li><li>skill = 2</li><li>discount = yes</li></ul></ul></ul></ul><li>else:</li><ul><li>random list:</li><ul><li>1:</li><ul><li>define advisor:</li><ul><li>type = natural_scientist</li><li>culture = creek_gnome</li><li>skill = 1</li><li>discount = yes</li></ul></ul><li>1:</li><ul><li>define advisor:</li><ul><li>type = philosopher</li><li>culture = creek_gnome</li><li>skill = 1</li><li>discount = yes</li></ul></ul></ul></ul></ul><li>Else if has region is west dameshead region, and has region is damescrown region, and has region is east dameshead region, and has region is esmaria region, and has region is the borders region, and has region is businor region:</li><ul><li>If has monthly income is 50:</li><ul><li>random list:</li><ul><li>1:</li><ul><li>define advisor:</li><ul><li>type = natural_scientist</li><li>culture = imperial_gnome</li><li>skill = 3</li><li>discount = yes</li></ul></ul><li>1:</li><ul><li>define advisor:</li><ul><li>type = philosopher</li><li>culture = imperial_gnome</li><li>skill = 3</li><li>discount = yes</li></ul></ul></ul></ul><li>Else if has monthly income is 25:</li><ul><li>random list:</li><ul><li>1:</li><ul><li>define advisor:</li><ul><li>type = natural_scientist</li><li>culture = imperial_gnome</li><li>skill = 2</li><li>discount = yes</li></ul></ul><li>1:</li><ul><li>define advisor:</li><ul><li>type = philosopher</li><li>culture = imperial_gnome</li><li>skill = 2</li><li>discount = yes</li></ul></ul></ul></ul><li>else:</li><ul><li>random list:</li><ul><li>1:</li><ul><li>define advisor:</li><ul><li>type = natural_scientist</li><li>culture = imperial_gnome</li><li>skill = 1</li><li>discount = yes</li></ul></ul><li>1:</li><ul><li>define advisor:</li><ul><li>type = philosopher</li><li>culture = imperial_gnome</li><li>skill = 1</li><li>discount = yes</li></ul></ul></ul></ul></ul><li>else:</li><ul><li>If has monthly income is 50:</li><ul><li>random list:</li><ul><li>1:</li><ul><li>define advisor:</li><ul><li>type = natural_scientist</li><li>culture = cliff_gnome</li><li>skill = 3</li><li>discount = yes</li></ul></ul><li>1:</li><ul><li>define advisor:</li><ul><li>type = philosopher</li><li>culture = cliff_gnome</li><li>skill = 3</li><li>discount = yes</li></ul></ul></ul></ul><li>Else if has monthly income is 25:</li><ul><li>random list:</li><ul><li>1:</li><ul><li>define advisor:</li><ul><li>type = natural_scientist</li><li>culture = cliff_gnome</li><li>skill = 2</li><li>discount = yes</li></ul></ul><li>1:</li><ul><li>define advisor:</li><ul><li>type = philosopher</li><li>culture = cliff_gnome</li><li>skill = 2</li><li>discount = yes</li></ul></ul></ul></ul><li>else:</li><ul><li>random list:</li><ul><li>1:</li><ul><li>define advisor:</li><ul><li>type = natural_scientist</li><li>culture = cliff_gnome</li><li>skill = 1</li><li>discount = yes</li></ul></ul><li>1:</li><ul><li>define advisor:</li><ul><li>type = philosopher</li><li>culture = cliff_gnome</li><li>skill = 1</li><li>discount = yes</li></ul></ul></ul></ul></ul></ul>

___
##A true exemplar of the community!

###AI weighting:
AI weights this option at 50
 - Multiplied by 2 if has wants to increase tolerance gnomish is yes


###Efects:<ul><li>medium increase of gnomish tolerance effect = yes</li></ul>

___
##So what?

###AI weighting:
AI weights this option at 50
 - Multiplied by 2 if has wants to decrease tolerance gnomish is yes


###Efects:<ul><li>small decrease of gnomish tolerance effect = yes</li></ul>
