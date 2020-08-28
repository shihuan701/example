import requests



class _requests:
    def _post(self,url, arg, headers):
        r = requests.post(url, json=arg, headers=headers, verify=False)
        return r


    def _get(self,url,headers):
        r = requests.get(url, params=None,headers=headers)
        return r