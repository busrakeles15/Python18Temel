import sqlite3 as sql
db = sql.connect("DB/IK.sqlite")
cur = db.cursor()

# aranan = input("Kelime Giriniz:")
# sorgu = f"""
# SELECT adi,
#        soyadi
#   FROM personeller where adi = '{aranan}'
# """
sorgu = """
insert into departmanlar
(departman_adi,lokasyon_id)
values ('{dep_adi}',{lokid})
"""

cur.execute(sorgu)
db.commit()
sorgu = """
SELECT *
  FROM departmanlar
 ORDER BY departman_id DESC
 LIMIT 1;
"""
cur.execute(sorgu)
liste = cur.fetchall()
print(*liste,sep="\n")