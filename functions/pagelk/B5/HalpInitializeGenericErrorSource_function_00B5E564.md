# HalpInitializeGenericErrorSource

- RVA: `0x00B5E564`–`0x00B5E8D2` (길이 `878` bytes)
- VA: `0x0000000140B5E564`
- 실행 섹션: `PAGELK`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C4570`
- 디코드: `208`개 명령, `878/878` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **15**; 고유 호출 대상: **7**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **38**

### Outgoing calls
- `0x00B5E684` → [HalpInitGenericErrorSourceEntry](HalpInitGenericErrorSourceEntry_function_00B5DF68.md) (function, `0x00B5DF68`)
- `0x00B5E68B` → [HalpInitGenericErrorSourceEntryV2](HalpInitGenericErrorSourceEntryV2_function_00B5E1D0.md) (function, `0x00B5E1D0`)
- `0x00B5E6B1` → [HalpRegisterPeiErrorSource](../../text/55/HalpRegisterPeiErrorSource_function_00555BD8.md) (function, `0x00555BD8`)
- `0x00B5E6F3` → [HalpInitGenericErrorSourceEntry](HalpInitGenericErrorSourceEntry_function_00B5DF68.md) (function, `0x00B5DF68`)
- `0x00B5E6FA` → [HalpInitGenericErrorSourceEntryV2](HalpInitGenericErrorSourceEntryV2_function_00B5E1D0.md) (function, `0x00B5E1D0`)
- `0x00B5E757` → [HalpInitGenericErrorSourceEntry](HalpInitGenericErrorSourceEntry_function_00B5DF68.md) (function, `0x00B5DF68`)
- `0x00B5E75E` → [HalpInitGenericErrorSourceEntryV2](HalpInitGenericErrorSourceEntryV2_function_00B5E1D0.md) (function, `0x00B5E1D0`)
- `0x00B5E7B4` → [HalpInitGenericErrorSourceEntry](HalpInitGenericErrorSourceEntry_function_00B5DF68.md) (function, `0x00B5DF68`)
- `0x00B5E7BB` → [HalpInitGenericErrorSourceEntryV2](HalpInitGenericErrorSourceEntryV2_function_00B5E1D0.md) (function, `0x00B5E1D0`)
- `0x00B5E7DC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00B5E7F7` → [MmMapIoSpaceEx](../../text/32/MmMapIoSpaceEx_function_00327830.md) (function, `0x00327830`)
- `0x00B5E853` → [HalpInitGenericErrorSourceEntry](HalpInitGenericErrorSourceEntry_function_00B5DF68.md) (function, `0x00B5DF68`)
- `0x00B5E85A` → [HalpInitGenericErrorSourceEntryV2](HalpInitGenericErrorSourceEntryV2_function_00B5E1D0.md) (function, `0x00B5E1D0`)
- `0x00B5E8AB` → [HalpInitGenericErrorSourcePollingRoutine](HalpInitGenericErrorSourcePollingRoutine_function_00B5E498.md) (function, `0x00B5E498`)
- `0x00B5E8B3` → [HalpGenInitialRead](HalpGenInitialRead_function_00B5DED4.md) (function, `0x00B5DED4`)

### Direct callers
- [HalpInitializeErrSrc](HalpInitializeErrSrc_function_00B5BBB0.md) at `0x00B5BBDC`

### Static image references
- `0x00B5E590` → RVA `0x00E1041C` (`.data`; read)
- `0x00B5E597` → RVA `0x00FC1550` (`.data`; read)
- `0x00B5E5A4` → RVA `0x00FC1570` (`.data`; read)
- `0x00B5E5AB` → RVA `0x00FC1680` (`.data`; read)
- `0x00B5E5B2` → RVA `0x00FC1540` (`.data`; read)
- `0x00B5E5B9` → RVA `0x00FC1560` (`.data`; read)
- `0x00B5E5C2` → RVA `0x00FC16A0` (`.data`; read)
- `0x00B5E5C9` → RVA `0x00E1041C` (`.data`; write)
- `0x00B5E5D0` → RVA `0x00FC16A8` (`.data`; write)
- `0x00B5E5D7` → RVA `0x00FC16A0` (`.data`; write)
- `0x00B5E5DE` → RVA `0x00FC1690` (`.data`; read)
- `0x00B5E5E5` → RVA `0x00FC1698` (`.data`; write)
- `0x00B5E5EC` → RVA `0x00FC1690` (`.data`; write)
- `0x00B5E5F3` → RVA `0x00FC1558` (`.data`; write)
- `0x00B5E5FA` → RVA `0x00FC1550` (`.data`; write)
- `0x00B5E601` → RVA `0x00FC1578` (`.data`; write)
- `0x00B5E608` → RVA `0x00FC1570` (`.data`; write)
- `0x00B5E60F` → RVA `0x00FC1688` (`.data`; write)
- `0x00B5E616` → RVA `0x00FC1680` (`.data`; write)
- `0x00B5E61D` → RVA `0x00FC1548` (`.data`; write)
- `0x00B5E624` → RVA `0x00FC1540` (`.data`; write)
- `0x00B5E62B` → RVA `0x00FC1568` (`.data`; write)
- `0x00B5E632` → RVA `0x00FC1560` (`.data`; write)
- `0x00B5E690` → RVA `0x00E10410` (`.data`; read)
- `0x00B5E69B` → RVA `0x00E10410` (`.data`; write)
- `0x00B5E6C0` → RVA `0x00FC1558` (`.data`; read)
- `0x00B5E705` → RVA `0x00FC1568` (`.data`; read)
- `0x00B5E731` → RVA `0x00E10414` (`.data`; read)
- `0x00B5E73E` → RVA `0x00E10414` (`.data`; write)
- `0x00B5E769` → RVA `0x00FC1548` (`.data`; read)
- `0x00B5E78E` → RVA `0x00E10420` (`.data`; read)
- `0x00B5E79B` → RVA `0x00E10420` (`.data`; write)
- `0x00B5E805` → RVA `0x00FC1688` (`.data`; read)
- `0x00B5E829` → RVA `0x00E1040C` (`.data`; read)
- `0x00B5E832` → RVA `0x00E1040C` (`.data`; write)
- `0x00B5E877` → RVA `0x00FC1578` (`.data`; read)
- `0x00B5E88A` → RVA `0x00E10418` (`.data`; read)
- `0x00B5E8A4` → RVA `0x00E10418` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00B5E6B1` → [HalpRegisterPeiErrorSource](../../text/55/HalpRegisterPeiErrorSource_function_00555BD8.md) (`PAGELK` → `.text`)
  - `0x00B5E7DC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGELK` → `POOLCODE`)
  - `0x00B5E7F7` → [MmMapIoSpaceEx](../../text/32/MmMapIoSpaceEx_function_00327830.md) (`PAGELK` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B5E564  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00B5E569  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
00B5E56E  55                              push rbp
00B5E56F  57                              push rdi
00B5E570  41 54                           push r12
00B5E572  41 55                           push r13
00B5E574  41 57                           push r15
00B5E576  48 8B EC                        mov rbp, rsp
00B5E579  48 83 EC 20                     sub rsp, 0x20
00B5E57D  48 83 65 40 00                  and qword ptr [rbp + 0x40], 0
00B5E582  48 8B FA                        mov rdi, rdx
00B5E585  85 C9                           test ecx, ecx
00B5E587  75 07                           jne 0x140b5e590
00B5E589  33 C0                           xor eax, eax
00B5E58B  E9 2A 03 00 00                  jmp 0x140b5e8ba
00B5E590  83 3D 85 1E 2B 00 00            cmp dword ptr [rip + 0x2b1e85], 0
00B5E597  4C 8D 2D B2 2F 46 00            lea r13, [rip + 0x462fb2]
00B5E59E  41 BF 01 00 00 00               mov r15d, 1
00B5E5A4  48 8D 35 C5 2F 46 00            lea rsi, [rip + 0x462fc5]
00B5E5AB  48 8D 15 CE 30 46 00            lea rdx, [rip + 0x4630ce]
00B5E5B2  4C 8D 25 87 2F 46 00            lea r12, [rip + 0x462f87]
00B5E5B9  48 8D 0D A0 2F 46 00            lea rcx, [rip + 0x462fa0]
00B5E5C0  75 77                           jne 0x140b5e639
00B5E5C2  48 8D 05 D7 30 46 00            lea rax, [rip + 0x4630d7]
00B5E5C9  44 89 3D 4C 1E 2B 00            mov dword ptr [rip + 0x2b1e4c], r15d
00B5E5D0  48 89 05 D1 30 46 00            mov qword ptr [rip + 0x4630d1], rax
00B5E5D7  48 89 05 C2 30 46 00            mov qword ptr [rip + 0x4630c2], rax
00B5E5DE  48 8D 05 AB 30 46 00            lea rax, [rip + 0x4630ab]
00B5E5E5  48 89 05 AC 30 46 00            mov qword ptr [rip + 0x4630ac], rax
00B5E5EC  48 89 05 9D 30 46 00            mov qword ptr [rip + 0x46309d], rax
00B5E5F3  4C 89 2D 5E 2F 46 00            mov qword ptr [rip + 0x462f5e], r13
00B5E5FA  4C 89 2D 4F 2F 46 00            mov qword ptr [rip + 0x462f4f], r13
00B5E601  48 89 35 70 2F 46 00            mov qword ptr [rip + 0x462f70], rsi
00B5E608  48 89 35 61 2F 46 00            mov qword ptr [rip + 0x462f61], rsi
00B5E60F  48 89 15 72 30 46 00            mov qword ptr [rip + 0x463072], rdx
00B5E616  48 89 15 63 30 46 00            mov qword ptr [rip + 0x463063], rdx
00B5E61D  4C 89 25 24 2F 46 00            mov qword ptr [rip + 0x462f24], r12
00B5E624  4C 89 25 15 2F 46 00            mov qword ptr [rip + 0x462f15], r12
00B5E62B  48 89 0D 36 2F 46 00            mov qword ptr [rip + 0x462f36], rcx
00B5E632  48 89 0D 27 2F 46 00            mov qword ptr [rip + 0x462f27], rcx
00B5E639  0F B6 4F 40                     movzx ecx, byte ptr [rdi + 0x40]
00B5E63D  85 C9                           test ecx, ecx
00B5E63F  0F 84 01 02 00 00               je 0x140b5e846
00B5E645  41 2B CF                        sub ecx, r15d
00B5E648  0F 84 F1 01 00 00               je 0x140b5e83f
00B5E64E  41 2B CF                        sub ecx, r15d
00B5E651  0F 84 E8 01 00 00               je 0x140b5e83f
00B5E657  83 E9 02                        sub ecx, 2
00B5E65A  0F 84 47 01 00 00               je 0x140b5e7a7
00B5E660  83 E9 04                        sub ecx, 4
00B5E663  0F 84 E1 00 00 00               je 0x140b5e74a
00B5E669  41 2B CF                        sub ecx, r15d
00B5E66C  74 78                           je 0x140b5e6e6
00B5E66E  41 3B CF                        cmp ecx, r15d
00B5E671  0F 85 C8 01 00 00               jne 0x140b5e83f
00B5E677  83 7F 08 0C                     cmp dword ptr [rdi + 8], 0xc
00B5E67B  48 8D 55 40                     lea rdx, [rbp + 0x40]
00B5E67F  48 8B CF                        mov rcx, rdi
00B5E682  74 07                           je 0x140b5e68b
00B5E684  E8 DF F8 FF FF                  call 0x140b5df68
00B5E689  EB 05                           jmp 0x140b5e690
00B5E68B  E8 40 FB FF FF                  call 0x140b5e1d0
00B5E690  83 3D 79 1D 2B 00 00            cmp dword ptr [rip + 0x2b1d79], 0
00B5E697  8B D8                           mov ebx, eax
00B5E699  75 07                           jne 0x140b5e6a2
00B5E69B  44 89 3D 6E 1D 2B 00            mov dword ptr [rip + 0x2b1d6e], r15d
00B5E6A2  85 DB                           test ebx, ebx
00B5E6A4  0F 88 0E 02 00 00               js 0x140b5e8b8
00B5E6AA  48 8B 75 40                     mov rsi, qword ptr [rbp + 0x40]
00B5E6AE  48 8B CE                        mov rcx, rsi
00B5E6B1  E8 22 75 9F FF                  call 0x140555bd8
00B5E6B6  8B D8                           mov ebx, eax
00B5E6B8  85 C0                           test eax, eax
00B5E6BA  0F 88 F8 01 00 00               js 0x140b5e8b8
00B5E6C0  48 8B 05 91 2E 46 00            mov rax, qword ptr [rip + 0x462e91]
00B5E6C7  4C 39 28                        cmp qword ptr [rax], r13
00B5E6CA  0F 85 B3 01 00 00               jne 0x140b5e883
00B5E6D0  4C 89 2E                        mov qword ptr [rsi], r13
00B5E6D3  48 89 46 08                     mov qword ptr [rsi + 8], rax
00B5E6D7  48 89 30                        mov qword ptr [rax], rsi
00B5E6DA  48 89 35 77 2E 46 00            mov qword ptr [rip + 0x462e77], rsi
00B5E6E1  E9 CA 01 00 00                  jmp 0x140b5e8b0
00B5E6E6  83 7F 08 0C                     cmp dword ptr [rdi + 8], 0xc
00B5E6EA  48 8D 55 40                     lea rdx, [rbp + 0x40]
00B5E6EE  48 8B CF                        mov rcx, rdi
00B5E6F1  74 07                           je 0x140b5e6fa
00B5E6F3  E8 70 F8 FF FF                  call 0x140b5df68
00B5E6F8  EB 05                           jmp 0x140b5e6ff
00B5E6FA  E8 D1 FA FF FF                  call 0x140b5e1d0
00B5E6FF  8B D8                           mov ebx, eax
00B5E701  85 C0                           test eax, eax
00B5E703  78 2C                           js 0x140b5e731
00B5E705  48 8B 0D 5C 2E 46 00            mov rcx, qword ptr [rip + 0x462e5c]
00B5E70C  48 8D 15 4D 2E 46 00            lea rdx, [rip + 0x462e4d]
00B5E713  48 39 11                        cmp qword ptr [rcx], rdx
00B5E716  0F 85 67 01 00 00               jne 0x140b5e883
00B5E71C  48 8B 45 40                     mov rax, qword ptr [rbp + 0x40]
00B5E720  48 89 10                        mov qword ptr [rax], rdx
00B5E723  48 89 48 08                     mov qword ptr [rax + 8], rcx
00B5E727  48 89 01                        mov qword ptr [rcx], rax
00B5E72A  48 89 05 37 2E 46 00            mov qword ptr [rip + 0x462e37], rax
00B5E731  83 3D DC 1C 2B 00 00            cmp dword ptr [rip + 0x2b1cdc], 0
00B5E738  0F 85 FB 00 00 00               jne 0x140b5e839
00B5E73E  44 89 3D CF 1C 2B 00            mov dword ptr [rip + 0x2b1ccf], r15d
00B5E745  E9 EF 00 00 00                  jmp 0x140b5e839
00B5E74A  83 7F 08 0C                     cmp dword ptr [rdi + 8], 0xc
00B5E74E  48 8D 55 40                     lea rdx, [rbp + 0x40]
00B5E752  48 8B CF                        mov rcx, rdi
00B5E755  74 07                           je 0x140b5e75e
00B5E757  E8 0C F8 FF FF                  call 0x140b5df68
00B5E75C  EB 05                           jmp 0x140b5e763
00B5E75E  E8 6D FA FF FF                  call 0x140b5e1d0
00B5E763  8B D8                           mov ebx, eax
00B5E765  85 C0                           test eax, eax
00B5E767  78 25                           js 0x140b5e78e
00B5E769  48 8B 0D D8 2D 46 00            mov rcx, qword ptr [rip + 0x462dd8]
00B5E770  4C 39 21                        cmp qword ptr [rcx], r12
00B5E773  0F 85 0A 01 00 00               jne 0x140b5e883
00B5E779  48 8B 45 40                     mov rax, qword ptr [rbp + 0x40]
00B5E77D  4C 89 20                        mov qword ptr [rax], r12
00B5E780  48 89 48 08                     mov qword ptr [rax + 8], rcx
00B5E784  48 89 01                        mov qword ptr [rcx], rax
00B5E787  48 89 05 BA 2D 46 00            mov qword ptr [rip + 0x462dba], rax
00B5E78E  83 3D 8B 1C 2B 00 00            cmp dword ptr [rip + 0x2b1c8b], 0
00B5E795  0F 85 9E 00 00 00               jne 0x140b5e839
00B5E79B  44 89 3D 7E 1C 2B 00            mov dword ptr [rip + 0x2b1c7e], r15d
00B5E7A2  E9 92 00 00 00                  jmp 0x140b5e839
00B5E7A7  83 7F 08 0C                     cmp dword ptr [rdi + 8], 0xc
00B5E7AB  48 8D 55 40                     lea rdx, [rbp + 0x40]
00B5E7AF  48 8B CF                        mov rcx, rdi
00B5E7B2  74 07                           je 0x140b5e7bb
00B5E7B4  E8 AF F7 FF FF                  call 0x140b5df68
00B5E7B9  EB 05                           jmp 0x140b5e7c0
00B5E7BB  E8 10 FA FF FF                  call 0x140b5e1d0
00B5E7C0  8B D8                           mov ebx, eax
00B5E7C2  85 C0                           test eax, eax
00B5E7C4  78 63                           js 0x140b5e829
00B5E7C6  48 8B 75 40                     mov rsi, qword ptr [rbp + 0x40]
00B5E7CA  48 8B 4E 28                     mov rcx, qword ptr [rsi + 0x28]
00B5E7CE  48 83 39 FF                     cmp qword ptr [rcx], -1
00B5E7D2  75 17                           jne 0x140b5e7eb
00B5E7D4  BA 48 61 6C 57                  mov edx, 0x576c6148
00B5E7D9  48 8B CE                        mov rcx, rsi
00B5E7DC  E8 8F 40 02 00                  call 0x140b82870
00B5E7E1  B8 01 00 00 C0                  mov eax, 0xc0000001
00B5E7E6  E9 CF 00 00 00                  jmp 0x140b5e8ba
00B5E7EB  8B 56 30                        mov edx, dword ptr [rsi + 0x30]
00B5E7EE  41 B8 04 02 00 00               mov r8d, 0x204
00B5E7F4  48 8B 09                        mov rcx, qword ptr [rcx]
00B5E7F7  E8 34 90 7C FF                  call 0x140327830
00B5E7FC  48 89 46 38                     mov qword ptr [rsi + 0x38], rax
00B5E800  48 85 C0                        test rax, rax
00B5E803  74 CF                           je 0x140b5e7d4
00B5E805  48 8B 05 7C 2E 46 00            mov rax, qword ptr [rip + 0x462e7c]
00B5E80C  48 8D 0D 6D 2E 46 00            lea rcx, [rip + 0x462e6d]
00B5E813  48 39 08                        cmp qword ptr [rax], rcx
00B5E816  75 6B                           jne 0x140b5e883
00B5E818  48 89 0E                        mov qword ptr [rsi], rcx
00B5E81B  48 89 46 08                     mov qword ptr [rsi + 8], rax
00B5E81F  48 89 30                        mov qword ptr [rax], rsi
00B5E822  48 89 35 5F 2E 46 00            mov qword ptr [rip + 0x462e5f], rsi
00B5E829  83 3D DC 1B 2B 00 00            cmp dword ptr [rip + 0x2b1bdc], 0
00B5E830  75 07                           jne 0x140b5e839
00B5E832  44 89 3D D3 1B 2B 00            mov dword ptr [rip + 0x2b1bd3], r15d
00B5E839  85 DB                           test ebx, ebx
00B5E83B  78 7B                           js 0x140b5e8b8
00B5E83D  EB 71                           jmp 0x140b5e8b0
00B5E83F  BB BB 00 00 C0                  mov ebx, 0xc00000bb
00B5E844  EB 72                           jmp 0x140b5e8b8
00B5E846  83 7F 08 0C                     cmp dword ptr [rdi + 8], 0xc
00B5E84A  48 8D 55 40                     lea rdx, [rbp + 0x40]
00B5E84E  48 8B CF                        mov rcx, rdi
00B5E851  74 07                           je 0x140b5e85a
00B5E853  E8 10 F7 FF FF                  call 0x140b5df68
00B5E858  EB 05                           jmp 0x140b5e85f
00B5E85A  E8 71 F9 FF FF                  call 0x140b5e1d0
00B5E85F  8B D8                           mov ebx, eax
00B5E861  48 A1 20 03 00 00 80 F7 FF FF   movabs rax, qword ptr [0xfffff78000000320]
00B5E86B  48 8B 4D 40                     mov rcx, qword ptr [rbp + 0x40]
00B5E86F  48 89 41 10                     mov qword ptr [rcx + 0x10], rax
00B5E873  85 DB                           test ebx, ebx
00B5E875  78 41                           js 0x140b5e8b8
00B5E877  48 8B 05 FA 2C 46 00            mov rax, qword ptr [rip + 0x462cfa]
00B5E87E  48 39 30                        cmp qword ptr [rax], rsi
00B5E881  74 07                           je 0x140b5e88a
00B5E883  B9 03 00 00 00                  mov ecx, 3
00B5E888  CD 29                           int 0x29
00B5E88A  83 3D 87 1B 2B 00 00            cmp dword ptr [rip + 0x2b1b87], 0
00B5E891  48 89 31                        mov qword ptr [rcx], rsi
00B5E894  48 89 41 08                     mov qword ptr [rcx + 8], rax
00B5E898  48 89 08                        mov qword ptr [rax], rcx
00B5E89B  48 89 0D D6 2C 46 00            mov qword ptr [rip + 0x462cd6], rcx
00B5E8A2  75 0C                           jne 0x140b5e8b0
00B5E8A4  44 89 3D 6D 1B 2B 00            mov dword ptr [rip + 0x2b1b6d], r15d
00B5E8AB  E8 E8 FB FF FF                  call 0x140b5e498
00B5E8B0  48 8B CF                        mov rcx, rdi
00B5E8B3  E8 1C F6 FF FF                  call 0x140b5ded4
00B5E8B8  8B C3                           mov eax, ebx
00B5E8BA  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
00B5E8BF  48 8B 74 24 58                  mov rsi, qword ptr [rsp + 0x58]
00B5E8C4  48 83 C4 20                     add rsp, 0x20
00B5E8C8  41 5F                           pop r15
00B5E8CA  41 5D                           pop r13
00B5E8CC  41 5C                           pop r12
00B5E8CE  5F                              pop rdi
00B5E8CF  5D                              pop rbp
00B5E8D0  C3                              ret
00B5E8D1  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpInitializeGenericErrorSource(int a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (32);
    if (a1 != 0) goto loc_00B5E590;
    result = 0;
    goto loc_00B5E8BA;
loc_00B5E590:
    if ((*(unsigned int *)(v_rip + 2825861)) == 0) {
        result = v_rip + 4600023;
        *(unsigned int *)(v_rip + 2825804) = 1;
        *(unsigned __int64 *)(v_rip + 4600017) = result;
        *(unsigned __int64 *)(v_rip + 4600002) = result;
        result = v_rip + 4599979;
        *(unsigned __int64 *)(v_rip + 4599980) = result;
        *(unsigned __int64 *)(v_rip + 4599965) = result;
        *(unsigned __int64 *)(v_rip + 4599646) = v_rip + 4599730;
        *(unsigned __int64 *)(v_rip + 4599631) = v_rip + 4599730;
        *(unsigned __int64 *)(v_rip + 4599664) = v_rip + 4599749;
        *(unsigned __int64 *)(v_rip + 4599649) = v_rip + 4599749;
        *(unsigned __int64 *)(v_rip + 4599922) = v_rip + 4600014;
        *(unsigned __int64 *)(v_rip + 4599907) = v_rip + 4600014;
        *(unsigned __int64 *)(v_rip + 4599588) = v_rip + 4599687;
        *(unsigned __int64 *)(v_rip + 4599573) = v_rip + 4599687;
        *(unsigned __int64 *)(v_rip + 4599606) = v_rip + 4599712;
        *(unsigned __int64 *)(v_rip + 4599591) = v_rip + 4599712;
    }
    if ((unsigned int)(*(unsigned __int8 *)(a2 + 64)) == 0) goto loc_00B5E846;
    a1 = (unsigned int)((*(unsigned __int8 *)(a2 + 64)) - (1));
    if (condition_is_equal) goto loc_00B5E83F;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00B5E83F;
    a1 = (unsigned int)((a1) - (2));
    if (condition_is_equal) goto loc_00B5E7A7;
    a1 = (unsigned int)((a1) - (4));
    if (condition_is_equal) goto loc_00B5E74A;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00B5E6E6;
    if (a1 != 1) goto loc_00B5E83F;
    if ((*(unsigned int *)(a2 + 8)) == 12) goto loc_00B5E68B;
    result = HalpInitGenericErrorSourceEntry(a2, v_stack_p18, a3, a4);
    goto loc_00B5E690;
loc_00B5E68B:
    result = HalpInitGenericErrorSourceEntryV2(a2, v_stack_p18, a3, a4);
loc_00B5E690:
    if ((*(unsigned int *)(v_rip + 2825593)) == 0) {
        *(unsigned int *)(v_rip + 2825582) = 1;
    }
    if (sign_flag) goto loc_00B5E8B8;
    result = HalpRegisterPeiErrorSource(v_stack_p18, v_stack_p18, a3, a4);
    if (sign_flag) goto loc_00B5E8B8;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4599441))) != (v_rip + 4599730)) goto loc_00B5E883;
    *(unsigned __int64 *)(v_stack_p18) = v_rip + 4599730;
    *(unsigned __int64 *)(v_stack_p18 + 8) = *(unsigned __int64 *)(v_rip + 4599441);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4599441)) = v_stack_p18;
    *(unsigned __int64 *)(v_rip + 4599415) = v_stack_p18;
    goto loc_00B5E8B0;
loc_00B5E6E6:
    if ((*(unsigned int *)(a2 + 8)) == 12) goto loc_00B5E6FA;
    result = HalpInitGenericErrorSourceEntry(a2, v_stack_p18, a3, a4);
    goto loc_00B5E6FF;
loc_00B5E6FA:
    result = HalpInitGenericErrorSourceEntryV2(a2, v_stack_p18, a3, a4);
loc_00B5E6FF:
    if (sign_flag) goto loc_00B5E731;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4599388))) != (v_rip + 4599373)) goto loc_00B5E883;
    *(unsigned __int64 *)(v_stack_p18) = v_rip + 4599373;
    *(unsigned __int64 *)(v_stack_p18 + 8) = *(unsigned __int64 *)(v_rip + 4599388);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4599388)) = v_stack_p18;
    *(unsigned __int64 *)(v_rip + 4599351) = v_stack_p18;
loc_00B5E731:
    if ((*(unsigned int *)(v_rip + 2825436)) != 0) goto loc_00B5E839;
    *(unsigned int *)(v_rip + 2825423) = 1;
    goto loc_00B5E839;
loc_00B5E74A:
    if ((*(unsigned int *)(a2 + 8)) == 12) goto loc_00B5E75E;
    result = HalpInitGenericErrorSourceEntry(a2, v_stack_p18, a3, a4);
    goto loc_00B5E763;
loc_00B5E75E:
    result = HalpInitGenericErrorSourceEntryV2(a2, v_stack_p18, a3, a4);
loc_00B5E763:
    if (sign_flag) goto loc_00B5E78E;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4599256))) != (v_rip + 4599687)) goto loc_00B5E883;
    *(unsigned __int64 *)(v_stack_p18) = v_rip + 4599687;
    *(unsigned __int64 *)(v_stack_p18 + 8) = *(unsigned __int64 *)(v_rip + 4599256);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4599256)) = v_stack_p18;
    *(unsigned __int64 *)(v_rip + 4599226) = v_stack_p18;
loc_00B5E78E:
    if ((*(unsigned int *)(v_rip + 2825355)) != 0) goto loc_00B5E839;
    *(unsigned int *)(v_rip + 2825342) = 1;
    goto loc_00B5E839;
loc_00B5E7A7:
    if ((*(unsigned int *)(a2 + 8)) == 12) goto loc_00B5E7BB;
    result = HalpInitGenericErrorSourceEntry(a2, v_stack_p18, a3, a4);
    goto loc_00B5E7C0;
loc_00B5E7BB:
    result = HalpInitGenericErrorSourceEntryV2(a2, v_stack_p18, a3, a4);
loc_00B5E7C0:
    if (sign_flag) goto loc_00B5E829;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p18 + 40))) != -1) goto loc_00B5E7EB;
loc_00B5E7D4:
    result = ExFreePoolWithTag(v_stack_p18, (unsigned int)(0x576C6148ULL), a3, a4);
    goto loc_00B5E8BA;
loc_00B5E7EB:
    result = MmMapIoSpaceEx(*(unsigned __int64 *)(v_stack_p18), (unsigned int)(*(unsigned int *)(v_stack_p18 + 48)), 516, a4);
    *(unsigned __int64 *)(v_stack_p18 + 56) = result;
    if (result == 0) goto loc_00B5E7D4;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4599420))) != (v_rip + 4599405)) goto loc_00B5E883;
    *(unsigned __int64 *)(v_stack_p18) = v_rip + 4599405;
    *(unsigned __int64 *)(v_stack_p18 + 8) = *(unsigned __int64 *)(v_rip + 4599420);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4599420)) = v_stack_p18;
    *(unsigned __int64 *)(v_rip + 4599391) = v_stack_p18;
loc_00B5E829:
    if ((*(unsigned int *)(v_rip + 2825180)) == 0) {
        *(unsigned int *)(v_rip + 2825171) = 1;
    }
    if (sign_flag) goto loc_00B5E8B8;
    goto loc_00B5E8B0;
loc_00B5E83F:
    goto loc_00B5E8B8;
loc_00B5E846:
    if ((*(unsigned int *)(a2 + 8)) == 12) goto loc_00B5E85A;
    result = HalpInitGenericErrorSourceEntry(a2, v_stack_p18, 516, a4);
    goto loc_00B5E85F;
loc_00B5E85A:
    result = HalpInitGenericErrorSourceEntryV2(a2, v_stack_p18, 516, a4);
loc_00B5E85F:
    *(unsigned __int64 *)(v_stack_p18 + 16) = result;
    if (sign_flag) goto loc_00B5E8B8;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4599034))) != v_stack_p18) {
        a1 = 3;
    }
    *(unsigned __int64 *)(a1) = v_stack_p18;
    *(unsigned __int64 *)(a1 + 8) = *(unsigned __int64 *)(v_rip + 4599034);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4599034)) = a1;
    *(unsigned __int64 *)(v_rip + 4598998) = a1;
    result = *(unsigned __int64 *)(v_rip + 4599034);
    if ((*(unsigned int *)(v_rip + 2825095)) == 0) {
        *(unsigned int *)(v_rip + 2825069) = 1;
        result = HalpInitGenericErrorSourcePollingRoutine(a1, v_stack_p18, 516, a4);
    }
    result = HalpGenInitialRead(a2, v_stack_p18, 516, a4);
loc_00B5E8B8:
loc_00B5E8BA:
    v_rsp = (v_rsp) + (32);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
}
```

## 5. (Beta) C Style

```c
int64_t HalpInitializeGenericErrorSource(int32_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (32);
    if (Arg1 != 0) goto loc_00B5E590;
    result = 0;
    goto loc_00B5E8BA;
loc_00B5E590:
    if ((*(uint32_t *)(v_rip + 0x2B1E85)) == 0) {
        result = v_rip + 4600023;
        *(uint32_t *)(v_rip + 0x2B1E4C) = 1;
        *(uint64_t *)(v_rip + 0x4630D1) = result;
        *(uint64_t *)(v_rip + 0x4630C2) = result;
        result = v_rip + 4599979;
        *(uint64_t *)(v_rip + 0x4630AC) = result;
        *(uint64_t *)(v_rip + 0x46309D) = result;
        *(uint64_t *)(v_rip + 0x462F5E) = v_rip + 4599730;
        *(uint64_t *)(v_rip + 0x462F4F) = v_rip + 4599730;
        *(uint64_t *)(v_rip + 0x462F70) = v_rip + 4599749;
        *(uint64_t *)(v_rip + 0x462F61) = v_rip + 4599749;
        *(uint64_t *)(v_rip + 0x463072) = v_rip + 4600014;
        *(uint64_t *)(v_rip + 0x463063) = v_rip + 4600014;
        *(uint64_t *)(v_rip + 0x462F24) = v_rip + 4599687;
        *(uint64_t *)(v_rip + 0x462F15) = v_rip + 4599687;
        *(uint64_t *)(v_rip + 0x462F36) = v_rip + 4599712;
        *(uint64_t *)(v_rip + 0x462F27) = v_rip + 4599712;
    }
    if ((uint32_t)(*(uint8_t *)(arg2 + 0x40)) == 0) goto loc_00B5E846;
    Arg1 = (uint32_t)((*(uint8_t *)(arg2 + 0x40)) - (1));
    if (condition_is_equal) goto loc_00B5E83F;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00B5E83F;
    Arg1 = (uint32_t)((Arg1) - (2));
    if (condition_is_equal) goto loc_00B5E7A7;
    Arg1 = (uint32_t)((Arg1) - (4));
    if (condition_is_equal) goto loc_00B5E74A;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00B5E6E6;
    if (Arg1 != 1) goto loc_00B5E83F;
    if ((*(uint32_t *)(arg2 + 0x8)) == 12) goto loc_00B5E68B;
    result = HalpInitGenericErrorSourceEntry(Arg2, v_stack_p18, a3, a4);
    goto loc_00B5E690;
loc_00B5E68B:
    result = HalpInitGenericErrorSourceEntryV2(Arg2, v_stack_p18, a3, a4);
loc_00B5E690:
    if ((*(uint32_t *)(v_rip + 0x2B1D79)) == 0) {
        *(uint32_t *)(v_rip + 0x2B1D6E) = 1;
    }
    if (sign_flag) goto loc_00B5E8B8;
    result = HalpRegisterPeiErrorSource(v_stack_p18, v_stack_p18, a3, a4);
    if (sign_flag) goto loc_00B5E8B8;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x462E91))) != (v_rip + 4599730)) goto loc_00B5E883;
    *(uint64_t *)(v_stack_p18) = v_rip + 4599730;
    *(uint64_t *)(v_stack_p18 + 0x8) = *(uint64_t *)(v_rip + 0x462E91);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x462E91)) = v_stack_p18;
    *(uint64_t *)(v_rip + 0x462E77) = v_stack_p18;
    goto loc_00B5E8B0;
loc_00B5E6E6:
    if ((*(uint32_t *)(arg2 + 0x8)) == 12) goto loc_00B5E6FA;
    result = HalpInitGenericErrorSourceEntry(Arg2, v_stack_p18, a3, a4);
    goto loc_00B5E6FF;
loc_00B5E6FA:
    result = HalpInitGenericErrorSourceEntryV2(Arg2, v_stack_p18, a3, a4);
loc_00B5E6FF:
    if (sign_flag) goto loc_00B5E731;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x462E5C))) != (v_rip + 4599373)) goto loc_00B5E883;
    *(uint64_t *)(v_stack_p18) = v_rip + 4599373;
    *(uint64_t *)(v_stack_p18 + 0x8) = *(uint64_t *)(v_rip + 0x462E5C);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x462E5C)) = v_stack_p18;
    *(uint64_t *)(v_rip + 0x462E37) = v_stack_p18;
loc_00B5E731:
    if ((*(uint32_t *)(v_rip + 0x2B1CDC)) != 0) goto loc_00B5E839;
    *(uint32_t *)(v_rip + 0x2B1CCF) = 1;
    goto loc_00B5E839;
loc_00B5E74A:
    if ((*(uint32_t *)(arg2 + 0x8)) == 12) goto loc_00B5E75E;
    result = HalpInitGenericErrorSourceEntry(Arg2, v_stack_p18, a3, a4);
    goto loc_00B5E763;
loc_00B5E75E:
    result = HalpInitGenericErrorSourceEntryV2(Arg2, v_stack_p18, a3, a4);
loc_00B5E763:
    if (sign_flag) goto loc_00B5E78E;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x462DD8))) != (v_rip + 4599687)) goto loc_00B5E883;
    *(uint64_t *)(v_stack_p18) = v_rip + 4599687;
    *(uint64_t *)(v_stack_p18 + 0x8) = *(uint64_t *)(v_rip + 0x462DD8);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x462DD8)) = v_stack_p18;
    *(uint64_t *)(v_rip + 0x462DBA) = v_stack_p18;
loc_00B5E78E:
    if ((*(uint32_t *)(v_rip + 0x2B1C8B)) != 0) goto loc_00B5E839;
    *(uint32_t *)(v_rip + 0x2B1C7E) = 1;
    goto loc_00B5E839;
loc_00B5E7A7:
    if ((*(uint32_t *)(arg2 + 0x8)) == 12) goto loc_00B5E7BB;
    result = HalpInitGenericErrorSourceEntry(Arg2, v_stack_p18, a3, a4);
    goto loc_00B5E7C0;
loc_00B5E7BB:
    result = HalpInitGenericErrorSourceEntryV2(Arg2, v_stack_p18, a3, a4);
loc_00B5E7C0:
    if (sign_flag) goto loc_00B5E829;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_p18 + 0x28))) != -1) goto loc_00B5E7EB;
loc_00B5E7D4:
    result = ExFreePoolWithTag(v_stack_p18, (uint32_t)(0x576C6148ULL), a3, a4);
    goto loc_00B5E8BA;
loc_00B5E7EB:
    result = MmMapIoSpaceEx(*(uint64_t *)(v_stack_p18), (uint32_t)(*(uint32_t *)(v_stack_p18 + 0x30)), 516, a4);
    *(uint64_t *)(v_stack_p18 + 0x38) = result;
    if (result == 0) goto loc_00B5E7D4;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x462E7C))) != (v_rip + 4599405)) goto loc_00B5E883;
    *(uint64_t *)(v_stack_p18) = v_rip + 4599405;
    *(uint64_t *)(v_stack_p18 + 0x8) = *(uint64_t *)(v_rip + 0x462E7C);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x462E7C)) = v_stack_p18;
    *(uint64_t *)(v_rip + 0x462E5F) = v_stack_p18;
loc_00B5E829:
    if ((*(uint32_t *)(v_rip + 0x2B1BDC)) == 0) {
        *(uint32_t *)(v_rip + 0x2B1BD3) = 1;
    }
    if (sign_flag) goto loc_00B5E8B8;
    goto loc_00B5E8B0;
loc_00B5E83F:
    goto loc_00B5E8B8;
loc_00B5E846:
    if ((*(uint32_t *)(arg2 + 0x8)) == 12) goto loc_00B5E85A;
    result = HalpInitGenericErrorSourceEntry(Arg2, v_stack_p18, 516, a4);
    goto loc_00B5E85F;
loc_00B5E85A:
    result = HalpInitGenericErrorSourceEntryV2(Arg2, v_stack_p18, 516, a4);
loc_00B5E85F:
    *(uint64_t *)(v_stack_p18 + 0x10) = result;
    if (sign_flag) goto loc_00B5E8B8;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x462CFA))) != v_stack_p18) {
        Arg1 = 3;
    }
    *(uint64_t *)(Arg1) = v_stack_p18;
    *(uint64_t *)(Arg1 + 0x8) = *(uint64_t *)(v_rip + 0x462CFA);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x462CFA)) = Arg1;
    *(uint64_t *)(v_rip + 0x462CD6) = Arg1;
    result = *(uint64_t *)(v_rip + 0x462CFA);
    if ((*(uint32_t *)(v_rip + 0x2B1B87)) == 0) {
        *(uint32_t *)(v_rip + 0x2B1B6D) = 1;
        result = HalpInitGenericErrorSourcePollingRoutine(Arg1, v_stack_p18, 516, a4);
    }
    result = HalpGenInitialRead(Arg2, v_stack_p18, 516, a4);
loc_00B5E8B8:
loc_00B5E8BA:
    local_rsp = (local_rsp) + (32);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x8` | `32` | `R` |
| `Arg2` | `+ 0x40` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagelk&rva=0x00B5E564&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
