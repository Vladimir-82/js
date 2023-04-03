from zipfile import ZipFile

with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()
    print(max(map(lambda x: x.compress_size / x.file_size, info)))
    # print([x.filename for x in info if  ])
