#Information
 - Title: Cotton Imports
 - ID: anb_price.33
#Description
Cotton Imports
#Mean Time to Happen:
Base time = 1 months

#Options

___
##We will not restrict free trade.

###AI weighting:
AI weights this option at 50
 - Multiplied by 1.5 if has cotton is 6
 - Multiplied by 1.5 if has cotton is 12
 - Multiplied by 1.5 if has cotton is 18


###Efects:<ul><li>change price:</li><ul><li>trade goods = wool</li><li>key = COTTON_IMPORTS</li><li>value = -0.10</li><li>duration = -1</li></ul><li>change price:</li><ul><li>trade goods = cotton</li><li>key = COTTON_IMPORTS</li><li>value = 0.20</li><li>duration = -1</li></ul><li>add mercantilism = -2</li><li>hidden effect:</li><ul><li>set global flag [cotton_imports_global](../flags/cotton_imports_global.md)</li></ul></ul>

___
##Mercantilism is the right way.

###AI weighting:
AI weights this option at 50
 - Multiplied by 1.5 if has wool is 6
 - Multiplied by 1.5 if has wool is 12
 - Multiplied by 1.5 if has wool is 18


###Efects:<ul><li>hidden effect:</li><ul><li>set global flag [cotton_imports_global](../flags/cotton_imports_global.md)</li></ul><li>hidden effect:</li><ul><li>set country flag [cotton_imports](../flags/cotton_imports.md)</li></ul><li>1361:</li><ul><li>add trade modifier:</li><ul><li>who = root</li><li>duration = -1</li><li>power = -10</li><li>key = COTTON_IMPORTS_BANNED</li></ul></ul><li>4485:</li><ul><li>add trade modifier:</li><ul><li>who = root</li><li>duration = -1</li><li>power = -10</li><li>key = COTTON_IMPORTS_BANNED</li></ul></ul><li>4460:</li><ul><li>add trade modifier:</li><ul><li>who = root</li><li>duration = -1</li><li>power = -10</li><li>key = COTTON_IMPORTS_BANNED</li></ul></ul><li>4435:</li><ul><li>add trade modifier:</li><ul><li>who = root</li><li>duration = -1</li><li>power = -10</li><li>key = COTTON_IMPORTS_BANNED</li></ul></ul></ul>


#Pages with same name:
The following pages have the same name as this page:
 - [cotton_imports_1](cotton_imports_1.md)
