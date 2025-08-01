#main concept is :
    # 1 Kills total
    # Give the point of kills
    # How many matches played the player

teams = {} 

def record_match_results(team_name, kills, won=False):
    """Records match results for a team."""
    if team_name not in teams:
        teams[team_name] = {"kills": 0, "wins": 0}  
    teams[team_name]["kills"] += kills
    if won:
        teams[team_name]["wins"] += 1

def display_standings():
    """Displays the tournament standings."""
    print("\n--- Current Standings ---")
    sorted_teams = sorted(teams.items(), key=lambda item: (item[1]["wins"], item[1]["kills"]), reverse=True)
    for team, data in sorted_teams:
        print(f"Team: {team}, Wins: {data['wins']}, Kills: {data['kills']}")


record_match_results("Team A", 10, True)  
record_match_results("Team B", 7)
record_match_results("Team C", 5)
record_match_results("Team A", 5)      
record_match_results("Team B", 12, True)
display_standings()
    