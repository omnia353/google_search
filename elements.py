elements = {
    "search": {
        "search_bar": {"method": "name",
                        "value": "q"},
        "first_link": {"method": "class_name",
                        "value": "g"}
    },
    "account": {
        "btn": {"method": "xpath",
                 "value": '//*[@id="landing-page-app"]/div/div[1]/div[3]/div[2]/div/div/div[2]/div/a'},
        "ip_user_name": { 'method' :'xpath',
                           'value' :'//*[@id="app"]/div/div[2]/div/div[2]/div/div/div/form/span[1]/input'},
        "ip-password": { 'method' : 'xpath',
                         'value' : '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div/form/span[2]/input'},
        "ip-confirm" : {'method' : 'xpath',
                        'value': '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div/form/span[3]/input'},
        "ip-email" : {'method' : 'xpath',
                      'value': '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div/form/span[4]/input'},
        "signup_btn": {'method' : 'xpath',
                       'value': '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div/button/div'}
        },
    "homepage" : {
        "btn" :{'method': 'id',
                'value':'banner_cta_button'}
    }
    }


