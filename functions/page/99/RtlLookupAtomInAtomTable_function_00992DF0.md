# RtlLookupAtomInAtomTable

- RVA: `0x00992DF0`–`0x009933AA` (길이 `1,466` bytes)
- VA: `0x0000000140992DF0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00098EA0`
- 디코드: `338`개 명령, `1,466/1,466` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **21**; 고유 호출 대상: **13**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00992E56` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00992E72` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x00992EFE` → [RtlUnicodeStringToInteger](RtlUnicodeStringToInteger_function_00993480.md) (function, `0x00993480`)
- `0x00992FCE` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (function, `0x00500080`)
- `0x00992FEA` → [RtlpLookupOrCreateLowBox](../../text/43/RtlpLookupOrCreateLowBox_function_00438940.md) (function, `0x00438940`)
- `0x00993073` → [ExpLookupHandleTableEntry](../86/ExpLookupHandleTableEntry_function_00869DB0.md) (function, `0x00869DB0`)
- `0x009930B3` → [ExGetHandlePointer](../../text/43/ExGetHandlePointer_function_00430C90.md) (function, `0x00430C90`)
- `0x009930D4` → [ExfUnblockPushLock](../../text/2A/ExfUnblockPushLock_function_002A3FE0.md) (function, `0x002A3FE0`)
- `0x009930EA` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x00993137` → [ExpBlockOnLockedHandleEntry](../86/ExpBlockOnLockedHandleEntry_function_00868838.md) (function, `0x00868838`)
- `0x009931AE` → [ExpLookupHandleTableEntry](../86/ExpLookupHandleTableEntry_function_00869DB0.md) (function, `0x00869DB0`)
- `0x009931F9` → [ExGetHandlePointer](../../text/43/ExGetHandlePointer_function_00430C90.md) (function, `0x00430C90`)
- `0x0099321A` → [ExfUnblockPushLock](../../text/2A/ExfUnblockPushLock_function_002A3FE0.md) (function, `0x002A3FE0`)
- `0x00993230` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x0099324E` → [ExpBlockOnLockedHandleEntry](../86/ExpBlockOnLockedHandleEntry_function_00868838.md) (function, `0x00868838`)
- `0x00993258` → [RtlUpcaseUnicodeChar](../85/RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)
- `0x0099328F` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x009932E8` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x00993363` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00993371` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x009933A3` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)

### Direct callers
- [NtFindAtom](../AF/NtFindAtom_function_00AF7560.md) at `0x00AF76A1`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **15**
  - `0x00992E56` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x00992E72` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x00992FCE` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (`PAGE` → `.text`)
  - `0x00992FEA` → [RtlpLookupOrCreateLowBox](../../text/43/RtlpLookupOrCreateLowBox_function_00438940.md) (`PAGE` → `.text`)
  - `0x009930B3` → [ExGetHandlePointer](../../text/43/ExGetHandlePointer_function_00430C90.md) (`PAGE` → `.text`)
  - `0x009930D4` → [ExfUnblockPushLock](../../text/2A/ExfUnblockPushLock_function_002A3FE0.md) (`PAGE` → `.text`)
  - `0x009930EA` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x009931F9` → [ExGetHandlePointer](../../text/43/ExGetHandlePointer_function_00430C90.md) (`PAGE` → `.text`)
  - `0x0099321A` → [ExfUnblockPushLock](../../text/2A/ExfUnblockPushLock_function_002A3FE0.md) (`PAGE` → `.text`)
  - `0x00993230` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x0099328F` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x009932E8` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x00993363` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00993371` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x009933A3` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00992DF0  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00992DF5  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
00992DFA  57                              push rdi
00992DFB  41 54                           push r12
00992DFD  41 55                           push r13
00992DFF  41 56                           push r14
00992E01  41 57                           push r15
00992E03  48 81 EC C0 00 00 00            sub rsp, 0xc0
00992E0A  4D 8B F8                        mov r15, r8
00992E0D  48 8B F2                        mov rsi, rdx
00992E10  4C 8B F1                        mov r14, rcx
00992E13  48 89 8C 24 88 00 00 00         mov qword ptr [rsp + 0x88], rcx
00992E1B  45 33 ED                        xor r13d, r13d
00992E1E  66 44 89 AC 24 F0 00 00 00      mov word ptr [rsp + 0xf0], r13w
00992E27  48 85 C9                        test rcx, rcx
00992E2A  0F 84 68 05 00 00               je 0x140993398
00992E30  81 39 41 74 6F 6D               cmp dword ptr [rcx], 0x6d6f7441
00992E36  0F 85 5C 05 00 00               jne 0x140993398
00992E3C  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00992E45  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00992E4C  90                              nop
00992E4D  45 33 C0                        xor r8d, r8d
00992E50  33 D2                           xor edx, edx
00992E52  48 83 C1 08                     add rcx, 8
00992E56  E8 D5 D3 87 FF                  call 0x140210230
00992E5B  48 8B D8                        mov rbx, rax
00992E5E  F0 49 0F BA 6E 08 00            lock bts qword ptr [r14 + 8], 0
00992E65  73 10                           jae 0x140992e77
00992E67  4D 8D 46 08                     lea r8, [r14 + 8]
00992E6B  48 8B D0                        mov rdx, rax
00992E6E  49 8D 4E 08                     lea rcx, [r14 + 8]
00992E72  E8 19 CE 87 FF                  call 0x14020fc90
00992E77  48 85 DB                        test rbx, rbx
00992E7A  74 04                           je 0x140992e80
00992E7C  C6 43 0A 01                     mov byte ptr [rbx + 0xa], 1
00992E80  48 8D 9C 24 F0 00 00 00         lea rbx, [rsp + 0xf0]
00992E88  48 89 74 24 68                  mov qword ptr [rsp + 0x68], rsi
00992E8D  0F 57 C0                        xorps xmm0, xmm0
00992E90  0F 11 44 24 58                  movups xmmword ptr [rsp + 0x58], xmm0
00992E95  4C 89 6C 24 40                  mov qword ptr [rsp + 0x40], r13
00992E9A  44 89 AC 24 08 01 00 00         mov dword ptr [rsp + 0x108], r13d
00992EA2  48 F7 C6 00 00 FF FF            test rsi, -0x10000
00992EA9  0F 84 67 04 00 00               je 0x140993316
00992EAF  66 83 3E 23                     cmp word ptr [rsi], 0x23
00992EB3  75 56                           jne 0x140992f0b
00992EB5  48 8D 4E 02                     lea rcx, [rsi + 2]
00992EB9  48 89 4C 24 68                  mov qword ptr [rsp + 0x68], rcx
00992EBE  48 8B C1                        mov rax, rcx
00992EC1  48 89 4C 24 40                  mov qword ptr [rsp + 0x40], rcx
00992EC6  0F B7 10                        movzx edx, word ptr [rax]
00992EC9  66 85 D2                        test dx, dx
00992ECC  0F 85 90 03 00 00               jne 0x140993262
00992ED2  44 89 AC 24 08 01 00 00         mov dword ptr [rsp + 0x108], r13d
00992EDA  48 89 4C 24 60                  mov qword ptr [rsp + 0x60], rcx
00992EDF  66 2B C1                        sub ax, cx
00992EE2  66 89 44 24 58                  mov word ptr [rsp + 0x58], ax
00992EE7  66 89 44 24 5A                  mov word ptr [rsp + 0x5a], ax
00992EEC  4C 8D 84 24 08 01 00 00         lea r8, [rsp + 0x108]
00992EF4  BA 0A 00 00 00                  mov edx, 0xa
00992EF9  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
00992EFE  E8 7D 05 00 00                  call 0x140993480
00992F03  85 C0                           test eax, eax
00992F05  0F 89 96 03 00 00               jns 0x1409932a1
00992F0B  B8 00 C0 00 00                  mov eax, 0xc000
00992F10  66 83 3E 00                     cmp word ptr [rsi], 0
00992F14  0F 84 1C 04 00 00               je 0x140993336
00992F1A  4C 8D 64 24 50                  lea r12, [rsp + 0x50]
00992F1F  44 89 6C 24 24                  mov dword ptr [rsp + 0x24], r13d
00992F24  4C 89 6C 24 48                  mov qword ptr [rsp + 0x48], r13
00992F29  4C 89 6C 24 28                  mov qword ptr [rsp + 0x28], r13
00992F2E  48 F7 C6 00 00 FF FF            test rsi, -0x10000
00992F35  0F 84 06 02 00 00               je 0x140993141
00992F3B  48 8B DE                        mov rbx, rsi
00992F3E  48 89 5C 24 48                  mov qword ptr [rsp + 0x48], rbx
00992F43  41 8B FD                        mov edi, r13d
00992F46  44 89 6C 24 24                  mov dword ptr [rsp + 0x24], r13d
00992F4B  41 BC E0 FF 00 00               mov r12d, 0xffe0
00992F51  0F B7 03                        movzx eax, word ptr [rbx]
00992F54  66 85 C0                        test ax, ax
00992F57  74 31                           je 0x140992f8a
00992F59  48 83 C3 02                     add rbx, 2
00992F5D  48 89 5C 24 48                  mov qword ptr [rsp + 0x48], rbx
00992F62  66 83 F8 61                     cmp ax, 0x61
00992F66  72 0E                           jb 0x140992f76
00992F68  66 83 F8 7A                     cmp ax, 0x7a
00992F6C  0F 87 E3 02 00 00               ja 0x140993255
00992F72  66 41 03 C4                     add ax, r12w
00992F76  0F B7 C8                        movzx ecx, ax
00992F79  8B C1                           mov eax, ecx
00992F7B  D1 E8                           shr eax, 1
00992F7D  03 C1                           add eax, ecx
00992F7F  8D 0C 48                        lea ecx, [rax + rcx*2]
00992F82  03 F9                           add edi, ecx
00992F84  89 7C 24 24                     mov dword ptr [rsp + 0x24], edi
00992F88  EB C7                           jmp 0x140992f51
00992F8A  48 2B DE                        sub rbx, rsi
00992F8D  48 D1 FB                        sar rbx, 1
00992F90  81 FB FF 00 00 00               cmp ebx, 0xff
00992F96  0F 87 7F 01 00 00               ja 0x14099311b
00992F9C  33 D2                           xor edx, edx
00992F9E  8B C7                           mov eax, edi
00992FA0  41 F7 76 1C                     div dword ptr [r14 + 0x1c]
00992FA4  8B FA                           mov edi, edx
00992FA6  48 83 C7 04                     add rdi, 4
00992FAA  49 8D 3C FE                     lea rdi, [r14 + rdi*8]
00992FAE  66 90                           nop
00992FB0  48 8B 3F                        mov rdi, qword ptr [rdi]
00992FB3  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
00992FB8  48 85 FF                        test rdi, rdi
00992FBB  74 1A                           je 0x140992fd7
00992FBD  0F B6 47 28                     movzx eax, byte ptr [rdi + 0x28]
00992FC1  3B C3                           cmp eax, ebx
00992FC3  74 02                           je 0x140992fc7
00992FC5  EB E9                           jmp 0x140992fb0
00992FC7  48 8D 4F 2A                     lea rcx, [rdi + 0x2a]
00992FCB  48 8B D6                        mov rdx, rsi
00992FCE  E8 AD D0 B6 FF                  call 0x140500080
00992FD3  85 C0                           test eax, eax
00992FD5  75 EE                           jne 0x140992fc5
00992FD7  4C 8D 64 24 50                  lea r12, [rsp + 0x50]
00992FDC  48 85 FF                        test rdi, rdi
00992FDF  74 1B                           je 0x140992ffc
00992FE1  41 B0 01                        mov r8b, 1
00992FE4  48 8B D7                        mov rdx, rdi
00992FE7  49 8B CE                        mov rcx, r14
00992FEA  E8 51 59 AA FF                  call 0x140438940
00992FEF  48 85 C0                        test rax, rax
00992FF2  0F 84 E4 01 00 00               je 0x1409931dc
00992FF8  49 89 04 24                     mov qword ptr [r12], rax
00992FFC  48 89 BC 24 80 00 00 00         mov qword ptr [rsp + 0x80], rdi
00993004  44 89 6C 24 20                  mov dword ptr [rsp + 0x20], r13d
00993009  48 85 FF                        test rdi, rdi
0099300C  0F 84 D7 01 00 00               je 0x1409931e9
00993012  0F B7 47 08                     movzx eax, word ptr [rdi + 8]
00993016  4C 89 6C 24 38                  mov qword ptr [rsp + 0x38], r13
0099301B  4C 89 6C 24 38                  mov qword ptr [rsp + 0x38], r13
00993020  44 8D 04 85 00 00 00 00         lea r8d, [rax*4]
00993028  44 89 44 24 38                  mov dword ptr [rsp + 0x38], r8d
0099302D  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00993036  48 89 8C 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rcx
0099303E  0F B7 81 E4 01 00 00            movzx eax, word ptr [rcx + 0x1e4]
00993045  66 FF C8                        dec ax
00993048  66 89 81 E4 01 00 00            mov word ptr [rcx + 0x1e4], ax
0099304F  90                              nop
00993050  49 8B 7E 10                     mov rdi, qword ptr [r14 + 0x10]
00993054  4C 89 6C 24 78                  mov qword ptr [rsp + 0x78], r13
00993059  48 8B 54 24 38                  mov rdx, qword ptr [rsp + 0x38]
0099305E  48 89 54 24 78                  mov qword ptr [rsp + 0x78], rdx
00993063  41 F7 C0 FC 03 00 00            test r8d, 0x3fc
0099306A  0F 84 0E 02 00 00               je 0x14099327e
00993070  48 8B CF                        mov rcx, rdi
00993073  E8 38 6D ED FF                  call 0x140869db0
00993078  48 8B D8                        mov rbx, rax
0099307B  48 85 C0                        test rax, rax
0099307E  0F 84 FA 01 00 00               je 0x14099327e
00993084  0F 1F 40 00                     nop dword ptr [rax]
00993088  0F 1F 84 00 00 00 00 00         nop dword ptr [rax + rax]
00993090  0F 0D 0B                        prefetchw byte ptr [rbx]
00993093  4C 8B 03                        mov r8, qword ptr [rbx]
00993096  41 F6 C0 01                     test r8b, 1
0099309A  0F 84 88 00 00 00               je 0x140993128
009930A0  49 8D 48 FF                     lea rcx, [r8 - 1]
009930A4  49 8B C0                        mov rax, r8
009930A7  F0 48 0F B1 0B                  lock cmpxchg qword ptr [rbx], rcx
009930AC  74 02                           je 0x1409930b0
009930AE  EB E0                           jmp 0x140993090
009930B0  48 8B CB                        mov rcx, rbx
009930B3  E8 D8 DB A9 FF                  call 0x140430c90
009930B8  48 8B F8                        mov rdi, rax
009930BB  49 8B 4E 10                     mov rcx, qword ptr [r14 + 0x10]
009930BF  F0 48 FF 03                     lock inc qword ptr [rbx]
009930C3  48 83 C1 30                     add rcx, 0x30
009930C7  F0 83 0C 24 00                  lock or dword ptr [rsp], 0
009930CC  48 83 39 00                     cmp qword ptr [rcx], 0
009930D0  74 07                           je 0x1409930d9
009930D2  33 D2                           xor edx, edx
009930D4  E8 07 0F 91 FF                  call 0x1402a3fe0
009930D9  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
009930E2  48 89 8C 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rcx
009930EA  E8 01 BF 8C FF                  call 0x14025eff0
009930EF  48 85 FF                        test rdi, rdi
009930F2  0F 84 9C 01 00 00               je 0x140993294
009930F8  44 89 6C 24 20                  mov dword ptr [rsp + 0x20], r13d
009930FD  4D 85 FF                        test r15, r15
00993100  0F 84 38 02 00 00               je 0x14099333e
00993106  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
0099310E  0F B7 48 0A                     movzx ecx, word ptr [rax + 0xa]
00993112  66 41 89 0F                     mov word ptr [r15], cx
00993116  E9 23 02 00 00                  jmp 0x14099333e
0099311B  49 8B FD                        mov rdi, r13
0099311E  4C 89 6C 24 28                  mov qword ptr [rsp + 0x28], r13
00993123  E9 D4 FE FF FF                  jmp 0x140992ffc
00993128  4D 85 C0                        test r8, r8
0099312B  0F 84 4D 01 00 00               je 0x14099327e
00993131  48 8B D3                        mov rdx, rbx
00993134  48 8B CF                        mov rcx, rdi
00993137  E8 FC 56 ED FF                  call 0x140868838
0099313C  E9 6D FF FF FF                  jmp 0x1409930ae
00993141  49 8B FD                        mov rdi, r13
00993144  4C 89 6C 24 28                  mov qword ptr [rsp + 0x28], r13
00993149  66 3B F0                        cmp si, ax
0099314C  0F 82 8A FE FF FF               jb 0x140992fdc
00993152  4C 89 6C 24 30                  mov qword ptr [rsp + 0x30], r13
00993157  4C 89 6C 24 30                  mov qword ptr [rsp + 0x30], r13
0099315C  81 E6 FF 3F 00 00               and esi, 0x3fff
00993162  C1 E6 02                        shl esi, 2
00993165  89 74 24 30                     mov dword ptr [rsp + 0x30], esi
00993169  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00993172  48 89 8C 24 90 00 00 00         mov qword ptr [rsp + 0x90], rcx
0099317A  0F B7 81 E4 01 00 00            movzx eax, word ptr [rcx + 0x1e4]
00993181  66 FF C8                        dec ax
00993184  66 89 81 E4 01 00 00            mov word ptr [rcx + 0x1e4], ax
0099318B  90                              nop
0099318C  49 8B 7E 10                     mov rdi, qword ptr [r14 + 0x10]
00993190  4C 89 6C 24 70                  mov qword ptr [rsp + 0x70], r13
00993195  48 8B 54 24 30                  mov rdx, qword ptr [rsp + 0x30]
0099319A  48 89 54 24 70                  mov qword ptr [rsp + 0x70], rdx
0099319F  F7 C6 FC 03 00 00               test esi, 0x3fc
009931A5  0F 84 2C 01 00 00               je 0x1409932d7
009931AB  48 8B CF                        mov rcx, rdi
009931AE  E8 FD 6B ED FF                  call 0x140869db0
009931B3  48 8B D8                        mov rbx, rax
009931B6  48 85 C0                        test rax, rax
009931B9  0F 84 18 01 00 00               je 0x1409932d7
009931BF  90                              nop
009931C0  0F 0D 0B                        prefetchw byte ptr [rbx]
009931C3  4C 8B 03                        mov r8, qword ptr [rbx]
009931C6  41 F6 C0 01                     test r8b, 1
009931CA  74 73                           je 0x14099323f
009931CC  49 8D 48 FF                     lea rcx, [r8 - 1]
009931D0  49 8B C0                        mov rax, r8
009931D3  F0 48 0F B1 0B                  lock cmpxchg qword ptr [rbx], rcx
009931D8  74 1C                           je 0x1409931f6
009931DA  EB E4                           jmp 0x1409931c0
009931DC  C7 44 24 20 17 00 00 C0         mov dword ptr [rsp + 0x20], 0xc0000017
009931E4  E9 55 01 00 00                  jmp 0x14099333e
009931E9  C7 44 24 20 34 00 00 C0         mov dword ptr [rsp + 0x20], 0xc0000034
009931F1  E9 48 01 00 00                  jmp 0x14099333e
009931F6  48 8B CB                        mov rcx, rbx
009931F9  E8 92 DA A9 FF                  call 0x140430c90
009931FE  48 8B F8                        mov rdi, rax
00993201  49 8B 4E 10                     mov rcx, qword ptr [r14 + 0x10]
00993205  F0 48 FF 03                     lock inc qword ptr [rbx]
00993209  48 83 C1 30                     add rcx, 0x30
0099320D  F0 83 0C 24 00                  lock or dword ptr [rsp], 0
00993212  48 83 39 00                     cmp qword ptr [rcx], 0
00993216  74 07                           je 0x14099321f
00993218  33 D2                           xor edx, edx
0099321A  E8 C1 0D 91 FF                  call 0x1402a3fe0
0099321F  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00993228  48 89 8C 24 98 00 00 00         mov qword ptr [rsp + 0x98], rcx
00993230  E8 BB BD 8C FF                  call 0x14025eff0
00993235  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
0099323A  E9 9D FD FF FF                  jmp 0x140992fdc
0099323F  4D 85 C0                        test r8, r8
00993242  0F 84 8F 00 00 00               je 0x1409932d7
00993248  48 8B D3                        mov rdx, rbx
0099324B  48 8B CF                        mov rcx, rdi
0099324E  E8 E5 55 ED FF                  call 0x140868838
00993253  EB 85                           jmp 0x1409931da
00993255  0F B7 C8                        movzx ecx, ax
00993258  E8 93 BE EC FF                  call 0x14085f0f0
0099325D  E9 14 FD FF FF                  jmp 0x140992f76
00993262  66 83 EA 30                     sub dx, 0x30
00993266  66 83 FA 09                     cmp dx, 9
0099326A  0F 87 9B FC FF FF               ja 0x140992f0b
00993270  48 83 C0 02                     add rax, 2
00993274  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00993279  E9 48 FC FF FF                  jmp 0x140992ec6
0099327E  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00993287  48 89 8C 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rcx
0099328F  E8 5C BD 8C FF                  call 0x14025eff0
00993294  C7 44 24 20 08 00 00 C0         mov dword ptr [rsp + 0x20], 0xc0000008
0099329C  E9 9D 00 00 00                  jmp 0x14099333e
009932A1  8B 8C 24 08 01 00 00            mov ecx, dword ptr [rsp + 0x108]
009932A8  8D 41 FF                        lea eax, [rcx - 1]
009932AB  3D FF BF 00 00                  cmp eax, 0xbfff
009932B0  B8 00 C0 00 00                  mov eax, 0xc000
009932B5  77 43                           ja 0x1409932fa
009932B7  66 89 0B                        mov word ptr [rbx], cx
009932BA  0F B7 B4 24 F0 00 00 00         movzx esi, word ptr [rsp + 0xf0]
009932C2  66 3B F0                        cmp si, ax
009932C5  73 38                           jae 0x1409932ff
009932C7  44 89 6C 24 20                  mov dword ptr [rsp + 0x20], r13d
009932CC  4D 85 FF                        test r15, r15
009932CF  74 6D                           je 0x14099333e
009932D1  66 41 89 37                     mov word ptr [r15], si
009932D5  EB 67                           jmp 0x14099333e
009932D7  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
009932E0  48 89 8C 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rcx
009932E8  E8 03 BD 8C FF                  call 0x14025eff0
009932ED  49 8B FD                        mov rdi, r13
009932F0  4C 89 6C 24 28                  mov qword ptr [rsp + 0x28], r13
009932F5  E9 02 FD FF FF                  jmp 0x140992ffc
009932FA  66 89 03                        mov word ptr [rbx], ax
009932FD  EB BB                           jmp 0x1409932ba
009932FF  41 0F B7 F5                     movzx esi, r13w
00993303  66 44 89 AC 24 F0 00 00 00      mov word ptr [rsp + 0xf0], r13w
0099330C  C7 44 24 20 0D 00 00 C0         mov dword ptr [rsp + 0x20], 0xc000000d
00993314  EB B6                           jmp 0x1409932cc
00993316  B8 00 C0 00 00                  mov eax, 0xc000
0099331B  66 3B F0                        cmp si, ax
0099331E  0F 83 EC FB FF FF               jae 0x140992f10
00993324  66 85 F6                        test si, si
00993327  75 03                           jne 0x14099332c
00993329  0F B7 F0                        movzx esi, ax
0099332C  66 89 B4 24 F0 00 00 00         mov word ptr [rsp + 0xf0], si
00993334  EB 8C                           jmp 0x1409932c2
00993336  C7 44 24 20 33 00 00 C0         mov dword ptr [rsp + 0x20], 0xc0000033
0099333E  EB 0C                           jmp 0x14099334c
00993340  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00993344  4C 8B B4 24 88 00 00 00         mov r14, qword ptr [rsp + 0x88]
0099334C  48 C7 C0 FF FF FF FF            mov rax, 0xffffffffffffffff
00993353  F0 49 0F C1 46 08               lock xadd qword ptr [r14 + 8], rax
00993359  24 06                           and al, 6
0099335B  3C 02                           cmp al, 2
0099335D  74 40                           je 0x14099339f
0099335F  49 8D 4E 08                     lea rcx, [r14 + 8]
00993363  E8 98 E2 94 FF                  call 0x1402e1600
00993368  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00993371  E8 7A BC 8C FF                  call 0x14025eff0
00993376  8B 44 24 20                     mov eax, dword ptr [rsp + 0x20]
0099337A  4C 8D 9C 24 C0 00 00 00         lea r11, [rsp + 0xc0]
00993382  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
00993386  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
0099338A  49 8B E3                        mov rsp, r11
0099338D  41 5F                           pop r15
0099338F  41 5E                           pop r14
00993391  41 5D                           pop r13
00993393  41 5C                           pop r12
00993395  5F                              pop rdi
00993396  C3                              ret
00993397  CC                              int3
00993398  B8 0D 00 00 C0                  mov eax, 0xc000000d
0099339D  EB DB                           jmp 0x14099337a
0099339F  49 8D 4E 08                     lea rcx, [r14 + 8]
009933A3  E8 28 2A 8D FF                  call 0x140265dd0
009933A8  EB B5                           jmp 0x14099335f
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlLookupAtomInAtomTable(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
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
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int16 v_stack_m8E;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned int v_stack_mC4;
    unsigned int v_stack_mC8;
    unsigned int v_stack_mE8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int16 v_stack_p8;

    v_stack_p10 = v_rbx;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (192);
    v_stack_m60 = a1;
    v_r13 = 0;
    v_stack_p8 = 0;
    if (a1 == 0) goto loc_00993398;
    if ((*(unsigned int *)(a1)) != 0x6D6F7441ULL) goto loc_00993398;
    a3 = 0;
    a2 = 0;
    a1 = (a1) + (8);
    result = KeAbPreAcquire(a1, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = a1 + 8;
        a2 = result;
        a1 = a1 + 8;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    v_stack_m80 = a2;
    v_stack_m90 = v_xmm0;
    v_stack_mA8 = 0;
    v_stack_p20 = 0;
    if (((a2) & (0xFFFFFFFFFFFF0000ULL)) == 0) goto loc_00993316;
    if ((*(unsigned __int16 *)(a2)) != 35) goto loc_00992F0B;
    v_stack_m80 = a2 + 2;
    v_stack_mA8 = a2 + 2;
loc_00992EC6:
    if ((unsigned __int16)(*(unsigned __int16 *)(a2 + 2)) != 0) goto loc_00993262;
    v_stack_p20 = 0;
    v_stack_m88 = a2 + 2;
    result = (unsigned __int16)((a2 + 2) - ((unsigned __int16)(a2 + 2)));
    v_stack_m90 = (unsigned __int16)(result);
    v_stack_m8E = (unsigned __int16)(result);
    result = RtlUnicodeStringToInteger(v_stack_m90, 10, v_stack_p20, a4);
    if (!sign_flag) goto loc_009932A1;
loc_00992F0B:
loc_00992F10:
    if ((*(unsigned __int16 *)(a2)) == 0) goto loc_00993336;
    v_stack_mC4 = 0;
    v_stack_mA0 = 0;
    v_stack_mC0 = 0;
    if (((a2) & (0xFFFFFFFFFFFF0000ULL)) == 0) goto loc_00993141;
    v_stack_mA0 = a2;
    v_stack_mC4 = 0;
loc_00992F51:
    if ((unsigned __int16)(*(unsigned __int16 *)(a2)) == 0) goto loc_00992F8A;
    v_rbx = (a2) + (2);
    v_stack_mA0 = v_rbx;
    if (((unsigned __int16)(*(unsigned __int16 *)(a2))) < 97) goto loc_00992F76;
    if (((unsigned __int16)(*(unsigned __int16 *)(a2))) > 122) goto loc_00993255;
    result = (unsigned __int16)((*(unsigned __int16 *)(a2)) + ((unsigned __int16)((unsigned int)(0xFFE0ULL))));
loc_00992F76:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned __int16)(result)))) >> (1));
    result = (unsigned int)((result) + ((unsigned int)((unsigned __int16)(result))));
    v_rdi = (unsigned int)((0) + ((unsigned int)(result + (unsigned __int16)(result) * 2)));
    v_stack_mC4 = (unsigned int)(v_rdi);
    goto loc_00992F51;
loc_00992F8A:
    v_rbx = (v_rbx) - (a2);
    v_rbx = (v_rbx) >> (1);
    if (((unsigned int)(v_rbx)) > 255) goto loc_0099311B;
    a2 = 0;
    v_rdi = (0) + (4);
loc_00992FB0:
    v_stack_mC0 = *(unsigned __int64 *)(a1 + v_rdi * 8);
    if (*(unsigned __int64 *)(a1 + v_rdi * 8) == 0) goto loc_00992FD7;
    if (((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + v_rdi * 8) + 40))) == ((unsigned int)(v_rbx))) goto loc_00992FC7;
loc_00992FC5:
    goto loc_00992FB0;
loc_00992FC7:
    result = wcsicmp(*(unsigned __int64 *)(a1 + v_rdi * 8) + 42, 0, v_stack_p20, a4);
    if ((unsigned int)(result) != 0) goto loc_00992FC5;
loc_00992FD7:
loc_00992FDC:
    if (*(unsigned __int64 *)(a1 + v_rdi * 8) == 0) goto loc_00992FFC;
    result = RtlpLookupOrCreateLowBox(a1, *(unsigned __int64 *)(a1 + v_rdi * 8), 1, a4);
    if (result == 0) goto loc_009931DC;
    *(unsigned __int64 *)(v_stack_m98) = result;
loc_00992FFC:
    v_stack_m68 = *(unsigned __int64 *)(a1 + v_rdi * 8);
    v_stack_mC8 = 0;
    if (*(unsigned __int64 *)(a1 + v_rdi * 8) == 0) goto loc_009931E9;
    v_stack_mB0 = 0;
    v_stack_mB0 = 0;
    v_stack_mB0 = (unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + v_rdi * 8) + 8) * 4);
    v_stack_m40 = *(unsigned __int64 *)(gs_base + (0 + 392));
    result = (unsigned __int16)((*(unsigned __int16 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 484)) - 1);
    *(unsigned __int16 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 484) = (unsigned __int16)(result);
    v_stack_m70 = 0;
    v_stack_m70 = v_stack_mB0;
    if ((((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + v_rdi * 8) + 8) * 4)) & (0x3FCULL)) == 0) goto loc_0099327E;
    result = ExpLookupHandleTableEntry(*(unsigned __int64 *)(a1 + 16), v_stack_mB0, *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + v_rdi * 8) + 8) * 4, a4);
    if (result == 0) goto loc_0099327E;
loc_00993090:
    if ((((unsigned __int8)(*(unsigned __int64 *)(result))) & (1)) == 0) goto loc_00993128;
    if ((((unsigned __int8)(*(unsigned __int64 *)(result))) & (1)) == 0) goto loc_009930B0;
loc_009930AE:
    goto loc_00993090;
loc_009930B0:
    result = ExGetHandlePointer(result, v_stack_mB0, *(unsigned __int64 *)(result), a4);
    a1 = (*(unsigned __int64 *)(a1 + 16)) + (48);
    if ((*(unsigned __int64 *)(a1)) != 0) {
        a2 = 0;
        result = ExfUnblockPushLock(a1, a2, *(unsigned __int64 *)(result), a4);
    }
    v_stack_m38 = *(unsigned __int64 *)(gs_base + (0 + 392));
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, *(unsigned __int64 *)(result), a4);
    if (result == 0) goto loc_00993294;
    v_stack_mC8 = 0;
    if (a3 == 0) goto loc_0099333E;
    *(unsigned __int16 *)(a3) = (unsigned __int16)(*(unsigned __int16 *)(v_stack_m68 + 10));
    goto loc_0099333E;
loc_0099311B:
    v_stack_mC0 = 0;
    goto loc_00992FFC;
loc_00993128:
    if (*(unsigned __int64 *)(result) == 0) goto loc_0099327E;
    result = ExpBlockOnLockedHandleEntry(0, result, *(unsigned __int64 *)(result), a4);
    goto loc_009930AE;
loc_00993141:
    v_stack_mC0 = 0;
    if (0 < ((unsigned __int16)(result))) goto loc_00992FDC;
    v_stack_mB8 = 0;
    v_stack_mB8 = 0;
    v_rsi = (unsigned int)((a2) & (0x3FFFULL));
    v_rsi = (unsigned int)((v_rsi) << (2));
    v_stack_mB8 = (unsigned int)(v_rsi);
    v_stack_m58 = *(unsigned __int64 *)(gs_base + (0 + 392));
    result = (unsigned __int16)((*(unsigned __int16 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 484)) - 1);
    *(unsigned __int16 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 484) = (unsigned __int16)(result);
    v_stack_m78 = 0;
    v_stack_m78 = v_stack_mB8;
    if ((((unsigned int)(v_rsi)) & (0x3FCULL)) == 0) goto loc_009932D7;
    result = ExpLookupHandleTableEntry(*(unsigned __int64 *)(a1 + 16), v_stack_mB8, *(unsigned __int64 *)(result), a4);
    if (result == 0) goto loc_009932D7;
loc_009931C0:
    if ((((unsigned __int8)(*(unsigned __int64 *)(result))) & (1)) == 0) goto loc_0099323F;
    if ((((unsigned __int8)(*(unsigned __int64 *)(result))) & (1)) == 0) goto loc_009931F6;
loc_009931DA:
    goto loc_009931C0;
loc_009931DC:
    v_stack_mC8 = 0xC0000017ULL;
    goto loc_0099333E;
loc_009931E9:
    v_stack_mC8 = 0xC0000034ULL;
    goto loc_0099333E;
loc_009931F6:
    result = ExGetHandlePointer(result, v_stack_mB8, *(unsigned __int64 *)(result), a4);
    a1 = (*(unsigned __int64 *)(a1 + 16)) + (48);
    if ((*(unsigned __int64 *)(a1)) != 0) {
        a2 = 0;
        result = ExfUnblockPushLock(a1, a2, *(unsigned __int64 *)(result), a4);
    }
    v_stack_m50 = *(unsigned __int64 *)(gs_base + (0 + 392));
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, *(unsigned __int64 *)(result), a4);
    v_stack_mC0 = result;
    goto loc_00992FDC;
loc_0099323F:
    if (*(unsigned __int64 *)(result) == 0) goto loc_009932D7;
    result = ExpBlockOnLockedHandleEntry(result, result, *(unsigned __int64 *)(result), a4);
    goto loc_009931DA;
loc_00993255:
    result = RtlUpcaseUnicodeChar((unsigned __int16)(result), result, *(unsigned __int64 *)(result), a4);
    goto loc_00992F76;
loc_00993262:
    a2 = (unsigned __int16)((result) - (48));
    if (((unsigned __int16)(a2)) > 9) goto loc_00992F0B;
    result = (result) + (2);
    v_stack_mA8 = result;
    goto loc_00992EC6;
loc_0099327E:
    v_stack_m30 = *(unsigned __int64 *)(gs_base + (0 + 392));
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, *(unsigned __int64 *)(result), a4);
loc_00993294:
    v_stack_mC8 = 0xC0000008ULL;
    goto loc_0099333E;
loc_009932A1:
    if (((unsigned int)((unsigned int)(v_stack_p20) - 1)) > 0xBFFFULL) goto loc_009932FA;
    *(unsigned __int16 *)(result) = (unsigned __int16)((unsigned int)(v_stack_p20));
loc_009932BA:
loc_009932C2:
    if (((unsigned __int16)(v_stack_p8)) >= ((unsigned __int16)((unsigned int)(0xC000ULL)))) goto loc_009932FF;
    v_stack_mC8 = 0;
loc_009932CC:
    if (a3 == 0) goto loc_0099333E;
    *(unsigned __int16 *)(a3) = (unsigned __int16)(v_stack_p8);
    goto loc_0099333E;
loc_009932D7:
    v_stack_m48 = *(unsigned __int64 *)(gs_base + (0 + 392));
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, *(unsigned __int64 *)(result), a4);
    v_stack_mC0 = 0;
    goto loc_00992FFC;
loc_009932FA:
    *(unsigned __int16 *)(result) = (unsigned __int16)(result);
    goto loc_009932BA;
loc_009932FF:
    v_stack_p8 = 0;
    v_stack_mC8 = 0xC000000DULL;
    goto loc_009932CC;
loc_00993316:
    if (0 >= ((unsigned __int16)((unsigned int)(0xC000ULL)))) goto loc_00992F10;
    v_rsi = 0;
    if (0 == 0) {
        v_rsi = (unsigned __int16)((unsigned int)(0xC000ULL));
    }
    v_stack_p8 = (unsigned __int16)(v_rsi);
    goto loc_009932C2;
loc_00993336:
    v_stack_mC8 = 0xC0000033ULL;
loc_0099333E:
    goto loc_0099334C;
loc_0099334C:
    result = (unsigned __int8)((-1) & (6));
    if (((unsigned __int8)(result)) == 2) goto loc_0099339F;
loc_0099335F:
    result = KeAbPostRelease(a1 + 8, a2, *(unsigned __int64 *)(result), a4);
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, *(unsigned __int64 *)(result), a4);
loc_0099337A:
    return (unsigned int)(v_stack_mC8);
loc_00993398:
    goto loc_0099337A;
loc_0099339F:
    result = ExfTryToWakePushLock(a1 + 8, a2, *(unsigned __int64 *)(result), a4);
    goto loc_0099335F;
}
```

## 5. (Beta) C Style

```c
int64_t RtlLookupAtomInAtomTable(void *Arg1, int64_t Arg2, int64_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r13;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
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
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint16_t v_stack_m8E;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint32_t v_stack_mC4;
    uint32_t v_stack_mC8;
    uint32_t v_stack_mE8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint32_t v_stack_p20;
    uint16_t v_stack_p8;

    v_stack_p10 = local_rbx;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (192);
    v_stack_m60 = Arg1;
    local_r13 = 0;
    v_stack_p8 = 0;
    if (Arg1 == NULL) goto loc_00993398;
    if ((*(uint32_t *)(arg1)) != 0x6D6F7441ULL) goto loc_00993398;
    Arg3 = 0;
    Arg2 = 0;
    Arg1 = (Arg1) + (8);
    result = KeAbPreAcquire(Arg1, Arg2, Arg3, a4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = Arg1 + 8;
        Arg2 = result;
        Arg1 = Arg1 + 8;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, a4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    v_stack_m80 = Arg2;
    v_stack_m90 = v_xmm0;
    v_stack_mA8 = 0;
    v_stack_p20 = 0;
    if (((Arg2) & (0xFFFFFFFFFFFF0000ULL)) == 0) goto loc_00993316;
    if ((*(uint16_t *)(Arg2)) != 35) goto loc_00992F0B;
    v_stack_m80 = Arg2 + 2;
    v_stack_mA8 = Arg2 + 2;
loc_00992EC6:
    if ((uint16_t)(*(uint16_t *)(Arg2 + 0x2)) != 0) goto loc_00993262;
    v_stack_p20 = 0;
    v_stack_m88 = Arg2 + 2;
    result = (uint16_t)((Arg2 + 2) - ((uint16_t)(Arg2 + 2)));
    v_stack_m90 = (uint16_t)(result);
    v_stack_m8E = (uint16_t)(result);
    result = RtlUnicodeStringToInteger(v_stack_m90, 10, v_stack_p20, a4);
    if (!sign_flag) goto loc_009932A1;
loc_00992F0B:
loc_00992F10:
    if ((*(uint16_t *)(Arg2)) == 0) goto loc_00993336;
    v_stack_mC4 = 0;
    v_stack_mA0 = 0;
    v_stack_mC0 = 0;
    if (((Arg2) & (0xFFFFFFFFFFFF0000ULL)) == 0) goto loc_00993141;
    v_stack_mA0 = Arg2;
    v_stack_mC4 = 0;
loc_00992F51:
    if ((uint16_t)(*(uint16_t *)(Arg2)) == 0) goto loc_00992F8A;
    local_rbx = (Arg2) + (2);
    v_stack_mA0 = local_rbx;
    if (((uint16_t)(*(uint16_t *)(Arg2))) < 97) goto loc_00992F76;
    if (((uint16_t)(*(uint16_t *)(Arg2))) > 122) goto loc_00993255;
    result = (uint16_t)((*(uint16_t *)(Arg2)) + ((uint16_t)((uint32_t)(0xFFE0ULL))));
loc_00992F76:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint16_t)(result)))) >> (1));
    result = (uint32_t)((result) + ((uint32_t)((uint16_t)(result))));
    local_rdi = (uint32_t)((0) + ((uint32_t)(result + (uint16_t)(result) * 2)));
    v_stack_mC4 = (uint32_t)(local_rdi);
    goto loc_00992F51;
loc_00992F8A:
    local_rbx = (local_rbx) - (Arg2);
    local_rbx = (local_rbx) >> (1);
    if (((uint32_t)(local_rbx)) > 255) goto loc_0099311B;
    Arg2 = 0;
    local_rdi = (0) + (4);
loc_00992FB0:
    v_stack_mC0 = *(uint64_t *)(arg1 + local_rdi * 8);
    if (*(uint64_t *)(arg1 + local_rdi * 8) == 0) goto loc_00992FD7;
    if (((uint32_t)(*(uint8_t *)(*(uint64_t *)(arg1 + local_rdi * 8) + 0x28))) == ((uint32_t)(local_rbx))) goto loc_00992FC7;
loc_00992FC5:
    goto loc_00992FB0;
loc_00992FC7:
    result = wcsicmp(*(uint64_t *)(arg1 + local_rdi * 8) + 42, 0, v_stack_p20, a4);
    if ((uint32_t)(result) != 0) goto loc_00992FC5;
loc_00992FD7:
loc_00992FDC:
    if (*(uint64_t *)(arg1 + local_rdi * 8) == 0) goto loc_00992FFC;
    result = RtlpLookupOrCreateLowBox(Arg1, *(uint64_t *)(arg1 + local_rdi * 8), 1, a4);
    if (result == 0) goto loc_009931DC;
    *(uint64_t *)(v_stack_m98) = result;
loc_00992FFC:
    v_stack_m68 = *(uint64_t *)(arg1 + local_rdi * 8);
    v_stack_mC8 = 0;
    if (*(uint64_t *)(arg1 + local_rdi * 8) == 0) goto loc_009931E9;
    v_stack_mB0 = 0;
    v_stack_mB0 = 0;
    v_stack_mB0 = (uint32_t)(*(uint16_t *)(*(uint64_t *)(arg1 + local_rdi * 8) + 0x8) * 4);
    v_stack_m40 = *(uint64_t *)(gs_base + (0 + 0x188));
    result = (uint16_t)((*(uint16_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x1E4)) - 1);
    *(uint16_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x1E4) = (uint16_t)(result);
    v_stack_m70 = 0;
    v_stack_m70 = v_stack_mB0;
    if ((((uint32_t)(*(uint16_t *)(*(uint64_t *)(arg1 + local_rdi * 8) + 0x8) * 4)) & (0x3FCULL)) == 0) goto loc_0099327E;
    result = ExpLookupHandleTableEntry(*(uint64_t *)(arg1 + 0x10), v_stack_mB0, *(uint16_t *)(*(uint64_t *)(arg1 + local_rdi * 8) + 0x8) * 4, a4);
    if (result == 0) goto loc_0099327E;
loc_00993090:
    if ((((uint8_t)(*(uint64_t *)(result))) & (1)) == 0) goto loc_00993128;
    if ((((uint8_t)(*(uint64_t *)(result))) & (1)) == 0) goto loc_009930B0;
loc_009930AE:
    goto loc_00993090;
loc_009930B0:
    result = ExGetHandlePointer(result, v_stack_mB0, *(uint64_t *)(result), a4);
    Arg1 = (*(uint64_t *)(arg1 + 0x10)) + (48);
    if ((*(uint64_t *)(arg1)) != 0) {
        Arg2 = 0;
        result = ExfUnblockPushLock(Arg1, Arg2, *(uint64_t *)(result), a4);
    }
    v_stack_m38 = *(uint64_t *)(gs_base + (0 + 0x188));
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, *(uint64_t *)(result), a4);
    if (result == 0) goto loc_00993294;
    v_stack_mC8 = 0;
    if (Arg3 == 0) goto loc_0099333E;
    *(uint16_t *)(Arg3) = (uint16_t)(*(uint16_t *)(v_stack_m68 + 0xA));
    goto loc_0099333E;
loc_0099311B:
    v_stack_mC0 = 0;
    goto loc_00992FFC;
loc_00993128:
    if (*(uint64_t *)(result) == 0) goto loc_0099327E;
    result = ExpBlockOnLockedHandleEntry(0, result, *(uint64_t *)(result), a4);
    goto loc_009930AE;
loc_00993141:
    v_stack_mC0 = 0;
    if (0 < ((uint16_t)(result))) goto loc_00992FDC;
    v_stack_mB8 = 0;
    v_stack_mB8 = 0;
    local_rsi = (uint32_t)((Arg2) & (0x3FFFULL));
    local_rsi = (uint32_t)((local_rsi) << (2));
    v_stack_mB8 = (uint32_t)(local_rsi);
    v_stack_m58 = *(uint64_t *)(gs_base + (0 + 0x188));
    result = (uint16_t)((*(uint16_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x1E4)) - 1);
    *(uint16_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x1E4) = (uint16_t)(result);
    v_stack_m78 = 0;
    v_stack_m78 = v_stack_mB8;
    if ((((uint32_t)(local_rsi)) & (0x3FCULL)) == 0) goto loc_009932D7;
    result = ExpLookupHandleTableEntry(*(uint64_t *)(arg1 + 0x10), v_stack_mB8, *(uint64_t *)(result), a4);
    if (result == 0) goto loc_009932D7;
loc_009931C0:
    if ((((uint8_t)(*(uint64_t *)(result))) & (1)) == 0) goto loc_0099323F;
    if ((((uint8_t)(*(uint64_t *)(result))) & (1)) == 0) goto loc_009931F6;
loc_009931DA:
    goto loc_009931C0;
loc_009931DC:
    v_stack_mC8 = 0xC0000017ULL;
    goto loc_0099333E;
loc_009931E9:
    v_stack_mC8 = 0xC0000034ULL;
    goto loc_0099333E;
loc_009931F6:
    result = ExGetHandlePointer(result, v_stack_mB8, *(uint64_t *)(result), a4);
    Arg1 = (*(uint64_t *)(arg1 + 0x10)) + (48);
    if ((*(uint64_t *)(arg1)) != 0) {
        Arg2 = 0;
        result = ExfUnblockPushLock(Arg1, Arg2, *(uint64_t *)(result), a4);
    }
    v_stack_m50 = *(uint64_t *)(gs_base + (0 + 0x188));
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, *(uint64_t *)(result), a4);
    v_stack_mC0 = result;
    goto loc_00992FDC;
loc_0099323F:
    if (*(uint64_t *)(result) == 0) goto loc_009932D7;
    result = ExpBlockOnLockedHandleEntry(result, result, *(uint64_t *)(result), a4);
    goto loc_009931DA;
loc_00993255:
    result = RtlUpcaseUnicodeChar((uint16_t)(result), result, *(uint64_t *)(result), a4);
    goto loc_00992F76;
loc_00993262:
    Arg2 = (uint16_t)((result) - (48));
    if (((uint16_t)(Arg2)) > 9) goto loc_00992F0B;
    result = (result) + (2);
    v_stack_mA8 = result;
    goto loc_00992EC6;
loc_0099327E:
    v_stack_m30 = *(uint64_t *)(gs_base + (0 + 0x188));
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, *(uint64_t *)(result), a4);
loc_00993294:
    v_stack_mC8 = 0xC0000008ULL;
    goto loc_0099333E;
loc_009932A1:
    if (((uint32_t)((uint32_t)(v_stack_p20) - 1)) > 0xBFFFULL) goto loc_009932FA;
    *(uint16_t *)(result) = (uint16_t)((uint32_t)(v_stack_p20));
loc_009932BA:
loc_009932C2:
    if (((uint16_t)(v_stack_p8)) >= ((uint16_t)((uint32_t)(0xC000ULL)))) goto loc_009932FF;
    v_stack_mC8 = 0;
loc_009932CC:
    if (Arg3 == 0) goto loc_0099333E;
    *(uint16_t *)(Arg3) = (uint16_t)(v_stack_p8);
    goto loc_0099333E;
loc_009932D7:
    v_stack_m48 = *(uint64_t *)(gs_base + (0 + 0x188));
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, *(uint64_t *)(result), a4);
    v_stack_mC0 = 0;
    goto loc_00992FFC;
loc_009932FA:
    *(uint16_t *)(result) = (uint16_t)(result);
    goto loc_009932BA;
loc_009932FF:
    v_stack_p8 = 0;
    v_stack_mC8 = 0xC000000DULL;
    goto loc_009932CC;
loc_00993316:
    if (0 >= ((uint16_t)((uint32_t)(0xC000ULL)))) goto loc_00992F10;
    local_rsi = 0;
    if (0 == 0) {
        local_rsi = (uint16_t)((uint32_t)(0xC000ULL));
    }
    v_stack_p8 = (uint16_t)(local_rsi);
    goto loc_009932C2;
loc_00993336:
    v_stack_mC8 = 0xC0000033ULL;
loc_0099333E:
    goto loc_0099334C;
loc_0099334C:
    result = (uint8_t)((-1) & (6));
    if (((uint8_t)(result)) == 2) goto loc_0099339F;
loc_0099335F:
    result = KeAbPostRelease(Arg1 + 8, Arg2, *(uint64_t *)(result), a4);
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, *(uint64_t *)(result), a4);
loc_0099337A:
    return (uint32_t)(v_stack_mC8);
loc_00993398:
    goto loc_0099337A;
loc_0099339F:
    result = ExfTryToWakePushLock(Arg1 + 8, Arg2, *(uint64_t *)(result), a4);
    goto loc_0099335F;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0 + rdi*8` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R/W` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x1C` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00992DF0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
