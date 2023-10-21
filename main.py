import subprocess

def php(script_path):
    p = subprocess.Popen(['php', script_path], stdout=subprocess.PIPE)
    result = p.communicate()[0]
    return result


news_script_output = php("a.php") 
result = news_script_output.decode('utf-8')

print(result)
