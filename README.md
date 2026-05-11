# MMD4Maya - Maya 2025+

[MMD4Maya](https://github.com/gameboy12615/MMD4Maya) を Maya 2025 以降で動作するように修正したプラグインです。

## 主な変更点

- Maya 2025 以降の Python 3 環境向けに互換修正を追加
- Maya が `__file__` を定義しない場合のプラグイン読み込みを修正
- PMX/VMD パス処理で `bytes` と `str` が混在して落ちる問題を修正
- `Program Files` のような空白を含むパスでも `pmx2fbx.exe` を実行できるように修正
- 同梱 `chardet` を 7.4.3 に更新
- 配布フォルダから古い `__pycache__` が混ざらないように整理
- 操作性の向上のためOS標準ダイアログ `QFileDialog` へ変更し、お気に入りフォルダや検索機能がそのまま使えるように変更  
  ※oldフォルダに従来のダイアログもあるので差し替え可能

## PMX2FBX について

ライセンス上の都合により、このリポジトリには `PMX2FBX/pmx2fbx.exe` および関連バイナリを同梱しません。

使用する場合は、以下のオリジナルリポジトリやサイトを参考に PMX2FBX を入手し、各自で配置してください。

- [MMD4Maya(オリジナル by gameboy12615)](https://github.com/gameboy12615/MMD4Maya)

- [MMD4MayaをMaya2020で使う方法](https://codelabo.com/posts/20200224192543)

配置先:

```text
plug-ins/MMD4Maya/Scripts/PMX2FBX/
```

最低限、Windows では以下のような構成が必要です。

```text
plug-ins/MMD4Maya/Scripts/PMX2FBX/
  pmx2fbx.exe
  pmx2fbx.xml
  mecab.dll
  libfbxsdk.dylib
  libmecab.dylib
```

## インストール

1. Mayaが起動している場合は終了します。
2. PMX2FBX を入手し、上記の `plug-ins/MMD4Maya/Scripts/PMX2FBX/` に配置します。
3. 以下のインストール先に`plug-ins`の中に入っている`MMD4Maya`フォルダと`MMD4Maya.py`を配置します。
4. Maya 2025 以降を起動します。
5. Plug-in Manager で `MMD4Maya.py` をロードします。
6. Maya メニューバーの `MMD4Maya > Open MMD4Maya` を開きます。

インストール先:

```text
C:\Program Files\Autodesk\Maya2025\bin\plug-ins
```



# MMD4Maya
This is maya plug-in which use for importing pmx/pmd model to maya.<br>
It is based on pmx2fbx.exe which is wrote by http://stereoarts.jp/

## Install:
1. Copy `MMD4Maya.py` and `MMD4Maya` folder to your maya plug-ins folder. like: `Maya2016\bin\plug-ins`.
2. Enable MMD4Maya in maya Plug-in Manager.

## Steps to import:
1. Select a pmx/pmd file.
2. Select one or multiple vmd files.
3. Check the terms of use then click Process.
![](http://images2015.cnblogs.com/blog/675680/201601/675680-20160131230507896-565921880.jpg)

## Attention:
1. The file name of fbx file and texture files should not be japanese or chinese.
2. You can only import one model at a time, please save your model as the standard fbx file, then create a new scene to import another one.
