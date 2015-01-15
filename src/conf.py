class Conf:
  c = {}
  
  c["tmplVars"] = {}
  c["tmplVars"]["baseTitle"] = 'Entelekia - '
  c["tmplVars"]["homeUrl"] = '/'
  c["tmplVars"]["baseImg"] = '/images/learnpgh-logo.png'
  c["tmplVars"]["explorelUrl"] = '/'
  c["tmplVars"]["submitUrl"] = '/'
  c["tmplVars"]["baseCity"] = 'Pittsburgh'
  c["tmplVars"]["twitUrl"] = 'https://www.twitter.com/learnpgh'
  c["tmplVars"]["ogTitle"] = 'Entelekia'
  c["tmplVars"]["ogDesc"] = 'One place to find all of the resources you need to learn about anything.'
  c["tmplVars"]["ogImg"] = '/images/learnpgh-logo.png'
  c["tmplVars"]["ogUrl"] = 'http://www.entelekia.org'

  def get(self, key):
    return self.c[key]