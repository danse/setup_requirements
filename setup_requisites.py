import re
import random

def convert_req(req, use_random=True):
    '''
    >>> req = 'svn+svn://svn.myserver.com/repos/myproject_mail/'
    >>> r = convert_req(req)
    >>> len(r)
    2
    >>> r['install_requires'] #doctest: +ELLIPSIS
    '...'
    >>> r['dependency_links'] #doctest: +ELLIPSIS
    'svn+svn://svn.myserver.com/repos/myproject_mail/#egg=...-dev'
    >>> r = convert_req(req, use_random=False)
    >>> r['install_requires']
    'svnsvnsvnmyservercomreposmyproject_mail'
    >>> r['dependency_links']
    'svn+svn://svn.myserver.com/repos/myproject_mail/#egg=svnsvnsvnmyservercomreposmyproject_mail-dev'
    '''
    r = {}
    if use_random: fake_package_name = str(random.randrange(1000000))
    else:          fake_package_name = re.sub('\W', '', req)
    r['install_requires'] = fake_package_name
    r['dependency_links'] = '{0}#egg={1}-dev'.format(req, fake_package_name)
    return r

def convert(reqs):
    '''
    >>> reqs = """
    ... svn+https://svn.myserver.com/repos/myproject/
    ... svn+https://svn.myserver.com/repos/myproject_mail/
    ... git+https://github.com/mozes/smpp.pdu.git
    ... """
    >>> reqs = convert(reqs)
    >>> reqs['install_requires'] #doctest: +ELLIPSIS
    ['...', '...', '...']
    >>> reqs['dependency_links'] #doctest: +ELLIPSIS
    ['svn+https://svn.myserver.com/repos/myproject/#egg=...-dev', 'svn+https://svn.myserver.com/repos/myproject_mail/#egg=...-dev', 'git+https://github.com/mozes/smpp.pdu.git#egg=...-dev']
    '''
    reqs_list  = reqs.split('\n')
    reqs_pairs = [convert_req(r) for r in reqs_list if r!='']
    return {
        'install_requires' : [r['install_requires'] for r in reqs_pairs],
        'dependency_links' : [r['dependency_links'] for r in reqs_pairs],
        }

