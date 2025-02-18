import os

def main():
    for i in range(1,12):
        print("main-asset\\LN-cover\\angel-next-door\\10-" + str(i) + ".jpg") 
        
main()

#####################################################################################################

# source_folder = "..\\main-asset\\LN-cover\\temp"

# def main():
#     counter = 1
#     for item in os.listdir(source_folder):
#         if os.path.isfile(os.path.join(source_folder,item)):
#             if item.endswith(".jpg"):
#                 try:
#                     a = "10-" + str(counter) + ".jpg"
#                     os.rename(os.path.join(source_folder,item),
#                         os.path.join(source_folder,a)
#                     )
#                 except Exception as e:
#                     raise Exception("")
                
#         counter = counter + 1
                
# main()