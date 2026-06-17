# Week 10 Homework ToDo

> 遠端檢查分支：`week10-1114405011-凃彥任`  
> 遠端作業資料夾：`weeks/week-10/solutions/1114405055/`  
> 檢查日期：2026-05-04

---



## 5. 建議本機最終驗證流程

請在本機作業資料夾執行：

```powershell
cd D:\Edwin\program\program-python\2026-python\weeks\week-10\solutions\1114405055
```

### 5.1 語法檢查

```powershell
python -m py_compile task1_csv_to_json.py
python -m py_compile task2_json_to_xml.py
python -m py_compile task3_plot_comparison.py
```

### 5.2 單元測試

```powershell
python -m unittest discover -s tests -p "test_*.py" -v
```

期望結果：

```text
Ran 14 tests in ...

OK
```

### 5.3 重新產生輸出檔

```powershell
python task1_csv_to_json.py
python task2_json_to_xml.py
python task3_plot_comparison.py
```

期望產生：

```text
output/students.json
output/students.xml
output/timing_comparison.png
```

### 5.4 檢查 git 狀態

```powershell
git status
```

確認只修改：

```text
weeks/week-10/solutions/1114405055/
```

不要修改：

```text
weeks/week-10/HOMEWORK.md
weeks/week-10/README.md
weeks/week-10/QUESTION-*.md
docs/
```

---

## 6. 最終 ToDo 清單

- [ ] 確認正確學號：`1114405011` 或 `1114405055`
- [ ] 確認遠端 Python 檔案是否有正確換行與縮排
- [ ] 執行 `python -m py_compile` 檢查三個 Python 檔
- [ ] 將 CSV 路徑改成 `pathlib` 穩定寫法
- [ ] 補完 `TIMING_REPORT.md` 四題回答
- [ ] 刪除 `TEST_LOG.md` 中的模板文字，補完整 Refactor 紀錄
- [ ] 將 `README.md` 從模板改成正式說明
- [ ] 補充 `AI_USAGE.md` 的相對路徑修正案例
- [ ] 確認 `output/students.json`、`output/students.xml`、`output/timing_comparison.png` 都能重新產生
- [ ] 確認所有變更都只在 `weeks/week-10/solutions/<student-id>/`
- [ ] 確認分支名稱是否需要改成 `submit/week-10`
- [ ] PR 標題使用 `Week 10 - 學號 - 姓名`
