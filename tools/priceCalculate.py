#coding=utf-8

class checkout_price:
    """
    #计算折扣
    def discount_price(self,sale_price,discountFlag,discountNum):
        if discountFlag==0:
            discountPrice=round(sale_price*discountNum)
        else:
            discountPrice=sale_price-discountNum
        print("discount:"+str(discountPrice))
        return discountPrice
    """        
    #计算税费    
    def tax_price(self,sale_price,ship_price,exciseTaxFlag):
        customsValue=round(sale_price+ship_price,2)
        print("customsValue:"+str(customsValue))        
        if exciseTaxFlag==0:
            exciseTax=0
        else:
            exciseTax=round(round(customsValue/0.7,2)*0.3,2)
            print("exciseTax:"+str(exciseTax))    
        addedTax=round(round(customsValue+exciseTax,2)*0.17,2)
        print("addedTax:"+str(addedTax))
        importTax=round(round(exciseTax+addedTax,2)*0.7,2)
        print("tax:"+str(importTax))
        return importTax
    
    #计算运费
    def ship_price(self,sale_price,warehouse_type,paperDiaper,Number):
        if paperDiaper==None:
            if warehouse_type!=8:
                if sale_price>=88:
                    ship_price=0
                else:
                    ship_price=10
            else:
                if sale_price>=228:
                    ship_price=0
                else:
                    ship_price=20
        else:
            if Number>=2:
                ship_price=0
            else:
                ship_price=10
        print("shipPrice:"+str(ship_price))
        return ship_price
    
    #计算最终价格        
    def all_price(self,sale_price,warehouse_type,Number,redbag_price=0,coupon_price=0,
                  paperDiaper=None,discountNum=0,exciseTaxFlag=0):
        salePrice=sale_price*Number
        #activityPrice=self.discount_price(salePrice,discountFlag,discountNum)
        shipPrice=self.ship_price(salePrice,warehouse_type,paperDiaper,Number)
        if warehouse_type!=6:
            taxPrice=0
        else:
            taxPrice=self.tax_price(salePrice-discountNum,shipPrice,exciseTaxFlag)
        allPrice=round(salePrice+shipPrice+taxPrice-redbag_price-coupon_price-discountNum,2)
        return allPrice
    
if __name__=="__main__":
    priceCalculate=checkout_price()
    allPrice=priceCalculate.all_price(32,6,1,exciseTaxFlag=1)
    allPrice=priceCalculate.all_price(78,7,1,exciseTaxFlag=0)
    print("allPrice:"+str(allPrice))