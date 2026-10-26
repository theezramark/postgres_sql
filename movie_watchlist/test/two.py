import sqlite3

a = sqlite3.connect("shop.db")   # customer A
b = sqlite3.connect("shop.db")   # customer B

a.execute("CREATE TABLE account(name TEXT, balance INTEGER)")
a.execute("INSERT INTO account VALUES ('Anna', 100)")
a.commit()

a.execute("UPDATE account SET balance = 70 WHERE name = 'Anna'")
print("1) a sees:", a.execute("SELECT balance FROM account").fetchone())
a.commit()

print("2) b sees:", b.execute("SELECT balance FROM account").fetchone())

a.rollback()
"""
output is going to be:
1) a sees: (70,)
2) b sees: (70,)
3) b sees: (100,)
"""
print("3) b sees:", b.execute("SELECT balance FROM account").fetchone())

a.close()
b.close()