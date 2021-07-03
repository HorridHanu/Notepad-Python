########################################################################################
########################################################################################
## # CODE LANGUAGE IS PYHTON!          ##      ##                                     ##
## # DATE: 1-JULY-2021                 ##      ##   ########   ##          ##     ##  ##
## # CODE BY HANU!                     ##########         ##   #########   ##     ##  ##
## # ONLY FOR EDUCATIONAL PURPOSE!     ##########    #######   ##     ##   ##     ##  ##
## # DATETIME PRINT                    ##      ##    ##   ##   ##     ##   ##     ##  ##
## # ITS ONLY DEMO!                    ##      ##    #######   ##     ##   ########   ##
########################################################################################
########################################################################################


          #IMPORT Datetime MODULE!

from datetime import datetime
now=datetime.now()               #used for current date time!
Time=now.strftime("%H:%M")       #used for time, %H for hour and %M for minute!
Date=now.strftime("%D")          #used for date!
def time_now():
    print(f"{Time}  {Date}")

time_now()