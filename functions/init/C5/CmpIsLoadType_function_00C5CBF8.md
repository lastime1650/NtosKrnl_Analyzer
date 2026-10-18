# CmpIsLoadType

- RVA: `0x00C5CBF8`–`0x00C5CF8D` (길이 `917` bytes)
- VA: `0x0000000140C5CBF8`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00068EF0`
- 디코드: `245`개 명령, `917/917` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **37**; 고유 호출 대상: **10**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x00C5CC7C` → [HvpGetCellFlat](../../page/85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x00C5CC83` → [HvpGetCellPaged](../../page/85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x00C5CCB5` → [CmpGetNodeName](CmpGetNodeName_function_00C5C95C.md) (function, `0x00C5C95C`)
- `0x00C5CCCD` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (function, `0x00463960`)
- `0x00C5CCE1` → [CmpFindSubKeyByName](../../page/A4/CmpFindSubKeyByName_function_00A49D58.md) (function, `0x00A49D58`)
- `0x00C5CCFD` → [HvpGetCellFlat](../../page/85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x00C5CD04` → [HvpGetCellPaged](../../page/85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x00C5CD1E` → [CmpFindValueByName](../../page/84/CmpFindValueByName_function_00844E1C.md) (function, `0x00844E1C`)
- `0x00C5CD36` → [HvpReleaseCellFlat](../../page/85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00C5CD3D` → [HvpReleaseCellPaged](../../page/85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00C5CD4D` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00C5CD72` → [CmpFindValueByName](../../page/84/CmpFindValueByName_function_00844E1C.md) (function, `0x00844E1C`)
- `0x00C5CD95` → [HvpGetCellFlat](../../page/85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x00C5CD9C` → [HvpGetCellPaged](../../page/85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x00C5CDC0` → [CmpValueToData](../../page/7F/CmpValueToData_function_007F3934.md) (function, `0x007F3934`)
- `0x00C5CDD8` → [HvpReleaseCellFlat](../../page/85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00C5CDDF` → [HvpReleaseCellPaged](../../page/85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00C5CE14` → [HvpReleaseCellFlat](../../page/85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00C5CE1B` → [HvpReleaseCellPaged](../../page/85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00C5CE2A` → [CmpFindSubKeyByName](../../page/A4/CmpFindSubKeyByName_function_00A49D58.md) (function, `0x00A49D58`)
- `0x00C5CE46` → [HvpGetCellFlat](../../page/85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x00C5CE4D` → [HvpGetCellPaged](../../page/85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x00C5CE67` → [CmpFindValueByName](../../page/84/CmpFindValueByName_function_00844E1C.md) (function, `0x00844E1C`)
- `0x00C5CE7F` → [HvpReleaseCellFlat](../../page/85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00C5CE86` → [HvpReleaseCellPaged](../../page/85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00C5CEA0` → [CmpFindValueByName](../../page/84/CmpFindValueByName_function_00844E1C.md) (function, `0x00844E1C`)
- `0x00C5CEC8` → [HvpGetCellFlat](../../page/85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x00C5CECF` → [HvpGetCellPaged](../../page/85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x00C5CEEF` → [CmpValueToData](../../page/7F/CmpValueToData_function_007F3934.md) (function, `0x007F3934`)
- `0x00C5CF0B` → [HvpReleaseCellFlat](../../page/85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00C5CF12` → [HvpReleaseCellPaged](../../page/85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00C5CF33` → [HvpReleaseCellFlat](../../page/85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00C5CF3A` → [HvpReleaseCellPaged](../../page/85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00C5CF47` → [HvpReleaseCellFlat](../../page/85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00C5CF4E` → [HvpReleaseCellPaged](../../page/85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00C5CF66` → [HvpReleaseCellFlat](../../page/85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00C5CF6D` → [HvpReleaseCellPaged](../../page/85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)

### Direct callers
- [CmpFindDrivers](CmpFindDrivers_function_00C5BFBC.md) at `0x00C5C10C`
- [CmpFindDrivers](CmpFindDrivers_function_00C5BFBC.md) at `0x00C5C1B0`

### Static image references
- `0x00C5CD0E` → RVA `0x00C821A8` (`CmpStartString`; read)
- `0x00C5CD65` → RVA `0x00C822A0` (`CmpTypeString`; read)
- `0x00C5CDF6` → RVA `0x00C82240` (`CmpDriverWildcardString`; read)
- `0x00C5CDFD` → RVA `0x00C822C0` (`CmpServiceWildcardString`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **36**
  - `0x00C5CC7C` → [HvpGetCellFlat](../../page/85/HvpGetCellFlat_function_00854C60.md) (`INIT` → `PAGE`)
  - `0x00C5CC83` → [HvpGetCellPaged](../../page/85/HvpGetCellPaged_function_00854CB0.md) (`INIT` → `PAGE`)
  - `0x00C5CCCD` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (`INIT` → `.text`)
  - `0x00C5CCE1` → [CmpFindSubKeyByName](../../page/A4/CmpFindSubKeyByName_function_00A49D58.md) (`INIT` → `PAGE`)
  - `0x00C5CCFD` → [HvpGetCellFlat](../../page/85/HvpGetCellFlat_function_00854C60.md) (`INIT` → `PAGE`)
  - `0x00C5CD04` → [HvpGetCellPaged](../../page/85/HvpGetCellPaged_function_00854CB0.md) (`INIT` → `PAGE`)
  - `0x00C5CD1E` → [CmpFindValueByName](../../page/84/CmpFindValueByName_function_00844E1C.md) (`INIT` → `PAGE`)
  - `0x00C5CD36` → [HvpReleaseCellFlat](../../page/85/HvpReleaseCellFlat_function_0085CC20.md) (`INIT` → `PAGE`)
  - `0x00C5CD3D` → [HvpReleaseCellPaged](../../page/85/HvpReleaseCellPaged_function_00855F40.md) (`INIT` → `PAGE`)
  - `0x00C5CD4D` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`INIT` → `.text`)
  - `0x00C5CD72` → [CmpFindValueByName](../../page/84/CmpFindValueByName_function_00844E1C.md) (`INIT` → `PAGE`)
  - `0x00C5CD95` → [HvpGetCellFlat](../../page/85/HvpGetCellFlat_function_00854C60.md) (`INIT` → `PAGE`)
  - `0x00C5CD9C` → [HvpGetCellPaged](../../page/85/HvpGetCellPaged_function_00854CB0.md) (`INIT` → `PAGE`)
  - `0x00C5CDC0` → [CmpValueToData](../../page/7F/CmpValueToData_function_007F3934.md) (`INIT` → `PAGE`)
  - `0x00C5CDD8` → [HvpReleaseCellFlat](../../page/85/HvpReleaseCellFlat_function_0085CC20.md) (`INIT` → `PAGE`)
  - `0x00C5CDDF` → [HvpReleaseCellPaged](../../page/85/HvpReleaseCellPaged_function_00855F40.md) (`INIT` → `PAGE`)
  - `0x00C5CE14` → [HvpReleaseCellFlat](../../page/85/HvpReleaseCellFlat_function_0085CC20.md) (`INIT` → `PAGE`)
  - `0x00C5CE1B` → [HvpReleaseCellPaged](../../page/85/HvpReleaseCellPaged_function_00855F40.md) (`INIT` → `PAGE`)
  - `0x00C5CE2A` → [CmpFindSubKeyByName](../../page/A4/CmpFindSubKeyByName_function_00A49D58.md) (`INIT` → `PAGE`)
  - `0x00C5CE46` → [HvpGetCellFlat](../../page/85/HvpGetCellFlat_function_00854C60.md) (`INIT` → `PAGE`)
  - `0x00C5CE4D` → [HvpGetCellPaged](../../page/85/HvpGetCellPaged_function_00854CB0.md) (`INIT` → `PAGE`)
  - `0x00C5CE67` → [CmpFindValueByName](../../page/84/CmpFindValueByName_function_00844E1C.md) (`INIT` → `PAGE`)
  - `0x00C5CE7F` → [HvpReleaseCellFlat](../../page/85/HvpReleaseCellFlat_function_0085CC20.md) (`INIT` → `PAGE`)
  - `0x00C5CE86` → [HvpReleaseCellPaged](../../page/85/HvpReleaseCellPaged_function_00855F40.md) (`INIT` → `PAGE`)
  - `0x00C5CEA0` → [CmpFindValueByName](../../page/84/CmpFindValueByName_function_00844E1C.md) (`INIT` → `PAGE`)
  - `0x00C5CEC8` → [HvpGetCellFlat](../../page/85/HvpGetCellFlat_function_00854C60.md) (`INIT` → `PAGE`)
  - `0x00C5CECF` → [HvpGetCellPaged](../../page/85/HvpGetCellPaged_function_00854CB0.md) (`INIT` → `PAGE`)
  - `0x00C5CEEF` → [CmpValueToData](../../page/7F/CmpValueToData_function_007F3934.md) (`INIT` → `PAGE`)
  - `0x00C5CF0B` → [HvpReleaseCellFlat](../../page/85/HvpReleaseCellFlat_function_0085CC20.md) (`INIT` → `PAGE`)
  - `0x00C5CF12` → [HvpReleaseCellPaged](../../page/85/HvpReleaseCellPaged_function_00855F40.md) (`INIT` → `PAGE`)
  - `0x00C5CF33` → [HvpReleaseCellFlat](../../page/85/HvpReleaseCellFlat_function_0085CC20.md) (`INIT` → `PAGE`)
  - `0x00C5CF3A` → [HvpReleaseCellPaged](../../page/85/HvpReleaseCellPaged_function_00855F40.md) (`INIT` → `PAGE`)
  - `0x00C5CF47` → [HvpReleaseCellFlat](../../page/85/HvpReleaseCellFlat_function_0085CC20.md) (`INIT` → `PAGE`)
  - `0x00C5CF4E` → [HvpReleaseCellPaged](../../page/85/HvpReleaseCellPaged_function_00855F40.md) (`INIT` → `PAGE`)
  - `0x00C5CF66` → [HvpReleaseCellFlat](../../page/85/HvpReleaseCellFlat_function_0085CC20.md) (`INIT` → `PAGE`)
  - `0x00C5CF6D` → [HvpReleaseCellPaged](../../page/85/HvpReleaseCellPaged_function_00855F40.md) (`INIT` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C5CBF8  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00C5CBFD  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
00C5CC02  44 89 44 24 18                  mov dword ptr [rsp + 0x18], r8d
00C5CC07  55                              push rbp
00C5CC08  56                              push rsi
00C5CC09  57                              push rdi
00C5CC0A  41 54                           push r12
00C5CC0C  41 55                           push r13
00C5CC0E  41 56                           push r14
00C5CC10  41 57                           push r15
00C5CC12  48 8B EC                        mov rbp, rsp
00C5CC15  48 83 EC 50                     sub rsp, 0x50
00C5CC19  33 DB                           xor ebx, ebx
00C5CC1B  4C 8D 85 88 00 00 00            lea r8, [rbp + 0x88]
00C5CC22  41 83 CD FF                     or r13d, 0xffffffff
00C5CC26  89 5D 64                        mov dword ptr [rbp + 0x64], ebx
00C5CC29  F6 81 8C 00 00 00 01            test byte ptr [rcx + 0x8c], 1
00C5CC30  0F 57 C0                        xorps xmm0, xmm0
00C5CC33  48 8B F9                        mov rdi, rcx
00C5CC36  44 89 6D 60                     mov dword ptr [rbp + 0x60], r13d
00C5CC3A  44 89 AD 88 00 00 00            mov dword ptr [rbp + 0x88], r13d
00C5CC41  44 8B F3                        mov r14d, ebx
00C5CC44  89 9D 8C 00 00 00               mov dword ptr [rbp + 0x8c], ebx
00C5CC4A  45 8B FD                        mov r15d, r13d
00C5CC4D  89 5D 58                        mov dword ptr [rbp + 0x58], ebx
00C5CC50  44 89 6D 40                     mov dword ptr [rbp + 0x40], r13d
00C5CC54  89 5D 44                        mov dword ptr [rbp + 0x44], ebx
00C5CC57  44 89 6D E0                     mov dword ptr [rbp - 0x20], r13d
00C5CC5B  89 5D E4                        mov dword ptr [rbp - 0x1c], ebx
00C5CC5E  44 89 6D 78                     mov dword ptr [rbp + 0x78], r13d
00C5CC62  89 5D 7C                        mov dword ptr [rbp + 0x7c], ebx
00C5CC65  0F 11 45 E8                     movups xmmword ptr [rbp - 0x18], xmm0
00C5CC69  44 89 AD 80 00 00 00            mov dword ptr [rbp + 0x80], r13d
00C5CC70  89 9D 84 00 00 00               mov dword ptr [rbp + 0x84], ebx
00C5CC76  66 89 5D 50                     mov word ptr [rbp + 0x50], bx
00C5CC7A  74 07                           je 0x140c5cc83
00C5CC7C  E8 DF 7F BF FF                  call 0x140854c60
00C5CC81  EB 05                           jmp 0x140c5cc88
00C5CC83  E8 28 80 BF FF                  call 0x140854cb0
00C5CC88  4C 8B E0                        mov r12, rax
00C5CC8B  48 85 C0                        test rax, rax
00C5CC8E  0F 84 E0 02 00 00               je 0x140c5cf74
00C5CC94  48 8B 75 68                     mov rsi, qword ptr [rbp + 0x68]
00C5CC98  48 85 F6                        test rsi, rsi
00C5CC9B  0F 84 EF 01 00 00               je 0x140c5ce90
00C5CCA1  48 39 5D 70                     cmp qword ptr [rbp + 0x70], rbx
00C5CCA5  0F 84 E5 01 00 00               je 0x140c5ce90
00C5CCAB  4C 8D 45 50                     lea r8, [rbp + 0x50]
00C5CCAF  49 8B D4                        mov rdx, r12
00C5CCB2  48 8B CF                        mov rcx, rdi
00C5CCB5  E8 A2 FC FF FF                  call 0x140c5c95c
00C5CCBA  4C 8B E8                        mov r13, rax
00C5CCBD  48 85 C0                        test rax, rax
00C5CCC0  0F 84 9B 00 00 00               je 0x140c5cd61
00C5CCC6  48 8B D0                        mov rdx, rax
00C5CCC9  48 8D 4D E8                     lea rcx, [rbp - 0x18]
00C5CCCD  E8 8E 6C 80 FF                  call 0x140463960
00C5CCD2  85 C0                           test eax, eax
00C5CCD4  78 6C                           js 0x140c5cd42
00C5CCD6  48 8B 55 70                     mov rdx, qword ptr [rbp + 0x70]
00C5CCDA  4C 8D 45 E8                     lea r8, [rbp - 0x18]
00C5CCDE  48 8B CE                        mov rcx, rsi
00C5CCE1  E8 72 D0 DE FF                  call 0x140a49d58
00C5CCE6  8B D0                           mov edx, eax
00C5CCE8  83 F8 FF                        cmp eax, -1
00C5CCEB  74 55                           je 0x140c5cd42
00C5CCED  F6 86 8C 00 00 00 01            test byte ptr [rsi + 0x8c], 1
00C5CCF4  4C 8D 45 40                     lea r8, [rbp + 0x40]
00C5CCF8  48 8B CE                        mov rcx, rsi
00C5CCFB  74 07                           je 0x140c5cd04
00C5CCFD  E8 5E 7F BF FF                  call 0x140854c60
00C5CD02  EB 05                           jmp 0x140c5cd09
00C5CD04  E8 A7 7F BF FF                  call 0x140854cb0
00C5CD09  48 85 C0                        test rax, rax
00C5CD0C  74 34                           je 0x140c5cd42
00C5CD0E  4C 8D 05 93 54 02 00            lea r8, [rip + 0x25493]
00C5CD15  48 8B D0                        mov rdx, rax
00C5CD18  48 8B CE                        mov rcx, rsi
00C5CD1B  4C 8B F6                        mov r14, rsi
00C5CD1E  E8 F9 80 BE FF                  call 0x140844e1c
00C5CD23  F6 86 8C 00 00 00 01            test byte ptr [rsi + 0x8c], 1
00C5CD2A  48 8D 55 40                     lea rdx, [rbp + 0x40]
00C5CD2E  44 8B F8                        mov r15d, eax
00C5CD31  48 8B CE                        mov rcx, rsi
00C5CD34  74 07                           je 0x140c5cd3d
00C5CD36  E8 E5 FE BF FF                  call 0x14085cc20
00C5CD3B  EB 05                           jmp 0x140c5cd42
00C5CD3D  E8 FE 91 BF FF                  call 0x140855f40
00C5CD42  0F B7 55 50                     movzx edx, word ptr [rbp + 0x50]
00C5CD46  49 8B CD                        mov rcx, r13
00C5CD49  48 8B 47 20                     mov rax, qword ptr [rdi + 0x20]
00C5CD4D  E8 7E DD A5 FF                  call 0x1406baad0
00C5CD52  41 83 CD FF                     or r13d, 0xffffffff
00C5CD56  45 3B FD                        cmp r15d, r13d
00C5CD59  0F 85 52 01 00 00               jne 0x140c5ceb1
00C5CD5F  EB 04                           jmp 0x140c5cd65
00C5CD61  41 83 CD FF                     or r13d, 0xffffffff
00C5CD65  4C 8D 05 34 55 02 00            lea r8, [rip + 0x25534]
00C5CD6C  49 8B D4                        mov rdx, r12
00C5CD6F  48 8B CF                        mov rcx, rdi
00C5CD72  E8 A5 80 BE FF                  call 0x140844e1c
00C5CD77  44 8B F0                        mov r14d, eax
00C5CD7A  41 3B C5                        cmp eax, r13d
00C5CD7D  0F 84 D0 01 00 00               je 0x140c5cf53
00C5CD83  F6 87 8C 00 00 00 01            test byte ptr [rdi + 0x8c], 1
00C5CD8A  4C 8D 45 78                     lea r8, [rbp + 0x78]
00C5CD8E  8B D0                           mov edx, eax
00C5CD90  48 8B CF                        mov rcx, rdi
00C5CD93  74 07                           je 0x140c5cd9c
00C5CD95  E8 C6 7E BF FF                  call 0x140854c60
00C5CD9A  EB 05                           jmp 0x140c5cda1
00C5CD9C  E8 0F 7F BF FF                  call 0x140854cb0
00C5CDA1  48 85 C0                        test rax, rax
00C5CDA4  0F 84 A9 01 00 00               je 0x140c5cf53
00C5CDAA  48 8D 4D E0                     lea rcx, [rbp - 0x20]
00C5CDAE  4C 8B C0                        mov r8, rax
00C5CDB1  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00C5CDB6  4C 8D 4D 58                     lea r9, [rbp + 0x58]
00C5CDBA  48 8B CF                        mov rcx, rdi
00C5CDBD  41 8B D6                        mov edx, r14d
00C5CDC0  E8 6F 6B B9 FF                  call 0x1407f3934
00C5CDC5  F6 87 8C 00 00 00 01            test byte ptr [rdi + 0x8c], 1
00C5CDCC  48 8D 55 78                     lea rdx, [rbp + 0x78]
00C5CDD0  4C 8B F0                        mov r14, rax
00C5CDD3  48 8B CF                        mov rcx, rdi
00C5CDD6  74 07                           je 0x140c5cddf
00C5CDD8  E8 43 FE BF FF                  call 0x14085cc20
00C5CDDD  EB 05                           jmp 0x140c5cde4
00C5CDDF  E8 5C 91 BF FF                  call 0x140855f40
00C5CDE4  4D 85 F6                        test r14, r14
00C5CDE7  0F 84 66 01 00 00               je 0x140c5cf53
00C5CDED  41 8B 06                        mov eax, dword ptr [r14]
00C5CDF0  48 8D 55 E0                     lea rdx, [rbp - 0x20]
00C5CDF4  A8 0B                           test al, 0xb
00C5CDF6  4C 8D 35 43 54 02 00            lea r14, [rip + 0x25443]
00C5CDFD  48 8D 05 BC 54 02 00            lea rax, [rip + 0x254bc]
00C5CE04  48 8B CF                        mov rcx, rdi
00C5CE07  4C 0F 44 F0                     cmove r14, rax
00C5CE0B  F6 87 8C 00 00 00 01            test byte ptr [rdi + 0x8c], 1
00C5CE12  74 07                           je 0x140c5ce1b
00C5CE14  E8 07 FE BF FF                  call 0x14085cc20
00C5CE19  EB 05                           jmp 0x140c5ce20
00C5CE1B  E8 20 91 BF FF                  call 0x140855f40
00C5CE20  48 8B 55 70                     mov rdx, qword ptr [rbp + 0x70]
00C5CE24  4D 8B C6                        mov r8, r14
00C5CE27  48 8B CE                        mov rcx, rsi
00C5CE2A  E8 29 CF DE FF                  call 0x140a49d58
00C5CE2F  8B D0                           mov edx, eax
00C5CE31  41 3B C5                        cmp eax, r13d
00C5CE34  74 5A                           je 0x140c5ce90
00C5CE36  F6 86 8C 00 00 00 01            test byte ptr [rsi + 0x8c], 1
00C5CE3D  4C 8D 45 40                     lea r8, [rbp + 0x40]
00C5CE41  48 8B CE                        mov rcx, rsi
00C5CE44  74 07                           je 0x140c5ce4d
00C5CE46  E8 15 7E BF FF                  call 0x140854c60
00C5CE4B  EB 05                           jmp 0x140c5ce52
00C5CE4D  E8 5E 7E BF FF                  call 0x140854cb0
00C5CE52  48 85 C0                        test rax, rax
00C5CE55  74 39                           je 0x140c5ce90
00C5CE57  4C 8D 05 4A 53 02 00            lea r8, [rip + 0x2534a]
00C5CE5E  48 8B D0                        mov rdx, rax
00C5CE61  48 8B CE                        mov rcx, rsi
00C5CE64  4C 8B F6                        mov r14, rsi
00C5CE67  E8 B0 7F BE FF                  call 0x140844e1c
00C5CE6C  F6 86 8C 00 00 00 01            test byte ptr [rsi + 0x8c], 1
00C5CE73  48 8D 55 40                     lea rdx, [rbp + 0x40]
00C5CE77  44 8B F8                        mov r15d, eax
00C5CE7A  48 8B CE                        mov rcx, rsi
00C5CE7D  74 07                           je 0x140c5ce86
00C5CE7F  E8 9C FD BF FF                  call 0x14085cc20
00C5CE84  EB 05                           jmp 0x140c5ce8b
00C5CE86  E8 B5 90 BF FF                  call 0x140855f40
00C5CE8B  45 3B FD                        cmp r15d, r13d
00C5CE8E  75 21                           jne 0x140c5ceb1
00C5CE90  4C 8D 05 11 53 02 00            lea r8, [rip + 0x25311]
00C5CE97  49 8B D4                        mov rdx, r12
00C5CE9A  48 8B CF                        mov rcx, rdi
00C5CE9D  4C 8B F7                        mov r14, rdi
00C5CEA0  E8 77 7F BE FF                  call 0x140844e1c
00C5CEA5  44 8B F8                        mov r15d, eax
00C5CEA8  41 3B C5                        cmp eax, r13d
00C5CEAB  0F 84 A2 00 00 00               je 0x140c5cf53
00C5CEB1  41 F6 86 8C 00 00 00 01         test byte ptr [r14 + 0x8c], 1
00C5CEB9  4C 8D 85 80 00 00 00            lea r8, [rbp + 0x80]
00C5CEC0  41 8B D7                        mov edx, r15d
00C5CEC3  49 8B CE                        mov rcx, r14
00C5CEC6  74 07                           je 0x140c5cecf
00C5CEC8  E8 93 7D BF FF                  call 0x140854c60
00C5CECD  EB 05                           jmp 0x140c5ced4
00C5CECF  E8 DC 7D BF FF                  call 0x140854cb0
00C5CED4  48 85 C0                        test rax, rax
00C5CED7  74 7A                           je 0x140c5cf53
00C5CED9  48 8D 4D 60                     lea rcx, [rbp + 0x60]
00C5CEDD  4C 8B C0                        mov r8, rax
00C5CEE0  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00C5CEE5  4C 8D 4D 58                     lea r9, [rbp + 0x58]
00C5CEE9  49 8B CE                        mov rcx, r14
00C5CEEC  41 8B D7                        mov edx, r15d
00C5CEEF  E8 40 6A B9 FF                  call 0x1407f3934
00C5CEF4  41 F6 86 8C 00 00 00 01         test byte ptr [r14 + 0x8c], 1
00C5CEFC  48 8D 95 80 00 00 00            lea rdx, [rbp + 0x80]
00C5CF03  48 8B F0                        mov rsi, rax
00C5CF06  49 8B CE                        mov rcx, r14
00C5CF09  74 07                           je 0x140c5cf12
00C5CF0B  E8 10 FD BF FF                  call 0x14085cc20
00C5CF10  EB 05                           jmp 0x140c5cf17
00C5CF12  E8 29 90 BF FF                  call 0x140855f40
00C5CF17  48 85 F6                        test rsi, rsi
00C5CF1A  74 37                           je 0x140c5cf53
00C5CF1C  83 3E 01                        cmp dword ptr [rsi], 1
00C5CF1F  48 8D 55 60                     lea rdx, [rbp + 0x60]
00C5CF23  41 8A 86 8C 00 00 00            mov al, byte ptr [r14 + 0x8c]
00C5CF2A  49 8B CE                        mov rcx, r14
00C5CF2D  75 14                           jne 0x140c5cf43
00C5CF2F  A8 01                           test al, 1
00C5CF31  74 07                           je 0x140c5cf3a
00C5CF33  E8 E8 FC BF FF                  call 0x14085cc20
00C5CF38  EB 05                           jmp 0x140c5cf3f
00C5CF3A  E8 01 90 BF FF                  call 0x140855f40
00C5CF3F  B3 01                           mov bl, 1
00C5CF41  EB 10                           jmp 0x140c5cf53
00C5CF43  A8 01                           test al, 1
00C5CF45  74 07                           je 0x140c5cf4e
00C5CF47  E8 D4 FC BF FF                  call 0x14085cc20
00C5CF4C  EB 05                           jmp 0x140c5cf53
00C5CF4E  E8 ED 8F BF FF                  call 0x140855f40
00C5CF53  F6 87 8C 00 00 00 01            test byte ptr [rdi + 0x8c], 1
00C5CF5A  48 8D 95 88 00 00 00            lea rdx, [rbp + 0x88]
00C5CF61  48 8B CF                        mov rcx, rdi
00C5CF64  74 07                           je 0x140c5cf6d
00C5CF66  E8 B5 FC BF FF                  call 0x14085cc20
00C5CF6B  EB 05                           jmp 0x140c5cf72
00C5CF6D  E8 CE 8F BF FF                  call 0x140855f40
00C5CF72  8A C3                           mov al, bl
00C5CF74  48 8B 9C 24 98 00 00 00         mov rbx, qword ptr [rsp + 0x98]
00C5CF7C  48 83 C4 50                     add rsp, 0x50
00C5CF80  41 5F                           pop r15
00C5CF82  41 5E                           pop r14
00C5CF84  41 5D                           pop r13
00C5CF86  41 5C                           pop r12
00C5CF88  5F                              pop rdi
00C5CF89  5E                              pop rsi
00C5CF8A  5D                              pop rbp
00C5CF8B  C3                              ret
00C5CF8C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpIsLoadType(__int64 a1, __int64 a2, int a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m50;
    unsigned int v_stack_m54;
    unsigned int v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p28;
    unsigned int v_stack_p2C;
    unsigned int v_stack_p40;
    unsigned int v_stack_p44;
    unsigned int v_stack_p48;
    unsigned int v_stack_p4C;
    unsigned int v_stack_p50;
    unsigned int v_stack_p54;
    unsigned int v_stack_p8;
    unsigned int v_stack_pC;

    v_stack_p10 = v_rbx;
    v_stack_p20 = a4;
    v_stack_p18 = a3;
    v_rsp = (v_rsp) - (80);
    v_rbx = 0;
    v_r13 = (unsigned int)((v_r13) | (0xFFFFFFFFULL));
    v_stack_p2C = 0;
    v_stack_p28 = (unsigned int)(v_r13);
    v_stack_p50 = (unsigned int)(v_r13);
    v_stack_p54 = 0;
    v_stack_p20 = 0;
    v_stack_p8 = (unsigned int)(v_r13);
    v_stack_pC = 0;
    v_stack_m58 = (unsigned int)(v_r13);
    v_stack_m54 = 0;
    v_stack_p40 = (unsigned int)(v_r13);
    v_stack_p44 = 0;
    v_stack_m50 = v_xmm0;
    v_stack_p48 = (unsigned int)(v_r13);
    v_stack_p4C = 0;
    v_stack_p18 = 0;
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_00C5CC83;
    result = HvpGetCellFlat(a1, a2, a10, a4);
    goto loc_00C5CC88;
loc_00C5CC83:
    result = HvpGetCellPaged(a1, a2, a10, a4);
loc_00C5CC88:
    if (result == 0) goto loc_00C5CF74;
    if (a6 == 0) goto loc_00C5CE90;
    if (a7 == 0) goto loc_00C5CE90;
    result = CmpGetNodeName(a1, result, v_stack_p18, a4);
    if (result == 0) goto loc_00C5CD61;
    result = RtlInitUnicodeStringEx(v_stack_m50, result, v_stack_p18, a4);
    if (sign_flag) goto loc_00C5CD42;
    result = CmpFindSubKeyByName(a6, a7, v_stack_m50, a4);
    if (((unsigned int)(result)) == -1) goto loc_00C5CD42;
    if (((*(unsigned __int8 *)(a6 + 140)) & (1)) == 0) goto loc_00C5CD04;
    result = HvpGetCellFlat(a6, (unsigned int)((unsigned int)(result)), v_stack_p8, a4);
    goto loc_00C5CD09;
loc_00C5CD04:
    result = HvpGetCellPaged(a6, (unsigned int)((unsigned int)(result)), v_stack_p8, a4);
loc_00C5CD09:
    if (result == 0) goto loc_00C5CD42;
    result = CmpFindValueByName(a6, result, v_rip + 152723, a4);
    if (((*(unsigned __int8 *)(a6 + 140)) & (1)) == 0) goto loc_00C5CD3D;
    result = HvpReleaseCellFlat(a6, v_stack_p8, v_rip + 152723, a4);
    goto loc_00C5CD42;
loc_00C5CD3D:
    result = HvpReleaseCellPaged(a6, v_stack_p8, v_rip + 152723, a4);
loc_00C5CD42:
    result = guard_dispatch_icall(result, v_stack_p18, v_rip + 152723, a4);
    v_r13 = (unsigned int)((result) | (0xFFFFFFFFULL));
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != ((unsigned int)(v_r13))) goto loc_00C5CEB1;
    goto loc_00C5CD65;
loc_00C5CD61:
    v_r13 = (unsigned int)((v_r13) | (0xFFFFFFFFULL));
loc_00C5CD65:
    result = CmpFindValueByName(a1, result, v_rip + 152884, a4);
    if (((unsigned int)(result)) == ((unsigned int)(v_r13))) goto loc_00C5CF53;
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_00C5CD9C;
    result = HvpGetCellFlat(a1, (unsigned int)((unsigned int)(result)), a8, a4);
    goto loc_00C5CDA1;
loc_00C5CD9C:
    result = HvpGetCellPaged(a1, (unsigned int)((unsigned int)(result)), a8, a4);
loc_00C5CDA1:
    if (result == 0) goto loc_00C5CF53;
    v_stack_m68 = v_stack_m58;
    result = CmpValueToData(a1, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), result, v_stack_p20);
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_00C5CDDF;
    result = HvpReleaseCellFlat(a1, a8, result, v_stack_p20);
    goto loc_00C5CDE4;
loc_00C5CDDF:
    result = HvpReleaseCellPaged(a1, a8, result, v_stack_p20);
loc_00C5CDE4:
    if (result == 0) goto loc_00C5CF53;
    v_r14 = v_rip + 152643;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result)))) & (11)) == 0) { v_r14 = v_rip + 152764; }
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_00C5CE1B;
    result = HvpReleaseCellFlat(a1, v_stack_m58, result, v_stack_p20);
    goto loc_00C5CE20;
loc_00C5CE1B:
    result = HvpReleaseCellPaged(a1, v_stack_m58, result, v_stack_p20);
loc_00C5CE20:
    result = CmpFindSubKeyByName(a6, a7, v_r14, v_stack_p20);
    if (((unsigned int)(result)) == ((unsigned int)(v_r13))) goto loc_00C5CE90;
    if (((*(unsigned __int8 *)(a6 + 140)) & (1)) == 0) goto loc_00C5CE4D;
    result = HvpGetCellFlat(a6, (unsigned int)((unsigned int)(result)), v_stack_p8, v_stack_p20);
    goto loc_00C5CE52;
loc_00C5CE4D:
    result = HvpGetCellPaged(a6, (unsigned int)((unsigned int)(result)), v_stack_p8, v_stack_p20);
loc_00C5CE52:
    if (result == 0) goto loc_00C5CE90;
    result = CmpFindValueByName(a6, result, v_rip + 152394, v_stack_p20);
    if (((*(unsigned __int8 *)(a6 + 140)) & (1)) == 0) goto loc_00C5CE86;
    result = HvpReleaseCellFlat(a6, v_stack_p8, v_rip + 152394, v_stack_p20);
    goto loc_00C5CE8B;
loc_00C5CE86:
    result = HvpReleaseCellPaged(a6, v_stack_p8, v_rip + 152394, v_stack_p20);
loc_00C5CE8B:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != ((unsigned int)(v_r13))) goto loc_00C5CEB1;
loc_00C5CE90:
    result = CmpFindValueByName(a1, result, v_rip + 152337, v_stack_p20);
    if (((unsigned int)(result)) == ((unsigned int)(v_r13))) goto loc_00C5CF53;
loc_00C5CEB1:
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_00C5CECF;
    result = HvpGetCellFlat(a1, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), a9, v_stack_p20);
    goto loc_00C5CED4;
loc_00C5CECF:
    result = HvpGetCellPaged(a1, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), a9, v_stack_p20);
loc_00C5CED4:
    if (result == 0) goto loc_00C5CF53;
    v_stack_m68 = a5;
    result = CmpValueToData(a1, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), result, v_stack_p20);
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_00C5CF12;
    result = HvpReleaseCellFlat(a1, a9, result, v_stack_p20);
    goto loc_00C5CF17;
loc_00C5CF12:
    result = HvpReleaseCellPaged(a1, a9, result, v_stack_p20);
loc_00C5CF17:
    if (result == 0) goto loc_00C5CF53;
    if ((*(unsigned int *)(result)) != 1) goto loc_00C5CF43;
    if ((((unsigned __int8)(*(unsigned __int8 *)(a1 + 140))) & (1)) == 0) goto loc_00C5CF3A;
    result = HvpReleaseCellFlat(a1, a5, result, v_stack_p20);
    goto loc_00C5CF3F;
loc_00C5CF3A:
    result = HvpReleaseCellPaged(a1, a5, result, v_stack_p20);
loc_00C5CF3F:
    goto loc_00C5CF53;
loc_00C5CF43:
    if ((((unsigned __int8)(result)) & (1)) == 0) goto loc_00C5CF4E;
    result = HvpReleaseCellFlat(a1, a5, result, v_stack_p20);
    goto loc_00C5CF53;
loc_00C5CF4E:
    result = HvpReleaseCellPaged(a1, a5, result, v_stack_p20);
loc_00C5CF53:
    if (((*(unsigned __int8 *)(a1 + 140)) & (1)) == 0) goto loc_00C5CF6D;
    result = HvpReleaseCellFlat(a1, a10, result, v_stack_p20);
    goto loc_00C5CF72;
loc_00C5CF6D:
    result = HvpReleaseCellPaged(a1, a10, result, v_stack_p20);
loc_00C5CF72:
loc_00C5CF74:
    v_rsp = (v_rsp) + (80);
    return 1;
}
```

## 5. (Beta) C Style

```c
int64_t CmpIsLoadType(void *Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4, int64_t Arg5, int64_t Arg6, int64_t Arg7, int64_t Arg8, int64_t Arg9, int64_t Arg10)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m50;
    uint32_t v_stack_m54;
    uint32_t v_stack_m58;
    uint64_t v_stack_m68;
    uint64_t v_stack_p10;
    uint32_t v_stack_p18;
    uint64_t v_stack_p20;
    uint32_t v_stack_p28;
    uint32_t v_stack_p2C;
    uint32_t v_stack_p40;
    uint32_t v_stack_p44;
    uint32_t v_stack_p48;
    uint32_t v_stack_p4C;
    uint32_t v_stack_p50;
    uint32_t v_stack_p54;
    uint32_t v_stack_p8;
    uint32_t v_stack_pC;

    v_stack_p10 = local_rbx;
    v_stack_p20 = Arg4;
    v_stack_p18 = Arg3;
    local_rsp = (local_rsp) - (80);
    local_rbx = 0;
    local_r13 = (uint32_t)((local_r13) | (0xFFFFFFFFULL));
    v_stack_p2C = 0;
    v_stack_p28 = (uint32_t)(local_r13);
    v_stack_p50 = (uint32_t)(local_r13);
    v_stack_p54 = 0;
    v_stack_p20 = 0;
    v_stack_p8 = (uint32_t)(local_r13);
    v_stack_pC = 0;
    v_stack_m58 = (uint32_t)(local_r13);
    v_stack_m54 = 0;
    v_stack_p40 = (uint32_t)(local_r13);
    v_stack_p44 = 0;
    v_stack_m50 = v_xmm0;
    v_stack_p48 = (uint32_t)(local_r13);
    v_stack_p4C = 0;
    v_stack_p18 = 0;
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_00C5CC83;
    result = HvpGetCellFlat(Arg1, Arg2, Arg10, Arg4);
    goto loc_00C5CC88;
loc_00C5CC83:
    result = HvpGetCellPaged(Arg1, Arg2, Arg10, Arg4);
loc_00C5CC88:
    if (result == 0) goto loc_00C5CF74;
    if (Arg6 == 0) goto loc_00C5CE90;
    if (Arg7 == 0) goto loc_00C5CE90;
    result = CmpGetNodeName(Arg1, result, v_stack_p18, Arg4);
    if (result == 0) goto loc_00C5CD61;
    result = RtlInitUnicodeStringEx(v_stack_m50, result, v_stack_p18, Arg4);
    if (sign_flag) goto loc_00C5CD42;
    result = CmpFindSubKeyByName(Arg6, Arg7, v_stack_m50, Arg4);
    if (((uint32_t)(result)) == -1) goto loc_00C5CD42;
    if (((*(uint8_t *)(Arg6 + 0x8C)) & (1)) == 0) goto loc_00C5CD04;
    result = HvpGetCellFlat(Arg6, (uint32_t)((uint32_t)(result)), v_stack_p8, Arg4);
    goto loc_00C5CD09;
loc_00C5CD04:
    result = HvpGetCellPaged(Arg6, (uint32_t)((uint32_t)(result)), v_stack_p8, Arg4);
loc_00C5CD09:
    if (result == 0) goto loc_00C5CD42;
    result = CmpFindValueByName(Arg6, result, v_rip + 152723, Arg4);
    if (((*(uint8_t *)(Arg6 + 0x8C)) & (1)) == 0) goto loc_00C5CD3D;
    result = HvpReleaseCellFlat(Arg6, v_stack_p8, v_rip + 152723, Arg4);
    goto loc_00C5CD42;
loc_00C5CD3D:
    result = HvpReleaseCellPaged(Arg6, v_stack_p8, v_rip + 152723, Arg4);
loc_00C5CD42:
    result = guard_dispatch_icall(result, v_stack_p18, v_rip + 152723, Arg4);
    local_r13 = (uint32_t)((result) | (0xFFFFFFFFULL));
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != ((uint32_t)(local_r13))) goto loc_00C5CEB1;
    goto loc_00C5CD65;
loc_00C5CD61:
    local_r13 = (uint32_t)((local_r13) | (0xFFFFFFFFULL));
loc_00C5CD65:
    result = CmpFindValueByName(Arg1, result, v_rip + 152884, Arg4);
    if (((uint32_t)(result)) == ((uint32_t)(local_r13))) goto loc_00C5CF53;
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_00C5CD9C;
    result = HvpGetCellFlat(Arg1, (uint32_t)((uint32_t)(result)), Arg8, Arg4);
    goto loc_00C5CDA1;
loc_00C5CD9C:
    result = HvpGetCellPaged(Arg1, (uint32_t)((uint32_t)(result)), Arg8, Arg4);
loc_00C5CDA1:
    if (result == 0) goto loc_00C5CF53;
    v_stack_m68 = v_stack_m58;
    result = CmpValueToData(Arg1, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), result, v_stack_p20);
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_00C5CDDF;
    result = HvpReleaseCellFlat(Arg1, Arg8, result, v_stack_p20);
    goto loc_00C5CDE4;
loc_00C5CDDF:
    result = HvpReleaseCellPaged(Arg1, Arg8, result, v_stack_p20);
loc_00C5CDE4:
    if (result == 0) goto loc_00C5CF53;
    local_r14 = v_rip + 152643;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result)))) & (11)) == 0) { local_r14 = v_rip + 152764; }
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_00C5CE1B;
    result = HvpReleaseCellFlat(Arg1, v_stack_m58, result, v_stack_p20);
    goto loc_00C5CE20;
loc_00C5CE1B:
    result = HvpReleaseCellPaged(Arg1, v_stack_m58, result, v_stack_p20);
loc_00C5CE20:
    result = CmpFindSubKeyByName(Arg6, Arg7, local_r14, v_stack_p20);
    if (((uint32_t)(result)) == ((uint32_t)(local_r13))) goto loc_00C5CE90;
    if (((*(uint8_t *)(Arg6 + 0x8C)) & (1)) == 0) goto loc_00C5CE4D;
    result = HvpGetCellFlat(Arg6, (uint32_t)((uint32_t)(result)), v_stack_p8, v_stack_p20);
    goto loc_00C5CE52;
loc_00C5CE4D:
    result = HvpGetCellPaged(Arg6, (uint32_t)((uint32_t)(result)), v_stack_p8, v_stack_p20);
loc_00C5CE52:
    if (result == 0) goto loc_00C5CE90;
    result = CmpFindValueByName(Arg6, result, v_rip + 152394, v_stack_p20);
    if (((*(uint8_t *)(Arg6 + 0x8C)) & (1)) == 0) goto loc_00C5CE86;
    result = HvpReleaseCellFlat(Arg6, v_stack_p8, v_rip + 152394, v_stack_p20);
    goto loc_00C5CE8B;
loc_00C5CE86:
    result = HvpReleaseCellPaged(Arg6, v_stack_p8, v_rip + 152394, v_stack_p20);
loc_00C5CE8B:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != ((uint32_t)(local_r13))) goto loc_00C5CEB1;
loc_00C5CE90:
    result = CmpFindValueByName(Arg1, result, v_rip + 152337, v_stack_p20);
    if (((uint32_t)(result)) == ((uint32_t)(local_r13))) goto loc_00C5CF53;
loc_00C5CEB1:
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_00C5CECF;
    result = HvpGetCellFlat(Arg1, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), Arg9, v_stack_p20);
    goto loc_00C5CED4;
loc_00C5CECF:
    result = HvpGetCellPaged(Arg1, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), Arg9, v_stack_p20);
loc_00C5CED4:
    if (result == 0) goto loc_00C5CF53;
    v_stack_m68 = Arg5;
    result = CmpValueToData(Arg1, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), result, v_stack_p20);
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_00C5CF12;
    result = HvpReleaseCellFlat(Arg1, Arg9, result, v_stack_p20);
    goto loc_00C5CF17;
loc_00C5CF12:
    result = HvpReleaseCellPaged(Arg1, Arg9, result, v_stack_p20);
loc_00C5CF17:
    if (result == 0) goto loc_00C5CF53;
    if ((*(uint32_t *)(result)) != 1) goto loc_00C5CF43;
    if ((((uint8_t)(*(uint8_t *)(arg1 + 0x8C))) & (1)) == 0) goto loc_00C5CF3A;
    result = HvpReleaseCellFlat(Arg1, Arg5, result, v_stack_p20);
    goto loc_00C5CF3F;
loc_00C5CF3A:
    result = HvpReleaseCellPaged(Arg1, Arg5, result, v_stack_p20);
loc_00C5CF3F:
    goto loc_00C5CF53;
loc_00C5CF43:
    if ((((uint8_t)(result)) & (1)) == 0) goto loc_00C5CF4E;
    result = HvpReleaseCellFlat(Arg1, Arg5, result, v_stack_p20);
    goto loc_00C5CF53;
loc_00C5CF4E:
    result = HvpReleaseCellPaged(Arg1, Arg5, result, v_stack_p20);
loc_00C5CF53:
    if (((*(uint8_t *)(arg1 + 0x8C)) & (1)) == 0) goto loc_00C5CF6D;
    result = HvpReleaseCellFlat(Arg1, Arg10, result, v_stack_p20);
    goto loc_00C5CF72;
loc_00C5CF6D:
    result = HvpReleaseCellPaged(Arg1, Arg10, result, v_stack_p20);
loc_00C5CF72:
loc_00C5CF74:
    local_rsp = (local_rsp) + (80);
    return 1;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x8C` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C5CBF8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
