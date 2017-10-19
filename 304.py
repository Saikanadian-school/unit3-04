import ui

def enter_button(sender):
    year = int(view['year_textfield'].text)
    if ((year % 100) == 0):
       if ((year % 400) == 0):
       	view['year_label'].text = ("leap year")
       else:
       	view['year_label'].text = ("not a leap year")
    else:
      if ((year % 4) == 0):
      	 view['year_label'].text = ("Leap year")
      else:
      	view['year_label'].text = ("not a leap year")

view = ui.load_view()
view.present('sheet')
