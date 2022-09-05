print("Hello! Choose the UI you want to use:")
print("1.menubased interface")   
print("2.command-based interface")
choice=input(">")
if choice=='1':
    from uimenu import*
elif choice=='2':
    from uiconsolebased import*
start()