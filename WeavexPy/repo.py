from pathlib import Path
import html

class __select_repository__:
    def __init__(self, repo, root):
        self.repo = Path(repo)
        self.root = root
        self.list = self.read()
        self.inter()

    def read(self):
        def r(dic):
            dicS = str(dic.resolve().relative_to(Path.cwd())).replace('\\', '/')
            l = {dicS : []}

            for item in sorted(dic.iterdir()):
                if item.is_dir():
                    
                    l[dicS].append(r(item))
                else:
                    l[dicS].append(str(item.resolve().relative_to(Path.cwd())).replace('\\', '/'))
                    
            return l

        return r(self.repo)
    

    def inter(self):
        def Int(dic):
            for k in dic.keys():
                html_content = f'''
        <style>
            body {{ padding: 10px; font-family: Verdana, Geneva, Tahoma, sans-serif; }}
            .folder {{ color: blue; text-decoration: none; }}
        </style>
        <h1>Página: {k.replace('/', ' / ')}</h1><hr>'''

                for c in dic[k]:
                    if not isinstance(c, dict):
                        try:
                            with open(c, 'r', encoding='utf-8', errors='replace') as C:
                                conteudo_arquivo = C.read()
                                conteudo = html.escape(conteudo_arquivo)
                                self.root.pages[c] = f'<pre><code>\n{conteudo}\n</pre></code>'
                        except Exception as e:
                            self.root.pages[c] = f"Erro ao ler arquivo: {e}"

                        f = Path(c)

                        if f.suffix == '.html':
                            self.root.pages[c.replace(f.suffix, '')] = conteudo_arquivo
                        elif f.suffix == '.js':
                            self.root.pages[c.replace(f.suffix, '')] = f'''<script>\n{conteudo_arquivo}\n</script>'''
                        elif f.suffix == '.bry':
                            self.root.pages[c.replace(f.suffix, '')] = f'''
<!DOCTYPE html>
<html>
<head>
    <script src="https://cdn.jsdelivr.net/npm/brython@3.11.0/brython.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/brython@3.11.0/brython_stdlib.js"></script>
</head>
<body onload="brython()">
    <script type="text/python">
from browser import document, alert, html

# Conteúdo original do arquivo .py:
{conteudo_arquivo}
    </script>
</body>
</html>'''

                        html_content += f'📄 [FILE] > <a href="{self.root.url}/{c}" class="folder">{c}</a><br>'
                        
                    else:
                        for k2 in c.keys():
                            Int(c)
                            html_content += f'📁 [DIR] > <a href="{self.root.url}/{k2}" class="folder">{k2} /</a><br>'

                self.root.pages[k] = html_content

        Int(self.list)

