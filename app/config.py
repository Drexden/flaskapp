key = "bc9njqhm2bcezun3k5hk66kq"

#URL structure - :sport/:league/teams/:teamId/news?key

sport_byu = "football"
league_byu = "college-football"
teamID_byu = "252"
base_url_byu = 'http://api.espn.com/v1/sports'
url_byu = base_url_byu + "/" + sport_byu + "/" + league_byu + "/teams" + "/" + teamID_byu + "/news" + "?apikey=" + key

sport_ars = "soccer"
league_ars = "eng.1"
teamID_ars = "359"
base_url_ars = 'http://api.espn.com/v1/sports'
url_ars = base_url_ars + "/" + sport_ars + "/" + league_ars + "/teams" + "/" + teamID_ars + "/news" + "?apikey=" + key

sport_suns = "basketball"
league_suns = "nba"
teamID_suns = "21"
base_url_suns = 'http://api.espn.com/v1/sports'
url_suns = base_url_suns + "/" + sport_suns + "/" + league_suns + "/teams" + "/" + teamID_suns + "/news" + "?apikey=" + key

sport_usmnt = "soccer"
league_usmnt = "fifa.world"
teamID_usmnt = "660"
base_url_usmnt = 'http://api.espn.com/v1/sports'
url_usmnt = base_url_usmnt + "/" + sport_usmnt + "/" + league_usmnt + "/teams" + "/" + teamID_usmnt + "/news" + "?apikey=" + key

url_stocks = 'http://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.quotes%20where%20symbol%20in%20(%22LUK%22%2C%22AMZN%22%2C%22AAPL%22)%0A%09%09&env=http%3A%2F%2Fdatatables.org%2Falltables.env&format=json'

