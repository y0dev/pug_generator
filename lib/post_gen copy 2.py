from .pug_manager import Pug_Manager, indentList


class Post_Generator:
    def __init__(self, title: str = 'Sample', description: str = 'Sample Description', post_type: str = 'article', json_obj: dict = {}) -> None:
        if len(json_obj) == 0:
            post_page_filename = 'main.pug'
        else:
            post_page_filename = json_obj['id']

        self.post_type = post_type
        if self.post_type.lower() == 'article':
            self.pm = Pug_Manager(
                output_path='output/pug/articles', filename=f'{post_page_filename}')
        else:
            self.pm = Pug_Manager(
                output_path='output/pug/notes', filename=f'{post_page_filename}')

        self.lines = []
        self.tags = []
        self.id_list = indentList()
        self.title = title
        self.description = description
        self.code_script_added = False
        self.headshot = 'https://i.ibb.co/HY4dx9s/headshot.jpg'  # 'headshot.png'
        self.logo = '/images/logo.png'  # 'images/logo192.png'
        self.__getPostDetails(json_obj)
        self.__setupInitHead()

        self.__setupBody()

    def __getPostDetails(self, json_obj: dict):
        if len(json_obj) == 0:
            self.post_time = 'Thursday, October 6, 2022'
            self.post_info = {'date': 'Thursday, October 6, 2022'}
        else:
            from datetime import datetime
            self.post_info = json_obj
            self.title = self.post_info['title']
            if self.post_type.lower() == 'article':
                self.description = f'Blog post about {self.post_info["description"]}.'
            else:
                self.description = f'Note about {self.post_info["description"]}.'

            self.tags = self.post_info['tags']
            # Convert from js timestamp
            py_timestamp = int(self.post_info['date'])/1000.0
            # print(py_timestamp)
            self.post_info['date'] = datetime.fromtimestamp(
                py_timestamp).strftime("%A, %B %d, %Y")

    # Helper

    def __setupInitHead(self):
        meta_links = {'twitter:card': 'summary_large_image', 'twitter:site': '@_yodev_',
                      'og:url': 'https://www.devontaereid.com', 'og:type': 'website'}
        self.pm.addTitle(self.title)
        self.pm.addDescription(self.description)
        self.pm.addIcon(logo_filename='/images/logo.png')
        self.pm.addImage(
            f'https://www.devontaereid.com/{self.post_info["image"]["name"]}')
        self.pm.addMeta(meta_links)
        self.pm.addCSS()

    def __addNavBar(self):
        self.lines.append(
            f'{self.id_list[0]}div#nav-bar.navbar.header-content--mini')
        self.lines.append(f'{self.id_list[1]}nav')
        self.lines.append(f'{self.id_list[2]}div.main-menu')
        self.lines.append(f'{self.id_list[3]}a.menu-branding(href="/")')
        self.lines.append(
            f'{self.id_list[4]}img.menu-branding(src="{self.logo}" alt="branding-logo")')
        self.lines.append(f'{self.id_list[4]}h3 Devontae Reid')

        # Menu List
        self.lines.append(f'{self.id_list[3]}ul.menu-list')
        self.lines.append(f'{self.id_list[4]}li')
        self.lines.append(f'{self.id_list[5]}a(href="/about-me") About Me')
        self.lines.append(f'{self.id_list[4]}li')
        self.lines.append(f'{self.id_list[5]}a(href="/projects") Projects')
        self.lines.append(f'{self.id_list[4]}li')
        self.lines.append(f'{self.id_list[5]}a(href="/articles") Articles')
        self.lines.append(f'{self.id_list[4]}li')
        self.lines.append(f'{self.id_list[5]}button.display-switch ??????')

    def __addPostTags(self):

        self.lines.append(f'{self.id_list[3]}div.post-header-tags')
        for tag in self.tags:
            self.lines.append(f'{self.id_list[5]}span.post-header-tag {tag}')

    def __addPostContent(self):
        self.lines.append(f'{self.id_list[1]}div.post-content')
        for content in self.post_info['content']:
            self.lines.append(f'{self.id_list[2]}div.post-section-container')
            self.lines.append(
                f'{self.id_list[3]}h2 {content["title"]["text"]}')
            for paragraph in content['paragraphs']:
                self.__addContentParagraph(content, paragraph)

    # TODO: Need to finish
    def __addList(self, indent_level: int, items: list, list_type='ordered'):
        if list_type == 'unordered':
            self.lines.append(f'{self.id_list[indent_level]}ul')
        else:
            self.lines.append(f'{self.id_list[indent_level]}ol')

        for item in items:
            pass

    def __addCodeBlock(self, code_content: dict, ident_level=4):

        if not self.code_script_added:
            self.code_script_added = True

        self.lines.append(
            f'{self.id_list[ident_level]}div.code-snippet-container')
        self.lines.append(
            f'{self.id_list[ident_level + 1]}div.code-snippet-header')
        self.lines.append(
            f'{self.id_list[ident_level + 2]}h5.code-snippet-title {code_content["title"]}')
        self.lines.append(f'{self.id_list[ident_level + 2]}button.copy-bttn')
        self.lines.append(
            f'{self.id_list[ident_level + 3]}img.copy-icon(src="/images/copy-icon.png")')

        self.lines.append(
            f'{self.id_list[ident_level + 1]}div.code-snippet-body')
        self.lines.append(
            f'{self.id_list[ident_level + 2]}pre.language-{code_content["language"]}')
        # Remove . from end
        self.lines.append(
            f'{self.id_list[ident_level + 3]}code.language-{code_content["language"]}')
        for line in code_content["content"]:
            if ':comment ' in line:
                l_start = len(':comment ')
                idx_start = line.index(':comment')
                comment = line[idx_start + l_start:]
                # print(comment)
                self.lines.append(
                    f'{self.id_list[ident_level + 4]}span.code-comment {comment}')
                self.lines.append(f'{self.id_list[ident_level + 4]}br')
                continue

            code_line = line
            while ':code-specific ' in code_line or ':path ' in code_line:
                if ':code-specific ' in code_line:
                    l_start = len(':code-specific ')
                    l_end = len(' :end')

                    idx_start = code_line.index(':code-specific')
                    idx_end = code_line.index(':end')
                    code_specific = code_line[idx_start + l_start: idx_end]
                    # print(code_specific)
                    self.lines.append(
                        f'{self.id_list[ident_level + 4]}span.code-specific {code_specific}')
                    code_line = code_line[idx_end + l_end:]

                    if ':path ' in code_line:
                        l_start = len(':path-start ')
                        l_end = len(' :path-end')

                        idx_start = code_line.index(':path-start')
                        idx_end = code_line.index(':path-end')
                        file_path = code_line[idx_start + l_start: idx_end]
                        # print(file_path)
                        self.lines.append(
                            f'{self.id_list[ident_level + 4]}span.code-file-path {file_path}')
                        code_line = code_line[idx_end + l_end:]
                        if len(code_line) == 0:
                            self.lines.append(
                                f'{self.id_list[ident_level + 4]}br')
                        else:
                            self.lines.append(
                                f'{self.id_list[ident_level + 4]}.')
                            self.lines.append(
                                f'{self.id_list[ident_level + 5]}{code_line[idx_end + l_end:]}')
                            self.lines.append(
                                f'{self.id_list[ident_level + 4]}br')
                    else:
                        # print(f'Line {code_line}')
                        self.lines.append(f'{self.id_list[ident_level + 4]}.')
                        self.lines.append(
                            f'{self.id_list[ident_level + 5]}{code_line}')
                        self.lines.append(f'{self.id_list[ident_level + 4]}br')

    def __addContentParagraph(self, content: dict, paragraph: str):
        # print(paragraph)
        # Check for image in paragraph
        if ':imagePlace' in paragraph:
            img_id = paragraph[-4:-1]
            # print(l,idx,img_id)
            for image in content['images']:
                if image['id'] == img_id:
                    # print(image)
                    self.lines.append(
                        f'{self.id_list[4]}div.post-image-container')
                    self.lines.append(
                        f'{self.id_list[5]}a.post-image-container(href="{image["link"]}")')
                    self.lines.append(
                        f'{self.id_list[6]}img.post-image(src="{image["link"]}" alt="{image["alt"]}")')
                    self.lines.append(
                        f'{self.id_list[5]}figcaption.post-image-caption {image["caption"]}')

        elif ':linkPlace' in paragraph:
            l = len(':linkPlace(XYZ)')
            idx = paragraph.index(':linkPlace')
            link_location = paragraph[idx:idx + l]
            link_id = link_location[-4:-1]
            # Add the paragraph without the placeholder
            self.lines.append(
                f'{self.id_list[4]}p.post-details {paragraph[:idx]}')
            for link in content['links']:
                if link['id'] == link_id:
                    self.lines.append(
                        f'{self.id_list[5]}a.post-link(href="{link["link"]}") {link["text"]}')

        elif ':listPlace' in paragraph:
            l = len(':listPlace(XYZ)')
            idx = paragraph.index(':listPlace')
            code_location = paragraph[idx:idx + l]
            code_id = code_location[-4:-1]
            self.lines.append(
                f'{self.id_list[4]}p.post-details {paragraph[:idx]}')
            for code in content['lists']:
                if code['id'] == code_id:
                    if code['list_type'] == 'unordered':
                        self.lines.append(f'{self.id_list[4]}ul')
                    else:
                        self.lines.append(f'{self.id_list[4]}ol')

                    for item in code['items']:
                        # Check for sublist
                        if ':listPlace' in item:
                            idx = item.index(':listPlace')
                            code_location = item[idx:idx + l]
                            code_id = code_location[-4:-1]
                            self.lines.append(
                                f'{self.id_list[5]}li.post-list-item {item[:idx]}')
                            for sub_list in content['lists']:
                                if sub_list['id'] == code_id:
                                    if sub_list['list_type'] == 'unordered':
                                        self.lines.append(
                                            f'{self.id_list[6]}ul.sublist')
                                    else:
                                        self.lines.append(
                                            f'{self.id_list[6]}ol.sublist')
                                    for item in sub_list['items']:
                                        self.lines.append(
                                            f'{self.id_list[7]}li.post-sublist-item {item}')
                                    code_id = ''
                        elif ':codePlace' in item:

                            l = len(':codePlace(XYZ)')
                            idx = item.index(':codePlace')
                            code_location = item[idx:idx + l]
                            code_id = code_location[-4:-1]
                            self.lines.append(
                                f'{self.id_list[4]}p.post-details {item[:idx]}')
                            for code in content['code']:
                                if code['id'] == code_id:
                                    self.__addCodeBlock(code, ident_level=5)
                        elif ':user-defined-code' in item:
                            l_start = len(':user-defined-code')
                            l_end = len(':end')
                            idx_start = item.index(':user-defined-code')
                            idx_end = item.index(':end')
                            code_ = item[idx_start + l_start:idx_end]
                            self.lines.append(
                                f'{self.id_list[5]}li.post-list-item')
                            self.lines.append(
                                f'{self.id_list[6]}| {item[:idx_start]}')
                            self.lines.append(
                                f'{self.id_list[6]}span.user-define-code{code_}')  # this can
                            self.lines.append(
                                f'{self.id_list[6]}| {item[idx_end + l_end:]}')
                        # If there isn't a sublist present
                        else:
                            self.lines.append(
                                f'{self.id_list[5]}li.post-list-item {item}')

        elif ':codePlace' in paragraph:
            l_start = len(':codePlace(XYZ)')
            idx_start = paragraph.index(':codePlace')
            code_location = paragraph[idx_start:idx_start + l_start]
            code_id = code_location[-4:-1]
            self.lines.append(
                f'{self.id_list[4]}p.post-details {paragraph[:idx_start]}')
            for code in content['code']:
                if code['id'] == code_id:
                    self.__addCodeBlock(code)

        elif ':user-defined-code' in paragraph:
            l_start = len(':user-defined-code')
            l_end = len(':end')
            idx_start = paragraph.index(':user-defined-code')
            idx_end = paragraph.index(':end')
            code_ = paragraph[idx_start + l_start:idx_end]
            self.lines.append(f'{self.id_list[4]}p.post-details')
            self.lines.append(f'{self.id_list[5]}| {paragraph[:idx_start]}')
            self.lines.append(
                f'{self.id_list[5]}span.user-define-code{code_}')  # this can
            self.lines.append(
                f'{self.id_list[5]}| {paragraph[idx_end + l_end:]}')
        else:
            self.lines.append(f'{self.id_list[4]}p.post-details {paragraph}')
            # print(paragraph)

    def __addJavascriptFiles(self):
        self.pm.addJavascriptFile(js_filename='scripts/main.js')
        if self.code_script_added:
            self.pm.addJavascriptFile(js_filename='scripts/code_script.js')
        self.pm.addBibleJavascriptFile()

    def __setupBody(self):
        self.__addNavBar()
        self.lines.append(f'{self.id_list[0]}div.post-body')
        self.lines.append(f'{self.id_list[1]}article.button#post-container')
        self.lines.append(f'{self.id_list[1]}div.post-header-container')
        self.lines.append(f'{self.id_list[2]}div.post-header-details')
        self.lines.append(f'{self.id_list[3]}h1#post-header-title')
        self.lines.append(f'{self.id_list[3]}div.post-header-meta')
        self.lines.append(
            f'{self.id_list[4]}img.post-header-icon(src="{self.headshot}" alt="headshot")')
        self.lines.append(
            f'{self.id_list[4]}p.post-header-time {self.post_info["date"]}')
        self.lines.append(f'{self.id_list[4]}span.post-header-divider |')
        self.lines.append(
            f'{self.id_list[4]}button.post-header-shareButton#shareButton')
        self.lines.append(
            f'{self.id_list[5]}span.post-header-shareButton-icon')
        self.lines.append(
            f'{self.id_list[6]}img(src="/images/share_icon.png" alt="share_icon")')
        self.lines.append(f'{self.id_list[6]}.')
        self.lines.append(f'{self.id_list[7]}Share')

        self.__addPostTags()
        self.lines.append(
            f'{self.id_list[2]}img.post-header-image(src="/{self.post_info["image"]["name"]}" alt="{self.post_info["image"]["alt"]}")')

        self.__addPostContent()

        self.__addJavascriptFiles()

    def generatePugFile(self):
        self.pm.appendLinesToBody(self.lines)
