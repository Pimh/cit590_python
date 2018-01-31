'''CIT590 HW6 - Voting Booth
Pimkhuan (Pim) Hannanta-anan
Due 10/18/2016'''

from tkinter import *

'''Functions for the buttons'''
global vcount
vcount = [0,0,0,0]

window = Tk()
window['bg'] = 'white'

'''Set up frame'''
frame1 = Frame(window, bg = 'white')
frame1.pack(side = 'top')
frame2 = Frame(window, bg = 'white')
frame2.pack(side = 'top')
frame3 = Frame(window, bg = 'white')
frame3.pack(side = 'bottom')

def press(butt):
    vcount[butt] += 1
    print_points()
    print_winner()

def print_points():
    '''Number of votes'''
    point1 = Label(frame2, text = str(vcount[0]))
    point1.grid(row = 1, column = 1)
    point2 = Label(frame2, text = str(vcount[1]))
    point2.grid(row = 2, column = 1)
    point3 = Label(frame2, text = str(vcount[2]))
    point3.grid(row = 3, column = 1)
    point3 = Label(frame2, text = str(vcount[3]))
    point3.grid(row = 4, column = 1)    

def print_winner():
    '''Display the winner'''
    butt_dict = {0:"Lionel Messi", 1:"Cristiano Ronaldo", 2:"Alexis Sanchez",
                 3:"Paul Cheh"}
    if vcount.count(max(vcount)) > 1:
        msg = "Tied!"
    else:
        max_vote_key = vcount.index(max(vcount))
        max_vote = butt_dict[max_vote_key]
        msg = "Man of the match is "+ max_vote + "!"
    msg = Label(frame3, text= msg, width = 30)
    msg.grid(row = 0, column = 0)
    
def main():
    '''Heading label'''
    head = Label(frame1, text="Vote for man of the match!", bg = 'darkred',
                 width = 30)
    head.pack()

    '''Column labels'''
    col_head1 = Label(frame2, text="Candidates")
    col_head1.grid(row = 0, column = 0)
    col_head2 = Label(frame2, text="Points")
    col_head2.grid(row = 0, column = 1, padx = 15)
    
    '''Option buttons'''
    butt1 = Button(frame2, text="Lionel Messi", command=lambda: press(0))
    butt1.grid(row = 1, column = 0)
    butt2 = Button(frame2, text="Cristiano Ronaldo", command=lambda: press(1))
    butt2.grid(row = 2, column = 0)
    butt3 = Button(frame2, text="Alexis Sanchez", command=lambda: press(2))
    butt3.grid(row = 3, column = 0)
    butt4 = Button(frame2, text="Paul Cheh", command=lambda: press(3))
    butt4.grid(row = 4, column = 0)
    
    mainloop()

main()

