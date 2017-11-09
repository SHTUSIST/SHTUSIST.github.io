def operator(s,l):
    s=s.split("],")

    connector=s[2]

    connector=connector.replace("""connectors":[""","")
    connector=connector.replace("\n","")
    connector=connector.replace(" ","")
    connector=connector.split("},")

    D,E,F=[],[],[]
    for i in connector:
        mao=i.find(":")+2  
        device=s[1]

        dian=i.find(".")

        inn=i[mao:dian]


        mao2=i.find(":",mao+1)+2
        dian2=i.find(".",dian+1)


        inn2=i[mao2:dian2]


        for i in l:
            if inn==i[0].lower():
             
                
                D.append(i)
                break;
        for i in l:
            if inn2==i[0].lower():

                E.append(i)
                break;

    ss=""
    for i in range(len(D)):
        ss=ss+"""
G1 Z80
G1 """+E[i][1]+" "+E[i][2]

        ss=ss+"""
G1 Z0
G1 E100
G1 Z80
G1 """+D[i][1]+" "+D[i][2]
        ss=ss+"""
G1 Z0
G1 E200"""
     
    print(ss[1:])

    f=open('f.txt','w') 
    f.write(ss[1:])
    f.close()
        
    
        

        
    
    









s="""{
  "width":800,
  "height":400,
  "showToolbox":true,
  "toolbox":[
    {"type":"In"},
    {"type":"Out"},
    {"type":"Joint"},
    {"type":"DC"},
    {"type":"LED","color":"#00BFFF","label":"LED(B)"},
    {"type":"PushOff"},
    {"type":"PushOn"},
    {"type":"Toggle"},
    {"type":"BUF"},
    {"type":"NOT"},
    {"type":"AND"},
    {"type":"NAND"},
    {"type":"OR"},
    {"type":"NOR"},
    {"type":"EOR"},
    {"type":"ENOR"},
    {"type":"OSC"},
    {"type":"7seg"},
    {"type":"16seg"},
    {"type":"4bit7seg"},
    {"type":"RotaryEncoder"},
    {"type":"BusIn"},
    {"type":"BusOut"},
    {"type":"RS-FF"},
    {"type":"JK-FF"},
    {"type":"T-FF"},
    {"type":"D-FF"},
    {"type":"8bitCounter"},
    {"type":"HalfAdder"},
    {"type":"FullAdder"},
    {"type":"4bitAdder"},
    {"type":"2to4BinaryDecoder"},
    {"type":"3to8BinaryDecoder"},
    {"type":"4to16BinaryDecoder"},
    {"type":"Transmitter"},
    {"type":"DSO"},
    {"type":"Delay"}
  ],
  "devices":[
    {"type":"BUF","id":"dev0","x":56,"y":104,"label":"BUF"},
    {"type":"BUF","id":"dev1","x":136,"y":104,"label":"BUF"},
    {"type":"BUF","id":"dev2","x":304,"y":104,"label":"BUF"},
    {"type":"BUF","id":"dev3","x":248,"y":96,"label":"BUF"},
    {"type":"NOT","id":"dev4","x":376,"y":104,"label":"NOT"},
    {"type":"NOT","id":"dev5","x":472,"y":104,"label":"NOT"},
    {"type":"NOT","id":"dev6","x":112,"y":200,"label":"NOT"},
    {"type":"NOT","id":"dev7","x":216,"y":192,"label":"NOT"},
    {"type":"NOT","id":"dev8","x":288,"y":192,"label":"NOT"},
    {"type":"BUF","id":"dev9","x":352,"y":200,"label":"BUF"}
  ],
  "connectors":[
    {"from":"dev0.in0","to":"dev1.out0"},
    {"from":"dev2.in0","to":"dev3.out0"},
    {"from":"dev5.in0","to":"dev4.out0"},
    {"from":"dev7.in0","to":"dev6.out0"},
    {"from":"dev9.in0","to":"dev8.out0"}
  ]
}"""
l=[['DEV0', 'X34', 'Y127'], ['DEV1', 'X70', 'Y127'], ['DEV2', 'X34', 'Y90'], ['DEV3', 'X70', 'Y90'], ['DEV4', 'X105', 'Y127'], ['DEV5', 'X143', 'Y127'], ['DEV6', 'X105', 'Y90'], ['DEV7', 'X143', 'Y90'], ['DEV8', 'X178', 'Y127'], ['DEV9', 'X178', 'Y90'],['DEV10', 'X178', 'Y90']]

operator(s,l)