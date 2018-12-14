from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount


my_app_id = '2015941031805106'
my_app_secret = 'c6730bc343cdefecc28c894e8db18d16'
my_access_token = 'EAAcpfNkWwLIBACWnQw7nzoW3LJKSOSMtojXI113FBek6MufUrZCLMO1KZCLxcZBZAnAC9jckCuxZBZB3vx9Lod0mDynA0hYyj8ZAZB6ZBZBqft6kHBFID9TB7vx3b3f1a1Lfvx9GoZCp2hXE4zM00mleygXc3RtlynSdV5rLSov02mlGgnr32npmOZB7whgImsq7ZClp5Jk3qxlfPFa1bzDZAvuQGs2SCLGZCglmMMZD'
FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)
my_account = AdAccount('act_202042424038719')

###

campaigns = my_account.get_campaigns()
print(campaigns)

