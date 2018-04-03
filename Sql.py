import sqlite3
import measure

class Sql:
	def __init__(self,max_height):
		self.conn=sqlite3.connect('super_water')
		self.ctrl = self.conn.cursor()
		self.maxHeight = max_height
	def createTable(self):
		self.table = "READINGS"
		self.TIME = "TIME"
		self.HEIGHT = "HEIGHT"
		self.PERCENTILE = "PERCENTILE"
		self.ctrl.execute("create table if not exists {tn}({t} date not null primary key,{h} real not null,{p} real not null)"\
		.format(tn=self.table,t=self.TIME,h=self.HEIGHT,p=self.PERCENTILE))
	
	def insertTable(self,height):
		self.height = self.maxHeight - height
		self.percentile = 100 * (float)(self.height) / (float)(self.maxHeight)
		self.ctrl.execute("insert into {tn} values(datetime('now'),{h},{p})"\
		.format(tn=self.table,h=self.height,p=self.percentile))
		self.conn.commit()
	def select_tb(self):
		self.ctrl.execute("select * from READINGS order by rowid desc limit 1")
		for self.row in self.ctrl:
			self.x=self.row[1]
			self.y=self.row[2]
		return self.x
	
	def update_tb(self,h):
		self.height = max_height - height
		self.percentile = 100 * (float)(self.height) / (float)(self.maxHeight)
		self.ctrl.execute("update {tn} SET {t}=datetime('now'),{h}={h_val},{p}={p_val} order by rowid desc limit 1"\
			.format(tn=self.table,t=self.TIME,h=self.HEIGHT,p=self.PERCENTILE,h_val=self.height,p_val=self.percentile))
		self.conn.commit()
	
	def __del__(self):
		self.conn.close()
		
def measureHeight():
	return float(raw_input("Enter the height"))

if __name__ == "__main__":
	t=measure.tank()
	t.select_max()
	s=Sql(t.height)
	s.createTable()
	s.insertTable(measureHeight())
	print s.select_tb()
