# KdInitSystem

- RVA: `0x00B85E30`–`0x00B8656F` (길이 `1,855` bytes)
- VA: `0x0000000140B85E30`
- 실행 섹션: `PAGEKD`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C9838`
- 디코드: `420`개 명령, `1,855/1,855` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **28**; 고유 호출 대상: **18**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **80**

### Outgoing calls
- `0x00B85EFC` → [MmGetPagedPoolCommitPointer](../../text/4F/MmGetPagedPoolCommitPointer_function_004F9AD8.md) (function, `0x004F9AD8`)
- `0x00B85F40` → [KdRegisterDebuggerDataBlock](KdRegisterDebuggerDataBlock_function_00B86578.md) (function, `0x00B86578`)
- `0x00B85FF3` → [strupr](../../text/4F/strupr_function_004FEEE0.md) (function, `0x004FEEE0`)
- `0x00B8600C` → [strstr](../../text/4F/strstr_function_004FF680.md) (function, `0x004FF680`)
- `0x00B8601F` → [atol](../../text/4F/atol_function_004FF8D0.md) (function, `0x004FF8D0`)
- `0x00B8605D` → [strstr](../../text/4F/strstr_function_004FF680.md) (function, `0x004FF680`)
- `0x00B86090` → [strstr](../../text/4F/strstr_function_004FF680.md) (function, `0x004FF680`)
- `0x00B860D4` → [strstr](../../text/4F/strstr_function_004FF680.md) (function, `0x004FF680`)
- `0x00B860E8` → [strstr](../../text/4F/strstr_function_004FF680.md) (function, `0x004FF680`)
- `0x00B8611F` → [strstr](../../text/4F/strstr_function_004FF680.md) (function, `0x004FF680`)
- `0x00B8618B` → [strncmp](../../text/6C/strncmp_function_006C6720.md) (function, `0x006C6720`)
- `0x00B861B2` → [strncmp](../../text/6C/strncmp_function_006C6720.md) (function, `0x006C6720`)
- `0x00B861D9` → [strncmp](../../text/6C/strncmp_function_006C6720.md) (function, `0x006C6720`)
- `0x00B86205` → [strstr](../../text/4F/strstr_function_004FF680.md) (function, `0x004FF680`)
- `0x00B8622A` → [strstr](../../text/4F/strstr_function_004FF680.md) (function, `0x004FF680`)
- `0x00B862CD` → `kdcom.dll!KdInitialize` (import, 간접 대상; import `kdcom.dll!KdInitialize`)
- `0x00B86328` → [KeInitializeDpc](../../text/45/KeInitializeDpc_function_0045BBD0.md) (function, `0x0045BBD0`)
- `0x00B86334` → [KeInitializeTimer](../../text/45/KeInitializeTimer_function_0045B590.md) (function, `0x0045B590`)
- `0x00B863D7` → [KdDisableDebuggerWithLock](../../text/5B/KdDisableDebuggerWithLock_function_005B0918.md) (function, `0x005B0918`)
- `0x00B863F1` → [KeIsKernelCetEnabled](../../text/45/KeIsKernelCetEnabled_function_0045D610.md) (function, `0x0045D610`)
- `0x00B8649A` → [RtlInitAnsiString](../../text/47/RtlInitAnsiString_function_00470F40.md) (function, `0x00470F40`)
- `0x00B864AB` → [DbgLoadImageSymbols](../../text/4A/DbgLoadImageSymbols_function_004AE220.md) (function, `0x004AE220`)
- `0x00B864B7` → [_report_rangecheckfailure](../../text/4F/_report_rangecheckfailure_function_004F5FDC.md) (function, `0x004F5FDC`)
- `0x00B864BD` → [KdPollBreakIn](../../text/39/KdPollBreakIn_function_0039CE80.md) (function, `0x0039CE80`)
- `0x00B864D9` → [DbgLoadImageSymbols](../../text/4A/DbgLoadImageSymbols_function_004AE220.md) (function, `0x004AE220`)
- `0x00B864E7` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x00B86512` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00B8654E` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [KdEnableDebuggerWithLock](../../text/5B/KdEnableDebuggerWithLock_function_005B0A7C.md) at `0x005B0B21`
- [KdEnableDebuggerWithLock](../../text/5B/KdEnableDebuggerWithLock_function_005B0A7C.md) at `0x005B0B81`
- [KeEnterKernelDebugger](../../text/5B/KeEnterKernelDebugger_function_005B3880.md) at `0x005B38CD`
- [KiSystemStartup](../../pagelk/B5/KiSystemStartup_function_00B5B3C0.md) at `0x00B5B407`
- [KiSystemStartup](../../pagelk/B5/KiSystemStartup_function_00B5B3C0.md) at `0x00B5B591`
- [KiSetFeatureBits](../../pagelk/B6/KiSetFeatureBits_function_00B6A03C.md) at `0x00B6A913`
- [PopHiberCheckResume](../../pagelk/B6/PopHiberCheckResume_function_00B6D840.md) at `0x00B6D952`
- [PopHiberCheckResume](../../pagelk/B6/PopHiberCheckResume_function_00B6D840.md) at `0x00B6D9D3`
- [Phase1InitializationDiscard](../../init/C1/Phase1InitializationDiscard_function_00C1C728.md) at `0x00C1D25A`

### Static image references
- `0x00B85E47` → RVA `0x00E0A740` (`.data`; read)
- `0x00B85E96` → RVA `0x00F475F8` (`.data`; read)
- `0x00B85EA3` → RVA `0x00E0AA1C` (`.data`; read)
- `0x00B85EAA` → RVA `0x00E664A8` (`.data`; write)
- `0x00B85EB1` → RVA `0x00F59CC9` (`.data`; write)
- `0x00B85EBA` → RVA `0x00F55C80` (`.data`; read)
- `0x00B85EC9` → RVA `0x00FC19A0` (`.data`; read)
- `0x00B85EDE` → RVA `0x00E0AA48` (`.data`; write)
- `0x00B85EE8` → RVA `0x00F55C70` (`.data`; read)
- `0x00B85EF5` → RVA `0x00F475E8` (`.data`; write)
- `0x00B85F01` → RVA `0x00E011D0` (`.data`; write)
- `0x00B85F0F` → RVA `0x00F55C90` (`.data`; read)
- `0x00B85F16` → RVA `0x00E664A0` (`.data`; write)
- `0x00B85F1D` → RVA `0x00E01060` (`.data`; read)
- `0x00B85F24` → RVA `0x00F55C98` (`.data`; write)
- `0x00B85F2B` → RVA `0x00F55C90` (`.data`; write)
- `0x00B85F32` → RVA `0x00F55C78` (`.data`; write)
- `0x00B85F39` → RVA `0x00F55C70` (`.data`; write)
- `0x00B85F45` → RVA `0x00E0A74C` (`.data`; read)
- `0x00B85F4B` → RVA `0x00E0AA22` (`.data`; write)
- `0x00B85F55` → RVA `0x00E0AA20` (`.data`; write)
- `0x00B85F5C` → RVA `0x00EF54C0` (`.data`; read)
- `0x00B85F63` → RVA `0x00E0AA40` (`.data`; write)
- `0x00B85F6F` → RVA `0x00E0AA26` (`.data`; read/write)
- `0x00B85F76` → RVA `0x00E0AA38` (`.data`; write)
- `0x00B85F7D` → RVA `0x00E0AA2B` (`.data`; write)
- `0x00B85FC4` → RVA `0x00F55CA8` (`.data`; read)
- `0x00B85FCB` → RVA `0x00E01338` (`.data`; write)
- `0x00B85FD2` → RVA `0x00F55CA8` (`.data`; write)
- `0x00B85FE0` → RVA `0x00E0AA30` (`.data`; write)
- `0x00B85FF8` → RVA `0x00B8ABE0` (` ?? ::DFIOBLLK::`string'`; read)
- `0x00B85FFF` → RVA `0x00F55C60` (`.data`; write)
- `0x00B86053` → RVA `0x00B8AC00` (` ?? ::DFIOBLLK::`string'`; read)
- `0x00B8606C` → RVA `0x00E0AA1C` (`.data`; write)
- `0x00B86073` → RVA `0x00F55CA2` (`.data`; write)
- `0x00B8607A` → RVA `0x00E0AA1D` (`.data`; write)
- `0x00B86086` → RVA `0x00B8AC10` (` ?? ::DFIOBLLK::`string'`; read)
- `0x00B860B0` → RVA `0x00F475DC` (`.data`; write)
- `0x00B860B7` → RVA `0x00F55C80` (`.data`; write)
- `0x00B860CA` → RVA `0x00B8AC20` (` ?? ::DFIOBLLK::`string'`; read)
- `0x00B860DE` → RVA `0x00B8ABA0` (` ?? ::DFIOBLLK::`string'`; read)
- `0x00B86115` → RVA `0x00B8AC30` (` ?? ::DFIOBLLK::`string'`; read)
- `0x00B8612D` → RVA `0x00F59CC8` (`.data`; write)
- `0x00B86184` → RVA `0x00B8ABB0` (` ?? ::DFIOBLLK::`string'`; read)
- `0x00B86197` → RVA `0x00F55CA1` (`.data`; write)
- `0x00B861AB` → RVA `0x00B8ABC0` (` ?? ::DFIOBLLK::`string'`; read)
- `0x00B861D2` → RVA `0x00B8ABD0` (` ?? ::DFIOBLLK::`string'`; read)
- `0x00B861E2` → RVA `0x00F55CA0` (`.data`; write)
- `0x00B861FB` → RVA `0x00B8AC40` (` ?? ::DFIOBLLK::`string'`; read)
- `0x00B86220` → RVA `0x00B8AC50` (` ?? ::DFIOBLLK::`string'`; read)
- `0x00B86239` → RVA `0x00F55CB1` (`.data`; write)
- `0x00B8625A` → RVA `0x00FC6B28` (`ALMOSTRO`; read)
- `0x00B8626B` → RVA `0x00E0AA30` (`.data`; read)
- `0x00B86272` → RVA `0x00E01078` (`.data`; write)
- `0x00B862C1` → RVA `0x00F475E0` (`.data`; read)
- `0x00B862CD` → RVA `0x001516B8` (`kdcom.dll!KdInitialize (IAT)`; read)
- `0x00B862FD` → RVA `0x00F55CB0` (`.data`; read)
- `0x00B86309` → RVA `0x00F475E4` (`.data`; write)
- `0x00B86310` → RVA `0x00B88610` (`KdpTimeSlipDpcRoutine`; read)
- `0x00B86317` → RVA `0x00F475E0` (`.data`; write)
- `0x00B86321` → RVA `0x00E66400` (`.data`; read)
- `0x00B8632D` → RVA `0x00E66440` (`.data`; read)
- `0x00B86339` → RVA `0x00B88650` (`KdpTimeSlipWork`; read)
- `0x00B86340` → RVA `0x00E66498` (`.data`; write)
- `0x00B86347` → RVA `0x00E66490` (`.data`; write)
- `0x00B8634E` → RVA `0x00E66480` (`.data`; write)
- `0x00B86355` → RVA `0x00F55CB0` (`.data`; write)
- `0x00B8635C` → RVA `0x00F59CC8` (`.data`; read)
- `0x00B86363` → RVA `0x00F55CB8` (`.data`; write)
- `0x00B8636C` → RVA `0x00E0AA1D` (`.data`; read)
- `0x00B8637C` → RVA `0x00F55CB3` (`.data`; write)
- `0x00B86393` → RVA `0x00FC5008` (`ALMOSTRO`; read)
- `0x00B8639A` → RVA `0x00F475F8` (`.data`; write)
- `0x00B863DC` → RVA `0x00F55CB2` (`.data`; write)
- `0x00B86403` → RVA `0x00F475DC` (`.data`; read)
- `0x00B8640C` → RVA `0x01201842` (`CFGRO`; read/write)
- `0x00B864CD` → RVA `0x00E01078` (`.data`; read)
- `0x00B864E0` → RVA `0x00F59CC0` (`.data`; read)
- `0x00B864F5` → RVA `0x00FC6A80` (`ALMOSTRO`; read)
- `0x00B86523` → RVA `0x00F55CC0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **26**
  - `0x00B85EFC` → [MmGetPagedPoolCommitPointer](../../text/4F/MmGetPagedPoolCommitPointer_function_004F9AD8.md) (`PAGEKD` → `.text`)
  - `0x00B85FF3` → [strupr](../../text/4F/strupr_function_004FEEE0.md) (`PAGEKD` → `.text`)
  - `0x00B8600C` → [strstr](../../text/4F/strstr_function_004FF680.md) (`PAGEKD` → `.text`)
  - `0x00B8601F` → [atol](../../text/4F/atol_function_004FF8D0.md) (`PAGEKD` → `.text`)
  - `0x00B8605D` → [strstr](../../text/4F/strstr_function_004FF680.md) (`PAGEKD` → `.text`)
  - `0x00B86090` → [strstr](../../text/4F/strstr_function_004FF680.md) (`PAGEKD` → `.text`)
  - `0x00B860D4` → [strstr](../../text/4F/strstr_function_004FF680.md) (`PAGEKD` → `.text`)
  - `0x00B860E8` → [strstr](../../text/4F/strstr_function_004FF680.md) (`PAGEKD` → `.text`)
  - `0x00B8611F` → [strstr](../../text/4F/strstr_function_004FF680.md) (`PAGEKD` → `.text`)
  - `0x00B8618B` → [strncmp](../../text/6C/strncmp_function_006C6720.md) (`PAGEKD` → `.text`)
  - `0x00B861B2` → [strncmp](../../text/6C/strncmp_function_006C6720.md) (`PAGEKD` → `.text`)
  - `0x00B861D9` → [strncmp](../../text/6C/strncmp_function_006C6720.md) (`PAGEKD` → `.text`)
  - `0x00B86205` → [strstr](../../text/4F/strstr_function_004FF680.md) (`PAGEKD` → `.text`)
  - `0x00B8622A` → [strstr](../../text/4F/strstr_function_004FF680.md) (`PAGEKD` → `.text`)
  - `0x00B86328` → [KeInitializeDpc](../../text/45/KeInitializeDpc_function_0045BBD0.md) (`PAGEKD` → `.text`)
  - `0x00B86334` → [KeInitializeTimer](../../text/45/KeInitializeTimer_function_0045B590.md) (`PAGEKD` → `.text`)
  - `0x00B863D7` → [KdDisableDebuggerWithLock](../../text/5B/KdDisableDebuggerWithLock_function_005B0918.md) (`PAGEKD` → `.text`)
  - `0x00B863F1` → [KeIsKernelCetEnabled](../../text/45/KeIsKernelCetEnabled_function_0045D610.md) (`PAGEKD` → `.text`)
  - `0x00B8649A` → [RtlInitAnsiString](../../text/47/RtlInitAnsiString_function_00470F40.md) (`PAGEKD` → `.text`)
  - `0x00B864AB` → [DbgLoadImageSymbols](../../text/4A/DbgLoadImageSymbols_function_004AE220.md) (`PAGEKD` → `.text`)
  - `0x00B864B7` → [_report_rangecheckfailure](../../text/4F/_report_rangecheckfailure_function_004F5FDC.md) (`PAGEKD` → `.text`)
  - `0x00B864BD` → [KdPollBreakIn](../../text/39/KdPollBreakIn_function_0039CE80.md) (`PAGEKD` → `.text`)
  - `0x00B864D9` → [DbgLoadImageSymbols](../../text/4A/DbgLoadImageSymbols_function_004AE220.md) (`PAGEKD` → `.text`)
  - `0x00B864E7` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (`PAGEKD` → `.text`)
  - `0x00B86512` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGEKD` → `POOLCODE`)
  - `0x00B8654E` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGEKD` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B85E30  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
00B85E35  55                              push rbp
00B85E36  56                              push rsi
00B85E37  57                              push rdi
00B85E38  41 54                           push r12
00B85E3A  41 55                           push r13
00B85E3C  41 56                           push r14
00B85E3E  41 57                           push r15
00B85E40  48 81 EC 40 01 00 00            sub rsp, 0x140
00B85E47  48 8B 05 F2 48 28 00            mov rax, qword ptr [rip + 0x2848f2]
00B85E4E  48 33 C4                        xor rax, rsp
00B85E51  48 89 84 24 30 01 00 00         mov qword ptr [rsp + 0x130], rax
00B85E59  45 33 ED                        xor r13d, r13d
00B85E5C  BE FF FF FF FF                  mov esi, 0xffffffff
00B85E61  48 8B DA                        mov rbx, rdx
00B85E64  45 8A E5                        mov r12b, r13b
00B85E67  45 8A FD                        mov r15b, r13b
00B85E6A  41 8D 7D 01                     lea edi, [r13 + 1]
00B85E6E  3B CE                           cmp ecx, esi
00B85E70  75 1C                           jne 0x140b85e8e
00B85E72  48 8B 82 F0 00 00 00            mov rax, qword ptr [rdx + 0xf0]
00B85E79  8B 88 84 00 00 00               mov ecx, dword ptr [rax + 0x84]
00B85E7F  F6 C1 08                        test cl, 8
00B85E82  0F 84 B9 06 00 00               je 0x140b86541
00B85E88  CC                              int3
00B85E89  E9 B3 06 00 00                  jmp 0x140b86541
00B85E8E  85 C9                           test ecx, ecx
00B85E90  0F 85 4A 06 00 00               jne 0x140b864e0
00B85E96  44 38 2D 5B 17 3C 00            cmp byte ptr [rip + 0x3c175b], r13b
00B85E9D  0F 85 F2 03 00 00               jne 0x140b86295
00B85EA3  44 38 2D 72 4B 28 00            cmp byte ptr [rip + 0x284b72], r13b
00B85EAA  44 89 2D F7 05 2E 00            mov dword ptr [rip + 0x2e05f7], r13d
00B85EB1  44 88 2D 11 3E 3D 00            mov byte ptr [rip + 0x3d3e11], r13b
00B85EB8  74 0C                           je 0x140b85ec6
00B85EBA  44 38 2D BF FD 3C 00            cmp byte ptr [rip + 0x3cfdbf], r13b
00B85EC1  44 8A F7                        mov r14b, dil
00B85EC4  75 03                           jne 0x140b85ec9
00B85EC6  45 8A F5                        mov r14b, r13b
00B85EC9  48 8B 05 D0 BA 43 00            mov rax, qword ptr [rip + 0x43bad0]
00B85ED0  48 85 C0                        test rax, rax
00B85ED3  74 13                           je 0x140b85ee8
00B85ED5  83 B8 EC 00 00 00 03            cmp dword ptr [rax + 0xec], 3
00B85EDC  75 0A                           jne 0x140b85ee8
00B85EDE  C7 05 60 4B 28 00 80 04 00 00   mov dword ptr [rip + 0x284b60], 0x480
00B85EE8  4C 39 2D 81 FD 3C 00            cmp qword ptr [rip + 0x3cfd81], r13
00B85EEF  0F 85 91 00 00 00               jne 0x140b85f86
00B85EF5  48 89 05 EC 16 3C 00            mov qword ptr [rip + 0x3c16ec], rax
00B85EFC  E8 D7 3B 97 FF                  call 0x1404f9ad8
00B85F01  48 89 05 C8 B2 27 00            mov qword ptr [rip + 0x27b2c8], rax
00B85F08  48 8D 3D 61 FD 3C 00            lea rdi, [rip + 0x3cfd61]
00B85F0F  48 8D 05 7A FD 3C 00            lea rax, [rip + 0x3cfd7a]
00B85F16  4C 89 2D 83 05 2E 00            mov qword ptr [rip + 0x2e0583], r13
00B85F1D  48 8D 15 3C B1 27 00            lea rdx, [rip + 0x27b13c]
00B85F24  48 89 05 6D FD 3C 00            mov qword ptr [rip + 0x3cfd6d], rax
00B85F2B  48 89 05 5E FD 3C 00            mov qword ptr [rip + 0x3cfd5e], rax
00B85F32  48 89 3D 3F FD 3C 00            mov qword ptr [rip + 0x3cfd3f], rdi
00B85F39  48 89 3D 30 FD 3C 00            mov qword ptr [rip + 0x3cfd30], rdi
00B85F40  E8 33 06 00 00                  call 0x140b86578
00B85F45  8B 05 01 48 28 00               mov eax, dword ptr [rip + 0x284801]
00B85F4B  66 89 05 D0 4A 28 00            mov word ptr [rip + 0x284ad0], ax
00B85F52  C1 E8 1C                        shr eax, 0x1c
00B85F55  66 89 05 C4 4A 28 00            mov word ptr [rip + 0x284ac4], ax
00B85F5C  48 8D 05 5D F5 36 00            lea rax, [rip + 0x36f55d]
00B85F63  48 89 3D D6 4A 28 00            mov qword ptr [rip + 0x284ad6], rdi
00B85F6A  BF 01 00 00 00                  mov edi, 1
00B85F6F  66 09 3D B0 4A 28 00            or word ptr [rip + 0x284ab0], di
00B85F76  48 89 05 BB 4A 28 00            mov qword ptr [rip + 0x284abb], rax
00B85F7D  66 C7 05 A5 4A 28 00 03 33      mov word ptr [rip + 0x284aa5], 0x3303
00B85F86  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
00B85F8F  4C 39 A9 C0 8F 00 00            cmp qword ptr [rcx + 0x8fc0], r13
00B85F96  75 18                           jne 0x140b85fb0
00B85F98  48 8D 81 F0 01 00 00            lea rax, [rcx + 0x1f0]
00B85F9F  C7 81 C8 8F 00 00 0B 00 10 00   mov dword ptr [rcx + 0x8fc8], 0x10000b
00B85FA9  48 89 81 C0 8F 00 00            mov qword ptr [rcx + 0x8fc0], rax
00B85FB0  48 85 DB                        test rbx, rbx
00B85FB3  0F 84 A1 02 00 00               je 0x140b8625a
00B85FB9  48 8D 53 10                     lea rdx, [rbx + 0x10]
00B85FBD  48 8B 02                        mov rax, qword ptr [rdx]
00B85FC0  48 8B 48 30                     mov rcx, qword ptr [rax + 0x30]
00B85FC4  48 8D 05 DD FC 3C 00            lea rax, [rip + 0x3cfcdd]
00B85FCB  48 89 05 66 B3 27 00            mov qword ptr [rip + 0x27b366], rax
00B85FD2  48 89 15 CF FC 3C 00            mov qword ptr [rip + 0x3cfccf], rdx
00B85FD9  48 8B B3 D8 00 00 00            mov rsi, qword ptr [rbx + 0xd8]
00B85FE0  48 89 0D 49 4A 28 00            mov qword ptr [rip + 0x284a49], rcx
00B85FE7  48 85 F6                        test rsi, rsi
00B85FEA  0F 84 52 02 00 00               je 0x140b86242
00B85FF0  48 8B CE                        mov rcx, rsi
00B85FF3  E8 E8 8E 97 FF                  call 0x1404feee0
00B85FF8  48 8D 15 E1 4B 00 00            lea rdx, [rip + 0x4be1]
00B85FFF  44 89 2D 5A FC 3C 00            mov dword ptr [rip + 0x3cfc5a], r13d
00B86006  48 8B CE                        mov rcx, rsi
00B86009  41 8A ED                        mov bpl, r13b
00B8600C  E8 6F 96 97 FF                  call 0x1404ff680
00B86011  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00B86016  48 85 C0                        test rax, rax
00B86019  74 38                           je 0x140b86053
00B8601B  48 8D 48 12                     lea rcx, [rax + 0x12]
00B8601F  E8 AC 98 97 FF                  call 0x1404ff8d0
00B86024  05 FF 0F 00 00                  add eax, 0xfff
00B86029  B9 00 00 00 01                  mov ecx, 0x1000000
00B8602E  25 00 F0 FF FF                  and eax, 0xfffff000
00B86033  89 05 27 FC 3C 00               mov dword ptr [rip + 0x3cfc27], eax
00B86039  3B C1                           cmp eax, ecx
00B8603B  76 08                           jbe 0x140b86045
00B8603D  89 0D 1D FC 3C 00               mov dword ptr [rip + 0x3cfc1d], ecx
00B86043  EB 0E                           jmp 0x140b86053
00B86045  3D 00 10 00 00                  cmp eax, 0x1000
00B8604A  77 07                           ja 0x140b86053
00B8604C  44 89 2D 0D FC 3C 00            mov dword ptr [rip + 0x3cfc0d], r13d
00B86053  48 8D 15 A6 4B 00 00            lea rdx, [rip + 0x4ba6]
00B8605A  48 8B CE                        mov rcx, rsi
00B8605D  E8 1E 96 97 FF                  call 0x1404ff680
00B86062  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00B86067  48 85 C0                        test rax, rax
00B8606A  74 1A                           je 0x140b86086
00B8606C  40 88 3D A9 49 28 00            mov byte ptr [rip + 0x2849a9], dil
00B86073  40 88 3D 28 FC 3C 00            mov byte ptr [rip + 0x3cfc28], dil
00B8607A  40 88 3D 9C 49 28 00            mov byte ptr [rip + 0x28499c], dil
00B86081  E9 8F 00 00 00                  jmp 0x140b86115
00B86086  48 8D 15 83 4B 00 00            lea rdx, [rip + 0x4b83]
00B8608D  48 8B CE                        mov rcx, rsi
00B86090  E8 EB 95 97 FF                  call 0x1404ff680
00B86095  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00B8609A  48 85 C0                        test rax, rax
00B8609D  74 28                           je 0x140b860c7
00B8609F  40 88 3D 76 49 28 00            mov byte ptr [rip + 0x284976], dil
00B860A6  44 8A F7                        mov r14b, dil
00B860A9  40 88 3D F2 FB 3C 00            mov byte ptr [rip + 0x3cfbf2], dil
00B860B0  40 88 3D 25 15 3C 00            mov byte ptr [rip + 0x3c1525], dil
00B860B7  40 88 3D C2 FB 3C 00            mov byte ptr [rip + 0x3cfbc2], dil
00B860BE  44 88 2D 58 49 28 00            mov byte ptr [rip + 0x284958], r13b
00B860C5  EB 4E                           jmp 0x140b86115
00B860C7  48 8B FE                        mov rdi, rsi
00B860CA  48 8D 15 4F 4B 00 00            lea rdx, [rip + 0x4b4f]
00B860D1  48 8B CF                        mov rcx, rdi
00B860D4  E8 A7 95 97 FF                  call 0x1404ff680
00B860D9  48 85 C0                        test rax, rax
00B860DC  75 14                           jne 0x140b860f2
00B860DE  48 8D 15 BB 4A 00 00            lea rdx, [rip + 0x4abb]
00B860E5  48 8B CF                        mov rcx, rdi
00B860E8  E8 93 95 97 FF                  call 0x1404ff680
00B860ED  48 85 C0                        test rax, rax
00B860F0  74 1E                           je 0x140b86110
00B860F2  8A 50 06                        mov dl, byte ptr [rax + 6]
00B860F5  48 8B C8                        mov rcx, rax
00B860F8  80 FA 3D                        cmp dl, 0x3d
00B860FB  74 3C                           je 0x140b86139
00B860FD  F6 C2 DF                        test dl, 0xdf
00B86100  74 37                           je 0x140b86139
00B86102  48 85 C0                        test rax, rax
00B86105  74 09                           je 0x140b86110
00B86107  48 8D 78 06                     lea rdi, [rax + 6]
00B8610B  48 85 FF                        test rdi, rdi
00B8610E  75 BA                           jne 0x140b860ca
00B86110  BF 01 00 00 00                  mov edi, 1
00B86115  48 8D 15 14 4B 00 00            lea rdx, [rip + 0x4b14]
00B8611C  48 8B CE                        mov rcx, rsi
00B8611F  E8 5C 95 97 FF                  call 0x1404ff680
00B86124  48 85 C0                        test rax, rax
00B86127  0F 84 CE 00 00 00               je 0x140b861fb
00B8612D  44 88 2D 94 3B 3D 00            mov byte ptr [rip + 0x3d3b94], r13b
00B86134  E9 E7 00 00 00                  jmp 0x140b86220
00B86139  BF 01 00 00 00                  mov edi, 1
00B8613E  44 88 2D D8 48 28 00            mov byte ptr [rip + 0x2848d8], r13b
00B86145  80 78 06 3D                     cmp byte ptr [rax + 6], 0x3d
00B86149  40 8A EF                        mov bpl, dil
00B8614C  75 C7                           jne 0x140b86115
00B8614E  48 83 C1 07                     add rcx, 7
00B86152  8A 01                           mov al, byte ptr [rcx]
00B86154  48 8B F9                        mov rdi, rcx
00B86157  EB 19                           jmp 0x140b86172
00B86159  3C 2C                           cmp al, 0x2c
00B8615B  77 10                           ja 0x140b8616d
00B8615D  48 BA 00 02 00 00 01 10 00 00   movabs rdx, 0x100100000200
00B86167  48 0F A3 C2                     bt rdx, rax
00B8616B  72 09                           jb 0x140b86176
00B8616D  48 FF C7                        inc rdi
00B86170  8A 07                           mov al, byte ptr [rdi]
00B86172  84 C0                           test al, al
00B86174  75 E3                           jne 0x140b86159
00B86176  8B C7                           mov eax, edi
00B86178  2B C1                           sub eax, ecx
00B8617A  74 94                           je 0x140b86110
00B8617C  83 F8 0A                        cmp eax, 0xa
00B8617F  75 22                           jne 0x140b861a3
00B86181  44 8B C0                        mov r8d, eax
00B86184  48 8D 15 25 4A 00 00            lea rdx, [rip + 0x4a25]
00B8618B  E8 90 05 B4 FF                  call 0x1406c6720
00B86190  85 C0                           test eax, eax
00B86192  75 55                           jne 0x140b861e9
00B86194  44 8A E5                        mov r12b, bpl
00B86197  40 88 2D 03 FB 3C 00            mov byte ptr [rip + 0x3cfb03], bpl
00B8619E  45 8A FD                        mov r15b, r13b
00B861A1  EB 46                           jmp 0x140b861e9
00B861A3  83 F8 07                        cmp eax, 7
00B861A6  75 22                           jne 0x140b861ca
00B861A8  44 8B C0                        mov r8d, eax
00B861AB  48 8D 15 0E 4A 00 00            lea rdx, [rip + 0x4a0e]
00B861B2  E8 69 05 B4 FF                  call 0x1406c6720
00B861B7  85 C0                           test eax, eax
00B861B9  75 2E                           jne 0x140b861e9
00B861BB  44 8A E5                        mov r12b, bpl
00B861BE  44 88 2D DC FA 3C 00            mov byte ptr [rip + 0x3cfadc], r13b
00B861C5  44 8A FD                        mov r15b, bpl
00B861C8  EB 1F                           jmp 0x140b861e9
00B861CA  83 F8 06                        cmp eax, 6
00B861CD  75 1A                           jne 0x140b861e9
00B861CF  44 8B C0                        mov r8d, eax
00B861D2  48 8D 15 F7 49 00 00            lea rdx, [rip + 0x49f7]
00B861D9  E8 42 05 B4 FF                  call 0x1406c6720
00B861DE  85 C0                           test eax, eax
00B861E0  75 07                           jne 0x140b861e9
00B861E2  40 88 2D B7 FA 3C 00            mov byte ptr [rip + 0x3cfab7], bpl
00B861E9  80 3F 2C                        cmp byte ptr [rdi], 0x2c
00B861EC  0F 85 1E FF FF FF               jne 0x140b86110
00B861F2  48 8D 4F 01                     lea rcx, [rdi + 1]
00B861F6  E9 57 FF FF FF                  jmp 0x140b86152
00B861FB  48 8D 15 3E 4A 00 00            lea rdx, [rip + 0x4a3e]
00B86202  48 8B CE                        mov rcx, rsi
00B86205  E8 76 94 97 FF                  call 0x1404ff680
00B8620A  48 85 C0                        test rax, rax
00B8620D  74 11                           je 0x140b86220
00B8620F  40 88 3D B2 3A 3D 00            mov byte ptr [rip + 0x3d3ab2], dil
00B86216  40 8A EF                        mov bpl, dil
00B86219  44 88 2D 82 FA 3C 00            mov byte ptr [rip + 0x3cfa82], r13b
00B86220  48 8D 15 29 4A 00 00            lea rdx, [rip + 0x4a29]
00B86227  48 8B CE                        mov rcx, rsi
00B8622A  E8 51 94 97 FF                  call 0x1404ff680
00B8622F  BE FF FF FF FF                  mov esi, 0xffffffff
00B86234  48 85 C0                        test rax, rax
00B86237  74 32                           je 0x140b8626b
00B86239  40 88 3D 71 FA 3C 00            mov byte ptr [rip + 0x3cfa71], dil
00B86240  EB 29                           jmp 0x140b8626b
00B86242  40 88 3D D3 47 28 00            mov byte ptr [rip + 0x2847d3], dil
00B86249  41 8A ED                        mov bpl, r13b
00B8624C  40 88 3D 4F FA 3C 00            mov byte ptr [rip + 0x3cfa4f], dil
00B86253  BE FF FF FF FF                  mov esi, 0xffffffff
00B86258  EB 11                           jmp 0x140b8626b
00B8625A  48 8B 05 C7 08 44 00            mov rax, qword ptr [rip + 0x4408c7]
00B86261  40 8A EF                        mov bpl, dil
00B86264  48 89 05 C5 47 28 00            mov qword ptr [rip + 0x2847c5], rax
00B8626B  48 8B 05 BE 47 28 00            mov rax, qword ptr [rip + 0x2847be]
00B86272  48 89 05 FF AD 27 00            mov qword ptr [rip + 0x27adff], rax
00B86279  45 84 F6                        test r14b, r14b
00B8627C  75 7F                           jne 0x140b862fd
00B8627E  48 85 DB                        test rbx, rbx
00B86281  74 06                           je 0x140b86289
00B86283  83 7B 0C 02                     cmp dword ptr [rbx + 0xc], 2
00B86287  72 05                           jb 0x140b8628e
00B86289  40 84 ED                        test bpl, bpl
00B8628C  75 33                           jne 0x140b862c1
00B8628E  40 88 3D 47 13 3C 00            mov byte ptr [rip + 0x3c1347], dil
00B86295  48 85 DB                        test rbx, rbx
00B86298  0F 84 A3 02 00 00               je 0x140b86541
00B8629E  48 8B BB F0 00 00 00            mov rdi, qword ptr [rbx + 0xf0]
00B862A5  48 85 FF                        test rdi, rdi
00B862A8  0F 84 93 02 00 00               je 0x140b86541
00B862AE  48 81 C7 A0 09 00 00            add rdi, 0x9a0
00B862B5  33 C0                           xor eax, eax
00B862B7  8D 48 20                        lea ecx, [rax + 0x20]
00B862BA  F3 AA                           rep stosb byte ptr [rdi], al
00B862BC  E9 80 02 00 00                  jmp 0x140b86541
00B862C1  4C 8D 05 18 13 3C 00            lea r8, [rip + 0x3c1318]
00B862C8  48 8B D3                        mov rdx, rbx
00B862CB  33 C9                           xor ecx, ecx
00B862CD  48 FF 15 E4 B3 5C FF            call qword ptr [rip - 0xa34c1c]
00B862D4  0F 1F 44 00 00                  nop dword ptr [rax + rax]
00B862D9  85 C0                           test eax, eax
00B862DB  78 08                           js 0x140b862e5
00B862DD  89 3D C5 01 2E 00               mov dword ptr [rip + 0x2e01c5], edi
00B862E3  EB 18                           jmp 0x140b862fd
00B862E5  44 88 2D 30 47 28 00            mov byte ptr [rip + 0x284730], r13b
00B862EC  41 8A ED                        mov bpl, r13b
00B862EF  40 88 3D E6 12 3C 00            mov byte ptr [rip + 0x3c12e6], dil
00B862F6  40 88 3D 83 F9 3C 00            mov byte ptr [rip + 0x3cf983], dil
00B862FD  44 38 2D AC F9 3C 00            cmp byte ptr [rip + 0x3cf9ac], r13b
00B86304  75 56                           jne 0x140b8635c
00B86306  45 33 C0                        xor r8d, r8d
00B86309  44 88 2D D4 12 3C 00            mov byte ptr [rip + 0x3c12d4], r13b
00B86310  48 8D 15 F9 22 00 00            lea rdx, [rip + 0x22f9]
00B86317  C7 05 BF 12 3C 00 14 00 00 00   mov dword ptr [rip + 0x3c12bf], 0x14
00B86321  48 8D 0D D8 00 2E 00            lea rcx, [rip + 0x2e00d8]
00B86328  E8 A3 58 8D FF                  call 0x14045bbd0
00B8632D  48 8D 0D 0C 01 2E 00            lea rcx, [rip + 0x2e010c]
00B86334  E8 57 52 8D FF                  call 0x14045b590
00B86339  48 8D 05 10 23 00 00            lea rax, [rip + 0x2310]
00B86340  4C 89 2D 51 01 2E 00            mov qword ptr [rip + 0x2e0151], r13
00B86347  48 89 05 42 01 2E 00            mov qword ptr [rip + 0x2e0142], rax
00B8634E  4C 89 2D 2B 01 2E 00            mov qword ptr [rip + 0x2e012b], r13
00B86355  40 88 3D 54 F9 3C 00            mov byte ptr [rip + 0x3cf954], dil
00B8635C  44 38 2D 65 39 3D 00            cmp byte ptr [rip + 0x3d3965], r13b
00B86363  4C 89 2D 4E F9 3C 00            mov qword ptr [rip + 0x3cf94e], r13
00B8636A  74 27                           je 0x140b86393
00B8636C  44 38 2D AA 46 28 00            cmp byte ptr [rip + 0x2846aa], r13b
00B86373  74 1E                           je 0x140b86393
00B86375  40 88 3D A0 46 28 00            mov byte ptr [rip + 0x2846a0], dil
00B8637C  40 88 2D 30 F9 3C 00            mov byte ptr [rip + 0x3cf930], bpl
00B86383  40 88 3D 52 12 3C 00            mov byte ptr [rip + 0x3c1252], dil
00B8638A  44 88 2D EF F8 3C 00            mov byte ptr [rip + 0x3cf8ef], r13b
00B86391  EB 22                           jmp 0x140b863b5
00B86393  48 8B 05 6E EC 43 00            mov rax, qword ptr [rip + 0x43ec6e]
00B8639A  40 88 3D 57 12 3C 00            mov byte ptr [rip + 0x3c1257], dil
00B863A1  40 88 B8 D4 02 00 00            mov byte ptr [rax + 0x2d4], dil
00B863A8  44 38 2D D1 F8 3C 00            cmp byte ptr [rip + 0x3cf8d1], r13b
00B863AF  0F 85 E0 FE FF FF               jne 0x140b86295
00B863B5  44 38 2D 0C 39 3D 00            cmp byte ptr [rip + 0x3d390c], r13b
00B863BC  74 0D                           je 0x140b863cb
00B863BE  44 38 2D 33 12 3C 00            cmp byte ptr [rip + 0x3c1233], r13b
00B863C5  0F 84 CA FE FF FF               je 0x140b86295
00B863CB  44 88 2D 4A 46 28 00            mov byte ptr [rip + 0x28464a], r13b
00B863D2  45 84 E4                        test r12b, r12b
00B863D5  74 11                           je 0x140b863e8
00B863D7  E8 3C A5 A2 FF                  call 0x1405b0918
00B863DC  44 88 3D CF F8 3C 00            mov byte ptr [rip + 0x3cf8cf], r15b
00B863E3  E9 AD FE FF FF                  jmp 0x140b86295
00B863E8  48 85 DB                        test rbx, rbx
00B863EB  0F 84 DC 00 00 00               je 0x140b864cd
00B863F1  E8 1A 72 8D FF                  call 0x14045d610
00B863F6  84 C0                           test al, al
00B863F8  74 34                           je 0x140b8642e
00B863FA  44 38 2D F7 11 3C 00            cmp byte ptr [rip + 0x3c11f7], r13b
00B86401  74 2B                           je 0x140b8642e
00B86403  44 38 2D D2 11 3C 00            cmp byte ptr [rip + 0x3c11d2], r13b
00B8640A  75 22                           jne 0x140b8642e
00B8640C  80 0D 2F B4 67 00 02            or byte ptr [rip + 0x67b42f], 2
00B86413  B9 A2 06 00 00                  mov ecx, 0x6a2
00B86418  0F 32                           rdmsr
00B8641A  48 C1 E2 20                     shl rdx, 0x20
00B8641E  48 0B C2                        or rax, rdx
00B86421  48 83 C8 02                     or rax, 2
00B86425  48 8B D0                        mov rdx, rax
00B86428  48 C1 EA 20                     shr rdx, 0x20
00B8642C  0F 30                           wrmsr
00B8642E  4C 8D 73 10                     lea r14, [rbx + 0x10]
00B86432  41 8B F5                        mov esi, r13d
00B86435  49 8B 3E                        mov rdi, qword ptr [r14]
00B86438  BD 00 01 00 00                  mov ebp, 0x100
00B8643D  41 BF FF FF FF FF               mov r15d, 0xffffffff
00B86443  49 3B FE                        cmp rdi, r14
00B86446  74 75                           je 0x140b864bd
00B86448  83 FE 03                        cmp esi, 3
00B8644B  73 70                           jae 0x140b864bd
00B8644D  0F 57 C0                        xorps xmm0, xmm0
00B86450  B8 FF 00 00 00                  mov eax, 0xff
00B86455  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
00B8645A  44 0F B7 47 48                  movzx r8d, word ptr [rdi + 0x48]
00B8645F  41 8B D5                        mov edx, r13d
00B86462  4C 8B 4F 50                     mov r9, qword ptr [rdi + 0x50]
00B86466  41 D1 E8                        shr r8d, 1
00B86469  44 3B C5                        cmp r8d, ebp
00B8646C  44 0F 43 C0                     cmovae r8d, eax
00B86470  41 8A 01                        mov al, byte ptr [r9]
00B86473  4D 8D 49 02                     lea r9, [r9 + 2]
00B86477  8B CA                           mov ecx, edx
00B86479  FF C2                           inc edx
00B8647B  88 44 0C 30                     mov byte ptr [rsp + rcx + 0x30], al
00B8647F  41 3B D0                        cmp edx, r8d
00B86482  72 EC                           jb 0x140b86470
00B86484  8B C2                           mov eax, edx
00B86486  48 3B C5                        cmp rax, rbp
00B86489  73 2C                           jae 0x140b864b7
00B8648B  44 88 6C 14 30                  mov byte ptr [rsp + rdx + 0x30], r13b
00B86490  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00B86495  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
00B8649A  E8 A1 AA 8E FF                  call 0x140470f40
00B8649F  48 8B 57 30                     mov rdx, qword ptr [rdi + 0x30]
00B864A3  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00B864A8  4D 8B C7                        mov r8, r15
00B864AB  E8 70 7D 92 FF                  call 0x1404ae220
00B864B0  48 8B 3F                        mov rdi, qword ptr [rdi]
00B864B3  FF C6                           inc esi
00B864B5  EB 8C                           jmp 0x140b86443
00B864B7  E8 20 FB 96 FF                  call 0x1404f5fdc
00B864BC  CC                              int3
00B864BD  E8 BE 69 81 FF                  call 0x14039ce80
00B864C2  88 05 01 38 3D 00               mov byte ptr [rip + 0x3d3801], al
00B864C8  E9 D1 FD FF FF                  jmp 0x140b8629e
00B864CD  48 8B 15 A4 AB 27 00            mov rdx, qword ptr [rip + 0x27aba4]
00B864D4  4C 8B C6                        mov r8, rsi
00B864D7  33 C9                           xor ecx, ecx
00B864D9  E8 42 7D 92 FF                  call 0x1404ae220
00B864DE  EB 61                           jmp 0x140b86541
00B864E0  48 8D 0D D9 37 3D 00            lea rcx, [rip + 0x3d37d9]
00B864E7  E8 F4 82 7F FF                  call 0x14037e7e0
00B864EC  44 38 2D 29 45 28 00            cmp byte ptr [rip + 0x284529], r13b
00B864F3  75 45                           jne 0x140b8653a
00B864F5  8B 05 85 05 44 00               mov eax, dword ptr [rip + 0x440585]
00B864FB  41 8B FD                        mov edi, r13d
00B864FE  85 C0                           test eax, eax
00B86500  74 38                           je 0x140b8653a
00B86502  BA 00 10 00 00                  mov edx, 0x1000
00B86507  B9 40 00 00 00                  mov ecx, 0x40
00B8650C  41 B8 4B 64 49 6F               mov r8d, 0x6f49644b
00B86512  E8 D9 BB FF FF                  call 0x140b820f0
00B86517  48 85 C0                        test rax, rax
00B8651A  74 12                           je 0x140b8652e
00B8651C  F0 44 09 2C 24                  lock or dword ptr [rsp], r13d
00B86521  8B CF                           mov ecx, edi
00B86523  48 8D 15 96 F7 3C 00            lea rdx, [rip + 0x3cf796]
00B8652A  48 89 04 CA                     mov qword ptr [rdx + rcx*8], rax
00B8652E  8B 0D 4C 05 44 00               mov ecx, dword ptr [rip + 0x44054c]
00B86534  FF C7                           inc edi
00B86536  3B F9                           cmp edi, ecx
00B86538  72 C8                           jb 0x140b86502
00B8653A  4C 89 2D 67 F7 3C 00            mov qword ptr [rip + 0x3cf767], r13
00B86541  B0 01                           mov al, 1
00B86543  48 8B 8C 24 30 01 00 00         mov rcx, qword ptr [rsp + 0x130]
00B8654B  48 33 CC                        xor rcx, rsp
00B8654E  E8 ED 60 B2 FF                  call 0x1406ac640
00B86553  48 8B 9C 24 90 01 00 00         mov rbx, qword ptr [rsp + 0x190]
00B8655B  48 81 C4 40 01 00 00            add rsp, 0x140
00B86562  41 5F                           pop r15
00B86564  41 5E                           pop r14
00B86566  41 5D                           pop r13
00B86568  41 5C                           pop r12
00B8656A  5F                              pop rdi
00B8656B  5E                              pop rsi
00B8656C  5D                              pop rbp
00B8656D  C3                              ret
00B8656E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KdInitSystem(int a1, __int64 a2)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m158;
    unsigned int v_stack_m178;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_p18;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (320);
    result = (*(unsigned __int64 *)(v_rip + 2640114)) ^ (v_rsp);
    v_stack_m48 = result;
    v_r13 = 0;
    if (a1 != ((unsigned int)((unsigned int)(0xFFFFFFFFULL)))) goto loc_00B85E8E;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 240) + 132)))) & (8)) == 0) goto loc_00B86541;
    goto loc_00B86541;
loc_00B85E8E:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 240) + 132))) != 0) goto loc_00B864E0;
    if ((*(unsigned __int8 *)(v_rip + 3938139)) != 0) goto loc_00B86295;
    *(unsigned int *)(v_rip + 3016183) = 0;
    *(unsigned __int8 *)(v_rip + 4013585) = 0;
    if ((*(unsigned __int8 *)(v_rip + 2640754)) == 0) goto loc_00B85EC6;
    v_r14 = (unsigned __int8)(v_r13 + 1);
    if ((*(unsigned __int8 *)(v_rip + 3997119)) == 0) {
        v_r14 = 0;
    }
    if (*(unsigned __int64 *)(v_rip + 4438736) == 0) goto loc_00B85EE8;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4438736) + 236)) == 3) {
        *(unsigned int *)(v_rip + 2640736) = 0x480ULL;
    }
    result = *(unsigned __int64 *)(v_rip + 4438736);
    v_rdi = v_r13 + 1;
    if ((*(unsigned __int64 *)(v_rip + 3997057)) == 0) {
        *(unsigned __int64 *)(v_rip + 3938028) = *(unsigned __int64 *)(v_rip + 4438736);
        result = MmGetPagedPoolCommitPointer((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 240) + 132)), a2, a3, a4);
        *(unsigned __int64 *)(v_rip + 2601672) = result;
        v_rdi = v_rip + 3997025;
        result = v_rip + 3997050;
        *(unsigned __int64 *)(v_rip + 3016067) = 0;
        a2 = v_rip + 2601276;
        *(unsigned __int64 *)(v_rip + 3997037) = result;
        *(unsigned __int64 *)(v_rip + 3997022) = result;
        *(unsigned __int64 *)(v_rip + 3996991) = v_rdi;
        *(unsigned __int64 *)(v_rip + 3996976) = v_rdi;
        result = KdRegisterDebuggerDataBlock((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 240) + 132)), a2, a3, a4);
        result = *(unsigned int *)(v_rip + 2639873);
        *(unsigned __int16 *)(v_rip + 2640592) = (unsigned __int16)(result);
        result = (unsigned int)((result) >> (28));
        *(unsigned __int16 *)(v_rip + 2640580) = (unsigned __int16)(result);
        result = v_rip + 3601757;
        *(unsigned __int64 *)(v_rip + 2640598) = v_rdi;
        v_rdi = 1;
        *(unsigned __int64 *)(v_rip + 2640571) = result;
        *(unsigned __int16 *)(v_rip + 2640549) = 0x3303ULL;
    }
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36800)) == 0) {
        result = *(unsigned __int64 *)(gs_base + (0 + 32)) + 496;
        *(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36808) = 0x10000BULL;
        *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36800) = result;
    }
    if (a2 == 0) goto loc_00B8625A;
    *(unsigned __int64 *)(v_rip + 2601830) = v_rip + 3996893;
    *(unsigned __int64 *)(v_rip + 3996879) = a2 + 16;
    *(unsigned __int64 *)(v_rip + 2640457) = *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 16) + 48);
    if (*(unsigned __int64 *)(a2 + 216) == 0) goto loc_00B86242;
    result = strupr(*(unsigned __int64 *)(a2 + 216), a2 + 16, a3, a4);
    *(unsigned int *)(v_rip + 3996762) = 0;
    result = strstr(*(unsigned __int64 *)(a2 + 216), v_rip + 19425, a3, a4);
    v_stack_m158 = result;
    if (result == 0) goto loc_00B86053;
    result = atol(result + 18, v_rip + 19425, a3, a4);
    result = (unsigned int)((result) + (0xFFFULL));
    result = (unsigned int)((result) & (0xFFFFF000ULL));
    *(unsigned int *)(v_rip + 3996711) = (unsigned int)(result);
    if (((unsigned int)(result)) <= ((unsigned int)((unsigned int)(0x1000000ULL)))) goto loc_00B86045;
    *(unsigned int *)(v_rip + 3996701) = (unsigned int)((unsigned int)(0x1000000ULL));
    goto loc_00B86053;
loc_00B86045:
    if (((unsigned int)(result)) <= 0x1000ULL) {
        *(unsigned int *)(v_rip + 3996685) = 0;
    }
    result = strstr(*(unsigned __int64 *)(a2 + 216), v_rip + 19366, a3, a4);
    v_stack_m158 = result;
    if (result == 0) goto loc_00B86086;
    *(unsigned __int8 *)(v_rip + 2640297) = (unsigned __int8)(v_rdi);
    *(unsigned __int8 *)(v_rip + 3996712) = (unsigned __int8)(v_rdi);
    *(unsigned __int8 *)(v_rip + 2640284) = (unsigned __int8)(v_rdi);
    goto loc_00B86115;
loc_00B86086:
    result = strstr(*(unsigned __int64 *)(a2 + 216), v_rip + 19331, a3, a4);
    v_stack_m158 = result;
    if (result == 0) goto loc_00B860C7;
    *(unsigned __int8 *)(v_rip + 2640246) = (unsigned __int8)(v_rdi);
    *(unsigned __int8 *)(v_rip + 3996658) = (unsigned __int8)(v_rdi);
    *(unsigned __int8 *)(v_rip + 3937573) = (unsigned __int8)(v_rdi);
    *(unsigned __int8 *)(v_rip + 3996610) = (unsigned __int8)(v_rdi);
    *(unsigned __int8 *)(v_rip + 2640216) = 0;
    goto loc_00B86115;
loc_00B860C7:
loc_00B860CA:
    result = strstr(*(unsigned __int64 *)(a2 + 216), v_rip + 19279, a3, a4);
    if (result != 0) goto loc_00B860F2;
    result = strstr(*(unsigned __int64 *)(a2 + 216), v_rip + 19131, a3, a4);
    if (result == 0) goto loc_00B86110;
loc_00B860F2:
    if (((unsigned __int8)(*(unsigned __int8 *)(result + 6))) == 61) goto loc_00B86139;
    if ((((unsigned __int8)(*(unsigned __int8 *)(result + 6))) & (223)) == 0) goto loc_00B86139;
    if (result == 0) goto loc_00B86110;
    if (result + 6 != 0) goto loc_00B860CA;
loc_00B86110:
loc_00B86115:
    result = strstr(*(unsigned __int64 *)(a2 + 216), v_rip + 19220, a3, a4);
    if (result == 0) goto loc_00B861FB;
    *(unsigned __int8 *)(v_rip + 4012948) = 0;
    goto loc_00B86220;
loc_00B86139:
    *(unsigned __int8 *)(v_rip + 2640088) = 0;
    if ((*(unsigned __int8 *)(result + 6)) != 61) goto loc_00B86115;
    a1 = (*(unsigned __int64 *)(a2 + 216)) + (7);
loc_00B86152:
    goto loc_00B86172;
loc_00B86159:
    if (((unsigned __int8)(*(unsigned __int8 *)(a1))) > 44) goto loc_00B8616D;
    if (((unsigned __int8)(*(unsigned __int8 *)(a1))) < 44) goto loc_00B86176;
loc_00B8616D:
    v_rdi = (a1) + 1;
loc_00B86172:
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rdi)) != 0) goto loc_00B86159;
loc_00B86176:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) - (a1));
    if (condition_is_equal) goto loc_00B86110;
    if (((unsigned int)(result)) != 10) goto loc_00B861A3;
    result = strncmp(a1, v_rip + 18981, (unsigned int)((unsigned int)(result)), a4);
    if ((unsigned int)(result) != 0) goto loc_00B861E9;
    *(unsigned __int8 *)(v_rip + 3996419) = 1;
    goto loc_00B861E9;
loc_00B861A3:
    if (((unsigned int)(result)) != 7) goto loc_00B861CA;
    result = strncmp(a1, v_rip + 18958, (unsigned int)((unsigned int)(result)), a4);
    if ((unsigned int)(result) != 0) goto loc_00B861E9;
    *(unsigned __int8 *)(v_rip + 3996380) = 0;
    goto loc_00B861E9;
loc_00B861CA:
    if (((unsigned int)(result)) != 6) goto loc_00B861E9;
    result = strncmp(a1, v_rip + 18935, (unsigned int)((unsigned int)(result)), a4);
    if ((unsigned int)(result) == 0) {
        *(unsigned __int8 *)(v_rip + 3996343) = 1;
    }
    if ((*(unsigned __int8 *)(v_rdi)) != 44) goto loc_00B86110;
    goto loc_00B86152;
loc_00B861FB:
    result = strstr(*(unsigned __int64 *)(a2 + 216), v_rip + 19006, (unsigned int)((unsigned int)(result)), a4);
    v_rbp = 1;
    if (result != 0) {
        *(unsigned __int8 *)(v_rip + 4012722) = (unsigned __int8)(v_rdi);
        v_rbp = (unsigned __int8)(v_rdi);
        *(unsigned __int8 *)(v_rip + 3996290) = 0;
    }
    result = strstr(*(unsigned __int64 *)(a2 + 216), v_rip + 18985, (unsigned int)((unsigned int)(result)), a4);
    if (result == 0) goto loc_00B8626B;
    *(unsigned __int8 *)(v_rip + 3996273) = (unsigned __int8)(v_rdi);
    goto loc_00B8626B;
loc_00B86242:
    *(unsigned __int8 *)(v_rip + 2639827) = (unsigned __int8)(v_rdi);
    *(unsigned __int8 *)(v_rip + 3996239) = (unsigned __int8)(v_rdi);
    goto loc_00B8626B;
loc_00B8625A:
    *(unsigned __int64 *)(v_rip + 2639813) = *(unsigned __int64 *)(v_rip + 4458695);
loc_00B8626B:
    *(unsigned __int64 *)(v_rip + 2600447) = *(unsigned __int64 *)(v_rip + 2639806);
    if ((unsigned __int8)((unsigned __int8)(v_rdi)) != 0) goto loc_00B862FD;
    if (a2 == 0) goto loc_00B86289;
    if ((*(unsigned int *)(a2 + 12)) < 2) goto loc_00B8628E;
loc_00B86289:
    if ((unsigned __int8)((unsigned __int8)(v_rdi)) != 0) goto loc_00B862C1;
loc_00B8628E:
    *(unsigned __int8 *)(v_rip + 3937095) = (unsigned __int8)(v_rdi);
loc_00B86295:
    if (a2 == 0) goto loc_00B86541;
loc_00B8629E:
    if (*(unsigned __int64 *)(a2 + 240) == 0) goto loc_00B86541;
    v_rdi = (*(unsigned __int64 *)(a2 + 240)) + (0x9A0ULL);
    result = 0;
    goto loc_00B86541;
loc_00B862C1:
    a1 = 0;
    result = kdcom_dll_KdInitialize(a1, a2, v_rip + 3937048, a4);
    if (sign_flag) goto loc_00B862E5;
    *(unsigned int *)(v_rip + 3015109) = (unsigned int)(v_rdi);
    goto loc_00B862FD;
loc_00B862E5:
    *(unsigned __int8 *)(v_rip + 2639664) = 0;
    *(unsigned __int8 *)(v_rip + 3936998) = (unsigned __int8)(v_rdi);
    *(unsigned __int8 *)(v_rip + 3996035) = (unsigned __int8)(v_rdi);
loc_00B862FD:
    if ((*(unsigned __int8 *)(v_rip + 3996076)) == 0) {
        a3 = 0;
        *(unsigned __int8 *)(v_rip + 3936980) = 0;
        a2 = v_rip + 8953;
        *(unsigned int *)(v_rip + 3936959) = 20;
        a1 = v_rip + 3014872;
        result = KeInitializeDpc(a1, a2, a3, a4);
        a1 = v_rip + 3014924;
        result = KeInitializeTimer(a1, a2, a3, a4);
        result = v_rip + 8976;
        *(unsigned __int64 *)(v_rip + 3014993) = 0;
        *(unsigned __int64 *)(v_rip + 3014978) = result;
        *(unsigned __int64 *)(v_rip + 3014955) = 0;
        *(unsigned __int8 *)(v_rip + 3995988) = (unsigned __int8)(v_rdi);
    }
    *(unsigned __int64 *)(v_rip + 3995982) = 0;
    if ((*(unsigned __int8 *)(v_rip + 4012389)) == 0) goto loc_00B86393;
    if ((*(unsigned __int8 *)(v_rip + 2639530)) == 0) goto loc_00B86393;
    *(unsigned __int8 *)(v_rip + 2639520) = (unsigned __int8)(v_rdi);
    *(unsigned __int8 *)(v_rip + 3995952) = 0;
    *(unsigned __int8 *)(v_rip + 3936850) = (unsigned __int8)(v_rdi);
    *(unsigned __int8 *)(v_rip + 3995887) = 0;
    goto loc_00B863B5;
loc_00B86393:
    *(unsigned __int8 *)(v_rip + 3936855) = (unsigned __int8)(v_rdi);
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 4451438) + 724) = (unsigned __int8)(v_rdi);
    if ((*(unsigned __int8 *)(v_rip + 3995857)) != 0) goto loc_00B86295;
loc_00B863B5:
    if ((*(unsigned __int8 *)(v_rip + 4012300)) == 0) goto loc_00B863CB;
    if ((*(unsigned __int8 *)(v_rip + 3936819)) == 0) goto loc_00B86295;
loc_00B863CB:
    *(unsigned __int8 *)(v_rip + 2639434) = 0;
    if (1 == 0) goto loc_00B863E8;
    result = KdDisableDebuggerWithLock(a1, a2, a3, a4);
    *(unsigned __int8 *)(v_rip + 3995855) = 1;
    goto loc_00B86295;
loc_00B863E8:
    if (a2 == 0) goto loc_00B864CD;
    result = KeIsKernelCetEnabled(a1, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00B8642E;
    if ((*(unsigned __int8 *)(v_rip + 3936759)) == 0) goto loc_00B8642E;
    if ((*(unsigned __int8 *)(v_rip + 3936722)) == 0) {
        a1 = 0x6A2ULL;
        a2 = (a2) << (32);
        result = (result) | (a2);
        result = (result) | (2);
        a2 = result;
        a2 = (a2) >> (32);
    }
loc_00B86443:
    if ((*(unsigned __int64 *)(a2 + 16)) == (a2 + 16)) goto loc_00B864BD;
    if (0 >= 3) goto loc_00B864BD;
    v_stack_m158 = v_xmm0;
    a3 = (unsigned int)((*(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 16) + 72)) >> (1));
    if (((unsigned int)(a3)) >= 256) { a3 = 255; }
loc_00B86470:
    a2 = (unsigned int)((0) + 1);
    *(unsigned __int8 *)(v_rsp + 0 * 1 + 48) = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 16) + 80)));
    if (((unsigned int)(a2)) < ((unsigned int)(a3))) goto loc_00B86470;
    if (((unsigned int)((unsigned int)(a2))) >= 256) goto loc_00B864B7;
    *(unsigned __int8 *)(v_rsp + a2 * 1 + 48) = 0;
    result = RtlInitAnsiString(v_stack_m158, v_stack_m148, a3, *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 16) + 80) + 2);
    result = DbgLoadImageSymbols(v_stack_m158, *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 16) + 48), (unsigned int)(0xFFFFFFFFULL), *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 16) + 80) + 2);
    v_rsi = (unsigned int)((0) + 1);
    goto loc_00B86443;
loc_00B864B7:
    result = _report_rangecheckfailure(v_stack_m158, *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 16) + 48), (unsigned int)(0xFFFFFFFFULL), *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 16) + 80) + 2);
loc_00B864BD:
    result = KdPollBreakIn(v_stack_m158, *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 16) + 48), (unsigned int)(0xFFFFFFFFULL), *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 16) + 80) + 2);
    *(unsigned __int8 *)(v_rip + 4012033) = (unsigned __int8)(result);
    goto loc_00B8629E;
loc_00B864CD:
    a1 = 0;
    result = DbgLoadImageSymbols(a1, *(unsigned __int64 *)(v_rip + 2599844), v_rsi, *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 16) + 80) + 2);
    goto loc_00B86541;
loc_00B864E0:
    result = KeQueryPerformanceCounter(v_rip + 4011993, *(unsigned __int64 *)(v_rip + 2599844), v_rsi, *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 16) + 80) + 2);
    if ((*(unsigned __int8 *)(v_rip + 2639145)) != 0) goto loc_00B8653A;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4457861))) == 0) goto loc_00B8653A;
loc_00B86502:
    result = ExAllocatePool2(64, (unsigned int)(0x1000ULL), (unsigned int)(0x6F49644BULL), *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 16) + 80) + 2);
    if (result != 0) {
        a1 = 0;
        a2 = v_rip + 3995542;
        *(unsigned __int64 *)(a2 + a1 * 8) = result;
    }
    v_rdi = (unsigned int)((0) + 1);
    if (((unsigned int)(v_rdi)) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4457804))))) goto loc_00B86502;
loc_00B8653A:
    *(unsigned __int64 *)(v_rip + 3995495) = 0;
loc_00B86541:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, (unsigned int)(0x6F49644BULL), *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 16) + 80) + 2);
    v_rsp = (v_rsp) + (320);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KdInitSystem(int32_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m148;
    uint64_t v_stack_m158;
    uint32_t v_stack_m178;
    uint64_t v_stack_m48;
    uint64_t v_stack_p18;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (320);
    result = (*(uint64_t *)(v_rip + 0x2848F2)) ^ (local_rsp);
    v_stack_m48 = result;
    local_r13 = 0;
    if (Arg1 != ((uint32_t)((uint32_t)(0xFFFFFFFFULL)))) goto loc_00B85E8E;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0xF0) + 0x84)))) & (8)) == 0) goto loc_00B86541;
    goto loc_00B86541;
loc_00B85E8E:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0xF0) + 0x84))) != 0) goto loc_00B864E0;
    if ((*(uint8_t *)(v_rip + 0x3C175B)) != 0) goto loc_00B86295;
    *(uint32_t *)(v_rip + 0x2E05F7) = 0;
    *(uint8_t *)(v_rip + 0x3D3E11) = 0;
    if ((*(uint8_t *)(v_rip + 0x284B72)) == 0) goto loc_00B85EC6;
    local_r14 = (uint8_t)(local_r13 + 1);
    if ((*(uint8_t *)(v_rip + 0x3CFDBF)) == 0) {
        local_r14 = 0;
    }
    if (*(uint64_t *)(v_rip + 0x43BAD0) == 0) goto loc_00B85EE8;
    if ((*(uint32_t *)(*(uint64_t *)(v_rip + 0x43BAD0) + 0xEC)) == 3) {
        *(uint32_t *)(v_rip + 0x284B60) = 0x480ULL;
    }
    result = *(uint64_t *)(v_rip + 0x43BAD0);
    local_rdi = local_r13 + 1;
    if ((*(uint64_t *)(v_rip + 0x3CFD81)) == 0) {
        *(uint64_t *)(v_rip + 0x3C16EC) = *(uint64_t *)(v_rip + 0x43BAD0);
        result = MmGetPagedPoolCommitPointer((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0xF0) + 0x84)), Arg2, a3, a4);
        *(uint64_t *)(v_rip + 0x27B2C8) = result;
        local_rdi = v_rip + 3997025;
        result = v_rip + 3997050;
        *(uint64_t *)(v_rip + 0x2E0583) = 0;
        Arg2 = v_rip + 2601276;
        *(uint64_t *)(v_rip + 0x3CFD6D) = result;
        *(uint64_t *)(v_rip + 0x3CFD5E) = result;
        *(uint64_t *)(v_rip + 0x3CFD3F) = local_rdi;
        *(uint64_t *)(v_rip + 0x3CFD30) = local_rdi;
        result = KdRegisterDebuggerDataBlock((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0xF0) + 0x84)), Arg2, a3, a4);
        result = *(uint32_t *)(v_rip + 0x284801);
        *(uint16_t *)(v_rip + 0x284AD0) = (uint16_t)(result);
        result = (uint32_t)((result) >> (28));
        *(uint16_t *)(v_rip + 0x284AC4) = (uint16_t)(result);
        result = v_rip + 3601757;
        *(uint64_t *)(v_rip + 0x284AD6) = local_rdi;
        local_rdi = 1;
        *(uint64_t *)(v_rip + 0x284ABB) = result;
        *(uint16_t *)(v_rip + 0x284AA5) = 0x3303ULL;
    }
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8FC0)) == 0) {
        result = *(uint64_t *)(gs_base + (0 + 0x20)) + 496;
        *(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8FC8) = 0x10000BULL;
        *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8FC0) = result;
    }
    if (Arg2 == NULL) goto loc_00B8625A;
    *(uint64_t *)(v_rip + 0x27B366) = v_rip + 3996893;
    *(void **)(v_rip + 0x3CFCCF) = Arg2 + 16;
    *(uint64_t *)(v_rip + 0x284A49) = *(uint64_t *)(*(uint64_t *)(arg2 + 0x10) + 0x30);
    if (*(uint64_t *)(arg2 + 0xD8) == 0) goto loc_00B86242;
    result = strupr(*(uint64_t *)(arg2 + 0xD8), Arg2 + 16, a3, a4);
    *(uint32_t *)(v_rip + 0x3CFC5A) = 0;
    result = strstr(*(uint64_t *)(arg2 + 0xD8), v_rip + 19425, a3, a4);
    v_stack_m158 = result;
    if (result == 0) goto loc_00B86053;
    result = atol(result + 18, v_rip + 19425, a3, a4);
    result = (uint32_t)((result) + (0xFFFULL));
    result = (uint32_t)((result) & (0xFFFFF000ULL));
    *(uint32_t *)(v_rip + 0x3CFC27) = (uint32_t)(result);
    if (((uint32_t)(result)) <= ((uint32_t)((uint32_t)(0x1000000ULL)))) goto loc_00B86045;
    *(uint32_t *)(v_rip + 0x3CFC1D) = (uint32_t)((uint32_t)(0x1000000ULL));
    goto loc_00B86053;
loc_00B86045:
    if (((uint32_t)(result)) <= 0x1000ULL) {
        *(uint32_t *)(v_rip + 0x3CFC0D) = 0;
    }
    result = strstr(*(uint64_t *)(arg2 + 0xD8), v_rip + 19366, a3, a4);
    v_stack_m158 = result;
    if (result == 0) goto loc_00B86086;
    *(uint8_t *)(v_rip + 0x2849A9) = (uint8_t)(local_rdi);
    *(uint8_t *)(v_rip + 0x3CFC28) = (uint8_t)(local_rdi);
    *(uint8_t *)(v_rip + 0x28499C) = (uint8_t)(local_rdi);
    goto loc_00B86115;
loc_00B86086:
    result = strstr(*(uint64_t *)(arg2 + 0xD8), v_rip + 19331, a3, a4);
    v_stack_m158 = result;
    if (result == 0) goto loc_00B860C7;
    *(uint8_t *)(v_rip + 0x284976) = (uint8_t)(local_rdi);
    *(uint8_t *)(v_rip + 0x3CFBF2) = (uint8_t)(local_rdi);
    *(uint8_t *)(v_rip + 0x3C1525) = (uint8_t)(local_rdi);
    *(uint8_t *)(v_rip + 0x3CFBC2) = (uint8_t)(local_rdi);
    *(uint8_t *)(v_rip + 0x284958) = 0;
    goto loc_00B86115;
loc_00B860C7:
loc_00B860CA:
    result = strstr(*(uint64_t *)(arg2 + 0xD8), v_rip + 19279, a3, a4);
    if (result != 0) goto loc_00B860F2;
    result = strstr(*(uint64_t *)(arg2 + 0xD8), v_rip + 19131, a3, a4);
    if (result == 0) goto loc_00B86110;
loc_00B860F2:
    if (((uint8_t)(*(uint8_t *)(result + 0x6))) == 61) goto loc_00B86139;
    if ((((uint8_t)(*(uint8_t *)(result + 0x6))) & (223)) == 0) goto loc_00B86139;
    if (result == 0) goto loc_00B86110;
    if (result + 6 != 0) goto loc_00B860CA;
loc_00B86110:
loc_00B86115:
    result = strstr(*(uint64_t *)(arg2 + 0xD8), v_rip + 19220, a3, a4);
    if (result == 0) goto loc_00B861FB;
    *(uint8_t *)(v_rip + 0x3D3B94) = 0;
    goto loc_00B86220;
loc_00B86139:
    *(uint8_t *)(v_rip + 0x2848D8) = 0;
    if ((*(uint8_t *)(result + 0x6)) != 61) goto loc_00B86115;
    Arg1 = (*(uint64_t *)(arg2 + 0xD8)) + (7);
loc_00B86152:
    goto loc_00B86172;
loc_00B86159:
    if (((uint8_t)(*(uint8_t *)(Arg1))) > 44) goto loc_00B8616D;
    if (((uint8_t)(*(uint8_t *)(Arg1))) < 44) goto loc_00B86176;
loc_00B8616D:
    local_rdi = (Arg1) + 1;
loc_00B86172:
    if ((uint8_t)(*(uint8_t *)(local_rdi)) != 0) goto loc_00B86159;
loc_00B86176:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) - (Arg1));
    if (condition_is_equal) goto loc_00B86110;
    if (((uint32_t)(result)) != 10) goto loc_00B861A3;
    result = strncmp(Arg1, v_rip + 18981, (uint32_t)((uint32_t)(result)), a4);
    if ((uint32_t)(result) != 0) goto loc_00B861E9;
    *(uint8_t *)(v_rip + 0x3CFB03) = 1;
    goto loc_00B861E9;
loc_00B861A3:
    if (((uint32_t)(result)) != 7) goto loc_00B861CA;
    result = strncmp(Arg1, v_rip + 18958, (uint32_t)((uint32_t)(result)), a4);
    if ((uint32_t)(result) != 0) goto loc_00B861E9;
    *(uint8_t *)(v_rip + 0x3CFADC) = 0;
    goto loc_00B861E9;
loc_00B861CA:
    if (((uint32_t)(result)) != 6) goto loc_00B861E9;
    result = strncmp(Arg1, v_rip + 18935, (uint32_t)((uint32_t)(result)), a4);
    if ((uint32_t)(result) == 0) {
        *(uint8_t *)(v_rip + 0x3CFAB7) = 1;
    }
    if ((*(uint8_t *)(local_rdi)) != 44) goto loc_00B86110;
    goto loc_00B86152;
loc_00B861FB:
    result = strstr(*(uint64_t *)(arg2 + 0xD8), v_rip + 19006, (uint32_t)((uint32_t)(result)), a4);
    local_rbp = 1;
    if (result != 0) {
        *(uint8_t *)(v_rip + 0x3D3AB2) = (uint8_t)(local_rdi);
        local_rbp = (uint8_t)(local_rdi);
        *(uint8_t *)(v_rip + 0x3CFA82) = 0;
    }
    result = strstr(*(uint64_t *)(arg2 + 0xD8), v_rip + 18985, (uint32_t)((uint32_t)(result)), a4);
    if (result == 0) goto loc_00B8626B;
    *(uint8_t *)(v_rip + 0x3CFA71) = (uint8_t)(local_rdi);
    goto loc_00B8626B;
loc_00B86242:
    *(uint8_t *)(v_rip + 0x2847D3) = (uint8_t)(local_rdi);
    *(uint8_t *)(v_rip + 0x3CFA4F) = (uint8_t)(local_rdi);
    goto loc_00B8626B;
loc_00B8625A:
    *(uint64_t *)(v_rip + 0x2847C5) = *(uint64_t *)(v_rip + 0x4408C7);
loc_00B8626B:
    *(uint64_t *)(v_rip + 0x27ADFF) = *(uint64_t *)(v_rip + 0x2847BE);
    if ((uint8_t)((uint8_t)(local_rdi)) != 0) goto loc_00B862FD;
    if (Arg2 == NULL) goto loc_00B86289;
    if ((*(uint32_t *)(arg2 + 0xC)) < 2) goto loc_00B8628E;
loc_00B86289:
    if ((uint8_t)((uint8_t)(local_rdi)) != 0) goto loc_00B862C1;
loc_00B8628E:
    *(uint8_t *)(v_rip + 0x3C1347) = (uint8_t)(local_rdi);
loc_00B86295:
    if (Arg2 == NULL) goto loc_00B86541;
loc_00B8629E:
    if (*(uint64_t *)(arg2 + 0xF0) == 0) goto loc_00B86541;
    local_rdi = (*(uint64_t *)(arg2 + 0xF0)) + (0x9A0ULL);
    result = 0;
    goto loc_00B86541;
loc_00B862C1:
    Arg1 = 0;
    result = kernel_indirect_call(Arg1, Arg2, v_rip + 3937048, a4);
    if (sign_flag) goto loc_00B862E5;
    *(uint32_t *)(v_rip + 0x2E01C5) = (uint32_t)(local_rdi);
    goto loc_00B862FD;
loc_00B862E5:
    *(uint8_t *)(v_rip + 0x284730) = 0;
    *(uint8_t *)(v_rip + 0x3C12E6) = (uint8_t)(local_rdi);
    *(uint8_t *)(v_rip + 0x3CF983) = (uint8_t)(local_rdi);
loc_00B862FD:
    if ((*(uint8_t *)(v_rip + 0x3CF9AC)) == 0) {
        a3 = 0;
        *(uint8_t *)(v_rip + 0x3C12D4) = 0;
        Arg2 = v_rip + 8953;
        *(uint32_t *)(v_rip + 0x3C12BF) = 20;
        Arg1 = v_rip + 3014872;
        result = KeInitializeDpc(Arg1, Arg2, a3, a4);
        Arg1 = v_rip + 3014924;
        result = KeInitializeTimer(Arg1, Arg2, a3, a4);
        result = v_rip + 8976;
        *(uint64_t *)(v_rip + 0x2E0151) = 0;
        *(uint64_t *)(v_rip + 0x2E0142) = result;
        *(uint64_t *)(v_rip + 0x2E012B) = 0;
        *(uint8_t *)(v_rip + 0x3CF954) = (uint8_t)(local_rdi);
    }
    *(uint64_t *)(v_rip + 0x3CF94E) = 0;
    if ((*(uint8_t *)(v_rip + 0x3D3965)) == 0) goto loc_00B86393;
    if ((*(uint8_t *)(v_rip + 0x2846AA)) == 0) goto loc_00B86393;
    *(uint8_t *)(v_rip + 0x2846A0) = (uint8_t)(local_rdi);
    *(uint8_t *)(v_rip + 0x3CF930) = 0;
    *(uint8_t *)(v_rip + 0x3C1252) = (uint8_t)(local_rdi);
    *(uint8_t *)(v_rip + 0x3CF8EF) = 0;
    goto loc_00B863B5;
loc_00B86393:
    *(uint8_t *)(v_rip + 0x3C1257) = (uint8_t)(local_rdi);
    *(uint8_t *)(*(uint64_t *)(v_rip + 0x43EC6E) + 0x2D4) = (uint8_t)(local_rdi);
    if ((*(uint8_t *)(v_rip + 0x3CF8D1)) != 0) goto loc_00B86295;
loc_00B863B5:
    if ((*(uint8_t *)(v_rip + 0x3D390C)) == 0) goto loc_00B863CB;
    if ((*(uint8_t *)(v_rip + 0x3C1233)) == 0) goto loc_00B86295;
loc_00B863CB:
    *(uint8_t *)(v_rip + 0x28464A) = 0;
    if (1 == 0) goto loc_00B863E8;
    result = KdDisableDebuggerWithLock(Arg1, Arg2, a3, a4);
    *(uint8_t *)(v_rip + 0x3CF8CF) = 1;
    goto loc_00B86295;
loc_00B863E8:
    if (Arg2 == NULL) goto loc_00B864CD;
    result = KeIsKernelCetEnabled(Arg1, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00B8642E;
    if ((*(uint8_t *)(v_rip + 0x3C11F7)) == 0) goto loc_00B8642E;
    if ((*(uint8_t *)(v_rip + 0x3C11D2)) == 0) {
        Arg1 = 0x6A2ULL;
        Arg2 = (Arg2) << (32);
        result = (result) | (Arg2);
        result = (result) | (2);
        Arg2 = result;
        Arg2 = (Arg2) >> (32);
    }
loc_00B86443:
    if ((*(uint64_t *)(arg2 + 0x10)) == (Arg2 + 16)) goto loc_00B864BD;
    if (0 >= 3) goto loc_00B864BD;
    v_stack_m158 = v_xmm0;
    a3 = (uint32_t)((*(uint16_t *)(*(uint64_t *)(arg2 + 0x10) + 0x48)) >> (1));
    if (((uint32_t)(a3)) >= 256) { a3 = 255; }
loc_00B86470:
    Arg2 = (uint32_t)((0) + 1);
    *(uint8_t *)(local_rsp + 0x0 * 1 + 0x30) = (uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x10) + 0x50)));
    if (((uint32_t)(Arg2)) < ((uint32_t)(a3))) goto loc_00B86470;
    if (((uint32_t)((uint32_t)(Arg2))) >= 256) goto loc_00B864B7;
    *(uint8_t *)(local_rsp + arg2 * 1 + 0x30) = 0;
    result = RtlInitAnsiString(v_stack_m158, v_stack_m148, a3, *(uint64_t *)(*(uint64_t *)(arg2 + 0x10) + 0x50) + 2);
    result = DbgLoadImageSymbols(v_stack_m158, *(uint64_t *)(*(uint64_t *)(arg2 + 0x10) + 0x30), (uint32_t)(0xFFFFFFFFULL), *(uint64_t *)(*(uint64_t *)(arg2 + 0x10) + 0x50) + 2);
    local_rsi = (uint32_t)((0) + 1);
    goto loc_00B86443;
loc_00B864B7:
    result = _report_rangecheckfailure(v_stack_m158, *(uint64_t *)(*(uint64_t *)(arg2 + 0x10) + 0x30), (uint32_t)(0xFFFFFFFFULL), *(uint64_t *)(*(uint64_t *)(arg2 + 0x10) + 0x50) + 2);
loc_00B864BD:
    result = KdPollBreakIn(v_stack_m158, *(uint64_t *)(*(uint64_t *)(arg2 + 0x10) + 0x30), (uint32_t)(0xFFFFFFFFULL), *(uint64_t *)(*(uint64_t *)(arg2 + 0x10) + 0x50) + 2);
    *(uint8_t *)(v_rip + 0x3D3801) = (uint8_t)(result);
    goto loc_00B8629E;
loc_00B864CD:
    Arg1 = 0;
    result = DbgLoadImageSymbols(Arg1, *(uint64_t *)(v_rip + 0x27ABA4), local_rsi, *(uint64_t *)(*(uint64_t *)(arg2 + 0x10) + 0x50) + 2);
    goto loc_00B86541;
loc_00B864E0:
    result = KeQueryPerformanceCounter(v_rip + 4011993, *(uint64_t *)(v_rip + 0x27ABA4), local_rsi, *(uint64_t *)(*(uint64_t *)(arg2 + 0x10) + 0x50) + 2);
    if ((*(uint8_t *)(v_rip + 0x284529)) != 0) goto loc_00B8653A;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x440585))) == 0) goto loc_00B8653A;
loc_00B86502:
    result = ExAllocatePool2(64, (uint32_t)(0x1000ULL), (uint32_t)(0x6F49644BULL), *(uint64_t *)(*(uint64_t *)(arg2 + 0x10) + 0x50) + 2);
    if (result != 0) {
        Arg1 = 0;
        Arg2 = v_rip + 3995542;
        *(uint64_t *)(arg2 + Arg1 * 8) = result;
    }
    local_rdi = (uint32_t)((0) + 1);
    if (((uint32_t)(local_rdi)) < ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x44054C))))) goto loc_00B86502;
loc_00B8653A:
    *(uint64_t *)(v_rip + 0x3CF767) = 0;
loc_00B86541:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, (uint32_t)(0x6F49644BULL), *(uint64_t *)(*(uint64_t *)(arg2 + 0x10) + 0x50) + 2);
    local_rsp = (local_rsp) + (320);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0xF0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagekd&rva=0x00B85E30&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
