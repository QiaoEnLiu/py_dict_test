# py_dict_test.py

R1X_Mapping={0:'Alarm2 , Alarm1',
             1:'x , Alarm3'}

R3X_Mapping={0:'Gas',
             
             2:'Temperature',

             4:'Calibration Gas %',

             6:'Calibration T',

             8:'Calibration CT1',

             10:'Calibration CT',

             12:'Read V3 voltage',

             14:'Read V2 voltage',

             16:'Read BAT',
             17:'Read BAT %',
             18:'Read Valid Form Calibration',
             19:'Read Pooling cnt',
             20:'Read Current %'
             }

R4X_Mapping={0:'Temp unit',
             1:'Date Formate',
             2:'Thermal Limit',
             3:'Thermal cut off',
             4:'Set Gas Unit',
             5:'Set Alarm flg1',
             6:'Set Alarm flg2',
             7:'Set Alarm flg3',
             8:'Set Alarm flg4',
             9:'set baudrate',
             10:'set ct range',
             11:'set CT1',
             12:'Set CT2',
             13:'Calibratile set',
             14:'configure set',
             15:'Member',
             16:'Set Pressur',
             
             18:'set CT1_1',
             19:'Set CT2_1',
             20:'AD-CT1-Low',
             21:'AD-CT1-High',
             22:'AD-CT2-Low',
             23:'AD-CT2-High',
             24:'RTC_YearMonth',
             25:'RTC_DateHour',
             26:'RTC_Minute'
             }

def R3X_address(searchName):
    address= next((key for key, value in R3X_Mapping.items() if value == searchName), None)
    return address

print(R3X_address('Read BAT'))