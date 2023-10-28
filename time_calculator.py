def add_time(start, duration, starting_day=""):

  start_nospace = start.split()
  start_format = start_nospace[1] #This is the AM or PM
  
  start_nodots = start_nospace[0].split(":")
  start_hour = int(start_nodots[0]) 
  start_minutes = int(start_nodots[1])

  duration_nodots = duration.split(":")
  duration_hours = int(duration_nodots[0])
  duration_minutes = int(duration_nodots[1])

  if start_format == "PM" and start_hour != 12:
    start_hour += 12
  elif start_format == "AM" and start_hour == 12:
    start_hour = 0

  total_hours = start_hour + duration_hours
  finish_minutes = start_minutes + duration_minutes
  if finish_minutes >= 60:
    finish_minutes -= 60
    total_hours += 1
  # Minutes done.

  finish_hours = total_hours % 24
  counting_days = (total_hours*60 + finish_minutes) // 1440 #Integer division floor
  # days = total minutes / minutes in a day
  finish_format = ""

  if finish_hours < 12:
    finish_format = "AM"
    if finish_hours == 0:
      finish_hours = 12
  else:
    finish_format = "PM"
    if finish_hours != 12:
      finish_hours -= 12
  # Hours done.

  finish_days_string = ""
  
  if counting_days == 1:
    finish_days_string = " (next day)"
  elif counting_days > 1:
    finish_days_string = " (" + str(counting_days) + " days later)"

  days_of_week_lc = ["monday", "tuesday", "wednesday", "thursday", 
                     "friday", "saturday", "sunday"]
  days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", 
                  "Friday", "Saturday", "Sunday"]
  if starting_day != "":
    finish_day_index = (days_of_week_lc.index(starting_day.lower()) + counting_days) % 7
    finish_day = days_of_week[finish_day_index]
    finish_days_string = ", " + finish_day + finish_days_string
    
  finish_minutes_string = str(finish_minutes)
  if finish_minutes < 10:
    finish_minutes_string = "0" + finish_minutes_string
  
  new_time = str(finish_hours) + ":" + finish_minutes_string + " " + finish_format + finish_days_string
    
  return new_time