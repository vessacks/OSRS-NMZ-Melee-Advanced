# NZM melee

from msilib.schema import Feature
import cv2 as cv
from cv2 import threshold
from cv2 import _InputArray_STD_BOOL_VECTOR
import numpy as np
import os
from windmouse import wind_mouse
from windowcapture import WindowCapture
from vision import Vision
import pyautogui
from pyHM import Mouse
import time
from action import Action

#notes:
# 1. run in classic fixed
# 2. it searches partly in color. don't throw black and white code in willy nilly
# 3. prayer hotkey set to f5 (standard)
# 4. inventory hotkey set to f1 (NOT STANDARD)
# 5. you have to enter the dream, hit the overload, and rock down to 1hp before starting the program. 

#thoughts
#1. consider running the vision part in color. It will make verything more accurate, and speed doesn't matter so much here. 


# initialize the WindowCapture class
wincap = WindowCapture('RuneLite - Vessacks')


# initialize the Vision class
#do these color
rapid_heal_vision = Vision('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\nmz melee\\image library\\rapid_heal.png', method = cv.TM_CCOEFF_NORMED, imread = cv.IMREAD_COLOR)
protect_melee_vision = Vision('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\nmz melee\\image library\\protect_melee.png', method = cv.TM_CCOEFF_NORMED, imread = cv.IMREAD_COLOR)

#do these grayscale
sorb_one_vision = 
sorb_two_vision = 
sorb_three_vision =
sorb_four_vision =

#color
max_sorb_vision = 


sorb_full_notification = #this is the chat message that says something like "you can't drink more absorbtion rn, ie you're at 1k"

#do these grayscale
overload_one_vision =
overload_two_vision = 
overload_three_vision = 
overload_four_vision = 

overload_active_vision = 

#color
fifty_one_health_vision=
one_health_vision= 

#initialize the action class
rapid_heal_action = Action('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\nmz melee\\image library\\rapid_heal.png')
protect_melee_action = Action('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\nmz melee\\image library\\protect_melee.png')

sorb_one_action = 
sorb_two_action = 
sorb_three_action =
sorb_four_action =

next_overload_action = #put any overload potion picture here, provided they are all the same size. They must be all the same size for this to work. 



PRAYER_THRESHOLD = .93
POTION_THRESHOLD = .93
FIFTY_ONE_HEALTH_THRESHOLD = .85

def speed():
    speed = np.random.normal(.7,.3)
    while speed > .85 or speed < .6:
        speed = np.random.normal(.75,.08)
    return speed


def tick_dropper(odds=20):
    if np.random.randint(0,odds) == 1:
        
        drop = np.random.uniform(.6,2)
        print('tick dropper! sleeping %s' %drop)
        time.sleep(drop)
    return

def wait():
    wait = (.1 + abs(np.random.normal(0,.05)))
    return wait

#determine the session parameters for how early to turn on protect melee
protect_melee_early_time_mean = np.random.uniform(.3,2)
protect_melee_early_time_stdDev = protect_melee_early_time_mean/6


#determine the session parameters for how late to turn off protect melee
protect_melee_late_time_mean = np.random.uniform(.3,2)
protect_melee_late_time_stdDev = protect_melee_early_time_mean/6

#determine the session parameters for how late to repot 
repot_late_time_mean = np.random.uniform(.1,.6)
repot_late_time_stdDev = repot_late_time_mean/5

#session parameters for rapid heal flicking
flick_early_time_mean = np.random.uniform(25,45)
flick_early_time_stdDev = abs(flick_early_time_mean-60)/10 

print('session figures:')
print('protect_melee_early_time_mean %s' %protect_melee_early_time_mean)
print('protect_melee_early_time_stdDev %s'%protect_melee_early_time_stdDev)
print('protect_melee_late_time_mean %s' %protect_melee_late_time_mean)
print('protect_melee_late_time_stdDev %s' %protect_melee_late_time_stdDev)
print('repot_late_time_mean %s' %repot_late_time_mean)
print('repot_late_time_stdDev %s' %repot_late_time_stdDev)
print('flick_early_time_mean %s'%flick_early_time_mean)
print('flick_early_time_stdDev %s' %flick_early_time_stdDev)

#find your overload potion locations (GRAYSCALE) before starting the loop
print('finding overload_ones')
screenshot = wincap.get_screenshot()
screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY) #grayscale
overload_one_allPoints, overload_one_bestPoint, overload_one_confidence = overload_one_vision.find(screenshot, threshold = POTION_THRESHOLD, debug_mode= 'rectangles', return_mode = 'allPoints + bestPoint + confidence')
if cv.waitKey(1) == ord('q'):
    cv.destroyAllWindows()
    exit()

print('finding overload_twos')
screenshot = wincap.get_screenshot()
screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY) #grayscale
overload_two_allPoints, overload_two_bestPoint, overload_two_confidence = overload_two_vision.find(screenshot, threshold = POTION_THRESHOLD, debug_mode= 'rectangles', return_mode = 'allPoints + bestPoint + confidence')
if cv.waitKey(1) == ord('q'):
    cv.destroyAllWindows()
    exit()
    
print('finding overload_threes')
screenshot = wincap.get_screenshot()
screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY) #grayscale
overload_three_allPoints, overload_three_bestPoint, overload_three_confidence = overload_three_vision.find(screenshot, threshold = POTION_THRESHOLD, debug_mode= 'rectangles', return_mode = 'allPoints + bestPoint + confidence')
if cv.waitKey(1) == ord('q'):
    cv.destroyAllWindows()
    exit()

print('finding overload_fours')
screenshot = wincap.get_screenshot() 
screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY) #grayscale
overload_four_allPoints, overload_four_bestPoint, overload_four_confidence = overload_four_vision.find(screenshot, threshold = POTION_THRESHOLD, debug_mode= 'rectangles', return_mode = 'allPoints + bestPoint + confidence')
if cv.waitKey(1) == ord('q'):
    cv.destroyAllWindows()
    exit()
    

#define the next overload for use in coming loop
print('looking for overloads...')
if overload_one_confidence > POTION_THRESHOLD:
    next_overload = overload_one_bestPoint
elif overload_two_confidence > POTION_THRESHOLD:
    next_overload = overload_two_bestPoint
elif overload_three_confidence > POTION_THRESHOLD:
    next_overload = overload_three_bestPoint
elif overload_four_confidence > POTION_THRESHOLD:
    next_overload = overload_four_bestPoint
else:
    print('problem: no overloads found on startup. exitting...')
    exit()

overload_total = len(overload_one_allPoints) + (len(overload_two_allPoints)*2) + (len(overload_three_allPoints)*3) + (len(overload_four_allPoints)*4)

print('found %s overload_ones | %s overload_twos | %s overload_threes | %s overload_fours | enough overloads for %s minutes' % (len(overload_one_allPoints), len(overload_two_allPoints), len(overload_three_allPoints), len(overload_four_allPoints), overload_total*5))

#find the protect melee for use in the coming loop
print('opening prayer tab w. f5')
pyautogui.keyDown('f5')
time.sleep(.15 + abs(np.random.normal(.1,.05)))
tick_dropper()
pyautogui.keyUp('f5')

print('looking for protect melee...') 
screenshot = wincap.get_screenshot() #color
protect_melee_allPoints, protect_melee_bestPoint, protect_melee_confidence = protect_melee_vision.find(screenshot, threshold = PRAYER_THRESHOLD, debug_mode= 'rectangles', return_mode = 'allPoints + bestPoint + confidence')
if cv.waitKey(1) == ord('q'):
    cv.destroyAllWindows()
    exit()

if protect_melee_confidence > PRAYER_THRESHOLD:
    print('found protect_melee at %s | confidence %s' % (protect_melee_bestPoint, round(protect_melee_confidence,3)))
else:
    print('no protect_melee found | confidence %s' % round(protect_melee_confidence))

input('press enter to begin...')
#note: you should turn protect melee on shortly before running out of overload, probably using a timer. I'm going to time an overload now. the time from overload click to return to 51 hp is exactly 5:00.
print('Click into game. you have 10 seconds...')
time.sleep(2)
print('Click into game. you have 8 seconds...')
time.sleep(2)
print('Click into game. you have 6 seconds...')
time.sleep(2)
print('Click into game. you have 4 seconds...')
time.sleep(2)
print('Click into game. you have 2 seconds...')
time.sleep(2)
print('we are now behaving as if in game...')
time.sleep(2)

print('setting tab to prayer (f5)')
pyautogui.keyDown('f5')
time.sleep(.15 + abs(np.random.normal(.1,.05)))
tick_dropper()
pyautogui.keyUp('f5')
time.sleep(.15 + abs(np.random.normal(.1,.05)))
tick_dropper()
current_tab = 'f5'



#potion loop will run until it's out of one type of potion
protect_melee_early_time = np.random.normal(protect_melee_early_time_mean, protect_melee_early_time_stdDev)
protect_melee_late_time = np.random.normal(protect_melee_late_time_mean, protect_melee_late_time_stdDev)
flick_early_time = np.random.normal(flick_early_time_mean,flick_early_time_stdDev)
last_overload_time = time.time()
protect_melee_click_time = time.time()
last_flick_time = time.time()
nothing_since_last_flick = True
while True:
    #see if it's time to flick
    if time.time() - last_flick_time > 60 -  flick_early_time:
        print('time to flick! | time since last flick %s | flick_early_time %s' %(time.time()-last_flick_time, flick_early_time))
        #get in the right tab
        if current_tab != 'f5':
            print('opening prayer tab w. f5')
            pyautogui.keyDown('f5')
            time.sleep(.15 + abs(np.random.normal(.1,.05)))
            tick_dropper()
            pyautogui.keyUp('f5')
            time.sleep(.15 + abs(np.random.normal(.1,.05)))
            tick_dropper()
            current_tab = 'f5'
        else:
            print('we are already in the prayer tab')
        
        screenshot = wincap.get_screenshot()
        rapid_heal_allPoints, rapid_heal_bestPoint, rapid_heal_confidence = rapid_heal_vision.find(screenshot, threshold = PRAYER_THRESHOLD, debug_mode= 'rectangles', return_mode= 'allPoints + bestPoint + confidence')
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            exit()
    
        if rapid_heal_confidence > PRAYER_THRESHOLD:
            rapid_heal_screenpoint = wincap.get_screen_position(rapid_heal_bestPoint)
            rapid_heal_clickpoint = rapid_heal_action.click(rapid_heal_screenpoint, speed = speed(), wait=wait(), tick_dropper_odds= 100)
            print('clicked rapid_heal on')
            time.sleep(wait())
            pyautogui.click()
            print('clicked rapid_heal off')
        else: 
            print('could not find rapid heal, quitting...')
            exit()
        
        #generating new values
        last_flick_time = time.time()
        flick_early_time = np.random.normal(flick_early_time_mean,flick_early_time_stdDev)
        nothing_since_last_flick = True


    #see if overload is active by seeing if we have 51 hitpoints (searching in COLOR). This is run on computer vision
    screenshot = wincap.get_screenshot()
    fifty_one_health_allPoints, fifty_one_health_bestPoint, fifty_one_health_confidence = fifty_one_health_vision.find(screenshot, threshold = FIFTY_ONE_HEALTH_THRESHOLD, debug_mode= 'rectangles', return_mode= 'allPoints + bestPoint + confidence')
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        exit()

    #determine if we should protect melee, which should happen shortly before overload runs out. this is run on timing with a computer vision backup
    if time.time() - last_overload_time > 300 - protect_melee_early_time or fifty_one_health_confidence > FIFTY_ONE_HEALTH_THRESHOLD: #ie its been five minutes less the early time since last overload click or I'm seeing the overload has worn off and I haven't turned on melee in the last 10 seconds
        if time.time() - protect_melee_click_time > 10: #ie we havent been down here int eh past 10 seconds
            print('%ss since last overload | protect_melee_early_time %s | turning on protect melee...'% (round(time.time() - last_overload_time,2), round(protect_melee_early_time,2))) 
            if current_tab != 'f5':
                print('opening prayer tab w. f5')
                pyautogui.keyDown('f5')
                time.sleep(.15 + abs(np.random.normal(.1,.05)))
                tick_dropper()
                pyautogui.keyUp('f5')
                time.sleep(.15 + abs(np.random.normal(.1,.05)))
                tick_dropper()
                current_tab = 'f5'
            else:
                print('we are already in the prayer tab')

            screenshot = wincap.get_screenshot()
            protect_melee_allPoints, protect_melee_bestPoint, protect_melee_confidence = protect_melee_vision.find(screenshot, threshold = PRAYER_THRESHOLD, debug_mode= 'rectangles', return_mode= 'allPoints + bestPoint + confidence')
            if cv.waitKey(1) == ord('q'):
                cv.destroyAllWindows()
                exit()
                
            if protect_melee_confidence > PRAYER_THRESHOLD:
                protect_melee_screenpoint = wincap.get_screen_position(protect_melee_bestPoint)
                protect_melee_action.click(protect_melee_screenpoint, speed = speed(), wait=wait(), tick_dropper_odds= 100)
                protect_melee_click_time = time.time() #this prevents us from reentering the melee on section of the loop for the next 10s
                nothing_since_last_flick = False #ie we have to move the mouse back to rapid heal
                print('clicked protect_melee at %s | confidence %s' %(round(protect_melee_click_time), round(protect_melee_confidence,3)))
            else:
                print('cannot find protect_melee | confidence %s | giving up...' %round(protect_melee_confidence,3))
                exit()
            
            #now create a new protect_melee_early_time for next repot
            protect_melee_early_time = np.random.normal(protect_melee_early_time_mean, protect_melee_early_time_stdDev)

        else: #we've been down this road in the last 10s
            pass
    
    #if the overload has run out, repot, wait 7 seconds (plus some random time) to hit 1hp, turn off protect from melee, resorb
    if fifty_one_health_confidence > FIFTY_ONE_HEALTH_THRESHOLD:
        print('I see fifty one health | confidence %s | repotting...' %round(fifty_one_health_confidence,3))
        #hit the next potion
        if current_tab != 'f1':
            print('opening inv tab w. f1')
            pyautogui.keyDown('f1')
            time.sleep(.15 + abs(np.random.normal(.1,.05)))
            tick_dropper()
            pyautogui.keyUp('f1')
            time.sleep(.15 + abs(np.random.normal(.1,.05)))
            tick_dropper()
            current_tab = 'f1'
        else:
            print('we are already in the inventory tab (f1)')
    
        next_overload_screenpoint = wincap.get_screen_position(next_overload)
        next_overload_clickpoint = next_overload_action.click(next_overload_screenpoint, speed = speed(), wait=wait(), tick_dropper_odds= 100)
        nothing_since_last_flick = False #ie we have to move the mouse back to rapid heal
        last_overload_time = time.time() #the next overload becomes the last overload
        print('clicked overload')

        #go to prayer tab in prep for protect from melee turn off
        print('switching to prayer tab (f5)')
        pyautogui.keyDown('f5')
        time.sleep(.15 + abs(np.random.normal(.1,.05)))
        tick_dropper()
        pyautogui.keyUp('f5')
        time.sleep(.15 + abs(np.random.normal(.1,.05)))
        tick_dropper()
        current_tab = 'f5'

        #here we wait for 7 seconds + protect_melee_late_time to have elapsed, then turn off protect from melee. because this takes so long, we also check whether it's time to flick 
        while True:
            #flicker
            if time.time() - last_flick_time > 60 -  flick_early_time:
                print('time to flick! | time since last flick %s | flick_early_time %s' %(time.time()-last_flick_time, flick_early_time))
                
                screenshot = wincap.get_screenshot()
                rapid_heal_allPoints, rapid_heal_bestPoint, rapid_heal_confidence = rapid_heal_vision.find(screenshot, threshold = PRAYER_THRESHOLD, debug_mode= 'rectangles', return_mode= 'allPoints + bestPoint + confidence')
                if cv.waitKey(1) == ord('q'):
                    cv.destroyAllWindows()
                    exit()
    
                if rapid_heal_confidence > PRAYER_THRESHOLD:
                    rapid_heal_screenpoint = wincap.get_screen_position(rapid_heal_bestPoint)
                    rapid_heal_clickpoint = rapid_heal_action.click(rapid_heal_screenpoint, speed = speed(), wait=wait(), tick_dropper_odds= 100)
                    print('clicked rapid_heal on')
                    time.sleep(wait())
                    pyautogui.click()
                    print('clicked rapid_heal off')
                else: 
                    print('could not find rapid heal, quitting...')
                    exit()
                #generating new flick values
                last_flick_time = time.time()
                flick_early_time = np.random.normal(flick_early_time_mean,flick_early_time_stdDev)
                nothing_since_last_flick = True
            
            #when this below condition is satisfied it turns off protect melee and breaks        
            if time.time() - last_overload_time > 7 + protect_melee_late_time:
                screenshot = wincap.get_screenshot()
                if cv.waitKey(1) == ord('q'):
                    cv.destroyAllWindows()
                    exit()
    
                protect_melee_allPoints, protect_melee_bestPoint, protect_melee_confidence = protect_melee_vision.find(screenshot, threshold = PRAYER_THRESHOLD, debug_mode= 'rectangles', return_mode= 'allPoints + bestPoint + confidence')
                if protect_melee_confidence > PRAYER_THRESHOLD:
                    protect_melee_screenpoint = wincap.get_screen_position(protect_melee_bestPoint)
                    protect_melee_action.click(protect_melee_screenpoint, speed = speed(), wait=wait(), tick_dropper_odds= 100)
                    protect_melee_click_time = time.time() #this prevents us from reentering the melee on section of the loop for the next 10s
                    nothing_since_last_flick = False #ie we have to move the mouse back to rapid heal
                    print('clicked (off) protect_melee at %s | confidence %s' %(round(protect_melee_click_time), round(protect_melee_confidence,3)))
                else:
                    print('cannot find protect_melee | confidence %s | giving up...' %round(protect_melee_confidence,3))
                    exit()
                break
            
        #calculate new next_overload
        print('switching to inventory tab (f1)')
        pyautogui.keyDown('f1')
        time.sleep(.15 + abs(np.random.normal(.1,.05)))
        tick_dropper()
        pyautogui.keyUp('f1')
        time.sleep(.15 + abs(np.random.normal(.1,.05)))
        tick_dropper()
        current_tab = 'f1'
        print('finding next_overload...')

        #print overload_ones
        screenshot = wincap.get_screenshot()
        screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY) #grayscale
        overload_one_allPoints, overload_one_bestPoint, overload_one_confidence = overload_one_vision.find(screenshot, threshold = POTION_THRESHOLD, debug_mode= 'rectangles', return_mode = 'allPoints + bestPoint + confidence')
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            exit()
    
        #print('finding overload_twos')
        screenshot = wincap.get_screenshot()
        screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY) #grayscale
        overload_two_allPoints, overload_two_bestPoint, overload_two_confidence = overload_two_vision.find(screenshot, threshold = POTION_THRESHOLD, debug_mode= 'rectangles', return_mode = 'allPoints + bestPoint + confidence')
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            exit()
    
        #print('finding overload_threes')
        screenshot = wincap.get_screenshot()
        screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY) #grayscale
        overload_three_allPoints, overload_three_bestPoint, overload_three_confidence = overload_three_vision.find(screenshot, threshold = POTION_THRESHOLD, debug_mode= 'rectangles', return_mode = 'allPoints + bestPoint + confidence')
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            exit()
    
        #print('finding overload_fours')
        screenshot = wincap.get_screenshot() 
        screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY) #grayscale
        overload_four_allPoints, overload_four_bestPoint, overload_four_confidence = overload_four_vision.find(screenshot, threshold = POTION_THRESHOLD, debug_mode= 'rectangles', return_mode = 'allPoints + bestPoint + confidence')
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            exit()
    

        #define the next overload for use in coming loop
        #print('looking for overloads...')
        if overload_one_confidence > POTION_THRESHOLD:
            next_overload = overload_one_bestPoint
            print('found next_overload | confidence %s'% overload_one_confidence)
        elif overload_two_confidence > POTION_THRESHOLD:
            next_overload = overload_two_bestPoint
            print('found next_overload | confidence %s'% overload_two_confidence)
        elif overload_three_confidence > POTION_THRESHOLD:
            next_overload = overload_three_bestPoint
            print('found next_overload | confidence %s'% overload_three_confidence)
        elif overload_four_confidence > POTION_THRESHOLD:
            next_overload = overload_four_bestPoint
            print('found next_overload | confidence %s'% overload_four_confidence)
        else:
            print('problem: no overloads found for next click. exitting...')
            exit()

        #this loop resorbs until it sees the no more resorb message
        print('we will now resorb...')
        while True:
            screenshot = wincap.get_screenshot() 
            screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY) #grayscale
            sorb_four_allPoints, sorb_four_bestPoint, sorb_four_confidence = sorb_four_vision.find(screenshot, threshold = POTION_THRESHOLD, debug_mode= 'rectangles', return_mode = 'allPoints + bestPoint + confidence')
            if cv.waitKey(1) == ord('q'):
                cv.destroyAllWindows()
                exit()
    





#everything below is scrap and template, not written for this program.

#genius moment: the wait time distribution changes every session. completely undetectable. Smooth like a bald man's head. 
protect_melee_early_time_mean = np.random.uniform(.3,2)
protect_melee_early_time_stdDev = protect_melee_early_time_mean/6

three_tick_wait_time_mean = np.random.uniform(1.2,2.5)
three_tick_wait_time_stdDev = three_tick_wait_time_mean/6




def fish_n_cut():
    loop_time = time.time()
    green_fish_click_time = time.time()
    green_fish_bestPoint_OLD = []      
    green_fish_confidence_OLD = 1 
    cycle_even = False
    cutting = False
    while True:
        if green_fish_confidence_OLD > .85: #ie if the previous fish was really green (ie .85 or higher confidence), wait for what will be two ticks (minus .5s find +move+wait+click time) then proceed to finding
            two_tick_wait =np.random.normal(two_tick_wait_time_mean,two_tick_wait_time_stdDev) #.8,.08 works well
            while time.time() - green_fish_click_time < two_tick_wait:
                pass
            timing_belt = two_tick_wait +.5 #we add the .5 because we expect about .5s of bullshit to happen between now and the click

        else: #if the previous fish was really blue (less than .85 confidence green fish), wait (waht will be) 3 ticks (after serachign, moving, and waiting time elapse)
            three_tick_wait = np.random.normal(three_tick_wait_time_mean,three_tick_wait_time_stdDev) #1.3,.12 works well
            while time.time() - green_fish_click_time < three_tick_wait:
                pass
            timing_belt = three_tick_wait +.5 #we add the .5 because we expect about .5s of bullshit to happen between now and the click

        #this line below is left in for debugging if needed
        #pre_find_wait_click_time = time.time()

        #we find and click the green fish. simple as. 
        screenshot = wincap.get_screenshot()
        screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
        green_fish_allPoints, green_fish_bestPoint, green_fish_confidence = green_fish_vision.find(screenshot, threshold = GREEN_FISH_THRESHOLD, debug_mode= 'rectangles', return_mode= 'allPoints + bestPoint + confidence')
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            exit()
        
        #this line below is left in for debugging if needed
        #fish_find_time = time.time() - pre_find_wait_click_time
        
        #if the best fish is an old fish, AND you didn't cut last cycle, the mouse is still hovering over it and you should just click the mouse again
        if green_fish_bestPoint == green_fish_bestPoint_OLD and cutting == False:
            best_fish_old_fish = True
            time.sleep(.5)
            tick_dropper()
            pyautogui.click()
            actual_wait_time = time.time() - green_fish_click_time
            green_fish_click_time = time.time()
        
        #if it's not this unusual case, then set up and click as usual
        else:
            best_fish_old_fish = False
            green_fish_screenPoint = wincap.get_screen_position(green_fish_bestPoint)
            tick_dropper()
            green_fish_click_point = green_fish_action.click(green_fish_screenPoint, speed = speed(), wait=wait(), no_post_click_wait= True)
            #this line below is left in for debugging if needed
            #move_wait_click_time = time.time() - pre_find_wait_click_time - fish_find_time
            actual_wait_time = time.time() - green_fish_click_time
            green_fish_click_time = time.time()

            

        #we can't look fast enough to cut fish every cycle. It's not that the cycle runs long if we cut, it's that looking for cuttable fish takes so long that we have to start shortly after the last cut action. Most of the fish found there will disappear next tick and we click the empty spaces
        #solution to cut time problem: only cut on even cycles, ie every other cycle, and when it was a non-green fish click.

        #this defines the fast cut condition
        if cutting == False and green_fish_confidence < .85: #ie we didn't cut last time and it was NOT a green fish click (ie it will take 3+ ticks to resolve)
            cutting = True
            #we're looking for knife
            screenshot = wincap.get_screenshot()
            screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
            knife_allPoints, knife_bestPoint, knife_confidence = knife_vision.find(screenshot, threshold = KNIFE_THRESHOLD, debug_mode= 'rectangles', return_mode = 'allPoints + bestPoint + confidence')
            knife_screenpoint = wincap.get_screen_position(knife_bestPoint)
            if cv.waitKey(1) == ord('q'):
                cv.destroyAllWindows()
                exit()

            #we're looking for inv. fish
            screenshot = wincap.get_screenshot()
            screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
            inv_fish_allPoints, inv_fish_bestPoint, inv_fish_confidence = inv_fish_vision.find(screenshot, threshold = INV_FISH_THRESHOLD, debug_mode= 'rectangles', return_mode= 'allPoints + bestPoint + confidence')
            if cv.waitKey(1) == ord('q'):
                cv.destroyAllWindows()
                exit()

            #if we see inv. fish, we cut it up before the next click
            if inv_fish_confidence > INV_FISH_THRESHOLD:
                tick_dropper()
                knife_click = knife_action.click(knife_screenpoint, speed = speed(), wait=wait()-.02, tick_dropper_odds= 100)
                fish_screenpoint = wincap.get_screen_position(inv_fish_bestPoint)
                tick_dropper()
                fish_click = inv_fish_action.click(fish_screenpoint, speed = speed()-.1, wait=wait()-.02, no_post_click_wait = True, tick_dropper_odds= 100)
            
            #we're looking for inv. tench
            screenshot = wincap.get_screenshot()
            screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
            inv_tench_allPoints, inv_tench_bestPoint, inv_tench_confidence = inv_tench_vision.find(screenshot, threshold = INV_TENCH_THRESHOLD, debug_mode= 'rectangles', return_mode= 'allPoints + bestPoint + confidence')
            if cv.waitKey(1) == ord('q'):
                cv.destroyAllWindows()
                exit()

            #if we see inv. tench, cut it up before the next click
            if inv_tench_confidence > INV_TENCH_THRESHOLD:
                knife_click = knife_action.click(knife_screenpoint, speed = speed(), wait=wait()-.02, tick_dropper_odds= 100)
                tench_screenpoint = wincap.get_screen_position(inv_tench_bestPoint)
                tick_dropper()
                tench_click = inv_tench_action.click(tench_screenpoint, speed = speed()-.1, wait=wait()-.02, no_post_click_wait = True, tick_dropper_odds= 100)

        else: #we're not cutting this cycle, but we still have to look for inv_fish and inv_tench to make sure we're not full inventory. This could theoretically be removed if you trusted the cut condition to cut enough (it only cuts at most 2 per call)
            #we're looking for inv. fish
            cutting = False
            screenshot = wincap.get_screenshot()
            screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
            inv_fish_allPoints, inv_fish_bestPoint, inv_fish_confidence = inv_fish_vision.find(screenshot, threshold = INV_FISH_THRESHOLD, debug_mode= 'rectangles', return_mode= 'allPoints + bestPoint + confidence')
            if cv.waitKey(1) == ord('q'):
                cv.destroyAllWindows()
                exit()

            #we're looking for inv. tench
            screenshot = wincap.get_screenshot()
            screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
            inv_tench_allPoints, inv_tench_bestPoint, inv_tench_confidence = inv_tench_vision.find(screenshot, threshold = INV_TENCH_THRESHOLD, debug_mode= 'rectangles', return_mode= 'allPoints + bestPoint + confidence')
            if cv.waitKey(1) == ord('q'):
                cv.destroyAllWindows()
                exit()
            
            if len(inv_fish_allPoints + inv_tench_allPoints) > 20:
                print('at least 21 fish, exiting fishloop')
                break


        #debuggery
        print('cutting? %s | intended wait %ss |actual wait %s |green_fish_conf %s |num inv_fish %s conf. %s |num inv_tench %s conf. %s' % (cutting, round(timing_belt,2), round(actual_wait_time,2), round(green_fish_confidence,2), len(inv_fish_allPoints), round(inv_fish_confidence,3), len(inv_tench_allPoints), round(inv_tench_confidence,3)))
        #print('timing_belt debug | timing_belt %s | fish_find_time %s | move_wait_click_time %s | TOTAL TIME STALL %s | cutting? %s' %(timing_belt, fish_find_time, move_wait_click_time, timing_belt + fish_find_time + move_wait_click_time, cutting))


        #the new fish becomes the old fish
        green_fish_bestPoint_OLD = green_fish_bestPoint    
        green_fish_confidence_OLD = green_fish_confidence
        
        breakroller()
        #defunct
        '''
        #the even cycle becomes the odd cycle
        if cycle_even == True:
            cycle_even = False
        
        else: cycle_even = True
        pass
        '''
#we should not  have to use this cutloop much anymore. I leave it in  as a failsafe for fuckups. 
def cut_backup():
    print('cutting up the fish')
    screenshot = wincap.get_screenshot()
    screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
    inv_fish_allPoints, inv_fish_bestPoint, inv_fish_confidence = inv_fish_vision.find(screenshot, threshold = INV_FISH_THRESHOLD, debug_mode= 'rectangles', return_mode= 'allPoints + bestPoint + confidence')

    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        exit()        

    screenshot = wincap.get_screenshot()
    screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
    knife_allPoints, knife_bestPoint, knife_confidence = knife_vision.find(screenshot, threshold = KNIFE_THRESHOLD, debug_mode= 'rectangles', return_mode = 'allPoints + bestPoint + confidence')
    knife_screenpoint = wincap.get_screen_position(knife_bestPoint)

    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        exit()

    tick_dropper()
    knife_click = knife_action.click(knife_screenpoint, speed = speed(), wait=wait(), tick_dropper_odds= 100)
    time.sleep(abs(np.random.normal(.1,.02)))
    fish_screenpoint = wincap.get_screen_position(inv_fish_bestPoint)
    tick_dropper()
    fish_click = inv_fish_action.click(fish_screenpoint, speed = speed()-.15, wait=wait(), tick_dropper_odds= 100)
    time.sleep(21 + abs(np.random.normal(0,.8)))

    #this is if you want to click FAST
    '''
    for fish in inv_fish_allPoints:
        time.sleep(abs(np.random.normal(.1,.02)))
        knife_click = knife_action.click(knife_screenpoint)

        time.sleep(abs(np.random.normal(.1,.02)))
        fish_screenpoint = wincap.get_screen_position(fish)
        fish_click = inv_fish_action.click(fish_screenpoint)
    '''


def breakroller():
    if breakroll := np.random.random() < .000666: #this is about 1 in 1500. I figure I run the loop 3000 times per hour
        sleep_time = np.random.random() * 220
        print('sleeping for %s out of a possible 220 seconds' % sleep_time)
        wind_mouse(pyautogui.position()[0], pyautogui.position()[1], 0,0)
        time.sleep(sleep_time)

quit_after = float(input('please enter the number of seconds to run for, then press enter. 1h = 3600s, 6h = 21600'))
runStart = time.time()
while True:
    fish_n_cut()
    cut_backup()
    breakroller()
    runTime = time.time() - runStart
    if runTime > quit_after:
        print('finished after running for %s seconds' % runTime)
        exit()
    print('runtime = %s | seconds remaining = %s' %(runTime, (quit_after - runTime)))
    

