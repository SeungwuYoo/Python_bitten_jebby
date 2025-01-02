from num_screens import render_number
import numpy as np
import time

class elec_jebby:
    def __init__(self, seed=None, 
                 jebby_prgm=['master', 'doctor'], 
                 jebby_rate=[21, 37], 
                 jebby_room=['204', '212B', '214', '314'], 
                 jebby_seat=[14, 11, 19, 13]
                 ):
        np.random.seed(seed)
        self.seed = seed
        self.jebby_prgm = np.array(jebby_prgm)
        self.jebby_rate = np.array(jebby_rate)
        self.jebby_room = np.array(jebby_room)
        self.jebby_seat = np.array(jebby_seat)
        self.jebby_aloc = np.zeros(len(jebby_room))
        
        self.act_name = []
        self.act_history = []
        
        self.td = 1
        
    def confirm_int(self, act, errortext=None, errorshow=False):
        try:
            act = int(act)
            return act
        except ValueError:
            if errorshow:
                print(errortext)
                return None
            else:
                return None
        
    def confirm_init(self):
        dict_init = {}
        
        prev_seed = self.seed
        react = input(f"Initial seed is {self.seed}, do you want to switch this? (Yes: 0, No: all the others) : ")        
        react = self.confirm_int(react)
        
        if react == 0:
            while True:
                curr_seed = input("Enter your seed : ")
                curr_seed = self.confirm_int(curr_seed, errortext="Please enter an integer as a seed!", errorshow=True)
                if curr_seed is not None:
                    break
            if type(curr_seed) is int and curr_seed >= 0:
                np.random.seed(curr_seed)
                self.seed = curr_seed
                dict_init['seed'] = (prev_seed, curr_seed)
            else:
                print("Please enter an integer larger than 0 as a seed!")
        else:
            dict_init['seed'] = (prev_seed, prev_seed)
        
        prev_prgm, curr_prgm = self.jebby_prgm, []
        react = input(f"Initial program set is {self.jebby_prgm}, do you want to switch this? (Yes: 0, No: all the others) : ")        
        react = self.confirm_int(react)
        
        if react == 0:
            while True:
                time.sleep(self.td)
                print("-------------------------------------------------------")
                print(f"Current program set: {curr_prgm}")
                print("If you want to interupt, enter the \'stop\'")
                print("If you want to wrap up the program set recording, enter the \'end\'")
                print("Z: Control Z")
                print("-------------------------------------------------------")
                prgm_name = input("Enter a program name : ")
                if prgm_name == 'stop':
                    dict_init['prgm'] = (prev_prgm, prev_prgm)
                    break
                elif prgm_name == 'end':
                    dict_init['prgm'] = (prev_prgm, curr_prgm)
                    self.jebby_prgm = curr_prgm
                    break
                elif prgm_name == 'Z' and len(curr_prgm) > 0:
                    curr_prgm = curr_prgm[:-1]
                elif prgm_name == 'Z' and len(curr_prgm) == 0:
                    print("Current program set doesn\'t have any element!")
                else:
                    curr_prgm.append(prgm_name)
        else:
            curr_prgm = self.jebby_prgm
            dict_init['prgm'] = (prev_prgm, curr_prgm)
        
        prev_rate, curr_rate = [], []
        for i, prgm in enumerate(self.jebby_prgm):
            try:
                prev_rate.append(self.jebby_rate[i])
            except IndexError:
                pass

            try:
                react = input(f"Initial number of {prgm} is {self.jebby_rate[i]}, do you want to switch this? (Yes: 0, No: all the others) : ")
                react = self.confirm_int(react)
            except IndexError:
                react = input(f"Initial number of {prgm} has no value, do you want to switch this? (Yes: 0, No: all the others -> Input 0) : ")
                react = self.confirm_int(react)
            
            if react == 0:
                while True:
                    rate = input(f"Enter the number of {prgm} : ")               
                    rate = self.confirm_int(rate, errortext=f"Please enter an interger as a number of {prgm}!", errorshow=True)
                    if rate is None:
                        continue
                    if rate < 0 and type(rate) is int:
                        print("Please enter an integer larger than 0 as a number!")
                        continue
                    elif type(rate) is int:
                        curr_rate.append(rate)
                        break
            else:
                try:
                    curr_rate.append(self.jebby_rate[i])
                except IndexError:
                    curr_rate.append(0)
        
        dict_init['rate'] = (prev_rate, curr_rate)
        self.jebby_rate = curr_rate
        
        prev_room, curr_room = self.jebby_room, []
        react = input(f"Initial room set is {self.jebby_room}, do you want to switch this? (Yes: 0, No: all the others) : ")        
        react = self.confirm_int(react)
        
        if react == 0:
            while True:
                time.sleep(self.td)
                print("-------------------------------------------------------")
                print(f"Current room set: {curr_room}")
                print("If you want to interupt, enter the \'stop\'")
                print("If you want to wrap up the program set recording, enter the \'end\'")
                print("Z: Control Z")
                print("-------------------------------------------------------")
                room_name = input("Enter a room name : ")
                if room_name == 'stop':
                    dict_init['room'] = (prev_room, prev_room)
                    break
                elif room_name == 'end':
                    dict_init['room'] = (prev_room, curr_room)
                    self.jebby_room = curr_room
                    break
                elif room_name == 'Z' and len(curr_room) > 0:
                    curr_room = curr_room[:-1]
                elif room_name == 'Z' and len(curr_room) == 0:
                    print("Current program set doesn\'t have any element!")
                else:
                    curr_room.append(room_name)
        
        prev_seat, curr_seat = [], []
        for i, room in enumerate(self.jebby_room):
            try:
                prev_seat.append(self.jebby_seat[i])
            except IndexError:
                pass
            
            try:
                react = input(f"Initial seat of {room} is {self.jebby_seat[i]}, do you want to switch this? (Yes: 0, No: all the others) : ")
                react = self.confirm_int(react)
            except IndexError:
                react = input(f"Initial number of {room} has no value, do you want to switch this? (Yes: 0, No: all the others -> Input 0) : ")
                react = self.confirm_int(react)
            
            if react == 0:
                while True:
                    seat = input(f"Enter the number of {room} : ")                    
                    seat = self.confirm_int(seat, errortext=f"Please enter an interger as a number of {prgm}!", errorshow=True)
                    if seat is None:
                        continue
                    if seat < 0 and type(seat) is int:
                        print("Please enter an integer larger than 0 as a number!")
                        continue
                    elif type(seat) is int:
                        curr_seat.append(seat)
                        break
            else:
                try:
                    curr_seat.append(self.jebby_seat[i])
                except IndexError:
                    curr_seat.append(0)
        
        dict_init['seat'] = (prev_seat, curr_seat)
        self.jebby_seat = curr_seat
        
        if sum(curr_rate) > sum(curr_seat):
            print('Caution! : The total number of people exceed number of seats!')
        
        self.act_history.append(dict_init)
        self.act_name.append("init_confirm")
        
    def room_prgmnum_calculator(self):
        prgmlist, alphalist = [], []
        for i, room in enumerate(self.jebby_room):
            seatnum = self.jebby_seat[i]
            
            prgmfloat = seatnum * np.array(self.jebby_rate) / np.sum(self.jebby_rate)
            prgmint = prgmfloat.astype(int)
            alphanum = prgmfloat - prgmint
            
            prgmlist.append(prgmint)
            alphalist.append(alphanum)
            '''alphasum, alphasort = int(np.sum(alphanum)), np.argsort(alphanum)
            remain = np.zeros(len(self.jebby_prgm))
            remain[np.argsort(alphasort)[::-1][:alphasum]] = 1
            
            prgmnum = prgmint + remain
            seatlist.append(prgmnum)'''
        
        prgmarr, alphaarr = np.array(prgmlist), np.array(alphalist)
        
        for j, prgm in enumerate(self.jebby_prgm):
            prgm_lack = int(self.jebby_rate[j] - np.sum(prgmarr.T[j]))
            remain = np.zeros(len(self.jebby_room), dtype=int)
            remain[np.argsort(alphaarr.T[j])[::-1][:prgm_lack]] = 1
            prgmarr.T[j] += remain
            
        for i, room in enumerate(self.jebby_room):
            for j, prgm in enumerate(self.jebby_prgm):
                print(f'program {prgm} in room {room} : {prgmarr[i][j]} seats!')
        
        self.seatnum_arr = prgmarr.T
        historyshow = []
        for j, prgm in enumerate(self.jebby_prgm):
            historyshow.append(prgm)
            historyshow.append(tuple(prgmarr.T[j].astype(int)))
        self.act_history.append(tuple(historyshow))
        self.act_name.append("room_prgm_num")
        
    def room_choice(self):
        print("-------------------------------------------------------")
        for i, prgm in enumerate(self.jebby_prgm):
            print(f'{i}: {prgm}')
        print("-------------------------------------------------------")
        
        while True:
            prgm_act = input("Choose your program with an integer : ")
            prgm_act = self.confirm_int(prgm_act, errortext='Please enter an interger!', errorshow=True)
            if prgm_act not in list(np.arange(len(self.jebby_prgm)).astype(int)):
                print(f'Please enter between {list(np.arange(len(self.jebby_prgm)).astype(int))}')
                continue
            if prgm_act is not None:
                break
        room_remains = self.seatnum_arr[prgm_act]
        num_remains = np.sum(room_remains)
        
        print("-------------------------------------------------------")
        for i, room in enumerate(self.jebby_room):
            print(f'{room} : {room_remains[i]}')
        print("-------------------------------------------------------")
        
        _ = input("Press enter if you want to check your room : ")
        time.sleep(self.td)
        
        while True:
            if num_remains < 1:
                break
            jebby = np.random.choice(np.arange(num_remains))
            for i in range(len(room_remains)):
                if jebby < sum(room_remains[:i + 1]):
                    room_act = i
                    break
                if i == len(room_remains) - 1:
                    room_act = i
            
            if room_remains[room_act] > 0:
                render_number(self.jebby_room[room_act])
                self.seatnum_arr[prgm_act][room_act] -= 1
                self.jebby_aloc[room_act] += 1
                break
        
        self.act_name.append("room_choice")
        self.act_history.append([prgm_act, self.jebby_prgm[prgm_act], room_act, self.jebby_room[room_act]])
            
    def seat_choice(self):
        print("-------------------------------------------------------")
        for i, room in enumerate(self.jebby_room):
            seatnum, alocnum = self.jebby_seat[i], self.jebby_aloc[i]
            print(f'{i}: {room} ({int(seatnum)} seats, {int(alocnum)} allocated)')
        print("-------------------------------------------------------")
        while True:
            room_act = input("Choose your room with an integer : ")
            room_act = self.confirm_int(room_act, errortext='Please enter an interger!', errorshow=True)
            if room_act not in list(np.arange(len(self.jebby_room)).astype(int)):
                print(f'Please enter between {list(np.arange(len(self.jebby_room)).astype(int))}')
                continue
            if room_act is not None:
                break
        seatnum = self.jebby_aloc[room_act]
        
        if seatnum == 1:
            print("Only one seat allocated, you don\'t need to pick order")
            return True
        
        order_already, order_yet = [], list(np.arange(seatnum) + 1)
        while True:
            print("-------------------------------------------------------")
            print("If you want to interupt, enter the \'stop\'")
            print("Z: Control Z")
            print("-------------------------------------------------------")
            react = input("Press enter if you want to check your order : ")
            if react == "Z" and len(order_already) == 0:
                self.ctrlz()
                return True
            elif react == "Z":
                self.ctrlz()
                order_yet.append(order_already[-1])
                order_already = order_already[:-1]
                time.sleep(self.td)
            elif react == 'stop':
                return True
            else:
                order = int(np.random.choice(order_yet))
                order_already.append(order)
                order_yet.remove(order)
                self.act_history.append([room_act, self.jebby_room[room_act], order])
                self.act_name.append("seat_choice")
                render_number(order)
                time.sleep(self.td)
                if len(order_yet) == 0:
                    print(f'All members in {self.jebby_room[room_act]} are allocated')
                    break
        
    def fixed_room_setting(self):
        print("-------------------------------------------------------")
        for i, prgm in enumerate(self.jebby_prgm):
            print(f'{i}: {prgm}')
        print("-------------------------------------------------------")
        while True:
            prgm_act = input("Choose your program with an integer : ")
            prgm_act = self.confirm_int(prgm_act, errortext='Please enter an interger!', errorshow=True)
            if prgm_act not in list(np.arange(len(self.jebby_prgm)).astype(int)):
                print(f'Please enter between {list(np.arange(len(self.jebby_prgm)).astype(int))}')
                continue
            if prgm_act is not None:
                break
        
        print("-------------------------------------------------------")
        for i, room in enumerate(self.jebby_room):
            seatnum, alocnum = self.jebby_seat[i], self.jebby_aloc[i]
            print(f'{i}: {room} ({int(seatnum)} seats, {int(alocnum)} allocated)')
        print("-------------------------------------------------------")
        while True:
            room_act = input("Choose your room with an integer : ")
            room_act = self.confirm_int(room_act, errortext='Please enter an interger!', errorshow=True)
            if room_act not in list(np.arange(len(self.jebby_prgm)).astype(int)):
                print(f'Please enter between {list(np.arange(len(self.jebby_room)).astype(int))}')
                continue
            if room_act is not None:
                break
        
        self.seatnum_arr[prgm_act][room_act] -= 1
        self.jebby_aloc[room_act] += 1
        
        self.act_history.append([prgm_act, self.jebby_prgm[prgm_act], room_act, self.jebby_room[room_act]])
        self.act_name.append("fixed_room_setting")
        
    def ctrlz(self):
        actname, act = self.act_name[-1], self.act_history[-1]
        if actname == 'init_confirm':
            self.seed = act['seed'][0]
            self.jebby_prgm = act['prgm'][0]
            self.jebby_rate = act['rate'][0]
            self.jebby_room = act['room'][0]
            self.jebby_seat = act['seat'][0]
            time.sleep(self.td)
        elif actname == 'room_prgm_num':
            self.seatnum_arr = None
            time.sleep(self.td)
        elif actname == 'room_choice':
            prgm_act, room_act = act[0], act[2]
            self.seatnum_arr[prgm_act][room_act] += 1
            self.jebby_aloc[room_act] -= 1
            time.sleep(self.td)
        elif actname == 'seat_choice':
            time.sleep(self.td)
        elif actname == 'fixed_room_setting':
            prgm_act, room_act = act[0], act[2]
            self.seatnum_arr[prgm_act][room_act] += 1
            self.jebby_aloc[room_act] -= 1
            time.sleep(self.td)
        
        print(f'Revert {actname} : {act}')
        self.act_name = self.act_name[:-1]
        self.act_history = self.act_history[:-1]        
        
    def acting(self):
        print("-------------------------------------------------------")
        print("If you want to end program, enter the \'stop\'")
        print("-------------------------------------------------------")
        print("Z: Control Z")
        print("1: Confirm the initial stage")
        print("2: Calculate the seat number for each room and program")
        print("3: Room choice")
        print("4: Seat choice")
        print("5: Fixed room setting")
        print("6: Read process")
        print("-------------------------------------------------------")
        act = input("Choose your act with an integer : ")
        try:
            act = int(act)
        except ValueError:
            if act == 'stop':
                time.sleep(self.td)
                react = input('Really? (Yes: 0, No: any other) : ')
                if react == '0':
                    return False
                else:
                    return True
            elif act == 'Z':
                time.sleep(self.td)
                eeje.ctrlz()
            print("Please enter an integer!")
            return True
        if act == 6:
            for i, actname in enumerate(self.act_name):
                print(f'{actname} : {self.act_history[i]}')
            time.sleep(2 * self.td)
            print('return to main menu')
            time.sleep(self.td)
            return True
        elif act == 1:
            self.confirm_init()
            return True
        elif act == 2:
            self.room_prgmnum_calculator()
            time.sleep(2 * self.td)
            print('return to main menu')
            time.sleep(self.td)
            return True
        elif act == 1220:
            print(self.seatnum_arr)
            time.sleep(2 * self.td)
            print('return to main menu')
            time.sleep(self.td)
            return True
        elif act == 3:
            self.room_choice()
            time.sleep(2 * self.td)
            print('return to main menu')
            time.sleep(self.td)
            return True
        elif act == 4:
            self.seat_choice()
            time.sleep(2 * self.td)
            print('return to main menu')
            time.sleep(self.td)
            return True
        elif act == 5:
            self.fixed_room_setting()
            time.sleep(2 * self.td)
            print('return to main menu')
            time.sleep(self.td)
            return True
        elif act == 8507:
            td = input('Set time delay unit : ')
            try:
                td = float(td)
            except:
                td = None
                print('Please enter a float as time delay')
            if td is not None:
                self.td = td
                print(f'Set time delay unit as {td} s')                
            return True
        else:
            print(f"{act} has no option")
            time.sleep(2 * self.td)
            print('return to main menu')
            time.sleep(self.td)
            return True
        
                
if __name__ == "__main__":
    eeje = elec_jebby()
    
    while True:
        repeat = eeje.acting()
        if not repeat:
            break
            
            
