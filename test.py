from datetime import date, timedelta, datetime

# 定义起始和结束日期
start_date = date(2026, 3, 26)
end_date = date(2026, 4, 25)
# aa=datetime(2026, 4, 15,12,12,1)

# 定义SQL模板
# sql_template = """
# INSERT INTO zb_mro_sj_xc_sbxjjl (BBM, SBBH, SBMC, SBGGXH, SSDW, SSDWMC, SSZJD, SSZJDMC, XJSJ, XJJG, YXQK, DQGK, XJRY, GXR, GXSJ, FJXX, BC, BZ, sjrq, XXJSL) select uuid() BBM, SBBH, SBMC, SBGGXH, SSDW, SSDWMC, SSZJD, SSZJDMC, DATE_ADD(xjsj,INTERVAL {addDay} DAY) XJSJ, XJJG, YXQK, DQGK, XJRY, GXR, GXSJ, FJXX, BC, BZ, '{target_date}' sjrq, XXJSL from zb_mro_sj_xc_sbxjjl where sjrq='2026-04-14';
# INSERT INTO zb_mro_sj_xc_xdjcjl (BBM, SSDW, SSDWMC, SSZJD, SSZJDMC, XDFLBM, XDFLMC, JCSJ, JCJG, JCRY, GXR, GXSJ, BC, BZ, sjrq, XJCDSL) select uuid() BBM, SSDW, SSDWMC, SSZJD, SSZJDMC, XDFLBM, XDFLMC, DATE_ADD(JCSJ,INTERVAL {addDay} DAY) JCSJ, JCJG, JCRY, GXR, GXSJ, BC, BZ, '{target_date}' sjrq, XJCDSL from zb_mro_sj_xc_xdjcjl where sjrq='2026-04-14';
#                """
#
# sql_template = """
# update  zb_mro_bb_bxd a INNER JOIN (select bbfl,shr from (select bbfl,shr FROM zb_mro_bb_bxd where sjrq='2026-04-14' GROUP BY bbfl) t) b on a.bbfl=b.bbfl set a.shr=b.shr where a.sjrq='{target_date}';
# update  zb_mro_bb_yzjjb1 a INNER JOIN (select bbfl,shr from (select bbfl,shr FROM zb_mro_bb_yzjjb1 where sjrq='2026-04-14' GROUP BY bbfl) t) b on a.bbfl=b.bbfl set a.shr=b.shr where a.sjrq='{target_date}';
# update  zb_mro_bb_yzjjb2 a INNER JOIN (select bbfl,shr from (select bbfl,shr FROM zb_mro_bb_yzjjb2 where sjrq='2026-04-14' GROUP BY bbfl) t) b on a.bbfl=b.bbfl set a.shr=b.shr where a.sjrq='{target_date}';
# update  zb_mro_bb_sbrsc a INNER JOIN (select SBBM,shr from (select SBBM,shr FROM zb_mro_bb_sbrsc where sjrq='2026-04-14' GROUP BY SBBM) t) b on a.SBBM=b.SBBM set a.shr=b.shr where a.sjrq='{target_date}';
#                """

sql_template = """
INSERT INTO zb_mro_bb_bxd (BBM, SJRQ, JDBM, XDFLBM, XBM, XMC, XDBM, XDMC, JCRY, FZR, BC, XDZT, YCNR, ZBSJ, TBSJ, TBZT, TBR, SHSJ, SHR, SJBB, GXR, GXSJ, BBFL, BZ)
select CONCAT(XDBM,'_',DATE_FORMAT(sjrq,'%Y%m%d'),'_',bbfl,'_',0,'_0') as BBM, SJRQ, JDBM, XDFLBM, XBM, XMC, XDBM, XDMC, JCRY, FZR,'白班' BC,'√' XDZT, YCNR, ZBSJ, TBSJ, TBZT, TBR, SHSJ, SHR, SJBB, GXR, GXSJ, BBFL, BZ FROM
zb_mro_bb_bxd 
where sjrq='{sjrq}' and bc='夜班'  and XDBM not in (select XDBM FROM zb_mro_bb_bxd where sjrq='{sjrq}' and bc='白班' );
INSERT INTO zb_mro_bb_bxd (BBM, SJRQ, JDBM, XDFLBM, XBM, XMC, XDBM, XDMC, JCRY, FZR, BC, XDZT, YCNR, ZBSJ, TBSJ, TBZT, TBR, SHSJ, SHR, SJBB, GXR, GXSJ, BBFL, BZ)
select CONCAT(XDBM,'_',DATE_FORMAT(sjrq,'%Y%m%d'),'_',bbfl,'_',1,'_0') as BBM, SJRQ, JDBM, XDFLBM, XBM, XMC, XDBM, XDMC, JCRY, FZR,'夜班' BC,'√' XDZT, YCNR, ZBSJ, TBSJ, TBZT, TBR, SHSJ, SHR, SJBB, GXR, GXSJ, BBFL, BZ FROM
zb_mro_bb_bxd 
where sjrq='{sjrq}' and bc='白班' and XDBM not in (select XDBM FROM zb_mro_bb_bxd where sjrq='{sjrq}' and bc='夜班' );
"""




current_date = start_date
print(f"-- 生成时间范围: {start_date} 到 {end_date}")
addday=1
while current_date <= end_date:
    date_str = current_date.strftime('%Y-%m-%d')

    # 1. 生成“白班”逻辑的SQL (从夜班补白班，flag=0)
    # 逻辑：找当天是夜班的，且XDBM不在当天白班列表里的记录
    sql_baiban = sql_template.format(

        # addDay=addday,
        sjrq=date_str,
    )

    # 2. 生成“夜班”逻辑的SQL (从白班补夜班，flag=1)
    # 逻辑：找当天是白班的，且XDBM不在当天夜班列表里的记录
    # sql_yeban = sql_template.format(
    #     flag=1,
    #     banci='夜班',
    #     target_date=date_str,
    #     source_banci='白班',
    #     target_banci='夜班'
    # )
    addday+=1
    print(f"-- 日期: {date_str}")
    print(sql_baiban)
    # print(sql_yeban)

    # 日期递增
    current_date += timedelta(days=1)