STRING_LIST = '''
aids
airlines
billionaires
broadway
business_dynamics
cancer
cars
classics
construction_permits
construction_spending
county_crime
county_demographics
drugs
drug_bank
earthquakes
education
election
energy
finance
food
food_access
global_development
graduates
health
hospitals
hydropower
immigration
injuries
labor
medal_of_honor
music
publishers
real_estate
retail_services
school_scores
skyscrapers
slavery
state_crime
state_demographics
state_fragility
suicide_attacks
supreme_court
tate
video_games
weather'''

MODULE_WHITE_LIST = [s.strip() for s in STRING_LIST.strip().split() if s.strip()]
