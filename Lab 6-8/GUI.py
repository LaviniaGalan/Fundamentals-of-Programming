import tkinter as tk 
from persons.PersonService import *
from activities.ActivityService import*

class GUI():
    def __init__(self,window,serv,act_serv,undo_controller):
        self.main_window=window
        self.init_main_window()
        self._personService=serv
        self._activityService=act_serv
        self.undo_controller=undo_controller

    def init_main_window(self):
        canvas=tk.Canvas(self.main_window,height=1000,width=800)
        canvas.pack()
        frame=tk.Frame(self.main_window,bg='#9FD5C7')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        label=tk.Label(frame, text='Activity Planner',bg='#9FD5C7',font=28)
        label.place(relx=0.395,rely=0.01,height=100)
        button1=tk.Button(frame, text='1. Manage the list of people.',font=18,bg='black',fg='white',command=self.menu_1) 
        button1.place(relx=0.3, rely=0.2,height=50)
        button2=tk.Button(frame, text='2. Manage the list of activities.',font=18,bg='black',fg='white',command=self.menu_2) 
        button2.place(relx=0.29, rely=0.3,height=50)
        button3=tk.Button(frame, text='3. Search for people or activities.',font=18,bg='black',fg='white',command=self.menu_3) 
        button3.place(relx=0.27, rely=0.4,height=50)
        button4=tk.Button(frame, text='4. Show statistics.',font=18,bg='black',fg='white',command=self.menu_4) 
        button4.place(relx=0.38, rely=0.5,height=50)
        button5=tk.Button(frame, text='5. Undo.',font=18,bg='black',fg='white',command=lambda:self.undo()) 
        button5.place(relx=0.45, rely=0.6,height=50)
        button6=tk.Button(frame, text='6. Redo.',font=18,bg='black',fg='white',command=lambda:self.redo()) 
        button6.place(relx=0.45, rely=0.7,height=50)
        button7=tk.Button(frame, text='7. Exit.',font=18,bg='black',fg='white',command=lambda:self.close_window(self.main_window)) 
        button7.place(relx=0.46, rely=0.8,height=50)

    def close_window(self,window):
        window.destroy()

    def menu_1(self):
        window1=tk.Tk()
        canvas=tk.Canvas(window1,height=700,width=800)
        canvas.pack()
        frame=tk.Frame(window1,bg='#9FD5C7')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        label=tk.Label(frame, text='Manage the list of people.',bg='#9FD5C7',font=28)
        label.place(relx=0.36,rely=0.01,height=100)
        button1=tk.Button(frame, text='1. Add person.',font=18,bg='black',fg='white',command=lambda:self.add_person_window()) 
        button1.place(relx=0.4, rely=0.2,height=50)
        button2=tk.Button(frame, text='2. Remove person.',font=18,bg='black',fg='white',command=lambda:self.remove_person_window()) 
        button2.place(relx=0.375, rely=0.35,height=50)
        button3=tk.Button(frame, text='3. Update person.',font=18,bg='black',fg='white',command=lambda:self.update_person_window()) 
        button3.place(relx=0.385, rely=0.50,height=50)
        button4=tk.Button(frame, text='4. Show people.',font=18,bg='black',fg='white',command=lambda:self.show_people_window()) 
        button4.place(relx=0.4, rely=0.65,height=50)
        button5=tk.Button(frame, text='5. Back to main menu.',font=18,bg='black',fg='white',command=lambda:self.close_window(window1)) 
        button5.place(relx=0.36, rely=0.8,height=50)

    def add_person_window(self):
        window_for_add=tk.Tk()
        canvas=tk.Canvas(window_for_add,height=700,width=800)
        canvas.pack()
        frame=tk.Frame(window_for_add,bg='#9FD5C7')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        label=tk.Label(frame, text='Add Person',bg='#9FD5C7',font=28)
        label.place(relx=0.395,rely=0.01,height=100)
        id_label=tk.Label(frame, text='Enter the ID:',bg='#9FD5C7',font=16)
        id_label.place(relx=0.2,rely=0.2)
        id_entry=tk.Entry(frame,width=30,bg='white')
        id_entry.place(relx=0.5,rely=0.2,height=30)
        name_label=tk.Label(frame, text='Enter the name:',bg='#9FD5C7',font=16)
        name_label.place(relx=0.2,rely=0.3)
        name_entry=tk.Entry(frame,width=30,bg='white')
        name_entry.place(relx=0.5,rely=0.3,height=30)
        phoneNo_label=tk.Label(frame, text='Enter the phone no:',bg='#9FD5C7',font=16)
        phoneNo_label.place(relx=0.2,rely=0.4)
        phoneNo_entry=tk.Entry(frame,width=30,bg='white')
        phoneNo_entry.place(relx=0.5,rely=0.4,height=30)
        button=tk.Button(frame,text='Submit.',font=18,bg='black',fg='white',command=lambda:self.add_person_ui(window_for_add,frame,id_entry.get(),name_entry.get(),phoneNo_entry.get()))
        button.place(relx=0.4,rely=0.6,height=50)

    def add_person_ui(self,window_for_add,frame,personID,name,phoneNo):
        try:
            self._personService.add_person(personID,name,phoneNo)
            result_label=tk.Label(frame, text='Person added!',bg='#9FD5C7',font=16)
            result_label.place(relx=0.36,rely=0.75,height=50)
        except Exception as error:
            result_label=tk.Label(frame, text=error,bg='#9FD5C7',font=16)
            result_label.place(relx=0.3,rely=0.75,height=50)
        window_for_add.after(1000, lambda: window_for_add.destroy())

    def remove_person_window(self):
        window_for_remove=tk.Tk()
        canvas=tk.Canvas(window_for_remove,height=700,width=800)
        canvas.pack()
        frame=tk.Frame(window_for_remove,bg='#9FD5C7')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        label=tk.Label(frame, text='Remove Person',bg='#9FD5C7',font=28)
        label.place(relx=0.395,rely=0.01,height=100)
        id_label=tk.Label(frame, text='Enter the ID:',bg='#9FD5C7',font=16)
        id_label.place(relx=0.2,rely=0.2)
        id_entry=tk.Entry(frame,width=30,bg='white')
        id_entry.place(relx=0.5,rely=0.2,height=30)
        button=tk.Button(frame,text='Submit.',font=18,bg='black',fg='white',command=lambda:self.remove_person_ui(window_for_remove,frame,id_entry.get()))
        button.place(relx=0.4,rely=0.6,height=50)

    def remove_person_ui(self,window_for_remove,frame,personID):
        try:
            op=self._personService.remove_by_id(personID)
            self._activityService.update_after_remove_person(personID,op)
            result_label=tk.Label(frame, text='Person removed!',bg='#9FD5C7',font=16)
            result_label.place(relx=0.36,rely=0.75,height=50)
        except Exception as error:
            result_label=tk.Label(frame, text=error,bg='#9FD5C7',font=16)
            result_label.place(relx=0.3,rely=0.75,height=50)
        window_for_remove.after(1000, lambda: window_for_remove.destroy())

    def update_person_window(self):
        window_for_update=tk.Tk()
        canvas=tk.Canvas(window_for_update,height=700,width=800)
        canvas.pack()
        frame=tk.Frame(window_for_update,bg='#9FD5C7')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        label=tk.Label(frame, text='Update Person',bg='#9FD5C7',font=28)
        label.place(relx=0.395,rely=0.01,height=100)
        id_label=tk.Label(frame, text='Enter the ID:',bg='#9FD5C7',font=16)
        id_label.place(relx=0.2,rely=0.2)
        id_entry=tk.Entry(frame,width=30,bg='white')
        id_entry.place(relx=0.5,rely=0.2,height=30)
        name_label=tk.Label(frame, text='Enter the new name:',bg='#9FD5C7',font=16)
        name_label.place(relx=0.2,rely=0.3)
        name_entry=tk.Entry(frame,width=30,bg='white')
        name_entry.place(relx=0.5,rely=0.3,height=30)
        phoneNo_label=tk.Label(frame, text='Enter the phone no:',bg='#9FD5C7',font=16)
        phoneNo_label.place(relx=0.2,rely=0.4)
        phoneNo_entry=tk.Entry(frame,width=30,bg='white')
        phoneNo_entry.place(relx=0.5,rely=0.4,height=30)
        button=tk.Button(frame,text='Submit.',font=18,bg='black',fg='white',command=lambda:self.update_person_ui(window_for_update,frame,id_entry.get(),name_entry.get(),phoneNo_entry.get()))
        button.place(relx=0.4,rely=0.6,height=50)

    def update_person_ui(self,window_for_update,frame,personID,new_name,new_phoneNo):
        try:
            self._personService.update_person(personID,new_name,new_phoneNo)
            result_label=tk.Label(frame, text='Person updated!',bg='#9FD5C7',font=16)
            result_label.place(relx=0.36,rely=0.75,height=50)
        except Exception as error:
            result_label=tk.Label(frame, text=error,bg='#9FD5C7',font=16)
            result_label.place(relx=0.3,rely=0.75,height=50)
        window_for_update.after(1000, lambda: window_for_update.destroy())

    def show_people_window(self):
        window_for_show=tk.Tk()
        canvas=tk.Canvas(window_for_show,height=700,width=800)
        canvas.pack()
        frame=tk.Frame(window_for_show,bg='#9FD5C7')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        label=tk.Label(frame, text='Show People',bg='#9FD5C7',font=28)
        label.place(relx=0.395,rely=0.01,height=100)
        result=self._personService.get_all()
        y=0.1
        for i in result:
            person_label=tk.Label(frame,bg='#9FD5C7',text=str(i),font=12)
            y=y+0.065
            person_label.place(relx=0.25,rely=y,height=50)

    def menu_2(self):
        window1=tk.Tk()
        canvas=tk.Canvas(window1,height=700,width=800)
        canvas.pack()
        frame=tk.Frame(window1,bg='#9FD5C7')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        label=tk.Label(frame, text='Manage the list of activities.',bg='#9FD5C7',font=28)
        label.place(relx=0.36,rely=0.01,height=100)
        button1=tk.Button(frame, text='1. Add activity.',font=18,bg='black',fg='white',command=lambda:self.add_activity_window()) 
        button1.place(relx=0.4, rely=0.2,height=50)
        button2=tk.Button(frame, text='2. Remove activity.',font=18,bg='black',fg='white',command=lambda:self.remove_activity_window()) 
        button2.place(relx=0.375, rely=0.35,height=50)
        button3=tk.Button(frame, text='3. Update activity.',font=18,bg='black',fg='white',command=lambda:self.update_activity_window()) 
        button3.place(relx=0.385, rely=0.50,height=50)
        button4=tk.Button(frame, text='4. Show activities.',font=18,bg='black',fg='white',command=lambda:self.show_activities()) 
        button4.place(relx=0.4, rely=0.65,height=50)
        button5=tk.Button(frame, text='5. Back to main menu.',font=18,bg='black',fg='white',command=lambda:self.close_window(window1)) 
        button5.place(relx=0.36, rely=0.8,height=50)

    def add_activity_window(self):
        window_for_add=tk.Tk()
        canvas=tk.Canvas(window_for_add,height=700,width=800)
        canvas.pack()
        frame=tk.Frame(window_for_add,bg='#9FD5C7')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        label=tk.Label(frame, text='Add activity',bg='#9FD5C7',font=28)
        label.place(relx=0.395,rely=0.01,height=100)
        id_label=tk.Label(frame, text='Enter the ID:',bg='#9FD5C7',font=16)
        id_label.place(relx=0.2,rely=0.2)
        id_entry=tk.Entry(frame,width=30,bg='white')
        id_entry.place(relx=0.5,rely=0.2,height=30)
        personIDs_label=tk.Label(frame, text='Enter the person IDs:',bg='#9FD5C7',font=16)
        personIDs_label.place(relx=0.2,rely=0.3)
        personIDs_entry=tk.Entry(frame,width=30,bg='white')
        personIDs_entry.place(relx=0.5,rely=0.3,height=30)
        date_label=tk.Label(frame, text='Enter the date:',bg='#9FD5C7',font=16)
        date_label.place(relx=0.2,rely=0.4)
        date_entry=tk.Entry(frame,width=30,bg='white')
        date_entry.place(relx=0.5,rely=0.4,height=30)
        time_label=tk.Label(frame, text='Enter the time:',bg='#9FD5C7',font=16)
        time_label.place(relx=0.2,rely=0.5)
        time_entry=tk.Entry(frame,width=30,bg='white')
        time_entry.place(relx=0.5,rely=0.5,height=30)
        description_label=tk.Label(frame, text='Enter the decription:',bg='#9FD5C7',font=16)
        description_label.place(relx=0.2,rely=0.6)
        description_entry=tk.Entry(frame,width=30,bg='white')
        description_entry.place(relx=0.5,rely=0.6,height=30)
        button=tk.Button(frame,text='Submit.',font=18,bg='black',fg='white',command=lambda:self.add_activity_ui(window_for_add,frame,id_entry.get(),personIDs_entry.get(),date_entry.get(),time_entry.get(),description_entry.get()))
        button.place(relx=0.4,rely=0.8,height=50)

    def add_activity_ui(self,window_for_add,frame,activityID,list_of_personIDs,date,time,description):
        try:
            list_of_personIDs=list_of_personIDs.split(',')
            self._activityService.add_activity(activityID,list_of_personIDs,date,time,description)
            result_label=tk.Label(frame, text='Activity added!',bg='#9FD5C7',font=16)
            result_label.place(relx=0.36,rely=0.8,height=50)
        except Exception as error:
            result_label=tk.Label(frame, text=error,bg='#9FD5C7',font=16)
            result_label.place(relx=0.3,rely=0.8,height=50)
        window_for_add.after(1000, lambda: window_for_add.destroy())

    def remove_activity_window(self):
        window_for_remove=tk.Tk()
        canvas=tk.Canvas(window_for_remove,height=700,width=800)
        canvas.pack()
        frame=tk.Frame(window_for_remove,bg='#9FD5C7')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        label=tk.Label(frame, text='Remove Activities',bg='#9FD5C7',font=28)
        label.place(relx=0.395,rely=0.01,height=100)
        id_label=tk.Label(frame, text='Enter the ID:',bg='#9FD5C7',font=16)
        id_label.place(relx=0.2,rely=0.2)
        id_entry=tk.Entry(frame,width=30,bg='white')
        id_entry.place(relx=0.5,rely=0.2,height=30)
        button=tk.Button(frame,text='Submit.',font=18,bg='black',fg='white',command=lambda:self.remove_activity_ui(window_for_remove,frame,id_entry.get()))
        button.place(relx=0.4,rely=0.4,height=50)

    def remove_activity_ui(self,window_for_remove,frame,activityID):
        try:
            self._activityService.remove_by_id(activityID)
            result_label=tk.Label(frame, text='Activity removed!',bg='#9FD5C7',font=16)
            result_label.place(relx=0.36,rely=0.7,height=50)
        except Exception as error:
            result_label=tk.Label(frame, text=error,bg='#9FD5C7',font=16)
            result_label.place(relx=0.2,rely=0.7,height=50)
        window_for_remove.after(1000, lambda: window_for_remove.destroy())

    def update_activity_window(self):
        window_for_update=tk.Tk()
        canvas=tk.Canvas(window_for_update,height=700,width=800)
        canvas.pack()
        frame=tk.Frame(window_for_update,bg='#9FD5C7')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        label=tk.Label(frame, text='Update Activity',bg='#9FD5C7',font=28)
        label.place(relx=0.395,rely=0.01,height=100)
        id_label=tk.Label(frame, text='Enter the ID:',bg='#9FD5C7',font=16)
        id_label.place(relx=0.2,rely=0.2)
        id_entry=tk.Entry(frame,width=30,bg='white')
        id_entry.place(relx=0.5,rely=0.2,height=30)
        personIDs_label=tk.Label(frame, text='Enter the person IDs:',bg='#9FD5C7',font=16)
        personIDs_label.place(relx=0.2,rely=0.3)
        personIDs_entry=tk.Entry(frame,width=30,bg='white')
        personIDs_entry.place(relx=0.5,rely=0.3,height=30)
        date_label=tk.Label(frame, text='Enter the date:',bg='#9FD5C7',font=16)
        date_label.place(relx=0.2,rely=0.4)
        date_entry=tk.Entry(frame,width=30,bg='white')
        date_entry.place(relx=0.5,rely=0.4,height=30)
        time_label=tk.Label(frame, text='Enter the time:',bg='#9FD5C7',font=16)
        time_label.place(relx=0.2,rely=0.5)
        time_entry=tk.Entry(frame,width=30,bg='white')
        time_entry.place(relx=0.5,rely=0.5,height=30)
        description_label=tk.Label(frame, text='Enter the decription:',bg='#9FD5C7',font=16)
        description_label.place(relx=0.2,rely=0.6)
        description_entry=tk.Entry(frame,width=30,bg='white')
        description_entry.place(relx=0.5,rely=0.6,height=30)
        button=tk.Button(frame,text='Submit.',font=18,bg='black',fg='white',command=lambda:self.update_activity_ui(window_for_update,frame,id_entry.get(),personIDs_entry.get(),date_entry.get(),time_entry.get(),description_entry.get()))
        button.place(relx=0.4,rely=0.8,height=50)

    def update_activity_ui(self,window_for_update,frame,activityID,list_of_personIDs,date,time,description):
        try:
            list_of_personIDs=list_of_personIDs.split(',')
            self._activityService.update_activity(activityID,list_of_personIDs,date,time,description)
            result_label=tk.Label(frame, text='Activity updated!',bg='#9FD5C7',font=16)
            result_label.place(relx=0.36,rely=0.8,height=50)
        except Exception as error:
            result_label=tk.Label(frame, text=error,bg='#9FD5C7',font=16)
            result_label.place(relx=0.3,rely=0.8,height=50)
        window_for_update.after(1000, lambda: window_for_update.destroy())

    def show_activities(self):
        window_for_show=tk.Tk()
        canvas=tk.Canvas(window_for_show,height=700,width=1500)
        canvas.pack()
        frame=tk.Frame(window_for_show,bg='#9FD5C7')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        label=tk.Label(frame, text='Show Activities',bg='#9FD5C7',font=28)
        label.place(relx=0.395,rely=0.01,height=100)
        result=self._activityService.get_all()
        y=0.1
        for i in result:
            activity_label=tk.Label(frame,bg='#9FD5C7',text=str(i.activityID)+'  '+str(i.personID).ljust(90)+'  '+str(i.date)+'  '+str(i.time)+'  '+str(i.description),font=11)
            y=y+0.065
            activity_label.place(relx=0.05,rely=y,height=50)
    
    def menu_3(self):
        window1=tk.Tk()
        canvas=tk.Canvas(window1,height=800,width=800)
        canvas.pack()
        frame=tk.Frame(window1,bg='#9FD5C7')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        label=tk.Label(frame, text='Search for people or activities.',bg='#9FD5C7',font=28)
        label.place(relx=0.3,rely=0.01,height=100)
        button1=tk.Button(frame, text='1. Search for people by name.',font=18,bg='black',fg='white',command=lambda:self.search_people_by_name()) 
        button1.place(relx=0.3, rely=0.2,height=50)
        button2=tk.Button(frame, text='2. Search for people by phone number.',font=18,bg='black',fg='white',command=lambda:self.search_people_by_phoneNo()) 
        button2.place(relx=0.25, rely=0.3,height=50)
        button3=tk.Button(frame, text='3. Search for activities by date.',font=18,bg='black',fg='white',command=lambda:self.search_activities_by_date()) 
        button3.place(relx=0.3, rely=0.4,height=50)
        button4=tk.Button(frame, text='4. Search for activities by time.',font=18,bg='black',fg='white',command=lambda:self.search_activities_by_time()) 
        button4.place(relx=0.3, rely=0.5,height=50)
        button4=tk.Button(frame, text='5. Search for activities by description.',font=18,bg='black',fg='white',command=lambda:self.search_activities_by_description()) 
        button4.place(relx=0.26, rely=0.6,height=50)
        button5=tk.Button(frame, text='6. Back to main menu.',font=18,bg='black',fg='white',command=lambda:self.close_window(window1)) 
        button5.place(relx=0.36, rely=0.7,height=50)

    def search_people_by_name(self):
        window_for_show=tk.Tk()
        canvas=tk.Canvas(window_for_show,height=1000,width=800)
        canvas.pack()
        frame=tk.Frame(window_for_show,bg='#9FD5C7')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        label=tk.Label(frame, text='Search poeople by name.',bg='#9FD5C7',font=28)
        label.place(relx=0.395,rely=0.01,height=100)
        name_label=tk.Label(frame, text='Enter the name:',bg='#9FD5C7',font=16)
        name_label.place(relx=0.2,rely=0.2)
        name_entry=tk.Entry(frame,width=30,bg='white')
        name_entry.place(relx=0.5,rely=0.2,height=30)
        button=tk.Button(frame,text='Submit.',font=18,bg='black',fg='white',command=lambda:self.search_people_by_name_ui(window_for_show,frame,name_entry.get()))
        button.place(relx=0.4,rely=0.3,height=50)

    def search_people_by_name_ui(self,window_for_show,frame,name):
        try:
            result=self._personService.find_people_by_name(name)
            y=0.4
            for i in result:
                person_label=tk.Label(frame,bg='#9FD5C7',text=str(i),font=8)
                y=y+0.055
                person_label.place(relx=0.2,rely=y,height=50)
        except Exception as error:
            result_label=tk.Label(frame, text=error,bg='#9FD5C7',font=16)
            result_label.place(relx=0.3,rely=0.8,height=50)
            window_for_show.after(1000, lambda: window_for_show.destroy())
        window_for_show.after(10000, lambda: window_for_show.destroy())

    def search_people_by_phoneNo(self):
        window_for_show=tk.Tk()
        canvas=tk.Canvas(window_for_show,height=1000,width=800)
        canvas.pack()
        frame=tk.Frame(window_for_show,bg='#9FD5C7')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        label=tk.Label(frame, text='Search poeople by phone number.',bg='#9FD5C7',font=28)
        label.place(relx=0.35,rely=0.01,height=100)
        phoneNo_label=tk.Label(frame, text='Enter the phoneNo:',bg='#9FD5C7',font=16)
        phoneNo_label.place(relx=0.2,rely=0.2)
        phoneNo_entry=tk.Entry(frame,width=30,bg='white')
        phoneNo_entry.place(relx=0.5,rely=0.2,height=30)
        button=tk.Button(frame,text='Submit.',font=18,bg='black',fg='white',command=lambda:self.search_people_by_phoneNo_ui(window_for_show,frame,phoneNo_entry.get()))
        button.place(relx=0.4,rely=0.3,height=50)

    def search_people_by_phoneNo_ui(self,window_for_show,frame,phoneNo):
        try:
            result=self._personService.find_people_by_phoneNo(phoneNo)
            y=0.4
            for i in result:
                person_label=tk.Label(frame,bg='#9FD5C7',text=str(i),font=8)
                y=y+0.055
                person_label.place(relx=0.2,rely=y,height=50)
        except Exception as error:
            result_label=tk.Label(frame, text=error,bg='#9FD5C7',font=16)
            result_label.place(relx=0.3,rely=0.8,height=50)
            window_for_show.after(1000, lambda: window_for_show.destroy())
        window_for_show.after(10000, lambda: window_for_show.destroy())

    def search_activities_by_date(self):
        window_for_show=tk.Tk()
        canvas=tk.Canvas(window_for_show,height=1300,width=1500)
        canvas.pack()
        frame=tk.Frame(window_for_show,bg='#9FD5C7')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        label=tk.Label(frame, text='Search activities by date.',bg='#9FD5C7',font=28)
        label.place(relx=0.365,rely=0.01,height=100)
        date_label=tk.Label(frame, text='Enter the date:',bg='#9FD5C7',font=16)
        date_label.place(relx=0.2,rely=0.2)
        date_entry=tk.Entry(frame,width=30,bg='white')
        date_entry.place(relx=0.5,rely=0.2,height=30)
        button=tk.Button(frame,text='Submit.',font=18,bg='black',fg='white',command=lambda:self.search_activities_by_date_ui(window_for_show,frame,date_entry.get()))
        button.place(relx=0.4,rely=0.3,height=50)

    def search_activities_by_date_ui(self,window_for_show,frame,date):
        try:
            result=self._activityService.find_activities_by_date(date)
            y=0.4
            for i in result:
                activity_label=tk.Label(frame,bg='#9FD5C7',text=str(i.activityID)+'  '+str(i.personID).ljust(90)+'  '+str(i.date)+'  '+str(i.time)+'  '+str(i.description),font=8)
                y=y+0.05
                activity_label.place(relx=0.05,rely=y,height=50)
        except Exception as error:
            result_label=tk.Label(frame, text=error,bg='#9FD5C7',font=16)
            result_label.place(relx=0.35,rely=0.55,height=50)
            window_for_show.after(1000, lambda: window_for_show.destroy())
        window_for_show.after(10000, lambda: window_for_show.destroy())

    def search_activities_by_time(self):
        window_for_show=tk.Tk()
        canvas=tk.Canvas(window_for_show,height=1300,width=1500)
        canvas.pack()
        frame=tk.Frame(window_for_show,bg='#9FD5C7')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        label=tk.Label(frame, text='Search activities by time.',bg='#9FD5C7',font=28)
        label.place(relx=0.365,rely=0.01,height=100)
        time_label=tk.Label(frame, text='Enter the time:',bg='#9FD5C7',font=16)
        time_label.place(relx=0.2,rely=0.2)
        time_entry=tk.Entry(frame,width=30,bg='white')
        time_entry.place(relx=0.5,rely=0.2,height=30)
        button=tk.Button(frame,text='Submit.',font=18,bg='black',fg='white',command=lambda:self.search_activities_by_time_ui(window_for_show,frame,time_entry.get()))
        button.place(relx=0.4,rely=0.3,height=50)

    def search_activities_by_time_ui(self,window_for_show,frame,time):
        try:
            result=self._activityService.find_activities_by_time(time)
            y=0.4
            for i in result:
                activity_label=tk.Label(frame,bg='#9FD5C7',text=str(i.activityID)+'  '+str(i.personID).ljust(90)+'  '+str(i.date)+'  '+str(i.time)+'  '+str(i.description),font=8)
                y=y+0.05
                activity_label.place(relx=0.05,rely=y,height=50)
        except Exception as error:
            result_label=tk.Label(frame, text=error,bg='#9FD5C7',font=16)
            result_label.place(relx=0.35,rely=0.55,height=50)
            window_for_show.after(1000, lambda: window_for_show.destroy())
        window_for_show.after(10000, lambda: window_for_show.destroy())


    def search_activities_by_description(self):
        window_for_show=tk.Tk()
        canvas=tk.Canvas(window_for_show,height=1300,width=1500)
        canvas.pack()
        frame=tk.Frame(window_for_show,bg='#9FD5C7')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        label=tk.Label(frame, text='Search activities by description.',bg='#9FD5C7',font=28)
        label.place(relx=0.365,rely=0.01,height=100)
        description_label=tk.Label(frame, text='Enter the description:',bg='#9FD5C7',font=16)
        description_label.place(relx=0.2,rely=0.2)
        description_entry=tk.Entry(frame,width=30,bg='white')
        description_entry.place(relx=0.5,rely=0.2,height=30)
        button=tk.Button(frame,text='Submit.',font=18,bg='black',fg='white',command=lambda:self.search_activities_by_description_ui(window_for_show,frame,description_entry.get()))
        button.place(relx=0.4,rely=0.3,height=50)

    def search_activities_by_description_ui(self,window_for_show,frame,description):
        try:
            result=self._activityService.find_activities_by_description(description)
            y=0.4
            for i in result:
                activity_label=tk.Label(frame,bg='#9FD5C7',text=str(i.activityID)+'  '+str(i.personID).ljust(90)+'  '+str(i.date)+'  '+str(i.time)+'  '+str(i.description),font=8)
                y=y+0.05
                activity_label.place(relx=0.05,rely=y,height=50)
        except Exception as error:
            result_label=tk.Label(frame, text=error,bg='#9FD5C7',font=16)
            result_label.place(relx=0.35,rely=0.55,height=50)
            window_for_show.after(1000, lambda: window_for_show.destroy())
        window_for_show.after(10000, lambda: window_for_show.destroy())

    def menu_4(self):
        window1=tk.Tk()
        canvas=tk.Canvas(window1,height=800,width=800)
        canvas.pack()
        frame=tk.Frame(window1,bg='#9FD5C7')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        label=tk.Label(frame, text='Search for people or activities.',bg='#9FD5C7',font=28)
        label.place(relx=0.3,rely=0.01,height=100)
        button1=tk.Button(frame, text='1. Activites for a  given date.',font=18,bg='black',fg='white',command=lambda:self.stat_activities_for_given_date()) 
        button1.place(relx=0.3, rely=0.2,height=50)
        button2=tk.Button(frame, text='2. Busiest days.',font=18,bg='black',fg='white',command=lambda:self.stat_busiest_days()) 
        button2.place(relx=0.38, rely=0.3,height=50)
        button3=tk.Button(frame, text='3. Activities with a given person.',font=18,bg='black',fg='white',command=lambda:self.stat_activities_for_given_person()) 
        button3.place(relx=0.28, rely=0.4,height=50)
        button5=tk.Button(frame, text='4. Back to main menu.',font=18,bg='black',fg='white',command=lambda:self.close_window(window1)) 
        button5.place(relx=0.34, rely=0.5,height=50)

    def stat_activities_for_given_date(self):
        window_for_show=tk.Tk()
        canvas=tk.Canvas(window_for_show,height=1300,width=1500)
        canvas.pack()
        frame=tk.Frame(window_for_show,bg='#9FD5C7')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        label=tk.Label(frame, text='Activities for a given date',bg='#9FD5C7',font=28)
        label.place(relx=0.3,rely=0.01,height=100)
        date_label=tk.Label(frame, text='Enter the date:',bg='#9FD5C7',font=16)
        date_label.place(relx=0.2,rely=0.2)
        date_entry=tk.Entry(frame,width=30,bg='white')
        date_entry.place(relx=0.5,rely=0.2,height=30)
        button=tk.Button(frame,text='Submit.',font=18,bg='black',fg='white',command=lambda:self.stat_activities_for_given_date_ui(window_for_show,frame,date_entry.get()))
        button.place(relx=0.4,rely=0.3,height=50)

    def stat_activities_for_given_date_ui(self,window_for_show,frame,date):
        try:
            y=0.4
            result=self._activityService.stat_activities_for_given_date(date)
            for i in result:
                activity_label=tk.Label(frame,bg='#9FD5C7',text=str(i.activityID)+'  '+str(i.personID).ljust(90)+'  '+str(i.date)+'  '+str(i.time)+'  '+str(i.description),font=8)
                y=y+0.05
                activity_label.place(relx=0.05,rely=y,height=50)
        except Exception as error:
            result_label=tk.Label(frame, text=error,bg='#9FD5C7',font=16)
            result_label.place(relx=0.35,rely=0.55,height=50)
            window_for_show.after(1000, lambda: window_for_show.destroy())
        window_for_show.after(10000, lambda: window_for_show.destroy())

    def stat_busiest_days(self):
        window_for_show=tk.Tk()
        canvas=tk.Canvas(window_for_show,height=1500,width=1500)
        canvas.pack()
        frame=tk.Frame(window_for_show,bg='#9FD5C7')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        label=tk.Label(frame, text='Show busiest days',bg='#9FD5C7',font=28)
        label.place(relx=0.395,rely=0.01,height=100)
        result=self._activityService.stat_busiest_days()
        y=0.15
        for i in result:
            date_label=tk.Label(frame,bg='#9FD5C7',text=i[0].date+":",font=8)
            date_label.place(relx=0.4,rely=y,height=30)
            y=y+0.065
            for j in i:
                activity_label=tk.Label(frame,bg='#9FD5C7',text=str(j.activityID)+'  '+str(j.personID).ljust(90)+'  '+str(j.date)+'  '+str(j.time)+'  '+str(j.description),font=11)
                activity_label.place(relx=0.05,rely=y,height=30)
                y=y+0.065
 
    def stat_activities_for_given_person(self):
        window_for_show=tk.Tk()
        canvas=tk.Canvas(window_for_show,height=1300,width=1500)
        canvas.pack()
        frame=tk.Frame(window_for_show,bg='#9FD5C7')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        label=tk.Label(frame, text='Activities for a given person',bg='#9FD5C7',font=28)
        label.place(relx=0.3,rely=0.01,height=100)
        person_label=tk.Label(frame, text='Enter the person:',bg='#9FD5C7',font=16)
        person_label.place(relx=0.2,rely=0.2)
        person_entry=tk.Entry(frame,width=30,bg='white')
        person_entry.place(relx=0.5,rely=0.2,height=30)
        button=tk.Button(frame,text='Submit.',font=18,bg='black',fg='white',command=lambda:self.stat_activities_for_given_person_ui(window_for_show,frame,person_entry.get()))
        button.place(relx=0.4,rely=0.3,height=50)

    def stat_activities_for_given_person_ui(self,window_for_show,frame,person):
        try:
            y=0.4
            result=self._activityService.stat_activities_for_given_person(person)
            for i in result:
                activity_label=tk.Label(frame,bg='#9FD5C7',text=str(i.activityID)+'  '+str(i.personID).ljust(90)+'  '+str(i.date)+'  '+str(i.time)+'  '+str(i.description),font=8)
                y=y+0.05
                activity_label.place(relx=0.05,rely=y,height=50)
        except Exception as error:
            result_label=tk.Label(frame, text=error,bg='#9FD5C7',font=16)
            result_label.place(relx=0.28,rely=0.55,height=50)
            window_for_show.after(1000, lambda: window_for_show.destroy())
        window_for_show.after(10000, lambda: window_for_show.destroy())

    def undo(self):
        window_for_undo=tk.Tk()
        canvas=tk.Canvas(window_for_undo,height=200,width=500)
        canvas.pack()
        frame=tk.Frame(window_for_undo,bg='#9FD5C7')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        try:
            self.undo_controller.undo()
            message_label=tk.Label(frame,bg='#9FD5C7',text='Operation undone!',font=28)
            message_label.place(relx=0.38,rely=0.2,height=50)
        except Exception as error:
            message_label=tk.Label(frame,bg='#9FD5C7',text=error,font=28)
            message_label.place(relx=0.38,rely=0.2,height=50)
        window_for_undo.after(700, lambda: window_for_undo.destroy())

    def redo(self):
        window_for_redo=tk.Tk()
        canvas=tk.Canvas(window_for_redo,height=200,width=500)
        canvas.pack()
        frame=tk.Frame(window_for_redo,bg='#9FD5C7')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        try:
            self.undo_controller.redo()
            message_label=tk.Label(frame,bg='#9FD5C7',text='Operation redone!',font=28)
            message_label.place(relx=0.38,rely=0.2,height=50)
        except Exception as error:
            message_label=tk.Label(frame,bg='#9FD5C7',text=error,font=28)
            message_label.place(relx=0.38,rely=0.2,height=50)
        window_for_redo.after(700, lambda: window_for_redo.destroy())
'''   
main_window=tk.Tk()
undo_controller=UndoController()
pServ=PService(undo_controller)
aServ=AService(pServ._repo,undo_controller)
gui=GUI(main_window,pServ,aServ,undo_controller)
gui.main_window.mainloop()
'''