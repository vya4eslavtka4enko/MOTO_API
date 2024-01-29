import requests
import os
import tkinter


class Motorcycle():
    def __init__(self):
        window = tkinter.Tk()
        window.geometry("600x400")
        self.company = tkinter.Label(window, text="COMPANY")
        self.company.grid(row=0, column=1)
        self.company_entry = tkinter.Entry(window, bd=2)
        self.company_entry.grid(row=0, column=2)
        self.company = tkinter.Label(window, text="MODEL")
        self.company.grid(row=1, column=1)
        self.model_entry = tkinter.Entry(window, bd=2)
        self.model_entry.grid(row=1, column=2)
        self.get_button = tkinter.Button(text="Click", command=self.make_request)
        self.get_button.grid(row=0, column=3)
        window.mainloop()

    def make_request(self):
        company = self.company_entry.get()
        model = self.model_entry.get()
        api_url = f'https://api.api-ninjas.com/v1/motorcycles?make={company}&model={model}'
        response = requests.get(api_url, headers={'X-Api-Key': os.environ['API_NIN']})
        if response.status_code == requests.codes.ok:
            list_moto = list(response.json())
            print(list_moto[0])
            # with open('model.txt', "w") as file:
            #     file.write(response[0].text)
            #     file.close()
        else:
            print("Error:", response.status_code, response.text)


new_class = Motorcycle()
