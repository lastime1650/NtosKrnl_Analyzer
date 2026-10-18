# CmpValidateHiveSecurityDescriptors

- RVA: `0x0096DAFC`–`0x0096DF3A` (길이 `1,086` bytes)
- VA: `0x000000014096DAFC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00095DF8`
- 디코드: `269`개 명령, `1,086/1,086` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **27**; 고유 호출 대상: **12**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0096DB31` → [HvpGetCellContextInitialize](../85/HvpGetCellContextInitialize_function_00855F10.md) (function, `0x00855F10`)
- `0x0096DB3D` → [HvpGetCellContextInitialize](../85/HvpGetCellContextInitialize_function_00855F10.md) (function, `0x00855F10`)
- `0x0096DB58` → [HvIsCellAllocated](../85/HvIsCellAllocated_function_00855D60.md) (function, `0x00855D60`)
- `0x0096DB80` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x0096DBB9` → [HvIsCellAllocated](../85/HvIsCellAllocated_function_00855D60.md) (function, `0x00855D60`)
- `0x0096DBE6` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x0096DC37` → [RtlValidRelativeSecurityDescriptor](../8B/RtlValidRelativeSecurityDescriptor_function_008BDC70.md) (function, `0x008BDC70`)
- `0x0096DC58` → [CmpAddSecurityCellToCache](CmpAddSecurityCellToCache_function_0096E228.md) (function, `0x0096E228`)
- `0x0096DC82` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x0096DC99` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x0096DCBA` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x0096DCD2` → [CmpAdjustSecurityCacheSize](CmpAdjustSecurityCacheSize_function_0096E4AC.md) (function, `0x0096E4AC`)
- `0x0096DD03` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x0096DD21` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x0096DD3A` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x0096DD44` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x0096DD70` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x0096DD87` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x0096DDA9` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x0096DDE1` → [CmpCheckSecurityCellAccess](../94/CmpCheckSecurityCellAccess_function_009470C0.md) (function, `0x009470C0`)
- `0x0096DDF4` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x0096DDFE` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x0096DE6A` → [CmpFindSecurityCellCacheIndex](../../text/42/CmpFindSecurityCellCacheIndex_function_00428060.md) (function, `0x00428060`)
- `0x0096DEB8` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x0096DEE4` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x0096DF03` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x0096DF2D` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)

### Direct callers
- [CmCheckRegistry](CmCheckRegistry_function_0096D2F4.md) at `0x0096D451`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **5**
  - `0x0096DD70` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x0096DDA9` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x0096DE6A` → [CmpFindSecurityCellCacheIndex](../../text/42/CmpFindSecurityCellCacheIndex_function_00428060.md) (`PAGE` → `.text`)
  - `0x0096DEB8` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x0096DF2D` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **10**
  - `0x0096DE2B` → [sub_00B28A98](../B2/Unknown_function_00B28A98.md) (`tail-transfer`)
  - `0x0096DE3E` → [sub_00B28A98](../B2/Unknown_function_00B28A98.md) (`tail-transfer`)
  - `0x0096DE4A` → [sub_00B28A98 + 0xD](../B2/Unknown_function_00B28A98.md) (`tail-transfer`)
  - `0x0096DE5D` → [sub_00B28A98 + 0xD](../B2/Unknown_function_00B28A98.md) (`tail-transfer`)
  - `0x0096DE71` → [sub_00B28A98 + 0x1F](../B2/Unknown_function_00B28A98.md) (`tail-transfer`)
  - `0x0096DEDE` → [sub_00B28A98 + 0x34](../B2/Unknown_function_00B28A98.md) (`tail-transfer`)
  - `0x0096DEEA` → [sub_00B28A98 + 0x39](../B2/Unknown_function_00B28A98.md) (`tail-transfer`)
  - `0x0096DEFD` → [sub_00B28A98 + 0x43](../B2/Unknown_function_00B28A98.md) (`tail-transfer`)
  - `0x0096DF09` → [sub_00B28A98 + 0x48](../B2/Unknown_function_00B28A98.md) (`tail-transfer`)
  - `0x0096DF11` → [sub_00B28A98 + 0x68](../B2/Unknown_function_00B28A98.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0096DAFC  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
0096DB01  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
0096DB06  89 54 24 10                     mov dword ptr [rsp + 0x10], edx
0096DB0A  55                              push rbp
0096DB0B  53                              push rbx
0096DB0C  56                              push rsi
0096DB0D  57                              push rdi
0096DB0E  41 54                           push r12
0096DB10  41 55                           push r13
0096DB12  41 56                           push r14
0096DB14  41 57                           push r15
0096DB16  48 8B EC                        mov rbp, rsp
0096DB19  48 83 EC 58                     sub rsp, 0x58
0096DB1D  48 83 65 E8 00                  and qword ptr [rbp - 0x18], 0
0096DB22  48 8B D9                        mov rbx, rcx
0096DB25  48 83 65 E0 00                  and qword ptr [rbp - 0x20], 0
0096DB2A  48 8D 4D E8                     lea rcx, [rbp - 0x18]
0096DB2E  49 8B F9                        mov rdi, r9
0096DB31  E8 DA 83 EE FF                  call 0x140855f10
0096DB36  48 8D 4D E0                     lea rcx, [rbp - 0x20]
0096DB3A  45 33 F6                        xor r14d, r14d
0096DB3D  E8 CE 83 EE FF                  call 0x140855f10
0096DB42  48 8B 53 40                     mov rdx, qword ptr [rbx + 0x40]
0096DB46  45 33 C0                        xor r8d, r8d
0096DB49  8B 83 50 07 00 00               mov eax, dword ptr [rbx + 0x750]
0096DB4F  48 8B CB                        mov rcx, rbx
0096DB52  89 45 DC                        mov dword ptr [rbp - 0x24], eax
0096DB55  8B 52 24                        mov edx, dword ptr [rdx + 0x24]
0096DB58  E8 03 82 EE FF                  call 0x140855d60
0096DB5D  84 C0                           test al, al
0096DB5F  0F 84 E9 01 00 00               je 0x14096dd4e
0096DB65  F6 83 8C 00 00 00 01            test byte ptr [rbx + 0x8c], 1
0096DB6C  4C 8D 45 E8                     lea r8, [rbp - 0x18]
0096DB70  48 8B 43 40                     mov rax, qword ptr [rbx + 0x40]
0096DB74  48 8B CB                        mov rcx, rbx
0096DB77  8B 50 24                        mov edx, dword ptr [rax + 0x24]
0096DB7A  0F 84 BA 01 00 00               je 0x14096dd3a
0096DB80  E8 DB 70 EE FF                  call 0x140854c60
0096DB85  4C 8B E8                        mov r13, rax
0096DB88  48 85 C0                        test rax, rax
0096DB8B  0F 84 93 02 00 00               je 0x14096de24
0096DB91  B8 FC FF FF FF                  mov eax, 0xfffffffc
0096DB96  41 2B 45 FC                     sub eax, dword ptr [r13 - 4]
0096DB9A  83 F8 4C                        cmp eax, 0x4c
0096DB9D  0F 8C A0 02 00 00               jl 0x14096de43
0096DBA3  45 8B 7D 2C                     mov r15d, dword ptr [r13 + 0x2c]
0096DBA7  33 F6                           xor esi, esi
0096DBA9  45 8B F7                        mov r14d, r15d
0096DBAC  44 89 7D D8                     mov dword ptr [rbp - 0x28], r15d
0096DBB0  4C 8B C7                        mov r8, rdi
0096DBB3  41 8B D7                        mov edx, r15d
0096DBB6  48 8B CB                        mov rcx, rbx
0096DBB9  E8 A2 81 EE FF                  call 0x140855d60
0096DBBE  4C 8B 65 68                     mov r12, qword ptr [rbp + 0x68]
0096DBC2  BF 4C 01 00 C0                  mov edi, 0xc000014c
0096DBC7  84 C0                           test al, al
0096DBC9  0F 84 3F 03 00 00               je 0x14096df0e
0096DBCF  F6 83 8C 00 00 00 01            test byte ptr [rbx + 0x8c], 1
0096DBD6  4C 8D 45 E0                     lea r8, [rbp - 0x20]
0096DBDA  41 8B D7                        mov edx, r15d
0096DBDD  48 8B CB                        mov rcx, rbx
0096DBE0  0F 84 B3 00 00 00               je 0x14096dc99
0096DBE6  E8 75 70 EE FF                  call 0x140854c60
0096DBEB  4C 8B F0                        mov r14, rax
0096DBEE  48 85 C0                        test rax, rax
0096DBF1  0F 84 11 02 00 00               je 0x14096de08
0096DBF7  B8 FC FF FF FF                  mov eax, 0xfffffffc
0096DBFC  41 2B 46 FC                     sub eax, dword ptr [r14 - 4]
0096DC00  83 F8 14                        cmp eax, 0x14
0096DC03  0F 82 E6 02 00 00               jb 0x14096deef
0096DC09  41 8B 56 10                     mov edx, dword ptr [r14 + 0x10]
0096DC0D  8D 4A 14                        lea ecx, [rdx + 0x14]
0096DC10  3B CA                           cmp ecx, edx
0096DC12  0F 82 D7 02 00 00               jb 0x14096deef
0096DC18  3B C8                           cmp ecx, eax
0096DC1A  0F 87 CF 02 00 00               ja 0x14096deef
0096DC20  44 3B 7D D8                     cmp r15d, dword ptr [rbp - 0x28]
0096DC24  74 0A                           je 0x14096dc30
0096DC26  41 39 76 08                     cmp dword ptr [r14 + 8], esi
0096DC2A  0F 85 61 01 00 00               jne 0x14096dd91
0096DC30  49 8D 4E 14                     lea rcx, [r14 + 0x14]
0096DC34  45 33 C0                        xor r8d, r8d
0096DC37  E8 34 00 F5 FF                  call 0x1408bdc70
0096DC3C  48 8B CB                        mov rcx, rbx
0096DC3F  84 C0                           test al, al
0096DC41  0F 84 8C 02 00 00               je 0x14096ded3
0096DC47  8B 7D DC                        mov edi, dword ptr [rbp - 0x24]
0096DC4A  41 8B D7                        mov edx, r15d
0096DC4D  85 FF                           test edi, edi
0096DC4F  0F 85 0D 02 00 00               jne 0x14096de62
0096DC55  41 B0 01                        mov r8b, 1
0096DC58  E8 CB 05 00 00                  call 0x14096e228
0096DC5D  8B F0                           mov esi, eax
0096DC5F  85 C0                           test eax, eax
0096DC61  0F 88 10 01 00 00               js 0x14096dd77
0096DC67  F6 83 8C 00 00 00 01            test byte ptr [rbx + 0x8c], 1
0096DC6E  48 8D 55 E0                     lea rdx, [rbp - 0x20]
0096DC72  41 8B F7                        mov esi, r15d
0096DC75  48 8B CB                        mov rcx, rbx
0096DC78  45 8B 7E 04                     mov r15d, dword ptr [r14 + 4]
0096DC7C  0F 85 05 01 00 00               jne 0x14096dd87
0096DC82  E8 B9 82 EE FF                  call 0x140855f40
0096DC87  44 8B 75 D8                     mov r14d, dword ptr [rbp - 0x28]
0096DC8B  45 3B FE                        cmp r15d, r14d
0096DC8E  74 13                           je 0x14096dca3
0096DC90  48 8B 7D 60                     mov rdi, qword ptr [rbp + 0x60]
0096DC94  E9 17 FF FF FF                  jmp 0x14096dbb0
0096DC99  E8 12 70 EE FF                  call 0x140854cb0
0096DC9E  E9 48 FF FF FF                  jmp 0x14096dbeb
0096DCA3  F6 83 8C 00 00 00 01            test byte ptr [rbx + 0x8c], 1
0096DCAA  4C 8D 45 E0                     lea r8, [rbp - 0x20]
0096DCAE  41 8B D7                        mov edx, r15d
0096DCB1  48 8B CB                        mov rcx, rbx
0096DCB4  0F 84 8A 00 00 00               je 0x14096dd44
0096DCBA  E8 A1 6F EE FF                  call 0x140854c60
0096DCBF  4C 8B F0                        mov r14, rax
0096DCC2  39 70 08                        cmp dword ptr [rax + 8], esi
0096DCC5  0F 85 C7 01 00 00               jne 0x14096de92
0096DCCB  85 FF                           test edi, edi
0096DCCD  75 08                           jne 0x14096dcd7
0096DCCF  48 8B CB                        mov rcx, rbx
0096DCD2  E8 D5 07 00 00                  call 0x14096e4ac
0096DCD7  F7 45 50 00 00 00 02            test dword ptr [rbp + 0x50], 0x2000000
0096DCDE  74 0D                           je 0x14096dced
0096DCE0  83 BB 50 07 00 00 01            cmp dword ptr [rbx + 0x750], 1
0096DCE7  0F 87 C6 00 00 00               ja 0x14096ddb3
0096DCED  33 F6                           xor esi, esi
0096DCEF  F6 83 8C 00 00 00 01            test byte ptr [rbx + 0x8c], 1
0096DCF6  48 8D 55 E8                     lea rdx, [rbp - 0x18]
0096DCFA  48 8B CB                        mov rcx, rbx
0096DCFD  0F 85 FB 00 00 00               jne 0x14096ddfe
0096DD03  E8 38 82 EE FF                  call 0x140855f40
0096DD08  4D 85 F6                        test r14, r14
0096DD0B  74 19                           je 0x14096dd26
0096DD0D  F6 83 8C 00 00 00 01            test byte ptr [rbx + 0x8c], 1
0096DD14  48 8D 55 E0                     lea rdx, [rbp - 0x20]
0096DD18  48 8B CB                        mov rcx, rbx
0096DD1B  0F 85 D3 00 00 00               jne 0x14096ddf4
0096DD21  E8 1A 82 EE FF                  call 0x140855f40
0096DD26  8B C6                           mov eax, esi
0096DD28  48 83 C4 58                     add rsp, 0x58
0096DD2C  41 5F                           pop r15
0096DD2E  41 5E                           pop r14
0096DD30  41 5D                           pop r13
0096DD32  41 5C                           pop r12
0096DD34  5F                              pop rdi
0096DD35  5E                              pop rsi
0096DD36  5B                              pop rbx
0096DD37  5D                              pop rbp
0096DD38  C3                              ret
0096DD39  CC                              int3
0096DD3A  E8 71 6F EE FF                  call 0x140854cb0
0096DD3F  E9 41 FE FF FF                  jmp 0x14096db85
0096DD44  E8 67 6F EE FF                  call 0x140854cb0
0096DD49  E9 71 FF FF FF                  jmp 0x14096dcbf
0096DD4E  48 8B 4D 68                     mov rcx, qword ptr [rbp + 0x68]
0096DD52  48 85 C9                        test rcx, rcx
0096DD55  0F 85 B7 00 00 00               jne 0x14096de12
0096DD5B  44 21 74 24 20                  and dword ptr [rsp + 0x20], r14d
0096DD60  33 D2                           xor edx, edx
0096DD62  BF 4C 01 00 C0                  mov edi, 0xc000014c
0096DD67  44 8B CF                        mov r9d, edi
0096DD6A  8B F7                           mov esi, edi
0096DD6C  44 8D 42 09                     lea r8d, [rdx + 9]
0096DD70  E8 DF 11 B0 FF                  call 0x14046ef54
0096DD75  EB AF                           jmp 0x14096dd26
0096DD77  C7 44 24 20 B0 00 00 00         mov dword ptr [rsp + 0x20], 0xb0
0096DD7F  44 8B C8                        mov r9d, eax
0096DD82  49 8B CC                        mov rcx, r12
0096DD85  EB 1A                           jmp 0x14096dda1
0096DD87  E8 94 EE EE FF                  call 0x14085cc20
0096DD8C  E9 F6 FE FF FF                  jmp 0x14096dc87
0096DD91  C7 44 24 20 A0 00 00 00         mov dword ptr [rsp + 0x20], 0xa0
0096DD99  49 8B CC                        mov rcx, r12
0096DD9C  8B F7                           mov esi, edi
0096DD9E  44 8B CF                        mov r9d, edi
0096DDA1  41 B8 09 00 00 00               mov r8d, 9
0096DDA7  33 D2                           xor edx, edx
0096DDA9  E8 A6 11 B0 FF                  call 0x14046ef54
0096DDAE  E9 3C FF FF FF                  jmp 0x14096dcef
0096DDB3  33 FF                           xor edi, edi
0096DDB5  3B BB 50 07 00 00               cmp edi, dword ptr [rbx + 0x750]
0096DDBB  0F 83 2C FF FF FF               jae 0x14096dced
0096DDC1  48 8B 93 60 07 00 00            mov rdx, qword ptr [rbx + 0x760]
0096DDC8  41 B9 19 00 02 00               mov r9d, 0x20019
0096DDCE  8B C7                           mov eax, edi
0096DDD0  41 B0 01                        mov r8b, 1
0096DDD3  48 03 C0                        add rax, rax
0096DDD6  C6 44 24 20 00                  mov byte ptr [rsp + 0x20], 0
0096DDDB  48 8B CB                        mov rcx, rbx
0096DDDE  8B 14 C2                        mov edx, dword ptr [rdx + rax*8]
0096DDE1  E8 DA 92 FD FF                  call 0x1409470c0
0096DDE6  8B F0                           mov esi, eax
0096DDE8  85 C0                           test eax, eax
0096DDEA  0F 88 B4 00 00 00               js 0x14096dea4
0096DDF0  FF C7                           inc edi
0096DDF2  EB C1                           jmp 0x14096ddb5
0096DDF4  E8 27 EE EE FF                  call 0x14085cc20
0096DDF9  E9 28 FF FF FF                  jmp 0x14096dd26
0096DDFE  E8 1D EE EE FF                  call 0x14085cc20
0096DE03  E9 00 FF FF FF                  jmp 0x14096dd08
0096DE08  C7 44 24 20 90 00 00 00         mov dword ptr [rsp + 0x20], 0x90
0096DE10  EB 87                           jmp 0x14096dd99
0096DE12  48 8B 43 40                     mov rax, qword ptr [rbx + 0x40]
0096DE16  8B 50 24                        mov edx, dword ptr [rax + 0x24]
0096DE19  89 91 F0 00 00 00               mov dword ptr [rcx + 0xf0], edx
0096DE1F  E9 37 FF FF FF                  jmp 0x14096dd5b
0096DE24  48 8B 4D 68                     mov rcx, qword ptr [rbp + 0x68]
0096DE28  48 85 C9                        test rcx, rcx
0096DE2B  0F 84 67 AC 1B 00               je 0x140b28a98
0096DE31  48 8B 43 40                     mov rax, qword ptr [rbx + 0x40]
0096DE35  8B 50 24                        mov edx, dword ptr [rax + 0x24]
0096DE38  89 91 F0 00 00 00               mov dword ptr [rcx + 0xf0], edx
0096DE3E  E9 55 AC 1B 00                  jmp 0x140b28a98
0096DE43  48 8B 4D 68                     mov rcx, qword ptr [rbp + 0x68]
0096DE47  48 85 C9                        test rcx, rcx
0096DE4A  0F 84 55 AC 1B 00               je 0x140b28aa5
0096DE50  48 8B 43 40                     mov rax, qword ptr [rbx + 0x40]
0096DE54  8B 50 24                        mov edx, dword ptr [rax + 0x24]
0096DE57  89 91 F0 00 00 00               mov dword ptr [rcx + 0xf0], edx
0096DE5D  E9 43 AC 1B 00                  jmp 0x140b28aa5
0096DE62  83 65 48 00                     and dword ptr [rbp + 0x48], 0
0096DE66  4C 8D 45 48                     lea r8, [rbp + 0x48]
0096DE6A  E8 F1 A1 AB FF                  call 0x140428060
0096DE6F  84 C0                           test al, al
0096DE71  0F 84 40 AC 1B 00               je 0x140b28ab7
0096DE77  48 8B 83 60 07 00 00            mov rax, qword ptr [rbx + 0x760]
0096DE7E  8B 4D 48                        mov ecx, dword ptr [rbp + 0x48]
0096DE81  48 03 C9                        add rcx, rcx
0096DE84  48 8B 4C C8 08                  mov rcx, qword ptr [rax + rcx*8 + 8]
0096DE89  83 61 1C 00                     and dword ptr [rcx + 0x1c], 0
0096DE8D  E9 D5 FD FF FF                  jmp 0x14096dc67
0096DE92  BF 4C 01 00 C0                  mov edi, 0xc000014c
0096DE97  C7 44 24 20 C8 00 00 00         mov dword ptr [rsp + 0x20], 0xc8
0096DE9F  E9 F5 FE FF FF                  jmp 0x14096dd99
0096DEA4  33 D2                           xor edx, edx
0096DEA6  C7 44 24 20 D0 00 00 00         mov dword ptr [rsp + 0x20], 0xd0
0096DEAE  44 8B CE                        mov r9d, esi
0096DEB1  49 8B CC                        mov rcx, r12
0096DEB4  44 8D 42 09                     lea r8d, [rdx + 9]
0096DEB8  E8 97 10 B0 FF                  call 0x14046ef54
0096DEBD  81 FE 9A 00 00 C0               cmp esi, 0xc000009a
0096DEC3  0F 84 26 FE FF FF               je 0x14096dcef
0096DEC9  BE 4C 01 00 C0                  mov esi, 0xc000014c
0096DECE  E9 1C FE FF FF                  jmp 0x14096dcef
0096DED3  F6 83 8C 00 00 00 01            test byte ptr [rbx + 0x8c], 1
0096DEDA  48 8D 55 E0                     lea rdx, [rbp - 0x20]
0096DEDE  0F 84 E8 AB 1B 00               je 0x140b28acc
0096DEE4  E8 37 ED EE FF                  call 0x14085cc20
0096DEE9  90                              nop
0096DEEA  E9 E2 AB 1B 00                  jmp 0x140b28ad1
0096DEEF  F6 83 8C 00 00 00 01            test byte ptr [rbx + 0x8c], 1
0096DEF6  48 8D 55 E0                     lea rdx, [rbp - 0x20]
0096DEFA  48 8B CB                        mov rcx, rbx
0096DEFD  0F 84 D8 AB 1B 00               je 0x140b28adb
0096DF03  E8 18 ED EE FF                  call 0x14085cc20
0096DF08  90                              nop
0096DF09  E9 D2 AB 1B 00                  jmp 0x140b28ae0
0096DF0E  45 3B F7                        cmp r14d, r15d
0096DF11  0F 85 E9 AB 1B 00               jne 0x140b28b00
0096DF17  33 D2                           xor edx, edx
0096DF19  C7 44 24 20 80 00 00 00         mov dword ptr [rsp + 0x20], 0x80
0096DF21  44 8B CF                        mov r9d, edi
0096DF24  49 8B CC                        mov rcx, r12
0096DF27  8B F7                           mov esi, edi
0096DF29  44 8D 42 09                     lea r8d, [rdx + 9]
0096DF2D  E8 22 10 B0 FF                  call 0x14046ef54
0096DF32  45 33 F6                        xor r14d, r14d
0096DF35  E9 B5 FD FF FF                  jmp 0x14096dcef
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpValidateHiveSecurityDescriptors(__int64 a1, int a2, __int64 a3, __int64 a4, __int64 a5)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned int v_stack_m64;
    unsigned int v_stack_m68;
    unsigned int v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p8;

    v_stack_p20 = a4;
    v_stack_p18 = a3;
    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (88);
    result = HvpGetCellContextInitialize(v_stack_m58, a2, a3, a4);
    v_r14 = 0;
    result = HvpGetCellContextInitialize(v_stack_m60, a2, a3, a4);
    a3 = 0;
    v_stack_m64 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 1872)));
    result = HvIsCellAllocated(a1, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 64) + 36)), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0096DD4E;
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_0096DD3A;
    result = HvpGetCellFlat(a1, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 64) + 36)), v_stack_m58, a4);
loc_0096DB85:
    if (result == 0) goto loc_0096DE24;
    result = (unsigned int)(((unsigned int)(0xFFFFFFFCULL)) - (*(unsigned int *)(result - 4)));
    if (((unsigned int)(result)) < 76) goto loc_0096DE43;
    v_rsi = 0;
    v_stack_m68 = (unsigned int)((unsigned int)(*(unsigned int *)(result + 44)));
loc_0096DBB0:
    result = HvIsCellAllocated(a1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + 44)))), a4, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0096DF0E;
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_0096DC99;
    result = HvpGetCellFlat(a1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + 44)))), v_stack_m60, a4);
loc_0096DBEB:
    if (result == 0) goto loc_0096DE08;
    result = (unsigned int)(((unsigned int)(0xFFFFFFFCULL)) - (*(unsigned int *)(result - 4)));
    if (((unsigned int)(result)) < 20) goto loc_0096DEEF;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result + 16)) + 20)) < ((unsigned int)((unsigned int)(*(unsigned int *)(result + 16))))) goto loc_0096DEEF;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result + 16)) + 20)) > ((unsigned int)(result))) goto loc_0096DEEF;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result + 44)))) == v_stack_m68) goto loc_0096DC30;
    if ((*(unsigned int *)(result + 8)) != 0) goto loc_0096DD91;
loc_0096DC30:
    a3 = 0;
    result = RtlValidRelativeSecurityDescriptor(result + 20, (unsigned int)(*(unsigned int *)(result + 16)), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0096DED3;
    if ((unsigned int)((unsigned int)(v_stack_m64)) != 0) goto loc_0096DE62;
    result = CmpAddSecurityCellToCache(a1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + 44)))), 1, a4);
    if (sign_flag) goto loc_0096DD77;
loc_0096DC67:
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) != 0) goto loc_0096DD87;
    result = HvpReleaseCellPaged(a1, v_stack_m60, 1, a4);
loc_0096DC87:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result + 4)))) == ((unsigned int)((unsigned int)(v_stack_m68)))) goto loc_0096DCA3;
    goto loc_0096DBB0;
loc_0096DC99:
    result = HvpGetCellPaged(a1, v_stack_m60, 1, a4);
    goto loc_0096DBEB;
loc_0096DCA3:
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_0096DD44;
    result = HvpGetCellFlat(a1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + 4)))), v_stack_m60, a4);
loc_0096DCBF:
    if ((*(unsigned int *)(result + 8)) != ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + 44))))))) goto loc_0096DE92;
    if ((unsigned int)(v_stack_p20) == 0) {
        a1 = a1;
        result = CmpAdjustSecurityCacheSize(a1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + 4)))), v_stack_m60, a4);
    }
    if (((v_stack_p10) & (0x2000000ULL)) == 0) goto loc_0096DCED;
    if ((*(unsigned int *)(a1 + 1872)) > 1) goto loc_0096DDB3;
loc_0096DCED:
    v_rsi = 0;
loc_0096DCEF:
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) != 0) goto loc_0096DDFE;
    result = HvpReleaseCellPaged(a1, v_stack_m58, v_stack_m60, a4);
loc_0096DD08:
    if (result == 0) goto loc_0096DD26;
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) != 0) goto loc_0096DDF4;
    result = HvpReleaseCellPaged(a1, v_stack_m60, v_stack_m60, a4);
loc_0096DD26:
    v_rsp = (v_rsp) + (88);
    return 0;
loc_0096DD3A:
    result = HvpGetCellPaged(a1, v_stack_m60, v_stack_m60, a4);
    goto loc_0096DB85;
loc_0096DD44:
    result = HvpGetCellPaged(a1, v_stack_m60, v_stack_m60, a4);
    goto loc_0096DCBF;
loc_0096DD4E:
    if (a5 != 0) goto loc_0096DE12;
loc_0096DD5B:
    a2 = 0;
    result = SetFailureLocation(a5, a2, a2 + 9, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
    goto loc_0096DD26;
loc_0096DD77:
    v_stack_p20 = 176;
    goto loc_0096DDA1;
loc_0096DD87:
    result = HvpReleaseCellFlat(a5, a2, a2 + 9, (unsigned int)((unsigned int)(result)));
    goto loc_0096DC87;
loc_0096DD91:
    v_stack_p20 = 160;
loc_0096DD99:
loc_0096DDA1:
    a2 = 0;
    result = SetFailureLocation(a5, a2, 9, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
    goto loc_0096DCEF;
loc_0096DDB3:
    v_rdi = 0;
loc_0096DDB5:
    if (0 >= (*(unsigned int *)(a1 + 1872))) goto loc_0096DCED;
    result = (0) + (0);
    v_stack_p20 = 0;
    result = CmpCheckSecurityCellAccess(a1, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 1888) + result * 8)), 1, (unsigned int)(0x20019ULL));
    if (sign_flag) goto loc_0096DEA4;
    v_rdi = (unsigned int)((v_rdi) + 1);
    goto loc_0096DDB5;
loc_0096DDF4:
    result = HvpReleaseCellFlat(a1, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 1888) + result * 8)), 1, (unsigned int)(0x20019ULL));
    goto loc_0096DD26;
loc_0096DDFE:
    result = HvpReleaseCellFlat(a1, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 1888) + result * 8)), 1, (unsigned int)(0x20019ULL));
    goto loc_0096DD08;
loc_0096DE08:
    v_stack_p20 = 144;
    goto loc_0096DD99;
loc_0096DE12:
    *(unsigned int *)(a1 + 240) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 64) + 36)));
    goto loc_0096DD5B;
loc_0096DE24:
    *(unsigned int *)(a5 + 240) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 64) + 36)));
loc_0096DE43:
    *(unsigned int *)(a5 + 240) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 64) + 36)));
loc_0096DE62:
    result = CmpFindSecurityCellCacheIndex(a5, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 64) + 36)), v_stack_p8, (unsigned int)(0x20019ULL));
    a1 = ((unsigned int)(v_stack_p8)) + ((unsigned int)(v_stack_p8));
    goto loc_0096DC67;
loc_0096DE92:
    v_stack_p20 = 200;
    goto loc_0096DD99;
loc_0096DEA4:
    a2 = 0;
    v_stack_p20 = 208;
    result = SetFailureLocation(a5, a2, a2 + 9, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == 0xC000009AULL) goto loc_0096DCEF;
    goto loc_0096DCEF;
loc_0096DED3:
    result = HvpReleaseCellFlat(a5, v_stack_m60, a2 + 9, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
loc_0096DEEF:
    result = HvpReleaseCellFlat(a1, v_stack_m60, a2 + 9, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
loc_0096DF0E:
    a2 = 0;
    v_stack_p20 = 128;
    result = SetFailureLocation(a5, a2, a2 + 9, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
    v_r14 = 0;
    goto loc_0096DCEF;
}
```

## 5. (Beta) C Style

```c
int64_t CmpValidateHiveSecurityDescriptors(void *Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r14;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint32_t v_stack_m64;
    uint32_t v_stack_m68;
    uint32_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint32_t v_stack_p8;

    v_stack_p20 = Arg4;
    v_stack_p18 = Arg3;
    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (88);
    result = HvpGetCellContextInitialize(v_stack_m58, Arg2, Arg3, Arg4);
    local_r14 = 0;
    result = HvpGetCellContextInitialize(v_stack_m60, Arg2, Arg3, Arg4);
    Arg3 = 0;
    v_stack_m64 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x750)));
    result = HvIsCellAllocated(Arg1, (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x40) + 0x24)), Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0096DD4E;
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_0096DD3A;
    result = HvpGetCellFlat(Arg1, (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x40) + 0x24)), v_stack_m58, Arg4);
loc_0096DB85:
    if (result == 0) goto loc_0096DE24;
    result = (uint32_t)(((uint32_t)(0xFFFFFFFCULL)) - (*(uint32_t *)(result - 0x4)));
    if (((uint32_t)(result)) < 76) goto loc_0096DE43;
    local_rsi = 0;
    v_stack_m68 = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x2C)));
loc_0096DBB0:
    result = HvIsCellAllocated(Arg1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x2C)))), Arg4, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0096DF0E;
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_0096DC99;
    result = HvpGetCellFlat(Arg1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x2C)))), v_stack_m60, Arg4);
loc_0096DBEB:
    if (result == 0) goto loc_0096DE08;
    result = (uint32_t)(((uint32_t)(0xFFFFFFFCULL)) - (*(uint32_t *)(result - 0x4)));
    if (((uint32_t)(result)) < 20) goto loc_0096DEEF;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x10)) + 20)) < ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x10))))) goto loc_0096DEEF;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x10)) + 20)) > ((uint32_t)(result))) goto loc_0096DEEF;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x2C)))) == v_stack_m68) goto loc_0096DC30;
    if ((*(uint32_t *)(result + 0x8)) != 0) goto loc_0096DD91;
loc_0096DC30:
    Arg3 = 0;
    result = RtlValidRelativeSecurityDescriptor(result + 20, (uint32_t)(*(uint32_t *)(result + 0x10)), Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0096DED3;
    if ((uint32_t)((uint32_t)(v_stack_m64)) != 0) goto loc_0096DE62;
    result = CmpAddSecurityCellToCache(Arg1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x2C)))), 1, Arg4);
    if (sign_flag) goto loc_0096DD77;
loc_0096DC67:
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) != 0) goto loc_0096DD87;
    result = HvpReleaseCellPaged(Arg1, v_stack_m60, 1, Arg4);
loc_0096DC87:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x4)))) == ((uint32_t)((uint32_t)(v_stack_m68)))) goto loc_0096DCA3;
    goto loc_0096DBB0;
loc_0096DC99:
    result = HvpGetCellPaged(Arg1, v_stack_m60, 1, Arg4);
    goto loc_0096DBEB;
loc_0096DCA3:
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_0096DD44;
    result = HvpGetCellFlat(Arg1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x4)))), v_stack_m60, Arg4);
loc_0096DCBF:
    if ((*(uint32_t *)(result + 0x8)) != ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x2C))))))) goto loc_0096DE92;
    if ((uint32_t)(v_stack_p20) == 0) {
        Arg1 = Arg1;
        result = CmpAdjustSecurityCacheSize(Arg1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x4)))), v_stack_m60, Arg4);
    }
    if (((v_stack_p10) & (0x2000000ULL)) == 0) goto loc_0096DCED;
    if ((*(uint32_t *)(arg1 + 0x750)) > 1) goto loc_0096DDB3;
loc_0096DCED:
    local_rsi = 0;
loc_0096DCEF:
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) != 0) goto loc_0096DDFE;
    result = HvpReleaseCellPaged(Arg1, v_stack_m58, v_stack_m60, Arg4);
loc_0096DD08:
    if (result == 0) goto loc_0096DD26;
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) != 0) goto loc_0096DDF4;
    result = HvpReleaseCellPaged(Arg1, v_stack_m60, v_stack_m60, Arg4);
loc_0096DD26:
    local_rsp = (local_rsp) + (88);
    return 0;
loc_0096DD3A:
    result = HvpGetCellPaged(Arg1, v_stack_m60, v_stack_m60, Arg4);
    goto loc_0096DB85;
loc_0096DD44:
    result = HvpGetCellPaged(Arg1, v_stack_m60, v_stack_m60, Arg4);
    goto loc_0096DCBF;
loc_0096DD4E:
    if (Arg5 != 0) goto loc_0096DE12;
loc_0096DD5B:
    Arg2 = 0;
    result = SetFailureLocation(Arg5, Arg2, Arg2 + 9, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
    goto loc_0096DD26;
loc_0096DD77:
    v_stack_p20 = 176;
    goto loc_0096DDA1;
loc_0096DD87:
    result = HvpReleaseCellFlat(Arg5, Arg2, Arg2 + 9, (uint32_t)((uint32_t)(result)));
    goto loc_0096DC87;
loc_0096DD91:
    v_stack_p20 = 160;
loc_0096DD99:
loc_0096DDA1:
    Arg2 = 0;
    result = SetFailureLocation(Arg5, Arg2, 9, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
    goto loc_0096DCEF;
loc_0096DDB3:
    local_rdi = 0;
loc_0096DDB5:
    if (0 >= (*(uint32_t *)(arg1 + 0x750))) goto loc_0096DCED;
    result = (0) + (0);
    v_stack_p20 = 0;
    result = CmpCheckSecurityCellAccess(Arg1, (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x760) + result * 8)), 1, (uint32_t)(0x20019ULL));
    if (sign_flag) goto loc_0096DEA4;
    local_rdi = (uint32_t)((local_rdi) + 1);
    goto loc_0096DDB5;
loc_0096DDF4:
    result = HvpReleaseCellFlat(Arg1, (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x760) + result * 8)), 1, (uint32_t)(0x20019ULL));
    goto loc_0096DD26;
loc_0096DDFE:
    result = HvpReleaseCellFlat(Arg1, (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x760) + result * 8)), 1, (uint32_t)(0x20019ULL));
    goto loc_0096DD08;
loc_0096DE08:
    v_stack_p20 = 144;
    goto loc_0096DD99;
loc_0096DE12:
    *(uint32_t *)(arg1 + 0xF0) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x40) + 0x24)));
    goto loc_0096DD5B;
loc_0096DE24:
    *(uint32_t *)(Arg5 + 0xF0) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x40) + 0x24)));
loc_0096DE43:
    *(uint32_t *)(Arg5 + 0xF0) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x40) + 0x24)));
loc_0096DE62:
    result = CmpFindSecurityCellCacheIndex(Arg5, (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x40) + 0x24)), v_stack_p8, (uint32_t)(0x20019ULL));
    Arg1 = ((uint32_t)(v_stack_p8)) + ((uint32_t)(v_stack_p8));
    goto loc_0096DC67;
loc_0096DE92:
    v_stack_p20 = 200;
    goto loc_0096DD99;
loc_0096DEA4:
    Arg2 = 0;
    v_stack_p20 = 208;
    result = SetFailureLocation(Arg5, Arg2, Arg2 + 9, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == 0xC000009AULL) goto loc_0096DCEF;
    goto loc_0096DCEF;
loc_0096DED3:
    result = HvpReleaseCellFlat(Arg5, v_stack_m60, Arg2 + 9, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
loc_0096DEEF:
    result = HvpReleaseCellFlat(Arg1, v_stack_m60, Arg2 + 9, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
loc_0096DF0E:
    Arg2 = 0;
    v_stack_p20 = 128;
    result = SetFailureLocation(Arg5, Arg2, Arg2 + 9, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
    local_r14 = 0;
    goto loc_0096DCEF;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x40` | `64` | `R` |
| `Arg1` | `+ 0x8C` | `8` | `R` |
| `Arg1` | `+ 0x750` | `32` | `R` |
| `Arg1` | `+ 0x760` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0096DAFC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
