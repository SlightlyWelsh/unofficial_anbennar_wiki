#Information
 - Title: The Prince of Khasa
 - ID: akan_flavour.1
#Description
The Prince of Khasa
#Options

___
##He's a mad prince of a fallen kingdom, begone.

###AI weighting:
AI weights this option at 50
 - Multiplied by 2 if has opinion has who is A47, and has opinion has value is 100
 - Multiplied by 2.5 if has A47 is controlled by the AI
 - Multiplied by 0.5 if has army size percentage is 0.75
 - Multiplied by 0.1 if does not have opinion has who is A47, and has opinion has value is 80; and  has A47 is not controlled by the AI


###Efects:<ul><li>U07:</li><ul><li>the event [The Prince of Khasa](../events/the_prince_of_khasa.md) happens</li></ul><li>hidden effect:</li><ul><li>A47:</li><ul><li>the event [The Boy who was Denied](../events/the_boy_who_was_denied.md) happens</li></ul></ul><li>add prestige = -10</li><li>add liberty desire = -15</li><li>hidden effect:</li><ul><li>set global flag [rejected_bashal](../flags/rejected_bashal.md)</li></ul></ul>

___
##Perhaps it is time for the prince to become a king.

###AI weighting:
AI weights this option at 40
 - Multiplied by 0.1 if has opinion has who is A47, and has opinion has value is 150
 - Multiplied by 2 if does not have opinion has who is A47, and has opinion has value is 100
 - Multiplied by 2 if has liberty desire is 50
 - Multiplied by 0.5 if does not have army size percentage is 0.75
 - Multiplied by 0.1 if has A47 is controlled by the AI


###Efects:<ul><li>declare war with cb:</li><ul><li>who = A47</li><li>casus belli = cb_independence_war</li></ul><li>define ruler:</li><ul><li>name = "Bashal I"</li><li>dynasty = "Keskhasa"</li><li>culture = khasani</li><li>religion = mother_akan</li><li>adm = 5</li><li>dip = 4</li><li>mil = 6</li><li>age = 20</li><li>claim = 50</li></ul><li>define ruler to general:</li><ul><li>fire = 2</li><li>shock = 5</li><li>manuever = 4</li><li>siege = 3</li></ul><li>remove historical friend = A47</li><li>A47:</li><ul><li>remove historical friend = U06</li></ul><li>If does not have religion is mother akan:</li><ul><li>U06:</li><ul><li>change religion = mother_akan</li></ul></ul><li>hidden effect:</li><ul><li>A47:</li><ul><li>the event [The Boy who would be King](../events/the_boy_who_would_be_king.md) happens</li></ul><li>U06:</li><ul><li>the event [The Prince of Khasa](../events/the_prince_of_khasa.md) happens</li></ul></ul><li>add prestige = 15</li></ul>

___
##Refuse him gently, and grant him his estate.

###Available if:
<li>owns core province 383</li>

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>custom tooltip = keskhasa_estate</li><li>383:</li><ul><li>cede province = F57</li><li>remove core = U06</li></ul><li>F57:</li><ul><li>define ruler:</li><ul><li>name = "Bashal I"</li><li>dynasty = "Keskhasa"</li><li>culture = khasani</li><li>religion = mother_akan</li><li>adm = 5</li><li>dip = 4</li><li>mil = 6</li><li>age = 20</li><li>claim = 95</li></ul><li>add ruler personality = inspiring_leader_personality</li><li>add historical friend = U06</li><li>hidden effect:</li><ul><li>the event [The Prince of Khasa](../events/the_prince_of_khasa.md) happens</li></ul></ul><li>switch tag = F57</li><li>hidden effect:</li><ul><li>U07:</li><ul><li>the event [The Prince of Khasa](../events/the_prince_of_khasa.md) happens</li></ul></ul><li>U06:</li><ul><li>add historical friend = F57</li></ul><li>hidden effect:</li><ul><li>A47:</li><ul><li>the event [The Boy King](../events/the_boy_king.md) happens</li></ul><li>F57:</li><ul><li>bulwar superregion:</li><ul><li>discover country = ROOT</li></ul><li>salahad superregion:</li><ul><li>discover country = ROOT</li></ul><li>ourdia region:</li><ul><li>discover country = ROOT</li></ul><li>seghdihr area:</li><ul><li>discover country = ROOT</li></ul><li>verkal gulan area:</li><ul><li>discover country = ROOT</li></ul><li>1891:</li><ul><li>discover country = ROOT</li></ul><li>1920:</li><ul><li>discover country = ROOT</li></ul><li>1921:</li><ul><li>discover country = ROOT</li></ul><li>1920:</li><ul><li>discover country = ROOT</li></ul><li>1648:</li><ul><li>discover country = ROOT</li></ul><li>1922:</li><ul><li>discover country = ROOT</li></ul><li>1793:</li><ul><li>discover country = ROOT</li></ul><li>1794:</li><ul><li>discover country = ROOT</li></ul><li>1795:</li><ul><li>discover country = ROOT</li></ul><li>3190:</li><ul><li>discover country = ROOT</li></ul><li>3191:</li><ul><li>discover country = ROOT</li></ul><li>6109:</li><ul><li>discover country = ROOT</li></ul><li>6108:</li><ul><li>discover country = ROOT</li></ul><li>6106:</li><ul><li>discover country = ROOT</li></ul><li>6105:</li><ul><li>discover country = ROOT</li></ul><li>divenhal sea region:</li><ul><li>discover country = ROOT</li></ul><li>ourdia region:</li><ul><li>discover country = ROOT</li></ul><li>businor region:</li><ul><li>discover country = ROOT</li></ul><li>the borders region:</li><ul><li>discover country = ROOT</li></ul><li>esmaria region:</li><ul><li>discover country = ROOT</li></ul><li>east dameshead region:</li><ul><li>discover country = ROOT</li></ul><li>west dameshead region:</li><ul><li>discover country = ROOT</li></ul><li>lencenor region:</li><ul><li>discover country = ROOT</li></ul><li>small country region:</li><ul><li>discover country = ROOT</li></ul><li>damescrown region:</li><ul><li>discover country = ROOT</li></ul><li>iochand area:</li><ul><li>discover country = ROOT</li></ul><li>dameshead sea region:</li><ul><li>discover country = ROOT</li></ul><li>westcoast region:</li><ul><li>discover country = ROOT</li></ul><li>4162:</li><ul><li>discover country = ROOT</li></ul><li>4167:</li><ul><li>discover country = ROOT</li></ul><li>4157:</li><ul><li>discover country = ROOT</li></ul><li>1976:</li><ul><li>discover country = ROOT</li></ul><li>1919:</li><ul><li>discover country = ROOT</li></ul></ul></ul></ul>


#Pages with same name:
The following pages have the same name as this page:
 - [the_prince_of_khasa_1](the_prince_of_khasa_1.md)


#Pages with same name:
The following pages have the same name as this page:
 - [the_prince_of_khasa_1](the_prince_of_khasa_1.md)


#Pages with same name:
The following pages have the same name as this page:
 - [the_prince_of_khasa_1](the_prince_of_khasa_1.md)


#Pages with same name:
The following pages have the same name as this page:
 - [the_prince_of_khasa_1](the_prince_of_khasa_1.md)


#Pages with same name:
The following pages have the same name as this page:
 - [the_prince_of_khasa_1](the_prince_of_khasa_1.md)
