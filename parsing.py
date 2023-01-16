import json
with open('example.json') as json_file:
    j = 0
    i = 0
    json_data = json.load(json_file)
    for i in range(len(json_data["frames"])):
        title = json_data["frames"][i]['image'][0:10]
        fileName = str(title) + ".txt"
        f= open(fileName,'w')
    #print(title)
    #f = open(title,'w')
        for j in range(len(json_data["frames"][i]['annotations'])):
            x = json_data["frames"][i]['annotations'][j]['label']['x']
            y = json_data["frames"][i]['annotations'][j]['label']['y']
            width = json_data["frames"][i]['annotations'][j]['label']['width']
            height = json_data["frames"][i]['annotations'][j]['label']['height']
            code = json_data["frames"][i]['annotations'][j]['category']['code']
            if code == 'wheelchair':
                code = 0
            elif code == 'person':
                code = 1
            elif code == 'drunk':
                code = 2
            elif code == 'child':
                code = 3
            elif code == 'merchant':
                code = 4
            elif code == 'blind':
                code = 5
            elif code == 'stroller':
                code = 6
            new_x = round((x+(width/2))/3840,6)
            new_y = round((y+(height/2))/2160,6)
            new_width = round(width / 3840,6)
            new_height = round(height /2160,6)
            print(str(new_x),str(new_y))
            
            
            txt = (str(code)+' '+str(new_x)+' '+str(new_y)+' '+str(new_width)+' '+str(new_height))
            f.write(txt)
            f.write('\n')

        f.close()#

        print(len(json_data["frames"][i]['annotations']))
