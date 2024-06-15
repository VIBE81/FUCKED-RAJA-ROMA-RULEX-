import requests

def getUserInfo(token):
    url = f"https://graph.facebook.com/v17.0/me?fields=id,name&access_token={token}"
    response = requests.get(url)
    data = response.json()
    return data

logo = """
_______________
                        
@@@@@@@    @@@@@@        @@@   @@@@@@   
@@@@@@@@  @@@@@@@@       @@@  @@@@@@@@  
@@!  @@@  @@!  @@@       @@!  @@!  @@@  
!@!  @!@  !@!  @!@       !@!  !@!  @!@  
@!@!!@!   @!@!@!@!       !!@  @!@!@!@!  
!!@!@!    !!!@!!!!       !!!  !!!@!!!!  
!!: :!!   !!:  !!!       !!:  !!:  !!!  
:!:  !:!  :!:  !:!  !!:  :!:  :!:  !:!  
::   :::  ::   :::  ::: : ::  ::   :::  
 :   : :   :   : :   : :::     :   : :  
                                        
________________

[ Facebook Account Information Tool ]
[ This tool is made by Mr Raja ]
________________       
"""

def main():
    print(logo)
    token = input("Enter Your Token: ")
    
    try:
        data = getUserInfo(token)
        uid = data['id']
        name = data['name']
        print(f" UID: {uid}")
        print(f" Name: {name}")
    except KeyError:
        print("Invalid Token or Token Expired!")

if _name_ == "_main_":
    main()
