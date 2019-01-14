# -*- mode: python -*-

block_cipher = None


a = Analysis(['renamer.py'],
             pathex=['C:\\Users\\x14715498790\\Desktop\\MOZAO_V2'],
             binaries=[],
             datas=[],
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

a.datas += [("source/view/main_window/main_window.qml", "C:\\Users\\x14715498790\\Desktop\\MOZAO_V2\\source\\view\\main_window\\main_window.qml", "DATA")]

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='renamer',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
