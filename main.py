import sys
from general import *
from domain import *
from get_ip import *
from nmaper import *
from robots_txt import *
from whois import *


ROOT_DIR = 'companies'
create_dir(ROOT_DIR)

def splash():
    print("""              
              .o######0o.
             0###########0.      .
            o####" "######0.    (## m#o
            ####(    ######0  ._ ##.##"nn
            0####o   ###" ## (##o.######"
    o00o.    0#####o,##. ,#"  "#######(
  .0#####0.   0###########0     ########
 .0#######0.   "0#########"  _.o###'"00"
.0###########o._ ""################       _  .
0####" "#########################0      .0#0n0
#####.   ""#####################"    _  0#####
0#####.     "###################._.o##o.#####"
"0#####..##mn ""#############################
  "0#######""_    ""##################"#####"
     ""####m###m      ""############"   ####
    .########\"""         .########"     "##"
    ####"##"###o        (0######"        ""
    "##".###,##     .o#o ""####.
         "##"      .0############.
                 .n###############                """)
    print('\033[91m' + "                    Python Recon" + '\033[0m')
    print('\33[34m' + "                      By: Nick" + '\033[0m')
    print("Usage: <target name> <nmap options>  <target url>")
    print("Example: ")
    print("reddit -F https://www.reddit.com")

def main():
    global command
    global name
    global url
    action = ""
    
    if not len(sys.argv[1:]):
        splash()
    
    while(1<2):
        action = raw_input('\033[91m' + "pr>" + '\033[0m')
        args = action.split(" ")
        
        if len(args) == 3:
            try:
                get_info(args[0], args[1], args[2])
            except OSError:
                print("Invalid Parameters")
                usage()
       

def usage():
    print("Usage: <target name> <nmap options>  <target url>")
    print("Example: ")
    print("reddit -F www.reddit.com")    

def get_info(name, cmd, url):
    domain_name = get_domain_name(url)
    ip_address = get_ip(domain_name)
    nmap = get_nmap(str(cmd), ip_address)
    robots_txt = get_robots_txt(url)
    whois = get_whois (domain_name)
    create_report(name, url, domain_name, nmap, robots_txt, whois)

def create_report(name, full_url, domain_name, nmap, robots_txt, whois):
    project_dir = ROOT_DIR + '/' + name
    create_dir(project_dir)
    write_file(project_dir + '/full_url.txt', full_url)
    write_file(project_dir + '/domain_name.txt', domain_name)
    write_file(project_dir + '/nmap.txt', nmap)
    write_file(project_dir + '/robots.txt', robots_txt)
    write_file(project_dir + '/whois.txt', whois)


main()
