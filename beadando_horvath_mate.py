import  teknős
behozatali  idő
 véletlenszerű importálás

késleltetés  =  0,1

# Pontszám
pontszám  =  0
high_score  =  0

# Állítsa be a képernyőt
wn  =  teknős . Képernyő ()
wn . cím ( "Snake Game by @TokyoEdTech" )
wn . bgcolor ( "zöld" )
wn . beállítás ( szélesség = 600 , magasság = 600 )
wn . nyomkövető ( 0 ) # Kikapcsolja a képernyőfrissítéseket

# Kígyófej
fej  =  teknős . Teknős ()
fej . sebesség ( 0 )
fej . forma ( "négyzet" )
fej . szín ( "fekete" )
fej . felemelés ()
fej . goto ( 0 , 0 )
fej . irány  =  "stop"

# Kígyóeledel
étel  =  teknős . Teknős ()
ételt . sebesség ( 0 )
ételt . forma ( "kör" )
ételt . szín ( "piros" )
ételt . felemelés ()
ételt . goto ( 0 , 100 )

szegmensek  = []

# Toll
toll  =  teknős . Teknős ()
toll . sebesség ( 0 )
toll . forma ( "négyzet" )
toll . szín ( "fehér" )
toll . felemelés ()
toll . rejtőzködő teknős ()
toll . goto ( 0 , 260 )
toll . write ( "Pontszám: 0 Magas pontszám: 0" , align = "center" , font = ( "Courier" , 24 , "normal" ))

# Funkciók
def  go_up ():
    ha  fej . irány  !=  "le" :
        fej . irány  =  "fel"

def  go_down ():
    ha  fej . irány  !=  "fel" :
        fej . irány  =  "le"

def  go_left ():
    ha  fej . irány  !=  "jobbra" :
        fej . irány  =  "balra"

def  go_right ():
    ha  fej . irány  !=  "balra" :
        fej . irány  =  "jobbra"

def  move ():
    ha  fej . irány  ==  "fel" :
        y  =  fej . ycor ()
        fej . sety ( y  +  20 )

    ha  fej . irány  ==  "le" :
        y  =  fej . ycor ()
        fej . sety ( y  -  20 )

    ha  fej . irány  ==  "balra" :
        x  =  fej . xcor ()
        fej . setx ( x  -  20 )

    ha  fej . irány  ==  "jobbra" :
        x  =  fej . xcor ()
        fej . setx ( x  +  20 )

# Billentyűzetkötések
wn . figyelj ()
wn . onkeypress ( go_up , "w" )
wn . onkeypress ( go_down , "s" )
wn . onkeypress ( go_left , "a" )
wn . onkeypress ( go_right , "d" )

# Fő játékhurok
míg  igaz :
    wn . frissítés ()

    # Ellenőrizze, nincs-e ütközés a határral
    ha  fej . xcor () > 290  vagy  fej . xcor () < - 290  vagy  fej . ycor () > 290  vagy  fej . ycor () < - 290 :
        idő . aludni ( 1 )
        fej . goto ( 0 , 0 )
        fej . irány  =  "stop"

        # A szegmensek elrejtése
         szegmensekben  : _ _  _
            szegmens . goto ( 1000 , 1000 )
        
        # Törölje a szegmensek listáját
        szegmensek . tiszta ()

        # Állítsa vissza a pontszámot
        pontszám  =  0

        # Állítsa vissza a késleltetést
        késleltetés  =  0,1

        toll . tiszta ()
        toll . write ( "Pontszám: {} Magas pontszám: {}" . formátum ( score , high_score ), align = "center" , font = ( "Courier" , 24 , "normal" ))


    # Ellenőrizze, hogy nem ütközött-e az élelmiszerrel
    ha  fej . távolság ( étel ) <  20 :
        # Helyezze az ételt egy véletlenszerű helyre
        x  =  véletlenszerű . randint ( - 290 , 290 )
        y  =  véletlenszerű . randint ( - 290 , 290 )
        ételt . goto ( x , y )

        # Szegmens hozzáadása
        new_segment  =  teknős . Teknős ()
        új_szegmens . sebesség ( 0 )
        új_szegmens . forma ( "négyzet" )
        új_szegmens . szín ( "szürke" )
        új_szegmens . felemelés ()
        szegmensek . hozzáfűzés ( új_szegmens )

        # Rövidítse le a késleltetést
        késleltetés  -=  0,001

        # Növelje a pontszámot
        pontszám  +=  10

        ha  pontszám  >  high_score :
            high_score  =  pontszám
        
        toll . tiszta ()
        toll . write ( "Pontszám: {} Magas pontszám: {}" . formátum ( score , high_score ), align = "center" , font = ( "Courier" , 24 , "normal" ))

    # Mozgassa először a végszegmenseket fordított sorrendben
    a  tartományban lévő indexhez  ( len ( szegmensek ) - 1 , 0 , - 1 ): 
        x  =  szegmensek [ index - 1 ]. xcor ()
        y  =  szegmensek [ index - 1 ]. ycor ()
        szegmensek [ index ]. goto ( x , y )

    # Mozgassa a 0. szegmenst oda, ahol a fej van
    ha  len ( szegmensek ) >  0 :
        x  =  fej . xcor ()
        y  =  fej . ycor ()
        szegmensek [ 0 ]. goto ( x , y )

    mozogni ()    

    # Ellenőrizze, hogy a fej nem ütközik-e a testrészekkel
     szegmensekben  : _ _  _
        ha  szegmens . távolság ( fej ) <  20 :
            idő . aludni ( 1 )
            fej . goto ( 0 , 0 )
            fej . irány  =  "stop"
        
            # A szegmensek elrejtése
             szegmensekben  : _ _  _
                szegmens . goto ( 1000 , 1000 )
        
            # Törölje a szegmensek listáját
            szegmensek . tiszta ()

            # Állítsa vissza a pontszámot
            pontszám  =  0

            # Állítsa vissza a késleltetést
            késleltetés  =  0,1
        
            # Frissítse a pontszám kijelzőt
            toll . tiszta ()
            toll . write ( "Pontszám: {} Magas pontszám: {}" . formátum ( score , high_score ), align = "center" , font = ( "Courier" , 24 , "normal" ))

    idő . alvás ( késés )

wn . főhurok ()
