#Information
 - Title: The [Root.new_monarch_religion.GetReligionGroupName] court of [Root.Monarch.GetName]
 - ID: culture_religion_events.6
#Description
The [Root.new_monarch_religion.GetReligionGroupName] court of [Root.Monarch.GetName]
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Come one come all!

###Efects:<ul><li>trigger switch:</li><ul><li>on trigger = has_country_flag</li><li>philosopher flag:</li><ul><li>If does not have monthly income is 30:</li><ul><li>define advisor:</li><ul><li>type = philosopher</li><li>name = advisor_attracted_by_ruler</li><li>religion = new_variable:ruler_religion</li><li>skill = 2</li><li>discount = yes</li></ul></ul><li>else:</li><ul><li>define advisor:</li><ul><li>type = philosopher</li><li>name = advisor_attracted_by_ruler</li><li>religion = new_variable:ruler_religion</li><li>skill = 3</li><li>discount = yes</li></ul></ul></ul><li>master of mint flag:</li><ul><li>If does not have monthly income is 30:</li><ul><li>define advisor:</li><ul><li>type = master_of_mint</li><li>name = advisor_attracted_by_ruler</li><li>religion = new_variable:ruler_religion</li><li>skill = 2</li><li>discount = yes</li></ul></ul><li>else:</li><ul><li>define advisor:</li><ul><li>type = master_of_mint</li><li>name = advisor_attracted_by_ruler</li><li>religion = new_variable:ruler_religion</li><li>skill = 3</li><li>discount = yes</li></ul></ul></ul><li>recruitmaster flag:</li><ul><li>If does not have monthly income is 30:</li><ul><li>define advisor:</li><ul><li>type = recruitmaster</li><li>name = advisor_attracted_by_ruler</li><li>religion = new_variable:ruler_religion</li><li>skill = 2</li><li>discount = yes</li></ul></ul><li>else:</li><ul><li>define advisor:</li><ul><li>type = recruitmaster</li><li>name = advisor_attracted_by_ruler</li><li>religion = new_variable:ruler_religion</li><li>skill = 3</li><li>discount = yes</li></ul></ul></ul></ul></ul>

___
##Their talents are needed in our [Root.new_monarch_religion.GetReligionName] Provinces

###Available if:
<li>any owned province:</li><ul><li>religion is new_variable:From:ruler_religion</li><li>is state</li><li>is not a capital</li></ul>

###Efects:<ul><li>trigger switch:</li><ul><li>on trigger = has_country_flag</li><li>philosopher flag:</li><ul><li>If random owned province has religion is new variable:From:ruler religion, and  is state, and  is not a capital:</li><ul><li>add base tax = 1</li></ul></ul><li>master of mint flag:</li><ul><li>If random owned province has religion is new variable:From:ruler religion, and  is state, and  is not a capital:</li><ul><li>add base production = 1</li></ul></ul><li>recruitmaster flag:</li><ul><li>If random owned province has religion is new variable:From:ruler religion, and  is state, and  is not a capital:</li><ul><li>add base manpower = 1</li></ul></ul></ul></ul>
