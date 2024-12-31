class phonefactory:
    model: None
    color: None
    is_android: None

    def __init__(self, model, color, is_android):
        self.model = model
        self.color = color
        self.is_android = is_android
        print ("phone created ")
    def __str__(self):
        return f"{self.model} - {self.color}"

    def check_os(self):
        if self.is_android:
            print("Android")
        else:
            print("iOS")

#apple_phone_1 = phonefactory()
#apple_phone_1.model = "Iphone 12"
#apple_phone_1.color = "black"
#apple_phone_1.is_android = FALSE
#print(apple_phone_1)

#samsung_phone_1 = phonefactory()
#samsung_phone_1.model= "galaxy A32"
#samgsung_phone_1.color = "gray"
#samgsung_phone_1,is_android = TRUE
#print(samgsung_phone_1)

