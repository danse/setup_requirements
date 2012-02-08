import re
def convert_req(req):
    '''
    >>> r = convert_req('svn+svn://svn.myserver.com/repos/myproject_mail/')
    >>> len(r)
    2
    >>> r['install_requires']
    'svnsvnsvnmyservercomreposmyproject_mail'
    >>> r['dependency_links']
    'svn+svn://svn.myserver.com/repos/myproject_mail/#egg=svnsvnsvnmyservercomreposmyproject_mail-dev'
    '''
    r = {}
    fake_package_name = re.sub('\W', '', req)
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
    >>> reqs['install_requires']
    ['svnhttpssvnmyservercomreposmyproject', 'svnhttpssvnmyservercomreposmyproject_mail', 'githttpsgithubcommozessmpppdugit']
    >>> reqs['dependency_links']
    ['svn+https://svn.myserver.com/repos/myproject/#egg=svnhttpssvnmyservercomreposmyproject-dev', 'svn+https://svn.myserver.com/repos/myproject_mail/#egg=svnhttpssvnmyservercomreposmyproject_mail-dev', 'git+https://github.com/mozes/smpp.pdu.git#egg=githttpsgithubcommozessmpppdugit-dev']
    '''
    reqs_list  = reqs.split('\n')
    reqs_pairs = [convert_req(r) for r in reqs_list if r!='']
    return {
        'install_requires' : [r['install_requires'] for r in reqs_pairs],
        'dependency_links' : [r['dependency_links'] for r in reqs_pairs],
        }
