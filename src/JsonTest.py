import json

if __name__ == '__main__':
    str1 = ['{"id": "PO_2021189070026000005", "merchantId": "e9688eeb-ae82-4398-b7d9-d5c7c8c8b141"}',
            '{"id": "PO_2021189070026000009", "merchantId": "e9688eeb-ae82-4398-b7d9-d5c7c8c8b141"}']
    for ele in str1:
        ss = ele.replace("'", '"')
        print(ss)
