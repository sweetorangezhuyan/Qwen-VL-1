def get_heji_json(data_csv,save_path):
    prompt='请输出该笔记的集数。'
    all_lists=[]
    data=pd.read_csv(data_csv)#data.drop_duplicates(keep='first')
    for i, row in tqdm.tqdm(data.iterrows()):
        data_row={}
        data_row['id']=row['note_id']
        images=eval(row['image_url_list'])#[0]

        images_str=''
        for ii,url in enumerate(images):
            if ii>1:
                break
            str_i="Picture {}: <img>".format(ii+1)+url+"</img> \n "
            images_str+=str_i
        title=row['note_title']
        content=row['note_content']
        ground_true=row['label']
        ocr=str(row['ocr_content'])
        content_str="笔记内容："+str(content )+"\n "
        title_str="笔记标题为："+str(title)+"\n "
        ocr_str="图像文本："+str(ocr)+"\n "
        conver=[]
        conver_data_1={}
        conver_data_2={}
        conver_data_1['from']='user'
        conver_data_1['value']=images_str+title_str+content_str+ocr_str+prompt
        # print(conver_data_1['value'])
        conver_data_2['from']='assistant'
        conver_data_2['value']= str(ground_true)
        conver.append(conver_data_1)
        conver.append(conver_data_2)
        data_row['conversations']=conver
        all_lists.append(data_row)
    json_str = json.dumps(all_lists,ensure_ascii=False)
    with open(save_path,'w',encoding='utf-8') as f:
        f.write(json_str)
