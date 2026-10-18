# EtwTraceEvent

- RVA: `0x002FD290`–`0x002FD8BD` (길이 `1,581` bytes)
- VA: `0x00000001402FD290`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00072C08`
- 디코드: `365`개 명령, `1,581/1,581` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **17**; 고유 호출 대상: **10**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x002FD31A` → [PsGetCurrentServerSiloGlobals](PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (function, `0x002FE1F0`)
- `0x002FD346` → [KeGetEffectiveIrql](KeGetEffectiveIrql_function_002F8030.md) (function, `0x002F8030`)
- `0x002FD3C6` → [EtwpCloseLogger](../41/EtwpCloseLogger_function_00418060.md) (function, `0x00418060`)
- `0x002FD4AB` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x002FD521` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x002FD54E` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x002FD587` → [EtwpReserveTraceBuffer](EtwpReserveTraceBuffer_function_002FC8C0.md) (function, `0x002FC8C0`)
- `0x002FD5CD` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x002FD621` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x002FD666` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x002FD695` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x002FD6C9` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x002FD7C3` → [ExReleaseRundownProtectionCacheAwareEx](../25/ExReleaseRundownProtectionCacheAwareEx_function_0025F050.md) (function, `0x0025F050`)
- `0x002FD7D1` → [KeLeaveCriticalRegionThread](../25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x002FD7E5` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x002FD82B` → [KeLeaveCriticalRegionThread](../25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x002FD8B3` → [EtwpInvokeEventCallback](../4B/EtwpInvokeEventCallback_function_004B6F0C.md) (function, `0x004B6F0C`)

### Direct callers
- [NtTraceEvent](NtTraceEvent_function_002FA6C0.md) at `0x002FAD8B`
- [IoWMIWriteEvent](../38/IoWMIWriteEvent_function_00386480.md) at `0x003864F6`
- [sub_006DF40E](../6D/Unknown_function_006DF40E.md) at `0x006DF537`

### Static image references
- `0x002FD2A7` → RVA `0x00E0A740` (`.data`; read)
- `0x002FD842` → RVA `0x00FC6AA8` (`ALMOSTRO`; read)
- `0x002FD881` → RVA `0x00F475DC` (`.data`; read)
- `0x002FD88E` → RVA `0x00E0AA1C` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x002FD521` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (`.text` → `PAGE`)
  - `0x002FD54E` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (`.text` → `PAGE`)
  - `0x002FD666` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (`.text` → `PAGE`)
  - `0x002FD6C9` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (`.text` → `PAGE`)
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x002FD888` → [sub_006DFD3C](../6D/Unknown_function_006DFD3C.md) (`tail-transfer`)
  - `0x002FD895` → [sub_006DFD3C](../6D/Unknown_function_006DFD3C.md) (`tail-transfer`)
  - `0x002FD89B` → [sub_006DFD3C + 0xD](../6D/Unknown_function_006DFD3C.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002FD290  44 89 4C 24 20                  mov dword ptr [rsp + 0x20], r9d
002FD295  53                              push rbx
002FD296  56                              push rsi
002FD297  57                              push rdi
002FD298  41 54                           push r12
002FD29A  41 55                           push r13
002FD29C  41 56                           push r14
002FD29E  41 57                           push r15
002FD2A0  48 81 EC C0 01 00 00            sub rsp, 0x1c0
002FD2A7  48 8B 05 92 D4 B0 00            mov rax, qword ptr [rip + 0xb0d492]
002FD2AE  48 33 C4                        xor rax, rsp
002FD2B1  48 89 84 24 B0 01 00 00         mov qword ptr [rsp + 0x1b0], rax
002FD2B9  45 8B F8                        mov r15d, r8d
002FD2BC  44 89 7C 24 50                  mov dword ptr [rsp + 0x50], r15d
002FD2C1  4C 8B E2                        mov r12, rdx
002FD2C4  48 89 54 24 68                  mov qword ptr [rsp + 0x68], rdx
002FD2C9  44 0F B6 B4 24 20 02 00 00      movzx r14d, byte ptr [rsp + 0x220]
002FD2D2  44 88 74 24 30                  mov byte ptr [rsp + 0x30], r14b
002FD2D7  44 88 74 24 38                  mov byte ptr [rsp + 0x38], r14b
002FD2DC  0F 57 C0                        xorps xmm0, xmm0
002FD2DF  33 C0                           xor eax, eax
002FD2E1  0F 11 84 24 80 00 00 00         movups xmmword ptr [rsp + 0x80], xmm0
002FD2E9  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
002FD2F1  33 FF                           xor edi, edi
002FD2F3  89 7C 24 48                     mov dword ptr [rsp + 0x48], edi
002FD2F7  89 7C 24 44                     mov dword ptr [rsp + 0x44], edi
002FD2FB  89 7C 24 40                     mov dword ptr [rsp + 0x40], edi
002FD2FF  89 7C 24 34                     mov dword ptr [rsp + 0x34], edi
002FD303  48 89 7C 24 78                  mov qword ptr [rsp + 0x78], rdi
002FD308  44 0F B7 E9                     movzx r13d, cx
002FD30C  44 89 6C 24 58                  mov dword ptr [rsp + 0x58], r13d
002FD311  45 84 F6                        test r14b, r14b
002FD314  0F 84 28 05 00 00               je 0x1402fd842
002FD31A  E8 D1 0E 00 00                  call 0x1402fe1f0
002FD31F  48 8B B0 40 03 00 00            mov rsi, qword ptr [rax + 0x340]
002FD326  48 89 74 24 70                  mov qword ptr [rsp + 0x70], rsi
002FD32B  48 89 74 24 60                  mov qword ptr [rsp + 0x60], rsi
002FD330  44 3B 6E 10                     cmp r13d, dword ptr [rsi + 0x10]
002FD334  0F 83 91 00 00 00               jae 0x1402fd3cb
002FD33A  32 DB                           xor bl, bl
002FD33C  88 5C 24 31                     mov byte ptr [rsp + 0x31], bl
002FD340  41 80 FE 01                     cmp r14b, 1
002FD344  74 09                           je 0x1402fd34f
002FD346  E8 E5 AC FF FF                  call 0x1402f8030
002FD34B  3C 02                           cmp al, 2
002FD34D  73 58                           jae 0x1402fd3a7
002FD34F  0F AE E8                        lfence
002FD352  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
002FD35B  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
002FD362  90                              nop
002FD363  48 8B 86 C0 02 00 00            mov rax, qword ptr [rsi + 0x2c0]
002FD36A  4E 8B 04 E8                     mov r8, qword ptr [rax + r13*8]
002FD36E  65 8B 04 25 A4 01 00 00         mov eax, dword ptr gs:[0x1a4]
002FD376  33 D2                           xor edx, edx
002FD378  41 F7 70 14                     div dword ptr [r8 + 0x14]
002FD37C  41 0F AF 50 10                  imul edx, dword ptr [r8 + 0x10]
002FD381  44 8B CA                        mov r9d, edx
002FD384  4D 03 08                        add r9, qword ptr [r8]
002FD387  41 0F 0D 09                     prefetchw byte ptr [r9]
002FD38B  49 8B 01                        mov rax, qword ptr [r9]
002FD38E  A8 01                           test al, 1
002FD390  0F 85 8C 04 00 00               jne 0x1402fd822
002FD396  48 8D 48 02                     lea rcx, [rax + 2]
002FD39A  F0 49 0F B1 09                  lock cmpxchg qword ptr [r9], rcx
002FD39F  75 ED                           jne 0x1402fd38e
002FD3A1  B3 01                           mov bl, 1
002FD3A3  88 5C 24 31                     mov byte ptr [rsp + 0x31], bl
002FD3A7  0F AE E8                        lfence
002FD3AA  48 8B 86 C8 02 00 00            mov rax, qword ptr [rsi + 0x2c8]
002FD3B1  4E 8B 2C E8                     mov r13, qword ptr [rax + r13*8]
002FD3B5  41 F6 C5 01                     test r13b, 1
002FD3B9  74 1D                           je 0x1402fd3d8
002FD3BB  44 0F B6 C3                     movzx r8d, bl
002FD3BF  48 8B D6                        mov rdx, rsi
002FD3C2  8B 4C 24 58                     mov ecx, dword ptr [rsp + 0x58]
002FD3C6  E8 95 AC 11 00                  call 0x140418060
002FD3CB  C7 44 24 34 08 00 00 C0         mov dword ptr [rsp + 0x34], 0xc0000008
002FD3D3  E9 FE 03 00 00                  jmp 0x1402fd7d6
002FD3D8  4C 89 AC 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], r13
002FD3E0  4D 85 ED                        test r13, r13
002FD3E3  74 E6                           je 0x1402fd3cb
002FD3E5  41 8B 45 0C                     mov eax, dword ptr [r13 + 0xc]
002FD3E9  84 C0                           test al, al
002FD3EB  0F 88 44 04 00 00               js 0x1402fd835
002FD3F1  45 84 F6                        test r14b, r14b
002FD3F4  0F 84 54 04 00 00               je 0x1402fd84e
002FD3FA  45 84 F6                        test r14b, r14b
002FD3FD  0F 84 0F 01 00 00               je 0x1402fd512
002FD403  41 F6 C4 03                     test r12b, 3
002FD407  0F 85 14 01 00 00               jne 0x1402fd521
002FD40D  4B 8D 0C 3C                     lea rcx, [r12 + r15]
002FD411  49 B9 00 00 FF FF FF 7F 00 00   movabs r9, 0x7fffffff0000
002FD41B  49 3B C9                        cmp rcx, r9
002FD41E  0F 87 02 01 00 00               ja 0x1402fd526
002FD424  49 3B CC                        cmp rcx, r12
002FD427  0F 82 F9 00 00 00               jb 0x1402fd526
002FD42D  41 0F B7 04 24                  movzx eax, word ptr [r12]
002FD432  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
002FD436  41 3B C7                        cmp eax, r15d
002FD439  0F 82 F0 00 00 00               jb 0x1402fd52f
002FD43F  41 8B 44 24 2C                  mov eax, dword ptr [r12 + 0x2c]
002FD444  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
002FD448  8B 74 24 40                     mov esi, dword ptr [rsp + 0x40]
002FD44C  0F BA E0 14                     bt eax, 0x14
002FD450  0F 83 A2 00 00 00               jae 0x1402fd4f8
002FD456  89 7C 24 4C                     mov dword ptr [rsp + 0x4c], edi
002FD45A  4B 8D 14 3C                     lea rdx, [r12 + r15]
002FD45E  8B CE                           mov ecx, esi
002FD460  41 2B CF                        sub ecx, r15d
002FD463  81 F9 00 01 00 00               cmp ecx, 0x100
002FD469  0F 87 CD 00 00 00               ja 0x1402fd53c
002FD46F  85 C9                           test ecx, ecx
002FD471  0F 84 81 00 00 00               je 0x1402fd4f8
002FD477  45 84 F6                        test r14b, r14b
002FD47A  74 21                           je 0x1402fd49d
002FD47C  F6 C2 03                        test dl, 3
002FD47F  0F 85 C9 00 00 00               jne 0x1402fd54e
002FD485  44 8B C1                        mov r8d, ecx
002FD488  4C 03 C2                        add r8, rdx
002FD48B  4D 3B C1                        cmp r8, r9
002FD48E  0F 87 BF 00 00 00               ja 0x1402fd553
002FD494  4C 3B C2                        cmp r8, rdx
002FD497  0F 82 B6 00 00 00               jb 0x1402fd553
002FD49D  44 8B F9                        mov r15d, ecx
002FD4A0  44 8B C1                        mov r8d, ecx
002FD4A3  48 8D 8C 24 B0 00 00 00         lea rcx, [rsp + 0xb0]
002FD4AB  E8 90 93 3C 00                  call 0x1406c6840
002FD4B0  8B 44 24 50                     mov eax, dword ptr [rsp + 0x50]
002FD4B4  8B F0                           mov esi, eax
002FD4B6  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
002FD4BA  49 C1 EF 04                     shr r15, 4
002FD4BE  44 89 7C 24 44                  mov dword ptr [rsp + 0x44], r15d
002FD4C3  8B D7                           mov edx, edi
002FD4C5  44 8B C0                        mov r8d, eax
002FD4C8  89 54 24 4C                     mov dword ptr [rsp + 0x4c], edx
002FD4CC  41 3B D7                        cmp edx, r15d
002FD4CF  7D 20                           jge 0x1402fd4f1
002FD4D1  48 63 C2                        movsxd rax, edx
002FD4D4  48 03 C0                        add rax, rax
002FD4D7  8B 8C C4 B8 00 00 00            mov ecx, dword ptr [rsp + rax*8 + 0xb8]
002FD4DE  42 8D 34 01                     lea esi, [rcx + r8]
002FD4E2  44 8B C6                        mov r8d, esi
002FD4E5  89 74 24 40                     mov dword ptr [rsp + 0x40], esi
002FD4E9  3B F1                           cmp esi, ecx
002FD4EB  72 12                           jb 0x1402fd4ff
002FD4ED  FF C2                           inc edx
002FD4EF  EB D7                           jmp 0x1402fd4c8
002FD4F1  4C 8B 64 24 68                  mov r12, qword ptr [rsp + 0x68]
002FD4F6  EB 64                           jmp 0x1402fd55c
002FD4F8  44 8B 7C 24 44                  mov r15d, dword ptr [rsp + 0x44]
002FD4FD  EB 5D                           jmp 0x1402fd55c
002FD4FF  B9 05 00 00 80                  mov ecx, 0x80000005
002FD504  89 4C 24 34                     mov dword ptr [rsp + 0x34], ecx
002FD508  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
002FD50D  E9 99 02 00 00                  jmp 0x1402fd7ab
002FD512  49 B9 00 00 FF FF FF 7F 00 00   movabs r9, 0x7fffffff0000
002FD51C  E9 0C FF FF FF                  jmp 0x1402fd42d
002FD521  E8 AA CA 59 00                  call 0x140899fd0
002FD526  41 0F B6 01                     movzx eax, byte ptr [r9]
002FD52A  E9 FE FE FF FF                  jmp 0x1402fd42d
002FD52F  C7 44 24 34 0D 00 00 C0         mov dword ptr [rsp + 0x34], 0xc000000d
002FD537  E9 6F 02 00 00                  jmp 0x1402fd7ab
002FD53C  C7 44 24 34 8C 00 00 C0         mov dword ptr [rsp + 0x34], 0xc000008c
002FD544  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
002FD549  E9 5D 02 00 00                  jmp 0x1402fd7ab
002FD54E  E8 7D CA 59 00                  call 0x140899fd0
002FD553  41 0F B6 01                     movzx eax, byte ptr [r9]
002FD557  E9 41 FF FF FF                  jmp 0x1402fd49d
002FD55C  EB 13                           jmp 0x1402fd571
002FD55E  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
002FD562  0F B6 5C 24 31                  movzx ebx, byte ptr [rsp + 0x31]
002FD567  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
002FD56C  E9 3A 02 00 00                  jmp 0x1402fd7ab
002FD571  89 7C 24 20                     mov dword ptr [rsp + 0x20], edi
002FD575  4C 8D 4C 24 78                  lea r9, [rsp + 0x78]
002FD57A  4C 8D 84 24 80 00 00 00         lea r8, [rsp + 0x80]
002FD582  8B D6                           mov edx, esi
002FD584  49 8B CD                        mov rcx, r13
002FD587  E8 34 F3 FF FF                  call 0x1402fc8c0
002FD58C  4C 8B F0                        mov r14, rax
002FD58F  48 89 84 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rax
002FD597  48 85 C0                        test rax, rax
002FD59A  0F 84 5E 02 00 00               je 0x1402fd7fe
002FD5A0  F7 44 24 48 00 00 10 00         test dword ptr [rsp + 0x48], 0x100000
002FD5A8  0F 84 CA 00 00 00               je 0x1402fd678
002FD5AE  89 7C 24 54                     mov dword ptr [rsp + 0x54], edi
002FD5B2  8B 44 24 50                     mov eax, dword ptr [rsp + 0x50]
002FD5B6  44 8B C0                        mov r8d, eax
002FD5B9  4E 8D 24 30                     lea r12, [rax + r14]
002FD5BD  4C 89 A4 24 98 00 00 00         mov qword ptr [rsp + 0x98], r12
002FD5C5  48 8B 54 24 68                  mov rdx, qword ptr [rsp + 0x68]
002FD5CA  49 8B CE                        mov rcx, r14
002FD5CD  E8 6E 92 3C 00                  call 0x1406c6840
002FD5D2  89 7C 24 54                     mov dword ptr [rsp + 0x54], edi
002FD5D6  41 3B FF                        cmp edi, r15d
002FD5D9  7D 5A                           jge 0x1402fd635
002FD5DB  48 63 C7                        movsxd rax, edi
002FD5DE  48 03 C0                        add rax, rax
002FD5E1  48 8B 94 C4 B0 00 00 00         mov rdx, qword ptr [rsp + rax*8 + 0xb0]
002FD5E9  8B 8C C4 B8 00 00 00            mov ecx, dword ptr [rsp + rax*8 + 0xb8]
002FD5F0  48 85 D2                        test rdx, rdx
002FD5F3  74 77                           je 0x1402fd66c
002FD5F5  85 C9                           test ecx, ecx
002FD5F7  74 73                           je 0x1402fd66c
002FD5F9  80 7C 24 30 00                  cmp byte ptr [rsp + 0x30], 0
002FD5FE  74 18                           je 0x1402fd618
002FD600  4C 8D 04 0A                     lea r8, [rdx + rcx]
002FD604  48 B8 00 00 FF FF FF 7F 00 00   movabs rax, 0x7fffffff0000
002FD60E  4C 3B C0                        cmp r8, rax
002FD611  77 5B                           ja 0x1402fd66e
002FD613  4C 3B C2                        cmp r8, rdx
002FD616  72 56                           jb 0x1402fd66e
002FD618  48 8B F1                        mov rsi, rcx
002FD61B  4C 8B C1                        mov r8, rcx
002FD61E  49 8B CC                        mov rcx, r12
002FD621  E8 1A 92 3C 00                  call 0x1406c6840
002FD626  4C 03 E6                        add r12, rsi
002FD629  4C 89 A4 24 98 00 00 00         mov qword ptr [rsp + 0x98], r12
002FD631  FF C7                           inc edi
002FD633  EB 9D                           jmp 0x1402fd5d2
002FD635  4C 8B 64 24 68                  mov r12, qword ptr [rsp + 0x68]
002FD63A  0F B6 7C 24 30                  movzx edi, byte ptr [rsp + 0x30]
002FD63F  49 BF 00 00 FF FF FF 7F 00 00   movabs r15, 0x7fffffff0000
002FD649  F7 44 24 48 00 00 08 00         test dword ptr [rsp + 0x48], 0x80000
002FD651  0F 84 8D 00 00 00               je 0x1402fd6e4
002FD657  49 8B 4C 24 18                  mov rcx, qword ptr [r12 + 0x18]
002FD65C  40 84 FF                        test dil, dil
002FD65F  74 7B                           je 0x1402fd6dc
002FD661  F6 C1 03                        test cl, 3
002FD664  74 68                           je 0x1402fd6ce
002FD666  E8 65 C9 59 00                  call 0x140899fd0
002FD66B  CC                              int3
002FD66C  EB C3                           jmp 0x1402fd631
002FD66E  0F B6 00                        movzx eax, byte ptr [rax]
002FD671  44 8B 7C 24 44                  mov r15d, dword ptr [rsp + 0x44]
002FD676  EB A0                           jmp 0x1402fd618
002FD678  0F B6 7C 24 30                  movzx edi, byte ptr [rsp + 0x30]
002FD67D  40 84 FF                        test dil, dil
002FD680  75 1A                           jne 0x1402fd69c
002FD682  49 BF 00 00 FF FF FF 7F 00 00   movabs r15, 0x7fffffff0000
002FD68C  44 8B C6                        mov r8d, esi
002FD68F  49 8B D4                        mov rdx, r12
002FD692  49 8B CE                        mov rcx, r14
002FD695  E8 A6 91 3C 00                  call 0x1406c6840
002FD69A  EB AD                           jmp 0x1402fd649
002FD69C  85 F6                           test esi, esi
002FD69E  74 E2                           je 0x1402fd682
002FD6A0  41 F6 C4 03                     test r12b, 3
002FD6A4  75 23                           jne 0x1402fd6c9
002FD6A6  8B CE                           mov ecx, esi
002FD6A8  49 03 CC                        add rcx, r12
002FD6AB  49 BF 00 00 FF FF FF 7F 00 00   movabs r15, 0x7fffffff0000
002FD6B5  49 3B CF                        cmp rcx, r15
002FD6B8  77 05                           ja 0x1402fd6bf
002FD6BA  49 3B CC                        cmp rcx, r12
002FD6BD  73 CD                           jae 0x1402fd68c
002FD6BF  41 0F B6 07                     movzx eax, byte ptr [r15]
002FD6C3  8B 74 24 40                     mov esi, dword ptr [rsp + 0x40]
002FD6C7  EB C3                           jmp 0x1402fd68c
002FD6C9  E8 02 C9 59 00                  call 0x140899fd0
002FD6CE  48 8B C1                        mov rax, rcx
002FD6D1  49 3B CF                        cmp rcx, r15
002FD6D4  49 0F 43 C7                     cmovae rax, r15
002FD6D8  90                              nop
002FD6D9  0F B6 00                        movzx eax, byte ptr [rax]
002FD6DC  0F 10 01                        movups xmm0, xmmword ptr [rcx]
002FD6DF  41 0F 11 46 18                  movups xmmword ptr [r14 + 0x18], xmm0
002FD6E4  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
002FD6E9  EB 23                           jmp 0x1402fd70e
002FD6EB  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
002FD6EF  4C 8B AC 24 A0 00 00 00         mov r13, qword ptr [rsp + 0xa0]
002FD6F7  0F B6 5C 24 31                  movzx ebx, byte ptr [rsp + 0x31]
002FD6FC  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
002FD701  4C 8B B4 24 A8 00 00 00         mov r14, qword ptr [rsp + 0xa8]
002FD709  0F B6 7C 24 38                  movzx edi, byte ptr [rsp + 0x38]
002FD70E  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
002FD717  8B 44 24 40                     mov eax, dword ptr [rsp + 0x40]
002FD71B  0B 84 24 18 02 00 00            or eax, dword ptr [rsp + 0x218]
002FD722  41 89 06                        mov dword ptr [r14], eax
002FD725  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
002FD72A  49 89 46 10                     mov qword ptr [r14 + 0x10], rax
002FD72E  8B 81 8C 02 00 00               mov eax, dword ptr [rcx + 0x28c]
002FD734  41 89 46 28                     mov dword ptr [r14 + 0x28], eax
002FD738  8B 81 DC 02 00 00               mov eax, dword ptr [rcx + 0x2dc]
002FD73E  41 89 46 2C                     mov dword ptr [r14 + 0x2c], eax
002FD742  8B 81 10 05 00 00               mov eax, dword ptr [rcx + 0x510]
002FD748  41 89 46 08                     mov dword ptr [r14 + 8], eax
002FD74C  8B 81 08 05 00 00               mov eax, dword ptr [rcx + 0x508]
002FD752  41 89 46 0C                     mov dword ptr [r14 + 0xc], eax
002FD756  41 F7 45 0C 00 00 08 00         test dword ptr [r13 + 0xc], 0x80000
002FD75E  0F 85 1D 01 00 00               jne 0x1402fd881
002FD764  49 83 BD 20 06 00 00 00         cmp qword ptr [r13 + 0x620], 0
002FD76C  0F 85 2E 01 00 00               jne 0x1402fd8a0
002FD772  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
002FD77A  0F 0D 08                        prefetchw byte ptr [rax]
002FD77D  48 8B 00                        mov rax, qword ptr [rax]
002FD780  48 8B 94 24 80 00 00 00         mov rdx, qword ptr [rsp + 0x80]
002FD788  48 8B CA                        mov rcx, rdx
002FD78B  48 33 C8                        xor rcx, rax
002FD78E  48 83 F9 0F                     cmp rcx, 0xf
002FD792  0F 83 CD 00 00 00               jae 0x1402fd865
002FD798  48 8D 48 01                     lea rcx, [rax + 1]
002FD79C  48 8B 94 24 88 00 00 00         mov rdx, qword ptr [rsp + 0x88]
002FD7A4  F0 48 0F B1 0A                  lock cmpxchg qword ptr [rdx], rcx
002FD7A9  75 D5                           jne 0x1402fd780
002FD7AB  84 DB                           test bl, bl
002FD7AD  74 27                           je 0x1402fd7d6
002FD7AF  8B 44 24 58                     mov eax, dword ptr [rsp + 0x58]
002FD7B3  48 8B 8E C0 02 00 00            mov rcx, qword ptr [rsi + 0x2c0]
002FD7BA  BA 01 00 00 00                  mov edx, 1
002FD7BF  48 8B 0C C1                     mov rcx, qword ptr [rcx + rax*8]
002FD7C3  E8 88 18 F6 FF                  call 0x14025f050
002FD7C8  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
002FD7D1  E8 1A 18 F6 FF                  call 0x14025eff0
002FD7D6  8B 44 24 34                     mov eax, dword ptr [rsp + 0x34]
002FD7DA  48 8B 8C 24 B0 01 00 00         mov rcx, qword ptr [rsp + 0x1b0]
002FD7E2  48 33 CC                        xor rcx, rsp
002FD7E5  E8 56 EE 3A 00                  call 0x1406ac640
002FD7EA  48 81 C4 C0 01 00 00            add rsp, 0x1c0
002FD7F1  41 5F                           pop r15
002FD7F3  41 5E                           pop r14
002FD7F5  41 5D                           pop r13
002FD7F7  41 5C                           pop r12
002FD7F9  5F                              pop rdi
002FD7FA  5E                              pop rsi
002FD7FB  5B                              pop rbx
002FD7FC  C3                              ret
002FD7FD  CC                              int3
002FD7FE  81 FE F8 FF 00 00               cmp esi, 0xfff8
002FD804  77 68                           ja 0x1402fd86e
002FD806  B8 17 00 00 C0                  mov eax, 0xc0000017
002FD80B  B9 05 00 00 80                  mov ecx, 0x80000005
002FD810  41 3B 75 08                     cmp esi, dword ptr [r13 + 8]
002FD814  0F 47 C1                        cmova eax, ecx
002FD817  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
002FD81B  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
002FD820  EB 89                           jmp 0x1402fd7ab
002FD822  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
002FD82B  E8 C0 17 F6 FF                  call 0x14025eff0
002FD830  E9 96 FB FF FF                  jmp 0x1402fd3cb
002FD835  C7 44 24 34 22 00 00 C0         mov dword ptr [rsp + 0x34], 0xc0000022
002FD83D  E9 69 FF FF FF                  jmp 0x1402fd7ab
002FD842  48 8B 35 5F 92 CC 00            mov rsi, qword ptr [rip + 0xcc925f]
002FD849  E9 D8 FA FF FF                  jmp 0x1402fd326
002FD84E  0F BA E0 18                     bt eax, 0x18
002FD852  0F 83 A2 FB FF FF               jae 0x1402fd3fa
002FD858  C7 44 24 34 BB 00 00 C0         mov dword ptr [rsp + 0x34], 0xc00000bb
002FD860  E9 46 FF FF FF                  jmp 0x1402fd7ab
002FD865  F0 FF 4A 0C                     lock dec dword ptr [rdx + 0xc]
002FD869  E9 3D FF FF FF                  jmp 0x1402fd7ab
002FD86E  B8 95 00 00 C0                  mov eax, 0xc0000095
002FD873  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
002FD877  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
002FD87C  E9 2A FF FF FF                  jmp 0x1402fd7ab
002FD881  80 3D 54 9D C4 00 00            cmp byte ptr [rip + 0xc49d54], 0
002FD888  0F 85 AE 24 3E 00               jne 0x1406dfd3c
002FD88E  80 3D 87 D1 B0 00 00            cmp byte ptr [rip + 0xb0d187], 0
002FD895  0F 85 A1 24 3E 00               jne 0x1406dfd3c
002FD89B  E9 A9 24 3E 00                  jmp 0x1406dfd49
002FD8A0  4D 8D 46 18                     lea r8, [r14 + 0x18]
002FD8A4  44 0F B6 CF                     movzx r9d, dil
002FD8A8  48 8D 94 24 80 00 00 00         lea rdx, [rsp + 0x80]
002FD8B0  49 8B CD                        mov rcx, r13
002FD8B3  E8 54 96 1B 00                  call 0x1404b6f0c
002FD8B8  E9 B5 FE FF FF                  jmp 0x1402fd772
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwTraceEvent(unsigned __int16 a1, __int64 a2, int a3, int a4, unsigned __int8 a5)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m180;
    unsigned __int64 v_stack_m188;
    unsigned __int64 v_stack_m190;
    unsigned __int64 v_stack_m198;
    unsigned int v_stack_m1A0;
    unsigned int v_stack_m1A4;
    unsigned int v_stack_m1A8;
    unsigned int v_stack_m1AC;
    unsigned int v_stack_m1B0;
    unsigned int v_stack_m1B4;
    unsigned int v_stack_m1B8;
    unsigned __int8 v_stack_m1C0;
    unsigned int v_stack_m1C4;
    unsigned __int8 v_stack_m1C7;
    unsigned __int8 v_stack_m1C8;
    unsigned int v_stack_m1D8;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_p20;
    unsigned int v_stack_p34;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p80;

    v_stack_p20 = a4;
    v_rsp = (v_rsp) - (448);
    result = (*(unsigned __int64 *)(v_rip + 11588754)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m1A8 = (unsigned int)((unsigned int)(a3));
    v_stack_m190 = a2;
    v_stack_m1C8 = a5;
    v_stack_m1C0 = a5;
    result = 0;
    v_stack_m178 = v_xmm0;
    v_stack_m168 = 0;
    v_rdi = 0;
    v_stack_m1B0 = 0;
    v_stack_m1B4 = 0;
    v_stack_m1B8 = 0;
    v_stack_m1C4 = 0;
    v_stack_m180 = 0;
    v_stack_m1A0 = a1;
    if (a5 == 0) goto loc_002FD842;
    result = PsGetCurrentServerSiloGlobals(a1, a2, a3, a4);
loc_002FD326:
    v_stack_m188 = *(unsigned __int64 *)(result + 832);
    v_stack_m198 = *(unsigned __int64 *)(result + 832);
    if (a1 >= (*(unsigned int *)(*(unsigned __int64 *)(result + 832) + 16))) goto loc_002FD3CB;
    v_rbx = 0;
    v_stack_m1C7 = 0;
    if (a5 == 1) goto loc_002FD34F;
    result = KeGetEffectiveIrql(a1, a2, a3, a4);
    if (((unsigned __int8)(result)) >= 2) goto loc_002FD3A7;
loc_002FD34F:
    a2 = 0;
    a2 = (unsigned int)((a2) * (*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 832) + 704) + a1 * 8) + 16)));
    a4 = ((unsigned int)((unsigned int)(a2))) + (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 832) + 704) + a1 * 8)));
loc_002FD38E:
    if ((((unsigned __int8)(*(unsigned __int64 *)(a4))) & (1)) != 0) goto loc_002FD822;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a4))) & (1)) != 0) goto loc_002FD38E;
    v_stack_m1C7 = 1;
loc_002FD3A7:
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 832) + 712) + a1 * 8))) & (1)) == 0) goto loc_002FD3D8;
    result = EtwpCloseLogger((unsigned int)(v_stack_m1A0), *(unsigned __int64 *)(result + 832), 1, a4);
loc_002FD3CB:
    v_stack_m1C4 = 0xC0000008ULL;
    goto loc_002FD7D6;
loc_002FD3D8:
    v_stack_m158 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 832) + 712) + a1 * 8);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 832) + 712) + a1 * 8) == 0) goto loc_002FD3CB;
    if (sign_flag) goto loc_002FD835;
    if (a5 == 0) goto loc_002FD84E;
loc_002FD3FA:
    if (a5 == 0) goto loc_002FD512;
    if ((((unsigned __int8)(a2)) & (3)) != 0) goto loc_002FD521;
    if ((a2 + (unsigned int)(a3) * 1) > a4) goto loc_002FD526;
    if ((a2 + (unsigned int)(a3) * 1) < a2) goto loc_002FD526;
loc_002FD42D:
    v_stack_m1B8 = (unsigned int)(*(unsigned __int16 *)(a2));
    if (((unsigned int)(*(unsigned __int16 *)(a2))) < ((unsigned int)((unsigned int)(a3)))) goto loc_002FD52F;
    v_stack_m1B0 = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 44)));
    if (((unsigned int)(*(unsigned __int16 *)(a2))) >= ((unsigned int)((unsigned int)(a3)))) goto loc_002FD4F8;
    v_stack_m1AC = 0;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m1B8)))) - ((unsigned int)((unsigned int)(a3))));
    if (a1 > 256) goto loc_002FD53C;
    if (a1 == 0) goto loc_002FD4F8;
    if (a5 == 0) goto loc_002FD49D;
    if ((((unsigned __int8)(a2 + (unsigned int)(a3) * 1)) & (3)) != 0) goto loc_002FD54E;
    a3 = ((unsigned int)(a1)) + (a2 + (unsigned int)(a3) * 1);
    if (a3 > a4) goto loc_002FD553;
    if (a3 < (a2 + (unsigned int)(a3) * 1)) goto loc_002FD553;
loc_002FD49D:
    result = memcpy(v_stack_m148, a2 + (unsigned int)(a3) * 1, (unsigned int)(a1), a4);
    v_stack_m1B8 = (unsigned int)((unsigned int)(v_stack_m1A8));
    v_r15 = ((unsigned int)(a1)) >> (4);
    v_stack_m1B4 = (unsigned int)(v_r15);
loc_002FD4C8:
    v_stack_m1AC = 0;
    if (0 >= ((unsigned int)(v_r15))) goto loc_002FD4F1;
    result = ((int)(0)) + ((int)(0));
    v_stack_m1B8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp + result * 8 + 184)) + (unsigned int)((unsigned int)((unsigned int)(v_stack_m1A8))) * 1);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp + result * 8 + 184)) + (unsigned int)((unsigned int)((unsigned int)(v_stack_m1A8))) * 1)) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp + result * 8 + 184))))) goto loc_002FD4FF;
    a2 = (unsigned int)((0) + 1);
    goto loc_002FD4C8;
loc_002FD4F1:
    goto loc_002FD55C;
loc_002FD4F8:
    goto loc_002FD55C;
loc_002FD4FF:
    v_stack_m1C4 = (unsigned int)((unsigned int)(0x80000005ULL));
    goto loc_002FD7AB;
loc_002FD512:
    goto loc_002FD42D;
loc_002FD521:
    result = ExRaiseDatatypeMisalignment((unsigned int)(0x80000005ULL), a2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp + result * 8 + 184)) + (unsigned int)((unsigned int)((unsigned int)(v_stack_m1A8))) * 1)), a4);
loc_002FD526:
    goto loc_002FD42D;
loc_002FD52F:
    v_stack_m1C4 = 0xC000000DULL;
    goto loc_002FD7AB;
loc_002FD53C:
    v_stack_m1C4 = 0xC000008CULL;
    goto loc_002FD7AB;
loc_002FD54E:
    result = ExRaiseDatatypeMisalignment((unsigned int)(0x80000005ULL), a2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp + result * 8 + 184)) + (unsigned int)((unsigned int)((unsigned int)(v_stack_m1A8))) * 1)), a4);
loc_002FD553:
    goto loc_002FD49D;
loc_002FD55C:
    goto loc_002FD571;
loc_002FD571:
    v_stack_m1D8 = 0;
    result = EtwpReserveTraceBuffer(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 832) + 712) + a1 * 8), (unsigned int)((unsigned int)(v_stack_m198)), v_stack_m178, v_stack_m180);
    v_stack_m150 = result;
    if (result == 0) goto loc_002FD7FE;
    if (((v_stack_m1B0) & (0x100000ULL)) == 0) goto loc_002FD678;
    v_stack_m1A4 = 0;
    v_stack_m160 = (unsigned int)(v_stack_m1A8) + result * 1;
    result = memcpy(result, v_stack_m190, (unsigned int)((unsigned int)((unsigned int)(v_stack_m1A8))), v_stack_m180);
loc_002FD5D2:
    v_stack_m1A4 = 0;
    if (0 >= ((unsigned int)((unsigned int)(v_stack_m1B4)))) goto loc_002FD635;
    result = ((int)(0)) + ((int)(0));
    if (*(unsigned __int64 *)(v_rsp + result * 8 + 176) == 0) goto loc_002FD66C;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp + result * 8 + 184))) == 0) goto loc_002FD66C;
    if (v_stack_m1C8 == 0) goto loc_002FD618;
    if ((*(unsigned __int64 *)(v_rsp + result * 8 + 176) + (unsigned int)(*(unsigned int *)(v_rsp + result * 8 + 184)) * 1) > result) goto loc_002FD66E;
    if ((*(unsigned __int64 *)(v_rsp + result * 8 + 176) + (unsigned int)(*(unsigned int *)(v_rsp + result * 8 + 184)) * 1) < (*(unsigned __int64 *)(v_rsp + result * 8 + 176))) goto loc_002FD66E;
loc_002FD618:
    result = memcpy((unsigned int)(v_stack_m1A8) + result * 1, *(unsigned __int64 *)(v_rsp + result * 8 + 176), (unsigned int)(*(unsigned int *)(v_rsp + result * 8 + 184)), v_stack_m180);
    v_r12 = ((unsigned int)(v_stack_m1A8) + result * 1) + ((unsigned int)(*(unsigned int *)(v_rsp + result * 8 + 184)));
    v_stack_m160 = v_r12;
loc_002FD631:
    v_rdi = (unsigned int)((v_rdi) + 1);
    goto loc_002FD5D2;
loc_002FD635:
loc_002FD649:
    if (((v_stack_m1B0) & (0x80000ULL)) == 0) goto loc_002FD6E4;
    if ((unsigned __int8)(v_stack_m1C8) == 0) goto loc_002FD6DC;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_m190 + 24))) & (3)) == 0) goto loc_002FD6CE;
    result = ExRaiseDatatypeMisalignment(*(unsigned __int64 *)(v_stack_m190 + 24), *(unsigned __int64 *)(v_rsp + result * 8 + 176), (unsigned int)(*(unsigned int *)(v_rsp + result * 8 + 184)), v_stack_m180);
loc_002FD66C:
    goto loc_002FD631;
loc_002FD66E:
    goto loc_002FD618;
loc_002FD678:
    if ((unsigned __int8)(v_stack_m1C8) != 0) goto loc_002FD69C;
loc_002FD682:
loc_002FD68C:
    result = memcpy(result, v_stack_m190, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp + result * 8 + 184)))), v_stack_m180);
    goto loc_002FD649;
loc_002FD69C:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp + result * 8 + 184))) == 0) goto loc_002FD682;
    if ((((unsigned __int8)(v_stack_m190)) & (3)) != 0) goto loc_002FD6C9;
    a1 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp + result * 8 + 184))))) + (v_stack_m190);
    if (a1 > ((unsigned int)(v_stack_m1B4))) goto loc_002FD6BF;
    if (a1 >= v_stack_m190) goto loc_002FD68C;
loc_002FD6BF:
    goto loc_002FD68C;
loc_002FD6C9:
    result = ExRaiseDatatypeMisalignment(a1, v_stack_m190, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp + result * 8 + 184)))), v_stack_m180);
loc_002FD6CE:
    if (a1 >= ((unsigned int)(v_stack_m1B4))) { a1 = (unsigned int)(v_stack_m1B4); }
loc_002FD6DC:
    *(unsigned __int64 *)(result + 24) = v_xmm0;
loc_002FD6E4:
    goto loc_002FD70E;
loc_002FD70E:
    result = (unsigned int)(((unsigned int)(v_stack_m1B8)) | (v_stack_p20));
    *(unsigned int *)(result) = (unsigned int)(result);
    *(unsigned __int64 *)(result + 16) = v_stack_m180;
    *(unsigned int *)(result + 40) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 652)));
    *(unsigned int *)(result + 44) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 732)));
    *(unsigned int *)(result + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1296)));
    *(unsigned int *)(result + 12) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1288)));
    if (((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 832) + 712) + a1 * 8) + 12)) & (0x80000ULL)) != 0) goto loc_002FD881;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 832) + 712) + a1 * 8) + 1568)) != 0) goto loc_002FD8A0;
loc_002FD772:
loc_002FD780:
    a1 = (v_stack_m178) ^ (*(unsigned __int64 *)(v_stack_m170));
    if (a1 >= 15) goto loc_002FD865;
    if (a1 != 15) goto loc_002FD780;
loc_002FD7AB:
    result = *(unsigned __int64 *)(v_stack_m170);
    if (1 != 0) {
        result = v_stack_m1A0;
        a1 = *(unsigned __int64 *)(v_stack_m198 + 704);
        a2 = 1;
        a1 = *(unsigned __int64 *)(a1 + result * 8);
        result = ExReleaseRundownProtectionCacheAwareEx(a1, a2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp + result * 8 + 184)))), v_stack_m180);
        a1 = *(unsigned __int64 *)(gs_base + (0 + 392));
        result = KeLeaveCriticalRegionThread(a1, a2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp + result * 8 + 184)))), v_stack_m180);
    }
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp + result * 8 + 184)))), v_stack_m180);
    v_rsp = (v_rsp) + (448);
    return result;
loc_002FD7FE:
    if (((unsigned int)(v_stack_m198)) > 0xFFF8ULL) goto loc_002FD86E;
    result = (unsigned int)(0xC0000017ULL);
    if (((unsigned int)(v_stack_m198)) > (*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 832) + 712) + a1 * 8) + 8))) { result = (unsigned int)((unsigned int)(0x80000005ULL)); }
    v_stack_p34 = (unsigned int)(result);
    goto loc_002FD7AB;
loc_002FD822:
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp + result * 8 + 184)))), v_stack_m180);
    goto loc_002FD3CB;
loc_002FD835:
    v_stack_p34 = 0xC0000022ULL;
    goto loc_002FD7AB;
loc_002FD842:
    goto loc_002FD326;
loc_002FD84E:
    if (((unsigned int)(v_stack_m198)) >= (*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 832) + 712) + a1 * 8) + 8))) goto loc_002FD3FA;
    v_stack_p34 = 0xC00000BBULL;
    goto loc_002FD7AB;
loc_002FD865:
    goto loc_002FD7AB;
loc_002FD86E:
    v_stack_p34 = (unsigned int)((unsigned int)(0xC0000095ULL));
    goto loc_002FD7AB;
loc_002FD881:
loc_002FD8A0:
    result = EtwpInvokeEventCallback(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 832) + 712) + a1 * 8), v_stack_p80, result + 24, (unsigned __int8)(v_stack_m1C8));
    goto loc_002FD772;
}
```

## 5. (Beta) C Style

```c
int64_t EtwTraceEvent(uint16_t Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4, uint8_t Arg5)
{
    int64_t result;
    int64_t local_r12;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m148;
    uint64_t v_stack_m150;
    uint64_t v_stack_m158;
    uint64_t v_stack_m160;
    uint64_t v_stack_m168;
    uint64_t v_stack_m170;
    uint64_t v_stack_m178;
    uint64_t v_stack_m180;
    uint64_t v_stack_m188;
    uint64_t v_stack_m190;
    uint64_t v_stack_m198;
    uint32_t v_stack_m1A0;
    uint32_t v_stack_m1A4;
    uint32_t v_stack_m1A8;
    uint32_t v_stack_m1AC;
    uint32_t v_stack_m1B0;
    uint32_t v_stack_m1B4;
    uint32_t v_stack_m1B8;
    uint8_t v_stack_m1C0;
    uint32_t v_stack_m1C4;
    uint8_t v_stack_m1C7;
    uint8_t v_stack_m1C8;
    uint32_t v_stack_m1D8;
    uint64_t v_stack_m48;
    uint32_t v_stack_p20;
    uint32_t v_stack_p34;
    uint64_t v_stack_p60;
    uint64_t v_stack_p80;

    v_stack_p20 = Arg4;
    local_rsp = (local_rsp) - (448);
    result = (*(uint64_t *)(v_rip + 0xB0D492)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m1A8 = (uint32_t)((uint32_t)(Arg3));
    v_stack_m190 = Arg2;
    v_stack_m1C8 = Arg5;
    v_stack_m1C0 = Arg5;
    result = 0;
    v_stack_m178 = v_xmm0;
    v_stack_m168 = 0;
    local_rdi = 0;
    v_stack_m1B0 = 0;
    v_stack_m1B4 = 0;
    v_stack_m1B8 = 0;
    v_stack_m1C4 = 0;
    v_stack_m180 = 0;
    v_stack_m1A0 = Arg1;
    if (Arg5 == 0) goto loc_002FD842;
    result = PsGetCurrentServerSiloGlobals(Arg1, Arg2, Arg3, Arg4);
loc_002FD326:
    v_stack_m188 = *(uint64_t *)(result + 0x340);
    v_stack_m198 = *(uint64_t *)(result + 0x340);
    if (Arg1 >= (*(uint32_t *)(*(uint64_t *)(result + 0x340) + 0x10))) goto loc_002FD3CB;
    local_rbx = 0;
    v_stack_m1C7 = 0;
    if (Arg5 == 1) goto loc_002FD34F;
    result = KeGetEffectiveIrql(Arg1, Arg2, Arg3, Arg4);
    if (((uint8_t)(result)) >= 2) goto loc_002FD3A7;
loc_002FD34F:
    Arg2 = 0;
    Arg2 = (uint32_t)((Arg2) * (*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x340) + 0x2C0) + Arg1 * 8) + 0x10)));
    Arg4 = ((uint32_t)((uint32_t)(Arg2))) + (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x340) + 0x2C0) + Arg1 * 8)));
loc_002FD38E:
    if ((((uint8_t)(*(uint64_t *)(Arg4))) & (1)) != 0) goto loc_002FD822;
    if ((((uint8_t)(*(uint64_t *)(Arg4))) & (1)) != 0) goto loc_002FD38E;
    v_stack_m1C7 = 1;
loc_002FD3A7:
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x340) + 0x2C8) + Arg1 * 8))) & (1)) == 0) goto loc_002FD3D8;
    result = EtwpCloseLogger((uint32_t)(v_stack_m1A0), *(uint64_t *)(result + 0x340), 1, Arg4);
loc_002FD3CB:
    v_stack_m1C4 = 0xC0000008ULL;
    goto loc_002FD7D6;
loc_002FD3D8:
    v_stack_m158 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x340) + 0x2C8) + Arg1 * 8);
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x340) + 0x2C8) + Arg1 * 8) == 0) goto loc_002FD3CB;
    if (sign_flag) goto loc_002FD835;
    if (Arg5 == 0) goto loc_002FD84E;
loc_002FD3FA:
    if (Arg5 == 0) goto loc_002FD512;
    if ((((uint8_t)(Arg2)) & (3)) != 0) goto loc_002FD521;
    if ((Arg2 + (uint32_t)(Arg3) * 1) > Arg4) goto loc_002FD526;
    if ((Arg2 + (uint32_t)(Arg3) * 1) < Arg2) goto loc_002FD526;
loc_002FD42D:
    v_stack_m1B8 = (uint32_t)(*(uint16_t *)(Arg2));
    if (((uint32_t)(*(uint16_t *)(Arg2))) < ((uint32_t)((uint32_t)(Arg3)))) goto loc_002FD52F;
    v_stack_m1B0 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0x2C)));
    if (((uint32_t)(*(uint16_t *)(Arg2))) >= ((uint32_t)((uint32_t)(Arg3)))) goto loc_002FD4F8;
    v_stack_m1AC = 0;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m1B8)))) - ((uint32_t)((uint32_t)(Arg3))));
    if (Arg1 > 256) goto loc_002FD53C;
    if (Arg1 == 0) goto loc_002FD4F8;
    if (Arg5 == 0) goto loc_002FD49D;
    if ((((uint8_t)(Arg2 + (uint32_t)(Arg3) * 1)) & (3)) != 0) goto loc_002FD54E;
    Arg3 = ((uint32_t)(Arg1)) + (Arg2 + (uint32_t)(Arg3) * 1);
    if (Arg3 > Arg4) goto loc_002FD553;
    if (Arg3 < (Arg2 + (uint32_t)(Arg3) * 1)) goto loc_002FD553;
loc_002FD49D:
    result = memcpy(v_stack_m148, Arg2 + (uint32_t)(Arg3) * 1, (uint32_t)(Arg1), Arg4);
    v_stack_m1B8 = (uint32_t)((uint32_t)(v_stack_m1A8));
    local_r15 = ((uint32_t)(Arg1)) >> (4);
    v_stack_m1B4 = (uint32_t)(local_r15);
loc_002FD4C8:
    v_stack_m1AC = 0;
    if (0 >= ((uint32_t)(local_r15))) goto loc_002FD4F1;
    result = ((int32_t)(0)) + ((int32_t)(0));
    v_stack_m1B8 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp + result * 8 + 0xB8)) + (uint32_t)((uint32_t)((uint32_t)(v_stack_m1A8))) * 1);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp + result * 8 + 0xB8)) + (uint32_t)((uint32_t)((uint32_t)(v_stack_m1A8))) * 1)) < ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp + result * 8 + 0xB8))))) goto loc_002FD4FF;
    Arg2 = (uint32_t)((0) + 1);
    goto loc_002FD4C8;
loc_002FD4F1:
    goto loc_002FD55C;
loc_002FD4F8:
    goto loc_002FD55C;
loc_002FD4FF:
    v_stack_m1C4 = (uint32_t)((uint32_t)(0x80000005ULL));
    goto loc_002FD7AB;
loc_002FD512:
    goto loc_002FD42D;
loc_002FD521:
    result = ExRaiseDatatypeMisalignment((uint32_t)(0x80000005ULL), Arg2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp + result * 8 + 0xB8)) + (uint32_t)((uint32_t)((uint32_t)(v_stack_m1A8))) * 1)), Arg4);
loc_002FD526:
    goto loc_002FD42D;
loc_002FD52F:
    v_stack_m1C4 = 0xC000000DULL;
    goto loc_002FD7AB;
loc_002FD53C:
    v_stack_m1C4 = 0xC000008CULL;
    goto loc_002FD7AB;
loc_002FD54E:
    result = ExRaiseDatatypeMisalignment((uint32_t)(0x80000005ULL), Arg2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp + result * 8 + 0xB8)) + (uint32_t)((uint32_t)((uint32_t)(v_stack_m1A8))) * 1)), Arg4);
loc_002FD553:
    goto loc_002FD49D;
loc_002FD55C:
    goto loc_002FD571;
loc_002FD571:
    v_stack_m1D8 = 0;
    result = EtwpReserveTraceBuffer(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x340) + 0x2C8) + Arg1 * 8), (uint32_t)((uint32_t)(v_stack_m198)), v_stack_m178, v_stack_m180);
    v_stack_m150 = result;
    if (result == 0) goto loc_002FD7FE;
    if (((v_stack_m1B0) & (0x100000ULL)) == 0) goto loc_002FD678;
    v_stack_m1A4 = 0;
    v_stack_m160 = (uint32_t)(v_stack_m1A8) + result * 1;
    result = memcpy(result, v_stack_m190, (uint32_t)((uint32_t)((uint32_t)(v_stack_m1A8))), v_stack_m180);
loc_002FD5D2:
    v_stack_m1A4 = 0;
    if (0 >= ((uint32_t)((uint32_t)(v_stack_m1B4)))) goto loc_002FD635;
    result = ((int32_t)(0)) + ((int32_t)(0));
    if (*(uint64_t *)(local_rsp + result * 8 + 0xB0) == 0) goto loc_002FD66C;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp + result * 8 + 0xB8))) == 0) goto loc_002FD66C;
    if (v_stack_m1C8 == 0) goto loc_002FD618;
    if ((*(uint64_t *)(local_rsp + result * 8 + 0xB0) + (uint32_t)(*(uint32_t *)(local_rsp + result * 8 + 0xB8)) * 1) > result) goto loc_002FD66E;
    if ((*(uint64_t *)(local_rsp + result * 8 + 0xB0) + (uint32_t)(*(uint32_t *)(local_rsp + result * 8 + 0xB8)) * 1) < (*(uint64_t *)(local_rsp + result * 8 + 0xB0))) goto loc_002FD66E;
loc_002FD618:
    result = memcpy((uint32_t)(v_stack_m1A8) + result * 1, *(uint64_t *)(local_rsp + result * 8 + 0xB0), (uint32_t)(*(uint32_t *)(local_rsp + result * 8 + 0xB8)), v_stack_m180);
    local_r12 = ((uint32_t)(v_stack_m1A8) + result * 1) + ((uint32_t)(*(uint32_t *)(local_rsp + result * 8 + 0xB8)));
    v_stack_m160 = local_r12;
loc_002FD631:
    local_rdi = (uint32_t)((local_rdi) + 1);
    goto loc_002FD5D2;
loc_002FD635:
loc_002FD649:
    if (((v_stack_m1B0) & (0x80000ULL)) == 0) goto loc_002FD6E4;
    if ((uint8_t)(v_stack_m1C8) == 0) goto loc_002FD6DC;
    if ((((uint8_t)(*(uint64_t *)(v_stack_m190 + 0x18))) & (3)) == 0) goto loc_002FD6CE;
    result = ExRaiseDatatypeMisalignment(*(uint64_t *)(v_stack_m190 + 0x18), *(uint64_t *)(local_rsp + result * 8 + 0xB0), (uint32_t)(*(uint32_t *)(local_rsp + result * 8 + 0xB8)), v_stack_m180);
loc_002FD66C:
    goto loc_002FD631;
loc_002FD66E:
    goto loc_002FD618;
loc_002FD678:
    if ((uint8_t)(v_stack_m1C8) != 0) goto loc_002FD69C;
loc_002FD682:
loc_002FD68C:
    result = memcpy(result, v_stack_m190, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp + result * 8 + 0xB8)))), v_stack_m180);
    goto loc_002FD649;
loc_002FD69C:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp + result * 8 + 0xB8))) == 0) goto loc_002FD682;
    if ((((uint8_t)(v_stack_m190)) & (3)) != 0) goto loc_002FD6C9;
    Arg1 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp + result * 8 + 0xB8))))) + (v_stack_m190);
    if (Arg1 > ((uint32_t)(v_stack_m1B4))) goto loc_002FD6BF;
    if (Arg1 >= v_stack_m190) goto loc_002FD68C;
loc_002FD6BF:
    goto loc_002FD68C;
loc_002FD6C9:
    result = ExRaiseDatatypeMisalignment(Arg1, v_stack_m190, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp + result * 8 + 0xB8)))), v_stack_m180);
loc_002FD6CE:
    if (Arg1 >= ((uint32_t)(v_stack_m1B4))) { Arg1 = (uint32_t)(v_stack_m1B4); }
loc_002FD6DC:
    *(uint64_t *)(result + 0x18) = v_xmm0;
loc_002FD6E4:
    goto loc_002FD70E;
loc_002FD70E:
    result = (uint32_t)(((uint32_t)(v_stack_m1B8)) | (v_stack_p20));
    *(uint32_t *)(result) = (uint32_t)(result);
    *(uint64_t *)(result + 0x10) = v_stack_m180;
    *(uint32_t *)(result + 0x28) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x28C)));
    *(uint32_t *)(result + 0x2C) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x2DC)));
    *(uint32_t *)(result + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x510)));
    *(uint32_t *)(result + 0xC) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x508)));
    if (((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x340) + 0x2C8) + Arg1 * 8) + 0xC)) & (0x80000ULL)) != 0) goto loc_002FD881;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x340) + 0x2C8) + Arg1 * 8) + 0x620)) != 0) goto loc_002FD8A0;
loc_002FD772:
loc_002FD780:
    Arg1 = (v_stack_m178) ^ (*(uint64_t *)(v_stack_m170));
    if (Arg1 >= 15) goto loc_002FD865;
    if (Arg1 != 15) goto loc_002FD780;
loc_002FD7AB:
    result = *(uint64_t *)(v_stack_m170);
    if (1 != 0) {
        result = v_stack_m1A0;
        Arg1 = *(uint64_t *)(v_stack_m198 + 0x2C0);
        Arg2 = 1;
        Arg1 = *(uint64_t *)(Arg1 + result * 8);
        result = ExReleaseRundownProtectionCacheAwareEx(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp + result * 8 + 0xB8)))), v_stack_m180);
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x188));
        result = KeLeaveCriticalRegionThread(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp + result * 8 + 0xB8)))), v_stack_m180);
    }
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp + result * 8 + 0xB8)))), v_stack_m180);
    local_rsp = (local_rsp) + (448);
    return result;
loc_002FD7FE:
    if (((uint32_t)(v_stack_m198)) > 0xFFF8ULL) goto loc_002FD86E;
    result = (uint32_t)(0xC0000017ULL);
    if (((uint32_t)(v_stack_m198)) > (*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x340) + 0x2C8) + Arg1 * 8) + 0x8))) { result = (uint32_t)((uint32_t)(0x80000005ULL)); }
    v_stack_p34 = (uint32_t)(result);
    goto loc_002FD7AB;
loc_002FD822:
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp + result * 8 + 0xB8)))), v_stack_m180);
    goto loc_002FD3CB;
loc_002FD835:
    v_stack_p34 = 0xC0000022ULL;
    goto loc_002FD7AB;
loc_002FD842:
    goto loc_002FD326;
loc_002FD84E:
    if (((uint32_t)(v_stack_m198)) >= (*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x340) + 0x2C8) + Arg1 * 8) + 0x8))) goto loc_002FD3FA;
    v_stack_p34 = 0xC00000BBULL;
    goto loc_002FD7AB;
loc_002FD865:
    goto loc_002FD7AB;
loc_002FD86E:
    v_stack_p34 = (uint32_t)((uint32_t)(0xC0000095ULL));
    goto loc_002FD7AB;
loc_002FD881:
loc_002FD8A0:
    result = EtwpInvokeEventCallback(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x340) + 0x2C8) + Arg1 * 8), v_stack_p80, result + 24, (uint8_t)(v_stack_m1C8));
    goto loc_002FD772;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002FD290&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
