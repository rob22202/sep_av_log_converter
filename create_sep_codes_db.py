#!/usr/bin/python
# -*- coding: utf-8 -*-

# Codes obtained from http://www.symantec.com/business/support/index?page=content&id=TECH100099

import sqlite3
import sys

try:
  con = sqlite3.connect('sep_codes.db')
	cur = con.cursor()  
	cur.executescript("""
		DROP TABLE IF EXISTS sep_codes;
		CREATE TABLE sep_codes(code int, event text);
		insert into sep_codes (code,event) values (1,'GL_EVENT_IS_ALERT');
		insert into sep_codes (code,event) values (2,'GL_EVENT_SCAN_STOP');
		insert into sep_codes (code,event) values (3,'GL_EVENT_SCAN_START');
		insert into sep_codes (code,event) values (4,'GL_EVENT_PATTERN_UPDATE');
		insert into sep_codes (code,event) values (5,'GL_EVENT_INFECTION');
		insert into sep_codes (code,event) values (6,'GL_EVENT_FILE_NOT_OPEN');
		insert into sep_codes (code,event) values (7,'GL_EVENT_LOAD_PATTERN');
		insert into sep_codes (code,event) values (8,'GL_STD_MESSAGE_INFONOTUSED');
		insert into sep_codes (code,event) values (9,'GL_STD_MESSAGE_ERRORNOTUSED');
		insert into sep_codes (code,event) values (10,'GL_EVENT_CHECKSUM');
		insert into sep_codes (code,event) values (11,'GL_EVENT_TRAP');
		insert into sep_codes (code,event) values (12,'GL_EVENT_CONFIG_CHANGE');
		insert into sep_codes (code,event) values (13,'GL_EVENT_SHUTDOWN');
		insert into sep_codes (code,event) values (14,'GL_EVENT_STARTUP');
		insert into sep_codes (code,event) values (16,'GL_EVENT_PATTERN_DOWNLOAD');
		insert into sep_codes (code,event) values (17,'GL_EVENT_TOO_MANY_VIRUSES');
		insert into sep_codes (code,event) values (18,'GL_EVENT_FWD_TO_QSERVER');
		insert into sep_codes (code,event) values (19,'GL_EVENT_SCANDLVR');
		insert into sep_codes (code,event) values (20,'GL_EVENT_BACKUP');
		insert into sep_codes (code,event) values (21,'GL_EVENT_SCAN_ABORT');
		insert into sep_codes (code,event) values (22,'GL_EVENT_RTS_LOAD_ERROR');
		insert into sep_codes (code,event) values (23,'GL_EVENT_RTS_LOAD');
		insert into sep_codes (code,event) values (24,'GL_EVENT_RTS_UNLOAD');
		insert into sep_codes (code,event) values (25,'GL_EVENT_REMOVE_CLIENT');
		insert into sep_codes (code,event) values (26,'GL_EVENT_SCAN_DELAYED');
		insert into sep_codes (code,event) values (27,'GL_EVENT_SCAN_RESTART');
		insert into sep_codes (code,event) values (28,'GL_EVENT_ADD_SAVROAMCLIENT_TOSERVER');
		insert into sep_codes (code,event) values (29,'GL_EVENT_REMOVE_SAVROAMCLIENT_FROMSERVER');
		insert into sep_codes (code,event) values (30,'GL_EVENT_LICENSE_WARNING');
		insert into sep_codes (code,event) values (31,'GL_EVENT_LICENSE_ERROR');
		insert into sep_codes (code,event) values (32,'GL_EVENT_LICENSE_GRACE');
		insert into sep_codes (code,event) values (33,'GL_EVENT_UNAUTHORIZED_COMM');
		insert into sep_codes (code,event) values (34,'GL_EVENT_LOG_FWD_THRD_ERR');
		insert into sep_codes (code,event) values (35,'GL_EVENT_LICENSE_INSTALLED');
		insert into sep_codes (code,event) values (36,'GL_EVENT_LICENSE_ALLOCATED');
		insert into sep_codes (code,event) values (37,'GL_EVENT_LICENSE_OK');
		insert into sep_codes (code,event) values (38,'GL_EVENT_LICENSE_DEALLOCATED');
		insert into sep_codes (code,event) values (39,'GL_EVENT_BAD_DEFS_ROLLBACK');
		insert into sep_codes (code,event) values (40,'GL_EVENT_BAD_DEFS_UNPROTECTED');
		insert into sep_codes (code,event) values (41,'GL_EVENT_SAV_PROVIDER_PARSING_ERROR');
		insert into sep_codes (code,event) values (42,'GL_EVENT_RTS_ERROR');
		insert into sep_codes (code,event) values (43,'GL_EVENT_COMPLIANCE_FAIL');
		insert into sep_codes (code,event) values (44,'GL_EVENT_COMPLIANCE_SUCCESS');
		insert into sep_codes (code,event) values (45,'GL_EVENT_SECURITY_SYMPROTECT_POLICYVIOLATION');
		insert into sep_codes (code,event) values (46,'GL_EVENT_ANOMALY_START');
		insert into sep_codes (code,event) values (47,'GL_EVENT_DETECTION_ACTION_TAKEN');
		insert into sep_codes (code,event) values (48,'GL_EVENT_REMEDIATION_ACTION_PENDING');
		insert into sep_codes (code,event) values (49,'GL_EVENT_REMEDIATION_ACTION_FAILED');
		insert into sep_codes (code,event) values (50,'GL_EVENT_REMEDIATION_ACTION_SUCCESSFUL');
		insert into sep_codes (code,event) values (51,'GL_EVENT_ANOMALY_FINISH');
		insert into sep_codes (code,event) values (52,'GL_EVENT_COMMS_LOGIN_FAILED');
		insert into sep_codes (code,event) values (53,'GL_EVENT_COMMS_LOGIN_SUCCESS');
		insert into sep_codes (code,event) values (54,'GL_EVENT_COMMS_UNAUTHORIZED_COMM');
		insert into sep_codes (code,event) values (55,'GL_EVENT_CLIENT_INSTALL_AV');
		insert into sep_codes (code,event) values (56,'GL_EVENT_CLIENT_INSTALL_FW');
		insert into sep_codes (code,event) values (57,'GL_EVENT_CLIENT_UNINSTALL');
		insert into sep_codes (code,event) values (58,'GL_EVENT_CLIENT_UNINSTALL_ROLLBACK');
		insert into sep_codes (code,event) values (59,'GL_EVENT_COMMS_SERVER_GROUP_ROOT_CERT_ISSUE');
		insert into sep_codes (code,event) values (60,'GL_EVENT_COMMS_SERVER_CERT_ISSUE');
		insert into sep_codes (code,event) values (61,'GL_EVENT_COMMS_TRUSTED_ROOT_CHANGE');
		insert into sep_codes (code,event) values (62,'GL_EVENT_COMMS_SERVER_CERT_STARTUP_FAILED');
		insert into sep_codes (code,event) values (63,'GL_EVENT_CLIENT_CHECKIN');
		insert into sep_codes (code,event) values (64,'GL_EVENT_CLIENT_NO_CHECKIN');
		insert into sep_codes (code,event) values (65,'GL_EVENT_SCAN_SUSPENDED');
		insert into sep_codes (code,event) values (66,'GL_EVENT_SCAN_RESUMED');
		insert into sep_codes (code,event) values (67,'GL_EVENT_SCAN_DURATION_INSUFFICIENT');
		insert into sep_codes (code,event) values (68,'GL_EVENT_CLIENT_MOVE');
		insert into sep_codes (code,event) values (69,'GL_EVENT_SCAN_FAILED_ENHANCED');
		insert into sep_codes (code,event) values (70,'GL_EVENT_MAX_EVENT_NUMBER');
		insert into sep_codes (code,event) values (71,'GL_EVENT_HEUR_THREAT_NOW_WHITELISTED');
		insert into sep_codes (code,event) values (72,'GL_EVENT_INTERESTING_PROCESS_DETECTED_START');
		insert into sep_codes (code,event) values (73,'GL_EVENT_LOAD_ERROR_COH');
		insert into sep_codes (code,event) values (74,'GL_EVENT_LOAD_ERROR_SYKNAPPS');
		insert into sep_codes (code,event) values (75,'GL_EVENT_INTERESTING_PROCESS_DETECTED_FINISH');
		insert into sep_codes (code,event) values (76,'GL_EVENT_HPP_SCAN_NOT_SUPPORTED_FOR_OS');
		insert into sep_codes (code,event) values (77,'GL_EVENT_HEUR_THREAT_NOW_KNOWN');
		""")

	con.commit()
	
except sqlite3.Error, e:
	
	if con:
		con.rollback()
		
	print "Error %s:" % e.args[0]
	sys.exit(1)
	
finally:
	
	if con:
		con.close()
