# EtwpTraceMessageVa

- RVA: `0x002FB2B0`–`0x002FBF05` (길이 `3,157` bytes)
- VA: `0x00000001402FB2B0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00072AA8`
- 디코드: `656`개 명령, `3,157/3,157` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **16**; 고유 호출 대상: **12**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **10**

### Outgoing calls
- `0x002FB3D3` → [KeAreInterruptsEnabled](KeAreInterruptsEnabled_function_002F8060.md) (function, `0x002F8060`)
- `0x002FB6D2` → [EtwpReserveTraceBuffer](EtwpReserveTraceBuffer_function_002FC8C0.md) (function, `0x002FC8C0`)
- `0x002FB900` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x002FBA1D` → [KeIsTraceCallbackAllowed](KeIsTraceCallbackAllowed_function_002FCE6C.md) (function, `0x002FCE6C`)
- `0x002FBA48` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x002FBAA4` → [ExReleaseRundownProtectionCacheAwareEx](../25/ExReleaseRundownProtectionCacheAwareEx_function_0025F050.md) (function, `0x0025F050`)
- `0x002FBAB2` → [KeLeaveCriticalRegionThread](../25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x002FBAC6` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x002FBB9B` → [EtwpLevelKeywordEnabled](EtwpLevelKeywordEnabled_function_002FD110.md) (function, `0x002FD110`)
- `0x002FBC82` → [EtwWriteEx](../25/EtwWriteEx_function_0025F0D0.md) (function, `0x0025F0D0`)
- `0x002FBCA8` → [ExReleaseRundownProtectionCacheAwareEx](../25/ExReleaseRundownProtectionCacheAwareEx_function_0025F050.md) (function, `0x0025F050`)
- `0x002FBCB6` → [KeLeaveCriticalRegionThread](../25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x002FBDD0` → [EtwWriteEx](../25/EtwWriteEx_function_0025F0D0.md) (function, `0x0025F0D0`)
- `0x002FBEB6` → [EtwpSendTraceEvent](../4B/EtwpSendTraceEvent_function_004B6E10.md) (function, `0x004B6E10`)
- `0x002FBED8` → [PsIsServerSilo](../22/PsIsServerSilo_function_00225828.md) (function, `0x00225828`)
- `0x002FBEEC` → [PsIsServerSilo](../22/PsIsServerSilo_function_00225828.md) (function, `0x00225828`)

### Direct callers
- [NtTraceEvent](NtTraceEvent_function_002FA6C0.md) at `0x002FABDE`
- [WmiTraceMessage](../46/WmiTraceMessage_function_00461D40.md) at `0x00461D59`
- [WmiTraceMessageVa](../4C/WmiTraceMessageVa_function_004C26B0.md) at `0x004C26C3`

### Static image references
- `0x002FB2CA` → RVA `0x00E0A740` (`.data`; read)
- `0x002FB39F` → RVA `0x00FCF940` (`CACHEALI`; read)
- `0x002FBA26` → RVA `0x00FC7408` (`ALMOSTRO`; read)
- `0x002FBAF2` → RVA `0x00EFF840` (`.data`; read)
- `0x002FBC31` → RVA `0x000105E0` (`.rdata`; read)
- `0x002FBC74` → RVA `0x00010FC0` (`.rdata`; read)
- `0x002FBC8C` → RVA `0x00FC6AA8` (`ALMOSTRO`; read)
- `0x002FBE95` → RVA `0x00E0AA1C` (`.data`; read)
- `0x002FBE9E` → RVA `0x00F55CB3` (`.data`; read)
- `0x002FBEFA` → RVA `0x00F475DC` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x002FBA0F` → [sub_006DF7AC](../6D/Unknown_function_006DF7AC.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002FB2B0  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
002FB2B5  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
002FB2BA  57                              push rdi
002FB2BB  41 54                           push r12
002FB2BD  41 55                           push r13
002FB2BF  41 56                           push r14
002FB2C1  41 57                           push r15
002FB2C3  48 81 EC F0 01 00 00            sub rsp, 0x1f0
002FB2CA  48 8B 05 6F F4 B0 00            mov rax, qword ptr [rip + 0xb0f46f]
002FB2D1  48 33 C4                        xor rax, rsp
002FB2D4  48 89 84 24 E0 01 00 00         mov qword ptr [rsp + 0x1e0], rax
002FB2DC  66 44 89 4C 24 48               mov word ptr [rsp + 0x48], r9w
002FB2E2  4C 89 84 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], r8
002FB2EA  89 54 24 68                     mov dword ptr [rsp + 0x68], edx
002FB2EE  4C 8B D1                        mov r10, rcx
002FB2F1  48 89 8C 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rcx
002FB2F9  4C 8B BC 24 40 02 00 00         mov r15, qword ptr [rsp + 0x240]
002FB301  44 0F B6 B4 24 48 02 00 00      movzx r14d, byte ptr [rsp + 0x248]
002FB30A  44 88 74 24 50                  mov byte ptr [rsp + 0x50], r14b
002FB30F  44 88 74 24 58                  mov byte ptr [rsp + 0x58], r14b
002FB314  0F 57 C0                        xorps xmm0, xmm0
002FB317  33 C0                           xor eax, eax
002FB319  0F 11 84 24 E8 00 00 00         movups xmmword ptr [rsp + 0xe8], xmm0
002FB321  48 89 84 24 F8 00 00 00         mov qword ptr [rsp + 0xf8], rax
002FB329  0F 11 84 24 30 01 00 00         movups xmmword ptr [rsp + 0x130], xmm0
002FB331  45 33 E4                        xor r12d, r12d
002FB334  44 89 64 24 44                  mov dword ptr [rsp + 0x44], r12d
002FB339  4C 89 A4 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], r12
002FB341  88 44 24 40                     mov byte ptr [rsp + 0x40], al
002FB345  4C 89 A4 24 90 00 00 00         mov qword ptr [rsp + 0x90], r12
002FB34D  88 44 24 41                     mov byte ptr [rsp + 0x41], al
002FB351  45 84 F6                        test r14b, r14b
002FB354  0F 84 32 09 00 00               je 0x1402fbc8c
002FB35A  65 8A 04 25 A0 01 00 00         mov al, byte ptr gs:[0x1a0]
002FB362  84 C0                           test al, al
002FB364  75 39                           jne 0x1402fb39f
002FB366  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
002FB36F  48 8B 88 98 06 00 00            mov rcx, qword ptr [rax + 0x698]
002FB376  48 83 F9 FD                     cmp rcx, -3
002FB37A  0F 85 4B 0B 00 00               jne 0x1402fbecb
002FB380  48 8B 80 20 02 00 00            mov rax, qword ptr [rax + 0x220]
002FB387  48 8B 88 F0 05 00 00            mov rcx, qword ptr [rax + 0x5f0]
002FB38E  48 89 8C 24 20 01 00 00         mov qword ptr [rsp + 0x120], rcx
002FB396  48 85 C9                        test rcx, rcx
002FB399  0F 85 52 0A 00 00               jne 0x1402fbdf1
002FB39F  48 8D 05 9A 45 CD 00            lea rax, [rip + 0xcd459a]
002FB3A6  48 8B B0 40 03 00 00            mov rsi, qword ptr [rax + 0x340]
002FB3AD  48 89 B4 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], rsi
002FB3B5  48 89 74 24 60                  mov qword ptr [rsp + 0x60], rsi
002FB3BA  41 0F B7 FA                     movzx edi, r10w
002FB3BE  3B 7E 10                        cmp edi, dword ptr [rsi + 0x10]
002FB3C1  0F 83 F4 08 00 00               jae 0x1402fbcbb
002FB3C7  32 DB                           xor bl, bl
002FB3C9  88 5C 24 42                     mov byte ptr [rsp + 0x42], bl
002FB3CD  41 80 FE 01                     cmp r14b, 1
002FB3D1  74 11                           je 0x1402fb3e4
002FB3D3  E8 88 CC FF FF                  call 0x1402f8060
002FB3D8  84 C0                           test al, al
002FB3DA  74 60                           je 0x1402fb43c
002FB3DC  44 0F 20 C0                     mov rax, cr8
002FB3E0  3C 02                           cmp al, 2
002FB3E2  73 58                           jae 0x1402fb43c
002FB3E4  0F AE E8                        lfence
002FB3E7  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
002FB3F0  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
002FB3F7  90                              nop
002FB3F8  48 8B 86 C0 02 00 00            mov rax, qword ptr [rsi + 0x2c0]
002FB3FF  4C 8B 04 F8                     mov r8, qword ptr [rax + rdi*8]
002FB403  65 8B 04 25 A4 01 00 00         mov eax, dword ptr gs:[0x1a4]
002FB40B  33 D2                           xor edx, edx
002FB40D  41 F7 70 14                     div dword ptr [r8 + 0x14]
002FB411  41 0F AF 50 10                  imul edx, dword ptr [r8 + 0x10]
002FB416  44 8B CA                        mov r9d, edx
002FB419  4D 03 08                        add r9, qword ptr [r8]
002FB41C  41 0F 0D 09                     prefetchw byte ptr [r9]
002FB420  49 8B 01                        mov rax, qword ptr [r9]
002FB423  A8 01                           test al, 1
002FB425  0F 85 82 08 00 00               jne 0x1402fbcad
002FB42B  48 8D 48 02                     lea rcx, [rax + 2]
002FB42F  F0 49 0F B1 09                  lock cmpxchg qword ptr [r9], rcx
002FB434  75 ED                           jne 0x1402fb423
002FB436  B3 01                           mov bl, 1
002FB438  88 5C 24 42                     mov byte ptr [rsp + 0x42], bl
002FB43C  0F AE E8                        lfence
002FB43F  4C 8D 04 FD 00 00 00 00         lea r8, [rdi*8]
002FB447  4C 89 44 24 78                  mov qword ptr [rsp + 0x78], r8
002FB44C  48 8B 86 C8 02 00 00            mov rax, qword ptr [rsi + 0x2c8]
002FB453  49 8B 3C 00                     mov rdi, qword ptr [r8 + rax]
002FB457  48 89 BC 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rdi
002FB45F  8B C7                           mov eax, edi
002FB461  F7 D0                           not eax
002FB463  A8 01                           test al, 1
002FB465  0F 84 5D 08 00 00               je 0x1402fbcc8
002FB46B  48 89 BC 24 10 01 00 00         mov qword ptr [rsp + 0x110], rdi
002FB473  48 85 FF                        test rdi, rdi
002FB476  0F 84 3F 08 00 00               je 0x1402fbcbb
002FB47C  48 8D 47 0C                     lea rax, [rdi + 0xc]
002FB480  48 89 84 24 18 01 00 00         mov qword ptr [rsp + 0x118], rax
002FB488  8B 00                           mov eax, dword ptr [rax]
002FB48A  84 C0                           test al, al
002FB48C  0F 88 ED 09 00 00               js 0x1402fbe7f
002FB492  45 84 F6                        test r14b, r14b
002FB495  0F 84 3F 09 00 00               je 0x1402fbdda
002FB49B  4C 89 A4 24 80 00 00 00         mov qword ptr [rsp + 0x80], r12
002FB4A3  8B 54 24 68                     mov edx, dword ptr [rsp + 0x68]
002FB4A7  0F B6 F2                        movzx esi, dl
002FB4AA  40 80 E6 40                     and sil, 0x40
002FB4AE  40 88 74 24 40                  mov byte ptr [rsp + 0x40], sil
002FB4B3  44 0F B6 F2                     movzx r14d, dl
002FB4B7  41 80 E6 80                     and r14b, 0x80
002FB4BB  44 88 74 24 41                  mov byte ptr [rsp + 0x41], r14b
002FB4C0  40 84 F6                        test sil, sil
002FB4C3  0F 84 2C 01 00 00               je 0x1402fb5f5
002FB4C9  8B 84 24 A4 00 00 00            mov eax, dword ptr [rsp + 0xa4]
002FB4D0  85 C0                           test eax, eax
002FB4D2  0F 84 F7 00 00 00               je 0x1402fb5cf
002FB4D8  4D 8D 2C 07                     lea r13, [r15 + rax]
002FB4DC  4C 89 AC 24 90 00 00 00         mov qword ptr [rsp + 0x90], r13
002FB4E4  4C 89 AC 24 98 00 00 00         mov qword ptr [rsp + 0x98], r13
002FB4EC  4C 89 A4 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], r12
002FB4F4  49 8B C7                        mov rax, r15
002FB4F7  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
002FB4FF  40 84 F6                        test sil, sil
002FB502  74 6F                           je 0x1402fb573
002FB504  45 84 F6                        test r14b, r14b
002FB507  75 7C                           jne 0x1402fb585
002FB509  48 8D 48 08                     lea rcx, [rax + 8]
002FB50D  48 8B C1                        mov rax, rcx
002FB510  49 3B CD                        cmp rcx, r13
002FB513  0F 87 A3 00 00 00               ja 0x1402fb5bc
002FB519  48 89 8C 24 80 00 00 00         mov qword ptr [rsp + 0x80], rcx
002FB521  48 8B 49 F8                     mov rcx, qword ptr [rcx - 8]
002FB525  48 85 C9                        test rcx, rcx
002FB528  74 31                           je 0x1402fb55b
002FB52A  40 84 F6                        test sil, sil
002FB52D  74 05                           je 0x1402fb534
002FB52F  45 84 F6                        test r14b, r14b
002FB532  75 7F                           jne 0x1402fb5b3
002FB534  48 83 C0 08                     add rax, 8
002FB538  48 8B 48 F8                     mov rcx, qword ptr [rax - 8]
002FB53C  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
002FB544  48 85 C9                        test rcx, rcx
002FB547  74 10                           je 0x1402fb559
002FB549  4C 03 E1                        add r12, rcx
002FB54C  4C 89 A4 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], r12
002FB554  4C 3B E1                        cmp r12, rcx
002FB557  72 45                           jb 0x1402fb59e
002FB559  EB A4                           jmp 0x1402fb4ff
002FB55B  48 8B 84 24 A8 00 00 00         mov rax, qword ptr [rsp + 0xa8]
002FB563  0F 10 00                        movups xmm0, xmmword ptr [rax]
002FB566  0F 11 84 24 30 01 00 00         movups xmmword ptr [rsp + 0x130], xmm0
002FB56E  E9 AA 00 00 00                  jmp 0x1402fb61d
002FB573  48 83 C0 08                     add rax, 8
002FB577  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
002FB57F  48 8B 48 F8                     mov rcx, qword ptr [rax - 8]
002FB583  EB A0                           jmp 0x1402fb525
002FB585  48 8D 48 04                     lea rcx, [rax + 4]
002FB589  48 8B C1                        mov rax, rcx
002FB58C  49 3B CD                        cmp rcx, r13
002FB58F  77 51                           ja 0x1402fb5e2
002FB591  48 89 8C 24 80 00 00 00         mov qword ptr [rsp + 0x80], rcx
002FB599  8B 49 FC                        mov ecx, dword ptr [rcx - 4]
002FB59C  EB 87                           jmp 0x1402fb525
002FB59E  41 BA 95 00 00 C0               mov r10d, 0xc0000095
002FB5A4  44 89 54 24 44                  mov dword ptr [rsp + 0x44], r10d
002FB5A9  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
002FB5AE  E9 DD 04 00 00                  jmp 0x1402fba90
002FB5B3  48 83 C0 04                     add rax, 4
002FB5B7  8B 48 FC                        mov ecx, dword ptr [rax - 4]
002FB5BA  EB 80                           jmp 0x1402fb53c
002FB5BC  BA 06 02 00 C0                  mov edx, 0xc0000206
002FB5C1  89 54 24 44                     mov dword ptr [rsp + 0x44], edx
002FB5C5  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
002FB5CA  E9 C1 04 00 00                  jmp 0x1402fba90
002FB5CF  BA 06 02 00 C0                  mov edx, 0xc0000206
002FB5D4  89 54 24 44                     mov dword ptr [rsp + 0x44], edx
002FB5D8  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
002FB5DD  E9 AE 04 00 00                  jmp 0x1402fba90
002FB5E2  BA 06 02 00 C0                  mov edx, 0xc0000206
002FB5E7  89 54 24 44                     mov dword ptr [rsp + 0x44], edx
002FB5EB  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
002FB5F0  E9 9B 04 00 00                  jmp 0x1402fba90
002FB5F5  4C 8B AC 24 90 00 00 00         mov r13, qword ptr [rsp + 0x90]
002FB5FD  E9 E2 FE FF FF                  jmp 0x1402fb4e4
002FB602  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
002FB606  0F B6 5C 24 42                  movzx ebx, byte ptr [rsp + 0x42]
002FB60B  48 8B B4 24 D8 00 00 00         mov rsi, qword ptr [rsp + 0xd8]
002FB613  4C 8B 44 24 78                  mov r8, qword ptr [rsp + 0x78]
002FB618  E9 73 04 00 00                  jmp 0x1402fba90
002FB61D  8B CA                           mov ecx, edx
002FB61F  83 E1 FE                        and ecx, 0xfffffffe
002FB622  48 83 BF 08 01 00 00 00         cmp qword ptr [rdi + 0x108], 0
002FB62A  0F 45 CA                        cmovne ecx, edx
002FB62D  89 8C 24 C0 00 00 00            mov dword ptr [rsp + 0xc0], ecx
002FB634  44 8B C1                        mov r8d, ecx
002FB637  41 83 E0 01                     and r8d, 1
002FB63B  44 89 84 24 C4 00 00 00         mov dword ptr [rsp + 0xc4], r8d
002FB643  44 8B D1                        mov r10d, ecx
002FB646  41 83 E2 02                     and r10d, 2
002FB64A  44 89 94 24 CC 00 00 00         mov dword ptr [rsp + 0xcc], r10d
002FB652  44 8B C9                        mov r9d, ecx
002FB655  41 83 E1 04                     and r9d, 4
002FB659  44 89 8C 24 C8 00 00 00         mov dword ptr [rsp + 0xc8], r9d
002FB661  44 8B D9                        mov r11d, ecx
002FB664  41 83 E3 20                     and r11d, 0x20
002FB668  44 89 5C 24 6C                  mov dword ptr [rsp + 0x6c], r11d
002FB66D  8B C1                           mov eax, ecx
002FB66F  24 18                           and al, 0x18
002FB671  F6 D8                           neg al
002FB673  1B D2                           sbb edx, edx
002FB675  83 E2 08                        and edx, 8
002FB678  41 8B C3                        mov eax, r11d
002FB67B  F7 D8                           neg eax
002FB67D  1B C9                           sbb ecx, ecx
002FB67F  83 E1 08                        and ecx, 8
002FB682  03 D1                           add edx, ecx
002FB684  41 8B C1                        mov eax, r9d
002FB687  F7 D8                           neg eax
002FB689  1B C9                           sbb ecx, ecx
002FB68B  83 E1 04                        and ecx, 4
002FB68E  03 D1                           add edx, ecx
002FB690  41 8B C2                        mov eax, r10d
002FB693  F7 D8                           neg eax
002FB695  1B C9                           sbb ecx, ecx
002FB697  83 E1 10                        and ecx, 0x10
002FB69A  41 03 CC                        add ecx, r12d
002FB69D  03 CA                           add ecx, edx
002FB69F  42 8D 0C 81                     lea ecx, [rcx + r8*4]
002FB6A3  83 C1 08                        add ecx, 8
002FB6A6  89 4C 24 68                     mov dword ptr [rsp + 0x68], ecx
002FB6AA  8B C1                           mov eax, ecx
002FB6AC  4C 3B E0                        cmp r12, rax
002FB6AF  0F 87 34 04 00 00               ja 0x1402fbae9
002FB6B5  45 33 C9                        xor r9d, r9d
002FB6B8  44 89 4C 24 20                  mov dword ptr [rsp + 0x20], r9d
002FB6BD  4C 8D 8C 24 D0 00 00 00         lea r9, [rsp + 0xd0]
002FB6C5  4C 8D 84 24 E8 00 00 00         lea r8, [rsp + 0xe8]
002FB6CD  8B D1                           mov edx, ecx
002FB6CF  48 8B CF                        mov rcx, rdi
002FB6D2  E8 E9 11 00 00                  call 0x1402fc8c0
002FB6D7  48 8B F8                        mov rdi, rax
002FB6DA  45 33 DB                        xor r11d, r11d
002FB6DD  41 8B CB                        mov ecx, r11d
002FB6E0  4C 8B 8C 24 E0 00 00 00         mov r9, qword ptr [rsp + 0xe0]
002FB6E8  49 8B 81 08 01 00 00            mov rax, qword ptr [r9 + 0x108]
002FB6EF  48 85 C0                        test rax, rax
002FB6F2  74 2E                           je 0x1402fb722
002FB6F4  B9 01 00 00 00                  mov ecx, 1
002FB6F9  F0 0F C1 08                     lock xadd dword ptr [rax], ecx
002FB6FD  FF C1                           inc ecx
002FB6FF  4C 8B A4 24 A0 00 00 00         mov r12, qword ptr [rsp + 0xa0]
002FB707  0F B6 74 24 40                  movzx esi, byte ptr [rsp + 0x40]
002FB70C  4C 8B AC 24 90 00 00 00         mov r13, qword ptr [rsp + 0x90]
002FB714  4C 89 AC 24 98 00 00 00         mov qword ptr [rsp + 0x98], r13
002FB71C  44 0F B6 74 24 41               movzx r14d, byte ptr [rsp + 0x41]
002FB722  8B 44 24 68                     mov eax, dword ptr [rsp + 0x68]
002FB726  48 85 FF                        test rdi, rdi
002FB729  0F 84 10 04 00 00               je 0x1402fbb3f
002FB72F  C7 07 00 00 00 90               mov dword ptr [rdi], 0x90000000
002FB735  66 89 07                        mov word ptr [rdi], ax
002FB738  0F B7 44 24 48                  movzx eax, word ptr [rsp + 0x48]
002FB73D  66 89 47 04                     mov word ptr [rdi + 4], ax
002FB741  45 84 F6                        test r14b, r14b
002FB744  0F 85 E2 06 00 00               jne 0x1402fbe2c
002FB74A  41 B8 80 00 00 00               mov r8d, 0x80
002FB750  44 8B 8C 24 C0 00 00 00         mov r9d, dword ptr [rsp + 0xc0]
002FB758  41 0F B7 C1                     movzx eax, r9w
002FB75C  66 83 E0 3F                     and ax, 0x3f
002FB760  66 41 0B C0                     or ax, r8w
002FB764  66 89 47 06                     mov word ptr [rdi + 6], ax
002FB768  48 83 C7 08                     add rdi, 8
002FB76C  48 89 7C 24 70                  mov qword ptr [rsp + 0x70], rdi
002FB771  4C 8B C7                        mov r8, rdi
002FB774  48 8B D7                        mov rdx, rdi
002FB777  83 BC 24 C4 00 00 00 00         cmp dword ptr [rsp + 0xc4], 0
002FB77F  74 11                           je 0x1402fb792
002FB781  89 0F                           mov dword ptr [rdi], ecx
002FB783  48 83 C7 04                     add rdi, 4
002FB787  48 8B D7                        mov rdx, rdi
002FB78A  48 89 7C 24 70                  mov qword ptr [rsp + 0x70], rdi
002FB78F  4C 8B C7                        mov r8, rdi
002FB792  83 BC 24 C8 00 00 00 00         cmp dword ptr [rsp + 0xc8], 0
002FB79A  0F 85 95 01 00 00               jne 0x1402fb935
002FB7A0  83 BC 24 CC 00 00 00 00         cmp dword ptr [rsp + 0xcc], 0
002FB7A8  74 1D                           je 0x1402fb7c7
002FB7AA  48 8B 84 24 A8 00 00 00         mov rax, qword ptr [rsp + 0xa8]
002FB7B2  0F 10 00                        movups xmm0, xmmword ptr [rax]
002FB7B5  0F 11 07                        movups xmmword ptr [rdi], xmm0
002FB7B8  49 8D 78 10                     lea rdi, [r8 + 0x10]
002FB7BC  4C 8B C7                        mov r8, rdi
002FB7BF  48 89 7C 24 70                  mov qword ptr [rsp + 0x70], rdi
002FB7C4  48 8B D7                        mov rdx, rdi
002FB7C7  41 F6 C1 08                     test r9b, 8
002FB7CB  74 1F                           je 0x1402fb7ec
002FB7CD  8B 84 24 D4 00 00 00            mov eax, dword ptr [rsp + 0xd4]
002FB7D4  89 42 04                        mov dword ptr [rdx + 4], eax
002FB7D7  8B 84 24 D0 00 00 00            mov eax, dword ptr [rsp + 0xd0]
002FB7DE  89 07                           mov dword ptr [rdi], eax
002FB7E0  49 8D 78 08                     lea rdi, [r8 + 8]
002FB7E4  48 89 7C 24 70                  mov qword ptr [rsp + 0x70], rdi
002FB7E9  4C 8B C7                        mov r8, rdi
002FB7EC  83 7C 24 6C 00                  cmp dword ptr [rsp + 0x6c], 0
002FB7F1  74 69                           je 0x1402fb85c
002FB7F3  65 48 8B 14 25 88 01 00 00      mov rdx, qword ptr gs:[0x188]
002FB7FC  48 89 94 24 28 01 00 00         mov qword ptr [rsp + 0x128], rdx
002FB804  8B 8A 10 05 00 00               mov ecx, dword ptr [rdx + 0x510]
002FB80A  89 8C 24 00 01 00 00            mov dword ptr [rsp + 0x100], ecx
002FB811  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
002FB816  89 08                           mov dword ptr [rax], ecx
002FB818  49 8D 48 04                     lea rcx, [r8 + 4]
002FB81C  48 89 4C 24 70                  mov qword ptr [rsp + 0x70], rcx
002FB821  8B 82 08 05 00 00               mov eax, dword ptr [rdx + 0x508]
002FB827  89 84 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], eax
002FB82E  89 01                           mov dword ptr [rcx], eax
002FB830  48 8D 79 04                     lea rdi, [rcx + 4]
002FB834  48 89 7C 24 70                  mov qword ptr [rsp + 0x70], rdi
002FB839  4C 8B A4 24 A0 00 00 00         mov r12, qword ptr [rsp + 0xa0]
002FB841  0F B6 74 24 40                  movzx esi, byte ptr [rsp + 0x40]
002FB846  4C 8B AC 24 90 00 00 00         mov r13, qword ptr [rsp + 0x90]
002FB84E  4C 89 AC 24 98 00 00 00         mov qword ptr [rsp + 0x98], r13
002FB856  44 0F B6 74 24 41               movzx r14d, byte ptr [rsp + 0x41]
002FB85C  4C 89 9C 24 88 00 00 00         mov qword ptr [rsp + 0x88], r11
002FB864  4C 89 A4 24 08 01 00 00         mov qword ptr [rsp + 0x108], r12
002FB86C  4C 89 BC 24 88 00 00 00         mov qword ptr [rsp + 0x88], r15
002FB874  48 B9 00 00 FF FF FF 7F 00 00   movabs rcx, 0x7fffffff0000
002FB87E  40 84 F6                        test sil, sil
002FB881  74 09                           je 0x1402fb88c
002FB883  45 84 F6                        test r14b, r14b
002FB886  0F 85 BE 00 00 00               jne 0x1402fb94a
002FB88C  49 83 C7 08                     add r15, 8
002FB890  49 8B 57 F8                     mov rdx, qword ptr [r15 - 8]
002FB894  4C 89 BC 24 88 00 00 00         mov qword ptr [rsp + 0x88], r15
002FB89C  48 85 D2                        test rdx, rdx
002FB89F  0F 84 8A 00 00 00               je 0x1402fb92f
002FB8A5  40 84 F6                        test sil, sil
002FB8A8  74 17                           je 0x1402fb8c1
002FB8AA  4D 3B FD                        cmp r15, r13
002FB8AD  0F 83 BC 00 00 00               jae 0x1402fb96f
002FB8B3  40 84 F6                        test sil, sil
002FB8B6  74 09                           je 0x1402fb8c1
002FB8B8  45 84 F6                        test r14b, r14b
002FB8BB  0F 85 96 00 00 00               jne 0x1402fb957
002FB8C1  49 83 C7 08                     add r15, 8
002FB8C5  4D 8B 6F F8                     mov r13, qword ptr [r15 - 8]
002FB8C9  4C 89 BC 24 88 00 00 00         mov qword ptr [rsp + 0x88], r15
002FB8D1  4D 85 ED                        test r13, r13
002FB8D4  74 4C                           je 0x1402fb922
002FB8D6  4D 3B EC                        cmp r13, r12
002FB8D9  0F 87 85 00 00 00               ja 0x1402fb964
002FB8DF  40 84 F6                        test sil, sil
002FB8E2  74 16                           je 0x1402fb8fa
002FB8E4  4A 8D 04 2A                     lea rax, [rdx + r13]
002FB8E8  48 3B C1                        cmp rax, rcx
002FB8EB  0F 87 89 00 00 00               ja 0x1402fb97a
002FB8F1  48 3B C2                        cmp rax, rdx
002FB8F4  0F 82 80 00 00 00               jb 0x1402fb97a
002FB8FA  4D 8B C5                        mov r8, r13
002FB8FD  48 8B CF                        mov rcx, rdi
002FB900  E8 3B AF 3C 00                  call 0x1406c6840
002FB905  4D 2B E5                        sub r12, r13
002FB908  4C 89 A4 24 08 01 00 00         mov qword ptr [rsp + 0x108], r12
002FB910  49 03 FD                        add rdi, r13
002FB913  48 89 7C 24 70                  mov qword ptr [rsp + 0x70], rdi
002FB918  48 B9 00 00 FF FF FF 7F 00 00   movabs rcx, 0x7fffffff0000
002FB922  4C 8B AC 24 98 00 00 00         mov r13, qword ptr [rsp + 0x98]
002FB92A  E9 4F FF FF FF                  jmp 0x1402fb87e
002FB92F  8B 54 24 44                     mov edx, dword ptr [rsp + 0x44]
002FB933  EB 6D                           jmp 0x1402fb9a2
002FB935  48 8B 84 24 A8 00 00 00         mov rax, qword ptr [rsp + 0xa8]
002FB93D  8B 00                           mov eax, dword ptr [rax]
002FB93F  89 07                           mov dword ptr [rdi], eax
002FB941  49 8D 78 04                     lea rdi, [r8 + 4]
002FB945  E9 72 FE FF FF                  jmp 0x1402fb7bc
002FB94A  49 83 C7 04                     add r15, 4
002FB94E  41 8B 57 FC                     mov edx, dword ptr [r15 - 4]
002FB952  E9 3D FF FF FF                  jmp 0x1402fb894
002FB957  49 83 C7 04                     add r15, 4
002FB95B  45 8B 6F FC                     mov r13d, dword ptr [r15 - 4]
002FB95F  E9 65 FF FF FF                  jmp 0x1402fb8c9
002FB964  BA 06 02 00 C0                  mov edx, 0xc0000206
002FB969  89 54 24 44                     mov dword ptr [rsp + 0x44], edx
002FB96D  EB 33                           jmp 0x1402fb9a2
002FB96F  BA 06 02 00 C0                  mov edx, 0xc0000206
002FB974  89 54 24 44                     mov dword ptr [rsp + 0x44], edx
002FB978  EB 28                           jmp 0x1402fb9a2
002FB97A  0F B6 01                        movzx eax, byte ptr [rcx]
002FB97D  48 8B 7C 24 70                  mov rdi, qword ptr [rsp + 0x70]
002FB982  0F B6 74 24 40                  movzx esi, byte ptr [rsp + 0x40]
002FB987  48 8B 84 24 90 00 00 00         mov rax, qword ptr [rsp + 0x90]
002FB98F  48 89 84 24 98 00 00 00         mov qword ptr [rsp + 0x98], rax
002FB997  44 0F B6 74 24 41               movzx r14d, byte ptr [rsp + 0x41]
002FB99D  E9 58 FF FF FF                  jmp 0x1402fb8fa
002FB9A2  48 8B BC 24 E0 00 00 00         mov rdi, qword ptr [rsp + 0xe0]
002FB9AA  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
002FB9AF  44 0F B6 64 24 50               movzx r12d, byte ptr [rsp + 0x50]
002FB9B5  EB 26                           jmp 0x1402fb9dd
002FB9B7  8B D0                           mov edx, eax
002FB9B9  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
002FB9BD  48 8B BC 24 10 01 00 00         mov rdi, qword ptr [rsp + 0x110]
002FB9C5  0F B6 5C 24 42                  movzx ebx, byte ptr [rsp + 0x42]
002FB9CA  48 8B B4 24 D8 00 00 00         mov rsi, qword ptr [rsp + 0xd8]
002FB9D2  48 89 74 24 60                  mov qword ptr [rsp + 0x60], rsi
002FB9D7  44 0F B6 64 24 58               movzx r12d, byte ptr [rsp + 0x58]
002FB9DD  85 D2                           test edx, edx
002FB9DF  78 6C                           js 0x1402fba4d
002FB9E1  48 8B 84 24 18 01 00 00         mov rax, qword ptr [rsp + 0x118]
002FB9E9  F7 00 00 00 08 00               test dword ptr [rax], 0x80000
002FB9EF  0F 85 A0 04 00 00               jne 0x1402fbe95
002FB9F5  4C 8B 8F 20 06 00 00            mov r9, qword ptr [rdi + 0x620]
002FB9FC  4D 85 C9                        test r9, r9
002FB9FF  74 4C                           je 0x1402fba4d
002FBA01  48 8B 8C 24 E8 00 00 00         mov rcx, qword ptr [rsp + 0xe8]
002FBA09  8B 11                           mov edx, dword ptr [rcx]
002FBA0B  85 D2                           test edx, edx
002FBA0D  74 3E                           je 0x1402fba4d
002FBA0F  E9 98 3D 3E 00                  jmp 0x1406df7ac
002FBA14  45 85 C0                        test r8d, r8d
002FBA17  74 34                           je 0x1402fba4d
002FBA19  41 0F B6 CC                     movzx ecx, r12b
002FBA1D  E8 4A 14 00 00                  call 0x1402fce6c
002FBA22  85 C0                           test eax, eax
002FBA24  74 27                           je 0x1402fba4d
002FBA26  48 8B 05 DB B9 CC 00            mov rax, qword ptr [rip + 0xccb9db]
002FBA2D  4D 8B 41 08                     mov r8, qword ptr [r9 + 8]
002FBA31  4C 89 44 24 20                  mov qword ptr [rsp + 0x20], r8
002FBA36  45 0F B6 CC                     movzx r9d, r12b
002FBA3A  4C 8D 84 24 30 01 00 00         lea r8, [rsp + 0x130]
002FBA42  41 8B D2                        mov edx, r10d
002FBA45  49 8B CB                        mov rcx, r11
002FBA48  E8 83 F0 3B 00                  call 0x1406baad0
002FBA4D  48 8B 84 24 F0 00 00 00         mov rax, qword ptr [rsp + 0xf0]
002FBA55  0F 0D 08                        prefetchw byte ptr [rax]
002FBA58  48 8B 00                        mov rax, qword ptr [rax]
002FBA5B  48 8B 94 24 E8 00 00 00         mov rdx, qword ptr [rsp + 0xe8]
002FBA63  48 8B CA                        mov rcx, rdx
002FBA66  48 33 C8                        xor rcx, rax
002FBA69  48 83 F9 0F                     cmp rcx, 0xf
002FBA6D  0F 83 19 04 00 00               jae 0x1402fbe8c
002FBA73  48 8D 48 01                     lea rcx, [rax + 1]
002FBA77  48 8B 94 24 F0 00 00 00         mov rdx, qword ptr [rsp + 0xf0]
002FBA7F  F0 48 0F B1 0A                  lock cmpxchg qword ptr [rdx], rcx
002FBA84  75 D5                           jne 0x1402fba5b
002FBA86  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
002FBA8B  4C 8B 44 24 78                  mov r8, qword ptr [rsp + 0x78]
002FBA90  84 DB                           test bl, bl
002FBA92  74 23                           je 0x1402fbab7
002FBA94  48 8B 8E C0 02 00 00            mov rcx, qword ptr [rsi + 0x2c0]
002FBA9B  BA 01 00 00 00                  mov edx, 1
002FBAA0  4A 8B 0C 01                     mov rcx, qword ptr [rcx + r8]
002FBAA4  E8 A7 35 F6 FF                  call 0x14025f050
002FBAA9  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
002FBAB2  E8 39 35 F6 FF                  call 0x14025eff0
002FBAB7  8B 44 24 44                     mov eax, dword ptr [rsp + 0x44]
002FBABB  48 8B 8C 24 E0 01 00 00         mov rcx, qword ptr [rsp + 0x1e0]
002FBAC3  48 33 CC                        xor rcx, rsp
002FBAC6  E8 75 0B 3B 00                  call 0x1406ac640
002FBACB  4C 8D 9C 24 F0 01 00 00         lea r11, [rsp + 0x1f0]
002FBAD3  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
002FBAD7  49 8B 73 48                     mov rsi, qword ptr [r11 + 0x48]
002FBADB  49 8B E3                        mov rsp, r11
002FBADE  41 5F                           pop r15
002FBAE0  41 5E                           pop r14
002FBAE2  41 5D                           pop r13
002FBAE4  41 5C                           pop r12
002FBAE6  5F                              pop rdi
002FBAE7  C3                              ret
002FBAE8  CC                              int3
002FBAE9  BA 06 02 00 C0                  mov edx, 0xc0000206
002FBAEE  89 54 24 44                     mov dword ptr [rsp + 0x44], edx
002FBAF2  4C 8B 05 47 3D C0 00            mov r8, qword ptr [rip + 0xc03d47]
002FBAF9  4D 85 C0                        test r8, r8
002FBAFC  74 1D                           je 0x1402fbb1b
002FBAFE  49 8B 48 20                     mov rcx, qword ptr [r8 + 0x20]
002FBB02  45 33 C9                        xor r9d, r9d
002FBB05  44 39 49 60                     cmp dword ptr [rcx + 0x60], r9d
002FBB09  0F 85 BF 01 00 00               jne 0x1402fbcce
002FBB0F  66 41 83 78 66 00               cmp word ptr [r8 + 0x66], 0
002FBB15  0F 85 1C 03 00 00               jne 0x1402fbe37
002FBB1B  F0 FF 87 F0 00 00 00            lock inc dword ptr [rdi + 0xf0]
002FBB22  8B 87 30 03 00 00               mov eax, dword ptr [rdi + 0x330]
002FBB28  A8 08                           test al, 8
002FBB2A  0F 84 56 FF FF FF               je 0x1402fba86
002FBB30  C7 87 C0 01 00 00 01 00 00 00   mov dword ptr [rdi + 0x1c0], 1
002FBB3A  E9 47 FF FF FF                  jmp 0x1402fba86
002FBB3F  3D F8 FF 00 00                  cmp eax, 0xfff8
002FBB44  0F 87 76 03 00 00               ja 0x1402fbec0
002FBB4A  B9 05 00 00 80                  mov ecx, 0x80000005
002FBB4F  41 BA 17 00 00 C0               mov r10d, 0xc0000017
002FBB55  41 3B 41 08                     cmp eax, dword ptr [r9 + 8]
002FBB59  44 0F 47 D1                     cmova r10d, ecx
002FBB5D  44 89 54 24 44                  mov dword ptr [rsp + 0x44], r10d
002FBB62  48 8B 15 D7 3C C0 00            mov rdx, qword ptr [rip + 0xc03cd7]
002FBB69  48 85 D2                        test rdx, rdx
002FBB6C  0F 84 14 FF FF FF               je 0x1402fba86
002FBB72  48 8B 4A 20                     mov rcx, qword ptr [rdx + 0x20]
002FBB76  44 39 59 60                     cmp dword ptr [rcx + 0x60], r11d
002FBB7A  0F 85 7D 02 00 00               jne 0x1402fbdfd
002FBB80  66 44 39 5A 66                  cmp word ptr [rdx + 0x66], r11w
002FBB85  0F 84 FB FE FF FF               je 0x1402fba86
002FBB8B  48 8B 4A 28                     mov rcx, qword ptr [rdx + 0x28]
002FBB8F  48 83 C1 60                     add rcx, 0x60
002FBB93  41 B8 40 00 00 00               mov r8d, 0x40
002FBB99  B2 02                           mov dl, 2
002FBB9B  E8 70 15 00 00                  call 0x1402fd110
002FBBA0  84 C0                           test al, al
002FBBA2  0F 84 DE FE FF FF               je 0x1402fba86
002FBBA8  44 89 94 24 B8 00 00 00         mov dword ptr [rsp + 0xb8], r10d
002FBBB0  0F B7 44 24 48                  movzx eax, word ptr [rsp + 0x48]
002FBBB5  66 89 44 24 58                  mov word ptr [rsp + 0x58], ax
002FBBBA  48 8D 84 24 30 01 00 00         lea rax, [rsp + 0x130]
002FBBC2  48 89 84 24 90 01 00 00         mov qword ptr [rsp + 0x190], rax
002FBBCA  48 C7 84 24 98 01 00 00 10 00 00 00  mov qword ptr [rsp + 0x198], 0x10
002FBBD6  48 8D 44 24 58                  lea rax, [rsp + 0x58]
002FBBDB  48 89 84 24 A0 01 00 00         mov qword ptr [rsp + 0x1a0], rax
002FBBE3  48 C7 84 24 A8 01 00 00 02 00 00 00  mov qword ptr [rsp + 0x1a8], 2
002FBBEF  48 8D 84 24 B8 00 00 00         lea rax, [rsp + 0xb8]
002FBBF7  48 89 84 24 B0 01 00 00         mov qword ptr [rsp + 0x1b0], rax
002FBBFF  48 C7 84 24 B8 01 00 00 04 00 00 00  mov qword ptr [rsp + 0x1b8], 4
002FBC0B  49 8B 81 90 00 00 00            mov rax, qword ptr [r9 + 0x90]
002FBC12  48 89 84 24 C0 01 00 00         mov qword ptr [rsp + 0x1c0], rax
002FBC1A  41 0F B7 81 88 00 00 00         movzx eax, word ptr [r9 + 0x88]
002FBC22  89 84 24 C8 01 00 00            mov dword ptr [rsp + 0x1c8], eax
002FBC29  44 89 9C 24 CC 01 00 00         mov dword ptr [rsp + 0x1cc], r11d
002FBC31  48 8D 05 A8 49 D1 FF            lea rax, [rip - 0x2eb658]
002FBC38  48 89 84 24 D0 01 00 00         mov qword ptr [rsp + 0x1d0], rax
002FBC40  48 C7 84 24 D8 01 00 00 02 00 00 00  mov qword ptr [rsp + 0x1d8], 2
002FBC4C  48 8D 84 24 90 01 00 00         lea rax, [rsp + 0x190]
002FBC54  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
002FBC59  C7 44 24 30 05 00 00 00         mov dword ptr [rsp + 0x30], 5
002FBC61  4C 89 5C 24 28                  mov qword ptr [rsp + 0x28], r11
002FBC66  4C 89 5C 24 20                  mov qword ptr [rsp + 0x20], r11
002FBC6B  41 B9 01 00 00 00               mov r9d, 1
002FBC71  45 33 C0                        xor r8d, r8d
002FBC74  48 8D 15 45 53 D1 FF            lea rdx, [rip - 0x2eacbb]
002FBC7B  48 8B 0D BE 3B C0 00            mov rcx, qword ptr [rip + 0xc03bbe]
002FBC82  E8 49 34 F6 FF                  call 0x14025f0d0
002FBC87  E9 FA FD FF FF                  jmp 0x1402fba86
002FBC8C  48 8B 35 15 AE CC 00            mov rsi, qword ptr [rip + 0xccae15]
002FBC93  E9 15 F7 FF FF                  jmp 0x1402fb3ad
002FBC98  48 8B 8E C0 02 00 00            mov rcx, qword ptr [rsi + 0x2c0]
002FBC9F  BA 01 00 00 00                  mov edx, 1
002FBCA4  4A 8B 0C 01                     mov rcx, qword ptr [rcx + r8]
002FBCA8  E8 A3 33 F6 FF                  call 0x14025f050
002FBCAD  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
002FBCB6  E8 35 33 F6 FF                  call 0x14025eff0
002FBCBB  C7 44 24 44 08 00 00 C0         mov dword ptr [rsp + 0x44], 0xc0000008
002FBCC3  E9 EF FD FF FF                  jmp 0x1402fbab7
002FBCC8  84 DB                           test bl, bl
002FBCCA  74 EF                           je 0x1402fbcbb
002FBCCC  EB CA                           jmp 0x1402fbc98
002FBCCE  80 79 64 01                     cmp byte ptr [rcx + 0x64], 1
002FBCD2  0F 84 37 FE FF FF               je 0x1402fbb0f
002FBCD8  8B 41 68                        mov eax, dword ptr [rcx + 0x68]
002FBCDB  F6 41 70 40                     test byte ptr [rcx + 0x70], 0x40
002FBCDF  0F 84 2A FE FF FF               je 0x1402fbb0f
002FBCE5  48 8B 49 78                     mov rcx, qword ptr [rcx + 0x78]
002FBCE9  48 8B C1                        mov rax, rcx
002FBCEC  83 E0 40                        and eax, 0x40
002FBCEF  48 3B C1                        cmp rax, rcx
002FBCF2  0F 85 17 FE FF FF               jne 0x1402fbb0f
002FBCF8  89 94 24 B0 00 00 00            mov dword ptr [rsp + 0xb0], edx
002FBCFF  0F B7 44 24 48                  movzx eax, word ptr [rsp + 0x48]
002FBD04  66 89 44 24 48                  mov word ptr [rsp + 0x48], ax
002FBD09  48 8D 84 24 30 01 00 00         lea rax, [rsp + 0x130]
002FBD11  48 89 84 24 40 01 00 00         mov qword ptr [rsp + 0x140], rax
002FBD19  48 C7 84 24 48 01 00 00 10 00 00 00  mov qword ptr [rsp + 0x148], 0x10
002FBD25  48 8D 44 24 48                  lea rax, [rsp + 0x48]
002FBD2A  48 89 84 24 50 01 00 00         mov qword ptr [rsp + 0x150], rax
002FBD32  48 C7 84 24 58 01 00 00 02 00 00 00  mov qword ptr [rsp + 0x158], 2
002FBD3E  48 8D 84 24 B0 00 00 00         lea rax, [rsp + 0xb0]
002FBD46  48 89 84 24 60 01 00 00         mov qword ptr [rsp + 0x160], rax
002FBD4E  48 C7 84 24 68 01 00 00 04 00 00 00  mov qword ptr [rsp + 0x168], 4
002FBD5A  48 8B 87 90 00 00 00            mov rax, qword ptr [rdi + 0x90]
002FBD61  48 89 84 24 70 01 00 00         mov qword ptr [rsp + 0x170], rax
002FBD69  0F B7 87 88 00 00 00            movzx eax, word ptr [rdi + 0x88]
002FBD70  89 84 24 78 01 00 00            mov dword ptr [rsp + 0x178], eax
002FBD77  44 89 8C 24 7C 01 00 00         mov dword ptr [rsp + 0x17c], r9d
002FBD7F  48 8D 05 5A 48 D1 FF            lea rax, [rip - 0x2eb7a6]
002FBD86  48 89 84 24 80 01 00 00         mov qword ptr [rsp + 0x180], rax
002FBD8E  48 C7 84 24 88 01 00 00 02 00 00 00  mov qword ptr [rsp + 0x188], 2
002FBD9A  48 8D 84 24 40 01 00 00         lea rax, [rsp + 0x140]
002FBDA2  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
002FBDA7  C7 44 24 30 05 00 00 00         mov dword ptr [rsp + 0x30], 5
002FBDAF  4C 89 4C 24 28                  mov qword ptr [rsp + 0x28], r9
002FBDB4  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
002FBDB9  41 B9 01 00 00 00               mov r9d, 1
002FBDBF  45 33 C0                        xor r8d, r8d
002FBDC2  48 8D 15 F7 51 D1 FF            lea rdx, [rip - 0x2eae09]
002FBDC9  48 8B 0D 70 3A C0 00            mov rcx, qword ptr [rip + 0xc03a70]
002FBDD0  E8 FB 32 F6 FF                  call 0x14025f0d0
002FBDD5  E9 41 FD FF FF                  jmp 0x1402fbb1b
002FBDDA  0F BA E0 18                     bt eax, 0x18
002FBDDE  0F 83 B7 F6 FF FF               jae 0x1402fb49b
002FBDE4  C7 44 24 44 BB 00 00 C0         mov dword ptr [rsp + 0x44], 0xc00000bb
002FBDEC  E9 9F FC FF FF                  jmp 0x1402fba90
002FBDF1  48 8B 81 E0 05 00 00            mov rax, qword ptr [rcx + 0x5e0]
002FBDF8  E9 A9 F5 FF FF                  jmp 0x1402fb3a6
002FBDFD  80 79 64 01                     cmp byte ptr [rcx + 0x64], 1
002FBE01  0F 84 79 FD FF FF               je 0x1402fbb80
002FBE07  8B 41 68                        mov eax, dword ptr [rcx + 0x68]
002FBE0A  F6 41 70 40                     test byte ptr [rcx + 0x70], 0x40
002FBE0E  0F 84 6C FD FF FF               je 0x1402fbb80
002FBE14  48 8B 49 78                     mov rcx, qword ptr [rcx + 0x78]
002FBE18  48 8B C1                        mov rax, rcx
002FBE1B  83 E0 40                        and eax, 0x40
002FBE1E  48 3B C1                        cmp rax, rcx
002FBE21  0F 84 81 FD FF FF               je 0x1402fbba8
002FBE27  E9 54 FD FF FF                  jmp 0x1402fbb80
002FBE2C  41 B8 40 00 00 00               mov r8d, 0x40
002FBE32  E9 19 F9 FF FF                  jmp 0x1402fb750
002FBE37  49 8B 48 28                     mov rcx, qword ptr [r8 + 0x28]
002FBE3B  83 79 60 00                     cmp dword ptr [rcx + 0x60], 0
002FBE3F  0F 84 D6 FC FF FF               je 0x1402fbb1b
002FBE45  0F B6 41 64                     movzx eax, byte ptr [rcx + 0x64]
002FBE49  45 84 C9                        test r9b, r9b
002FBE4C  0F 85 C9 FC FF FF               jne 0x1402fbb1b
002FBE52  3C 01                           cmp al, 1
002FBE54  0F 84 C1 FC FF FF               je 0x1402fbb1b
002FBE5A  8B 41 68                        mov eax, dword ptr [rcx + 0x68]
002FBE5D  F6 41 70 40                     test byte ptr [rcx + 0x70], 0x40
002FBE61  0F 84 B4 FC FF FF               je 0x1402fbb1b
002FBE67  48 8B 49 78                     mov rcx, qword ptr [rcx + 0x78]
002FBE6B  48 8B C1                        mov rax, rcx
002FBE6E  83 E0 40                        and eax, 0x40
002FBE71  48 3B C1                        cmp rax, rcx
002FBE74  0F 85 A1 FC FF FF               jne 0x1402fbb1b
002FBE7A  E9 79 FE FF FF                  jmp 0x1402fbcf8
002FBE7F  C7 44 24 44 22 00 00 C0         mov dword ptr [rsp + 0x44], 0xc0000022
002FBE87  E9 04 FC FF FF                  jmp 0x1402fba90
002FBE8C  F0 FF 4A 0C                     lock dec dword ptr [rdx + 0xc]
002FBE90  E9 F6 FB FF FF                  jmp 0x1402fba8b
002FBE95  80 3D 80 EB B0 00 00            cmp byte ptr [rip + 0xb0eb80], 0
002FBE9C  74 5C                           je 0x1402fbefa
002FBE9E  80 3D 0E 9E C5 00 00            cmp byte ptr [rip + 0xc59e0e], 0
002FBEA5  0F 84 4A FB FF FF               je 0x1402fb9f5
002FBEAB  48 8D 94 24 E8 00 00 00         lea rdx, [rsp + 0xe8]
002FBEB3  48 8B CF                        mov rcx, rdi
002FBEB6  E8 55 AF 1B 00                  call 0x1404b6e10
002FBEBB  E9 35 FB FF FF                  jmp 0x1402fb9f5
002FBEC0  41 BA 95 00 00 C0               mov r10d, 0xc0000095
002FBEC6  E9 92 FC FF FF                  jmp 0x1402fbb5d
002FBECB  48 85 C9                        test rcx, rcx
002FBECE  75 08                           jne 0x1402fbed8
002FBED0  49 8B CC                        mov rcx, r12
002FBED3  E9 B6 F4 FF FF                  jmp 0x1402fb38e
002FBED8  E8 4B 99 F2 FF                  call 0x140225828
002FBEDD  84 C0                           test al, al
002FBEDF  0F 85 A9 F4 FF FF               jne 0x1402fb38e
002FBEE5  48 8B 89 18 05 00 00            mov rcx, qword ptr [rcx + 0x518]
002FBEEC  E8 37 99 F2 FF                  call 0x140225828
002FBEF1  84 C0                           test al, al
002FBEF3  74 F0                           je 0x1402fbee5
002FBEF5  E9 94 F4 FF FF                  jmp 0x1402fb38e
002FBEFA  80 3D DB B6 C4 00 00            cmp byte ptr [rip + 0xc4b6db], 0
002FBF01  75 9B                           jne 0x1402fbe9e
002FBF03  EB A6                           jmp 0x1402fbeab
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpTraceMessageVa(__int64 a1, int a2, __int64 a3, unsigned __int16 a4, __int64 a5, unsigned __int8 a6)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned int v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned int v_stack_m144;
    unsigned __int64 v_stack_m148;
    unsigned int v_stack_m14C;
    unsigned int v_stack_m150;
    unsigned int v_stack_m154;
    unsigned int v_stack_m158;
    unsigned __int64 v_stack_m170;
    unsigned int v_stack_m174;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m180;
    unsigned __int64 v_stack_m188;
    unsigned __int64 v_stack_m190;
    unsigned __int64 v_stack_m198;
    unsigned __int64 v_stack_m1A0;
    unsigned __int64 v_stack_m1A8;
    unsigned int v_stack_m1AC;
    unsigned int v_stack_m1B0;
    unsigned __int64 v_stack_m1B8;
    unsigned __int8 v_stack_m1C0;
    unsigned __int8 v_stack_m1C8;
    unsigned __int16 v_stack_m1D0;
    unsigned int v_stack_m1D4;
    unsigned __int8 v_stack_m1D6;
    unsigned __int8 v_stack_m1D7;
    unsigned __int8 v_stack_m1D8;
    unsigned int v_stack_m1F8;
    unsigned __int64 v_stack_m20;
    unsigned int v_stack_m24;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_m74;
    unsigned int v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p20;

    v_stack_p10 = v_rbx;
    v_stack_p20 = v_rsi;
    v_rsp = (v_rsp) - (496);
    result = (*(unsigned __int64 *)(v_rip + 11596911)) ^ (v_rsp);
    v_stack_m38 = result;
    v_stack_m1D0 = a4;
    v_stack_m170 = a3;
    v_stack_m1B0 = a2;
    v_stack_m178 = a1;
    v_stack_m1C8 = a6;
    v_stack_m1C0 = a6;
    result = 0;
    v_stack_m130 = v_xmm0;
    v_stack_m120 = 0;
    v_stack_mE8 = v_xmm0;
    v_r12 = 0;
    v_stack_m1D4 = 0;
    v_stack_m148 = 0;
    v_stack_m1D8 = 0;
    v_stack_m188 = 0;
    v_stack_m1D7 = 0;
    if (a6 == 0) goto loc_002FBC8C;
    if ((unsigned __int8)(*(unsigned __int8 *)(gs_base + (0 + 416))) != 0) goto loc_002FB39F;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1688)) != -3) goto loc_002FBECB;
loc_002FB38E:
    v_stack_mF8 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544) + 1520);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544) + 1520) != 0) goto loc_002FBDF1;
loc_002FB39F:
loc_002FB3A6:
loc_002FB3AD:
    v_stack_m140 = *(unsigned __int64 *)(v_rip + 13452698 + 832);
    v_stack_m1B8 = *(unsigned __int64 *)(v_rip + 13452698 + 832);
    if (((unsigned int)((unsigned __int16)(a1))) >= (*(unsigned int *)(*(unsigned __int64 *)(v_rip + 13452698 + 832) + 16))) goto loc_002FBCBB;
    v_rbx = 0;
    v_stack_m1D6 = 0;
    if (a6 == 1) goto loc_002FB3E4;
    result = KeAreInterruptsEnabled(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544) + 1520), a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_002FB43C;
    if (((unsigned __int8)(v_cr8)) >= 2) goto loc_002FB43C;
loc_002FB3E4:
    a2 = 0;
    a2 = (unsigned int)((a2) * (*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 13452698 + 832) + 704) + (unsigned __int16)(a1) * 8) + 16)));
    a4 = ((unsigned int)(a2)) + (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 13452698 + 832) + 704) + (unsigned __int16)(a1) * 8)));
loc_002FB423:
    if ((((unsigned __int8)(*(unsigned __int64 *)(a4))) & (1)) != 0) goto loc_002FBCAD;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a4))) & (1)) != 0) goto loc_002FB423;
    v_stack_m1D6 = 1;
loc_002FB43C:
    v_stack_m1A0 = (unsigned __int16)(a1) * 8;
    v_stack_m138 = *(unsigned __int64 *)((unsigned __int16)(a1) * 8 + *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 13452698 + 832) + 712) * 1);
    result = (unsigned int)(~((unsigned int)((unsigned int)(*(unsigned __int64 *)((unsigned __int16)(a1) * 8 + *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 13452698 + 832) + 712) * 1)))));
    if ((((unsigned __int8)(result)) & (1)) == 0) goto loc_002FBCC8;
    v_stack_m108 = *(unsigned __int64 *)((unsigned __int16)(a1) * 8 + *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 13452698 + 832) + 712) * 1);
    if (*(unsigned __int64 *)((unsigned __int16)(a1) * 8 + *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 13452698 + 832) + 712) * 1) == 0) goto loc_002FBCBB;
    v_stack_m100 = *(unsigned __int64 *)((unsigned __int16)(a1) * 8 + *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 13452698 + 832) + 712) * 1) + 12;
    if (sign_flag) goto loc_002FBE7F;
    if (a6 == 0) goto loc_002FBDDA;
loc_002FB49B:
    v_stack_m198 = 0;
    v_rsi = (unsigned __int8)(((unsigned __int8)((unsigned int)(v_stack_m1B0))) & (64));
    v_stack_m1D8 = (unsigned __int8)(v_rsi);
    v_r14 = (unsigned __int8)(((unsigned __int8)((unsigned int)(v_stack_m1B0))) & (128));
    v_stack_m1D7 = (unsigned __int8)(v_r14);
    if ((unsigned __int8)(v_rsi) == 0) goto loc_002FB5F5;
    if ((unsigned int)((unsigned int)(v_stack_m174)) == 0) goto loc_002FB5CF;
    v_stack_m188 = a5 + (unsigned int)(v_stack_m174) * 1;
loc_002FB4E4:
    v_stack_m180 = a5 + (unsigned int)(v_stack_m174) * 1;
    v_stack_m178 = 0;
    v_stack_m198 = a5;
loc_002FB4FF:
    if ((unsigned __int8)(v_rsi) == 0) goto loc_002FB573;
    if ((unsigned __int8)(v_r14) != 0) goto loc_002FB585;
    if ((a5 + 8) > (a5 + (unsigned int)(v_stack_m174) * 1)) goto loc_002FB5BC;
    v_stack_m198 = a5 + 8;
loc_002FB525:
    if (*(unsigned __int64 *)(a5 + 8 - 8) == 0) goto loc_002FB55B;
    if ((unsigned __int8)(v_rsi) == 0) goto loc_002FB534;
    if ((unsigned __int8)(v_r14) != 0) goto loc_002FB5B3;
loc_002FB534:
    result = (a5 + 8) + (8);
loc_002FB53C:
    v_stack_m198 = result;
    if (*(unsigned __int64 *)(result - 8) == 0) goto loc_002FB559;
    v_r12 = (v_r12) + (*(unsigned __int64 *)(result - 8));
    v_stack_m178 = v_r12;
    if (v_r12 < (*(unsigned __int64 *)(result - 8))) goto loc_002FB59E;
loc_002FB559:
    goto loc_002FB4FF;
loc_002FB55B:
    v_stack_mE8 = v_xmm0;
    goto loc_002FB61D;
loc_002FB573:
    result = (v_stack_m170) + (8);
    v_stack_m198 = result;
    goto loc_002FB525;
loc_002FB585:
    if ((result + 4) > (a5 + (unsigned int)(v_stack_m174) * 1)) goto loc_002FB5E2;
    v_stack_m198 = result + 4;
    goto loc_002FB525;
loc_002FB59E:
    v_stack_m1D4 = (unsigned int)((unsigned int)(0xC0000095ULL));
    goto loc_002FBA90;
loc_002FB5B3:
    result = (result + 4) + (4);
    goto loc_002FB53C;
loc_002FB5BC:
    v_stack_m1D4 = (unsigned int)((unsigned int)(0xC0000206ULL));
    goto loc_002FBA90;
loc_002FB5CF:
    v_stack_m1D4 = (unsigned int)((unsigned int)(0xC0000206ULL));
    goto loc_002FBA90;
loc_002FB5E2:
    v_stack_m1D4 = (unsigned int)((unsigned int)(0xC0000206ULL));
    goto loc_002FBA90;
loc_002FB5F5:
    goto loc_002FB4E4;
loc_002FB61D:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(0xC0000206ULL)))) & (0xFFFFFFFEULL));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned __int16)(a1) * 8 + *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 13452698 + 832) + 712) * 1) + 264)) != 0) { a1 = (unsigned int)((unsigned int)(0xC0000206ULL)); }
    v_stack_m158 = (unsigned int)(a1);
    a3 = (unsigned int)(((unsigned int)((unsigned int)(a1))) & (1));
    v_stack_m154 = (unsigned int)(a3);
    v_r10 = (unsigned int)(((unsigned int)((unsigned int)(a1))) & (2));
    v_stack_m14C = (unsigned int)(v_r10);
    a4 = (unsigned int)(((unsigned int)((unsigned int)(a1))) & (4));
    v_stack_m150 = a4;
    v_r11 = (unsigned int)(((unsigned int)((unsigned int)(a1))) & (32));
    v_stack_m1AC = (unsigned int)(v_r11);
    result = (unsigned __int8)(((unsigned int)((unsigned int)(a1))) & (24));
    result = (unsigned __int8)(-(result));
    a2 = (unsigned int)(((unsigned int)(0xC0000206ULL)) & (8));
    result = (unsigned int)(-((unsigned int)((unsigned int)(v_r11))));
    a1 = (unsigned int)((a1) & (8));
    a2 = (unsigned int)((a2) + ((unsigned int)(a1)));
    result = (unsigned int)(-((unsigned int)(a4)));
    a1 = (unsigned int)((a1) & (4));
    a2 = (unsigned int)((a2) + ((unsigned int)(a1)));
    result = (unsigned int)(-((unsigned int)((unsigned int)(v_r10))));
    a1 = (unsigned int)((a1) & (16));
    a1 = (unsigned int)((a1) + ((unsigned int)(v_r12)));
    a1 = (unsigned int)((a1) + (a2));
    a1 = (unsigned int)((a1 + a3 * 4) + (8));
    v_stack_m1B0 = (unsigned int)(a1);
    if (v_r12 > ((unsigned int)((unsigned int)(a1)))) goto loc_002FBAE9;
    a4 = 0;
    v_stack_m1F8 = 0;
    result = EtwpReserveTraceBuffer(*(unsigned __int64 *)((unsigned __int16)(a1) * 8 + *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 13452698 + 832) + 712) * 1), (unsigned int)((unsigned int)(a1)), v_stack_m130, v_stack_m148);
    v_r11 = 0;
    v_rsi = v_stack_m1B8;
    v_r13 = v_stack_m188;
    if (*(unsigned __int64 *)(v_stack_m138 + 264) != 0) {
        a1 = 1;
        a1 = (unsigned int)((a1) + 1);
        v_r12 = v_stack_m178;
        v_rsi = v_stack_m1D8;
        v_r13 = v_stack_m188;
        v_stack_m180 = v_r13;
        v_r14 = v_stack_m1D7;
    }
    if (result == 0) goto loc_002FBB3F;
    *(unsigned int *)(result) = 0x90000000ULL;
    *(unsigned __int16 *)(result) = (unsigned __int16)((unsigned int)(v_stack_m1B0));
    *(unsigned __int16 *)(result + 4) = (unsigned __int16)(v_stack_m1D0);
    if ((unsigned __int8)(v_r14) != 0) goto loc_002FBE2C;
loc_002FB750:
    result = (unsigned __int16)(((unsigned __int16)((unsigned int)(v_stack_m158))) & (63));
    result = (unsigned __int16)((result) | (128));
    *(unsigned __int16 *)(result + 6) = (unsigned __int16)(result);
    v_rdi = (result) + (8);
    v_stack_m1A8 = v_rdi;
    if (v_stack_m154 != 0) {
        *(unsigned int *)(v_rdi) = (unsigned int)(a1);
        v_rdi = (v_rdi) + (4);
        a2 = v_rdi;
        v_stack_m1A8 = v_rdi;
        a3 = v_rdi;
    }
    if (v_stack_m150 != 0) goto loc_002FB935;
    if (v_stack_m14C == 0) goto loc_002FB7C7;
    *(unsigned __int64 *)(v_rdi) = v_xmm0;
loc_002FB7BC:
    v_stack_m1A8 = a3 + 16;
loc_002FB7C7:
    result = v_stack_m170;
    v_rdi = a3 + 16;
    if ((((unsigned __int8)((unsigned int)(v_stack_m158))) & (8)) != 0) {
        result = v_stack_m144;
        *(unsigned int *)(a3 + 16 + 4) = (unsigned int)(result);
        result = v_stack_m148;
        *(unsigned int *)(a3 + 16) = (unsigned int)(result);
        v_rdi = a3 + 16 + 8;
        v_stack_m1A8 = v_rdi;
        a3 = v_rdi;
    }
    if (v_stack_m1AC != 0) {
        a2 = *(unsigned __int64 *)(gs_base + (0 + 392));
        v_stack_mF0 = a2;
        a1 = *(unsigned int *)(a2 + 1296);
        v_stack_m118 = (unsigned int)(a1);
        result = v_stack_m1A8;
        *(unsigned int *)(result) = (unsigned int)(a1);
        a1 = a3 + 4;
        v_stack_m1A8 = a1;
        result = *(unsigned int *)(a2 + 1288);
        v_stack_m170 = (unsigned int)(result);
        *(unsigned int *)(a1) = (unsigned int)(result);
        v_rdi = a1 + 4;
        v_stack_m1A8 = v_rdi;
        v_r12 = v_stack_m178;
        v_rsi = v_stack_m1D8;
        v_r13 = v_stack_m188;
        v_stack_m180 = v_r13;
        v_r14 = v_stack_m1D7;
    }
    v_stack_m190 = 0;
    v_stack_m110 = v_r12;
    v_stack_m190 = a5;
loc_002FB87E:
    if ((unsigned __int8)(v_rsi) == 0) goto loc_002FB88C;
    if ((unsigned __int8)(v_r14) != 0) goto loc_002FB94A;
loc_002FB88C:
    v_r15 = (a5) + (8);
loc_002FB894:
    v_stack_m190 = v_r15;
    if (*(unsigned __int64 *)(v_r15 - 8) == 0) goto loc_002FB92F;
    if ((unsigned __int8)(v_rsi) == 0) goto loc_002FB8C1;
    if (v_r15 >= v_r13) goto loc_002FB96F;
    if ((unsigned __int8)(v_rsi) == 0) goto loc_002FB8C1;
    if ((unsigned __int8)(v_r14) != 0) goto loc_002FB957;
loc_002FB8C1:
    v_r15 = (v_r15) + (8);
loc_002FB8C9:
    v_stack_m190 = v_r15;
    if (*(unsigned __int64 *)(v_r15 - 8) == 0) goto loc_002FB922;
    if ((*(unsigned __int64 *)(v_r15 - 8)) > v_r12) goto loc_002FB964;
    if ((unsigned __int8)(v_rsi) == 0) goto loc_002FB8FA;
    if ((*(unsigned __int64 *)(v_r15 - 8) + *(unsigned __int64 *)(v_r15 - 8) * 1) > a1) goto loc_002FB97A;
    if ((*(unsigned __int64 *)(v_r15 - 8) + *(unsigned __int64 *)(v_r15 - 8) * 1) < (*(unsigned __int64 *)(v_r15 - 8))) goto loc_002FB97A;
loc_002FB8FA:
    result = memcpy(v_rdi, *(unsigned __int64 *)(v_r15 - 8), *(unsigned __int64 *)(v_r15 - 8), (unsigned int)(v_stack_m158));
    v_r12 = (v_r12) - (*(unsigned __int64 *)(v_r15 - 8));
    v_stack_m110 = v_r12;
    v_rdi = (v_rdi) + (*(unsigned __int64 *)(v_r15 - 8));
    v_stack_m1A8 = v_rdi;
loc_002FB922:
    goto loc_002FB87E;
loc_002FB92F:
    goto loc_002FB9A2;
loc_002FB935:
    *(unsigned int *)(v_rdi) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m170)));
    goto loc_002FB7BC;
loc_002FB94A:
    v_r15 = (v_r15) + (4);
    goto loc_002FB894;
loc_002FB957:
    v_r15 = (v_r15) + (4);
    goto loc_002FB8C9;
loc_002FB964:
    v_stack_m1D4 = (unsigned int)((unsigned int)(0xC0000206ULL));
    goto loc_002FB9A2;
loc_002FB96F:
    v_stack_m1D4 = (unsigned int)((unsigned int)(0xC0000206ULL));
    goto loc_002FB9A2;
loc_002FB97A:
    v_stack_m180 = v_stack_m188;
    goto loc_002FB8FA;
loc_002FB9A2:
    goto loc_002FB9DD;
loc_002FB9DD:
    if (sign_flag) goto loc_002FBA4D;
    if (((*(unsigned int *)(v_stack_m100)) & (0x80000ULL)) != 0) goto loc_002FBE95;
loc_002FB9F5:
    if (*(unsigned __int64 *)(v_stack_m138 + 1568) == 0) goto loc_002FBA4D;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m130))) == 0) goto loc_002FBA4D;
loc_002FBA4D:
loc_002FBA5B:
    a1 = (v_stack_m130) ^ (*(unsigned __int64 *)(v_stack_m128));
    if (a1 >= 15) goto loc_002FBE8C;
    if (a1 != 15) goto loc_002FBA5B;
loc_002FBA86:
loc_002FBA8B:
loc_002FBA90:
    result = *(unsigned __int64 *)(v_stack_m128);
    if (1 != 0) {
        a1 = *(unsigned __int64 *)(v_stack_m1B8 + 704);
        a2 = 1;
        a1 = *(unsigned __int64 *)(a1 + v_stack_m1A0 * 1);
        result = ExReleaseRundownProtectionCacheAwareEx(a1, a2, v_stack_m1A0, *(unsigned __int64 *)(v_stack_m138 + 1568));
        a1 = *(unsigned __int64 *)(gs_base + (0 + 392));
        result = KeLeaveCriticalRegionThread(a1, a2, v_stack_m1A0, *(unsigned __int64 *)(v_stack_m138 + 1568));
    }
    a1 = (v_stack_m38) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, v_stack_m1A0, *(unsigned __int64 *)(v_stack_m138 + 1568));
    return result;
loc_002FBAE9:
    v_stack_m1AC = (unsigned int)((unsigned int)(0xC0000206ULL));
    if (*(unsigned __int64 *)(v_rip + 12598599) == 0) goto loc_002FBB1B;
    a4 = 0;
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12598599) + 32) + 96)) != 0) goto loc_002FBCCE;
loc_002FBB0F:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 12598599) + 102)) != 0) goto loc_002FBE37;
loc_002FBB1B:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m138 + 816)))) & (8)) == 0) goto loc_002FBA86;
    *(unsigned int *)(v_stack_m138 + 448) = 1;
    goto loc_002FBA86;
loc_002FBB3F:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m138 + 816)))) > 0xFFF8ULL) goto loc_002FBEC0;
    v_r10 = (unsigned int)(0xC0000017ULL);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m138 + 816)))) > (*(unsigned int *)(a4 + 8))) { v_r10 = (unsigned int)((unsigned int)(0x80000005ULL)); }
loc_002FBB5D:
    v_stack_m1AC = (unsigned int)(v_r10);
    if (*(unsigned __int64 *)(v_rip + 12598487) == 0) goto loc_002FBA86;
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12598487) + 32) + 96)) != ((unsigned int)(v_stack_m28))) goto loc_002FBDFD;
loc_002FBB80:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 12598487) + 102)) == ((unsigned __int16)(v_stack_m28))) goto loc_002FBA86;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12598487) + 40)) + (96);
    result = EtwpLevelKeywordEnabled(a1, 2, 64, a4);
    if ((unsigned __int8)(result) == 0) goto loc_002FBA86;
loc_002FBBA8:
    v_stack_m138 = (unsigned int)(v_r10);
    v_stack_m198 = (unsigned __int16)(v_stack_m1A8);
    v_stack_m60 = v_stack_mC0;
    v_stack_m58 = 16;
    v_stack_m50 = v_stack_m198;
    v_stack_m48 = 2;
    v_stack_m40 = v_stack_m138;
    v_stack_m38 = 4;
    v_stack_m30 = *(unsigned __int64 *)(a4 + 144);
    v_stack_m28 = (unsigned int)(*(unsigned __int16 *)(a4 + 136));
    v_stack_m24 = (unsigned int)(v_stack_m28);
    v_stack_m20 = v_rip - 3061336;
    v_stack_m18 = 2;
    v_stack_m1B8 = v_stack_m60;
    v_stack_m1C0 = 5;
    v_stack_m1C8 = v_stack_m28;
    v_stack_m1D0 = v_stack_m28;
    a3 = 0;
    result = EtwWriteEx(*(unsigned __int64 *)(v_rip + 12598206), v_rip - 3058875, a3, 1);
    goto loc_002FBA86;
loc_002FBC8C:
    goto loc_002FB3AD;
loc_002FBC98:
    result = ExReleaseRundownProtectionCacheAwareEx(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 13413909) + 704) + a3 * 1), 1, a3, 1);
loc_002FBCAD:
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), 1, a3, 1);
loc_002FBCBB:
    v_stack_m1AC = 0xC0000008ULL;
    goto loc_002FBAB7;
loc_002FBCC8:
    if ((unsigned __int8)(*(unsigned __int64 *)(v_stack_m28 + 56)) == 0) goto loc_002FBCBB;
    goto loc_002FBC98;
loc_002FBCCE:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 100)) == 1) goto loc_002FBB0F;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 112)) & (64)) == 0) goto loc_002FBB0F;
    result = (unsigned int)((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 120)) & (64));
    if (result != (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 120))) goto loc_002FBB0F;
loc_002FBCF8:
    v_stack_m140 = 1;
    v_stack_m1A8 = (unsigned __int16)(v_stack_m1A8);
    v_stack_mB0 = v_stack_mC0;
    v_stack_mA8 = 16;
    v_stack_mA0 = v_stack_m1A8;
    v_stack_m98 = 2;
    v_stack_m90 = v_stack_m140;
    v_stack_m88 = 4;
    v_stack_m80 = *(unsigned __int64 *)(v_stack_m138 + 144);
    v_stack_m78 = (unsigned int)(*(unsigned __int16 *)(v_stack_m138 + 136));
    v_stack_m74 = 1;
    v_stack_m70 = v_rip - 3061670;
    v_stack_m68 = 2;
    v_stack_m1B8 = v_stack_mB0;
    v_stack_m1C0 = 5;
    v_stack_m1C8 = 1;
    v_stack_m1D0 = 1;
    a3 = 0;
    result = EtwWriteEx(*(unsigned __int64 *)(v_rip + 12597872), v_rip - 3059209, a3, 1);
    goto loc_002FBB1B;
loc_002FBDDA:
    if (condition_is_above_or_equal) goto loc_002FB49B;
    v_stack_m1AC = 0xC00000BBULL;
    goto loc_002FBA90;
loc_002FBDF1:
    goto loc_002FB3A6;
loc_002FBDFD:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 12597872) + 100)) == 1) goto loc_002FBB80;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 12597872) + 112)) & (64)) == 0) goto loc_002FBB80;
    result = (unsigned int)((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12597872) + 120)) & (64));
    if (result == (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12597872) + 120))) goto loc_002FBBA8;
    goto loc_002FBB80;
loc_002FBE2C:
    goto loc_002FB750;
loc_002FBE37:
    if ((*(unsigned int *)(*(unsigned __int64 *)(64 + 40) + 96)) == 0) goto loc_002FBB1B;
    if (1 != 0) goto loc_002FBB1B;
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(64 + 40) + 100))) == 1) goto loc_002FBB1B;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(64 + 40) + 112)) & (64)) == 0) goto loc_002FBB1B;
    result = (unsigned int)((*(unsigned __int64 *)(*(unsigned __int64 *)(64 + 40) + 120)) & (64));
    if (result != (*(unsigned __int64 *)(*(unsigned __int64 *)(64 + 40) + 120))) goto loc_002FBB1B;
    goto loc_002FBCF8;
loc_002FBE7F:
    v_stack_m1AC = 0xC0000022ULL;
    goto loc_002FBA90;
loc_002FBE8C:
    goto loc_002FBA8B;
loc_002FBE95:
    if ((*(unsigned __int8 *)(v_rip + 11594624)) == 0) goto loc_002FBEFA;
loc_002FBE9E:
    if ((*(unsigned __int8 *)(v_rip + 12951054)) == 0) goto loc_002FB9F5;
loc_002FBEAB:
    result = EtwpSendTraceEvent(v_stack_m138, v_stack_m108, 64, 1);
    goto loc_002FB9F5;
loc_002FBEC0:
    goto loc_002FBB5D;
loc_002FBECB:
    if (v_stack_m138 != 0) goto loc_002FBED8;
    goto loc_002FB38E;
loc_002FBED8:
    result = PsIsServerSilo(v_stack_m1C8, v_stack_m108, 64, 1);
    if ((unsigned __int8)(result) != 0) goto loc_002FB38E;
loc_002FBEE5:
    result = PsIsServerSilo(*(unsigned __int64 *)(v_stack_m1C8 + 1304), v_stack_m108, 64, 1);
    if ((unsigned __int8)(result) == 0) goto loc_002FBEE5;
    goto loc_002FB38E;
loc_002FBEFA:
    if ((*(unsigned __int8 *)(v_rip + 12891867)) != 0) goto loc_002FBE9E;
    goto loc_002FBEAB;
}
```

## 5. (Beta) C Style

```c
int64_t EtwpTraceMessageVa(int64_t Arg1, int32_t Arg2, int64_t Arg3, uint16_t Arg4, void *Arg5, uint8_t Arg6)
{
    uint8_t *arg5 = (uint8_t *)Arg5;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint32_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint32_t v_stack_m144;
    uint64_t v_stack_m148;
    uint32_t v_stack_m14C;
    uint32_t v_stack_m150;
    uint32_t v_stack_m154;
    uint32_t v_stack_m158;
    uint64_t v_stack_m170;
    uint32_t v_stack_m174;
    uint64_t v_stack_m178;
    uint64_t v_stack_m18;
    uint64_t v_stack_m180;
    uint64_t v_stack_m188;
    uint64_t v_stack_m190;
    uint64_t v_stack_m198;
    uint64_t v_stack_m1A0;
    uint64_t v_stack_m1A8;
    uint32_t v_stack_m1AC;
    uint32_t v_stack_m1B0;
    uint64_t v_stack_m1B8;
    uint8_t v_stack_m1C0;
    uint8_t v_stack_m1C8;
    uint16_t v_stack_m1D0;
    uint32_t v_stack_m1D4;
    uint8_t v_stack_m1D6;
    uint8_t v_stack_m1D7;
    uint8_t v_stack_m1D8;
    uint32_t v_stack_m1F8;
    uint64_t v_stack_m20;
    uint32_t v_stack_m24;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint32_t v_stack_m74;
    uint32_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p20;

    v_stack_p10 = local_rbx;
    v_stack_p20 = local_rsi;
    local_rsp = (local_rsp) - (496);
    result = (*(uint64_t *)(v_rip + 0xB0F46F)) ^ (local_rsp);
    v_stack_m38 = result;
    v_stack_m1D0 = Arg4;
    v_stack_m170 = Arg3;
    v_stack_m1B0 = Arg2;
    v_stack_m178 = Arg1;
    v_stack_m1C8 = Arg6;
    v_stack_m1C0 = Arg6;
    result = 0;
    v_stack_m130 = v_xmm0;
    v_stack_m120 = 0;
    v_stack_mE8 = v_xmm0;
    local_r12 = 0;
    v_stack_m1D4 = 0;
    v_stack_m148 = 0;
    v_stack_m1D8 = 0;
    v_stack_m188 = 0;
    v_stack_m1D7 = 0;
    if (Arg6 == 0) goto loc_002FBC8C;
    if ((uint8_t)(*(uint8_t *)(gs_base + (0 + 0x1A0))) != 0) goto loc_002FB39F;
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x698)) != -3) goto loc_002FBECB;
loc_002FB38E:
    v_stack_mF8 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220) + 0x5F0);
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220) + 0x5F0) != 0) goto loc_002FBDF1;
loc_002FB39F:
loc_002FB3A6:
loc_002FB3AD:
    v_stack_m140 = *(uint64_t *)(v_rip + 0xCD459A + 0x340);
    v_stack_m1B8 = *(uint64_t *)(v_rip + 0xCD459A + 0x340);
    if (((uint32_t)((uint16_t)(Arg1))) >= (*(uint32_t *)(*(uint64_t *)(v_rip + 0xCD459A + 0x340) + 0x10))) goto loc_002FBCBB;
    local_rbx = 0;
    v_stack_m1D6 = 0;
    if (Arg6 == 1) goto loc_002FB3E4;
    result = KeAreInterruptsEnabled(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220) + 0x5F0), Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_002FB43C;
    if (((uint8_t)(v_cr8)) >= 2) goto loc_002FB43C;
loc_002FB3E4:
    Arg2 = 0;
    Arg2 = (uint32_t)((Arg2) * (*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xCD459A + 0x340) + 0x2C0) + (uint16_t)(Arg1) * 8) + 0x10)));
    Arg4 = ((uint32_t)(Arg2)) + (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xCD459A + 0x340) + 0x2C0) + (uint16_t)(Arg1) * 8)));
loc_002FB423:
    if ((((uint8_t)(*(uint64_t *)(Arg4))) & (1)) != 0) goto loc_002FBCAD;
    if ((((uint8_t)(*(uint64_t *)(Arg4))) & (1)) != 0) goto loc_002FB423;
    v_stack_m1D6 = 1;
loc_002FB43C:
    v_stack_m1A0 = (uint16_t)(Arg1) * 8;
    v_stack_m138 = *(uint64_t *)((uint16_t)(Arg1) * 8 + *(uint64_t *)(*(uint64_t *)(v_rip + 0xCD459A + 0x340) + 0x2C8) * 1);
    result = (uint32_t)(~((uint32_t)((uint32_t)(*(uint64_t *)((uint16_t)(Arg1) * 8 + *(uint64_t *)(*(uint64_t *)(v_rip + 0xCD459A + 0x340) + 0x2C8) * 1)))));
    if ((((uint8_t)(result)) & (1)) == 0) goto loc_002FBCC8;
    v_stack_m108 = *(uint64_t *)((uint16_t)(Arg1) * 8 + *(uint64_t *)(*(uint64_t *)(v_rip + 0xCD459A + 0x340) + 0x2C8) * 1);
    if (*(uint64_t *)((uint16_t)(Arg1) * 8 + *(uint64_t *)(*(uint64_t *)(v_rip + 0xCD459A + 0x340) + 0x2C8) * 1) == 0) goto loc_002FBCBB;
    v_stack_m100 = *(uint64_t *)((uint16_t)(Arg1) * 8 + *(uint64_t *)(*(uint64_t *)(v_rip + 0xCD459A + 0x340) + 0x2C8) * 1) + 12;
    if (sign_flag) goto loc_002FBE7F;
    if (Arg6 == 0) goto loc_002FBDDA;
loc_002FB49B:
    v_stack_m198 = 0;
    local_rsi = (uint8_t)(((uint8_t)((uint32_t)(v_stack_m1B0))) & (64));
    v_stack_m1D8 = (uint8_t)(local_rsi);
    local_r14 = (uint8_t)(((uint8_t)((uint32_t)(v_stack_m1B0))) & (128));
    v_stack_m1D7 = (uint8_t)(local_r14);
    if ((uint8_t)(local_rsi) == 0) goto loc_002FB5F5;
    if ((uint32_t)((uint32_t)(v_stack_m174)) == 0) goto loc_002FB5CF;
    v_stack_m188 = Arg5 + (uint32_t)(v_stack_m174) * 1;
loc_002FB4E4:
    v_stack_m180 = Arg5 + (uint32_t)(v_stack_m174) * 1;
    v_stack_m178 = 0;
    v_stack_m198 = Arg5;
loc_002FB4FF:
    if ((uint8_t)(local_rsi) == 0) goto loc_002FB573;
    if ((uint8_t)(local_r14) != 0) goto loc_002FB585;
    if ((Arg5 + 8) > (Arg5 + (uint32_t)(v_stack_m174) * 1)) goto loc_002FB5BC;
    v_stack_m198 = Arg5 + 8;
loc_002FB525:
    if (*(uint64_t *)(arg5 + 0x8 - 0x8) == 0) goto loc_002FB55B;
    if ((uint8_t)(local_rsi) == 0) goto loc_002FB534;
    if ((uint8_t)(local_r14) != 0) goto loc_002FB5B3;
loc_002FB534:
    result = (Arg5 + 8) + (8);
loc_002FB53C:
    v_stack_m198 = result;
    if (*(uint64_t *)(result - 0x8) == 0) goto loc_002FB559;
    local_r12 = (local_r12) + (*(uint64_t *)(result - 0x8));
    v_stack_m178 = local_r12;
    if (local_r12 < (*(uint64_t *)(result - 0x8))) goto loc_002FB59E;
loc_002FB559:
    goto loc_002FB4FF;
loc_002FB55B:
    v_stack_mE8 = v_xmm0;
    goto loc_002FB61D;
loc_002FB573:
    result = (v_stack_m170) + (8);
    v_stack_m198 = result;
    goto loc_002FB525;
loc_002FB585:
    if ((result + 4) > (Arg5 + (uint32_t)(v_stack_m174) * 1)) goto loc_002FB5E2;
    v_stack_m198 = result + 4;
    goto loc_002FB525;
loc_002FB59E:
    v_stack_m1D4 = (uint32_t)((uint32_t)(0xC0000095ULL));
    goto loc_002FBA90;
loc_002FB5B3:
    result = (result + 4) + (4);
    goto loc_002FB53C;
loc_002FB5BC:
    v_stack_m1D4 = (uint32_t)((uint32_t)(0xC0000206ULL));
    goto loc_002FBA90;
loc_002FB5CF:
    v_stack_m1D4 = (uint32_t)((uint32_t)(0xC0000206ULL));
    goto loc_002FBA90;
loc_002FB5E2:
    v_stack_m1D4 = (uint32_t)((uint32_t)(0xC0000206ULL));
    goto loc_002FBA90;
loc_002FB5F5:
    goto loc_002FB4E4;
loc_002FB61D:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(0xC0000206ULL)))) & (0xFFFFFFFEULL));
    if ((*(uint64_t *)(*(uint64_t *)((uint16_t)(Arg1) * 8 + *(uint64_t *)(*(uint64_t *)(v_rip + 0xCD459A + 0x340) + 0x2C8) * 1) + 0x108)) != 0) { Arg1 = (uint32_t)((uint32_t)(0xC0000206ULL)); }
    v_stack_m158 = (uint32_t)(Arg1);
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) & (1));
    v_stack_m154 = (uint32_t)(Arg3);
    local_r10 = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) & (2));
    v_stack_m14C = (uint32_t)(local_r10);
    Arg4 = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) & (4));
    v_stack_m150 = Arg4;
    local_r11 = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) & (32));
    v_stack_m1AC = (uint32_t)(local_r11);
    result = (uint8_t)(((uint32_t)((uint32_t)(Arg1))) & (24));
    result = (uint8_t)(-(result));
    Arg2 = (uint32_t)(((uint32_t)(0xC0000206ULL)) & (8));
    result = (uint32_t)(-((uint32_t)((uint32_t)(local_r11))));
    Arg1 = (uint32_t)((Arg1) & (8));
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)(Arg1)));
    result = (uint32_t)(-((uint32_t)(Arg4)));
    Arg1 = (uint32_t)((Arg1) & (4));
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)(Arg1)));
    result = (uint32_t)(-((uint32_t)((uint32_t)(local_r10))));
    Arg1 = (uint32_t)((Arg1) & (16));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(local_r12)));
    Arg1 = (uint32_t)((Arg1) + (Arg2));
    Arg1 = (uint32_t)((Arg1 + Arg3 * 4) + (8));
    v_stack_m1B0 = (uint32_t)(Arg1);
    if (local_r12 > ((uint32_t)((uint32_t)(Arg1)))) goto loc_002FBAE9;
    Arg4 = 0;
    v_stack_m1F8 = 0;
    result = EtwpReserveTraceBuffer(*(uint64_t *)((uint16_t)(Arg1) * 8 + *(uint64_t *)(*(uint64_t *)(v_rip + 0xCD459A + 0x340) + 0x2C8) * 1), (uint32_t)((uint32_t)(Arg1)), v_stack_m130, v_stack_m148);
    local_r11 = 0;
    local_rsi = v_stack_m1B8;
    local_r13 = v_stack_m188;
    if (*(uint64_t *)(v_stack_m138 + 0x108) != 0) {
        Arg1 = 1;
        Arg1 = (uint32_t)((Arg1) + 1);
        local_r12 = v_stack_m178;
        local_rsi = v_stack_m1D8;
        local_r13 = v_stack_m188;
        v_stack_m180 = local_r13;
        local_r14 = v_stack_m1D7;
    }
    if (result == 0) goto loc_002FBB3F;
    *(uint32_t *)(result) = 0x90000000ULL;
    *(uint16_t *)(result) = (uint16_t)((uint32_t)(v_stack_m1B0));
    *(uint16_t *)(result + 0x4) = (uint16_t)(v_stack_m1D0);
    if ((uint8_t)(local_r14) != 0) goto loc_002FBE2C;
loc_002FB750:
    result = (uint16_t)(((uint16_t)((uint32_t)(v_stack_m158))) & (63));
    result = (uint16_t)((result) | (128));
    *(uint16_t *)(result + 0x6) = (uint16_t)(result);
    local_rdi = (result) + (8);
    v_stack_m1A8 = local_rdi;
    if (v_stack_m154 != 0) {
        *(uint32_t *)(local_rdi) = (uint32_t)(Arg1);
        local_rdi = (local_rdi) + (4);
        Arg2 = local_rdi;
        v_stack_m1A8 = local_rdi;
        Arg3 = local_rdi;
    }
    if (v_stack_m150 != 0) goto loc_002FB935;
    if (v_stack_m14C == 0) goto loc_002FB7C7;
    *(uint64_t *)(local_rdi) = v_xmm0;
loc_002FB7BC:
    v_stack_m1A8 = Arg3 + 16;
loc_002FB7C7:
    result = v_stack_m170;
    local_rdi = Arg3 + 16;
    if ((((uint8_t)((uint32_t)(v_stack_m158))) & (8)) != 0) {
        result = v_stack_m144;
        *(uint32_t *)(Arg3 + 0x10 + 0x4) = (uint32_t)(result);
        result = v_stack_m148;
        *(uint32_t *)(Arg3 + 0x10) = (uint32_t)(result);
        local_rdi = Arg3 + 16 + 8;
        v_stack_m1A8 = local_rdi;
        Arg3 = local_rdi;
    }
    if (v_stack_m1AC != 0) {
        Arg2 = *(uint64_t *)(gs_base + (0 + 0x188));
        v_stack_mF0 = Arg2;
        Arg1 = *(uint32_t *)(Arg2 + 0x510);
        v_stack_m118 = (uint32_t)(Arg1);
        result = v_stack_m1A8;
        *(uint32_t *)(result) = (uint32_t)(Arg1);
        Arg1 = Arg3 + 4;
        v_stack_m1A8 = Arg1;
        result = *(uint32_t *)(Arg2 + 0x508);
        v_stack_m170 = (uint32_t)(result);
        *(uint32_t *)(Arg1) = (uint32_t)(result);
        local_rdi = Arg1 + 4;
        v_stack_m1A8 = local_rdi;
        local_r12 = v_stack_m178;
        local_rsi = v_stack_m1D8;
        local_r13 = v_stack_m188;
        v_stack_m180 = local_r13;
        local_r14 = v_stack_m1D7;
    }
    v_stack_m190 = 0;
    v_stack_m110 = local_r12;
    v_stack_m190 = Arg5;
loc_002FB87E:
    if ((uint8_t)(local_rsi) == 0) goto loc_002FB88C;
    if ((uint8_t)(local_r14) != 0) goto loc_002FB94A;
loc_002FB88C:
    local_r15 = (Arg5) + (8);
loc_002FB894:
    v_stack_m190 = local_r15;
    if (*(uint64_t *)(local_r15 - 0x8) == 0) goto loc_002FB92F;
    if ((uint8_t)(local_rsi) == 0) goto loc_002FB8C1;
    if (local_r15 >= local_r13) goto loc_002FB96F;
    if ((uint8_t)(local_rsi) == 0) goto loc_002FB8C1;
    if ((uint8_t)(local_r14) != 0) goto loc_002FB957;
loc_002FB8C1:
    local_r15 = (local_r15) + (8);
loc_002FB8C9:
    v_stack_m190 = local_r15;
    if (*(uint64_t *)(local_r15 - 0x8) == 0) goto loc_002FB922;
    if ((*(uint64_t *)(local_r15 - 0x8)) > local_r12) goto loc_002FB964;
    if ((uint8_t)(local_rsi) == 0) goto loc_002FB8FA;
    if ((*(uint64_t *)(local_r15 - 0x8) + *(uint64_t *)(local_r15 - 0x8) * 1) > Arg1) goto loc_002FB97A;
    if ((*(uint64_t *)(local_r15 - 0x8) + *(uint64_t *)(local_r15 - 0x8) * 1) < (*(uint64_t *)(local_r15 - 0x8))) goto loc_002FB97A;
loc_002FB8FA:
    result = memcpy(local_rdi, *(uint64_t *)(local_r15 - 0x8), *(uint64_t *)(local_r15 - 0x8), (uint32_t)(v_stack_m158));
    local_r12 = (local_r12) - (*(uint64_t *)(local_r15 - 0x8));
    v_stack_m110 = local_r12;
    local_rdi = (local_rdi) + (*(uint64_t *)(local_r15 - 0x8));
    v_stack_m1A8 = local_rdi;
loc_002FB922:
    goto loc_002FB87E;
loc_002FB92F:
    goto loc_002FB9A2;
loc_002FB935:
    *(uint32_t *)(local_rdi) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m170)));
    goto loc_002FB7BC;
loc_002FB94A:
    local_r15 = (local_r15) + (4);
    goto loc_002FB894;
loc_002FB957:
    local_r15 = (local_r15) + (4);
    goto loc_002FB8C9;
loc_002FB964:
    v_stack_m1D4 = (uint32_t)((uint32_t)(0xC0000206ULL));
    goto loc_002FB9A2;
loc_002FB96F:
    v_stack_m1D4 = (uint32_t)((uint32_t)(0xC0000206ULL));
    goto loc_002FB9A2;
loc_002FB97A:
    v_stack_m180 = v_stack_m188;
    goto loc_002FB8FA;
loc_002FB9A2:
    goto loc_002FB9DD;
loc_002FB9DD:
    if (sign_flag) goto loc_002FBA4D;
    if (((*(uint32_t *)(v_stack_m100)) & (0x80000ULL)) != 0) goto loc_002FBE95;
loc_002FB9F5:
    if (*(uint64_t *)(v_stack_m138 + 0x620) == 0) goto loc_002FBA4D;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m130))) == 0) goto loc_002FBA4D;
loc_002FBA4D:
loc_002FBA5B:
    Arg1 = (v_stack_m130) ^ (*(uint64_t *)(v_stack_m128));
    if (Arg1 >= 15) goto loc_002FBE8C;
    if (Arg1 != 15) goto loc_002FBA5B;
loc_002FBA86:
loc_002FBA8B:
loc_002FBA90:
    result = *(uint64_t *)(v_stack_m128);
    if (1 != 0) {
        Arg1 = *(uint64_t *)(v_stack_m1B8 + 0x2C0);
        Arg2 = 1;
        Arg1 = *(uint64_t *)(Arg1 + v_stack_m1A0 * 1);
        result = ExReleaseRundownProtectionCacheAwareEx(Arg1, Arg2, v_stack_m1A0, *(uint64_t *)(v_stack_m138 + 0x620));
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x188));
        result = KeLeaveCriticalRegionThread(Arg1, Arg2, v_stack_m1A0, *(uint64_t *)(v_stack_m138 + 0x620));
    }
    Arg1 = (v_stack_m38) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, v_stack_m1A0, *(uint64_t *)(v_stack_m138 + 0x620));
    return result;
loc_002FBAE9:
    v_stack_m1AC = (uint32_t)((uint32_t)(0xC0000206ULL));
    if (*(uint64_t *)(v_rip + 0xC03D47) == 0) goto loc_002FBB1B;
    Arg4 = 0;
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xC03D47) + 0x20) + 0x60)) != 0) goto loc_002FBCCE;
loc_002FBB0F:
    if ((*(uint16_t *)(*(uint64_t *)(v_rip + 0xC03D47) + 0x66)) != 0) goto loc_002FBE37;
loc_002FBB1B:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m138 + 0x330)))) & (8)) == 0) goto loc_002FBA86;
    *(uint32_t *)(v_stack_m138 + 0x1C0) = 1;
    goto loc_002FBA86;
loc_002FBB3F:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m138 + 0x330)))) > 0xFFF8ULL) goto loc_002FBEC0;
    local_r10 = (uint32_t)(0xC0000017ULL);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m138 + 0x330)))) > (*(uint32_t *)(Arg4 + 0x8))) { local_r10 = (uint32_t)((uint32_t)(0x80000005ULL)); }
loc_002FBB5D:
    v_stack_m1AC = (uint32_t)(local_r10);
    if (*(uint64_t *)(v_rip + 0xC03CD7) == 0) goto loc_002FBA86;
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xC03CD7) + 0x20) + 0x60)) != ((uint32_t)(v_stack_m28))) goto loc_002FBDFD;
loc_002FBB80:
    if ((*(uint16_t *)(*(uint64_t *)(v_rip + 0xC03CD7) + 0x66)) == ((uint16_t)(v_stack_m28))) goto loc_002FBA86;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(v_rip + 0xC03CD7) + 0x28)) + (96);
    result = EtwpLevelKeywordEnabled(Arg1, 2, 64, Arg4);
    if ((uint8_t)(result) == 0) goto loc_002FBA86;
loc_002FBBA8:
    v_stack_m138 = (uint32_t)(local_r10);
    v_stack_m198 = (uint16_t)(v_stack_m1A8);
    v_stack_m60 = v_stack_mC0;
    v_stack_m58 = 16;
    v_stack_m50 = v_stack_m198;
    v_stack_m48 = 2;
    v_stack_m40 = v_stack_m138;
    v_stack_m38 = 4;
    v_stack_m30 = *(uint64_t *)(Arg4 + 0x90);
    v_stack_m28 = (uint32_t)(*(uint16_t *)(Arg4 + 0x88));
    v_stack_m24 = (uint32_t)(v_stack_m28);
    v_stack_m20 = v_rip - 3061336;
    v_stack_m18 = 2;
    v_stack_m1B8 = v_stack_m60;
    v_stack_m1C0 = 5;
    v_stack_m1C8 = v_stack_m28;
    v_stack_m1D0 = v_stack_m28;
    Arg3 = 0;
    result = EtwWriteEx(*(uint64_t *)(v_rip + 0xC03BBE), v_rip - 3058875, Arg3, 1);
    goto loc_002FBA86;
loc_002FBC8C:
    goto loc_002FB3AD;
loc_002FBC98:
    result = ExReleaseRundownProtectionCacheAwareEx(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xCCAE15) + 0x2C0) + Arg3 * 1), 1, Arg3, 1);
loc_002FBCAD:
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), 1, Arg3, 1);
loc_002FBCBB:
    v_stack_m1AC = 0xC0000008ULL;
    goto loc_002FBAB7;
loc_002FBCC8:
    if ((uint8_t)(*(uint64_t *)(v_stack_m28 + 0x38)) == 0) goto loc_002FBCBB;
    goto loc_002FBC98;
loc_002FBCCE:
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x64)) == 1) goto loc_002FBB0F;
    if (((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x70)) & (64)) == 0) goto loc_002FBB0F;
    result = (uint32_t)((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x78)) & (64));
    if (result != (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x78))) goto loc_002FBB0F;
loc_002FBCF8:
    v_stack_m140 = 1;
    v_stack_m1A8 = (uint16_t)(v_stack_m1A8);
    v_stack_mB0 = v_stack_mC0;
    v_stack_mA8 = 16;
    v_stack_mA0 = v_stack_m1A8;
    v_stack_m98 = 2;
    v_stack_m90 = v_stack_m140;
    v_stack_m88 = 4;
    v_stack_m80 = *(uint64_t *)(v_stack_m138 + 0x90);
    v_stack_m78 = (uint32_t)(*(uint16_t *)(v_stack_m138 + 0x88));
    v_stack_m74 = 1;
    v_stack_m70 = v_rip - 3061670;
    v_stack_m68 = 2;
    v_stack_m1B8 = v_stack_mB0;
    v_stack_m1C0 = 5;
    v_stack_m1C8 = 1;
    v_stack_m1D0 = 1;
    Arg3 = 0;
    result = EtwWriteEx(*(uint64_t *)(v_rip + 0xC03A70), v_rip - 3059209, Arg3, 1);
    goto loc_002FBB1B;
loc_002FBDDA:
    if (condition_is_above_or_equal) goto loc_002FB49B;
    v_stack_m1AC = 0xC00000BBULL;
    goto loc_002FBA90;
loc_002FBDF1:
    goto loc_002FB3A6;
loc_002FBDFD:
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0xC03A70) + 0x64)) == 1) goto loc_002FBB80;
    if (((*(uint8_t *)(*(uint64_t *)(v_rip + 0xC03A70) + 0x70)) & (64)) == 0) goto loc_002FBB80;
    result = (uint32_t)((*(uint64_t *)(*(uint64_t *)(v_rip + 0xC03A70) + 0x78)) & (64));
    if (result == (*(uint64_t *)(*(uint64_t *)(v_rip + 0xC03A70) + 0x78))) goto loc_002FBBA8;
    goto loc_002FBB80;
loc_002FBE2C:
    goto loc_002FB750;
loc_002FBE37:
    if ((*(uint32_t *)(*(uint64_t *)(64 + 0x28) + 0x60)) == 0) goto loc_002FBB1B;
    if (1 != 0) goto loc_002FBB1B;
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(64 + 0x28) + 0x64))) == 1) goto loc_002FBB1B;
    if (((*(uint8_t *)(*(uint64_t *)(64 + 0x28) + 0x70)) & (64)) == 0) goto loc_002FBB1B;
    result = (uint32_t)((*(uint64_t *)(*(uint64_t *)(64 + 0x28) + 0x78)) & (64));
    if (result != (*(uint64_t *)(*(uint64_t *)(64 + 0x28) + 0x78))) goto loc_002FBB1B;
    goto loc_002FBCF8;
loc_002FBE7F:
    v_stack_m1AC = 0xC0000022ULL;
    goto loc_002FBA90;
loc_002FBE8C:
    goto loc_002FBA8B;
loc_002FBE95:
    if ((*(uint8_t *)(v_rip + 0xB0EB80)) == 0) goto loc_002FBEFA;
loc_002FBE9E:
    if ((*(uint8_t *)(v_rip + 0xC59E0E)) == 0) goto loc_002FB9F5;
loc_002FBEAB:
    result = EtwpSendTraceEvent(v_stack_m138, v_stack_m108, 64, 1);
    goto loc_002FB9F5;
loc_002FBEC0:
    goto loc_002FBB5D;
loc_002FBECB:
    if (v_stack_m138 != 0) goto loc_002FBED8;
    goto loc_002FB38E;
loc_002FBED8:
    result = PsIsServerSilo(v_stack_m1C8, v_stack_m108, 64, 1);
    if ((uint8_t)(result) != 0) goto loc_002FB38E;
loc_002FBEE5:
    result = PsIsServerSilo(*(uint64_t *)(v_stack_m1C8 + 0x518), v_stack_m108, 64, 1);
    if ((uint8_t)(result) == 0) goto loc_002FBEE5;
    goto loc_002FB38E;
loc_002FBEFA:
    if ((*(uint8_t *)(v_rip + 0xC4B6DB)) != 0) goto loc_002FBE9E;
    goto loc_002FBEAB;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg5` | `- 0x8` | `64` | `R` |
| `Arg5` | `- 0x4` | `32` | `R` |
| `Arg5` | `+ 0x0 + rax*1` | `64` | `R` |
| `Arg5` | `+ 0x4` | `64` | `R` |
| `Arg5` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002FB2B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
