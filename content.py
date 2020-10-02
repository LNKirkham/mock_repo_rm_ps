# Contributions-Importer-For-Github/run_script.py
import git
from git_contributions_importer import *

# Your private repo or Bitbucket repo
repo = git.Repo("/Users/louisekirkham/Documents/projects/production_scheduler/demand-forecast")

# Your mock repo
mock_repo = git.Repo("/Users/louisekirkham/Documents/my_projects/mock_repo_rm_ps")
importer = Importer([repo], mock_repo)

# I use both my personal email and work email here,
# Since the private repo uses work email, and Github profiles uses
# my work email
importer.set_author(['louisek@gmail.com', 'louise.kirkham@royalmail.com'])
importer.import_repository()
print("qshmd")
print("wriwm")
print("rivyf")
print("fnqso")
print("nurru")
print("dvoiq")
print("eaimx")
print("xlfkx")
print("aumcm")
print("ibjgq")
print("jvovo")
print("odgvd")
print("bxviy")
print("hkfob")
print("twool")
print("pnwss")
print("tnbpw")
print("veaxy")
print("blotp")
print("nuhuy")
print("qtjmm")
print("sigiw")
print("khkfh")
