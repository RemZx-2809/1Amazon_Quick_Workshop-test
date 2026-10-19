// Embedded Sales Dataset (Exact 100 rows from sheet 'Sales')
    const RAW_SALES_DATA = [{"id": "S001", "date": "2026-08-01", "branch": "มหาวิทยาลัย", "product": "อเมริกาโน", "category": "กาแฟ", "qty": 14, "price": 60.0, "cost": 20.0}, {"id": "S002", "date": "2026-08-01", "branch": "สำนักงาน", "product": "ชาไทย", "category": "เครื่องดื่มอื่น", "qty": 6, "price": 55.0, "cost": 18.0}, {"id": "S003", "date": "2026-08-01", "branch": "ห้างสรรพสินค้า", "product": "บราวนี", "category": "เบเกอรี", "qty": 5, "price": 55.0, "cost": 22.0}, {"id": "S004", "date": "2026-08-01", "branch": "มหาวิทยาลัย", "product": "ลาเต้", "category": "กาแฟ", "qty": 7, "price": 75.0, "cost": 28.0}, {"id": "S005", "date": "2026-08-02", "branch": "สำนักงาน", "product": "โกโก้", "category": "เครื่องดื่มอื่น", "qty": 5, "price": 65.0, "cost": 25.0}, {"id": "S006", "date": "2026-08-02", "branch": "ห้างสรรพสินค้า", "product": "ชีสเค้ก", "category": "เบเกอรี", "qty": 4, "price": 110.0, "cost": 72.0}, {"id": "S007", "date": "2026-08-02", "branch": "มหาวิทยาลัย", "product": "คาปูชิโน", "category": "กาแฟ", "qty": 20, "price": 75.0, "cost": 27.0}, {"id": "S008", "date": "2026-08-03", "branch": "สำนักงาน", "product": "ครัวซองต์", "category": "เบเกอรี", "qty": 6, "price": 85.0, "cost": 60.0}, {"id": "S009", "date": "2026-08-03", "branch": "ห้างสรรพสินค้า", "product": "ลาเต้", "category": "กาแฟ", "qty": 9, "price": 75.0, "cost": 28.0}, {"id": "S010", "date": "2026-08-03", "branch": "มหาวิทยาลัย", "product": "โกโก้", "category": "เครื่องดื่มอื่น", "qty": 13, "price": 65.0, "cost": 25.0}, {"id": "S011", "date": "2026-08-04", "branch": "สำนักงาน", "product": "ชีสเค้ก", "category": "เบเกอรี", "qty": 13, "price": 110.0, "cost": 72.0}, {"id": "S012", "date": "2026-08-04", "branch": "ห้างสรรพสินค้า", "product": "คาปูชิโน", "category": "กาแฟ", "qty": 12, "price": 75.0, "cost": 27.0}, {"id": "S013", "date": "2026-08-04", "branch": "มหาวิทยาลัย", "product": "ครัวซองต์", "category": "เบเกอรี", "qty": 16, "price": 85.0, "cost": 60.0}, {"id": "S014", "date": "2026-08-05", "branch": "สำนักงาน", "product": "อเมริกาโน", "category": "กาแฟ", "qty": 8, "price": 60.0, "cost": 20.0}, {"id": "S015", "date": "2026-08-05", "branch": "ห้างสรรพสินค้า", "product": "ชาไทย", "category": "เครื่องดื่มอื่น", "qty": 9, "price": 55.0, "cost": 18.0}, {"id": "S016", "date": "2026-08-05", "branch": "มหาวิทยาลัย", "product": "บราวนี", "category": "เบเกอรี", "qty": 19, "price": 55.0, "cost": 22.0}, {"id": "S017", "date": "2026-08-05", "branch": "สำนักงาน", "product": "คาปูชิโน", "category": "กาแฟ", "qty": 5, "price": 75.0, "cost": 27.0}, {"id": "S018", "date": "2026-08-06", "branch": "ห้างสรรพสินค้า", "product": "ครัวซองต์", "category": "เบเกอรี", "qty": 2, "price": 85.0, "cost": 60.0}, {"id": "S019", "date": "2026-08-06", "branch": "มหาวิทยาลัย", "product": "อเมริกาโน", "category": "กาแฟ", "qty": 16, "price": 60.0, "cost": 20.0}, {"id": "S020", "date": "2026-08-06", "branch": "สำนักงาน", "product": "ชาไทย", "category": "เครื่องดื่มอื่น", "qty": 6, "price": 55.0, "cost": 18.0}, {"id": "S021", "date": "2026-08-07", "branch": "ห้างสรรพสินค้า", "product": "บราวนี", "category": "เบเกอรี", "qty": 9, "price": 55.0, "cost": 22.0}, {"id": "S022", "date": "2026-08-07", "branch": "มหาวิทยาลัย", "product": "ลาเต้", "category": "กาแฟ", "qty": 19, "price": 75.0, "cost": 28.0}, {"id": "S023", "date": "2026-08-07", "branch": "สำนักงาน", "product": "โกโก้", "category": "เครื่องดื่มอื่น", "qty": 9, "price": 65.0, "cost": 25.0}, {"id": "S024", "date": "2026-08-08", "branch": "ห้างสรรพสินค้า", "product": "ชีสเค้ก", "category": "เบเกอรี", "qty": 4, "price": 110.0, "cost": 72.0}, {"id": "S025", "date": "2026-08-08", "branch": "มหาวิทยาลัย", "product": "ชาไทย", "category": "เครื่องดื่มอื่น", "qty": 8, "price": 55.0, "cost": 18.0}, {"id": "S026", "date": "2026-08-08", "branch": "สำนักงาน", "product": "บราวนี", "category": "เบเกอรี", "qty": 14, "price": 55.0, "cost": 22.0}, {"id": "S027", "date": "2026-08-09", "branch": "ห้างสรรพสินค้า", "product": "ลาเต้", "category": "กาแฟ", "qty": 9, "price": 75.0, "cost": 28.0}, {"id": "S028", "date": "2026-08-09", "branch": "มหาวิทยาลัย", "product": "โกโก้", "category": "เครื่องดื่มอื่น", "qty": 11, "price": 65.0, "cost": 25.0}, {"id": "S029", "date": "2026-08-09", "branch": "สำนักงาน", "product": "ชีสเค้ก", "category": "เบเกอรี", "qty": 13, "price": 110.0, "cost": 72.0}, {"id": "S030", "date": "2026-08-09", "branch": "ห้างสรรพสินค้า", "product": "คาปูชิโน", "category": "กาแฟ", "qty": 6, "price": 75.0, "cost": 27.0}, {"id": "S031", "date": "2026-08-10", "branch": "มหาวิทยาลัย", "product": "ครัวซองต์", "category": "เบเกอรี", "qty": 12, "price": 85.0, "cost": 60.0}, {"id": "S032", "date": "2026-08-10", "branch": "สำนักงาน", "product": "อเมริกาโน", "category": "กาแฟ", "qty": 6, "price": 60.0, "cost": 20.0}, {"id": "S033", "date": "2026-08-10", "branch": "ห้างสรรพสินค้า", "product": "โกโก้", "category": "เครื่องดื่มอื่น", "qty": 11, "price": 65.0, "cost": 25.0}, {"id": "S034", "date": "2026-08-11", "branch": "มหาวิทยาลัย", "product": "ชีสเค้ก", "category": "เบเกอรี", "qty": 13, "price": 110.0, "cost": 72.0}, {"id": "S035", "date": "2026-08-11", "branch": "สำนักงาน", "product": "คาปูชิโน", "category": "กาแฟ", "qty": 3, "price": 75.0, "cost": 27.0}, {"id": "S036", "date": "2026-08-11", "branch": "ห้างสรรพสินค้า", "product": "ครัวซองต์", "category": "เบเกอรี", "qty": 12, "price": 85.0, "cost": 60.0}, {"id": "S037", "date": "2026-08-12", "branch": "มหาวิทยาลัย", "product": "อเมริกาโน", "category": "กาแฟ", "qty": 14, "price": 60.0, "cost": 20.0}, {"id": "S038", "date": "2026-08-12", "branch": "สำนักงาน", "product": "ชาไทย", "category": "เครื่องดื่มอื่น", "qty": 14, "price": 55.0, "cost": 18.0}, {"id": "S039", "date": "2026-08-12", "branch": "ห้างสรรพสินค้า", "product": "บราวนี", "category": "เบเกอรี", "qty": 3, "price": 55.0, "cost": 22.0}, {"id": "S040", "date": "2026-08-13", "branch": "มหาวิทยาลัย", "product": "ลาเต้", "category": "กาแฟ", "qty": 13, "price": 75.0, "cost": 28.0}, {"id": "S041", "date": "2026-08-13", "branch": "สำนักงาน", "product": "ครัวซองต์", "category": "เบเกอรี", "qty": 9, "price": 85.0, "cost": 60.0}, {"id": "S042", "date": "2026-08-13", "branch": "ห้างสรรพสินค้า", "product": "อเมริกาโน", "category": "กาแฟ", "qty": 10, "price": 60.0, "cost": 20.0}, {"id": "S043", "date": "2026-08-14", "branch": "มหาวิทยาลัย", "product": "ชาไทย", "category": "เครื่องดื่มอื่น", "qty": 14, "price": 55.0, "cost": 18.0}, {"id": "S044", "date": "2026-08-14", "branch": "สำนักงาน", "product": "บราวนี", "category": "เบเกอรี", "qty": 4, "price": 55.0, "cost": 22.0}, {"id": "S045", "date": "2026-08-14", "branch": "ห้างสรรพสินค้า", "product": "ลาเต้", "category": "กาแฟ", "qty": 3, "price": 75.0, "cost": 28.0}, {"id": "S046", "date": "2026-08-14", "branch": "มหาวิทยาลัย", "product": "โกโก้", "category": "เครื่องดื่มอื่น", "qty": 11, "price": 65.0, "cost": 25.0}, {"id": "S047", "date": "2026-08-15", "branch": "สำนักงาน", "product": "ชีสเค้ก", "category": "เบเกอรี", "qty": 3, "price": 110.0, "cost": 72.0}, {"id": "S048", "date": "2026-08-15", "branch": "ห้างสรรพสินค้า", "product": "คาปูชิโน", "category": "กาแฟ", "qty": 4, "price": 75.0, "cost": 27.0}, {"id": "S049", "date": "2026-08-15", "branch": "มหาวิทยาลัย", "product": "บราวนี", "category": "เบเกอรี", "qty": 12, "price": 55.0, "cost": 22.0}, {"id": "S050", "date": "2026-08-16", "branch": "สำนักงาน", "product": "ลาเต้", "category": "กาแฟ", "qty": 12, "price": 75.0, "cost": 28.0}, {"id": "S051", "date": "2026-08-16", "branch": "ห้างสรรพสินค้า", "product": "โกโก้", "category": "เครื่องดื่มอื่น", "qty": 11, "price": 65.0, "cost": 25.0}, {"id": "S052", "date": "2026-08-16", "branch": "มหาวิทยาลัย", "product": "ชีสเค้ก", "category": "เบเกอรี", "qty": 15, "price": 110.0, "cost": 72.0}, {"id": "S053", "date": "2026-08-17", "branch": "สำนักงาน", "product": "คาปูชิโน", "category": "กาแฟ", "qty": 11, "price": 75.0, "cost": 27.0}, {"id": "S054", "date": "2026-08-17", "branch": "ห้างสรรพสินค้า", "product": "ครัวซองต์", "category": "เบเกอรี", "qty": 2, "price": 85.0, "cost": 60.0}, {"id": "S055", "date": "2026-08-17", "branch": "มหาวิทยาลัย", "product": "อเมริกาโน", "category": "กาแฟ", "qty": 20, "price": 60.0, "cost": 20.0}, {"id": "S056", "date": "2026-08-18", "branch": "สำนักงาน", "product": "ชาไทย", "category": "เครื่องดื่มอื่น", "qty": 14, "price": 55.0, "cost": 18.0}, {"id": "S057", "date": "2026-08-18", "branch": "ห้างสรรพสินค้า", "product": "ชีสเค้ก", "category": "เบเกอรี", "qty": 9, "price": 110.0, "cost": 72.0}, {"id": "S058", "date": "2026-08-18", "branch": "มหาวิทยาลัย", "product": "คาปูชิโน", "category": "กาแฟ", "qty": 19, "price": 75.0, "cost": 27.0}, {"id": "S059", "date": "2026-08-18", "branch": "สำนักงาน", "product": "ครัวซองต์", "category": "เบเกอรี", "qty": 3, "price": 85.0, "cost": 60.0}, {"id": "S060", "date": "2026-08-19", "branch": "ห้างสรรพสินค้า", "product": "อเมริกาโน", "category": "กาแฟ", "qty": 12, "price": 60.0, "cost": 20.0}, {"id": "S061", "date": "2026-08-19", "branch": "มหาวิทยาลัย", "product": "ชาไทย", "category": "เครื่องดื่มอื่น", "qty": 10, "price": 55.0, "cost": 18.0}, {"id": "S062", "date": "2026-08-19", "branch": "สำนักงาน", "product": "บราวนี", "category": "เบเกอรี", "qty": 4, "price": 55.0, "cost": 22.0}, {"id": "S063", "date": "2026-08-20", "branch": "ห้างสรรพสินค้า", "product": "ลาเต้", "category": "กาแฟ", "qty": 15, "price": 75.0, "cost": 28.0}, {"id": "S064", "date": "2026-08-20", "branch": "มหาวิทยาลัย", "product": "โกโก้", "category": "เครื่องดื่มอื่น", "qty": 19, "price": 65.0, "cost": 25.0}, {"id": "S065", "date": "2026-08-20", "branch": "สำนักงาน", "product": "อเมริกาโน", "category": "กาแฟ", "qty": 5, "price": 60.0, "cost": 20.0}, {"id": "S066", "date": "2026-08-21", "branch": "ห้างสรรพสินค้า", "product": "ชาไทย", "category": "เครื่องดื่มอื่น", "qty": 2, "price": 55.0, "cost": 18.0}, {"id": "S067", "date": "2026-08-21", "branch": "มหาวิทยาลัย", "product": "บราวนี", "category": "เบเกอรี", "qty": 20, "price": 55.0, "cost": 22.0}, {"id": "S068", "date": "2026-08-21", "branch": "สำนักงาน", "product": "ลาเต้", "category": "กาแฟ", "qty": 14, "price": 75.0, "cost": 28.0}, {"id": "S069", "date": "2026-08-22", "branch": "ห้างสรรพสินค้า", "product": "โกโก้", "category": "เครื่องดื่มอื่น", "qty": 5, "price": 65.0, "cost": 25.0}, {"id": "S070", "date": "2026-08-22", "branch": "มหาวิทยาลัย", "product": "ชีสเค้ก", "category": "เบเกอรี", "qty": 13, "price": 110.0, "cost": 72.0}, {"id": "S071", "date": "2026-08-22", "branch": "สำนักงาน", "product": "คาปูชิโน", "category": "กาแฟ", "qty": 7, "price": 75.0, "cost": 27.0}, {"id": "S072", "date": "2026-08-23", "branch": "ห้างสรรพสินค้า", "product": "ครัวซองต์", "category": "เบเกอรี", "qty": 8, "price": 85.0, "cost": 60.0}, {"id": "S073", "date": "2026-08-23", "branch": "มหาวิทยาลัย", "product": "ลาเต้", "category": "กาแฟ", "qty": 10, "price": 75.0, "cost": 28.0}, {"id": "S074", "date": "2026-08-23", "branch": "สำนักงาน", "product": "โกโก้", "category": "เครื่องดื่มอื่น", "qty": 2, "price": 65.0, "cost": 25.0}, {"id": "S075", "date": "2026-08-23", "branch": "ห้างสรรพสินค้า", "product": "ชีสเค้ก", "category": "เบเกอรี", "qty": 9, "price": 110.0, "cost": 72.0}, {"id": "S076", "date": "2026-08-24", "branch": "มหาวิทยาลัย", "product": "คาปูชิโน", "category": "กาแฟ", "qty": 19, "price": 75.0, "cost": 27.0}, {"id": "S077", "date": "2026-08-24", "branch": "สำนักงาน", "product": "ครัวซองต์", "category": "เบเกอรี", "qty": 9, "price": 85.0, "cost": 60.0}, {"id": "S078", "date": "2026-08-24", "branch": "ห้างสรรพสินค้า", "product": "อเมริกาโน", "category": "กาแฟ", "qty": 12, "price": 60.0, "cost": 20.0}, {"id": "S079", "date": "2026-08-25", "branch": "มหาวิทยาลัย", "product": "ชาไทย", "category": "เครื่องดื่มอื่น", "qty": 8, "price": 55.0, "cost": 18.0}, {"id": "S080", "date": "2026-08-25", "branch": "สำนักงาน", "product": "บราวนี", "category": "เบเกอรี", "qty": 10, "price": 55.0, "cost": 22.0}, {"id": "S081", "date": "2026-08-25", "branch": "ห้างสรรพสินค้า", "product": "คาปูชิโน", "category": "กาแฟ", "qty": 7, "price": 75.0, "cost": 27.0}, {"id": "S082", "date": "2026-08-26", "branch": "มหาวิทยาลัย", "product": "ครัวซองต์", "category": "เบเกอรี", "qty": 9, "price": 85.0, "cost": 60.0}, {"id": "S083", "date": "2026-08-26", "branch": "สำนักงาน", "product": "อเมริกาโน", "category": "กาแฟ", "qty": 15, "price": 60.0, "cost": 20.0}, {"id": "S084", "date": "2026-08-26", "branch": "ห้างสรรพสินค้า", "product": "ชาไทย", "category": "เครื่องดื่มอื่น", "qty": 10, "price": 55.0, "cost": 18.0}, {"id": "S085", "date": "2026-08-27", "branch": "มหาวิทยาลัย", "product": "บราวนี", "category": "เบเกอรี", "qty": 8, "price": 55.0, "cost": 22.0}, {"id": "S086", "date": "2026-08-27", "branch": "สำนักงาน", "product": "ลาเต้", "category": "กาแฟ", "qty": 10, "price": 75.0, "cost": 28.0}, {"id": "S087", "date": "2026-08-27", "branch": "ห้างสรรพสินค้า", "product": "โกโก้", "category": "เครื่องดื่มอื่น", "qty": 11, "price": 65.0, "cost": 25.0}, {"id": "S088", "date": "2026-08-27", "branch": "มหาวิทยาลัย", "product": "ชีสเค้ก", "category": "เบเกอรี", "qty": 7, "price": 110.0, "cost": 72.0}, {"id": "S089", "date": "2026-08-28", "branch": "สำนักงาน", "product": "ชาไทย", "category": "เครื่องดื่มอื่น", "qty": 11, "price": 55.0, "cost": 18.0}, {"id": "S090", "date": "2026-08-28", "branch": "ห้างสรรพสินค้า", "product": "บราวนี", "category": "เบเกอรี", "qty": 2, "price": 55.0, "cost": 22.0}, {"id": "S091", "date": "2026-08-28", "branch": "มหาวิทยาลัย", "product": "ลาเต้", "category": "กาแฟ", "qty": 14, "price": 75.0, "cost": 28.0}, {"id": "S092", "date": "2026-08-29", "branch": "สำนักงาน", "product": "โกโก้", "category": "เครื่องดื่มอื่น", "qty": 10, "price": 65.0, "cost": 25.0}, {"id": "S093", "date": "2026-08-29", "branch": "ห้างสรรพสินค้า", "product": "ชีสเค้ก", "category": "เบเกอรี", "qty": 5, "price": 110.0, "cost": 72.0}, {"id": "S094", "date": "2026-08-29", "branch": "มหาวิทยาลัย", "product": "คาปูชิโน", "category": "กาแฟ", "qty": 7, "price": 75.0, "cost": 27.0}, {"id": "S095", "date": "2026-08-30", "branch": "สำนักงาน", "product": "ครัวซองต์", "category": "เบเกอรี", "qty": 15, "price": 85.0, "cost": 60.0}, {"id": "S096", "date": "2026-08-30", "branch": "ห้างสรรพสินค้า", "product": "อเมริกาโน", "category": "กาแฟ", "qty": 8, "price": 60.0, "cost": 20.0}, {"id": "S097", "date": "2026-08-30", "branch": "มหาวิทยาลัย", "product": "โกโก้", "category": "เครื่องดื่มอื่น", "qty": 20, "price": 65.0, "cost": 25.0}, {"id": "S098", "date": "2026-08-31", "branch": "สำนักงาน", "product": "ชีสเค้ก", "category": "เบเกอรี", "qty": 14, "price": 110.0, "cost": 72.0}, {"id": "S099", "date": "2026-08-31", "branch": "ห้างสรรพสินค้า", "product": "คาปูชิโน", "category": "กาแฟ", "qty": 5, "price": 75.0, "cost": 27.0}, {"id": "S100", "date": "2026-08-31", "branch": "มหาวิทยาลัย", "product": "ครัวซองต์", "category": "เบเกอรี", "qty": 15, "price": 85.0, "cost": 60.0}];

    // Pre-calculate derived columns for each record
    const THAI_DAYS = ['วันอาทิตย์', 'วันจันทร์', 'วันอังคาร', 'วันพุธ', 'วันพฤหัสบดี', 'วันศุกร์', 'วันเสาร์'];
    const DOW_ORDER = ['วันจันทร์', 'วันอังคาร', 'วันพุธ', 'วันพฤหัสบดี', 'วันศุกร์', 'วันเสาร์', 'วันอาทิตย์'];

    const STORAGE_KEY_DATA = 'amazon_workshop_sales_data_v2';
    const STORAGE_KEY_BATCHES = 'amazon_workshop_batches_v2';

    let SALES_DATA = [];
    let BATCH_METADATA = [];
    let ALL_BRANCHES = [];
    let ALL_CATEGORIES = [];
    let ALL_PRODUCTS = [];

    function createRecordFromRaw(row, idx) {
      const d = new Date(row.date + 'T00:00:00');
      const dayOfWeek = THAI_DAYS[d.getDay()];
      const qty = Number(row.qty);
      const price = Number(row.price);
      const cost = Number(row.cost);
      const revenue = qty * price;
      const profit = qty * (price - cost);
      const margin = revenue > 0 ? (profit / revenue) : 0;
      const year = row.date.slice(0, 4);
      return {
        id: row.id || `S${String(idx + 1).padStart(3, '0')}`,
        date: row.date,
        dayOfWeek: dayOfWeek,
        dayIndex: d.getDay(),
        branch: row.branch,
        product: row.product,
        category: row.category,
        qty: qty,
        price: price,
        cost: cost,
        revenue: revenue,
        gross_profit: profit,
        margin: margin,
        batchId: row.batchId || 'batch_seed_001',
        year: year
      };
    }

    function createDefaultBatch(records) {
      const dates = records.map(r => r.date).sort();
      const totalRev = records.reduce((sum, r) => sum + r.revenue, 0);
      return {
        id: 'batch_seed_001',
        name: 'ชุดข้อมูลตั้งต้น (ชีต Sales ส.ค. 2569)',
        uploadedAt: '2026-08-31 23:59:00',
        fileName: 'ชีต Sales (Excel ต้นฉบับ)',
        recordCount: records.length,
        totalRevenue: totalRev,
        minDate: dates[0] || '2026-08-01',
        maxDate: dates[dates.length - 1] || '2026-08-31',
        years: Array.from(new Set(records.map(r => r.year)))
      };
    }

    function initDataset() {
      let storedData = null;
      let storedBatches = null;
      try {
        const d = localStorage.getItem(STORAGE_KEY_DATA);
        const b = localStorage.getItem(STORAGE_KEY_BATCHES);
        if (d) storedData = JSON.parse(d);
        if (b) storedBatches = JSON.parse(b);
      } catch (e) {
        console.warn('LocalStorage error:', e);
      }

      if (storedData && Array.isArray(storedData) && storedData.length > 0) {
        SALES_DATA = storedData;
        BATCH_METADATA = (storedBatches && Array.isArray(storedBatches)) ? storedBatches : [createDefaultBatch(SALES_DATA)];
      } else {
        SALES_DATA = RAW_SALES_DATA.map(createRecordFromRaw);
        BATCH_METADATA = [createDefaultBatch(SALES_DATA)];
        saveDatasetToStorage();
      }
      recomputeDimensions(false);
    }

    function saveDatasetToStorage() {
      try {
        localStorage.setItem(STORAGE_KEY_DATA, JSON.stringify(SALES_DATA));
        localStorage.setItem(STORAGE_KEY_BATCHES, JSON.stringify(BATCH_METADATA));
      } catch (e) {
        console.error('LocalStorage save error:', e);
      }
    }

    function recomputeDimensions(preserveFilters = true) {
      ALL_BRANCHES = Array.from(new Set(SALES_DATA.map(x => x.branch))).sort();
      ALL_CATEGORIES = Array.from(new Set(SALES_DATA.map(x => x.category))).sort();
      ALL_PRODUCTS = Array.from(new Set(SALES_DATA.map(x => x.product))).sort();

      const dates = SALES_DATA.map(x => x.date).sort();
      const minDate = dates[0] || '2026-08-01';
      const maxDate = dates[dates.length - 1] || '2026-08-31';

      const startInp = document.getElementById('filterStartDate');
      const endInp = document.getElementById('filterEndDate');
      if (startInp && endInp) {
        startInp.min = minDate;
        startInp.max = maxDate;
        endInp.min = minDate;
        endInp.max = maxDate;
        if (!preserveFilters || !state.filters.startDate || state.filters.startDate < minDate) {
          startInp.value = minDate;
          state.filters.startDate = minDate;
        }
        if (!preserveFilters || !state.filters.endDate || state.filters.endDate > maxDate) {
          endInp.value = maxDate;
          state.filters.endDate = maxDate;
        }
      } else {
        state.filters.startDate = minDate;
        state.filters.endDate = maxDate;
      }

      if (preserveFilters) {
        state.filters.branches = new Set(ALL_BRANCHES.filter(b => state.filters.branches.has(b)));
        if (state.filters.branches.size === 0) state.filters.branches = new Set(ALL_BRANCHES);

        state.filters.categories = new Set(ALL_CATEGORIES.filter(c => state.filters.categories.has(c)));
        if (state.filters.categories.size === 0) state.filters.categories = new Set(ALL_CATEGORIES);

        state.filters.products = new Set(ALL_PRODUCTS.filter(p => state.filters.products.has(p)));
        if (state.filters.products.size === 0) state.filters.products = new Set(ALL_PRODUCTS);
      } else {
        state.filters.branches = new Set(ALL_BRANCHES);
        state.filters.categories = new Set(ALL_CATEGORIES);
        state.filters.products = new Set(ALL_PRODUCTS);
      }
      state.filters.dows = new Set(DOW_ORDER);

      // Re-render pills if container exists
      const bContainer = document.getElementById('branchFilterPills');
      if (bContainer) initFilterPills();
    }

    // State Management
    const state = {
      filters: {
        branches: new Set(),
        categories: new Set(),
        products: new Set(),
        dows: new Set(DOW_ORDER),
        startDate: '2026-08-01',
        endDate: '2026-08-31'
      },
      globalMetric: 'revenue', // 'revenue' | 'gross_profit' | 'qty'
      topRankLimit: 3,
      selectedBranchDrilldown: null, // null = all
      currentTab: 'tabOverview',
      txTable: {
        search: '',
        sortCol: 'id',
        sortAsc: true,
        page: 1,
        pageSize: 25
      },
      branchTable: {
        sortCol: 'revenue',
        sortAsc: false
      },
      productTable: {
        sortCol: 'revenue',
        sortAsc: false
      },
      simulation: {
        priceDeltaPct: 0,
        costDeltaPct: 0
      }
    };

    // Formatters
    function formatCurrency(val) {
      return '฿' + Number(val).toLocaleString('th-TH', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
    }
    function formatInteger(val) {
      return Number(val).toLocaleString('th-TH');
    }
    function formatPercent(val) {
      return (Number(val) * 100).toFixed(2) + '%';
    }

    // Filter Logic
    function getFilteredData() {
      return SALES_DATA.filter(row => {
        if (!state.filters.branches.has(row.branch)) return false;
        if (!state.filters.categories.has(row.category)) return false;
        if (!state.filters.products.has(row.product)) return false;
        if (!state.filters.dows.has(row.dayOfWeek)) return false;
        if (state.filters.startDate && row.date < state.filters.startDate) return false;
        if (state.filters.endDate && row.date > state.filters.endDate) return false;
        return true;
      });
    }

    const DOW_SHORT = {
      'วันจันทร์': 'จ.',
      'วันอังคาร': 'อ.',
      'วันพุธ': 'พ.',
      'วันพฤหัสบดี': 'พฤ.',
      'วันศุกร์': 'ศ.',
      'วันเสาร์': 'ส.',
      'วันอาทิตย์': 'อา.'
    };

    // Toggle filter panel body collapse/expand with smooth animation
    function toggleFilterPanel(forceCollapse) {
      const section = document.getElementById('filterSection');
      const wrapper = document.getElementById('filterCollapsibleWrapper');
      const panel = document.getElementById('filterPanelBody');
      const btn = document.getElementById('btnToggleFilters');
      const header = document.getElementById('filterHeader');
      if (!wrapper) return;

      if (panel && panel.style.display) {
        panel.style.display = '';
      }

      const isCurrentlyCollapsed = wrapper.classList.contains('collapsed');
      const shouldCollapse = (typeof forceCollapse === 'boolean') ? forceCollapse : !isCurrentlyCollapsed;

      if (shouldCollapse) {
        wrapper.classList.add('collapsed');
        if (section) section.classList.add('is-collapsed');
        if (header) header.setAttribute('aria-expanded', 'false');
        if (btn) {
          btn.classList.remove('btn-outline');
          btn.classList.add('btn-orange');
          btn.title = 'คลิกเพื่อแสดงตัวกรอง';
          const txt = btn.querySelector('.toggle-text');
          if (txt) {
            txt.textContent = 'แสดงตัวกรอง (ขยาย)';
          } else {
            btn.innerHTML = '<span class="toggle-icon">▲</span> <span class="toggle-text">แสดงตัวกรอง (ขยาย)</span>';
          }
        }
      } else {
        wrapper.classList.remove('collapsed');
        if (section) section.classList.remove('is-collapsed');
        if (header) header.setAttribute('aria-expanded', 'true');
        if (btn) {
          btn.classList.remove('btn-orange');
          btn.classList.add('btn-outline');
          btn.title = 'กดเก็บหรือเปิดเลื่อนตัวกรอง';
          const txt = btn.querySelector('.toggle-text');
          if (txt) {
            txt.textContent = 'ซ่อนตัวกรอง (กดเก็บ)';
          } else {
            btn.innerHTML = '<span class="toggle-icon">▲</span> <span class="toggle-text">ซ่อนตัวกรอง (กดเก็บ)</span>';
          }
        }
      }
    }
    window.toggleFilterPanel = toggleFilterPanel;

    function handleFilterHeaderClick(event) {
      if (event && event.target && event.target.closest('button, input, select, label, a')) {
        return;
      }
      toggleFilterPanel();
    }
    window.handleFilterHeaderClick = handleFilterHeaderClick;

    // Initial Filter Pills Rendering
    function initFilterPills() {
      // Branches
      const branchContainer = document.getElementById('branchFilterPills');
      branchContainer.innerHTML = ALL_BRANCHES.map(b => `
        <label class="pill-checkbox active" id="pill_branch_${b}">
          <input type="checkbox" checked onchange="toggleFilter('branch', '${b}', this.checked)">
          <span>${b}</span>
        </label>
      `).join('');

      // Categories
      const catContainer = document.getElementById('categoryFilterPills');
      catContainer.innerHTML = ALL_CATEGORIES.map(c => `
        <label class="pill-checkbox active" id="pill_category_${c}">
          <input type="checkbox" checked onchange="toggleFilter('category', '${c}', this.checked)">
          <span>${c}</span>
        </label>
      `).join('');

      // Day of Week - 1 single line with concise short day names
      const dowContainer = document.getElementById('dowFilterPills');
      dowContainer.innerHTML = DOW_ORDER.map(d => `
        <label class="pill-checkbox active" id="pill_dow_${d}" title="${d}">
          <input type="checkbox" checked onchange="toggleFilter('dow', '${d}', this.checked)">
          <span>${DOW_SHORT[d] || d.replace('วัน', '')}</span>
        </label>
      `).join('');

      // Products
      const prodContainer = document.getElementById('productFilterPills');
      prodContainer.innerHTML = ALL_PRODUCTS.map(p => `
        <label class="pill-checkbox active" id="pill_product_${p}">
          <input type="checkbox" checked onchange="toggleFilter('product', '${p}', this.checked)">
          <span>${p}</span>
        </label>
      `).join('');

      // Date inputs
      document.getElementById('filterStartDate').addEventListener('change', (e) => {
        state.filters.startDate = e.target.value;
        onFilterChange();
      });
      document.getElementById('filterEndDate').addEventListener('change', (e) => {
        state.filters.endDate = e.target.value;
        onFilterChange();
      });

      // Reset filters button
      document.getElementById('btnResetFilters').addEventListener('click', resetAllFilters);
    }

    function toggleFilter(type, value, isChecked) {
      let setRef;
      if (type === 'branch') setRef = state.filters.branches;
      else if (type === 'category') setRef = state.filters.categories;
      else if (type === 'product') setRef = state.filters.products;
      else if (type === 'dow') setRef = state.filters.dows;

      if (isChecked) {
        setRef.add(value);
      } else {
        setRef.delete(value);
      }

      const pill = document.getElementById(`pill_${type}_${value}`);
      if (pill) {
        if (isChecked) pill.classList.add('active');
        else pill.classList.remove('active');
      }

      onFilterChange();
    }

    function quickSelectFilter(type, selectAll) {
      let allItems = [];
      let setRef;
      if (type === 'branch') { allItems = ALL_BRANCHES; setRef = state.filters.branches; }
      else if (type === 'category') { allItems = ALL_CATEGORIES; setRef = state.filters.categories; }
      else if (type === 'product') { allItems = ALL_PRODUCTS; setRef = state.filters.products; }

      setRef.clear();
      allItems.forEach(item => {
        if (selectAll) setRef.add(item);
        const pill = document.getElementById(`pill_${type}_${item}`);
        if (pill) {
          const cb = pill.querySelector('input');
          if (cb) cb.checked = selectAll;
          if (selectAll) pill.classList.add('active');
          else pill.classList.remove('active');
        }
      });
      onFilterChange();
    }

    function setDowPreset(preset) {
      state.filters.dows.clear();
      DOW_ORDER.forEach(d => {
        let shouldSelect = false;
        if (preset === 'all') shouldSelect = true;
        else if (preset === 'weekday' && ['วันจันทร์', 'วันอังคาร', 'วันพุธ', 'วันพฤหัสบดี', 'วันศุกร์'].includes(d)) shouldSelect = true;
        else if (preset === 'weekend' && ['วันเสาร์', 'วันอาทิตย์'].includes(d)) shouldSelect = true;

        if (shouldSelect) state.filters.dows.add(d);
        const pill = document.getElementById(`pill_dow_${d}`);
        if (pill) {
          const cb = pill.querySelector('input');
          if (cb) cb.checked = shouldSelect;
          if (shouldSelect) pill.classList.add('active');
          else pill.classList.remove('active');
        }
      });
      onFilterChange();
    }

    function setDatePreset(preset) {
      const startInp = document.getElementById('filterStartDate');
      const endInp = document.getElementById('filterEndDate');
      if (preset === 'all') {
        startInp.value = '2026-08-01';
        endInp.value = '2026-08-31';
      } else if (preset === 'w1') {
        startInp.value = '2026-08-01';
        endInp.value = '2026-08-07';
      } else if (preset === 'w2') {
        startInp.value = '2026-08-08';
        endInp.value = '2026-08-14';
      } else if (preset === 'w3') {
        startInp.value = '2026-08-15';
        endInp.value = '2026-08-21';
      } else if (preset === 'w4') {
        startInp.value = '2026-08-22';
        endInp.value = '2026-08-31';
      }
      state.filters.startDate = startInp.value;
      state.filters.endDate = endInp.value;
      onFilterChange();
    }

    function resetAllFilters() {
      state.filters.branches = new Set(ALL_BRANCHES);
      state.filters.categories = new Set(ALL_CATEGORIES);
      state.filters.products = new Set(ALL_PRODUCTS);
      state.filters.dows = new Set(DOW_ORDER);
      state.filters.startDate = '2026-08-01';
      state.filters.endDate = '2026-08-31';
      state.selectedBranchDrilldown = null;

      document.querySelectorAll('.pill-checkbox').forEach(p => {
        p.classList.add('active');
        const cb = p.querySelector('input');
        if (cb) cb.checked = true;
      });
      document.getElementById('filterStartDate').value = '2026-08-01';
      document.getElementById('filterEndDate').value = '2026-08-31';

      onFilterChange();
    }

    function updateActiveFilterTags(filtered) {
      const tagsContainer = document.getElementById('activeFilterTags');
      const bar = document.getElementById('activeFiltersBar');
      const tags = [];

      if (state.filters.branches.size < ALL_BRANCHES.length) {
        tags.push(`สาขา: ${Array.from(state.filters.branches).join(', ') || 'ไม่มี'}`);
      }
      if (state.filters.categories.size < ALL_CATEGORIES.length) {
        tags.push(`หมวด: ${Array.from(state.filters.categories).join(', ') || 'ไม่มี'}`);
      }
      if (state.filters.products.size < ALL_PRODUCTS.length) {
        tags.push(`สินค้า: ${state.filters.products.size} รายการ`);
      }
      if (state.filters.dows.size < DOW_ORDER.length) {
        tags.push(`วัน: ${Array.from(state.filters.dows).map(d => DOW_SHORT[d] || d.replace('วัน','')).join(', ') || 'ไม่มี'}`);
      }
      if (state.filters.startDate !== '2026-08-01' || state.filters.endDate !== '2026-08-31') {
        tags.push(`วันที่: ${state.filters.startDate} ถึง ${state.filters.endDate}`);
      }

      if (tags.length > 0) {
        bar.style.display = 'flex';
        tagsContainer.innerHTML = tags.map(t => `
          <span class="active-filter-tag">${t}</span>
        `).join('');
      } else {
        bar.style.display = 'none';
      }

      const badge = document.getElementById('filterRowCountBadge');
      if (badge) {
        const pct = ((filtered.length / SALES_DATA.length) * 100).toFixed(1);
        badge.textContent = `${filtered.length}/${SALES_DATA.length} (${pct}%)`;
      }

      const summaryChip = document.getElementById('filterSummaryBar');
      if (summaryChip) {
        const bText = state.filters.branches.size === ALL_BRANCHES.length ? 'ทุกสาขา' : `${state.filters.branches.size} สาขา`;
        const cText = state.filters.categories.size === ALL_CATEGORIES.length ? 'ทุกหมวด' : `${state.filters.categories.size} หมวด`;
        const dText = state.filters.dows.size === DOW_ORDER.length ? 'ทุกวัน' : `${state.filters.dows.size} วัน`;
        const pText = state.filters.products.size === ALL_PRODUCTS.length ? '8 สินค้า' : `${state.filters.products.size} สินค้า`;
        const dateText = (state.filters.startDate === '2026-08-01' && state.filters.endDate === '2026-08-31') ? 'ส.ค. 69' : `${state.filters.startDate.slice(5)} - ${state.filters.endDate.slice(5)}`;
        summaryChip.textContent = `${bText} • ${cText} • ${dText} • ${pText} • ${dateText}`;
      }
    }

    function onFilterChange() {
      const filtered = getFilteredData();
      updateActiveFilterTags(filtered);
      renderAllViews(filtered);
    }

    function setGlobalMetric(metric) {
      state.globalMetric = metric;
      document.querySelectorAll('.metric-btn').forEach(btn => {
        if (btn.dataset.metric === metric) btn.classList.add('active');
        else btn.classList.remove('active');
      });
      const filtered = getFilteredData();
      renderAllViews(filtered);
    }

    function setTopRankLimit(limit) {
      state.topRankLimit = limit;
      document.querySelectorAll('.top-rank-btn').forEach(btn => {
        if (Number(btn.dataset.top) === limit) btn.classList.add('active');
        else btn.classList.remove('active');
      });
      const filtered = getFilteredData();
      renderTopProductsChart(filtered);
    }

    function switchTab(tabId) {
      if (state.currentTab !== tabId && state.currentTab !== 'tabDataManager') {
        state.previousTab = state.currentTab;
      }
      state.currentTab = tabId;
      document.querySelectorAll('.tab-btn').forEach(btn => {
        if (btn.dataset.tab === tabId) btn.classList.add('active');
        else btn.classList.remove('active');
      });
      document.querySelectorAll('.tab-content').forEach(panel => {
        if (panel.id === tabId) panel.classList.add('active');
        else panel.classList.remove('active');
      });

      // Synchronize header button appearance
      const btnHeader = document.getElementById('btnOpenDataManager');
      if (btnHeader) {
        if (tabId === 'tabDataManager') {
          btnHeader.innerHTML = '⬅️ กลับหน้าแดชบอร์ด';
          btnHeader.classList.remove('btn-primary');
          btnHeader.classList.add('btn-orange');
          btnHeader.title = 'คลิกเพื่อย้อนกลับไปยังหน้าแดชบอร์ด';
          btnHeader.setAttribute('onclick', 'goBackFromDataManager()');
        } else {
          btnHeader.innerHTML = '📁 นำเข้า/จัดการข้อมูล';
          btnHeader.classList.remove('btn-orange');
          btnHeader.classList.add('btn-primary');
          btnHeader.title = 'นำเข้าข้อมูลใหม่ หรือจัดการตัดลบข้อมูลเก่า';
          btnHeader.setAttribute('onclick', "switchTab('tabDataManager')");
        }
      }

      // Render chart for newly active tab
      const filtered = getFilteredData();
      if (tabId === 'tabBranches') renderBranchTab(filtered);
      else if (tabId === 'tabProducts') renderProductTab(filtered);
      else if (tabId === 'tabTrends') renderTrendsTab(filtered);
      else if (tabId === 'tabTransactions') renderTxTable(filtered);
      else if (tabId === 'tabDataManager') renderDataManagerTab();
    }

    function goBackFromDataManager() {
      const target = state.previousTab || 'tabOverview';
      switchTab(target);
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }
    window.goBackFromDataManager = goBackFromDataManager;

    // ==========================================
    // RENDER ALL VIEWS
    // ==========================================
    function renderAllViews(data) {
      renderKpis(data);
      renderTopProductsChart(data);
      renderOverviewBranchTable(data);
      renderSmartInsights(data);
      renderReconciliationTable(data);
      updateSimulation();

      // Refresh tab specific views
      if (state.currentTab === 'tabBranches') renderBranchTab(data);
      else if (state.currentTab === 'tabProducts') renderProductTab(data);
      else if (state.currentTab === 'tabTrends') renderTrendsTab(data);
      else if (state.currentTab === 'tabTransactions') renderTxTable(data);
      else if (state.currentTab === 'tabDataManager') renderDataManagerTab();
    }

    // --- 1. KPI CARDS ---
    
    function getNiceMax(val) {
      if (val <= 0) return 100;
      const target = val * 1.15;
      const rough = target / 5;
      const mag = Math.pow(10, Math.floor(Math.log10(rough)));
      const factor = rough / mag;
      let step;
      if (factor <= 1.2) step = 1 * mag;
      else if (factor <= 2.2) step = 2 * mag;
      else if (factor <= 3) step = 2.5 * mag;
      else if (factor <= 7) step = 5 * mag;
      else step = 10 * mag;
      return Math.ceil(target / step) * step;
    }

    function renderKpis(data) {
      const totalRev = data.reduce((acc, x) => acc + x.revenue, 0);
      const totalQty = data.reduce((acc, x) => acc + x.qty, 0);
      const totalProfit = data.reduce((acc, x) => acc + x.gross_profit, 0);
      const margin = totalRev > 0 ? (totalProfit / totalRev) : 0;
      const txCount = data.length;
      const avgTx = txCount > 0 ? (totalRev / txCount) : 0;
      const avgPrice = totalQty > 0 ? (totalRev / totalQty) : 0;

      document.getElementById('kpiTotalRevenue').textContent = formatCurrency(totalRev);
      document.getElementById('kpiTotalQty').textContent = formatInteger(totalQty) + ' ชิ้น';
      document.getElementById('kpiTotalProfit').textContent = formatCurrency(totalProfit);
      document.getElementById('kpiGrossMarginBadge').textContent = formatPercent(margin);
      document.getElementById('kpiTxCount').textContent = formatInteger(txCount) + ' รายการ';
      document.getElementById('kpiAvgTx').textContent = formatCurrency(avgTx);
      document.getElementById('kpiAvgPrice').textContent = formatCurrency(avgPrice);
    }

    // --- 2. TOP PRODUCTS CHART (SVG HORIZONTAL BAR) ---
    function renderTopProductsChart(data) {
      const container = document.getElementById('topProductsChartContainer');
      const metric = state.globalMetric;

      // Group by product across all branches
      const prodMap = {};
      data.forEach(x => {
        if (!prodMap[x.product]) {
          prodMap[x.product] = { product: x.product, category: x.category, revenue: 0, gross_profit: 0, qty: 0 };
        }
        prodMap[x.product].revenue += x.revenue;
        prodMap[x.product].gross_profit += x.gross_profit;
        prodMap[x.product].qty += x.qty;
      });

      let sorted = Object.values(prodMap).sort((a, b) => b[metric] - a[metric]);
      const topItems = sorted.slice(0, state.topRankLimit);

      if (topItems.length === 0) {
        container.innerHTML = '<div style="padding: 40px; text-align: center; color: var(--text-muted);">ไม่มีข้อมูลสำหรับตัวกรองที่เลือก</div>';
        return;
      }

      const maxVal = Math.max(...topItems.map(x => x[metric]), 1);
      const rowHeight = 44;
      const margin = { top: 20, right: 105, bottom: 25, left: 125 };
      const width = 580;
      const height = margin.top + (topItems.length * rowHeight) + margin.bottom;

      let metricLabel = 'รายได้ (฿)';
      if (metric === 'gross_profit') metricLabel = 'กำไรขั้นต้น (฿)';
      else if (metric === 'qty') metricLabel = 'จำนวนขาย (ชิ้น)';

      let barsSvg = '';
      topItems.forEach((item, idx) => {
        const y = margin.top + (idx * rowHeight);
        const val = item[metric];
        const barWidth = ((val / maxVal) * (width - margin.left - margin.right));
        const formattedVal = (metric === 'qty') ? formatInteger(val) + ' ชิ้น' : formatCurrency(val);
        const rankColor = idx === 0 ? '#ea580c' : (idx === 1 ? '#2563eb' : '#3b82f6');

        barsSvg += `
          <g class="bar-group" style="cursor: pointer;" onmousemove="showTooltip(event, '${item.product} (${item.category})<br>${metricLabel}: ${formattedVal}<br>รายได้: ${formatCurrency(item.revenue)}<br>กำไร: ${formatCurrency(item.gross_profit)}<br>จำนวน: ${formatInteger(item.qty)} ชิ้น')" onmouseleave="hideTooltip()">
            <!-- Rank & Label with plenty of left padding -->
            <text x="${margin.left - 12}" y="${y + 22}" text-anchor="end" fill="var(--text-main)" font-size="12" font-weight="600">
              #${idx + 1} ${item.product}
            </text>
            <!-- Background track -->
            <rect x="${margin.left}" y="${y + 8}" width="${width - margin.left - margin.right}" height="20" rx="4" fill="var(--bg-card-subtle)" />
            <!-- Bar fill -->
            <rect x="${margin.left}" y="${y + 8}" width="${barWidth}" height="20" rx="4" fill="${rankColor}" opacity="0.9" />
            <!-- Value text on right -->
            <text x="${margin.left + barWidth + 8}" y="${y + 23}" fill="var(--text-main)" font-size="11" font-weight="700">
              ${formattedVal}
            </text>
          </g>
        `;
      });

      container.innerHTML = `
        <svg viewBox="0 0 ${width} ${height}" class="interactive-svg">
          <line x1="${margin.left}" y1="${margin.top}" x2="${margin.left}" y2="${height - margin.bottom}" stroke="var(--border-color)" stroke-width="1.5" />
          ${barsSvg}
        </svg>
      `;
    }

    function renderOverviewBranchTable(data) {
      const tbody = document.getElementById('overviewBranchTableBody');
      const bMap = {};
      let totalRev = 0;
      let totalProfit = 0;
      let totalQty = 0;

      data.forEach(x => {
        if (!bMap[x.branch]) {
          bMap[x.branch] = { branch: x.branch, revenue: 0, gross_profit: 0, qty: 0 };
        }
        bMap[x.branch].revenue += x.revenue;
        bMap[x.branch].gross_profit += x.gross_profit;
        bMap[x.branch].qty += x.qty;
        totalRev += x.revenue;
        totalProfit += x.gross_profit;
        totalQty += x.qty;
      });

      const branches = Object.values(bMap).sort((a, b) => b.revenue - a.revenue);

      if (branches.length === 0) {
        tbody.innerHTML = '<tr><td colspan="5" class="text-center" style="padding: 20px; color: var(--text-muted);">ไม่มีข้อมูลสำหรับตัวกรองที่เลือก</td></tr>';
        return;
      }

      let html = branches.map(b => {
        const share = totalRev > 0 ? (b.revenue / totalRev) * 100 : 0;
        const margin = b.revenue > 0 ? (b.gross_profit / b.revenue) : 0;
        return `
          <tr>
            <td style="font-weight: 600;">${b.branch}</td>
            <td class="text-right" style="font-weight: 700;">${formatCurrency(b.revenue)}</td>
            <td class="text-right">
              <div class="share-bar-container">
                <span style="min-width: 42px;">${share.toFixed(1)}%</span>
                <div class="share-bar-outer"><div class="share-bar-inner" style="width: ${share}%;"></div></div>
              </div>
            </td>
            <td class="text-right" style="color: var(--accent-emerald); font-weight: 600;">${formatCurrency(b.gross_profit)}</td>
            <td class="text-right">${formatPercent(margin)}</td>
          </tr>
        `;
      }).join('');

      // Total Row
      const totalMargin = totalRev > 0 ? (totalProfit / totalRev) : 0;
      html += `
        <tr class="total-row">
          <td>รวมทั้งหมด (${branches.length} สาขา)</td>
          <td class="text-right">${formatCurrency(totalRev)}</td>
          <td class="text-right">100.0%</td>
          <td class="text-right" style="color: var(--accent-emerald);">${formatCurrency(totalProfit)}</td>
          <td class="text-right">${formatPercent(totalMargin)}</td>
        </tr>
      `;

      tbody.innerHTML = html;
    }

    // --- 4. SMART INSIGHTS ---
    function renderSmartInsights(data) {
      const container = document.getElementById('smartInsightsContainer');
      if (data.length === 0) {
        container.innerHTML = '<div style="color: var(--text-muted);">ไม่มีข้อมูลสำหรับวิเคราะห์</div>';
        return;
      }

      // Top revenue product vs top profit product
      const prodStats = {};
      const branchStats = {};
      const dowStats = {};
      let totalRev = 0;
      let totalProfit = 0;

      data.forEach(x => {
        totalRev += x.revenue;
        totalProfit += x.gross_profit;
        if (!prodStats[x.product]) prodStats[x.product] = { rev: 0, profit: 0, qty: 0, margin: x.margin, cat: x.category };
        prodStats[x.product].rev += x.revenue;
        prodStats[x.product].profit += x.gross_profit;
        prodStats[x.product].qty += x.qty;

        if (!branchStats[x.branch]) branchStats[x.branch] = { rev: 0, profit: 0, qty: 0 };
        branchStats[x.branch].rev += x.revenue;
        branchStats[x.branch].profit += x.gross_profit;

        if (!dowStats[x.dayOfWeek]) dowStats[x.dayOfWeek] = { rev: 0, profit: 0, qty: 0 };
        dowStats[x.dayOfWeek].rev += x.revenue;
        dowStats[x.dayOfWeek].qty += x.qty;
      });

      const prodsSortedRev = Object.entries(prodStats).sort((a, b) => b[1].rev - a[1].rev);
      const prodsSortedProfit = Object.entries(prodStats).sort((a, b) => b[1].profit - a[1].profit);
      const branchesSorted = Object.entries(branchStats).sort((a, b) => b[1].rev - a[1].rev);
      const dowSorted = Object.entries(dowStats).sort((a, b) => b[1].rev - a[1].rev);

      const topRevProd = prodsSortedRev[0];
      const topProfitProd = prodsSortedProfit[0];
      const topBranch = branchesSorted[0];
      const topDow = dowSorted[0];

      const topBranchShare = totalRev > 0 ? ((topBranch[1].rev / totalRev) * 100).toFixed(1) : 0;
      const topRevShare = totalRev > 0 ? ((topRevProd[1].rev / totalRev) * 100).toFixed(1) : 0;

      container.innerHTML = `
        <div class="insight-item">
          <span class="insight-icon">🏆</span>
          <div class="insight-text">
            <strong>${topRevProd[0]}</strong> ครองแชมป์ยอดขายสูงสุด สร้างรายได้ <strong>${formatCurrency(topRevProd[1].rev)}</strong> (${topRevShare}% ของรายได้ทั้งหมด) โดยมีกำไรขั้นต้น ${formatCurrency(topRevProd[1].profit)}
          </div>
        </div>
        <div class="insight-item">
          <span class="insight-icon">💎</span>
          <div class="insight-text">
            สินค้าสร้างกำไรสูงสุดคือ <strong>${topProfitProd[0]}</strong> ด้วยกำไรขั้นต้น <strong>${formatCurrency(topProfitProd[1].profit)}</strong> (อัตรากำไร ${(topProfitProd[1].profit / topProfitProd[1].rev * 100).toFixed(1)}%)
          </div>
        </div>
        <div class="insight-item">
          <span class="insight-icon">🏢</span>
          <div class="insight-text">
            สาขา <strong>${topBranch[0]}</strong> มีผลงานอันดับ 1 กวาดรายได้ไป <strong>${formatCurrency(topBranch[1].rev)}</strong> คิดเป็น ${topBranchShare}% ของยอดรวมทั้งหมด
          </div>
        </div>
        <div class="insight-item">
          <span class="insight-icon">📅</span>
          <div class="insight-text">
            ช่วงเวลาขายดีที่สุดในสัปดาห์คือ <strong>${topDow[0]}</strong> มียอดขายรวม <strong>${formatCurrency(topDow[1].rev)}</strong> (${topDow[1].qty} ชิ้น)
          </div>
        </div>
      `;
    }

    // --- 5. RECONCILIATION TABLE ---
    function renderReconciliationTable(data) {
      const tbody = document.getElementById('reconciliationTableBody');
      const targetRevenue = data.reduce((acc, x) => acc + x.revenue, 0);

      const dimensions = [
        { name: 'รวมตามสินค้า (Sum by Product)', getGroup: x => x.product },
        { name: 'รวมตามสาขา (Sum by Branch)', getGroup: x => x.branch },
        { name: 'รวมตามหมวดหมู่ (Sum by Category)', getGroup: x => x.category },
        { name: 'รวมตามวันที่ (Sum by Date)', getGroup: x => x.date },
        { name: 'รวมตามวันในสัปดาห์ (Sum by Day of Week)', getGroup: x => x.dayOfWeek }
      ];

      const html = dimensions.map(dim => {
        const groups = {};
        data.forEach(x => {
          const key = dim.getGroup(x);
          groups[key] = (groups[key] || 0) + x.revenue;
        });

        const groupCount = Object.keys(groups).length;
        const dimTotal = Object.values(groups).reduce((acc, v) => acc + v, 0);
        const diff = Math.abs(dimTotal - targetRevenue);
        const isMatched = diff < 0.001;

        return `
          <tr>
            <td style="font-weight: 600;">${dim.name}</td>
            <td class="text-center">${groupCount} กลุ่ม</td>
            <td class="text-right" style="font-weight: 700;">${formatCurrency(dimTotal)}</td>
            <td class="text-right">${formatCurrency(targetRevenue)}</td>
            <td class="text-right" style="color: ${diff === 0 ? 'var(--text-muted)' : 'var(--accent-rose)'};">฿${diff.toFixed(2)}</td>
            <td class="text-center">
              ${isMatched 
                ? '<span class="badge badge-success" style="font-size: 0.8rem;">✔ กระทบยอดตรง 100%</span>' 
                : '<span class="badge" style="background: rgba(225,29,72,0.15); color: var(--accent-rose);">✖ ไม่ตรงกัน</span>'}
            </td>
          </tr>
        `;
      }).join('');

      tbody.innerHTML = html;
    }

    // --- 6. TAB 2: BRANCHES & HEATMAP ---
    function renderBranchTab(data) {
      renderFullBranchTable(data);
      renderBranchDrilldown(data);
      renderHeatmap(data);
    }

    function renderFullBranchTable(data) {
      const tbody = document.getElementById('fullBranchTableBody');
      const bMap = {};
      let totalRev = 0, totalProfit = 0, totalQty = 0, totalTx = 0;

      data.forEach(x => {
        if (!bMap[x.branch]) {
          bMap[x.branch] = { branch: x.branch, revenue: 0, gross_profit: 0, qty: 0, tx: 0 };
        }
        bMap[x.branch].revenue += x.revenue;
        bMap[x.branch].gross_profit += x.gross_profit;
        bMap[x.branch].qty += x.qty;
        bMap[x.branch].tx += 1;
        totalRev += x.revenue;
        totalProfit += x.gross_profit;
        totalQty += x.qty;
        totalTx += 1;
      });

      let list = Object.values(bMap).map(b => ({
        ...b,
        share: totalRev > 0 ? (b.revenue / totalRev) * 100 : 0,
        margin: b.revenue > 0 ? (b.gross_profit / b.revenue) : 0
      }));

      const col = state.branchTable.sortCol;
      const asc = state.branchTable.sortAsc;
      list.sort((a, b) => asc ? (a[col] > b[col] ? 1 : -1) : (a[col] < b[col] ? 1 : -1));

      let html = list.map(b => {
        const isSelected = state.selectedBranchDrilldown === b.branch;
        return `
          <tr class="${isSelected ? 'selected' : ''}" style="cursor: pointer;" onclick="selectBranchDrilldown('${b.branch}')">
            <td style="font-weight: 700;">${b.branch} ${isSelected ? '📌' : ''}</td>
            <td class="text-right">
              <div class="share-bar-container">
                <span style="min-width: 42px;">${b.share.toFixed(1)}%</span>
                <div class="share-bar-outer"><div class="share-bar-inner" style="width: ${b.share}%;"></div></div>
              </div>
            </td>
            <td class="text-right" style="font-weight: 700;">${formatCurrency(b.revenue)}</td>
            <td class="text-right" style="color: var(--accent-emerald); font-weight: 600;">${formatCurrency(b.gross_profit)}</td>
            <td class="text-right">${formatPercent(b.margin)}</td>
            <td class="text-right">${formatInteger(b.qty)}</td>
            <td class="text-right">${formatInteger(b.tx)}</td>
          </tr>
        `;
      }).join('');

      const totalMargin = totalRev > 0 ? (totalProfit / totalRev) : 0;
      html += `
        <tr class="total-row" onclick="selectBranchDrilldown(null)" style="cursor: pointer;" title="คลิกเพื่อเลือกทุกสาขา">
          <td>รวมทุกสาขา (${list.length} สาขา)</td>
          <td class="text-right">100.0%</td>
          <td class="text-right">${formatCurrency(totalRev)}</td>
          <td class="text-right" style="color: var(--accent-emerald);">${formatCurrency(totalProfit)}</td>
          <td class="text-right">${formatPercent(totalMargin)}</td>
          <td class="text-right">${formatInteger(totalQty)}</td>
          <td class="text-right">${formatInteger(totalTx)}</td>
        </tr>
      `;

      tbody.innerHTML = html;
    }

    function selectBranchDrilldown(branch) {
      state.selectedBranchDrilldown = (state.selectedBranchDrilldown === branch) ? null : branch;
      const ind = document.getElementById('selectedBranchIndicator');
      ind.textContent = state.selectedBranchDrilldown ? `กำลังเลือก: ${state.selectedBranchDrilldown}` : 'กำลังเลือก: ทุกสาขา';
      const filtered = getFilteredData();
      renderFullBranchTable(filtered);
      renderBranchDrilldown(filtered);
    }

    function sortBranchTable(col) {
      if (state.branchTable.sortCol === col) {
        state.branchTable.sortAsc = !state.branchTable.sortAsc;
      } else {
        state.branchTable.sortCol = col;
        state.branchTable.sortAsc = false;
      }
      renderFullBranchTable(getFilteredData());
    }

    function renderBranchDrilldown(data) {
      const container = document.getElementById('branchDrilldownChart');
      const title = document.getElementById('branchDrilldownTitle');
      const branch = state.selectedBranchDrilldown;
      title.innerHTML = `<span>📦 ยอดขายรายสินค้าสำหรับ: <strong>${branch || 'ทุกสาขา'}</strong></span>`;

      const subset = branch ? data.filter(x => x.branch === branch) : data;
      const prodMap = {};
      subset.forEach(x => {
        if (!prodMap[x.product]) prodMap[x.product] = { product: x.product, revenue: 0, profit: 0, qty: 0 };
        prodMap[x.product].revenue += x.revenue;
        prodMap[x.product].profit += x.gross_profit;
        prodMap[x.product].qty += x.qty;
      });

      const metric = state.globalMetric;
      const list = Object.values(prodMap).sort((a, b) => b[metric] - a[metric]);

      if (list.length === 0) {
        container.innerHTML = '<div style="padding: 40px; text-align: center; color: var(--text-muted);">ไม่มีข้อมูล</div>';
        return;
      }

      const maxVal = Math.max(...list.map(x => x[metric]), 1);
      const rowHeight = 30;
      const margin = { top: 15, right: 80, bottom: 20, left: 95 };
      const width = 500;
      const height = margin.top + (list.length * rowHeight) + margin.bottom;

      let bars = list.map((item, idx) => {
        const y = margin.top + (idx * rowHeight);
        const w = (item[metric] / maxVal) * (width - margin.left - margin.right);
        const labelVal = metric === 'qty' ? formatInteger(item[metric]) : formatCurrency(item[metric]);
        return `
          <g>
            <text x="${margin.left - 8}" y="${y + 16}" text-anchor="end" fill="var(--text-main)" font-size="11" font-weight="600">${item.product}</text>
            <rect x="${margin.left}" y="${y + 4}" width="${width - margin.left - margin.right}" height="16" rx="3" fill="var(--bg-card-subtle)" />
            <rect x="${margin.left}" y="${y + 4}" width="${w}" height="16" rx="3" fill="var(--primary-blue)" opacity="0.85" />
            <text x="${margin.left + w + 6}" y="${y + 16}" fill="var(--text-main)" font-size="10" font-weight="700">${labelVal}</text>
          </g>
        `;
      }).join('');

      container.innerHTML = `
        <svg viewBox="0 0 ${width} ${height}" class="interactive-svg">
          <line x1="${margin.left}" y1="${margin.top}" x2="${margin.left}" y2="${height - margin.bottom}" stroke="var(--border-color)" />
          ${bars}
        </svg>
      `;
    }

    function renderHeatmap(data) {
      const container = document.getElementById('heatmapContainer');
      const matrix = {};
      const branchTotals = {};
      const prodTotals = {};
      let maxRev = 0;

      ALL_BRANCHES.forEach(b => {
        matrix[b] = {};
        branchTotals[b] = 0;
        ALL_PRODUCTS.forEach(p => matrix[b][p] = 0);
      });
      ALL_PRODUCTS.forEach(p => prodTotals[p] = 0);

      data.forEach(x => {
        if (matrix[x.branch] && matrix[x.branch][x.product] !== undefined) {
          matrix[x.branch][x.product] += x.revenue;
          branchTotals[x.branch] += x.revenue;
          prodTotals[x.product] += x.revenue;
          if (matrix[x.branch][x.product] > maxRev) maxRev = matrix[x.branch][x.product];
        }
      });

      let thead = '<tr><th>สาขา \ สินค้า</th>' + ALL_PRODUCTS.map(p => `<th class="text-right" style="font-size: 0.76rem;">${p}</th>`).join('') + '<th class="text-right">รวมสาขา</th></tr>';

      let rows = ALL_BRANCHES.map(b => {
        let cells = ALL_PRODUCTS.map(p => {
          const rev = matrix[b][p];
          const intensity = maxRev > 0 ? (rev / maxRev) : 0;
          // Gradient from subtle blue to vibrant orange
          const bg = intensity > 0 
            ? `rgba(234, 88, 12, ${Math.max(0.12, intensity * 0.85)})` 
            : 'var(--bg-card-subtle)';
          const textColor = intensity > 0.5 ? '#ffffff' : 'var(--text-main)';
          return `
            <td class="text-right heatmap-cell" style="background: ${bg}; color: ${textColor};" onmousemove="showTooltip(event, '${b} × ${p}<br>รายได้: ${formatCurrency(rev)}')" onmouseleave="hideTooltip()">
              ${rev > 0 ? formatCurrency(rev).replace('฿', '') : '-'}
            </td>
          `;
        }).join('');

        return `
          <tr>
            <td style="font-weight: 700;">${b}</td>
            ${cells}
            <td class="text-right" style="font-weight: 800; background: var(--bg-card-subtle);">${formatCurrency(branchTotals[b])}</td>
          </tr>
        `;
      }).join('');

      let footerCells = ALL_PRODUCTS.map(p => `<td class="text-right" style="font-weight: 800;">${formatCurrency(prodTotals[p])}</td>`).join('');
      let totalRevAll = Object.values(prodTotals).reduce((a, b) => a + b, 0);

      container.innerHTML = `
        <table class="data-table" style="font-size: 0.8rem;">
          <thead>${thead}</thead>
          <tbody>${rows}</tbody>
          <tfoot>
            <tr class="total-row">
              <td>รวมสินค้า</td>
              ${footerCells}
              <td class="text-right" style="color: var(--primary-orange);">${formatCurrency(totalRevAll)}</td>
            </tr>
          </tfoot>
        </table>
      `;
    }

    // --- 7. TAB 3: PRODUCTS & ABC (PARETO & SCATTER) ---
    function renderProductTab(data) {
      renderParetoChart(data);
      renderScatterPlot(data);
      renderProductMasterTable(data);
    }

    function renderParetoChart(data) {
      const barContainer = document.getElementById('abcBarChartContainer');
      const lineContainer = document.getElementById('abcLineChartContainer');
      const summaryBanner = document.getElementById('abcSummaryBanner');
      const metric = state.globalMetric;

      const pMap = {};
      let totalVal = 0;
      data.forEach(x => {
        if (!pMap[x.product]) pMap[x.product] = { product: x.product, category: x.category, val: 0, revenue: 0, profit: 0, qty: 0 };
        pMap[x.product].val += x[metric];
        pMap[x.product].revenue += x.revenue;
        pMap[x.product].profit += x.gross_profit;
        pMap[x.product].qty += x.qty;
        totalVal += x[metric];
      });

      const prods = Object.values(pMap).sort((a, b) => b.val - a.val);
      if (prods.length === 0 || totalVal === 0) {
        if (barContainer) barContainer.innerHTML = '<div style="padding: 40px; text-align: center; color: var(--text-muted);">ไม่มีข้อมูลสำหรับวิเคราะห์ ABC</div>';
        if (lineContainer) lineContainer.innerHTML = '';
        if (summaryBanner) summaryBanner.innerHTML = '';
        return;
      }

      // Classify ABC: Prior cumulative < 80% => A, < 95% => B, else => C
      let cum = 0;
      let countA = 0, countB = 0, countC = 0;
      let valA = 0, valB = 0, valC = 0;

      prods.forEach(p => {
        const priorCumPct = (cum / totalVal) * 100;
        cum += p.val;
        p.cumPct = (cum / totalVal) * 100;

        if (priorCumPct < 80) {
          p.abc = 'A';
          countA++;
          valA += p.val;
        } else if (priorCumPct < 95) {
          p.abc = 'B';
          countB++;
          valB += p.val;
        } else {
          p.abc = 'C';
          countC++;
          valC += p.val;
        }
      });

      // ----------------------------------------------------
      // 1. PURE BAR CHART (NO LINES, 100% UNCLUTTERED!)
      // ----------------------------------------------------
      if (barContainer) {
        const width = 500;
        const height = 320;
        const margin = { top: 35, right: 25, bottom: 85, left: 65 };
        const chartW = width - margin.left - margin.right;
        const chartH = height - margin.top - margin.bottom;
        const maxVal = getNiceMax(prods[0].val);
        const colW = chartW / prods.length;
        const barW = Math.max(16, colW * 0.65);

        let gridLines = '';
        for (let i = 0; i <= 4; i++) {
          const val = (i / 4) * maxVal;
          const y = margin.top + chartH - (i / 4) * chartH;
          gridLines += `
            <line x1="${margin.left}" y1="${y}" x2="${width - margin.right}" y2="${y}" class="svg-grid-line" />
            <text x="${margin.left - 8}" y="${y + 4}" text-anchor="end" class="svg-axis-text">${formatInteger(val)}</text>
          `;
        }

        let bars = prods.map((p, idx) => {
          const cx = margin.left + (idx * colW) + (colW / 2);
          const barH = (p.val / maxVal) * chartH;
          const barY = margin.top + chartH - barH;
          const color = p.abc === 'A' ? 'var(--primary-blue)' : (p.abc === 'B' ? 'var(--primary-orange)' : '#94a3b8');
          const formattedVal = metric === 'qty' ? formatInteger(p.val) : formatInteger(p.val);

          return `
            <g style="cursor: pointer;" onmousemove="showTooltip(event, '<strong>${p.product}</strong> [กลุ่ม ${p.abc}]<br>${metric === 'qty' ? 'จำนวน' : (metric === 'gross_profit' ? 'กำไร' : 'รายได้')}: ${metric === 'qty' ? formatInteger(p.val) + ' ชิ้น' : formatCurrency(p.val)}')" onmouseleave="hideTooltip()">
              <!-- Value on top of bar -->
              <text x="${cx}" y="${barY - 6}" text-anchor="middle" font-size="10" font-weight="700" fill="var(--text-main)">${formattedVal}</text>
              <!-- Clean Bar (No lines cutting through!) -->
              <rect x="${cx - barW / 2}" y="${barY}" width="${barW}" height="${barH}" rx="4" fill="${color}" opacity="0.9" />
              <!-- ABC Badge below baseline -->
              <rect x="${cx - 12}" y="${height - margin.bottom + 6}" width="24" height="16" rx="3" fill="${color}" opacity="0.18" />
              <text x="${cx}" y="${height - margin.bottom + 17.5}" text-anchor="middle" font-size="10" font-weight="800" fill="${color}">${p.abc}</text>
              <!-- Product Name -->
              <text x="${cx - 4}" y="${height - margin.bottom + 36}" text-anchor="end" transform="rotate(-35, ${cx - 4}, ${height - margin.bottom + 36})" font-size="11" font-weight="600" fill="var(--text-main)">${p.product}</text>
            </g>
          `;
        }).join('');

        barContainer.innerHTML = `
          <svg viewBox="0 0 ${width} ${height}" class="interactive-svg">
            ${gridLines}
            <line x1="${margin.left}" y1="${height - margin.bottom}" x2="${width - margin.right}" y2="${height - margin.bottom}" class="svg-axis-line" />
            ${bars}
            <text x="${margin.left}" y="18" class="svg-axis-title">${metric === 'qty' ? 'จำนวนขาย (ชิ้น)' : (metric === 'gross_profit' ? 'กำไรขั้นต้น (฿)' : 'รายได้รวม (฿)')}</text>
          </svg>
        `;
      }

      // ----------------------------------------------------
      // 2. PURE CUMULATIVE LINE CHART (NO BARS, 100% CLEAN!)
      // ----------------------------------------------------
      if (lineContainer) {
        const width = 500;
        const height = 320;
        const margin = { top: 35, right: 45, bottom: 85, left: 55 };
        const chartW = width - margin.left - margin.right;
        const chartH = height - margin.top - margin.bottom;
        const colW = chartW / prods.length;

        let gridLines = '';
        for (let p = 0; p <= 100; p += 20) {
          const y = margin.top + chartH - (p / 100) * chartH;
          gridLines += `
            <line x1="${margin.left}" y1="${y}" x2="${width - margin.right}" y2="${y}" class="svg-grid-line" />
            <text x="${margin.left - 8}" y="${y + 4}" text-anchor="end" class="svg-axis-text">${p}%</text>
          `;
        }

        // Reference lines at 80% & 95% with clear badge pills
        const y80 = margin.top + chartH - (0.80 * chartH);
        const y95 = margin.top + chartH - (0.95 * chartH);
        const refLines = `
          <line x1="${margin.left}" y1="${y95}" x2="${width - margin.right}" y2="${y95}" stroke="#f59e0b" stroke-dasharray="5,3" stroke-width="1.5" />
          <g transform="translate(${margin.left + 8}, ${y95 - 18})">
            <rect x="0" y="0" width="116" height="17" rx="3" fill="var(--bg-card)" stroke="#f59e0b" stroke-width="1" opacity="0.95" />
            <text x="58" y="12" text-anchor="middle" fill="#d97706" font-size="9.5" font-weight="700">เกณฑ์ 95% (กลุ่ม B)</text>
          </g>
          <line x1="${margin.left}" y1="${y80}" x2="${width - margin.right}" y2="${y80}" stroke="#ea580c" stroke-dasharray="5,3" stroke-width="1.5" />
          <g transform="translate(${margin.left + 8}, ${y80 - 18})">
            <rect x="0" y="0" width="116" height="17" rx="3" fill="var(--bg-card)" stroke="#ea580c" stroke-width="1" opacity="0.95" />
            <text x="58" y="12" text-anchor="middle" fill="#ea580c" font-size="9.5" font-weight="700">เกณฑ์ 80% (กลุ่ม A)</text>
          </g>
        `;

        const coords = prods.map((p, idx) => {
          const x = margin.left + (idx * colW) + (colW / 2);
          const y = margin.top + chartH - ((p.cumPct / 100) * chartH);
          return { x, y, p };
        });

        const areaPoints = [
          `${coords[0].x},${margin.top + chartH}`,
          ...coords.map(c => `${c.x},${c.y}`),
          `${coords[coords.length - 1].x},${margin.top + chartH}`
        ].join(' ');

        const linePoints = coords.map(c => `${c.x},${c.y}`).join(' ');

        const points = coords.map(c => `
          <g style="cursor: pointer;" onmousemove="showTooltip(event, '<strong>${c.p.product}</strong><br>สัดส่วนสะสม: ${c.p.cumPct.toFixed(1)}%<br>กลุ่ม: ${c.p.abc}')" onmouseleave="hideTooltip()">
            <circle cx="${c.x}" cy="${c.y}" r="4.5" fill="#ffffff" stroke="#ea580c" stroke-width="2.5" />
            <text x="${c.x}" y="${c.y - 8}" text-anchor="middle" font-size="10" font-weight="700" fill="#ea580c">${c.p.cumPct.toFixed(1)}%</text>
            <text x="${c.x - 4}" y="${height - margin.bottom + 28}" text-anchor="end" transform="rotate(-35, ${c.x - 4}, ${height - margin.bottom + 28})" font-size="11" font-weight="600" fill="var(--text-main)">${c.p.product}</text>
          </g>
        `).join('');

        lineContainer.innerHTML = `
          <svg viewBox="0 0 ${width} ${height}" class="interactive-svg">
            <defs>
              <linearGradient id="cumLineGrad" x1="0" y1="0" x2="0" y2="1">
                <stop offset="0%" stop-color="#ea580c" stop-opacity="0.25" />
                <stop offset="100%" stop-color="#ea580c" stop-opacity="0.02" />
              </linearGradient>
            </defs>
            ${gridLines}
            ${refLines}
            <polygon fill="url(#cumLineGrad)" points="${areaPoints}" />
            <polyline fill="none" stroke="#ea580c" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" points="${linePoints}" />
            ${points}
            <line x1="${margin.left}" y1="${height - margin.bottom}" x2="${width - margin.right}" y2="${height - margin.bottom}" class="svg-axis-line" />
            <text x="${margin.left}" y="18" class="svg-axis-title">เปอร์เซ็นต์สะสม (Cumulative %)</text>
          </svg>
        `;
      }

      // ABC summary box
      if (summaryBanner) {
        summaryBanner.innerHTML = `
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px;">
            <div>
              <strong style="color: var(--primary-blue);">กลุ่ม A (${countA} รายการ):</strong> ${((valA / totalVal) * 100).toFixed(1)}% ของมูลค่ารวม
              <div style="font-size: 0.78rem; color: var(--text-muted);">สินค้าสร้างรายได้หลัก ควรบริหารสต็อกห้ามขาด</div>
            </div>
            <div>
              <strong style="color: var(--primary-orange);">กลุ่ม B (${countB} รายการ):</strong> ${((valB / totalVal) * 100).toFixed(1)}% ของมูลค่ารวม
              <div style="font-size: 0.78rem; color: var(--text-muted);">สินค้าทำเงินระดับรอง จัดโปรโมชันกระตุ้นยอดได้</div>
            </div>
            <div>
              <strong style="color: var(--text-muted);">กลุ่ม C (${countC} รายการ):</strong> ${((valC / totalVal) * 100).toFixed(1)}% ของมูลค่ารวม
              <div style="font-size: 0.78rem; color: var(--text-muted);">สินค้าหางยาว ติดตามต้นทุนและสต็อกอย่างรัดกุม</div>
            </div>
          </div>
        `;
      }
    }

    function renderScatterPlot(data) {
      const container = document.getElementById('scatterChartContainer');
      const prodStats = {};
      let totalQty = 0, totalProfit = 0, totalRev = 0;

      data.forEach(x => {
        if (!prodStats[x.product]) {
          prodStats[x.product] = { product: x.product, category: x.category, qty: 0, revenue: 0, profit: 0 };
        }
        prodStats[x.product].qty += x.qty;
        prodStats[x.product].revenue += x.revenue;
        prodStats[x.product].profit += x.gross_profit;
        totalQty += x.qty;
        totalProfit += x.gross_profit;
        totalRev += x.revenue;
      });

      const prods = Object.values(prodStats).map(p => ({
        ...p,
        margin: p.revenue > 0 ? (p.profit / p.revenue) : 0
      }));

      if (prods.length === 0) {
        container.innerHTML = '<div style="padding: 40px; text-align: center; color: var(--text-muted);">ไม่มีข้อมูล</div>';
        return;
      }

      const avgQty = totalQty / prods.length;
      const avgMargin = totalRev > 0 ? (totalProfit / totalRev) : 0;

      // Auto-scale X domain to actual data spread (100 to 150 units) so bubbles never clump together!
      const allQtys = prods.map(p => p.qty);
      const minX = Math.max(0, Math.floor((Math.min(...allQtys) - 5) / 10) * 10);
      const maxX = Math.ceil((Math.max(...allQtys) + 5) / 10) * 10;

      // Auto-scale Y domain (20% to 75%)
      const minY = 0.20;
      const maxY = 0.75;

      const margin = { top: 35, right: 35, bottom: 50, left: 65 };
      const width = 560;
      const height = 340;
      const chartW = width - margin.left - margin.right;
      const chartH = height - margin.top - margin.bottom;

      // Quadrant line coordinates (Crosshairs at average qty and average margin)
      const splitX = margin.left + ((avgQty - minX) / (maxX - minX)) * chartW;
      const splitY = margin.top + chartH - (((avgMargin - minY) / (maxY - minY)) * chartH);

      // Gridlines & Ticks for X Axis
      let xTicksSvg = '';
      const xStep = (maxX - minX) <= 60 ? 10 : 20;
      for (let q = minX; q <= maxX; q += xStep) {
        const x = margin.left + ((q - minX) / (maxX - minX)) * chartW;
        xTicksSvg += `
          <line x1="${x}" y1="${margin.top}" x2="${x}" y2="${height - margin.bottom}" stroke="var(--border-color)" stroke-dasharray="3,3" stroke-width="0.8" opacity="0.6" />
          <text x="${x}" y="${height - margin.bottom + 16}" text-anchor="middle" font-size="10" fill="var(--text-muted)">${q}</text>
        `;
      }

      // Gridlines & Ticks for Y Axis
      let yTicksSvg = '';
      for (let m = 0.20; m <= 0.75; m += 0.10) {
        const y = margin.top + chartH - (((m - minY) / (maxY - minY)) * chartH);
        yTicksSvg += `
          <line x1="${margin.left}" y1="${y}" x2="${width - margin.right}" y2="${y}" stroke="var(--border-color)" stroke-dasharray="3,3" stroke-width="0.8" opacity="0.6" />
          <text x="${margin.left - 8}" y="${y + 3.5}" text-anchor="end" font-size="10" fill="var(--text-muted)">${Math.round(m * 100)}%</text>
        `;
      }

      // Group products into 4 quadrants for summary cards
      const stars = [];
      const cows = [];
      const niches = [];
      const dogs = [];

      // Category color map
      const catColors = { 'กาแฟ': '#2563eb', 'เบเกอรี': '#ea580c', 'เครื่องดื่มอื่น': '#0284c7' };

      // Bubbles & clean non-overlapping labels
      let bubblesSvg = '';
      prods.forEach(p => {
        const cx = margin.left + ((p.qty - minX) / (maxX - minX)) * chartW;
        const cy = margin.top + chartH - (((p.margin - minY) / (maxY - minY)) * chartH);
        const r = Math.max(12, Math.min(22, Math.sqrt(p.revenue) * 0.18));
        const col = catColors[p.category] || 'var(--primary-blue)';

        // Categorize into quadrant
        if (p.qty >= avgQty && p.margin >= avgMargin) stars.push(p.product);
        else if (p.qty >= avgQty && p.margin < avgMargin) cows.push(p.product);
        else if (p.qty < avgQty && p.margin >= avgMargin) niches.push(p.product);
        else dogs.push(p.product);

        // Smart label placement (alternate above/below to guarantee zero collision!)
        const isLabelAbove = ['ลาเต้', 'อเมริกาโน', 'ชาไทย', 'ชีสเค้ก'].includes(p.product);
        const labelY = isLabelAbove ? (cy - r - 5) : (cy + r + 13);

        bubblesSvg += `
          <g style="cursor: pointer;" onmousemove="showTooltip(event, '<strong>${p.product}</strong> (${p.category})<br>จำนวนขาย: ${formatInteger(p.qty)} ชิ้น<br>อัตรากำไร: ${formatPercent(p.margin)}<br>รายได้รวม: ${formatCurrency(p.revenue)}<br>กำไรขั้นต้น: ${formatCurrency(p.profit)}')" onmouseleave="hideTooltip()">
            <!-- Bubble with shadow and border -->
            <circle cx="${cx}" cy="${cy}" r="${r}" fill="${col}" opacity="0.75" stroke="#ffffff" stroke-width="2" />
            <!-- Inner white dot -->
            <circle cx="${cx}" cy="${cy}" r="3" fill="#ffffff" pointer-events="none" />
            <!-- Full readable product label with background outline (Never blurred or cut off!) -->
            <text x="${cx}" y="${labelY}" text-anchor="middle" font-size="10.5" font-weight="700" fill="var(--text-main)" stroke="var(--bg-card)" stroke-width="3" stroke-linejoin="round" paint-order="stroke fill" pointer-events="none">
              ${p.product}
            </text>
          </g>
        `;
      });

      container.innerHTML = `
        <svg viewBox="0 0 ${width} ${height}" class="interactive-svg">
          <!-- Soft Quadrant Background Tints -->
          <rect x="${splitX}" y="${margin.top}" width="${width - margin.right - splitX}" height="${splitY - margin.top}" fill="#059669" opacity="0.04" />
          <rect x="${splitX}" y="${splitY}" width="${width - margin.right - splitX}" height="${height - margin.bottom - splitY}" fill="#ea580c" opacity="0.04" />
          <rect x="${margin.left}" y="${margin.top}" width="${splitX - margin.left}" height="${splitY - margin.top}" fill="#0284c7" opacity="0.04" />
          <rect x="${margin.left}" y="${splitY}" width="${splitX - margin.left}" height="${height - margin.bottom - splitY}" fill="#64748b" opacity="0.04" />

          <!-- Axis Gridlines -->
          ${xTicksSvg}
          ${yTicksSvg}

          <!-- Quadrant Watermark Badges (Subtle, never colliding) -->
          <text x="${width - margin.right - 8}" y="${margin.top + 16}" text-anchor="end" font-size="10" font-weight="700" fill="#059669" opacity="0.8">⭐ ดาวเด่น (ยอดขายสูง • กำไรสูง)</text>
          <text x="${width - margin.right - 8}" y="${height - margin.bottom - 10}" text-anchor="end" font-size="10" font-weight="700" fill="#ea580c" opacity="0.8">📦 ขุมพลังทำเงิน (ยอดขายสูง • กำไรบาง)</text>
          <text x="${margin.left + 8}" y="${margin.top + 16}" text-anchor="start" font-size="10" font-weight="700" fill="#0284c7" opacity="0.8">💎 โอกาสสูง (ขายน้อย • กำไรสูง)</text>
          <text x="${margin.left + 8}" y="${height - margin.bottom - 10}" text-anchor="start" font-size="10" font-weight="700" fill="#64748b" opacity="0.8">🔍 ต้องทบทวน (ขายน้อย • กำไรบาง)</text>

          <!-- Crosshairs Average Lines -->
          <line x1="${splitX}" y1="${margin.top}" x2="${splitX}" y2="${height - margin.bottom}" stroke="var(--primary-blue)" stroke-dasharray="5,4" stroke-width="1.5" opacity="0.7" />
          <line x1="${margin.left}" y1="${splitY}" x2="${width - margin.right}" y2="${splitY}" stroke="var(--primary-orange)" stroke-dasharray="5,4" stroke-width="1.5" opacity="0.7" />

          <!-- Average Axis Markers -->
          <g transform="translate(${splitX}, ${height - margin.bottom + 26})">
            <text x="0" y="0" text-anchor="middle" font-size="9" font-weight="700" fill="var(--primary-blue)">เฉลี่ย ${Math.round(avgQty)} ชิ้น</text>
          </g>
          <g transform="translate(${margin.left - 6}, ${splitY - 6})">
            <text x="0" y="0" text-anchor="end" font-size="9" font-weight="700" fill="var(--primary-orange)">เฉลี่ย ${(avgMargin * 100).toFixed(1)}%</text>
          </g>

          <!-- Axes Lines -->
          <line x1="${margin.left}" y1="${height - margin.bottom}" x2="${width - margin.right}" y2="${height - margin.bottom}" class="svg-axis-line" stroke-width="1.5" />
          <line x1="${margin.left}" y1="${margin.top}" x2="${margin.left}" y2="${height - margin.bottom}" class="svg-axis-line" stroke-width="1.5" />

          <!-- Data Bubbles & Labels -->
          ${bubblesSvg}

          <!-- Axis Titles -->
          <text x="${width / 2}" y="${height - 6}" text-anchor="middle" class="svg-axis-title">จำนวนหน่วยที่ขาย (ชิ้น)</text>
          <text x="14" y="${height / 2}" text-anchor="middle" transform="rotate(-90, 14, ${height / 2})" class="svg-axis-title">อัตรากำไรขั้นต้น (Margin %)</text>
        </svg>

        <!-- 4-Quadrant Strategic Breakdown Cards (ดูง่าย เข้าใจได้ทันที!) -->
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(210px, 1fr)); gap: 8px; margin-top: 14px; font-size: 0.8rem;">
          <div style="background: rgba(5, 150, 105, 0.08); border: 1px solid rgba(5, 150, 105, 0.25); border-radius: var(--radius-sm); padding: 8px 12px;">
            <div style="font-weight: 700; color: var(--accent-emerald); display: flex; justify-content: space-between;">
              <span>⭐ สินค้าดาวเด่น</span>
              <span>${stars.length} รายการ</span>
            </div>
            <div style="font-weight: 600; color: var(--text-main); margin: 3px 0;">${stars.join(', ') || '-'}</div>
            <div style="font-size: 0.72rem; color: var(--text-muted);">ขายดี & กำไรสูง • โปรโมตและรักษามาตรฐานต่อเนื่อง</div>
          </div>

          <div style="background: rgba(234, 88, 12, 0.08); border: 1px solid rgba(234, 88, 12, 0.25); border-radius: var(--radius-sm); padding: 8px 12px;">
            <div style="font-weight: 700; color: var(--primary-orange); display: flex; justify-content: space-between;">
              <span>📦 ขุมพลังทำเงิน</span>
              <span>${cows.length} รายการ</span>
            </div>
            <div style="font-weight: 600; color: var(--text-main); margin: 3px 0;">${cows.join(', ') || '-'}</div>
            <div style="font-size: 0.72rem; color: var(--text-muted);">ปริมาณขายสูงแต่กำไรบาง • บริหารต้นทุนเพื่อเพิ่มมาร์จิ้น</div>
          </div>

          <div style="background: rgba(2, 132, 199, 0.08); border: 1px solid rgba(2, 132, 199, 0.25); border-radius: var(--radius-sm); padding: 8px 12px;">
            <div style="font-weight: 700; color: var(--accent-cyan); display: flex; justify-content: space-between;">
              <span>💎 โอกาสเติบโต</span>
              <span>${niches.length} รายการ</span>
            </div>
            <div style="font-weight: 600; color: var(--text-main); margin: 3px 0;">${niches.join(', ') || '-'}</div>
            <div style="font-size: 0.72rem; color: var(--text-muted);">มาร์จิ้นสูงแต่ขายน้อย • จัดโปรโมชันกระตุ้นยอดขาย</div>
          </div>

          <div style="background: rgba(148, 163, 184, 0.08); border: 1px solid rgba(148, 163, 184, 0.25); border-radius: var(--radius-sm); padding: 8px 12px;">
            <div style="font-weight: 700; color: var(--text-muted); display: flex; justify-content: space-between;">
              <span>🔍 ต้องทบทวน</span>
              <span>${dogs.length} รายการ</span>
            </div>
            <div style="font-weight: 600; color: var(--text-main); margin: 3px 0;">${dogs.join(', ') || '-'}</div>
            <div style="font-size: 0.72rem; color: var(--text-muted);">ปริมาณขายน้อยและกำไรบาง • พิจารณาปรับสูตรหรือทบทวน</div>
          </div>
        </div>
      `;
    }

    function renderProductMasterTable(data) {
      const tbody = document.getElementById('productMasterTableBody');
      const pMap = {};
      let totalRev = 0;

      data.forEach(x => {
        if (!pMap[x.product]) {
          pMap[x.product] = { product: x.product, category: x.category, price: x.price, cost: x.cost, qty: 0, revenue: 0, gross_profit: 0 };
        }
        pMap[x.product].qty += x.qty;
        pMap[x.product].revenue += x.revenue;
        pMap[x.product].gross_profit += x.gross_profit;
        totalRev += x.revenue;
      });

      let list = Object.values(pMap).map(p => ({
        ...p,
        margin: p.revenue > 0 ? (p.gross_profit / p.revenue) : 0,
        unitProfit: p.price - p.cost
      }));

      // Calculate ABC rank
      list.sort((a, b) => b.revenue - a.revenue);
      let cum = 0;
      list.forEach(p => {
        const priorCumPct = (cum / totalRev) * 100;
        cum += p.revenue;
        p.abc = priorCumPct < 80 ? 'A' : (priorCumPct < 95 ? 'B' : 'C');
      });

      const col = state.productTable.sortCol;
      const asc = state.productTable.sortAsc;
      list.sort((a, b) => asc ? (a[col] > b[col] ? 1 : -1) : (a[col] < b[col] ? 1 : -1));

      tbody.innerHTML = list.map(p => `
        <tr>
          <td style="font-weight: 700;">${p.product}</td>
          <td>${p.category}</td>
          <td class="text-center">
            <span class="badge" style="background: ${p.abc === 'A' ? 'rgba(37,99,235,0.15)' : (p.abc === 'B' ? 'rgba(234,88,12,0.15)' : 'rgba(148,163,184,0.15)')}; color: ${p.abc === 'A' ? 'var(--primary-blue)' : (p.abc === 'B' ? 'var(--primary-orange)' : 'var(--text-muted)')};">
              กลุ่ม ${p.abc}
            </span>
          </td>
          <td class="text-right">฿${p.price.toFixed(2)}</td>
          <td class="text-right">฿${p.cost.toFixed(2)}</td>
          <td class="text-right">${formatInteger(p.qty)}</td>
          <td class="text-right" style="font-weight: 700;">${formatCurrency(p.revenue)}</td>
          <td class="text-right" style="color: var(--accent-emerald); font-weight: 600;">${formatCurrency(p.gross_profit)}</td>
          <td class="text-right">${formatPercent(p.margin)}</td>
        </tr>
      `).join('');
    }

    function sortProductTable(col) {
      if (state.productTable.sortCol === col) state.productTable.sortAsc = !state.productTable.sortAsc;
      else { state.productTable.sortCol = col; state.productTable.sortAsc = false; }
      renderProductMasterTable(getFilteredData());
    }

    // --- 8. TAB 4: TIME TRENDS & CALENDAR ---
    function renderTrendsTab(data) {
      renderCumulativeTrend(data);
      renderDowChart(data);
      renderCalendarGrid(data);
    }

    function renderCumulativeTrend(data) {
      const container = document.getElementById('cumulativeTrendChart');
      if (!data || data.length === 0) {
        container.innerHTML = '<div style="padding: 40px; text-align: center; color: var(--text-muted);">ไม่มีข้อมูลตามตัวกรองที่เลือก</div>';
        return;
      }

      const dateMap = {};
      data.forEach(x => {
        dateMap[x.date] = (dateMap[x.date] || 0) + x.revenue;
      });

      const dates = Object.keys(dateMap).sort();
      let runningSum = 0;
      const trendPoints = dates.map(d => {
        runningSum += dateMap[d];
        return { date: d, day: d.slice(5), daily: dateMap[d], cum: runningSum };
      });

      const maxCum = Math.max(...trendPoints.map(p => p.cum), 1);
      const margin = { top: 20, right: 30, bottom: 40, left: 75 };
      const width = 800;
      const height = 280;
      const chartW = width - margin.left - margin.right;
      const chartH = height - margin.top - margin.bottom;

      let gridLines = '';
      for (let i = 0; i <= 4; i++) {
        const val = (maxCum / 4) * i;
        const y = margin.top + chartH - (i / 4) * chartH;
        gridLines += `
          <line x1="${margin.left}" y1="${y}" x2="${width - margin.right}" y2="${y}" class="svg-grid-line" />
          <text x="${margin.left - 8}" y="${y + 4}" text-anchor="end" class="svg-axis-text">${formatCurrency(val)}</text>
        `;
      }

      const coords = trendPoints.map((p, idx) => {
        const x = margin.left + (idx / (trendPoints.length - 1)) * chartW;
        const y = margin.top + chartH - ((p.cum / maxCum) * chartH);
        return { x, y, ...p };
      });

      const areaPoints = [`${margin.left},${margin.top + chartH}`, ...coords.map(c => `${c.x},${c.y}`), `${width - margin.right},${margin.top + chartH}`].join(' ');
      const linePoints = coords.map(c => `${c.x},${c.y}`).join(' ');

      const circles = coords.filter((c, i) => i % 3 === 0 || i === coords.length - 1).map(c => `
        <circle cx="${c.x}" cy="${c.y}" r="3.5" fill="#ffffff" stroke="var(--primary-blue)" stroke-width="2" style="cursor: pointer;" onmousemove="showTooltip(event, 'วันที่ ${c.date}<br>ยอดขายวันนั้น: ${formatCurrency(c.daily)}<br>ยอดสะสม: ${formatCurrency(c.cum)}')" onmouseleave="hideTooltip()" />
      `).join('');

      container.innerHTML = `
        <svg viewBox="0 0 ${width} ${height}" class="interactive-svg">
          <defs>
            <linearGradient id="areaGrad" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0%" stop-color="var(--primary-blue)" stop-opacity="0.35" />
              <stop offset="100%" stop-color="var(--primary-blue)" stop-opacity="0.02" />
            </linearGradient>
          </defs>
          ${gridLines}
          <polygon fill="url(#areaGrad)" points="${areaPoints}" />
          <polyline fill="none" stroke="var(--primary-blue)" stroke-width="2.5" points="${linePoints}" />
          ${circles}
          <!-- X Axis Dates -->
          <line x1="${margin.left}" y1="${height - margin.bottom}" x2="${width - margin.right}" y2="${height - margin.bottom}" class="svg-axis-line" />
          <text x="${margin.left}" y="${height - 12}" class="svg-axis-text">1 ส.ค.</text>
          <text x="${margin.left + chartW * 0.25}" y="${height - 12}" class="svg-axis-text">8 ส.ค.</text>
          <text x="${margin.left + chartW * 0.5}" y="${height - 12}" class="svg-axis-text">15 ส.ค.</text>
          <text x="${margin.left + chartW * 0.75}" y="${height - 12}" class="svg-axis-text">22 ส.ค.</text>
          <text x="${width - margin.right}" y="${height - 12}" text-anchor="end" class="svg-axis-text">31 ส.ค.</text>
        </svg>
      `;
    }

    function renderDowChart(data) {
      const container = document.getElementById('dowChartContainer');
      const metric = state.globalMetric;

      const dowMap = {};
      DOW_ORDER.forEach(d => dowMap[d] = { dow: d, val: 0, revenue: 0, profit: 0, qty: 0 });
      data.forEach(x => {
        if (dowMap[x.dayOfWeek]) {
          dowMap[x.dayOfWeek].val += x[metric];
          dowMap[x.dayOfWeek].revenue += x.revenue;
          dowMap[x.dayOfWeek].profit += x.gross_profit;
          dowMap[x.dayOfWeek].qty += x.qty;
        }
      });

      const items = DOW_ORDER.map(d => dowMap[d]);
      const maxVal = getNiceMax(Math.max(...items.map(x => x.val), 1));
      const avgVal = items.reduce((acc, x) => acc + x.val, 0) / items.length;

      const margin = { top: 35, right: 30, bottom: 45, left: 75 };
      const width = 520;
      const height = 290;
      const chartW = width - margin.left - margin.right;
      const chartH = height - margin.top - margin.bottom;
      const colW = chartW / items.length;
      const barW = Math.max(16, colW * 0.62);

      const avgY = margin.top + chartH - ((avgVal / maxVal) * chartH);

      let gridLines = '';
      for (let i = 0; i <= 4; i++) {
        const val = (i / 4) * maxVal;
        const y = margin.top + chartH - (i / 4) * chartH;
        gridLines += `
          <line x1="${margin.left}" y1="${y}" x2="${width - margin.right}" y2="${y}" class="svg-grid-line" />
          <text x="${margin.left - 8}" y="${y + 4}" text-anchor="end" class="svg-axis-text">${formatInteger(val)}</text>
        `;
      }

      let bars = items.map((item, idx) => {
        const cx = margin.left + (idx * colW) + (colW / 2);
        const barH = (item.val / maxVal) * chartH;
        const barY = margin.top + chartH - barH;
        const isWeekend = ['วันเสาร์', 'วันอาทิตย์'].includes(item.dow);
        const col = isWeekend ? 'var(--primary-orange)' : 'var(--primary-blue)';
        const formattedVal = metric === 'qty' ? formatInteger(item.val) : formatCurrency(item.val);

        return `
          <g style="cursor: pointer;" onmousemove="showTooltip(event, '<strong>${item.dow}</strong><br>ค่า: ${formattedVal}<br>รายได้: ${formatCurrency(item.revenue)}<br>กำไร: ${formatCurrency(item.profit)}<br>จำนวน: ${formatInteger(item.qty)} ชิ้น')" onmouseleave="hideTooltip()">
            <rect x="${cx - barW / 2}" y="${barY}" width="${barW}" height="${barH}" rx="4" fill="${col}" opacity="0.9" />
            <text x="${cx}" y="${height - margin.bottom + 18}" text-anchor="middle" font-size="11" font-weight="600" fill="var(--text-main)">${item.dow.replace('วัน', '')}</text>
          </g>
        `;
      }).join('');

      container.innerHTML = `
        <svg viewBox="0 0 ${width} ${height}" class="interactive-svg">
          ${gridLines}
          <!-- Average Line & Badge on LEFT (Never collides with Sunday bar on right!) -->
          <line x1="${margin.left}" y1="${avgY}" x2="${width - margin.right}" y2="${avgY}" stroke="#94a3b8" stroke-dasharray="5,4" stroke-width="1.5" />
          <g transform="translate(${margin.left + 10}, ${avgY - 22})">
            <rect x="0" y="0" width="138" height="20" rx="4" fill="var(--bg-card)" stroke="#94a3b8" stroke-width="1.2" opacity="0.96" />
            <text x="69" y="14" text-anchor="middle" font-size="10" font-weight="700" fill="var(--text-muted)">เฉลี่ย: ${metric === 'qty' ? formatInteger(avgVal) + ' ชิ้น' : formatCurrency(avgVal)}</text>
          </g>
          <line x1="${margin.left}" y1="${height - margin.bottom}" x2="${width - margin.right}" y2="${height - margin.bottom}" class="svg-axis-line" />
          ${bars}
        </svg>
      `;
    }

    function renderCalendarGrid(data) {
      const container = document.getElementById('calendarGridContainer');
      const daySales = {};
      let maxDaily = 0;

      data.forEach(x => {
        daySales[x.date] = (daySales[x.date] || 0) + x.revenue;
        if (daySales[x.date] > maxDaily) maxDaily = daySales[x.date];
      });

      // August 2026: Day 1 is Saturday (dayOfWeek = 6 in Sun=0 based)
      // If Monday is col 0, Sat is col 5. Empty cells for Mon..Fri (5 cells)
      let html = '';
      for (let empty = 0; empty < 5; empty++) {
        html += '<div class="cal-day-cell empty"></div>';
      }

      for (let day = 1; day <= 31; day++) {
        const dStr = `2026-08-${String(day).padStart(2, '0')}`;
        const rev = daySales[dStr] || 0;
        const intensity = maxDaily > 0 ? (rev / maxDaily) : 0;
        const bg = intensity > 0 
          ? `rgba(234, 88, 12, ${Math.max(0.15, intensity * 0.9)})` 
          : 'var(--bg-card-subtle)';
        const textColor = intensity > 0.55 ? '#ffffff' : 'var(--text-main)';

        html += `
          <div class="cal-day-cell" style="background: ${bg}; color: ${textColor};" onclick="setDateFilterSingle('${dStr}')" onmousemove="showTooltip(event, '${dStr}<br>รายได้: ${formatCurrency(rev)}')" onmouseleave="hideTooltip()">
            <span style="font-weight: 700;">${day}</span>
            <span style="font-size: 0.65rem;">${rev > 0 ? '฿' + Math.round(rev) : '-'}</span>
          </div>
        `;
      }

      container.innerHTML = html;
    }

    function setDateFilterSingle(dateStr) {
      document.getElementById('filterStartDate').value = dateStr;
      document.getElementById('filterEndDate').value = dateStr;
      state.filters.startDate = dateStr;
      state.filters.endDate = dateStr;
      onFilterChange();
    }

    // --- 9. TAB 5: TRANSACTIONS TABLE & PAGINATION ---
    function renderTxTable(data) {
      const tbody = document.getElementById('txTableBody');
      const search = state.txTable.search.toLowerCase().trim();

      let filtered = data;
      if (search) {
        filtered = data.filter(x => 
          x.id.toLowerCase().includes(search) ||
          x.product.toLowerCase().includes(search) ||
          x.branch.toLowerCase().includes(search) ||
          x.category.toLowerCase().includes(search) ||
          x.date.includes(search)
        );
      }

      const col = state.txTable.sortCol;
      const asc = state.txTable.sortAsc;
      filtered.sort((a, b) => asc ? (a[col] > b[col] ? 1 : -1) : (a[col] < b[col] ? 1 : -1));

      const totalRows = filtered.length;
      const pageSize = state.txTable.pageSize;
      const totalPages = Math.ceil(totalRows / pageSize) || 1;
      if (state.txTable.page > totalPages) state.txTable.page = totalPages;

      const startIdx = (state.txTable.page - 1) * pageSize;
      const pageRows = filtered.slice(startIdx, startIdx + pageSize);

      if (pageRows.length === 0) {
        tbody.innerHTML = '<tr><td colspan="14" class="text-center" style="padding: 30px; color: var(--text-muted);">ไม่พบรายการที่ค้นหา</td></tr>';
      } else {
        tbody.innerHTML = pageRows.map(r => {
          const batch = BATCH_METADATA.find(b => b.id === r.batchId);
          const batchName = batch ? batch.name : (r.batchId || 'ชุดเริ่มต้น');
          const shortName = batchName.length > 22 ? batchName.slice(0, 20) + '…' : batchName;
          return `
            <tr>
              <td style="font-weight: 700; color: var(--primary-blue);">${r.id}</td>
              <td>${r.date}</td>
              <td>${r.dayOfWeek.replace('วัน', '')}</td>
              <td>${r.branch}</td>
              <td style="font-weight: 600;">${r.product}</td>
              <td>${r.category}</td>
              <td class="text-right">${formatInteger(r.qty)}</td>
              <td class="text-right">฿${r.price.toFixed(2)}</td>
              <td class="text-right">฿${r.cost.toFixed(2)}</td>
              <td class="text-right" style="font-weight: 700;">${formatCurrency(r.revenue)}</td>
              <td class="text-right" style="color: var(--accent-emerald); font-weight: 600;">${formatCurrency(r.gross_profit)}</td>
              <td class="text-right">${formatPercent(r.margin)}</td>
              <td><span class="dm-batch-badge" title="${batchName}">${shortName}</span></td>
              <td class="text-center">
                <button class="btn btn-danger btn-xs" onclick="deleteIndividualRecord('${r.id}')" title="ลบรายการนี้" style="padding: 2px 7px;">🗑️</button>
              </td>
            </tr>
          `;
        }).join('');
      }

      // Update Pagination info
      document.getElementById('txPaginationInfo').textContent = 
        `กำลังแสดง ${totalRows > 0 ? startIdx + 1 : 0}–${Math.min(startIdx + pageSize, totalRows)} จาก ${totalRows} รายการ`;

      // Render pagination buttons
      const nav = document.getElementById('txPageNav');
      let navHtml = `
        <button onclick="goToPage(1)" ${state.txTable.page === 1 ? 'disabled' : ''}>« แรก</button>
        <button onclick="goToPage(${state.txTable.page - 1})" ${state.txTable.page === 1 ? 'disabled' : ''}>‹ ก่อน</button>
      `;
      for (let p = 1; p <= totalPages; p++) {
        if (p === 1 || p === totalPages || (p >= state.txTable.page - 1 && p <= state.txTable.page + 1)) {
          navHtml += `<button class="${p === state.txTable.page ? 'active' : ''}" onclick="goToPage(${p})">${p}</button>`;
        } else if (p === state.txTable.page - 2 || p === state.txTable.page + 2) {
          navHtml += '<span style="padding: 0 4px;">...</span>';
        }
      }
      navHtml += `
        <button onclick="goToPage(${state.txTable.page + 1})" ${state.txTable.page === totalPages ? 'disabled' : ''}>ถัดไป ›</button>
        <button onclick="goToPage(${totalPages})" ${state.txTable.page === totalPages ? 'disabled' : ''}>ท้าย »</button>
      `;
      nav.innerHTML = navHtml;
    }

    function handleTxSearch() {
      state.txTable.search = document.getElementById('txSearchInput').value;
      state.txTable.page = 1;
      renderTxTable(getFilteredData());
    }

    function changePageSize(val) {
      state.txTable.pageSize = Number(val);
      state.txTable.page = 1;
      renderTxTable(getFilteredData());
    }

    function goToPage(p) {
      state.txTable.page = p;
      renderTxTable(getFilteredData());
    }

    function sortTxTable(col) {
      if (state.txTable.sortCol === col) state.txTable.sortAsc = !state.txTable.sortAsc;
      else { state.txTable.sortCol = col; state.txTable.sortAsc = true; }
      renderTxTable(getFilteredData());
    }

    // Export CSV with UTF-8 BOM
    function exportFilteredCSV() {
      const data = getFilteredData();
      let csv = '\uFEFF'; // BOM for Excel Thai support
      csv += 'รหัสรายการ,วันที่,วันในสัปดาห์,สาขา,สินค้า,หมวดหมู่,จำนวนขาย (หน่วย),ราคาขายต่อหน่วย (บาท),ต้นทุนต่อหน่วย (บาท),รายได้ (บาท),กำไรขั้นต้น (บาท),อัตรากำไรขั้นต้น,กลุ่มชุดข้อมูล\n';

      data.forEach(r => {
        const batch = BATCH_METADATA.find(b => b.id === r.batchId);
        const batchName = batch ? batch.name : (r.batchId || '-');
        csv += `"${r.id}","${r.date}","${r.dayOfWeek}","${r.branch}","${r.product}","${r.category}",${r.qty},${r.price},${r.cost},${r.revenue},${r.gross_profit},${r.margin.toFixed(4)},"${batchName}"\n`;
      });

      const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
      const url = URL.createObjectURL(blob);
      const link = document.createElement('a');
      link.setAttribute('href', url);
      link.setAttribute('download', `sales_export_${new Date().toISOString().slice(0, 10)}.csv`);
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    }

    // --- 10. WHAT-IF PROFIT SIMULATOR ---
    function toggleSimulator() {
      const el = document.getElementById('simulatorSection');
      el.style.display = (el.style.display === 'none') ? 'block' : 'none';
      if (el.style.display === 'block') updateSimulation();
    }

    function updateSimulation() {
      const pSlider = document.getElementById('simPriceSlider');
      const cSlider = document.getElementById('simCostSlider');
      if (!pSlider || !cSlider) return;

      const pPct = Number(pSlider.value);
      const cPct = Number(cSlider.value);

      document.getElementById('simPriceVal').textContent = (pPct >= 0 ? '+' : '') + pPct + '%';
      document.getElementById('simCostVal').textContent = (cPct >= 0 ? '+' : '') + cPct + '%';

      const data = getFilteredData();
      let baselineRevenue = 0;
      let baselineProfit = 0;
      let simRevenue = 0;
      let simProfit = 0;

      data.forEach(x => {
        baselineRevenue += x.revenue;
        baselineProfit += x.gross_profit;

        const newPrice = x.price * (1 + (pPct / 100));
        const newCost = x.cost * (1 + (cPct / 100));
        simRevenue += x.qty * newPrice;
        simProfit += x.qty * (newPrice - newCost);
      });

      const simMargin = simRevenue > 0 ? (simProfit / simRevenue) : 0;
      const deltaProfit = simProfit - baselineProfit;

      document.getElementById('simProjRevenue').textContent = formatCurrency(simRevenue);
      document.getElementById('simProjProfit').textContent = formatCurrency(simProfit);
      document.getElementById('simProjMargin').textContent = formatPercent(simMargin);

      const deltaEl = document.getElementById('simDeltaProfit');
      deltaEl.textContent = (deltaProfit >= 0 ? '+' : '') + formatCurrency(deltaProfit);
      deltaEl.style.color = deltaProfit >= 0 ? 'var(--accent-emerald)' : 'var(--accent-rose)';
    }

    function resetSimulator() {
      document.getElementById('simPriceSlider').value = 0;
      document.getElementById('simCostSlider').value = 0;
      updateSimulation();
    }

    // --- 11. TOOLTIPS & MODALS ---
    const tooltip = document.getElementById('globalTooltip');
    function showTooltip(e, text) {
      tooltip.innerHTML = text;
      tooltip.style.display = 'block';
      const x = e.pageX + 14;
      const y = e.pageY + 14;
      tooltip.style.left = x + 'px';
      tooltip.style.top = y + 'px';
    }
    function hideTooltip() {
      tooltip.style.display = 'none';
    }

    function openAuditModal() {
      document.getElementById('auditModal').classList.add('active');
    }
    function closeAuditModal() {
      document.getElementById('auditModal').classList.remove('active');
    }

    // --- 12. THEME & PRINT ---
    function initThemeAndPrint() {
      const btnTheme = document.getElementById('btnThemeToggle');
      btnTheme.addEventListener('click', () => {
        const isDark = document.body.getAttribute('data-theme') === 'dark';
        if (isDark) {
          document.body.removeAttribute('data-theme');
          btnTheme.textContent = '🌙 สลับธีม';
        } else {
          document.body.setAttribute('data-theme', 'dark');
          btnTheme.textContent = '☀️ ธีมสว่าง';
        }
        // Re-render charts to adjust text color
        onFilterChange();
      });

      document.getElementById('btnPrint').addEventListener('click', () => window.print());
      document.getElementById('btnDownloadCSV').addEventListener('click', exportFilteredCSV);
      document.getElementById('btnAuditReport').addEventListener('click', openAuditModal);
    }

    // ==========================================
    // 13. DATA MANAGEMENT & MULTI-BATCH CONTROLLER
    // ==========================================

    let currentParsedPreview = null;
    const pruneState = {
      page: 1,
      pageSize: 25,
      search: '',
      batchFilter: 'all',
      yearFilter: 'all',
      selectedIds: new Set()
    };

    function normalizeHeaderName(header) {
      if (!header) return null;
      const h = String(header).toLowerCase().replace(/[\s_\-\(\)\/]/g, '');
      if (/^(id|รหัส|รหัสรายการ|transactionid|no|orderid)$/.test(h)) return 'id';
      if (/^(date|วันที่|transdate|saledate|วัน)$/.test(h)) return 'date';
      if (/^(branch|สาขา|branchname|ร้าน|สถานที่|location)$/.test(h)) return 'branch';
      if (/^(product|สินค้า|productname|ชื่อสินค้า|item)$/.test(h)) return 'product';
      if (/^(category|หมวดหมู่|หมวด|group|type|ประเภท)$/.test(h)) return 'category';
      if (/^(qty|จำนวน|จำนวนขาย|quantity|units|ชิ้น|จำนวนชิ้น)$/.test(h)) return 'qty';
      if (/^(price|ราคา|ราคาขาย|unitprice|ราคาต่อหน่วย|ราคาขายต่อหน่วย)$/.test(h)) return 'price';
      if (/^(cost|ต้นทุน|unitcost|ต้นทุนต่อหน่วย|ต้นทุนหน่วย)$/.test(h)) return 'cost';
      return null;
    }

    function normalizeDateString(raw) {
      if (!raw) return null;
      const s = String(raw).trim();
      // Excel serial date e.g. 46235
      if (/^\d{5}$/.test(s)) {
        const serial = parseInt(s, 10);
        const utcDays = serial - 25569;
        const d = new Date(utcDays * 86400 * 1000);
        return d.toISOString().slice(0, 10);
      }
      // ISO YYYY-MM-DD
      const mIso = s.match(/^(\d{4})[-\/.](\d{1,2})[-\/.](\d{1,2})/);
      if (mIso) {
        let year = parseInt(mIso[1], 10);
        if (year > 2400) year -= 543; // Buddhist era to Gregorian
        const month = String(parseInt(mIso[2], 10)).padStart(2, '0');
        const day = String(parseInt(mIso[3], 10)).padStart(2, '0');
        return `${year}-${month}-${day}`;
      }
      // DD-MM-YYYY or DD/MM/YYYY
      const mDmy = s.match(/^(\d{1,2})[-\/.](\d{1,2})[-\/.](\d{4})/);
      if (mDmy) {
        let year = parseInt(mDmy[3], 10);
        if (year > 2400) year -= 543;
        const month = String(parseInt(mDmy[2], 10)).padStart(2, '0');
        const day = String(parseInt(mDmy[1], 10)).padStart(2, '0');
        return `${year}-${month}-${day}`;
      }
      return null;
    }

    function parseCSV(text) {
      const lines = text.replace(/\r\n/g, '\n').replace(/\r/g, '\n').split('\n').filter(l => l.trim().length > 0);
      if (lines.length < 2) return [];

      let delimiter = ',';
      if (lines[0].includes('\t')) delimiter = '\t';
      else if (lines[0].includes(';') && !lines[0].includes(',')) delimiter = ';';

      function splitRow(line) {
        const result = [];
        let current = '';
        let inQuotes = false;
        for (let i = 0; i < line.length; i++) {
          const char = line[i];
          if (char === '"') {
            if (inQuotes && line[i + 1] === '"') {
              current += '"';
              i++;
            } else {
              inQuotes = !inQuotes;
            }
          } else if (char === delimiter && !inQuotes) {
            result.push(current.trim());
            current = '';
          } else {
            current += char;
          }
        }
        result.push(current.trim());
        return result;
      }

      const rawHeaders = splitRow(lines[0]).map(h => h.replace(/^["']|["']$/g, '').trim());
      const normalizedHeaders = rawHeaders.map(normalizeHeaderName);

      const rows = [];
      for (let i = 1; i < lines.length; i++) {
        const values = splitRow(lines[i]).map(v => v.replace(/^["']|["']$/g, '').trim());
        if (values.length === 0 || (values.length === 1 && !values[0])) continue;
        const obj = {};
        normalizedHeaders.forEach((key, colIdx) => {
          if (key) obj[key] = values[colIdx] !== undefined ? values[colIdx] : '';
        });
        rows.push(obj);
      }
      return rows;
    }

    function parseJSON(text) {
      const parsed = JSON.parse(text);
      if (!Array.isArray(parsed)) throw new Error('ข้อมูล JSON ต้องเป็น Array ของรายการข้อมูล');
      return parsed.map(item => {
        const obj = {};
        Object.keys(item).forEach(k => {
          const normKey = normalizeHeaderName(k);
          if (normKey) obj[normKey] = item[k];
        });
        return obj;
      });
    }

    function createRecordFromParsed(raw, batchId, fallbackIdx) {
      const dateStr = normalizeDateString(raw.date);
      if (!dateStr) return null;
      const d = new Date(dateStr + 'T00:00:00');
      if (isNaN(d.getTime())) return null;

      const dayOfWeek = THAI_DAYS[d.getDay()];
      const qty = parseFloat(String(raw.qty).replace(/,/g, '')) || 0;
      const price = parseFloat(String(raw.price).replace(/,/g, '')) || 0;
      const cost = parseFloat(String(raw.cost).replace(/,/g, '')) || 0;
      if (qty <= 0) return null;

      const revenue = qty * price;
      const profit = qty * (price - cost);
      const margin = revenue > 0 ? (profit / revenue) : 0;
      const year = dateStr.slice(0, 4);

      const id = raw.id ? String(raw.id).trim() : `IMP_${Date.now().toString(36).toUpperCase()}_${String(fallbackIdx + 1).padStart(3, '0')}`;

      return {
        id: id,
        date: dateStr,
        dayOfWeek: dayOfWeek,
        dayIndex: d.getDay(),
        branch: (raw.branch || 'สาขาทั่วไป').trim(),
        product: (raw.product || 'สินค้าทั่วไป').trim(),
        category: (raw.category || 'หมวดหมู่อื่น').trim(),
        qty: qty,
        price: price,
        cost: cost,
        revenue: revenue,
        gross_profit: profit,
        margin: margin,
        batchId: batchId,
        year: year
      };
    }

    function processParsedRecords(rawRows, sourceName) {
      if (!rawRows || rawRows.length === 0) {
        alert('ไม่พบแถวข้อมูลที่สามารถนำเข้าได้ กรุณาตรวจสอบรูปแบบไฟล์');
        return;
      }

      const tempBatchId = 'temp_' + Date.now();
      const validRecords = [];
      let invalidCount = 0;

      rawRows.forEach((r, idx) => {
        const rec = createRecordFromParsed(r, tempBatchId, idx);
        if (rec) validRecords.push(rec);
        else invalidCount++;
      });

      if (validRecords.length === 0) {
        alert('ไม่สามารถประมวลผลข้อมูลได้: ไม่มีแถวใดที่มีข้อมูลวันที่ และจำนวนขายที่ถูกต้อง');
        return;
      }

      currentParsedPreview = {
        rows: validRecords,
        validCount: validRecords.length,
        invalidCount: invalidCount,
        sourceName: sourceName
      };

      // Show preview
      const previewBox = document.getElementById('dmPreviewBox');
      const statusEl = document.getElementById('dmValidationStatus');
      const tbody = document.getElementById('dmPreviewTableBody');

      statusEl.innerHTML = `
        <div style="background: rgba(5, 150, 105, 0.1); border: 1px solid rgba(5, 150, 105, 0.3); border-radius: var(--radius-sm); padding: 10px 14px; color: var(--accent-emerald); font-size: 0.88rem; font-weight: 600;">
          ✔ ตรวจพบข้อมูลทั้งหมด <strong>${formatInteger(validRecords.length)}</strong> แถวที่สมบูรณ์ 
          ${invalidCount > 0 ? `<span style="color: var(--accent-amber); font-weight: 500;">(ข้ามแถวว่างหรือไม่สมบูรณ์ ${invalidCount} แถว)</span>` : ''}
          • พร้อมนำเข้าสู่ระบบ
        </div>
      `;

      tbody.innerHTML = validRecords.slice(0, 5).map(r => `
        <tr>
          <td style="font-weight: 700; color: var(--primary-blue);">${r.id}</td>
          <td>${r.date}</td>
          <td>${r.dayOfWeek.replace('วัน', '')}</td>
          <td>${r.branch}</td>
          <td style="font-weight: 600;">${r.product}</td>
          <td>${r.category}</td>
          <td class="text-right">${formatInteger(r.qty)}</td>
          <td class="text-right">฿${r.price.toFixed(2)}</td>
          <td class="text-right">฿${r.cost.toFixed(2)}</td>
          <td class="text-right" style="font-weight: 700;">${formatCurrency(r.revenue)}</td>
          <td class="text-right" style="color: var(--accent-emerald); font-weight: 600;">${formatCurrency(r.gross_profit)}</td>
        </tr>
      `).join('');

      previewBox.style.display = 'block';
    }

    function cancelImportPreview() {
      currentParsedPreview = null;
      document.getElementById('dmPreviewBox').style.display = 'none';
      document.getElementById('dmFileInput').value = '';
      document.getElementById('dmPasteInput').value = '';
    }

    function confirmImport() {
      if (!currentParsedPreview || currentParsedPreview.rows.length === 0) {
        alert('ไม่มีข้อมูลที่พร้อมนำเข้า');
        return;
      }

      const batchId = 'batch_' + Date.now();
      const customName = document.getElementById('dmBatchNameInput').value.trim();
      const finalName = customName || currentParsedPreview.sourceName || `ชุดข้อมูลนำเข้า ${new Date().toLocaleDateString('th-TH')}`;

      // Set actual batchId on records
      const recordsToImport = currentParsedPreview.rows.map(r => ({ ...r, batchId: batchId }));
      const dates = recordsToImport.map(r => r.date).sort();
      const totalRev = recordsToImport.reduce((sum, r) => sum + r.revenue, 0);

      const newBatch = {
        id: batchId,
        name: finalName,
        uploadedAt: new Date().toISOString().replace('T', ' ').slice(0, 19),
        fileName: currentParsedPreview.sourceName,
        recordCount: recordsToImport.length,
        totalRevenue: totalRev,
        minDate: dates[0] || '',
        maxDate: dates[dates.length - 1] || '',
        years: Array.from(new Set(recordsToImport.map(r => r.year)))
      };

      const importMode = document.querySelector('input[name="dmImportMode"]:checked')?.value || 'append';

      if (importMode === 'replace') {
        if (!confirm('คำเตือน: คุณเลือกโหมด "ล้างและแทนที่ทั้งหมด" ข้อมูลเดิมทั้งหมดจะถูกลบและแทนที่ด้วยชุดข้อมูลนี้ ยืนยันหรือไม่?')) {
          return;
        }
        SALES_DATA = recordsToImport;
        BATCH_METADATA = [newBatch];
      } else {
        SALES_DATA = [...SALES_DATA, ...recordsToImport];
        BATCH_METADATA.push(newBatch);
      }

      saveDatasetToStorage();
      recomputeDimensions(false);
      cancelImportPreview();
      document.getElementById('dmBatchNameInput').value = '';

      onFilterChange();
      renderDataManagerTab();

      alert(`✅ นำเข้าข้อมูลสำเร็จเรียบร้อยแล้ว!\n• เพิ่มข้อมูล: ${formatInteger(recordsToImport.length)} รายการ\n• กลุ่มชุดข้อมูล: "${finalName}"\n• ยอดขายรวมของกลุ่ม: ${formatCurrency(totalRev)}`);
    }

    function setImportInputMode(mode) {
      const btnUpload = document.getElementById('dmTabUploadFile');
      const btnPaste = document.getElementById('dmTabPasteText');
      const areaUpload = document.getElementById('dmUploadFileArea');
      const areaPaste = document.getElementById('dmPasteTextArea');

      if (mode === 'paste') {
        btnPaste.classList.replace('btn-outline', 'btn-primary');
        btnUpload.classList.replace('btn-primary', 'btn-outline');
        areaPaste.style.display = 'block';
        areaUpload.style.display = 'none';
      } else {
        btnUpload.classList.replace('btn-outline', 'btn-primary');
        btnPaste.classList.replace('btn-primary', 'btn-outline');
        areaUpload.style.display = 'block';
        areaPaste.style.display = 'none';
      }
    }

    function handleFileSelect(e) {
      const file = e.target.files[0];
      if (!file) return;

      const nameWithoutExt = file.name.replace(/\.[^/.]+$/, '');
      const batchInput = document.getElementById('dmBatchNameInput');
      if (batchInput && !batchInput.value.trim()) {
        batchInput.value = nameWithoutExt;
      }

      const reader = new FileReader();
      reader.onload = function(evt) {
        const text = evt.target.result;
        try {
          if (file.name.toLowerCase().endsWith('.json')) {
            const rawRows = parseJSON(text);
            processParsedRecords(rawRows, file.name);
          } else {
            const rawRows = parseCSV(text);
            processParsedRecords(rawRows, file.name);
          }
        } catch (err) {
          alert('เกิดข้อผิดพลาดในการอ่านไฟล์: ' + err.message);
        }
      };
      reader.readAsText(file, 'UTF-8');
    }

    let pasteDebounceTimer = null;
    function handlePasteInput() {
      clearTimeout(pasteDebounceTimer);
      pasteDebounceTimer = setTimeout(() => {
        const text = document.getElementById('dmPasteInput').value.trim();
        if (!text) return;
        try {
          if (text.startsWith('[') || text.startsWith('{')) {
            const raw = parseJSON(text);
            processParsedRecords(raw, 'ข้อมูลคัดลอก JSON');
          } else {
            const raw = parseCSV(text);
            processParsedRecords(raw, 'ข้อมูลคัดลอกจาก Excel');
          }
        } catch (err) {
          alert('ไม่สามารถอ่านข้อมูลที่วางได้: ' + err.message);
        }
      }, 300);
    }

    function initDataManagerEvents() {
      const dropZone = document.getElementById('dmDropZone');
      if (!dropZone) return;

      ['dragenter', 'dragover'].forEach(eventName => {
        dropZone.addEventListener(eventName, (e) => {
          e.preventDefault();
          e.stopPropagation();
          dropZone.classList.add('dragover');
        }, false);
      });

      ['dragleave', 'drop'].forEach(eventName => {
        dropZone.addEventListener(eventName, (e) => {
          e.preventDefault();
          e.stopPropagation();
          dropZone.classList.remove('dragover');
        }, false);
      });

      dropZone.addEventListener('drop', (e) => {
        const dt = e.dataTransfer;
        const files = dt.files;
        if (files && files.length > 0) {
          const input = document.getElementById('dmFileInput');
          input.files = files;
          handleFileSelect({ target: { files: files } });
        }
      }, false);
    }

    function renderDataManagerTab() {
      // 1. Top Summary Stats
      const totalRecords = SALES_DATA.length;
      const totalBatches = BATCH_METADATA.length;
      const years = Array.from(new Set(SALES_DATA.map(x => x.year))).sort();
      const dates = SALES_DATA.map(x => x.date).sort();
      const minDate = dates[0] || '-';
      const maxDate = dates[dates.length - 1] || '-';

      const totalRecEl = document.getElementById('dmTotalRecords');
      if (totalRecEl) totalRecEl.textContent = `${formatInteger(totalRecords)} แถว`;

      const totalBatchEl = document.getElementById('dmTotalBatches');
      if (totalBatchEl) totalBatchEl.textContent = `${totalBatches} กลุ่ม`;

      const yearRangeEl = document.getElementById('dmYearRange');
      if (yearRangeEl) {
        if (years.length === 0) yearRangeEl.textContent = 'ไม่มีข้อมูล';
        else yearRangeEl.textContent = years.map(y => `${y} (${Number(y) + 543})`).join(', ');
      }

      const dateRangeSubEl = document.getElementById('dmDateRangeSub');
      if (dateRangeSubEl) dateRangeSubEl.textContent = totalRecords > 0 ? `${minDate} ถึง ${maxDate}` : 'ไม่มีข้อมูล';

      const storageEl = document.getElementById('dmStorageUsed');
      if (storageEl) {
        try {
          const dataBytes = (localStorage.getItem(STORAGE_KEY_DATA) || '').length;
          const batchBytes = (localStorage.getItem(STORAGE_KEY_BATCHES) || '').length;
          const kb = ((dataBytes + batchBytes) / 1024).toFixed(1);
          storageEl.textContent = `~${kb} KB`;
        } catch (e) {
          storageEl.textContent = 'พร้อมใช้งาน';
        }
      }

      // 2. Year-based Pruner Cards ("ลดการสะสมข้อมูลเยอะเกินไปของแต่ละปีเป็นต้น")
      const yearContainer = document.getElementById('dmYearPruneContainer');
      if (yearContainer) {
        if (years.length === 0) {
          yearContainer.innerHTML = '<div style="color: var(--text-muted); font-size: 0.85rem;">ไม่มีข้อมูลในระบบ</div>';
        } else {
          yearContainer.innerHTML = years.map(y => {
            const yRecords = SALES_DATA.filter(r => r.year === y);
            const count = yRecords.length;
            const rev = yRecords.reduce((sum, r) => sum + r.revenue, 0);
            const profit = yRecords.reduce((sum, r) => sum + r.gross_profit, 0);
            return `
              <div class="dm-year-card">
                <div class="dm-year-info">
                  <h4>🗓️ ปี ${y} <span style="font-weight: 500; font-size: 0.8rem; color: var(--text-muted);">(พ.ศ. ${Number(y) + 543})</span></h4>
                  <div class="dm-year-meta">
                    <strong>${formatInteger(count)}</strong> รายการ • ยอดขาย <strong>${formatCurrency(rev)}</strong><br>
                    กำไรขั้นต้น ${formatCurrency(profit)}
                  </div>
                </div>
                <div>
                  <button class="btn btn-danger btn-xs" onclick="deleteYearRecords('${y}')" title="ล้างข้อมูลปีนี้เพื่อลดการสะสมข้อมูล">
                    🗑️ ล้างข้อมูลปีนี้
                  </button>
                </div>
              </div>
            `;
          }).join('');
        }
      }

      // 3. Batches History Table ("แบ่งว่าอันนี้เข้ามาตอนไหนแบ่งเป็นกลุ่ม")
      const batchTbody = document.getElementById('dmBatchesTableBody');
      if (batchTbody) {
        if (BATCH_METADATA.length === 0) {
          batchTbody.innerHTML = '<tr><td colspan="8" class="text-center" style="padding: 24px; color: var(--text-muted);">ไม่มีกลุ่มข้อมูลที่บันทึกไว้</td></tr>';
        } else {
          batchTbody.innerHTML = BATCH_METADATA.map(b => {
            const actualRows = SALES_DATA.filter(r => r.batchId === b.id);
            const count = actualRows.length;
            const totalRev = actualRows.reduce((sum, r) => sum + r.revenue, 0);
            const dateSpan = actualRows.length > 0 
              ? `${actualRows.map(r=>r.date).sort()[0]} ~ ${actualRows.map(r=>r.date).sort()[actualRows.length-1]}`
              : (b.minDate ? `${b.minDate} ~ ${b.maxDate}` : '-');
            const yearsText = Array.from(new Set(actualRows.map(r => r.year))).join(', ') || '-';

            return `
              <tr>
                <td style="font-weight: 700; color: var(--text-main);">${b.name}</td>
                <td style="font-size: 0.78rem; color: var(--text-muted);">${b.uploadedAt || '-'}</td>
                <td><span class="dm-batch-badge">${b.fileName || 'ระบบ'}</span></td>
                <td style="font-size: 0.78rem;">${dateSpan}</td>
                <td>${yearsText}</td>
                <td class="text-right" style="font-weight: 700;">${formatInteger(count)}</td>
                <td class="text-right" style="font-weight: 700; color: var(--primary-blue);">${formatCurrency(totalRev)}</td>
                <td class="text-center">
                  <div style="display: flex; gap: 4px; justify-content: center;">
                    <button class="btn btn-outline btn-xs" onclick="exportBatchCSV('${b.id}')" title="ดาวน์โหลดเฉพาะกลุ่มนี้เป็น CSV">
                      📥 CSV
                    </button>
                    <button class="btn btn-danger btn-xs" onclick="deleteBatch('${b.id}')" title="ลบทั้งไฟล์กลุ่มที่อัปโหลดนี้">
                      🗑️ ลบทั้งกลุ่ม
                    </button>
                  </div>
                </td>
              </tr>
            `;
          }).join('');
        }
      }

      // 4. Update Prune Filter Dropdowns
      const batchSelect = document.getElementById('dmPruneBatchFilter');
      if (batchSelect) {
        const curBatch = pruneState.batchFilter;
        batchSelect.innerHTML = '<option value="all">ทุกกลุ่มชุดข้อมูล (All Batches)</option>' + 
          BATCH_METADATA.map(b => `<option value="${b.id}" ${curBatch === b.id ? 'selected' : ''}>${b.name}</option>`).join('');
      }

      const yearSelect = document.getElementById('dmPruneYearFilter');
      if (yearSelect) {
        const curYear = pruneState.yearFilter;
        yearSelect.innerHTML = '<option value="all">ทุกปี (All Years)</option>' + 
          years.map(y => `<option value="${y}" ${curYear === y ? 'selected' : ''}>ปี ${y} (พ.ศ. ${Number(y) + 543})</option>`).join('');
      }

      // 5. Render Prune Table
      renderPruneTable();
    }

    function renderPruneTable() {
      const search = (document.getElementById('dmPruneSearch')?.value || '').trim().toLowerCase();
      const batchFilter = document.getElementById('dmPruneBatchFilter')?.value || 'all';
      const yearFilter = document.getElementById('dmPruneYearFilter')?.value || 'all';

      pruneState.search = search;
      pruneState.batchFilter = batchFilter;
      pruneState.yearFilter = yearFilter;

      let filtered = SALES_DATA.filter(r => {
        if (batchFilter !== 'all' && r.batchId !== batchFilter) return false;
        if (yearFilter !== 'all' && r.year !== yearFilter) return false;
        if (search) {
          const match = r.id.toLowerCase().includes(search) ||
                        r.product.toLowerCase().includes(search) ||
                        r.branch.toLowerCase().includes(search) ||
                        r.category.toLowerCase().includes(search) ||
                        r.date.includes(search);
          if (!match) return false;
        }
        return true;
      });

      const totalRows = filtered.length;
      const pageSize = pruneState.pageSize;
      const totalPages = Math.ceil(totalRows / pageSize) || 1;
      if (pruneState.page > totalPages) pruneState.page = totalPages;

      const startIdx = (pruneState.page - 1) * pageSize;
      const pageRows = filtered.slice(startIdx, startIdx + pageSize);

      const tbody = document.getElementById('dmPruneTableBody');
      if (tbody) {
        if (pageRows.length === 0) {
          tbody.innerHTML = '<tr><td colspan="11" class="text-center" style="padding: 24px; color: var(--text-muted);">ไม่พบรายการตามเงื่อนไข</td></tr>';
        } else {
          tbody.innerHTML = pageRows.map(r => {
            const batch = BATCH_METADATA.find(b => b.id === r.batchId);
            const batchName = batch ? batch.name : (r.batchId || '-');
            const shortName = batchName.length > 18 ? batchName.slice(0, 16) + '…' : batchName;
            const isChecked = pruneState.selectedIds.has(r.id);

            return `
              <tr>
                <td style="text-align: center;">
                  <input type="checkbox" ${isChecked ? 'checked' : ''} onchange="toggleSelectPruneRow('${r.id}', this.checked)">
                </td>
                <td style="font-weight: 700; color: var(--primary-blue);">${r.id}</td>
                <td>${r.date}</td>
                <td>${r.branch}</td>
                <td style="font-weight: 600;">${r.product}</td>
                <td>${r.category}</td>
                <td class="text-right">${formatInteger(r.qty)}</td>
                <td class="text-right">฿${r.price.toFixed(2)}</td>
                <td class="text-right" style="font-weight: 700;">${formatCurrency(r.revenue)}</td>
                <td><span class="dm-batch-badge" title="${batchName}">${shortName}</span></td>
                <td class="text-center">
                  <button class="btn btn-danger btn-xs" onclick="deleteIndividualRecord('${r.id}')" title="ลบเฉพาะรายการนี้" style="padding: 2px 7px;">
                    🗑️
                  </button>
                </td>
              </tr>
            `;
          }).join('');
        }
      }

      // Update Select All Checkbox
      const selectAllCb = document.getElementById('dmSelectAllRows');
      if (selectAllCb) {
        const allOnPageSelected = pageRows.length > 0 && pageRows.every(r => pruneState.selectedIds.has(r.id));
        selectAllCb.checked = allOnPageSelected;
      }

      // Update Pagination Bar
      const infoEl = document.getElementById('dmPrunePaginationInfo');
      if (infoEl) {
        infoEl.textContent = `กำลังแสดง ${totalRows > 0 ? startIdx + 1 : 0}–${Math.min(startIdx + pageSize, totalRows)} จาก ${formatInteger(totalRows)} รายการ`;
      }

      const navEl = document.getElementById('dmPrunePageNav');
      if (navEl) {
        let navHtml = `
          <button onclick="goToPrunePage(1)" ${pruneState.page === 1 ? 'disabled' : ''}>« แรก</button>
          <button onclick="goToPrunePage(${pruneState.page - 1})" ${pruneState.page === 1 ? 'disabled' : ''}>‹ ก่อน</button>
        `;
        for (let p = 1; p <= totalPages; p++) {
          if (p === 1 || p === totalPages || (p >= pruneState.page - 1 && p <= pruneState.page + 1)) {
            navHtml += `<button class="${p === pruneState.page ? 'active' : ''}" onclick="goToPrunePage(${p})">${p}</button>`;
          } else if (p === pruneState.page - 2 || p === pruneState.page + 2) {
            navHtml += '<span style="padding: 0 4px;">...</span>';
          }
        }
        navHtml += `
          <button onclick="goToPrunePage(${pruneState.page + 1})" ${pruneState.page === totalPages ? 'disabled' : ''}>ถัดไป ›</button>
          <button onclick="goToPrunePage(${totalPages})" ${pruneState.page === totalPages ? 'disabled' : ''}>ท้าย »</button>
        `;
        navEl.innerHTML = navHtml;
      }

      updateBulkDeleteButton();
    }

    function goToPrunePage(p) {
      pruneState.page = p;
      renderPruneTable();
    }

    function toggleSelectPruneRow(id, isChecked) {
      if (isChecked) pruneState.selectedIds.add(id);
      else pruneState.selectedIds.delete(id);
      updateBulkDeleteButton();
    }

    function toggleSelectAllPrune(isChecked) {
      const search = pruneState.search;
      const batchFilter = pruneState.batchFilter;
      const yearFilter = pruneState.yearFilter;

      const filtered = SALES_DATA.filter(r => {
        if (batchFilter !== 'all' && r.batchId !== batchFilter) return false;
        if (yearFilter !== 'all' && r.year !== yearFilter) return false;
        if (search) {
          const match = r.id.toLowerCase().includes(search) ||
                        r.product.toLowerCase().includes(search) ||
                        r.branch.toLowerCase().includes(search) ||
                        r.category.toLowerCase().includes(search) ||
                        r.date.includes(search);
          if (!match) return false;
        }
        return true;
      });

      const pageSize = pruneState.pageSize;
      const startIdx = (pruneState.page - 1) * pageSize;
      const pageRows = filtered.slice(startIdx, startIdx + pageSize);

      pageRows.forEach(r => {
        if (isChecked) pruneState.selectedIds.add(r.id);
        else pruneState.selectedIds.delete(r.id);
      });

      renderPruneTable();
    }

    function updateBulkDeleteButton() {
      const btn = document.getElementById('btnBulkDelete');
      const countEl = document.getElementById('dmSelectedCount');
      if (!btn || !countEl) return;
      const count = pruneState.selectedIds.size;
      countEl.textContent = count;
      btn.style.display = count > 0 ? 'inline-flex' : 'none';
    }

    function deleteSelectedPruneRows() {
      const count = pruneState.selectedIds.size;
      if (count === 0) return;
      if (!confirm(`ยืนยันการลบรายการที่เลือกทั้งหมด ${formatInteger(count)} รายการ?`)) return;

      SALES_DATA = SALES_DATA.filter(r => !pruneState.selectedIds.has(r.id));
      pruneState.selectedIds.clear();

      // Update batches count & cleanup empty batches
      cleanupBatchesMetadata();
      saveDatasetToStorage();
      recomputeDimensions(true);
      onFilterChange();
      renderDataManagerTab();

      alert(`✅ ลบรายการสำเร็จ ${formatInteger(count)} รายการ`);
    }

    function deleteBatch(batchId) {
      const batch = BATCH_METADATA.find(b => b.id === batchId);
      const batchName = batch ? batch.name : batchId;
      const count = SALES_DATA.filter(r => r.batchId === batchId).length;

      if (!confirm(`คุณต้องการลบทั้งกลุ่มชุดข้อมูล:\n"${batchName}"\n(จำนวน ${formatInteger(count)} รายการ) ใช่หรือไม่?`)) {
        return;
      }

      SALES_DATA = SALES_DATA.filter(r => r.batchId !== batchId);
      BATCH_METADATA = BATCH_METADATA.filter(b => b.id !== batchId);
      pruneState.selectedIds.clear();

      saveDatasetToStorage();
      recomputeDimensions(false);
      onFilterChange();
      renderDataManagerTab();

      alert(`✅ ลบกลุ่มชุดข้อมูล "${batchName}" เรียบร้อยแล้ว`);
    }

    function deleteYearRecords(year) {
      const count = SALES_DATA.filter(r => r.year === String(year)).length;
      if (count === 0) {
        alert(`ไม่พบข้อมูลของปี ${year}`);
        return;
      }

      if (!confirm(`ยืนยันการล้างข้อมูลของปี ${year} (พ.ศ. ${Number(year) + 543}) ทั้งหมด ${formatInteger(count)} รายการ?\n\nการดำเนินการนี้จะช่วยลดการสะสมข้อมูลที่มากเกินไปในระบบ`)) {
        return;
      }

      SALES_DATA = SALES_DATA.filter(r => r.year !== String(year));
      pruneState.selectedIds.clear();

      cleanupBatchesMetadata();
      saveDatasetToStorage();
      recomputeDimensions(false);
      onFilterChange();
      renderDataManagerTab();

      alert(`✅ ตัดลบข้อมูลปี ${year} สำเร็จ (${formatInteger(count)} รายการถูกนำออก)`);
    }

    function deleteIndividualRecord(id) {
      const rec = SALES_DATA.find(r => r.id === id);
      if (!rec) return;

      if (!confirm(`ยืนยันการลบรายการขายรหัส ${id} (${rec.product} - ${rec.branch})?`)) {
        return;
      }

      SALES_DATA = SALES_DATA.filter(r => r.id !== id);
      pruneState.selectedIds.delete(id);

      cleanupBatchesMetadata();
      saveDatasetToStorage();
      recomputeDimensions(true);
      onFilterChange();

      if (state.currentTab === 'tabDataManager') renderDataManagerTab();
    }

    function cleanupBatchesMetadata() {
      // Recalculate stats for batches or remove batches with 0 rows
      const activeBatchIds = new Set(SALES_DATA.map(r => r.batchId));
      BATCH_METADATA = BATCH_METADATA.filter(b => activeBatchIds.has(b.id));

      BATCH_METADATA.forEach(b => {
        const bRows = SALES_DATA.filter(r => r.batchId === b.id);
        b.recordCount = bRows.length;
        b.totalRevenue = bRows.reduce((sum, r) => sum + r.revenue, 0);
        b.years = Array.from(new Set(bRows.map(r => r.year)));
        const d = bRows.map(r => r.date).sort();
        b.minDate = d[0] || '';
        b.maxDate = d[d.length - 1] || '';
      });
    }

    function restoreInitialSeedData() {
      if (!confirm('คุณต้องการกู้คืนข้อมูลเริ่มต้น (ชีต Sales 100 รายการเดิม) หรือไม่?\nข้อมูลที่เคยนำเข้าเพิ่มเติมจะถูกรีเซ็ตกลับเป็นค่าโรงงาน')) {
        return;
      }
      try {
        localStorage.removeItem(STORAGE_KEY_DATA);
        localStorage.removeItem(STORAGE_KEY_BATCHES);
      } catch (e) {}

      initDataset();
      pruneState.selectedIds.clear();
      onFilterChange();
      renderDataManagerTab();

      alert('✅ กู้คืนข้อมูลเริ่มต้นของชีต Sales (100 รายการ) สำเร็จแล้ว');
    }

    function clearAllDataPrompt() {
      if (!confirm('⚠️ คำเตือนร้ายแรง: คุณต้องการล้างข้อมูลการขายทั้งหมดในระบบหรือไม่?\nแดชบอร์ดจะว่างเปล่าจนกว่าจะมีการนำเข้าข้อมูลใหม่')) {
        return;
      }
      SALES_DATA = [];
      BATCH_METADATA = [];
      pruneState.selectedIds.clear();

      saveDatasetToStorage();
      recomputeDimensions(false);
      onFilterChange();
      renderDataManagerTab();

      alert('ฐานข้อมูลทั้งหมดถูกล้างเรียบร้อยแล้ว คุณสามารถนำเข้าข้อมูลใหม่หรือคลิกกู้คืนข้อมูลเริ่มต้นได้ตลอดเวลา');
    }

    function exportBatchCSV(batchId) {
      const batch = BATCH_METADATA.find(b => b.id === batchId);
      const batchName = batch ? batch.name : 'batch';
      const rows = SALES_DATA.filter(r => r.batchId === batchId);

      let csv = '\uFEFF';
      csv += 'รหัสรายการ,วันที่,วันในสัปดาห์,สาขา,สินค้า,หมวดหมู่,จำนวนขาย (หน่วย),ราคาขายต่อหน่วย (บาท),ต้นทุนต่อหน่วย (บาท),รายได้ (บาท),กำไรขั้นต้น (บาท),อัตรากำไรขั้นต้น\n';

      rows.forEach(r => {
        csv += `"${r.id}","${r.date}","${r.dayOfWeek}","${r.branch}","${r.product}","${r.category}",${r.qty},${r.price},${r.cost},${r.revenue},${r.gross_profit},${r.margin.toFixed(4)}\n`;
      });

      const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
      const url = URL.createObjectURL(blob);
      const link = document.createElement('a');
      link.setAttribute('href', url);
      link.setAttribute('download', `batch_${batchId}_${new Date().toISOString().slice(0, 10)}.csv`);
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    }

    function downloadSampleTemplate(format) {
      if (format === 'json') {
        const sampleJson = [
          {
            "id": "S101",
            "date": "2026-09-01",
            "branch": "มหาวิทยาลัย",
            "product": "อเมริกาโน",
            "category": "กาแฟ",
            "qty": 18,
            "price": 60.0,
            "cost": 20.0
          },
          {
            "id": "S102",
            "date": "2026-09-01",
            "branch": "สำนักงาน",
            "product": "ชาไทย",
            "category": "เครื่องดื่มอื่น",
            "qty": 12,
            "price": 55.0,
            "cost": 18.0
          },
          {
            "id": "S103",
            "date": "2026-09-02",
            "branch": "ห้างสรรพสินค้า",
            "product": "ครัวซองต์",
            "category": "เบเกอรี",
            "qty": 15,
            "price": 85.0,
            "cost": 60.0
          },
          {
            "id": "S104",
            "date": "2027-01-10",
            "branch": "มหาวิทยาลัย",
            "product": "ลาเต้",
            "category": "กาแฟ",
            "qty": 20,
            "price": 75.0,
            "cost": 28.0
          }
        ];
        const blob = new Blob([JSON.stringify(sampleJson, null, 2)], { type: 'application/json;charset=utf-8;' });
        const url = URL.createObjectURL(blob);
        const link = document.createElement('a');
        link.setAttribute('href', url);
        link.setAttribute('download', 'sales_import_template.json');
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
      } else {
        let csv = '\uFEFF';
        csv += 'รหัสรายการ,วันที่,สาขา,สินค้า,หมวดหมู่,จำนวนขาย,ราคาต่อหน่วย,ต้นทุนต่อหน่วย\n';
        csv += 'S101,2026-09-01,มหาวิทยาลัย,อเมริกาโน,กาแฟ,18,60,20\n';
        csv += 'S102,2026-09-01,สำนักงาน,ชาไทย,เครื่องดื่มอื่น,12,55,18\n';
        csv += 'S103,2026-09-02,ห้างสรรพสินค้า,ครัวซองต์,เบเกอรี,15,85,60\n';
        csv += 'S104,2027-01-10,มหาวิทยาลัย,ลาเต้,กาแฟ,20,75,28\n';
        csv += 'S105,2027-01-11,สำนักงาน,บราวนี,เบเกอรี,14,55,22\n';

        const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
        const url = URL.createObjectURL(blob);
        const link = document.createElement('a');
        link.setAttribute('href', url);
        link.setAttribute('download', 'sales_import_template.csv');
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
      }
    }

    // Expose Data Manager globals
    window.switchTab = switchTab;
    window.setImportInputMode = setImportInputMode;
    window.handleFileSelect = handleFileSelect;
    window.handlePasteInput = handlePasteInput;
    window.cancelImportPreview = cancelImportPreview;
    window.confirmImport = confirmImport;
    window.renderPruneTable = renderPruneTable;
    window.goToPrunePage = goToPrunePage;
    window.toggleSelectAllPrune = toggleSelectAllPrune;
    window.toggleSelectPruneRow = toggleSelectPruneRow;
    window.deleteSelectedPruneRows = deleteSelectedPruneRows;
    window.deleteBatch = deleteBatch;
    window.deleteYearRecords = deleteYearRecords;
    window.deleteIndividualRecord = deleteIndividualRecord;
    window.restoreInitialSeedData = restoreInitialSeedData;
    window.clearAllDataPrompt = clearAllDataPrompt;
    window.exportBatchCSV = exportBatchCSV;
    window.downloadSampleTemplate = downloadSampleTemplate;

    // Initializer
    window.addEventListener('DOMContentLoaded', () => {
      initDataset();
      initFilterPills();
      initThemeAndPrint();
      initDataManagerEvents();
      onFilterChange();

      const filterHeader = document.getElementById('filterHeader');
      if (filterHeader) {
        filterHeader.addEventListener('keydown', (e) => {
          if (e.key === 'Enter' || e.key === ' ') {
            if (e.target && e.target.closest('button, input, select, label, a')) return;
            e.preventDefault();
            toggleFilterPanel();
          }
        });
      }
    });
