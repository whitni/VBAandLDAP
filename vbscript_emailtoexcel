'VBA Script start
Sub CopyToExcel(olItem As Outlook.MailItem)
Dim xlApp As Object
'try and get the current running object
Dim xlWB As Object
Dim xlSheet As Object
Dim xlOpenWB As Object
Dim vText As Variant
Dim sText As String
Dim rCount As Long
Dim bXStarted As Boolean
Dim enviro As String
Dim strPath As String
Dim Reg1 As RegExp
Dim M1 As MatchCollection
Dim M As Match
Dim xlUp As Long
Dim FileName As String
xlUp = -4162

'put together to add the date to the file name
FileName = "\Desktop\newhires" &amp; Format(Date, "yyyyMMDD") &amp; ".xlsx"

'the path of the workbook VB function, don't change
enviro = (Environ("USERPROFILE"))

strPath = enviro &amp; FileName
On Error Resume Next
Set xlApp = GetObject(, "Excel.Application")

If Err.Number &lt;&gt; 0 Then 'no object was found so create one
Set xlApp = CreateObject("Excel.Application")
Err.Clear
End If

'Add the workbook to input the data
Set xlWB = xlApp.Workbooks.Add()
xlWB.Save (strPath)

'open the workbook to input the data
Set xlOpenWB = xlApp.Workbooks.Open(strPath)
Set xlSheet = xlOpenWB.Sheets("Sheet1")

'Find the next empty line of the worksheet
rCount = xlSheet.Range("A" &amp; xlSheet.Rows.Count).End(xlUp).Row
rCount = rCount + 1

'sText is content of the email
sText = olItem.Body

Set Reg1 = New RegExp

' \s* = invisible spaces
' \d* = match digits
' \w* = match alphanumeric

With Reg1
.pattern = "(Employee Number\s*[:]\s*(\d*))"
End With
If Reg1.test(sText) Then

Set M1 = Reg1.Execute(sText)
For Each M In M1
vText = Trim(M.SubMatches(1))
Next
End If

xlSheet.Range("A" &amp; rCount) = vText
vText.RemoveDuplicates Columns:=Array(1)
xlOpenWB.Close 1

'removed xlApp.Quit
Set xlApp = Nothing
Set Reg1 = Nothing
Set xlWB = Nothing
Set xlSheet = Nothing
Set xlOpenWB = Nothing

End Sub
'VBA script end
