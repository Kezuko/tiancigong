import uuid
from lunardate import LunarDate
from datetime import date

def chinese_zodiac_sign(year):
    zodiac_signs = ["鼠", "牛", "虎", "兔", "龙", "蛇", "马", "羊", "猴", "鸡", "狗", "猪"]
    return zodiac_signs[(year - 1900) % 12]
    
def generate_membership():
    return str(uuid.uuid4().int>>64)[0:18]
    
def get_current_lunar_date():
    dt = date.today()
    lunar_date = LunarDate.fromSolarDate(dt.year, dt.month, dt.day)
    return lunar_date.day
            
    