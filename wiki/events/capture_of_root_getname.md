#Information
 - Title: Capture of [Root.GetName]
 - ID: diggy.13
#Description
Capture of [Root.GetName]
#Options

___
##Such is the nature of war

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>goto = ROOT</li><li>add devastation = 20</li><li>If has province modifier is partially ruined hold:</li><ul><li>remove province modifier = dig_1</li><li>remove province modifier = dig_2</li><li>remove province modifier = dig_3</li><li>remove province modifier = dig_4</li><li>remove province modifier = dig_5</li><li>remove province modifier = dig_6</li><li>remove province modifier = dig_7</li><li>remove province modifier = dig_8</li><li>remove province modifier = dig_9</li><li>remove province modifier = dig_10</li><li>remove province modifier = dig_11</li><li>remove province modifier = partially_ruined_hold</li><li>add permanent province modifier:</li><ul><li>name = ruined_hold</li><li>duration = -1</li></ul><li>add base production = -3</li><li>add base manpower = -3</li><li>add base tax = -3</li></ul><li>Else if has province modifier is damaged hold:</li><ul><li>remove province modifier = damaged_hold</li><li>add permanent province modifier:</li><ul><li>name = partially_ruined_hold</li><li>duration = -1</li></ul><li>add base production = -2</li><li>add base manpower = -2</li><li>add base tax = -2</li></ul><li>else:</li><ul><li>add permanent province modifier:</li><ul><li>name = damaged_hold</li><li>duration = -1</li></ul><li>add base production = -1</li><li>add base manpower = -1</li><li>add base tax = -1</li></ul></ul>
