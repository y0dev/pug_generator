from lib.pug_manager import Pug_Manager

pm = Pug_Manager()
meta_links = {'twitter:card': 'summary_large_image', 'twitter:site': '@_yodev_',
              'og:url': 'https://www.devontaereid.com', 'og:type': 'website'}

headshot = 'headshot.png'
post_image = 'https://www.history.com/.image/ar_1:1%2Cc_fill%2Ccs_srgb%2Cfl_progressive%2Cq_auto:good%2Cw_1200/MTU3ODc4NjAzNzg5NDQ0NDI1/list-seal-missions-navy-seal-photos-beach-assualt-1708498496-o-3.jpg'
link = '#'
body_class = ['post-body']

# Header
pm.addTitle('Devontae Reid')
pm.addDescription('some description')

pm.addCSS()
pm.addIcon()
pm.addMeta(meta_links)

# Body

first_level_body_idn = pm.indent(2)
second_level_body_idn = pm.indent(3)
third_level_body_idn = pm.indent(4)
fourth_level_body_idn = pm.indent(5)
fifth_level_body_idn = pm.indent(6)
sixth_level_body_idn = pm.indent(7)
seventh_level_body_idn = pm.indent(8)
eighth_level_body_idn = pm.indent(9)
ninth_level_body_idn = pm.indent(10)

lines = []

lines.append(f'{first_level_body_idn}div.{body_class[0]}')
lines.append(f'{second_level_body_idn}article.button#post-container')
lines.append(f'{second_level_body_idn}div.post-header-container')
lines.append(f'{third_level_body_idn}div.post-header-details')
lines.append(f'{fourth_level_body_idn}h1#post-header-title')
lines.append(f'{fourth_level_body_idn}div.post-header-meta')
lines.append(
    f'{fifth_level_body_idn}img.post-header-icon(src="{headshot}" alt="headshot")')
lines.append(
    f'{fifth_level_body_idn}p.post-header-time Thursday, October 6, 2022')
lines.append(f'{fifth_level_body_idn}span.post-header-divider |')
lines.append(
    f'{fifth_level_body_idn}button.post-header-shareButton#shareButton')
lines.append(f'{sixth_level_body_idn}span.post-header-shareButton-icon')
lines.append(f'{seventh_level_body_idn}i.fa-light.fa-share-nodes.')
lines.append(f'{seventh_level_body_idn}Share')

# Tags
tags = ['Phone', 'Dog', 'Okay']
lines.append(f'{fourth_level_body_idn}div.post-header-tags')
lines.append(f'{sixth_level_body_idn}span.post-header-tag {tags[0]}')
lines.append(f'{sixth_level_body_idn}span.post-header-tag {tags[1]}')
lines.append(f'{sixth_level_body_idn}span.post-header-tag {tags[2]}')

# Post Content
lines.append(f'{second_level_body_idn}div.post-content')
lines.append(f'{third_level_body_idn}div.post-section-container')
lines.append(f'{fourth_level_body_idn}h2 Post Title')

# Paragraphs
lines.append(f'{fourth_level_body_idn}div.post-container')
lines.append(f'{fifth_level_body_idn}p.post-details')
# Add Link finder
lines.append(f'{fifth_level_body_idn}a.post-link(href="{link}") text')
lines.append(f'{fifth_level_body_idn}div.post-image-container')
lines.append(
    f'{sixth_level_body_idn}a.post-image-container(href="{link}") text')
lines.append(
    f'{seventh_level_body_idn}img.post-image(src="{post_image}" alt="post-image")')
lines.append(f'{sixth_level_body_idn}figcaption.post-image-caption Caption')
lines.append(f'{fifth_level_body_idn}pre.language-')
lines.append(f'{sixth_level_body_idn}code.language-')
lines.append(
    f'{fifth_level_body_idn}blockquote.post-quote(cite="") Blockquote')
lines.append(f'{fifth_level_body_idn}ol')
lines.append(f'{sixth_level_body_idn}li something')
lines.append(f'{sixth_level_body_idn}li something')
lines.append(f'{sixth_level_body_idn}li something')
lines.append(f'{fifth_level_body_idn}ul')
lines.append(f'{sixth_level_body_idn}li something')
lines.append(f'{sixth_level_body_idn}li something')
lines.append(f'{sixth_level_body_idn}li something')


pm.appendToBody(lines)
