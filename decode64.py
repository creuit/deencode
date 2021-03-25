import base64



def main():
    ed = input('Press 2 = Encode, 1 = Decode')
    ed = int(ed)
    while ed > 0 :
        #Decode
        if ed == 1:
            string = input('Decode:')
            string_b = string.encode('utf-8')
            base64_bytes = base64.b64encode(string_b)
            print(base64_bytes.decode('utf-8'))
            ed = input('Press 2 = Encode, 1 = Decode')
            ed = int(ed)

        #Encode
        elif ed == 2:
            string = input('Encode')
            x = len(string)
            itsokay = x % 4
            whattoad = 4 - itsokay

            if itsokay !=0:
                count = 0
                while count!= whattoad:
                    string += '='
                    count += 1

                #string_b = string.encode('utf-8')
                print(string)
                string_b64 = base64.b64decode(string)
                #PERITTO OXI BAN base64_bytes = base64.b64decode(string_b64)
                print(string_b64.decode('utf-8'))
            else:
                print(string)
                string_b64 = base64.b64decode(string)
                #PERITTO OXI BAN base64_bytes = base64.b64decode(string_b64)
                print(string_b64.decode('utf-8'))



        else:
            #input('Do you want to quit? 1 =  ')
            quit()



main()
