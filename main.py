import os
import gifos

# Inicializa o terminal do gifos
t = gifos.Terminal(width=320, height=240, xpad=5, ypad=5)

# O gifos busca automaticamente a variável 'GITHUB_TOKEN' do ambiente do sistema
github_stats = gifos.utils.fetch_github_stats(
    user_name="jeffersonverus"
)

t.gen_text(text=f"GitHub Name: {github_stats['name']}", row_num=1)
t.gen_text(text=f"Public Repos: {github_stats['public_repos']}", row_num=2)

# Gera o arquivo de saída (ex: output.gif)
t.gen_gif()
