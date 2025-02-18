import json
import re
from bs4 import BeautifulSoup


class ProductSchema:
    def __init__(self, product_schemas, source):
        self.product_schemas = product_schemas
        self.source = source
        self.parsed_products = self.parse_product_schemas(self.product_schemas)

    def get_parsed_products(self):
        return self.parsed_products

    def parse_product_schemas(self, product_schemas):
        parsed_products = []

        for schema in product_schemas:
            if schema.get('@type') == 'Product':
                offers_info = self.extract_offers(schema)
                for offer in offers_info:

                    if (offer.get('@type') == 'Offer'):
                        prices = self.get_prices(offer)
                        currency = self.get_currency(offer)
                        seller = self.get_seller(offer)
                        description = self.get_description(offer)
                        title = self.get_title(offer)
                        images = self.get_images(offer)
                        url = self.get_url(offer)
                        product_details = self.create_product_details(title, images, prices, currency, url, description,
                                                                      seller, schema)
                        parsed_products.append(product_details)

                    elif (offer.get('@type') == 'AggregateOffer'):
                        for suboffer in self.extract_offers(offer):
                            prices = self.get_prices(suboffer)
                            currency = self.get_currency(suboffer)
                            seller = self.get_seller(suboffer)
                            description = self.get_description(suboffer)
                            title = self.get_title(suboffer)
                            images = self.get_images(suboffer)
                            url = self.get_url(suboffer)
                            product_details = self.create_product_details(title, images, prices, currency, url,
                                                                          description, seller, schema)
                            parsed_products.append(product_details)
        return parsed_products

    def get_title(self, data):
        if isinstance(data, dict):
            for key, value in data.items():
                if key.lower() not in ['seller', 'brand']:
                    if key == 'name':
                        return value
                    else:
                        result = self.get_title(value)
                        if result:
                            return result
        else:
            return None

    def get_images(self, data):
        images = []
        if isinstance(data, dict):
            for key, value in data.items():
                if key == 'image' and isinstance(value, (list, str)):
                    if isinstance(value, list):
                        images.extend(value)
                    else:
                        images.append(value)
                else:
                    images.extend(self.get_images(value))
        elif isinstance(data, list):
            for item in data:
                images.extend(self.get_images(item))
        return images

    def get_prices(self, data):
        prices = []
        if isinstance(data, dict):
            for key, value in data.items():
                if key.lower() in ['price', 'lowprice', 'highprice'] and isinstance(value, str):
                    prices.append(value.replace("$", "").replace(",", "").replace(" ", ""))
                elif key.lower() in ['price', 'lowprice', 'highprice'] and isinstance(value, (int, float)):
                    prices.append(value)
                else:
                    prices.extend(self.get_prices(value))
        elif isinstance(data, list):
            for item in data:
                prices.extend(self.get_prices(item))
        return prices

    def get_currency(self, data):
        if isinstance(data, dict):
            currency = data.get('priceCurrency', None)
            if currency:
                return currency
            for value in data.values():
                result = self.get_currency(value)
                if result:
                    return result
        elif isinstance(data, list):
            for item in data:
                result = self.get_currency(item)
                if result:
                    return result

    def get_url(self, data):
        if self.source == "modesens":
            if isinstance(data, dict):
                url = data.get('url', None)
                if url:
                    return f"https://modesens.com{url}"
                for value in data.values():
                    result = self.get_url(value)
                    if result:
                        return f"https://modesens.com{url}"
            elif isinstance(data, list):
                for item in data:
                    result = self.get_url(item)
                    if result:
                        return f"https://modesens.com{result}"
        else:
            if isinstance(data, dict):
                url = data.get('url', None)
                if url:
                    return f"{url}"
                for value in data.values():
                    result = self.get_url(value)
                    if result:
                        return f"{url}"
            elif isinstance(data, list):
                for item in data:
                    result = self.get_url(item)
                    if result:
                        return f"{result}"

    def get_description(self, data):
        if isinstance(data, dict):
            for key, value in data.items():
                if key == 'description':
                    return value
                else:
                    result = self.get_description(value)
                    if result:
                        return result

    def get_seller(self, data):
        if isinstance(data, dict):
            seller = data.get('seller', None)
            if isinstance(seller, dict) and 'name' in seller:
                return seller['name']
            for value in data.values():
                result = self.get_seller(value)
                if result:
                    return result
        elif isinstance(data, list):
            for item in data:
                result = self.get_seller(item)
                if result:
                    return result

    def extract_offers(self, data):
        offers = []

        if isinstance(data, dict):
            if 'offers' in data:
                # Directly append the offer or aggregate offer object
                offer_data = data['offers']
                if isinstance(offer_data, list):
                    offers.extend(offer_data)  # List of individual offers
                else:
                    offers.append(offer_data)  # Single or aggregate offer
            else:
                # Recursively search for offers in other dictionary values
                for value in data.values():
                    offers.extend(self.extract_offers(value))

        elif isinstance(data, list):
            # If the data is a list, apply the function to each element
            for item in data:
                offers.extend(self.extract_offers(item))

        return offers

    def create_product_details(self, title, images, prices, currency, url, description, seller, schema):
        product_details = {
            'title': title,
            'images': images,
            'prices': prices,
            'currency': currency,
            'url': url,
            'description': description,
            'seller': seller.lower() if seller else None
        }
        for key, value in product_details.items():
            if value in [None, [], "", {}]:
                if key == 'title':
                    product_details[key] = self.get_title(schema)
                elif key == 'images':
                    product_details[key] = self.get_images(schema)
                elif key == 'prices':
                    product_details[key] = self.get_prices(schema)
                elif key == 'currency':
                    product_details[key] = self.get_currency(schema)
                elif key == 'url':
                    product_details[key] = self.get_url(schema)
                elif key == 'description':
                    product_details[key] = self.get_description(schema)
                elif key == 'seller':
                    seller = self.get_seller(schema)
                    product_details[key] = seller.lower() if seller else seller
        return product_details


class ModesensParser():
    def __init__(self, html):
        self.soup = BeautifulSoup(html, 'html.parser')
        self.blocks = self.extract_blocks()
        self.product_details = self.get_product_details()

    def extract_blocks(self):
        blocks = self.soup.find_all('div', class_='d-inline-block')
        return blocks

    def get_product_details(self):
        product_details = []
        for block in self.blocks:
            # Handle different types of price blocks
            product_detail = {}
            price_box = block.find('div', class_='price-box') or block.find('span', class_='price-box')
            merchant_name = block.find('div', class_='merchant-name')

            # Extracting seller
            seller = merchant_name.get_text(strip=True) if merchant_name else None
            prices = []
            if price_box:
                # Find all span elements that potentially contain prices
                price_spans = price_box.find_all('span', class_='position-relative') or [price_box]
                for span in price_spans:
                    # Extracting numeric part of the price
                    price_text = span.get_text(strip=True)
                    match = re.search(r'\d+(?:\.\d+)?', price_text)

                    if match:
                        price = float(match.group())
                        prices.append(price)

                    # Extracting currency symbol
                    currency = price_text[0] if price_text else None

            # Store the highest price, seller, and currency
            if prices:
                highest_price = max(prices)
                product_detail['price'] = highest_price
                product_detail['seller'] = seller
                product_detail['currency'] = currency
                product_details.append(product_detail)

        return product_details

class GeneralParser:
    def __init__(self,html_content,settings,brand_id):
        brand_settings=settings.get(f"{brand_id}")
        self.product_details=self.get_product_details(html_content,brand_settings)
    def get_product_details(self,html_content,brand_settings):
        product_details={}
        original_price=""
        sale_price=""
        soup = BeautifulSoup(html_content, 'html.parser')
        outer_type=brand_settings.get("Outer_Type","")
        outer_class=brand_settings.get("Outer_Class","")
        outer_details_block=soup.find(outer_type,class_=outer_class)
        #Get prices
        price_method = brand_settings.get("Price_Method", "")
        if price_method=="Require_Outer":
            # Get original price
            original_price_type = brand_settings.get("Original_Price_Type", "")
            original_price_class = brand_settings.get("Original_Price_Class", "")
            original_price_type_2 = brand_settings.get("Original_Price_Type_2", "")
            original_price_class_2 = brand_settings.get("Original_Price_Class_2", "")
            outer_price_type = brand_settings.get("Price_Outer_Type", "")
            outer_price_class = brand_settings.get("Price_Outer_Class", "")
            outer_price_block = outer_details_block.find(outer_price_type,class_=outer_price_class)
            original_price_block = outer_price_block.find(original_price_type, class_=original_price_class)
            if original_price_block:
                original_price = original_price_block.text.strip()
                product_details["Original_Price"] = original_price
            if original_price_class_2 and original_price_type_2:
                original_price_block = outer_price_block.find(original_price_type_2, class_=original_price_class_2)
                if original_price_block:
                    original_price = original_price_block.text.strip()
                    product_details["Original_Price"] = original_price
            # Get sale price
            sale_price_type = brand_settings.get("Sales_Price_Type", "")
            sale_price_class = brand_settings.get("Sales_Price_Class", "")
            sale_price_block = outer_price_block.find(sale_price_type, class_=sale_price_class)
            if sale_price_block:
                sale_price = sale_price_block.text.strip()
                product_details["Sale_Price"] = sale_price

        else:
            # Get original price
            original_price_type=brand_settings.get("Original_Price_Type","")
            original_price_class = brand_settings.get("Original_Price_Class","")
            original_price_type_2=brand_settings.get("Original_Price_Type_2","")
            original_price_class_2=brand_settings.get("Original_Price_Class_2","")

            original_price_block=outer_details_block.find(original_price_type, class_=original_price_class)
            if original_price_block:
                original_price=original_price_block.text.strip()
                product_details["Original_Price"]=original_price
            if original_price_class_2 and original_price_type_2:
                original_price_block = outer_details_block.find(original_price_type_2, class_=original_price_class_2)
                if original_price_block:
                    original_price = original_price_block.text.strip()
                    product_details["Original_Price"] = original_price

            # Get sale price
            sale_price_type = brand_settings.get("Sales_Price_Type","")
            sale_price_class = brand_settings.get("Sales_Price_Class","")
            sale_price_block=outer_details_block.find(sale_price_type, class_=sale_price_class)
            if sale_price_block:
                sale_price = sale_price_block.text.strip()
                product_details["Sale_Price"] = sale_price


        # Fix prices
        if not original_price and sale_price:
            original_price=sale_price
            product_details["Original_Price"] = original_price
        if not sale_price and original_price:
            sale_price = original_price
            product_details["Sale_Price"] = sale_price
        if price_method=="Switch_Prices":
            original_price_num=float(original_price.replace("$",""))
            sale_price_num=float(sale_price.replace("$",""))
            if original_price_num<sale_price_num:
                product_details["Original_Price"] = sale_price
                product_details["Sale_Price"] = original_price

        # Get currency
        if "$" in sale_price or "$" in original_price:
            product_details["Currency"] = "USD"
        if "€" in sale_price or "€" in original_price:
            product_details["Currency"] = "Euro"
        currency_type = brand_settings.get("Currency_Type", "")
        currency_class = brand_settings.get("Currency_Class", "")
        currency_block = outer_details_block.find(currency_type, class_=currency_class)
        if currency_block:
            currency = currency_block.text.strip()
            product_details["Currency"] = currency

        # Get name
        name_type = brand_settings.get("Name_Type","")
        name_class = brand_settings.get("Name_Class","")
        name_block=outer_details_block.find(name_type, class_=name_class)
        if name_block:
            name = name_block.text.strip()
            product_details["Name"] = name

        # Get source
        source_type = brand_settings.get("Source_Type","")
        source_class = brand_settings.get("Source_Class","")
        source_block=outer_details_block.find(source_type, class_=source_class)
        if source_block:
            source = source_block.text.strip()
            product_details["Source"] = source

        # Get color
        color_type = brand_settings.get("Color_Type","")
        color_class = brand_settings.get("Color_Class","")
        color_block=outer_details_block.find(color_type, class_=color_class)
        if color_block:
            color = color_block.text.strip()
            product_details["Color"] = color

        # Get composition
        composition_type = brand_settings.get("Composition_Type","")
        composition_class = brand_settings.get("Composition_Class","")
        composition_block=outer_details_block.find(composition_type, class_=composition_class)
        if composition_block:
            composition = composition_block.text.strip()
            product_details["Composition"] = composition

        # Get description
        description_type = brand_settings.get("Description_Type","")
        description_class = brand_settings.get("Description_Class","")
        description_block=outer_details_block.find(description_type, class_=description_class)
        if description_block:
            description = description_block.text.strip()
            product_details["Description"] = description

        #Get images
        images_type = brand_settings.get("Images_Type", "")
        images_class = brand_settings.get("Images_Class", "")
        images_method = brand_settings.get("Images_Method", "")
        images_key = brand_settings.get("Images_Key", "")
        print(images_method)
        images_blocks = outer_details_block.find_all(images_type, class_=images_class)
        print(images_blocks)
        for images_block in images_blocks:
            if images_block:
                product_details["Images"]=[]
                if images_method=="Dictionary":
                    images=images_block[images_key]
                    print(images)
                    product_details["Images"].append(images)
                else:
                    images = images_block.text.strip()
                    product_details["Images"].append(images)

        # Get product id
        pid_1_type = brand_settings.get("Product_ID_1_Type", "")
        pid_1_class = brand_settings.get("Product_ID_1_Class", "")
        pid_1_method = brand_settings.get("Product_ID_1_Method", "")
        pid_1_text = brand_settings.get("Product_ID_1_Text", "")
        pid_2_type = brand_settings.get("Product_ID_2_Type", "")
        pid_2_class = brand_settings.get("Product_ID_2_Class", "")
        pid_2_method = brand_settings.get("Product_ID_2_Method", "")
        pid_2_text = brand_settings.get("Product_ID_2_Text", "")
        pid_3_type = brand_settings.get("Product_ID_3_Type", "")
        pid_3_class = brand_settings.get("Product_ID_3_Class", "")
        pid_3_method = brand_settings.get("Product_ID_3_Method", "")
        pid_3_text = brand_settings.get("Product_ID_3_Text", "")
        pid_4_type = brand_settings.get("Product_ID_4_Type", "")
        pid_4_class = brand_settings.get("Product_ID_4_Class", "")
        pid_4_method = brand_settings.get("Product_ID_4_Method", "")
        pid_4_text = brand_settings.get("Product_ID_4_Text", "")
        pid_list = [{"pid_type": pid_1_type,
                     "pid_class": pid_1_class,
                     "pid_method": pid_1_method,
                     "pid_text": pid_1_text},
                    {"pid_type": pid_2_type,
                     "pid_class": pid_2_class,
                     "pid_method": pid_2_method,
                     "pid_text": pid_2_text},
                    {"pid_type": pid_3_type,
                     "pid_class": pid_3_class,
                     "pid_method": pid_3_method,
                     "pid_text": pid_3_text},
                    {"pid_type": pid_4_type,
                     "pid_class": pid_4_class,
                     "pid_method": pid_4_method,
                     "pid_text": pid_4_text}
                    ]
        for index, pid_dict in enumerate(pid_list):
            pid_type = pid_dict["pid_type"]
            pid_class = pid_dict["pid_class"]
            pid_method = pid_dict["pid_method"]
            pid_text = pid_dict["pid_text"]
            if pid_method == "List":
                pid_blocks = outer_details_block.find_all(pid_type, class_=pid_class)
                for pid_block in pid_blocks:
                    if pid_block:
                        if pid_text in pid_block.text.strip():
                            pid = pid_block.text.strip().replace(pid_text,"")
                            product_details[f"Product_ID_{index+1}"] = pid
            else:
                pid_block = outer_details_block.find(pid_type, class_=pid_class)
                if pid_block:
                    pid = pid_block.text.strip()
                    product_details[f"Product_ID_{index+1}"] = pid
        #Get brand name (mainly whitelist)
        brand_name_class = brand_settings.get("Brand_Name_Class", "")
        brand_name_type = brand_settings.get("Brand_Name_Type", "")
        brand_name_block = outer_details_block.find(brand_name_type, class_=brand_name_class)
        if brand_name_block:
            brand_name = brand_name_block.text.strip()
            product_details["Brand_Name"] = brand_name
        return product_details

def extract_product_schema(html_content):
    product_schemas = []  # List to store all found product schemas

    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        schema_tags = soup.find_all('script', {'type': 'application/ld+json'})

        for tag in schema_tags:
            try:
                data = json.loads(tag.text)
                if data.get('@type') == 'Product':
                    # Log the raw product schema for debugging
                    print("Raw Product Schema: %s", json.dumps(data, indent=4))
                    product_schemas.append(data)
            except json.JSONDecodeError:
                continue

        if not product_schemas:
            print("No Product schema found in the HTML content.")
            return None

        return product_schemas
    except Exception as e:
        print(f"Error extracting product schemas from HTML: {e}")
        return None


if __name__=="__main__":
    input={'URL': 'https://www.saksfifthavenue.com/product/ralph-lauren-purple-label-striped-cotton-button-up-shirt-0400021783286.html?dwvar_0400021783286_color=GREY%20WHITE', 'Variations': ['BB60KSB24E341'], 'Level': 'whitelist', 'Currency': 'Wrong Currency','Whitelist_ID':'0000'}
    settings = json.loads(open("parsing_settings.json").read())
    brand_id = "201"
    level=input["Level"]
    source_url=input["URL"]
    product_details="No product details found"
    whitelist_id=input.get('Whitelist_ID')
    if level=="unapproved":
        #unapproved_html_content=input["html_url"]
        unapproved_html_content =open("output.html").read()
        product_schema=extract_product_schema(unapproved_html_content)
        if product_schema:
            SchemaParser=ProductSchema(product_schema,source_url)
            product_details=SchemaParser.parsed_products
        print(product_details)
    elif level=="whitelist":
        whitelist_html_content=open("output.html").read()
        product_details=GeneralParser(whitelist_html_content,settings,whitelist_id).product_details
        print(product_details)
    elif level == "modesens":
        # modesens_html_content=input["html_url"]
        modesens_html_content = open("output.html").read()
        product_details=ModesensParser(modesens_html_content).product_details
        print(product_details)
    elif level=="brand":
        # brand_html_content=input["html_url"]
        brand_html_content=open("output.html").read()
        product_details=GeneralParser(brand_html_content,settings,brand_id).product_details
        print(product_details)
    input["Product_Details"]=product_details
    print(input)
