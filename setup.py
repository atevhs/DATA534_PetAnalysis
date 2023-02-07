from distutils.core import setup
setup(
  name = 'petanalysis', 
  packages = ['petanalysis'],  
  version = '0.1.0',
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'The TIC wrapper API allows you to access the analysis on thousands of pets listed on
              Petfinder.com and animal welfare shelters hosting these pets.', 
  author = 'ZiYing(Sophie) Chen, Shveta Sharma, Alyssa Foote',            
  author_email = 'yamapi0927@hotmail.com, atevhs@gmail.com, alyssa.k.foote@gmail.com',
  url = 'https://github.com/atevhs/DATA534_PetAnalysis', 
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['pets', 'dogs', 'adoption organizations', 'analysis', 'api wrapper', 'petfinder'],
  install_requires=[            # I get to this in a second
          'pgeocode',
          'pandas',
          'mlxtend',
          'seaborn',
          'matplotlib',
      ],
  classifiers=[
    'Development Status :: 4 - Beta', 
    'Intended Audience :: Researchers',      # Define that your audience are developers
    'Topic :: Data Science :: Pet Analysis Tool',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.10',
  ],
)