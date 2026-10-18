# HalpMiscGetParameters

- RVA: `0x00C1FD30`–`0x00C200FB` (길이 `971` bytes)
- VA: `0x0000000140C1FD30`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C4144`
- 디코드: `245`개 명령, `971/971` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **35**; 고유 호출 대상: **12**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **41**

### Outgoing calls
- `0x00C1FD51` → [HalpInterruptModel](../../text/4A/HalpInterruptModel_function_004ACA38.md) (function, `0x004ACA38`)
- `0x00C1FD64` → [HalpProcIsSmtDisabled](HalpProcIsSmtDisabled_function_00C1FBF4.md) (function, `0x00C1FBF4`)
- `0x00C1FDB0` → [strstr](../../text/4F/strstr_function_004FF680.md) (function, `0x004FF680`)
- `0x00C1FDBF` → [strstr](../../text/4F/strstr_function_004FF680.md) (function, `0x004FF680`)
- `0x00C1FDDD` → [strstr](../../text/4F/strstr_function_004FF680.md) (function, `0x004FF680`)
- `0x00C1FDF8` → [strstr](../../text/4F/strstr_function_004FF680.md) (function, `0x004FF680`)
- `0x00C1FE13` → [strstr](../../text/4F/strstr_function_004FF680.md) (function, `0x004FF680`)
- `0x00C1FE38` → [atoi](../../text/4F/atoi_function_004FF8B0.md) (function, `0x004FF8B0`)
- `0x00C1FE3F` → [HalpInterruptForceClusterMode](../../text/54/HalpInterruptForceClusterMode_function_00543F68.md) (function, `0x00543F68`)
- `0x00C1FE4E` → [strstr](../../text/4F/strstr_function_004FF680.md) (function, `0x004FF680`)
- `0x00C1FE73` → [atoi](../../text/4F/atoi_function_004FF8B0.md) (function, `0x004FF8B0`)
- `0x00C1FE8D` → [strstr](../../text/4F/strstr_function_004FF680.md) (function, `0x004FF680`)
- `0x00C1FEA8` → [strstr](../../text/4F/strstr_function_004FF680.md) (function, `0x004FF680`)
- `0x00C1FEC3` → [strstr](../../text/4F/strstr_function_004FF680.md) (function, `0x004FF680`)
- `0x00C1FEDE` → [strstr](../../text/4F/strstr_function_004FF680.md) (function, `0x004FF680`)
- `0x00C1FEFB` → [strstr](../../text/4F/strstr_function_004FF680.md) (function, `0x004FF680`)
- `0x00C1FF16` → [strstr](../../text/4F/strstr_function_004FF680.md) (function, `0x004FF680`)
- `0x00C1FF31` → [strstr](../../text/4F/strstr_function_004FF680.md) (function, `0x004FF680`)
- `0x00C1FF49` → [strstr](../../text/4F/strstr_function_004FF680.md) (function, `0x004FF680`)
- `0x00C1FF55` → [HalpInterruptSetMsiOverride](../../text/54/HalpInterruptSetMsiOverride_function_00544748.md) (function, `0x00544748`)
- `0x00C1FF5A` → [HalpIsHvPresent](../../text/4A/HalpIsHvPresent_function_004AFA10.md) (function, `0x004AFA10`)
- `0x00C1FF6A` → [HalpIsPartitionCpuManager](../../text/4F/HalpIsPartitionCpuManager_function_004F8DEC.md) (function, `0x004F8DEC`)
- `0x00C1FF7A` → [HalpIsMicrosoftCompatibleHvLoaded](../../text/4A/HalpIsMicrosoftCompatibleHvLoaded_function_004AFAAC.md) (function, `0x004AFAAC`)
- `0x00C1FF93` → [HalpIsXboxNanovisorPresent](../../text/54/HalpIsXboxNanovisorPresent_function_0054C3C0.md) (function, `0x0054C3C0`)
- `0x00C1FFBD` → [HalpGetCpuInfo](../../text/49/HalpGetCpuInfo_function_00498A70.md) (function, `0x00498A70`)
- `0x00C1FFF3` → [strstr](../../text/4F/strstr_function_004FF680.md) (function, `0x004FF680`)
- `0x00C1FFFD` → [HalpIsMicrosoftCompatibleHvLoaded](../../text/4A/HalpIsMicrosoftCompatibleHvLoaded_function_004AFAAC.md) (function, `0x004AFAAC`)
- `0x00C20020` → [strstr](../../text/4F/strstr_function_004FF680.md) (function, `0x004FF680`)
- `0x00C2003B` → [strstr](../../text/4F/strstr_function_004FF680.md) (function, `0x004FF680`)
- `0x00C20056` → [strstr](../../text/4F/strstr_function_004FF680.md) (function, `0x004FF680`)
- `0x00C2007B` → [atoi](../../text/4F/atoi_function_004FF8B0.md) (function, `0x004FF8B0`)
- `0x00C200BA` → [strstr](../../text/4F/strstr_function_004FF680.md) (function, `0x004FF680`)
- `0x00C200C9` → [strstr](../../text/4F/strstr_function_004FF680.md) (function, `0x004FF680`)
- `0x00C200D8` → [strstr](../../text/4F/strstr_function_004FF680.md) (function, `0x004FF680`)
- `0x00C200E5` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [HalpMiscInitSystem](../../pagelk/B5/HalpMiscInitSystem_function_00B5D510.md) at `0x00B5D53D`

### Static image references
- `0x00C1FD3F` → RVA `0x00E0A740` (`.data`; read)
- `0x00C1FD5B` → RVA `0x00FC19BA` (`.data`; write)
- `0x00C1FD69` → RVA `0x00F9070A` (`.data`; write)
- `0x00C1FD8F` → RVA `0x00F90709` (`.data`; write)
- `0x00C1FDA6` → RVA `0x00024328` (`.rdata`; read)
- `0x00C1FDB5` → RVA `0x00024338` (`.rdata`; read)
- `0x00C1FDC9` → RVA `0x00E10208` (`.data`; write)
- `0x00C1FDD3` → RVA `0x00024450` (`.rdata`; read)
- `0x00C1FDE7` → RVA `0x00E10204` (`.data`; write)
- `0x00C1FDEE` → RVA `0x00024444` (`.rdata`; read)
- `0x00C1FE02` → RVA `0x00FC19B9` (`.data`; write)
- `0x00C1FE09` → RVA `0x000243A0` (`.rdata`; read)
- `0x00C1FE44` → RVA `0x000243E0` (`.rdata`; read)
- `0x00C1FE7D` → RVA `0x00E101D8` (`.data`; write)
- `0x00C1FE83` → RVA `0x00024350` (`.rdata`; read)
- `0x00C1FE97` → RVA `0x00E0A77C` (`.data`; write)
- `0x00C1FE9E` → RVA `0x000243C8` (`.rdata`; read)
- `0x00C1FEB9` → RVA `0x00024388` (`.rdata`; read)
- `0x00C1FED4` → RVA `0x000244F8` (`.rdata`; read)
- `0x00C1FEE8` → RVA `0x00FC2160` (`.data`; write)
- `0x00C1FEF1` → RVA `0x00024460` (`.rdata`; read)
- `0x00C1FF05` → RVA `0x00FC2170` (`.data`; write)
- `0x00C1FF0C` → RVA `0x000244C0` (`.rdata`; read)
- `0x00C1FF20` → RVA `0x00E103F8` (`.data`; write)
- `0x00C1FF27` → RVA `0x000243F0` (`.rdata`; read)
- `0x00C1FF3F` → RVA `0x000243B8` (`.rdata`; read)
- `0x00C1FF63` → RVA `0x00FC1ED1` (`.data`; write)
- `0x00C1FF73` → RVA `0x00FC1ED0` (`.data`; write)
- `0x00C1FF9C` → RVA `0x00FC2150` (`.data`; write)
- `0x00C1FFA3` → RVA `0x00FC1ED0` (`.data`; read)
- `0x00C1FFE9` → RVA `0x00024428` (`.rdata`; read)
- `0x00C20016` → RVA `0x00024488` (`.rdata`; read)
- `0x00C2002A` → RVA `0x00FC4050` (`.data`; write)
- `0x00C20031` → RVA `0x00024340` (`.rdata`; read)
- `0x00C20045` → RVA `0x00FC40F8` (`.data`; write)
- `0x00C2004C` → RVA `0x000244E8` (`.rdata`; read)
- `0x00C20080` → RVA `0x00E0A81C` (`.data`; write)
- `0x00C200AD` → RVA `0x00E10462` (`.data`; write)
- `0x00C200B3` → RVA `0x00024368` (`.rdata`; read)
- `0x00C200BF` → RVA `0x000244A0` (`.rdata`; read)
- `0x00C200CE` → RVA `0x00024408` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **34**
  - `0x00C1FD51` → [HalpInterruptModel](../../text/4A/HalpInterruptModel_function_004ACA38.md) (`INIT` → `.text`)
  - `0x00C1FDB0` → [strstr](../../text/4F/strstr_function_004FF680.md) (`INIT` → `.text`)
  - `0x00C1FDBF` → [strstr](../../text/4F/strstr_function_004FF680.md) (`INIT` → `.text`)
  - `0x00C1FDDD` → [strstr](../../text/4F/strstr_function_004FF680.md) (`INIT` → `.text`)
  - `0x00C1FDF8` → [strstr](../../text/4F/strstr_function_004FF680.md) (`INIT` → `.text`)
  - `0x00C1FE13` → [strstr](../../text/4F/strstr_function_004FF680.md) (`INIT` → `.text`)
  - `0x00C1FE38` → [atoi](../../text/4F/atoi_function_004FF8B0.md) (`INIT` → `.text`)
  - `0x00C1FE3F` → [HalpInterruptForceClusterMode](../../text/54/HalpInterruptForceClusterMode_function_00543F68.md) (`INIT` → `.text`)
  - `0x00C1FE4E` → [strstr](../../text/4F/strstr_function_004FF680.md) (`INIT` → `.text`)
  - `0x00C1FE73` → [atoi](../../text/4F/atoi_function_004FF8B0.md) (`INIT` → `.text`)
  - `0x00C1FE8D` → [strstr](../../text/4F/strstr_function_004FF680.md) (`INIT` → `.text`)
  - `0x00C1FEA8` → [strstr](../../text/4F/strstr_function_004FF680.md) (`INIT` → `.text`)
  - `0x00C1FEC3` → [strstr](../../text/4F/strstr_function_004FF680.md) (`INIT` → `.text`)
  - `0x00C1FEDE` → [strstr](../../text/4F/strstr_function_004FF680.md) (`INIT` → `.text`)
  - `0x00C1FEFB` → [strstr](../../text/4F/strstr_function_004FF680.md) (`INIT` → `.text`)
  - `0x00C1FF16` → [strstr](../../text/4F/strstr_function_004FF680.md) (`INIT` → `.text`)
  - `0x00C1FF31` → [strstr](../../text/4F/strstr_function_004FF680.md) (`INIT` → `.text`)
  - `0x00C1FF49` → [strstr](../../text/4F/strstr_function_004FF680.md) (`INIT` → `.text`)
  - `0x00C1FF55` → [HalpInterruptSetMsiOverride](../../text/54/HalpInterruptSetMsiOverride_function_00544748.md) (`INIT` → `.text`)
  - `0x00C1FF5A` → [HalpIsHvPresent](../../text/4A/HalpIsHvPresent_function_004AFA10.md) (`INIT` → `.text`)
  - `0x00C1FF6A` → [HalpIsPartitionCpuManager](../../text/4F/HalpIsPartitionCpuManager_function_004F8DEC.md) (`INIT` → `.text`)
  - `0x00C1FF7A` → [HalpIsMicrosoftCompatibleHvLoaded](../../text/4A/HalpIsMicrosoftCompatibleHvLoaded_function_004AFAAC.md) (`INIT` → `.text`)
  - `0x00C1FF93` → [HalpIsXboxNanovisorPresent](../../text/54/HalpIsXboxNanovisorPresent_function_0054C3C0.md) (`INIT` → `.text`)
  - `0x00C1FFBD` → [HalpGetCpuInfo](../../text/49/HalpGetCpuInfo_function_00498A70.md) (`INIT` → `.text`)
  - `0x00C1FFF3` → [strstr](../../text/4F/strstr_function_004FF680.md) (`INIT` → `.text`)
  - `0x00C1FFFD` → [HalpIsMicrosoftCompatibleHvLoaded](../../text/4A/HalpIsMicrosoftCompatibleHvLoaded_function_004AFAAC.md) (`INIT` → `.text`)
  - `0x00C20020` → [strstr](../../text/4F/strstr_function_004FF680.md) (`INIT` → `.text`)
  - `0x00C2003B` → [strstr](../../text/4F/strstr_function_004FF680.md) (`INIT` → `.text`)
  - `0x00C20056` → [strstr](../../text/4F/strstr_function_004FF680.md) (`INIT` → `.text`)
  - `0x00C2007B` → [atoi](../../text/4F/atoi_function_004FF8B0.md) (`INIT` → `.text`)
  - `0x00C200BA` → [strstr](../../text/4F/strstr_function_004FF680.md) (`INIT` → `.text`)
  - `0x00C200C9` → [strstr](../../text/4F/strstr_function_004FF680.md) (`INIT` → `.text`)
  - `0x00C200D8` → [strstr](../../text/4F/strstr_function_004FF680.md) (`INIT` → `.text`)
  - `0x00C200E5` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`INIT` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C1FD30  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00C1FD35  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
00C1FD3A  57                              push rdi
00C1FD3B  48 83 EC 40                     sub rsp, 0x40
00C1FD3F  48 8B 05 FA A9 1E 00            mov rax, qword ptr [rip + 0x1ea9fa]
00C1FD46  48 33 C4                        xor rax, rsp
00C1FD49  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00C1FD4E  48 8B F1                        mov rsi, rcx
00C1FD51  E8 E2 CC 88 FF                  call 0x1404aca38
00C1FD56  83 F8 01                        cmp eax, 1
00C1FD59  75 06                           jne 0x140c1fd61
00C1FD5B  88 05 59 1C 3A 00               mov byte ptr [rip + 0x3a1c59], al
00C1FD61  48 8B CE                        mov rcx, rsi
00C1FD64  E8 8B FE FF FF                  call 0x140c1fbf4
00C1FD69  88 05 9B 09 37 00               mov byte ptr [rip + 0x37099b], al
00C1FD6F  48 85 F6                        test rsi, rsi
00C1FD72  0F 84 65 03 00 00               je 0x140c200dd
00C1FD78  84 C0                           test al, al
00C1FD7A  74 1A                           je 0x140c1fd96
00C1FD7C  48 8B 86 F0 00 00 00            mov rax, qword ptr [rsi + 0xf0]
00C1FD83  F7 80 84 00 00 00 00 02 00 00   test dword ptr [rax + 0x84], 0x200
00C1FD8D  75 07                           jne 0x140c1fd96
00C1FD8F  C6 05 73 09 37 00 01            mov byte ptr [rip + 0x370973], 1
00C1FD96  48 8B BE D8 00 00 00            mov rdi, qword ptr [rsi + 0xd8]
00C1FD9D  48 85 FF                        test rdi, rdi
00C1FDA0  0F 84 37 03 00 00               je 0x140c200dd
00C1FDA6  48 8D 15 7B 45 40 FF            lea rdx, [rip - 0xbfba85]
00C1FDAD  48 8B CF                        mov rcx, rdi
00C1FDB0  E8 CB F8 8D FF                  call 0x1404ff680
00C1FDB5  48 8D 15 7C 45 40 FF            lea rdx, [rip - 0xbfba84]
00C1FDBC  48 8B CF                        mov rcx, rdi
00C1FDBF  E8 BC F8 8D FF                  call 0x1404ff680
00C1FDC4  48 85 C0                        test rax, rax
00C1FDC7  74 0A                           je 0x140c1fdd3
00C1FDC9  C7 05 35 04 1F 00 01 00 00 00   mov dword ptr [rip + 0x1f0435], 1
00C1FDD3  48 8D 15 76 46 40 FF            lea rdx, [rip - 0xbfb98a]
00C1FDDA  48 8B CF                        mov rcx, rdi
00C1FDDD  E8 9E F8 8D FF                  call 0x1404ff680
00C1FDE2  48 85 C0                        test rax, rax
00C1FDE5  74 07                           je 0x140c1fdee
00C1FDE7  C6 05 16 04 1F 00 01            mov byte ptr [rip + 0x1f0416], 1
00C1FDEE  48 8D 15 4F 46 40 FF            lea rdx, [rip - 0xbfb9b1]
00C1FDF5  48 8B CF                        mov rcx, rdi
00C1FDF8  E8 83 F8 8D FF                  call 0x1404ff680
00C1FDFD  48 85 C0                        test rax, rax
00C1FE00  74 07                           je 0x140c1fe09
00C1FE02  C6 05 B0 1B 3A 00 01            mov byte ptr [rip + 0x3a1bb0], 1
00C1FE09  48 8D 15 90 45 40 FF            lea rdx, [rip - 0xbfba70]
00C1FE10  48 8B CF                        mov rcx, rdi
00C1FE13  E8 68 F8 8D FF                  call 0x1404ff680
00C1FE18  48 85 C0                        test rax, rax
00C1FE1B  74 27                           je 0x140c1fe44
00C1FE1D  EB 10                           jmp 0x140c1fe2f
00C1FE1F  80 F9 20                        cmp cl, 0x20
00C1FE22  74 11                           je 0x140c1fe35
00C1FE24  80 E9 30                        sub cl, 0x30
00C1FE27  80 F9 09                        cmp cl, 9
00C1FE2A  76 09                           jbe 0x140c1fe35
00C1FE2C  48 FF C0                        inc rax
00C1FE2F  8A 08                           mov cl, byte ptr [rax]
00C1FE31  84 C9                           test cl, cl
00C1FE33  75 EA                           jne 0x140c1fe1f
00C1FE35  48 8B C8                        mov rcx, rax
00C1FE38  E8 73 FA 8D FF                  call 0x1404ff8b0
00C1FE3D  8B C8                           mov ecx, eax
00C1FE3F  E8 24 41 92 FF                  call 0x140543f68
00C1FE44  48 8D 15 95 45 40 FF            lea rdx, [rip - 0xbfba6b]
00C1FE4B  48 8B CF                        mov rcx, rdi
00C1FE4E  E8 2D F8 8D FF                  call 0x1404ff680
00C1FE53  48 85 C0                        test rax, rax
00C1FE56  74 2B                           je 0x140c1fe83
00C1FE58  EB 10                           jmp 0x140c1fe6a
00C1FE5A  80 F9 20                        cmp cl, 0x20
00C1FE5D  74 11                           je 0x140c1fe70
00C1FE5F  80 E9 30                        sub cl, 0x30
00C1FE62  80 F9 09                        cmp cl, 9
00C1FE65  76 09                           jbe 0x140c1fe70
00C1FE67  48 FF C0                        inc rax
00C1FE6A  8A 08                           mov cl, byte ptr [rax]
00C1FE6C  84 C9                           test cl, cl
00C1FE6E  75 EA                           jne 0x140c1fe5a
00C1FE70  48 8B C8                        mov rcx, rax
00C1FE73  E8 38 FA 8D FF                  call 0x1404ff8b0
00C1FE78  83 F8 01                        cmp eax, 1
00C1FE7B  72 06                           jb 0x140c1fe83
00C1FE7D  89 05 55 03 1F 00               mov dword ptr [rip + 0x1f0355], eax
00C1FE83  48 8D 15 C6 44 40 FF            lea rdx, [rip - 0xbfbb3a]
00C1FE8A  48 8B CF                        mov rcx, rdi
00C1FE8D  E8 EE F7 8D FF                  call 0x1404ff680
00C1FE92  48 85 C0                        test rax, rax
00C1FE95  74 07                           je 0x140c1fe9e
00C1FE97  C6 05 DE A8 1E 00 01            mov byte ptr [rip + 0x1ea8de], 1
00C1FE9E  48 8D 15 23 45 40 FF            lea rdx, [rip - 0xbfbadd]
00C1FEA5  48 8B CF                        mov rcx, rdi
00C1FEA8  E8 D3 F7 8D FF                  call 0x1404ff680
00C1FEAD  48 85 C0                        test rax, rax
00C1FEB0  74 07                           je 0x140c1feb9
00C1FEB2  C6 05 C3 A8 1E 00 00            mov byte ptr [rip + 0x1ea8c3], 0
00C1FEB9  48 8D 15 C8 44 40 FF            lea rdx, [rip - 0xbfbb38]
00C1FEC0  48 8B CF                        mov rcx, rdi
00C1FEC3  E8 B8 F7 8D FF                  call 0x1404ff680
00C1FEC8  48 85 C0                        test rax, rax
00C1FECB  74 07                           je 0x140c1fed4
00C1FECD  C6 05 A8 A8 1E 00 00            mov byte ptr [rip + 0x1ea8a8], 0
00C1FED4  48 8D 15 1D 46 40 FF            lea rdx, [rip - 0xbfb9e3]
00C1FEDB  48 8B CF                        mov rcx, rdi
00C1FEDE  E8 9D F7 8D FF                  call 0x1404ff680
00C1FEE3  48 85 C0                        test rax, rax
00C1FEE6  74 09                           je 0x140c1fef1
00C1FEE8  C6 05 71 22 3A 00 01            mov byte ptr [rip + 0x3a2271], 1
00C1FEEF  EB 1B                           jmp 0x140c1ff0c
00C1FEF1  48 8D 15 68 45 40 FF            lea rdx, [rip - 0xbfba98]
00C1FEF8  48 8B CF                        mov rcx, rdi
00C1FEFB  E8 80 F7 8D FF                  call 0x1404ff680
00C1FF00  48 85 C0                        test rax, rax
00C1FF03  74 07                           je 0x140c1ff0c
00C1FF05  C6 05 64 22 3A 00 01            mov byte ptr [rip + 0x3a2264], 1
00C1FF0C  48 8D 15 AD 45 40 FF            lea rdx, [rip - 0xbfba53]
00C1FF13  48 8B CF                        mov rcx, rdi
00C1FF16  E8 65 F7 8D FF                  call 0x1404ff680
00C1FF1B  48 85 C0                        test rax, rax
00C1FF1E  74 07                           je 0x140c1ff27
00C1FF20  C6 05 D1 04 1F 00 01            mov byte ptr [rip + 0x1f04d1], 1
00C1FF27  48 8D 15 C2 44 40 FF            lea rdx, [rip - 0xbfbb3e]
00C1FF2E  48 8B CF                        mov rcx, rdi
00C1FF31  E8 4A F7 8D FF                  call 0x1404ff680
00C1FF36  48 85 C0                        test rax, rax
00C1FF39  74 04                           je 0x140c1ff3f
00C1FF3B  33 C9                           xor ecx, ecx
00C1FF3D  EB 16                           jmp 0x140c1ff55
00C1FF3F  48 8D 15 72 44 40 FF            lea rdx, [rip - 0xbfbb8e]
00C1FF46  48 8B CF                        mov rcx, rdi
00C1FF49  E8 32 F7 8D FF                  call 0x1404ff680
00C1FF4E  48 85 C0                        test rax, rax
00C1FF51  74 07                           je 0x140c1ff5a
00C1FF53  B1 01                           mov cl, 1
00C1FF55  E8 EE 47 92 FF                  call 0x140544748
00C1FF5A  E8 B1 FA 88 FF                  call 0x1404afa10
00C1FF5F  84 C0                           test al, al
00C1FF61  74 30                           je 0x140c1ff93
00C1FF63  C6 05 67 1F 3A 00 01            mov byte ptr [rip + 0x3a1f67], 1
00C1FF6A  E8 7D 8E 8D FF                  call 0x1404f8dec
00C1FF6F  84 C0                           test al, al
00C1FF71  74 07                           je 0x140c1ff7a
00C1FF73  C6 05 56 1F 3A 00 01            mov byte ptr [rip + 0x3a1f56], 1
00C1FF7A  E8 2D FB 88 FF                  call 0x1404afaac
00C1FF7F  84 C0                           test al, al
00C1FF81  74 10                           je 0x140c1ff93
00C1FF83  33 C9                           xor ecx, ecx
00C1FF85  B8 04 00 00 40                  mov eax, 0x40000004
00C1FF8A  0F A2                           cpuid
00C1FF8C  C1 E8 04                        shr eax, 4
00C1FF8F  A8 01                           test al, 1
00C1FF91  EB 07                           jmp 0x140c1ff9a
00C1FF93  E8 28 C4 92 FF                  call 0x14054c3c0
00C1FF98  84 C0                           test al, al
00C1FF9A  74 07                           je 0x140c1ffa3
00C1FF9C  C6 05 AD 21 3A 00 01            mov byte ptr [rip + 0x3a21ad], 1
00C1FFA3  80 3D 26 1F 3A 00 00            cmp byte ptr [rip + 0x3a1f26], 0
00C1FFAA  74 3D                           je 0x140c1ffe9
00C1FFAC  4C 8D 4C 24 20                  lea r9, [rsp + 0x20]
00C1FFB1  C6 44 24 20 00                  mov byte ptr [rsp + 0x20], 0
00C1FFB6  45 33 C0                        xor r8d, r8d
00C1FFB9  33 D2                           xor edx, edx
00C1FFBB  33 C9                           xor ecx, ecx
00C1FFBD  E8 AE 8A 87 FF                  call 0x140498a70
00C1FFC2  84 C0                           test al, al
00C1FFC4  74 23                           je 0x140c1ffe9
00C1FFC6  80 7C 24 20 02                  cmp byte ptr [rsp + 0x20], 2
00C1FFCB  75 1C                           jne 0x140c1ffe9
00C1FFCD  B9 FE 00 00 00                  mov ecx, 0xfe
00C1FFD2  0F 32                           rdmsr
00C1FFD4  48 C1 E2 20                     shl rdx, 0x20
00C1FFD8  48 0B C2                        or rax, rdx
00C1FFDB  48 0F BA E0 0F                  bt rax, 0xf
00C1FFE0  73 07                           jae 0x140c1ffe9
00C1FFE2  C6 05 D1 19 3A 00 01            mov byte ptr [rip + 0x3a19d1], 1
00C1FFE9  48 8D 15 38 44 40 FF            lea rdx, [rip - 0xbfbbc8]
00C1FFF0  48 8B CF                        mov rcx, rdi
00C1FFF3  E8 88 F6 8D FF                  call 0x1404ff680
00C1FFF8  48 85 C0                        test rax, rax
00C1FFFB  75 12                           jne 0x140c2000f
00C1FFFD  E8 AA FA 88 FF                  call 0x1404afaac
00C20002  84 C0                           test al, al
00C20004  74 10                           je 0x140c20016
00C20006  80 3D C3 1E 3A 00 00            cmp byte ptr [rip + 0x3a1ec3], 0
00C2000D  75 07                           jne 0x140c20016
00C2000F  C6 05 A4 19 3A 00 00            mov byte ptr [rip + 0x3a19a4], 0
00C20016  48 8D 15 6B 44 40 FF            lea rdx, [rip - 0xbfbb95]
00C2001D  48 8B CF                        mov rcx, rdi
00C20020  E8 5B F6 8D FF                  call 0x1404ff680
00C20025  48 85 C0                        test rax, rax
00C20028  74 07                           je 0x140c20031
00C2002A  C6 05 1F 40 3A 00 01            mov byte ptr [rip + 0x3a401f], 1
00C20031  48 8D 15 08 43 40 FF            lea rdx, [rip - 0xbfbcf8]
00C20038  48 8B CF                        mov rcx, rdi
00C2003B  E8 40 F6 8D FF                  call 0x1404ff680
00C20040  48 85 C0                        test rax, rax
00C20043  74 07                           je 0x140c2004c
00C20045  C6 05 AC 40 3A 00 01            mov byte ptr [rip + 0x3a40ac], 1
00C2004C  48 8D 15 95 44 40 FF            lea rdx, [rip - 0xbfbb6b]
00C20053  48 8B CF                        mov rcx, rdi
00C20056  E8 25 F6 8D FF                  call 0x1404ff680
00C2005B  48 85 C0                        test rax, rax
00C2005E  74 37                           je 0x140c20097
00C20060  EB 10                           jmp 0x140c20072
00C20062  80 F9 20                        cmp cl, 0x20
00C20065  74 11                           je 0x140c20078
00C20067  80 E9 30                        sub cl, 0x30
00C2006A  80 F9 09                        cmp cl, 9
00C2006D  76 09                           jbe 0x140c20078
00C2006F  48 FF C0                        inc rax
00C20072  8A 08                           mov cl, byte ptr [rax]
00C20074  84 C9                           test cl, cl
00C20076  75 EA                           jne 0x140c20062
00C20078  48 8B C8                        mov rcx, rax
00C2007B  E8 30 F8 8D FF                  call 0x1404ff8b0
00C20080  89 05 96 A7 1E 00               mov dword ptr [rip + 0x1ea796], eax
00C20086  FF C8                           dec eax
00C20088  83 F8 3F                        cmp eax, 0x3f
00C2008B  76 0A                           jbe 0x140c20097
00C2008D  C7 05 85 A7 1E 00 40 00 00 00   mov dword ptr [rip + 0x1ea785], 0x40
00C20097  48 8B 86 F0 00 00 00            mov rax, qword ptr [rsi + 0xf0]
00C2009E  48 8B CF                        mov rcx, rdi
00C200A1  8B 90 84 00 00 00               mov edx, dword ptr [rax + 0x84]
00C200A7  C1 EA 11                        shr edx, 0x11
00C200AA  80 E2 01                        and dl, 1
00C200AD  88 15 AF 03 1F 00               mov byte ptr [rip + 0x1f03af], dl
00C200B3  48 8D 15 AE 42 40 FF            lea rdx, [rip - 0xbfbd52]
00C200BA  E8 C1 F5 8D FF                  call 0x1404ff680
00C200BF  48 8D 15 DA 43 40 FF            lea rdx, [rip - 0xbfbc26]
00C200C6  48 8B CF                        mov rcx, rdi
00C200C9  E8 B2 F5 8D FF                  call 0x1404ff680
00C200CE  48 8D 15 33 43 40 FF            lea rdx, [rip - 0xbfbccd]
00C200D5  48 8B CF                        mov rcx, rdi
00C200D8  E8 A3 F5 8D FF                  call 0x1404ff680
00C200DD  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
00C200E2  48 33 CC                        xor rcx, rsp
00C200E5  E8 56 C5 A8 FF                  call 0x1406ac640
00C200EA  48 8B 5C 24 58                  mov rbx, qword ptr [rsp + 0x58]
00C200EF  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
00C200F4  48 83 C4 40                     add rsp, 0x40
00C200F8  5F                              pop rdi
00C200F9  C3                              ret
00C200FA  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpMiscGetParameters(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;

    v_stack_p10 = v_rbx;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (64);
    result = (*(unsigned __int64 *)(v_rip + 2009594)) ^ (v_rsp);
    v_stack_m10 = result;
    result = HalpInterruptModel(a1, a2, a3, a4);
    if (((unsigned int)(result)) == 1) {
        *(unsigned __int8 *)(v_rip + 3808345) = (unsigned __int8)(result);
    }
    result = HalpProcIsSmtDisabled(a1, a2, a3, a4);
    *(unsigned __int8 *)(v_rip + 3606939) = (unsigned __int8)(result);
    if (a1 == 0) goto loc_00C200DD;
    if ((unsigned __int8)(result) == 0) goto loc_00C1FD96;
    if (((*(unsigned int *)(*(unsigned __int64 *)(a1 + 240) + 132)) & (512)) == 0) {
        *(unsigned __int8 *)(v_rip + 3606899) = 1;
    }
    if (*(unsigned __int64 *)(a1 + 216) == 0) goto loc_00C200DD;
    result = strstr(*(unsigned __int64 *)(a1 + 216), v_rip - 12565125, a3, a4);
    result = strstr(*(unsigned __int64 *)(a1 + 216), v_rip - 12565124, a3, a4);
    if (result != 0) {
        *(unsigned int *)(v_rip + 2032693) = 1;
    }
    result = strstr(*(unsigned __int64 *)(a1 + 216), v_rip - 12564874, a3, a4);
    if (result != 0) {
        *(unsigned __int8 *)(v_rip + 2032662) = 1;
    }
    result = strstr(*(unsigned __int64 *)(a1 + 216), v_rip - 12564913, a3, a4);
    if (result != 0) {
        *(unsigned __int8 *)(v_rip + 3808176) = 1;
    }
    result = strstr(*(unsigned __int64 *)(a1 + 216), v_rip - 12565104, a3, a4);
    if (result == 0) goto loc_00C1FE44;
    goto loc_00C1FE2F;
loc_00C1FE1F:
    if (((unsigned __int8)(*(unsigned __int64 *)(a1 + 216))) == 32) goto loc_00C1FE35;
    a1 = (unsigned __int8)((*(unsigned __int64 *)(a1 + 216)) - (48));
    if (((unsigned __int8)(a1)) <= 9) goto loc_00C1FE35;
    result = (result) + 1;
loc_00C1FE2F:
    if ((unsigned __int8)(*(unsigned __int8 *)(result)) != 0) goto loc_00C1FE1F;
loc_00C1FE35:
    result = atoi(result, v_rip - 12565104, a3, a4);
    result = HalpInterruptForceClusterMode((unsigned int)((unsigned int)(result)), v_rip - 12565104, a3, a4);
loc_00C1FE44:
    result = strstr(*(unsigned __int64 *)(a1 + 216), v_rip - 12565099, a3, a4);
    if (result == 0) goto loc_00C1FE83;
    goto loc_00C1FE6A;
loc_00C1FE5A:
    if (((unsigned __int8)(*(unsigned __int64 *)(a1 + 216))) == 32) goto loc_00C1FE70;
    a1 = (unsigned __int8)((*(unsigned __int64 *)(a1 + 216)) - (48));
    if (((unsigned __int8)(a1)) <= 9) goto loc_00C1FE70;
    result = (result) + 1;
loc_00C1FE6A:
    if ((unsigned __int8)(*(unsigned __int8 *)(result)) != 0) goto loc_00C1FE5A;
loc_00C1FE70:
    result = atoi(result, v_rip - 12565099, a3, a4);
    if (((unsigned int)(result)) >= 1) {
        *(unsigned int *)(v_rip + 2032469) = (unsigned int)(result);
    }
    result = strstr(*(unsigned __int64 *)(a1 + 216), v_rip - 12565306, a3, a4);
    if (result != 0) {
        *(unsigned __int8 *)(v_rip + 2009310) = 1;
    }
    result = strstr(*(unsigned __int64 *)(a1 + 216), v_rip - 12565213, a3, a4);
    if (result != 0) {
        *(unsigned __int8 *)(v_rip + 2009283) = 0;
    }
    result = strstr(*(unsigned __int64 *)(a1 + 216), v_rip - 12565304, a3, a4);
    if (result != 0) {
        *(unsigned __int8 *)(v_rip + 2009256) = 0;
    }
    result = strstr(*(unsigned __int64 *)(a1 + 216), v_rip - 12564963, a3, a4);
    if (result == 0) goto loc_00C1FEF1;
    *(unsigned __int8 *)(v_rip + 3809905) = 1;
    goto loc_00C1FF0C;
loc_00C1FEF1:
    result = strstr(*(unsigned __int64 *)(a1 + 216), v_rip - 12565144, a3, a4);
    if (result != 0) {
        *(unsigned __int8 *)(v_rip + 3809892) = 1;
    }
    result = strstr(*(unsigned __int64 *)(a1 + 216), v_rip - 12565075, a3, a4);
    if (result != 0) {
        *(unsigned __int8 *)(v_rip + 2032849) = 1;
    }
    result = strstr(*(unsigned __int64 *)(a1 + 216), v_rip - 12565310, a3, a4);
    if (result == 0) goto loc_00C1FF3F;
    a1 = 0;
    goto loc_00C1FF55;
loc_00C1FF3F:
    result = strstr(*(unsigned __int64 *)(a1 + 216), v_rip - 12565390, a3, a4);
    if (result == 0) goto loc_00C1FF5A;
loc_00C1FF55:
    result = HalpInterruptSetMsiOverride(1, v_rip - 12565390, a3, a4);
loc_00C1FF5A:
    result = HalpIsHvPresent(1, v_rip - 12565390, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00C1FF93;
    *(unsigned __int8 *)(v_rip + 3809127) = 1;
    result = HalpIsPartitionCpuManager(1, v_rip - 12565390, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        *(unsigned __int8 *)(v_rip + 3809110) = 1;
    }
    result = HalpIsMicrosoftCompatibleHvLoaded(1, v_rip - 12565390, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00C1FF93;
    a1 = 0;
    result = (unsigned int)(((unsigned int)(0x40000004ULL)) >> (4));
    goto loc_00C1FF9A;
loc_00C1FF93:
    result = HalpIsXboxNanovisorPresent(a1, v_rip - 12565390, a3, a4);
loc_00C1FF9A:
    if ((unsigned __int8)(result) != 0) {
        *(unsigned __int8 *)(v_rip + 3809709) = 1;
    }
    if ((*(unsigned __int8 *)(v_rip + 3809062)) == 0) goto loc_00C1FFE9;
    v_stack_m28 = 0;
    a3 = 0;
    a2 = 0;
    a1 = 0;
    result = HalpGetCpuInfo(a1, a2, a3, v_stack_m28);
    if ((unsigned __int8)(result) == 0) goto loc_00C1FFE9;
    if (v_stack_m28 != 2) goto loc_00C1FFE9;
    a2 = (a2) << (32);
    result = (result) | (a2);
    if (!(condition_is_above_or_equal)) {
        *(unsigned __int8 *)(v_rip + 3807697) = 1;
    }
    result = strstr(*(unsigned __int64 *)(a1 + 216), v_rip - 12565448, a3, v_stack_m28);
    if (result != 0) goto loc_00C2000F;
    result = HalpIsMicrosoftCompatibleHvLoaded(*(unsigned __int64 *)(a1 + 216), v_rip - 12565448, a3, v_stack_m28);
    if ((unsigned __int8)(result) == 0) goto loc_00C20016;
    if ((*(unsigned __int8 *)(v_rip + 3808963)) == 0) {
        *(unsigned __int8 *)(v_rip + 3807652) = 0;
    }
    result = strstr(*(unsigned __int64 *)(a1 + 216), v_rip - 12565397, a3, v_stack_m28);
    if (result != 0) {
        *(unsigned __int8 *)(v_rip + 3817503) = 1;
    }
    result = strstr(*(unsigned __int64 *)(a1 + 216), v_rip - 12565752, a3, v_stack_m28);
    if (result != 0) {
        *(unsigned __int8 *)(v_rip + 3817644) = 1;
    }
    result = strstr(*(unsigned __int64 *)(a1 + 216), v_rip - 12565355, a3, v_stack_m28);
    if (result == 0) goto loc_00C20097;
    goto loc_00C20072;
loc_00C20062:
    if (((unsigned __int8)(*(unsigned __int64 *)(a1 + 216))) == 32) goto loc_00C20078;
    a1 = (unsigned __int8)((*(unsigned __int64 *)(a1 + 216)) - (48));
    if (((unsigned __int8)(a1)) <= 9) goto loc_00C20078;
    result = (result) + 1;
loc_00C20072:
    if ((unsigned __int8)(*(unsigned __int8 *)(result)) != 0) goto loc_00C20062;
loc_00C20078:
    result = atoi(result, v_rip - 12565355, a3, v_stack_m28);
    *(unsigned int *)(v_rip + 2008982) = (unsigned int)(result);
    result = (unsigned int)((result) - 1);
    if (((unsigned int)(result)) >= = 63) {
        *(unsigned int *)(v_rip + 2008965) = 64;
    }
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 240) + 132))) >> (17));
    a2 = (unsigned __int8)((a2) & (1));
    *(unsigned __int8 *)(v_rip + 2032559) = (unsigned __int8)(a2);
    result = strstr(*(unsigned __int64 *)(a1 + 216), v_rip - 12565842, a3, v_stack_m28);
    result = strstr(*(unsigned __int64 *)(a1 + 216), v_rip - 12565542, a3, v_stack_m28);
    result = strstr(*(unsigned __int64 *)(a1 + 216), v_rip - 12565709, a3, v_stack_m28);
loc_00C200DD:
    a1 = (v_stack_m10) ^ (v_rsp);
    result = _security_check_cookie(a1, v_rip - 12565709, a3, v_stack_m28);
    v_rsp = (v_rsp) + (64);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HalpMiscGetParameters(int64_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint64_t v_stack_m28;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;

    v_stack_p10 = local_rbx;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (64);
    result = (*(uint64_t *)(v_rip + 0x1EA9FA)) ^ (local_rsp);
    v_stack_m10 = result;
    result = HalpInterruptModel(Arg1, Arg2, Arg3, a4);
    if (((uint32_t)(result)) == 1) {
        *(uint8_t *)(v_rip + 0x3A1C59) = (uint8_t)(result);
    }
    result = HalpProcIsSmtDisabled(Arg1, Arg2, Arg3, a4);
    *(uint8_t *)(v_rip + 0x37099B) = (uint8_t)(result);
    if (Arg1 == 0) goto loc_00C200DD;
    if ((uint8_t)(result) == 0) goto loc_00C1FD96;
    if (((*(uint32_t *)(*(uint64_t *)(Arg1 + 0xF0) + 0x84)) & (512)) == 0) {
        *(uint8_t *)(v_rip + 0x370973) = 1;
    }
    if (*(uint64_t *)(Arg1 + 0xD8) == 0) goto loc_00C200DD;
    result = strstr(*(uint64_t *)(Arg1 + 0xD8), v_rip - 12565125, Arg3, a4);
    result = strstr(*(uint64_t *)(Arg1 + 0xD8), v_rip - 12565124, Arg3, a4);
    if (result != 0) {
        *(uint32_t *)(v_rip + 0x1F0435) = 1;
    }
    result = strstr(*(uint64_t *)(Arg1 + 0xD8), v_rip - 12564874, Arg3, a4);
    if (result != 0) {
        *(uint8_t *)(v_rip + 0x1F0416) = 1;
    }
    result = strstr(*(uint64_t *)(Arg1 + 0xD8), v_rip - 12564913, Arg3, a4);
    if (result != 0) {
        *(uint8_t *)(v_rip + 0x3A1BB0) = 1;
    }
    result = strstr(*(uint64_t *)(Arg1 + 0xD8), v_rip - 12565104, Arg3, a4);
    if (result == 0) goto loc_00C1FE44;
    goto loc_00C1FE2F;
loc_00C1FE1F:
    if (((uint8_t)(*(uint64_t *)(Arg1 + 0xD8))) == 32) goto loc_00C1FE35;
    Arg1 = (uint8_t)((*(uint64_t *)(Arg1 + 0xD8)) - (48));
    if (((uint8_t)(Arg1)) <= 9) goto loc_00C1FE35;
    result = (result) + 1;
loc_00C1FE2F:
    if ((uint8_t)(*(uint8_t *)(result)) != 0) goto loc_00C1FE1F;
loc_00C1FE35:
    result = atoi(result, v_rip - 12565104, Arg3, a4);
    result = HalpInterruptForceClusterMode((uint32_t)((uint32_t)(result)), v_rip - 12565104, Arg3, a4);
loc_00C1FE44:
    result = strstr(*(uint64_t *)(Arg1 + 0xD8), v_rip - 12565099, Arg3, a4);
    if (result == 0) goto loc_00C1FE83;
    goto loc_00C1FE6A;
loc_00C1FE5A:
    if (((uint8_t)(*(uint64_t *)(Arg1 + 0xD8))) == 32) goto loc_00C1FE70;
    Arg1 = (uint8_t)((*(uint64_t *)(Arg1 + 0xD8)) - (48));
    if (((uint8_t)(Arg1)) <= 9) goto loc_00C1FE70;
    result = (result) + 1;
loc_00C1FE6A:
    if ((uint8_t)(*(uint8_t *)(result)) != 0) goto loc_00C1FE5A;
loc_00C1FE70:
    result = atoi(result, v_rip - 12565099, Arg3, a4);
    if (((uint32_t)(result)) >= 1) {
        *(uint32_t *)(v_rip + 0x1F0355) = (uint32_t)(result);
    }
    result = strstr(*(uint64_t *)(Arg1 + 0xD8), v_rip - 12565306, Arg3, a4);
    if (result != 0) {
        *(uint8_t *)(v_rip + 0x1EA8DE) = 1;
    }
    result = strstr(*(uint64_t *)(Arg1 + 0xD8), v_rip - 12565213, Arg3, a4);
    if (result != 0) {
        *(uint8_t *)(v_rip + 0x1EA8C3) = 0;
    }
    result = strstr(*(uint64_t *)(Arg1 + 0xD8), v_rip - 12565304, Arg3, a4);
    if (result != 0) {
        *(uint8_t *)(v_rip + 0x1EA8A8) = 0;
    }
    result = strstr(*(uint64_t *)(Arg1 + 0xD8), v_rip - 12564963, Arg3, a4);
    if (result == 0) goto loc_00C1FEF1;
    *(uint8_t *)(v_rip + 0x3A2271) = 1;
    goto loc_00C1FF0C;
loc_00C1FEF1:
    result = strstr(*(uint64_t *)(Arg1 + 0xD8), v_rip - 12565144, Arg3, a4);
    if (result != 0) {
        *(uint8_t *)(v_rip + 0x3A2264) = 1;
    }
    result = strstr(*(uint64_t *)(Arg1 + 0xD8), v_rip - 12565075, Arg3, a4);
    if (result != 0) {
        *(uint8_t *)(v_rip + 0x1F04D1) = 1;
    }
    result = strstr(*(uint64_t *)(Arg1 + 0xD8), v_rip - 12565310, Arg3, a4);
    if (result == 0) goto loc_00C1FF3F;
    Arg1 = 0;
    goto loc_00C1FF55;
loc_00C1FF3F:
    result = strstr(*(uint64_t *)(Arg1 + 0xD8), v_rip - 12565390, Arg3, a4);
    if (result == 0) goto loc_00C1FF5A;
loc_00C1FF55:
    result = HalpInterruptSetMsiOverride(1, v_rip - 12565390, Arg3, a4);
loc_00C1FF5A:
    result = HalpIsHvPresent(1, v_rip - 12565390, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_00C1FF93;
    *(uint8_t *)(v_rip + 0x3A1F67) = 1;
    result = HalpIsPartitionCpuManager(1, v_rip - 12565390, Arg3, a4);
    if ((uint8_t)(result) != 0) {
        *(uint8_t *)(v_rip + 0x3A1F56) = 1;
    }
    result = HalpIsMicrosoftCompatibleHvLoaded(1, v_rip - 12565390, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_00C1FF93;
    Arg1 = 0;
    result = (uint32_t)(((uint32_t)(0x40000004ULL)) >> (4));
    goto loc_00C1FF9A;
loc_00C1FF93:
    result = HalpIsXboxNanovisorPresent(Arg1, v_rip - 12565390, Arg3, a4);
loc_00C1FF9A:
    if ((uint8_t)(result) != 0) {
        *(uint8_t *)(v_rip + 0x3A21AD) = 1;
    }
    if ((*(uint8_t *)(v_rip + 0x3A1F26)) == 0) goto loc_00C1FFE9;
    v_stack_m28 = 0;
    Arg3 = 0;
    Arg2 = 0;
    Arg1 = 0;
    result = HalpGetCpuInfo(Arg1, Arg2, Arg3, v_stack_m28);
    if ((uint8_t)(result) == 0) goto loc_00C1FFE9;
    if (v_stack_m28 != 2) goto loc_00C1FFE9;
    Arg2 = (Arg2) << (32);
    result = (result) | (Arg2);
    if (!(condition_is_above_or_equal)) {
        *(uint8_t *)(v_rip + 0x3A19D1) = 1;
    }
    result = strstr(*(uint64_t *)(Arg1 + 0xD8), v_rip - 12565448, Arg3, v_stack_m28);
    if (result != 0) goto loc_00C2000F;
    result = HalpIsMicrosoftCompatibleHvLoaded(*(uint64_t *)(Arg1 + 0xD8), v_rip - 12565448, Arg3, v_stack_m28);
    if ((uint8_t)(result) == 0) goto loc_00C20016;
    if ((*(uint8_t *)(v_rip + 0x3A1EC3)) == 0) {
        *(uint8_t *)(v_rip + 0x3A19A4) = 0;
    }
    result = strstr(*(uint64_t *)(Arg1 + 0xD8), v_rip - 12565397, Arg3, v_stack_m28);
    if (result != 0) {
        *(uint8_t *)(v_rip + 0x3A401F) = 1;
    }
    result = strstr(*(uint64_t *)(Arg1 + 0xD8), v_rip - 12565752, Arg3, v_stack_m28);
    if (result != 0) {
        *(uint8_t *)(v_rip + 0x3A40AC) = 1;
    }
    result = strstr(*(uint64_t *)(Arg1 + 0xD8), v_rip - 12565355, Arg3, v_stack_m28);
    if (result == 0) goto loc_00C20097;
    goto loc_00C20072;
loc_00C20062:
    if (((uint8_t)(*(uint64_t *)(Arg1 + 0xD8))) == 32) goto loc_00C20078;
    Arg1 = (uint8_t)((*(uint64_t *)(Arg1 + 0xD8)) - (48));
    if (((uint8_t)(Arg1)) <= 9) goto loc_00C20078;
    result = (result) + 1;
loc_00C20072:
    if ((uint8_t)(*(uint8_t *)(result)) != 0) goto loc_00C20062;
loc_00C20078:
    result = atoi(result, v_rip - 12565355, Arg3, v_stack_m28);
    *(uint32_t *)(v_rip + 0x1EA796) = (uint32_t)(result);
    result = (uint32_t)((result) - 1);
    if (((uint32_t)(result)) >= = 63) {
        *(uint32_t *)(v_rip + 0x1EA785) = 64;
    }
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg1 + 0xF0) + 0x84))) >> (17));
    Arg2 = (uint8_t)((Arg2) & (1));
    *(uint8_t *)(v_rip + 0x1F03AF) = (uint8_t)(Arg2);
    result = strstr(*(uint64_t *)(Arg1 + 0xD8), v_rip - 12565842, Arg3, v_stack_m28);
    result = strstr(*(uint64_t *)(Arg1 + 0xD8), v_rip - 12565542, Arg3, v_stack_m28);
    result = strstr(*(uint64_t *)(Arg1 + 0xD8), v_rip - 12565709, Arg3, v_stack_m28);
loc_00C200DD:
    Arg1 = (v_stack_m10) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_rip - 12565709, Arg3, v_stack_m28);
    local_rsp = (local_rsp) + (64);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C1FD30&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
