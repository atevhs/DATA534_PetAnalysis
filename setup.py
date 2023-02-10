from distutils.core import setup
setup(
  name = 'petanalysis', 
  packages = ['petanalysis'],  
  version = '0.1.0',
  license='MIT',
  description = 'The TIC wrapper API allows you to access the analysis on thousands of pets listed on
              Petfinder.com and animal welfare shelters hosting these pets.', 
  author = 'ZiYing(Sophie) Chen, Shveta Sharma, Alyssa Foote',            
  author_email = 'yamapi0927@hotmail.com, atevhs@gmail.com, alyssa.k.foote@gmail.com',
  url = 'https://github.com/atevhs/DATA534_PetAnalysis', 
  keywords = ['pets', 'dogs', 'adoption organizations', 'analysis', 'api wrapper', 'petfinder'],
  package_data={'': ['*.csv']},
  install_requires=[
          'pgeocode',
          'pandas',
          'mlxtend',
          'seaborn',
          'matplotlib',
      ],
  classifiers=[
    'Development Status :: 4 - Beta', 
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.10',
  ],
)