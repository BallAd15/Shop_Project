import tkinter
from PIL import ImageTk,Image,ImageDraw,ImageFont,ImageOps,ImageSequence 
import requests
def get_main_img(url,width,height):
	profile_img = Image.open(requests.get(url, stream=True).raw)
	profile_img= profile_img.resize((width,height), Image.ANTIALIAS)
	profile_img = ImageTk.PhotoImage(profile_img)
	return profile_img
'''
https://github.com/SujithBonthala/TheEmporium/blob/main/TheEmporium.py
{'Stages': [{'Sid': '6944', 'Snm': 'League Cup: Play-off', 'Scd': 'league-cup-play-off', 'Cid': '136', 'Cnm': 'Japan', 'Csnm': 'Japan', 'Ccd': 'japan', 'Ccdiso': 'JPN', 'Scu': 1, 'Chi': 0, 'Shi': 0, 'Sdn': 'League Cup: Play-off', 'Events': [{'Eid': '485399', 'Pids': {'1': '3657686', '6': '28191728', '8': '485399', '12': 'SBTE_24232607'}, 'Eps': 'HT', 'Esid': 10, 'Epr': 1, 'Ecov': 0, 'ErnO': 0, 'Ern': 1004, 'ErnInf': 'Quarter Finals', 'Et': 1, 'Tr1': '0', 'Tr2': '0', 'Trh1': '0', 'Trh2': '0', 'Tr1OR': '0', 'Tr2OR': '0', 'T1': [{'Nm': 'Cerezo Osaka', 'ID': '7548', 'tbd': 0, 'Img': 'enet/4692.png', 'EL': [], 'Gd': 1, 'Pids': {'1': ['4692'], '6': ['3141'], '8': ['7548'], '12': ['SBTP_4731']}, 'CoNm': 'Japan', 'CoId': 'JPN', 'Shrt': {'Bs': 'fa0000', 'Sl': 'f50000', 'Nmb': 'ffffff', 'Sq': False, 'St': False, 'Hst': False, 'Spl': False, 'Sld': '0c0227'}}], 'T2': [{'Nm': 'Gamba Osaka', 'ID': '7602', 'tbd': 0, 'Img': 'enet/6582.png', 'EL': [], 'Gd': 1, 'Pids': {'1': ['6582'], '6': ['3138'], '8': ['7602'], '12': ['SBTP_4730']}, 'CoNm': 'Japan', 'CoId': 'JPN', 'Shrt': {'Bs': '25255f', 'Sl': '000000', 'Nmb': 'ffffff', 'Sq': False, 'St': False, 'Hst': False, 'Spl': True, 'SplC': '000000'}}], 'IncsX': 0, 'ComX': 0, 'LuX': 0, 'StatX': 1, 'SubsX': 0, 'SDFowX': 0, 'SDInnX': 0, 'Esd': 20210901170000, 'LuUT': 0, 'Eds': 20210901174549, 'Edf': 0, 'EO': 16775, 'Eact': 1, 'Stg': {'Sid': '6944', 'Snm': 'League Cup: Play-off', 'Scd': 'league-cup-play-off', 'Cid': '136', 'Cnm': 'Japan', 'Csnm': 'Japan', 'Ccd': 'japan', 'Ccdiso': 'JPN', 'Scu': 1, 'Chi': 0, 'Shi': 0, 'Sdn': 'League Cup: Play-off'}, 'Ehid': 0, 'Sids': {'1': '873437', '6': '120298', '8': '6944', '12': 'SBTC3_90982'}, 'Pid': 8, 'Spid': 1}, {'Eid': '485403', 'Pids': {'1': '3657688', '6': '28191810', '8': '485403', '12': 'SBTE_24232606'}, 'Eps': 'HT', 'Esid': 10, 'Epr': 1, 'Ecov': 0, 'ErnO': 0, 'Ern': 1004, 'ErnInf': 'Quarter Finals', 'Et': 1, 'Tr1': '1', 'Tr2': '1', 'Trh1': '1', 'Trh2': '1', 'Tr1OR': '1', 'Tr2OR': '1', 'T1': [{'Nm': 'Consadole Sapporo', 'ID': '7607', 'tbd': 0, 'Img': 'enet/112688.png', 'EL': [], 'Gd': 1, 'Pids': {'1': ['112688'], '6': ['3142'], '8': ['7607'], '12': ['SBTP_7348']}, 'CoNm': 'Japan', 'CoId': 'JPN', 'Shrt': {'Bs': 'ff0000', 'Sl': 'ff0000', 'Nmb': 'ffffff', 'Sq': False, 'St': True, 'StC': '000000', 'Hst': False, 'Spl': False, 'Sld': '000000'}}], 'T2': [{'Nm': 'FC Tokyo', 'ID': '7606', 'tbd': 0, 'Img': 'enet/4399.png', 'EL': [], 'Gd': 1, 'Pids': {'1': ['4399'], '6': ['3147'], '8': ['7606'], '12': ['SBTP_3268']}, 'CoNm': 'Japan', 'CoId': 'JPN', 'Shrt': {'Bs': '0033cc', 'Sl': '0033cc', 'Nmb': 'ffffff', 'Sq': False, 'St': True, 'StC': 'ef0635', 'Hst': False, 'Spl': False, 'Sld': '0033cc'}}], 'IncsX': 1, 'ComX': 0, 'LuX': 0, 'StatX': 1, 'SubsX': 0, 'SDFowX': 0, 'SDInnX': 0, 'Esd': 20210901170000, 'LuUT': 0, 'Eds': 20210901174604, 'Edf': 0, 'EO': 16783, 'Eact': 1, 'Stg': {'Sid': '6944', 'Snm': 'League Cup: Play-off', 'Scd': 'league-cup-play-off', 'Cid': '136', 'Cnm': 'Japan', 'Csnm': 'Japan', 'Ccd': 'japan', 'Ccdiso': 'JPN', 'Scu': 1, 'Chi': 0, 'Shi': 0, 'Sdn': 'League Cup: Play-off'}, 'Ehid': 0, 'Sids': {'1': '873437', '6': '120298', '8': '6944', '12': 'SBTC3_90982'}, 'Pid': 8, 'Spid': 1}, {'Eid': '485398', 'Pids': {'1': '3657690', '6': '28191820', '8': '485398', '12': 'SBTE_24232608'}, 'Eps': 'HT', 'Esid': 10, 'Epr': 1, 'Ecov': 0, 'ErnO': 0, 'Ern': 1004, 'ErnInf': 'Quarter Finals', 'Et': 1, 'Tr1': '1', 'Tr2': '0', 'Trh1': '1', 'Trh2': '0', 'Tr1OR': '1', 'Tr2OR': '0', 'T1': [{'Nm': 'Nagoya Grampus Eight', 'ID': '7529', 'tbd': 0, 'Img': 'enet/8006.png', 'EL': [], 'Gd': 1, 'Pids': {'1': ['8006'], '6': ['3136'], '8': ['7529'], '12': ['SBTP_3943']}, 'CoNm': 'Japan', 'CoId': 'JPN', 'Shrt': {'Bs': 'cc0000', 'Sl': 'cc0000', 'Nmb': 'ffffff', 'Sq': False, 'St': False, 'Hst': False, 'Spl': False, 'Sld': 'f43e01'}}], 'T2': [{'Nm': 'Kashima Antlers', 'ID': '4842', 'tbd': 0, 'Img': 'enet/4397.png', 'EL': [], 'Gd': 1, 'Pids': {'1': ['4397'], '6': ['3134'], '8': ['4842'], '12': ['SBTP_10664']}, 'CoNm': 'Japan', 'CoId': 'JPN', 'Shrt': {'Bs': 'bb0000', 'Sl': 'bb0000', 'Nmb': 'ffffff', 'Sq': False, 'St': False, 'Hst': False, 'Spl': False, 'Sld': '000000'}}], 'IncsX': 1, 'ComX': 0, 'LuX': 0, 'StatX': 1, 'SubsX': 0, 'SDFowX': 0, 'SDInnX': 0, 'Esd': 20210901170000, 'LuUT': 0, 'Eds': 20210901174620, 'Edf': 0, 'EO': 16783, 'Eact': 1, 'Stg': {'Sid': '6944', 'Snm': 'League Cup: Play-off', 'Scd': 'league-cup-play-off', 'Cid': '136', 'Cnm': 'Japan', 'Csnm': 'Japan', 'Ccd': 'japan', 'Ccdiso': 'JPN', 'Scu': 1, 'Chi': 0, 'Shi': 0, 'Sdn': 'League Cup: Play-off'}, 'Ehid': 0, 'Sids': {'1': '873437', '6': '120298', '8': '6944', '12': 'SBTC3_90982'}, 'Pid': 8, 'Spid': 1}, {'Eid': '485401', 'Pids': {'1': '3657692', '6': '28191822', '8': '485401', '12': 'SBTE_24232622'}, 'Eps': 'HT', 'Esid': 10, 'Epr': 1, 'Ecov': 0, 'ErnO': 0, 'Ern': 1004, 'ErnInf': 'Quarter Finals', 'Et': 1, 'Tr1': '1', 'Tr2': '0', 'Trh1': '1', 'Trh2': '0', 'Tr1OR': '1', 'Tr2OR': '0', 'T1': [{'Nm': 'Urawa Red Diamonds', 'ID': '7601', 'tbd': 0, 'Img': 'enet/6244.png', 'EL': [], 'Gd': 1, 'Pids': {'1': ['6244'], '6': ['3145'], '8': ['7601'], '12': ['SBTP_44580']}, 'CoNm': 'Japan', 'CoId': 'JPN', 'Shrt': {'Bs': 'ca0202', 'Sl': 'ca0202', 'Nmb': 'ffffff', 'Sq': False, 'St': False, 'Hst': False, 'Spl': False, 'Sld': '000000'}}], 'T2': [{'Nm': 'Kawasaki Frontale', 'ID': '7608', 'tbd': 0, 'Img': 'enet/6304.png', 'EL': [], 'Gd': 1, 'Pids': {'1': ['6304'], '6': ['5127'], '8': ['7608'], '12': ['SBTP_3271']}, 'CoNm': 'Japan', 'CoId': 'JPN', 'Shrt': {'Bs': '138be7', 'Sl': '138be7', 'Nmb': 'ffffff', 'Sq': False, 'St': False, 'Hst': False, 'Spl': False, 'Sld': '000000'}}], 'IncsX': 1, 'ComX': 0, 'LuX': 0, 'StatX': 1, 'SubsX': 0, 'SDFowX': 0, 'SDInnX': 0, 'Esd': 20210901170000, 'LuUT': 0, 'Eds': 20210901174638, 'Edf': 0, 'EO': 16783, 'Eact': 1, 'Stg': {'Sid': '6944', 'Snm': 'League Cup: Play-off', 'Scd': 'league-cup-play-off', 'Cid': '136', 'Cnm': 'Japan', 'Csnm': 'Japan', 'Ccd': 'japan', 'Ccdiso': 'JPN', 'Scu': 1, 'Chi': 0, 'Shi': 0, 'Sdn': 'League Cup: Play-off'}, 'Ehid': 0, 'Sids': {'1': '873437', '6': '120298', '8': '6944', '12': 'SBTC3_90982'}, 'Pid': 8, 'Spid': 1}]}, {'Sid': '5731', 'Snm': '2. Division: Group 1', 'Sds': '2. Division: Group 1', 'Scd': '2-division-group-1', 'Cid': '250', 'Cnm': 'Norway', 'Csnm': 'Norway', 'Ccd': 'norway', 'Ccdiso': 'NOR', 'Scu': 0, 'Chi': 0, 'Shi': 0, 'Sdn': '2. Division: Group 1', 'Events': [{'Eid': '356227', 'Pids': {'1': '3517775', '6': '27573390', '8': '356227', '12': 'SBTE_24285296'}, 'Eps': "1'", 'Esid': 2, 'Epr': 1, 'Ecov': 0, 'ErnO': 0, 'Ern': 15, 'ErnInf': '15', 'Et': 1, 'Tr1': '0', 'Tr2': '0', 'Tr1OR': '0', 'Tr2OR': '0', 'T1': [{'Nm': 'Senja', 'ID': '10398', 'tbd': 0, 'Img': 'enet/2316.png', 'EL': [], 'Gd': 1, 'Pids': {'1': ['2316'], '6': ['864'], '8': ['10398'], '12': ['SBTP_33116']}, 'CoNm': 'Norway', 'CoId': 'NOR'}], 'T2': [{'Nm': 'Eidsvold TF', 'ID': '10520', 'tbd': 0, 'Img': 'enet/8292.png', 'EL': [], 'Gd': 1, 'Pids': {'1': ['8292'], '6': ['694'], '8': ['10520'], '12': ['SBTP_17083']}, 'CoNm': 'Norway', 'CoId': 'NOR'}], 'IncsX': 0, 'ComX': 0, 'LuX': 0, 'StatX': 0, 'SubsX': 0, 'SDFowX': 0, 'SDInnX': 0, 'Esd': 20210901181500, 'LuUT': 0, 'Eds': 20210901181633, 'Edf': 0, 'EO': 16519, 'Eact': 1, 'Stg': {'Sid': '5731', 'Snm': '2. Division: Group 1', 'Sds': '2. Division: Group 1', 'Scd': '2-division-group-1', 'Cid': '250', 'Cnm': 'Norway', 'Csnm': 'Norway', 'Ccd': 'norway', 'Ccdiso': 'NOR', 'Scu': 0, 'Chi': 0, 'Shi': 0, 'Sdn': '2. Division: Group 1'}, 'Ehid': 0, 'Sids': {'1': '871717', '6': '54830', '8': '5731', '12': 'SBTC3_86480'}, 'Pid': 8, 'Spid': 1}]}, {'Sid': '5791', 'Snm': 'K-League 1', 'Sds': 'K-League 1', 'Scd': 'k-league-1', 'Cid': '111', 'Cnm': 'Republic of Korea', 'Csnm': 'Republic of Korea', 'Ccd': 'korea-republic', 'Ccdiso': 'KOR', 'Scu': 0, 'Chi': 0, 'Shi': 0, 'Sdn': 'K-League 1', 'Events': [{'Eid': '362922', 'Pids': {'1': '3524595', '6': '28304912', '8': '362922', '12': 'SBTE_24269231'}, 'Eps': "61'", 'Esid': 3, 'Epr': 1, 'Ecov': 0, 'ErnO': 0, 'Ern': 20, 'ErnInf': '20', 'Et': 1, 'Tr1': '0', 'Tr2': '1', 'Trh1': '0', 'Trh2': '1', 'Tr1OR': '0', 'Tr2OR': '1', 'T1': [{'Nm': 'Jeonbuk FC', 'ID': '7194', 'tbd': 0, 'Img': 'enet/46038.png', 'EL': [], 'Gd': 1, 'Pids': {'1': ['46038'], '6': ['6908'], '8': ['7194'], '12': ['SBTP_320771']}, 'CoNm': 'South Korea', 'CoId': 'KOR', 'Shrt': {'Bs': '00db1a', 'Sl': '00db1a', 'Nmb': '030303', 'Sq': False, 'St': False, 'Hst': False, 'Spl': False, 'Sld': '000000'}}], 'T2': [{'Nm': 'Pohang Steelers', 'ID': '8103', 'tbd': 0, 'Img': 'enet/109373.png', 'EL': [], 'Gd': 1, 'Pids': {'1': ['109373'], '6': ['7650'], '8': ['8103'], '12': ['SBTP_10722']}, 'CoNm': 'South Korea', 'CoId': 'KOR', 'Shrt': {'Bs': '000000', 'Sl': 'ff0000', 'Nmb': 'ffffff', 'Sq': False, 'St': False, 'Hst': False, 'Spl': False}}], 'IncsX': 1, 'ComX': 1, 'LuX': 1, 'StatX': 1, 'SubsX': 1, 'SDFowX': 0, 'SDInnX': 0, 'Esd': 20210901170000, 'LuUT': 20210901170024, 'Eds': 20210901170022, 'Edf': 0, 'EO': 17279, 'Eact': 1, 'Stg': {'Sid': '5791', 'Snm': 'K-League 1', 'Sds': 'K-League 1', 'Scd': 'k-league-1', 'Cid': '111', 'Cnm': 'Republic of Korea', 'Csnm': 'Republic of Korea', 'Ccd': 'korea-republic', 'Ccdiso': 'KOR', 'Scu': 0, 'Chi': 0, 'Shi': 0, 'Sdn': 'K-League 1'}, 'Ehid': 0, 'Sids': {'1': '871839', '6': '54718', '8': '5791', '12': 'SBTC3_90093'}, 'Pid': 8, 'Spid': 1}]}]}
{'Stages': [{'Sid': '6944', 'Snm': 'League Cup: Play-off', 'Scd': 'league-cup-play-off', 'Cid': '136', 'Cnm': 'Japan', 'Csnm': 'Japan', 'Ccd': 'japan', 'Ccdiso': 'JPN', 'Scu': 1, 'Chi': 0, 'Shi': 0, 'Sdn': 'League Cup: Play-off', 'Events': [{'Eid': '485399', 'Pids': {'1': '3657686', '6': '28191728', '8': '485399', '12': 'SBTE_24232607'}, 'Eps': 'HT', 'Esid': 10, 'Epr': 1, 'Ecov': 0, 'ErnO': 0, 'Ern': 1004, 'ErnInf': 'Quarter Finals', 'Et': 1, 'Tr1': '0', 'Tr2': '0', 'Trh1': '0', 'Trh2': '0', 'Tr1OR': '0', 'Tr2OR': '0', 'T1': [{'Nm': 'Cerezo Osaka', 'ID': '7548', 'tbd': 0, 'Img': 'enet/4692.png', 'EL': [], 'Gd': 1, 'Pids': {'1': ['4692'], '6': ['3141'], '8': ['7548'], '12': ['SBTP_4731']}, 'CoNm': 'Japan', 'CoId': 'JPN', 'Shrt': {'Bs': 'fa0000', 'Sl': 'f50000', 'Nmb': 'ffffff', 'Sq': False, 'St': False, 'Hst': False, 'Spl': False, 'Sld': '0c0227'}}], 'T2': [{'Nm': 'Gamba Osaka', 'ID': '7602', 'tbd': 0, 'Img': 'enet/6582.png', 'EL': [], 'Gd': 1, 'Pids': {'1': ['6582'], '6': ['3138'], '8': ['7602'], '12': ['SBTP_4730']}, 'CoNm': 'Japan', 'CoId': 'JPN', 'Shrt': {'Bs': '25255f', 'Sl': '000000', 'Nmb': 'ffffff', 'Sq': False, 'St': False, 'Hst': False, 'Spl': True, 'SplC': '000000'}}], 'IncsX': 0, 'ComX': 0, 'LuX': 0, 'StatX': 1, 'SubsX': 0, 'SDFowX': 0, 'SDInnX': 0, 'Esd': 20210901170000, 'LuUT': 0, 'Eds': 20210901174549, 'Edf': 0, 'EO': 16775, 'Eact': 1, 'Stg': {'Sid': '6944', 'Snm': 'League Cup: Play-off', 'Scd': 'league-cup-play-off', 'Cid': '136', 'Cnm': 'Japan', 'Csnm': 'Japan', 'Ccd': 'japan', 'Ccdiso': 'JPN', 'Scu': 1, 'Chi': 0, 'Shi': 0, 'Sdn': 'League Cup: Play-off'}, 'Ehid': 0, 'Sids': {'1': '873437', '6': '120298', '8': '6944', '12': 'SBTC3_90982'}, 'Pid': 8, 'Spid': 1}, {'Eid': '485403', 'Pids': {'1': '3657688', '6': '28191810', '8': '485403', '12': 'SBTE_24232606'}, 'Eps': 'HT', 'Esid': 10, 'Epr': 1, 'Ecov': 0, 'ErnO': 0, 'Ern': 1004, 'ErnInf': 'Quarter Finals', 'Et': 1, 'Tr1': '1', 'Tr2': '1', 'Trh1': '1', 'Trh2': '1', 'Tr1OR': '1', 'Tr2OR': '1', 'T1': [{'Nm': 'Consadole Sapporo', 'ID': '7607', 'tbd': 0, 'Img': 'enet/112688.png', 'EL': [], 'Gd': 1, 'Pids': {'1': ['112688'], '6': ['3142'], '8': ['7607'], '12': ['SBTP_7348']}, 'CoNm': 'Japan', 'CoId': 'JPN', 'Shrt': {'Bs': 'ff0000', 'Sl': 'ff0000', 'Nmb': 'ffffff', 'Sq': False, 'St': True, 'StC': '000000', 'Hst': False, 'Spl': False, 'Sld': '000000'}}], 'T2': [{'Nm': 'FC Tokyo', 'ID': '7606', 'tbd': 0, 'Img': 'enet/4399.png', 'EL': [], 'Gd': 1, 'Pids': {'1': ['4399'], '6': ['3147'], '8': ['7606'], '12': ['SBTP_3268']}, 'CoNm': 'Japan', 'CoId': 'JPN', 'Shrt': {'Bs': '0033cc', 'Sl': '0033cc', 'Nmb': 'ffffff', 'Sq': False, 'St': True, 'StC': 'ef0635', 'Hst': False, 'Spl': False, 'Sld': '0033cc'}}], 'IncsX': 1, 'ComX': 0, 'LuX': 0, 'StatX': 1, 'SubsX': 0, 'SDFowX': 0, 'SDInnX': 0, 'Esd': 20210901170000, 'LuUT': 0, 'Eds': 20210901174604, 'Edf': 0, 'EO': 16783, 'Eact': 1, 'Stg': {'Sid': '6944', 'Snm': 'League Cup: Play-off', 'Scd': 'league-cup-play-off', 'Cid': '136', 'Cnm': 'Japan', 'Csnm': 'Japan', 'Ccd': 'japan', 'Ccdiso': 'JPN', 'Scu': 1, 'Chi': 0, 'Shi': 0, 'Sdn': 'League Cup: Play-off'}, 'Ehid': 0, 'Sids': {'1': '873437', '6': '120298', '8': '6944', '12': 'SBTC3_90982'}, 'Pid': 8, 'Spid': 1}, {'Eid': '485398', 'Pids': {'1': '3657690', '6': '28191820', '8': '485398', '12': 'SBTE_24232608'}, 'Eps': 'HT', 'Esid': 10, 'Epr': 1, 'Ecov': 0, 'ErnO': 0, 'Ern': 1004, 'ErnInf': 'Quarter Finals', 'Et': 1, 'Tr1': '1', 'Tr2': '0', 'Trh1': '1', 'Trh2': '0', 'Tr1OR': '1', 'Tr2OR': '0', 'T1': [{'Nm': 'Nagoya Grampus Eight', 'ID': '7529', 'tbd': 0, 'Img': 'enet/8006.png', 'EL': [], 'Gd': 1, 'Pids': {'1': ['8006'], '6': ['3136'], '8': ['7529'], '12': ['SBTP_3943']}, 'CoNm': 'Japan', 'CoId': 'JPN', 'Shrt': {'Bs': 'cc0000', 'Sl': 'cc0000', 'Nmb': 'ffffff', 'Sq': False, 'St': False, 'Hst': False, 'Spl': False, 'Sld': 'f43e01'}}], 'T2': [{'Nm': 'Kashima Antlers', 'ID': '4842', 'tbd': 0, 'Img': 'enet/4397.png', 'EL': [], 'Gd': 1, 'Pids': {'1': ['4397'], '6': ['3134'], '8': ['4842'], '12': ['SBTP_10664']}, 'CoNm': 'Japan', 'CoId': 'JPN', 'Shrt': {'Bs': 'bb0000', 'Sl': 'bb0000', 'Nmb': 'ffffff', 'Sq': False, 'St': False, 'Hst': False, 'Spl': False, 'Sld': '000000'}}], 'IncsX': 1, 'ComX': 0, 'LuX': 0, 'StatX': 1, 'SubsX': 0, 'SDFowX': 0, 'SDInnX': 0, 'Esd': 20210901170000, 'LuUT': 0, 'Eds': 20210901174620, 'Edf': 0, 'EO': 16783, 'Eact': 1, 'Stg': {'Sid': '6944', 'Snm': 'League Cup: Play-off', 'Scd': 'league-cup-play-off', 'Cid': '136', 'Cnm': 'Japan', 'Csnm': 'Japan', 'Ccd': 'japan', 'Ccdiso': 'JPN', 'Scu': 1, 'Chi': 0, 'Shi': 0, 'Sdn': 'League Cup: Play-off'}, 'Ehid': 0, 'Sids': {'1': '873437', '6': '120298', '8': '6944', '12': 'SBTC3_90982'}, 'Pid': 8, 'Spid': 1}, {'Eid': '485401', 'Pids': {'1': '3657692', '6': '28191822', '8': '485401', '12': 'SBTE_24232622'}, 'Eps': 'HT', 'Esid': 10, 'Epr': 1, 'Ecov': 0, 'ErnO': 0, 'Ern': 1004, 'ErnInf': 'Quarter Finals', 'Et': 1, 'Tr1': '1', 'Tr2': '0', 'Trh1': '1', 'Trh2': '0', 'Tr1OR': '1', 'Tr2OR': '0', 'T1': [{'Nm': 'Urawa Red Diamonds', 'ID': '7601', 'tbd': 0, 'Img': 'enet/6244.png', 'EL': [], 'Gd': 1, 'Pids': {'1': ['6244'], '6': ['3145'], '8': ['7601'], '12': ['SBTP_44580']}, 'CoNm': 'Japan', 'CoId': 'JPN', 'Shrt': {'Bs': 'ca0202', 'Sl': 'ca0202', 'Nmb': 'ffffff', 'Sq': False, 'St': False, 'Hst': False, 'Spl': False, 'Sld': '000000'}}], 'T2': [{'Nm': 'Kawasaki Frontale', 'ID': '7608', 'tbd': 0, 'Img': 'enet/6304.png', 'EL': [], 'Gd': 1, 'Pids': {'1': ['6304'], '6': ['5127'], '8': ['7608'], '12': ['SBTP_3271']}, 'CoNm': 'Japan', 'CoId': 'JPN', 'Shrt': {'Bs': '138be7', 'Sl': '138be7', 'Nmb': 'ffffff', 'Sq': False, 'St': False, 'Hst': False, 'Spl': False, 'Sld': '000000'}}], 'IncsX': 1, 'ComX': 0, 'LuX': 0, 'StatX': 1, 'SubsX': 0, 'SDFowX': 0, 'SDInnX': 0, 'Esd': 20210901170000, 'LuUT': 0, 'Eds': 20210901174638, 'Edf': 0, 'EO': 16783, 'Eact': 1, 'Stg': {'Sid': '6944', 'Snm': 'League Cup: Play-off', 'Scd': 'league-cup-play-off', 'Cid': '136', 'Cnm': 'Japan', 'Csnm': 'Japan', 'Ccd': 'japan', 'Ccdiso': 'JPN', 'Scu': 1, 'Chi': 0, 'Shi': 0, 'Sdn': 'League Cup: Play-off'}, 'Ehid': 0, 'Sids': {'1': '873437', '6': '120298', '8': '6944', '12': 'SBTC3_90982'}, 'Pid': 8, 'Spid': 1}]}, {'Sid': '5731', 'Snm': '2. Division: Group 1', 'Sds': '2. Division: Group 1', 'Scd': '2-division-group-1', 'Cid': '250', 'Cnm': 'Norway', 'Csnm': 'Norway', 'Ccd': 'norway', 'Ccdiso': 'NOR', 'Scu': 0, 'Chi': 0, 'Shi': 0, 'Sdn': '2. Division: Group 1', 'Events': [{'Eid': '356227', 'Pids': {'1': '3517775', '6': '27573390', '8': '356227', '12': 'SBTE_24285296'}, 'Eps': "3'", 'Esid': 2, 'Epr': 1, 'Ecov': 0, 'ErnO': 0, 'Ern': 15, 'ErnInf': '15', 'Et': 1, 'Tr1': '0', 'Tr2': '0', 'Tr1OR': '0', 'Tr2OR': '0', 'T1': [{'Nm': 'Senja', 'ID': '10398', 'tbd': 0, 'Img': 'enet/2316.png', 'EL': [], 'Gd': 1, 'Pids': {'1': ['2316'], '6': ['864'], '8': ['10398'], '12': ['SBTP_33116']}, 'CoNm': 'Norway', 'CoId': 'NOR'}], 'T2': [{'Nm': 'Eidsvold TF', 'ID': '10520', 'tbd': 0, 'Img': 'enet/8292.png', 'EL': [], 'Gd': 1, 'Pids': {'1': ['8292'], '6': ['694'], '8': ['10520'], '12': ['SBTP_17083']}, 'CoNm': 'Norway', 'CoId': 'NOR'}], 'IncsX': 0, 'ComX': 0, 'LuX': 0, 'StatX': 0, 'SubsX': 0, 'SDFowX': 0, 'SDInnX': 0, 'Esd': 20210901181500, 'LuUT': 0, 'Eds': 20210901181633, 'Edf': 0, 'EO': 16519, 'Eact': 1, 'Stg': {'Sid': '5731', 'Snm': '2. Division: Group 1', 'Sds': '2. Division: Group 1', 'Scd': '2-division-group-1', 'Cid': '250', 'Cnm': 'Norway', 'Csnm': 'Norway', 'Ccd': 'norway', 'Ccdiso': 'NOR', 'Scu': 0, 'Chi': 0, 'Shi': 0, 'Sdn': '2. Division: Group 1'}, 'Ehid': 0, 'Sids': {'1': '871717', '6': '54830', '8': '5731', '12': 'SBTC3_86480'}, 'Pid': 8, 'Spid': 1}]}, {'Sid': '5791', 'Snm': 'K-League 1', 'Sds': 'K-League 1', 'Scd': 'k-league-1', 'Cid': '111', 'Cnm': 'Republic of Korea', 'Csnm': 'Republic of Korea', 'Ccd': 'korea-republic', 'Ccdiso': 'KOR', 'Scu': 0, 'Chi': 0, 'Shi': 0, 'Sdn': 'K-League 1', 'Events': [{'Eid': '362922', 'Pids': {'1': '3524595', '6': '28304912', '8': '362922', '12': 'SBTE_24269231'}, 'Eps': "63'", 'Esid': 3, 'Epr': 1, 'Ecov': 0, 'ErnO': 0, 'Ern': 20, 'ErnInf': '20', 'Et': 1, 'Tr1': '0', 'Tr2': '1', 'Trh1': '0', 'Trh2': '1', 'Tr1OR': '0', 'Tr2OR': '1', 'T1': [{'Nm': 'Jeonbuk FC', 'ID': '7194', 'tbd': 0, 'Img': 'enet/46038.png', 'EL': [], 'Gd': 1, 'Pids': {'1': ['46038'], '6': ['6908'], '8': ['7194'], '12': ['SBTP_320771']}, 'CoNm': 'South Korea', 'CoId': 'KOR', 'Shrt': {'Bs': '00db1a', 'Sl': '00db1a', 'Nmb': '030303', 'Sq': False, 'St': False, 'Hst': False, 'Spl': False, 'Sld': '000000'}}], 'T2': [{'Nm': 'Pohang Steelers', 'ID': '8103', 'tbd': 0, 'Img': 'enet/109373.png', 'EL': [], 'Gd': 1, 'Pids': {'1': ['109373'], '6': ['7650'], '8': ['8103'], '12': ['SBTP_10722']}, 'CoNm': 'South Korea', 'CoId': 'KOR', 'Shrt': {'Bs': '000000', 'Sl': 'ff0000', 'Nmb': 'ffffff', 'Sq': False, 'St': False, 'Hst': False, 'Spl': False}}], 'IncsX': 1, 'ComX': 1, 'LuX': 1, 'StatX': 1, 'SubsX': 1, 'SDFowX': 0, 'SDInnX': 0, 'Esd': 20210901170000, 'LuUT': 20210901170024, 'Eds': 20210901170022, 'Edf': 0, 'EO': 17279, 'Eact': 1, 'Stg': {'Sid': '5791', 'Snm': 'K-League 1', 'Sds': 'K-League 1', 'Scd': 'k-league-1', 'Cid': '111', 'Cnm': 'Republic of Korea', 'Csnm': 'Republic of Korea', 'Ccd': 'korea-republic', 'Ccdiso': 'KOR', 'Scu': 0, 'Chi': 0, 'Shi': 0, 'Sdn': 'K-League 1'}, 'Ehid': 0, 'Sids': {'1': '871839', '6': '54718', '8': '5791', '12': 'SBTC3_90093'}, 'Pid': 8, 'Spid': 1}]}]}
{'Stages': [{'Sid': '6944', 'Snm': 'League Cup: Play-off', 'Scd': 'league-cup-play-off', 'Cid': '136', 'Cnm': 'Japan', 'Csnm': 'Japan', 'Ccd': 'japan', 'Ccdiso': 'JPN', 'Scu': 1, 'Chi': 0, 'Shi': 0, 'Sdn': 'League Cup: Play-off', 'Events': [{'Eid': '485399', 'Pids': {'1': '3657686', '6': '28191728', '8': '485399', '12': 'SBTE_24232607'}, 'Eps': 'HT', 'Esid': 10, 'Epr': 1, 'Ecov': 0, 'ErnO': 0, 'Ern': 1004, 'ErnInf': 'Quarter Finals', 'Et': 1, 'Tr1': '0', 'Tr2': '0', 'Trh1': '0', 'Trh2': '0', 'Tr1OR': '0', 'Tr2OR': '0', 'T1': [{'Nm': 'Cerezo Osaka', 'ID': '7548', 'tbd': 0, 'Img': 'enet/4692.png', 'EL': [], 'Gd': 1, 'Pids': {'1': ['4692'], '6': ['3141'], '8': ['7548'], '12': ['SBTP_4731']}, 'CoNm': 'Japan', 'CoId': 'JPN', 'Shrt': {'Bs': 'fa0000', 'Sl': 'f50000', 'Nmb': 'ffffff', 'Sq': False, 'St': False, 'Hst': False, 'Spl': False, 'Sld': '0c0227'}}], 'T2': [{'Nm': 'Gamba Osaka', 'ID': '7602', 'tbd': 0, 'Img': 'enet/6582.png', 'EL': [], 'Gd': 1, 'Pids': {'1': ['6582'], '6': ['3138'], '8': ['7602'], '12': ['SBTP_4730']}, 'CoNm': 'Japan', 'CoId': 'JPN', 'Shrt': {'Bs': '25255f', 'Sl': '000000', 'Nmb': 'ffffff', 'Sq': False, 'St': False, 'Hst': False, 'Spl': True, 'SplC': '000000'}}], 'IncsX': 0, 'ComX': 0, 'LuX': 0, 'StatX': 1, 'SubsX': 0, 'SDFowX': 0, 'SDInnX': 0, 'Esd': 20210901170000, 'LuUT': 0, 'Eds': 20210901174549, 'Edf': 0, 'EO': 16775, 'Eact': 1, 'Stg': {'Sid': '6944', 'Snm': 'League Cup: Play-off', 'Scd': 'league-cup-play-off', 'Cid': '136', 'Cnm': 'Japan', 'Csnm': 'Japan', 'Ccd': 'japan', 'Ccdiso': 'JPN', 'Scu': 1, 'Chi': 0, 'Shi': 0, 'Sdn': 'League Cup: Play-off'}, 'Ehid': 0, 'Sids': {'1': '873437', '6': '120298', '8': '6944', '12': 'SBTC3_90982'}, 'Pid': 8, 'Spid': 1}, {'Eid': '485403', 'Pids': {'1': '3657688', '6': '28191810', '8': '485403', '12': 'SBTE_24232606'}, 'Eps': 'HT', 'Esid': 10, 'Epr': 1, 'Ecov': 0, 'ErnO': 0, 'Ern': 1004, 'ErnInf': 'Quarter Finals', 'Et': 1, 'Tr1': '1', 'Tr2': '1', 'Trh1': '1', 'Trh2': '1', 'Tr1OR': '1', 'Tr2OR': '1', 'T1': [{'Nm': 'Consadole Sapporo', 'ID': '7607', 'tbd': 0, 'Img': 'enet/112688.png', 'EL': [], 'Gd': 1, 'Pids': {'1': ['112688'], '6': ['3142'], '8': ['7607'], '12': ['SBTP_7348']}, 'CoNm': 'Japan', 'CoId': 'JPN', 'Shrt': {'Bs': 'ff0000', 'Sl': 'ff0000', 'Nmb': 'ffffff', 'Sq': False, 'St': True, 'StC': '000000', 'Hst': False, 'Spl': False, 'Sld': '000000'}}], 'T2': [{'Nm': 'FC Tokyo', 'ID': '7606', 'tbd': 0, 'Img': 'enet/4399.png', 'EL': [], 'Gd': 1, 'Pids': {'1': ['4399'], '6': ['3147'], '8': ['7606'], '12': ['SBTP_3268']}, 'CoNm': 'Japan', 'CoId': 'JPN', 'Shrt': {'Bs': '0033cc', 'Sl': '0033cc', 'Nmb': 'ffffff', 'Sq': False, 'St': True, 'StC': 'ef0635', 'Hst': False, 'Spl': False, 'Sld': '0033cc'}}], 'IncsX': 1, 'ComX': 0, 'LuX': 0, 'StatX': 1, 'SubsX': 0, 'SDFowX': 0, 'SDInnX': 0, 'Esd': 20210901170000, 'LuUT': 0, 'Eds': 20210901174604, 'Edf': 0, 'EO': 16783, 'Eact': 1, 'Stg': {'Sid': '6944', 'Snm': 'League Cup: Play-off', 'Scd': 'league-cup-play-off', 'Cid': '136', 'Cnm': 'Japan', 'Csnm': 'Japan', 'Ccd': 'japan', 'Ccdiso': 'JPN', 'Scu': 1, 'Chi': 0, 'Shi': 0, 'Sdn': 'League Cup: Play-off'}, 'Ehid': 0, 'Sids': {'1': '873437', '6': '120298', '8': '6944', '12': 'SBTC3_90982'}, 'Pid': 8, 'Spid': 1}, {'Eid': '485398', 'Pids': {'1': '3657690', '6': '28191820', '8': '485398', '12': 'SBTE_24232608'}, 'Eps': 'HT', 'Esid': 10, 'Epr': 1, 'Ecov': 0, 'ErnO': 0, 'Ern': 1004, 'ErnInf': 'Quarter Finals', 'Et': 1, 'Tr1': '1', 'Tr2': '0', 'Trh1': '1', 'Trh2': '0', 'Tr1OR': '1', 'Tr2OR': '0', 'T1': [{'Nm': 'Nagoya Grampus Eight', 'ID': '7529', 'tbd': 0, 'Img': 'enet/8006.png', 'EL': [], 'Gd': 1, 'Pids': {'1': ['8006'], '6': ['3136'], '8': ['7529'], '12': ['SBTP_3943']}, 'CoNm': 'Japan', 'CoId': 'JPN', 'Shrt': {'Bs': 'cc0000', 'Sl': 'cc0000', 'Nmb': 'ffffff', 'Sq': False, 'St': False, 'Hst': False, 'Spl': False, 'Sld': 'f43e01'}}], 'T2': [{'Nm': 'Kashima Antlers', 'ID': '4842', 'tbd': 0, 'Img': 'enet/4397.png', 'EL': [], 'Gd': 1, 'Pids': {'1': ['4397'], '6': ['3134'], '8': ['4842'], '12': ['SBTP_10664']}, 'CoNm': 'Japan', 'CoId': 'JPN', 'Shrt': {'Bs': 'bb0000', 'Sl': 'bb0000', 'Nmb': 'ffffff', 'Sq': False, 'St': False, 'Hst': False, 'Spl': False, 'Sld': '000000'}}], 'IncsX': 1, 'ComX': 0, 'LuX': 0, 'StatX': 1, 'SubsX': 0, 'SDFowX': 0, 'SDInnX': 0, 'Esd': 20210901170000, 'LuUT': 0, 'Eds': 20210901174620, 'Edf': 0, 'EO': 16783, 'Eact': 1, 'Stg': {'Sid': '6944', 'Snm': 'League Cup: Play-off', 'Scd': 'league-cup-play-off', 'Cid': '136', 'Cnm': 'Japan', 'Csnm': 'Japan', 'Ccd': 'japan', 'Ccdiso': 'JPN', 'Scu': 1, 'Chi': 0, 'Shi': 0, 'Sdn': 'League Cup: Play-off'}, 'Ehid': 0, 'Sids': {'1': '873437', '6': '120298', '8': '6944', '12': 'SBTC3_90982'}, 'Pid': 8, 'Spid': 1}, {'Eid': '485401', 'Pids': {'1': '3657692', '6': '28191822', '8': '485401', '12': 'SBTE_24232622'}, 'Eps': 'HT', 'Esid': 10, 'Epr': 1, 'Ecov': 0, 'ErnO': 0, 'Ern': 1004, 'ErnInf': 'Quarter Finals', 'Et': 1, 'Tr1': '1', 'Tr2': '0', 'Trh1': '1', 'Trh2': '0', 'Tr1OR': '1', 'Tr2OR': '0', 'T1': [{'Nm': 'Urawa Red Diamonds', 'ID': '7601', 'tbd': 0, 'Img': 'enet/6244.png', 'EL': [], 'Gd': 1, 'Pids': {'1': ['6244'], '6': ['3145'], '8': ['7601'], '12': ['SBTP_44580']}, 'CoNm': 'Japan', 'CoId': 'JPN', 'Shrt': {'Bs': 'ca0202', 'Sl': 'ca0202', 'Nmb': 'ffffff', 'Sq': False, 'St': False, 'Hst': False, 'Spl': False, 'Sld': '000000'}}], 'T2': [{'Nm': 'Kawasaki Frontale', 'ID': '7608', 'tbd': 0, 'Img': 'enet/6304.png', 'EL': [], 'Gd': 1, 'Pids': {'1': ['6304'], '6': ['5127'], '8': ['7608'], '12': ['SBTP_3271']}, 'CoNm': 'Japan', 'CoId': 'JPN', 'Shrt': {'Bs': '138be7', 'Sl': '138be7', 'Nmb': 'ffffff', 'Sq': False, 'St': False, 'Hst': False, 'Spl': False, 'Sld': '000000'}}], 'IncsX': 1, 'ComX': 0, 'LuX': 0, 'StatX': 1, 'SubsX': 0, 'SDFowX': 0, 'SDInnX': 0, 'Esd': 20210901170000, 'LuUT': 0, 'Eds': 20210901174638, 'Edf': 0, 'EO': 16783, 'Eact': 1, 'Stg': {'Sid': '6944', 'Snm': 'League Cup: Play-off', 'Scd': 'league-cup-play-off', 'Cid': '136', 'Cnm': 'Japan', 'Csnm': 'Japan', 'Ccd': 'japan', 'Ccdiso': 'JPN', 'Scu': 1, 'Chi': 0, 'Shi': 0, 'Sdn': 'League Cup: Play-off'}, 'Ehid': 0, 'Sids': {'1': '873437', '6': '120298', '8': '6944', '12': 'SBTC3_90982'}, 'Pid': 8, 'Spid': 1}]}, {'Sid': '5731', 'Snm': '2. Division: Group 1', 'Sds': '2. Division: Group 1', 'Scd': '2-division-group-1', 'Cid': '250', 'Cnm': 'Norway', 'Csnm': 'Norway', 'Ccd': 'norway', 'Ccdiso': 'NOR', 'Scu': 0, 'Chi': 0, 'Shi': 0, 'Sdn': '2. Division: Group 1', 'Events': [{'Eid': '356227', 'Pids': {'1': '3517775', '6': '27573390', '8': '356227', '12': 'SBTE_24285296'}, 'Eps': "4'", 'Esid': 2, 'Epr': 1, 'Ecov': 0, 'ErnO': 0, 'Ern': 15, 'ErnInf': '15', 'Et': 1, 'Tr1': '0', 'Tr2': '0', 'Tr1OR': '0', 'Tr2OR': '0', 'T1': [{'Nm': 'Senja', 'ID': '10398', 'tbd': 0, 'Img': 'enet/2316.png', 'EL': [], 'Gd': 1, 'Pids': {'1': ['2316'], '6': ['864'], '8': ['10398'], '12': ['SBTP_33116']}, 'CoNm': 'Norway', 'CoId': 'NOR'}], 'T2': [{'Nm': 'Eidsvold TF', 'ID': '10520', 'tbd': 0, 'Img': 'enet/8292.png', 'EL': [], 'Gd': 1, 'Pids': {'1': ['8292'], '6': ['694'], '8': ['10520'], '12': ['SBTP_17083']}, 'CoNm': 'Norway', 'CoId': 'NOR'}], 'IncsX': 0, 'ComX': 0, 'LuX': 0, 'StatX': 0, 'SubsX': 0, 'SDFowX': 0, 'SDInnX': 0, 'Esd': 20210901181500, 'LuUT': 0, 'Eds': 20210901181633, 'Edf': 0, 'EO': 16519, 'Eact': 1, 'Stg': {'Sid': '5731', 'Snm': '2. Division: Group 1', 'Sds': '2. Division: Group 1', 'Scd': '2-division-group-1', 'Cid': '250', 'Cnm': 'Norway', 'Csnm': 'Norway', 'Ccd': 'norway', 'Ccdiso': 'NOR', 'Scu': 0, 'Chi': 0, 'Shi': 0, 'Sdn': '2. Division: Group 1'}, 'Ehid': 0, 'Sids': {'1': '871717', '6': '54830', '8': '5731', '12': 'SBTC3_86480'}, 'Pid': 8, 'Spid': 1}]}, {'Sid': '5791', 'Snm': 'K-League 1', 'Sds': 'K-League 1', 'Scd': 'k-league-1', 'Cid': '111', 'Cnm': 'Republic of Korea', 'Csnm': 'Republic of Korea', 'Ccd': 'korea-republic', 'Ccdiso': 'KOR', 'Scu': 0, 'Chi': 0, 'Shi': 0, 'Sdn': 'K-League 1', 'Events': [{'Eid': '362922', 'Pids': {'1': '3524595', '6': '28304912', '8': '362922', '12': 'SBTE_24269231'}, 'Eps': "64'", 'Esid': 3, 'Epr': 1, 'Ecov': 0, 'ErnO': 0, 'Ern': 20, 'ErnInf': '20', 'Et': 1, 'Tr1': '0', 'Tr2': '1', 'Trh1': '0', 'Trh2': '1', 'Tr1OR': '0', 'Tr2OR': '1', 'T1': [{'Nm': 'Jeonbuk FC', 'ID': '7194', 'tbd': 0, 'Img': 'enet/46038.png', 'EL': [], 'Gd': 1, 'Pids': {'1': ['46038'], '6': ['6908'], '8': ['7194'], '12': ['SBTP_320771']}, 'CoNm': 'South Korea', 'CoId': 'KOR', 'Shrt': {'Bs': '00db1a', 'Sl': '00db1a', 'Nmb': '030303', 'Sq': False, 'St': False, 'Hst': False, 'Spl': False, 'Sld': '000000'}}], 'T2': [{'Nm': 'Pohang Steelers', 'ID': '8103', 'tbd': 0, 'Img': 'enet/109373.png', 'EL': [], 'Gd': 1, 'Pids': {'1': ['109373'], '6': ['7650'], '8': ['8103'], '12': ['SBTP_10722']}, 'CoNm': 'South Korea', 'CoId': 'KOR', 'Shrt': {'Bs': '000000', 'Sl': 'ff0000', 'Nmb': 'ffffff', 'Sq': False, 'St': False, 'Hst': False, 'Spl': False}}], 'IncsX': 1, 'ComX': 1, 'LuX': 1, 'StatX': 1, 'SubsX': 1, 'SDFowX': 0, 'SDInnX': 0, 'Esd': 20210901170000, 'LuUT': 20210901170024, 'Eds': 20210901170022, 'Edf': 0, 'EO': 17279, 'Eact': 1, 'Stg': {'Sid': '5791', 'Snm': 'K-League 1', 'Sds': 'K-League 1', 'Scd': 'k-league-1', 'Cid': '111', 'Cnm': 'Republic of Korea', 'Csnm': 'Republic of Korea', 'Ccd': 'korea-republic', 'Ccdiso': 'KOR', 'Scu': 0, 'Chi': 0, 'Shi': 0, 'Sdn': 'K-League 1'}, 'Ehid': 0, 'Sids': {'1': '871839', '6': '54718', '8': '5791', '12': 'SBTC3_90093'}, 'Pid': 8, 'Spid': 1}]}]}
{'Stages': [{'Sid': '6944', 'Snm': 'League Cup: Play-off', 'Scd': 'league-cup-play-off', 'Cid': '136', 'Cnm': 'Japan', 'Csnm': 'Japan', 'Ccd': 'japan', 'Ccdiso': 'JPN', 'Scu': 1, 'Chi': 0, 'Shi': 0, 'Sdn': 'League Cup: Play-off', 'Events': [{'Eid': '485399', 'Pids': {'1': '3657686', '6': '28191728', '8': '485399', '12': 'SBTE_24232607'}, 'Eps': 'HT', 'Esid': 10, 'Epr': 1, 'Ecov': 0, 'ErnO': 0, 'Ern': 1004, 'ErnInf': 'Quarter Finals', 'Et': 1, 'Tr1': '0', 'Tr2': '0', 'Trh1': '0', 'Trh2': '0', 'Tr1OR': '0', 'Tr2OR': '0', 'T1': [{'Nm': 'Cerezo Osaka', 'ID': '7548', 'tbd': 0, 'Img': 'enet/4692.png', 'EL': [], 'Gd': 1, 'Pids': {'1': ['4692'], '6': ['3141'], '8': ['7548'], '12': ['SBTP_4731']}, 'CoNm': 'Japan', 'CoId': 'JPN', 'Shrt': {'Bs': 'fa0000', 'Sl': 'f50000', 'Nmb': 'ffffff', 'Sq': False, 'St': False, 'Hst': False, 'Spl': False, 'Sld': '0c0227'}}], 'T2': [{'Nm': 'Gamba Osaka', 'ID': '7602', 'tbd': 0, 'Img': 'enet/6582.png', 'EL': [], 'Gd': 1, 'Pids': {'1': ['6582'], '6': ['3138'], '8': ['7602'], '12': ['SBTP_4730']}, 'CoNm': 'Japan', 'CoId': 'JPN', 'Shrt': {'Bs': '25255f', 'Sl': '000000', 'Nmb': 'ffffff', 'Sq': False, 'St': False, 'Hst': False, 'Spl': True, 'SplC': '000000'}}], 'IncsX': 0, 'ComX': 0, 'LuX': 0, 'StatX': 1, 'SubsX': 0, 'SDFowX': 0, 'SDInnX': 0, 'Esd': 20210901170000, 'LuUT': 0, 'Eds': 20210901174549, 'Edf': 0, 'EO': 16775, 'Eact': 1, 'Stg': {'Sid': '6944', 'Snm': 'League Cup: Play-off', 'Scd': 'league-cup-play-off', 'Cid': '136', 'Cnm': 'Japan', 'Csnm': 'Japan', 'Ccd': 'japan', 'Ccdiso': 'JPN', 'Scu': 1, 'Chi': 0, 'Shi': 0, 'Sdn': 'League Cup: Play-off'}, 'Ehid': 0, 'Sids': {'1': '873437', '6': '120298', '8': '6944', '12': 'SBTC3_90982'}, 'Pid': 8, 'Spid': 1}, {'Eid': '485403', 'Pids': {'1': '3657688', '6': '28191810', '8': '485403', '12': 'SBTE_24232606'}, 'Eps': 'HT', 'Esid': 10, 'Epr': 1, 'Ecov': 0, 'ErnO': 0, 'Ern': 1004, 'ErnInf': 'Quarter Finals', 'Et': 1, 'Tr1': '1', 'Tr2': '1', 'Trh1': '1', 'Trh2': '1', 'Tr1OR': '1', 'Tr2OR': '1', 'T1': [{'Nm': 'Consadole Sapporo', 'ID': '7607', 'tbd': 0, 'Img': 'enet/112688.png', 'EL': [], 'Gd': 1, 'Pids': {'1': ['112688'], '6': ['3142'], '8': ['7607'], '12': ['SBTP_7348']}, 'CoNm': 'Japan', 'CoId': 'JPN', 'Shrt': {'Bs': 'ff0000', 'Sl': 'ff0000', 'Nmb': 'ffffff', 'Sq': False, 'St': True, 'StC': '000000', 'Hst': False, 'Spl': False, 'Sld': '000000'}}], 'T2': [{'Nm': 'FC Tokyo', 'ID': '7606', 'tbd': 0, 'Img': 'enet/4399.png', 'EL': [], 'Gd': 1, 'Pids': {'1': ['4399'], '6': ['3147'], '8': ['7606'], '12': ['SBTP_3268']}, 'CoNm': 'Japan', 'CoId': 'JPN', 'Shrt': {'Bs': '0033cc', 'Sl': '0033cc', 'Nmb': 'ffffff', 'Sq': False, 'St': True, 'StC': 'ef0635', 'Hst': False, 'Spl': False, 'Sld': '0033cc'}}], 'IncsX': 1, 'ComX': 0, 'LuX': 0, 'StatX': 1, 'SubsX': 0, 'SDFowX': 0, 'SDInnX': 0, 'Esd': 20210901170000, 'LuUT': 0, 'Eds': 20210901174604, 'Edf': 0, 'EO': 16783, 'Eact': 1, 'Stg': {'Sid': '6944', 'Snm': 'League Cup: Play-off', 'Scd': 'league-cup-play-off', 'Cid': '136', 'Cnm': 'Japan', 'Csnm': 'Japan', 'Ccd': 'japan', 'Ccdiso': 'JPN', 'Scu': 1, 'Chi': 0, 'Shi': 0, 'Sdn': 'League Cup: Play-off'}, 'Ehid': 0, 'Sids': {'1': '873437', '6': '120298', '8': '6944', '12': 'SBTC3_90982'}, 'Pid': 8, 'Spid': 1}, {'Eid': '485398', 'Pids': {'1': '3657690', '6': '28191820', '8': '485398', '12': 'SBTE_24232608'}, 'Eps': 'HT', 'Esid': 10, 'Epr': 1, 'Ecov': 0, 'ErnO': 0, 'Ern': 1004, 'ErnInf': 'Quarter Finals', 'Et': 1, 'Tr1': '1', 'Tr2': '0', 'Trh1': '1', 'Trh2': '0', 'Tr1OR': '1', 'Tr2OR': '0', 'T1': [{'Nm': 'Nagoya Grampus Eight', 'ID': '7529', 'tbd': 0, 'Img': 'enet/8006.png', 'EL': [], 'Gd': 1, 'Pids': {'1': ['8006'], '6': ['3136'], '8': ['7529'], '12': ['SBTP_3943']}, 'CoNm': 'Japan', 'CoId': 'JPN', 'Shrt': {'Bs': 'cc0000', 'Sl': 'cc0000', 'Nmb': 'ffffff', 'Sq': False, 'St': False, 'Hst': False, 'Spl': False, 'Sld': 'f43e01'}}], 'T2': [{'Nm': 'Kashima Antlers', 'ID': '4842', 'tbd': 0, 'Img': 'enet/4397.png', 'EL': [], 'Gd': 1, 'Pids': {'1': ['4397'], '6': ['3134'], '8': ['4842'], '12': ['SBTP_10664']}, 'CoNm': 'Japan', 'CoId': 'JPN', 'Shrt': {'Bs': 'bb0000', 'Sl': 'bb0000', 'Nmb': 'ffffff', 'Sq': False, 'St': False, 'Hst': False, 'Spl': False, 'Sld': '000000'}}], 'IncsX': 1, 'ComX': 0, 'LuX': 0, 'StatX': 1, 'SubsX': 0, 'SDFowX': 0, 'SDInnX': 0, 'Esd': 20210901170000, 'LuUT': 0, 'Eds': 20210901174620, 'Edf': 0, 'EO': 16783, 'Eact': 1, 'Stg': {'Sid': '6944', 'Snm': 'League Cup: Play-off', 'Scd': 'league-cup-play-off', 'Cid': '136', 'Cnm': 'Japan', 'Csnm': 'Japan', 'Ccd': 'japan', 'Ccdiso': 'JPN', 'Scu': 1, 'Chi': 0, 'Shi': 0, 'Sdn': 'League Cup: Play-off'}, 'Ehid': 0, 'Sids': {'1': '873437', '6': '120298', '8': '6944', '12': 'SBTC3_90982'}, 'Pid': 8, 'Spid': 1}, {'Eid': '485401', 'Pids': {'1': '3657692', '6': '28191822', '8': '485401', '12': 'SBTE_24232622'}, 'Eps': 'HT', 'Esid': 10, 'Epr': 1, 'Ecov': 0, 'ErnO': 0, 'Ern': 1004, 'ErnInf': 'Quarter Finals', 'Et': 1, 'Tr1': '1', 'Tr2': '0', 'Trh1': '1', 'Trh2': '0', 'Tr1OR': '1', 'Tr2OR': '0', 'T1': [{'Nm': 'Urawa Red Diamonds', 'ID': '7601', 'tbd': 0, 'Img': 'enet/6244.png', 'EL': [], 'Gd': 1, 'Pids': {'1': ['6244'], '6': ['3145'], '8': ['7601'], '12': ['SBTP_44580']}, 'CoNm': 'Japan', 'CoId': 'JPN', 'Shrt': {'Bs': 'ca0202', 'Sl': 'ca0202', 'Nmb': 'ffffff', 'Sq': False, 'St': False, 'Hst': False, 'Spl': False, 'Sld': '000000'}}], 'T2': [{'Nm': 'Kawasaki Frontale', 'ID': '7608', 'tbd': 0, 'Img': 'enet/6304.png', 'EL': [], 'Gd': 1, 'Pids': {'1': ['6304'], '6': ['5127'], '8': ['7608'], '12': ['SBTP_3271']}, 'CoNm': 'Japan', 'CoId': 'JPN', 'Shrt': {'Bs': '138be7', 'Sl': '138be7', 'Nmb': 'ffffff', 'Sq': False, 'St': False, 'Hst': False, 'Spl': False, 'Sld': '000000'}}], 'IncsX': 1, 'ComX': 0, 'LuX': 0, 'StatX': 1, 'SubsX': 0, 'SDFowX': 0, 'SDInnX': 0, 'Esd': 20210901170000, 'LuUT': 0, 'Eds': 20210901174638, 'Edf': 0, 'EO': 16783, 'Eact': 1, 'Stg': {'Sid': '6944', 'Snm': 'League Cup: Play-off', 'Scd': 'league-cup-play-off', 'Cid': '136', 'Cnm': 'Japan', 'Csnm': 'Japan', 'Ccd': 'japan', 'Ccdiso': 'JPN', 'Scu': 1, 'Chi': 0, 'Shi': 0, 'Sdn': 'League Cup: Play-off'}, 'Ehid': 0, 'Sids': {'1': '873437', '6': '120298', '8': '6944', '12': 'SBTC3_90982'}, 'Pid': 8, 'Spid': 1}]}, {'Sid': '5731', 'Snm': '2. Division: Group 1', 'Sds': '2. Division: Group 1', 'Scd': '2-division-group-1', 'Cid': '250', 'Cnm': 'Norway', 'Csnm': 'Norway', 'Ccd': 'norway', 'Ccdiso': 'NOR', 'Scu': 0, 'Chi': 0, 'Shi': 0, 'Sdn': '2. Division: Group 1', 'Events': [{'Eid': '356227', 'Pids': {'1': '3517775', '6': '27573390', '8': '356227', '12': 'SBTE_24285296'}, 'Eps': "6'", 'Esid': 2, 'Epr': 1, 'Ecov': 0, 'ErnO': 0, 'Ern': 15, 'ErnInf': '15', 'Et': 1, 'Tr1': '0', 'Tr2': '0', 'Tr1OR': '0', 'Tr2OR': '0', 'T1': [{'Nm': 'Senja', 'ID': '10398', 'tbd': 0, 'Img': 'enet/2316.png', 'EL': [], 'Gd': 1, 'Pids': {'1': ['2316'], '6': ['864'], '8': ['10398'], '12': ['SBTP_33116']}, 'CoNm': 'Norway', 'CoId': 'NOR'}], 'T2': [{'Nm': 'Eidsvold TF', 'ID': '10520', 'tbd': 0, 'Img': 'enet/8292.png', 'EL': [], 'Gd': 1, 'Pids': {'1': ['8292'], '6': ['694'], '8': ['10520'], '12': ['SBTP_17083']}, 'CoNm': 'Norway', 'CoId': 'NOR'}], 'IncsX': 0, 'ComX': 0, 'LuX': 0, 'StatX': 0, 'SubsX': 0, 'SDFowX': 0, 'SDInnX': 0, 'Esd': 20210901181500, 'LuUT': 0, 'Eds': 20210901181633, 'Edf': 0, 'EO': 16519, 'Eact': 1, 'Stg': {'Sid': '5731', 'Snm': '2. Division: Group 1', 'Sds': '2. Division: Group 1', 'Scd': '2-division-group-1', 'Cid': '250', 'Cnm': 'Norway', 'Csnm': 'Norway', 'Ccd': 'norway', 'Ccdiso': 'NOR', 'Scu': 0, 'Chi': 0, 'Shi': 0, 'Sdn': '2. Division: Group 1'}, 'Ehid': 0, 'Sids': {'1': '871717', '6': '54830', '8': '5731', '12': 'SBTC3_86480'}, 'Pid': 8, 'Spid': 1}]}, {'Sid': '5791', 'Snm': 'K-League 1', 'Sds': 'K-League 1', 'Scd': 'k-league-1', 'Cid': '111', 'Cnm': 'Republic of Korea', 'Csnm': 'Republic of Korea', 'Ccd': 'korea-republic', 'Ccdiso': 'KOR', 'Scu': 0, 'Chi': 0, 'Shi': 0, 'Sdn': 'K-League 1', 'Events': [{'Eid': '362922', 'Pids': {'1': '3524595', '6': '28304912', '8': '362922', '12': 'SBTE_24269231'}, 'Eps': "66'", 'Esid': 3, 'Epr': 1, 'Ecov': 0, 'ErnO': 0, 'Ern': 20, 'ErnInf': '20', 'Et': 1, 'Tr1': '0', 'Tr2': '1', 'Trh1': '0', 'Trh2': '1', 'Tr1OR': '0', 'Tr2OR': '1', 'T1': [{'Nm': 'Jeonbuk FC', 'ID': '7194', 'tbd': 0, 'Img': 'enet/46038.png', 'EL': [], 'Gd': 1, 'Pids': {'1': ['46038'], '6': ['6908'], '8': ['7194'], '12': ['SBTP_320771']}, 'CoNm': 'South Korea', 'CoId': 'KOR', 'Shrt': {'Bs': '00db1a', 'Sl': '00db1a', 'Nmb': '030303', 'Sq': False, 'St': False, 'Hst': False, 'Spl': False, 'Sld': '000000'}}], 'T2': [{'Nm': 'Pohang Steelers', 'ID': '8103', 'tbd': 0, 'Img': 'enet/109373.png', 'EL': [], 'Gd': 1, 'Pids': {'1': ['109373'], '6': ['7650'], '8': ['8103'], '12': ['SBTP_10722']}, 'CoNm': 'South Korea', 'CoId': 'KOR', 'Shrt': {'Bs': '000000', 'Sl': 'ff0000', 'Nmb': 'ffffff', 'Sq': False, 'St': False, 'Hst': False, 'Spl': False}}], 'IncsX': 1, 'ComX': 1, 'LuX': 1, 'StatX': 1, 'SubsX': 1, 'SDFowX': 0, 'SDInnX': 0, 'Esd': 20210901170000, 'LuUT': 20210901170024, 'Eds': 20210901170022, 'Edf': 0, 'EO': 17279, 'Eact': 1, 'Stg': {'Sid': '5791', 'Snm': 'K-League 1', 'Sds': 'K-League 1', 'Scd': 'k-league-1', 'Cid': '111', 'Cnm': 'Republic of Korea', 'Csnm': 'Republic of Korea', 'Ccd': 'korea-republic', 'Ccdiso': 'KOR', 'Scu': 0, 'Chi': 0, 'Shi': 0, 'Sdn': 'K-League 1'}, 'Ehid': 0, 'Sids': {'1': '871839', '6': '54718', '8': '5791', '12': 'SBTC3_90093'}, 'Pid': 8, 'Spid': 1}]}]}
