from datetime import date
import calendar
import datetime

my_day = date.today()
now = datetime.datetime.now()

int_day = my_day.weekday()
today = calendar.day_name[my_day.weekday()]
c_time = now.strftime("%I:%M:%S%p").lower()
c_hour = int(now.strftime("%I"))
c_min = int(now.strftime("%M"))
am_pm = now.strftime("%p")

# print(f"The day is {my_day}")
# print(int_day)
# print(c_hour)
# print(c_min)
# print(am_pm)


# Saturday

if int_day == 5:
    if am_pm == "PM":
        if c_hour == 6 and c_min < 31:
            print(
                f"""
    Today is {today} and the time is {c_time}
            """)
            print(
    """
    ===========The_Previous_Class_Was===========
    Subject Name: Chemistry-1 (65913)
    Room No     : 203
    Time        : 03:30pm - 04:15pm
    Teacher Name: Mr. Mazarul Islam Chowdhury
    
    ==============Running_Class_Is==============
    Subject Name: Unknown (?)
    Room No     : 206
    Time        : 04:15pm - 06:30pm
    Teacher Name: Mr. Y (R.S)
    
    =============Next_Class_Will_Be=============           
    It is the last class for Today.
    The class will end at 06:30pm
    """)
        elif c_hour >= 6 and c_hour != 12:
            print(
                f"""
    Today is "{today}" and the time is {c_time}
            """)
            print(
    """
    There are no more classes today
    The Last Class Ended at 06:30pm
    """)

        elif c_hour == 5 and c_min >= 0:
            print(
                f"""
    Today is {today} and the time is {c_time}
            """)
            print(
    """
    ===========The_Previous_Class_Was===========
    Subject Name: Chemistry-1 (65913)
    Room No     : 100-A
    Time        : 03:30pm - 04:15pm
    Teacher Name: Mr. Mazarul Islam Chowdhury
    
    ==============Running_Class_Is==============
    Subject Name: Unknown (?)
    Room No     : 206
    Time        : 04:15pm - 06:30pm
    Teacher Name: Mr. Y (R.S)
    
    =============Next_Class_Will_Be=============           
    It is the last class for Today.
    The class will end at 06:30pm
    """)
        elif c_hour == 4 and c_min >= 15:
            print(
                f"""
    Today is {today} and the time is {c_time}
            """)
            print(
    """
    ===========The_Previous_Class_Was===========
    Subject Name: Chemistry-1 (65913)
    Room No     : 100-A
    Time        : 03:30pm - 04:15pm
    Teacher Name: Mr. Mazarul Islam Chowdhury
    ==============Running_Class_Is==============
    Subject Name: Unknown (?)
    Room No     : 206
    Time        : 04:15pm - 06:30pm
    Teacher Name: Mr. Y (R.S)
    =============Next_Class_Will_Be=============           
    It is the last class for Today.
    The class will end at 06:30pm
    """)
        elif c_hour == 4 and c_min < 15:
            print(
                f"""
    Today is {today} and the time is {c_time}
            """)
            print(
    """
    ===========The_Previous_Class_Was===========
    Subject Name: Programming Essentials (66631)
    Room No     : 203
    Time        : 02:00pm - 03:30pm
    Teacher Name: Mr. Aminur Rahman.
    ==============Running_Class_Is==============
    Subject Name: Chemistry-1 (65913)
    Room No     : 100-A
    Time        : 03:30pm - 04:15pm
    Teacher Name: Mr. Mazarul Islam Chowdhury
    =============Next_Class_Will_Be=============           
    Subject Name: Unknown (?)
    Room No     : 206
    Time        : 04:15pm - 06:30pm
    Teacher Name: Mr. Y (R.S)
    """)
        elif c_hour == 3 and c_min >= 30:
            print(
                f"""
    Today is {today} and the time is {c_time}
            """)
            print(
    """
    ===========The_Previous_Class_Was===========
    Subject Name: Programming Essentials (66631)
    Room No     : 203
    Time        : 02:00pm - 03:30pm
    Teacher Name: Mr. Aminur Rahman.
    ==============Running_Class_Is==============
    Subject Name: Chemistry-1 (65913)
    Room No     : 100-A
    Time        : 03:30pm - 04:15pm
    Teacher Name: Mr. Mazarul Islam Chowdhury.
    =============Next_Class_Will_Be=============           
    Subject Name: Unknown (?)
    Room No     : 206
    Time        : 04:15pm - 06:30pm
    Teacher Name: Mr. Y (R.S)
    """)
        elif c_hour == 3 and c_min < 30:
            print(
                f"""
    Today is {today} and the time is {c_time}. 
            """)
            print(
    """
    ===========The_Previous_Class_Was===========
    Subject Name: Mathmatics-3 (65931)
    Room No     : 203
    Time        : 01:15pm - 02:00pm
    Teacher Name: Mr. Hasmut ullah Sajib.
    
    ==============Running_Class_Is==============
    Subject Name: Programming Essentials (66631)
    Room No     : 203
    Time        : 02:00pm - 03:30pm
    Teacher Name: Mr. Aminur Rahman.
    
    =============Next_Class_Will_Be=============           
    Subject Name: Chemistry-1 (65913)
    Room No     : 100-A
    Time        : 03:30pm - 04:15pm
    Teacher Name: Mr. Mazarul Islam Chowdhury
    """)
        elif c_hour == 2 and c_min >= 0:
            print(
                f"""
    Today is {today} and the time is {c_time}
            """)
            print(
    """
    ===========The_Previous_Class_Was===========
    Subject Name: Mathmatics-3 (65931)
    Room No     : 203
    Time        : 01:15pm - 02:00pm
    Teacher Name: Mr. Hasmut ullah Sajib.
    
    ==============Running_Class_Is==============
    Subject Name: Programming Essentials (66631)
    Room No     : 203
    Time        : 02:00pm - 03:30pm
    Teacher Name: Mr. Aminur Rahman.
    
    =============Next_Class_Will_Be=============          
    Subject Name: Chemistry-1 (65913)
    Room No     : 100-A
    Time        : 03:30pm - 04:15pm
    Teacher Name: Mr. Mazarul Islam Chowdhury
    """)
        elif c_hour == 1 and c_min >= 15:
            print(
                f"""
    Today is {today} and the time is {c_time}
            """)
            print(
    """
    ===========The_Previous_Class_Was===========
    ||Subject Name: N/A                       ||
    ============================================
    
    ==============Running_Class_Is==============
    ||Subject Name: Mathmatics-3 (65931)      ||  
    ||Room No     : 203                       ||  
    ||Time        : 01:15pm - 02:00pm         ||  
    ||Teacher Name: Mr. Hasmut ullah Sajib    ||  
    ============================================
     
    =============Next_Class_Will_Be=============
    ||Subject Name: Programming Essentials    ||  
    ||Room No     : 203                       || 
    ||Time        : 02:00pm - 03:30pm         || 
    ||Teacher Name: Mr. Aminur Rahman.        ||
    ============================================
    """)
        elif c_hour == 1 and c_min < 15:
            print(
                f"""
    Today is {today} and the time is {c_time}. 
            """)
            print(
    """
    ============================================
    Class will start very soon at 01:15pm
    Today's first class is Math (65931)
    Room No: 203
    Class will be held form 01:15-02:00pm
    Teacher Name: Mr. Hasmut ullah Sajib
    ============================================
    """)
        elif c_hour == 12 and c_min >= 0:
            print(
                f"""

    ================================================
    ||Today is {today} and the time is {c_time}||
    ================================================
    """)
            print(
    """                        
    ================================================
    ||Classes not started yet                     ||
    ||Today's first class is Math (65931)         ||
    ||And Class will start at 01:15pm             ||
    ||Teacher Name: Mr. Hasmut ullah Sajib.       ||
    ================================================                   
    """)
    else:
        print(
            f"""

    Today is {today} and the time is {c_time}
     ================================================
     ||          There are 4 Classes Today         ||
     ================================================                  
     ||      Subject_Name                 Time     ||
     || 1. Mathmatics-3              1:15pm-2:00pm ||
     || 2. Programming Essentials    2:00pm-3:30pm ||
     || 3. Chemistry-1               3:30pm-4:15pm ||
     || 4. Unknown                   4:15pm-6:30pm || 
     ================================================
    """)


# Sunday

elif int_day == 6:
    if am_pm == "PM":
        if c_hour == 6 and c_min < 31:
            print(
                f"""
    Today is {today} and the time is {c_time}
            """)
            print(
                """
    ===========The_Previous_Class_Was===========
    Subject Name: Social Science (65811)
    Room No     : 101
    Time        : 03:30pm - 04:15pm
    Teacher Name: Biplob kumar Sorka
    ==============Running_Class_Is==============
    Subject Name: Web Design (66632)
    Room No     : Application Lab
    Time        : 04:15pm - 06:30pm
    Teacher Name: Mst Mi
    =============Next_Class_Will_Be=============           
    It is the last class for Today.
    The class will end at 06:30pm
    """)
        elif c_hour >= 6 and c_hour != 12:
            print(
                f"""
            Today is "{today}" and the time is {c_time}
            """)
            print(
                """
                There are no more classes today
                The Last Class was ended at 06:30pm
                """)

        elif c_hour == 5 and c_min >= 0:
            print(
                f"""
            Today is {today} and the time is {c_time}
            """)
            print(
                """
                ===========The_Previous_Class_Was===========
                Subject Name: Social Science (65811)
                Room No     : 101
                Time        : 03:30pm - 04:15pm
                Teacher Name: Biplob kumar Sorkar.

                ==============Running_Class_Is==============
                Subject Name: Web Design (66632)
                Room No     : Application Lab
                Time        : 04:15pm - 06:30pm
                Teacher Name: Mst Mim.

                =============Next_Class_Will_Be=============           
                It is the last class for Today.
                The class will end at 06:30pm
                """)
        elif c_hour == 4 and c_min >= 15:
            print(
                f"""
            Today is {today} and the time is {c_time}
            """)
            print(
                """
                ===========The_Previous_Class_Was===========
                Subject Name: Social Science (65811)
                Room No     : 101
                Time        : 03:30pm - 04:15pm
                Teacher Name: Biplob kumar Sorkar.

                ==============Running_Class_Is==============
                Subject Name: Web Design (66632)
                Room No     : Application Lab
                Time        : 04:15pm - 06:30pm
                Teacher Name: Mst Mim.

                =============Next_Class_Will_Be=============           
                It is the last class for Today.
                The class will end at 06:30pm
                """)
        elif c_hour == 4 and c_min < 15:
            print(
                f"""
            Today is {today} and the time is {c_time}
            """)
            print(
                """
                ===========The_Previous_Class_Was===========
                SSubject Name: Graphics Design-2 (66633)
                Room No     : 102
                Time        : 01:15pm - 03:30pm
                Teacher Name: Humaira Aktar.

                ==============Running_Class_Is==============
                Subject Name: Social Science (65811)
                Room No     : 101
                Time        : 03:31pm - 04:15pm
                Teacher Name: Biplob kumar Sorkar.

                =============Next_Class_Will_Be=============           
                Subject Name: Web Design (66632)
                Room No     : Application Lab
                Time        : 04:15pm - 06:30pm
                Teacher Name: Mst Mim.
                """)
        elif c_hour == 3 and c_min >= 30:
            print(
                f"""
            Today is {today} and the time is {c_time}
            """)
            print(
                """
                ===========The_Previous_Class_Was===========
                Subject Name: Graphics Design-2 (66633)
                Room No     : 102
                Time        : 01:15pm - 03:30pm
                Teacher Name: Humaira Aktar.

                ==============Running_Class_Is==============
                Subject Name: Social Science (65811)
                Room No     : 101
                Time        : 03:31pm - 04:15pm
                Teacher Name: Biplob kumar Sorkar.

                =============Next_Class_Will_Be=============           
                Subject Name: Web Design (66632)
                Room No     : Application Lab
                Time        : 04:15pm - 06:30pm
                Teacher Name: Mst Mim.
                """)
        elif c_hour == 3 and c_min < 30:
            print(
                f"""
            Today is {today} and the time is {c_time}. 
            """)
            print(
                """
                ===========The_Previous_Class_Was===========
                Subject Name: N/A

                ==============Running_Class_Is==============
                Subject Name: Graphics Design-2 (66633)
                Room No     : 102
                Time        : 01:15pm - 03:30pm
                Teacher Name: Humaira Aktar.

                =============Next_Class_Will_Be=============
                Subject Name: Social Science (65811)
                Room No     : 101
                Time        : 03:31pm - 04:15pm
                Teacher Name: Biplob kumar Sorkar.
                """)
        elif c_hour == 2 and c_min >= 0:
            print(
                f"""
            Today is {today} and the time is {c_time}
            """)
            print(
                """
                ===========The_Previous_Class_Was===========
                Subject Name: N/A

                ==============Running_Class_Is==============
                Subject Name: Graphics Design-2 (66633)
                Room No     : 102
                Time        : 01:15pm - 03:30pm
                Teacher Name: Humaira Aktar.

                =============Next_Class_Will_Be=============
                Subject Name: Social Science (65811)
                Room No     : 101
                Time        : 03:31pm - 04:15pm
                Teacher Name: Biplob kumar Sorkar.
                """)
        elif c_hour == 1 and c_min >= 15:
            print(
                f"""
            Today is {today} and the time is {c_time}
            """)
            print(
                """
                ===========The_Previous_Class_Was===========
                Subject Name: N/A

                ==============Running_Class_Is==============
                Subject Name: Graphics Design-2 (66633)
                Room No     : 102
                Time        : 01:15pm - 03:30pm
                Teacher Name: Humaira Aktar.

                =============Next_Class_Will_Be=============
                Subject Name: Social Science (65811)
                Room No     : 101
                Time        : 03:31pm - 04:15pm
                Teacher Name: Biplob kumar Sorkar.
                """)
        elif c_hour == 1 and c_min < 15:
            print(
                f"""
                Today is {today} and the time is {c_time}. 
                """)
            print(
                """
                ===================================
                Class will start very soon at 01:15pm
                Today's first class is Graphics Design-2(66633)
                Room No: 102
                Class will be held form 01:15pm - 03:30pm
                Teacher Name: Humaira Aktar.
                ===================================
                """)
        elif c_hour == 12 and c_min >= 0:
            print(
                f"""

                ===================================
                Today is {today} and the time is {c_time}
                """)
            print(
                """                        
                ===================================
                Classes not started yet
                Today's first class is Graphics Design-2 (66633)
                And The class will start at 01:15pm
                Teacher Name: Humaira Aktar.
                ===================================                   
                """)
    else:
        print(
            f"""

    Today is {today} and the time is {c_time}
     ================================================
     ||          There are 3 Classes Today         ||
     ================================================                  
     ||      Subject_Name                 Time     ||
     || 1. Graphics Desing           1:15pm-3:30pm ||
     || 2. Social Science            3:30pm-4:15pm ||
     || 3. Web Design                4:15pm-6:30pm ||  
     ================================================
    """)


# Monday

elif int_day == 0:
    if am_pm == "PM":
        if c_hour == 6 and c_min < 30:
            print(
                f"""
                Today is {today} and the time is {c_time}
            """)
            print(
                """
                ===========The_Previous_Class_Was===========
                Subject Name: It Support System-2 (66^34)
                Room No     : Programming Lab
                Time        : 03:30pm - 05:45pm
                Teacher Name: Taskin Nahar.

                ==============Running_Class_Is==============
                Subject Name: Mathmatics-3 (65931)
                Room No     : 308
                Time        : 05:45pm - 06:30pm
                Teacher Name: Mr. Hasmut Ullah Sajib.

                =============Next_Class_Will_Be=============           
                There are no more classes today.
                Current class will end at 06:30pm
                """)
        elif c_hour >= 6 and c_hour != 12:
            print(
                f"""
            Today is "{today}" and the time is {c_time}
            """)
            print(
                """
                There are no more classes today.
                The Last Class was ended at 06:30pm.
                """)
        elif c_hour == 5 and c_min > 45:
            print(
                f"""
                Today is {today} and the time is {c_time}
                """)
            print(
                """
                ===========The_Previous_Class_Was===========
                Subject Name: It Support System-2 (66^34)
                Room No     : Programming Lab
                Time        : 03:30pm - 05:45pm
                Teacher Name: Taskin Nahar.

                ==============Running_Class_Is==============
                Subject Name: Mathmatics-3 (65931)
                Room No     : 308
                Time        : 05:45pm - 06:30pm
                Teacher Name: Mr. Hasmut Ullah Sajib.

                =============Next_Class_Will_Be=============           
                There are no more classes today.
                Current class will end at 06:30pm
                """)
        elif c_hour == 5 and c_min <= 45:
            print(
                f"""
            Today is {today} and the time is {c_time}
            """)
            print(
                """
                ===========The_Previous_Class_Was===========
                Subject Name: Social Science (65811)
                Room No     : 105
                Time        : 02:45pm - 03:30pm
                Teacher Name: Biplob kumar Sorkar.

                ==============Running_Class_Is==============
                Subject Name: It Support System-2 (66^34)
                Room No     : Programming Lab
                Time        : 03:30pm - 05:45pm
                Teacher Name: Taskin Nahar.

                =============Next_Class_Will_Be=============           
                Subject Name: Mathmatics-3 (65931)
                Room No     : 308
                Time        : 05:45pm - 06:30pm
                Teacher Name: Mr. Hasmut Ullah Sajib.
                """)
        elif c_hour == 4 and c_min >= 0:
            print(
                f"""
            Today is {today} and the time is {c_time}
            """)
            print(
                """
                ===========The_Previous_Class_Was===========
                Subject Name: Social Science (65811)
                Room No     : 105
                Time        : 02:45pm - 03:30pm
                Teacher Name: Biplob kumar Sorkar.

                ==============Running_Class_Is==============
                Subject Name: It Support System-2 (66^34)
                Room No     : Programming Lab
                Time        : 03:30pm - 05:45pm
                Teacher Name: Taskin Nahar.

                =============Next_Class_Will_Be=============           
                Subject Name: Mathmatics-3 (65931)
                Room No     : 308
                Time        : 05:45pm - 06:30pm
                Teacher Name: Mr. Hasmut Ullah Sajib
                """)
        elif c_hour == 3 and c_min >= 30:
            print(
                f"""
            Today is {today} and the time is {c_time}
            """)
            print(
                """
                ===========The_Previous_Class_Was===========
                Subject Name: Social Science (65811)
                Room No     : 105
                Time        : 02:45pm - 03:30pm
                Teacher Name: Biplob kumar Sorkar.

                ==============Running_Class_Is==============
                Subject Name: It Support System-2 (66^34)
                Room No     : Programming Lab
                Time        : 03:30pm - 05:45pm
                Teacher Name: Taskin Nahar.

                =============Next_Class_Will_Be=============           
                Subject Name: Mathmatics-3 (65931)
                Room No     : 308
                Time        : 05:45pm - 06:30pm
                Teacher Name: Mr. Hasmut Ullah Sajib
                """)
        elif c_hour == 3 and c_min < 30:
            print(
                f"""
                Today is {today} and the time is {c_time}. 
                """)
            print(
                """
                ===========The_Previous_Class_Was===========
                Subject Name: Chemistry-1 (65913)
                Room No     : 105
                Time        : 02:00pm - 02:45pm
                Teacher Name: Mr. Mazarul Islam Chowdhury.

                ==============Running_Class_Is==============
                Subject Name: Social Science (65811)
                Room No     : 105
                Time        : 02:45pm - 03:30pm
                Teacher Name: Biplob kumar Sorkar.

                =============Next_Class_Will_Be=============
                Subject Name: It Support System-2 (66634)
                Room No     : Programming Lab
                Time        : 03:30pm - 05:45pm
                Teacher Name: Taskin Nahar.
                """)
        elif c_hour == 2 and c_min >= 45:
            print(
                f"""
                Today is {today} and the time is {c_time}
                 """)
            print(
                """
                ===========The_Previous_Class_Was===========
                Subject Name: Chemistry-1 (65913)
                Room No     : 105
                Time        : 02:00pm - 02:45pm
                Teacher Name: Mr. Mazarul Islam Chowdhury.

                ==============Running_Class_Is==============
                Subject Name: Social Science (65811)
                Room No     : 105
                Time        : 02:45pm - 03:30pm
                Teacher Name: Biplob kumar Sorkar.

                =============Next_Class_Will_Be=============
                Subject Name: It Support System-2 (66^34)
                Room No     : Programming Lab
                Time        : 03:30pm - 05:45pm
                Teacher Name: Taskin Nahar.
                """)
        elif c_hour == 2 and c_min < 45:
            print(
                f"""
            Today is {today} and the time is {c_time}
            """)
            print(
                """
                ===========The_Previous_Class_Was===========
                Subject Name: NIS HOD
                Room No     : N/A
                Time        : 01:15pm - 02:00pm
                Teacher Name: N/A

                ==============Running_Class_Is==============
                Subject Name: Chemistry-1 (65913)
                Room No     : 105
                Time        : 02:00pm - 02:45pm
                Teacher Name: Mr. Mazarul Islam Chowdhury.

                =============Next_Class_Will_Be=============
                Subject Name: Social Science (65811)
                Room No     : 105
                Time        : 02:45pm - 03:30pm
                Teacher Name: Biplob kumar Sorkar.
                """)
        elif c_hour == 1 and c_min >= 15:
            print(
                f"""
            Today is {today} and the time is {c_time}
            """)
            print(
                """
                ===========The_Previous_Class_Was===========
                Subject Name: N/A

                ==============Running_Class_Is==============
                Subject Name: NIS HOD
                Room No     : N/A
                Time        : 01:15pm - 02:00pm
                Teacher Name: N/A

                =============Next_Class_Will_Be=============
                Subject Name: Chemistry-1 (65913)
                Room No     : 105
                Time        : 02:00pm - 02:45pm
                Teacher Name: Mr. Mazarul Islam Chowdhury.
                """)
        elif c_hour == 1 and c_min < 15:
            print(
                f"""
                Today is {today} and the time is {c_time}. 
                """)
            print(
                """
                ===================================
                Class will start very soon at 01:15pm
                Today's first class is "NIS HOD"
                Room No: N/A
                Class will be held form 01:15pm - 02:00pm
                Teacher Name: N/A
                ===================================
                """)
        elif c_hour == 12 and c_min >= 0:
            print(
                f"""

                ===================================
                Today is {today} and the time is {c_time}
                """)
            print(
                """                        
                ===================================
                Classes not started yet
                Today's first class is "NIS HOD"
                And The class will start at 01:15pm
                Teacher Name: N/A
                ===================================                   
                """)
    else:
        print(
            f"""

    Today is {today} and the time is {c_time}
     ================================================
     ||          There are 5 Classes Today         ||
     ================================================                  
     ||      Subject_Name                 Time     ||
     || 1. NIS HOD                   1:15pm-2:00pm ||
     || 2. Chemistry-1               2:00pm-2:45pm ||
     || 3. Social Science            2:45pm-3:30pm ||
     || 4. It Support System-2       3:30pm-5:45pm ||
     || 5. Mathmatics-3              5:45pm-6:30pm ||  
     ================================================
    """)


# Tuesday

elif int_day == 1:
    if am_pm == "PM":
        if c_hour == 6 and c_min < 31:
            print(
                f"""
            Today is {today} and the time is {c_time}
            """)
            print(
                """
                ===========The_Previous_Class_Was===========
                Subject Name: Chemistry-1 (65913)
                Room No     : 105
                Time        : 03:30pm - 04:15pm
                Teacher Name: Mr. Mazarul Islam Chowdhury.

                ==============Running_Class_Is==============
                Subject Name: Graphics Design (66633)
                Room No     : Software Lab
                Time        : 04:15pm - 06:30pm
                Teacher Name: Humaira Aktar.

                =============Next_Class_Will_Be=============           
                It is the last class for Today.
                Current class will end at 06:30pm
                """)
        elif c_hour >= 6 and c_hour != 12:
            print(
                f"""
            Today is "{today}" and the time is {c_time}
            """)
            print(
                """
                There are no more classes today
                The Last Class was ended at 06:30pm
                """)

        elif c_hour == 5 and c_min >= 0:
            print(
                f"""
            Today is {today} and the time is {c_time}
            """)
            print(
                """
                ===========The_Previous_Class_Was===========
                Subject Name: Chemistry-1 (65913)
                Room No     : 105
                Time        : 03:30pm - 04:15pm
                Teacher Name: Mr. Mazarul Islam Chowdhury.

                ==============Running_Class_Is==============
                Subject Name: Graphics Design (66633)
                Room No     : Software Lab
                Time        : 04:15pm - 06:30pm
                Teacher Name: Humaira Aktar.

                =============Next_Class_Will_Be=============           
                It is the last class for Today.
                Current class will end at 06:30pm
                """)
        elif c_hour == 4 and c_min >= 15:
            print(
                f"""
            Today is {today} and the time is {c_time}
            """)
            print(
                """
                ===========The_Previous_Class_Was===========
                Subject Name: Chemistry-1 (65913)
                Room No     : 105
                Time        : 03:30pm - 04:15pm
                Teacher Name: Mr. Mazarul Islam Chowdhury.

                ==============Running_Class_Is==============
                Subject Name: Graphics Design (66633)
                Room No     : Software Lab
                Time        : 04:15pm - 06:30pm
                Teacher Name: Humaira Aktar.

                =============Next_Class_Will_Be=============           
                It is the last class for Today.
                Current class will end at 06:30pm
                """)
        elif c_hour == 4 and c_min < 15:
            print(
                f"""
            Today is {today} and the time is {c_time}
            """)
            print(
                """
                ===========The_Previous_Class_Was===========
                Subject Name: Programming Essentials (66631)
                Room No     : Software Lab
                Time        : 01:15pm - 03:30pm
                Teacher Name: Md. Aminur Rahman.

                ==============Running_Class_Is==============
                Subject Name: Chemistry-1 (65913)
                Room No     : 105
                Time        : 03:30pm - 04:15pm
                Teacher Name: Mr. Mazarul Islam Chowdhury.

                =============Next_Class_Will_Be=============           
                Subject Name: Graphics Design (66633)
                Room No     : Software Lab
                Time        : 04:15pm - 06:30pm
                Teacher Name: Humaira Aktar.
                """)
        elif c_hour == 3 and c_min >= 30:
            print(
                f"""
            Today is {today} and the time is {c_time}
            """)
            print(
                """
                ===========The_Previous_Class_Was===========
                Subject Name: Programming Essentials (66631)
                Room No     : Software Lab
                Time        : 01:15pm - 03:30pm
                Teacher Name: Md. Aminur Rahman.

                ==============Running_Class_Is==============
                Subject Name: Chemistry-1 (65913)
                Room No     : 105
                Time        : 03:30pm - 04:15pm
                Teacher Name: Mr. Mazarul Islam Chowdhury.

                =============Next_Class_Will_Be=============           
                Subject Name: Graphics Design (66633)
                Room No     : Software Lab
                Time        : 04:15pm - 06:30pm
                Teacher Name: Humaira Aktar.
                """)
        elif c_hour == 3 and c_min < 30:
            print(
                f"""
            Today is {today} and the time is {c_time}. 
            """)
            print(
                """
                ===========The_Previous_Class_Was===========
                Subject Name: N/A

                ==============Running_Class_Is==============
                Subject Name: Programming Essentials (66631)
                Room No     : Software Lab
                Time        : 01:15pm - 03:30pm
                Teacher Name: Md. Aminur Rahman.

                =============Next_Class_Will_Be=============
                Subject Name: Chemistry-1 (65913)
                Room No     : 105
                Time        : 03:30pm - 04:15pm
                Teacher Name: Mr. Mazarul Islam Chowdhury.
                """)
        elif c_hour == 2 and c_min >= 0:
            print(
                f"""
            Today is {today} and the time is {c_time}
            """)
            print(
                """
                ===========The_Previous_Class_Was===========
                Subject Name: N/A

                ==============Running_Class_Is==============
                Subject Name: Programming Essentials (66631)
                Room No     : Software Lab
                Time        : 01:15pm - 03:30pm
                Teacher Name: Md. Aminur Rahman.

                =============Next_Class_Will_Be=============
                Subject Name: Chemistry-1 (65913)
                Room No     : 105
                Time        : 03:30pm - 04:15pm
                Teacher Name: Mr. Mazarul Islam Chowdhury.
                """)
        elif c_hour == 1 and c_min >= 15:
            print(
                f"""
            Today is {today} and the time is {c_time}
            """)
            print(
                """
                ===========The_Previous_Class_Was===========
                Subject Name: N/A

                ==============Running_Class_Is==============
                Subject Name: Programming Essentials (66631)
                Room No     : Software Lab
                Time        : 01:15pm - 03:30pm
                Teacher Name: Md. Aminur Rahman.

                =============Next_Class_Will_Be=============
                Subject Name: Chemistry-1 (65913)
                Room No     : 105
                Time        : 03:30pm - 04:15pm
                Teacher Name: Mr. Mazarul Islam Chowdhury.
                """)
        elif c_hour == 1 and c_min < 15:
            print(
                f"""
                Today is {today} and the time is {c_time}. 
                """)
            print(
                """
                ===================================
                Class will start very soon at 01:15pm
                Today's first class is Programming Essentials (66631)
                Room No: Software Lab
                Class will be held form 01:15pm - 03:30pm
                Teacher Name: Mr. Aminur Rahman
                ===================================
                """)
        elif c_hour == 12 and c_min >= 0:
            print(
                f"""

                ===================================
                Today is {today} and the time is {c_time}
                """)
            print(
                """                        
                ===================================
                Classes not started yet
                Today's first class is Programming Essentials (66631)
                And The class will start at 01:15pm
                Teacher Name: Mr. Aminur Rahman
                ===================================                   
                """)
    else:
        print(
            f"""

    Today is {today} and the time is {c_time}
     ================================================
     ||          There are 3 Classes Today         ||
     ================================================                  
     ||      Subject_Name                 Time     ||
     || 1. Programming Essentials    1:15pm-3:30pm ||
     || 2. Chemistry-1               3:30pm-4:15pm ||
     || 3. Graphics Design-2         4:15pm-6:30pm ||  
     ================================================
    """)


# Wednesday

elif int_day == 2:
    if am_pm == "PM":
        if c_hour >= 5 and c_hour != 12 and c_min > 45:
            print(
                f"""
            Today is "{today}" and the time is {c_time}
            """)
            print(
                """
                There are no more classes today
                The Last Class was ended at 06:30pm
                """)

        elif c_hour == 5 and c_min <= 45:
            print(
                f"""
            Today is {today} and the time is {c_time}
            """)
            print(
                """
                ===========The_Previous_Class_Was===========
                Subject     : Period Gap of 45 minutes
                Time        : 04:15pm - 05:00pm

                ==============Running_Class_Is==============
                Subject     : A Cleaning session.
                Room Name   : Software Lab.
                Time        : 05:00pm - 05:45pm

                =============Next_Class_Will_Be=============           
                It is the last class for Today.
                Current session will end at 05:45pm
                """)
        elif c_hour == 4 and c_min >= 15:
            print(
                f"""
            Today is {today} and the time is {c_time}
            """)
            print(
                """
                ===========The_Previous_Class_Was===========
                Subject Name: Social Science (65811)
                Room No     : 105
                Time        : 03:30pm - 04:15pm
                Teacher Name: Mr. Biplob Kumar Sorkar.

                ==============Running_Class_Is==============
                Subject     : Period Gap of 45 minutes
                Time        : 04:15pm - 05:00pm

                =============Next_Class_Will_Be=============           
                Subject     : A Cleaning session.
                Room Name   : Software Lab.
                Time        : 05:00pm - 05:45pm
                """)
        elif c_hour == 4 and c_min < 15:
            print(
                f"""
            Today is {today} and the time is {c_time}
            """)
            print(
                """
                ===========The_Previous_Class_Was===========
                Subject Name: Chemistry-1 (65913)
                Room No     : Chemirsry Lab
                Time        : 03:30pm - 04:15pm
                Teacher Name: Mr. Mazarul Islam Chowdhury.

                ==============Running_Class_Is==============
                Subject Name: Social Science (65811)
                Room No     : 105
                Time        : 03:30pm - 04:15pm
                Teacher Name: Mr. Biplob Kumar Sorkar.

                =============Next_Class_Will_Be=============           
                There is a Period Gap form 04:15pm to 05:00pm
                After that there is a cleaning session at Software Lab
                ============================================
                """)
        elif c_hour == 3 and c_min >= 30:
            print(
                f"""
            Today is {today} and the time is {c_time}
            """)
            print(
                """
                ===========The_Previous_Class_Was===========
                Subject Name: Chemistry-1 (65913)
                Room No     : Chemirsry Lab
                Time        : 03:30pm - 04:15pm
                Teacher Name: Mr. Mazarul Islam Chowdhury.

                ==============Running_Class_Is==============
                Subject Name: Social Science (65811)
                Room No     : 105
                Time        : 03:30pm - 04:15pm
                Teacher Name: Mr. Biplob Kumar Sorkar.

                =============Next_Class_Will_Be=============           
                There is a Period Gap form 04:15pm to 05:00pm
                After that there is a cleaning class at Software Lab
                ============================================
                """)
        elif c_hour == 3 and c_min < 30:
            print(
                f"""
            Today is {today} and the time is {c_time}. 
            """)
            print(
                """
                ===========The_Previous_Class_Was===========
                Subject Name: N/A

                ==============Running_Class_Is==============
                Subject Name: Chemistry-1 (65913)
                Room No     : Chemirsry Lab
                Time        : 03:30pm - 04:15pm
                Teacher Name: Mr. Mazarul Islam Chowdhury.

                =============Next_Class_Will_Be=============
                Subject Name: Social Science (65811)
                Room No     : 105
                Time        : 03:30pm - 04:15pm
                Teacher Name: Mr. Biplob Kumar Sorkar.
                """)
        elif c_hour == 2 and c_min >= 0:
            print(
                f"""
            Today is {today} and the time is {c_time}
            """)
            print(
                """
                ===========The_Previous_Class_Was===========
                Subject Name: N/A

                ==============Running_Class_Is==============
                Subject Name: Chemistry-1 (65913)
                Room No     : Chemirsry Lab
                Time        : 03:30pm - 04:15pm
                Teacher Name: Mr. Mazarul Islam Chowdhury.

                =============Next_Class_Will_Be=============
                Subject Name: Social Science (65811)
                Room No     : 105
                Time        : 03:30pm - 04:15pm
                Teacher Name: Mr. Biplob Kumar Sorkar.
                """)
        elif c_hour == 1 and c_min >= 15:
            print(
                f"""
            Today is {today} and the time is {c_time}
            """)
            print(
                """
                ===========The_Previous_Class_Was===========
                Subject Name: N/A

                ==============Running_Class_Is==============
                Subject Name: Chemistry-1 (65913)
                Room No     : Chemirsry Lab
                Time        : 03:30pm - 04:15pm
                Teacher Name: Mr. Mazarul Islam Chowdhury.

                =============Next_Class_Will_Be=============
                Subject Name: Social Science (65811)
                Room No     : 105
                Time        : 03:30pm - 04:15pm
                Teacher Name: Mr. Biplob Kumar Sorkar.
                """)
        elif c_hour == 1 and c_min < 15:
            print(
                f"""
                Today is {today} and the time is {c_time}. 
                """)
            print(
                """
                ===================================
                Class will start very soon at 01:15pm
                Today's first class is Chemistry-1 (65913)
                Room No: Chemistry Lab
                Class will be held form 01:15pm - 03:30pm
                Teacher Name: Md. Mazarul Islam Chowdhury.
                ===================================
                """)
        elif c_hour == 12 and c_min >= 0:
            print(
                f"""

                ===================================
                Today is {today} and the time is {c_time}
                """)
            print(
                """                        
                ===================================
                Classes not started yet
                Today's first class is Chemistry-1 (65913)
                And The class will start at 01:15pm
                Teacher Name: Md. Mazarul Islam Chowdhury.
                ===================================                   
                """)
    else:
        print(
            f"""

    Today is {today} and the time is {c_time}
     ================================================
     ||          There are 3 Classes Today         ||
     ================================================                  
     ||      Subject_Name                 Time     ||
     || 1. Chemistry-1               1:15pm-3:30pm ||
     || 2. Social Science            3:30pm-4:15pm ||
     || 3. Cleaning Session          4:15pm-6:30pm ||  
     ================================================
    """)


# Thursday

elif int_day == 3:
    if am_pm == "PM":
        if c_hour == 6 and c_min < 31:
            print(
                f"""
    Today is {today} and the time is {c_time}
            """)
            print(
                """
    ===========The_Previous_Class_Was===========
    Subject Name: Social Science (65811)
    Room No     : 101
    Time        : 03:30pm - 04:15pm
    Teacher Name: Biplob kumar Sorkar.
    
    ==============Running_Class_Is==============
    Subject Name: Web Design (66632)
    Room No     : Application Lab
    Time        : 04:15pm - 06:30pm
    Teacher Name: Mst Mim.
    
    =============Next_Class_Will_Be=============           
    It is the last class for Today.
    The class will end at 06:30pm
                """)
        elif c_hour >= 6 and c_hour != 12:
            print(
                f"""
    Today is "{today}" and the time is {c_time}
            """)
            print(
                """
    There are no more classes today
    The Last Class was ended at 06:30pm
                """)

        elif c_hour == 5 and c_min >= 0:
            print(
                f"""
    Today is {today} and the time is {c_time}
            """)
            print(
                """
    ===========The_Previous_Class_Was===========
    Subject Name: Social Science (65811)
    Room No     : 101
    Time        : 03:30pm - 04:15pm
    Teacher Name: Biplob kumar Sorkar.
    
    ==============Running_Class_Is==============
    Subject Name: Web Design (66632)
    Room No     : Application Lab
    Time        : 04:15pm - 06:30pm
    Teacher Name: Mst Mim.
    
    =============Next_Class_Will_Be=============           
    It is the last class for Today.
    The class will end at 06:30pm
                """)
        elif c_hour == 4 and c_min >= 15:
            print(
                f"""
    Today is {today} and the time is {c_time}
            """)
            print(
                """
    ===========The_Previous_Class_Was===========
    Subject Name: Mathmatics-3 (65931)
    Room No     : 302
    Time        : 03:31pm - 04:15pm
    Teacher Name: Md. Hasmut Ullah Sajib.
    
    ==============Running_Class_Is==============
    Subject Name: Web Design (66632)
    Room No     : Application Lab
    Time        : 04:15pm - 06:30pm
    Teacher Name: Mst Mim.
    
    =============Next_Class_Will_Be=============           
    It is the last class for Today.
    The class will end at 06:30pm
                """)
        elif c_hour == 4 and c_min < 15:
            print(
                f"""
    Today is {today} and the time is {c_time}
            """)
            print(
                """
    ===========The_Previous_Class_Was===========
    Subject Name: It Support System-2 (66634)
    Room No     : 206
    Time        : 01:15pm - 03:30pm
    Teacher Name: Taskin Nahar.
    
    ==============Running_Class_Is==============
    Subject Name: Mathmatics-3 (65931)
    Room No     : 302
    Time        : 03:31pm - 04:15pm
    Teacher Name: Md. Hasmut Ullah Sajib.
    
    =============Next_Class_Will_Be=============           
    Subject Name: Web Design (66632)
    Room No     : Application Lab
    Time        : 04:15pm - 06:30pm
    Teacher Name: Mst Mim.
                """)
        elif c_hour == 3 and c_min >= 30:
            print(
                f"""

    Today is {today} and the time is {c_time}
        """)
            print(
                """
    ===========The_Previous_Class_Was===========
    Subject Name: It Support System-2 (66634)
    Room No     : 206
    Time        : 01:15pm - 03:30pm
    Teacher Name: Taskin Nahar.
    
    ==============Running_Class_Is==============
    Subject Name: Mathmatics-3 (65931)
    Room No     : 302
    Time        : 03:31pm - 04:15pm
    Teacher Name: Md. Hasmut Ullah Sajib.
    
    =============Next_Class_Will_Be=============           
    Subject Name: Web Design (66632)
    Room No     : Application Lab
    Time        : 04:15pm - 06:30pm
    Teacher Name: Mst Mim.
                """)
        elif c_hour == 3 and c_min < 30:
            print(
                f"""

    Today is {today} and the time is {c_time}.
            """)
            print(
                """
    ===========The_Previous_Class_Was===========
    Subject Name: N/A
    
    ==============Running_Class_Is==============
    Subject Name: It Support System-2 (66634)
    Room No     : 206
    Time        : 01:15pm - 03:30pm
    Teacher Name: Taskin Nahar.
    
    =============Next_Class_Will_Be=============
    Subject Name: Mathmatics-3 (65931)
    Room No     : 302
    Time        : 03:31pm - 04:15pm
    Teacher Name: Md. Hasmut Ullah Sajib.
                """)
        elif c_hour == 2 and c_min >= 0:
            print(
                f"""

    Today is {today} and the time is {c_time}
            """)
            print(
                """
    ===========The_Previous_Class_Was===========
    Subject Name: N/A
    
    ==============Running_Class_Is==============
    Subject Name: It Support System-2 (66634)
    Room No     : 206
    Time        : 01:15pm - 03:30pm
    Teacher Name: Taskin Nahar.
    
    =============Next_Class_Will_Be=============
    Subject Name: Mathmatics-3 (65931)
    Room No     : 302
    Time        : 03:31pm - 04:15pm
    Teacher Name: Md. Hasmut Ullah Sajib.
                """)
        elif c_hour == 1 and c_min >= 15:
            print(
                f"""
    ============================================
    ||Today is {today} and the time is {c_time}||
    ============================================
                """)
            print(
    """
    ===========The_Previous_Class_Was===========
    Subject Name: N/A
    
    ==============Running_Class_Is==============
    Subject Name: It Support System-2 (66634)
    Room No     : 206
    Time        : 01:15pm - 03:30pm
    Teacher Name: Taskin Nahar.
    
    =============Next_Class_Will_Be=============
    Subject Name: Mathmatics-3 (65931)
    Room No     : 302
    Time        : 03:31pm - 04:15pm
    Teacher Name: Md. Hasmut Ullah Sajib.
    """)
        elif c_hour == 1 and c_min < 15:
            print(
        f"""
    Today is {today} and the time is {c_time}.
    """)
            print(
    """
    
    ===================================
    Class will start very soon at 01:15pm
    Today's first class is "It Support System-2 (66634)"
    Room No: 206
    Class will be held form 01:15pm - 03:30pm
    Teacher Name: Taskin Nahar
    ===================================
    """)
        elif c_hour == 12 and c_min >= 0:
            print(
        f"""
        
    ===================================
    Today is {today} and the time is {c_time}
    """)
            print(
    """                        
    ===================================
    Classes not started yet
    Today's first class is "It Support System-2 (66634)"
    And The class will start at 01:15pm
    Teacher Name: Taskin Nahar.
    ===================================                   
    """)
    else:
        print(
            f"""

    Today is {today} and the time is {c_time}
     ================================================
     ||          There are 3 Classes Today         ||
     ================================================                  
     ||      Subject_Name                 Time     ||
     || 1. It Support System         1:15pm-3:30pm ||
     || 2. Mathmatics-3              3:30pm-4:15pm ||
     || 3. Graphics Design-2         4:15pm-6:30pm ||  
     ================================================
    """)

# Friday

else:
    print(
        f"""

        ===================================
        Today is {today} and the time is {c_time}
        ===================================
        It's Our National Holiday.
        There are no classes today.
        ===================================
        """)