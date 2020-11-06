import Connection

results = Connection.connect('SELECT TOP 10 * FROM dbo.SteamRecommendations')

for x in results:
    print(x)