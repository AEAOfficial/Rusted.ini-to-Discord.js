import os
from os import path
import glob, os
import sys
try:
    from os import scandir
except ImportError:
    from scandir import scandir


err1 = 'No stats inputed'
count = 0
cnt = 0

somestats = [] 
# DEFAULT STATS TO BE USED
defstats  = [ " displayText: ",
              " displayDescription: ",
              " maxHp: ",
              " maxShield: ",
              " price: ",
              " buildSpeed: ",
              " maxAttackRange: ",
              " directDamage: ",
              " areaDamage: ",
              " moveSpeed: "
              " maxTurnSpeed: "
              ]

# DEFAULT PATHS TO BE USED
defpath = './input/MOD'

outpath = './output'


# PROMPT FOR GENERATION
unit_stats = input(">>> PRESS ENTER TO GENERATE UNIT JS FILES \n") # INPUT STRINGS TO BE FOUND SEPERATED BY COMMAS
if (unit_stats): # CHECKS FOR THE STAT INPUT IF ANY

    somestats.append(unit_stats)
    print(somestats[0])
    
else:
    print('>>> Umm uh..')
    
print('> Executing main process...')
# FIND ALL DIRECTORIES IN THE DEFAULT PATH
# CHEERS TO https://stackoverflow.com/users/68707/ben-hoyt FOR THIS GLORIOUS CODE SNIPPET

def scantree(path):
    """Recursively yield DirEntry objects for given directory."""
    for entry in scandir(path):
        if not entry.name.startswith('.') and entry.is_dir(follow_symlinks=False):
            yield from scantree(entry.path)  # see below for Python 2.x
        else:
            yield entry

if __name__ == '__main__':
    for entry in scantree(sys.argv[1] if len(sys.argv) > 1 else '.'):

        # PRINT ALL THE INI FILES AND COUNT THEM
        if entry.is_file() and entry.name.endswith('.ini'):

            count = count + 1      
            print(count, entry.path)
            # WRITE THE JS FILES IN OUTPUT
            with open(entry.path, encoding="utf8") as file:
                name = False
                one = False
                two = False
                three = False
                four = False    
                for line in file:
                    #DECLARE VARIABLES 
                  
                    if not name == True:

                        if 'name: ' in line:
                            if not ',' in line:
                                        fs = open('./output/'+entry.name+'.js',"a+")
                                        ini = line.split('name:')[1].replace("c_","").replace("cexper","exper")
                                        fs.write("exports.code = function(){ \n")
                                        fs.write("    client.on('message', message => {\n")
                                        fs.write("            if (message.content.toLowerCase() === " + f"'{ini}".replace(" ","").lower().rstrip() + "') { \n")
                                        fs.write("              if(message.author.bot) return; \n")
                                        fs.write("              message.channel.send(" + f"{ini}".replace(" ","").rstrip() + "); \n")
                                        fs.write("	          }\n")
                                        fs.write("	  });\n")
                                        fs.write("const " + f"{ini}".replace(" ","").replace("-", "").rstrip() + " = new Discord.MessageEmbed()")
                                        fs.write(" \n   .setColor('#1500f7') \n")
                                        fs.write("   .setAuthor('Lemons#5444', 'https://imgur.com/6NICs3U.png') \n")
                                        fs.write("   .setThumbnail('https://cdn.discordapp.com/icons/606586202942079017/7eafb97b0aa80cecb8e4a9f0a7f87c21.webp?size=128')\n")
                                        fs.write("   //.attachFiles(['./resources/" + f"{ini}".replace(" ","").rstrip() +".png']) \n")
                                        fs.write("   //.setImage('attachment://" + f"{ini}".replace(" ","").rstrip() +".png') \n")
                                        name = True
                    if not one == True:
                        if 'displayText:' in line:
                                            fs = open('./output/'+entry.name+'.js',"a+")
                                            dt = line.split('displayText:')[1]
                                            fs.writelines(f"   .setTitle('{dt}".rstrip() + "') \n")

                        elif 'displayDescription:' in line:
                                            fs = open('./output/'+entry.name+'.js',"a+")
                                            dd = line.split('displayDescription:')[1].replace("'","")
                                            fs.writelines(f"   .setDescription('{dd}".rstrip() + "') \n")
                                            fs.writelines("   .addField('Stats','__________________') \n")
                                            one = True
                    if not two == True:
                        if 'maxHp:' in line:
                                            fs = open('./output/'+entry.name+'.js',"a+")
                                            hp = line.split('maxHp:')[1]
                                            fs.writelines(f"   .addField('Health: {hp}".rstrip() + "','__________________')\n")

                        elif 'maxShield:' in line:
                                            fs = open('./output/'+entry.name+'.js',"a+")
                                            ms = line.split('maxShield:')[1]
                                            fs.writelines(f"   .addField('Shield: {ms}".rstrip() + "','__________________')\n")
                                            two = True
                                            

                    if not three == True:
                            if 'directDamage:' in line:
                                                fs = open('./output/'+entry.name+'.js',"a+")
                                                dmg = line.split('directDamage:')[1]
                                                fs.writelines(f"   .addField('Direct Damage: {dmg}".rstrip() + "','__________________')\n") 

                            elif 'areaDamage:' in line:
                                                fs = open('./output/'+entry.name+'.js',"a+")
                                                admg = line.split('areaDamage:')[1]
                                                fs.writelines(f"   .addField('Area Damage: {admg}".rstrip() + "','__________________')\n") 

                            elif 'maxAttackRange:' in line:
                                                fs = open('./output/'+entry.name+'.js',"a+")
                                                rg = line.split('maxAttackRange:')[1]
                                                fs.writelines(f"   .addField('Range: {rg}".rstrip() + "','__________________')\n") 
                                                
                            elif 'moveSpeed:' in line:
                                                fs = open('./output/'+entry.name+'.js',"a+")
                                                mvs = line.split('moveSpeed:')[1]
                                                fs.writelines(f"   .addField('Move Speed: {mvs}".rstrip() + "','__________________')\n")
                                                three = True 
                    if not four == True:
                            if 'buildSpeed' in line:
                                            fs = open('./output/'+entry.name+'.js',"a+")
                                            bs = line.split('buildSpeed:')[1]
                                            fs.writelines(f"   .addField('Build Speed: {bs}".rstrip() + "','__________________')\n")

                            elif 'price:' in line:
                                            fs = open('./output/'+entry.name+'.js',"a+")
                                            pr = line.split('price:')[1]
                                            fs.writelines(f"   .addField('Price: {pr}".rstrip() + "','__________________')\n")
                                            four = True
                        
                    elif 'maxTurnSpeed:' in line:
                                            fs = open('./output/'+entry.name+'.js',"a+")
                                            mts = line.split('maxTurnSpeed:')[1]
                                            fs.writelines(f"   .addField('Turn Speed: {mts}".rstrip() + "','__________________')\n")   
                fs = open('./output/'+entry.name+'.js',"a+")
                fs.writelines("   .setTimestamp() \n")
                fs.writelines("   .setFooter('SkaarjLord', 'https://cdn.discordapp.com/avatars/287608141191970817/6d82a2d09c9b2323f453abf5bfaaa588.png?size=128'); \n") 
                fs.writelines("}\n")

                fs = open('./output/!8128316LOADER.js',"a+")
                cnt = cnt + 1
                fs.write("var loader" + f"{count}" + " = require('./units/" + entry.name + ".js');\n")
                fs.writelines("loader" + f"{count}" + ".code()\n")  
                fs.close()
                
                