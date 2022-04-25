import tkinter as tk
import json

HEIGHT = 600
WIDTH = 1000

def get_content():
    print("hello")
    with open('content.js') as f:
        data = json.load(f)
        print (data)
    content_json = data[0]
    title = content_json['title']
    content = content_json['content']    
  
    output = tk.Text(frame, width = 75, height = 60, bg = "#FCFBF4", font="none 12 bold")
    output.place(relwidth= 1, relheight=1)
    output.insert(tk.END, title)
    output.insert(tk.END, "\n\n")
    output.insert(tk.END, content)

def get_score(rate):
    with open('content.js') as f:
        data = json.load(f)
        #print (data)
    content_json = data[0]
    
    current_voted = content_json["voted"]
    current_score = content_json["score"]
    vote_times = current_voted + 1
    score = current_score + rate 
    print(vote_times, score)
    final_score = "{:.2f}".format(score/vote_times)
    print(final_score)
    rate_label['text'] = final_score

root = tk.Tk()

canvas = tk.Canvas(root, height= HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg= "#FCFBF4", bd= 5)
frame.place(relheight=0.9, relwidth= 0.9, relx= 0.02, rely = 0.05)

button_get_content = tk.Button(root, text = " Get\nContent ", bg = "#e2eaf2", font=40, command=get_content)
button_get_content.place(relx = 0.92, rely = 0.02, relwidth= 0.08, relheight=0.1)

rate_label_title=tk.Label(root, text = 'Rates:', bg = "#e2eaf2", font=40)
rate_label_title.place(relx = 0.92, rely = 0.15, relwidth= 0.08, relheight=0.1)
rate_label=tk.Label(root, text = '0', bg = "#e2eaf2", font=40)
rate_label.place(relx = 0.92, rely = 0.22, relwidth= 0.08, relheight=0.1)

# rate_frame = tk.Frame(root, bg="blue")
# rate_frame.place(relx = 0.5, rely= 0.9, relwidth= 0.9, relheight=0.12, anchor='n')

#Thumbs up button 
# photo_up_1 = tk.PhotoImage(file = r'small_down.png')
# button_up2 = tk.Button(root, text = " Rate up 2 ", image= photo_up_1)
# button_up2.place(relx = 0.25, rely = 0.9, relwidth= 0.1, relheight=0.1)

button_up2 = tk.Button(root, text = " Rate up 2 ", bg = "#ffbf00", command=lambda: get_score(2))
button_up2.place(relx = 0.25, rely = 0.9, relwidth= 0.1, relheight=0.1)

button_up1 = tk.Button(root, text = " Rate up 1 ", bg = "#ffbf00", command=lambda: get_score(1))
button_up1.place(relx = 0.38, rely = 0.9, relwidth= 0.1, relheight=0.1)

button_up2 = tk.Button(root, text = " Rate down 2 ", bg = "#ffbf00", command=lambda: get_score(-2))
button_up2.place(relx = 0.65, rely = 0.9, relwidth= 0.1, relheight=0.1)

button_up1 = tk.Button(root, text = " Rate down 1 ", bg = "#ffbf00", command=lambda: get_score(-1))
button_up1.place(relx = 0.78, rely = 0.9, relwidth= 0.1, relheight=0.1)

# entry = tk.Entry(frame, bg ="#f9ecf9", font = 40)
# entry.place(relwidth = 0.65, relheight= 1, relx = 0.78)

root.mainloop()

