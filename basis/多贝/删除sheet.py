"""
@Author: yanzx
@Date: 2021-09-29 13:17:22
@Desc: 
"""
def delete_sheet():
    sheet_tokens = {
        # "活跃用户版本分布 副本": "shtcnp3sz3lWycDd2jaU3iPEXBh",
        # "同视-在网客户活跃度明细-日报 副本": "shtcno8zq0d8igD5nUc5rTS7tEg",
        # "同视-在网用户活跃度明细-日报 副本": "shtcnudbYagyp9q5TQYt3QWVTM0",
        # "同视-在网终端APP客户活跃度明细-日报 副本": "shtcn1dCMCNJE77ZOODB8pS6VVh",
        "同视-在网PC APP客户活跃度明细-日报 副本": "shtcnP6Yo5KtMIulGEx4kTjzefA",
    }

    yunying_data_sheet_tokens = {
        "活跃用户版本分布 副本": "shtcnp3sz3lWycDd2jaU3iPEXBh",
        "同视-在网客户活跃度明细-日报 副本": "shtcno8zq0d8igD5nUc5rTS7tEg",
        "同视-在网用户活跃度明细-日报 副本": "shtcnudbYagyp9q5TQYt3QWVTM0",
        "同视-在网终端APP客户活跃度明细-日报 副本": "shtcn1dCMCNJE77ZOODB8pS6VVh",
        "同视-在网PC APP客户活跃度明细-日报 副本": "shtcnP6Yo5KtMIulGEx4kTjzefA",
    }
    for sheet_token in sheet_tokens.values():
        # 删除 7月1日 - 9月30日
        for i in range(7, 10):
            for j in range(1, 32):
                sheet_id = get_sheet_id(str(i) + "月" + str(j) + "日", sheet_token)
                body = model.SpreadsheetsSheetsBatchUpdateReqBody([
                    {
                        "deleteSheet": {
                            "sheetId": sheet_id,
                        }
                    },
                ])
                req_call = service.spreadsheetss.sheets_batch_update(body=body)
                req_call.set_spreadsheetToken(sheet_token)
                resp = req_call.do()
                if resp.code != 200:
                    logger.error(f"msg={resp.msg}, code={resp.code}")