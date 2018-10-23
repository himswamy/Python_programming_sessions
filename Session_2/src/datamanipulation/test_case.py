# test cases .....

import unittest
import app_pipeline
import logging
import os

class test_app_pipeline(unittest.TestCase):
	file_name = "/Users/himswamy0/Desktop/Python_practice/Session_2/data/flights.csv"
	data = app_pipeline.LoadData()

		
	def expect_exception(exception):
		"""Marks test to expect the specified exception. Call assertRaises internally"""
		def test_decorator(fn):
			def test_decorated(self, *args, **kwargs):
				self.assertRaises(exception, fn, self, *args, **kwargs)
			return test_decorated
		return test_decorator

		
		
	def test_LoadData_Count(self):
		columns_ct=len(self.__class__.data)
		self.assertTrue(len(self.__class__.data) >= 1, msg="The number of rows in the data set is too less")
	
	
	def test_Columns_Count(self):
		datacolumns=[u'FLIGHT_NUMBER', u'TAIL_NUMBER']
		data = self.__class__.data 
		self.assertListEqual(list(data.columns) ,datacolumns, msg="The columns does not match")
		
		
	
	def test_check_nulls(self):
		data= app_pipeline.check_nulls(self.__class__.data)
		nullcount = data.isnull().sum()
		self.assertEqual(nullcount.sum(), 0, "The dataset has null values")
		
	#####@expect_exception(ValueError)
	def test_add_column(self):
		data1= app_pipeline.add_column(self.__class__.data)
		chk_departue_time=data1.DEPARTURE_TIME
		zero_departure =(chk_departue_time == 0).sum()
		self.assertGreater(0,zero_departure,msg="Departure cannot be zero")
	
####Integration test
	def test_file_created(self):
		data = self.__class__.data 
		file='/Users/himswamy0/Desktop/Python_practice/Session_2/data/final_data.csv'
		app_pipeline.write_to_file(data)
		self.assertTrue(os.path.exists(file))
		
		
		
if __name__ == "__main__":
	logger = logging.getLogger("exampleApp")
	logger.setLevel(logging.INFO)
	fh = logging.FileHandler("test.log")
	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	fh.setFormatter(formatter)
	logger.addHandler(fh)
	logger.info("Program started")
	
	unittest.main()
	
