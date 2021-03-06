﻿#"""
#This file is part of Happypanda.
#Happypanda is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 2 of the License, or
#any later version.
#Happypanda is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#You should have received a copy of the GNU General Public License
#along with Happypanda.  If not, see <http://www.gnu.org/licenses/>.
#"""

import sys, logging, logging.handlers, os, argparse, platform, scandir, traceback

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QFile

from database import db, db_constants
import app
import gui_constants
import gallerydb

#IMPORTANT STUFF
def start(test=False):

	if os.name == 'posix':
		main_path = os.path.dirname(os.path.realpath(__file__))
		log_path = os.path.join(main_path, 'happypanda.log')
		debug_log_path = os.path.join(main_path, 'happypanda_debug.log')
	else:
		log_path = 'happypanda.log'
		debug_log_path = 'happypanda_debug.log'

	parser = argparse.ArgumentParser(prog='Happypanda',
								  description='A manga/doujinshi manager with tagging support')
	parser.add_argument('-d', '--debug', action='store_true',
					 help='happypanda_debug_log.log will be created in main directory')
	parser.add_argument('-t', '--test', action='store_true',
					 help='Run happypanda in test mode. 5000 gallery will be preadded in DB.')
	parser.add_argument('-v', '--versi on', action='version',
					 version='Happypanda v{}'.format(gui_constants.vs))
	parser.add_argument('-e', '--exceptions', action='store_true',
					 help='Disable custom excepthook')

	args = parser.parse_args()
	if args.debug:
		print("happypanda_debug.log created at {}".format(os.getcwd()))
		# create log
		try:
			with open(debug_log_path, 'x') as f:
				pass
		except FileExistsError:
			pass

		logging.basicConfig(level=logging.DEBUG,
						format='%(asctime)-8s %(levelname)-6s %(name)-6s %(message)s',
						datefmt='%d-%m %H:%M',
						filename='happypanda_debug.log',
						filemode='w')
		gui_constants.DEBUG = True
	else:
		try:
			with open(log_path, 'x') as f:
				pass
		except FileExistsError: pass
		file_handler = logging.handlers.RotatingFileHandler(
			log_path, maxBytes=1000000*10, encoding='utf-8', backupCount=2)
		logging.basicConfig(level=logging.INFO,
						format='%(asctime)-8s %(levelname)-6s %(name)-6s %(message)s',
						datefmt='%d-%m %H:%M',
						handlers=(file_handler,))


	log = logging.getLogger(__name__)
	log_i = log.info
	log_d = log.debug
	log_w = log.warning
	log_e = log.error
	log_c = log.critical

	if not args.exceptions:
		def uncaught_exceptions(ex_type, ex, tb):
			log_c(''.join(traceback.format_tb(tb)))
			log_c('{}: {}'.format(ex_type, ex))
			traceback.print_exception(ex_type, ex, tb)

		sys.excepthook = uncaught_exceptions

	application = QApplication(sys.argv)
	application.setOrganizationName('Pewpews')
	application.setOrganizationDomain('https://github.com/Pewpews/happypanda')
	application.setApplicationName('Happypanda')
	application.setApplicationDisplayName('Happypanda')
	application.setApplicationVersion('v{}'.format(gui_constants.vs))
	log_i('Happypanda Version {}'.format(gui_constants.vs))
	log_i('OS: {} {}\n'.format(platform.system(), platform.release()))
	try:
		if args.test:
			conn = db.init_db(True)
		else:
			conn = db.init_db()
		log_d('Init DB Conn: OK')
		log_i("DB Version: {}".format(db_constants.REAL_DB_VERSION))
	except:
		log_c('Invalid database')
		log.exception('Database connection failed!')
		from PyQt5.QtGui import QIcon
		from PyQt5.QtWidgets import QMessageBox
		msg_box = QMessageBox()
		msg_box.setWindowIcon(QIcon(gui_constants.APP_ICO_PATH))
		msg_box.setText('Invalid database')
		msg_box.setInformativeText("Do you want to create a new database?")
		msg_box.setIcon(QMessageBox.Critical)
		msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
		msg_box.setDefaultButton(QMessageBox.Yes)
		if msg_box.exec() == QMessageBox.Yes:
			pass
		else:
			application.exit()
			log_d('Normal Exit App: OK')
			sys.exit()

	def start_main_window(conn):
		DB = db.DBThread(conn)
		#if args.test:
		#	import threading, time
		#	ser_list = []
		#	for x in range(5000):
		#		s = gallerydb.gallery()
		#		s.profile = gui_constants.NO_IMAGE_PATH
		#		s.title = 'Test {}'.format(x)
		#		s.artist = 'Author {}'.format(x)
		#		s.path = gui_constants.static_dir
		#		s.type = 'Test'
		#		s.chapters = {0:gui_constants.static_dir}
		#		s.language = 'English'
		#		s.info = 'I am number {}'.format(x)
		#		ser_list.append(s)

		#	done = False
		#	thread_list = []
		#	i = 0
		#	while not done:
		#		try:
		#			if threading.active_count() > 5000:
		#				thread_list = []
		#				done = True
		#			else:
		#				thread_list.append(
		#					threading.Thread(target=gallerydb.galleryDB.add_gallery,
		#					  args=(ser_list[i],)))
		#				thread_list[i].start()
		#				i += 1
		#				print(i)
		#				print('Threads running: {}'.format(threading.activeCount()))
		#		except IndexError:
		#			done = True

		WINDOW = app.AppWindow()

		# styling
		d_style = gui_constants.default_stylesheet_path
		u_style =  gui_constants.user_stylesheet_path

		if len(u_style) is not 0:
			try:
				style_file = QFile(u_style)
				log_i('Select userstyle: OK')
			except:
				style_file = QFile(d_style)
				log_i('Select defaultstyle: OK')
		else:
			style_file = QFile(d_style)
			log_i('Select defaultstyle: OK')

		style_file.open(QFile.ReadOnly)
		style = str(style_file.readAll(), 'utf-8')
		application.setStyleSheet(style)
		try:
			os.mkdir(gui_constants.temp_dir)
		except FileExistsError:
			try:
				for root, dirs, files in scandir.walk('temp', topdown=False):
					for name in files:
						os.remove(os.path.join(root, name))
					for name in dirs:
						os.rmdir(os.path.join(root, name))
			except:
				log_i('Empty temp: FAIL')
		log_d('Create temp: OK')

		if test:
			return application, WINDOW

		sys.exit(application.exec_())

	def db_upgrade():
		log_d('Database connection failed')
		from PyQt5.QtGui import QIcon
		from PyQt5.QtWidgets import QMessageBox

		msg_box = QMessageBox()
		msg_box.setWindowIcon(QIcon(gui_constants.APP_ICO_PATH))
		msg_box.setText('Incompatible database!')
		msg_box.setInformativeText("Do you want to upgrade to newest version?" +
							 " It shouldn't take more than a second. Don't start a new instance!")
		msg_box.setIcon(QMessageBox.Critical)
		msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
		msg_box.setDefaultButton(QMessageBox.Yes)
		if msg_box.exec() == QMessageBox.Yes:

			import threading
			db_p = db_constants.DB_PATH
			threading.Thread(target=db.add_db_revisions,
					args=(db_p,)).start()
			done = None
			while not done:
				done = db.ResultQueue.get()
			conn = db.init_db()
			start_main_window(conn)
		else:
			application.exit()
			log_d('Normal Exit App: OK')
			sys.exit()

	if conn:
		start_main_window(conn)
	else:
		db_upgrade()

if __name__ == '__main__':
	start()
