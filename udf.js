function transform(line) {
    var values = line.split(',');
    var obj = new Object();
    obj.copyright = values[0];
    obj.date = values[1];
    obj.explanation = values[2];
    obj.hdurl = values[3];
    obj.media_type = values[4];
    obj.service_version = values[5];
    obj.title = values[6];
    obj.url = values[7];
    var jsonString = JSON.stringify(obj);
    return jsonString;
   }


   
   
   
   
   
   
   
   