#Information
 - Title: The Scorching Sun
 - ID: jaddari_missions.104
#Description
The Scorching Sun
#Options

___
##Personally visit [scorching_sun_target_east.GetAreaName].

###Efects:<ul><li>goto = scorching_sun_target_east</li><li>add dip power = -50</li><li>event target:scorching sun target east:</li><ul><li>area:</li><ul><li>add province modifier:</li><ul><li>name = jaddari_burned_out_the_darkness</li><li>duration = 3650</li></ul></ul></ul><li>event target:scorching sun target west:</li><ul><li>area:</li><ul><li>add province modifier:</li><ul><li>name = jaddari_punished_by_the_blazing_sun</li><li>duration = 3650</li></ul></ul></ul><li>jaddempire change leaning east tiny = yes</li></ul>

___
##Show [scorching_sun_target_west.GetAreaName] that they are blessed.

###Efects:<ul><li>goto = scorching_sun_target_west</li><li>add dip power = -50</li><li>event target:scorching sun target west:</li><ul><li>area:</li><ul><li>add province modifier:</li><ul><li>name = jaddari_burned_out_the_darkness</li><li>duration = 3650</li></ul></ul></ul><li>event target:scorching sun target east:</li><ul><li>area:</li><ul><li>add province modifier:</li><ul><li>name = jaddari_punished_by_the_blazing_sun</li><li>duration = 3650</li></ul></ul></ul><li>jaddempire change leaning west tiny = yes</li></ul>

___
##There are other matters to attend to.

###Efects:<ul><li>event target:scorching sun target west:</li><ul><li>add province modifier:</li><ul><li>name = jaddari_punished_by_the_blazing_sun</li><li>duration = 3650</li></ul></ul><li>event target:scorching sun target east:</li><ul><li>add province modifier:</li><ul><li>name = jaddari_punished_by_the_blazing_sun</li><li>duration = 3650</li></ul></ul></ul>
