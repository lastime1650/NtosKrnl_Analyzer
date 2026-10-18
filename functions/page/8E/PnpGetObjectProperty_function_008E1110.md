# PnpGetObjectProperty

- RVA: `0x008E1110`–`0x008E15E2` (길이 `1,234` bytes)
- VA: `0x00000001408E1110`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00085E08`
- 디코드: `295`개 명령, `1,234/1,234` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **17**; 고유 호출 대상: **12**
- 직접 호출자로 확인된 함수: **10**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x008E1170` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008E1180` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008E123B` → [PiPnpRtlObjectActionCallback](PiPnpRtlObjectActionCallback_function_008E2850.md) (function, `0x008E2850`)
- `0x008E1277` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008E12CB` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008E1356` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x008E13E0` → [_PnpDispatchDevice](_PnpDispatchDevice_function_008E1D60.md) (function, `0x008E1D60`)
- `0x008E13FC` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x008E143F` → [PiPnpRtlObjectActionCallback](PiPnpRtlObjectActionCallback_function_008E2850.md) (function, `0x008E2850`)
- `0x008E1488` → [_PnpDispatchDeviceInterface](_PnpDispatchDeviceInterface_function_008E0DB0.md) (function, `0x008E0DB0`)
- `0x008E14D2` → [PnpGetGenericStoreProperty](PnpGetGenericStoreProperty_function_008EFBA0.md) (function, `0x008EFBA0`)
- `0x008E14F0` → [PnpValidatePropertyData](../8F/PnpValidatePropertyData_function_008F7658.md) (function, `0x008F7658`)
- `0x008E1520` → [DrvDbDispatchDriverPackage](../93/DrvDbDispatchDriverPackage_function_009303A0.md) (function, `0x009303A0`)
- `0x008E1550` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x008E1596` → [PnpOpenObjectRegKey](PnpOpenObjectRegKey_function_008E15E8.md) (function, `0x008E15E8`)
- `0x008E15B7` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x008E15CE` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [IoGetDeviceDirectory](../72/IoGetDeviceDirectory_function_00728370.md) at `0x007284D1`
- [PiPnpRtlGatherInterfaceDeleteInfo](../72/PiPnpRtlGatherInterfaceDeleteInfo_function_0072FD48.md) at `0x0072FEC9`
- [sub_008E314B](Unknown_function_008E314B.md) at `0x008E3228`
- [sub_008E314B](Unknown_function_008E314B.md) at `0x008E3360`
- [IopGetDeviceInterfaces](../8F/IopGetDeviceInterfaces_function_008F0120.md) at `0x008F0353`
- [PiDmObjectProcessPropertyChange](../8F/PiDmObjectProcessPropertyChange_function_008F8A48.md) at `0x008F8CAE`
- [PiDmObjectUpdateCachedObjectProperty](../8F/PiDmObjectUpdateCachedObjectProperty_function_008F9C94.md) at `0x008F9E07`
- [PiUEventCacheObjectProperties](../A2/PiUEventCacheObjectProperties_function_00A2C458.md) at `0x00A2C4F6`
- [PiUEventCacheObjectProperties](../A2/PiUEventCacheObjectProperties_function_00A2C458.md) at `0x00A2C5EE`
- [PnpInitializeInheritedRestrictedSd](../A7/PnpInitializeInheritedRestrictedSd_function_00A7FB28.md) at `0x00A7FB9C`
- [PiDevCfgResolveVariableDeviceProperty](../AA/PiDevCfgResolveVariableDeviceProperty_function_00AA63A0.md) at `0x00AA6525`
- [sub_00B41876](../B4/Unknown_function_00B41876.md) at `0x00B418BC`

### Static image references
- `0x008E1158` → RVA `0x008E2850` (`PiPnpRtlObjectActionCallback`; read)
- `0x008E11A7` → RVA `0x00E66398` (`.data`; read)
- `0x008E13BC` → RVA `0x008E1D60` (`_PnpDispatchDevice`; read)
- `0x008E146C` → RVA `0x008E0DB0` (`_PnpDispatchDeviceInterface`; read)
- `0x008E1508` → RVA `0x009303A0` (`DrvDbDispatchDriverPackage`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **9**
  - `0x008E1170` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008E1180` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008E1277` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008E12CB` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008E1356` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x008E13FC` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x008E1550` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x008E15B7` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x008E15CE` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008E1110  48 8B C4                        mov rax, rsp
008E1113  44 89 48 20                     mov dword ptr [rax + 0x20], r9d
008E1117  4C 89 40 18                     mov qword ptr [rax + 0x18], r8
008E111B  55                              push rbp
008E111C  56                              push rsi
008E111D  57                              push rdi
008E111E  41 54                           push r12
008E1120  41 56                           push r14
008E1122  48 8D 68 A8                     lea rbp, [rax - 0x58]
008E1126  48 81 EC 30 01 00 00            sub rsp, 0x130
008E112D  48 8B BD A0 00 00 00            mov rdi, qword ptr [rbp + 0xa0]
008E1134  45 33 F6                        xor r14d, r14d
008E1137  48 89 58 08                     mov qword ptr [rax + 8], rbx
008E113B  45 8B D1                        mov r10d, r9d
008E113E  4C 89 68 D0                     mov qword ptr [rax - 0x30], r13
008E1142  4D 8B D8                        mov r11, r8
008E1145  44 8B E1                        mov r12d, ecx
008E1148  89 55 68                        mov dword ptr [rbp + 0x68], edx
008E114B  4C 89 37                        mov qword ptr [rdi], r14
008E114E  41 8B F6                        mov esi, r14d
008E1151  4C 89 78 C8                     mov qword ptr [rax - 0x38], r15
008E1155  8B 45 68                        mov eax, dword ptr [rbp + 0x68]
008E1158  48 8D 0D F1 16 00 00            lea rcx, [rip + 0x16f1]
008E115F  3B C6                           cmp eax, esi
008E1161  76 3D                           jbe 0x1408e11a0
008E1163  48 8B 0F                        mov rcx, qword ptr [rdi]
008E1166  8B F0                           mov esi, eax
008E1168  48 85 C9                        test rcx, rcx
008E116B  74 08                           je 0x1408e1175
008E116D  41 8B D4                        mov edx, r12d
008E1170  E8 FB 16 2A 00                  call 0x140b82870
008E1175  48 8B D6                        mov rdx, rsi
008E1178  45 8B C4                        mov r8d, r12d
008E117B  B9 00 01 00 00                  mov ecx, 0x100
008E1180  E8 6B 0F 2A 00                  call 0x140b820f0
008E1185  48 89 07                        mov qword ptr [rdi], rax
008E1188  48 85 C0                        test rax, rax
008E118B  0F 84 47 04 00 00               je 0x1408e15d8
008E1191  44 8B 55 78                     mov r10d, dword ptr [rbp + 0x78]
008E1195  48 8D 0D B4 16 00 00            lea rcx, [rip + 0x16b4]
008E119C  4C 8B 5D 70                     mov r11, qword ptr [rbp + 0x70]
008E11A0  48 8B 85 80 00 00 00            mov rax, qword ptr [rbp + 0x80]
008E11A7  4C 8B 2D EA 51 58 00            mov r13, qword ptr [rip + 0x5851ea]
008E11AE  4C 8B BD 98 00 00 00            mov r15, qword ptr [rbp + 0x98]
008E11B5  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
008E11B9  48 8B 85 88 00 00 00            mov rax, qword ptr [rbp + 0x88]
008E11C0  48 89 45 A8                     mov qword ptr [rbp - 0x58], rax
008E11C4  48 8B 85 90 00 00 00            mov rax, qword ptr [rbp + 0x90]
008E11CB  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
008E11CF  48 8B 07                        mov rax, qword ptr [rdi]
008E11D2  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
008E11D6  48 8D 45 68                     lea rax, [rbp + 0x68]
008E11DA  44 89 75 68                     mov dword ptr [rbp + 0x68], r14d
008E11DE  4C 89 75 90                     mov qword ptr [rbp - 0x70], r14
008E11E2  4C 89 75 98                     mov qword ptr [rbp - 0x68], r14
008E11E6  44 89 75 CC                     mov dword ptr [rbp - 0x34], r14d
008E11EA  44 89 75 DC                     mov dword ptr [rbp - 0x24], r14d
008E11EE  4D 8B B5 E8 01 00 00            mov r14, qword ptr [r13 + 0x1e8]
008E11F5  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
008E11F9  8B 85 B0 00 00 00               mov eax, dword ptr [rbp + 0xb0]
008E11FF  89 45 D8                        mov dword ptr [rbp - 0x28], eax
008E1202  4C 89 7D B8                     mov qword ptr [rbp - 0x48], r15
008E1206  89 75 C8                        mov dword ptr [rbp - 0x38], esi
008E1209  4D 85 F6                        test r14, r14
008E120C  0F 84 D1 00 00 00               je 0x1408e12e3
008E1212  48 8D 45 90                     lea rax, [rbp - 0x70]
008E1216  4C 3B F1                        cmp r14, rcx
008E1219  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008E121E  41 B9 08 00 00 00               mov r9d, 8
008E1224  C7 44 24 20 01 00 00 00         mov dword ptr [rsp + 0x20], 1
008E122C  45 8B C2                        mov r8d, r10d
008E122F  49 8B D3                        mov rdx, r11
008E1232  49 8B CD                        mov rcx, r13
008E1235  0F 85 79 03 00 00               jne 0x1408e15b4
008E123B  E8 10 16 00 00                  call 0x1408e2850
008E1240  3D 02 00 00 C0                  cmp eax, 0xc0000002
008E1245  0F 84 DF 02 00 00               je 0x1408e152a
008E124B  3D 20 01 00 C0                  cmp eax, 0xc0000120
008E1250  0F 85 81 00 00 00               jne 0x1408e12d7
008E1256  8B 5D 90                        mov ebx, dword ptr [rbp - 0x70]
008E1259  81 FB 23 00 00 C0               cmp ebx, 0xc0000023
008E125F  0F 84 CF 02 00 00               je 0x1408e1534
008E1265  85 DB                           test ebx, ebx
008E1267  79 40                           jns 0x1408e12a9
008E1269  45 33 F6                        xor r14d, r14d
008E126C  48 8B 0F                        mov rcx, qword ptr [rdi]
008E126F  48 85 C9                        test rcx, rcx
008E1272  74 0B                           je 0x1408e127f
008E1274  41 8B D4                        mov edx, r12d
008E1277  E8 F4 15 2A 00                  call 0x140b82870
008E127C  4C 89 37                        mov qword ptr [rdi], r14
008E127F  4C 8B BC 24 20 01 00 00         mov r15, qword ptr [rsp + 0x120]
008E1287  8B C3                           mov eax, ebx
008E1289  48 8B 9C 24 60 01 00 00         mov rbx, qword ptr [rsp + 0x160]
008E1291  4C 8B AC 24 28 01 00 00         mov r13, qword ptr [rsp + 0x128]
008E1299  48 81 C4 30 01 00 00            add rsp, 0x130
008E12A0  41 5E                           pop r14
008E12A2  41 5C                           pop r12
008E12A4  5F                              pop rdi
008E12A5  5E                              pop rsi
008E12A6  5D                              pop rbp
008E12A7  C3                              ret
008E12A8  CC                              int3
008E12A9  48 8B 8D A8 00 00 00            mov rcx, qword ptr [rbp + 0xa8]
008E12B0  48 85 C9                        test rcx, rcx
008E12B3  74 05                           je 0x1408e12ba
008E12B5  8B 45 68                        mov eax, dword ptr [rbp + 0x68]
008E12B8  89 01                           mov dword ptr [rcx], eax
008E12BA  83 7D 68 00                     cmp dword ptr [rbp + 0x68], 0
008E12BE  75 BF                           jne 0x1408e127f
008E12C0  48 8B 0F                        mov rcx, qword ptr [rdi]
008E12C3  48 85 C9                        test rcx, rcx
008E12C6  74 B7                           je 0x1408e127f
008E12C8  41 8B D4                        mov edx, r12d
008E12CB  E8 A0 15 2A 00                  call 0x140b82870
008E12D0  33 C0                           xor eax, eax
008E12D2  48 89 07                        mov qword ptr [rdi], rax
008E12D5  EB A8                           jmp 0x1408e127f
008E12D7  85 C0                           test eax, eax
008E12D9  0F 85 83 01 00 00               jne 0x1408e1462
008E12DF  4C 8B 7D B8                     mov r15, qword ptr [rbp - 0x48]
008E12E3  4C 8B 45 B0                     mov r8, qword ptr [rbp - 0x50]
008E12E7  8B 45 D8                        mov eax, dword ptr [rbp - 0x28]
008E12EA  48 8B 55 D0                     mov rdx, qword ptr [rbp - 0x30]
008E12EE  48 8B 5D C0                     mov rbx, qword ptr [rbp - 0x40]
008E12F2  8B 4D C8                        mov ecx, dword ptr [rbp - 0x38]
008E12F5  4C 89 44 24 78                  mov qword ptr [rsp + 0x78], r8
008E12FA  4C 8B 45 A8                     mov r8, qword ptr [rbp - 0x58]
008E12FE  4C 89 45 80                     mov qword ptr [rbp - 0x80], r8
008E1302  4C 8B 45 A0                     mov r8, qword ptr [rbp - 0x60]
008E1306  4C 89 44 24 50                  mov qword ptr [rsp + 0x50], r8
008E130B  45 33 C0                        xor r8d, r8d
008E130E  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
008E1312  0F B7 C0                        movzx eax, ax
008E1315  48 89 54 24 60                  mov qword ptr [rsp + 0x60], rdx
008E131A  89 8D A0 00 00 00               mov dword ptr [rbp + 0xa0], ecx
008E1320  48 89 5C 24 68                  mov qword ptr [rsp + 0x68], rbx
008E1325  4C 89 44 24 70                  mov qword ptr [rsp + 0x70], r8
008E132A  85 C0                           test eax, eax
008E132C  0F 85 30 02 00 00               jne 0x1408e1562
008E1332  48 85 DB                        test rbx, rbx
008E1335  0F 84 C1 01 00 00               je 0x1408e14fc
008E133B  85 C9                           test ecx, ecx
008E133D  49 0F 44 D8                     cmove rbx, r8
008E1341  48 89 5C 24 68                  mov qword ptr [rsp + 0x68], rbx
008E1346  45 89 07                        mov dword ptr [r15], r8d
008E1349  48 8D 4D E0                     lea rcx, [rbp - 0x20]
008E134D  44 89 02                        mov dword ptr [rdx], r8d
008E1350  33 D2                           xor edx, edx
008E1352  44 8D 42 40                     lea r8d, [rdx + 0x40]
008E1356  E8 E5 58 DE FF                  call 0x1406c6c40
008E135B  48 63 55 78                     movsxd rdx, dword ptr [rbp + 0x78]
008E135F  8D 42 FF                        lea eax, [rdx - 1]
008E1362  83 F8 0A                        cmp eax, 0xa
008E1365  0F 87 01 02 00 00               ja 0x1408e156c
008E136B  49 8B 84 D5 28 01 00 00         mov rax, qword ptr [r13 + rdx*8 + 0x128]
008E1373  48 85 C0                        test rax, rax
008E1376  0F 84 45 02 00 00               je 0x1408e15c1
008E137C  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
008E1381  44 8B C2                        mov r8d, edx
008E1384  48 8B 55 70                     mov rdx, qword ptr [rbp + 0x70]
008E1388  41 B9 08 00 00 00               mov r9d, 8
008E138E  48 89 4D E0                     mov qword ptr [rbp - 0x20], rcx
008E1392  48 8B 4D 80                     mov rcx, qword ptr [rbp - 0x80]
008E1396  48 89 4D E8                     mov qword ptr [rbp - 0x18], rcx
008E139A  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
008E139F  48 89 4D F0                     mov qword ptr [rbp - 0x10], rcx
008E13A3  8B 8D A0 00 00 00               mov ecx, dword ptr [rbp + 0xa0]
008E13A9  89 4D 08                        mov dword ptr [rbp + 8], ecx
008E13AC  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
008E13B1  48 89 4D 10                     mov qword ptr [rbp + 0x10], rcx
008E13B5  8B 4C 24 58                     mov ecx, dword ptr [rsp + 0x58]
008E13B9  89 4D 18                        mov dword ptr [rbp + 0x18], ecx
008E13BC  48 8D 0D 9D 09 00 00            lea rcx, [rip + 0x99d]
008E13C3  4C 89 7D F8                     mov qword ptr [rbp - 8], r15
008E13C7  48 89 5D 00                     mov qword ptr [rbp], rbx
008E13CB  48 3B C1                        cmp rax, rcx
008E13CE  0F 85 98 00 00 00               jne 0x1408e146c
008E13D4  48 8D 45 E0                     lea rax, [rbp - 0x20]
008E13D8  49 8B CD                        mov rcx, r13
008E13DB  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008E13E0  E8 7B 09 00 00                  call 0x1408e1d60
008E13E5  8B D8                           mov ebx, eax
008E13E7  3D 16 00 00 C0                  cmp eax, 0xc0000016
008E13EC  0F 84 A0 00 00 00               je 0x1408e1492
008E13F2  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
008E13F7  48 85 C9                        test rcx, rcx
008E13FA  74 05                           je 0x1408e1401
008E13FC  E8 AF BE DC FF                  call 0x1406ad2b0
008E1401  4D 85 F6                        test r14, r14
008E1404  0F 84 4F FE FF FF               je 0x1408e1259
008E140A  44 8B 45 78                     mov r8d, dword ptr [rbp + 0x78]
008E140E  48 8D 05 3B 14 00 00            lea rax, [rip + 0x143b]
008E1415  48 8B 55 70                     mov rdx, qword ptr [rbp + 0x70]
008E1419  4C 3B F0                        cmp r14, rax
008E141C  48 8D 45 90                     lea rax, [rbp - 0x70]
008E1420  89 5D 90                        mov dword ptr [rbp - 0x70], ebx
008E1423  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008E1428  41 B9 08 00 00 00               mov r9d, 8
008E142E  C7 44 24 20 02 00 00 00         mov dword ptr [rsp + 0x20], 2
008E1436  49 8B CD                        mov rcx, r13
008E1439  0F 85 8C 01 00 00               jne 0x1408e15cb
008E143F  E8 0C 14 00 00                  call 0x1408e2850
008E1444  3D 02 00 00 C0                  cmp eax, 0xc0000002
008E1449  0F 84 0A FE FF FF               je 0x1408e1259
008E144F  3D 20 01 00 C0                  cmp eax, 0xc0000120
008E1454  0F 84 00 01 00 00               je 0x1408e155a
008E145A  85 C0                           test eax, eax
008E145C  0F 84 F7 FD FF FF               je 0x1408e1259
008E1462  BB E5 00 00 C0                  mov ebx, 0xc00000e5
008E1467  E9 FD FD FF FF                  jmp 0x1408e1269
008E146C  48 8D 0D 3D F9 FF FF            lea rcx, [rip - 0x6c3]
008E1473  48 3B C1                        cmp rax, rcx
008E1476  0F 85 8C 00 00 00               jne 0x1408e1508
008E147C  48 8D 45 E0                     lea rax, [rbp - 0x20]
008E1480  49 8B CD                        mov rcx, r13
008E1483  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008E1488  E8 23 F9 FF FF                  call 0x1408e0db0
008E148D  E9 53 FF FF FF                  jmp 0x1408e13e5
008E1492  48 83 7C 24 50 00               cmp qword ptr [rsp + 0x50], 0
008E1498  0F 84 D8 00 00 00               je 0x1408e1576
008E149E  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
008E14A3  49 8B CD                        mov rcx, r13
008E14A6  4C 8B 4C 24 78                  mov r9, qword ptr [rsp + 0x78]
008E14AB  4C 8B 45 80                     mov r8, qword ptr [rbp - 0x80]
008E14AF  48 8B 54 24 50                  mov rdx, qword ptr [rsp + 0x50]
008E14B4  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
008E14B9  8B 85 A0 00 00 00               mov eax, dword ptr [rbp + 0xa0]
008E14BF  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
008E14C3  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
008E14C8  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008E14CD  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
008E14D2  E8 C9 E6 00 00                  call 0x1408efba0
008E14D7  8B D8                           mov ebx, eax
008E14D9  85 C0                           test eax, eax
008E14DB  0F 88 11 FF FF FF               js 0x1408e13f2
008E14E1  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
008E14E6  45 8B 07                        mov r8d, dword ptr [r15]
008E14E9  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
008E14EE  8B 10                           mov edx, dword ptr [rax]
008E14F0  E8 63 61 01 00                  call 0x1408f7658
008E14F5  8B D8                           mov ebx, eax
008E14F7  E9 F6 FE FF FF                  jmp 0x1408e13f2
008E14FC  44 89 85 A0 00 00 00            mov dword ptr [rbp + 0xa0], r8d
008E1503  E9 3E FE FF FF                  jmp 0x1408e1346
008E1508  48 8D 0D 91 EE 04 00            lea rcx, [rip + 0x4ee91]
008E150F  48 3B C1                        cmp rax, rcx
008E1512  75 30                           jne 0x1408e1544
008E1514  48 8D 45 E0                     lea rax, [rbp - 0x20]
008E1518  49 8B CD                        mov rcx, r13
008E151B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008E1520  E8 7B EE 04 00                  call 0x1409303a0
008E1525  E9 BB FE FF FF                  jmp 0x1408e13e5
008E152A  33 C0                           xor eax, eax
008E152C  44 8B F0                        mov r14d, eax
008E152F  E9 AB FD FF FF                  jmp 0x1408e12df
008E1534  44 8B 55 78                     mov r10d, dword ptr [rbp + 0x78]
008E1538  45 33 F6                        xor r14d, r14d
008E153B  4C 8B 5D 70                     mov r11, qword ptr [rbp + 0x70]
008E153F  E9 11 FC FF FF                  jmp 0x1408e1155
008E1544  48 8D 4D E0                     lea rcx, [rbp - 0x20]
008E1548  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
008E154D  49 8B CD                        mov rcx, r13
008E1550  E8 7B 95 DD FF                  call 0x1406baad0
008E1555  E9 8B FE FF FF                  jmp 0x1408e13e5
008E155A  8B 5D 90                        mov ebx, dword ptr [rbp - 0x70]
008E155D  E9 F7 FC FF FF                  jmp 0x1408e1259
008E1562  BB 0D 00 00 C0                  mov ebx, 0xc000000d
008E1567  E9 95 FE FF FF                  jmp 0x1408e1401
008E156C  BB 0D 00 00 C0                  mov ebx, 0xc000000d
008E1571  E9 7C FE FF FF                  jmp 0x1408e13f2
008E1576  44 8B 45 78                     mov r8d, dword ptr [rbp + 0x78]
008E157A  48 8D 44 24 70                  lea rax, [rsp + 0x70]
008E157F  48 8B 55 70                     mov rdx, qword ptr [rbp + 0x70]
008E1583  41 B9 01 00 00 02               mov r9d, 0x2000001
008E1589  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008E158E  49 8B CD                        mov rcx, r13
008E1591  C6 44 24 20 00                  mov byte ptr [rsp + 0x20], 0
008E1596  E8 4D 00 00 00                  call 0x1408e15e8
008E159B  8B D8                           mov ebx, eax
008E159D  85 C0                           test eax, eax
008E159F  0F 88 4D FE FF FF               js 0x1408e13f2
008E15A5  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
008E15AA  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
008E15AF  E9 EA FE FF FF                  jmp 0x1408e149e
008E15B4  49 8B C6                        mov rax, r14
008E15B7  E8 14 95 DD FF                  call 0x1406baad0
008E15BC  E9 7F FC FF FF                  jmp 0x1408e1240
008E15C1  BB 02 00 00 C0                  mov ebx, 0xc0000002
008E15C6  E9 27 FE FF FF                  jmp 0x1408e13f2
008E15CB  49 8B C6                        mov rax, r14
008E15CE  E8 FD 94 DD FF                  call 0x1406baad0
008E15D3  E9 6C FE FF FF                  jmp 0x1408e1444
008E15D8  BB 9A 00 00 C0                  mov ebx, 0xc000009a
008E15DD  E9 8A FC FF FF                  jmp 0x1408e126c
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PnpGetObjectProperty(int a1, int a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m130;
    unsigned int v_stack_m138;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned int v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p50;
    unsigned int v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;
    unsigned __int64 v_stack_p8;

    *(unsigned int *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    v_rsp = (v_rsp) - (304);
    v_r14 = 0;
    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp - 48) = v_r13;
    *(unsigned int *)(v_rsp - 88 + 104) = a2;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 88 + 160)) = 0;
    *(unsigned __int64 *)(v_rsp - 56) = v_r15;
loc_008E1155:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 88 + 104)))) <= 0) goto loc_008E11A0;
    result = (unsigned int)(*(unsigned int *)(v_rsp - 88 + 104));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 88 + 160)) != 0) {
        a2 = (unsigned int)((unsigned int)(a1));
        result = ExFreePoolWithTag(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 88 + 160)), a2, a3, a4);
    }
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 88 + 104)))), (unsigned int)((unsigned int)((unsigned int)(a1))), a4);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 88 + 160)) = result;
    if (result == 0) goto loc_008E15D8;
loc_008E11A0:
    *(unsigned __int64 *)(v_rsp - 88 - 96) = *(unsigned __int64 *)(v_rsp - 88 + 128);
    *(unsigned __int64 *)(v_rsp - 88 - 88) = *(unsigned __int64 *)(v_rsp - 88 + 136);
    *(unsigned __int64 *)(v_rsp - 88 - 80) = *(unsigned __int64 *)(v_rsp - 88 + 144);
    *(unsigned __int64 *)(v_rsp - 88 - 64) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 88 + 160));
    *(unsigned int *)(v_rsp - 88 + 104) = 0;
    *(unsigned __int64 *)(v_rsp - 88 - 112) = 0;
    *(unsigned __int64 *)(v_rsp - 88 - 104) = 0;
    *(unsigned int *)(v_rsp - 88 - 52) = 0;
    *(unsigned int *)(v_rsp - 88 - 36) = 0;
    *(unsigned __int64 *)(v_rsp - 88 - 48) = v_rsp - 88 + 104;
    *(unsigned int *)(v_rsp - 88 - 40) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 88 + 176)));
    *(unsigned __int64 *)(v_rsp - 88 - 72) = *(unsigned __int64 *)(v_rsp - 88 + 152);
    *(unsigned int *)(v_rsp - 88 - 56) = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 88 + 104)))));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 5788138) + 488) == 0) goto loc_008E12E3;
    v_stack_m130 = v_rsp - 88 - 112;
    v_stack_m138 = 1;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 5788138) + 488)) != (v_rip + 5812)) goto loc_008E15B4;
    result = PiPnpRtlObjectActionCallback(*(unsigned __int64 *)(v_rip + 5788138), *(unsigned __int64 *)(v_rsp - 88 + 112), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 88 + 120)))), 8);
loc_008E1240:
    if (((unsigned int)(result)) == 0xC0000002ULL) goto loc_008E152A;
    if (((unsigned int)(result)) != 0xC0000120ULL) goto loc_008E12D7;
loc_008E1259:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 88 - 112)))) == 0xC0000023ULL) goto loc_008E1534;
    if (!sign_flag) goto loc_008E12A9;
loc_008E1269:
    v_r14 = 0;
loc_008E126C:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 88 + 160)) != 0) {
        a2 = (unsigned int)((unsigned int)(a1));
        result = ExFreePoolWithTag(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 88 + 160)), a2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 88 + 120)))), 8);
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 88 + 160)) = 0;
    }
    v_rsp = (v_rsp) + (304);
    return (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 88 - 112))));
loc_008E12A9:
    result = (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 88 - 112))));
    if (*(unsigned __int64 *)(v_rsp - 88 + 168) != 0) {
        result = *(unsigned int *)(v_rsp - 88 + 104);
        *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 88 + 168)) = (unsigned int)(result);
    }
    if ((*(unsigned int *)(v_rsp - 88 + 104)) != 0) goto loc_008E127F;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 88 + 160)) == 0) goto loc_008E127F;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 88 + 160)), (unsigned int)((unsigned int)((unsigned int)(a1))), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 88 + 120)))), 8);
    result = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 88 + 160)) = 0;
    goto loc_008E127F;
loc_008E12D7:
    if (0 != 0) goto loc_008E1462;
loc_008E12DF:
loc_008E12E3:
    v_stack_p78 = *(unsigned __int64 *)(v_rsp - 88 - 80);
    *(unsigned __int64 *)(v_rsp - 88 - 128) = *(unsigned __int64 *)(v_rsp - 88 - 88);
    v_stack_p50 = *(unsigned __int64 *)(v_rsp - 88 - 96);
    a3 = 0;
    v_stack_p58 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 88 - 40)));
    v_stack_p60 = *(unsigned __int64 *)(v_rsp - 88 - 48);
    *(unsigned int *)(v_rsp - 88 + 160) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 88 - 56)));
    v_stack_p68 = *(unsigned __int64 *)(v_rsp - 88 - 64);
    v_stack_p70 = 0;
    if ((unsigned int)((unsigned __int16)((unsigned int)(*(unsigned int *)(v_rsp - 88 - 40)))) != 0) goto loc_008E1562;
    if (*(unsigned __int64 *)(v_rsp - 88 - 64) == 0) goto loc_008E14FC;
    v_rbx = *(unsigned __int64 *)(v_rsp - 88 - 64);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 88 - 56))) == 0) { v_rbx = 0; }
    v_stack_p68 = v_rbx;
loc_008E1346:
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 88 - 72)) = 0;
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 88 - 48)) = 0;
    a2 = 0;
    result = memset(v_rsp - 88 - 32, a2, a2 + 64, 8);
    if (((unsigned int)((int)(*(unsigned int *)(v_rsp - 88 + 120)) - 1)) > 10) goto loc_008E156C;
    if (*(unsigned __int64 *)(v_stack_m30 + (int)(*(unsigned int *)(v_rsp - 88 + 120)) * 8 + 296) == 0) goto loc_008E15C1;
    *(unsigned __int64 *)(v_rsp - 88 - 32) = v_stack_p50;
    *(unsigned __int64 *)(v_rsp - 88 - 24) = *(unsigned __int64 *)(v_rsp - 88 - 128);
    *(unsigned __int64 *)(v_rsp - 88 - 16) = v_stack_p78;
    *(unsigned int *)(v_rsp - 88 + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 88 + 160)));
    *(unsigned __int64 *)(v_rsp - 88 + 16) = v_stack_p60;
    *(unsigned int *)(v_rsp - 88 + 24) = (unsigned int)((unsigned int)(v_stack_p58));
    *(unsigned __int64 *)(v_rsp - 88 - 8) = *(unsigned __int64 *)(v_rsp - 88 - 72);
    *(unsigned __int64 *)(v_rsp - 88) = v_rbx;
    if ((*(unsigned __int64 *)(v_stack_m30 + (int)(*(unsigned int *)(v_rsp - 88 + 120)) * 8 + 296)) != (v_rip + 2461)) goto loc_008E146C;
    v_stack_p20 = v_rsp - 88 - 32;
    result = _PnpDispatchDevice(v_stack_m30, *(unsigned __int64 *)(v_rsp - 88 + 112), (unsigned int)((unsigned int)((int)(*(unsigned int *)(v_rsp - 88 + 120)))), 8);
loc_008E13E5:
    if (((unsigned int)(result)) == 0xC0000016ULL) goto loc_008E1492;
loc_008E13F2:
    if (v_stack_p70 != 0) {
        result = ZwClose(v_stack_p70, *(unsigned __int64 *)(v_rsp - 88 + 112), (unsigned int)((unsigned int)((int)(*(unsigned int *)(v_rsp - 88 + 120)))), 8);
    }
    if (0 == 0) goto loc_008E1259;
    *(unsigned int *)(v_rsp - 88 - 112) = (unsigned int)((unsigned int)((unsigned int)(result)));
    v_stack_p28 = v_rsp - 88 - 112;
    v_stack_p20 = 2;
    if (0 != (v_rip + 5179)) goto loc_008E15CB;
    result = PiPnpRtlObjectActionCallback(v_stack_m30, *(unsigned __int64 *)(v_rsp - 88 + 112), (unsigned int)(*(unsigned int *)(v_rsp - 88 + 120)), 8);
loc_008E1444:
    if (((unsigned int)(result)) == 0xC0000002ULL) goto loc_008E1259;
    if (((unsigned int)(result)) == 0xC0000120ULL) goto loc_008E155A;
    if ((unsigned int)(result) == 0) goto loc_008E1259;
loc_008E1462:
    goto loc_008E1269;
loc_008E146C:
    if (result != (v_rip - 1731)) goto loc_008E1508;
    v_stack_p20 = v_rsp - 88 - 32;
    result = _PnpDispatchDeviceInterface(v_stack_m30, *(unsigned __int64 *)(v_rsp - 88 + 112), (unsigned int)(*(unsigned int *)(v_rsp - 88 + 120)), 8);
    goto loc_008E13E5;
loc_008E1492:
    if (v_stack_p50 == 0) goto loc_008E1576;
loc_008E149E:
    v_stack_p38 = v_stack_p60;
    v_stack_p30 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 88 + 160)));
    v_stack_p28 = v_stack_p68;
    v_stack_p20 = *(unsigned __int64 *)(v_rsp - 88 - 72);
    result = PnpGetGenericStoreProperty(v_stack_m30, v_stack_p50, *(unsigned __int64 *)(v_rsp - 88 - 128), v_stack_p78);
    if (sign_flag) goto loc_008E13F2;
    result = PnpValidatePropertyData(v_stack_p68, (unsigned int)(*(unsigned int *)(v_stack_p60)), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 88 - 72))), v_stack_p78);
    goto loc_008E13F2;
loc_008E14FC:
    *(unsigned int *)(v_rsp - 88 + 160) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 88 - 72))));
    goto loc_008E1346;
loc_008E1508:
    if (result != (v_rip + 323217)) goto loc_008E1544;
    v_stack_p20 = v_rsp - 88 - 32;
    result = DrvDbDispatchDriverPackage(v_stack_m30, (unsigned int)(*(unsigned int *)(v_stack_p60)), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 88 - 72))), v_stack_p78);
    goto loc_008E13E5;
loc_008E152A:
    result = 0;
    goto loc_008E12DF;
loc_008E1534:
    v_r14 = 0;
    goto loc_008E1155;
loc_008E1544:
    v_stack_p20 = v_rsp - 88 - 32;
    result = guard_dispatch_icall(v_stack_m30, (unsigned int)(*(unsigned int *)(v_stack_p60)), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 88 - 72))), v_stack_p78);
    goto loc_008E13E5;
loc_008E155A:
    goto loc_008E1259;
loc_008E1562:
    goto loc_008E1401;
loc_008E156C:
    goto loc_008E13F2;
loc_008E1576:
    v_stack_p28 = v_stack_p70;
    v_stack_p20 = 0;
    result = PnpOpenObjectRegKey(v_stack_m30, *(unsigned __int64 *)(v_rsp - 88 + 112), (unsigned int)(*(unsigned int *)(v_rsp - 88 + 120)), (unsigned int)(0x2000001ULL));
    if (sign_flag) goto loc_008E13F2;
    v_stack_p50 = v_stack_p70;
    goto loc_008E149E;
loc_008E15B4:
    result = guard_dispatch_icall(v_stack_m30, *(unsigned __int64 *)(v_rsp - 88 + 112), (unsigned int)(*(unsigned int *)(v_rsp - 88 + 120)), (unsigned int)(0x2000001ULL));
    goto loc_008E1240;
loc_008E15C1:
    goto loc_008E13F2;
loc_008E15CB:
    result = guard_dispatch_icall(v_stack_m30, *(unsigned __int64 *)(v_rsp - 88 + 112), (unsigned int)(*(unsigned int *)(v_rsp - 88 + 120)), (unsigned int)(0x2000001ULL));
    goto loc_008E1444;
loc_008E15D8:
    goto loc_008E126C;
}
```

## 5. (Beta) C Style

```c
int64_t PnpGetObjectProperty(int32_t Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m130;
    uint32_t v_stack_m138;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint32_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p50;
    uint32_t v_stack_p58;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;
    uint64_t v_stack_p8;

    *(uint32_t *)(local_rsp + 0x20) = Arg4;
    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    local_rsp = (local_rsp) - (304);
    local_r14 = 0;
    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp - 0x30) = local_r13;
    *(uint32_t *)(local_rsp - 0x58 + 0x68) = Arg2;
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x58 + 0xA0)) = 0;
    *(uint64_t *)(local_rsp - 0x38) = local_r15;
loc_008E1155:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x58 + 0x68)))) <= 0) goto loc_008E11A0;
    result = (uint32_t)(*(uint32_t *)(local_rsp - 0x58 + 0x68));
    if (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x58 + 0xA0)) != 0) {
        Arg2 = (uint32_t)((uint32_t)(Arg1));
        result = ExFreePoolWithTag(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x58 + 0xA0)), Arg2, Arg3, Arg4);
    }
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x58 + 0x68)))), (uint32_t)((uint32_t)((uint32_t)(Arg1))), Arg4);
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x58 + 0xA0)) = result;
    if (result == 0) goto loc_008E15D8;
loc_008E11A0:
    *(uint64_t *)(local_rsp - 0x58 - 0x60) = *(uint64_t *)(local_rsp - 0x58 + 0x80);
    *(uint64_t *)(local_rsp - 0x58 - 0x58) = *(uint64_t *)(local_rsp - 0x58 + 0x88);
    *(uint64_t *)(local_rsp - 0x58 - 0x50) = *(uint64_t *)(local_rsp - 0x58 + 0x90);
    *(uint64_t *)(local_rsp - 0x58 - 0x40) = *(uint64_t *)(*(uint64_t *)(local_rsp - 0x58 + 0xA0));
    *(uint32_t *)(local_rsp - 0x58 + 0x68) = 0;
    *(uint64_t *)(local_rsp - 0x58 - 0x70) = 0;
    *(uint64_t *)(local_rsp - 0x58 - 0x68) = 0;
    *(uint32_t *)(local_rsp - 0x58 - 0x34) = 0;
    *(uint32_t *)(local_rsp - 0x58 - 0x24) = 0;
    *(uint64_t *)(local_rsp - 0x58 - 0x30) = local_rsp - 88 + 104;
    *(uint32_t *)(local_rsp - 0x58 - 0x28) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x58 + 0xB0)));
    *(uint64_t *)(local_rsp - 0x58 - 0x48) = *(uint64_t *)(local_rsp - 0x58 + 0x98);
    *(uint32_t *)(local_rsp - 0x58 - 0x38) = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x58 + 0x68)))));
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0x5851EA) + 0x1E8) == 0) goto loc_008E12E3;
    v_stack_m130 = local_rsp - 88 - 112;
    v_stack_m138 = 1;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x5851EA) + 0x1E8)) != (v_rip + 5812)) goto loc_008E15B4;
    result = PiPnpRtlObjectActionCallback(*(uint64_t *)(v_rip + 0x5851EA), *(uint64_t *)(local_rsp - 0x58 + 0x70), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x58 + 0x78)))), 8);
loc_008E1240:
    if (((uint32_t)(result)) == 0xC0000002ULL) goto loc_008E152A;
    if (((uint32_t)(result)) != 0xC0000120ULL) goto loc_008E12D7;
loc_008E1259:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x58 - 0x70)))) == 0xC0000023ULL) goto loc_008E1534;
    if (!sign_flag) goto loc_008E12A9;
loc_008E1269:
    local_r14 = 0;
loc_008E126C:
    if (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x58 + 0xA0)) != 0) {
        Arg2 = (uint32_t)((uint32_t)(Arg1));
        result = ExFreePoolWithTag(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x58 + 0xA0)), Arg2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x58 + 0x78)))), 8);
        *(uint64_t *)(*(uint64_t *)(local_rsp - 0x58 + 0xA0)) = 0;
    }
    local_rsp = (local_rsp) + (304);
    return (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x58 - 0x70))));
loc_008E12A9:
    result = (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x58 - 0x70))));
    if (*(uint64_t *)(local_rsp - 0x58 + 0xA8) != 0) {
        result = *(uint32_t *)(local_rsp - 0x58 + 0x68);
        *(uint32_t *)(*(uint64_t *)(local_rsp - 0x58 + 0xA8)) = (uint32_t)(result);
    }
    if ((*(uint32_t *)(local_rsp - 0x58 + 0x68)) != 0) goto loc_008E127F;
    if (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x58 + 0xA0)) == 0) goto loc_008E127F;
    result = ExFreePoolWithTag(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x58 + 0xA0)), (uint32_t)((uint32_t)((uint32_t)(Arg1))), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x58 + 0x78)))), 8);
    result = 0;
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x58 + 0xA0)) = 0;
    goto loc_008E127F;
loc_008E12D7:
    if (0 != 0) goto loc_008E1462;
loc_008E12DF:
loc_008E12E3:
    v_stack_p78 = *(uint64_t *)(local_rsp - 0x58 - 0x50);
    *(uint64_t *)(local_rsp - 0x58 - 0x80) = *(uint64_t *)(local_rsp - 0x58 - 0x58);
    v_stack_p50 = *(uint64_t *)(local_rsp - 0x58 - 0x60);
    Arg3 = 0;
    v_stack_p58 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x58 - 0x28)));
    v_stack_p60 = *(uint64_t *)(local_rsp - 0x58 - 0x30);
    *(uint32_t *)(local_rsp - 0x58 + 0xA0) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x58 - 0x38)));
    v_stack_p68 = *(uint64_t *)(local_rsp - 0x58 - 0x40);
    v_stack_p70 = 0;
    if ((uint32_t)((uint16_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x58 - 0x28)))) != 0) goto loc_008E1562;
    if (*(uint64_t *)(local_rsp - 0x58 - 0x40) == 0) goto loc_008E14FC;
    local_rbx = *(uint64_t *)(local_rsp - 0x58 - 0x40);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x58 - 0x38))) == 0) { local_rbx = 0; }
    v_stack_p68 = local_rbx;
loc_008E1346:
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x58 - 0x48)) = 0;
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x58 - 0x30)) = 0;
    Arg2 = 0;
    result = memset(local_rsp - 88 - 32, Arg2, Arg2 + 64, 8);
    if (((uint32_t)((int32_t)(*(uint32_t *)(local_rsp - 0x58 + 0x78)) - 1)) > 10) goto loc_008E156C;
    if (*(uint64_t *)(v_stack_m30 + (int32_t)(*(uint32_t *)(local_rsp - 0x58 + 0x78)) * 8 + 0x128) == 0) goto loc_008E15C1;
    *(uint64_t *)(local_rsp - 0x58 - 0x20) = v_stack_p50;
    *(uint64_t *)(local_rsp - 0x58 - 0x18) = *(uint64_t *)(local_rsp - 0x58 - 0x80);
    *(uint64_t *)(local_rsp - 0x58 - 0x10) = v_stack_p78;
    *(uint32_t *)(local_rsp - 0x58 + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x58 + 0xA0)));
    *(uint64_t *)(local_rsp - 0x58 + 0x10) = v_stack_p60;
    *(uint32_t *)(local_rsp - 0x58 + 0x18) = (uint32_t)((uint32_t)(v_stack_p58));
    *(uint64_t *)(local_rsp - 0x58 - 0x8) = *(uint64_t *)(local_rsp - 0x58 - 0x48);
    *(uint64_t *)(local_rsp - 0x58) = local_rbx;
    if ((*(uint64_t *)(v_stack_m30 + (int32_t)(*(uint32_t *)(local_rsp - 0x58 + 0x78)) * 8 + 0x128)) != (v_rip + 2461)) goto loc_008E146C;
    v_stack_p20 = local_rsp - 88 - 32;
    result = _PnpDispatchDevice(v_stack_m30, *(uint64_t *)(local_rsp - 0x58 + 0x70), (uint32_t)((uint32_t)((int32_t)(*(uint32_t *)(local_rsp - 0x58 + 0x78)))), 8);
loc_008E13E5:
    if (((uint32_t)(result)) == 0xC0000016ULL) goto loc_008E1492;
loc_008E13F2:
    if (v_stack_p70 != 0) {
        result = ZwClose(v_stack_p70, *(uint64_t *)(local_rsp - 0x58 + 0x70), (uint32_t)((uint32_t)((int32_t)(*(uint32_t *)(local_rsp - 0x58 + 0x78)))), 8);
    }
    if (0 == 0) goto loc_008E1259;
    *(uint32_t *)(local_rsp - 0x58 - 0x70) = (uint32_t)((uint32_t)((uint32_t)(result)));
    v_stack_p28 = local_rsp - 88 - 112;
    v_stack_p20 = 2;
    if (0 != (v_rip + 5179)) goto loc_008E15CB;
    result = PiPnpRtlObjectActionCallback(v_stack_m30, *(uint64_t *)(local_rsp - 0x58 + 0x70), (uint32_t)(*(uint32_t *)(local_rsp - 0x58 + 0x78)), 8);
loc_008E1444:
    if (((uint32_t)(result)) == 0xC0000002ULL) goto loc_008E1259;
    if (((uint32_t)(result)) == 0xC0000120ULL) goto loc_008E155A;
    if ((uint32_t)(result) == 0) goto loc_008E1259;
loc_008E1462:
    goto loc_008E1269;
loc_008E146C:
    if (result != (v_rip - 1731)) goto loc_008E1508;
    v_stack_p20 = local_rsp - 88 - 32;
    result = _PnpDispatchDeviceInterface(v_stack_m30, *(uint64_t *)(local_rsp - 0x58 + 0x70), (uint32_t)(*(uint32_t *)(local_rsp - 0x58 + 0x78)), 8);
    goto loc_008E13E5;
loc_008E1492:
    if (v_stack_p50 == 0) goto loc_008E1576;
loc_008E149E:
    v_stack_p38 = v_stack_p60;
    v_stack_p30 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x58 + 0xA0)));
    v_stack_p28 = v_stack_p68;
    v_stack_p20 = *(uint64_t *)(local_rsp - 0x58 - 0x48);
    result = PnpGetGenericStoreProperty(v_stack_m30, v_stack_p50, *(uint64_t *)(local_rsp - 0x58 - 0x80), v_stack_p78);
    if (sign_flag) goto loc_008E13F2;
    result = PnpValidatePropertyData(v_stack_p68, (uint32_t)(*(uint32_t *)(v_stack_p60)), (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x58 - 0x48))), v_stack_p78);
    goto loc_008E13F2;
loc_008E14FC:
    *(uint32_t *)(local_rsp - 0x58 + 0xA0) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x58 - 0x48))));
    goto loc_008E1346;
loc_008E1508:
    if (result != (v_rip + 323217)) goto loc_008E1544;
    v_stack_p20 = local_rsp - 88 - 32;
    result = DrvDbDispatchDriverPackage(v_stack_m30, (uint32_t)(*(uint32_t *)(v_stack_p60)), (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x58 - 0x48))), v_stack_p78);
    goto loc_008E13E5;
loc_008E152A:
    result = 0;
    goto loc_008E12DF;
loc_008E1534:
    local_r14 = 0;
    goto loc_008E1155;
loc_008E1544:
    v_stack_p20 = local_rsp - 88 - 32;
    result = guard_dispatch_icall(v_stack_m30, (uint32_t)(*(uint32_t *)(v_stack_p60)), (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x58 - 0x48))), v_stack_p78);
    goto loc_008E13E5;
loc_008E155A:
    goto loc_008E1259;
loc_008E1562:
    goto loc_008E1401;
loc_008E156C:
    goto loc_008E13F2;
loc_008E1576:
    v_stack_p28 = v_stack_p70;
    v_stack_p20 = 0;
    result = PnpOpenObjectRegKey(v_stack_m30, *(uint64_t *)(local_rsp - 0x58 + 0x70), (uint32_t)(*(uint32_t *)(local_rsp - 0x58 + 0x78)), (uint32_t)(0x2000001ULL));
    if (sign_flag) goto loc_008E13F2;
    v_stack_p50 = v_stack_p70;
    goto loc_008E149E;
loc_008E15B4:
    result = guard_dispatch_icall(v_stack_m30, *(uint64_t *)(local_rsp - 0x58 + 0x70), (uint32_t)(*(uint32_t *)(local_rsp - 0x58 + 0x78)), (uint32_t)(0x2000001ULL));
    goto loc_008E1240;
loc_008E15C1:
    goto loc_008E13F2;
loc_008E15CB:
    result = guard_dispatch_icall(v_stack_m30, *(uint64_t *)(local_rsp - 0x58 + 0x70), (uint32_t)(*(uint32_t *)(local_rsp - 0x58 + 0x78)), (uint32_t)(0x2000001ULL));
    goto loc_008E1444;
loc_008E15D8:
    goto loc_008E126C;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008E1110&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
