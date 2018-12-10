from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount


my_app_id = '2015941031805106'
my_app_secret = 'c6730bc343cdefecc28c894e8db18d16'
my_access_token = 'EAAcpfNkWwLIBAJ8TvDkZBhgMBggvJOZCKj2LqlP1XxRiZCujuZCyln1Y78NZC7I2HkazMDZCjFZAv7YHiEY9LusRNUtEHzgkHQgO1ZAx5drFBdAPynxpSzBNAmfA35xE0s4fJFjZAsPZApv4IKYNmcSsA7dbgAUoBy6NiRmnmELXVR5m6F5n2qq3GU47J77WAfh1kvEeZCWtZAdk4Uj7X1IdZAlfhnbDFNBGZC6YcZD'
FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)
my_account = AdAccount('act_202042424038719')

###

campaigns = my_account.get_campaigns()
print(campaigns)

