import sys
import pyperclip
import json

SAVED_DATA = "clip-board.json"

def save_data(filepath, data):
    with open(filepath,"w") as f:
        json.dump(data, f)

#save_items("test.json",{"key2":"value2"})

def load_data(filepath):
    try:
        with open(filepath,"r") as f:
            data = json.load(f)
            return data
    except:
        return {}

if len(sys.argv)==2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)  # Calling load_data function to store Initialise the data.
    
    if command == "save":
        key = input("Enter a key: ")
        data[key] = pyperclip.paste()
        save_data(SAVED_DATA, data)
        print("Data Saved !")

    elif command =="load":
        key= input("Enter a key: ")
        if key in data:
            pyperclip.copy(data[key])
            print("Data copied to clipboard")

    elif command =="list":
        print(data)
    else:
        print("Unknown command")

else:
    print("Please pass exactly one commmand")