# encoding:utf-8
import requests
import json
import base64


def car_attribute_tell(img):
    """
    汽车属性识别调用百度api
    :param img: base64格式
    :return:
    """
    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    #host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=Hq0l6mMzuWoG8Arw0Hvtc7RO&client_secret=zGOkZpLfbrlZ0EOcP0H2UyC6ybOrpWoM'
    headers = {'content-type': 'application/json; charset=UTF-8'}
    #response = requests.post(host, headers=headers)
    #access_token = json.loads(response.text).get('access_token')
    access_token = "24.77db488047ec3fc092811a7e407122f4.2592000.1565399787.282335-16735578"
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/vehicle_attr"
    request_url = request_url + "?access_token=" + access_token
    data = {'image': img}
    response2 = requests.post(url=request_url, data=data, headers=headers)
    return response2.text


if __name__ == "__main__":
    # 二进制方式打开图片文件
    f = open('timg.jpg', 'rb')
    img = base64.b64encode(f.read())
    print(img)
    print(car_attribute_tell(img))