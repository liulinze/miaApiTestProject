#7-1有效可单独售卖的有库存且仓库属于7的特卖商品---sku仅存在于有效未开始特卖中---下单成功
SELECT i.id,i.warehouse_type,s.warehouse_id,s.stock_quantity,s.item_size,i.sale_price FROM item AS i JOIN stock_item AS s
WHERE i.id=s.item_id AND i.status=1 AND i.is_spu=0 AND i.is_outlets=1 AND i.is_single_sale=1 AND s.status=1
AND i.warehouse_type=7 AND s.stock_quantity>100
AND i.id IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()<oi.start_time AND oi.STATUS=1)
AND i.id IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()<oi.start_time AND oi.STATUS=1)
AND i.id NOT IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()>=oi.start_time AND NOW()<=oi.end_time AND oi.STATUS=1)
AND i.id NOT IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()>oi.end_time AND oi.STATUS=1)
AND i.id NOT IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()<oi.start_time AND oi.STATUS!=1)
AND i.id NOT IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()>=oi.start_time AND NOW()<=oi.end_time AND oi.STATUS!=1)
AND i.id NOT IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()>oi.end_time AND oi.STATUS!=1);

#7-2有效可单独售卖的有库存且仓库属于7的特卖商品---sku仅存在于有效已开始特卖中---下单成功
SELECT i.id,i.warehouse_type,s.warehouse_id,s.stock_quantity,s.item_size,i.sale_price FROM item AS i JOIN stock_item AS s
WHERE i.id=s.item_id AND i.status=1 AND i.is_spu=0 AND i.is_outlets=1 AND i.is_single_sale=1 AND s.status=1
AND i.warehouse_type=7 AND s.stock_quantity>100
AND i.id NOT IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()<oi.start_time AND oi.STATUS=1)
AND i.id IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()>=oi.start_time AND NOW()<=oi.end_time AND oi.STATUS=1)
AND i.id NOT IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()>oi.end_time AND oi.STATUS=1)
AND i.id NOT IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()<oi.start_time AND oi.STATUS!=1)
AND i.id NOT IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()>=oi.start_time AND NOW()<=oi.end_time AND oi.STATUS!=1)
AND i.id NOT IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()>oi.end_time AND oi.STATUS!=1);

#7-3有效可单独售卖的有库存且仓库属于7的特卖商品---sku仅存在于有效已结束特卖中---703
SELECT i.id,i.warehouse_type,s.warehouse_id,s.stock_quantity,s.item_size,i.sale_price FROM item AS i JOIN stock_item AS s
WHERE i.id=s.item_id AND i.status=1 AND i.is_spu=0 AND i.is_outlets=1 AND i.is_single_sale=1 AND s.status=1
AND i.warehouse_type=7 AND s.stock_quantity>100
AND i.id NOT IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()<oi.start_time AND oi.STATUS=1)
AND i.id NOT IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()>=oi.start_time AND NOW()<=oi.end_time AND oi.STATUS=1)
AND i.id IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()>oi.end_time AND oi.STATUS=1)
AND i.id NOT IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()<oi.start_time AND oi.STATUS!=1)
AND i.id NOT IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()>=oi.start_time AND NOW()<=oi.end_time AND oi.STATUS!=1)
AND i.id NOT IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()>oi.end_time AND oi.STATUS!=1);

#7-4有效可单独售卖的有库存且仓库属于7的特卖商品---sku仅存在于无效未开始特卖中---结果未知
SELECT i.id,i.warehouse_type,s.warehouse_id,s.stock_quantity,s.item_size,i.sale_price FROM item AS i JOIN stock_item AS s
WHERE i.id=s.item_id AND i.status=1 AND i.is_spu=0 AND i.is_outlets=1 AND i.is_single_sale=1 AND s.status=1
AND i.warehouse_type=7 AND s.stock_quantity>100
AND i.id NOT IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()<oi.start_time AND oi.STATUS=1)
AND i.id NOT IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()>=oi.start_time AND NOW()<=oi.end_time AND oi.STATUS=1)
AND i.id NOT IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()>oi.end_time AND oi.STATUS=1)
AND i.id IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()<oi.start_time AND oi.STATUS!=1)
AND i.id NOT IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()>=oi.start_time AND NOW()<=oi.end_time AND oi.STATUS!=1)
AND i.id NOT IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()>oi.end_time AND oi.STATUS!=1);

#7-5有效可单独售卖的有库存且仓库属于7的特卖商品---sku仅存在于无效已开始特卖中---结果未知
SELECT i.id,i.warehouse_type,s.warehouse_id,s.stock_quantity,s.item_size,i.sale_price FROM item AS i JOIN stock_item AS s
WHERE i.id=s.item_id AND i.status=1 AND i.is_spu=0 AND i.is_outlets=1 AND i.is_single_sale=1 AND s.status=1
AND i.warehouse_type=7 AND s.stock_quantity>100
AND i.id NOT IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()<oi.start_time AND oi.STATUS=1)
AND i.id NOT IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()>=oi.start_time AND NOW()<=oi.end_time AND oi.STATUS=1)
AND i.id NOT IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()>oi.end_time AND oi.STATUS=1)
AND i.id NOT IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()<oi.start_time AND oi.STATUS!=1)
AND i.id IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()>=oi.start_time AND NOW()<=oi.end_time AND oi.STATUS!=1)
AND i.id NOT IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()>oi.end_time AND oi.STATUS!=1);

#7-6有效可单独售卖的有库存且仓库属于7的特卖商品---sku仅存在于无效已结束特卖中---结果未知
SELECT i.id,i.warehouse_type,s.warehouse_id,s.stock_quantity,s.item_size,i.sale_price FROM item AS i JOIN stock_item AS s
WHERE i.id=s.item_id AND i.status=1 AND i.is_spu=0 AND i.is_outlets=1 AND i.is_single_sale=1 AND s.status=1
AND i.warehouse_type=7 AND s.stock_quantity>100
AND i.id NOT IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()<oi.start_time AND oi.STATUS=1)
AND i.id NOT IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()>=oi.start_time AND NOW()<=oi.end_time AND oi.STATUS=1)
AND i.id NOT IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()>oi.end_time AND oi.STATUS=1)
AND i.id NOT IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()<oi.start_time AND oi.STATUS!=1)
AND i.id NOT IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()>=oi.start_time AND NOW()<=oi.end_time AND oi.STATUS!=1)
AND i.id IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()>oi.end_time AND oi.STATUS!=1);

#7-7有效可单独售卖的有库存且仓库属于7的特卖商品---sku未加入任何特卖中---下单成功
SELECT i.id,i.warehouse_type,s.warehouse_id,s.stock_quantity,s.item_size,i.sale_price FROM item AS i JOIN stock_item AS s
WHERE i.id=s.item_id AND i.status=1 AND i.is_spu=0 AND i.is_outlets=1 AND i.is_single_sale=1 AND s.status=1
AND i.warehouse_type=7 AND s.stock_quantity>100
AND i.id NOT IN(SELECT DISTINCT sku FROM oper_outlet_goods);

#7-8有效可单独售卖的有库存且仓库属于7的非特卖商品---sku仅存在于有效未开始特卖中---下单成功
SELECT i.id,i.warehouse_type,s.warehouse_id,s.stock_quantity,s.item_size,i.sale_price FROM item AS i JOIN stock_item AS s
WHERE i.id=s.item_id AND i.status=1 AND i.is_spu=0 AND i.is_outlets=0 AND i.is_single_sale=1 AND s.status=1
AND i.warehouse_type=7 AND s.stock_quantity>100
AND i.id IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()<oi.start_time AND oi.STATUS=1)
AND i.id IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()<oi.start_time AND oi.STATUS=1)
AND i.id NOT IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()>=oi.start_time AND NOW()<=oi.end_time AND oi.STATUS=1)
AND i.id NOT IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()>oi.end_time AND oi.STATUS=1)
AND i.id NOT IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()<oi.start_time AND oi.STATUS!=1)
AND i.id NOT IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()>=oi.start_time AND NOW()<=oi.end_time AND oi.STATUS!=1)
AND i.id NOT IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()>oi.end_time AND oi.STATUS!=1);

#7-9有效可单独售卖的有库存且仓库属于7的非特卖商品---sku仅存在于有效已开始特卖中---下单成功
SELECT i.id,i.warehouse_type,s.warehouse_id,s.stock_quantity,s.item_size,i.sale_price FROM item AS i JOIN stock_item AS s
WHERE i.id=s.item_id AND i.status=1 AND i.is_spu=0 AND i.is_outlets=0 AND i.is_single_sale=1 AND s.status=1
AND i.warehouse_type=7 AND s.stock_quantity>100
AND i.id NOT IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()<oi.start_time AND oi.STATUS=1)
AND i.id IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()>=oi.start_time AND NOW()<=oi.end_time AND oi.STATUS=1)
AND i.id NOT IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()>oi.end_time AND oi.STATUS=1)
AND i.id NOT IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()<oi.start_time AND oi.STATUS!=1)
AND i.id NOT IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()>=oi.start_time AND NOW()<=oi.end_time AND oi.STATUS!=1)
AND i.id NOT IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()>oi.end_time AND oi.STATUS!=1);

#7-10有效可单独售卖的有库存且仓库属于7的非特卖商品---sku仅存在于有效已结束特卖中---下单成功
SELECT i.id,i.warehouse_type,s.warehouse_id,s.stock_quantity,s.item_size,i.sale_price FROM item AS i JOIN stock_item AS s
WHERE i.id=s.item_id AND i.status=1 AND i.is_spu=0 AND i.is_outlets=0 AND i.is_single_sale=1 AND s.status=1
AND i.warehouse_type=7 AND s.stock_quantity>100
AND i.id NOT IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()<oi.start_time AND oi.STATUS=1)
AND i.id NOT IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()>=oi.start_time AND NOW()<=oi.end_time AND oi.STATUS=1)
AND i.id IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()>oi.end_time AND oi.STATUS=1)
AND i.id NOT IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()<oi.start_time AND oi.STATUS!=1)
AND i.id NOT IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()>=oi.start_time AND NOW()<=oi.end_time AND oi.STATUS!=1)
AND i.id NOT IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()>oi.end_time AND oi.STATUS!=1);

#7-11有效可单独售卖的有库存且仓库属于7的非特卖商品---sku仅存在于无效未开始特卖中---结果未知
SELECT i.id,i.warehouse_type,s.warehouse_id,s.stock_quantity,s.item_size,i.sale_price FROM item AS i JOIN stock_item AS s
WHERE i.id=s.item_id AND i.status=1 AND i.is_spu=0 AND i.is_outlets=0 AND i.is_single_sale=1 AND s.status=1
AND i.warehouse_type=7 AND s.stock_quantity>100
AND i.id NOT IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()<oi.start_time AND oi.STATUS=1)
AND i.id NOT IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()>=oi.start_time AND NOW()<=oi.end_time AND oi.STATUS=1)
AND i.id NOT IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()>oi.end_time AND oi.STATUS=1)
AND i.id IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()<oi.start_time AND oi.STATUS!=1)
AND i.id NOT IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()>=oi.start_time AND NOW()<=oi.end_time AND oi.STATUS!=1)
AND i.id NOT IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()>oi.end_time AND oi.STATUS!=1);

#7-12有效可单独售卖的有库存且仓库属于7的非特卖商品---sku仅存在于无效已开始特卖中---结果未知
SELECT i.id,i.warehouse_type,s.warehouse_id,s.stock_quantity,s.item_size,i.sale_price FROM item AS i JOIN stock_item AS s
WHERE i.id=s.item_id AND i.status=1 AND i.is_spu=0 AND i.is_outlets=0 AND i.is_single_sale=1 AND s.status=1
AND i.warehouse_type=7 AND s.stock_quantity>100
AND i.id NOT IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()<oi.start_time AND oi.STATUS=1)
AND i.id NOT IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()>=oi.start_time AND NOW()<=oi.end_time AND oi.STATUS=1)
AND i.id NOT IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()>oi.end_time AND oi.STATUS=1)
AND i.id NOT IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()<oi.start_time AND oi.STATUS!=1)
AND i.id IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()>=oi.start_time AND NOW()<=oi.end_time AND oi.STATUS!=1)
AND i.id NOT IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()>oi.end_time AND oi.STATUS!=1);

#7-13有效可单独售卖的有库存且仓库属于7的非特卖商品---sku仅存在于无效已结束特卖中---结果未知
SELECT i.id,i.warehouse_type,s.warehouse_id,s.stock_quantity,s.item_size,i.sale_price FROM item AS i JOIN stock_item AS s
WHERE i.id=s.item_id AND i.status=1 AND i.is_spu=0 AND i.is_outlets=0 AND i.is_single_sale=1 AND s.status=1
AND i.warehouse_type=7 AND s.stock_quantity>100
AND i.id NOT IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()<oi.start_time AND oi.STATUS=1)
AND i.id NOT IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()>=oi.start_time AND NOW()<=oi.end_time AND oi.STATUS=1)
AND i.id NOT IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()>oi.end_time AND oi.STATUS=1)
AND i.id NOT IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()<oi.start_time AND oi.STATUS!=1)
AND i.id NOT IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()>=oi.start_time AND NOW()<=oi.end_time AND oi.STATUS!=1)
AND i.id IN(SELECT DISTINCT og.sku FROM oper_outlet_goods AS og JOIN oper_outlet_info AS oi
WHERE og.oid=oi.id AND NOW()>oi.end_time AND oi.STATUS!=1);

#7-14有效可单独售卖的有库存且仓库属于7的非特卖商品---sku未加入任何特卖中---下单成功
SELECT i.id,i.warehouse_type,s.warehouse_id,s.stock_quantity,s.item_size,i.sale_price FROM item AS i JOIN stock_item AS s
WHERE i.id=s.item_id AND i.status=1 AND i.is_spu=0 AND i.is_outlets=0 AND i.is_single_sale=1 AND s.status=1
AND i.warehouse_type=7 AND s.stock_quantity>100
AND i.id NOT IN(SELECT DISTINCT sku FROM oper_outlet_goods);