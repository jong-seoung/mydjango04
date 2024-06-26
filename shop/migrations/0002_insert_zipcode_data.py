# Generated by Django 4.2.7 on 2023-12-14 06:08

import csv
from typing import Dict, Iterator, Tuple

from django.db import migrations


CSV_PATH = "shop/assets/zipcode_db/20231205/서울특별시.txt"


def get_code_and_name_from_csv(zipcode_csv_path: str) -> Iterator[Tuple[str, str]]:
    """CSV 파일에서 우편번호, 시도, 시군구, 도로명을 읽어서, 우편번호와 주소를 생성합니다.
    :param zipcode_csv_path: 우편번호 CSV 파일 경로
    :return: 우편번호, 주소 튜플을 생성(yield)합니다.
    """

    with open(zipcode_csv_path, "rt", encoding="utf-8-sig") as csvfile:
        csv_reader = csv.DictReader(csvfile, delimiter="|")

        row: Dict
        for row in csv_reader:
            code = row["우편번호"]
            name = "{시도} {시군구} {도로명}".format(**row)
            yield code, name


def add_zipcode_data(apps, schema_editor):
    ZipCode = apps.get_model("shop", "ZipCode")

    # Generator Expression
    #  - 리스트로 변환하기보다 "제너레이터 표현식"을 활용하면
    #    메모리도 아끼고 보다 빠르게 작업을 시작할 수 있습니다.
    zipcode_list = (
        ZipCode(code=code, name=name)
        for code, name in get_code_and_name_from_csv(CSV_PATH)
    )

    # 배치 크기 단위로 INSERT 쿼리를 모아서 실행
    ZipCode.objects.bulk_create(zipcode_list, batch_size=1000)


def remove_zipcode_data(apps, schema_editor):
    ZipCode = apps.get_model("shop", "ZipCode")
    ZipCode.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(add_zipcode_data, remove_zipcode_data),
    ]