import difflib

with open("C:\\Users\\wasim\\OneDrive\\Desktop\\Automation\\Devices\\host.txt","r") as do:
    " Return list of device "
    host=do.read().splitlines()

for device in host:
    with open("C:\\Users\\wasim\\OneDrive\\Desktop\\Automation\\Pre-Check\\" + device + ".txt", "r") as pre_obj:
        pre=pre_obj.readlines()
    with open("C:\\Users\\wasim\\OneDrive\\Desktop\\Automation\\Post-Check\\" + device + ".txt", "r") as post_obj:
        post=post_obj.readlines()
    difference=difflib.HtmlDiff(wrapcolumn=80).make_file(pre,post,fromdesc="PRE",todesc="POST")

    with open("C:\\Users\\wasim\\OneDrive\\Desktop\\Automation\\HTMLReport\\"+"Pre_Post_Diff_check.html","w") as difference_report:
        difference_report.write(difference)