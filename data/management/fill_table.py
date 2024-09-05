import pandas as pd
from index import RetailPrices,Session

with Session.begin() as db:
    data=pd.read_csv("data/retail_prices.csv")  
    for index ,row in data.iterrows():
        retail_prices=RetailPrices(
        product_id=row[0],
        product_category_name=row[1],
        month_year=row[2],
        qty=row[3],
        total_price=row[4],
        freight_price=row[5],
        unit_price=row[6],
        product_name_length=row[7],
        product_description_length=row[8],
        product_photos_qty=row[9],
        product_weight_g=row[10],
        customers_product_score=row[11],
        customers=row[12],
        weekday=row[13],
        weekend=row[14],
        holiday=row[15],
        month=row[16],
        year=row[17],
        volume=row[18],
        comp_1=row[19],
        ps1=row[20],
        fp1=row[21],
        comp_2=row[22],
        ps2=row[23],
        fp2=row[24],
        comp_3=row[25],
        ps3=row[26],
        fp3=row[27],
        lag_price=row[28]
    )
    db.add(retail_prices)