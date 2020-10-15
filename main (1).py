import re
class Regex():
    def __init__(self, credit_card_number):
        self.credit_card_number = credit_card_number
    
    def validation(self):
        if len(credit_card_number) == 19 and re.match('^[4-6]', credit_card_number) and re.match('[0-9]{4}\-[0-9]{4}\-[0-9]{4}\-[0-9]{4}$', credit_card_number):
            try:#To raise an exception if the credit card number is valid which means there is no sequence of repeated digits
                num_list = credit_card_number.split('-')
                num = ('').join(num_list)
                result = re.search(r'(\d)\1{3}', num)#This line searches for a digit that is repeated in a sequence for atleast 4 times
                result.group()#This line raises an exception
                print('Invalid')
            except:
                print('Valid')
        elif len(credit_card_number) == 16 and re.match('^[4-6]', credit_card_number) and re.match('[0-9]+', credit_card_number):
            print('Valid')
        else:
            print('Invalid')

if __name__ == '__main__':
    test_case_number = int(input())

    for _ in range(test_case_number):
        credit_card_number = input()
        my_object = Regex(credit_card_number)
        my_object.validation()

