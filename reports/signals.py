import pandas as pd
from pathlib import Path

from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models import *
from unnamed_project import settings


@receiver(post_save, sender=ExcelFile)
def save_file_data(sender, instance, created, **kwargs):
    if created:
        file = instance
        excel_file = file.excel_file.url
        file_dir = str(settings.BASE_DIR) + excel_file
        data = pd.read_excel(file_dir, skiprows=3)
        df = pd.DataFrame(data)
        df = df.dropna(how='all')
        df_list = df.values.tolist()
        rows = [[str(j) for j in i] for i in df_list]
        cleaned_rows = [i for i in rows if i]

        for i in cleaned_rows:
            report = Report.objects.create(
                user=instance.user,
                excel_file=instance,
                tnved=str(i[0]),
                full_product_name=str(i[1]),
                trademark=str(i[2]),
                article_type=str(i[3]),
                article_value=str(i[4]),
                product_type=str(i[5]),
                color=str(i[6]),
                target_gender=str(i[7]),
                clothing_type=str(i[8]),
                clothing_value=str(i[9]),
                composition=str(i[10]),
                standard_no=str(i[11]),
                status=str(i[12])
            )
            report.save()
