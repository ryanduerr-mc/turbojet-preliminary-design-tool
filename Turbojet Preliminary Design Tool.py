"""
Turbojet Preliminary Design Tool (TPDT)

Interactive command-line tool for preliminary turbojet aircraft sizing.
Estimates: payload weight, takeoff gross weight, required thrust, empty weight,
wing loading, wing area, span, average chord, and stall velocity.

Author: Ryan Duerr
"""

import math

name = ''
bot_name: str = 'TPDT'

def calculate(wc, passengers, dx, cd0, k, m, a, c, dr, twe, wso, dens, clmto, ar):
    #Weight calculations
    wp = wc+(passengers*200)
    Em = 1 / (2*(math.sqrt(k*cd0)))
    Vcr= m*a
    zeta=1 - math.exp(-(c*dx)/(0.866*Em*Vcr))
    wfo=zeta/0.8
    #twceil is T/W at max ceiling, tw is at sea level. 
    twceil=1/Em
    tw=twceil/dr
    weo=tw/twe
    wo=wp/(1-wso-weo-wfo)
    treq=tw*wo
    emptyweight=weo*wo+wo*wso
    #wingloading calculations (ft & ft/s)

    cl=(cd0/(3*k))**(1/2)
    wingloading=0.5*dens*dr*((Vcr*(5280/3600))**2)
    s=wo/wingloading
    b=(ar*s)**(0.5)
    cavg=s/b

    vstall=((2*wingloading)/(dens*clmto))**(0.5)

    return wp, wo, treq, emptyweight, wingloading, s, b, cavg, vstall




#Assumptions
assumptions: str = '''Cruise altitude - 35000 ft
Zero-Lift Drag Coefficient - 0.016
Induced Drag Factor - 0.0468
Aspect Ratio - 8
Oswald Efficiency = 0.85
Fuel Consumption - 0.95 lb/hr/lb
Thrust to Engine Weight Ratio - 5
Max Lift Coefficient at Takeoff - 2.2
Absolute Ceiling - 45000 ft
Mach Number - 0.8 
Runway Length - 5000 ft
Speed of Sound at 35000 ft - 662.752 mi/hr
Percentage of Fuel Used for Cruise - 80%
Structure Weight Ratio - 0.45
Density Ratio - 0.310
Density at Sea Level - 23.769*10^-4'''

print(f'Hello! I\'m {bot_name}, short for Turbojet Preliminary Design Tool. Please type assumptions to see the chosen assumptions for this tool before beginning calculations.')

cruisealt=35000; cd0=0.016; k=0.0468; ar=8; e=0.85; c=0.95; twe=5; clmto=2.2
absceil=45000; m=0.8; runway=5000; a=662.752; cfp=0.8; wso=0.45; dr=0.310
dens=23.769*(10**(-4))

while True:
    user_input: str= input('You:').lower()

    if user_input in ['assumptions']:
        print(f'{bot_name}: Hi {name}, here is the list of assumptions: {assumptions}')
        change = input(f'{bot_name}: Would you like to change any variables? [y/n] ').lower().strip()
        if change in ['no','n']:
            cruisealt=35000;cd0=0.016;k=0.0468;ar=8;e=0.85;c=0.95;twe=5;clmto=2.2;absceil=45000;m=0.8;runway=5000;a=662.752;cfp=0.8;wso=0.45;dr=0.310;dens=23.769*(10**(-4))
            print(f'{bot_name}: Please type start to begin the calculations.')
        elif change in ['yes','y']:

            print(f'{bot_name}: Please input the following variables without units.') 
            try:
                cruisealt: float = float(input('Cruise Altitude: '))
                cd0: float = float(input('Zero-Lift Drag Coefficient: '))
                k: float = float(input('Induced Drag Factor: '))
                ar: float = float(input('Aspect Ratio: '))
                e: float = float(input('Oswald Efficiency: '))
                c: float = float(input('Fuel Consumption: '))
                twe: float = float(input('Thrust to Engine Weight Ratio: '))
                clmto: float = float(input('Max Lift Coefficient at Takeoff: '))
                absceil: float = float(input('Absolute Ceiling: '))
                m: float = float(input('Mach #: '))
                runway: float = float(input('Runway Length: '))
                a: float = float(input('Speed of Sound at 35000 ft: '))
                print(f'{bot_name}: For the percentage of fuel used for cruise, please input the percentage as a decimal.')
                cfp: float = float(input('Percentage of Fuel Used for Cruise: '))
                wso: float = float(input('Structure Weight Ratio: '))
                dr: float = float(input('Density Ratio: '))
                dens: float = float(input('Density at Sea Level: '))
                print(f'{bot_name}: Thank you! Type start to begin the calculations.')

            except ValueError:
                print(f'{bot_name}: Something went wrong. Make sure you only enter numbers. (Ex: 35000)')
                continue
        else:
            print(f"{bot_name}: Please enter 'y' or 'n'. Type assumptions to try again.")
    elif user_input in ['start', 'begin']:
        print(f'{bot_name}: Let\'s get started. Please input the cargo weight, number of passengers, and desired range. Remember that weight should be in pounds and range in miles. Do not include units.')
        try: 
            wc: float = float(input('Cargo Weight: '))
            passengers: float = float(input('# of Passengers: '))
            dx: float = float(input('Desired Range: '))
        
        except ValueError:
            print(f'{bot_name}: Something went wrong. Make sure you only enter numbers. (Ex: 35000)')
            continue
        results = calculate(wc, passengers, dx, cd0, k, m, a, c, dr, twe, wso, dens, clmto, ar)

        wp, wo, treq, emptyweight, wingloading, s, b, cavg, vstall = results

        print("\n--- DESIGN RESULTS ---")
        print(f"Payload Weight: {wp} lbs")
        print(f"Total Weight: {wo} lbs")
        print(f"Required Thrust: {treq} lbs")
        print(f"Empty Weight: {emptyweight} lbs")
        print(f"Wing Loading: {wingloading} lb/ft^2")
        print(f"Wing Area: {s} ft^2")
        print(f"Wing Span: {b} ft")
        print(f"Average Chord: {cavg} ft")
        print(f"Stall Velocity: {vstall} ft/s")

    

    elif user_input in ['bye', 'see you']:
        print(f'{bot_name}:Goodbye {name}, have a great day!')
        break




