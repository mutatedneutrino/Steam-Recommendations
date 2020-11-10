import Database_Queries

#SELECT QUERY
#select = 'TOP 10 *'
#table = 'dbo.SteamRecommendations'

#Database_Queries.select(select,table)

#JOIN QUERY
select = 'TOP 100 dbo.SteamRecommendations.NAME, dbo.GameSales.Genre, dbo.GameSales.Year'
table1 = 'dbo.SteamRecommendations'
table2 = 'dbo.GameSales'
join_type = 'RIGHT OUTER JOIN'
join_property = 'dbo.GameSales.Name=dbo.SteamRecommendations.NAME'

Database_Queries.join(select,table1,table2,join_type,join_property)