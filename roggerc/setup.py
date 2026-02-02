from setuptools import setup,find_packages

setup(

    name="rogger",
   packages=find_packages(),
    install_requires=[

        "yt-dlp",

    ],

    entry_points={
        "console_scripts":[
            "captain=rogger.main:main",
        ]
    },

)