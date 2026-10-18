# sub_006DCEEE

- RVA: `0x006DCEEE`–`0x006DD377` (길이 `1,161` bytes)
- VA: `0x00000001406DCEEE`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006F760`
- 디코드: `273`개 명령, `1,161/1,161` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **14**; 고유 호출 대상: **12**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **11**

### Outgoing calls
- `0x006DCF30` → [KiSetClockTimer](../39/KiSetClockTimer_function_0039DB2C.md) (function, `0x0039DB2C`)
- `0x006DCF9B` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006DCFC8` → [PpmIdleSetSynchronizationState](../4D/PpmIdleSetSynchronizationState_function_004D9958.md) (function, `0x004D9958`)
- `0x006DCFF7` → [PpmIdleRecheckCoordinatedIdleMask](../5D/PpmIdleRecheckCoordinatedIdleMask_function_005D00FC.md) (function, `0x005D00FC`)
- `0x006DD05D` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006DD0A6` → [PpmIdlePrepareExitLatencyTrace](../5C/PpmIdlePrepareExitLatencyTrace_function_005CFFB8.md) (function, `0x005CFFB8`)
- `0x006DD120` → [KePrepareClockTimerForPlatformIdle](../5B/KePrepareClockTimerForPlatformIdle_function_005BA820.md) (function, `0x005BA820`)
- `0x006DD135` → [KePrepareClockTimerForIdle](../5B/KePrepareClockTimerForIdle_function_005BA49C.md) (function, `0x005BA49C`)
- `0x006DD287` → [KeQueryWakeSource](../5B/KeQueryWakeSource_function_005B19AC.md) (function, `0x005B19AC`)
- `0x006DD2E1` → [KeWakeProcessor](../5B/KeWakeProcessor_function_005BE080.md) (function, `0x005BE080`)
- `0x006DD31D` → [KeResumeClockTimerFromIdle](../5B/KeResumeClockTimerFromIdle_function_005BACC4.md) (function, `0x005BACC4`)
- `0x006DD329` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006DD35E` → [KeAccumulateTicks](../39/KeAccumulateTicks_function_0039C140.md) (function, `0x0039C140`)
- `0x006DD36C` → [PpmCancelExitLatencyTrace](../5C/PpmCancelExitLatencyTrace_function_005CF47C.md) (function, `0x005CF47C`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x006DCEEE` → RVA `0x00FC6A85` (`ALMOSTRO`; read)
- `0x006DCF91` → RVA `0x00E009A0` (`.data`; read)
- `0x006DD034` → RVA `0x00E67684` (`.data`; read/write)
- `0x006DD044` → RVA `0x00FCF000` (`CACHEALI`; read)
- `0x006DD04A` → RVA `0x00F21FB0` (`.data`; read)
- `0x006DD056` → RVA `0x00E00AE8` (`.data`; read)
- `0x006DD07A` → RVA `0x00F21F24` (`.data`; read/write)
- `0x006DD0C8` → RVA `0x00E0B3B4` (`.data`; read)
- `0x006DD251` → RVA `0x00FC6AD0` (`ALMOSTRO`; read)
- `0x006DD298` → RVA `0x00FC6AFA` (`ALMOSTRO`; read)
- `0x006DD322` → RVA `0x00E009B0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **12**
  - `0x006DCF3C` → [PpmIdleExecuteTransition + 0x134](../2D/PpmIdleExecuteTransition_function_002D0A1C.md) (`tail-transfer`)
  - `0x006DCF5C` → [PpmIdleExecuteTransition + 0x134](../2D/PpmIdleExecuteTransition_function_002D0A1C.md) (`tail-transfer`)
  - `0x006DCFD9` → [PpmIdleExecuteTransition + 0x1E0](../2D/PpmIdleExecuteTransition_function_002D0A1C.md) (`tail-transfer`)
  - `0x006DD16D` → [PpmIdleExecuteTransition + 0x145](../2D/PpmIdleExecuteTransition_function_002D0A1C.md) (`tail-transfer`)
  - `0x006DD176` → [PpmIdleExecuteTransition + 0x145](../2D/PpmIdleExecuteTransition_function_002D0A1C.md) (`tail-transfer`)
  - `0x006DD180` → [PpmIdleExecuteTransition + 0x37D](../2D/PpmIdleExecuteTransition_function_002D0A1C.md) (`tail-transfer`)
  - `0x006DD217` → [PpmIdleExecuteTransition + 0x4E1](../2D/PpmIdleExecuteTransition_function_002D0A1C.md) (`tail-transfer`)
  - `0x006DD229` → [PpmIdleExecuteTransition + 0x4E1](../2D/PpmIdleExecuteTransition_function_002D0A1C.md) (`tail-transfer`)
  - `0x006DD235` → [PpmIdleExecuteTransition + 0x1D6](../2D/PpmIdleExecuteTransition_function_002D0A1C.md) (`tail-transfer`)
  - `0x006DD23E` → [PpmIdleExecuteTransition + 0x203](../2D/PpmIdleExecuteTransition_function_002D0A1C.md) (`tail-transfer`)
  - `0x006DD364` → [PpmIdleExecuteTransition + 0x21B](../2D/PpmIdleExecuteTransition_function_002D0A1C.md) (`tail-transfer`)
  - `0x006DD372` → [PpmIdleExecuteTransition + 0x2C7](../2D/PpmIdleExecuteTransition_function_002D0A1C.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006DCEEE  44 38 1D 90 9B 8E 00            cmp byte ptr [rip + 0x8e9b90], r11b
006DCEF5  48 8B 95 C0 00 00 00            mov rdx, qword ptr [rbp + 0xc0]
006DCEFC  44 88 4C 24 56                  mov byte ptr [rsp + 0x56], r9b
006DCF01  48 8D 0C 10                     lea rcx, [rax + rdx]
006DCF05  48 89 4C 24 78                  mov qword ptr [rsp + 0x78], rcx
006DCF0A  74 35                           je 0x1406dcf41
006DCF0C  44 38 9F CC 02 00 00            cmp byte ptr [rdi + 0x2cc], r11b
006DCF13  4C 8B C1                        mov r8, rcx
006DCF16  48 8B CB                        mov rcx, rbx
006DCF19  0F 94 C0                        sete al
006DCF1C  45 33 C9                        xor r9d, r9d
006DCF1F  88 44 24 30                     mov byte ptr [rsp + 0x30], al
006DCF23  44 88 5C 24 28                  mov byte ptr [rsp + 0x28], r11b
006DCF28  C7 44 24 20 05 00 00 00         mov dword ptr [rsp + 0x20], 5
006DCF30  E8 F7 0B CC FF                  call 0x14039db2c
006DCF35  45 33 DB                        xor r11d, r11d
006DCF38  45 8D 4B 01                     lea r9d, [r11 + 1]
006DCF3C  E9 0F 3C BF FF                  jmp 0x1402d0b50
006DCF41  48 89 8B 70 88 00 00            mov qword ptr [rbx + 0x8870], rcx
006DCF48  48 8B 8B C0 00 00 00            mov rcx, qword ptr [rbx + 0xc0]
006DCF4F  0F B6 83 D1 00 00 00            movzx eax, byte ptr [rbx + 0xd1]
006DCF56  F0 48 0F AB 41 48               lock bts qword ptr [rcx + 0x48], rax
006DCF5C  E9 EF 3B BF FF                  jmp 0x1402d0b50
006DCF61  4C 8B 83 C8 00 00 00            mov r8, qword ptr [rbx + 0xc8]
006DCF68  48 8B 93 C0 00 00 00            mov rdx, qword ptr [rbx + 0xc0]
006DCF6F  44 88 4C 24 54                  mov byte ptr [rsp + 0x54], r9b
006DCF74  0F 0D 4A 40                     prefetchw byte ptr [rdx + 0x40]
006DCF78  48 8B 42 40                     mov rax, qword ptr [rdx + 0x40]
006DCF7C  48 8B C8                        mov rcx, rax
006DCF7F  49 0B C8                        or rcx, r8
006DCF82  F0 48 0F B1 4A 40               lock cmpxchg qword ptr [rdx + 0x40], rcx
006DCF88  75 F2                           jne 0x1406dcf7c
006DCF8A  41 0F B6 CE                     movzx ecx, r14b
006DCF8E  48 8B F0                        mov rsi, rax
006DCF91  48 8B 05 08 3A 72 00            mov rax, qword ptr [rip + 0x723a08]
006DCF98  41 33 C9                        xor ecx, r9d
006DCF9B  E8 30 DB FD FF                  call 0x1406baad0
006DCFA0  44 8B F8                        mov r15d, eax
006DCFA3  45 33 DB                        xor r11d, r11d
006DCFA6  8B 83 58 38 00 00               mov eax, dword ptr [rbx + 0x3858]
006DCFAC  85 C0                           test eax, eax
006DCFAE  74 2E                           je 0x1406dcfde
006DCFB0  41 BF 11 00 00 80               mov r15d, 0x80000011
006DCFB6  44 38 9D C8 00 00 00            cmp byte ptr [rbp + 0xc8], r11b
006DCFBD  74 0E                           je 0x1406dcfcd
006DCFBF  33 D2                           xor edx, edx
006DCFC1  48 8D 8B 8C 88 00 00            lea rcx, [rbx + 0x888c]
006DCFC8  E8 8B C9 DF FF                  call 0x1404d9958
006DCFCD  B9 01 00 00 00                  mov ecx, 1
006DCFD2  44 8A E9                        mov r13b, cl
006DCFD5  88 4C 24 52                     mov byte ptr [rsp + 0x52], cl
006DCFD9  E9 1E 3C BF FF                  jmp 0x1402d0bfc
006DCFDE  45 85 FF                        test r15d, r15d
006DCFE1  78 D3                           js 0x1406dcfb6
006DCFE3  48 0B B3 C8 00 00 00            or rsi, qword ptr [rbx + 0xc8]
006DCFEA  48 8B CF                        mov rcx, rdi
006DCFED  0F B6 93 D0 00 00 00            movzx edx, byte ptr [rbx + 0xd0]
006DCFF4  4C 8B C6                        mov r8, rsi
006DCFF7  E8 00 31 EF FF                  call 0x1405d00fc
006DCFFC  45 33 DB                        xor r11d, r11d
006DCFFF  84 C0                           test al, al
006DD001  74 08                           je 0x1406dd00b
006DD003  41 BF 16 00 00 C0               mov r15d, 0xc0000016
006DD009  EB AB                           jmp 0x1406dcfb6
006DD00B  44 8B A5 B0 00 00 00            mov r12d, dword ptr [rbp + 0xb0]
006DD012  44 38 9D D8 00 00 00            cmp byte ptr [rbp + 0xd8], r11b
006DD019  74 0B                           je 0x1406dd026
006DD01B  45 85 E4                        test r12d, r12d
006DD01E  75 06                           jne 0x1406dd026
006DD020  41 BF 80 00 00 00               mov r15d, 0x80
006DD026  45 84 F6                        test r14b, r14b
006DD029  74 5F                           je 0x1406dd08a
006DD02B  B9 01 00 00 00                  mov ecx, 1
006DD030  88 4C 24 57                     mov byte ptr [rsp + 0x57], cl
006DD034  F0 01 0D 49 A6 78 00            lock add dword ptr [rip + 0x78a649], ecx
006DD03B  65 48 8B 34 25 20 00 00 00      mov rsi, qword ptr gs:[0x20]
006DD044  8B 05 B6 1F 8F 00               mov eax, dword ptr [rip + 0x8f1fb6]
006DD04A  44 8B 35 5F 4F 84 00            mov r14d, dword ptr [rip + 0x844f5f]
006DD051  84 4E 22                        test byte ptr [rsi + 0x22], cl
006DD054  74 1E                           je 0x1406dd074
006DD056  48 8B 05 8B 3A 72 00            mov rax, qword ptr [rip + 0x723a8b]
006DD05D  E8 6E DA FD FF                  call 0x1406baad0
006DD062  45 33 DB                        xor r11d, r11d
006DD065  44 88 9E 08 96 00 00            mov byte ptr [rsi + 0x9608], r11b
006DD06C  80 66 22 FE                     and byte ptr [rsi + 0x22], 0xfe
006DD070  41 8D 4B 01                     lea ecx, [r11 + 1]
006DD074  44 39 76 24                     cmp dword ptr [rsi + 0x24], r14d
006DD078  75 06                           jne 0x1406dd080
006DD07A  01 0D A4 4E 84 00               add dword ptr [rip + 0x844ea4], ecx
006DD080  44 38 5E 21                     cmp byte ptr [rsi + 0x21], r11b
006DD084  74 04                           je 0x1406dd08a
006DD086  44 88 5E 21                     mov byte ptr [rsi + 0x21], r11b
006DD08A  48 83 4C 24 78 FF               or qword ptr [rsp + 0x78], 0xffffffffffffffff
006DD090  44 38 9F CC 02 00 00            cmp byte ptr [rdi + 0x2cc], r11b
006DD097  0F 84 8A 00 00 00               je 0x1406dd127
006DD09D  8B 74 24 68                     mov esi, dword ptr [rsp + 0x68]
006DD0A1  48 8B CF                        mov rcx, rdi
006DD0A4  8B D6                           mov edx, esi
006DD0A6  E8 0D 2F EF FF                  call 0x1405cffb8
006DD0AB  88 44 24 55                     mov byte ptr [rsp + 0x55], al
006DD0AF  84 C0                           test al, al
006DD0B1  74 09                           je 0x1406dd0bc
006DD0B3  B9 00 02 00 00                  mov ecx, 0x200
006DD0B8  66 09 4F 38                     or word ptr [rdi + 0x38], cx
006DD0BC  45 85 E4                        test r12d, r12d
006DD0BF  74 2C                           je 0x1406dd0ed
006DD0C1  83 C9 FF                        or ecx, 0xffffffff
006DD0C4  3B F1                           cmp esi, ecx
006DD0C6  74 11                           je 0x1406dd0d9
006DD0C8  39 0D E6 E2 72 00               cmp dword ptr [rip + 0x72e2e6], ecx
006DD0CE  B9 01 00 00 00                  mov ecx, 1
006DD0D3  44 0F 45 E9                     cmovne r13d, ecx
006DD0D7  EB 05                           jmp 0x1406dd0de
006DD0D9  B9 01 00 00 00                  mov ecx, 1
006DD0DE  BA 02 00 00 00                  mov edx, 2
006DD0E3  44 3B E2                        cmp r12d, edx
006DD0E6  75 05                           jne 0x1406dd0ed
006DD0E8  44 8B C1                        mov r8d, ecx
006DD0EB  EB 12                           jmp 0x1406dd0ff
006DD0ED  45 8B C3                        mov r8d, r11d
006DD0F0  45 85 E4                        test r12d, r12d
006DD0F3  74 07                           je 0x1406dd0fc
006DD0F5  B9 01 00 00 00                  mov ecx, 1
006DD0FA  EB 03                           jmp 0x1406dd0ff
006DD0FC  41 8A CB                        mov cl, r11b
006DD0FF  4C 8B 8F B8 02 00 00            mov r9, qword ptr [rdi + 0x2b8]
006DD106  48 8D 54 24 78                  lea rdx, [rsp + 0x78]
006DD10B  48 89 54 24 30                  mov qword ptr [rsp + 0x30], rdx
006DD110  48 8D 55 80                     lea rdx, [rbp - 0x80]
006DD114  48 89 54 24 28                  mov qword ptr [rsp + 0x28], rdx
006DD119  41 8A D5                        mov dl, r13b
006DD11C  88 44 24 20                     mov byte ptr [rsp + 0x20], al
006DD120  E8 FB D6 ED FF                  call 0x1405ba820
006DD125  EB 2E                           jmp 0x1406dd155
006DD127  44 38 1D 57 99 8E 00            cmp byte ptr [rip + 0x8e9957], r11b
006DD12E  74 42                           je 0x1406dd172
006DD130  48 8D 4C 24 78                  lea rcx, [rsp + 0x78]
006DD135  E8 62 D3 ED FF                  call 0x1405ba49c
006DD13A  8B 43 24                        mov eax, dword ptr [rbx + 0x24]
006DD13D  B9 0A 00 00 00                  mov ecx, 0xa
006DD142  39 05 68 4E 84 00               cmp dword ptr [rip + 0x844e68], eax
006DD148  8B 74 24 68                     mov esi, dword ptr [rsp + 0x68]
006DD14C  8D 51 F8                        lea edx, [rcx - 8]
006DD14F  0F 44 CA                        cmove ecx, edx
006DD152  89 4D 80                        mov dword ptr [rbp - 0x80], ecx
006DD155  45 33 DB                        xor r11d, r11d
006DD158  44 38 1D 26 99 8E 00            cmp byte ptr [rip + 0x8e9926], r11b
006DD15F  74 11                           je 0x1406dd172
006DD161  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
006DD166  48 89 83 70 88 00 00            mov qword ptr [rbx + 0x8870], rax
006DD16D  E9 EF 39 BF FF                  jmp 0x1402d0b61
006DD172  8B 74 24 68                     mov esi, dword ptr [rsp + 0x68]
006DD176  E9 E6 39 BF FF                  jmp 0x1402d0b61
006DD17B  44 88 54 24 51                  mov byte ptr [rsp + 0x51], r10b
006DD180  E9 14 3C BF FF                  jmp 0x1402d0d99
006DD185  0F 0D 8B E0 06 00 00            prefetchw byte ptr [rbx + 0x6e0]
006DD18C  0F B7 B3 E0 06 00 00            movzx esi, word ptr [rbx + 0x6e0]
006DD193  40 F6 C6 04                     test sil, 4
006DD197  74 6C                           je 0x1406dd205
006DD199  84 8B D8 06 00 00               test byte ptr [rbx + 0x6d8], cl
006DD19F  74 2A                           je 0x1406dd1cb
006DD1A1  0F B7 83 E6 06 00 00            movzx eax, word ptr [rbx + 0x6e6]
006DD1A8  A8 03                           test al, 3
006DD1AA  75 1F                           jne 0x1406dd1cb
006DD1AC  66 41 0B C1                     or ax, r9w
006DD1B0  66 45 0B C1                     or r8w, r9w
006DD1B4  0F B7 D0                        movzx edx, ax
006DD1B7  B9 48 00 00 00                  mov ecx, 0x48
006DD1BC  66 89 93 E6 06 00 00            mov word ptr [rbx + 0x6e6], dx
006DD1C3  8B C2                           mov eax, edx
006DD1C5  48 C1 EA 20                     shr rdx, 0x20
006DD1C9  0F 30                           wrmsr
006DD1CB  66 F0 44 09 8B E0 06 00 00      lock or word ptr [rbx + 0x6e0], r9w
006DD1D4  48 8B 93 B0 2D 00 00            mov rdx, qword ptr [rbx + 0x2db0]
006DD1DB  0F 0D 8A E0 06 00 00            prefetchw byte ptr [rdx + 0x6e0]
006DD1E2  41 B9 0A 00 00 00               mov r9d, 0xa
006DD1E8  0F B7 82 E0 06 00 00            movzx eax, word ptr [rdx + 0x6e0]
006DD1EF  0F B7 C8                        movzx ecx, ax
006DD1F2  66 83 E1 EE                     and cx, 0xffee
006DD1F6  66 41 0B C9                     or cx, r9w
006DD1FA  66 F0 0F B1 8A E0 06 00 00      lock cmpxchg word ptr [rdx + 0x6e0], cx
006DD203  75 E3                           jne 0x1406dd1e8
006DD205  F6 83 DC 06 00 00 40            test byte ptr [rbx + 0x6dc], 0x40
006DD20C  44 89 54 24 70                  mov dword ptr [rsp + 0x70], r10d
006DD211  66 44 89 44 24 70               mov word ptr [rsp + 0x70], r8w
006DD217  0F 84 E0 3C BF FF               je 0x1402d0efd
006DD21D  0F B7 83 AA AE 00 00            movzx eax, word ptr [rbx + 0xaeaa]
006DD224  66 89 44 24 72                  mov word ptr [rsp + 0x72], ax
006DD229  E9 CF 3C BF FF                  jmp 0x1402d0efd
006DD22E  44 88 9B 7D 88 00 00            mov byte ptr [rbx + 0x887d], r11b
006DD235  E9 B8 39 BF FF                  jmp 0x1402d0bf2
006DD23A  44 88 5F 41                     mov byte ptr [rdi + 0x41], r11b
006DD23E  E9 DC 39 BF FF                  jmp 0x1402d0c1f
006DD243  84 C0                           test al, al
006DD245  74 70                           je 0x1406dd2b7
006DD247  45 85 FF                        test r15d, r15d
006DD24A  78 6B                           js 0x1406dd2b7
006DD24C  45 84 ED                        test r13b, r13b
006DD24F  75 66                           jne 0x1406dd2b7
006DD251  48 8B 0D 78 98 8E 00            mov rcx, qword ptr [rip + 0x8e9878]
006DD258  48 85 C9                        test rcx, rcx
006DD25B  74 5A                           je 0x1406dd2b7
006DD25D  8B 05 51 E1 72 00               mov eax, dword ptr [rip + 0x72e151]
006DD263  83 F8 FF                        cmp eax, -1
006DD266  74 4F                           je 0x1406dd2b7
006DD268  48 69 C0 C0 01 00 00            imul rax, rax, 0x1c0
006DD26F  8B 84 08 A0 01 00 00            mov eax, dword ptr [rax + rcx + 0x1a0]
006DD276  85 C0                           test eax, eax
006DD278  74 3D                           je 0x1406dd2b7
006DD27A  4C 8D 45 A0                     lea r8, [rbp - 0x60]
006DD27E  48 8D 54 24 6C                  lea rdx, [rsp + 0x6c]
006DD283  48 8D 4D 80                     lea rcx, [rbp - 0x80]
006DD287  E8 20 47 ED FF                  call 0x1405b19ac
006DD28C  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
006DD291  45 33 DB                        xor r11d, r11d
006DD294  85 C0                           test eax, eax
006DD296  78 15                           js 0x1406dd2ad
006DD298  44 38 1D 5B 98 8E 00            cmp byte ptr [rip + 0x8e985b], r11b
006DD29F  74 1B                           je 0x1406dd2bc
006DD2A1  44 39 5C 24 6C                  cmp dword ptr [rsp + 0x6c], r11d
006DD2A6  75 14                           jne 0x1406dd2bc
006DD2A8  C6 06 01                        mov byte ptr [rsi], 1
006DD2AB  EB 0F                           jmp 0x1406dd2bc
006DD2AD  C7 44 24 6C 03 00 00 00         mov dword ptr [rsp + 0x6c], 3
006DD2B5  EB 05                           jmp 0x1406dd2bc
006DD2B7  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
006DD2BC  48 8B 83 C0 00 00 00            mov rax, qword ptr [rbx + 0xc0]
006DD2C3  0F B6 8B D1 00 00 00            movzx ecx, byte ptr [rbx + 0xd1]
006DD2CA  F0 48 0F B3 48 40               lock btr qword ptr [rax + 0x40], rcx
006DD2D0  44 38 5C 24 51                  cmp byte ptr [rsp + 0x51], r11b
006DD2D5  74 12                           je 0x1406dd2e9
006DD2D7  8A 83 5A 86 00 00               mov al, byte ptr [rbx + 0x865a]
006DD2DD  84 C0                           test al, al
006DD2DF  74 08                           je 0x1406dd2e9
006DD2E1  E8 9A 0D EE FF                  call 0x1405be080
006DD2E6  45 33 DB                        xor r11d, r11d
006DD2E9  44 38 5C 24 55                  cmp byte ptr [rsp + 0x55], r11b
006DD2EE  74 1A                           je 0x1406dd30a
006DD2F0  45 85 FF                        test r15d, r15d
006DD2F3  78 15                           js 0x1406dd30a
006DD2F5  B8 02 00 00 00                  mov eax, 2
006DD2FA  4C 8D 44 24 74                  lea r8, [rsp + 0x74]
006DD2FF  39 85 B0 00 00 00               cmp dword ptr [rbp + 0xb0], eax
006DD305  0F 94 C2                        sete dl
006DD308  EB 11                           jmp 0x1406dd31b
006DD30A  B8 02 00 00 00                  mov eax, 2
006DD30F  39 85 B0 00 00 00               cmp dword ptr [rbp + 0xb0], eax
006DD315  0F 94 C2                        sete dl
006DD318  45 33 C0                        xor r8d, r8d
006DD31B  8A 0E                           mov cl, byte ptr [rsi]
006DD31D  E8 A2 D9 ED FF                  call 0x1405bacc4
006DD322  48 8B 05 87 36 72 00            mov rax, qword ptr [rip + 0x723687]
006DD329  E8 A2 D7 FD FF                  call 0x1406baad0
006DD32E  45 33 DB                        xor r11d, r11d
006DD331  8A 06                           mov al, byte ptr [rsi]
006DD333  49 B8 20 03 00 00 80 F7 FF FF   movabs r8, 0xfffff78000000320
006DD33D  F6 D8                           neg al
006DD33F  48 8B CB                        mov rcx, rbx
006DD342  1B C0                           sbb eax, eax
006DD344  45 33 C9                        xor r9d, r9d
006DD347  45 8B 00                        mov r8d, dword ptr [r8]
006DD34A  F7 D8                           neg eax
006DD34C  8B 93 C0 38 00 00               mov edx, dword ptr [rbx + 0x38c0]
006DD352  83 C0 03                        add eax, 3
006DD355  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
006DD359  44 88 5C 24 20                  mov byte ptr [rsp + 0x20], r11b
006DD35E  E8 DD ED CB FF                  call 0x14039c140
006DD363  90                              nop
006DD364  E9 CE 38 BF FF                  jmp 0x1402d0c37
006DD369  48 8B CB                        mov rcx, rbx
006DD36C  E8 0B 21 EF FF                  call 0x1405cf47c
006DD371  90                              nop
006DD372  E9 6C 39 BF FF                  jmp 0x1402d0ce3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006DCEEE(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r11;
    unsigned int v_stack_p20;
    unsigned __int8 v_stack_p28;
    unsigned __int8 v_stack_p30;
    unsigned __int8 v_stack_p51;
    unsigned __int8 v_stack_p52;
    unsigned __int8 v_stack_p54;
    unsigned __int8 v_stack_p55;
    unsigned __int8 v_stack_p56;
    unsigned __int8 v_stack_p57;
    unsigned __int64 v_stack_p60;
    unsigned int v_stack_p68;
    unsigned __int64 v_stack_p6C;
    unsigned int v_stack_p70;
    unsigned __int16 v_stack_p72;
    unsigned __int64 v_stack_p74;
    unsigned __int64 v_stack_p78;

    v_stack_p56 = (unsigned __int8)(a4);
    v_stack_p78 = result + *(unsigned __int64 *)(v_rbp + 192) * 1;
    if ((*(unsigned __int8 *)(v_rip + 9345936)) == ((unsigned __int8)(v_r11))) goto loc_006DCF41;
    result = ((*(unsigned __int8 *)(v_rdi + 716)) == ((unsigned __int8)(v_r11))) ? 1 : 0;
    a4 = 0;
    v_stack_p30 = (unsigned __int8)(result);
    v_stack_p28 = (unsigned __int8)(v_r11);
    v_stack_p20 = 5;
    result = KiSetClockTimer(v_rbx, *(unsigned __int64 *)(v_rbp + 192), result + *(unsigned __int64 *)(v_rbp + 192) * 1, a4);
    v_r11 = 0;
loc_006DCF41:
    *(unsigned __int64 *)(v_rbx + 34928) = v_rbx;
}
```

## 5. (Beta) C Style

```c
int64_t sub_006DCEEE(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_r11;
    uint32_t v_stack_p20;
    uint8_t v_stack_p28;
    uint8_t v_stack_p30;
    uint8_t v_stack_p51;
    uint8_t v_stack_p52;
    uint8_t v_stack_p54;
    uint8_t v_stack_p55;
    uint8_t v_stack_p56;
    uint8_t v_stack_p57;
    uint64_t v_stack_p60;
    uint32_t v_stack_p68;
    uint64_t v_stack_p6C;
    uint32_t v_stack_p70;
    uint16_t v_stack_p72;
    uint64_t v_stack_p74;
    uint64_t v_stack_p78;

    v_stack_p56 = (uint8_t)(Arg4);
    v_stack_p78 = result + *(uint64_t *)(local_rbp + 0xC0) * 1;
    if ((*(uint8_t *)(v_rip + 0x8E9B90)) == ((uint8_t)(local_r11))) goto loc_006DCF41;
    result = ((*(uint8_t *)(local_rdi + 0x2CC)) == ((uint8_t)(local_r11))) ? 1 : 0;
    Arg4 = 0;
    v_stack_p30 = (uint8_t)(result);
    v_stack_p28 = (uint8_t)(local_r11);
    v_stack_p20 = 5;
    result = KiSetClockTimer(local_rbx, *(uint64_t *)(local_rbp + 0xC0), result + *(uint64_t *)(local_rbp + 0xC0) * 1, Arg4);
    local_r11 = 0;
loc_006DCF41:
    *(uint64_t *)(local_rbx + 0x8870) = local_rbx;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006DCEEE&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
