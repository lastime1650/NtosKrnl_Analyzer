# HalpTimerSelectRoles

- RVA: `0x0053D4B0`–`0x0053D928` (길이 `1,144` bytes)
- VA: `0x000000014053D4B0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006E5F8`
- 디코드: `258`개 명령, `1,144/1,144` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **29**; 고유 호출 대상: **13**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **25**

### Outgoing calls
- `0x0053D4C4` → [HalpTimerFindIdealScalingSource](HalpTimerFindIdealScalingSource_function_0053C9D0.md) (function, `0x0053C9D0`)
- `0x0053D4D4` → [HalpTimerInitialize](HalpTimerInitialize_function_0053CF38.md) (function, `0x0053CF38`)
- `0x0053D4E0` → [HalpTimerMeasureFrequencies](../54/HalpTimerMeasureFrequencies_function_005493C0.md) (function, `0x005493C0`)
- `0x0053D506` → [HalpTimerFindIdealClockSource](HalpTimerFindIdealClockSource_function_0053C61C.md) (function, `0x0053C61C`)
- `0x0053D51A` → [HalpTimerInitialize](HalpTimerInitialize_function_0053CF38.md) (function, `0x0053CF38`)
- `0x0053D550` → [HalpTimerFindIdealPerformanceCounterSource](HalpTimerFindIdealPerformanceCounterSource_function_0053C880.md) (function, `0x0053C880`)
- `0x0053D564` → [HalpTimerInitialize](HalpTimerInitialize_function_0053CF38.md) (function, `0x0053CF38`)
- `0x0053D577` → [HalpTimerPropagateQpcBiasUpdate](../4A/HalpTimerPropagateQpcBiasUpdate_function_004AB9F4.md) (function, `0x004AB9F4`)
- `0x0053D5F7` → [HalpFindTimer](../54/HalpFindTimer_function_005488D0.md) (function, `0x005488D0`)
- `0x0053D614` → [HalpTimerInitialize](HalpTimerInitialize_function_0053CF38.md) (function, `0x0053CF38`)
- `0x0053D649` → [HalpTimerFindBestAlwaysOnTimer](../54/HalpTimerFindBestAlwaysOnTimer_function_005491F8.md) (function, `0x005491F8`)
- `0x0053D659` → [HalpTimerInitialize](HalpTimerInitialize_function_0053CF38.md) (function, `0x0053CF38`)
- `0x0053D688` → [HalpVpptTimerRegister](../54/HalpVpptTimerRegister_function_0054A42C.md) (function, `0x0054A42C`)
- `0x0053D6A7` → [HalpFindTimer](../54/HalpFindTimer_function_005488D0.md) (function, `0x005488D0`)
- `0x0053D6BF` → [HalpTimerInitialize](HalpTimerInitialize_function_0053CF38.md) (function, `0x0053CF38`)
- `0x0053D700` → [HalpVpptTimerRegister](../54/HalpVpptTimerRegister_function_0054A42C.md) (function, `0x0054A42C`)
- `0x0053D720` → [HalpFindTimer](../54/HalpFindTimer_function_005488D0.md) (function, `0x005488D0`)
- `0x0053D76D` → [HalpTimerFindBestAlwaysOnTimer](../54/HalpTimerFindBestAlwaysOnTimer_function_005491F8.md) (function, `0x005491F8`)
- `0x0053D77D` → [HalpTimerInitialize](HalpTimerInitialize_function_0053CF38.md) (function, `0x0053CF38`)
- `0x0053D7C4` → [HalpFindTimer](../54/HalpFindTimer_function_005488D0.md) (function, `0x005488D0`)
- `0x0053D7D1` → [HalpQueryMaximumRegisteredProcessorCount](../54/HalpQueryMaximumRegisteredProcessorCount_function_00543BE8.md) (function, `0x00543BE8`)
- `0x0053D7F1` → [HalpFindTimer](../54/HalpFindTimer_function_005488D0.md) (function, `0x005488D0`)
- `0x0053D805` → [HalpTimerInitialize](HalpTimerInitialize_function_0053CF38.md) (function, `0x0053CF38`)
- `0x0053D81C` → [HalpTimerStopProfileInterrupt](../54/HalpTimerStopProfileInterrupt_function_0054B8A4.md) (function, `0x0054B8A4`)
- `0x0053D844` → [HalpTimerFindIdealPerformanceCounterSource](HalpTimerFindIdealPerformanceCounterSource_function_0053C880.md) (function, `0x0053C880`)
- `0x0053D854` → [HalpTimerInitialize](HalpTimerInitialize_function_0053CF38.md) (function, `0x0053CF38`)
- `0x0053D887` → [HalpTimerSetProblemEx](../4F/HalpTimerSetProblemEx_function_004FAEC4.md) (function, `0x004FAEC4`)
- `0x0053D8E2` → [HalpTimerFindIdealWatchdog](HalpTimerFindIdealWatchdog_function_0053CAB0.md) (function, `0x0053CAB0`)
- `0x0053D8F2` → [HalpTimerInitialize](HalpTimerInitialize_function_0053CF38.md) (function, `0x0053CF38`)

### Direct callers
- [HalpInitializeTimers](HalpInitializeTimers_function_0053C1E0.md) at `0x0053C2E8`

### Static image references
- `0x0053D4BC` → RVA `0x00FC4138` (`.data`; read)
- `0x0053D4E5` → RVA `0x00FC4138` (`.data`; write)
- `0x0053D4EE` → RVA `0x00E10358` (`.data`; write)
- `0x0053D4FD` → RVA `0x00FC40F0` (`.data`; read)
- `0x0053D52A` → RVA `0x00FC40F0` (`.data`; write)
- `0x0053D531` → RVA `0x00FC3FD0` (`.data`; read)
- `0x0053D570` → RVA `0x00FC3FD0` (`.data`; write)
- `0x0053D583` → RVA `0x00FC4100` (`.data`; read)
- `0x0053D5BE` → RVA `0x00FC4100` (`.data`; write)
- `0x0053D5C5` → RVA `0x00FC4038` (`.data`; read)
- `0x0053D5D8` → RVA `0x00FC4130` (`.data`; read)
- `0x0053D624` → RVA `0x00FC4130` (`.data`; write)
- `0x0053D62B` → RVA `0x00FC4108` (`.data`; read)
- `0x0053D669` → RVA `0x00FC4108` (`.data`; write)
- `0x0053D73C` → RVA `0x00FC4140` (`.data`; read)
- `0x0053D78D` → RVA `0x00FC4140` (`.data`; write)
- `0x0053D794` → RVA `0x00FC3FC0` (`.data`; read)
- `0x0053D7A1` → RVA `0x000071E0` (`.rdata`; read)
- `0x0053D7A8` → RVA `0x00E03B20` (`.data`; read)
- `0x0053D815` → RVA `0x00FC3FC0` (`.data`; write)
- `0x0053D837` → RVA `0x00FC40C0` (`.data`; read)
- `0x0053D864` → RVA `0x00FC40C0` (`.data`; write)
- `0x0053D880` → RVA `0x0001BE98` (`.rdata`; read)
- `0x0053D8DA` → RVA `0x00FC2160` (`.data`; read)
- `0x0053D902` → RVA `0x00FC4028` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0053D4B0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0053D4B5  57                              push rdi
0053D4B6  48 83 EC 30                     sub rsp, 0x30
0053D4BA  33 DB                           xor ebx, ebx
0053D4BC  38 1D 76 6C A8 00               cmp byte ptr [rip + 0xa86c76], bl
0053D4C2  75 39                           jne 0x14053d4fd
0053D4C4  E8 07 F5 FF FF                  call 0x14053c9d0
0053D4C9  48 8B F8                        mov rdi, rax
0053D4CC  48 85 C0                        test rax, rax
0053D4CF  74 1D                           je 0x14053d4ee
0053D4D1  48 8B C8                        mov rcx, rax
0053D4D4  E8 5F FA FF FF                  call 0x14053cf38
0053D4D9  85 C0                           test eax, eax
0053D4DB  78 DF                           js 0x14053d4bc
0053D4DD  48 8B CF                        mov rcx, rdi
0053D4E0  E8 DB BE 00 00                  call 0x1405493c0
0053D4E5  C6 05 4C 6C A8 00 01            mov byte ptr [rip + 0xa86c4c], 1
0053D4EC  EB CE                           jmp 0x14053d4bc
0053D4EE  C7 05 60 2E 8D 00 13 00 00 00   mov dword ptr [rip + 0x8d2e60], 0x13
0053D4F8  E9 18 04 00 00                  jmp 0x14053d915
0053D4FD  48 39 1D EC 6B A8 00            cmp qword ptr [rip + 0xa86bec], rbx
0053D504  75 2B                           jne 0x14053d531
0053D506  E8 11 F1 FF FF                  call 0x14053c61c
0053D50B  48 8B F8                        mov rdi, rax
0053D50E  48 85 C0                        test rax, rax
0053D511  0F 84 91 00 00 00               je 0x14053d5a8
0053D517  48 8B C8                        mov rcx, rax
0053D51A  E8 19 FA FF FF                  call 0x14053cf38
0053D51F  85 C0                           test eax, eax
0053D521  78 DA                           js 0x14053d4fd
0053D523  83 8F B8 00 00 00 04            or dword ptr [rdi + 0xb8], 4
0053D52A  48 89 3D BF 6B A8 00            mov qword ptr [rip + 0xa86bbf], rdi
0053D531  48 8B 0D 98 6A A8 00            mov rcx, qword ptr [rip + 0xa86a98]
0053D538  48 85 C9                        test rcx, rcx
0053D53B  74 13                           je 0x14053d550
0053D53D  8B 81 B8 00 00 00               mov eax, dword ptr [rcx + 0xb8]
0053D543  A8 04                           test al, 4
0053D545  74 09                           je 0x14053d550
0053D547  48 3B 0D A2 6B A8 00            cmp rcx, qword ptr [rip + 0xa86ba2]
0053D54E  75 33                           jne 0x14053d583
0053D550  E8 2B F3 FF FF                  call 0x14053c880
0053D555  48 8B F8                        mov rdi, rax
0053D558  48 85 C0                        test rax, rax
0053D55B  0F 84 AA 03 00 00               je 0x14053d90b
0053D561  48 8B C8                        mov rcx, rax
0053D564  E8 CF F9 FF FF                  call 0x14053cf38
0053D569  85 C0                           test eax, eax
0053D56B  78 C4                           js 0x14053d531
0053D56D  48 8B CF                        mov rcx, rdi
0053D570  48 89 3D 59 6A A8 00            mov qword ptr [rip + 0xa86a59], rdi
0053D577  E8 78 E4 F6 FF                  call 0x1404ab9f4
0053D57C  83 8F B8 00 00 00 04            or dword ptr [rdi + 0xb8], 4
0053D583  48 8B 0D 76 6B A8 00            mov rcx, qword ptr [rip + 0xa86b76]
0053D58A  F7 81 E0 00 00 00 00 20 00 00   test dword ptr [rcx + 0xe0], 0x2000
0053D594  75 21                           jne 0x14053d5b7
0053D596  48 3B 0D 53 6B A8 00            cmp rcx, qword ptr [rip + 0xa86b53]
0053D59D  74 18                           je 0x14053d5b7
0053D59F  83 89 B8 00 00 00 04            or dword ptr [rcx + 0xb8], 4
0053D5A6  EB 1D                           jmp 0x14053d5c5
0053D5A8  C7 05 A6 2D 8D 00 14 00 00 00   mov dword ptr [rip + 0x8d2da6], 0x14
0053D5B2  E9 5E 03 00 00                  jmp 0x14053d915
0053D5B7  48 8B 0D 12 6A A8 00            mov rcx, qword ptr [rip + 0xa86a12]
0053D5BE  48 89 0D 3B 6B A8 00            mov qword ptr [rip + 0xa86b3b], rcx
0053D5C5  48 8B 05 6C 6A A8 00            mov rax, qword ptr [rip + 0xa86a6c]
0053D5CC  48 3B C8                        cmp rcx, rax
0053D5CF  74 07                           je 0x14053d5d8
0053D5D1  83 88 B8 00 00 00 04            or dword ptr [rax + 0xb8], 4
0053D5D8  48 39 1D 51 6B A8 00            cmp qword ptr [rip + 0xa86b51], rbx
0053D5DF  75 4A                           jne 0x14053d62b
0053D5E1  45 33 C9                        xor r9d, r9d
0053D5E4  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
0053D5E8  BA 02 00 10 00                  mov edx, 0x100002
0053D5ED  41 B8 00 60 00 00               mov r8d, 0x6000
0053D5F3  41 8D 49 0F                     lea ecx, [r9 + 0xf]
0053D5F7  E8 D4 B2 00 00                  call 0x1405488d0
0053D5FC  48 8B F8                        mov rdi, rax
0053D5FF  48 85 C0                        test rax, rax
0053D602  74 27                           je 0x14053d62b
0053D604  48 81 B8 C0 00 00 00 00 CA 9A 3B  cmp qword ptr [rax + 0xc0], 0x3b9aca00
0053D60F  77 1A                           ja 0x14053d62b
0053D611  48 8B C8                        mov rcx, rax
0053D614  E8 1F F9 FF FF                  call 0x14053cf38
0053D619  85 C0                           test eax, eax
0053D61B  78 0E                           js 0x14053d62b
0053D61D  83 8F B8 00 00 00 04            or dword ptr [rdi + 0xb8], 4
0053D624  48 89 3D 05 6B A8 00            mov qword ptr [rip + 0xa86b05], rdi
0053D62B  48 39 1D D6 6A A8 00            cmp qword ptr [rip + 0xa86ad6], rbx
0053D632  75 3C                           jne 0x14053d670
0053D634  48 8B 05 B5 6A A8 00            mov rax, qword ptr [rip + 0xa86ab5]
0053D63B  F7 80 E0 00 00 00 00 80 00 00   test dword ptr [rax + 0xe0], 0x8000
0053D645  75 29                           jne 0x14053d670
0053D647  33 C9                           xor ecx, ecx
0053D649  E8 AA BB 00 00                  call 0x1405491f8
0053D64E  48 8B F8                        mov rdi, rax
0053D651  48 85 C0                        test rax, rax
0053D654  74 1A                           je 0x14053d670
0053D656  48 8B C8                        mov rcx, rax
0053D659  E8 DA F8 FF FF                  call 0x14053cf38
0053D65E  85 C0                           test eax, eax
0053D660  78 C9                           js 0x14053d62b
0053D662  83 8F B8 00 00 00 04            or dword ptr [rdi + 0xb8], 4
0053D669  48 89 3D 98 6A A8 00            mov qword ptr [rip + 0xa86a98], rdi
0053D670  48 8B 0D 79 6A A8 00            mov rcx, qword ptr [rip + 0xa86a79]
0053D677  BF 20 00 00 00                  mov edi, 0x20
0053D67C  8B 81 E0 00 00 00               mov eax, dword ptr [rcx + 0xe0]
0053D682  A8 01                           test al, 1
0053D684  75 54                           jne 0x14053d6da
0053D686  33 D2                           xor edx, edx
0053D688  E8 9F CD 00 00                  call 0x14054a42c
0053D68D  85 C0                           test eax, eax
0053D68F  0F 88 FC 01 00 00               js 0x14053d891
0053D695  41 B9 00 0F 00 00               mov r9d, 0xf00
0053D69B  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
0053D69F  45 33 C0                        xor r8d, r8d
0053D6A2  8D 4F EC                        lea ecx, [rdi - 0x14]
0053D6A5  8B D7                           mov edx, edi
0053D6A7  E8 24 B2 00 00                  call 0x1405488d0
0053D6AC  48 89 05 3D 6A A8 00            mov qword ptr [rip + 0xa86a3d], rax
0053D6B3  48 85 C0                        test rax, rax
0053D6B6  0F 84 DF 01 00 00               je 0x14053d89b
0053D6BC  48 8B C8                        mov rcx, rax
0053D6BF  E8 74 F8 FF FF                  call 0x14053cf38
0053D6C4  48 8B 0D 25 6A A8 00            mov rcx, qword ptr [rip + 0xa86a25]
0053D6CB  85 C0                           test eax, eax
0053D6CD  0F 88 9A 01 00 00               js 0x14053d86d
0053D6D3  83 89 B8 00 00 00 04            or dword ptr [rcx + 0xb8], 4
0053D6DA  4C 8B 05 27 6A A8 00            mov r8, qword ptr [rip + 0xa86a27]
0053D6E1  4D 85 C0                        test r8, r8
0053D6E4  74 56                           je 0x14053d73c
0053D6E6  41 8B 80 E0 00 00 00            mov eax, dword ptr [r8 + 0xe0]
0053D6ED  A8 01                           test al, 1
0053D6EF  75 4B                           jne 0x14053d73c
0053D6F1  8B 81 E0 00 00 00               mov eax, dword ptr [rcx + 0xe0]
0053D6F7  A8 01                           test al, 1
0053D6F9  74 41                           je 0x14053d73c
0053D6FB  B2 01                           mov dl, 1
0053D6FD  49 8B C8                        mov rcx, r8
0053D700  E8 27 CD 00 00                  call 0x14054a42c
0053D705  85 C0                           test eax, eax
0053D707  0F 88 A1 01 00 00               js 0x14053d8ae
0053D70D  45 33 C0                        xor r8d, r8d
0053D710  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
0053D714  41 B9 00 0F 00 00               mov r9d, 0xf00
0053D71A  8B D7                           mov edx, edi
0053D71C  41 8D 48 0C                     lea ecx, [r8 + 0xc]
0053D720  E8 AB B1 00 00                  call 0x1405488d0
0053D725  48 89 05 DC 69 A8 00            mov qword ptr [rip + 0xa869dc], rax
0053D72C  48 85 C0                        test rax, rax
0053D72F  0F 84 80 01 00 00               je 0x14053d8b5
0053D735  83 88 B8 00 00 00 04            or dword ptr [rax + 0xb8], 4
0053D73C  48 39 1D FD 69 A8 00            cmp qword ptr [rip + 0xa869fd], rbx
0053D743  75 4F                           jne 0x14053d794
0053D745  48 8B 05 84 68 A8 00            mov rax, qword ptr [rip + 0xa86884]
0053D74C  F7 80 E0 00 00 00 00 80 00 00   test dword ptr [rax + 0xe0], 0x8000
0053D756  74 13                           je 0x14053d76b
0053D758  48 8B 05 A1 69 A8 00            mov rax, qword ptr [rip + 0xa869a1]
0053D75F  F7 80 E0 00 00 00 00 80 00 00   test dword ptr [rax + 0xe0], 0x8000
0053D769  75 29                           jne 0x14053d794
0053D76B  B1 01                           mov cl, 1
0053D76D  E8 86 BA 00 00                  call 0x1405491f8
0053D772  48 8B F8                        mov rdi, rax
0053D775  48 85 C0                        test rax, rax
0053D778  74 1A                           je 0x14053d794
0053D77A  48 8B C8                        mov rcx, rax
0053D77D  E8 B6 F7 FF FF                  call 0x14053cf38
0053D782  85 C0                           test eax, eax
0053D784  78 B6                           js 0x14053d73c
0053D786  83 8F B8 00 00 00 04            or dword ptr [rdi + 0xb8], 4
0053D78D  48 89 3D AC 69 A8 00            mov qword ptr [rip + 0xa869ac], rdi
0053D794  48 39 1D 25 68 A8 00            cmp qword ptr [rip + 0xa86825], rbx
0053D79B  0F 85 80 00 00 00               jne 0x14053d821
0053D7A1  48 8D 05 38 9A AC FF            lea rax, [rip - 0x5365c8]
0053D7A8  48 39 05 71 63 8C 00            cmp qword ptr [rip + 0x8c6371], rax
0053D7AF  75 70                           jne 0x14053d821
0053D7B1  45 33 C0                        xor r8d, r8d
0053D7B4  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
0053D7B8  41 B9 00 0F 00 00               mov r9d, 0xf00
0053D7BE  33 C9                           xor ecx, ecx
0053D7C0  41 8D 50 41                     lea edx, [r8 + 0x41]
0053D7C4  E8 07 B1 00 00                  call 0x1405488d0
0053D7C9  48 8B F8                        mov rdi, rax
0053D7CC  48 85 C0                        test rax, rax
0053D7CF  75 31                           jne 0x14053d802
0053D7D1  E8 12 64 00 00                  call 0x140543be8
0053D7D6  83 F8 01                        cmp eax, 1
0053D7D9  0F 85 E2 00 00 00               jne 0x14053d8c1
0053D7DF  41 B9 00 0F 00 00               mov r9d, 0xf00
0053D7E5  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
0053D7E9  45 33 C0                        xor r8d, r8d
0053D7EC  8D 57 40                        lea edx, [rdi + 0x40]
0053D7EF  33 C9                           xor ecx, ecx
0053D7F1  E8 DA B0 00 00                  call 0x1405488d0
0053D7F6  48 8B F8                        mov rdi, rax
0053D7F9  48 85 C0                        test rax, rax
0053D7FC  0F 84 BF 00 00 00               je 0x14053d8c1
0053D802  48 8B CF                        mov rcx, rdi
0053D805  E8 2E F7 FF FF                  call 0x14053cf38
0053D80A  85 C0                           test eax, eax
0053D80C  78 86                           js 0x14053d794
0053D80E  83 8F B8 00 00 00 04            or dword ptr [rdi + 0xb8], 4
0053D815  48 89 3D A4 67 A8 00            mov qword ptr [rip + 0xa867a4], rdi
0053D81C  E8 83 E0 00 00                  call 0x14054b8a4
0053D821  48 8B 05 A8 67 A8 00            mov rax, qword ptr [rip + 0xa867a8]
0053D828  8B 88 E0 00 00 00               mov ecx, dword ptr [rax + 0xe0]
0053D82E  F6 C1 01                        test cl, 1
0053D831  0F 84 A3 00 00 00               je 0x14053d8da
0053D837  48 39 1D 82 68 A8 00            cmp qword ptr [rip + 0xa86882], rbx
0053D83E  0F 85 96 00 00 00               jne 0x14053d8da
0053D844  E8 37 F0 FF FF                  call 0x14053c880
0053D849  48 8B F8                        mov rdi, rax
0053D84C  48 85 C0                        test rax, rax
0053D84F  74 7F                           je 0x14053d8d0
0053D851  48 8B C8                        mov rcx, rax
0053D854  E8 DF F6 FF FF                  call 0x14053cf38
0053D859  85 C0                           test eax, eax
0053D85B  78 DA                           js 0x14053d837
0053D85D  83 8F B8 00 00 00 04            or dword ptr [rdi + 0xb8], 4
0053D864  48 89 3D 55 68 A8 00            mov qword ptr [rip + 0xa86855], rdi
0053D86B  EB 6D                           jmp 0x14053d8da
0053D86D  C7 44 24 20 71 0D 00 00         mov dword ptr [rsp + 0x20], 0xd71
0053D875  41 B8 02 00 00 00               mov r8d, 2
0053D87B  BA 14 00 00 00                  mov edx, 0x14
0053D880  4C 8D 0D 11 E6 AD FF            lea r9, [rip - 0x5219ef]
0053D887  E8 38 D6 FB FF                  call 0x1404faec4
0053D88C  E9 84 00 00 00                  jmp 0x14053d915
0053D891  48 8B C3                        mov rax, rbx
0053D894  48 89 1D 55 68 A8 00            mov qword ptr [rip + 0xa86855], rbx
0053D89B  C7 44 24 20 65 0D 00 00         mov dword ptr [rsp + 0x20], 0xd65
0053D8A3  41 B8 01 00 00 00               mov r8d, 1
0053D8A9  48 8B C8                        mov rcx, rax
0053D8AC  EB CD                           jmp 0x14053d87b
0053D8AE  48 89 1D 53 68 A8 00            mov qword ptr [rip + 0xa86853], rbx
0053D8B5  C7 05 99 2A 8D 00 21 00 00 00   mov dword ptr [rip + 0x8d2a99], 0x21
0053D8BF  EB 54                           jmp 0x14053d915
0053D8C1  C7 05 8D 2A 8D 00 17 00 00 00   mov dword ptr [rip + 0x8d2a8d], 0x17
0053D8CB  E9 51 FF FF FF                  jmp 0x14053d821
0053D8D0  C7 05 7E 2A 8D 00 16 00 00 00   mov dword ptr [rip + 0x8d2a7e], 0x16
0053D8DA  38 1D 80 48 A8 00               cmp byte ptr [rip + 0xa84880], bl
0053D8E0  75 38                           jne 0x14053d91a
0053D8E2  E8 C9 F1 FF FF                  call 0x14053cab0
0053D8E7  48 8B F8                        mov rdi, rax
0053D8EA  48 85 C0                        test rax, rax
0053D8ED  74 2B                           je 0x14053d91a
0053D8EF  48 8B C8                        mov rcx, rax
0053D8F2  E8 41 F6 FF FF                  call 0x14053cf38
0053D8F7  85 C0                           test eax, eax
0053D8F9  78 1F                           js 0x14053d91a
0053D8FB  83 8F B8 00 00 00 04            or dword ptr [rdi + 0xb8], 4
0053D902  48 89 3D 1F 67 A8 00            mov qword ptr [rip + 0xa8671f], rdi
0053D909  EB 0F                           jmp 0x14053d91a
0053D90B  C7 05 43 2A 8D 00 15 00 00 00   mov dword ptr [rip + 0x8d2a43], 0x15
0053D915  BB 01 00 00 C0                  mov ebx, 0xc0000001
0053D91A  8B C3                           mov eax, ebx
0053D91C  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
0053D921  48 83 C4 30                     add rsp, 0x30
0053D925  5F                              pop rdi
0053D926  C3                              ret
0053D927  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpTimerSelectRoles(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned int v_stack_m18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (48);
    v_rbx = 0;
loc_0053D4BC:
    if ((*(unsigned __int8 *)(v_rip + 11037814)) != 0) goto loc_0053D4FD;
    result = HalpTimerFindIdealScalingSource(a1, a2, a3, a4);
    if (result == 0) goto loc_0053D4EE;
    result = HalpTimerInitialize(result, a2, a3, a4);
    if (sign_flag) goto loc_0053D4BC;
    result = HalpTimerMeasureFrequencies(result, a2, a3, a4);
    *(unsigned __int8 *)(v_rip + 11037772) = 1;
    goto loc_0053D4BC;
loc_0053D4EE:
    *(unsigned int *)(v_rip + 9252448) = 19;
    goto loc_0053D915;
loc_0053D4FD:
    if ((*(unsigned __int64 *)(v_rip + 11037676)) != 0) goto loc_0053D531;
    result = HalpTimerFindIdealClockSource(result, a2, a3, a4);
    if (result == 0) goto loc_0053D5A8;
    result = HalpTimerInitialize(result, a2, a3, a4);
    if (sign_flag) goto loc_0053D4FD;
    *(unsigned __int64 *)(v_rip + 11037631) = result;
loc_0053D531:
    if (*(unsigned __int64 *)(v_rip + 11037336) == 0) goto loc_0053D550;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11037336) + 184)))) & (4)) == 0) goto loc_0053D550;
    if ((*(unsigned __int64 *)(v_rip + 11037336)) != (*(unsigned __int64 *)(v_rip + 11037602))) goto loc_0053D583;
loc_0053D550:
    result = HalpTimerFindIdealPerformanceCounterSource(*(unsigned __int64 *)(v_rip + 11037336), a2, a3, a4);
    if (result == 0) goto loc_0053D90B;
    result = HalpTimerInitialize(result, a2, a3, a4);
    if (sign_flag) goto loc_0053D531;
    *(unsigned __int64 *)(v_rip + 11037273) = result;
    result = HalpTimerPropagateQpcBiasUpdate(result, a2, a3, a4);
loc_0053D583:
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11037558) + 224)) & (0x2000ULL)) != 0) goto loc_0053D5B7;
    if ((*(unsigned __int64 *)(v_rip + 11037558)) == (*(unsigned __int64 *)(v_rip + 11037523))) goto loc_0053D5B7;
    goto loc_0053D5C5;
loc_0053D5A8:
    *(unsigned int *)(v_rip + 9252262) = 20;
    goto loc_0053D915;
loc_0053D5B7:
    *(unsigned __int64 *)(v_rip + 11037499) = *(unsigned __int64 *)(v_rip + 11037202);
loc_0053D5C5:
    if ((*(unsigned __int64 *)(v_rip + 11037202)) != (*(unsigned __int64 *)(v_rip + 11037292))) {
    }
    if ((*(unsigned __int64 *)(v_rip + 11037521)) != 0) goto loc_0053D62B;
    a4 = 0;
    v_stack_m18 = 0;
    result = HalpFindTimer(a4 + 15, (unsigned int)(0x100002ULL), (unsigned int)(0x6000ULL), a4);
    if (result == 0) goto loc_0053D62B;
    if ((*(unsigned __int64 *)(result + 192)) > 0x3B9ACA00ULL) goto loc_0053D62B;
    result = HalpTimerInitialize(result, (unsigned int)(0x100002ULL), (unsigned int)(0x6000ULL), a4);
    if (!(sign_flag)) {
        *(unsigned __int64 *)(v_rip + 11037445) = result;
    }
    if ((*(unsigned __int64 *)(v_rip + 11037398)) != 0) goto loc_0053D670;
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11037365) + 224)) & (0x8000ULL)) != 0) goto loc_0053D670;
    a1 = 0;
    result = HalpTimerFindBestAlwaysOnTimer(a1, (unsigned int)(0x100002ULL), (unsigned int)(0x6000ULL), a4);
    if (result == 0) goto loc_0053D670;
    result = HalpTimerInitialize(result, (unsigned int)(0x100002ULL), (unsigned int)(0x6000ULL), a4);
    if (sign_flag) goto loc_0053D62B;
    *(unsigned __int64 *)(v_rip + 11037336) = result;
loc_0053D670:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11037305) + 224)))) & (1)) != 0) goto loc_0053D6DA;
    a2 = 0;
    result = HalpVpptTimerRegister(*(unsigned __int64 *)(v_rip + 11037305), a2, (unsigned int)(0x6000ULL), a4);
    if (sign_flag) goto loc_0053D891;
    v_stack_m18 = 0;
    a3 = 0;
    result = HalpFindTimer(32 - 20, 32, a3, (unsigned int)(0xF00ULL));
    *(unsigned __int64 *)(v_rip + 11037245) = result;
    if (result == 0) goto loc_0053D89B;
    result = HalpTimerInitialize(result, 32, a3, (unsigned int)(0xF00ULL));
    if (sign_flag) goto loc_0053D86D;
loc_0053D6DA:
    if (*(unsigned __int64 *)(v_rip + 11037223) == 0) goto loc_0053D73C;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11037223) + 224)))) & (1)) != 0) goto loc_0053D73C;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11037221) + 224)))) & (1)) == 0) goto loc_0053D73C;
    result = HalpVpptTimerRegister(*(unsigned __int64 *)(v_rip + 11037223), 1, *(unsigned __int64 *)(v_rip + 11037223), (unsigned int)(0xF00ULL));
    if (sign_flag) goto loc_0053D8AE;
    a3 = 0;
    v_stack_m18 = 0;
    result = HalpFindTimer(a3 + 12, 32, a3, (unsigned int)(0xF00ULL));
    *(unsigned __int64 *)(v_rip + 11037148) = result;
    if (result == 0) goto loc_0053D8B5;
loc_0053D73C:
    if ((*(unsigned __int64 *)(v_rip + 11037181)) != 0) goto loc_0053D794;
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11036804) + 224)) & (0x8000ULL)) == 0) goto loc_0053D76B;
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11037089) + 224)) & (0x8000ULL)) != 0) goto loc_0053D794;
loc_0053D76B:
    result = HalpTimerFindBestAlwaysOnTimer(1, 32, a3, (unsigned int)(0xF00ULL));
    if (result == 0) goto loc_0053D794;
    result = HalpTimerInitialize(result, 32, a3, (unsigned int)(0xF00ULL));
    if (sign_flag) goto loc_0053D73C;
    *(unsigned __int64 *)(v_rip + 11037100) = result;
loc_0053D794:
    if ((*(unsigned __int64 *)(v_rip + 11036709)) != 0) goto loc_0053D821;
    if ((*(unsigned __int64 *)(v_rip + 9200497)) != (v_rip - 5465544)) goto loc_0053D821;
    a3 = 0;
    v_stack_m18 = 0;
    a1 = 0;
    result = HalpFindTimer(a1, a3 + 65, a3, (unsigned int)(0xF00ULL));
    if (result != 0) goto loc_0053D802;
    result = HalpQueryMaximumRegisteredProcessorCount(a1, a3 + 65, a3, (unsigned int)(0xF00ULL));
    if (((unsigned int)(result)) != 1) goto loc_0053D8C1;
    v_stack_m18 = 0;
    a3 = 0;
    a1 = 0;
    result = HalpFindTimer(a1, result + 64, a3, (unsigned int)(0xF00ULL));
    if (result == 0) goto loc_0053D8C1;
loc_0053D802:
    result = HalpTimerInitialize(result, result + 64, a3, (unsigned int)(0xF00ULL));
    if (sign_flag) goto loc_0053D794;
    *(unsigned __int64 *)(v_rip + 11036580) = result;
    result = HalpTimerStopProfileInterrupt(result, result + 64, a3, (unsigned int)(0xF00ULL));
loc_0053D821:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11036584) + 224)))) & (1)) == 0) goto loc_0053D8DA;
loc_0053D837:
    if ((*(unsigned __int64 *)(v_rip + 11036802)) != 0) goto loc_0053D8DA;
    result = HalpTimerFindIdealPerformanceCounterSource((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11036584) + 224)), result + 64, a3, (unsigned int)(0xF00ULL));
    if (result == 0) goto loc_0053D8D0;
    result = HalpTimerInitialize(result, result + 64, a3, (unsigned int)(0xF00ULL));
    if (sign_flag) goto loc_0053D837;
    *(unsigned __int64 *)(v_rip + 11036757) = result;
    goto loc_0053D8DA;
loc_0053D86D:
    v_stack_m18 = 0xD71ULL;
loc_0053D87B:
    result = HalpTimerSetProblemEx(result, 20, 2, v_rip - 5380591);
    goto loc_0053D915;
loc_0053D891:
    *(unsigned __int64 *)(v_rip + 11036757) = 0;
loc_0053D89B:
    v_stack_m18 = 0xD65ULL;
    goto loc_0053D87B;
loc_0053D8AE:
    *(unsigned __int64 *)(v_rip + 11036755) = 0;
loc_0053D8B5:
    *(unsigned int *)(v_rip + 9251481) = 33;
    goto loc_0053D915;
loc_0053D8C1:
    *(unsigned int *)(v_rip + 9251469) = 23;
    goto loc_0053D821;
loc_0053D8D0:
    *(unsigned int *)(v_rip + 9251454) = 22;
loc_0053D8DA:
    if ((*(unsigned __int8 *)(v_rip + 11028608)) != 0) goto loc_0053D91A;
    result = HalpTimerFindIdealWatchdog(0, 20, 1, v_rip - 5380591);
    if (result == 0) goto loc_0053D91A;
    result = HalpTimerInitialize(result, 20, 1, v_rip - 5380591);
    if (sign_flag) goto loc_0053D91A;
    *(unsigned __int64 *)(v_rip + 11036447) = result;
    goto loc_0053D91A;
loc_0053D90B:
    *(unsigned int *)(v_rip + 9251395) = 21;
loc_0053D915:
loc_0053D91A:
    v_rsp = (v_rsp) + (48);
    return (unsigned int)((unsigned int)((unsigned int)(0xC0000001ULL)));
}
```

## 5. (Beta) C Style

```c
int64_t HalpTimerSelectRoles(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint32_t v_stack_m18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (48);
    local_rbx = 0;
loc_0053D4BC:
    if ((*(uint8_t *)(v_rip + 0xA86C76)) != 0) goto loc_0053D4FD;
    result = HalpTimerFindIdealScalingSource(Arg1, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_0053D4EE;
    result = HalpTimerInitialize(result, Arg2, Arg3, Arg4);
    if (sign_flag) goto loc_0053D4BC;
    result = HalpTimerMeasureFrequencies(result, Arg2, Arg3, Arg4);
    *(uint8_t *)(v_rip + 0xA86C4C) = 1;
    goto loc_0053D4BC;
loc_0053D4EE:
    *(uint32_t *)(v_rip + 0x8D2E60) = 19;
    goto loc_0053D915;
loc_0053D4FD:
    if ((*(uint64_t *)(v_rip + 0xA86BEC)) != 0) goto loc_0053D531;
    result = HalpTimerFindIdealClockSource(result, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_0053D5A8;
    result = HalpTimerInitialize(result, Arg2, Arg3, Arg4);
    if (sign_flag) goto loc_0053D4FD;
    *(uint64_t *)(v_rip + 0xA86BBF) = result;
loc_0053D531:
    if (*(uint64_t *)(v_rip + 0xA86A98) == 0) goto loc_0053D550;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA86A98) + 0xB8)))) & (4)) == 0) goto loc_0053D550;
    if ((*(uint64_t *)(v_rip + 0xA86A98)) != (*(uint64_t *)(v_rip + 0xA86BA2))) goto loc_0053D583;
loc_0053D550:
    result = HalpTimerFindIdealPerformanceCounterSource(*(uint64_t *)(v_rip + 0xA86A98), Arg2, Arg3, Arg4);
    if (result == 0) goto loc_0053D90B;
    result = HalpTimerInitialize(result, Arg2, Arg3, Arg4);
    if (sign_flag) goto loc_0053D531;
    *(uint64_t *)(v_rip + 0xA86A59) = result;
    result = HalpTimerPropagateQpcBiasUpdate(result, Arg2, Arg3, Arg4);
loc_0053D583:
    if (((*(uint32_t *)(*(uint64_t *)(v_rip + 0xA86B76) + 0xE0)) & (0x2000ULL)) != 0) goto loc_0053D5B7;
    if ((*(uint64_t *)(v_rip + 0xA86B76)) == (*(uint64_t *)(v_rip + 0xA86B53))) goto loc_0053D5B7;
    goto loc_0053D5C5;
loc_0053D5A8:
    *(uint32_t *)(v_rip + 0x8D2DA6) = 20;
    goto loc_0053D915;
loc_0053D5B7:
    *(uint64_t *)(v_rip + 0xA86B3B) = *(uint64_t *)(v_rip + 0xA86A12);
loc_0053D5C5:
    if ((*(uint64_t *)(v_rip + 0xA86A12)) != (*(uint64_t *)(v_rip + 0xA86A6C))) {
    }
    if ((*(uint64_t *)(v_rip + 0xA86B51)) != 0) goto loc_0053D62B;
    Arg4 = 0;
    v_stack_m18 = 0;
    result = HalpFindTimer(Arg4 + 15, (uint32_t)(0x100002ULL), (uint32_t)(0x6000ULL), Arg4);
    if (result == 0) goto loc_0053D62B;
    if ((*(uint64_t *)(result + 0xC0)) > 0x3B9ACA00ULL) goto loc_0053D62B;
    result = HalpTimerInitialize(result, (uint32_t)(0x100002ULL), (uint32_t)(0x6000ULL), Arg4);
    if (!(sign_flag)) {
        *(uint64_t *)(v_rip + 0xA86B05) = result;
    }
    if ((*(uint64_t *)(v_rip + 0xA86AD6)) != 0) goto loc_0053D670;
    if (((*(uint32_t *)(*(uint64_t *)(v_rip + 0xA86AB5) + 0xE0)) & (0x8000ULL)) != 0) goto loc_0053D670;
    Arg1 = 0;
    result = HalpTimerFindBestAlwaysOnTimer(Arg1, (uint32_t)(0x100002ULL), (uint32_t)(0x6000ULL), Arg4);
    if (result == 0) goto loc_0053D670;
    result = HalpTimerInitialize(result, (uint32_t)(0x100002ULL), (uint32_t)(0x6000ULL), Arg4);
    if (sign_flag) goto loc_0053D62B;
    *(uint64_t *)(v_rip + 0xA86A98) = result;
loc_0053D670:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA86A79) + 0xE0)))) & (1)) != 0) goto loc_0053D6DA;
    Arg2 = 0;
    result = HalpVpptTimerRegister(*(uint64_t *)(v_rip + 0xA86A79), Arg2, (uint32_t)(0x6000ULL), Arg4);
    if (sign_flag) goto loc_0053D891;
    v_stack_m18 = 0;
    Arg3 = 0;
    result = HalpFindTimer(32 - 20, 32, Arg3, (uint32_t)(0xF00ULL));
    *(uint64_t *)(v_rip + 0xA86A3D) = result;
    if (result == 0) goto loc_0053D89B;
    result = HalpTimerInitialize(result, 32, Arg3, (uint32_t)(0xF00ULL));
    if (sign_flag) goto loc_0053D86D;
loc_0053D6DA:
    if (*(uint64_t *)(v_rip + 0xA86A27) == 0) goto loc_0053D73C;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA86A27) + 0xE0)))) & (1)) != 0) goto loc_0053D73C;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA86A25) + 0xE0)))) & (1)) == 0) goto loc_0053D73C;
    result = HalpVpptTimerRegister(*(uint64_t *)(v_rip + 0xA86A27), 1, *(uint64_t *)(v_rip + 0xA86A27), (uint32_t)(0xF00ULL));
    if (sign_flag) goto loc_0053D8AE;
    Arg3 = 0;
    v_stack_m18 = 0;
    result = HalpFindTimer(Arg3 + 12, 32, Arg3, (uint32_t)(0xF00ULL));
    *(uint64_t *)(v_rip + 0xA869DC) = result;
    if (result == 0) goto loc_0053D8B5;
loc_0053D73C:
    if ((*(uint64_t *)(v_rip + 0xA869FD)) != 0) goto loc_0053D794;
    if (((*(uint32_t *)(*(uint64_t *)(v_rip + 0xA86884) + 0xE0)) & (0x8000ULL)) == 0) goto loc_0053D76B;
    if (((*(uint32_t *)(*(uint64_t *)(v_rip + 0xA869A1) + 0xE0)) & (0x8000ULL)) != 0) goto loc_0053D794;
loc_0053D76B:
    result = HalpTimerFindBestAlwaysOnTimer(1, 32, Arg3, (uint32_t)(0xF00ULL));
    if (result == 0) goto loc_0053D794;
    result = HalpTimerInitialize(result, 32, Arg3, (uint32_t)(0xF00ULL));
    if (sign_flag) goto loc_0053D73C;
    *(uint64_t *)(v_rip + 0xA869AC) = result;
loc_0053D794:
    if ((*(uint64_t *)(v_rip + 0xA86825)) != 0) goto loc_0053D821;
    if ((*(uint64_t *)(v_rip + 0x8C6371)) != (v_rip - 5465544)) goto loc_0053D821;
    Arg3 = 0;
    v_stack_m18 = 0;
    Arg1 = 0;
    result = HalpFindTimer(Arg1, Arg3 + 65, Arg3, (uint32_t)(0xF00ULL));
    if (result != 0) goto loc_0053D802;
    result = HalpQueryMaximumRegisteredProcessorCount(Arg1, Arg3 + 65, Arg3, (uint32_t)(0xF00ULL));
    if (((uint32_t)(result)) != 1) goto loc_0053D8C1;
    v_stack_m18 = 0;
    Arg3 = 0;
    Arg1 = 0;
    result = HalpFindTimer(Arg1, result + 64, Arg3, (uint32_t)(0xF00ULL));
    if (result == 0) goto loc_0053D8C1;
loc_0053D802:
    result = HalpTimerInitialize(result, result + 64, Arg3, (uint32_t)(0xF00ULL));
    if (sign_flag) goto loc_0053D794;
    *(uint64_t *)(v_rip + 0xA867A4) = result;
    result = HalpTimerStopProfileInterrupt(result, result + 64, Arg3, (uint32_t)(0xF00ULL));
loc_0053D821:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA867A8) + 0xE0)))) & (1)) == 0) goto loc_0053D8DA;
loc_0053D837:
    if ((*(uint64_t *)(v_rip + 0xA86882)) != 0) goto loc_0053D8DA;
    result = HalpTimerFindIdealPerformanceCounterSource((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA867A8) + 0xE0)), result + 64, Arg3, (uint32_t)(0xF00ULL));
    if (result == 0) goto loc_0053D8D0;
    result = HalpTimerInitialize(result, result + 64, Arg3, (uint32_t)(0xF00ULL));
    if (sign_flag) goto loc_0053D837;
    *(uint64_t *)(v_rip + 0xA86855) = result;
    goto loc_0053D8DA;
loc_0053D86D:
    v_stack_m18 = 0xD71ULL;
loc_0053D87B:
    result = HalpTimerSetProblemEx(result, 20, 2, v_rip - 5380591);
    goto loc_0053D915;
loc_0053D891:
    *(uint64_t *)(v_rip + 0xA86855) = 0;
loc_0053D89B:
    v_stack_m18 = 0xD65ULL;
    goto loc_0053D87B;
loc_0053D8AE:
    *(uint64_t *)(v_rip + 0xA86853) = 0;
loc_0053D8B5:
    *(uint32_t *)(v_rip + 0x8D2A99) = 33;
    goto loc_0053D915;
loc_0053D8C1:
    *(uint32_t *)(v_rip + 0x8D2A8D) = 23;
    goto loc_0053D821;
loc_0053D8D0:
    *(uint32_t *)(v_rip + 0x8D2A7E) = 22;
loc_0053D8DA:
    if ((*(uint8_t *)(v_rip + 0xA84880)) != 0) goto loc_0053D91A;
    result = HalpTimerFindIdealWatchdog(0, 20, 1, v_rip - 5380591);
    if (result == 0) goto loc_0053D91A;
    result = HalpTimerInitialize(result, 20, 1, v_rip - 5380591);
    if (sign_flag) goto loc_0053D91A;
    *(uint64_t *)(v_rip + 0xA8671F) = result;
    goto loc_0053D91A;
loc_0053D90B:
    *(uint32_t *)(v_rip + 0x8D2A43) = 21;
loc_0053D915:
loc_0053D91A:
    local_rsp = (local_rsp) + (48);
    return (uint32_t)((uint32_t)((uint32_t)(0xC0000001ULL)));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0053D4B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
