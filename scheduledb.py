import hashlib
import logging
import sqlite3

from datetime import datetime

import config

organization_field_length = 15
faculty_field_length = 10
group_field_length = 5

class ScheduleDB:
    def __init__(self):
        self.con = sqlite3.connect(config.db_path)
        self.cur = self.con.cursor()

        logging.basicConfig(format='%(astime)-15s [ %(levelname)s ] %(message)s',
                            filemode='a',
                            filename=config.log_dir_patch + "log-{0}.log".format(datetime.now().strftime("%Y-%m")))
        self.logger = logging.getLogger('db-logger')

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.con.commit()
        self.con.close()

    @staticmethod
    def create_tag(organization, faculty, group):
        org_hash = hashlib.sha256(organization.encode('utf-8')).hexdigest()
        faculty_hash = hashlib.sha256(faculty.encode('utf-8')).hexdigest()
        group_hash = hashlib.sha256(group.encode('utf-8')).hexdigest()
        return org_hash[:organization_field_length] + \
            faculty_hash[:faculty_field_length] + \
            group_hash[:group_field_length]

    def add_lesson(self, tag, day, number, week_type, time_start, time_end, title, classroom, lecturer):
        try:
            self.cur.execute("INSERT INTO schedule(tag, day, number, type, startTime, endTime, \
                             title, classroom, lecturer) VALUES (?, ?, ?, ?, ?, ?, ?, ?);",
                             (tag, day, number, week_type, time_start, time_end, title, classroom, lecturer))
            self.con.commit()
            return True
        except BaseException as e:
            self.logger.warning('Add to schedule Failed. Error: {0}. Data:\
                                tag={1],\
                                day={2],\
                                number={3},\
                                week_type={4},\
                                time_start={5},\
                                time_end={6},\
                                title={7},\
                                classroom={8},\
                        lecturer={9}'.format(str(e), tag, day, number, week_type, time_start, time_end, title, classroom, lecturer))
            return False

    def add_organization(self, organization, faculty, group):
        tag = self.create_tag(organization, faculty, group)
        try:
            self.cur.execute('INSERT INTO organizations(organization, faculty, studGroup, tag) VALUES(?,?,?,?);',
                             (organization, faculty, group, tag))
            self.con.commit()
            return tag
        except BaseException as e:
            self.logger.warning('Add organization failed. Error: {0}. Data:\
                                organization={1},\
                                facluty={2},\
                                group={3},\
                                tag={4}'.format(str(e), organization, faculty, group, tag))




