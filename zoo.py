print("I love animals!")
print("Let's check out the animals...")
print("The deer looks fine.")
print("The lion looks healthy.")
camel = r"""
The camel habitat...
         ___.-''''-.
        /___  @    |
       ',,,,.     |         _.'''''''._
            '     |        /           \
            |     \    _.-'             \
            |      '.-'                  '-.
            |                               ',
            |                                '',
             ',,-,                           ':;
                  ',,| ;,,                 ,' ;;
                     ! ;!'',,,',',,,,'!  ;   ;:
                    : ; ! ! ! ! ! ! ! ; ; ; ;,
                    ; ; ! ! ! ! ! ! ! ; ; ; ;
                   ; ; ! ! ! ! ! ! ! ; ; ; ;
                  ; ; ! ! ! ! ! ! ! ; ; ; ;
                 ;,,!,!,!,!,!,!,!,!,!;!;!;!;
                     /_I_I_I_I_I_I_I_I_I_I_\
"""

lion = r"""
The lion habitat...
                                               ,w.
                                             ,YWMMw  ,M  ,
                        _.---.._   __..---._.'MMMMMw,wMWmW,
                   _.-""        '''           YP"WMMMMMMMMMb,
                .-' __.'                   .'     MMMMW^WMMMM;
    _,        .'.-'"; `,       /`     .--""      :MMM[==MWMW^;
 ,mM^"     ,-'.'   /   ;      ;      /   ,       MMMMb_wMW"  @\ 
,MM:.    .'.-'   .'     ;     `\    ;     `,     MMMMMMMW `"=./`-,
WMMm__,-'.'     /      _.\      F'''-+,,   ;_,_.dMMMMMMMM[,_ / `=_}
"^MP__.-'    ,-' _.--""   `-,   ;       \  .'\    ^"WMMMMMP^` ; __|
           /   .'            ; ;         )  )`( ,  `       `./"     \
          /  .'             /  (       .'  /     Ww._     `. '"     `"
         /  Y,              `,  `-,=,_{   ;      MMMP`""-,  `-._.-,/
        (--, )                `,_ / `) \/"")      ^"      `-, -;"\:
The lion is roaring!
"""

deer = r"""
The deer habitat...
   /|       |\
`__\\       //__'
   ||      ||
 \__`\     |'__/
   `_\\   //_'
      _.,:---;,._
     \_:     :_/
       |@. .@|
       |     |
       ,\.-./ \
       ;;`-'   `---__________-----.-.
       ;;;                         \
       ';;;                         |
        ;    |                      ;
         \   \     \        |      /
          \_, \    /        \     |\
            |';|  |,,,,,,,,/ \    \ \
            |  |  |           \   /   |
            \  \  |           |  / \  |
             | || |           | |   | |
             | || |           | |   | |
             | || |           | |   | |
             |_||_|           |_|   |_|
            /_//_/           /_/   /_/
"""

goose = r"""
The goose habitat...
                                    _
                                ,-"" "".
                              ,'  ____  `.
                            ,'  ,'    `.  `._
   (`.         _..--.._   ,'  ,'        \    \
  (`-.\    .-""        ""'   /          (  d _b
 (`._  `-"" ,._             (            `-(   \
 <_  `     (  <`<            \              `-._\
  <`-       (__< <           :
   (__        (_<_<          ;
    `------------------------------------------
"""

bat = r"""
The bat habitat...
_________________               _________________
     ~-.              \|\_--_/|                 .-~
         ~-.           / o o \           .-~
            >         (   "   )          <
           /        \   \     /   /        \
          /_          '-.__.-'          _\
         ~    ,                   ,    ~
          ~   /    \           /    \   ~
           ~ /      \ / _  _ \ /      \ ~
            ~           " ~ "           ~
"""

rabbit = r"""
The rabbit habitat...
         ,
        /|      __
       / |   ,-~ /
      Y :|  //  /
      | jj /( .^
      >-"~"-v"
     /       Y
    jo  o    |
   ( ~T~     j
    >._-' _./
   /   "~"  |
  Y     _,  |
 /| ;-"~ _  l
/ l/ ,-"~    \
\//\/      .- \
 Y        /    Y 
 l       I     !
 ]\      _\    /"\
(" ~----( ~   Y.  )
"""

animals = [camel, lion, deer, goose, bat, rabbit]

while True:
    user_input = input("Please enter the number of the habitat you would like to view: > ")
    if user_input == "exit":
        print("See you later!")
        break
    elif user_input.isdigit() and int(user_input) < len(animals):
        habitat_index = int(user_input)
        print(animals[habitat_index])
    else:
        print("Invalid input. Please enter a number between 0 and", len(animals) - 1, "or 'exit' to quit.")
