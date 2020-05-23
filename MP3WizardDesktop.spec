# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['D:/mp3WizardDesktop/loginDash.py'],
             pathex=['D:\\mp3WizardDesktop'],
             binaries=[],
             datas=[('D:/mp3WizardDesktop/simpleicon.png', '.img'), ('D:/mp3WizardDesktop/loginDash_support.py', '.'), ('D:/mp3WizardDesktop/uploadBookDash.py', '.'), ('D:/mp3WizardDesktop/uploadBookDash_support.py', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='MP3WizardDesktop',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='D:\\mp3WizardDesktop\\simpleicon.ico')
