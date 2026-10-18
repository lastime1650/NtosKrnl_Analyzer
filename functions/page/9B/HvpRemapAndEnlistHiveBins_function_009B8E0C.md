# HvpRemapAndEnlistHiveBins

- RVA: `0x009B8E0C`–`0x009B94C0` (길이 `1,716` bytes)
- VA: `0x00000001409B8E0C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0009E9DC`
- 디코드: `432`개 명령, `1,716/1,716` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **33**; 고유 호출 대상: **14**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x009B8E3F` → [HvpGetBinContextInitialize](../../pagecmrc/BC/HvpGetBinContextInitialize_function_00BC98D0.md) (function, `0x00BC98D0`)
- `0x009B8EA3` → [HvpGetCellMap](../../pagecmrc/BC/HvpGetCellMap_function_00BC9710.md) (function, `0x00BC9710`)
- `0x009B8EB2` → [HvpMapEntryGetBinAddress](../../pagecmrc/BC/HvpMapEntryGetBinAddress_function_00BC9770.md) (function, `0x00BC9770`)
- `0x009B8FA9` → [HvpMarkDirty](../85/HvpMarkDirty_function_008593C0.md) (function, `0x008593C0`)
- `0x009B8FC9` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x009B8FFC` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x009B9019` → [HvpGetCellMap](../../pagecmrc/BC/HvpGetCellMap_function_00BC9710.md) (function, `0x00BC9710`)
- `0x009B902E` → [HvpGetCellMap](../../pagecmrc/BC/HvpGetCellMap_function_00BC9710.md) (function, `0x00BC9710`)
- `0x009B907D` → [HvpGetBinContextInitialize](../../pagecmrc/BC/HvpGetBinContextInitialize_function_00BC98D0.md) (function, `0x00BC98D0`)
- `0x009B9088` → [HvpGetCellMap](../../pagecmrc/BC/HvpGetCellMap_function_00BC9710.md) (function, `0x00BC9710`)
- `0x009B909D` → [HvpMapEntryGetBinAddress](../../pagecmrc/BC/HvpMapEntryGetBinAddress_function_00BC9770.md) (function, `0x00BC9770`)
- `0x009B90C4` → [RtlSetBits](../../text/3E/RtlSetBits_function_003E1610.md) (function, `0x003E1610`)
- `0x009B9113` → [HvpMapEntryReleaseBinAddress](../../pagecmrc/BC/HvpMapEntryReleaseBinAddress_function_00BC9790.md) (function, `0x00BC9790`)
- `0x009B911C` → [HvpGetBinContextInitialize](../../pagecmrc/BC/HvpGetBinContextInitialize_function_00BC98D0.md) (function, `0x00BC98D0`)
- `0x009B9162` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x009B91A4` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x009B91E5` → [HvpMapEntryReleaseBinAddress](../../pagecmrc/BC/HvpMapEntryReleaseBinAddress_function_00BC9790.md) (function, `0x00BC9790`)
- `0x009B91EE` → [HvpGetBinContextInitialize](../../pagecmrc/BC/HvpGetBinContextInitialize_function_00BC98D0.md) (function, `0x00BC98D0`)
- `0x009B9211` → [HvpViewMapPromoteRangeToMapping](HvpViewMapPromoteRangeToMapping_function_009B94C8.md) (function, `0x009B94C8`)
- `0x009B9239` → [HvpGetCellMap](../../pagecmrc/BC/HvpGetCellMap_function_00BC9710.md) (function, `0x00BC9710`)
- `0x009B9273` → [HvpMapEntryGetBinAddress](../../pagecmrc/BC/HvpMapEntryGetBinAddress_function_00BC9770.md) (function, `0x00BC9770`)
- `0x009B92B0` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x009B92E6` → [HvpGetCellMap](../../pagecmrc/BC/HvpGetCellMap_function_00BC9710.md) (function, `0x00BC9710`)
- `0x009B9332` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x009B9361` → [HvpGetCellMap](../../pagecmrc/BC/HvpGetCellMap_function_00BC9710.md) (function, `0x00BC9710`)
- `0x009B9370` → [HvpMapEntryGetBinAddress](../../pagecmrc/BC/HvpMapEntryGetBinAddress_function_00BC9770.md) (function, `0x00BC9770`)
- `0x009B9381` → [HvpValidateLoadedBin](HvpValidateLoadedBin_function_009BA590.md) (function, `0x009BA590`)
- `0x009B93A9` → [HvpEnlistFreeCells](../85/HvpEnlistFreeCells_function_0085AC00.md) (function, `0x0085AC00`)
- `0x009B93CB` → [HvpMapEntryReleaseBinAddress](../../pagecmrc/BC/HvpMapEntryReleaseBinAddress_function_00BC9790.md) (function, `0x00BC9790`)
- `0x009B93D4` → [HvpGetBinContextInitialize](../../pagecmrc/BC/HvpGetBinContextInitialize_function_00BC98D0.md) (function, `0x00BC98D0`)
- `0x009B9462` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x009B947F` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x009B94B6` → [HvpFreeBin](../A8/HvpFreeBin_function_00A8158C.md) (function, `0x00A8158C`)

### Direct callers
- [HvLoadHive](HvLoadHive_function_009B8138.md) at `0x009B837C`

### Static image references
- `0x009B91B5` → RVA `0x00FD8002` (`PAGEDATA`; read)
- `0x009B91C2` → RVA `0x00EF7C60` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **28**
  - `0x009B8E3F` → [HvpGetBinContextInitialize](../../pagecmrc/BC/HvpGetBinContextInitialize_function_00BC98D0.md) (`PAGE` → `PAGECMRC`)
  - `0x009B8EA3` → [HvpGetCellMap](../../pagecmrc/BC/HvpGetCellMap_function_00BC9710.md) (`PAGE` → `PAGECMRC`)
  - `0x009B8EB2` → [HvpMapEntryGetBinAddress](../../pagecmrc/BC/HvpMapEntryGetBinAddress_function_00BC9770.md) (`PAGE` → `PAGECMRC`)
  - `0x009B8FC9` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x009B8FFC` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x009B9019` → [HvpGetCellMap](../../pagecmrc/BC/HvpGetCellMap_function_00BC9710.md) (`PAGE` → `PAGECMRC`)
  - `0x009B902E` → [HvpGetCellMap](../../pagecmrc/BC/HvpGetCellMap_function_00BC9710.md) (`PAGE` → `PAGECMRC`)
  - `0x009B907D` → [HvpGetBinContextInitialize](../../pagecmrc/BC/HvpGetBinContextInitialize_function_00BC98D0.md) (`PAGE` → `PAGECMRC`)
  - `0x009B9088` → [HvpGetCellMap](../../pagecmrc/BC/HvpGetCellMap_function_00BC9710.md) (`PAGE` → `PAGECMRC`)
  - `0x009B909D` → [HvpMapEntryGetBinAddress](../../pagecmrc/BC/HvpMapEntryGetBinAddress_function_00BC9770.md) (`PAGE` → `PAGECMRC`)
  - `0x009B90C4` → [RtlSetBits](../../text/3E/RtlSetBits_function_003E1610.md) (`PAGE` → `.text`)
  - `0x009B9113` → [HvpMapEntryReleaseBinAddress](../../pagecmrc/BC/HvpMapEntryReleaseBinAddress_function_00BC9790.md) (`PAGE` → `PAGECMRC`)
  - `0x009B911C` → [HvpGetBinContextInitialize](../../pagecmrc/BC/HvpGetBinContextInitialize_function_00BC98D0.md) (`PAGE` → `PAGECMRC`)
  - `0x009B9162` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x009B91A4` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x009B91E5` → [HvpMapEntryReleaseBinAddress](../../pagecmrc/BC/HvpMapEntryReleaseBinAddress_function_00BC9790.md) (`PAGE` → `PAGECMRC`)
  - `0x009B91EE` → [HvpGetBinContextInitialize](../../pagecmrc/BC/HvpGetBinContextInitialize_function_00BC98D0.md) (`PAGE` → `PAGECMRC`)
  - `0x009B9239` → [HvpGetCellMap](../../pagecmrc/BC/HvpGetCellMap_function_00BC9710.md) (`PAGE` → `PAGECMRC`)
  - `0x009B9273` → [HvpMapEntryGetBinAddress](../../pagecmrc/BC/HvpMapEntryGetBinAddress_function_00BC9770.md) (`PAGE` → `PAGECMRC`)
  - `0x009B92B0` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x009B92E6` → [HvpGetCellMap](../../pagecmrc/BC/HvpGetCellMap_function_00BC9710.md) (`PAGE` → `PAGECMRC`)
  - `0x009B9332` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x009B9361` → [HvpGetCellMap](../../pagecmrc/BC/HvpGetCellMap_function_00BC9710.md) (`PAGE` → `PAGECMRC`)
  - `0x009B9370` → [HvpMapEntryGetBinAddress](../../pagecmrc/BC/HvpMapEntryGetBinAddress_function_00BC9770.md) (`PAGE` → `PAGECMRC`)
  - `0x009B93CB` → [HvpMapEntryReleaseBinAddress](../../pagecmrc/BC/HvpMapEntryReleaseBinAddress_function_00BC9790.md) (`PAGE` → `PAGECMRC`)
  - `0x009B93D4` → [HvpGetBinContextInitialize](../../pagecmrc/BC/HvpGetBinContextInitialize_function_00BC98D0.md) (`PAGE` → `PAGECMRC`)
  - `0x009B9462` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x009B947F` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **6**
  - `0x009B91D6` → [sub_00B2E0F0 + 0x64](../B2/Unknown_function_00B2E0F0.md) (`tail-transfer`)
  - `0x009B9388` → [sub_00B2E0F0 + 0xA7](../B2/Unknown_function_00B2E0F0.md) (`tail-transfer`)
  - `0x009B9396` → [sub_00B2E0F0 + 0x14B](../B2/Unknown_function_00B2E0F0.md) (`tail-transfer`)
  - `0x009B9432` → [sub_00B2E0F0](../B2/Unknown_function_00B2E0F0.md) (`tail-transfer`)
  - `0x009B9446` → [sub_00B2E0F0](../B2/Unknown_function_00B2E0F0.md) (`tail-transfer`)
  - `0x009B9490` → [sub_00B2E0F0 + 0x64](../B2/Unknown_function_00B2E0F0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
009B8E0C  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
009B8E11  89 54 24 10                     mov dword ptr [rsp + 0x10], edx
009B8E15  55                              push rbp
009B8E16  53                              push rbx
009B8E17  56                              push rsi
009B8E18  57                              push rdi
009B8E19  41 54                           push r12
009B8E1B  41 55                           push r13
009B8E1D  41 56                           push r14
009B8E1F  41 57                           push r15
009B8E21  48 8D 6C 24 E1                  lea rbp, [rsp - 0x1f]
009B8E26  48 81 EC 88 00 00 00            sub rsp, 0x88
009B8E2D  48 8B F1                        mov rsi, rcx
009B8E30  45 33 C9                        xor r9d, r9d
009B8E33  48 8D 4D 7F                     lea rcx, [rbp + 0x7f]
009B8E37  66 44 89 4D 7F                  mov word ptr [rbp + 0x7f], r9w
009B8E3C  4D 8B E8                        mov r13, r8
009B8E3F  E8 8C 0A 21 00                  call 0x140bc98d0
009B8E44  F7 86 A0 00 00 00 00 00 02 00   test dword ptr [rsi + 0xa0], 0x20000
009B8E4E  41 8B C1                        mov eax, r9d
009B8E51  8B 9E 18 01 00 00               mov ebx, dword ptr [rsi + 0x118]
009B8E57  48 89 45 CF                     mov qword ptr [rbp - 0x31], rax
009B8E5B  48 89 45 FF                     mov qword ptr [rbp - 1], rax
009B8E5F  89 45 C7                        mov dword ptr [rbp - 0x39], eax
009B8E62  4C 89 4D 07                     mov qword ptr [rbp + 7], r9
009B8E66  44 89 4D E7                     mov dword ptr [rbp - 0x19], r9d
009B8E6A  89 5D E3                        mov dword ptr [rbp - 0x1d], ebx
009B8E6D  0F 84 91 05 00 00               je 0x1409b9404
009B8E73  44 8B 96 E8 00 00 00            mov r10d, dword ptr [rsi + 0xe8]
009B8E7A  41 81 EA 00 10 00 00            sub r10d, 0x1000
009B8E81  44 89 55 DF                     mov dword ptr [rbp - 0x21], r10d
009B8E85  45 8B F1                        mov r14d, r9d
009B8E88  41 BB 10 00 00 00               mov r11d, 0x10
009B8E8E  41 BC 4C 01 00 C0               mov r12d, 0xc000014c
009B8E94  45 3B F2                        cmp r14d, r10d
009B8E97  0F 83 45 05 00 00               jae 0x1409b93e2
009B8E9D  41 8B D6                        mov edx, r14d
009B8EA0  48 8B CE                        mov rcx, rsi
009B8EA3  E8 68 08 21 00                  call 0x140bc9710
009B8EA8  48 8B D0                        mov rdx, rax
009B8EAB  4C 8D 45 7F                     lea r8, [rbp + 0x7f]
009B8EAF  4C 8B F8                        mov r15, rax
009B8EB2  E8 B9 08 21 00                  call 0x140bc9770
009B8EB7  48 8B F8                        mov rdi, rax
009B8EBA  48 89 45 0F                     mov qword ptr [rbp + 0xf], rax
009B8EBE  8B 48 08                        mov ecx, dword ptr [rax + 8]
009B8EC1  44 8B 40 04                     mov r8d, dword ptr [rax + 4]
009B8EC5  41 8D 14 08                     lea edx, [r8 + rcx]
009B8EC9  3B D3                           cmp edx, ebx
009B8ECB  0F 87 7A 02 00 00               ja 0x1409b914b
009B8ED1  81 F9 00 10 00 00               cmp ecx, 0x1000
009B8ED7  0F 82 6E 02 00 00               jb 0x1409b914b
009B8EDD  3B D1                           cmp edx, ecx
009B8EDF  0F 82 66 02 00 00               jb 0x1409b914b
009B8EE5  F7 C1 FF 0F 00 00               test ecx, 0xfff
009B8EEB  0F 85 5A 02 00 00               jne 0x1409b914b
009B8EF1  45 3B C6                        cmp r8d, r14d
009B8EF4  0F 85 51 02 00 00               jne 0x1409b914b
009B8EFA  81 38 68 62 69 6E               cmp dword ptr [rax], 0x6e696268
009B8F00  0F 85 45 02 00 00               jne 0x1409b914b
009B8F06  8B 47 08                        mov eax, dword ptr [rdi + 8]
009B8F09  3D 00 10 00 00                  cmp eax, 0x1000
009B8F0E  0F 85 C7 02 00 00               jne 0x1409b91db
009B8F14  45 33 C9                        xor r9d, r9d
009B8F17  4C 8B 56 38                     mov r10, qword ptr [rsi + 0x38]
009B8F1B  BB 20 00 00 00                  mov ebx, 0x20
009B8F20  83 86 90 00 00 00 20            add dword ptr [rsi + 0x90], 0x20
009B8F27  4C 89 55 EF                     mov qword ptr [rbp - 0x11], r10
009B8F2B  44 88 4D 67                     mov byte ptr [rbp + 0x67], r9b
009B8F2F  8B 57 08                        mov edx, dword ptr [rdi + 8]
009B8F32  89 5D DB                        mov dword ptr [rbp - 0x25], ebx
009B8F35  3B DA                           cmp ebx, edx
009B8F37  0F 83 B6 01 00 00               jae 0x1409b90f3
009B8F3D  8B C3                           mov eax, ebx
009B8F3F  48 03 C7                        add rax, rdi
009B8F42  48 89 45 F7                     mov qword ptr [rbp - 9], rax
009B8F46  8B 00                           mov eax, dword ptr [rax]
009B8F48  44 8B E0                        mov r12d, eax
009B8F4B  85 C0                           test eax, eax
009B8F4D  79 03                           jns 0x1409b8f52
009B8F4F  41 F7 DC                        neg r12d
009B8F52  C1 E8 1F                        shr eax, 0x1f
009B8F55  41 8D 0C 1C                     lea ecx, [r12 + rbx]
009B8F59  41 BB 01 00 00 00               mov r11d, 1
009B8F5F  41 32 C3                        xor al, r11b
009B8F62  3B CB                           cmp ecx, ebx
009B8F64  0F 82 1A 02 00 00               jb 0x1409b9184
009B8F6A  3B CA                           cmp ecx, edx
009B8F6C  0F 87 12 02 00 00               ja 0x1409b9184
009B8F72  41 F6 C4 07                     test r12b, 7
009B8F76  0F 85 08 02 00 00               jne 0x1409b9184
009B8F7C  45 85 E4                        test r12d, r12d
009B8F7F  0F 84 FF 01 00 00               je 0x1409b9184
009B8F85  84 C0                           test al, al
009B8F87  75 7B                           jne 0x1409b9004
009B8F89  44 01 A6 98 00 00 00            add dword ptr [rsi + 0x98], r12d
009B8F90  41 03 DC                        add ebx, r12d
009B8F93  EB 9A                           jmp 0x1409b8f2f
009B8F95  44 8B 67 08                     mov r12d, dword ptr [rdi + 8]
009B8F99  42 8D 14 33                     lea edx, [rbx + r14]
009B8F9D  44 2B E3                        sub r12d, ebx
009B8FA0  45 33 C9                        xor r9d, r9d
009B8FA3  45 8B C4                        mov r8d, r12d
009B8FA6  48 8B CE                        mov rcx, rsi
009B8FA9  E8 12 04 EA FF                  call 0x1408593c0
009B8FAE  8B D8                           mov ebx, eax
009B8FB0  44 8B F8                        mov r15d, eax
009B8FB3  33 C0                           xor eax, eax
009B8FB5  85 DB                           test ebx, ebx
009B8FB7  0F 88 C8 04 00 00               js 0x1409b9485
009B8FBD  48 8B 5D F7                     mov rbx, qword ptr [rbp - 9]
009B8FC1  33 D2                           xor edx, edx
009B8FC3  48 8B CB                        mov rcx, rbx
009B8FC6  45 8B C4                        mov r8d, r12d
009B8FC9  E8 72 DC D0 FF                  call 0x1406c6c40
009B8FCE  B9 01 00 00 00                  mov ecx, 1
009B8FD3  44 89 23                        mov dword ptr [rbx], r12d
009B8FD6  48 8B 46 40                     mov rax, qword ptr [rsi + 0x40]
009B8FDA  8B D1                           mov edx, ecx
009B8FDC  88 4D 67                        mov byte ptr [rbp + 0x67], cl
009B8FDF  41 B9 09 00 00 40               mov r9d, 0x40000009
009B8FE5  C7 44 24 20 20 00 00 00         mov dword ptr [rsp + 0x20], 0x20
009B8FED  44 8D 41 19                     lea r8d, [rcx + 0x19]
009B8FF1  48 8B 4D EF                     mov rcx, qword ptr [rbp - 0x11]
009B8FF5  83 88 F8 0F 00 00 04            or dword ptr [rax + 0xff8], 4
009B8FFC  E8 53 5F AB FF                  call 0x14046ef54
009B9001  8B 5D DB                        mov ebx, dword ptr [rbp - 0x25]
009B9004  44 01 A6 94 00 00 00            add dword ptr [rsi + 0x94], r12d
009B900B  46 8D 04 33                     lea r8d, [rbx + r14]
009B900F  41 8B D0                        mov edx, r8d
009B9012  44 89 45 F7                     mov dword ptr [rbp - 9], r8d
009B9016  48 8B CE                        mov rcx, rsi
009B9019  E8 F2 06 21 00                  call 0x140bc9710
009B901E  41 8B D8                        mov ebx, r8d
009B9021  48 8B CE                        mov rcx, rsi
009B9024  81 E3 00 F0 FF FF               and ebx, 0xfffff000
009B902A  2B 18                           sub ebx, dword ptr [rax]
009B902C  8B D3                           mov edx, ebx
009B902E  E8 DD 06 21 00                  call 0x140bc9710
009B9033  45 33 C9                        xor r9d, r9d
009B9036  8B 40 10                        mov eax, dword ptr [rax + 0x10]
009B9039  89 45 D7                        mov dword ptr [rbp - 0x29], eax
009B903C  44 8D 3C 18                     lea r15d, [rax + rbx]
009B9040  85 DB                           test ebx, ebx
009B9042  74 12                           je 0x1409b9056
009B9044  8B CB                           mov ecx, ebx
009B9046  48 83 C1 20                     add rcx, 0x20
009B904A  41 8B C0                        mov eax, r8d
009B904D  48 3B C1                        cmp rax, rcx
009B9050  0F 84 3E 02 00 00               je 0x1409b9294
009B9056  45 8B FC                        mov r15d, r12d
009B9059  44 89 4D F7                     mov dword ptr [rbp - 9], r9d
009B905D  41 C1 EF 03                     shr r15d, 3
009B9061  41 BA 01 00 00 00               mov r10d, 1
009B9067  45 2B FA                        sub r15d, r10d
009B906A  41 83 FF 10                     cmp r15d, 0x10
009B906E  0F 83 B9 00 00 00               jae 0x1409b912d
009B9074  48 8D 4D D7                     lea rcx, [rbp - 0x29]
009B9078  66 44 89 4D D7                  mov word ptr [rbp - 0x29], r9w
009B907D  E8 4E 08 21 00                  call 0x140bc98d0
009B9082  41 8B D0                        mov edx, r8d
009B9085  48 8B CE                        mov rcx, rsi
009B9088  E8 83 06 21 00                  call 0x140bc9710
009B908D  48 85 C0                        test rax, rax
009B9090  0F 84 D2 03 00 00               je 0x1409b9468
009B9096  4C 8D 45 D7                     lea r8, [rbp - 0x29]
009B909A  48 8B D0                        mov rdx, rax
009B909D  E8 CE 06 21 00                  call 0x140bc9770
009B90A2  41 8B D7                        mov edx, r15d
009B90A5  48 8D 8E 40 01 00 00            lea rcx, [rsi + 0x140]
009B90AC  8B 78 04                        mov edi, dword ptr [rax + 4]
009B90AF  44 8B 40 08                     mov r8d, dword ptr [rax + 8]
009B90B3  48 8D 1C 52                     lea rbx, [rdx + rdx*2]
009B90B7  C1 EF 0C                        shr edi, 0xc
009B90BA  48 8D 0C D9                     lea rcx, [rcx + rbx*8]
009B90BE  8B D7                           mov edx, edi
009B90C0  41 C1 E8 0C                     shr r8d, 0xc
009B90C4  E8 47 85 A2 FF                  call 0x1403e1610
009B90C9  89 BC DE 3C 01 00 00            mov dword ptr [rsi + rbx*8 + 0x13c], edi
009B90D0  41 8B CF                        mov ecx, r15d
009B90D3  48 8B 7D 0F                     mov rdi, qword ptr [rbp + 0xf]
009B90D7  B8 01 00 00 00                  mov eax, 1
009B90DC  D3 E0                           shl eax, cl
009B90DE  09 86 88 03 00 00               or dword ptr [rsi + 0x388], eax
009B90E4  45 33 C9                        xor r9d, r9d
009B90E7  4C 8B 55 EF                     mov r10, qword ptr [rbp - 0x11]
009B90EB  8B 5D DB                        mov ebx, dword ptr [rbp - 0x25]
009B90EE  E9 9D FE FF FF                  jmp 0x1409b8f90
009B90F3  44 8B 5D C7                     mov r11d, dword ptr [rbp - 0x39]
009B90F7  4C 8D 45 7F                     lea r8, [rbp + 0x7f]
009B90FB  44 38 4D 67                     cmp byte ptr [rbp + 0x67], r9b
009B90FF  B8 01 00 00 00                  mov eax, 1
009B9104  45 0F B6 DB                     movzx r11d, r11b
009B9108  44 0F 45 D8                     cmovne r11d, eax
009B910C  44 03 F2                        add r14d, edx
009B910F  44 89 5D C7                     mov dword ptr [rbp - 0x39], r11d
009B9113  E8 78 06 21 00                  call 0x140bc9790
009B9118  48 8D 4D 7F                     lea rcx, [rbp + 0x7f]
009B911C  E8 AF 07 21 00                  call 0x140bc98d0
009B9121  44 8B 55 DF                     mov r10d, dword ptr [rbp - 0x21]
009B9125  8B 5D E3                        mov ebx, dword ptr [rbp - 0x1d]
009B9128  E9 5B FD FF FF                  jmp 0x1409b8e88
009B912D  41 C1 EF 04                     shr r15d, 4
009B9131  41 81 FF FF 00 00 00            cmp r15d, 0xff
009B9138  0F 87 CE 02 00 00               ja 0x1409b940c
009B913E  45 0F BD FF                     bsr r15d, r15d
009B9142  41 83 C7 10                     add r15d, 0x10
009B9146  E9 29 FF FF FF                  jmp 0x1409b9074
009B914B  BA 01 00 00 00                  mov edx, 1
009B9150  44 89 5C 24 20                  mov dword ptr [rsp + 0x20], r11d
009B9155  45 8B CC                        mov r9d, r12d
009B9158  49 8B CD                        mov rcx, r13
009B915B  41 8B DC                        mov ebx, r12d
009B915E  44 8D 42 21                     lea r8d, [rdx + 0x21]
009B9162  E8 ED 5D AB FF                  call 0x14046ef54
009B9167  F7 45 6F 00 00 02 00            test dword ptr [rbp + 0x6f], 0x20000
009B916E  0F 84 B6 02 00 00               je 0x1409b942a
009B9174  C7 44 24 20 20 00 00 00         mov dword ptr [rsp + 0x20], 0x20
009B917C  45 8B CC                        mov r9d, r12d
009B917F  E9 A3 01 00 00                  jmp 0x1409b9327
009B9184  41 BC 4C 01 00 C0               mov r12d, 0xc000014c
009B918A  C7 44 24 20 08 00 00 00         mov dword ptr [rsp + 0x20], 8
009B9192  45 8B CC                        mov r9d, r12d
009B9195  41 B8 1A 00 00 00               mov r8d, 0x1a
009B919B  41 8B D3                        mov edx, r11d
009B919E  49 8B CA                        mov rcx, r10
009B91A1  45 8B FC                        mov r15d, r12d
009B91A4  E8 AB 5D AB FF                  call 0x14046ef54
009B91A9  45 33 C0                        xor r8d, r8d
009B91AC  F7 45 6F 00 00 02 00            test dword ptr [rbp + 0x6f], 0x20000
009B91B3  75 1B                           jne 0x1409b91d0
009B91B5  44 38 05 46 EE 61 00            cmp byte ptr [rip + 0x61ee46], r8b
009B91BC  0F 85 D3 FD FF FF               jne 0x1409b8f95
009B91C2  8B 05 98 EA 53 00               mov eax, dword ptr [rip + 0x53ea98]
009B91C8  A8 06                           test al, 6
009B91CA  0F 85 C5 FD FF FF               jne 0x1409b8f95
009B91D0  41 8B DC                        mov ebx, r12d
009B91D3  41 8B D0                        mov edx, r8d
009B91D6  E9 79 4F 17 00                  jmp 0x140b2e154
009B91DB  4C 8D 45 7F                     lea r8, [rbp + 0x7f]
009B91DF  89 45 E7                        mov dword ptr [rbp - 0x19], eax
009B91E2  44 8B E0                        mov r12d, eax
009B91E5  E8 A6 05 21 00                  call 0x140bc9790
009B91EA  48 8D 4D 7F                     lea rcx, [rbp + 0x7f]
009B91EE  E8 DD 06 21 00                  call 0x140bc98d0
009B91F3  43 8D 0C 34                     lea ecx, [r12 + r14]
009B91F7  41 3B CA                        cmp ecx, r10d
009B91FA  0F 87 DC 01 00 00               ja 0x1409b93dc
009B9200  48 8D 8E E0 00 00 00            lea rcx, [rsi + 0xe0]
009B9207  45 8B C4                        mov r8d, r12d
009B920A  4C 8D 4D 07                     lea r9, [rbp + 7]
009B920E  41 8B D6                        mov edx, r14d
009B9211  E8 B2 02 00 00                  call 0x1409b94c8
009B9216  45 33 C9                        xor r9d, r9d
009B9219  8B D8                           mov ebx, eax
009B921B  85 C0                           test eax, eax
009B921D  0F 88 F9 00 00 00               js 0x1409b931c
009B9223  48 8B 5D 07                     mov rbx, qword ptr [rbp + 7]
009B9227  45 8B C1                        mov r8d, r9d
009B922A  45 3B C4                        cmp r8d, r12d
009B922D  73 3D                           jae 0x1409b926c
009B922F  47 8D 1C 30                     lea r11d, [r8 + r14]
009B9233  48 8B CE                        mov rcx, rsi
009B9236  41 8B D3                        mov edx, r11d
009B9239  E8 D2 04 21 00                  call 0x140bc9710
009B923E  45 33 C9                        xor r9d, r9d
009B9241  4C 8B D0                        mov r10, rax
009B9244  48 85 C0                        test rax, rax
009B9247  0F 84 FE 01 00 00               je 0x1409b944b
009B924D  48 89 58 08                     mov qword ptr [rax + 8], rbx
009B9251  45 85 C0                        test r8d, r8d
009B9254  74 2E                           je 0x1409b9284
009B9256  41 8B C1                        mov eax, r9d
009B9259  41 89 42 10                     mov dword ptr [r10 + 0x10], eax
009B925D  41 8B C0                        mov eax, r8d
009B9260  41 81 C0 00 10 00 00            add r8d, 0x1000
009B9267  49 89 02                        mov qword ptr [r10], rax
009B926A  EB BE                           jmp 0x1409b922a
009B926C  4C 8D 45 7F                     lea r8, [rbp + 0x7f]
009B9270  49 8B D7                        mov rdx, r15
009B9273  E8 F8 04 21 00                  call 0x140bc9770
009B9278  48 8B F8                        mov rdi, rax
009B927B  48 89 45 0F                     mov qword ptr [rbp + 0xf], rax
009B927F  E9 93 FC FF FF                  jmp 0x1409b8f17
009B9284  48 8B CB                        mov rcx, rbx
009B9287  48 83 C9 01                     or rcx, 1
009B928B  48 89 48 08                     mov qword ptr [rax + 8], rcx
009B928F  41 8B C4                        mov eax, r12d
009B9292  EB C5                           jmp 0x1409b9259
009B9294  43 8D 04 20                     lea eax, [r8 + r12]
009B9298  41 3B C7                        cmp eax, r15d
009B929B  0F 85 B5 FD FF FF               jne 0x1409b9056
009B92A1  48 8B 46 18                     mov rax, qword ptr [rsi + 0x18]
009B92A5  33 D2                           xor edx, edx
009B92A7  41 B8 43 4D 37 20               mov r8d, 0x20374d43
009B92AD  8D 4A 18                        lea ecx, [rdx + 0x18]
009B92B0  E8 1B 18 D0 FF                  call 0x1406baad0
009B92B5  45 33 C9                        xor r9d, r9d
009B92B8  4C 8B C0                        mov r8, rax
009B92BB  48 85 C0                        test rax, rax
009B92BE  0F 84 37 01 00 00               je 0x1409b93fb
009B92C4  4C 89 08                        mov qword ptr [rax], r9
009B92C7  8B CB                           mov ecx, ebx
009B92C9  4C 89 48 08                     mov qword ptr [rax + 8], r9
009B92CD  0F BA F1 1F                     btr ecx, 0x1f
009B92D1  8B 45 D7                        mov eax, dword ptr [rbp - 0x29]
009B92D4  41 89 40 10                     mov dword ptr [r8 + 0x10], eax
009B92D8  41 89 48 14                     mov dword ptr [r8 + 0x14], ecx
009B92DC  41 3B DF                        cmp ebx, r15d
009B92DF  73 20                           jae 0x1409b9301
009B92E1  8B D3                           mov edx, ebx
009B92E3  48 8B CE                        mov rcx, rsi
009B92E6  E8 25 04 21 00                  call 0x140bc9710
009B92EB  81 C3 00 10 00 00               add ebx, 0x1000
009B92F1  48 83 48 08 02                  or qword ptr [rax + 8], 2
009B92F6  4C 89 00                        mov qword ptr [rax], r8
009B92F9  41 3B DF                        cmp ebx, r15d
009B92FC  72 E3                           jb 0x1409b92e1
009B92FE  45 33 C9                        xor r9d, r9d
009B9301  48 8D 86 78 03 00 00            lea rax, [rsi + 0x378]
009B9308  48 8B 08                        mov rcx, qword ptr [rax]
009B930B  48 39 41 08                     cmp qword ptr [rcx + 8], rax
009B930F  0F 84 02 01 00 00               je 0x1409b9417
009B9315  B9 03 00 00 00                  mov ecx, 3
009B931A  CD 29                           int 0x29
009B931C  C7 44 24 20 40 00 00 00         mov dword ptr [rsp + 0x20], 0x40
009B9324  44 8B C8                        mov r9d, eax
009B9327  33 D2                           xor edx, edx
009B9329  41 B8 22 00 00 00               mov r8d, 0x22
009B932F  49 8B CD                        mov rcx, r13
009B9332  E8 1D 5C AB FF                  call 0x14046ef54
009B9337  48 8B 7D CF                     mov rdi, qword ptr [rbp - 0x31]
009B933B  48 85 FF                        test rdi, rdi
009B933E  0F 85 69 01 00 00               jne 0x1409b94ad
009B9344  8B C3                           mov eax, ebx
009B9346  48 81 C4 88 00 00 00            add rsp, 0x88
009B934D  41 5F                           pop r15
009B934F  41 5E                           pop r14
009B9351  41 5D                           pop r13
009B9353  41 5C                           pop r12
009B9355  5F                              pop rdi
009B9356  5E                              pop rsi
009B9357  5B                              pop rbx
009B9358  5D                              pop rbp
009B9359  C3                              ret
009B935A  CC                              int3
009B935B  41 8B D6                        mov edx, r14d
009B935E  48 8B CE                        mov rcx, rsi
009B9361  E8 AA 03 21 00                  call 0x140bc9710
009B9366  48 8B D0                        mov rdx, rax
009B9369  4C 8D 45 7F                     lea r8, [rbp + 0x7f]
009B936D  4C 8B F8                        mov r15, rax
009B9370  E8 FB 03 21 00                  call 0x140bc9770
009B9375  48 8B C8                        mov rcx, rax
009B9378  44 8B C3                        mov r8d, ebx
009B937B  41 8B D6                        mov edx, r14d
009B937E  48 8B F8                        mov rdi, rax
009B9381  E8 0A 12 00 00                  call 0x1409ba590
009B9386  84 C0                           test al, al
009B9388  0F 84 09 4E 17 00               je 0x140b2e197
009B938E  8B 47 08                        mov eax, dword ptr [rdi + 8]
009B9391  3D 00 10 00 00                  cmp eax, 0x1000
009B9396  0F 85 9F 4E 17 00               jne 0x140b2e23b
009B939C  44 8B 4D 6F                     mov r9d, dword ptr [rbp + 0x6f]
009B93A0  45 8B C6                        mov r8d, r14d
009B93A3  48 8B D7                        mov rdx, rdi
009B93A6  48 8B CE                        mov rcx, rsi
009B93A9  E8 52 18 EA FF                  call 0x14085ac00
009B93AE  8B D8                           mov ebx, eax
009B93B0  3D 09 00 00 40                  cmp eax, 0x40000009
009B93B5  0F 85 DA 00 00 00               jne 0x1409b9495
009B93BB  B8 01 00 00 00                  mov eax, 1
009B93C0  89 45 C7                        mov dword ptr [rbp - 0x39], eax
009B93C3  44 03 77 08                     add r14d, dword ptr [rdi + 8]
009B93C7  4C 8D 45 7F                     lea r8, [rbp + 0x7f]
009B93CB  E8 C0 03 21 00                  call 0x140bc9790
009B93D0  48 8D 4D 7F                     lea rcx, [rbp + 0x7f]
009B93D4  E8 F7 04 21 00                  call 0x140bc98d0
009B93D9  8B 5D E3                        mov ebx, dword ptr [rbp - 0x1d]
009B93DC  41 BC 4C 01 00 C0               mov r12d, 0xc000014c
009B93E2  44 3B F3                        cmp r14d, ebx
009B93E5  0F 82 70 FF FF FF               jb 0x1409b935b
009B93EB  F6 5D C7                        neg byte ptr [rbp - 0x39]
009B93EE  1B DB                           sbb ebx, ebx
009B93F0  81 E3 09 00 00 40               and ebx, 0x40000009
009B93F6  E9 3C FF FF FF                  jmp 0x1409b9337
009B93FB  44 8B 45 F7                     mov r8d, dword ptr [rbp - 9]
009B93FF  E9 52 FC FF FF                  jmp 0x1409b9056
009B9404  45 8B D1                        mov r10d, r9d
009B9407  E9 75 FA FF FF                  jmp 0x1409b8e81
009B940C  41 BF 17 00 00 00               mov r15d, 0x17
009B9412  E9 5D FC FF FF                  jmp 0x1409b9074
009B9417  49 89 08                        mov qword ptr [r8], rcx
009B941A  49 89 40 08                     mov qword ptr [r8 + 8], rax
009B941E  4C 89 41 08                     mov qword ptr [rcx + 8], r8
009B9422  4C 89 00                        mov qword ptr [rax], r8
009B9425  E9 BD FC FF FF                  jmp 0x1409b90e7
009B942A  33 C0                           xor eax, eax
009B942C  38 05 D0 EB 61 00               cmp byte ptr [rip + 0x61ebd0], al
009B9432  0F 85 B8 4C 17 00               jne 0x140b2e0f0
009B9438  8B 05 22 E8 53 00               mov eax, dword ptr [rip + 0x53e822]
009B943E  A8 06                           test al, 6
009B9440  0F 84 2E FD FF FF               je 0x1409b9174
009B9446  E9 A5 4C 17 00                  jmp 0x140b2e0f0
009B944B  BA 01 00 00 00                  mov edx, 1
009B9450  45 8B CB                        mov r9d, r11d
009B9453  4C 8B C6                        mov r8, rsi
009B9456  48 C7 44 24 20 28 04 00 00      mov qword ptr [rsp + 0x20], 0x428
009B945F  8D 4A 50                        lea ecx, [rdx + 0x50]
009B9462  E8 F9 41 B4 FF                  call 0x1404fd660
009B9467  CC                              int3
009B9468  45 8B C8                        mov r9d, r8d
009B946B  49 8B D2                        mov rdx, r10
009B946E  4C 8B C6                        mov r8, rsi
009B9471  48 C7 44 24 20 B9 02 00 00      mov qword ptr [rsp + 0x20], 0x2b9
009B947A  B9 51 00 00 00                  mov ecx, 0x51
009B947F  E8 DC 41 B4 FF                  call 0x1404fd660
009B9484  CC                              int3
009B9485  8B D0                           mov edx, eax
009B9487  44 8B E3                        mov r12d, ebx
009B948A  41 B8 10 00 00 00               mov r8d, 0x10
009B9490  E9 BF 4C 17 00                  jmp 0x140b2e154
009B9495  85 DB                           test ebx, ebx
009B9497  0F 89 26 FF FF FF               jns 0x1409b93c3
009B949D  C7 44 24 20 B0 00 00 00         mov dword ptr [rsp + 0x20], 0xb0
009B94A5  44 8B CB                        mov r9d, ebx
009B94A8  E9 7A FE FF FF                  jmp 0x1409b9327
009B94AD  8B 55 E7                        mov edx, dword ptr [rbp - 0x19]
009B94B0  4C 8B C7                        mov r8, rdi
009B94B3  48 8B CE                        mov rcx, rsi
009B94B6  E8 D1 80 0C 00                  call 0x140a8158c
009B94BB  E9 84 FE FF FF                  jmp 0x1409b9344
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HvpRemapAndEnlistHiveBins(__int64 a1, int a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m5F;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_m78;
    unsigned int v_stack_m7C;
    unsigned int v_stack_m80;
    unsigned int v_stack_m84;
    unsigned int v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned int v_stack_m98;
    unsigned int v_stack_mA8;
    unsigned int v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int8 v_stack_p8;

    v_stack_p18 = a3;
    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (136);
    a4 = 0;
    v_stack_p20 = 0;
    result = HvpGetBinContextInitialize(v_stack_p20, a2, a3, a4);
    v_stack_m90 = 0;
    v_stack_m60 = 0;
    v_stack_m98 = 0;
    v_stack_m58 = 0;
    v_stack_m78 = 0;
    v_stack_m7C = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 280)));
    if (((*(unsigned int *)(a1 + 160)) & (0x20000ULL)) == 0) goto loc_009B9404;
    v_r10 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 232))) - (0x1000ULL));
loc_009B8E81:
    v_stack_m80 = (unsigned int)(v_r10);
loc_009B8E88:
    if (0 >= ((unsigned int)(v_r10))) goto loc_009B93E2;
    result = HvpGetCellMap(a1, 0, a3, a4);
    result = HvpMapEntryGetBinAddress(a1, result, v_stack_p20, a4);
    v_stack_m50 = result;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result + 4)) + (unsigned int)(*(unsigned int *)(result + 8)) * 1)) > ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 280))))) goto loc_009B914B;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result + 8)))) < 0x1000ULL) goto loc_009B914B;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result + 4)) + (unsigned int)(*(unsigned int *)(result + 8)) * 1)) < ((unsigned int)((unsigned int)(*(unsigned int *)(result + 8))))) goto loc_009B914B;
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(result + 8)))) & (0xFFFULL)) != 0) goto loc_009B914B;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result + 4)))) != 0) goto loc_009B914B;
    if ((*(unsigned int *)(result)) != 0x6E696268ULL) goto loc_009B914B;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result + 8)))) != 0x1000ULL) goto loc_009B91DB;
    a4 = 0;
loc_009B8F17:
    v_stack_m70 = *(unsigned __int64 *)(a1 + 56);
    v_stack_p8 = 0;
loc_009B8F2F:
    v_stack_m84 = 32;
    if (32 >= ((unsigned int)((unsigned int)(*(unsigned int *)(result + 8))))) goto loc_009B90F3;
    result = (32) + (result);
    v_stack_m68 = result;
    v_r12 = (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result))));
    if (sign_flag) {
        v_r12 = (unsigned int)(-((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result))))));
    }
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result))) >> (31));
    result = (unsigned __int8)((result) ^ (1));
    if (((unsigned int)(v_r12 + 32 * 1)) < 32) goto loc_009B9184;
    if (((unsigned int)(v_r12 + 32 * 1)) > ((unsigned int)((unsigned int)(*(unsigned int *)(result + 8))))) goto loc_009B9184;
    if ((((unsigned __int8)(v_r12)) & (7)) != 0) goto loc_009B9184;
    if ((unsigned int)(v_r12) == 0) goto loc_009B9184;
    if ((unsigned __int8)(result) != 0) goto loc_009B9004;
loc_009B8F90:
    v_rbx = (unsigned int)((32) + ((unsigned int)(v_r12)));
    goto loc_009B8F2F;
loc_009B8F95:
    v_r12 = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 8))) - ((unsigned int)(v_rbx)));
    a4 = 0;
    result = HvpMarkDirty(a1, v_rbx + 0 * 1, (unsigned int)((unsigned int)(v_r12)), a4);
    result = 0;
    if (sign_flag) goto loc_009B9485;
    a2 = 0;
    result = memset(v_stack_m68, a2, (unsigned int)((unsigned int)(v_r12)), a4);
    *(unsigned int *)(v_stack_m68) = (unsigned int)(v_r12);
    v_stack_p8 = 1;
    v_stack_mA8 = 32;
    result = SetFailureLocation(v_stack_m70, 1, 1 + 25, (unsigned int)(0x40000009ULL));
loc_009B9004:
    v_stack_m68 = (unsigned int)((unsigned int)(v_stack_m84) + 0 * 1);
    result = HvpGetCellMap(a1, (unsigned int)((unsigned int)((unsigned int)(v_stack_m84) + 0 * 1)), (unsigned int)(v_stack_m84) + 0 * 1, (unsigned int)(0x40000009ULL));
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m84) + 0 * 1))) & (0xFFFFF000ULL));
    v_rbx = (unsigned int)((v_rbx) - (*(unsigned int *)(result)));
    result = HvpGetCellMap(a1, (unsigned int)((unsigned int)(v_rbx)), (unsigned int)(v_stack_m84) + 0 * 1, (unsigned int)(0x40000009ULL));
    a4 = 0;
    v_stack_m88 = (unsigned int)((unsigned int)(*(unsigned int *)(result + 16)));
    if ((unsigned int)(v_rbx) == 0) goto loc_009B9056;
    a1 = ((unsigned int)((unsigned int)(v_rbx))) + (32);
    if (((unsigned int)((unsigned int)((unsigned int)(v_stack_m84) + 0 * 1))) == a1) goto loc_009B9294;
loc_009B9056:
    v_stack_m68 = 0;
    v_r15 = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) >> (3));
    v_r15 = (unsigned int)((v_r15) - (1));
    if (((unsigned int)(v_r15)) >= 16) goto loc_009B912D;
loc_009B9074:
    v_stack_m88 = 0;
    result = HvpGetBinContextInitialize(v_stack_m88, (unsigned int)((unsigned int)(v_rbx)), (unsigned int)(v_stack_m84) + 0 * 1, a4);
    result = HvpGetCellMap(a1, (unsigned int)((unsigned int)((unsigned int)(v_stack_m84) + 0 * 1)), (unsigned int)(v_stack_m84) + 0 * 1, a4);
    if (result == 0) goto loc_009B9468;
    result = HvpMapEntryGetBinAddress(a1, result, v_stack_m88, a4);
    v_rdi = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 4))) >> (12));
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 8))) >> (12));
    result = RtlSetBits(a1 + 320 + (unsigned int)((unsigned int)(v_r15)) + (unsigned int)((unsigned int)(v_r15)) * 2 * 8, (unsigned int)((unsigned int)(v_rdi)), a3, a4);
    *(unsigned int *)(a1 + (unsigned int)((unsigned int)(v_r15)) + (unsigned int)((unsigned int)(v_r15)) * 2 * 8 + 316) = (unsigned int)(v_rdi);
    result = (unsigned int)((1) << ((unsigned __int8)((unsigned int)((unsigned int)(v_r15)))));
    a4 = 0;
loc_009B90E7:
    goto loc_009B8F90;
loc_009B90F3:
    v_r11 = (unsigned __int8)((unsigned int)(v_stack_m98));
    if (v_stack_p8 != 0) { v_r11 = 1; }
    v_r14 = (unsigned int)((0) + ((unsigned int)((unsigned int)((unsigned int)(v_rdi)))));
    v_stack_m98 = (unsigned int)(v_r11);
    result = HvpMapEntryReleaseBinAddress((unsigned int)((unsigned int)(v_r15)), (unsigned int)((unsigned int)(v_rdi)), v_stack_p20, a4);
    result = HvpGetBinContextInitialize(v_stack_p20, (unsigned int)((unsigned int)(v_rdi)), v_stack_p20, a4);
    goto loc_009B8E88;
loc_009B912D:
    v_r15 = (unsigned int)((v_r15) >> (4));
    if (((unsigned int)(v_r15)) > 255) goto loc_009B940C;
    v_r15 = (unsigned int)((v_r15) + (16));
    goto loc_009B9074;
loc_009B914B:
    v_stack_mA8 = (unsigned int)(v_r11);
    result = SetFailureLocation(a3, 1, 1 + 33, (unsigned int)((unsigned int)(v_r12)));
    if (((v_stack_p10) & (0x20000ULL)) == 0) goto loc_009B942A;
loc_009B9174:
    v_stack_mA8 = 32;
    goto loc_009B9327;
loc_009B9184:
    v_stack_mA8 = 8;
    result = SetFailureLocation((unsigned int)(v_stack_m80), (unsigned int)((unsigned int)(v_r11)), 26, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
    a3 = 0;
    if (((v_stack_p10) & (0x20000ULL)) != 0) goto loc_009B91D0;
    if ((*(unsigned __int8 *)(v_rip + 6417990)) != 0) goto loc_009B8F95;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 5499544)))) & (6)) != 0) goto loc_009B8F95;
loc_009B91D0:
loc_009B91DB:
    v_stack_m78 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5499544)));
    result = HvpMapEntryReleaseBinAddress((unsigned int)(v_stack_m80), 0, v_stack_p20, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
    result = HvpGetBinContextInitialize(v_stack_p20, 0, v_stack_p20, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))));
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5499544)))) + v_r14 * 1)) > ((unsigned int)((unsigned int)(v_stack_m80)))) goto loc_009B93DC;
    result = HvpViewMapPromoteRangeToMapping(a1 + 224, (unsigned int)((unsigned int)(v_r14)), (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5499544)))))), v_stack_m58);
    a4 = 0;
    if (sign_flag) goto loc_009B931C;
loc_009B922A:
    if (0 >= ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5499544))))))) goto loc_009B926C;
    result = HvpGetCellMap(a1, (unsigned int)((unsigned int)(0 + v_r14 * 1)), 0, a4);
    a4 = 0;
    if (result == 0) goto loc_009B944B;
    *(unsigned __int64 *)(result + 8) = v_stack_m58;
    if (0 == 0) goto loc_009B9284;
loc_009B9259:
    *(unsigned int *)(result + 16) = 0;
    a3 = (unsigned int)((0) + (0x1000ULL));
    *(unsigned __int64 *)(result) = 0;
    goto loc_009B922A;
loc_009B926C:
    result = HvpMapEntryGetBinAddress(a1, (unsigned int)((unsigned int)((unsigned int)(0xC000014CULL))), v_stack_p20, a4);
    v_stack_m50 = result;
    goto loc_009B8F17;
loc_009B9284:
    a1 = (v_stack_m58) | (1);
    *(unsigned __int64 *)(result + 8) = a1;
    goto loc_009B9259;
loc_009B9294:
    if (((unsigned int)(v_stack_p20 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5499544)))) * 1)) != ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0xC000014CULL)))))) goto loc_009B9056;
    a2 = 0;
    result = guard_dispatch_icall(a2 + 24, a2, (unsigned int)(0x20374D43ULL), a4);
    a4 = 0;
    if (result == 0) goto loc_009B93FB;
    *(unsigned __int64 *)(result) = 0;
    *(unsigned __int64 *)(result + 8) = 0;
    *(unsigned int *)(result + 16) = (unsigned int)((unsigned int)(v_stack_m88));
    *(unsigned int *)(result + 20) = (unsigned int)((unsigned int)((unsigned int)(v_stack_m58)));
    if (((unsigned int)(v_stack_m58)) >= ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0xC000014CULL)))))) goto loc_009B9301;
loc_009B92E1:
    result = HvpGetCellMap(a1, (unsigned int)((unsigned int)(v_stack_m58)), result, a4);
    v_rbx = (unsigned int)((v_stack_m58) + (0x1000ULL));
    *(unsigned __int64 *)(result) = result;
    if (((unsigned int)(v_rbx)) < ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0xC000014CULL)))))) goto loc_009B92E1;
    a4 = 0;
loc_009B9301:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 888) + 8)) == (a1 + 888)) goto loc_009B9417;
loc_009B931C:
    v_stack_mA8 = 64;
loc_009B9327:
    a2 = 0;
    result = SetFailureLocation(a3, a2, 34, (unsigned int)((unsigned int)(a1 + 888)));
loc_009B9337:
    if (v_stack_m90 != 0) goto loc_009B94AD;
loc_009B9344:
    v_rsp = (v_rsp) + (136);
    return (unsigned int)((unsigned int)(v_rbx));
loc_009B935B:
    result = HvpGetCellMap(a1, (unsigned int)((unsigned int)(v_r14)), 34, (unsigned int)((unsigned int)(a1 + 888)));
    result = HvpMapEntryGetBinAddress(a1, result, v_stack_p20, (unsigned int)((unsigned int)(a1 + 888)));
    result = HvpValidateLoadedBin(result, (unsigned int)((unsigned int)(v_r14)), (unsigned int)((unsigned int)(v_rbx)), (unsigned int)((unsigned int)(a1 + 888)));
    result = HvpEnlistFreeCells(a1, result, (unsigned int)((unsigned int)(v_r14)), (unsigned int)(v_stack_p10));
    if (((unsigned int)(result)) != 0x40000009ULL) goto loc_009B9495;
    v_stack_m98 = 1;
loc_009B93C3:
    v_r14 = (unsigned int)((v_r14) + (*(unsigned int *)(result + 8)));
    result = HvpMapEntryReleaseBinAddress(a1, result, v_stack_p20, (unsigned int)(v_stack_p10));
    result = HvpGetBinContextInitialize(v_stack_p20, result, v_stack_p20, (unsigned int)(v_stack_p10));
loc_009B93DC:
loc_009B93E2:
    if (((unsigned int)(v_r14)) < ((unsigned int)((unsigned int)(v_stack_m7C)))) goto loc_009B935B;
    v_rbx = (unsigned int)(((unsigned int)(v_stack_m7C)) & (0x40000009ULL));
    goto loc_009B9337;
loc_009B93FB:
    goto loc_009B9056;
loc_009B9404:
    goto loc_009B8E81;
loc_009B940C:
    goto loc_009B9074;
loc_009B9417:
    *(unsigned __int64 *)((unsigned int)(v_stack_m68)) = v_stack_p20;
    *(unsigned __int64 *)((unsigned int)(v_stack_m68) + 8) = result;
    *(unsigned __int64 *)(v_stack_p20 + 8) = (unsigned int)(v_stack_m68);
    *(unsigned __int64 *)(result) = (unsigned int)(v_stack_m68);
    goto loc_009B90E7;
loc_009B942A:
    result = 0;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 5498914)))) & (6)) == 0) goto loc_009B9174;
loc_009B944B:
    v_stack_p20 = 0x428ULL;
    result = KeBugCheckEx(1 + 80, 1, a1, (unsigned int)((unsigned int)(0 + v_r14 * 1)));
loc_009B9468:
    v_stack_p20 = 697;
    result = KeBugCheckEx(81, (unsigned int)((unsigned int)((unsigned int)(v_stack_p10))), a1, (unsigned int)((unsigned int)(a1)));
loc_009B9485:
loc_009B9495:
    if (!sign_flag) goto loc_009B93C3;
    v_stack_p20 = 176;
    goto loc_009B9327;
loc_009B94AD:
    result = HvpFreeBin(a1, (unsigned int)(v_stack_m78), result, (unsigned int)((unsigned int)(v_rbx)));
    goto loc_009B9344;
}
```

## 5. (Beta) C Style

```c
int64_t HvpRemapAndEnlistHiveBins(void *Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m5F;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint32_t v_stack_m78;
    uint32_t v_stack_m7C;
    uint32_t v_stack_m80;
    uint32_t v_stack_m84;
    uint32_t v_stack_m88;
    uint64_t v_stack_m90;
    uint32_t v_stack_m98;
    uint32_t v_stack_mA8;
    uint32_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint8_t v_stack_p8;

    v_stack_p18 = Arg3;
    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (136);
    Arg4 = 0;
    v_stack_p20 = 0;
    result = HvpGetBinContextInitialize(v_stack_p20, Arg2, Arg3, Arg4);
    v_stack_m90 = 0;
    v_stack_m60 = 0;
    v_stack_m98 = 0;
    v_stack_m58 = 0;
    v_stack_m78 = 0;
    v_stack_m7C = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x118)));
    if (((*(uint32_t *)(arg1 + 0xA0)) & (0x20000ULL)) == 0) goto loc_009B9404;
    local_r10 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0xE8))) - (0x1000ULL));
loc_009B8E81:
    v_stack_m80 = (uint32_t)(local_r10);
loc_009B8E88:
    if (0 >= ((uint32_t)(local_r10))) goto loc_009B93E2;
    result = HvpGetCellMap(Arg1, 0, Arg3, Arg4);
    result = HvpMapEntryGetBinAddress(Arg1, result, v_stack_p20, Arg4);
    v_stack_m50 = result;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x4)) + (uint32_t)(*(uint32_t *)(result + 0x8)) * 1)) > ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x118))))) goto loc_009B914B;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x8)))) < 0x1000ULL) goto loc_009B914B;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x4)) + (uint32_t)(*(uint32_t *)(result + 0x8)) * 1)) < ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x8))))) goto loc_009B914B;
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x8)))) & (0xFFFULL)) != 0) goto loc_009B914B;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x4)))) != 0) goto loc_009B914B;
    if ((*(uint32_t *)(result)) != 0x6E696268ULL) goto loc_009B914B;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x8)))) != 0x1000ULL) goto loc_009B91DB;
    Arg4 = 0;
loc_009B8F17:
    v_stack_m70 = *(uint64_t *)(arg1 + 0x38);
    v_stack_p8 = 0;
loc_009B8F2F:
    v_stack_m84 = 32;
    if (32 >= ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x8))))) goto loc_009B90F3;
    result = (32) + (result);
    v_stack_m68 = result;
    local_r12 = (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result))));
    if (sign_flag) {
        local_r12 = (uint32_t)(-((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result))))));
    }
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result))) >> (31));
    result = (uint8_t)((result) ^ (1));
    if (((uint32_t)(local_r12 + 32 * 1)) < 32) goto loc_009B9184;
    if (((uint32_t)(local_r12 + 32 * 1)) > ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x8))))) goto loc_009B9184;
    if ((((uint8_t)(local_r12)) & (7)) != 0) goto loc_009B9184;
    if ((uint32_t)(local_r12) == 0) goto loc_009B9184;
    if ((uint8_t)(result) != 0) goto loc_009B9004;
loc_009B8F90:
    local_rbx = (uint32_t)((32) + ((uint32_t)(local_r12)));
    goto loc_009B8F2F;
loc_009B8F95:
    local_r12 = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x8))) - ((uint32_t)(local_rbx)));
    Arg4 = 0;
    result = HvpMarkDirty(Arg1, local_rbx + 0 * 1, (uint32_t)((uint32_t)(local_r12)), Arg4);
    result = 0;
    if (sign_flag) goto loc_009B9485;
    Arg2 = 0;
    result = memset(v_stack_m68, Arg2, (uint32_t)((uint32_t)(local_r12)), Arg4);
    *(uint32_t *)(v_stack_m68) = (uint32_t)(local_r12);
    v_stack_p8 = 1;
    v_stack_mA8 = 32;
    result = SetFailureLocation(v_stack_m70, 1, 1 + 25, (uint32_t)(0x40000009ULL));
loc_009B9004:
    v_stack_m68 = (uint32_t)((uint32_t)(v_stack_m84) + 0 * 1);
    result = HvpGetCellMap(Arg1, (uint32_t)((uint32_t)((uint32_t)(v_stack_m84) + 0 * 1)), (uint32_t)(v_stack_m84) + 0 * 1, (uint32_t)(0x40000009ULL));
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m84) + 0 * 1))) & (0xFFFFF000ULL));
    local_rbx = (uint32_t)((local_rbx) - (*(uint32_t *)(result)));
    result = HvpGetCellMap(Arg1, (uint32_t)((uint32_t)(local_rbx)), (uint32_t)(v_stack_m84) + 0 * 1, (uint32_t)(0x40000009ULL));
    Arg4 = 0;
    v_stack_m88 = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x10)));
    if ((uint32_t)(local_rbx) == 0) goto loc_009B9056;
    Arg1 = ((uint32_t)((uint32_t)(local_rbx))) + (32);
    if (((uint32_t)((uint32_t)((uint32_t)(v_stack_m84) + 0 * 1))) == Arg1) goto loc_009B9294;
loc_009B9056:
    v_stack_m68 = 0;
    local_r15 = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) >> (3));
    local_r15 = (uint32_t)((local_r15) - (1));
    if (((uint32_t)(local_r15)) >= 16) goto loc_009B912D;
loc_009B9074:
    v_stack_m88 = 0;
    result = HvpGetBinContextInitialize(v_stack_m88, (uint32_t)((uint32_t)(local_rbx)), (uint32_t)(v_stack_m84) + 0 * 1, Arg4);
    result = HvpGetCellMap(Arg1, (uint32_t)((uint32_t)((uint32_t)(v_stack_m84) + 0 * 1)), (uint32_t)(v_stack_m84) + 0 * 1, Arg4);
    if (result == 0) goto loc_009B9468;
    result = HvpMapEntryGetBinAddress(Arg1, result, v_stack_m88, Arg4);
    local_rdi = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x4))) >> (12));
    Arg3 = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x8))) >> (12));
    result = RtlSetBits(Arg1 + 320 + (uint32_t)((uint32_t)(local_r15)) + (uint32_t)((uint32_t)(local_r15)) * 2 * 8, (uint32_t)((uint32_t)(local_rdi)), Arg3, Arg4);
    *(uint32_t *)(arg1 + (uint32_t)((uint32_t)(local_r15)) + (uint32_t)((uint32_t)(local_r15)) * 2 * 8 + 0x13C) = (uint32_t)(local_rdi);
    result = (uint32_t)((1) << ((uint8_t)((uint32_t)((uint32_t)(local_r15)))));
    Arg4 = 0;
loc_009B90E7:
    goto loc_009B8F90;
loc_009B90F3:
    local_r11 = (uint8_t)((uint32_t)(v_stack_m98));
    if (v_stack_p8 != 0) { local_r11 = 1; }
    local_r14 = (uint32_t)((0) + ((uint32_t)((uint32_t)((uint32_t)(local_rdi)))));
    v_stack_m98 = (uint32_t)(local_r11);
    result = HvpMapEntryReleaseBinAddress((uint32_t)((uint32_t)(local_r15)), (uint32_t)((uint32_t)(local_rdi)), v_stack_p20, Arg4);
    result = HvpGetBinContextInitialize(v_stack_p20, (uint32_t)((uint32_t)(local_rdi)), v_stack_p20, Arg4);
    goto loc_009B8E88;
loc_009B912D:
    local_r15 = (uint32_t)((local_r15) >> (4));
    if (((uint32_t)(local_r15)) > 255) goto loc_009B940C;
    local_r15 = (uint32_t)((local_r15) + (16));
    goto loc_009B9074;
loc_009B914B:
    v_stack_mA8 = (uint32_t)(local_r11);
    result = SetFailureLocation(Arg3, 1, 1 + 33, (uint32_t)((uint32_t)(local_r12)));
    if (((v_stack_p10) & (0x20000ULL)) == 0) goto loc_009B942A;
loc_009B9174:
    v_stack_mA8 = 32;
    goto loc_009B9327;
loc_009B9184:
    v_stack_mA8 = 8;
    result = SetFailureLocation((uint32_t)(v_stack_m80), (uint32_t)((uint32_t)(local_r11)), 26, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
    Arg3 = 0;
    if (((v_stack_p10) & (0x20000ULL)) != 0) goto loc_009B91D0;
    if ((*(uint8_t *)(v_rip + 0x61EE46)) != 0) goto loc_009B8F95;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x53EA98)))) & (6)) != 0) goto loc_009B8F95;
loc_009B91D0:
loc_009B91DB:
    v_stack_m78 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x53EA98)));
    result = HvpMapEntryReleaseBinAddress((uint32_t)(v_stack_m80), 0, v_stack_p20, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
    result = HvpGetBinContextInitialize(v_stack_p20, 0, v_stack_p20, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))));
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x53EA98)))) + local_r14 * 1)) > ((uint32_t)((uint32_t)(v_stack_m80)))) goto loc_009B93DC;
    result = HvpViewMapPromoteRangeToMapping(Arg1 + 224, (uint32_t)((uint32_t)(local_r14)), (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x53EA98)))))), v_stack_m58);
    Arg4 = 0;
    if (sign_flag) goto loc_009B931C;
loc_009B922A:
    if (0 >= ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x53EA98))))))) goto loc_009B926C;
    result = HvpGetCellMap(Arg1, (uint32_t)((uint32_t)(0 + local_r14 * 1)), 0, Arg4);
    Arg4 = 0;
    if (result == 0) goto loc_009B944B;
    *(uint64_t *)(result + 0x8) = v_stack_m58;
    if (0 == 0) goto loc_009B9284;
loc_009B9259:
    *(uint32_t *)(result + 0x10) = 0;
    Arg3 = (uint32_t)((0) + (0x1000ULL));
    *(uint64_t *)(result) = 0;
    goto loc_009B922A;
loc_009B926C:
    result = HvpMapEntryGetBinAddress(Arg1, (uint32_t)((uint32_t)((uint32_t)(0xC000014CULL))), v_stack_p20, Arg4);
    v_stack_m50 = result;
    goto loc_009B8F17;
loc_009B9284:
    Arg1 = (v_stack_m58) | (1);
    *(void **)(result + 0x8) = Arg1;
    goto loc_009B9259;
loc_009B9294:
    if (((uint32_t)(v_stack_p20 + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x53EA98)))) * 1)) != ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0xC000014CULL)))))) goto loc_009B9056;
    Arg2 = 0;
    result = guard_dispatch_icall(Arg2 + 24, Arg2, (uint32_t)(0x20374D43ULL), Arg4);
    Arg4 = 0;
    if (result == 0) goto loc_009B93FB;
    *(uint64_t *)(result) = 0;
    *(uint64_t *)(result + 0x8) = 0;
    *(uint32_t *)(result + 0x10) = (uint32_t)((uint32_t)(v_stack_m88));
    *(uint32_t *)(result + 0x14) = (uint32_t)((uint32_t)((uint32_t)(v_stack_m58)));
    if (((uint32_t)(v_stack_m58)) >= ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0xC000014CULL)))))) goto loc_009B9301;
loc_009B92E1:
    result = HvpGetCellMap(Arg1, (uint32_t)((uint32_t)(v_stack_m58)), result, Arg4);
    local_rbx = (uint32_t)((v_stack_m58) + (0x1000ULL));
    *(uint64_t *)(result) = result;
    if (((uint32_t)(local_rbx)) < ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0xC000014CULL)))))) goto loc_009B92E1;
    Arg4 = 0;
loc_009B9301:
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x378) + 0x8)) == (Arg1 + 888)) goto loc_009B9417;
loc_009B931C:
    v_stack_mA8 = 64;
loc_009B9327:
    Arg2 = 0;
    result = SetFailureLocation(Arg3, Arg2, 34, (uint32_t)((uint32_t)(Arg1 + 888)));
loc_009B9337:
    if (v_stack_m90 != 0) goto loc_009B94AD;
loc_009B9344:
    local_rsp = (local_rsp) + (136);
    return (uint32_t)((uint32_t)(local_rbx));
loc_009B935B:
    result = HvpGetCellMap(Arg1, (uint32_t)((uint32_t)(local_r14)), 34, (uint32_t)((uint32_t)(Arg1 + 888)));
    result = HvpMapEntryGetBinAddress(Arg1, result, v_stack_p20, (uint32_t)((uint32_t)(Arg1 + 888)));
    result = HvpValidateLoadedBin(result, (uint32_t)((uint32_t)(local_r14)), (uint32_t)((uint32_t)(local_rbx)), (uint32_t)((uint32_t)(Arg1 + 888)));
    result = HvpEnlistFreeCells(Arg1, result, (uint32_t)((uint32_t)(local_r14)), (uint32_t)(v_stack_p10));
    if (((uint32_t)(result)) != 0x40000009ULL) goto loc_009B9495;
    v_stack_m98 = 1;
loc_009B93C3:
    local_r14 = (uint32_t)((local_r14) + (*(uint32_t *)(result + 0x8)));
    result = HvpMapEntryReleaseBinAddress(Arg1, result, v_stack_p20, (uint32_t)(v_stack_p10));
    result = HvpGetBinContextInitialize(v_stack_p20, result, v_stack_p20, (uint32_t)(v_stack_p10));
loc_009B93DC:
loc_009B93E2:
    if (((uint32_t)(local_r14)) < ((uint32_t)((uint32_t)(v_stack_m7C)))) goto loc_009B935B;
    local_rbx = (uint32_t)(((uint32_t)(v_stack_m7C)) & (0x40000009ULL));
    goto loc_009B9337;
loc_009B93FB:
    goto loc_009B9056;
loc_009B9404:
    goto loc_009B8E81;
loc_009B940C:
    goto loc_009B9074;
loc_009B9417:
    *(uint64_t *)((uint32_t)(v_stack_m68)) = v_stack_p20;
    *(uint64_t *)((uint32_t)(v_stack_m68) + 0x8) = result;
    *(uint64_t *)(v_stack_p20 + 0x8) = (uint32_t)(v_stack_m68);
    *(uint64_t *)(result) = (uint32_t)(v_stack_m68);
    goto loc_009B90E7;
loc_009B942A:
    result = 0;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x53E822)))) & (6)) == 0) goto loc_009B9174;
loc_009B944B:
    v_stack_p20 = 0x428ULL;
    result = KeBugCheckEx(1 + 80, 1, Arg1, (uint32_t)((uint32_t)(0 + local_r14 * 1)));
loc_009B9468:
    v_stack_p20 = 697;
    result = KeBugCheckEx(81, (uint32_t)((uint32_t)((uint32_t)(v_stack_p10))), Arg1, (uint32_t)((uint32_t)(Arg1)));
loc_009B9485:
loc_009B9495:
    if (!sign_flag) goto loc_009B93C3;
    v_stack_p20 = 176;
    goto loc_009B9327;
loc_009B94AD:
    result = HvpFreeBin(Arg1, (uint32_t)(v_stack_m78), result, (uint32_t)((uint32_t)(local_rbx)));
    goto loc_009B9344;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x0` | `64` | `W` |
| `Arg1` | `+ 0x0 + rbx*8` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x38` | `64` | `R` |
| `Arg1` | `+ 0x40` | `64` | `R` |
| `Arg1` | `+ 0x90` | `32` | `R/W` |
| `Arg1` | `+ 0x94` | `32` | `R/W` |
| `Arg1` | `+ 0x98` | `32` | `R/W` |
| `Arg1` | `+ 0xA0` | `32` | `R` |
| `Arg1` | `+ 0xE0` | `64` | `R` |
| `Arg1` | `+ 0xE8` | `32` | `R` |
| `Arg1` | `+ 0x118` | `32` | `R` |
| `Arg1` | `+ 0x13C + rbx*8` | `32` | `W` |
| `Arg1` | `+ 0x140` | `64` | `R` |
| `Arg1` | `+ 0x378` | `64` | `R` |
| `Arg1` | `+ 0x388` | `32` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009B8E0C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
