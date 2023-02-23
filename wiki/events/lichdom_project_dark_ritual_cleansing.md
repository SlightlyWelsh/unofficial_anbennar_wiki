#Information
 - Title: Lichdom Project: Dark Ritual Cleansing
 - ID: magic_project_lichdom.9
#Description
Lichdom Project: Dark Ritual Cleansing
#Mean Time to Happen:
Base time = 12 months
 - Multiplied by 0.5 if has ruler flag is [magic_project_lichdom_fast](../flags/magic_project_lichdom_fast.md)
 - Multiplied by 0.05 if has had ruler flag is [magic_project_lichdom_8](../flags/magic_project_lichdom_8.md) for 730 days

#Options

___
##Begin the Cleanse

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>add ruler modifier:</li><ul><li>name = magic_project_necromancy_ruler_cleansing</li><li>duration = 1095</li></ul><li>set ruler flag [magic_project_lichdom_9](../flags/magic_project_lichdom_9.md)</li><li>hidden effect:</li><ul><li>the event [Lichdom Project: Consumption](../events/lichdom_project_consumption.md) happens</li></ul><li>custom tooltip = tooltip_magic_project_advance</li></ul>

___
##Transmutation spells will help quicken the process

###Available if:
<li>has ruler flag [transmutation_2](../flags/transmutation_2.md)</li>

###AI weighting:
AI weights this option at 50
 - Multiplied by 10 if has ruler flag is [transmutation_2](../flags/transmutation_2.md)


###Efects:<ul><li>highlight = yes</li><li>add ruler modifier:</li><ul><li>name = magic_project_necromancy_ruler_cleansing</li><li>duration = 365</li></ul><li>hidden effect:</li><ul><li>the event [Lichdom Project: Consumption](../events/lichdom_project_consumption.md) happens</li></ul><li>set ruler flag [magic_project_lichdom_9](../flags/magic_project_lichdom_9.md)</li><li>custom tooltip = tooltip_magic_project_advance</li><li>custom tooltip = tooltip_option_transmutation_1</li></ul>
