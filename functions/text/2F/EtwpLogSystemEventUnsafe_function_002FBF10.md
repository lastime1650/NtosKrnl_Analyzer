# EtwpLogSystemEventUnsafe

- RVA: `0x002FBF10`–`0x002FC8AC` (길이 `2,460` bytes)
- VA: `0x00000001402FBF10`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00072B04`
- 디코드: `537`개 명령, `2,460/2,460` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **23**; 고유 호출 대상: **20**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **11**

### Outgoing calls
- `0x002FC144` → [EtwpReserveTraceBuffer](EtwpReserveTraceBuffer_function_002FC8C0.md) (function, `0x002FC8C0`)
- `0x002FC20D` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x002FC2D1` → [KeIsTraceCallbackAllowed](KeIsTraceCallbackAllowed_function_002FCE6C.md) (function, `0x002FCE6C`)
- `0x002FC2F7` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x002FC388` → [ExReleaseRundownProtectionCacheAwareEx](../25/ExReleaseRundownProtectionCacheAwareEx_function_0025F050.md) (function, `0x0025F050`)
- `0x002FC396` → [KeLeaveCriticalRegionThread](../25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x002FC3A5` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x002FC419` → [EtwpLevelKeywordEnabled](EtwpLevelKeywordEnabled_function_002FD110.md) (function, `0x002FD110`)
- `0x002FC4F4` → [EtwWriteEx](../25/EtwWriteEx_function_0025F0D0.md) (function, `0x0025F0D0`)
- `0x002FC590` → [EtwpStackTraceDispatcher](EtwpStackTraceDispatcher_function_002FA4A0.md) (function, `0x002FA4A0`)
- `0x002FC61C` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x002FC624` → [EtwpUpdateEventsLostCount](../3F/EtwpUpdateEventsLostCount_function_003F18E0.md) (function, `0x003F18E0`)
- `0x002FC637` → [EtwEventEnabled](../39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x002FC656` → [EtwpTraceLostSystemEvent](../4C/EtwpTraceLostSystemEvent_function_004C37E4.md) (function, `0x004C37E4`)
- `0x002FC681` → [EtwpSendTraceEvent](../4B/EtwpSendTraceEvent_function_004B6E10.md) (function, `0x004B6E10`)
- `0x002FC727` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x002FC79F` → [KeGetCurrentStackPointer](../6B/KeGetCurrentStackPointer_function_006B1070.md) (function, `0x006B1070`)
- `0x002FC7B6` → [KeQueryCurrentStackInformationEx](KeQueryCurrentStackInformationEx_function_002F7CD0.md) (function, `0x002F7CD0`)
- `0x002FC7EF` → [ExpInterlockedPopEntrySList](../6B/ExpInterlockedPopEntrySList_function_006BA570.md) (function, `0x006BA570`)
- `0x002FC812` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x002FC833` → [ExpInterlockedPushEntrySList](../6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (function, `0x006BA5B0`)
- `0x002FC840` → [KeGetCurrentStackPointer](../6B/KeGetCurrentStackPointer_function_006B1070.md) (function, `0x006B1070`)
- `0x002FC894` → [EtwpContextRegisterTracingDispatcher](../4D/EtwpContextRegisterTracingDispatcher_function_004D83F4.md) (function, `0x004D83F4`)

### Direct callers
- [NtTraceEvent](NtTraceEvent_function_002FA6C0.md) at `0x002FAD3B`
- [EtwpTraceThreadRundown](../3C/EtwpTraceThreadRundown_function_003C370C.md) at `0x003C3982`
- [EtwpSetMark](../../page/7B/EtwpSetMark_function_007B878C.md) at `0x007B88A6`
- [sub_008629D0](../../page/86/Unknown_function_008629D0.md) at `0x00862AC7`

### Static image references
- `0x002FBF29` → RVA `0x00E0A740` (`.data`; read)
- `0x002FC2DA` → RVA `0x00FC7408` (`ALMOSTRO`; read)
- `0x002FC3E4` → RVA `0x00EFF840` (`.data`; read)
- `0x002FC483` → RVA `0x000105E0` (`.rdata`; read)
- `0x002FC4E6` → RVA `0x000105E8` (`.rdata`; read)
- `0x002FC660` → RVA `0x00E0AA1C` (`.data`; read)
- `0x002FC66D` → RVA `0x00F55CB3` (`.data`; read)
- `0x002FC7D9` → RVA `0x00FC6DA0` (`ALMOSTRO`; read)
- `0x002FC7E8` → RVA `0x00E28FB0` (`.data`; read)
- `0x002FC802` → RVA `0x00E00BE8` (`.data`; read)
- `0x002FC875` → RVA `0x00F475DC` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **4**
  - `0x002FC2AB` → [sub_006DF902](../6D/Unknown_function_006DF902.md) (`tail-transfer`)
  - `0x002FC819` → [sub_006DF902 + 0x144](../6D/Unknown_function_006DF902.md) (`tail-transfer`)
  - `0x002FC860` → [sub_006DF902 + 0x12B](../6D/Unknown_function_006DF902.md) (`tail-transfer`)
  - `0x002FC870` → [sub_006DF902 + 0x12B](../6D/Unknown_function_006DF902.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002FBF10  40 55                           push rbp
002FBF12  53                              push rbx
002FBF13  56                              push rsi
002FBF14  57                              push rdi
002FBF15  41 54                           push r12
002FBF17  41 55                           push r13
002FBF19  41 56                           push r14
002FBF1B  41 57                           push r15
002FBF1D  48 81 EC 78 01 00 00            sub rsp, 0x178
002FBF24  48 8D 6C 24 40                  lea rbp, [rsp + 0x40]
002FBF29  48 8B 05 10 E8 B0 00            mov rax, qword ptr [rip + 0xb0e810]
002FBF30  48 33 C5                        xor rax, rbp
002FBF33  48 89 85 20 01 00 00            mov qword ptr [rbp + 0x120], rax
002FBF3A  44 89 4D 38                     mov dword ptr [rbp + 0x38], r9d
002FBF3E  4D 8B F0                        mov r14, r8
002FBF41  4C 89 85 90 00 00 00            mov qword ptr [rbp + 0x90], r8
002FBF48  48 8B FA                        mov rdi, rdx
002FBF4B  48 89 95 80 00 00 00            mov qword ptr [rbp + 0x80], rdx
002FBF52  48 8B D9                        mov rbx, rcx
002FBF55  48 89 8D 88 00 00 00            mov qword ptr [rbp + 0x88], rcx
002FBF5C  44 8B AD A0 01 00 00            mov r13d, dword ptr [rbp + 0x1a0]
002FBF63  48 89 8D A0 00 00 00            mov qword ptr [rbp + 0xa0], rcx
002FBF6A  4C 89 85 A8 00 00 00            mov qword ptr [rbp + 0xa8], r8
002FBF71  44 89 4D 50                     mov dword ptr [rbp + 0x50], r9d
002FBF75  0F B7 85 A8 01 00 00            movzx eax, word ptr [rbp + 0x1a8]
002FBF7C  66 89 45 00                     mov word ptr [rbp], ax
002FBF80  44 8B 9D B0 01 00 00            mov r11d, dword ptr [rbp + 0x1b0]
002FBF87  44 89 5D 08                     mov dword ptr [rbp + 8], r11d
002FBF8B  44 89 5D 40                     mov dword ptr [rbp + 0x40], r11d
002FBF8F  0F 57 C0                        xorps xmm0, xmm0
002FBF92  33 C0                           xor eax, eax
002FBF94  0F 11 45 60                     movups xmmword ptr [rbp + 0x60], xmm0
002FBF98  48 89 45 70                     mov qword ptr [rbp + 0x70], rax
002FBF9C  48 89 45 28                     mov qword ptr [rbp + 0x28], rax
002FBFA0  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
002FBFA9  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
002FBFB0  90                              nop
002FBFB1  41 8B C1                        mov eax, r9d
002FBFB4  4C 8D 0C C5 00 00 00 00         lea r9, [rax*8]
002FBFBC  48 8B 81 C0 02 00 00            mov rax, qword ptr [rcx + 0x2c0]
002FBFC3  49 8B 0C 01                     mov rcx, qword ptr [r9 + rax]
002FBFC7  65 8B 04 25 A4 01 00 00         mov eax, dword ptr gs:[0x1a4]
002FBFCF  33 D2                           xor edx, edx
002FBFD1  F7 71 14                        div dword ptr [rcx + 0x14]
002FBFD4  0F AF 51 10                     imul edx, dword ptr [rcx + 0x10]
002FBFD8  44 8B C2                        mov r8d, edx
002FBFDB  4C 03 01                        add r8, qword ptr [rcx]
002FBFDE  41 0F 0D 08                     prefetchw byte ptr [r8]
002FBFE2  49 8B 00                        mov rax, qword ptr [r8]
002FBFE5  A8 01                           test al, 1
002FBFE7  0F 85 A0 03 00 00               jne 0x1402fc38d
002FBFED  48 8D 48 02                     lea rcx, [rax + 2]
002FBFF1  F0 49 0F B1 08                  lock cmpxchg qword ptr [r8], rcx
002FBFF6  75 ED                           jne 0x1402fbfe5
002FBFF8  48 8B 83 C8 02 00 00            mov rax, qword ptr [rbx + 0x2c8]
002FBFFF  4D 8B 24 01                     mov r12, qword ptr [r9 + rax]
002FC003  41 F6 C4 01                     test r12b, 1
002FC007  0F 85 A3 02 00 00               jne 0x1402fc2b0
002FC00D  4C 89 A5 98 00 00 00            mov qword ptr [rbp + 0x98], r12
002FC014  4D 85 E4                        test r12, r12
002FC017  0F 84 7E 03 00 00               je 0x1402fc39b
002FC01D  33 F6                           xor esi, esi
002FC01F  89 75 20                        mov dword ptr [rbp + 0x20], esi
002FC022  45 33 D2                        xor r10d, r10d
002FC025  41 83 FD 08                     cmp r13d, 8
002FC029  0F 82 D6 00 00 00               jb 0x1402fc105
002FC02F  41 8B F5                        mov esi, r13d
002FC032  83 E6 F8                        and esi, 0xfffffff8
002FC035  0F 57 ED                        xorps xmm5, xmm5
002FC038  0F 57 E4                        xorps xmm4, xmm4
002FC03B  41 BB 02 00 00 00               mov r11d, 2
002FC041  45 8B CA                        mov r9d, r10d
002FC044  45 8D 43 01                     lea r8d, [r11 + 1]
002FC048  4D 03 C0                        add r8, r8
002FC04B  41 8B D3                        mov edx, r11d
002FC04E  48 03 D2                        add rdx, rdx
002FC051  41 8D 4B FF                     lea ecx, [r11 - 1]
002FC055  48 03 C9                        add rcx, rcx
002FC058  4D 03 C9                        add r9, r9
002FC05B  66 42 0F 6E 4C C7 08            movd xmm1, dword ptr [rdi + r8*8 + 8]
002FC062  66 0F 6E 54 D7 08               movd xmm2, dword ptr [rdi + rdx*8 + 8]
002FC068  66 0F 6E 44 CF 08               movd xmm0, dword ptr [rdi + rcx*8 + 8]
002FC06E  66 42 0F 6E 5C CF 08            movd xmm3, dword ptr [rdi + r9*8 + 8]
002FC075  66 0F 62 D1                     punpckldq xmm2, xmm1
002FC079  66 0F 62 D8                     punpckldq xmm3, xmm0
002FC07D  66 0F 6C DA                     punpcklqdq xmm3, xmm2
002FC081  66 0F FE EB                     paddd xmm5, xmm3
002FC085  45 8D 4B 05                     lea r9d, [r11 + 5]
002FC089  4D 03 C9                        add r9, r9
002FC08C  45 8D 43 04                     lea r8d, [r11 + 4]
002FC090  4D 03 C0                        add r8, r8
002FC093  41 8D 53 03                     lea edx, [r11 + 3]
002FC097  48 03 D2                        add rdx, rdx
002FC09A  41 8D 4B 02                     lea ecx, [r11 + 2]
002FC09E  48 03 C9                        add rcx, rcx
002FC0A1  66 42 0F 6E 4C CF 08            movd xmm1, dword ptr [rdi + r9*8 + 8]
002FC0A8  66 42 0F 6E 54 C7 08            movd xmm2, dword ptr [rdi + r8*8 + 8]
002FC0AF  66 0F 6E 44 D7 08               movd xmm0, dword ptr [rdi + rdx*8 + 8]
002FC0B5  66 0F 6E 5C CF 08               movd xmm3, dword ptr [rdi + rcx*8 + 8]
002FC0BB  66 0F 62 D1                     punpckldq xmm2, xmm1
002FC0BF  66 0F 62 D8                     punpckldq xmm3, xmm0
002FC0C3  66 0F 6C DA                     punpcklqdq xmm3, xmm2
002FC0C7  66 0F FE E3                     paddd xmm4, xmm3
002FC0CB  41 83 C2 08                     add r10d, 8
002FC0CF  41 83 C3 08                     add r11d, 8
002FC0D3  44 3B D6                        cmp r10d, esi
002FC0D6  0F 82 65 FF FF FF               jb 0x1402fc041
002FC0DC  66 0F FE E5                     paddd xmm4, xmm5
002FC0E0  66 0F 6F C4                     movdqa xmm0, xmm4
002FC0E4  66 0F 73 D8 08                  psrldq xmm0, 8
002FC0E9  66 0F FE E0                     paddd xmm4, xmm0
002FC0ED  66 0F 6F C4                     movdqa xmm0, xmm4
002FC0F1  66 0F 73 D8 04                  psrldq xmm0, 4
002FC0F6  66 0F FE E0                     paddd xmm4, xmm0
002FC0FA  66 0F 7E E6                     movd esi, xmm4
002FC0FE  89 75 20                        mov dword ptr [rbp + 0x20], esi
002FC101  44 8B 5D 08                     mov r11d, dword ptr [rbp + 8]
002FC105  45 3B D5                        cmp r10d, r13d
002FC108  73 23                           jae 0x1402fc12d
002FC10A  41 8B CA                        mov ecx, r10d
002FC10D  48 C1 E1 04                     shl rcx, 4
002FC111  48 83 C1 08                     add rcx, 8
002FC115  48 03 CF                        add rcx, rdi
002FC118  41 8B D5                        mov edx, r13d
002FC11B  41 2B D2                        sub edx, r10d
002FC11E  03 31                           add esi, dword ptr [rcx]
002FC120  48 8D 49 10                     lea rcx, [rcx + 0x10]
002FC124  48 83 EA 01                     sub rdx, 1
002FC128  75 F4                           jne 0x1402fc11e
002FC12A  89 75 20                        mov dword ptr [rbp + 0x20], esi
002FC12D  44 8D 7E 20                     lea r15d, [rsi + 0x20]
002FC131  44 89 5C 24 20                  mov dword ptr [rsp + 0x20], r11d
002FC136  4C 8D 4D 28                     lea r9, [rbp + 0x28]
002FC13A  4C 8D 45 60                     lea r8, [rbp + 0x60]
002FC13E  41 8B D7                        mov edx, r15d
002FC141  49 8B CC                        mov rcx, r12
002FC144  E8 77 07 00 00                  call 0x1402fc8c0
002FC149  48 8B C8                        mov rcx, rax
002FC14C  44 8B 55 08                     mov r10d, dword ptr [rbp + 8]
002FC150  48 85 C0                        test rax, rax
002FC153  0F 84 66 02 00 00               je 0x1402fc3bf
002FC159  41 8B D2                        mov edx, r10d
002FC15C  81 E2 00 00 00 C0               and edx, 0xc0000000
002FC162  45 0F B6 CA                     movzx r9d, r10b
002FC166  4C 8B C0                        mov r8, rax
002FC169  81 FA 00 00 00 80               cmp edx, 0x80000000
002FC16F  B8 00 00 01 C0                  mov eax, 0xc0010000
002FC174  41 BB 00 00 02 C0               mov r11d, 0xc0020000
002FC17A  41 0F 45 C3                     cmovne eax, r11d
002FC17E  41 0B C1                        or eax, r9d
002FC181  41 89 00                        mov dword ptr [r8], eax
002FC184  48 8B 45 28                     mov rax, qword ptr [rbp + 0x28]
002FC188  48 89 41 10                     mov qword ptr [rcx + 0x10], rax
002FC18C  66 44 89 79 04                  mov word ptr [rcx + 4], r15w
002FC191  44 0F B7 5D 00                  movzx r11d, word ptr [rbp]
002FC196  66 44 89 59 06                  mov word ptr [rcx + 6], r11w
002FC19B  41 8B 86 10 05 00 00            mov eax, dword ptr [r14 + 0x510]
002FC1A2  89 41 08                        mov dword ptr [rcx + 8], eax
002FC1A5  41 8B 86 08 05 00 00            mov eax, dword ptr [r14 + 0x508]
002FC1AC  89 41 0C                        mov dword ptr [rcx + 0xc], eax
002FC1AF  41 8B 86 8C 02 00 00            mov eax, dword ptr [r14 + 0x28c]
002FC1B6  89 41 18                        mov dword ptr [rcx + 0x18], eax
002FC1B9  41 8B 86 DC 02 00 00            mov eax, dword ptr [r14 + 0x2dc]
002FC1C0  89 41 1C                        mov dword ptr [rcx + 0x1c], eax
002FC1C3  48 8D 41 20                     lea rax, [rcx + 0x20]
002FC1C7  48 89 85 B0 00 00 00            mov qword ptr [rbp + 0xb0], rax
002FC1CE  48 85 C0                        test rax, rax
002FC1D1  0F 84 ED 01 00 00               je 0x1402fc3c4
002FC1D7  44 8B F6                        mov r14d, esi
002FC1DA  89 75 48                        mov dword ptr [rbp + 0x48], esi
002FC1DD  C7 45 30 00 00 00 00            mov dword ptr [rbp + 0x30], 0
002FC1E4  4C 8B F8                        mov r15, rax
002FC1E7  48 89 45 78                     mov qword ptr [rbp + 0x78], rax
002FC1EB  33 DB                           xor ebx, ebx
002FC1ED  89 5D 30                        mov dword ptr [rbp + 0x30], ebx
002FC1F0  41 3B DD                        cmp ebx, r13d
002FC1F3  73 36                           jae 0x1402fc22b
002FC1F5  8B C3                           mov eax, ebx
002FC1F7  48 03 C0                        add rax, rax
002FC1FA  8B 74 C7 08                     mov esi, dword ptr [rdi + rax*8 + 8]
002FC1FE  48 8B 14 C7                     mov rdx, qword ptr [rdi + rax*8]
002FC202  41 3B F6                        cmp esi, r14d
002FC205  77 28                           ja 0x1402fc22f
002FC207  44 8B C6                        mov r8d, esi
002FC20A  49 8B CF                        mov rcx, r15
002FC20D  E8 2E A6 3C 00                  call 0x1406c6840
002FC212  4C 03 FE                        add r15, rsi
002FC215  4C 89 7D 78                     mov qword ptr [rbp + 0x78], r15
002FC219  44 2B F6                        sub r14d, esi
002FC21C  44 89 75 48                     mov dword ptr [rbp + 0x48], r14d
002FC220  FF C3                           inc ebx
002FC222  48 8B BD 80 00 00 00            mov rdi, qword ptr [rbp + 0x80]
002FC229  EB C2                           jmp 0x1402fc1ed
002FC22B  33 F6                           xor esi, esi
002FC22D  EB 05                           jmp 0x1402fc234
002FC22F  BE 04 00 00 C0                  mov esi, 0xc0000004
002FC234  89 75 34                        mov dword ptr [rbp + 0x34], esi
002FC237  48 8B 9D 88 00 00 00            mov rbx, qword ptr [rbp + 0x88]
002FC23E  48 8B BD 90 00 00 00            mov rdi, qword ptr [rbp + 0x90]
002FC245  44 8B 75 08                     mov r14d, dword ptr [rbp + 8]
002FC249  44 0F B7 7D 00                  movzx r15d, word ptr [rbp]
002FC24E  EB 2D                           jmp 0x1402fc27d
002FC250  8B F0                           mov esi, eax
002FC252  89 45 34                        mov dword ptr [rbp + 0x34], eax
002FC255  4C 8B A5 98 00 00 00            mov r12, qword ptr [rbp + 0x98]
002FC25C  48 8B 9D A0 00 00 00            mov rbx, qword ptr [rbp + 0xa0]
002FC263  48 8B BD A8 00 00 00            mov rdi, qword ptr [rbp + 0xa8]
002FC26A  8B 45 50                        mov eax, dword ptr [rbp + 0x50]
002FC26D  89 45 38                        mov dword ptr [rbp + 0x38], eax
002FC270  44 0F B7 7D 00                  movzx r15d, word ptr [rbp]
002FC275  44 8B 75 40                     mov r14d, dword ptr [rbp + 0x40]
002FC279  44 89 75 08                     mov dword ptr [rbp + 8], r14d
002FC27D  85 F6                           test esi, esi
002FC27F  0F 85 8A 03 00 00               jne 0x1402fc60f
002FC285  41 F7 44 24 0C 00 00 08 00      test dword ptr [r12 + 0xc], 0x80000
002FC28E  0F 85 CC 03 00 00               jne 0x1402fc660
002FC294  4D 8B 8C 24 20 06 00 00         mov r9, qword ptr [r12 + 0x620]
002FC29C  4D 85 C9                        test r9, r9
002FC29F  74 5B                           je 0x1402fc2fc
002FC2A1  48 8B 4D 60                     mov rcx, qword ptr [rbp + 0x60]
002FC2A5  8B 11                           mov edx, dword ptr [rcx]
002FC2A7  85 D2                           test edx, edx
002FC2A9  74 51                           je 0x1402fc2fc
002FC2AB  E9 52 36 3E 00                  jmp 0x1406df902
002FC2B0  48 8B 8B C0 02 00 00            mov rcx, qword ptr [rbx + 0x2c0]
002FC2B7  4A 8B 0C 09                     mov rcx, qword ptr [rcx + r9]
002FC2BB  E9 C3 00 00 00                  jmp 0x1402fc383
002FC2C0  45 85 C0                        test r8d, r8d
002FC2C3  74 37                           je 0x1402fc2fc
002FC2C5  44 0F B6 95 B8 01 00 00         movzx r10d, byte ptr [rbp + 0x1b8]
002FC2CD  41 0F B6 CA                     movzx ecx, r10b
002FC2D1  E8 96 0B 00 00                  call 0x1402fce6c
002FC2D6  85 C0                           test eax, eax
002FC2D8  74 22                           je 0x1402fc2fc
002FC2DA  48 8B 05 27 B1 CC 00            mov rax, qword ptr [rip + 0xccb127]
002FC2E1  4D 8B 41 08                     mov r8, qword ptr [r9 + 8]
002FC2E5  4C 89 44 24 20                  mov qword ptr [rsp + 0x20], r8
002FC2EA  45 0F B6 CA                     movzx r9d, r10b
002FC2EE  45 33 C0                        xor r8d, r8d
002FC2F1  41 8B D3                        mov edx, r11d
002FC2F4  48 8B CE                        mov rcx, rsi
002FC2F7  E8 D4 E7 3B 00                  call 0x1406baad0
002FC2FC  48 8B 45 68                     mov rax, qword ptr [rbp + 0x68]
002FC300  0F 0D 08                        prefetchw byte ptr [rax]
002FC303  48 8B 00                        mov rax, qword ptr [rax]
002FC306  48 8B 55 60                     mov rdx, qword ptr [rbp + 0x60]
002FC30A  48 8B CA                        mov rcx, rdx
002FC30D  48 33 C8                        xor rcx, rax
002FC310  48 83 F9 0F                     cmp rcx, 0xf
002FC314  0F 83 92 02 00 00               jae 0x1402fc5ac
002FC31A  48 8D 48 01                     lea rcx, [rax + 1]
002FC31E  48 8B 55 68                     mov rdx, qword ptr [rbp + 0x68]
002FC322  F0 48 0F B1 0A                  lock cmpxchg qword ptr [rdx], rcx
002FC327  75 DD                           jne 0x1402fc306
002FC329  41 8B 84 24 30 03 00 00         mov eax, dword ptr [r12 + 0x330]
002FC331  44 0F B7 45 00                  movzx r8d, word ptr [rbp]
002FC336  84 C0                           test al, al
002FC338  0F 88 1E 02 00 00               js 0x1402fc55c
002FC33E  41 8B 84 24 34 03 00 00         mov eax, dword ptr [r12 + 0x334]
002FC346  A8 02                           test al, 2
002FC348  0F 85 67 02 00 00               jne 0x1402fc5b5
002FC34E  41 F7 84 24 30 03 00 00 00 80 00 00  test dword ptr [r12 + 0x330], 0x8000
002FC35A  0F 85 CF 01 00 00               jne 0x1402fc52f
002FC360  8B 55 08                        mov edx, dword ptr [rbp + 8]
002FC363  41 F7 84 24 30 03 00 00 00 00 00 04  test dword ptr [r12 + 0x330], 0x4000000
002FC36F  0F 85 65 02 00 00               jne 0x1402fc5da
002FC375  8B 45 38                        mov eax, dword ptr [rbp + 0x38]
002FC378  48 8B 8B C0 02 00 00            mov rcx, qword ptr [rbx + 0x2c0]
002FC37F  48 8B 0C C1                     mov rcx, qword ptr [rcx + rax*8]
002FC383  BA 01 00 00 00                  mov edx, 1
002FC388  E8 C3 2C F6 FF                  call 0x14025f050
002FC38D  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
002FC396  E8 55 2C F6 FF                  call 0x14025eff0
002FC39B  48 8B 8D 20 01 00 00            mov rcx, qword ptr [rbp + 0x120]
002FC3A2  48 33 CD                        xor rcx, rbp
002FC3A5  E8 96 02 3B 00                  call 0x1406ac640
002FC3AA  48 8D A5 38 01 00 00            lea rsp, [rbp + 0x138]
002FC3B1  41 5F                           pop r15
002FC3B3  41 5E                           pop r14
002FC3B5  41 5D                           pop r13
002FC3B7  41 5C                           pop r12
002FC3B9  5F                              pop rdi
002FC3BA  5E                              pop rsi
002FC3BB  5B                              pop rbx
002FC3BC  5D                              pop rbp
002FC3BD  C3                              ret
002FC3BE  CC                              int3
002FC3BF  44 0F B7 5D 00                  movzx r11d, word ptr [rbp]
002FC3C4  81 FE F8 FF 00 00               cmp esi, 0xfff8
002FC3CA  0F 87 BB 02 00 00               ja 0x1402fc68b
002FC3D0  B8 05 00 00 80                  mov eax, 0x80000005
002FC3D5  41 B9 17 00 00 C0               mov r9d, 0xc0000017
002FC3DB  41 3B 74 24 08                  cmp esi, dword ptr [r12 + 8]
002FC3E0  44 0F 47 C8                     cmova r9d, eax
002FC3E4  48 8B 15 55 34 C0 00            mov rdx, qword ptr [rip + 0xc03455]
002FC3EB  48 85 D2                        test rdx, rdx
002FC3EE  74 85                           je 0x1402fc375
002FC3F0  48 8B 4A 20                     mov rcx, qword ptr [rdx + 0x20]
002FC3F4  83 79 60 00                     cmp dword ptr [rcx + 0x60], 0
002FC3F8  0F 85 00 01 00 00               jne 0x1402fc4fe
002FC3FE  66 83 7A 66 00                  cmp word ptr [rdx + 0x66], 0
002FC403  0F 84 6C FF FF FF               je 0x1402fc375
002FC409  48 8B 4A 28                     mov rcx, qword ptr [rdx + 0x28]
002FC40D  48 83 C1 60                     add rcx, 0x60
002FC411  41 B8 40 00 00 00               mov r8d, 0x40
002FC417  B2 02                           mov dl, 2
002FC419  E8 F2 0C 00 00                  call 0x1402fd110
002FC41E  84 C0                           test al, al
002FC420  0F 84 4F FF FF FF               je 0x1402fc375
002FC426  44 89 4D 18                     mov dword ptr [rbp + 0x18], r9d
002FC42A  66 44 89 5D 10                  mov word ptr [rbp + 0x10], r11w
002FC42F  48 8D 45 10                     lea rax, [rbp + 0x10]
002FC433  48 89 85 C0 00 00 00            mov qword ptr [rbp + 0xc0], rax
002FC43A  48 C7 85 C8 00 00 00 02 00 00 00  mov qword ptr [rbp + 0xc8], 2
002FC445  48 8D 45 18                     lea rax, [rbp + 0x18]
002FC449  48 89 85 D0 00 00 00            mov qword ptr [rbp + 0xd0], rax
002FC450  48 C7 85 D8 00 00 00 04 00 00 00  mov qword ptr [rbp + 0xd8], 4
002FC45B  49 8B 84 24 90 00 00 00         mov rax, qword ptr [r12 + 0x90]
002FC463  48 89 85 E0 00 00 00            mov qword ptr [rbp + 0xe0], rax
002FC46A  41 0F B7 84 24 88 00 00 00      movzx eax, word ptr [r12 + 0x88]
002FC473  89 85 E8 00 00 00               mov dword ptr [rbp + 0xe8], eax
002FC479  C7 85 EC 00 00 00 00 00 00 00   mov dword ptr [rbp + 0xec], 0
002FC483  48 8D 05 56 41 D1 FF            lea rax, [rip - 0x2ebeaa]
002FC48A  48 89 85 F0 00 00 00            mov qword ptr [rbp + 0xf0], rax
002FC491  48 C7 85 F8 00 00 00 02 00 00 00  mov qword ptr [rbp + 0xf8], 2
002FC49C  41 0F BA E2 09                  bt r10d, 9
002FC4A1  B8 05 00 00 00                  mov eax, 5
002FC4A6  41 B9 01 00 00 00               mov r9d, 1
002FC4AC  44 0F 42 C8                     cmovb r9d, eax
002FC4B0  41 F7 C2 00 06 00 00            test r10d, 0x600
002FC4B7  0F 85 E6 03 00 00               jne 0x1402fc8a3
002FC4BD  48 8D 85 C0 00 00 00            lea rax, [rbp + 0xc0]
002FC4C4  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
002FC4C9  C7 44 24 30 04 00 00 00         mov dword ptr [rsp + 0x30], 4
002FC4D1  48 C7 44 24 28 00 00 00 00      mov qword ptr [rsp + 0x28], 0
002FC4DA  48 C7 44 24 20 00 00 00 00      mov qword ptr [rsp + 0x20], 0
002FC4E3  45 33 C0                        xor r8d, r8d
002FC4E6  48 8D 15 FB 40 D1 FF            lea rdx, [rip - 0x2ebf05]
002FC4ED  48 8B 0D 4C 33 C0 00            mov rcx, qword ptr [rip + 0xc0334c]
002FC4F4  E8 D7 2B F6 FF                  call 0x14025f0d0
002FC4F9  E9 77 FE FF FF                  jmp 0x1402fc375
002FC4FE  0F B6 41 64                     movzx eax, byte ptr [rcx + 0x64]
002FC502  3C 02                           cmp al, 2
002FC504  0F 82 95 00 00 00               jb 0x1402fc59f
002FC50A  8B 41 68                        mov eax, dword ptr [rcx + 0x68]
002FC50D  F6 41 70 40                     test byte ptr [rcx + 0x70], 0x40
002FC511  0F 84 E7 FE FF FF               je 0x1402fc3fe
002FC517  48 8B 49 78                     mov rcx, qword ptr [rcx + 0x78]
002FC51B  48 8B C1                        mov rax, rcx
002FC51E  83 E0 40                        and eax, 0x40
002FC521  48 3B C1                        cmp rax, rcx
002FC524  0F 84 FC FE FF FF               je 0x1402fc426
002FC52A  E9 CF FE FF FF                  jmp 0x1402fc3fe
002FC52F  33 D2                           xor edx, edx
002FC531  49 8B 84 24 30 04 00 00         mov rax, qword ptr [r12 + 0x430]
002FC539  8B 48 08                        mov ecx, dword ptr [rax + 8]
002FC53C  3B D1                           cmp edx, ecx
002FC53E  0F 83 1C FE FF FF               jae 0x1402fc360
002FC544  49 8B 84 24 30 04 00 00         mov rax, qword ptr [r12 + 0x430]
002FC54C  66 44 39 44 50 0C               cmp word ptr [rax + rdx*2 + 0xc], r8w
002FC552  0F 84 D9 01 00 00               je 0x1402fc731
002FC558  FF C2                           inc edx
002FC55A  EB D5                           jmp 0x1402fc531
002FC55C  41 8B C8                        mov ecx, r8d
002FC55F  81 E1 FF 1F 00 00               and ecx, 0x1fff
002FC565  8B C1                           mov eax, ecx
002FC567  48 C1 E8 03                     shr rax, 3
002FC56B  49 03 84 24 18 04 00 00         add rax, qword ptr [r12 + 0x418]
002FC573  83 E1 07                        and ecx, 7
002FC576  0F B6 00                        movzx eax, byte ptr [rax]
002FC579  D2 F8                           sar al, cl
002FC57B  A8 01                           test al, 1
002FC57D  0F 84 BB FD FF FF               je 0x1402fc33e
002FC583  45 8B CE                        mov r9d, r14d
002FC586  4C 8B C7                        mov r8, rdi
002FC589  48 8D 55 28                     lea rdx, [rbp + 0x28]
002FC58D  49 8B CC                        mov rcx, r12
002FC590  E8 0B DF FF FF                  call 0x1402fa4a0
002FC595  44 0F B7 45 00                  movzx r8d, word ptr [rbp]
002FC59A  E9 9F FD FF FF                  jmp 0x1402fc33e
002FC59F  84 C0                           test al, al
002FC5A1  0F 84 63 FF FF FF               je 0x1402fc50a
002FC5A7  E9 52 FE FF FF                  jmp 0x1402fc3fe
002FC5AC  F0 FF 4A 0C                     lock dec dword ptr [rdx + 0xc]
002FC5B0  E9 74 FD FF FF                  jmp 0x1402fc329
002FC5B5  33 C9                           xor ecx, ecx
002FC5B7  41 8B 84 24 04 05 00 00         mov eax, dword ptr [r12 + 0x504]
002FC5BF  3B C8                           cmp ecx, eax
002FC5C1  0F 83 87 FD FF FF               jae 0x1402fc34e
002FC5C7  66 45 39 84 4C 08 05 00 00      cmp word ptr [r12 + rcx*2 + 0x508], r8w
002FC5D0  0F 84 B1 02 00 00               je 0x1402fc887
002FC5D6  FF C1                           inc ecx
002FC5D8  EB DD                           jmp 0x1402fc5b7
002FC5DA  45 33 C9                        xor r9d, r9d
002FC5DD  44 0F B7 7D 00                  movzx r15d, word ptr [rbp]
002FC5E2  49 8B 84 24 38 04 00 00         mov rax, qword ptr [r12 + 0x438]
002FC5EA  8B 48 18                        mov ecx, dword ptr [rax + 0x18]
002FC5ED  44 3B C9                        cmp r9d, ecx
002FC5F0  0F 83 7F FD FF FF               jae 0x1402fc375
002FC5F6  4D 8B 84 24 38 04 00 00         mov r8, qword ptr [r12 + 0x438]
002FC5FE  66 47 39 7C 48 1C               cmp word ptr [r8 + r9*2 + 0x1c], r15w
002FC604  0F 84 8C 00 00 00               je 0x1402fc696
002FC60A  41 FF C1                        inc r9d
002FC60D  EB D3                           jmp 0x1402fc5e2
002FC60F  44 8B 45 20                     mov r8d, dword ptr [rbp + 0x20]
002FC613  33 D2                           xor edx, edx
002FC615  48 8B 8D B0 00 00 00            mov rcx, qword ptr [rbp + 0xb0]
002FC61C  E8 1F A6 3C 00                  call 0x1406c6c40
002FC621  49 8B CC                        mov rcx, r12
002FC624  E8 B7 52 0F 00                  call 0x1403f18e0
002FC629  48 8D 15 B8 3F D1 FF            lea rdx, [rip - 0x2ec048]
002FC630  48 8B 0D 09 32 C0 00            mov rcx, qword ptr [rip + 0xc03209]
002FC637  E8 14 5E 09 00                  call 0x140392450
002FC63C  84 C0                           test al, al
002FC63E  0F 84 41 FC FF FF               je 0x1402fc285
002FC644  49 8D 94 24 88 00 00 00         lea rdx, [r12 + 0x88]
002FC64C  44 8B CE                        mov r9d, esi
002FC64F  45 8B C6                        mov r8d, r14d
002FC652  41 0F B7 CF                     movzx ecx, r15w
002FC656  E8 89 71 1C 00                  call 0x1404c37e4
002FC65B  E9 25 FC FF FF                  jmp 0x1402fc285
002FC660  80 3D B5 E3 B0 00 00            cmp byte ptr [rip + 0xb0e3b5], 0
002FC667  0F 84 08 02 00 00               je 0x1402fc875
002FC66D  80 3D 3F 96 C5 00 00            cmp byte ptr [rip + 0xc5963f], 0
002FC674  0F 84 1A FC FF FF               je 0x1402fc294
002FC67A  48 8D 55 60                     lea rdx, [rbp + 0x60]
002FC67E  49 8B CC                        mov rcx, r12
002FC681  E8 8A A7 1B 00                  call 0x1404b6e10
002FC686  E9 09 FC FF FF                  jmp 0x1402fc294
002FC68B  41 B9 95 00 00 C0               mov r9d, 0xc0000095
002FC691  E9 4E FD FF FF                  jmp 0x1402fc3e4
002FC696  0F 57 C0                        xorps xmm0, xmm0
002FC699  F3 0F 7F 85 E0 00 00 00         movdqu xmmword ptr [rbp + 0xe0], xmm0
002FC6A1  C7 85 F4 00 00 00 00 00 00 00   mov dword ptr [rbp + 0xf4], 0
002FC6AB  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
002FC6B4  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
002FC6BD  48 39 48 18                     cmp qword ptr [rax + 0x18], rcx
002FC6C1  0F 84 AE FC FF FF               je 0x1402fc375
002FC6C7  F7 C2 00 18 00 00               test edx, 0x1800
002FC6CD  0F 84 A2 FC FF FF               je 0x1402fc375
002FC6D3  48 85 FF                        test rdi, rdi
002FC6D6  48 0F 44 F9                     cmove rdi, rcx
002FC6DA  4C 89 A5 C0 00 00 00            mov qword ptr [rbp + 0xc0], r12
002FC6E1  89 95 F0 00 00 00               mov dword ptr [rbp + 0xf0], edx
002FC6E7  8B 87 08 05 00 00               mov eax, dword ptr [rdi + 0x508]
002FC6ED  89 85 D0 00 00 00               mov dword ptr [rbp + 0xd0], eax
002FC6F3  8B 87 10 05 00 00               mov eax, dword ptr [rdi + 0x510]
002FC6F9  89 85 D4 00 00 00               mov dword ptr [rbp + 0xd4], eax
002FC6FF  48 8B 45 28                     mov rax, qword ptr [rbp + 0x28]
002FC703  48 89 85 C8 00 00 00            mov qword ptr [rbp + 0xc8], rax
002FC70A  49 8B 40 08                     mov rax, qword ptr [r8 + 8]
002FC70E  48 89 85 D8 00 00 00            mov qword ptr [rbp + 0xd8], rax
002FC715  49 8B 40 10                     mov rax, qword ptr [r8 + 0x10]
002FC719  48 8B 40 10                     mov rax, qword ptr [rax + 0x10]
002FC71D  48 8D 95 C0 00 00 00            lea rdx, [rbp + 0xc0]
002FC724  49 8B 08                        mov rcx, qword ptr [r8]
002FC727  E8 A4 E3 3B 00                  call 0x1406baad0
002FC72C  E9 44 FC FF FF                  jmp 0x1402fc375
002FC731  C7 45 10 00 00 00 00            mov dword ptr [rbp + 0x10], 0
002FC738  48 C7 85 B8 00 00 00 00 00 00 00  mov qword ptr [rbp + 0xb8], 0
002FC743  0F 57 C0                        xorps xmm0, xmm0
002FC746  0F 11 85 C0 00 00 00            movups xmmword ptr [rbp + 0xc0], xmm0
002FC74D  0F 11 85 D0 00 00 00            movups xmmword ptr [rbp + 0xd0], xmm0
002FC754  0F 11 85 E0 00 00 00            movups xmmword ptr [rbp + 0xe0], xmm0
002FC75B  48 C7 45 58 00 00 00 00         mov qword ptr [rbp + 0x58], 0
002FC763  C7 45 18 00 00 00 00            mov dword ptr [rbp + 0x18], 0
002FC76A  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
002FC773  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
002FC77C  48 39 48 18                     cmp qword ptr [rax + 0x18], rcx
002FC780  0F 84 DA FB FF FF               je 0x1402fc360
002FC786  8B 55 08                        mov edx, dword ptr [rbp + 8]
002FC789  F7 C2 00 18 00 00               test edx, 0x1800
002FC78F  0F 84 CE FB FF FF               je 0x1402fc363
002FC795  4C 8B FF                        mov r15, rdi
002FC798  48 85 FF                        test rdi, rdi
002FC79B  4C 0F 44 F9                     cmove r15, rcx
002FC79F  E8 CC 48 3B 00                  call 0x1406b1070
002FC7A4  48 8B C8                        mov rcx, rax
002FC7A7  4C 8D 8D B8 00 00 00            lea r9, [rbp + 0xb8]
002FC7AE  4C 8D 45 58                     lea r8, [rbp + 0x58]
002FC7B2  48 8D 55 18                     lea rdx, [rbp + 0x18]
002FC7B6  E8 15 B5 FF FF                  call 0x1402f7cd0
002FC7BB  84 C0                           test al, al
002FC7BD  0F 84 9D FB FF FF               je 0x1402fc360
002FC7C3  8B 45 18                        mov eax, dword ptr [rbp + 0x18]
002FC7C6  83 F8 09                        cmp eax, 9
002FC7C9  77 0E                           ja 0x1402fc7d9
002FC7CB  B9 A1 03 00 00                  mov ecx, 0x3a1
002FC7D0  0F A3 C1                        bt ecx, eax
002FC7D3  0F 82 87 FB FF FF               jb 0x1402fc360
002FC7D9  8B 05 C1 A5 CC 00               mov eax, dword ptr [rip + 0xcca5c1]
002FC7DF  8D 34 40                        lea esi, [rax + rax*2]
002FC7E2  C1 E6 03                        shl esi, 3
002FC7E5  45 32 ED                        xor r13b, r13b
002FC7E8  48 8D 0D C1 C7 B2 00            lea rcx, [rip + 0xb2c7c1]
002FC7EF  E8 7C DD 3B 00                  call 0x1406ba570
002FC7F4  48 85 C0                        test rax, rax
002FC7F7  74 44                           je 0x1402fc83d
002FC7F9  4C 8D 70 10                     lea r14, [rax + 0x10]
002FC7FD  4D 85 F6                        test r14, r14
002FC800  74 3B                           je 0x1402fc83d
002FC802  48 8B 05 DF 43 B0 00            mov rax, qword ptr [rip + 0xb043df]
002FC809  4C 8D 45 10                     lea r8, [rbp + 0x10]
002FC80D  49 8B D6                        mov rdx, r14
002FC810  8B CE                           mov ecx, esi
002FC812  E8 B9 E2 3B 00                  call 0x1406baad0
002FC817  85 C0                           test eax, eax
002FC819  0F 89 27 32 3E 00               jns 0x1406dfa46
002FC81F  45 84 ED                        test r13b, r13b
002FC822  0F 85 38 FB FF FF               jne 0x1402fc360
002FC828  49 8D 56 F0                     lea rdx, [r14 - 0x10]
002FC82C  48 8D 0D 7D C7 B2 00            lea rcx, [rip + 0xb2c77d]
002FC833  E8 78 DD 3B 00                  call 0x1406ba5b0
002FC838  E9 23 FB FF FF                  jmp 0x1402fc360
002FC83D  44 8B F6                        mov r14d, esi
002FC840  E8 2B 48 3B 00                  call 0x1406b1070
002FC845  48 2B 45 58                     sub rax, qword ptr [rbp + 0x58]
002FC849  48 8D 8E 30 0E 00 00            lea rcx, [rsi + 0xe30]
002FC850  48 3B C1                        cmp rax, rcx
002FC853  0F 86 07 FB FF FF               jbe 0x1402fc360
002FC859  48 8D 46 0F                     lea rax, [rsi + 0xf]
002FC85D  49 3B C6                        cmp rax, r14
002FC860  0F 87 C7 31 3E 00               ja 0x1406dfa2d
002FC866  48 B8 F0 FF FF FF FF FF FF 0F   movabs rax, 0xffffffffffffff0
002FC870  E9 B8 31 3E 00                  jmp 0x1406dfa2d
002FC875  80 3D 60 AD C4 00 00            cmp byte ptr [rip + 0xc4ad60], 0
002FC87C  0F 85 EB FD FF FF               jne 0x1402fc66d
002FC882  E9 F3 FD FF FF                  jmp 0x1402fc67a
002FC887  45 8B CE                        mov r9d, r14d
002FC88A  4C 8B C7                        mov r8, rdi
002FC88D  48 8D 55 28                     lea rdx, [rbp + 0x28]
002FC891  49 8B CC                        mov rcx, r12
002FC894  E8 5B BB 1D 00                  call 0x1404d83f4
002FC899  44 0F B7 45 00                  movzx r8d, word ptr [rbp]
002FC89E  E9 AB FA FF FF                  jmp 0x1402fc34e
002FC8A3  41 83 C9 08                     or r9d, 8
002FC8A7  E9 11 FC FF FF                  jmp 0x1402fc4bd
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpLogSystemEventUnsafe(__int64 a1, __int64 a2, __int64 a3, int a4, unsigned int a5, unsigned __int16 a6, unsigned int a7)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
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
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned int v_stack_m128;
    unsigned int v_stack_m130;
    unsigned int v_stack_m138;
    unsigned int v_stack_m140;
    unsigned int v_stack_m144;
    unsigned int v_stack_m148;
    unsigned __int64 v_stack_m150;
    unsigned int v_stack_m158;
    unsigned int v_stack_m160;
    unsigned __int16 v_stack_m168;
    unsigned int v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned int v_stack_m198;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m80;
    unsigned int v_stack_m84;
    unsigned __int64 v_stack_m88;
    unsigned int v_stack_m8C;
    unsigned int v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned int v_stack_mA4;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned int v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int8 v_stack_p40;

    v_rsp = (v_rsp) - (376);
    result = (*(unsigned __int64 *)(v_rip + 11593744)) ^ (v_stack_m178);
    v_stack_m58 = result;
    v_stack_m140 = a4;
    v_stack_mE8 = a3;
    v_stack_mF8 = a2;
    v_stack_mF0 = a1;
    v_stack_mD8 = a1;
    v_stack_mD0 = a3;
    v_stack_m128 = a4;
    v_stack_m178 = a6;
    v_stack_m170 = (unsigned int)((unsigned int)(a7));
    v_stack_m138 = (unsigned int)((unsigned int)(a7));
    result = 0;
    v_stack_m118 = v_xmm0;
    v_stack_m108 = 0;
    v_stack_m150 = 0;
    a2 = 0;
    a2 = (unsigned int)((a2) * (*(unsigned int *)(*(unsigned __int64 *)((unsigned int)(a4) * 8 + *(unsigned __int64 *)(a1 + 704) * 1) + 16)));
    a3 = ((unsigned int)((unsigned int)(a2))) + (*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(a4) * 8 + *(unsigned __int64 *)(a1 + 704) * 1)));
loc_002FBFE5:
    if ((((unsigned __int8)(*(unsigned __int64 *)(a3))) & (1)) != 0) goto loc_002FC38D;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a3))) & (1)) != 0) goto loc_002FBFE5;
    if ((((unsigned __int8)(*(unsigned __int64 *)((unsigned int)(a4) * 8 + *(unsigned __int64 *)(a1 + 712) * 1))) & (1)) != 0) goto loc_002FC2B0;
    v_stack_mE0 = *(unsigned __int64 *)((unsigned int)(a4) * 8 + *(unsigned __int64 *)(a1 + 712) * 1);
    if (*(unsigned __int64 *)((unsigned int)(a4) * 8 + *(unsigned __int64 *)(a1 + 712) * 1) == 0) goto loc_002FC39B;
    v_rsi = 0;
    v_stack_m158 = 0;
    v_r10 = 0;
    if (((unsigned int)((unsigned int)(a5))) < 8) goto loc_002FC105;
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a5)))) & (0xFFFFFFF8ULL));
loc_002FC041:
    a3 = (2 + 1) + (2 + 1);
    a2 = (2) + (2);
    a1 = (2 - 1) + (2 - 1);
    a4 = (0) + (0);
    a4 = (2 + 5) + (2 + 5);
    a3 = (2 + 4) + (2 + 4);
    a2 = (2 + 3) + (2 + 3);
    a1 = (2 + 2) + (2 + 2);
    v_r10 = (unsigned int)((v_r10) + (8));
    v_r11 = (unsigned int)((2) + (8));
    if (((unsigned int)(v_r10)) < ((unsigned int)(v_rsi))) goto loc_002FC041;
    v_stack_m158 = (unsigned int)(v_rsi);
loc_002FC105:
    if (((unsigned int)(v_r10)) >= ((unsigned int)((unsigned int)(a5)))) goto loc_002FC12D;
    a1 = ((unsigned int)((unsigned int)(v_r10))) << (4);
    a1 = (a1) + (8);
    a1 = (a1) + (a2);
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a5)))) - ((unsigned int)(v_r10)));
loc_002FC11E:
    v_rsi = (unsigned int)((v_rsi) + (*(unsigned int *)(a1)));
    a2 = (a2) - (1);
    if (condition_is_not_equal) goto loc_002FC11E;
    v_stack_m158 = (unsigned int)(v_rsi);
loc_002FC12D:
    v_stack_m198 = (unsigned int)((unsigned int)(v_stack_m170));
    result = EtwpReserveTraceBuffer(*(unsigned __int64 *)((unsigned int)(a4) * 8 + *(unsigned __int64 *)(a1 + 712) * 1), (unsigned int)((unsigned int)(v_rsi + 32)), v_stack_m118, v_stack_m150);
    if (result == 0) goto loc_002FC3BF;
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m170)))) & (0xC0000000ULL));
    result = (unsigned int)(0xC0010000ULL);
    if (((unsigned int)(a2)) != 0x80000000ULL) { result = (unsigned int)((unsigned int)(0xC0020000ULL)); }
    result = (unsigned int)((result) | ((unsigned int)((unsigned __int8)((unsigned int)(v_stack_m170)))));
    *(unsigned int *)(result) = (unsigned int)(result);
    *(unsigned __int64 *)(result + 16) = v_stack_m150;
    *(unsigned __int16 *)(result + 4) = (unsigned __int16)(v_rsi + 32);
    *(unsigned __int16 *)(result + 6) = (unsigned __int16)(v_stack_m178);
    *(unsigned int *)(result + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(a3 + 1296)));
    *(unsigned int *)(result + 12) = (unsigned int)((unsigned int)(*(unsigned int *)(a3 + 1288)));
    *(unsigned int *)(result + 24) = (unsigned int)((unsigned int)(*(unsigned int *)(a3 + 652)));
    *(unsigned int *)(result + 28) = (unsigned int)((unsigned int)(*(unsigned int *)(a3 + 732)));
    v_stack_mC8 = result + 32;
    if (result + 32 == 0) goto loc_002FC3C4;
    v_stack_m130 = (unsigned int)(v_rsi);
    v_stack_m148 = 0;
    v_stack_m100 = result + 32;
    v_rbx = 0;
loc_002FC1ED:
    v_stack_m148 = 0;
    if (0 >= ((unsigned int)((unsigned int)(a5)))) goto loc_002FC22B;
    result = (0) + (0);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + result * 8 + 8)))) > ((unsigned int)((unsigned int)((unsigned int)(v_rsi))))) goto loc_002FC22F;
    result = memcpy(result + 32, *(unsigned __int64 *)(a2 + result * 8), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + result * 8 + 8)))), (unsigned __int8)((unsigned int)(v_stack_m170)));
    v_r15 = (result + 32) + ((unsigned int)(*(unsigned int *)(a2 + result * 8 + 8)));
    v_stack_m100 = v_r15;
    v_r14 = (unsigned int)(((unsigned int)((unsigned int)(v_rsi))) - ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + result * 8 + 8)))));
    v_stack_m130 = (unsigned int)(v_r14);
    v_rbx = (unsigned int)((v_rbx) + 1);
    goto loc_002FC1ED;
loc_002FC22B:
    v_rsi = 0;
    goto loc_002FC234;
loc_002FC22F:
loc_002FC234:
    v_stack_m144 = (unsigned int)((unsigned int)(0xC0000004ULL));
    goto loc_002FC27D;
loc_002FC27D:
    if ((unsigned int)((unsigned int)(0xC0000004ULL)) != 0) goto loc_002FC60F;
loc_002FC285:
    if (((*(unsigned int *)(*(unsigned __int64 *)((unsigned int)(a4) * 8 + *(unsigned __int64 *)(a1 + 712) * 1) + 12)) & (0x80000ULL)) != 0) goto loc_002FC660;
loc_002FC294:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(a4) * 8 + *(unsigned __int64 *)(a1 + 712) * 1) + 1568) == 0) goto loc_002FC2FC;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m118))) == 0) goto loc_002FC2FC;
loc_002FC2B0:
    goto loc_002FC383;
loc_002FC2FC:
loc_002FC306:
    a1 = (v_stack_m118) ^ (*(unsigned __int64 *)(v_stack_m110));
    if (a1 >= 15) goto loc_002FC5AC;
    if (a1 != 15) goto loc_002FC306;
loc_002FC329:
    if (sign_flag) goto loc_002FC55C;
loc_002FC33E:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned int)(a4) * 8 + *(unsigned __int64 *)(a1 + 712) * 1) + 820)))) & (2)) != 0) goto loc_002FC5B5;
loc_002FC34E:
    if (((*(unsigned int *)(*(unsigned __int64 *)((unsigned int)(a4) * 8 + *(unsigned __int64 *)(a1 + 712) * 1) + 816)) & (0x8000ULL)) != 0) goto loc_002FC52F;
loc_002FC360:
loc_002FC363:
    if (((*(unsigned int *)(*(unsigned __int64 *)((unsigned int)(a4) * 8 + *(unsigned __int64 *)(a1 + 712) * 1) + 816)) & (0x4000000ULL)) != 0) goto loc_002FC5DA;
loc_002FC375:
loc_002FC383:
    result = ExReleaseRundownProtectionCacheAwareEx(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mF0 + 704) + (unsigned int)(v_stack_m140) * 8), 1, v_stack_m178, *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(a4) * 8 + *(unsigned __int64 *)(a1 + 712) * 1) + 1568));
loc_002FC38D:
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), 1, v_stack_m178, *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(a4) * 8 + *(unsigned __int64 *)(a1 + 712) * 1) + 1568));
loc_002FC39B:
    a1 = (v_stack_m58) ^ (v_stack_m178);
    result = _security_check_cookie(a1, 1, v_stack_m178, *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(a4) * 8 + *(unsigned __int64 *)(a1 + 712) * 1) + 1568));
    return result;
loc_002FC3BF:
loc_002FC3C4:
    if (((unsigned int)((unsigned int)(0xC0000004ULL))) > 0xFFF8ULL) goto loc_002FC68B;
    a4 = (unsigned int)(0xC0000017ULL);
    if (((unsigned int)((unsigned int)(0xC0000004ULL))) > (*(unsigned int *)(*(unsigned __int64 *)((unsigned int)(a4) * 8 + *(unsigned __int64 *)(a1 + 712) * 1) + 8))) { a4 = (unsigned int)((unsigned int)(0x80000005ULL)); }
loc_002FC3E4:
    if (*(unsigned __int64 *)(v_rip + 12596309) == 0) goto loc_002FC375;
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12596309) + 32) + 96)) != 0) goto loc_002FC4FE;
loc_002FC3FE:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 12596309) + 102)) == 0) goto loc_002FC375;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12596309) + 40)) + (96);
    result = EtwpLevelKeywordEnabled(a1, 2, 64, a4);
    if ((unsigned __int8)(result) == 0) goto loc_002FC375;
loc_002FC426:
    v_stack_m160 = a4;
    v_stack_m168 = (unsigned __int16)(v_stack_m178);
    v_stack_mB8 = v_stack_m168;
    v_stack_mB0 = 2;
    v_stack_mA8 = v_stack_m160;
    v_stack_mA0 = 4;
    v_stack_m98 = *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(a4) * 8 + *(unsigned __int64 *)(a1 + 712) * 1) + 144);
    v_stack_m90 = (unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)((unsigned int)(a4) * 8 + *(unsigned __int64 *)(a1 + 712) * 1) + 136));
    v_stack_m8C = 0;
    v_stack_m88 = v_rip - 3063466;
    v_stack_m80 = 2;
    a4 = 1;
    if (condition_is_below) { a4 = 5; }
    if ((((unsigned int)((unsigned int)(v_stack_m170))) & (0x600ULL)) != 0) goto loc_002FC8A3;
loc_002FC4BD:
    v_stack_p38 = v_stack_mB8;
    v_stack_p30 = 4;
    v_stack_p28 = 0;
    v_stack_p20 = 0;
    a3 = 0;
    result = EtwWriteEx(*(unsigned __int64 *)(v_rip + 12596044), v_rip - 3063557, a3, a4);
    goto loc_002FC375;
loc_002FC4FE:
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 12596044) + 100))) < 2) goto loc_002FC59F;
loc_002FC50A:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 12596044) + 112)) & (64)) == 0) goto loc_002FC3FE;
    result = (unsigned int)((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12596044) + 120)) & (64));
    if (result == (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12596044) + 120))) goto loc_002FC426;
    goto loc_002FC3FE;
loc_002FC52F:
    a2 = 0;
loc_002FC531:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(a4) * 8 + *(unsigned __int64 *)(a1 + 712) * 1) + 1072) + 8))))) goto loc_002FC360;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(a4) * 8 + *(unsigned __int64 *)(a1 + 712) * 1) + 1072) + a2 * 2 + 12)) == 0) goto loc_002FC731;
    a2 = (unsigned int)((a2) + 1);
    goto loc_002FC531;
loc_002FC55C:
    a1 = (unsigned int)((0) & (0x1FFFULL));
    result = ((unsigned int)((unsigned int)(a1))) >> (3);
    result = (result) + (*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(a4) * 8 + *(unsigned __int64 *)(a1 + 712) * 1) + 1048));
    a1 = (unsigned int)((a1) & (7));
    result = (unsigned __int8)((*(unsigned __int8 *)(result)) >> ((unsigned __int8)(a1)));
    if ((((unsigned __int8)(result)) & (1)) == 0) goto loc_002FC33E;
    result = EtwpStackTraceDispatcher(*(unsigned __int64 *)((unsigned int)(a4) * 8 + *(unsigned __int64 *)(a1 + 712) * 1), v_stack_m150, v_stack_mE8, (unsigned int)((unsigned int)((unsigned int)(v_stack_m170))));
    goto loc_002FC33E;
loc_002FC59F:
    if ((unsigned __int8)(result) == 0) goto loc_002FC50A;
    goto loc_002FC3FE;
loc_002FC5AC:
    goto loc_002FC329;
loc_002FC5B5:
    a1 = 0;
loc_002FC5B7:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned int)(a4) * 8 + *(unsigned __int64 *)(a1 + 712) * 1) + 1284))))) goto loc_002FC34E;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)((unsigned int)(a4) * 8 + *(unsigned __int64 *)(a1 + 712) * 1) + a1 * 2 + 1288)) == ((unsigned __int16)(v_stack_m178))) goto loc_002FC887;
    a1 = (unsigned int)((a1) + 1);
    goto loc_002FC5B7;
loc_002FC5DA:
    a4 = 0;
loc_002FC5E2:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(a4) * 8 + *(unsigned __int64 *)(a1 + 712) * 1) + 1080) + 24))))) goto loc_002FC375;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(a4) * 8 + *(unsigned __int64 *)(a1 + 712) * 1) + 1080) + a4 * 2 + 28)) == ((unsigned __int16)(v_stack_m178))) goto loc_002FC696;
    a4 = (unsigned int)((a4) + 1);
    goto loc_002FC5E2;
loc_002FC60F:
    a2 = 0;
    result = memset(v_stack_mC8, a2, (unsigned int)(v_stack_m158), a4);
    result = EtwpUpdateEventsLostCount(*(unsigned __int64 *)((unsigned int)(a4) * 8 + *(unsigned __int64 *)(a1 + 712) * 1), a2, (unsigned int)(v_stack_m158), a4);
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 12595721), v_rip - 3063880, (unsigned int)(v_stack_m158), a4);
    if ((unsigned __int8)(result) == 0) goto loc_002FC285;
    result = EtwpTraceLostSystemEvent((unsigned __int16)(v_stack_m178), *(unsigned __int64 *)((unsigned int)(a4) * 8 + *(unsigned __int64 *)(a1 + 712) * 1) + 136, (unsigned int)((unsigned int)((unsigned int)(v_stack_m170))), (unsigned int)((unsigned int)((unsigned int)(0xC0000004ULL))));
    goto loc_002FC285;
loc_002FC660:
    if ((*(unsigned __int8 *)(v_rip + 11592629)) == 0) goto loc_002FC875;
loc_002FC66D:
    if ((*(unsigned __int8 *)(v_rip + 12949055)) == 0) goto loc_002FC294;
loc_002FC67A:
    result = EtwpSendTraceEvent(*(unsigned __int64 *)((unsigned int)(a4) * 8 + *(unsigned __int64 *)(a1 + 712) * 1), v_stack_m118, (unsigned int)((unsigned int)((unsigned int)(v_stack_m170))), (unsigned int)((unsigned int)((unsigned int)(0xC0000004ULL))));
    goto loc_002FC294;
loc_002FC68B:
    goto loc_002FC3E4;
loc_002FC696:
    v_stack_m98 = v_xmm0;
    v_stack_m84 = 0;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 24)) == (*(unsigned __int64 *)(gs_base + (0 + 392)))) goto loc_002FC375;
    if ((((unsigned int)(v_stack_m118)) & (0x1800ULL)) == 0) goto loc_002FC375;
    v_rdi = v_stack_mE8;
    if (v_stack_mE8 == 0) { v_rdi = *(unsigned __int64 *)(gs_base + (0 + 392)); }
    v_stack_mB8 = *(unsigned __int64 *)((unsigned int)(a4) * 8 + *(unsigned __int64 *)(a1 + 712) * 1);
    v_stack_m88 = (unsigned int)(v_stack_m118);
    v_stack_mA8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 1288)));
    v_stack_mA4 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 1296)));
    v_stack_mB0 = v_stack_m150;
    v_stack_mA0 = *(unsigned __int64 *)((unsigned int)((unsigned int)((unsigned int)(v_stack_m170))) + 8);
    result = guard_dispatch_icall(*(unsigned __int64 *)((unsigned int)((unsigned int)((unsigned int)(v_stack_m170)))), v_stack_mB8, (unsigned int)((unsigned int)((unsigned int)(v_stack_m170))), (unsigned int)(0xC0000095ULL));
    goto loc_002FC375;
loc_002FC731:
    v_stack_m168 = 0;
    v_stack_mC0 = 0;
    v_stack_mB8 = v_xmm0;
    v_stack_mA8 = v_xmm0;
    v_stack_m98 = v_xmm0;
    v_stack_m120 = 0;
    v_stack_m160 = 0;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 24)) == (*(unsigned __int64 *)(gs_base + (0 + 392)))) goto loc_002FC360;
    if ((((unsigned int)((unsigned int)(v_stack_m170))) & (0x1800ULL)) == 0) goto loc_002FC363;
    v_r15 = v_rdi;
    if (v_rdi == 0) { v_r15 = *(unsigned __int64 *)(gs_base + (0 + 392)); }
    result = KeGetCurrentStackPointer(*(unsigned __int64 *)(gs_base + (0 + 392)), (unsigned int)(v_stack_m170), (unsigned int)((unsigned int)((unsigned int)(v_stack_m170))), (unsigned int)(0xC0000095ULL));
    result = KeQueryCurrentStackInformationEx(result, v_stack_m160, v_stack_m120, v_stack_mC0);
    if ((unsigned __int8)(result) == 0) goto loc_002FC360;
    if (((unsigned int)((unsigned int)(v_stack_m160))) > 9) goto loc_002FC7D9;
    if (((unsigned int)((unsigned int)(v_stack_m160))) < 9) goto loc_002FC360;
loc_002FC7D9:
    v_rsi = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 13411777)) + (unsigned int)(*(unsigned int *)(v_rip + 13411777)) * 2) << (3));
    v_r13 = 0;
    result = ExpInterlockedPopEntrySList(v_rip + 11716545, v_stack_m160, v_stack_m120, v_stack_mC0);
    if (result == 0) goto loc_002FC83D;
    if (result + 16 == 0) goto loc_002FC83D;
    result = guard_dispatch_icall((unsigned int)((unsigned int)(v_rsi)), result + 16, v_stack_m168, v_stack_mC0);
    if (0 != 0) goto loc_002FC360;
    result = ExpInterlockedPushEntrySList(v_rip + 11716477, result + 16 - 16, v_stack_m168, v_stack_mC0);
    goto loc_002FC360;
loc_002FC83D:
    result = KeGetCurrentStackPointer(v_rip + 11716477, result + 16 - 16, v_stack_m168, v_stack_mC0);
    result = (result) - (v_stack_m120);
    if (result <= (v_rsi + 3632)) goto loc_002FC360;
loc_002FC875:
    if ((*(unsigned __int8 *)(v_rip + 12889440)) != 0) goto loc_002FC66D;
    goto loc_002FC67A;
loc_002FC887:
    result = EtwpContextRegisterTracingDispatcher(*(unsigned __int64 *)((unsigned int)(a4) * 8 + *(unsigned __int64 *)(a1 + 712) * 1), v_stack_m150, v_rdi, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rsi)))));
    goto loc_002FC34E;
loc_002FC8A3:
    a4 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rsi))))) | (8));
    goto loc_002FC4BD;
}
```

## 5. (Beta) C Style

```c
int64_t EtwpLogSystemEventUnsafe(void *Arg1, void *Arg2, void *Arg3, int32_t Arg4, uint32_t Arg5, uint16_t Arg6, uint32_t Arg7)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
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
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint32_t v_stack_m128;
    uint32_t v_stack_m130;
    uint32_t v_stack_m138;
    uint32_t v_stack_m140;
    uint32_t v_stack_m144;
    uint32_t v_stack_m148;
    uint64_t v_stack_m150;
    uint32_t v_stack_m158;
    uint32_t v_stack_m160;
    uint16_t v_stack_m168;
    uint32_t v_stack_m170;
    uint64_t v_stack_m178;
    uint32_t v_stack_m198;
    uint64_t v_stack_m40;
    uint64_t v_stack_m58;
    uint64_t v_stack_m80;
    uint32_t v_stack_m84;
    uint64_t v_stack_m88;
    uint32_t v_stack_m8C;
    uint32_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint32_t v_stack_mA4;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint32_t v_stack_p30;
    uint64_t v_stack_p38;
    uint8_t v_stack_p40;

    local_rsp = (local_rsp) - (376);
    result = (*(uint64_t *)(v_rip + 0xB0E810)) ^ (v_stack_m178);
    v_stack_m58 = result;
    v_stack_m140 = Arg4;
    v_stack_mE8 = Arg3;
    v_stack_mF8 = Arg2;
    v_stack_mF0 = Arg1;
    v_stack_mD8 = Arg1;
    v_stack_mD0 = Arg3;
    v_stack_m128 = Arg4;
    v_stack_m178 = Arg6;
    v_stack_m170 = (uint32_t)((uint32_t)(Arg7));
    v_stack_m138 = (uint32_t)((uint32_t)(Arg7));
    result = 0;
    v_stack_m118 = v_xmm0;
    v_stack_m108 = 0;
    v_stack_m150 = 0;
    Arg2 = 0;
    Arg2 = (uint32_t)((Arg2) * (*(uint32_t *)(*(uint64_t *)((uint32_t)(Arg4) * 8 + *(uint64_t *)(arg1 + 0x2C0) * 1) + 0x10)));
    Arg3 = ((uint32_t)((uint32_t)(Arg2))) + (*(uint64_t *)(*(uint64_t *)((uint32_t)(Arg4) * 8 + *(uint64_t *)(arg1 + 0x2C0) * 1)));
loc_002FBFE5:
    if ((((uint8_t)(*(uint64_t *)(arg3))) & (1)) != 0) goto loc_002FC38D;
    if ((((uint8_t)(*(uint64_t *)(arg3))) & (1)) != 0) goto loc_002FBFE5;
    if ((((uint8_t)(*(uint64_t *)((uint32_t)(Arg4) * 8 + *(uint64_t *)(arg1 + 0x2C8) * 1))) & (1)) != 0) goto loc_002FC2B0;
    v_stack_mE0 = *(uint64_t *)((uint32_t)(Arg4) * 8 + *(uint64_t *)(arg1 + 0x2C8) * 1);
    if (*(uint64_t *)((uint32_t)(Arg4) * 8 + *(uint64_t *)(arg1 + 0x2C8) * 1) == 0) goto loc_002FC39B;
    local_rsi = 0;
    v_stack_m158 = 0;
    local_r10 = 0;
    if (((uint32_t)((uint32_t)(Arg5))) < 8) goto loc_002FC105;
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg5)))) & (0xFFFFFFF8ULL));
loc_002FC041:
    Arg3 = (2 + 1) + (2 + 1);
    Arg2 = (2) + (2);
    Arg1 = (2 - 1) + (2 - 1);
    Arg4 = (0) + (0);
    Arg4 = (2 + 5) + (2 + 5);
    Arg3 = (2 + 4) + (2 + 4);
    Arg2 = (2 + 3) + (2 + 3);
    Arg1 = (2 + 2) + (2 + 2);
    local_r10 = (uint32_t)((local_r10) + (8));
    local_r11 = (uint32_t)((2) + (8));
    if (((uint32_t)(local_r10)) < ((uint32_t)(local_rsi))) goto loc_002FC041;
    v_stack_m158 = (uint32_t)(local_rsi);
loc_002FC105:
    if (((uint32_t)(local_r10)) >= ((uint32_t)((uint32_t)(Arg5)))) goto loc_002FC12D;
    Arg1 = ((uint32_t)((uint32_t)(local_r10))) << (4);
    Arg1 = (Arg1) + (8);
    Arg1 = (Arg1) + (Arg2);
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg5)))) - ((uint32_t)(local_r10)));
loc_002FC11E:
    local_rsi = (uint32_t)((local_rsi) + (*(uint32_t *)(arg1)));
    Arg2 = (Arg2) - (1);
    if (condition_is_not_equal) goto loc_002FC11E;
    v_stack_m158 = (uint32_t)(local_rsi);
loc_002FC12D:
    v_stack_m198 = (uint32_t)((uint32_t)(v_stack_m170));
    result = EtwpReserveTraceBuffer(*(uint64_t *)((uint32_t)(Arg4) * 8 + *(uint64_t *)(arg1 + 0x2C8) * 1), (uint32_t)((uint32_t)(local_rsi + 32)), v_stack_m118, v_stack_m150);
    if (result == 0) goto loc_002FC3BF;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m170)))) & (0xC0000000ULL));
    result = (uint32_t)(0xC0010000ULL);
    if (((uint32_t)(Arg2)) != 0x80000000ULL) { result = (uint32_t)((uint32_t)(0xC0020000ULL)); }
    result = (uint32_t)((result) | ((uint32_t)((uint8_t)((uint32_t)(v_stack_m170)))));
    *(uint32_t *)(result) = (uint32_t)(result);
    *(uint64_t *)(result + 0x10) = v_stack_m150;
    *(uint16_t *)(result + 0x4) = (uint16_t)(local_rsi + 32);
    *(uint16_t *)(result + 0x6) = (uint16_t)(v_stack_m178);
    *(uint32_t *)(result + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0x510)));
    *(uint32_t *)(result + 0xC) = (uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0x508)));
    *(uint32_t *)(result + 0x18) = (uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0x28C)));
    *(uint32_t *)(result + 0x1C) = (uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0x2DC)));
    v_stack_mC8 = result + 32;
    if (result + 32 == 0) goto loc_002FC3C4;
    v_stack_m130 = (uint32_t)(local_rsi);
    v_stack_m148 = 0;
    v_stack_m100 = result + 32;
    local_rbx = 0;
loc_002FC1ED:
    v_stack_m148 = 0;
    if (0 >= ((uint32_t)((uint32_t)(Arg5)))) goto loc_002FC22B;
    result = (0) + (0);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + result * 8 + 0x8)))) > ((uint32_t)((uint32_t)((uint32_t)(local_rsi))))) goto loc_002FC22F;
    result = memcpy(result + 32, *(uint64_t *)(arg2 + result * 8), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + result * 8 + 0x8)))), (uint8_t)((uint32_t)(v_stack_m170)));
    local_r15 = (result + 32) + ((uint32_t)(*(uint32_t *)(arg2 + result * 8 + 0x8)));
    v_stack_m100 = local_r15;
    local_r14 = (uint32_t)(((uint32_t)((uint32_t)(local_rsi))) - ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + result * 8 + 0x8)))));
    v_stack_m130 = (uint32_t)(local_r14);
    local_rbx = (uint32_t)((local_rbx) + 1);
    goto loc_002FC1ED;
loc_002FC22B:
    local_rsi = 0;
    goto loc_002FC234;
loc_002FC22F:
loc_002FC234:
    v_stack_m144 = (uint32_t)((uint32_t)(0xC0000004ULL));
    goto loc_002FC27D;
loc_002FC27D:
    if ((uint32_t)((uint32_t)(0xC0000004ULL)) != 0) goto loc_002FC60F;
loc_002FC285:
    if (((*(uint32_t *)(*(uint64_t *)((uint32_t)(Arg4) * 8 + *(uint64_t *)(arg1 + 0x2C8) * 1) + 0xC)) & (0x80000ULL)) != 0) goto loc_002FC660;
loc_002FC294:
    if (*(uint64_t *)(*(uint64_t *)((uint32_t)(Arg4) * 8 + *(uint64_t *)(arg1 + 0x2C8) * 1) + 0x620) == 0) goto loc_002FC2FC;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m118))) == 0) goto loc_002FC2FC;
loc_002FC2B0:
    goto loc_002FC383;
loc_002FC2FC:
loc_002FC306:
    Arg1 = (v_stack_m118) ^ (*(uint64_t *)(v_stack_m110));
    if (Arg1 >= 15) goto loc_002FC5AC;
    if (Arg1 != 15) goto loc_002FC306;
loc_002FC329:
    if (sign_flag) goto loc_002FC55C;
loc_002FC33E:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)((uint32_t)(Arg4) * 8 + *(uint64_t *)(arg1 + 0x2C8) * 1) + 0x334)))) & (2)) != 0) goto loc_002FC5B5;
loc_002FC34E:
    if (((*(uint32_t *)(*(uint64_t *)((uint32_t)(Arg4) * 8 + *(uint64_t *)(arg1 + 0x2C8) * 1) + 0x330)) & (0x8000ULL)) != 0) goto loc_002FC52F;
loc_002FC360:
loc_002FC363:
    if (((*(uint32_t *)(*(uint64_t *)((uint32_t)(Arg4) * 8 + *(uint64_t *)(arg1 + 0x2C8) * 1) + 0x330)) & (0x4000000ULL)) != 0) goto loc_002FC5DA;
loc_002FC375:
loc_002FC383:
    result = ExReleaseRundownProtectionCacheAwareEx(*(uint64_t *)(*(uint64_t *)(v_stack_mF0 + 0x2C0) + (uint32_t)(v_stack_m140) * 8), 1, v_stack_m178, *(uint64_t *)(*(uint64_t *)((uint32_t)(Arg4) * 8 + *(uint64_t *)(arg1 + 0x2C8) * 1) + 0x620));
loc_002FC38D:
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), 1, v_stack_m178, *(uint64_t *)(*(uint64_t *)((uint32_t)(Arg4) * 8 + *(uint64_t *)(arg1 + 0x2C8) * 1) + 0x620));
loc_002FC39B:
    Arg1 = (v_stack_m58) ^ (v_stack_m178);
    result = _security_check_cookie(Arg1, 1, v_stack_m178, *(uint64_t *)(*(uint64_t *)((uint32_t)(Arg4) * 8 + *(uint64_t *)(arg1 + 0x2C8) * 1) + 0x620));
    return result;
loc_002FC3BF:
loc_002FC3C4:
    if (((uint32_t)((uint32_t)(0xC0000004ULL))) > 0xFFF8ULL) goto loc_002FC68B;
    Arg4 = (uint32_t)(0xC0000017ULL);
    if (((uint32_t)((uint32_t)(0xC0000004ULL))) > (*(uint32_t *)(*(uint64_t *)((uint32_t)(Arg4) * 8 + *(uint64_t *)(arg1 + 0x2C8) * 1) + 0x8))) { Arg4 = (uint32_t)((uint32_t)(0x80000005ULL)); }
loc_002FC3E4:
    if (*(uint64_t *)(v_rip + 0xC03455) == 0) goto loc_002FC375;
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xC03455) + 0x20) + 0x60)) != 0) goto loc_002FC4FE;
loc_002FC3FE:
    if ((*(uint16_t *)(*(uint64_t *)(v_rip + 0xC03455) + 0x66)) == 0) goto loc_002FC375;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(v_rip + 0xC03455) + 0x28)) + (96);
    result = EtwpLevelKeywordEnabled(Arg1, 2, 64, Arg4);
    if ((uint8_t)(result) == 0) goto loc_002FC375;
loc_002FC426:
    v_stack_m160 = Arg4;
    v_stack_m168 = (uint16_t)(v_stack_m178);
    v_stack_mB8 = v_stack_m168;
    v_stack_mB0 = 2;
    v_stack_mA8 = v_stack_m160;
    v_stack_mA0 = 4;
    v_stack_m98 = *(uint64_t *)(*(uint64_t *)((uint32_t)(Arg4) * 8 + *(uint64_t *)(arg1 + 0x2C8) * 1) + 0x90);
    v_stack_m90 = (uint32_t)(*(uint16_t *)(*(uint64_t *)((uint32_t)(Arg4) * 8 + *(uint64_t *)(arg1 + 0x2C8) * 1) + 0x88));
    v_stack_m8C = 0;
    v_stack_m88 = v_rip - 3063466;
    v_stack_m80 = 2;
    Arg4 = 1;
    if (condition_is_below) { Arg4 = 5; }
    if ((((uint32_t)((uint32_t)(v_stack_m170))) & (0x600ULL)) != 0) goto loc_002FC8A3;
loc_002FC4BD:
    v_stack_p38 = v_stack_mB8;
    v_stack_p30 = 4;
    v_stack_p28 = 0;
    v_stack_p20 = 0;
    Arg3 = 0;
    result = EtwWriteEx(*(uint64_t *)(v_rip + 0xC0334C), v_rip - 3063557, Arg3, Arg4);
    goto loc_002FC375;
loc_002FC4FE:
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(v_rip + 0xC0334C) + 0x64))) < 2) goto loc_002FC59F;
loc_002FC50A:
    if (((*(uint8_t *)(*(uint64_t *)(v_rip + 0xC0334C) + 0x70)) & (64)) == 0) goto loc_002FC3FE;
    result = (uint32_t)((*(uint64_t *)(*(uint64_t *)(v_rip + 0xC0334C) + 0x78)) & (64));
    if (result == (*(uint64_t *)(*(uint64_t *)(v_rip + 0xC0334C) + 0x78))) goto loc_002FC426;
    goto loc_002FC3FE;
loc_002FC52F:
    Arg2 = 0;
loc_002FC531:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(Arg4) * 8 + *(uint64_t *)(arg1 + 0x2C8) * 1) + 0x430) + 0x8))))) goto loc_002FC360;
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(Arg4) * 8 + *(uint64_t *)(arg1 + 0x2C8) * 1) + 0x430) + arg2 * 2 + 0xC)) == 0) goto loc_002FC731;
    Arg2 = (uint32_t)((Arg2) + 1);
    goto loc_002FC531;
loc_002FC55C:
    Arg1 = (uint32_t)((0) & (0x1FFFULL));
    result = ((uint32_t)((uint32_t)(Arg1))) >> (3);
    result = (result) + (*(uint64_t *)(*(uint64_t *)((uint32_t)(Arg4) * 8 + *(uint64_t *)(arg1 + 0x2C8) * 1) + 0x418));
    Arg1 = (uint32_t)((Arg1) & (7));
    result = (uint8_t)((*(uint8_t *)(result)) >> ((uint8_t)(Arg1)));
    if ((((uint8_t)(result)) & (1)) == 0) goto loc_002FC33E;
    result = EtwpStackTraceDispatcher(*(uint64_t *)((uint32_t)(Arg4) * 8 + *(uint64_t *)(arg1 + 0x2C8) * 1), v_stack_m150, v_stack_mE8, (uint32_t)((uint32_t)((uint32_t)(v_stack_m170))));
    goto loc_002FC33E;
loc_002FC59F:
    if ((uint8_t)(result) == 0) goto loc_002FC50A;
    goto loc_002FC3FE;
loc_002FC5AC:
    goto loc_002FC329;
loc_002FC5B5:
    Arg1 = 0;
loc_002FC5B7:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)((uint32_t)(Arg4) * 8 + *(uint64_t *)(arg1 + 0x2C8) * 1) + 0x504))))) goto loc_002FC34E;
    if ((*(uint16_t *)(*(uint64_t *)((uint32_t)(Arg4) * 8 + *(uint64_t *)(arg1 + 0x2C8) * 1) + arg1 * 2 + 0x508)) == ((uint16_t)(v_stack_m178))) goto loc_002FC887;
    Arg1 = (uint32_t)((Arg1) + 1);
    goto loc_002FC5B7;
loc_002FC5DA:
    Arg4 = 0;
loc_002FC5E2:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(Arg4) * 8 + *(uint64_t *)(arg1 + 0x2C8) * 1) + 0x438) + 0x18))))) goto loc_002FC375;
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(Arg4) * 8 + *(uint64_t *)(arg1 + 0x2C8) * 1) + 0x438) + Arg4 * 2 + 0x1C)) == ((uint16_t)(v_stack_m178))) goto loc_002FC696;
    Arg4 = (uint32_t)((Arg4) + 1);
    goto loc_002FC5E2;
loc_002FC60F:
    Arg2 = 0;
    result = memset(v_stack_mC8, Arg2, (uint32_t)(v_stack_m158), Arg4);
    result = EtwpUpdateEventsLostCount(*(uint64_t *)((uint32_t)(Arg4) * 8 + *(uint64_t *)(arg1 + 0x2C8) * 1), Arg2, (uint32_t)(v_stack_m158), Arg4);
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0xC03209), v_rip - 3063880, (uint32_t)(v_stack_m158), Arg4);
    if ((uint8_t)(result) == 0) goto loc_002FC285;
    result = EtwpTraceLostSystemEvent((uint16_t)(v_stack_m178), *(uint64_t *)((uint32_t)(Arg4) * 8 + *(uint64_t *)(arg1 + 0x2C8) * 1) + 136, (uint32_t)((uint32_t)((uint32_t)(v_stack_m170))), (uint32_t)((uint32_t)((uint32_t)(0xC0000004ULL))));
    goto loc_002FC285;
loc_002FC660:
    if ((*(uint8_t *)(v_rip + 0xB0E3B5)) == 0) goto loc_002FC875;
loc_002FC66D:
    if ((*(uint8_t *)(v_rip + 0xC5963F)) == 0) goto loc_002FC294;
loc_002FC67A:
    result = EtwpSendTraceEvent(*(uint64_t *)((uint32_t)(Arg4) * 8 + *(uint64_t *)(arg1 + 0x2C8) * 1), v_stack_m118, (uint32_t)((uint32_t)((uint32_t)(v_stack_m170))), (uint32_t)((uint32_t)((uint32_t)(0xC0000004ULL))));
    goto loc_002FC294;
loc_002FC68B:
    goto loc_002FC3E4;
loc_002FC696:
    v_stack_m98 = v_xmm0;
    v_stack_m84 = 0;
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x18)) == (*(uint64_t *)(gs_base + (0 + 0x188)))) goto loc_002FC375;
    if ((((uint32_t)(v_stack_m118)) & (0x1800ULL)) == 0) goto loc_002FC375;
    local_rdi = v_stack_mE8;
    if (v_stack_mE8 == 0) { local_rdi = *(uint64_t *)(gs_base + (0 + 0x188)); }
    v_stack_mB8 = *(uint64_t *)((uint32_t)(Arg4) * 8 + *(uint64_t *)(arg1 + 0x2C8) * 1);
    v_stack_m88 = (uint32_t)(v_stack_m118);
    v_stack_mA8 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x508)));
    v_stack_mA4 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x510)));
    v_stack_mB0 = v_stack_m150;
    v_stack_mA0 = *(uint64_t *)((uint32_t)((uint32_t)((uint32_t)(v_stack_m170))) + 0x8);
    result = guard_dispatch_icall(*(uint64_t *)((uint32_t)((uint32_t)((uint32_t)(v_stack_m170)))), v_stack_mB8, (uint32_t)((uint32_t)((uint32_t)(v_stack_m170))), (uint32_t)(0xC0000095ULL));
    goto loc_002FC375;
loc_002FC731:
    v_stack_m168 = 0;
    v_stack_mC0 = 0;
    v_stack_mB8 = v_xmm0;
    v_stack_mA8 = v_xmm0;
    v_stack_m98 = v_xmm0;
    v_stack_m120 = 0;
    v_stack_m160 = 0;
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x18)) == (*(uint64_t *)(gs_base + (0 + 0x188)))) goto loc_002FC360;
    if ((((uint32_t)((uint32_t)(v_stack_m170))) & (0x1800ULL)) == 0) goto loc_002FC363;
    local_r15 = local_rdi;
    if (local_rdi == 0) { local_r15 = *(uint64_t *)(gs_base + (0 + 0x188)); }
    result = KeGetCurrentStackPointer(*(uint64_t *)(gs_base + (0 + 0x188)), (uint32_t)(v_stack_m170), (uint32_t)((uint32_t)((uint32_t)(v_stack_m170))), (uint32_t)(0xC0000095ULL));
    result = KeQueryCurrentStackInformationEx(result, v_stack_m160, v_stack_m120, v_stack_mC0);
    if ((uint8_t)(result) == 0) goto loc_002FC360;
    if (((uint32_t)((uint32_t)(v_stack_m160))) > 9) goto loc_002FC7D9;
    if (((uint32_t)((uint32_t)(v_stack_m160))) < 9) goto loc_002FC360;
loc_002FC7D9:
    local_rsi = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xCCA5C1)) + (uint32_t)(*(uint32_t *)(v_rip + 0xCCA5C1)) * 2) << (3));
    local_r13 = 0;
    result = ExpInterlockedPopEntrySList(v_rip + 11716545, v_stack_m160, v_stack_m120, v_stack_mC0);
    if (result == 0) goto loc_002FC83D;
    if (result + 16 == 0) goto loc_002FC83D;
    result = guard_dispatch_icall((uint32_t)((uint32_t)(local_rsi)), result + 16, v_stack_m168, v_stack_mC0);
    if (0 != 0) goto loc_002FC360;
    result = ExpInterlockedPushEntrySList(v_rip + 11716477, result + 16 - 16, v_stack_m168, v_stack_mC0);
    goto loc_002FC360;
loc_002FC83D:
    result = KeGetCurrentStackPointer(v_rip + 11716477, result + 16 - 16, v_stack_m168, v_stack_mC0);
    result = (result) - (v_stack_m120);
    if (result <= (local_rsi + 3632)) goto loc_002FC360;
loc_002FC875:
    if ((*(uint8_t *)(v_rip + 0xC4AD60)) != 0) goto loc_002FC66D;
    goto loc_002FC67A;
loc_002FC887:
    result = EtwpContextRegisterTracingDispatcher(*(uint64_t *)((uint32_t)(Arg4) * 8 + *(uint64_t *)(arg1 + 0x2C8) * 1), v_stack_m150, local_rdi, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rsi)))));
    goto loc_002FC34E;
loc_002FC8A3:
    Arg4 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rsi))))) | (8));
    goto loc_002FC4BD;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x2C0` | `64` | `R` |
| `Arg1` | `+ 0x2C8` | `64` | `R` |
| `Arg2` | `+ 0x8 + r8*8` | `32` | `R` |
| `Arg2` | `+ 0x8 + r9*8` | `32` | `R` |
| `Arg2` | `+ 0x8 + rcx*8` | `32` | `R` |
| `Arg2` | `+ 0x8 + rdx*8` | `32` | `R` |
| `Arg3` | `+ 0x28C` | `32` | `R` |
| `Arg3` | `+ 0x2DC` | `32` | `R` |
| `Arg3` | `+ 0x508` | `32` | `R` |
| `Arg3` | `+ 0x510` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002FBF10&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
