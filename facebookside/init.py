from facebookads.adobjects.adaccount import AdAccount
from facebookads.adobjects.adsinsights import AdsInsights
from facebookads.api import FacebookAdsApi

access_token = 'EAAcpfNkWwLIBAJ8TvDkZBhgMBggvJOZCKj2LqlP1XxRiZCujuZCyln1Y78NZC7I2HkazMDZCjFZAv7YHiEY9LusRNUtEHzgkHQgO1ZAx5drFBdAPynxpSzBNAmfA35xE0s4fJFjZAsPZApv4IKYNmcSsA7dbgAUoBy6NiRmnmELXVR5m6F5n2qq3GU47J77WAfh1kvEeZCWtZAdk4Uj7X1IdZAlfhnbDFNBGZC6YcZD'
ad_account_id = 'act_202042424038719'
app_secret = 'c6730bc343cdefecc28c894e8db18d16'
app_id = '2015941031805106'

FacebookAdsApi.init(access_token=access_token)

fields = [
    'account_id',
    'account_name',
    'campaign_group_name',
    'campaign_group_id',
    'campaign_name',
    'campaign_id',
    'adgroup_id',
    'adgroup_name',
]
params = {
    'level': 'campaign',
    'filtering': [],
    'breakdowns': [],
    'time_range': {'since':'2018-11-11','until':'2018-12-11'},
}
df = AdAccount(ad_account_id).get_insights(
    fields=fields,
    params=params,
)

