# -*- coding: utf-8 -*-
import typing as t

import aiohttp


class JollyMaxParser:
    def __init__(self, user_id: int):
        self.user_id = user_id

        self.headers = {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json',
            'Referer': 'https://www.jollymax.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        }

        self.session = None
        self._user_info = {'id': None, 'nickname': None}
        self._token = None

    async def get_token(self) -> t.Union[str, None]:
        json_data = {
            'terminalType':    'PC_H5',
            'accessTokenType': 'access_token',
            'bizType':         'userLogin',
            'deviceId':        'ddd05e88be7640ffbc949adc705b5cee',
            'loginType':       'visitor',
            'loginInfo': {
                'country':    'tr',
                'language':   'en',
                'deviceType': 'mobile',
            },
            'version': '1.0',
            'domain':  'www.jollymax.com',
        }
        url = 'https://api.jollymax.com/aggregate-pay-gate/api/gateway'

        async with self.session.post(url, headers=self.headers, json=json_data) as response:
            data = await response.json()
            return data['data']['token'] if data.get('success') else None

    async def fetch_user_info(self):
        token = await self.get_token()
        if not token: return self._user_info
        self._token = token

        json_data = {
            'token':     token,
            'userId':    self.user_id,
            'appId':     'APP20220811034444301',
            'country':   'tr',
            'language':  'en',
            'appAlias':  'pubg',
            'goodsId':   'G20230718123400139',
            'payTypeId': '698832',
            'domain':    'www.jollymax.com',
        }
        url = 'https://topup-center.shoplay365.com/shareit-topup-center/order/check-uid'

        async with self.session.post(url, headers=self.headers, json=json_data) as response:
            if response.status != 200: return self._user_info

            data = await response.json()

            if 'msg' not in data or 'nickName' not in data['data']:
                return self._user_info

            self._user_info['id'] = self.user_id
            self._user_info['nickname'] = data['data']['nickName']

        return self._user_info

    @property
    def id(self) -> t.Union[int, None]:
        return self._user_info.get('id')

    @property
    def nick_name(self) -> t.Union[str, None]:
        return self._user_info.get('nickname')

    @property
    def token(self) -> t.Union[str, None]:
        return self._token

    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        await self.fetch_user_info()  # fetch user
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        await self.session.close()
