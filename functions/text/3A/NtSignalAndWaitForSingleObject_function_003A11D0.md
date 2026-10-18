# NtSignalAndWaitForSingleObject

- RVA: `0x003A11D0`–`0x003A1699` (길이 `1,225` bytes)
- VA: `0x00000001403A11D0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00081E68`
- 디코드: `298`개 명령, `1,225/1,225` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **23**; 고유 호출 대상: **12**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x003A124A` → [ObReferenceObjectByHandleWithTag](../../page/86/ObReferenceObjectByHandleWithTag_function_00869610.md) (function, `0x00869610`)
- `0x003A127D` → [ObReferenceObjectByHandleWithTag](../../page/86/ObReferenceObjectByHandleWithTag_function_00869610.md) (function, `0x00869610`)
- `0x003A1352` → [KeSetEvent](../33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x003A136D` → [KeWaitForSingleObject](../20/KeWaitForSingleObject_function_0020E6B0.md) (function, `0x0020E6B0`)
- `0x003A13B8` → [ObpPushStackInfo](../21/ObpPushStackInfo_function_002109E4.md) (function, `0x002109E4`)
- `0x003A13FE` → [ObpPushStackInfo](../21/ObpPushStackInfo_function_002109E4.md) (function, `0x002109E4`)
- `0x003A1455` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x003A1480` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x003A14C6` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x003A1501` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x003A156E` → [KeReleaseMutantEx](../39/KeReleaseMutantEx_function_00396850.md) (function, `0x00396850`)
- `0x003A15B8` → [KeAreAllApcsDisabled](../2F/KeAreAllApcsDisabled_function_002F7AC0.md) (function, `0x002F7AC0`)
- `0x003A15C4` → [OBJECT_HEADER_TO_HANDLE_REVOCATION_INFO](OBJECT_HEADER_TO_HANDLE_REVOCATION_INFO_function_003A1840.md) (function, `0x003A1840`)
- `0x003A15D1` → [ObpHandleRevocationBlockRemoveObject](../../page/9D/ObpHandleRevocationBlockRemoveObject_function_009D7E30.md) (function, `0x009D7E30`)
- `0x003A15E8` → [ObpDeregisterObject](../../page/9D/ObpDeregisterObject_function_009D7F78.md) (function, `0x009D7F78`)
- `0x003A15F2` → [ObpRemoveObjectRoutine](../../page/86/ObpRemoveObjectRoutine_function_00864A60.md) (function, `0x00864A60`)
- `0x003A15FC` → [ObpDeferObjectDeletion](ObpDeferObjectDeletion_function_003A2394.md) (function, `0x003A2394`)
- `0x003A1606` → [KeAreAllApcsDisabled](../2F/KeAreAllApcsDisabled_function_002F7AC0.md) (function, `0x002F7AC0`)
- `0x003A1612` → [OBJECT_HEADER_TO_HANDLE_REVOCATION_INFO](OBJECT_HEADER_TO_HANDLE_REVOCATION_INFO_function_003A1840.md) (function, `0x003A1840`)
- `0x003A161F` → [ObpHandleRevocationBlockRemoveObject](../../page/9D/ObpHandleRevocationBlockRemoveObject_function_009D7E30.md) (function, `0x009D7E30`)
- `0x003A1637` → [ObpDeregisterObject](../../page/9D/ObpDeregisterObject_function_009D7F78.md) (function, `0x009D7F78`)
- `0x003A1641` → [ObpRemoveObjectRoutine](../../page/86/ObpRemoveObjectRoutine_function_00864A60.md) (function, `0x00864A60`)
- `0x003A164B` → [ObpDeferObjectDeletion](ObpDeferObjectDeletion_function_003A2394.md) (function, `0x003A2394`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x003A1286` → RVA `0x00FC7800` (`ALMOSTRO`; read)
- `0x003A12C4` → RVA `0x00FC6E4C` (`ALMOSTRO`; read)
- `0x003A12F3` → RVA `0x00EFA128` (`.data`; read)
- `0x003A1328` → RVA `0x00FC6B80` (`ALMOSTRO`; read)
- `0x003A139B` → RVA `0x00FC5010` (`ALMOSTRO`; read)
- `0x003A1553` → RVA `0x00FC52B8` (`ALMOSTRO`; read)
- `0x003A1666` → RVA `0x00FC52C0` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **8**
  - `0x003A124A` → [ObReferenceObjectByHandleWithTag](../../page/86/ObReferenceObjectByHandleWithTag_function_00869610.md) (`.text` → `PAGE`)
  - `0x003A127D` → [ObReferenceObjectByHandleWithTag](../../page/86/ObReferenceObjectByHandleWithTag_function_00869610.md) (`.text` → `PAGE`)
  - `0x003A15D1` → [ObpHandleRevocationBlockRemoveObject](../../page/9D/ObpHandleRevocationBlockRemoveObject_function_009D7E30.md) (`.text` → `PAGE`)
  - `0x003A15E8` → [ObpDeregisterObject](../../page/9D/ObpDeregisterObject_function_009D7F78.md) (`.text` → `PAGE`)
  - `0x003A15F2` → [ObpRemoveObjectRoutine](../../page/86/ObpRemoveObjectRoutine_function_00864A60.md) (`.text` → `PAGE`)
  - `0x003A161F` → [ObpHandleRevocationBlockRemoveObject](../../page/9D/ObpHandleRevocationBlockRemoveObject_function_009D7E30.md) (`.text` → `PAGE`)
  - `0x003A1637` → [ObpDeregisterObject](../../page/9D/ObpDeregisterObject_function_009D7F78.md) (`.text` → `PAGE`)
  - `0x003A1641` → [ObpRemoveObjectRoutine](../../page/86/ObpRemoveObjectRoutine_function_00864A60.md) (`.text` → `PAGE`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x003A1671` → [sub_006E631C](../6E/Unknown_function_006E631C.md) (`tail-transfer`)
  - `0x003A167F` → [sub_006E631C](../6E/Unknown_function_006E631C.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003A11D0  4C 8B DC                        mov r11, rsp
003A11D3  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
003A11D7  49 89 73 10                     mov qword ptr [r11 + 0x10], rsi
003A11DB  4D 89 4B 20                     mov qword ptr [r11 + 0x20], r9
003A11DF  57                              push rdi
003A11E0  41 54                           push r12
003A11E2  41 55                           push r13
003A11E4  41 56                           push r14
003A11E6  41 57                           push r15
003A11E8  48 81 EC 90 00 00 00            sub rsp, 0x90
003A11EF  45 0F B6 E0                     movzx r12d, r8b
003A11F3  48 8B FA                        mov rdi, rdx
003A11F6  33 F6                           xor esi, esi
003A11F8  49 89 73 A8                     mov qword ptr [r11 - 0x58], rsi
003A11FC  49 89 73 98                     mov qword ptr [r11 - 0x68], rsi
003A1200  49 89 73 B0                     mov qword ptr [r11 - 0x50], rsi
003A1204  49 89 73 A0                     mov qword ptr [r11 - 0x60], rsi
003A1208  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
003A1211  0F B6 98 32 02 00 00            movzx ebx, byte ptr [rax + 0x232]
003A1218  4D 8B 7B 20                     mov r15, qword ptr [r11 + 0x20]
003A121C  4D 85 FF                        test r15, r15
003A121F  0F 85 E2 02 00 00               jne 0x1403a1507
003A1225  48 8D 44 24 60                  lea rax, [rsp + 0x60]
003A122A  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
003A122F  48 8D 44 24 50                  lea rax, [rsp + 0x50]
003A1234  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
003A1239  C7 44 24 20 4F 62 57 74         mov dword ptr [rsp + 0x20], 0x7457624f
003A1241  44 0F B6 CB                     movzx r9d, bl
003A1245  45 33 C0                        xor r8d, r8d
003A1248  33 D2                           xor edx, edx
003A124A  E8 C1 83 4C 00                  call 0x140869610
003A124F  85 C0                           test eax, eax
003A1251  0F 88 BB 01 00 00               js 0x1403a1412
003A1257  48 89 74 24 30                  mov qword ptr [rsp + 0x30], rsi
003A125C  48 8D 44 24 58                  lea rax, [rsp + 0x58]
003A1261  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
003A1266  C7 44 24 20 4F 62 57 74         mov dword ptr [rsp + 0x20], 0x7457624f
003A126E  44 0F B6 CB                     movzx r9d, bl
003A1272  45 33 C0                        xor r8d, r8d
003A1275  BA 00 00 10 00                  mov edx, 0x100000
003A127A  48 8B CF                        mov rcx, rdi
003A127D  E8 8E 83 4C 00                  call 0x140869610
003A1282  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
003A1286  4C 8D 2D 73 65 C2 00            lea r13, [rip + 0xc26573]
003A128D  85 C0                           test eax, eax
003A128F  0F 88 F1 01 00 00               js 0x1403a1486
003A1295  4C 8B 4C 24 58                  mov r9, qword ptr [rsp + 0x58]
003A129A  49 8D 79 D0                     lea rdi, [r9 - 0x30]
003A129E  48 89 7C 24 78                  mov qword ptr [rsp + 0x78], rdi
003A12A3  48 8B C7                        mov rax, rdi
003A12A6  48 C1 E8 08                     shr rax, 8
003A12AA  44 0F B6 D0                     movzx r10d, al
003A12AE  4C 89 54 24 48                  mov qword ptr [rsp + 0x48], r10
003A12B3  44 88 54 24 44                  mov byte ptr [rsp + 0x44], r10b
003A12B8  48 8D 47 18                     lea rax, [rdi + 0x18]
003A12BC  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
003A12C4  44 0F B6 1D 80 5B C2 00         movzx r11d, byte ptr [rip + 0xc25b80]
003A12CC  41 8B CB                        mov ecx, r11d
003A12CF  49 33 CA                        xor rcx, r10
003A12D2  0F B6 00                        movzx eax, byte ptr [rax]
003A12D5  48 33 C8                        xor rcx, rax
003A12D8  4D 8B 44 CD 00                  mov r8, qword ptr [r13 + rcx*8]
003A12DD  4D 8B 70 20                     mov r14, qword ptr [r8 + 0x20]
003A12E1  41 F6 C6 01                     test r14b, 1
003A12E5  0F 85 55 02 00 00               jne 0x1403a1540
003A12EB  4D 85 F6                        test r14, r14
003A12EE  78 03                           js 0x1403a12f3
003A12F0  4D 03 F1                        add r14, r9
003A12F3  4C 39 05 2E 8E B5 00            cmp qword ptr [rip + 0xb58e2e], r8
003A12FA  0F 84 87 03 00 00               je 0x1403a1687
003A1300  4C 8B 54 24 50                  mov r10, qword ptr [rsp + 0x50]
003A1305  49 8D 42 D0                     lea rax, [r10 - 0x30]
003A1309  48 C1 E8 08                     shr rax, 8
003A130D  0F B6 D0                        movzx edx, al
003A1310  41 0F B6 42 E8                  movzx eax, byte ptr [r10 - 0x18]
003A1315  48 33 D0                        xor rdx, rax
003A1318  49 33 D3                        xor rdx, r11
003A131B  49 8B 44 D5 00                  mov rax, qword ptr [r13 + rdx*8]
003A1320  C7 44 24 40 22 00 00 C0         mov dword ptr [rsp + 0x40], 0xc0000022
003A1328  48 3B 05 51 58 C2 00            cmp rax, qword ptr [rip + 0xc25851]
003A132F  0F 85 1E 02 00 00               jne 0x1403a1553
003A1335  84 DB                           test bl, bl
003A1337  74 0E                           je 0x1403a1347
003A1339  8B 44 24 64                     mov eax, dword ptr [rsp + 0x64]
003A133D  F7 D0                           not eax
003A133F  A8 02                           test al, 2
003A1341  0F 85 48 03 00 00               jne 0x1403a168f
003A1347  41 B0 01                        mov r8b, 1
003A134A  BA 01 00 00 00                  mov edx, 1
003A134F  49 8B CA                        mov rcx, r10
003A1352  E8 B9 DF F9 FF                  call 0x14033f310
003A1357  90                              nop
003A1358  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
003A135D  45 0F B6 CC                     movzx r9d, r12b
003A1361  44 0F B6 C3                     movzx r8d, bl
003A1365  BA 06 00 00 00                  mov edx, 6
003A136A  49 8B CE                        mov rcx, r14
003A136D  E8 3E D3 E6 FF                  call 0x14020e6b0
003A1372  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
003A1376  4C 8B 74 24 48                  mov r14, qword ptr [rsp + 0x48]
003A137B  EB 1C                           jmp 0x1403a1399
003A137D  89 44 24 70                     mov dword ptr [rsp + 0x70], eax
003A1381  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
003A1385  33 F6                           xor esi, esi
003A1387  4C 8D 2D 72 64 C2 00            lea r13, [rip + 0xc26472]
003A138E  44 0F B6 74 24 44               movzx r14d, byte ptr [rsp + 0x44]
003A1394  48 8B 7C 24 78                  mov rdi, qword ptr [rsp + 0x78]
003A1399  8B C6                           mov eax, esi
003A139B  83 3D 6E 3C C2 00 00            cmp dword ptr [rip + 0xc23c6e], 0
003A13A2  0F 95 C0                        setne al
003A13A5  85 C0                           test eax, eax
003A13A7  74 14                           je 0x1403a13bd
003A13A9  33 D2                           xor edx, edx
003A13AB  41 B9 4F 62 57 74               mov r9d, 0x7457624f
003A13B1  44 8D 42 01                     lea r8d, [rdx + 1]
003A13B5  48 8B CF                        mov rcx, rdi
003A13B8  E8 27 F6 E6 FF                  call 0x1402109e4
003A13BD  48 C7 C3 FF FF FF FF            mov rbx, 0xffffffffffffffff
003A13C4  48 8B C3                        mov rax, rbx
003A13C7  F0 48 0F C1 07                  lock xadd qword ptr [rdi], rax
003A13CC  48 83 E8 01                     sub rax, 1
003A13D0  0F 8E 85 00 00 00               jle 0x1403a145b
003A13D6  48 8B 7C 24 50                  mov rdi, qword ptr [rsp + 0x50]
003A13DB  48 83 C7 D0                     add rdi, -0x30
003A13DF  8B C6                           mov eax, esi
003A13E1  83 3D 28 3C C2 00 00            cmp dword ptr [rip + 0xc23c28], 0
003A13E8  0F 95 C0                        setne al
003A13EB  85 C0                           test eax, eax
003A13ED  74 14                           je 0x1403a1403
003A13EF  33 D2                           xor edx, edx
003A13F1  41 B9 4F 62 57 74               mov r9d, 0x7457624f
003A13F7  44 8D 42 01                     lea r8d, [rdx + 1]
003A13FB  48 8B CF                        mov rcx, rdi
003A13FE  E8 E1 F5 E6 FF                  call 0x1402109e4
003A1403  F0 48 0F C1 1F                  lock xadd qword ptr [rdi], rbx
003A1408  48 83 EB 01                     sub rbx, 1
003A140C  7E 22                           jle 0x1403a1430
003A140E  8B 44 24 40                     mov eax, dword ptr [rsp + 0x40]
003A1412  4C 8D 9C 24 90 00 00 00         lea r11, [rsp + 0x90]
003A141A  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
003A141E  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
003A1422  49 8B E3                        mov rsp, r11
003A1425  41 5F                           pop r15
003A1427  41 5E                           pop r14
003A1429  41 5D                           pop r13
003A142B  41 5C                           pop r12
003A142D  5F                              pop rdi
003A142E  C3                              ret
003A142F  CC                              int3
003A1430  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
003A1434  48 85 C9                        test rcx, rcx
003A1437  75 59                           jne 0x1403a1492
003A1439  48 85 DB                        test rbx, rbx
003A143C  0F 89 76 01 00 00               jns 0x1403a15b8
003A1442  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
003A1447  44 8D 49 02                     lea r9d, [rcx + 2]
003A144B  4C 8B 44 24 50                  mov r8, qword ptr [rsp + 0x50]
003A1450  33 D2                           xor edx, edx
003A1452  8D 4A 18                        lea ecx, [rdx + 0x18]
003A1455  E8 06 C2 15 00                  call 0x1404fd660
003A145A  CC                              int3
003A145B  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
003A145F  48 85 C9                        test rcx, rcx
003A1462  75 68                           jne 0x1403a14cc
003A1464  48 85 C0                        test rax, rax
003A1467  0F 89 99 01 00 00               jns 0x1403a1606
003A146D  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
003A1472  44 8D 49 02                     lea r9d, [rcx + 2]
003A1476  4C 8B 44 24 58                  mov r8, qword ptr [rsp + 0x58]
003A147B  33 D2                           xor edx, edx
003A147D  8D 4A 18                        lea ecx, [rdx + 0x18]
003A1480  E8 DB C1 15 00                  call 0x1404fd660
003A1485  CC                              int3
003A1486  48 C7 C3 FF FF FF FF            mov rbx, 0xffffffffffffffff
003A148D  E9 44 FF FF FF                  jmp 0x1403a13d6
003A1492  48 8B C7                        mov rax, rdi
003A1495  48 C1 E8 08                     shr rax, 8
003A1499  0F B6 D0                        movzx edx, al
003A149C  0F B6 47 18                     movzx eax, byte ptr [rdi + 0x18]
003A14A0  48 33 D0                        xor rdx, rax
003A14A3  0F B6 05 A2 59 C2 00            movzx eax, byte ptr [rip + 0xc259a2]
003A14AA  48 33 D0                        xor rdx, rax
003A14AD  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
003A14B2  41 B9 01 00 00 00               mov r9d, 1
003A14B8  4C 8B 44 24 50                  mov r8, qword ptr [rsp + 0x50]
003A14BD  49 8B 54 D5 00                  mov rdx, qword ptr [r13 + rdx*8]
003A14C2  41 8D 49 17                     lea ecx, [r9 + 0x17]
003A14C6  E8 95 C1 15 00                  call 0x1404fd660
003A14CB  CC                              int3
003A14CC  41 0F B6 D6                     movzx edx, r14b
003A14D0  0F B6 05 75 59 C2 00            movzx eax, byte ptr [rip + 0xc25975]
003A14D7  48 33 D0                        xor rdx, rax
003A14DA  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
003A14E2  0F B6 00                        movzx eax, byte ptr [rax]
003A14E5  48 33 D0                        xor rdx, rax
003A14E8  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
003A14ED  41 B9 01 00 00 00               mov r9d, 1
003A14F3  4C 8B 44 24 58                  mov r8, qword ptr [rsp + 0x58]
003A14F8  49 8B 54 D5 00                  mov rdx, qword ptr [r13 + rdx*8]
003A14FD  41 8D 49 17                     lea ecx, [r9 + 0x17]
003A1501  E8 5A C1 15 00                  call 0x1404fd660
003A1506  CC                              int3
003A1507  84 DB                           test bl, bl
003A1509  0F 84 16 FD FF FF               je 0x1403a1225
003A150F  48 B8 00 00 FF FF FF 7F 00 00   movabs rax, 0x7fffffff0000
003A1519  4C 3B F8                        cmp r15, rax
003A151C  49 0F 42 C7                     cmovb rax, r15
003A1520  90                              nop
003A1521  48 8B 00                        mov rax, qword ptr [rax]
003A1524  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
003A1529  4C 8D 7C 24 68                  lea r15, [rsp + 0x68]
003A152E  4C 89 BC 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], r15
003A1536  E9 EA FC FF FF                  jmp 0x1403a1225
003A153B  E9 D2 FE FF FF                  jmp 0x1403a1412
003A1540  41 F6 C6 02                     test r14b, 2
003A1544  75 4C                           jne 0x1403a1592
003A1546  4B 8D 04 0E                     lea rax, [r14 + r9]
003A154A  4C 8B 70 FF                     mov r14, qword ptr [rax - 1]
003A154E  E9 A0 FD FF FF                  jmp 0x1403a12f3
003A1553  48 3B 05 5E 3D C2 00            cmp rax, qword ptr [rip + 0xc23d5e]
003A155A  0F 85 06 01 00 00               jne 0x1403a1666
003A1560  45 33 C9                        xor r9d, r9d
003A1563  41 8D 51 01                     lea edx, [r9 + 1]
003A1567  45 8D 41 02                     lea r8d, [r9 + 2]
003A156B  49 8B CA                        mov rcx, r10
003A156E  E8 DD 52 FF FF                  call 0x140396850
003A1573  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
003A1577  3D 80 00 00 00                  cmp eax, 0x80
003A157C  0F 84 0D 01 00 00               je 0x1403a168f
003A1582  3D 46 00 00 C0                  cmp eax, 0xc0000046
003A1587  0F 85 CB FD FF FF               jne 0x1403a1358
003A158D  E9 FD 00 00 00                  jmp 0x1403a168f
003A1592  41 0F B7 90 B4 00 00 00         movzx edx, word ptr [r8 + 0xb4]
003A159A  41 8B 88 B0 00 00 00            mov ecx, dword ptr [r8 + 0xb0]
003A15A1  8B C1                           mov eax, ecx
003A15A3  42 23 04 0A                     and eax, dword ptr [rdx + r9]
003A15A7  3B C1                           cmp eax, ecx
003A15A9  0F 84 A6 00 00 00               je 0x1403a1655
003A15AF  49 83 C6 FD                     add r14, -3
003A15B3  E9 38 FD FF FF                  jmp 0x1403a12f0
003A15B8  E8 03 65 F5 FF                  call 0x1402f7ac0
003A15BD  48 8B CF                        mov rcx, rdi
003A15C0  84 C0                           test al, al
003A15C2  75 38                           jne 0x1403a15fc
003A15C4  E8 77 02 00 00                  call 0x1403a1840
003A15C9  48 85 C0                        test rax, rax
003A15CC  74 08                           je 0x1403a15d6
003A15CE  48 8B C8                        mov rcx, rax
003A15D1  E8 5A 68 63 00                  call 0x1409d7e30
003A15D6  83 3D 33 3A C2 00 00            cmp dword ptr [rip + 0xc23a33], 0
003A15DD  40 0F 95 C6                     setne sil
003A15E1  85 F6                           test esi, esi
003A15E3  74 08                           je 0x1403a15ed
003A15E5  48 8B CF                        mov rcx, rdi
003A15E8  E8 8B 69 63 00                  call 0x1409d7f78
003A15ED  33 D2                           xor edx, edx
003A15EF  48 8B CF                        mov rcx, rdi
003A15F2  E8 69 34 4C 00                  call 0x140864a60
003A15F7  E9 12 FE FF FF                  jmp 0x1403a140e
003A15FC  E8 93 0D 00 00                  call 0x1403a2394
003A1601  E9 08 FE FF FF                  jmp 0x1403a140e
003A1606  E8 B5 64 F5 FF                  call 0x1402f7ac0
003A160B  48 8B CF                        mov rcx, rdi
003A160E  84 C0                           test al, al
003A1610  75 39                           jne 0x1403a164b
003A1612  E8 29 02 00 00                  call 0x1403a1840
003A1617  48 85 C0                        test rax, rax
003A161A  74 08                           je 0x1403a1624
003A161C  48 8B C8                        mov rcx, rax
003A161F  E8 0C 68 63 00                  call 0x1409d7e30
003A1624  8B C6                           mov eax, esi
003A1626  83 3D E3 39 C2 00 00            cmp dword ptr [rip + 0xc239e3], 0
003A162D  0F 95 C0                        setne al
003A1630  85 C0                           test eax, eax
003A1632  74 08                           je 0x1403a163c
003A1634  48 8B CF                        mov rcx, rdi
003A1637  E8 3C 69 63 00                  call 0x1409d7f78
003A163C  33 D2                           xor edx, edx
003A163E  48 8B CF                        mov rcx, rdi
003A1641  E8 1A 34 4C 00                  call 0x140864a60
003A1646  E9 8B FD FF FF                  jmp 0x1403a13d6
003A164B  E8 44 0D 00 00                  call 0x1403a2394
003A1650  E9 81 FD FF FF                  jmp 0x1403a13d6
003A1655  41 0F B7 80 B6 00 00 00         movzx eax, word ptr [r8 + 0xb6]
003A165D  4E 8B 34 08                     mov r14, qword ptr [rax + r9]
003A1661  E9 8D FC FF FF                  jmp 0x1403a12f3
003A1666  48 3B 05 53 3C C2 00            cmp rax, qword ptr [rip + 0xc23c53]
003A166D  75 18                           jne 0x1403a1687
003A166F  84 DB                           test bl, bl
003A1671  0F 84 A5 4C 34 00               je 0x1406e631c
003A1677  8B 44 24 64                     mov eax, dword ptr [rsp + 0x64]
003A167B  F7 D0                           not eax
003A167D  A8 02                           test al, 2
003A167F  0F 84 97 4C 34 00               je 0x1406e631c
003A1685  EB 08                           jmp 0x1403a168f
003A1687  C7 44 24 40 24 00 00 C0         mov dword ptr [rsp + 0x40], 0xc0000024
003A168F  4C 8B 74 24 48                  mov r14, qword ptr [rsp + 0x48]
003A1694  E9 00 FD FF FF                  jmp 0x1403a1399
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtSignalAndWaitForSingleObject(__int64 a1, __int64 a2, int a3, __int64 a4)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m2C;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned int v_stack_m48;
    unsigned int v_stack_m50;
    unsigned int v_stack_m54;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int8 v_stack_m74;
    unsigned int v_stack_m78;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned int v_stack_m98;
    unsigned __int64 v_stack_p48;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = a4;
    v_rsp = (v_rsp) - (144);
    v_rsi = 0;
    *(unsigned __int64 *)(v_rsp - 88) = 0;
    *(unsigned __int64 *)(v_rsp - 104) = 0;
    *(unsigned __int64 *)(v_rsp - 80) = 0;
    *(unsigned __int64 *)(v_rsp - 96) = 0;
    if (*(unsigned __int64 *)(v_rsp + 32) != 0) goto loc_003A1507;
loc_003A1225:
    v_stack_m88 = v_stack_m58;
    v_stack_m90 = v_stack_m68;
    v_stack_m98 = 0x7457624FULL;
    a3 = 0;
    a2 = 0;
    result = ObReferenceObjectByHandleWithTag(a1, a2, a3, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    if (sign_flag) goto loc_003A1412;
    v_stack_m88 = 0;
    v_stack_m90 = v_stack_m60;
    v_stack_m98 = 0x7457624FULL;
    a3 = 0;
    result = ObReferenceObjectByHandleWithTag(0, (unsigned int)(0x100000ULL), a3, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    v_stack_m78 = (unsigned int)(result);
    if (sign_flag) goto loc_003A1486;
    v_stack_m40 = v_stack_m60 - 48;
    result = (v_stack_m60 - 48) >> (8);
    v_stack_m70 = (unsigned __int8)(result);
    v_stack_m74 = (unsigned __int8)((unsigned __int8)(result));
    v_stack_m38 = v_stack_m60 - 48 + 24;
    a1 = ((unsigned int)((unsigned int)(*(unsigned __int8 *)(v_rip + 12737408)))) ^ ((unsigned __int8)(result));
    a1 = (a1) ^ (*(unsigned __int8 *)(v_stack_m60 - 48 + 24));
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12739955 + a1 * 8) + 32))) & (1)) != 0) goto loc_003A1540;
    v_r14 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12739955 + a1 * 8) + 32);
    if (!(sign_flag)) {
        v_r14 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12739955 + a1 * 8) + 32)) + (v_stack_m60);
    }
    if ((*(unsigned __int64 *)(v_rip + 11898414)) == (*(unsigned __int64 *)(v_rip + 12739955 + a1 * 8))) goto loc_003A1687;
    result = (v_stack_m68 - 48) >> (8);
    a2 = ((unsigned __int8)(result)) ^ (*(unsigned __int8 *)(v_stack_m68 - 24));
    a2 = (a2) ^ (*(unsigned __int8 *)(v_rip + 12737408));
    v_stack_m78 = 0xC0000022ULL;
    if ((*(unsigned __int64 *)(v_rip + 12739955 + a2 * 8)) != (*(unsigned __int64 *)(v_rip + 12736593))) goto loc_003A1553;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_003A1347;
    result = (unsigned int)(~((unsigned int)(v_stack_m54)));
    if ((((unsigned __int8)(result)) & (2)) != 0) goto loc_003A168F;
loc_003A1347:
    result = KeSetEvent(v_stack_m68, 1, 1, v_stack_m60);
loc_003A1358:
    v_stack_m98 = *(unsigned __int64 *)(v_rsp + 32);
    result = KeWaitForSingleObject(v_r14, 6, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), (unsigned __int8)((unsigned __int8)(a3)));
    v_stack_m78 = (unsigned int)(result);
    goto loc_003A1399;
loc_003A1399:
    result = ((*(unsigned int *)(v_rip + 12729454)) != 0) ? 1 : 0;
    if ((unsigned int)(result) != 0) {
        a2 = 0;
        a4 = 0x7457624FULL;
        a3 = a2 + 1;
        a1 = v_stack_m60 - 48;
        result = ObpPushStackInfo(a1, a2, a3, a4);
    }
    result = (-1) - (1);
    if (condition_is_less_or_equal) goto loc_003A145B;
loc_003A13D6:
    v_rdi = (v_stack_m68) + (-48);
    result = ((*(unsigned int *)(v_rip + 12729384)) != 0) ? 1 : 0;
    if ((unsigned int)(result) != 0) {
        a2 = 0;
        a4 = 0x7457624FULL;
        a3 = a2 + 1;
        a1 = v_rdi;
        result = ObpPushStackInfo(a1, a2, a3, a4);
    }
    v_rbx = (-1) - (1);
    if (condition_is_less_or_equal) goto loc_003A1430;
loc_003A140E:
loc_003A1412:
    return (unsigned int)(v_stack_m78);
loc_003A1430:
    if (*(unsigned __int64 *)(v_rdi + 8) != 0) goto loc_003A1492;
    if (!sign_flag) goto loc_003A15B8;
    v_stack_m70 = *(unsigned __int64 *)(v_stack_m28 + 48);
    a2 = 0;
    result = KeBugCheckEx(a2 + 24, a2, v_stack_m40, *(unsigned __int64 *)(v_rdi + 8) + 2);
loc_003A145B:
    if (*(unsigned __int64 *)(v_rdi + 8) != 0) goto loc_003A14CC;
    if (!sign_flag) goto loc_003A1606;
    v_stack_m70 = result;
    a2 = 0;
    result = KeBugCheckEx(a2 + 24, a2, v_stack_m38, *(unsigned __int64 *)(v_rdi + 8) + 2);
loc_003A1486:
    goto loc_003A13D6;
loc_003A1492:
    result = (v_rdi) >> (8);
    a2 = ((unsigned __int8)(result)) ^ (*(unsigned __int8 *)(v_rdi + 24));
    a2 = (a2) ^ (*(unsigned __int8 *)(v_rip + 12736930));
    v_stack_m70 = a2 + 24;
    result = KeBugCheckEx(1 + 23, *(unsigned __int64 *)(v_rip + 12739955 + a2 * 8), v_stack_m40, 1);
loc_003A14CC:
    a2 = ((unsigned __int8)(v_stack_m70)) ^ (*(unsigned __int8 *)(v_rip + 12736885));
    a2 = (a2) ^ (*(unsigned __int8 *)(v_stack_m10));
    v_stack_m70 = 1 + 23;
    result = KeBugCheckEx(1 + 23, *(unsigned __int64 *)(v_rip + 12739955 + a2 * 8), v_stack_m38, 1);
loc_003A1507:
    if (-1 == 0) goto loc_003A1225;
    if ((*(unsigned __int64 *)(v_rsp + 32)) < result) { result = *(unsigned __int64 *)(v_rsp + 32); }
    v_stack_m28 = *(unsigned __int64 *)(result);
    v_stack_p48 = v_stack_m28;
    goto loc_003A1225;
loc_003A1540:
    if ((((unsigned __int8)(v_stack_m70)) & (2)) != 0) goto loc_003A1592;
    goto loc_003A12F3;
loc_003A1553:
    if ((v_stack_m70 + 1 * 1) != (*(unsigned __int64 *)(v_rip + 12729694))) goto loc_003A1666;
    a4 = 0;
    result = KeReleaseMutantEx(v_stack_m68, a4 + 1, a4 + 2, a4);
    v_stack_m50 = (unsigned int)(result);
    if (((unsigned int)(result)) == 128) goto loc_003A168F;
    if (((unsigned int)(result)) != 0xC0000046ULL) goto loc_003A1358;
    goto loc_003A168F;
loc_003A1592:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 2 + 176))))) & (*(unsigned int *)(*(unsigned __int16 *)(a4 + 2 + 180) + a4 * 1)));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 2 + 176))))) goto loc_003A1655;
    v_r14 = (*(unsigned __int64 *)(v_stack_m70 + 1 * 1 - 1)) + (-3);
    goto loc_003A12F0;
loc_003A15B8:
    result = KeAreAllApcsDisabled((unsigned int)(*(unsigned int *)(a4 + 2 + 176)), *(unsigned __int16 *)(a4 + 2 + 180), a4 + 2, a4);
    if ((unsigned __int8)(result) != 0) goto loc_003A15FC;
    result = OBJECT_HEADER_TO_HANDLE_REVOCATION_INFO(v_rdi, *(unsigned __int16 *)(a4 + 2 + 180), a4 + 2, a4);
    if (result != 0) {
        a1 = result;
        result = ObpHandleRevocationBlockRemoveObject(a1, *(unsigned __int16 *)(a4 + 2 + 180), a4 + 2, a4);
    }
    v_rsi = ((*(unsigned int *)(v_rip + 12728883)) != 0) ? 1 : 0;
    if ((unsigned int)(v_rsi) != 0) {
        a1 = v_rdi;
        result = ObpDeregisterObject(a1, *(unsigned __int16 *)(a4 + 2 + 180), a4 + 2, a4);
    }
    a2 = 0;
    result = ObpRemoveObjectRoutine(v_rdi, a2, a4 + 2, a4);
    goto loc_003A140E;
loc_003A15FC:
    result = ObpDeferObjectDeletion(v_rdi, a2, a4 + 2, a4);
    goto loc_003A140E;
loc_003A1606:
    result = KeAreAllApcsDisabled(v_rdi, a2, a4 + 2, a4);
    if ((unsigned __int8)(result) != 0) goto loc_003A164B;
    result = OBJECT_HEADER_TO_HANDLE_REVOCATION_INFO(v_rdi, a2, a4 + 2, a4);
    if (result != 0) {
        a1 = result;
        result = ObpHandleRevocationBlockRemoveObject(a1, a2, a4 + 2, a4);
    }
    result = ((*(unsigned int *)(v_rip + 12728803)) != 0) ? 1 : 0;
    if ((unsigned int)(result) != 0) {
        a1 = v_rdi;
        result = ObpDeregisterObject(a1, a2, a4 + 2, a4);
    }
    a2 = 0;
    result = ObpRemoveObjectRoutine(v_rdi, a2, a4 + 2, a4);
    goto loc_003A13D6;
loc_003A164B:
    result = ObpDeferObjectDeletion(v_rdi, a2, a4 + 2, a4);
    goto loc_003A13D6;
loc_003A1655:
    goto loc_003A12F3;
loc_003A1666:
    if ((*(unsigned __int16 *)(a4 + 2 + 182)) != (*(unsigned __int64 *)(v_rip + 12729427))) goto loc_003A1687;
    result = (unsigned int)(~((unsigned int)(v_stack_m2C)));
    goto loc_003A168F;
loc_003A1687:
    v_stack_m50 = 0xC0000024ULL;
loc_003A168F:
    goto loc_003A1399;
}
```

## 5. (Beta) C Style

```c
int64_t NtSignalAndWaitForSingleObject(int64_t Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint64_t v_stack_m28;
    uint32_t v_stack_m2C;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint32_t v_stack_m48;
    uint32_t v_stack_m50;
    uint32_t v_stack_m54;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint8_t v_stack_m74;
    uint32_t v_stack_m78;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint32_t v_stack_m98;
    uint64_t v_stack_p48;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = Arg4;
    local_rsp = (local_rsp) - (144);
    local_rsi = 0;
    *(uint64_t *)(local_rsp - 0x58) = 0;
    *(uint64_t *)(local_rsp - 0x68) = 0;
    *(uint64_t *)(local_rsp - 0x50) = 0;
    *(uint64_t *)(local_rsp - 0x60) = 0;
    if (*(uint64_t *)(local_rsp + 0x20) != 0) goto loc_003A1507;
loc_003A1225:
    v_stack_m88 = v_stack_m58;
    v_stack_m90 = v_stack_m68;
    v_stack_m98 = 0x7457624FULL;
    Arg3 = 0;
    Arg2 = 0;
    result = ObReferenceObjectByHandleWithTag(Arg1, Arg2, Arg3, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    if (sign_flag) goto loc_003A1412;
    v_stack_m88 = 0;
    v_stack_m90 = v_stack_m60;
    v_stack_m98 = 0x7457624FULL;
    Arg3 = 0;
    result = ObReferenceObjectByHandleWithTag(0, (uint32_t)(0x100000ULL), Arg3, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    v_stack_m78 = (uint32_t)(result);
    if (sign_flag) goto loc_003A1486;
    v_stack_m40 = v_stack_m60 - 48;
    result = (v_stack_m60 - 48) >> (8);
    v_stack_m70 = (uint8_t)(result);
    v_stack_m74 = (uint8_t)((uint8_t)(result));
    v_stack_m38 = v_stack_m60 - 48 + 24;
    Arg1 = ((uint32_t)((uint32_t)(*(uint8_t *)(v_rip + 0xC25B80)))) ^ ((uint8_t)(result));
    Arg1 = (Arg1) ^ (*(uint8_t *)(v_stack_m60 - 0x30 + 0x18));
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xC26573 + Arg1 * 8) + 0x20))) & (1)) != 0) goto loc_003A1540;
    local_r14 = *(uint64_t *)(*(uint64_t *)(v_rip + 0xC26573 + Arg1 * 8) + 0x20);
    if (!(sign_flag)) {
        local_r14 = (*(uint64_t *)(*(uint64_t *)(v_rip + 0xC26573 + Arg1 * 8) + 0x20)) + (v_stack_m60);
    }
    if ((*(uint64_t *)(v_rip + 0xB58E2E)) == (*(uint64_t *)(v_rip + 0xC26573 + Arg1 * 8))) goto loc_003A1687;
    result = (v_stack_m68 - 48) >> (8);
    Arg2 = ((uint8_t)(result)) ^ (*(uint8_t *)(v_stack_m68 - 0x18));
    Arg2 = (Arg2) ^ (*(uint8_t *)(v_rip + 0xC25B80));
    v_stack_m78 = 0xC0000022ULL;
    if ((*(uint64_t *)(v_rip + 0xC26573 + Arg2 * 8)) != (*(uint64_t *)(v_rip + 0xC25851))) goto loc_003A1553;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_003A1347;
    result = (uint32_t)(~((uint32_t)(v_stack_m54)));
    if ((((uint8_t)(result)) & (2)) != 0) goto loc_003A168F;
loc_003A1347:
    result = KeSetEvent(v_stack_m68, 1, 1, v_stack_m60);
loc_003A1358:
    v_stack_m98 = *(uint64_t *)(local_rsp + 0x20);
    result = KeWaitForSingleObject(local_r14, 6, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), (uint8_t)((uint8_t)(Arg3)));
    v_stack_m78 = (uint32_t)(result);
    goto loc_003A1399;
loc_003A1399:
    result = ((*(uint32_t *)(v_rip + 0xC23C6E)) != 0) ? 1 : 0;
    if ((uint32_t)(result) != 0) {
        Arg2 = 0;
        Arg4 = 0x7457624FULL;
        Arg3 = Arg2 + 1;
        Arg1 = v_stack_m60 - 48;
        result = ObpPushStackInfo(Arg1, Arg2, Arg3, Arg4);
    }
    result = (-1) - (1);
    if (condition_is_less_or_equal) goto loc_003A145B;
loc_003A13D6:
    local_rdi = (v_stack_m68) + (-48);
    result = ((*(uint32_t *)(v_rip + 0xC23C28)) != 0) ? 1 : 0;
    if ((uint32_t)(result) != 0) {
        Arg2 = 0;
        Arg4 = 0x7457624FULL;
        Arg3 = Arg2 + 1;
        Arg1 = local_rdi;
        result = ObpPushStackInfo(Arg1, Arg2, Arg3, Arg4);
    }
    local_rbx = (-1) - (1);
    if (condition_is_less_or_equal) goto loc_003A1430;
loc_003A140E:
loc_003A1412:
    return (uint32_t)(v_stack_m78);
loc_003A1430:
    if (*(uint64_t *)(local_rdi + 0x8) != 0) goto loc_003A1492;
    if (!sign_flag) goto loc_003A15B8;
    v_stack_m70 = *(uint64_t *)(v_stack_m28 + 0x30);
    Arg2 = 0;
    result = KeBugCheckEx(Arg2 + 24, Arg2, v_stack_m40, *(uint64_t *)(local_rdi + 0x8) + 2);
loc_003A145B:
    if (*(uint64_t *)(local_rdi + 0x8) != 0) goto loc_003A14CC;
    if (!sign_flag) goto loc_003A1606;
    v_stack_m70 = result;
    Arg2 = 0;
    result = KeBugCheckEx(Arg2 + 24, Arg2, v_stack_m38, *(uint64_t *)(local_rdi + 0x8) + 2);
loc_003A1486:
    goto loc_003A13D6;
loc_003A1492:
    result = (local_rdi) >> (8);
    Arg2 = ((uint8_t)(result)) ^ (*(uint8_t *)(local_rdi + 0x18));
    Arg2 = (Arg2) ^ (*(uint8_t *)(v_rip + 0xC259A2));
    v_stack_m70 = Arg2 + 24;
    result = KeBugCheckEx(1 + 23, *(uint64_t *)(v_rip + 0xC26573 + Arg2 * 8), v_stack_m40, 1);
loc_003A14CC:
    Arg2 = ((uint8_t)(v_stack_m70)) ^ (*(uint8_t *)(v_rip + 0xC25975));
    Arg2 = (Arg2) ^ (*(uint8_t *)(v_stack_m10));
    v_stack_m70 = 1 + 23;
    result = KeBugCheckEx(1 + 23, *(uint64_t *)(v_rip + 0xC26573 + Arg2 * 8), v_stack_m38, 1);
loc_003A1507:
    if (-1 == 0) goto loc_003A1225;
    if ((*(uint64_t *)(local_rsp + 0x20)) < result) { result = *(uint64_t *)(local_rsp + 0x20); }
    v_stack_m28 = *(uint64_t *)(result);
    v_stack_p48 = v_stack_m28;
    goto loc_003A1225;
loc_003A1540:
    if ((((uint8_t)(v_stack_m70)) & (2)) != 0) goto loc_003A1592;
    goto loc_003A12F3;
loc_003A1553:
    if ((v_stack_m70 + 1 * 1) != (*(uint64_t *)(v_rip + 0xC23D5E))) goto loc_003A1666;
    Arg4 = 0;
    result = KeReleaseMutantEx(v_stack_m68, Arg4 + 1, Arg4 + 2, Arg4);
    v_stack_m50 = (uint32_t)(result);
    if (((uint32_t)(result)) == 128) goto loc_003A168F;
    if (((uint32_t)(result)) != 0xC0000046ULL) goto loc_003A1358;
    goto loc_003A168F;
loc_003A1592:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x2 + 0xB0))))) & (*(uint32_t *)(*(uint16_t *)(Arg4 + 0x2 + 0xB4) + Arg4 * 1)));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x2 + 0xB0))))) goto loc_003A1655;
    local_r14 = (*(uint64_t *)(v_stack_m70 + 0x1 * 1 - 0x1)) + (-3);
    goto loc_003A12F0;
loc_003A15B8:
    result = KeAreAllApcsDisabled((uint32_t)(*(uint32_t *)(Arg4 + 0x2 + 0xB0)), *(uint16_t *)(Arg4 + 0x2 + 0xB4), Arg4 + 2, Arg4);
    if ((uint8_t)(result) != 0) goto loc_003A15FC;
    result = OBJECT_HEADER_TO_HANDLE_REVOCATION_INFO(local_rdi, *(uint16_t *)(Arg4 + 0x2 + 0xB4), Arg4 + 2, Arg4);
    if (result != 0) {
        Arg1 = result;
        result = ObpHandleRevocationBlockRemoveObject(Arg1, *(uint16_t *)(Arg4 + 0x2 + 0xB4), Arg4 + 2, Arg4);
    }
    local_rsi = ((*(uint32_t *)(v_rip + 0xC23A33)) != 0) ? 1 : 0;
    if ((uint32_t)(local_rsi) != 0) {
        Arg1 = local_rdi;
        result = ObpDeregisterObject(Arg1, *(uint16_t *)(Arg4 + 0x2 + 0xB4), Arg4 + 2, Arg4);
    }
    Arg2 = 0;
    result = ObpRemoveObjectRoutine(local_rdi, Arg2, Arg4 + 2, Arg4);
    goto loc_003A140E;
loc_003A15FC:
    result = ObpDeferObjectDeletion(local_rdi, Arg2, Arg4 + 2, Arg4);
    goto loc_003A140E;
loc_003A1606:
    result = KeAreAllApcsDisabled(local_rdi, Arg2, Arg4 + 2, Arg4);
    if ((uint8_t)(result) != 0) goto loc_003A164B;
    result = OBJECT_HEADER_TO_HANDLE_REVOCATION_INFO(local_rdi, Arg2, Arg4 + 2, Arg4);
    if (result != 0) {
        Arg1 = result;
        result = ObpHandleRevocationBlockRemoveObject(Arg1, Arg2, Arg4 + 2, Arg4);
    }
    result = ((*(uint32_t *)(v_rip + 0xC239E3)) != 0) ? 1 : 0;
    if ((uint32_t)(result) != 0) {
        Arg1 = local_rdi;
        result = ObpDeregisterObject(Arg1, Arg2, Arg4 + 2, Arg4);
    }
    Arg2 = 0;
    result = ObpRemoveObjectRoutine(local_rdi, Arg2, Arg4 + 2, Arg4);
    goto loc_003A13D6;
loc_003A164B:
    result = ObpDeferObjectDeletion(local_rdi, Arg2, Arg4 + 2, Arg4);
    goto loc_003A13D6;
loc_003A1655:
    goto loc_003A12F3;
loc_003A1666:
    if ((*(uint16_t *)(Arg4 + 0x2 + 0xB6)) != (*(uint64_t *)(v_rip + 0xC23C53))) goto loc_003A1687;
    result = (uint32_t)(~((uint32_t)(v_stack_m2C)));
    goto loc_003A168F;
loc_003A1687:
    v_stack_m50 = 0xC0000024ULL;
loc_003A168F:
    goto loc_003A1399;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003A11D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
