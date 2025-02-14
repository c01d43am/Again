import random

# List of banners to choose from
banners = [
    """
     ░█████╗░░██████╗░░█████╗░██╗███╗░░██╗░█████╗░
     ██╔══██╗██╔════╝░██╔══██╗██║████╗░██║██╔══██╗
     ███████║██║░░██╗░███████║██║██╔██╗██║╚═╝███╔╝
     ██╔══██║██║░░╚██╗██╔══██║██║██║╚████║░░░╚══╝░
     ██║░░██║╚██████╔╝██║░░██║██║██║░╚███║░░░██╗░░
     ╚═╝░░╚═╝░╚═════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░░░╚═╝░░
    """,
    """
    .S_SSSs      sSSSSs   .S_SSSs     .S   .S_sSSs    
    .SS~SSSSS    d%%%%SP  .SS~SSSSS   .SS  .SS~YS%%b   
    S%S   SSSS  d%S'      S%S   SSSS  S%S  S%S   `S%b  
    S%S    S%S  S%S       S%S    S%S  S%S  S%S    S%S  
    S%S SSSS%S  S&S       S%S SSSS%S  S&S  S%S    S&S  
    S&S  SSS%S  S&S       S&S  SSS%S  S&S  S&S    S&S  
    S&S    S&S  S&S       S&S    S&S  S&S  S&S    S&S  
    S&S    S&S  S&S sSSs  S&S    S&S  S&S  S&S    S&S  
    S*S    S&S  S*b `S%%  S*S    S&S  S*S  S*S    S*S  
    S*S    S*S  S*S   S%  S*S    S*S  S*S  S*S    S*S  
    S*S    S*S   SS_sSSS  S*S    S*S  S*S  S*S    S*S  
    SSS    S*S    Y~YSSY  SSS    S*S  S*S  S*S    SSS  
           SP                    SP   SP   SP          
           Y                     Y    Y    Y           
    """,
    """
                                  88              
                                  ""              
                                                  
    ,adPPYYba,  ,adPPYb,d8 ,adPPYYba, 88 8b,dPPYba,   
    ""     `Y8 a8"    `Y88 ""     `Y8 88 88P'   `"8a  
    ,adPPPPP88 8b       88 ,adPPPPP88 88 88       88  
    88,    ,88 "8a,   ,d88 88,    ,88 88 88       88  
    `"8bbdP"Y8  `"YbbdP"Y8 `"8bbdP"Y8 88 88       88  
                aa,    ,88                            
                 "Y8bbdP"                          
    """,
    """
     ______   ______   ______  _____  ______  
    | |  | | | | ____ | |  | |  | |  | |  \ \ 
    | |__| | | |  | | | |__| |  | |  | |  | | 
    |_|  |_| |_|__|_| |_|  |_| _|_|_ |_|  |_| 
    """,
    """
.------..------..------..------..------.
|A.--. ||G.--. ||A.--. ||I.--. ||N.--. |
| (\/) || :/\: || (\/) || (\/) || :(): |
| :\/: || :\/: || :\/: || :\/: || ()() |
| '--'A|| '--'G|| '--'A|| '--'I|| '--'N|
`------'`------'`------'`------'`------'
    """,
    """
      ___         ___         ___                   ___     
     /  /\       /  /\       /  /\        ___      /  /\    
    /  /::\     /  /::\     /  /::\      /__/\    /  /::|   
   /  /:/\:\   /  /:/\:\   /  /:/\:\     \__\:\  /  /:|:|   
  /  /::\ \:\ /  /:/  \:\ /  /::\ \:\    /  /::\/  /:/|:|__ 
 /__/:/\:\_\:/__/:/_\_ \:/__/:/\:\_\:\__/  /:/\/__/:/ |:| /// 
 \__\/  \:\/:\  \:\__/\_\\__\/  \:\/:/__/\/:/~~\__\/  |:|/:/ 
      \__\::/ \  \:\ \:\      \__\::/\  \::/       |  |:/:/  
      /  /:/   \  \:\/:/      /  /:/  \  \:\       |__|::/  
     /__/:/     \  \::/      /__/:/    \__\/       /__/:/   
     \__\/       \__\/       \__\/                 \__\/    
    """
]

def Font_banner():
    # ANSI escape codes for colors
    colors = ["\033[31m", "\033[32m", "\033[33m", "\033[34m", "\033[35m", "\033[36m"]
    reset = "\033[0m"  # Reset color
    green = "\033[32m"  # Green color
    color = random.choice(colors)  # Pick a random color

    banner = random.choice(banners)  # Pick a random banner
    print(f"{color}{banner}{reset}")

    # Display version at the bottom left corner
    version = f"{green}\t\t\tv0.1.0 by c01d43am{reset}"
    print("\t\thttps://github.com/c01d43am")
    print(f"\n{version}\n")

# Call function for testing
if __name__ == "__main__":
    Font_banner()
