import requests
import urllib3

links = [
        "https://prod-eb-platform-a1qa-apigateway.ele.local/swagger/index.html",
        "https://prod-eb-platform-admin-api.ele.local/swagger/index.html",
        'https://prod-eb-platform-admin-portal-apigateway.ele.local/swagger/index.html',
        'https://prod-eb-platform-admin-portal-frontend.ele.local/auth/login',
        'https://prod-eb-platform-contact-api.ele.local/swagger/index.html',
        'https://prod-eb-platform-content-api.ele.local/swagger/index.html',
        'https://prod-eb-platform-customer-api.ele.local/swagger/index.html',
        'https://prod-eb-platform-eb-games-api-gateway.ele.local/swagger/index.html',
        'https://prod-eb-platform-faq-api.ele.local/swagger/index.html',
        'https://prod-eb-platform-game-api.ele.local/swagger/index.html',
        'https://prod-casino-general-internal-service.ele.local/api/',
        'https://prod-eb-platform-integrations-connectivegames-api.ele.local/swagger/index.html',
        'https://prod-eb-platform-integrations-egt-api.ele.local/swagger/index.html',
        'https://prod-eb-platform-integrations-netent-api.ele.local/swagger/index.html',
        'https://prod-eb-platform-integrations-playngo-api.ele.local/swagger',
        'https://prod-eb-platform-integrations-pvp-api.ele.local/swagger/index.html',
        'https://prod-eb-platform-integrations-xcrms-api.ele.local/swagger/ui/index',
        'https://prod-eb-platform-integrations-yggdrasil-api.ele.local/swagger/index.html',
        'https://prod-eb-platform-login-api.ele.local/swagger/index.html',
        'https://mobile.stage.europebet.com/api/swagger/',
        'https://prod-eb-platform-mobileverification-api.ele.local/swagger/index.html',
        'https://prod-eb-platform-promotions-api.ele.local/swagger/index.html',
        'https://promotions-api.europebet.com/swagger/index.html',
        'https://prod-eb-platform-realitycheck-api.ele.local/swagger/index.html',
        'https://prod-eb-platform-registration-api.ele.local/swagger/index.html',
        'https://prod-eb-platform-subcore-apigateway.ele.local/swagger/index.html',
        'https://prod-eb-platform-survey-api.ele.local/swagger/index.html',
        'https://prod-eb-platform-tutorials-api.ele.local/swagger/index.html'
        ]


n=0
for i in links:
    n+=1
    try:
        r = requests.get(i, verify=False)
        urllib3.disable_warnings()
        print(n, 'link: ', r.url , r.status_code)
    except:
        print(n, 'error', i)
print(n)
