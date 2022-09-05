
import tkinter as tk
import re
from persons.PersonRepository import*
from persons.PersonTextRepository import*
from persons.PersonBinaryRepository import*
from activities.ActivityRepository import*
from activities.ActivityTextRepository import*
from activities.ActivityBinaryRepository import*
from UI import*
from GUI import*
from controller.UndoController import*

f = open("settings_properties.txt","r")
value = f.readline()
value = value.split('=')
value = value[1]
repo = 0
if 'inmemory' in value:
    repo = "inmemory"
    prepo = PRepo()
    arepo = ARepo()
    value = f.readline()
    value = f.readline()
elif 'text file repository' in value or 'binary file repository' in value:
    file_name = f.readline()
    file_name = file_name[:-2]
    file_name = file_name.split('=')
    file_name = file_name[1][2:]
    person_file = file_name
    file_name = f.readline()
    file_name = file_name[:-2]
    file_name = file_name.split('=')
    file_name = file_name[1][2:]
    activity_file = file_name
    if 'text file repository' in value:
        prepo = PersonTextRepository(person_file)
        arepo = ActivityTextRepository(activity_file)
    elif 'binary file repository' in value:
        prepo = PersonBinaryRepository(person_file)
        arepo = ActivityBinaryRepository(activity_file)
value = f.readline()
f.close()
value = value.split('=')
value = value[1]
value = value[:-1]
print (value)
if value ==" 'gui'":
    main_window=tk.Tk()
    undo_controller=UndoController()
    pServ=PService(undo_controller,prepo)
    aServ=AService(pServ._repo,undo_controller,arepo)
    if repo == 'inmemory':
        pServ.init_list_of_people()
        aServ.init_list_of_activities()
    gui=GUI(main_window,pServ,aServ,undo_controller)
    gui.main_window.mainloop()

elif value ==" 'command based ui'":
    undo_controller=UndoController()
    pServ=PService(undo_controller,prepo)
    aServ=AService(pServ._repo,undo_controller,arepo)
    if repo == 'inmemory':
        pServ.init_list_of_people()
        aServ.init_list_of_activities()
    c=Console(pServ,aServ,undo_controller)
    c.run()

