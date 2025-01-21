def check_product_data(input,variations,approved_sellers):
    level=input["Level"]
    product_details=input["Product_Details"]
    url=input["URL"]
    url=url.lower().strip()
    currency_url=input["Currency"]
    bool_sku=False
    bool_currency=False
    if level=="brand":
        currency_inner = product_details["Currency"]
        pid_list = [product_details.get("Product_ID_1", ""), product_details.get("Product_ID_2", ""),
                    product_details.get("Product_ID_3", ""), product_details.get("Product_ID_4", "")]
        for variation in variations:
            variation=variation.lower().strip()
            for pid in pid_list:
                if variation in url or variation==pid:
                    bool_sku=True
                if bool_sku:
                    break
            if bool_sku:
                break
        if currency_url=="Correct Currency" or currency_inner=="USD":
            bool_currency=True
        if bool_sku and bool_currency:
            return True
    elif level=="modesens":
        bool_list=[]
        for product_detail in product_details:
            bool_seller = False
            bool_currency=False
            seller_inner=product_detail.get("seller","")
            seller_inner=seller_inner.strip().lower()
            for seller in approved_sellers:
                if seller in seller_inner:
                    bool_seller=True
                if bool_seller:
                    break
            currency_inner=product_detail.get("currency","")
            if currency_inner=="$" or currency_url=="Correct Currency":
                bool_currency=True
            if bool_currency and bool_seller:
                bool_list.append(True)
            else:
                bool_list.append(False)
        return bool_list

    return False

if __name__=="__main__":
    input={'URL': 'https://modesens.com/product/givenchy-women-straw-medium-voyou-basket-shopping-bag-brown-107056049/?srsltid=AfmBOopaeFWB1EfjVueUNeuLWF9SBGWBGEYC4EF-Wcb8IehkINLozNHl', 'Variations': ['BB50V9B1UC-105'], 'Level': 'modesens', 'Currency': 'Wrong Currency', 'Product_Details': [{'price': 675.0, 'seller': 'MytheresaVISIT STORE', 'currency': '$'}, {'price': 675.0, 'seller': 'FORWARDVISIT STORE', 'currency': '$'}, {'price': 345.0, 'seller': 'FARFETCHVISIT STORE', 'currency': '$'}, {'price': 609.0, 'seller': 'SENSERVISIT STORE', 'currency': '$'}]}
    temp_list=[{'Query': '"BB50V9B1UC-105" GIV', 'Variation': 'BB50V9B1UC-105'}, {'Query': '"BB50V9B1UC-105" Givenchy', 'Variation': 'BB50V9B1UC-105'}, {'Query': '"BB50V9B1UC-105" GIVENCHY', 'Variation': 'BB50V9B1UC-105'}, {'Query': '"BB50V9B1UC-105"', 'Variation': 'BB50V9B1UC-105'}, {'Query': '"BB50V9B1UC" GIV', 'Variation': 'BB50V9B1UC'}, {'Query': '"BB50V9B1UC" Givenchy', 'Variation': 'BB50V9B1UC'}, {'Query': '"BB50V9B1UC" GIVENCHY', 'Variation': 'BB50V9B1UC'}, {'Query': '"BB50V9B1UC"', 'Variation': 'BB50V9B1UC'}, {'Query': '"BB50V9B1UC"', 'Variation': 'BB50V9B1UC'}, {'Query': '"BB50V.9B1UC.105" GIV', 'Variation': 'BB50V.9B1UC.105'}, {'Query': '"BB50V.9B1UC.105" Givenchy', 'Variation': 'BB50V.9B1UC.105'}, {'Query': '"BB50V.9B1UC.105" GIVENCHY', 'Variation': 'BB50V.9B1UC.105'}, {'Query': '"BB50V.9B1UC.105"', 'Variation': 'BB50V.9B1UC.105'}, {'Query': '"BB50V.9B1UC.105"', 'Variation': 'BB50V.9B1UC.105'}, {'Query': '"BB50V.9B1UC.105"', 'Variation': 'BB50V.9B1UC.105'}, {'Query': '"BB50V.9B1UC" GIV', 'Variation': 'BB50V.9B1UC'}, {'Query': '"BB50V.9B1UC" Givenchy', 'Variation': 'BB50V.9B1UC'}, {'Query': '"BB50V.9B1UC" GIVENCHY', 'Variation': 'BB50V.9B1UC'}, {'Query': '"BB50V.9B1UC"', 'Variation': 'BB50V.9B1UC'}, {'Query': '"BB50V.9B1UC"', 'Variation': 'BB50V.9B1UC'}, {'Query': '"BB50V.9B1UC"', 'Variation': 'BB50V.9B1UC'}, {'Query': '"BB50V.9B1UC"', 'Variation': 'BB50V.9B1UC'}, {'Query': '"BB50V.9B1UC 105" GIV', 'Variation': 'BB50V.9B1UC 105'}, {'Query': '"BB50V.9B1UC 105" Givenchy', 'Variation': 'BB50V.9B1UC 105'}, {'Query': '"BB50V.9B1UC 105" GIVENCHY', 'Variation': 'BB50V.9B1UC 105'}, {'Query': '"BB50V.9B1UC 105"', 'Variation': 'BB50V.9B1UC 105'}, {'Query': '"BB50V.9B1UC 105"', 'Variation': 'BB50V.9B1UC 105'}, {'Query': '"BB50V.9B1UC 105"', 'Variation': 'BB50V.9B1UC 105'}, {'Query': '"BB50V.9B1UC 105"', 'Variation': 'BB50V.9B1UC 105'}, {'Query': '"BB50V.9B1UC 105"', 'Variation': 'BB50V.9B1UC 105'}, {'Query': '"BB50V.9B1UC-105" GIV', 'Variation': 'BB50V.9B1UC-105'}, {'Query': '"BB50V.9B1UC-105" Givenchy', 'Variation': 'BB50V.9B1UC-105'}, {'Query': '"BB50V.9B1UC-105" GIVENCHY', 'Variation': 'BB50V.9B1UC-105'}, {'Query': '"BB50V.9B1UC-105"', 'Variation': 'BB50V.9B1UC-105'}, {'Query': '"BB50V.9B1UC-105"', 'Variation': 'BB50V.9B1UC-105'}, {'Query': '"BB50V.9B1UC-105"', 'Variation': 'BB50V.9B1UC-105'}, {'Query': '"BB50V.9B1UC-105"', 'Variation': 'BB50V.9B1UC-105'}, {'Query': '"BB50V.9B1UC-105"', 'Variation': 'BB50V.9B1UC-105'}, {'Query': '"BB50V.9B1UC-105"', 'Variation': 'BB50V.9B1UC-105'}, {'Query': '"BB50V.9B1UC_105" GIV', 'Variation': 'BB50V.9B1UC_105'}, {'Query': '"BB50V.9B1UC_105" Givenchy', 'Variation': 'BB50V.9B1UC_105'}, {'Query': '"BB50V.9B1UC_105" GIVENCHY', 'Variation': 'BB50V.9B1UC_105'}, {'Query': '"BB50V.9B1UC_105"', 'Variation': 'BB50V.9B1UC_105'}, {'Query': '"BB50V.9B1UC_105"', 'Variation': 'BB50V.9B1UC_105'}, {'Query': '"BB50V.9B1UC_105"', 'Variation': 'BB50V.9B1UC_105'}, {'Query': '"BB50V.9B1UC_105"', 'Variation': 'BB50V.9B1UC_105'}, {'Query': '"BB50V.9B1UC_105"', 'Variation': 'BB50V.9B1UC_105'}, {'Query': '"BB50V.9B1UC_105"', 'Variation': 'BB50V.9B1UC_105'}, {'Query': '"BB50V.9B1UC_105"', 'Variation': 'BB50V.9B1UC_105'}, {'Query': '"BB50V.9B1UC105" GIV', 'Variation': 'BB50V.9B1UC105'}, {'Query': '"BB50V.9B1UC105" Givenchy', 'Variation': 'BB50V.9B1UC105'}, {'Query': '"BB50V.9B1UC105" GIVENCHY', 'Variation': 'BB50V.9B1UC105'}, {'Query': '"BB50V.9B1UC105"', 'Variation': 'BB50V.9B1UC105'}, {'Query': '"BB50V.9B1UC105"', 'Variation': 'BB50V.9B1UC105'}, {'Query': '"BB50V.9B1UC105"', 'Variation': 'BB50V.9B1UC105'}, {'Query': '"BB50V.9B1UC105"', 'Variation': 'BB50V.9B1UC105'}, {'Query': '"BB50V.9B1UC105"', 'Variation': 'BB50V.9B1UC105'}, {'Query': '"BB50V.9B1UC105"', 'Variation': 'BB50V.9B1UC105'}, {'Query': '"BB50V.9B1UC105"', 'Variation': 'BB50V.9B1UC105'}, {'Query': '"BB50V.9B1UC105"', 'Variation': 'BB50V.9B1UC105'}, {'Query': '"BB50V 9B1UC.105" GIV', 'Variation': 'BB50V 9B1UC.105'}, {'Query': '"BB50V 9B1UC.105" Givenchy', 'Variation': 'BB50V 9B1UC.105'}, {'Query': '"BB50V 9B1UC.105" GIVENCHY', 'Variation': 'BB50V 9B1UC.105'}, {'Query': '"BB50V 9B1UC.105"', 'Variation': 'BB50V 9B1UC.105'}, {'Query': '"BB50V 9B1UC.105"', 'Variation': 'BB50V 9B1UC.105'}, {'Query': '"BB50V 9B1UC.105"', 'Variation': 'BB50V 9B1UC.105'}, {'Query': '"BB50V 9B1UC.105"', 'Variation': 'BB50V 9B1UC.105'}, {'Query': '"BB50V 9B1UC.105"', 'Variation': 'BB50V 9B1UC.105'}, {'Query': '"BB50V 9B1UC.105"', 'Variation': 'BB50V 9B1UC.105'}, {'Query': '"BB50V 9B1UC.105"', 'Variation': 'BB50V 9B1UC.105'}, {'Query': '"BB50V 9B1UC.105"', 'Variation': 'BB50V 9B1UC.105'}, {'Query': '"BB50V 9B1UC.105"', 'Variation': 'BB50V 9B1UC.105'}, {'Query': '"BB50V 9B1UC" GIV', 'Variation': 'BB50V 9B1UC'}, {'Query': '"BB50V 9B1UC" Givenchy', 'Variation': 'BB50V 9B1UC'}, {'Query': '"BB50V 9B1UC" GIVENCHY', 'Variation': 'BB50V 9B1UC'}, {'Query': '"BB50V 9B1UC"', 'Variation': 'BB50V 9B1UC'}, {'Query': '"BB50V 9B1UC"', 'Variation': 'BB50V 9B1UC'}, {'Query': '"BB50V 9B1UC"', 'Variation': 'BB50V 9B1UC'}, {'Query': '"BB50V 9B1UC"', 'Variation': 'BB50V 9B1UC'}, {'Query': '"BB50V 9B1UC"', 'Variation': 'BB50V 9B1UC'}, {'Query': '"BB50V 9B1UC"', 'Variation': 'BB50V 9B1UC'}, {'Query': '"BB50V 9B1UC"', 'Variation': 'BB50V 9B1UC'}, {'Query': '"BB50V 9B1UC"', 'Variation': 'BB50V 9B1UC'}, {'Query': '"BB50V 9B1UC"', 'Variation': 'BB50V 9B1UC'}, {'Query': '"BB50V 9B1UC"', 'Variation': 'BB50V 9B1UC'}, {'Query': '"BB50V 9B1UC 105" GIV', 'Variation': 'BB50V 9B1UC 105'}, {'Query': '"BB50V 9B1UC 105" Givenchy', 'Variation': 'BB50V 9B1UC 105'}, {'Query': '"BB50V 9B1UC 105" GIVENCHY', 'Variation': 'BB50V 9B1UC 105'}, {'Query': '"BB50V 9B1UC 105"', 'Variation': 'BB50V 9B1UC 105'}, {'Query': '"BB50V 9B1UC 105"', 'Variation': 'BB50V 9B1UC 105'}, {'Query': '"BB50V 9B1UC 105"', 'Variation': 'BB50V 9B1UC 105'}, {'Query': '"BB50V 9B1UC 105"', 'Variation': 'BB50V 9B1UC 105'}, {'Query': '"BB50V 9B1UC 105"', 'Variation': 'BB50V 9B1UC 105'}, {'Query': '"BB50V 9B1UC 105"', 'Variation': 'BB50V 9B1UC 105'}, {'Query': '"BB50V 9B1UC 105"', 'Variation': 'BB50V 9B1UC 105'}, {'Query': '"BB50V 9B1UC 105"', 'Variation': 'BB50V 9B1UC 105'}, {'Query': '"BB50V 9B1UC 105"', 'Variation': 'BB50V 9B1UC 105'}, {'Query': '"BB50V 9B1UC 105"', 'Variation': 'BB50V 9B1UC 105'}, {'Query': '"BB50V 9B1UC 105"', 'Variation': 'BB50V 9B1UC 105'}, {'Query': '"BB50V 9B1UC-105" GIV', 'Variation': 'BB50V 9B1UC-105'}, {'Query': '"BB50V 9B1UC-105" Givenchy', 'Variation': 'BB50V 9B1UC-105'}, {'Query': '"BB50V 9B1UC-105" GIVENCHY', 'Variation': 'BB50V 9B1UC-105'}, {'Query': '"BB50V 9B1UC-105"', 'Variation': 'BB50V 9B1UC-105'}, {'Query': '"BB50V 9B1UC-105"', 'Variation': 'BB50V 9B1UC-105'}, {'Query': '"BB50V 9B1UC-105"', 'Variation': 'BB50V 9B1UC-105'}, {'Query': '"BB50V 9B1UC-105"', 'Variation': 'BB50V 9B1UC-105'}, {'Query': '"BB50V 9B1UC-105"', 'Variation': 'BB50V 9B1UC-105'}, {'Query': '"BB50V 9B1UC-105"', 'Variation': 'BB50V 9B1UC-105'}, {'Query': '"BB50V 9B1UC-105"', 'Variation': 'BB50V 9B1UC-105'}, {'Query': '"BB50V 9B1UC-105"', 'Variation': 'BB50V 9B1UC-105'}, {'Query': '"BB50V 9B1UC-105"', 'Variation': 'BB50V 9B1UC-105'}, {'Query': '"BB50V 9B1UC-105"', 'Variation': 'BB50V 9B1UC-105'}, {'Query': '"BB50V 9B1UC-105"', 'Variation': 'BB50V 9B1UC-105'}, {'Query': '"BB50V 9B1UC-105"', 'Variation': 'BB50V 9B1UC-105'}, {'Query': '"BB50V 9B1UC_105" GIV', 'Variation': 'BB50V 9B1UC_105'}, {'Query': '"BB50V 9B1UC_105" Givenchy', 'Variation': 'BB50V 9B1UC_105'}, {'Query': '"BB50V 9B1UC_105" GIVENCHY', 'Variation': 'BB50V 9B1UC_105'}, {'Query': '"BB50V 9B1UC_105"', 'Variation': 'BB50V 9B1UC_105'}, {'Query': '"BB50V 9B1UC_105"', 'Variation': 'BB50V 9B1UC_105'}, {'Query': '"BB50V 9B1UC_105"', 'Variation': 'BB50V 9B1UC_105'}, {'Query': '"BB50V 9B1UC_105"', 'Variation': 'BB50V 9B1UC_105'}, {'Query': '"BB50V 9B1UC_105"', 'Variation': 'BB50V 9B1UC_105'}, {'Query': '"BB50V 9B1UC_105"', 'Variation': 'BB50V 9B1UC_105'}, {'Query': '"BB50V 9B1UC_105"', 'Variation': 'BB50V 9B1UC_105'}, {'Query': '"BB50V 9B1UC_105"', 'Variation': 'BB50V 9B1UC_105'}, {'Query': '"BB50V 9B1UC_105"', 'Variation': 'BB50V 9B1UC_105'}, {'Query': '"BB50V 9B1UC_105"', 'Variation': 'BB50V 9B1UC_105'}, {'Query': '"BB50V 9B1UC_105"', 'Variation': 'BB50V 9B1UC_105'}, {'Query': '"BB50V 9B1UC_105"', 'Variation': 'BB50V 9B1UC_105'}, {'Query': '"BB50V 9B1UC_105"', 'Variation': 'BB50V 9B1UC_105'}, {'Query': '"BB50V 9B1UC105" GIV', 'Variation': 'BB50V 9B1UC105'}, {'Query': '"BB50V 9B1UC105" Givenchy', 'Variation': 'BB50V 9B1UC105'}, {'Query': '"BB50V 9B1UC105" GIVENCHY', 'Variation': 'BB50V 9B1UC105'}, {'Query': '"BB50V 9B1UC105"', 'Variation': 'BB50V 9B1UC105'}, {'Query': '"BB50V 9B1UC105"', 'Variation': 'BB50V 9B1UC105'}, {'Query': '"BB50V 9B1UC105"', 'Variation': 'BB50V 9B1UC105'}, {'Query': '"BB50V 9B1UC105"', 'Variation': 'BB50V 9B1UC105'}, {'Query': '"BB50V 9B1UC105"', 'Variation': 'BB50V 9B1UC105'}, {'Query': '"BB50V 9B1UC105"', 'Variation': 'BB50V 9B1UC105'}, {'Query': '"BB50V 9B1UC105"', 'Variation': 'BB50V 9B1UC105'}, {'Query': '"BB50V 9B1UC105"', 'Variation': 'BB50V 9B1UC105'}, {'Query': '"BB50V 9B1UC105"', 'Variation': 'BB50V 9B1UC105'}, {'Query': '"BB50V 9B1UC105"', 'Variation': 'BB50V 9B1UC105'}, {'Query': '"BB50V 9B1UC105"', 'Variation': 'BB50V 9B1UC105'}, {'Query': '"BB50V 9B1UC105"', 'Variation': 'BB50V 9B1UC105'}, {'Query': '"BB50V 9B1UC105"', 'Variation': 'BB50V 9B1UC105'}, {'Query': '"BB50V 9B1UC105"', 'Variation': 'BB50V 9B1UC105'}, {'Query': '"BB50V-9B1UC.105" GIV', 'Variation': 'BB50V-9B1UC.105'}, {'Query': '"BB50V-9B1UC.105" Givenchy', 'Variation': 'BB50V-9B1UC.105'}, {'Query': '"BB50V-9B1UC.105" GIVENCHY', 'Variation': 'BB50V-9B1UC.105'}, {'Query': '"BB50V-9B1UC.105"', 'Variation': 'BB50V-9B1UC.105'}, {'Query': '"BB50V-9B1UC.105"', 'Variation': 'BB50V-9B1UC.105'}, {'Query': '"BB50V-9B1UC.105"', 'Variation': 'BB50V-9B1UC.105'}, {'Query': '"BB50V-9B1UC.105"', 'Variation': 'BB50V-9B1UC.105'}, {'Query': '"BB50V-9B1UC.105"', 'Variation': 'BB50V-9B1UC.105'}, {'Query': '"BB50V-9B1UC.105"', 'Variation': 'BB50V-9B1UC.105'}, {'Query': '"BB50V-9B1UC.105"', 'Variation': 'BB50V-9B1UC.105'}, {'Query': '"BB50V-9B1UC.105"', 'Variation': 'BB50V-9B1UC.105'}, {'Query': '"BB50V-9B1UC.105"', 'Variation': 'BB50V-9B1UC.105'}, {'Query': '"BB50V-9B1UC.105"', 'Variation': 'BB50V-9B1UC.105'}, {'Query': '"BB50V-9B1UC.105"', 'Variation': 'BB50V-9B1UC.105'}, {'Query': '"BB50V-9B1UC.105"', 'Variation': 'BB50V-9B1UC.105'}, {'Query': '"BB50V-9B1UC.105"', 'Variation': 'BB50V-9B1UC.105'}, {'Query': '"BB50V-9B1UC.105"', 'Variation': 'BB50V-9B1UC.105'}, {'Query': '"BB50V-9B1UC.105"', 'Variation': 'BB50V-9B1UC.105'}, {'Query': '"BB50V-9B1UC" GIV', 'Variation': 'BB50V-9B1UC'}, {'Query': '"BB50V-9B1UC" Givenchy', 'Variation': 'BB50V-9B1UC'}, {'Query': '"BB50V-9B1UC" GIVENCHY', 'Variation': 'BB50V-9B1UC'}, {'Query': '"BB50V-9B1UC"', 'Variation': 'BB50V-9B1UC'}, {'Query': '"BB50V-9B1UC"', 'Variation': 'BB50V-9B1UC'}, {'Query': '"BB50V-9B1UC"', 'Variation': 'BB50V-9B1UC'}, {'Query': '"BB50V-9B1UC"', 'Variation': 'BB50V-9B1UC'}, {'Query': '"BB50V-9B1UC"', 'Variation': 'BB50V-9B1UC'}, {'Query': '"BB50V-9B1UC"', 'Variation': 'BB50V-9B1UC'}, {'Query': '"BB50V-9B1UC"', 'Variation': 'BB50V-9B1UC'}, {'Query': '"BB50V-9B1UC"', 'Variation': 'BB50V-9B1UC'}, {'Query': '"BB50V-9B1UC"', 'Variation': 'BB50V-9B1UC'}, {'Query': '"BB50V-9B1UC"', 'Variation': 'BB50V-9B1UC'}, {'Query': '"BB50V-9B1UC"', 'Variation': 'BB50V-9B1UC'}, {'Query': '"BB50V-9B1UC"', 'Variation': 'BB50V-9B1UC'}, {'Query': '"BB50V-9B1UC"', 'Variation': 'BB50V-9B1UC'}, {'Query': '"BB50V-9B1UC"', 'Variation': 'BB50V-9B1UC'}, {'Query': '"BB50V-9B1UC"', 'Variation': 'BB50V-9B1UC'}, {'Query': '"BB50V-9B1UC"', 'Variation': 'BB50V-9B1UC'}, {'Query': '"BB50V-9B1UC 105" GIV', 'Variation': 'BB50V-9B1UC 105'}, {'Query': '"BB50V-9B1UC 105" Givenchy', 'Variation': 'BB50V-9B1UC 105'}, {'Query': '"BB50V-9B1UC 105" GIVENCHY', 'Variation': 'BB50V-9B1UC 105'}, {'Query': '"BB50V-9B1UC 105"', 'Variation': 'BB50V-9B1UC 105'}, {'Query': '"BB50V-9B1UC 105"', 'Variation': 'BB50V-9B1UC 105'}, {'Query': '"BB50V-9B1UC 105"', 'Variation': 'BB50V-9B1UC 105'}, {'Query': '"BB50V-9B1UC 105"', 'Variation': 'BB50V-9B1UC 105'}, {'Query': '"BB50V-9B1UC 105"', 'Variation': 'BB50V-9B1UC 105'}, {'Query': '"BB50V-9B1UC 105"', 'Variation': 'BB50V-9B1UC 105'}, {'Query': '"BB50V-9B1UC 105"', 'Variation': 'BB50V-9B1UC 105'}, {'Query': '"BB50V-9B1UC 105"', 'Variation': 'BB50V-9B1UC 105'}, {'Query': '"BB50V-9B1UC 105"', 'Variation': 'BB50V-9B1UC 105'}, {'Query': '"BB50V-9B1UC 105"', 'Variation': 'BB50V-9B1UC 105'}, {'Query': '"BB50V-9B1UC 105"', 'Variation': 'BB50V-9B1UC 105'}, {'Query': '"BB50V-9B1UC 105"', 'Variation': 'BB50V-9B1UC 105'}, {'Query': '"BB50V-9B1UC 105"', 'Variation': 'BB50V-9B1UC 105'}, {'Query': '"BB50V-9B1UC 105"', 'Variation': 'BB50V-9B1UC 105'}, {'Query': '"BB50V-9B1UC 105"', 'Variation': 'BB50V-9B1UC 105'}, {'Query': '"BB50V-9B1UC 105"', 'Variation': 'BB50V-9B1UC 105'}, {'Query': '"BB50V-9B1UC 105"', 'Variation': 'BB50V-9B1UC 105'}, {'Query': '"BB50V-9B1UC-105" GIV', 'Variation': 'BB50V-9B1UC-105'}, {'Query': '"BB50V-9B1UC-105" Givenchy', 'Variation': 'BB50V-9B1UC-105'}, {'Query': '"BB50V-9B1UC-105" GIVENCHY', 'Variation': 'BB50V-9B1UC-105'}, {'Query': '"BB50V-9B1UC-105"', 'Variation': 'BB50V-9B1UC-105'}, {'Query': '"BB50V-9B1UC-105"', 'Variation': 'BB50V-9B1UC-105'}, {'Query': '"BB50V-9B1UC-105"', 'Variation': 'BB50V-9B1UC-105'}, {'Query': '"BB50V-9B1UC-105"', 'Variation': 'BB50V-9B1UC-105'}, {'Query': '"BB50V-9B1UC-105"', 'Variation': 'BB50V-9B1UC-105'}, {'Query': '"BB50V-9B1UC-105"', 'Variation': 'BB50V-9B1UC-105'}, {'Query': '"BB50V-9B1UC-105"', 'Variation': 'BB50V-9B1UC-105'}, {'Query': '"BB50V-9B1UC-105"', 'Variation': 'BB50V-9B1UC-105'}, {'Query': '"BB50V-9B1UC-105"', 'Variation': 'BB50V-9B1UC-105'}, {'Query': '"BB50V-9B1UC-105"', 'Variation': 'BB50V-9B1UC-105'}, {'Query': '"BB50V-9B1UC-105"', 'Variation': 'BB50V-9B1UC-105'}, {'Query': '"BB50V-9B1UC-105"', 'Variation': 'BB50V-9B1UC-105'}, {'Query': '"BB50V-9B1UC-105"', 'Variation': 'BB50V-9B1UC-105'}, {'Query': '"BB50V-9B1UC-105"', 'Variation': 'BB50V-9B1UC-105'}, {'Query': '"BB50V-9B1UC-105"', 'Variation': 'BB50V-9B1UC-105'}, {'Query': '"BB50V-9B1UC-105"', 'Variation': 'BB50V-9B1UC-105'}, {'Query': '"BB50V-9B1UC-105"', 'Variation': 'BB50V-9B1UC-105'}, {'Query': '"BB50V-9B1UC-105"', 'Variation': 'BB50V-9B1UC-105'}, {'Query': '"BB50V-9B1UC_105" GIV', 'Variation': 'BB50V-9B1UC_105'}, {'Query': '"BB50V-9B1UC_105" Givenchy', 'Variation': 'BB50V-9B1UC_105'}, {'Query': '"BB50V-9B1UC_105" GIVENCHY', 'Variation': 'BB50V-9B1UC_105'}, {'Query': '"BB50V-9B1UC_105"', 'Variation': 'BB50V-9B1UC_105'}, {'Query': '"BB50V-9B1UC_105"', 'Variation': 'BB50V-9B1UC_105'}, {'Query': '"BB50V-9B1UC_105"', 'Variation': 'BB50V-9B1UC_105'}, {'Query': '"BB50V-9B1UC_105"', 'Variation': 'BB50V-9B1UC_105'}, {'Query': '"BB50V-9B1UC_105"', 'Variation': 'BB50V-9B1UC_105'}, {'Query': '"BB50V-9B1UC_105"', 'Variation': 'BB50V-9B1UC_105'}, {'Query': '"BB50V-9B1UC_105"', 'Variation': 'BB50V-9B1UC_105'}, {'Query': '"BB50V-9B1UC_105"', 'Variation': 'BB50V-9B1UC_105'}, {'Query': '"BB50V-9B1UC_105"', 'Variation': 'BB50V-9B1UC_105'}, {'Query': '"BB50V-9B1UC_105"', 'Variation': 'BB50V-9B1UC_105'}, {'Query': '"BB50V-9B1UC_105"', 'Variation': 'BB50V-9B1UC_105'}, {'Query': '"BB50V-9B1UC_105"', 'Variation': 'BB50V-9B1UC_105'}, {'Query': '"BB50V-9B1UC_105"', 'Variation': 'BB50V-9B1UC_105'}, {'Query': '"BB50V-9B1UC_105"', 'Variation': 'BB50V-9B1UC_105'}, {'Query': '"BB50V-9B1UC_105"', 'Variation': 'BB50V-9B1UC_105'}, {'Query': '"BB50V-9B1UC_105"', 'Variation': 'BB50V-9B1UC_105'}, {'Query': '"BB50V-9B1UC_105"', 'Variation': 'BB50V-9B1UC_105'}, {'Query': '"BB50V-9B1UC_105"', 'Variation': 'BB50V-9B1UC_105'}, {'Query': '"BB50V-9B1UC_105"', 'Variation': 'BB50V-9B1UC_105'}, {'Query': '"BB50V-9B1UC105" GIV', 'Variation': 'BB50V-9B1UC105'}, {'Query': '"BB50V-9B1UC105" Givenchy', 'Variation': 'BB50V-9B1UC105'}, {'Query': '"BB50V-9B1UC105" GIVENCHY', 'Variation': 'BB50V-9B1UC105'}, {'Query': '"BB50V-9B1UC105"', 'Variation': 'BB50V-9B1UC105'}, {'Query': '"BB50V-9B1UC105"', 'Variation': 'BB50V-9B1UC105'}, {'Query': '"BB50V-9B1UC105"', 'Variation': 'BB50V-9B1UC105'}, {'Query': '"BB50V-9B1UC105"', 'Variation': 'BB50V-9B1UC105'}, {'Query': '"BB50V-9B1UC105"', 'Variation': 'BB50V-9B1UC105'}, {'Query': '"BB50V-9B1UC105"', 'Variation': 'BB50V-9B1UC105'}, {'Query': '"BB50V-9B1UC105"', 'Variation': 'BB50V-9B1UC105'}, {'Query': '"BB50V-9B1UC105"', 'Variation': 'BB50V-9B1UC105'}, {'Query': '"BB50V-9B1UC105"', 'Variation': 'BB50V-9B1UC105'}, {'Query': '"BB50V-9B1UC105"', 'Variation': 'BB50V-9B1UC105'}, {'Query': '"BB50V-9B1UC105"', 'Variation': 'BB50V-9B1UC105'}, {'Query': '"BB50V-9B1UC105"', 'Variation': 'BB50V-9B1UC105'}, {'Query': '"BB50V-9B1UC105"', 'Variation': 'BB50V-9B1UC105'}, {'Query': '"BB50V-9B1UC105"', 'Variation': 'BB50V-9B1UC105'}, {'Query': '"BB50V-9B1UC105"', 'Variation': 'BB50V-9B1UC105'}, {'Query': '"BB50V-9B1UC105"', 'Variation': 'BB50V-9B1UC105'}, {'Query': '"BB50V-9B1UC105"', 'Variation': 'BB50V-9B1UC105'}, {'Query': '"BB50V-9B1UC105"', 'Variation': 'BB50V-9B1UC105'}, {'Query': '"BB50V-9B1UC105"', 'Variation': 'BB50V-9B1UC105'}, {'Query': '"BB50V-9B1UC105"', 'Variation': 'BB50V-9B1UC105'}, {'Query': '"BB50V_9B1UC.105" GIV', 'Variation': 'BB50V_9B1UC.105'}, {'Query': '"BB50V_9B1UC.105" Givenchy', 'Variation': 'BB50V_9B1UC.105'}, {'Query': '"BB50V_9B1UC.105" GIVENCHY', 'Variation': 'BB50V_9B1UC.105'}, {'Query': '"BB50V_9B1UC.105"', 'Variation': 'BB50V_9B1UC.105'}, {'Query': '"BB50V_9B1UC.105"', 'Variation': 'BB50V_9B1UC.105'}, {'Query': '"BB50V_9B1UC.105"', 'Variation': 'BB50V_9B1UC.105'}, {'Query': '"BB50V_9B1UC.105"', 'Variation': 'BB50V_9B1UC.105'}, {'Query': '"BB50V_9B1UC.105"', 'Variation': 'BB50V_9B1UC.105'}, {'Query': '"BB50V_9B1UC.105"', 'Variation': 'BB50V_9B1UC.105'}, {'Query': '"BB50V_9B1UC.105"', 'Variation': 'BB50V_9B1UC.105'}, {'Query': '"BB50V_9B1UC.105"', 'Variation': 'BB50V_9B1UC.105'}, {'Query': '"BB50V_9B1UC.105"', 'Variation': 'BB50V_9B1UC.105'}, {'Query': '"BB50V_9B1UC.105"', 'Variation': 'BB50V_9B1UC.105'}, {'Query': '"BB50V_9B1UC.105"', 'Variation': 'BB50V_9B1UC.105'}, {'Query': '"BB50V_9B1UC.105"', 'Variation': 'BB50V_9B1UC.105'}, {'Query': '"BB50V_9B1UC.105"', 'Variation': 'BB50V_9B1UC.105'}, {'Query': '"BB50V_9B1UC.105"', 'Variation': 'BB50V_9B1UC.105'}, {'Query': '"BB50V_9B1UC.105"', 'Variation': 'BB50V_9B1UC.105'}, {'Query': '"BB50V_9B1UC.105"', 'Variation': 'BB50V_9B1UC.105'}, {'Query': '"BB50V_9B1UC.105"', 'Variation': 'BB50V_9B1UC.105'}, {'Query': '"BB50V_9B1UC.105"', 'Variation': 'BB50V_9B1UC.105'}, {'Query': '"BB50V_9B1UC.105"', 'Variation': 'BB50V_9B1UC.105'}, {'Query': '"BB50V_9B1UC.105"', 'Variation': 'BB50V_9B1UC.105'}, {'Query': '"BB50V_9B1UC.105"', 'Variation': 'BB50V_9B1UC.105'}, {'Query': '"BB50V_9B1UC" GIV', 'Variation': 'BB50V_9B1UC'}, {'Query': '"BB50V_9B1UC" Givenchy', 'Variation': 'BB50V_9B1UC'}, {'Query': '"BB50V_9B1UC" GIVENCHY', 'Variation': 'BB50V_9B1UC'}, {'Query': '"BB50V_9B1UC"', 'Variation': 'BB50V_9B1UC'}, {'Query': '"BB50V_9B1UC"', 'Variation': 'BB50V_9B1UC'}, {'Query': '"BB50V_9B1UC"', 'Variation': 'BB50V_9B1UC'}, {'Query': '"BB50V_9B1UC"', 'Variation': 'BB50V_9B1UC'}, {'Query': '"BB50V_9B1UC"', 'Variation': 'BB50V_9B1UC'}, {'Query': '"BB50V_9B1UC"', 'Variation': 'BB50V_9B1UC'}, {'Query': '"BB50V_9B1UC"', 'Variation': 'BB50V_9B1UC'}, {'Query': '"BB50V_9B1UC"', 'Variation': 'BB50V_9B1UC'}, {'Query': '"BB50V_9B1UC"', 'Variation': 'BB50V_9B1UC'}, {'Query': '"BB50V_9B1UC"', 'Variation': 'BB50V_9B1UC'}, {'Query': '"BB50V_9B1UC"', 'Variation': 'BB50V_9B1UC'}, {'Query': '"BB50V_9B1UC"', 'Variation': 'BB50V_9B1UC'}, {'Query': '"BB50V_9B1UC"', 'Variation': 'BB50V_9B1UC'}, {'Query': '"BB50V_9B1UC"', 'Variation': 'BB50V_9B1UC'}, {'Query': '"BB50V_9B1UC"', 'Variation': 'BB50V_9B1UC'}, {'Query': '"BB50V_9B1UC"', 'Variation': 'BB50V_9B1UC'}, {'Query': '"BB50V_9B1UC"', 'Variation': 'BB50V_9B1UC'}, {'Query': '"BB50V_9B1UC"', 'Variation': 'BB50V_9B1UC'}, {'Query': '"BB50V_9B1UC"', 'Variation': 'BB50V_9B1UC'}, {'Query': '"BB50V_9B1UC"', 'Variation': 'BB50V_9B1UC'}, {'Query': '"BB50V_9B1UC"', 'Variation': 'BB50V_9B1UC'}, {'Query': '"BB50V_9B1UC"', 'Variation': 'BB50V_9B1UC'}, {'Query': '"BB50V_9B1UC 105" GIV', 'Variation': 'BB50V_9B1UC 105'}, {'Query': '"BB50V_9B1UC 105" Givenchy', 'Variation': 'BB50V_9B1UC 105'}, {'Query': '"BB50V_9B1UC 105" GIVENCHY', 'Variation': 'BB50V_9B1UC 105'}, {'Query': '"BB50V_9B1UC 105"', 'Variation': 'BB50V_9B1UC 105'}, {'Query': '"BB50V_9B1UC 105"', 'Variation': 'BB50V_9B1UC 105'}, {'Query': '"BB50V_9B1UC 105"', 'Variation': 'BB50V_9B1UC 105'}, {'Query': '"BB50V_9B1UC 105"', 'Variation': 'BB50V_9B1UC 105'}, {'Query': '"BB50V_9B1UC 105"', 'Variation': 'BB50V_9B1UC 105'}, {'Query': '"BB50V_9B1UC 105"', 'Variation': 'BB50V_9B1UC 105'}, {'Query': '"BB50V_9B1UC 105"', 'Variation': 'BB50V_9B1UC 105'}, {'Query': '"BB50V_9B1UC 105"', 'Variation': 'BB50V_9B1UC 105'}, {'Query': '"BB50V_9B1UC 105"', 'Variation': 'BB50V_9B1UC 105'}, {'Query': '"BB50V_9B1UC 105"', 'Variation': 'BB50V_9B1UC 105'}, {'Query': '"BB50V_9B1UC 105"', 'Variation': 'BB50V_9B1UC 105'}, {'Query': '"BB50V_9B1UC 105"', 'Variation': 'BB50V_9B1UC 105'}, {'Query': '"BB50V_9B1UC 105"', 'Variation': 'BB50V_9B1UC 105'}, {'Query': '"BB50V_9B1UC 105"', 'Variation': 'BB50V_9B1UC 105'}, {'Query': '"BB50V_9B1UC 105"', 'Variation': 'BB50V_9B1UC 105'}, {'Query': '"BB50V_9B1UC 105"', 'Variation': 'BB50V_9B1UC 105'}, {'Query': '"BB50V_9B1UC 105"', 'Variation': 'BB50V_9B1UC 105'}, {'Query': '"BB50V_9B1UC 105"', 'Variation': 'BB50V_9B1UC 105'}, {'Query': '"BB50V_9B1UC 105"', 'Variation': 'BB50V_9B1UC 105'}, {'Query': '"BB50V_9B1UC 105"', 'Variation': 'BB50V_9B1UC 105'}, {'Query': '"BB50V_9B1UC 105"', 'Variation': 'BB50V_9B1UC 105'}, {'Query': '"BB50V_9B1UC 105"', 'Variation': 'BB50V_9B1UC 105'}, {'Query': '"BB50V_9B1UC 105"', 'Variation': 'BB50V_9B1UC 105'}, {'Query': '"BB50V_9B1UC-105" GIV', 'Variation': 'BB50V_9B1UC-105'}, {'Query': '"BB50V_9B1UC-105" Givenchy', 'Variation': 'BB50V_9B1UC-105'}, {'Query': '"BB50V_9B1UC-105" GIVENCHY', 'Variation': 'BB50V_9B1UC-105'}, {'Query': '"BB50V_9B1UC-105"', 'Variation': 'BB50V_9B1UC-105'}, {'Query': '"BB50V_9B1UC-105"', 'Variation': 'BB50V_9B1UC-105'}, {'Query': '"BB50V_9B1UC-105"', 'Variation': 'BB50V_9B1UC-105'}, {'Query': '"BB50V_9B1UC-105"', 'Variation': 'BB50V_9B1UC-105'}, {'Query': '"BB50V_9B1UC-105"', 'Variation': 'BB50V_9B1UC-105'}, {'Query': '"BB50V_9B1UC-105"', 'Variation': 'BB50V_9B1UC-105'}, {'Query': '"BB50V_9B1UC-105"', 'Variation': 'BB50V_9B1UC-105'}, {'Query': '"BB50V_9B1UC-105"', 'Variation': 'BB50V_9B1UC-105'}, {'Query': '"BB50V_9B1UC-105"', 'Variation': 'BB50V_9B1UC-105'}, {'Query': '"BB50V_9B1UC-105"', 'Variation': 'BB50V_9B1UC-105'}, {'Query': '"BB50V_9B1UC-105"', 'Variation': 'BB50V_9B1UC-105'}, {'Query': '"BB50V_9B1UC-105"', 'Variation': 'BB50V_9B1UC-105'}, {'Query': '"BB50V_9B1UC-105"', 'Variation': 'BB50V_9B1UC-105'}, {'Query': '"BB50V_9B1UC-105"', 'Variation': 'BB50V_9B1UC-105'}, {'Query': '"BB50V_9B1UC-105"', 'Variation': 'BB50V_9B1UC-105'}, {'Query': '"BB50V_9B1UC-105"', 'Variation': 'BB50V_9B1UC-105'}, {'Query': '"BB50V_9B1UC-105"', 'Variation': 'BB50V_9B1UC-105'}, {'Query': '"BB50V_9B1UC-105"', 'Variation': 'BB50V_9B1UC-105'}, {'Query': '"BB50V_9B1UC-105"', 'Variation': 'BB50V_9B1UC-105'}, {'Query': '"BB50V_9B1UC-105"', 'Variation': 'BB50V_9B1UC-105'}, {'Query': '"BB50V_9B1UC-105"', 'Variation': 'BB50V_9B1UC-105'}, {'Query': '"BB50V_9B1UC-105"', 'Variation': 'BB50V_9B1UC-105'}, {'Query': '"BB50V_9B1UC-105"', 'Variation': 'BB50V_9B1UC-105'}, {'Query': '"BB50V_9B1UC-105"', 'Variation': 'BB50V_9B1UC-105'}, {'Query': '"BB50V_9B1UC_105" GIV', 'Variation': 'BB50V_9B1UC_105'}, {'Query': '"BB50V_9B1UC_105" Givenchy', 'Variation': 'BB50V_9B1UC_105'}, {'Query': '"BB50V_9B1UC_105" GIVENCHY', 'Variation': 'BB50V_9B1UC_105'}, {'Query': '"BB50V_9B1UC_105"', 'Variation': 'BB50V_9B1UC_105'}, {'Query': '"BB50V_9B1UC_105"', 'Variation': 'BB50V_9B1UC_105'}, {'Query': '"BB50V_9B1UC_105"', 'Variation': 'BB50V_9B1UC_105'}, {'Query': '"BB50V_9B1UC_105"', 'Variation': 'BB50V_9B1UC_105'}, {'Query': '"BB50V_9B1UC_105"', 'Variation': 'BB50V_9B1UC_105'}, {'Query': '"BB50V_9B1UC_105"', 'Variation': 'BB50V_9B1UC_105'}, {'Query': '"BB50V_9B1UC_105"', 'Variation': 'BB50V_9B1UC_105'}, {'Query': '"BB50V_9B1UC_105"', 'Variation': 'BB50V_9B1UC_105'}, {'Query': '"BB50V_9B1UC_105"', 'Variation': 'BB50V_9B1UC_105'}, {'Query': '"BB50V_9B1UC_105"', 'Variation': 'BB50V_9B1UC_105'}, {'Query': '"BB50V_9B1UC_105"', 'Variation': 'BB50V_9B1UC_105'}, {'Query': '"BB50V_9B1UC_105"', 'Variation': 'BB50V_9B1UC_105'}, {'Query': '"BB50V_9B1UC_105"', 'Variation': 'BB50V_9B1UC_105'}, {'Query': '"BB50V_9B1UC_105"', 'Variation': 'BB50V_9B1UC_105'}, {'Query': '"BB50V_9B1UC_105"', 'Variation': 'BB50V_9B1UC_105'}, {'Query': '"BB50V_9B1UC_105"', 'Variation': 'BB50V_9B1UC_105'}, {'Query': '"BB50V_9B1UC_105"', 'Variation': 'BB50V_9B1UC_105'}, {'Query': '"BB50V_9B1UC_105"', 'Variation': 'BB50V_9B1UC_105'}, {'Query': '"BB50V_9B1UC_105"', 'Variation': 'BB50V_9B1UC_105'}, {'Query': '"BB50V_9B1UC_105"', 'Variation': 'BB50V_9B1UC_105'}, {'Query': '"BB50V_9B1UC_105"', 'Variation': 'BB50V_9B1UC_105'}, {'Query': '"BB50V_9B1UC_105"', 'Variation': 'BB50V_9B1UC_105'}, {'Query': '"BB50V_9B1UC_105"', 'Variation': 'BB50V_9B1UC_105'}, {'Query': '"BB50V_9B1UC_105"', 'Variation': 'BB50V_9B1UC_105'}, {'Query': '"BB50V_9B1UC_105"', 'Variation': 'BB50V_9B1UC_105'}, {'Query': '"BB50V_9B1UC105" GIV', 'Variation': 'BB50V_9B1UC105'}, {'Query': '"BB50V_9B1UC105" Givenchy', 'Variation': 'BB50V_9B1UC105'}, {'Query': '"BB50V_9B1UC105" GIVENCHY', 'Variation': 'BB50V_9B1UC105'}, {'Query': '"BB50V_9B1UC105"', 'Variation': 'BB50V_9B1UC105'}, {'Query': '"BB50V_9B1UC105"', 'Variation': 'BB50V_9B1UC105'}, {'Query': '"BB50V_9B1UC105"', 'Variation': 'BB50V_9B1UC105'}, {'Query': '"BB50V_9B1UC105"', 'Variation': 'BB50V_9B1UC105'}, {'Query': '"BB50V_9B1UC105"', 'Variation': 'BB50V_9B1UC105'}, {'Query': '"BB50V_9B1UC105"', 'Variation': 'BB50V_9B1UC105'}, {'Query': '"BB50V_9B1UC105"', 'Variation': 'BB50V_9B1UC105'}, {'Query': '"BB50V_9B1UC105"', 'Variation': 'BB50V_9B1UC105'}, {'Query': '"BB50V_9B1UC105"', 'Variation': 'BB50V_9B1UC105'}, {'Query': '"BB50V_9B1UC105"', 'Variation': 'BB50V_9B1UC105'}, {'Query': '"BB50V_9B1UC105"', 'Variation': 'BB50V_9B1UC105'}, {'Query': '"BB50V_9B1UC105"', 'Variation': 'BB50V_9B1UC105'}, {'Query': '"BB50V_9B1UC105"', 'Variation': 'BB50V_9B1UC105'}, {'Query': '"BB50V_9B1UC105"', 'Variation': 'BB50V_9B1UC105'}, {'Query': '"BB50V_9B1UC105"', 'Variation': 'BB50V_9B1UC105'}, {'Query': '"BB50V_9B1UC105"', 'Variation': 'BB50V_9B1UC105'}, {'Query': '"BB50V_9B1UC105"', 'Variation': 'BB50V_9B1UC105'}, {'Query': '"BB50V_9B1UC105"', 'Variation': 'BB50V_9B1UC105'}, {'Query': '"BB50V_9B1UC105"', 'Variation': 'BB50V_9B1UC105'}, {'Query': '"BB50V_9B1UC105"', 'Variation': 'BB50V_9B1UC105'}, {'Query': '"BB50V_9B1UC105"', 'Variation': 'BB50V_9B1UC105'}, {'Query': '"BB50V_9B1UC105"', 'Variation': 'BB50V_9B1UC105'}, {'Query': '"BB50V_9B1UC105"', 'Variation': 'BB50V_9B1UC105'}, {'Query': '"BB50V_9B1UC105"', 'Variation': 'BB50V_9B1UC105'}, {'Query': '"BB50V_9B1UC105"', 'Variation': 'BB50V_9B1UC105'}, {'Query': '"BB50V_9B1UC105"', 'Variation': 'BB50V_9B1UC105'}, {'Query': '"BB50V9B1UC.105" GIV', 'Variation': 'BB50V9B1UC.105'}, {'Query': '"BB50V9B1UC.105" Givenchy', 'Variation': 'BB50V9B1UC.105'}, {'Query': '"BB50V9B1UC.105" GIVENCHY', 'Variation': 'BB50V9B1UC.105'}, {'Query': '"BB50V9B1UC.105"', 'Variation': 'BB50V9B1UC.105'}, {'Query': '"BB50V9B1UC.105"', 'Variation': 'BB50V9B1UC.105'}, {'Query': '"BB50V9B1UC.105"', 'Variation': 'BB50V9B1UC.105'}, {'Query': '"BB50V9B1UC.105"', 'Variation': 'BB50V9B1UC.105'}, {'Query': '"BB50V9B1UC.105"', 'Variation': 'BB50V9B1UC.105'}, {'Query': '"BB50V9B1UC.105"', 'Variation': 'BB50V9B1UC.105'}, {'Query': '"BB50V9B1UC.105"', 'Variation': 'BB50V9B1UC.105'}, {'Query': '"BB50V9B1UC.105"', 'Variation': 'BB50V9B1UC.105'}, {'Query': '"BB50V9B1UC.105"', 'Variation': 'BB50V9B1UC.105'}, {'Query': '"BB50V9B1UC.105"', 'Variation': 'BB50V9B1UC.105'}, {'Query': '"BB50V9B1UC.105"', 'Variation': 'BB50V9B1UC.105'}, {'Query': '"BB50V9B1UC.105"', 'Variation': 'BB50V9B1UC.105'}, {'Query': '"BB50V9B1UC.105"', 'Variation': 'BB50V9B1UC.105'}, {'Query': '"BB50V9B1UC.105"', 'Variation': 'BB50V9B1UC.105'}, {'Query': '"BB50V9B1UC.105"', 'Variation': 'BB50V9B1UC.105'}, {'Query': '"BB50V9B1UC.105"', 'Variation': 'BB50V9B1UC.105'}, {'Query': '"BB50V9B1UC.105"', 'Variation': 'BB50V9B1UC.105'}, {'Query': '"BB50V9B1UC.105"', 'Variation': 'BB50V9B1UC.105'}, {'Query': '"BB50V9B1UC.105"', 'Variation': 'BB50V9B1UC.105'}, {'Query': '"BB50V9B1UC.105"', 'Variation': 'BB50V9B1UC.105'}, {'Query': '"BB50V9B1UC.105"', 'Variation': 'BB50V9B1UC.105'}, {'Query': '"BB50V9B1UC.105"', 'Variation': 'BB50V9B1UC.105'}, {'Query': '"BB50V9B1UC.105"', 'Variation': 'BB50V9B1UC.105'}, {'Query': '"BB50V9B1UC.105"', 'Variation': 'BB50V9B1UC.105'}, {'Query': '"BB50V9B1UC.105"', 'Variation': 'BB50V9B1UC.105'}, {'Query': '"BB50V9B1UC.105"', 'Variation': 'BB50V9B1UC.105'}, {'Query': '"BB50V9B1UC.105"', 'Variation': 'BB50V9B1UC.105'}, {'Query': '"BB50V9B1UC 105" GIV', 'Variation': 'BB50V9B1UC 105'}, {'Query': '"BB50V9B1UC 105" Givenchy', 'Variation': 'BB50V9B1UC 105'}, {'Query': '"BB50V9B1UC 105" GIVENCHY', 'Variation': 'BB50V9B1UC 105'}, {'Query': '"BB50V9B1UC 105"', 'Variation': 'BB50V9B1UC 105'}, {'Query': '"BB50V9B1UC 105"', 'Variation': 'BB50V9B1UC 105'}, {'Query': '"BB50V9B1UC 105"', 'Variation': 'BB50V9B1UC 105'}, {'Query': '"BB50V9B1UC 105"', 'Variation': 'BB50V9B1UC 105'}, {'Query': '"BB50V9B1UC 105"', 'Variation': 'BB50V9B1UC 105'}, {'Query': '"BB50V9B1UC 105"', 'Variation': 'BB50V9B1UC 105'}, {'Query': '"BB50V9B1UC 105"', 'Variation': 'BB50V9B1UC 105'}, {'Query': '"BB50V9B1UC 105"', 'Variation': 'BB50V9B1UC 105'}, {'Query': '"BB50V9B1UC 105"', 'Variation': 'BB50V9B1UC 105'}, {'Query': '"BB50V9B1UC 105"', 'Variation': 'BB50V9B1UC 105'}, {'Query': '"BB50V9B1UC 105"', 'Variation': 'BB50V9B1UC 105'}, {'Query': '"BB50V9B1UC 105"', 'Variation': 'BB50V9B1UC 105'}, {'Query': '"BB50V9B1UC 105"', 'Variation': 'BB50V9B1UC 105'}, {'Query': '"BB50V9B1UC 105"', 'Variation': 'BB50V9B1UC 105'}, {'Query': '"BB50V9B1UC 105"', 'Variation': 'BB50V9B1UC 105'}, {'Query': '"BB50V9B1UC 105"', 'Variation': 'BB50V9B1UC 105'}, {'Query': '"BB50V9B1UC 105"', 'Variation': 'BB50V9B1UC 105'}, {'Query': '"BB50V9B1UC 105"', 'Variation': 'BB50V9B1UC 105'}, {'Query': '"BB50V9B1UC 105"', 'Variation': 'BB50V9B1UC 105'}, {'Query': '"BB50V9B1UC 105"', 'Variation': 'BB50V9B1UC 105'}, {'Query': '"BB50V9B1UC 105"', 'Variation': 'BB50V9B1UC 105'}, {'Query': '"BB50V9B1UC 105"', 'Variation': 'BB50V9B1UC 105'}, {'Query': '"BB50V9B1UC 105"', 'Variation': 'BB50V9B1UC 105'}, {'Query': '"BB50V9B1UC 105"', 'Variation': 'BB50V9B1UC 105'}, {'Query': '"BB50V9B1UC 105"', 'Variation': 'BB50V9B1UC 105'}, {'Query': '"BB50V9B1UC 105"', 'Variation': 'BB50V9B1UC 105'}, {'Query': '"BB50V9B1UC 105"', 'Variation': 'BB50V9B1UC 105'}, {'Query': '"BB50V9B1UC 105"', 'Variation': 'BB50V9B1UC 105'}, {'Query': '"BB50V9B1UC_105" GIV', 'Variation': 'BB50V9B1UC_105'}, {'Query': '"BB50V9B1UC_105" Givenchy', 'Variation': 'BB50V9B1UC_105'}, {'Query': '"BB50V9B1UC_105" GIVENCHY', 'Variation': 'BB50V9B1UC_105'}, {'Query': '"BB50V9B1UC_105"', 'Variation': 'BB50V9B1UC_105'}, {'Query': '"BB50V9B1UC_105"', 'Variation': 'BB50V9B1UC_105'}, {'Query': '"BB50V9B1UC_105"', 'Variation': 'BB50V9B1UC_105'}, {'Query': '"BB50V9B1UC_105"', 'Variation': 'BB50V9B1UC_105'}, {'Query': '"BB50V9B1UC_105"', 'Variation': 'BB50V9B1UC_105'}, {'Query': '"BB50V9B1UC_105"', 'Variation': 'BB50V9B1UC_105'}, {'Query': '"BB50V9B1UC_105"', 'Variation': 'BB50V9B1UC_105'}, {'Query': '"BB50V9B1UC_105"', 'Variation': 'BB50V9B1UC_105'}, {'Query': '"BB50V9B1UC_105"', 'Variation': 'BB50V9B1UC_105'}, {'Query': '"BB50V9B1UC_105"', 'Variation': 'BB50V9B1UC_105'}, {'Query': '"BB50V9B1UC_105"', 'Variation': 'BB50V9B1UC_105'}, {'Query': '"BB50V9B1UC_105"', 'Variation': 'BB50V9B1UC_105'}, {'Query': '"BB50V9B1UC_105"', 'Variation': 'BB50V9B1UC_105'}, {'Query': '"BB50V9B1UC_105"', 'Variation': 'BB50V9B1UC_105'}, {'Query': '"BB50V9B1UC_105"', 'Variation': 'BB50V9B1UC_105'}, {'Query': '"BB50V9B1UC_105"', 'Variation': 'BB50V9B1UC_105'}, {'Query': '"BB50V9B1UC_105"', 'Variation': 'BB50V9B1UC_105'}, {'Query': '"BB50V9B1UC_105"', 'Variation': 'BB50V9B1UC_105'}, {'Query': '"BB50V9B1UC_105"', 'Variation': 'BB50V9B1UC_105'}, {'Query': '"BB50V9B1UC_105"', 'Variation': 'BB50V9B1UC_105'}, {'Query': '"BB50V9B1UC_105"', 'Variation': 'BB50V9B1UC_105'}, {'Query': '"BB50V9B1UC_105"', 'Variation': 'BB50V9B1UC_105'}, {'Query': '"BB50V9B1UC_105"', 'Variation': 'BB50V9B1UC_105'}, {'Query': '"BB50V9B1UC_105"', 'Variation': 'BB50V9B1UC_105'}, {'Query': '"BB50V9B1UC_105"', 'Variation': 'BB50V9B1UC_105'}, {'Query': '"BB50V9B1UC_105"', 'Variation': 'BB50V9B1UC_105'}, {'Query': '"BB50V9B1UC_105"', 'Variation': 'BB50V9B1UC_105'}, {'Query': '"BB50V9B1UC_105"', 'Variation': 'BB50V9B1UC_105'}, {'Query': '"BB50V9B1UC_105"', 'Variation': 'BB50V9B1UC_105'}, {'Query': '"BB50V9B1UC105" GIV', 'Variation': 'BB50V9B1UC105'}, {'Query': '"BB50V9B1UC105" Givenchy', 'Variation': 'BB50V9B1UC105'}, {'Query': '"BB50V9B1UC105" GIVENCHY', 'Variation': 'BB50V9B1UC105'}, {'Query': '"BB50V9B1UC105"', 'Variation': 'BB50V9B1UC105'}, {'Query': '"BB50V9B1UC105"', 'Variation': 'BB50V9B1UC105'}, {'Query': '"BB50V9B1UC105"', 'Variation': 'BB50V9B1UC105'}, {'Query': '"BB50V9B1UC105"', 'Variation': 'BB50V9B1UC105'}, {'Query': '"BB50V9B1UC105"', 'Variation': 'BB50V9B1UC105'}, {'Query': '"BB50V9B1UC105"', 'Variation': 'BB50V9B1UC105'}, {'Query': '"BB50V9B1UC105"', 'Variation': 'BB50V9B1UC105'}, {'Query': '"BB50V9B1UC105"', 'Variation': 'BB50V9B1UC105'}, {'Query': '"BB50V9B1UC105"', 'Variation': 'BB50V9B1UC105'}, {'Query': '"BB50V9B1UC105"', 'Variation': 'BB50V9B1UC105'}, {'Query': '"BB50V9B1UC105"', 'Variation': 'BB50V9B1UC105'}, {'Query': '"BB50V9B1UC105"', 'Variation': 'BB50V9B1UC105'}, {'Query': '"BB50V9B1UC105"', 'Variation': 'BB50V9B1UC105'}, {'Query': '"BB50V9B1UC105"', 'Variation': 'BB50V9B1UC105'}, {'Query': '"BB50V9B1UC105"', 'Variation': 'BB50V9B1UC105'}, {'Query': '"BB50V9B1UC105"', 'Variation': 'BB50V9B1UC105'}, {'Query': '"BB50V9B1UC105"', 'Variation': 'BB50V9B1UC105'}, {'Query': '"BB50V9B1UC105"', 'Variation': 'BB50V9B1UC105'}, {'Query': '"BB50V9B1UC105"', 'Variation': 'BB50V9B1UC105'}, {'Query': '"BB50V9B1UC105"', 'Variation': 'BB50V9B1UC105'}, {'Query': '"BB50V9B1UC105"', 'Variation': 'BB50V9B1UC105'}, {'Query': '"BB50V9B1UC105"', 'Variation': 'BB50V9B1UC105'}, {'Query': '"BB50V9B1UC105"', 'Variation': 'BB50V9B1UC105'}, {'Query': '"BB50V9B1UC105"', 'Variation': 'BB50V9B1UC105'}, {'Query': '"BB50V9B1UC105"', 'Variation': 'BB50V9B1UC105'}, {'Query': '"BB50V9B1UC105"', 'Variation': 'BB50V9B1UC105'}, {'Query': '"BB50V9B1UC105"', 'Variation': 'BB50V9B1UC105'}, {'Query': '"BB50V9B1UC105"', 'Variation': 'BB50V9B1UC105'}, {'Query': '"BB50V9B1UC105"', 'Variation': 'BB50V9B1UC105'}, {'Query': '"BB50V9B1UC105"', 'Variation': 'BB50V9B1UC105'}]
    variations_list=[]
    for item in temp_list:
        variations_list.append(item["Variation"])
    approved_seller_list = [
        'saks fifth avenue',
        'nordstrom',
        'fwrd',
        'forward',
        'ssense',
        'net-a-porter'
    ]
    #variations_list will be taken from the variation_table
    #for modesens returns list of true/false one True/False for each listed product data
    #change modesens when SQL implemented
    print(check_product_data(input,variations_list,approved_seller_list))