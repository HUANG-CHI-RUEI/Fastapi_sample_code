import random

from fastapi import APIRouter,Request
from sqlalchemy import delete
from influxdb import InfluxDBClient


router = APIRouter()
CLIENT = InfluxDBClient('127.0.0.1', 8086, 'root', 'password', 'testdb') 


# host,8086,your_username,your_password,your_dbname
# @router.api_route("/temperature", methods=['GET', 'POST', 'DELETE'])
# def handle_temperature(request:Request):
#     def write_temperature():
#         temperature = [
#             {
#                 "measurement": "Temperature",
#                 "tags": {
#                     "topic": "Sensor/Temperature"
#                 },
#                 "fields":{
#                     "tem": 18
#                 }
#             }
#         ]
#         CLIENT.write_points(temperature)
#         print('write ok')
#         return {"result": "Done"}

#     def read_temparature():
#         sql = 'select * from Temperature'
#         result = list(CLIENT.query(sql).get_points())
#         return result

#     def delete_temparature():
#         drop_temp = CLIENT.query('DELETE FROM Temperature')
#         print('delete ok')
#         return drop_temp 

#     request_dict={'GET':read_temparature(), 'DELETE':delete_temparature(), 'POST':write_temperature()}
#     result = request_dict.get(request['method'], '')
    
#     return result

@router.get("/read_param")
def read_param():
        sql = 'select * from parameter'
        result = list(CLIENT.query(sql).get_points())
        return result



@router.delete("/del_param", status_code=204)
def delete_temp():
    drop_temp = CLIENT.query('delete from parameter')
    return {"result": "delete completed!"}


@router.post("/write_temperature")
def write_temperature():
    value = random.randint(10,30)
    #溫度
    temperature = [
        {
            "measurement": "parameter",
            "tags": {
                "topic": "temperature"
            },
            "fields":{
                "value": value
            }
        }
    ]
    CLIENT.write_points(temperature)

    return {"result": "Done"}


@router.post("/write_phvalue")
def write_phvalue():
    value = random.randint(10,30)
    #酸鹼度
    phvalue = [
        {
            "measurement": "parameter",
            "tags": {
                "topic": "phvalue"
            },
            "fields":{
                "value": value
            }
        }
    ]
    CLIENT.write_points(phvalue)
   
    return {"result": "Done"}


@router.post("/write_atp")
def write_temperature():
    value = random.randint(10,100)
    
    atp_param = [
        {
            "measurement": "parameter",
            "tags": {
                "topic": "atp_details",
            },
            "fields":{
                "atp":"151",
                "atp_hour": "30",
                "pH": "7.5",
                "turbidity":"0.043",
                "orp":"9",
                "temperature":"21",
                "water":"1330",
                "uvp":"230"
            }
        }
    ]
    CLIENT.write_points(atp_param)

    return {"result": "Done"}

# @router.post("/write_redoxpotential")
# def write_redoxpotential():
#     #氧化還原電位
#     redoxpotential = [
#         {
#             "measurement": "Redox",
#             "tags": {
#                 "topic": "Sensor/Redox"
#             },
#             "fields":{
#                 "redox": 45
#             }
#         }
#     ]
#     CLIENT.write_points(redoxpotential)
#     return {"result": "Done"}

# @router.post("/write_turbidity")
# def write_turbidity():
#     #濁度
#     turbidity = [
#         {
#             "measurement": "Turbidity",
#             "tags": {
#                 "topic": "Sensor/Turbidity"
#             },
#             "fields":{
#                 "redox": 17
#             }
#         }
#     ]
#     CLIENT.write_points(turbidity)
   
#     return {"result": "Done"}

# @router.post("/write_circulatingflow")
# def write_circulatingflow():
#     # 循環流量
#     circulatingflow = [
#         {
#             "measurement": "CirculatingFlow",
#             "tags": {
#                 "topic": "Sensor/circulatingflow"
#             },
#             "fields":{
#                 "cf": 123
#             }
#         }
#     ]
#     CLIENT.write_points(circulatingflow)
   
#     return {"result": "Done"}

# @router.post("/write_uvpower")
# def write_uvpower():
#     # UV功率
#     uvpower = [
#         {
#             "measurement": "UVPower",
#             "tags": {
#                 "topic": "Sensor/UVPower"
#             },
#             "fields":{
#                 "uvp": 63
#             }
#         }
#     ]
#     CLIENT.write_points(uvpower)
   
#     return {"result": "Done"}

# @router.post("/write_uvtime")
# def write_uvtime():
#     # UV使用時數
#     uvtime = [
#         {
#             "measurement": "UVTime",
#             "tags": {
#                 "topic": "Sensor/UVTime"
#             },
#             "fields":{
#                 "uvt": 8.9
#             }
#         }
#     ]
#     CLIENT.write_points(uvtime)
   
#     return {"result": "Done"}

# @router.post("/write_uvtime")
# def write_uvtime():
#     # UV使用時數
#     uvtime = [
#         {
#             "measurement": "UVTime",
#             "tags": {
#                 "topic": "Sensor/UVTime"
#             },
#             "fields":{
#                 "uvt": 8.9
#             }
#         }
#     ]
#     CLIENT.write_points(uvtime)
   
#     return {"result": "Done"}

# @router.post("/write_colony")
# def write_colony():
#     # 菌落數
#     colony = [
#         {
#             "measurement": "Colony",
#             "tags": {
#                 "topic": "Sensor/Colony"
#             },
#             "fields":{
#                 "count": 50897
#             }
#         }
#     ]
#     CLIENT.write_points(colony)
   
#     return {"result": "Done"}











