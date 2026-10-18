# EtwpLogContextSwapEvent

- RVA: `0x004175F0`–`0x00417BB5` (길이 `1,477` bytes)
- VA: `0x00000001404175F0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009CD74`
- 디코드: `349`개 명령, `1,477/1,477` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **11**; 고유 호출 대상: **11**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00417795` → [EtwpReserveTraceBuffer](../2F/EtwpReserveTraceBuffer_function_002FC8C0.md) (function, `0x002FC8C0`)
- `0x004179DE` → [EtwpGetLoggerTimeStamp](../37/EtwpGetLoggerTimeStamp_function_0037E690.md) (function, `0x0037E690`)
- `0x004179F8` → [EtwpCCSwapTrace](EtwpCCSwapTrace_function_00417BBC.md) (function, `0x00417BBC`)
- `0x00417A18` → [EtwpStackTraceDispatcher](../2F/EtwpStackTraceDispatcher_function_002FA4A0.md) (function, `0x002FA4A0`)
- `0x00417AE8` → [EtwpReserveWithPebsIndex](EtwpReserveWithPebsIndex_function_0041809C.md) (function, `0x0041809C`)
- `0x00417B19` → [EtwpReserveWithPmcCounters](../2F/EtwpReserveWithPmcCounters_function_002FCED0.md) (function, `0x002FCED0`)
- `0x00417B30` → [EtwpTraceLastBranchRecord](../2F/EtwpTraceLastBranchRecord_function_002F7B00.md) (function, `0x002F7B00`)
- `0x00417B4D` → [EtwpTraceProcessorTrace](EtwpTraceProcessorTrace_function_00418130.md) (function, `0x00418130`)
- `0x00417B70` → [EtwpContextRegisterTracingDispatcher](../4D/EtwpContextRegisterTracingDispatcher_function_004D83F4.md) (function, `0x004D83F4`)
- `0x00417B8D` → [EtwEventEnabled](../39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x00417BAE` → [EtwpTraceLostSystemEvent](../4C/EtwpTraceLostSystemEvent_function_004C37E4.md) (function, `0x004C37E4`)

### Direct callers
- [KiSwapThread](../35/KiSwapThread_function_00355640.md) at `0x00355ACE`
- [KiSwapThread](../35/KiSwapThread_function_00355640.md) at `0x00355AFF`
- [KiSwapThread](../35/KiSwapThread_function_00355640.md) at `0x00355B77`
- [KiSwapThread](../35/KiSwapThread_function_00355640.md) at `0x00355BAB`
- [EtwTraceContextSwap](EtwTraceContextSwap_function_004174A0.md) at `0x00417551`
- [EtwTraceContextSwap](EtwTraceContextSwap_function_004174A0.md) at `0x0041758D`
- [EtwTraceContextSwap](EtwTraceContextSwap_function_004174A0.md) at `0x004175A2`

### Static image references
- `0x00417B7F` → RVA `0x00EFF840` (`.data`; read)
- `0x00417B86` → RVA `0x000105E8` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004175F0  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
004175F5  55                              push rbp
004175F6  56                              push rsi
004175F7  57                              push rdi
004175F8  41 54                           push r12
004175FA  41 55                           push r13
004175FC  41 56                           push r14
004175FE  41 57                           push r15
00417600  48 8B EC                        mov rbp, rsp
00417603  48 83 EC 50                     sub rsp, 0x50
00417607  44 8B A9 A8 11 00 00            mov r13d, dword ptr [rcx + 0x11a8]
0041760E  45 33 C9                        xor r9d, r9d
00417611  33 C0                           xor eax, eax
00417613  4C 89 4D 58                     mov qword ptr [rbp + 0x58], r9
00417617  49 8B F0                        mov rsi, r8
0041761A  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
0041761E  45 0F BC C5                     bsf r8d, r13d
00417622  0F 57 C0                        xorps xmm0, xmm0
00417625  4C 8B F2                        mov r14, rdx
00417628  44 89 45 40                     mov dword ptr [rbp + 0x40], r8d
0041762C  4C 8B F9                        mov r15, rcx
0041762F  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
00417633  45 8B E1                        mov r12d, r9d
00417636  0F 84 16 01 00 00               je 0x140417752
0041763C  41 BA 24 05 00 00               mov r10d, 0x524
00417642  44 8D 58 2C                     lea r11d, [rax + 0x2c]
00417646  41 8D 45 FF                     lea eax, [r13 - 1]
0041764A  44 23 E8                        and r13d, eax
0041764D  41 8B C0                        mov eax, r8d
00417650  48 C1 E0 05                     shl rax, 5
00417654  48 05 CC 11 00 00               add rax, 0x11cc
0041765A  49 03 C7                        add rax, r15
0041765D  0F 84 E1 00 00 00               je 0x140417744
00417663  8B 40 04                        mov eax, dword ptr [rax + 4]
00417666  A8 04                           test al, 4
00417668  0F 84 D6 00 00 00               je 0x140417744
0041766E  43 0F B6 84 47 98 11 00 00      movzx eax, byte ptr [r15 + r8*2 + 0x1198]
00417677  41 3B 47 10                     cmp eax, dword ptr [r15 + 0x10]
0041767B  0F 83 C3 00 00 00               jae 0x140417744
00417681  0F AE E8                        lfence
00417684  8B C8                           mov ecx, eax
00417686  49 8B 87 C8 02 00 00            mov rax, qword ptr [r15 + 0x2c8]
0041768D  48 8B 3C C8                     mov rdi, qword ptr [rax + rcx*8]
00417691  40 F6 C7 01                     test dil, 1
00417695  0F 85 A9 00 00 00               jne 0x140417744
0041769B  8B 45 40                        mov eax, dword ptr [rbp + 0x40]
0041769E  48 C1 E0 05                     shl rax, 5
004176A2  48 05 CC 11 00 00               add rax, 0x11cc
004176A8  49 03 C7                        add rax, r15
004176AB  0F 84 BA 00 00 00               je 0x14041776b
004176B1  F7 40 04 00 01 00 00            test dword ptr [rax + 4], 0x100
004176B8  0F 84 AD 00 00 00               je 0x14041776b
004176BE  8B 8F C8 00 00 00               mov ecx, dword ptr [rdi + 0xc8]
004176C4  BB 01 00 00 00                  mov ebx, 1
004176C9  41 8B C4                        mov eax, r12d
004176CC  D3 E3                           shl ebx, cl
004176CE  F7 D0                           not eax
004176D0  85 C3                           test ebx, eax
004176D2  0F 85 03 03 00 00               jne 0x1404179db
004176D8  48 8B DF                        mov rbx, rdi
004176DB  BF 24 05 00 00                  mov edi, 0x524
004176E0  48 85 F6                        test rsi, rsi
004176E3  0F 84 6C 04 00 00               je 0x140417b55
004176E9  8B 83 30 03 00 00               mov eax, dword ptr [rbx + 0x330]
004176EF  84 C0                           test al, al
004176F1  79 14                           jns 0x140417707
004176F3  48 8B 83 18 04 00 00            mov rax, qword ptr [rbx + 0x418]
004176FA  F6 80 A4 00 00 00 10            test byte ptr [rax + 0xa4], 0x10
00417701  0F 85 01 03 00 00               jne 0x140417a08
00417707  8B 83 34 03 00 00               mov eax, dword ptr [rbx + 0x334]
0041770D  A8 02                           test al, 2
0041770F  0F 85 56 03 00 00               jne 0x140417a6b
00417715  45 33 C9                        xor r9d, r9d
00417718  F7 83 30 03 00 00 00 80 00 00   test dword ptr [rbx + 0x330], 0x8000
00417722  0F 85 0F 03 00 00               jne 0x140417a37
00417728  F7 83 30 03 00 00 00 00 00 04   test dword ptr [rbx + 0x330], 0x4000000
00417732  41 BA 24 05 00 00               mov r10d, 0x524
00417738  0F 85 52 03 00 00               jne 0x140417a90
0041773E  41 BB 2C 00 00 00               mov r11d, 0x2c
00417744  45 0F BC C5                     bsf r8d, r13d
00417748  44 89 45 40                     mov dword ptr [rbp + 0x40], r8d
0041774C  0F 85 F4 FE FF FF               jne 0x140417646
00417752  48 8B 9C 24 98 00 00 00         mov rbx, qword ptr [rsp + 0x98]
0041775A  48 83 C4 50                     add rsp, 0x50
0041775E  41 5F                           pop r15
00417760  41 5E                           pop r14
00417762  41 5D                           pop r13
00417764  41 5C                           pop r12
00417766  5F                              pop rdi
00417767  5E                              pop rsi
00417768  5D                              pop rbp
00417769  C3                              ret
0041776A  CC                              int3
0041776B  8B 87 30 03 00 00               mov eax, dword ptr [rdi + 0x330]
00417771  48 8B DF                        mov rbx, rdi
00417774  A9 00 0C 00 00                  test eax, 0xc00
00417779  0F 85 C9 01 00 00               jne 0x140417948
0041777F  4C 8D 4D 58                     lea r9, [rbp + 0x58]
00417783  C7 44 24 20 05 5A 50 00         mov dword ptr [rsp + 0x20], 0x505a05
0041778B  4C 8D 45 E0                     lea r8, [rbp - 0x20]
0041778F  41 8B D3                        mov edx, r11d
00417792  48 8B CB                        mov rcx, rbx
00417795  E8 26 51 EE FF                  call 0x1402fc8c0
0041779A  45 33 C9                        xor r9d, r9d
0041779D  48 85 C0                        test rax, rax
004177A0  0F 84 D4 03 00 00               je 0x140417b7a
004177A6  48 8B 4D 58                     mov rcx, qword ptr [rbp + 0x58]
004177AA  48 8D 50 10                     lea rdx, [rax + 0x10]
004177AE  48 89 48 08                     mov qword ptr [rax + 8], rcx
004177B2  C7 00 05 00 11 C0               mov dword ptr [rax], 0xc0110005
004177B8  C7 40 04 2C 00 24 05            mov dword ptr [rax + 4], 0x524002c
004177BF  BF 24 05 00 00                  mov edi, 0x524
004177C4  48 85 D2                        test rdx, rdx
004177C7  0F 84 B2 03 00 00               je 0x140417b7f
004177CD  33 C0                           xor eax, eax
004177CF  0F 57 C0                        xorps xmm0, xmm0
004177D2  0F 11 02                        movups xmmword ptr [rdx], xmm0
004177D5  48 89 42 10                     mov qword ptr [rdx + 0x10], rax
004177D9  89 42 18                        mov dword ptr [rdx + 0x18], eax
004177DC  4D 85 F6                        test r14, r14
004177DF  0F 84 BE 00 00 00               je 0x1404178a3
004177E5  41 8B 86 10 05 00 00            mov eax, dword ptr [r14 + 0x510]
004177EC  89 42 04                        mov dword ptr [rdx + 4], eax
004177EF  41 8A 86 C3 00 00 00            mov al, byte ptr [r14 + 0xc3]
004177F6  88 42 09                        mov byte ptr [rdx + 9], al
004177F9  41 8A 86 83 02 00 00            mov al, byte ptr [r14 + 0x283]
00417800  88 42 0C                        mov byte ptr [rdx + 0xc], al
00417803  8A 42 0D                        mov al, byte ptr [rdx + 0xd]
00417806  8A C8                           mov cl, al
00417808  41 32 8E 87 01 00 00            xor cl, byte ptr [r14 + 0x187]
0041780F  80 E1 01                        and cl, 1
00417812  32 C8                           xor cl, al
00417814  88 4A 0D                        mov byte ptr [rdx + 0xd], cl
00417817  41 8A 86 84 01 00 00            mov al, byte ptr [r14 + 0x184]
0041781E  88 42 0E                        mov byte ptr [rdx + 0xe], al
00417821  41 8A 86 4C 02 00 00            mov al, byte ptr [r14 + 0x24c]
00417828  88 42 0F                        mov byte ptr [rdx + 0xf], al
0041782B  41 8A 8E 04 02 00 00            mov cl, byte ptr [r14 + 0x204]
00417832  8A 42 0D                        mov al, byte ptr [rdx + 0xd]
00417835  02 C9                           add cl, cl
00417837  32 C8                           xor cl, al
00417839  80 E1 0E                        and cl, 0xe
0041783C  32 C8                           xor cl, al
0041783E  88 4A 0D                        mov byte ptr [rdx + 0xd], cl
00417841  49 8B 4E 20                     mov rcx, qword ptr [r14 + 0x20]
00417845  49 8B 46 48                     mov rax, qword ptr [r14 + 0x48]
00417849  48 2B C8                        sub rcx, rax
0041784C  48 C1 E9 0A                     shr rcx, 0xa
00417850  89 4A 14                        mov dword ptr [rdx + 0x14], ecx
00417853  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
0041785C  4C 3B 70 18                     cmp r14, qword ptr [rax + 0x18]
00417860  0F 85 2D 01 00 00               jne 0x140417993
00417866  48 8B 80 40 88 00 00            mov rax, qword ptr [rax + 0x8840]
0041786D  48 85 C0                        test rax, rax
00417870  74 06                           je 0x140417878
00417872  8A 40 1C                        mov al, byte ptr [rax + 0x1c]
00417875  88 42 0A                        mov byte ptr [rdx + 0xa], al
00417878  41 8B 86 E4 01 00 00            mov eax, dword ptr [r14 + 0x1e4]
0041787F  85 C0                           test eax, eax
00417881  0F 85 03 01 00 00               jne 0x14041798a
00417887  66 45 39 8E E6 01 00 00         cmp word ptr [r14 + 0x1e6], r9w
0041788F  0F 85 99 01 00 00               jne 0x140417a2e
00417895  41 80 BE 86 01 00 00 01         cmp byte ptr [r14 + 0x186], 1
0041789D  0F 83 8B 01 00 00               jae 0x140417a2e
004178A3  48 85 F6                        test rsi, rsi
004178A6  74 6D                           je 0x140417915
004178A8  8B 86 10 05 00 00               mov eax, dword ptr [rsi + 0x510]
004178AE  89 02                           mov dword ptr [rdx], eax
004178B0  8A 86 C3 00 00 00               mov al, byte ptr [rsi + 0xc3]
004178B6  88 42 08                        mov byte ptr [rdx + 8], al
004178B9  8A 86 06 02 00 00               mov al, byte ptr [rsi + 0x206]
004178BF  88 42 0B                        mov byte ptr [rdx + 0xb], al
004178C2  8A 8E 04 02 00 00               mov cl, byte ptr [rsi + 0x204]
004178C8  8A 42 0D                        mov al, byte ptr [rdx + 0xd]
004178CB  C0 E1 04                        shl cl, 4
004178CE  32 C8                           xor cl, al
004178D0  80 E1 70                        and cl, 0x70
004178D3  32 C8                           xor cl, al
004178D5  48 B8 20 03 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000320
004178DF  88 4A 0D                        mov byte ptr [rdx + 0xd], cl
004178E2  8B 00                           mov eax, dword ptr [rax]
004178E4  2B 86 B4 01 00 00               sub eax, dword ptr [rsi + 0x1b4]
004178EA  89 42 10                        mov dword ptr [rdx + 0x10], eax
004178ED  44 39 8E E4 01 00 00            cmp dword ptr [rsi + 0x1e4], r9d
004178F4  0F 85 2B 01 00 00               jne 0x140417a25
004178FA  66 44 39 8E E6 01 00 00         cmp word ptr [rsi + 0x1e6], r9w
00417902  0F 85 CA 00 00 00               jne 0x1404179d2
00417908  80 BE 86 01 00 00 01            cmp byte ptr [rsi + 0x186], 1
0041790F  0F 83 BD 00 00 00               jae 0x1404179d2
00417915  48 8B 45 E8                     mov rax, qword ptr [rbp - 0x18]
00417919  0F 0D 08                        prefetchw byte ptr [rax]
0041791C  48 8B 00                        mov rax, qword ptr [rax]
0041791F  48 8B 55 E0                     mov rdx, qword ptr [rbp - 0x20]
00417923  48 8B CA                        mov rcx, rdx
00417926  48 33 C8                        xor rcx, rax
00417929  48 83 F9 0F                     cmp rcx, 0xf
0041792D  0F 83 8B 01 00 00               jae 0x140417abe
00417933  48 8B 55 E8                     mov rdx, qword ptr [rbp - 0x18]
00417937  48 8D 48 01                     lea rcx, [rax + 1]
0041793B  F0 48 0F B1 0A                  lock cmpxchg qword ptr [rdx], rcx
00417940  0F 84 9A FD FF FF               je 0x1404176e0
00417946  EB D7                           jmp 0x14041791f
00417948  0F BA E0 0A                     bt eax, 0xa
0041794C  0F 82 75 01 00 00               jb 0x140417ac7
00417952  0F BA E0 0B                     bt eax, 0xb
00417956  0F 83 23 FE FF FF               jae 0x14041777f
0041795C  41 8B D1                        mov edx, r9d
0041795F  48 8B 87 28 04 00 00            mov rax, qword ptr [rdi + 0x428]
00417966  8B 48 08                        mov ecx, dword ptr [rax + 8]
00417969  3B D1                           cmp edx, ecx
0041796B  0F 83 0E FE FF FF               jae 0x14041777f
00417971  48 8B 87 28 04 00 00            mov rax, qword ptr [rdi + 0x428]
00417978  8B CA                           mov ecx, edx
0041797A  66 44 39 54 48 0C               cmp word ptr [rax + rcx*2 + 0xc], r10w
00417980  0F 84 72 01 00 00               je 0x140417af8
00417986  FF C2                           inc edx
00417988  EB D5                           jmp 0x14041795f
0041798A  80 4A 18 01                     or byte ptr [rdx + 0x18], 1
0041798E  E9 F4 FE FF FF                  jmp 0x140417887
00417993  49 8B 4E 68                     mov rcx, qword ptr [r14 + 0x68]
00417997  48 85 C9                        test rcx, rcx
0041799A  74 2B                           je 0x1404179c7
0041799C  8B 80 D8 00 00 00               mov eax, dword ptr [rax + 0xd8]
004179A2  48 03 C1                        add rax, rcx
004179A5  81 78 7C FF 00 00 00            cmp dword ptr [rax + 0x7c], 0xff
004179AC  0F 87 B2 00 00 00               ja 0x140417a64
004179B2  8A 48 7C                        mov cl, byte ptr [rax + 0x7c]
004179B5  84 C9                           test cl, cl
004179B7  75 11                           jne 0x1404179ca
004179B9  48 8B 80 A0 01 00 00            mov rax, qword ptr [rax + 0x1a0]
004179C0  48 85 C0                        test rax, rax
004179C3  75 E0                           jne 0x1404179a5
004179C5  EB 03                           jmp 0x1404179ca
004179C7  41 8A C9                        mov cl, r9b
004179CA  88 4A 0A                        mov byte ptr [rdx + 0xa], cl
004179CD  E9 A6 FE FF FF                  jmp 0x140417878
004179D2  80 4A 18 08                     or byte ptr [rdx + 0x18], 8
004179D6  E9 3A FF FF FF                  jmp 0x140417915
004179DB  48 8B CF                        mov rcx, rdi
004179DE  E8 AD 6C F6 FF                  call 0x14037e690
004179E3  48 89 45 58                     mov qword ptr [rbp + 0x58], rax
004179E7  4C 8D 4D 58                     lea r9, [rbp + 0x58]
004179EB  44 8B 87 C8 00 00 00            mov r8d, dword ptr [rdi + 0xc8]
004179F2  48 8B D6                        mov rdx, rsi
004179F5  49 8B CE                        mov rcx, r14
004179F8  E8 BF 01 00 00                  call 0x140417bbc
004179FD  44 0B E3                        or r12d, ebx
00417A00  45 33 C9                        xor r9d, r9d
00417A03  E9 D0 FC FF FF                  jmp 0x1404176d8
00417A08  41 B9 05 5A 50 00               mov r9d, 0x505a05
00417A0E  48 8D 55 58                     lea rdx, [rbp + 0x58]
00417A12  4C 8B C6                        mov r8, rsi
00417A15  48 8B CB                        mov rcx, rbx
00417A18  E8 83 2A EE FF                  call 0x1402fa4a0
00417A1D  45 33 C9                        xor r9d, r9d
00417A20  E9 E2 FC FF FF                  jmp 0x140417707
00417A25  80 4A 18 04                     or byte ptr [rdx + 0x18], 4
00417A29  E9 CC FE FF FF                  jmp 0x1404178fa
00417A2E  80 4A 18 02                     or byte ptr [rdx + 0x18], 2
00417A32  E9 6C FE FF FF                  jmp 0x1404178a3
00417A37  41 8B D1                        mov edx, r9d
00417A3A  48 8B 83 30 04 00 00            mov rax, qword ptr [rbx + 0x430]
00417A41  8B 48 08                        mov ecx, dword ptr [rax + 8]
00417A44  3B D1                           cmp edx, ecx
00417A46  0F 83 DC FC FF FF               jae 0x140417728
00417A4C  48 8B 83 30 04 00 00            mov rax, qword ptr [rbx + 0x430]
00417A53  8B CA                           mov ecx, edx
00417A55  66 39 7C 48 0C                  cmp word ptr [rax + rcx*2 + 0xc], di
00417A5A  0F 84 C0 00 00 00               je 0x140417b20
00417A60  FF C2                           inc edx
00417A62  EB D6                           jmp 0x140417a3a
00417A64  B1 FF                           mov cl, 0xff
00417A66  E9 5F FF FF FF                  jmp 0x1404179ca
00417A6B  41 8B C9                        mov ecx, r9d
00417A6E  8B 83 04 05 00 00               mov eax, dword ptr [rbx + 0x504]
00417A74  3B C8                           cmp ecx, eax
00417A76  0F 83 99 FC FF FF               jae 0x140417715
00417A7C  8B C1                           mov eax, ecx
00417A7E  66 39 BC 43 08 05 00 00         cmp word ptr [rbx + rax*2 + 0x508], di
00417A86  0F 84 D4 00 00 00               je 0x140417b60
00417A8C  FF C1                           inc ecx
00417A8E  EB DE                           jmp 0x140417a6e
00417A90  41 8B D1                        mov edx, r9d
00417A93  48 8B 83 38 04 00 00            mov rax, qword ptr [rbx + 0x438]
00417A9A  8B 48 18                        mov ecx, dword ptr [rax + 0x18]
00417A9D  3B D1                           cmp edx, ecx
00417A9F  0F 83 99 FC FF FF               jae 0x14041773e
00417AA5  48 8B 83 38 04 00 00            mov rax, qword ptr [rbx + 0x438]
00417AAC  8B CA                           mov ecx, edx
00417AAE  66 44 39 54 48 1C               cmp word ptr [rax + rcx*2 + 0x1c], r10w
00417AB4  0F 84 83 00 00 00               je 0x140417b3d
00417ABA  FF C2                           inc edx
00417ABC  EB D5                           jmp 0x140417a93
00417ABE  F0 FF 4A 0C                     lock dec dword ptr [rdx + 0xc]
00417AC2  E9 19 FC FF FF                  jmp 0x1404176e0
00417AC7  48 8D 45 58                     lea rax, [rbp + 0x58]
00417ACB  C7 44 24 28 05 5A 50 00         mov dword ptr [rsp + 0x28], 0x505a05
00417AD3  41 8B D2                        mov edx, r10d
00417AD6  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00417ADB  4C 8D 4D E0                     lea r9, [rbp - 0x20]
00417ADF  41 B8 1C 00 00 00               mov r8d, 0x1c
00417AE5  48 8B CF                        mov rcx, rdi
00417AE8  E8 AF 05 00 00                  call 0x14041809c
00417AED  48 8B D0                        mov rdx, rax
00417AF0  45 33 C9                        xor r9d, r9d
00417AF3  E9 C7 FC FF FF                  jmp 0x1404177bf
00417AF8  48 8D 45 58                     lea rax, [rbp + 0x58]
00417AFC  C7 44 24 28 05 5A 50 00         mov dword ptr [rsp + 0x28], 0x505a05
00417B04  41 8B D2                        mov edx, r10d
00417B07  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00417B0C  4C 8D 4D E0                     lea r9, [rbp - 0x20]
00417B10  41 B8 1C 00 00 00               mov r8d, 0x1c
00417B16  48 8B CB                        mov rcx, rbx
00417B19  E8 B2 53 EE FF                  call 0x1402fced0
00417B1E  EB CD                           jmp 0x140417aed
00417B20  41 B9 05 5A 50 00               mov r9d, 0x505a05
00417B26  48 8D 55 58                     lea rdx, [rbp + 0x58]
00417B2A  4C 8B C6                        mov r8, rsi
00417B2D  48 8B CB                        mov rcx, rbx
00417B30  E8 CB FF ED FF                  call 0x1402f7b00
00417B35  45 33 C9                        xor r9d, r9d
00417B38  E9 EB FB FF FF                  jmp 0x140417728
00417B3D  41 B9 05 5A 50 00               mov r9d, 0x505a05
00417B43  48 8D 55 58                     lea rdx, [rbp + 0x58]
00417B47  4C 8B C6                        mov r8, rsi
00417B4A  48 8B CB                        mov rcx, rbx
00417B4D  E8 DE 05 00 00                  call 0x140418130
00417B52  45 33 C9                        xor r9d, r9d
00417B55  41 BA 24 05 00 00               mov r10d, 0x524
00417B5B  E9 DE FB FF FF                  jmp 0x14041773e
00417B60  41 B9 05 5A 50 00               mov r9d, 0x505a05
00417B66  48 8D 55 58                     lea rdx, [rbp + 0x58]
00417B6A  4C 8B C6                        mov r8, rsi
00417B6D  48 8B CB                        mov rcx, rbx
00417B70  E8 7F 08 0C 00                  call 0x1404d83f4
00417B75  E9 9B FB FF FF                  jmp 0x140417715
00417B7A  BF 24 05 00 00                  mov edi, 0x524
00417B7F  48 8B 0D BA 7C AE 00            mov rcx, qword ptr [rip + 0xae7cba]
00417B86  48 8D 15 5B 8A BF FF            lea rdx, [rip - 0x4075a5]
00417B8D  E8 BE A8 F7 FF                  call 0x140392450
00417B92  45 33 C9                        xor r9d, r9d
00417B95  84 C0                           test al, al
00417B97  74 BC                           je 0x140417b55
00417B99  48 8D 93 88 00 00 00            lea rdx, [rbx + 0x88]
00417BA0  8B CF                           mov ecx, edi
00417BA2  41 B9 17 00 00 C0               mov r9d, 0xc0000017
00417BA8  41 B8 05 5A 50 00               mov r8d, 0x505a05
00417BAE  E8 31 BC 0A 00                  call 0x1404c37e4
00417BB3  EB 9D                           jmp 0x140417b52
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpLogContextSwapEvent(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p28;
    unsigned int v_stack_p8;

    v_stack_p10 = v_rbx;
    v_rsp = (v_rsp) - (80);
    a4 = 0;
    result = 0;
    v_stack_p20 = 0;
    v_stack_m48 = 0;
    v_stack_p8 = (unsigned int)(a3);
    v_stack_m58 = v_xmm0;
    if (condition_is_equal) goto loc_00417752;
loc_00417646:
    v_r13 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 4520))) & ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4520)) - 1)));
    result = ((unsigned int)((unsigned int)(a3))) << (5);
    result = (result) + (0x11CCULL);
    result = (result) + (a1);
    if (condition_is_equal) goto loc_00417744;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 4)))) & (4)) == 0) goto loc_00417744;
    if (((unsigned int)(*(unsigned __int8 *)(a1 + a3 * 2 + 4504))) >= (*(unsigned int *)(a1 + 16))) goto loc_00417744;
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 712) + (unsigned int)((unsigned int)(*(unsigned __int8 *)(a1 + a3 * 2 + 4504))) * 8))) & (1)) != 0) goto loc_00417744;
    result = ((unsigned int)(v_stack_p8)) << (5);
    result = (result) + (0x11CCULL);
    result = (result) + (a1);
    if (condition_is_equal) goto loc_0041776B;
    if (((*(unsigned int *)(result + 4)) & (256)) == 0) goto loc_0041776B;
    v_rbx = (unsigned int)((1) << ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 712) + (unsigned int)((unsigned int)(*(unsigned __int8 *)(a1 + a3 * 2 + 4504))) * 8) + 200)))));
    result = (unsigned int)(~(0));
    if ((((unsigned int)(v_rbx)) & ((unsigned int)(result))) != 0) goto loc_004179DB;
loc_004176D8:
loc_004176E0:
    if (a3 == 0) goto loc_00417B55;
    if (!sign_flag) goto loc_00417707;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 712) + (unsigned int)((unsigned int)(*(unsigned __int8 *)(a1 + a3 * 2 + 4504))) * 8) + 1048) + 164)) & (16)) != 0) goto loc_00417A08;
loc_00417707:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 712) + (unsigned int)((unsigned int)(*(unsigned __int8 *)(a1 + a3 * 2 + 4504))) * 8) + 820)))) & (2)) != 0) goto loc_00417A6B;
loc_00417715:
    a4 = 0;
    if (((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 712) + (unsigned int)((unsigned int)(*(unsigned __int8 *)(a1 + a3 * 2 + 4504))) * 8) + 816)) & (0x8000ULL)) != 0) goto loc_00417A37;
loc_00417728:
    if (((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 712) + (unsigned int)((unsigned int)(*(unsigned __int8 *)(a1 + a3 * 2 + 4504))) * 8) + 816)) & (0x4000000ULL)) != 0) goto loc_00417A90;
loc_0041773E:
loc_00417744:
    v_stack_p8 = (unsigned int)(a3);
    if (((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 712) + (unsigned int)((unsigned int)(*(unsigned __int8 *)(a1 + a3 * 2 + 4504))) * 8) + 816)) & (0x4000000ULL)) != 0) goto loc_00417646;
loc_00417752:
    v_rsp = (v_rsp) + (80);
    return (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 712) + (unsigned int)((unsigned int)(*(unsigned __int8 *)(a1 + a3 * 2 + 4504))) * 8) + 820));
loc_0041776B:
    if ((((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(0x524ULL) + 816)))) & (0xC00ULL)) != 0) goto loc_00417948;
loc_0041777F:
    v_stack_p20 = 0x505A05ULL;
    result = EtwpReserveTraceBuffer((unsigned int)(0x524ULL), 44, v_stack_m58, v_stack_p20);
    a4 = 0;
    if (result == 0) goto loc_00417B7A;
    *(unsigned __int64 *)(result + 8) = v_stack_p20;
    *(unsigned int *)(result) = 0xC0110005ULL;
    *(unsigned int *)(result + 4) = 0x524002CULL;
loc_004177BF:
    if (result + 16 == 0) goto loc_00417B7F;
    result = 0;
    *(unsigned __int64 *)(result + 16) = v_xmm0;
    *(unsigned __int64 *)(result + 16 + 16) = 0;
    *(unsigned int *)(result + 16 + 24) = 0;
    if (a2 == 0) goto loc_004178A3;
    *(unsigned int *)(result + 16 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 1296)));
    *(unsigned __int8 *)(result + 16 + 9) = (unsigned __int8)(*(unsigned __int8 *)(a2 + 195));
    *(unsigned __int8 *)(result + 16 + 12) = (unsigned __int8)(*(unsigned __int8 *)(a2 + 643));
    a1 = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(result + 16 + 13))) ^ (*(unsigned __int8 *)(a2 + 391)));
    a1 = (unsigned __int8)((a1) & (1));
    a1 = (unsigned __int8)((a1) ^ ((unsigned __int8)(*(unsigned __int8 *)(result + 16 + 13))));
    *(unsigned __int8 *)(result + 16 + 13) = (unsigned __int8)(a1);
    *(unsigned __int8 *)(result + 16 + 14) = (unsigned __int8)(*(unsigned __int8 *)(a2 + 388));
    *(unsigned __int8 *)(result + 16 + 15) = (unsigned __int8)(*(unsigned __int8 *)(a2 + 588));
    a1 = (unsigned __int8)((*(unsigned __int8 *)(a2 + 516)) + ((unsigned __int8)(*(unsigned __int8 *)(a2 + 516))));
    a1 = (unsigned __int8)((a1) ^ ((unsigned __int8)(*(unsigned __int8 *)(result + 16 + 13))));
    a1 = (unsigned __int8)((a1) & (14));
    a1 = (unsigned __int8)((a1) ^ ((unsigned __int8)(*(unsigned __int8 *)(result + 16 + 13))));
    *(unsigned __int8 *)(result + 16 + 13) = (unsigned __int8)(a1);
    a1 = (*(unsigned __int64 *)(a2 + 32)) - (*(unsigned __int64 *)(a2 + 72));
    a1 = (a1) >> (10);
    *(unsigned int *)(result + 16 + 20) = (unsigned int)(a1);
    if (a2 != (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 24))) goto loc_00417993;
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34880);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34880) != 0) {
        result = *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34880) + 28);
        *(unsigned __int8 *)(result + 16 + 10) = (unsigned __int8)(result);
    }
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 484))) != 0) goto loc_0041798A;
loc_00417887:
    if ((*(unsigned __int16 *)(a2 + 486)) != 0) goto loc_00417A2E;
    if ((*(unsigned __int8 *)(a2 + 390)) >= 1) goto loc_00417A2E;
loc_004178A3:
    if (a3 == 0) goto loc_00417915;
    *(unsigned int *)(result + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(a3 + 1296)));
    *(unsigned __int8 *)(result + 16 + 8) = (unsigned __int8)(*(unsigned __int8 *)(a3 + 195));
    *(unsigned __int8 *)(result + 16 + 11) = (unsigned __int8)(*(unsigned __int8 *)(a3 + 518));
    a1 = (unsigned __int8)((*(unsigned __int8 *)(a3 + 516)) << (4));
    a1 = (unsigned __int8)((a1) ^ ((unsigned __int8)(*(unsigned __int8 *)(result + 16 + 13))));
    a1 = (unsigned __int8)((a1) & (112));
    a1 = (unsigned __int8)((a1) ^ ((unsigned __int8)(*(unsigned __int8 *)(result + 16 + 13))));
    *(unsigned __int8 *)(result + 16 + 13) = (unsigned __int8)(a1);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int8 *)(result + 16 + 13)))) - (*(unsigned int *)(a3 + 436)));
    *(unsigned int *)(result + 16 + 16) = (unsigned int)(result);
    if ((*(unsigned int *)(a3 + 484)) != 0) goto loc_00417A25;
loc_004178FA:
    if ((*(unsigned __int16 *)(a3 + 486)) != 0) goto loc_004179D2;
    if ((*(unsigned __int8 *)(a3 + 390)) >= 1) goto loc_004179D2;
loc_00417915:
loc_0041791F:
    a1 = (v_stack_m58) ^ (*(unsigned __int64 *)(v_stack_m50));
    if (a1 >= 15) goto loc_00417ABE;
    if (a1 == 15) goto loc_004176E0;
    goto loc_0041791F;
loc_00417948:
    if (a1 < 15) goto loc_00417AC7;
    if (a1 >= 15) goto loc_0041777F;
loc_0041795F:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned int)(0x524ULL) + 1064) + 8))))) goto loc_0041777F;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)((unsigned int)(0x524ULL) + 1064) + 0 * 2 + 12)) == ((unsigned __int16)((unsigned int)(0x524ULL)))) goto loc_00417AF8;
    a2 = (unsigned int)((0) + 1);
    goto loc_0041795F;
loc_0041798A:
    goto loc_00417887;
loc_00417993:
    if (*(unsigned __int64 *)(a2 + 104) == 0) goto loc_004179C7;
    result = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned int)(0x524ULL) + 1064) + 216))) + (*(unsigned __int64 *)(a2 + 104));
loc_004179A5:
    if ((*(unsigned int *)(result + 124)) > 255) goto loc_00417A64;
    if ((unsigned __int8)(*(unsigned __int8 *)(result + 124)) != 0) goto loc_004179CA;
    if (*(unsigned __int64 *)(result + 416) != 0) goto loc_004179A5;
    goto loc_004179CA;
loc_004179C7:
loc_004179CA:
    *(unsigned __int8 *)(a2 + 10) = 0;
    goto loc_00417878;
loc_004179D2:
    goto loc_00417915;
loc_004179DB:
    result = EtwpGetLoggerTimeStamp((unsigned int)(0x524ULL), a2, v_stack_m58, a4);
    v_stack_p20 = result;
    result = EtwpCCSwapTrace(a2, a3, (unsigned int)(*(unsigned int *)((unsigned int)(0x524ULL) + 200)), v_stack_p20);
    v_r12 = (unsigned int)((0) | ((unsigned int)((unsigned int)(0x524ULL))));
    a4 = 0;
    goto loc_004176D8;
loc_00417A08:
    result = EtwpStackTraceDispatcher((unsigned int)(0x524ULL), v_stack_p20, a3, (unsigned int)(0x505A05ULL));
    a4 = 0;
    goto loc_00417707;
loc_00417A25:
    goto loc_004178FA;
loc_00417A2E:
    goto loc_004178A3;
loc_00417A37:
loc_00417A3A:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned int)(0x524ULL) + 1072) + 8))))) goto loc_00417728;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)((unsigned int)(0x524ULL) + 1072) + 0 * 2 + 12)) == ((unsigned __int16)((unsigned int)(0x524ULL)))) goto loc_00417B20;
    a2 = (unsigned int)((0) + 1);
    goto loc_00417A3A;
loc_00417A64:
    goto loc_004179CA;
loc_00417A6B:
loc_00417A6E:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(0x524ULL) + 1284))))) goto loc_00417715;
    if ((*(unsigned __int16 *)((unsigned int)(0x524ULL) + 0 * 2 + 1288)) == ((unsigned __int16)((unsigned int)(0x524ULL)))) goto loc_00417B60;
    a1 = (unsigned int)((0) + 1);
    goto loc_00417A6E;
loc_00417A90:
loc_00417A93:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned int)(0x524ULL) + 1080) + 24))))) goto loc_0041773E;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)((unsigned int)(0x524ULL) + 1080) + 0 * 2 + 28)) == ((unsigned __int16)((unsigned int)(0x524ULL)))) goto loc_00417B3D;
    a2 = (unsigned int)((0) + 1);
    goto loc_00417A93;
loc_00417ABE:
    goto loc_004176E0;
loc_00417AC7:
    v_stack_p28 = 0x505A05ULL;
    v_stack_p20 = v_stack_p20;
    result = EtwpReserveWithPebsIndex((unsigned int)(0x524ULL), (unsigned int)((unsigned int)((unsigned int)(0x524ULL))), 28, v_stack_m58);
loc_00417AED:
    a4 = 0;
    goto loc_004177BF;
loc_00417AF8:
    v_stack_p28 = 0x505A05ULL;
    v_stack_p20 = v_stack_p20;
    result = EtwpReserveWithPmcCounters((unsigned int)(0x524ULL), (unsigned int)((unsigned int)((unsigned int)(0x524ULL))), 28, v_stack_m58);
    goto loc_00417AED;
loc_00417B20:
    result = EtwpTraceLastBranchRecord((unsigned int)(0x524ULL), v_stack_p20, a3, (unsigned int)(0x505A05ULL));
    a4 = 0;
    goto loc_00417728;
loc_00417B3D:
    result = EtwpTraceProcessorTrace((unsigned int)(0x524ULL), v_stack_p20, a3, (unsigned int)(0x505A05ULL));
loc_00417B52:
    a4 = 0;
loc_00417B55:
    goto loc_0041773E;
loc_00417B60:
    result = EtwpContextRegisterTracingDispatcher((unsigned int)(0x524ULL), v_stack_p20, a3, (unsigned int)(0x505A05ULL));
    goto loc_00417715;
loc_00417B7A:
loc_00417B7F:
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 11435194), v_rip - 4224421, a3, (unsigned int)(0x505A05ULL));
    a4 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_00417B55;
    result = EtwpTraceLostSystemEvent((unsigned int)((unsigned int)((unsigned int)(0x524ULL))), (unsigned int)(0x524ULL) + 136, (unsigned int)(0x505A05ULL), (unsigned int)(0xC0000017ULL));
    goto loc_00417B52;
}
```

## 5. (Beta) C Style

```c
int64_t EtwpLogContextSwapEvent(void *Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_p10;
    uint64_t v_stack_p20;
    uint32_t v_stack_p28;
    uint32_t v_stack_p8;

    v_stack_p10 = local_rbx;
    local_rsp = (local_rsp) - (80);
    Arg4 = 0;
    result = 0;
    v_stack_p20 = 0;
    v_stack_m48 = 0;
    v_stack_p8 = (uint32_t)(Arg3);
    v_stack_m58 = v_xmm0;
    if (condition_is_equal) goto loc_00417752;
loc_00417646:
    local_r13 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x11A8))) & ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x11A8)) - 1)));
    result = ((uint32_t)((uint32_t)(Arg3))) << (5);
    result = (result) + (0x11CCULL);
    result = (result) + (Arg1);
    if (condition_is_equal) goto loc_00417744;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0x4)))) & (4)) == 0) goto loc_00417744;
    if (((uint32_t)(*(uint8_t *)(arg1 + Arg3 * 2 + 0x1198))) >= (*(uint32_t *)(arg1 + 0x10))) goto loc_00417744;
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x2C8) + (uint32_t)((uint32_t)(*(uint8_t *)(arg1 + Arg3 * 2 + 0x1198))) * 8))) & (1)) != 0) goto loc_00417744;
    result = ((uint32_t)(v_stack_p8)) << (5);
    result = (result) + (0x11CCULL);
    result = (result) + (Arg1);
    if (condition_is_equal) goto loc_0041776B;
    if (((*(uint32_t *)(result + 0x4)) & (256)) == 0) goto loc_0041776B;
    local_rbx = (uint32_t)((1) << ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x2C8) + (uint32_t)((uint32_t)(*(uint8_t *)(arg1 + Arg3 * 2 + 0x1198))) * 8) + 0xC8)))));
    result = (uint32_t)(~(0));
    if ((((uint32_t)(local_rbx)) & ((uint32_t)(result))) != 0) goto loc_004179DB;
loc_004176D8:
loc_004176E0:
    if (Arg3 == 0) goto loc_00417B55;
    if (!sign_flag) goto loc_00417707;
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x2C8) + (uint32_t)((uint32_t)(*(uint8_t *)(arg1 + Arg3 * 2 + 0x1198))) * 8) + 0x418) + 0xA4)) & (16)) != 0) goto loc_00417A08;
loc_00417707:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x2C8) + (uint32_t)((uint32_t)(*(uint8_t *)(arg1 + Arg3 * 2 + 0x1198))) * 8) + 0x334)))) & (2)) != 0) goto loc_00417A6B;
loc_00417715:
    Arg4 = 0;
    if (((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x2C8) + (uint32_t)((uint32_t)(*(uint8_t *)(arg1 + Arg3 * 2 + 0x1198))) * 8) + 0x330)) & (0x8000ULL)) != 0) goto loc_00417A37;
loc_00417728:
    if (((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x2C8) + (uint32_t)((uint32_t)(*(uint8_t *)(arg1 + Arg3 * 2 + 0x1198))) * 8) + 0x330)) & (0x4000000ULL)) != 0) goto loc_00417A90;
loc_0041773E:
loc_00417744:
    v_stack_p8 = (uint32_t)(Arg3);
    if (((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x2C8) + (uint32_t)((uint32_t)(*(uint8_t *)(arg1 + Arg3 * 2 + 0x1198))) * 8) + 0x330)) & (0x4000000ULL)) != 0) goto loc_00417646;
loc_00417752:
    local_rsp = (local_rsp) + (80);
    return (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x2C8) + (uint32_t)((uint32_t)(*(uint8_t *)(arg1 + Arg3 * 2 + 0x1198))) * 8) + 0x334));
loc_0041776B:
    if ((((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(0x524ULL) + 0x330)))) & (0xC00ULL)) != 0) goto loc_00417948;
loc_0041777F:
    v_stack_p20 = 0x505A05ULL;
    result = EtwpReserveTraceBuffer((uint32_t)(0x524ULL), 44, v_stack_m58, v_stack_p20);
    Arg4 = 0;
    if (result == 0) goto loc_00417B7A;
    *(uint64_t *)(result + 0x8) = v_stack_p20;
    *(uint32_t *)(result) = 0xC0110005ULL;
    *(uint32_t *)(result + 0x4) = 0x524002CULL;
loc_004177BF:
    if (result + 16 == 0) goto loc_00417B7F;
    result = 0;
    *(uint64_t *)(result + 0x10) = v_xmm0;
    *(uint64_t *)(result + 0x10 + 0x10) = 0;
    *(uint32_t *)(result + 0x10 + 0x18) = 0;
    if (Arg2 == 0) goto loc_004178A3;
    *(uint32_t *)(result + 0x10 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0x510)));
    *(uint8_t *)(result + 0x10 + 0x9) = (uint8_t)(*(uint8_t *)(Arg2 + 0xC3));
    *(uint8_t *)(result + 0x10 + 0xC) = (uint8_t)(*(uint8_t *)(Arg2 + 0x283));
    Arg1 = (uint8_t)(((uint8_t)(*(uint8_t *)(result + 0x10 + 0xD))) ^ (*(uint8_t *)(Arg2 + 0x187)));
    Arg1 = (uint8_t)((Arg1) & (1));
    Arg1 = (uint8_t)((Arg1) ^ ((uint8_t)(*(uint8_t *)(result + 0x10 + 0xD))));
    *(uint8_t *)(result + 0x10 + 0xD) = (uint8_t)(Arg1);
    *(uint8_t *)(result + 0x10 + 0xE) = (uint8_t)(*(uint8_t *)(Arg2 + 0x184));
    *(uint8_t *)(result + 0x10 + 0xF) = (uint8_t)(*(uint8_t *)(Arg2 + 0x24C));
    Arg1 = (uint8_t)((*(uint8_t *)(Arg2 + 0x204)) + ((uint8_t)(*(uint8_t *)(Arg2 + 0x204))));
    Arg1 = (uint8_t)((Arg1) ^ ((uint8_t)(*(uint8_t *)(result + 0x10 + 0xD))));
    Arg1 = (uint8_t)((Arg1) & (14));
    Arg1 = (uint8_t)((Arg1) ^ ((uint8_t)(*(uint8_t *)(result + 0x10 + 0xD))));
    *(uint8_t *)(result + 0x10 + 0xD) = (uint8_t)(Arg1);
    Arg1 = (*(uint64_t *)(Arg2 + 0x20)) - (*(uint64_t *)(Arg2 + 0x48));
    Arg1 = (Arg1) >> (10);
    *(uint32_t *)(result + 0x10 + 0x14) = (uint32_t)(Arg1);
    if (Arg2 != (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x18))) goto loc_00417993;
    result = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8840);
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8840) != 0) {
        result = *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8840) + 0x1C);
        *(uint8_t *)(result + 0x10 + 0xA) = (uint8_t)(result);
    }
    if ((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0x1E4))) != 0) goto loc_0041798A;
loc_00417887:
    if ((*(uint16_t *)(Arg2 + 0x1E6)) != 0) goto loc_00417A2E;
    if ((*(uint8_t *)(Arg2 + 0x186)) >= 1) goto loc_00417A2E;
loc_004178A3:
    if (Arg3 == 0) goto loc_00417915;
    *(uint32_t *)(result + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg3 + 0x510)));
    *(uint8_t *)(result + 0x10 + 0x8) = (uint8_t)(*(uint8_t *)(Arg3 + 0xC3));
    *(uint8_t *)(result + 0x10 + 0xB) = (uint8_t)(*(uint8_t *)(Arg3 + 0x206));
    Arg1 = (uint8_t)((*(uint8_t *)(Arg3 + 0x204)) << (4));
    Arg1 = (uint8_t)((Arg1) ^ ((uint8_t)(*(uint8_t *)(result + 0x10 + 0xD))));
    Arg1 = (uint8_t)((Arg1) & (112));
    Arg1 = (uint8_t)((Arg1) ^ ((uint8_t)(*(uint8_t *)(result + 0x10 + 0xD))));
    *(uint8_t *)(result + 0x10 + 0xD) = (uint8_t)(Arg1);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint8_t *)(result + 0x10 + 0xD)))) - (*(uint32_t *)(Arg3 + 0x1B4)));
    *(uint32_t *)(result + 0x10 + 0x10) = (uint32_t)(result);
    if ((*(uint32_t *)(Arg3 + 0x1E4)) != 0) goto loc_00417A25;
loc_004178FA:
    if ((*(uint16_t *)(Arg3 + 0x1E6)) != 0) goto loc_004179D2;
    if ((*(uint8_t *)(Arg3 + 0x186)) >= 1) goto loc_004179D2;
loc_00417915:
loc_0041791F:
    Arg1 = (v_stack_m58) ^ (*(uint64_t *)(v_stack_m50));
    if (Arg1 >= 15) goto loc_00417ABE;
    if (Arg1 == 15) goto loc_004176E0;
    goto loc_0041791F;
loc_00417948:
    if (Arg1 < 15) goto loc_00417AC7;
    if (Arg1 >= 15) goto loc_0041777F;
loc_0041795F:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)((uint32_t)(0x524ULL) + 0x428) + 0x8))))) goto loc_0041777F;
    if ((*(uint16_t *)(*(uint64_t *)((uint32_t)(0x524ULL) + 0x428) + 0x0 * 2 + 0xC)) == ((uint16_t)((uint32_t)(0x524ULL)))) goto loc_00417AF8;
    Arg2 = (uint32_t)((0) + 1);
    goto loc_0041795F;
loc_0041798A:
    goto loc_00417887;
loc_00417993:
    if (*(uint64_t *)(Arg2 + 0x68) == 0) goto loc_004179C7;
    result = ((uint32_t)(*(uint32_t *)(*(uint64_t *)((uint32_t)(0x524ULL) + 0x428) + 0xD8))) + (*(uint64_t *)(Arg2 + 0x68));
loc_004179A5:
    if ((*(uint32_t *)(result + 0x7C)) > 255) goto loc_00417A64;
    if ((uint8_t)(*(uint8_t *)(result + 0x7C)) != 0) goto loc_004179CA;
    if (*(uint64_t *)(result + 0x1A0) != 0) goto loc_004179A5;
    goto loc_004179CA;
loc_004179C7:
loc_004179CA:
    *(uint8_t *)(Arg2 + 0xA) = 0;
    goto loc_00417878;
loc_004179D2:
    goto loc_00417915;
loc_004179DB:
    result = EtwpGetLoggerTimeStamp((uint32_t)(0x524ULL), Arg2, v_stack_m58, Arg4);
    v_stack_p20 = result;
    result = EtwpCCSwapTrace(Arg2, Arg3, (uint32_t)(*(uint32_t *)((uint32_t)(0x524ULL) + 0xC8)), v_stack_p20);
    local_r12 = (uint32_t)((0) | ((uint32_t)((uint32_t)(0x524ULL))));
    Arg4 = 0;
    goto loc_004176D8;
loc_00417A08:
    result = EtwpStackTraceDispatcher((uint32_t)(0x524ULL), v_stack_p20, Arg3, (uint32_t)(0x505A05ULL));
    Arg4 = 0;
    goto loc_00417707;
loc_00417A25:
    goto loc_004178FA;
loc_00417A2E:
    goto loc_004178A3;
loc_00417A37:
loc_00417A3A:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)((uint32_t)(0x524ULL) + 0x430) + 0x8))))) goto loc_00417728;
    if ((*(uint16_t *)(*(uint64_t *)((uint32_t)(0x524ULL) + 0x430) + 0x0 * 2 + 0xC)) == ((uint16_t)((uint32_t)(0x524ULL)))) goto loc_00417B20;
    Arg2 = (uint32_t)((0) + 1);
    goto loc_00417A3A;
loc_00417A64:
    goto loc_004179CA;
loc_00417A6B:
loc_00417A6E:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(0x524ULL) + 0x504))))) goto loc_00417715;
    if ((*(uint16_t *)((uint32_t)(0x524ULL) + 0x0 * 2 + 0x508)) == ((uint16_t)((uint32_t)(0x524ULL)))) goto loc_00417B60;
    Arg1 = (uint32_t)((0) + 1);
    goto loc_00417A6E;
loc_00417A90:
loc_00417A93:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)((uint32_t)(0x524ULL) + 0x438) + 0x18))))) goto loc_0041773E;
    if ((*(uint16_t *)(*(uint64_t *)((uint32_t)(0x524ULL) + 0x438) + 0x0 * 2 + 0x1C)) == ((uint16_t)((uint32_t)(0x524ULL)))) goto loc_00417B3D;
    Arg2 = (uint32_t)((0) + 1);
    goto loc_00417A93;
loc_00417ABE:
    goto loc_004176E0;
loc_00417AC7:
    v_stack_p28 = 0x505A05ULL;
    v_stack_p20 = v_stack_p20;
    result = EtwpReserveWithPebsIndex((uint32_t)(0x524ULL), (uint32_t)((uint32_t)((uint32_t)(0x524ULL))), 28, v_stack_m58);
loc_00417AED:
    Arg4 = 0;
    goto loc_004177BF;
loc_00417AF8:
    v_stack_p28 = 0x505A05ULL;
    v_stack_p20 = v_stack_p20;
    result = EtwpReserveWithPmcCounters((uint32_t)(0x524ULL), (uint32_t)((uint32_t)((uint32_t)(0x524ULL))), 28, v_stack_m58);
    goto loc_00417AED;
loc_00417B20:
    result = EtwpTraceLastBranchRecord((uint32_t)(0x524ULL), v_stack_p20, Arg3, (uint32_t)(0x505A05ULL));
    Arg4 = 0;
    goto loc_00417728;
loc_00417B3D:
    result = EtwpTraceProcessorTrace((uint32_t)(0x524ULL), v_stack_p20, Arg3, (uint32_t)(0x505A05ULL));
loc_00417B52:
    Arg4 = 0;
loc_00417B55:
    goto loc_0041773E;
loc_00417B60:
    result = EtwpContextRegisterTracingDispatcher((uint32_t)(0x524ULL), v_stack_p20, Arg3, (uint32_t)(0x505A05ULL));
    goto loc_00417715;
loc_00417B7A:
loc_00417B7F:
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0xAE7CBA), v_rip - 4224421, Arg3, (uint32_t)(0x505A05ULL));
    Arg4 = 0;
    if ((uint8_t)(result) == 0) goto loc_00417B55;
    result = EtwpTraceLostSystemEvent((uint32_t)((uint32_t)((uint32_t)(0x524ULL))), (uint32_t)(0x524ULL) + 136, (uint32_t)(0x505A05ULL), (uint32_t)(0xC0000017ULL));
    goto loc_00417B52;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x10` | `32` | `R` |
| `Arg1` | `+ 0x2C8` | `64` | `R` |
| `Arg1` | `+ 0x1198 + r8*2` | `8` | `R` |
| `Arg1` | `+ 0x11A8` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004175F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
