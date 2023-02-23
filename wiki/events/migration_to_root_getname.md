#Information
 - Title: Migration to [Root.GetName]
 - ID: the_command.20
#Description
Migration to [Root.GetName]
#Mean Time to Happen:
Base time = 3 months
 - Multiplied by 0.8 if has province id is 4635
 - Multiplied by 0.5 if has province id is 4635, and does not have culture is lion command
 - Multiplied by 0.8 if has area is ghilapur area, and has area is nadida area

#Options

___
##War may change, but the camp is eternal.

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>owner:</li><ul><li>If random owned province has region is jade mines region, and has hobgoblin majority trigger is yes, and has hobgoblin minority trigger is yes:</li><ul><li>If has hobgoblin minority trigger is yes:</li><ul><li>remove hobgoblin minority size effect = yes</li></ul><li>Else if does not have development is 5; and has AND has province id is 4313, and does not have development is 17; and has AND has province id is 4311, and does not have development is 24:</li><ul><li>If has development is 4:</li><ul><li>random list:</li><ul><li>1:</li><ul><li>trigger:</li><ul><li>base tax = 2</li></ul><li>add base tax = -1</li></ul><li>1:</li><ul><li>trigger:</li><ul><li>base production = 2</li></ul><li>add base production = -1</li></ul><li>1:</li><ul><li>trigger:</li><ul><li>base manpower = 2</li></ul><li>add base manpower = -1</li></ul></ul></ul><li>change culture = undergrowth_goblin</li></ul><li>else:</li><ul><li>random list:</li><ul><li>1:</li><ul><li>trigger:</li><ul><li>base tax = 2</li></ul><li>add base tax = -1</li></ul><li>1:</li><ul><li>trigger:</li><ul><li>base production = 2</li></ul><li>add base production = -1</li></ul><li>1:</li><ul><li>trigger:</li><ul><li>base manpower = 2</li></ul><li>add base manpower = -1</li></ul></ul></ul></ul></ul><li>ROOT:</li><ul><li>If has large hobgoblin minority trigger is yes:</li><ul><li>If has owner has num of owned provinces with has value is 4, and num of owned provinces with has culture is lion command, and num of owned provinces with has region is shamakhad region:</li><ul><li>random list:</li><ul><li>3:</li><ul><li>add base tax = 1</li></ul><li>3:</li><ul><li>add base production = 1</li></ul><li>4:</li><ul><li>add base manpower = 1</li></ul></ul></ul><li>else:</li><ul><li>random list:</li><ul><li>3:</li><ul><li>random list:</li><ul><li>3:</li><ul><li>add base tax = 1</li></ul><li>3:</li><ul><li>add base production = 1</li></ul><li>4:</li><ul><li>add base manpower = 1</li></ul></ul></ul><li>1:</li><ul><li>change culture = lion_command</li><li>change religion = godlost</li><li>hidden effect:</li><ul><li>on province culture converted estate privilges effect = yes</li></ul></ul></ul></ul></ul><li>Else if has hobgoblin majority trigger is yes:</li><ul><li>random list:</li><ul><li>3:</li><ul><li>add base tax = 1</li></ul><li>3:</li><ul><li>add base production = 1</li></ul><li>4:</li><ul><li>add base manpower = 1</li></ul></ul></ul><li>else:</li><ul><li>add hobgoblin minority size effect = yes</li></ul></ul></ul>
