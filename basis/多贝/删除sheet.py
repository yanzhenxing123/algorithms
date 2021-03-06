"""
@Author: yanzx
@Date: 2021-09-29 13:17:22
@Desc: 
"""
from larksuiteoapi import DOMAIN_FEISHU, DefaultLogger, LEVEL_DEBUG
from loguru import logger
from larksuiteoapi import DOMAIN_FEISHU, Config, LEVEL_DEBUG, DefaultLogger

from feishu_sheet import get_sheet_id, app_settings
from larksuiteoapi.service.sheets.v2 import Service as SheetsService, model

conf = Config.new_config_with_memory_store(DOMAIN_FEISHU, app_settings, DefaultLogger(), LEVEL_DEBUG)
service = SheetsService(conf)


def delete_sheet():
    sheet_tokens = {
        # "活跃用户版本分布 副本": "shtcnUz8rLfgcvcgYVqullxNI4K",
        # "同视-在网客户活跃度明细-日报 副本": "shtcnxvX6ykAxm9xABJFlwREU5f",
        # "同视-在网用户活跃度明细-日报 副本": "shtcnOSfPD3ayNM7xszPBUEpbkf",
        "同视-在网终端APP客户活跃度明细-日报 副本": "shtcnDzDQe79SuWub3y90FddxZb",
        "同视-在网PC APP客户活跃度明细-日报 副本": "shtcnbKLM6Xxam7ExVgxyuisWSf",
    }

    yunying_data_sheet_tokens = {
        "活跃用户版本分布 副本": "shtcnp3sz3lWycDd2jaU3iPEXBh",
        "同视-在网客户活跃度明细-日报 副本": "shtcno8zq0d8igD5nUc5rTS7tEg",
        "同视-在网用户活跃度明细-日报 副本": "shtcnOSfPD3ayNM7xszPBUEpbkf",
        "同视-在网终端APP客户活跃度明细-日报 副本": "shtcn1dCMCNJE77ZOODB8pS6VVh",
        "同视-在网PC APP客户活跃度明细-日报 副本": "shtcnP6Yo5KtMIulGEx4kTjzefA",
    }
    for excel_name, sheet_token in sheet_tokens.items():
        # 删除 7月1日 - 9月30日
        for i in [
            # 3, 4,
            5, 6, 10,
            11]:
            for j in range(1, 32):
                sheet_name = str(i) + "月" + str(j) + "日"
                sheet_id = get_sheet_id(sheet_name, sheet_token)
                if sheet_id is None:
                    continue
                print(excel_name + " " + sheet_name)
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


if __name__ == '__main__':
    delete_sheet()
