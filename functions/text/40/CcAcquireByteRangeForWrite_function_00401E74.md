# CcAcquireByteRangeForWrite

- RVA: `0x00401E74`–`0x00402911` (길이 `2,717` bytes)
- VA: `0x0000000140401E74`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0009A624`
- 디코드: `609`개 명령, `2,717/2,717` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **27**; 고유 호출 대상: **13**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00401F3E` → [ExAcquireFastMutex](../20/ExAcquireFastMutex_function_0020E5A0.md) (function, `0x0020E5A0`)
- `0x004020C1` → [KeAcquireInStackQueuedSpinLock](../27/KeAcquireInStackQueuedSpinLock_function_002757A0.md) (function, `0x002757A0`)
- `0x004020CD` → [CcDeductDirtyPages](../38/CcDeductDirtyPages_function_0038C20C.md) (function, `0x0038C20C`)
- `0x004020FA` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x00402134` → [ExReleaseFastMutex](../25/ExReleaseFastMutex_function_002519C0.md) (function, `0x002519C0`)
- `0x004021B9` → [CcFindBitmapRangeToClean](CcFindBitmapRangeToClean_function_00402AF4.md) (function, `0x00402AF4`)
- `0x0040228E` → [ExReleaseFastMutex](../25/ExReleaseFastMutex_function_002519C0.md) (function, `0x002519C0`)
- `0x004022D5` → [CcFindBcb](../34/CcFindBcb_function_00341800.md) (function, `0x00341800`)
- `0x00402342` → [CcFindBitmapRangeToClean](CcFindBitmapRangeToClean_function_00402AF4.md) (function, `0x00402AF4`)
- `0x00402468` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x004024F3` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00402543` → [CcUnpinFileDataEx](../35/CcUnpinFileDataEx_function_00359DEC.md) (function, `0x00359DEC`)
- `0x00402595` → [ExReleaseFastMutex](../25/ExReleaseFastMutex_function_002519C0.md) (function, `0x002519C0`)
- `0x004025BC` → [CcUnpinFileDataEx](../35/CcUnpinFileDataEx_function_00359DEC.md) (function, `0x00359DEC`)
- `0x004025C8` → [ExAcquireFastMutex](../20/ExAcquireFastMutex_function_0020E5A0.md) (function, `0x0020E5A0`)
- `0x0040272A` → [ExAcquireResourceExclusiveLite](../21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)
- `0x0040273E` → [ExAcquireFastMutex](../20/ExAcquireFastMutex_function_0020E5A0.md) (function, `0x0020E5A0`)
- `0x0040278A` → [ExReleaseFastMutex](../25/ExReleaseFastMutex_function_002519C0.md) (function, `0x002519C0`)
- `0x00402797` → [CcUnpinFileDataEx](../35/CcUnpinFileDataEx_function_00359DEC.md) (function, `0x00359DEC`)
- `0x004027A3` → [ExAcquireFastMutex](../20/ExAcquireFastMutex_function_0020E5A0.md) (function, `0x0020E5A0`)
- `0x004027F1` → [CcUnpinFileDataEx](../35/CcUnpinFileDataEx_function_00359DEC.md) (function, `0x00359DEC`)
- `0x004027FD` → [ExAcquireFastMutex](../20/ExAcquireFastMutex_function_0020E5A0.md) (function, `0x0020E5A0`)
- `0x0040281C` → [PsBoostThreadIoEx](../39/PsBoostThreadIoEx_function_00392C00.md) (function, `0x00392C00`)
- `0x004028B1` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x004028BA` → [CcInsertIntoCleanSharedCacheMapList](../45/CcInsertIntoCleanSharedCacheMapList_function_004511CC.md) (function, `0x004511CC`)
- `0x004028E9` → [PsBoostThreadIoEx](../39/PsBoostThreadIoEx_function_00392C00.md) (function, `0x00392C00`)
- `0x0040290B` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)

### Direct callers
- [CcFlushCacheAcquireRange](../35/CcFlushCacheAcquireRange_function_0035A408.md) at `0x0035A4D6`
- [CcNotifyOfMappedWrite](CcNotifyOfMappedWrite_function_0040338C.md) at `0x00403619`

### Static image references
- `0x00401FE2` → RVA `0x00E65B20` (`.data`; read/write)
- `0x00402042` → RVA `0x00E65B24` (`.data`; read)
- `0x00402224` → RVA `0x00E0A870` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **4**
  - `0x00402858` → [sub_006EC13A](../6E/Unknown_function_006EC13A.md) (`tail-transfer`)
  - `0x00402865` → [sub_006EC13A](../6E/Unknown_function_006EC13A.md) (`tail-transfer`)
  - `0x0040288B` → [sub_006EC13A + 0x89](../6E/Unknown_function_006EC13A.md) (`tail-transfer`)
  - `0x00402894` → [sub_006EC13A + 0x8C](../6E/Unknown_function_006EC13A.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00401E74  4C 8B DC                        mov r11, rsp
00401E77  4D 89 4B 20                     mov qword ptr [r11 + 0x20], r9
00401E7B  45 89 43 18                     mov dword ptr [r11 + 0x18], r8d
00401E7F  49 89 53 10                     mov qword ptr [r11 + 0x10], rdx
00401E83  49 89 4B 08                     mov qword ptr [r11 + 8], rcx
00401E87  53                              push rbx
00401E88  56                              push rsi
00401E89  57                              push rdi
00401E8A  41 54                           push r12
00401E8C  41 55                           push r13
00401E8E  41 56                           push r14
00401E90  41 57                           push r15
00401E92  48 81 EC 20 01 00 00            sub rsp, 0x120
00401E99  41 8B F0                        mov esi, r8d
00401E9C  4C 8B E9                        mov r13, rcx
00401E9F  33 FF                           xor edi, edi
00401EA1  48 89 7C 24 58                  mov qword ptr [rsp + 0x58], rdi
00401EA6  49 89 BB 58 FF FF FF            mov qword ptr [r11 - 0xa8], rdi
00401EAD  8B C7                           mov eax, edi
00401EAF  89 44 24 54                     mov dword ptr [rsp + 0x54], eax
00401EB3  44 8B FF                        mov r15d, edi
00401EB6  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00401EBB  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00401EC0  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
00401EC4  44 8B F7                        mov r14d, edi
00401EC7  48 89 BC 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rdi
00401ECF  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00401ED4  48 BB FF FF FF FF FF FF FF 7F   movabs rbx, 0x7fffffffffffffff
00401EDE  48 89 9C 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rbx
00401EE6  0F 57 C0                        xorps xmm0, xmm0
00401EE9  41 0F 11 43 98                  movups xmmword ptr [r11 - 0x68], xmm0
00401EEE  49 89 43 A8                     mov qword ptr [r11 - 0x58], rax
00401EF2  40 38 BC 24 98 01 00 00         cmp byte ptr [rsp + 0x198], dil
00401EFA  0F 85 0B 09 00 00               jne 0x14040280b
00401F00  49 8B 85 18 02 00 00            mov rax, qword ptr [r13 + 0x218]
00401F07  48 89 84 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rax
00401F0F  48 89 84 24 E8 00 00 00         mov qword ptr [rsp + 0xe8], rax
00401F17  48 8B 84 24 80 01 00 00         mov rax, qword ptr [rsp + 0x180]
00401F1F  48 89 38                        mov qword ptr [rax], rdi
00401F22  4C 8B A4 24 88 01 00 00         mov r12, qword ptr [rsp + 0x188]
00401F2A  41 89 3C 24                     mov dword ptr [r12], edi
00401F2E  4D 85 C9                        test r9, r9
00401F31  0F 85 20 05 00 00               jne 0x140402457
00401F37  49 8D 8D 20 01 00 00            lea rcx, [r13 + 0x120]
00401F3E  E8 5D C6 E0 FF                  call 0x14020e5a0
00401F43  4D 8B 95 A8 00 00 00            mov r10, qword ptr [r13 + 0xa8]
00401F4A  4C 89 54 24 78                  mov qword ptr [rsp + 0x78], r10
00401F4F  4D 85 D2                        test r10, r10
00401F52  74 0A                           je 0x140401f5e
00401F54  41 39 7A 08                     cmp dword ptr [r10 + 8], edi
00401F58  0F 85 23 02 00 00               jne 0x140402181
00401F5E  4C 8B 8C 24 68 01 00 00         mov r9, qword ptr [rsp + 0x168]
00401F66  49 8D 8D D0 00 00 00            lea rcx, [r13 + 0xd0]
00401F6D  4D 8D 45 10                     lea r8, [r13 + 0x10]
00401F71  48 8B 9C 24 B0 00 00 00         mov rbx, qword ptr [rsp + 0xb0]
00401F79  49 8B 75 18                     mov rsi, qword ptr [r13 + 0x18]
00401F7D  48 83 EE 10                     sub rsi, 0x10
00401F81  48 89 74 24 58                  mov qword ptr [rsp + 0x58], rsi
00401F86  41 F7 85 98 00 00 00 00 02 00 00  test dword ptr [r13 + 0x98], 0x200
00401F91  0F 85 0A 03 00 00               jne 0x1404022a1
00401F97  48 8B 94 24 78 01 00 00         mov rdx, qword ptr [rsp + 0x178]
00401F9F  4C 8B 8C 24 68 01 00 00         mov r9, qword ptr [rsp + 0x168]
00401FA7  48 8D 46 10                     lea rax, [rsi + 0x10]
00401FAB  49 3B C0                        cmp rax, r8
00401FAE  74 74                           je 0x140402024
00401FB0  B8 FD 02 00 00                  mov eax, 0x2fd
00401FB5  66 39 06                        cmp word ptr [rsi], ax
00401FB8  75 4B                           jne 0x140402005
00401FBA  41 F7 85 98 00 00 00 00 00 00 01  test dword ptr [r13 + 0x98], 0x1000000
00401FC5  74 23                           je 0x140401fea
00401FC7  48 85 D2                        test rdx, rdx
00401FCA  74 1E                           je 0x140401fea
00401FCC  48 8B 02                        mov rax, qword ptr [rdx]
00401FCF  48 39 46 30                     cmp qword ptr [rsi + 0x30], rax
00401FD3  7E 15                           jle 0x140401fea
00401FD5  48 8B 76 18                     mov rsi, qword ptr [rsi + 0x18]
00401FD9  48 83 EE 10                     sub rsi, 0x10
00401FDD  48 89 74 24 58                  mov qword ptr [rsp + 0x58], rsi
00401FE2  FF 05 38 3B A6 00               inc dword ptr [rip + 0xa63b38]
00401FE8  EB BD                           jmp 0x140401fa7
00401FEA  4D 85 C9                        test r9, r9
00401FED  75 25                           jne 0x140402014
00401FEF  41 8B 04 24                     mov eax, dword ptr [r12]
00401FF3  85 C0                           test eax, eax
00401FF5  0F 85 1F 04 00 00               jne 0x14040241a
00401FFB  40 38 7E 02                     cmp byte ptr [rsi + 2], dil
00401FFF  0F 85 5F 05 00 00               jne 0x140402564
00402005  48 8B 76 18                     mov rsi, qword ptr [rsi + 0x18]
00402009  48 83 EE 10                     sub rsi, 0x10
0040200D  48 89 74 24 58                  mov qword ptr [rsp + 0x58], rsi
00402012  EB 93                           jmp 0x140401fa7
00402014  8B 84 24 70 01 00 00            mov eax, dword ptr [rsp + 0x170]
0040201B  49 03 01                        add rax, qword ptr [r9]
0040201E  48 3B 46 08                     cmp rax, qword ptr [rsi + 8]
00402022  7F CB                           jg 0x140401fef
00402024  48 8B 94 24 80 01 00 00         mov rdx, qword ptr [rsp + 0x180]
0040202C  39 7C 24 54                     cmp dword ptr [rsp + 0x54], edi
00402030  0F 84 36 02 00 00               je 0x14040226c
00402036  4C 8B 8C 24 68 01 00 00         mov r9, qword ptr [rsp + 0x168]
0040203E  8B 74 24 50                     mov esi, dword ptr [rsp + 0x50]
00402042  8B 05 DC 3A A6 00               mov eax, dword ptr [rip + 0xa63adc]
00402048  A8 01                           test al, 1
0040204A  0F 85 38 08 00 00               jne 0x140402888
00402050  8B 9C 24 70 01 00 00            mov ebx, dword ptr [rsp + 0x170]
00402057  4C 8B 94 24 68 01 00 00         mov r10, qword ptr [rsp + 0x168]
0040205F  4C 8B 4C 24 70                  mov r9, qword ptr [rsp + 0x70]
00402064  4C 8B 5C 24 60                  mov r11, qword ptr [rsp + 0x60]
00402069  45 8B 01                        mov r8d, dword ptr [r9]
0040206C  44 85 C6                        test esi, r8d
0040206F  0F 85 88 01 00 00               jne 0x1404021fd
00402075  41 8B 14 24                     mov edx, dword ptr [r12]
00402079  48 8B 5C 24 78                  mov rbx, qword ptr [rsp + 0x78]
0040207E  8B 43 04                        mov eax, dword ptr [rbx + 4]
00402081  8B C8                           mov ecx, eax
00402083  2B CA                           sub ecx, edx
00402085  3B D0                           cmp edx, eax
00402087  1B C0                           sbb eax, eax
00402089  23 C1                           and eax, ecx
0040208B  89 43 04                        mov dword ptr [rbx + 4], eax
0040208E  8B 43 08                        mov eax, dword ptr [rbx + 8]
00402091  41 8B 0C 24                     mov ecx, dword ptr [r12]
00402095  3B C1                           cmp eax, ecx
00402097  0F 82 56 08 00 00               jb 0x1404028f3
0040209D  2B C1                           sub eax, ecx
0040209F  89 43 08                        mov dword ptr [rbx + 8], eax
004020A2  41 8B 04 24                     mov eax, dword ptr [r12]
004020A6  41 29 47 20                     sub dword ptr [r15 + 0x20], eax
004020AA  48 8B B4 24 B8 00 00 00         mov rsi, qword ptr [rsp + 0xb8]
004020B2  48 8D 8E 00 03 00 00            lea rcx, [rsi + 0x300]
004020B9  48 8D 94 24 F0 00 00 00         lea rdx, [rsp + 0xf0]
004020C1  E8 DA 36 E7 FF                  call 0x1402757a0
004020C6  41 8B 14 24                     mov edx, dword ptr [r12]
004020CA  49 8B CD                        mov rcx, r13
004020CD  E8 3A A1 F8 FF                  call 0x14038c20c
004020D2  41 8B 0C 24                     mov ecx, dword ptr [r12]
004020D6  39 8E D0 03 00 00               cmp dword ptr [rsi + 0x3d0], ecx
004020DC  0F 87 F4 06 00 00               ja 0x1404027d6
004020E2  89 BE D0 03 00 00               mov dword ptr [rsi + 0x3d0], edi
004020E8  41 39 7D 70                     cmp dword ptr [r13 + 0x70], edi
004020EC  0F 84 C5 07 00 00               je 0x1404028b7
004020F2  48 8D 8C 24 F0 00 00 00         lea rcx, [rsp + 0xf0]
004020FA  E8 E1 0B F4 FF                  call 0x140342ce0
004020FF  41 39 7F 20                     cmp dword ptr [r15 + 0x20], edi
00402103  0F 85 8A 05 00 00               jne 0x140402693
00402109  41 83 4F 18 FF                  or dword ptr [r15 + 0x18], 0xffffffff
0040210E  41 89 7F 1C                     mov dword ptr [r15 + 0x1c], edi
00402112  49 8B 47 10                     mov rax, qword ptr [r15 + 0x10]
00402116  48 05 00 20 00 00               add rax, 0x2000
0040211C  48 89 43 20                     mov qword ptr [rbx + 0x20], rax
00402120  49 8D 45 10                     lea rax, [r13 + 0x10]
00402124  48 39 00                        cmp qword ptr [rax], rax
00402127  0F 84 30 01 00 00               je 0x14040225d
0040212D  49 8D 8D 20 01 00 00            lea rcx, [r13 + 0x120]
00402134  E8 87 F8 E4 FF                  call 0x1402519c0
00402139  41 C1 24 24 0C                  shl dword ptr [r12], 0xc
0040213E  49 C1 E6 0C                     shl r14, 0xc
00402142  48 8B 84 24 80 01 00 00         mov rax, qword ptr [rsp + 0x180]
0040214A  4C 89 30                        mov qword ptr [rax], r14
0040214D  48 8B 84 24 90 01 00 00         mov rax, qword ptr [rsp + 0x190]
00402155  48 89 38                        mov qword ptr [rax], rdi
00402158  40 38 BC 24 98 01 00 00         cmp byte ptr [rsp + 0x198], dil
00402160  0F 85 72 07 00 00               jne 0x1404028d8
00402166  41 39 3C 24                     cmp dword ptr [r12], edi
0040216A  0F 95 C0                        setne al
0040216D  48 81 C4 20 01 00 00            add rsp, 0x120
00402174  41 5F                           pop r15
00402176  41 5E                           pop r14
00402178  41 5D                           pop r13
0040217A  41 5C                           pop r12
0040217C  5F                              pop rdi
0040217D  5E                              pop rsi
0040217E  5B                              pop rbx
0040217F  C3                              ret
00402180  CC                              int3
00402181  41 39 7A 04                     cmp dword ptr [r10 + 4], edi
00402185  0F 84 D2 04 00 00               je 0x14040265d
0040218B  4C 8B 8C 24 68 01 00 00         mov r9, qword ptr [rsp + 0x168]
00402193  4D 85 C9                        test r9, r9
00402196  0F 84 84 01 00 00               je 0x140402320
0040219C  49 8B 09                        mov rcx, qword ptr [r9]
0040219F  4C 8B F1                        mov r14, rcx
004021A2  49 C1 FE 0C                     sar r14, 0xc
004021A6  8B C6                           mov eax, esi
004021A8  48 8D 59 FF                     lea rbx, [rcx - 1]
004021AC  48 03 D8                        add rbx, rax
004021AF  48 C1 FB 0C                     sar rbx, 0xc
004021B3  49 8B D6                        mov rdx, r14
004021B6  49 8B CA                        mov rcx, r10
004021B9  E8 36 09 00 00                  call 0x140402af4
004021BE  4C 8B F8                        mov r15, rax
004021C1  48 8B 40 10                     mov rax, qword ptr [rax + 0x10]
004021C5  41 8B 4F 18                     mov ecx, dword ptr [r15 + 0x18]
004021C9  48 03 C8                        add rcx, rax
004021CC  48 3B D9                        cmp rbx, rcx
004021CF  0F 8C 91 FD FF FF               jl 0x140401f66
004021D5  41 8B 4F 1C                     mov ecx, dword ptr [r15 + 0x1c]
004021D9  48 03 C1                        add rax, rcx
004021DC  4C 3B F0                        cmp r14, rax
004021DF  0F 8F 81 FD FF FF               jg 0x140401f66
004021E5  48 3B D8                        cmp rbx, rax
004021E8  49 8B 47 28                     mov rax, qword ptr [r15 + 0x28]
004021EC  0F 8D 70 01 00 00               jge 0x140402362
004021F2  8B CB                           mov ecx, ebx
004021F4  41 2B 4F 10                     sub ecx, dword ptr [r15 + 0x10]
004021F8  E9 65 01 00 00                  jmp 0x140402362
004021FD  4D 85 D2                        test r10, r10
00402200  0F 85 F1 00 00 00               jne 0x1404022f7
00402206  41 8B 4F 1C                     mov ecx, dword ptr [r15 + 0x1c]
0040220A  48 C1 E9 05                     shr rcx, 5
0040220E  49 8B 47 28                     mov rax, qword ptr [r15 + 0x28]
00402212  48 8D 0C 88                     lea rcx, [rax + rcx*4]
00402216  4C 3B C9                        cmp r9, rcx
00402219  0F 87 7A 06 00 00               ja 0x140402899
0040221F  4D 85 D2                        test r10, r10
00402222  75 10                           jne 0x140402234
00402224  8B 05 46 86 A0 00               mov eax, dword ptr [rip + 0xa08646]
0040222A  41 39 04 24                     cmp dword ptr [r12], eax
0040222E  0F 83 41 FE FF FF               jae 0x140402075
00402234  44 2B C6                        sub r8d, esi
00402237  45 89 01                        mov dword ptr [r9], r8d
0040223A  41 FF 04 24                     inc dword ptr [r12]
0040223E  03 F6                           add esi, esi
00402240  0F 85 23 FE FF FF               jne 0x140402069
00402246  49 83 C1 04                     add r9, 4
0040224A  BE 01 00 00 00                  mov esi, 1
0040224F  4D 3B CB                        cmp r9, r11
00402252  0F 87 1D FE FF FF               ja 0x140402075
00402258  E9 0C FE FF FF                  jmp 0x140402069
0040225D  8B 43 04                        mov eax, dword ptr [rbx + 4]
00402260  41 89 85 C8 00 00 00            mov dword ptr [r13 + 0xc8], eax
00402267  E9 C1 FE FF FF                  jmp 0x14040212d
0040226C  41 8B 04 24                     mov eax, dword ptr [r12]
00402270  85 C0                           test eax, eax
00402272  0F 84 F2 03 00 00               je 0x14040266a
00402278  48 83 BC 24 68 01 00 00 00      cmp qword ptr [rsp + 0x168], 0
00402281  0F 84 A3 03 00 00               je 0x14040262a
00402287  49 8D 8D 20 01 00 00            lea rcx, [r13 + 0x120]
0040228E  E8 2D F7 E4 FF                  call 0x1402519c0
00402293  48 85 DB                        test rbx, rbx
00402296  0F 84 BC FE FF FF               je 0x140402158
0040229C  E9 2B 02 00 00                  jmp 0x1404024cc
004022A1  48 8B D1                        mov rdx, rcx
004022A4  4D 85 C9                        test r9, r9
004022A7  49 0F 45 D1                     cmovne rdx, r9
004022AB  48 8B 02                        mov rax, qword ptr [rdx]
004022AE  48 85 C0                        test rax, rax
004022B1  0F 84 E0 FC FF FF               je 0x140401f97
004022B7  48 05 00 10 00 00               add rax, 0x1000
004022BD  48 89 84 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rax
004022C5  4C 8D 4C 24 58                  lea r9, [rsp + 0x58]
004022CA  4C 8D 84 24 A8 00 00 00         lea r8, [rsp + 0xa8]
004022D2  49 8B CD                        mov rcx, r13
004022D5  E8 26 F5 F3 FF                  call 0x140341800
004022DA  49 8D 8D D0 00 00 00            lea rcx, [r13 + 0xd0]
004022E1  4D 8D 45 10                     lea r8, [r13 + 0x10]
004022E5  84 C0                           test al, al
004022E7  0F 84 D2 04 00 00               je 0x1404027bf
004022ED  48 8B 74 24 58                  mov rsi, qword ptr [rsp + 0x58]
004022F2  E9 A0 FC FF FF                  jmp 0x140401f97
004022F7  8B CB                           mov ecx, ebx
004022F9  49 8B 02                        mov rax, qword ptr [r10]
004022FC  48 05 FF 0F 00 00               add rax, 0xfff
00402302  48 03 C8                        add rcx, rax
00402305  48 C1 F9 0C                     sar rcx, 0xc
00402309  8B C9                           mov ecx, ecx
0040230B  41 8B 04 24                     mov eax, dword ptr [r12]
0040230F  49 03 C6                        add rax, r14
00402312  48 3B C1                        cmp rax, rcx
00402315  0F 8D 5A FD FF FF               jge 0x140402075
0040231B  E9 E6 FE FF FF                  jmp 0x140402206
00402320  4C 8B F7                        mov r14, rdi
00402323  85 F6                           test esi, esi
00402325  0F 84 03 05 00 00               je 0x14040282e
0040232B  48 8B 84 24 A0 01 00 00         mov rax, qword ptr [rsp + 0x1a0]
00402333  48 85 C0                        test rax, rax
00402336  0F 85 FB 04 00 00               jne 0x140402837
0040233C  49 8B D6                        mov rdx, r14
0040233F  49 8B CA                        mov rcx, r10
00402342  E8 AD 07 00 00                  call 0x140402af4
00402347  4C 8B F8                        mov r15, rax
0040234A  8B 48 1C                        mov ecx, dword ptr [rax + 0x1c]
0040234D  48 8B 50 10                     mov rdx, qword ptr [rax + 0x10]
00402351  48 8D 04 11                     lea rax, [rcx + rdx]
00402355  4C 3B F0                        cmp r14, rax
00402358  0F 8F E5 04 00 00               jg 0x140402843
0040235E  49 8B 47 28                     mov rax, qword ptr [r15 + 0x28]
00402362  48 C1 E9 05                     shr rcx, 5
00402366  4C 8D 04 88                     lea r8, [rax + rcx*4]
0040236A  4C 89 44 24 60                  mov qword ptr [rsp + 0x60], r8
0040236F  41 8B 57 18                     mov edx, dword ptr [r15 + 0x18]
00402373  49 03 57 10                     add rdx, qword ptr [r15 + 0x10]
00402377  4C 3B F2                        cmp r14, rdx
0040237A  49 0F 4D D6                     cmovge rdx, r14
0040237E  4C 8B F2                        mov r14, rdx
00402381  8B C2                           mov eax, edx
00402383  41 2B 47 10                     sub eax, dword ptr [r15 + 0x10]
00402387  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
0040238C  8B C8                           mov ecx, eax
0040238E  48 C1 E9 05                     shr rcx, 5
00402392  49 8B 47 28                     mov rax, qword ptr [r15 + 0x28]
00402396  4C 8D 1C 88                     lea r11, [rax + rcx*4]
0040239A  4C 89 5C 24 70                  mov qword ptr [rsp + 0x70], r11
0040239F  48 8B C2                        mov rax, rdx
004023A2  48 99                           cqo
004023A4  B9 20 00 00 00                  mov ecx, 0x20
004023A9  48 F7 F9                        idiv rcx
004023AC  48 8B CA                        mov rcx, rdx
004023AF  83 CE FF                        or esi, 0xffffffff
004023B2  D3 E6                           shl esi, cl
004023B4  41 8B 03                        mov eax, dword ptr [r11]
004023B7  85 C6                           test esi, eax
004023B9  0F 84 FC 02 00 00               je 0x1404026bb
004023BF  F7 DE                           neg esi
004023C1  89 74 24 50                     mov dword ptr [rsp + 0x50], esi
004023C5  85 C6                           test esi, eax
004023C7  75 0D                           jne 0x1404023d6
004023C9  03 F6                           add esi, esi
004023CB  49 FF C6                        inc r14
004023CE  85 C6                           test esi, eax
004023D0  74 F7                           je 0x1404023c9
004023D2  89 74 24 50                     mov dword ptr [rsp + 0x50], esi
004023D6  4D 85 C9                        test r9, r9
004023D9  0F 84 63 FC FF FF               je 0x140402042
004023DF  8B 8C 24 70 01 00 00            mov ecx, dword ptr [rsp + 0x170]
004023E6  49 8B 11                        mov rdx, qword ptr [r9]
004023E9  48 81 C1 FF 0F 00 00            add rcx, 0xfff
004023F0  48 03 D1                        add rdx, rcx
004023F3  48 C1 FA 0C                     sar rdx, 0xc
004023F7  4C 3B F2                        cmp r14, rdx
004023FA  0F 8D 66 FB FF FF               jge 0x140401f66
00402400  49 8D 45 10                     lea rax, [r13 + 0x10]
00402404  48 39 00                        cmp qword ptr [rax], rax
00402407  0F 84 35 FC FF FF               je 0x140402042
0040240D  C7 44 24 54 01 00 00 00         mov dword ptr [rsp + 0x54], 1
00402415  E9 4C FB FF FF                  jmp 0x140401f66
0040241A  48 8B 94 24 80 01 00 00         mov rdx, qword ptr [rsp + 0x180]
00402422  40 38 7E 02                     cmp byte ptr [rsi + 2], dil
00402426  0F 84 00 FC FF FF               je 0x14040202c
0040242C  48 8B 4E 08                     mov rcx, qword ptr [rsi + 8]
00402430  48 03 02                        add rax, qword ptr [rdx]
00402433  48 3B C8                        cmp rcx, rax
00402436  0F 85 F0 FB FF FF               jne 0x14040202c
0040243C  39 7E 40                        cmp dword ptr [rsi + 0x40], edi
0040243F  0F 85 E7 FB FF FF               jne 0x14040202c
00402445  48 F7 C1 FF FF FF 01            test rcx, 0x1ffffff
0040244C  0F 84 DA FB FF FF               je 0x14040202c
00402452  E9 34 01 00 00                  jmp 0x14040258b
00402457  49 8B 8D F8 00 00 00            mov rcx, qword ptr [r13 + 0xf8]
0040245E  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
00402462  49 8B 11                        mov rdx, qword ptr [r9]
00402465  48 8B 09                        mov rcx, qword ptr [rcx]
00402468  E8 63 86 2B 00                  call 0x1406baad0
0040246D  E9 C5 FA FF FF                  jmp 0x140401f37
00402472  33 FF                           xor edi, edi
00402474  4C 8B A4 24 88 01 00 00         mov r12, qword ptr [rsp + 0x188]
0040247C  4C 8B AC 24 60 01 00 00         mov r13, qword ptr [rsp + 0x160]
00402484  8B C7                           mov eax, edi
00402486  89 44 24 54                     mov dword ptr [rsp + 0x54], eax
0040248A  44 8B F8                        mov r15d, eax
0040248D  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00402492  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00402497  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
0040249B  4C 8B B4 24 E0 00 00 00         mov r14, qword ptr [rsp + 0xe0]
004024A3  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
004024A8  48 8B 9C 24 A8 00 00 00         mov rbx, qword ptr [rsp + 0xa8]
004024B0  48 8B 84 24 E8 00 00 00         mov rax, qword ptr [rsp + 0xe8]
004024B8  48 89 84 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rax
004024C0  8B B4 24 70 01 00 00            mov esi, dword ptr [rsp + 0x170]
004024C7  E9 6B FA FF FF                  jmp 0x140401f37
004024CC  49 8B 8D F8 00 00 00            mov rcx, qword ptr [r13 + 0xf8]
004024D3  48 8B D3                        mov rdx, rbx
004024D6  41 F7 85 98 00 00 00 00 00 00 02  test dword ptr [r13 + 0x98], 0x2000000
004024E1  75 09                           jne 0x1404024ec
004024E3  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
004024E7  48 8B 09                        mov rcx, qword ptr [rcx]
004024EA  EB 07                           jmp 0x1404024f3
004024EC  49 8B 85 00 01 00 00            mov rax, qword ptr [r13 + 0x100]
004024F3  E8 D8 85 2B 00                  call 0x1406baad0
004024F8  E9 5B FC FF FF                  jmp 0x140402158
004024FD  33 DB                           xor ebx, ebx
004024FF  48 8B BC 24 90 01 00 00         mov rdi, qword ptr [rsp + 0x190]
00402507  4C 8B B4 24 80 01 00 00         mov r14, qword ptr [rsp + 0x180]
0040250F  4C 8B BC 24 60 01 00 00         mov r15, qword ptr [rsp + 0x160]
00402517  48 8B 07                        mov rax, qword ptr [rdi]
0040251A  48 8B 70 10                     mov rsi, qword ptr [rax + 0x10]
0040251E  48 83 EE 10                     sub rsi, 0x10
00402522  B9 FD 02 00 00                  mov ecx, 0x2fd
00402527  66 39 08                        cmp word ptr [rax], cx
0040252A  75 1C                           jne 0x140402548
0040252C  48 8B 58 08                     mov rbx, qword ptr [rax + 8]
00402530  41 0F B6 97 98 00 00 00         movzx edx, byte ptr [r15 + 0x98]
00402538  D1 EA                           shr edx, 1
0040253A  83 E2 01                        and edx, 1
0040253D  45 33 C0                        xor r8d, r8d
00402540  48 8B C8                        mov rcx, rax
00402543  E8 A4 78 F5 FF                  call 0x140359dec
00402548  48 89 37                        mov qword ptr [rdi], rsi
0040254B  49 39 1E                        cmp qword ptr [r14], rbx
0040254E  75 C7                           jne 0x140402517
00402550  4C 8B A4 24 88 01 00 00         mov r12, qword ptr [rsp + 0x188]
00402558  41 83 24 24 00                  and dword ptr [r12], 0
0040255D  33 FF                           xor edi, edi
0040255F  E9 F4 FB FF FF                  jmp 0x140402158
00402564  4D 85 C9                        test r9, r9
00402567  0F 85 FD 02 00 00               jne 0x14040286a
0040256D  48 8B 01                        mov rax, qword ptr [rcx]
00402570  48 39 46 08                     cmp qword ptr [rsi + 8], rax
00402574  0F 8C 8B FA FF FF               jl 0x140402005
0040257A  EB 05                           jmp 0x140402581
0040257C  4D 85 C9                        test r9, r9
0040257F  74 EC                           je 0x14040256d
00402581  39 7C 24 54                     cmp dword ptr [rsp + 0x54], edi
00402585  0F 85 68 01 00 00               jne 0x1404026f3
0040258B  FF 46 40                        inc dword ptr [rsi + 0x40]
0040258E  49 8D 8D 20 01 00 00            lea rcx, [r13 + 0x120]
00402595  E8 26 F4 E4 FF                  call 0x1402519c0
0040259A  41 8B 85 98 00 00 00            mov eax, dword ptr [r13 + 0x98]
004025A1  25 02 02 00 00                  and eax, 0x202
004025A6  3D 00 02 00 00                  cmp eax, 0x200
004025AB  0F 84 6E 01 00 00               je 0x14040271f
004025B1  41 B8 02 00 00 00               mov r8d, 2
004025B7  B2 01                           mov dl, 1
004025B9  48 8B CE                        mov rcx, rsi
004025BC  E8 2B 78 F5 FF                  call 0x140359dec
004025C1  49 8D 8D 20 01 00 00            lea rcx, [r13 + 0x120]
004025C8  E8 D3 BF E0 FF                  call 0x14020e5a0
004025CD  48 8B 94 24 78 01 00 00         mov rdx, qword ptr [rsp + 0x178]
004025D5  89 7C 24 54                     mov dword ptr [rsp + 0x54], edi
004025D9  41 39 3C 24                     cmp dword ptr [r12], edi
004025DD  0F 84 28 01 00 00               je 0x14040270b
004025E3  48 8B 84 24 90 01 00 00         mov rax, qword ptr [rsp + 0x190]
004025EB  48 89 30                        mov qword ptr [rax], rsi
004025EE  8B 46 04                        mov eax, dword ptr [rsi + 4]
004025F1  41 01 04 24                     add dword ptr [r12], eax
004025F5  41 F7 85 98 00 00 00 00 00 00 03  test dword ptr [r13 + 0x98], 0x3000000
00402600  74 0B                           je 0x14040260d
00402602  48 8B 46 30                     mov rax, qword ptr [rsi + 0x30]
00402606  48 3B C3                        cmp rax, rbx
00402609  48 0F 4F D8                     cmovg rbx, rax
0040260D  48 8B 76 18                     mov rsi, qword ptr [rsi + 0x18]
00402611  48 83 EE 10                     sub rsi, 0x10
00402615  49 8D 8D D0 00 00 00            lea rcx, [r13 + 0xd0]
0040261C  48 89 74 24 58                  mov qword ptr [rsp + 0x58], rsi
00402621  4D 8D 45 10                     lea r8, [r13 + 0x10]
00402625  E9 75 F9 FF FF                  jmp 0x140401f9f
0040262A  48 03 02                        add rax, qword ptr [rdx]
0040262D  49 89 85 D0 00 00 00            mov qword ptr [r13 + 0xd0], rax
00402634  41 8B 0C 24                     mov ecx, dword ptr [r12]
00402638  C1 E9 0C                        shr ecx, 0xc
0040263B  41 39 8D C8 00 00 00            cmp dword ptr [r13 + 0xc8], ecx
00402642  0F 86 34 02 00 00               jbe 0x14040287c
00402648  41 8B 85 C8 00 00 00            mov eax, dword ptr [r13 + 0xc8]
0040264F  2B C1                           sub eax, ecx
00402651  41 89 85 C8 00 00 00            mov dword ptr [r13 + 0xc8], eax
00402658  E9 2A FC FF FF                  jmp 0x140402287
0040265D  85 F6                           test esi, esi
0040265F  0F 85 26 FB FF FF               jne 0x14040218b
00402665  E9 F4 F8 FF FF                  jmp 0x140401f5e
0040266A  49 8D 8D D0 00 00 00            lea rcx, [r13 + 0xd0]
00402671  48 39 39                        cmp qword ptr [rcx], rdi
00402674  0F 84 0D FC FF FF               je 0x140402287
0040267A  4C 8B 8C 24 68 01 00 00         mov r9, qword ptr [rsp + 0x168]
00402682  4D 85 C9                        test r9, r9
00402685  0F 85 FC FB FF FF               jne 0x140402287
0040268B  48 89 39                        mov qword ptr [rcx], rdi
0040268E  E9 E6 F8 FF FF                  jmp 0x140401f79
00402693  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
00402698  41 39 47 18                     cmp dword ptr [r15 + 0x18], eax
0040269C  0F 84 22 02 00 00               je 0x1404028c4
004026A2  39 BC 24 70 01 00 00            cmp dword ptr [rsp + 0x170], edi
004026A9  0F 85 71 FA FF FF               jne 0x140402120
004026AF  41 8B 04 24                     mov eax, dword ptr [r12]
004026B3  49 03 C6                        add rax, r14
004026B6  E9 61 FA FF FF                  jmp 0x14040211c
004026BB  83 CE FF                        or esi, 0xffffffff
004026BE  89 74 24 50                     mov dword ptr [rsp + 0x50], esi
004026C2  49 83 E6 E0                     and r14, 0xffffffffffffffe0
004026C6  48 8B 54 24 68                  mov rdx, qword ptr [rsp + 0x68]
004026CB  48 89 54 24 68                  mov qword ptr [rsp + 0x68], rdx
004026D0  49 83 C3 04                     add r11, 4
004026D4  4C 89 5C 24 70                  mov qword ptr [rsp + 0x70], r11
004026D9  49 83 C6 20                     add r14, 0x20
004026DD  4D 3B D8                        cmp r11, r8
004026E0  0F 87 69 01 00 00               ja 0x14040284f
004026E6  41 8B 03                        mov eax, dword ptr [r11]
004026E9  85 C0                           test eax, eax
004026EB  0F 85 CE FC FF FF               jne 0x1404023bf
004026F1  EB DD                           jmp 0x1404026d0
004026F3  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
004026F7  48 C1 F8 0C                     sar rax, 0xc
004026FB  8B C0                           mov eax, eax
004026FD  4C 3B F0                        cmp r14, rax
00402700  0F 8E 38 F9 FF FF               jle 0x14040203e
00402706  E9 80 FE FF FF                  jmp 0x14040258b
0040270B  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
0040270F  48 8B 8C 24 80 01 00 00         mov rcx, qword ptr [rsp + 0x180]
00402717  48 89 01                        mov qword ptr [rcx], rax
0040271A  E9 C4 FE FF FF                  jmp 0x1404025e3
0040271F  41 39 3C 24                     cmp dword ptr [r12], edi
00402723  0F 94 C2                        sete dl
00402726  48 8D 4E 48                     lea rcx, [rsi + 0x48]
0040272A  E8 F1 26 E1 FF                  call 0x140214e20
0040272F  84 C0                           test al, al
00402731  0F 84 B2 00 00 00               je 0x1404027e9
00402737  49 8D 8D 20 01 00 00            lea rcx, [r13 + 0x120]
0040273E  E8 5D BE E0 FF                  call 0x14020e5a0
00402743  8A 4E 02                        mov cl, byte ptr [rsi + 2]
00402746  84 C9                           test cl, cl
00402748  74 39                           je 0x140402783
0040274A  48 8B 94 24 78 01 00 00         mov rdx, qword ptr [rsp + 0x178]
00402752  41 F7 85 98 00 00 00 00 00 00 01  test dword ptr [r13 + 0x98], 0x1000000
0040275D  0F 84 72 FE FF FF               je 0x1404025d5
00402763  48 85 D2                        test rdx, rdx
00402766  0F 84 69 FE FF FF               je 0x1404025d5
0040276C  48 8B 02                        mov rax, qword ptr [rdx]
0040276F  48 39 46 30                     cmp qword ptr [rsi + 0x30], rax
00402773  0F 8E 5C FE FF FF               jle 0x1404025d5
00402779  84 C9                           test cl, cl
0040277B  74 06                           je 0x140402783
0040277D  FF 05 9D 33 A6 00               inc dword ptr [rip + 0xa6339d]
00402783  49 8D 8D 20 01 00 00            lea rcx, [r13 + 0x120]
0040278A  E8 31 F2 E4 FF                  call 0x1402519c0
0040278F  45 33 C0                        xor r8d, r8d
00402792  33 D2                           xor edx, edx
00402794  48 8B CE                        mov rcx, rsi
00402797  E8 50 76 F5 FF                  call 0x140359dec
0040279C  49 8D 8D 20 01 00 00            lea rcx, [r13 + 0x120]
004027A3  E8 F8 BD E0 FF                  call 0x14020e5a0
004027A8  41 39 3C 24                     cmp dword ptr [r12], edi
004027AC  75 54                           jne 0x140402802
004027AE  49 8B 75 18                     mov rsi, qword ptr [r13 + 0x18]
004027B2  48 8B 94 24 78 01 00 00         mov rdx, qword ptr [rsp + 0x178]
004027BA  E9 52 FE FF FF                  jmp 0x140402611
004027BF  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
004027C4  48 8B 70 18                     mov rsi, qword ptr [rax + 0x18]
004027C8  48 83 EE 10                     sub rsi, 0x10
004027CC  48 89 74 24 58                  mov qword ptr [rsp + 0x58], rsi
004027D1  E9 C1 F7 FF FF                  jmp 0x140401f97
004027D6  8B 86 D0 03 00 00               mov eax, dword ptr [rsi + 0x3d0]
004027DC  2B C1                           sub eax, ecx
004027DE  89 86 D0 03 00 00               mov dword ptr [rsi + 0x3d0], eax
004027E4  E9 FF F8 FF FF                  jmp 0x1404020e8
004027E9  45 33 C0                        xor r8d, r8d
004027EC  B2 01                           mov dl, 1
004027EE  48 8B CE                        mov rcx, rsi
004027F1  E8 F6 75 F5 FF                  call 0x140359dec
004027F6  49 8D 8D 20 01 00 00            lea rcx, [r13 + 0x120]
004027FD  E8 9E BD E0 FF                  call 0x14020e5a0
00402802  4D 8D 45 10                     lea r8, [r13 + 0x10]
00402806  E9 19 F8 FF FF                  jmp 0x140402024
0040280B  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00402814  45 33 C9                        xor r9d, r9d
00402817  45 33 C0                        xor r8d, r8d
0040281A  33 D2                           xor edx, edx
0040281C  E8 DF 03 F9 FF                  call 0x140392c00
00402821  4C 8B 8C 24 78 01 00 00         mov r9, qword ptr [rsp + 0x178]
00402829  E9 D2 F6 FF FF                  jmp 0x140401f00
0040282E  4D 8B 72 20                     mov r14, qword ptr [r10 + 0x20]
00402832  E9 F4 FA FF FF                  jmp 0x14040232b
00402837  4C 8B 30                        mov r14, qword ptr [rax]
0040283A  49 C1 FE 0C                     sar r14, 0xc
0040283E  E9 F9 FA FF FF                  jmp 0x14040233c
00402843  45 8B 77 18                     mov r14d, dword ptr [r15 + 0x18]
00402847  4C 03 F2                        add r14, rdx
0040284A  E9 0F FB FF FF                  jmp 0x14040235e
0040284F  8B 8C 24 70 01 00 00            mov ecx, dword ptr [rsp + 0x170]
00402856  85 C9                           test ecx, ecx
00402858  0F 85 DC 98 2E 00               jne 0x1406ec13a
0040285E  8D 42 FF                        lea eax, [rdx - 1]
00402861  41 89 47 1C                     mov dword ptr [r15 + 0x1c], eax
00402865  E9 D0 98 2E 00                  jmp 0x1406ec13a
0040286A  48 8B 46 20                     mov rax, qword ptr [rsi + 0x20]
0040286E  49 39 01                        cmp qword ptr [r9], rax
00402871  0F 8D 8E F7 FF FF               jge 0x140402005
00402877  E9 00 FD FF FF                  jmp 0x14040257c
0040287C  41 89 BD C8 00 00 00            mov dword ptr [r13 + 0xc8], edi
00402883  E9 FF F9 FF FF                  jmp 0x140402287
00402888  4D 85 C9                        test r9, r9
0040288B  0F 84 32 99 2E 00               je 0x1406ec1c3
00402891  4D 8B 09                        mov r9, qword ptr [r9]
00402894  E9 2D 99 2E 00                  jmp 0x1406ec1c6
00402899  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
0040289E  45 33 C9                        xor r9d, r9d
004028A1  BA 8E 12 00 00                  mov edx, 0x128e
004028A6  41 8D 49 34                     lea ecx, [r9 + 0x34]
004028AA  49 C7 C0 20 04 00 C0            mov r8, 0xffffffffc0000420
004028B1  E8 AA AD 0F 00                  call 0x1404fd660
004028B6  CC                              int3
004028B7  49 8B CD                        mov rcx, r13
004028BA  E8 0D E9 04 00                  call 0x1404511cc
004028BF  E9 2E F8 FF FF                  jmp 0x1404020f2
004028C4  41 8B 0C 24                     mov ecx, dword ptr [r12]
004028C8  41 2B 4F 10                     sub ecx, dword ptr [r15 + 0x10]
004028CC  41 03 CE                        add ecx, r14d
004028CF  41 89 4F 18                     mov dword ptr [r15 + 0x18], ecx
004028D3  E9 CA FD FF FF                  jmp 0x1404026a2
004028D8  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
004028E1  45 33 C9                        xor r9d, r9d
004028E4  45 33 C0                        xor r8d, r8d
004028E7  B2 01                           mov dl, 1
004028E9  E8 12 03 F9 FF                  call 0x140392c00
004028EE  E9 73 F8 FF FF                  jmp 0x140402166
004028F3  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
004028F8  45 33 C9                        xor r9d, r9d
004028FB  BA BD 12 00 00                  mov edx, 0x12bd
00402900  41 8D 49 34                     lea ecx, [r9 + 0x34]
00402904  49 C7 C0 20 04 00 C0            mov r8, 0xffffffffc0000420
0040290B  E8 50 AD 0F 00                  call 0x1404fd660
00402910  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CcAcquireByteRangeForWrite(__int64 a1, __int64 a2, int a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, unsigned __int8 a8, __int64 a9)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned int v_stack_m104;
    unsigned int v_stack_m108;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p160;
    unsigned __int64 v_stack_p168;
    unsigned int v_stack_p170;
    unsigned __int64 v_stack_p178;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p180;
    unsigned __int64 v_stack_p188;
    unsigned __int64 v_stack_p190;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p50;
    unsigned int v_stack_p54;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_pA8;
    unsigned __int64 v_stack_pB8;
    unsigned __int64 v_stack_pE0;
    unsigned __int64 v_stack_pE8;

    *(unsigned __int64 *)(v_rsp + 32) = a4;
    *(unsigned int *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (288);
    v_rdi = 0;
    v_stack_m100 = 0;
    *(unsigned __int64 *)(v_rsp - 168) = 0;
    v_stack_m104 = 0;
    v_stack_mF8 = 0;
    v_stack_mE8 = 0;
    v_stack_m108 = 0;
    v_stack_m78 = 0;
    v_stack_mF0 = 0;
    v_stack_mB0 = v_rbx;
    *(unsigned __int64 *)(v_rsp - 104) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 88) = 0;
    if (a8 != 0) goto loc_0040280B;
loc_00401F00:
    v_stack_mA0 = *(unsigned __int64 *)(a1 + 536);
    v_stack_m70 = *(unsigned __int64 *)(a1 + 536);
    *(unsigned __int64 *)(a5) = 0;
    *(unsigned int *)(a6) = 0;
    if (a4 != 0) goto loc_00402457;
loc_00401F37:
    result = ExAcquireFastMutex(a1 + 288, a2, a3, a4);
    v_stack_mE0 = *(unsigned __int64 *)(a1 + 168);
    if (*(unsigned __int64 *)(a1 + 168) == 0) goto loc_00401F5E;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 168) + 8)) != 0) goto loc_00402181;
loc_00401F5E:
loc_00401F66:
loc_00401F79:
    v_rsi = (*(unsigned __int64 *)(a1 + 24)) - (16);
    v_stack_m100 = v_rsi;
    if (((*(unsigned int *)(a1 + 152)) & (512)) != 0) goto loc_004022A1;
loc_00401F97:
loc_00401F9F:
loc_00401FA7:
    if ((v_rsi + 16) == (a1 + 16)) goto loc_00402024;
    if ((*(unsigned __int16 *)(v_rsi)) != 765) goto loc_00402005;
    if (((*(unsigned int *)(a1 + 152)) & (0x1000000ULL)) == 0) goto loc_00401FEA;
    if (v_stack_p20 == 0) goto loc_00401FEA;
    if ((*(unsigned __int64 *)(v_rsi + 48)) <= (*(unsigned __int64 *)(v_stack_p20))) goto loc_00401FEA;
    v_rsi = (*(unsigned __int64 *)(v_rsi + 24)) - (16);
    v_stack_m100 = v_rsi;
    goto loc_00401FA7;
loc_00401FEA:
    if (v_stack_p10 != 0) goto loc_00402014;
loc_00401FEF:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a6))) != 0) goto loc_0040241A;
    if ((*(unsigned __int8 *)(v_rsi + 2)) != 0) goto loc_00402564;
loc_00402005:
    v_rsi = (*(unsigned __int64 *)(v_rsi + 24)) - (16);
    v_stack_m100 = v_rsi;
    goto loc_00401FA7;
loc_00402014:
    result = ((unsigned int)(v_stack_p18)) + (*(unsigned __int64 *)(v_stack_p10));
    if (result > (*(unsigned __int64 *)(v_rsi + 8))) goto loc_00401FEF;
loc_00402024:
loc_0040202C:
    if (v_stack_m104 == 0) goto loc_0040226C;
loc_0040203E:
loc_00402042:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 10894044)))) & (1)) != 0) goto loc_00402888;
loc_00402069:
    if ((((unsigned int)((unsigned int)(v_stack_m108))) & ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mE8))))) != 0) goto loc_004021FD;
loc_00402075:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mE0 + 4))))) - ((unsigned int)((unsigned int)(*(unsigned int *)(a6)))));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_mE0 + 4))) & ((unsigned int)(a1)));
    *(unsigned int *)(v_stack_mE0 + 4) = (unsigned int)(result);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mE0 + 8)))) < ((unsigned int)((unsigned int)(*(unsigned int *)(a6))))) goto loc_004028F3;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_mE0 + 8))) - ((unsigned int)((unsigned int)(*(unsigned int *)(a6)))));
    *(unsigned int *)(v_stack_mE0 + 8) = (unsigned int)(result);
    result = KeAcquireInStackQueuedSpinLock(v_stack_mA0 + 768, v_stack_m68, (unsigned int)(*(unsigned int *)(v_stack_mE8)), v_stack_mE8);
    result = CcDeductDirtyPages(a1, (unsigned int)(*(unsigned int *)(a6)), (unsigned int)(*(unsigned int *)(v_stack_mE8)), v_stack_mE8);
    if ((*(unsigned int *)(v_stack_mA0 + 976)) > ((unsigned int)((unsigned int)(*(unsigned int *)(a6))))) goto loc_004027D6;
    *(unsigned int *)(v_stack_mA0 + 976) = 0;
loc_004020E8:
    if ((*(unsigned int *)(a1 + 112)) == 0) goto loc_004028B7;
loc_004020F2:
    result = KeReleaseInStackQueuedSpinLock(v_stack_m68, (unsigned int)(*(unsigned int *)(a6)), (unsigned int)(*(unsigned int *)(v_stack_mE8)), v_stack_mE8);
    if ((*(unsigned int *)(0 + 32)) != 0) goto loc_00402693;
    *(unsigned int *)(0 + 28) = 0;
    result = (*(unsigned __int64 *)(0 + 16)) + (0x2000ULL);
loc_0040211C:
    *(unsigned __int64 *)(v_stack_mE0 + 32) = result;
loc_00402120:
    if ((*(unsigned __int64 *)(a1 + 16)) == (a1 + 16)) goto loc_0040225D;
loc_0040212D:
    result = ExReleaseFastMutex(a1 + 288, (unsigned int)(*(unsigned int *)(a6)), (unsigned int)(*(unsigned int *)(v_stack_mE8)), v_stack_mE8);
    v_r14 = (0) << (12);
    *(unsigned __int64 *)(a5) = v_r14;
    *(unsigned __int64 *)(a7) = 0;
loc_00402158:
    if (a8 != 0) goto loc_004028D8;
loc_00402166:
    result = ((*(unsigned int *)(a6)) != 0) ? 1 : 0;
    v_rsp = (v_rsp) + (288);
    return result;
loc_00402181:
    if ((*(unsigned int *)(v_stack_p10 + 4)) == 0) goto loc_0040265D;
loc_0040218B:
    if (v_stack_p168 == 0) goto loc_00402320;
    v_r14 = (*(unsigned __int64 *)(v_stack_p168)) >> (12);
    v_rbx = (*(unsigned __int64 *)(v_stack_p168) - 1) + ((unsigned int)((unsigned int)(v_stack_mA0)));
    v_rbx = (v_rbx) >> (12);
    result = CcFindBitmapRangeToClean(v_stack_p10, v_r14, (unsigned int)(*(unsigned int *)(v_stack_mE8)), v_stack_p168);
    a1 = ((unsigned int)(*(unsigned int *)(result + 24))) + (*(unsigned __int64 *)(result + 16));
    if (v_rbx < a1) goto loc_00401F66;
    result = (*(unsigned __int64 *)(result + 16)) + ((unsigned int)(*(unsigned int *)(result + 28)));
    if (v_r14 > result) goto loc_00401F66;
    if (v_rbx >= result) goto loc_00402362;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) - (*(unsigned int *)(result + 16)));
    goto loc_00402362;
loc_004021FD:
    if (v_stack_p10 != 0) goto loc_004022F7;
loc_00402206:
    a1 = ((unsigned int)(*(unsigned int *)(result + 28))) >> (5);
    if (v_stack_p168 > (*(unsigned __int64 *)(result + 40) + a1 * 4)) goto loc_00402899;
    if (v_stack_p10 != 0) goto loc_00402234;
    if ((*(unsigned int *)(a6)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10520134))))) goto loc_00402075;
loc_00402234:
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_mE8))) - ((unsigned int)(v_stack_mA0)));
    *(unsigned int *)(v_stack_p168) = a3;
    v_rsi = (unsigned int)((v_stack_mA0) + ((unsigned int)(v_stack_mA0)));
    if (condition_is_not_equal) goto loc_00402069;
    a4 = (v_stack_p168) + (4);
    if (a4 > v_stack_mF8) goto loc_00402075;
    goto loc_00402069;
loc_0040225D:
    *(unsigned int *)(a1 + 200) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 4)));
    goto loc_0040212D;
loc_0040226C:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a6))) == 0) goto loc_0040266A;
    if (v_stack_p168 == 0) goto loc_0040262A;
loc_00402287:
    result = ExReleaseFastMutex(a1 + 288, v_r14, a3, a4);
    if (v_rbx == 0) goto loc_00402158;
    goto loc_004024CC;
loc_004022A1:
    a2 = a1 + 288;
    if (a4 != 0) { a2 = a4; }
    if (*(unsigned __int64 *)(a2) == 0) goto loc_00401F97;
    result = (*(unsigned __int64 *)(a2)) + (0x1000ULL);
    v_stack_pA8 = result;
    result = CcFindBcb(a1, a2, v_stack_pA8, v_stack_p58);
    if ((unsigned __int8)(result) == 0) goto loc_004027BF;
    goto loc_00401F97;
loc_004022F7:
    result = (*(unsigned __int64 *)(v_stack_p10)) + (0xFFFULL);
    a1 = ((unsigned int)((unsigned int)(v_rbx))) + (result);
    a1 = (a1) >> (12);
    result = ((unsigned int)(*(unsigned int *)(a6))) + (v_r14);
    if (result >= ((unsigned int)((unsigned int)(a1)))) goto loc_00402075;
    goto loc_00402206;
loc_00402320:
    if ((unsigned int)(v_stack_p58) == 0) goto loc_0040282E;
loc_0040232B:
    if (a9 != 0) goto loc_00402837;
loc_0040233C:
    result = CcFindBitmapRangeToClean(v_stack_p10, 0, a1 + 16, v_stack_p58);
    if (0 > ((unsigned int)(*(unsigned int *)(result + 28)) + *(unsigned __int64 *)(result + 16) * 1)) goto loc_00402843;
loc_0040235E:
loc_00402362:
    a1 = ((unsigned int)(*(unsigned int *)(result + 28))) >> (5);
    v_stack_p60 = *(unsigned __int64 *)(result + 40) + a1 * 4;
    a2 = ((unsigned int)(*(unsigned int *)(result + 24))) + (*(unsigned __int64 *)(result + 16));
    if (0 >= a2) { a2 = 0; }
    result = (unsigned int)(((unsigned int)((unsigned int)(a2))) - (*(unsigned int *)(result + 16)));
    v_stack_p68 = result;
    a1 = ((unsigned int)((unsigned int)(result))) >> (5);
    v_stack_p70 = *(unsigned __int64 *)(result + 40) + a1 * 4;
    v_rsi = (unsigned int)((v_stack_p58) | (0xFFFFFFFFULL));
    v_rsi = (unsigned int)((v_rsi) << ((unsigned __int8)(a2)));
    if ((((unsigned int)(v_rsi)) & ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 40) + a1 * 4))))) == 0) goto loc_004026BB;
loc_004023BF:
    v_rsi = (unsigned int)(-(v_rsi));
    v_stack_p50 = (unsigned int)(v_rsi);
    if ((((unsigned int)(v_rsi)) & ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 40) + a1 * 4))))) != 0) goto loc_004023D6;
loc_004023C9:
    v_rsi = (unsigned int)((v_rsi) + ((unsigned int)(v_rsi)));
    v_r14 = (a2) + 1;
    if ((((unsigned int)(v_rsi)) & ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 40) + a1 * 4))))) == 0) goto loc_004023C9;
    v_stack_p50 = (unsigned int)(v_rsi);
loc_004023D6:
    if (v_stack_p58 == 0) goto loc_00402042;
    a1 = ((unsigned int)(v_stack_p170)) + (0xFFFULL);
    a2 = (*(unsigned __int64 *)(v_stack_p58)) + (a1);
    a2 = (a2) >> (12);
    if (v_r14 >= a2) goto loc_00401F66;
    if ((*(unsigned __int64 *)(a1 + 16)) == (a1 + 16)) goto loc_00402042;
    v_stack_p54 = 1;
    goto loc_00401F66;
loc_0040241A:
    if ((*(unsigned __int8 *)(v_rsi + 2)) == 0) goto loc_0040202C;
    result = (a1 + 16) + (*(unsigned __int64 *)(a5));
    if ((*(unsigned __int64 *)(v_rsi + 8)) != result) goto loc_0040202C;
    if ((*(unsigned int *)(v_rsi + 64)) != 0) goto loc_0040202C;
    if (((*(unsigned __int64 *)(v_rsi + 8)) & (0x1FFFFFFULL)) == 0) goto loc_0040202C;
    goto loc_0040258B;
loc_00402457:
    result = guard_dispatch_icall(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 248)), *(unsigned __int64 *)(v_stack_p58), *(unsigned __int64 *)(result + 40) + a1 * 4, v_stack_p58);
    goto loc_00401F37;
loc_004024CC:
    if (((*(unsigned int *)(a1 + 152)) & (0x2000000ULL)) != 0) goto loc_004024EC;
    goto loc_004024F3;
loc_004024EC:
loc_004024F3:
    result = guard_dispatch_icall(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 248)), v_rbx, *(unsigned __int64 *)(result + 40) + a1 * 4, v_stack_p58);
    goto loc_00402158;
loc_00402564:
    if (v_stack_p58 != 0) goto loc_0040286A;
loc_0040256D:
    if ((*(unsigned __int64 *)(v_rsi + 8)) < (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 248))))) goto loc_00402005;
    goto loc_00402581;
loc_0040257C:
    if (v_stack_p58 == 0) goto loc_0040256D;
loc_00402581:
    if (v_stack_p54 != 0) goto loc_004026F3;
loc_0040258B:
    result = ExReleaseFastMutex(a1 + 288, v_rbx, *(unsigned __int64 *)(result + 40) + a1 * 4, v_stack_p58);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 152))) & (514));
    if (((unsigned int)(result)) == 512) goto loc_0040271F;
    result = CcUnpinFileDataEx(v_rsi, 1, 2, v_stack_p58);
    result = ExAcquireFastMutex(a1 + 288, 1, 2, v_stack_p58);
loc_004025D5:
    v_stack_p54 = 0;
    if ((*(unsigned int *)(a6)) == 0) goto loc_0040270B;
loc_004025E3:
    *(unsigned __int64 *)(a7) = v_rsi;
    result = (unsigned int)(*(unsigned int *)(v_rsi + 4));
    if (((*(unsigned int *)(a1 + 152)) & (0x3000000ULL)) != 0) {
        result = *(unsigned __int64 *)(v_rsi + 48);
        if (result > v_rbx) { v_rbx = result; }
    }
loc_00402611:
    v_rsi = (*(unsigned __int64 *)(v_rsi + 24)) - (16);
    v_stack_p58 = v_rsi;
    goto loc_00401F9F;
loc_0040262A:
    result = (result) + (*(unsigned __int64 *)(v_stack_p178));
    *(unsigned __int64 *)(a1 + 208) = result;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a6))) >> (12));
    if ((*(unsigned int *)(a1 + 200)) <= ((unsigned int)(a1))) goto loc_0040287C;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 200))) - ((unsigned int)(a1)));
    *(unsigned int *)(a1 + 200) = (unsigned int)(result);
    goto loc_00402287;
loc_0040265D:
    if ((unsigned int)(v_rsi) != 0) goto loc_0040218B;
    goto loc_00401F5E;
loc_0040266A:
    if ((*(unsigned __int64 *)(a1 + 208)) == 0) goto loc_00402287;
    if (v_stack_p168 != 0) goto loc_00402287;
    *(unsigned __int64 *)(a1 + 208) = 0;
    goto loc_00401F79;
loc_00402693:
    if ((*(unsigned int *)(result + 24)) == ((unsigned int)(v_stack_p68))) goto loc_004028C4;
loc_004026A2:
    if (v_stack_p170 != 0) goto loc_00402120;
    result = ((unsigned int)(*(unsigned int *)(a6))) + (v_r14);
    goto loc_0040211C;
loc_004026BB:
    v_rsi = (unsigned int)((v_rsi) | (0xFFFFFFFFULL));
    v_stack_p50 = (unsigned int)(v_rsi);
    v_r14 = (v_r14) & (-32);
    v_stack_p68 = v_stack_p68;
loc_004026D0:
    v_r11 = (*(unsigned __int64 *)(result + 40) + a1 * 4) + (4);
    v_stack_p70 = v_r11;
    v_r14 = (v_r14) + (32);
    if (v_r11 > (a1 + 16)) goto loc_0040284F;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_r11))) != 0) goto loc_004023BF;
    goto loc_004026D0;
loc_004026F3:
    result = (*(unsigned __int64 *)(v_rsi + 8)) >> (12);
    if (v_r14 <= ((unsigned int)((unsigned int)(result)))) goto loc_0040203E;
    goto loc_0040258B;
loc_0040270B:
    *(unsigned __int64 *)(a5) = *(unsigned __int64 *)(v_rsi + 8);
    goto loc_004025E3;
loc_0040271F:
    a2 = ((*(unsigned int *)(a6)) == 0) ? 1 : 0;
    result = ExAcquireResourceExclusiveLite(v_rsi + 72, a2, a1 + 16, v_stack_p168);
    if ((unsigned __int8)(result) == 0) goto loc_004027E9;
    result = ExAcquireFastMutex(a1 + 288, a2, a1 + 16, v_stack_p168);
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rsi + 2)) == 0) goto loc_00402783;
    if (((*(unsigned int *)(a1 + 152)) & (0x1000000ULL)) == 0) goto loc_004025D5;
    if (v_stack_p178 == 0) goto loc_004025D5;
    if ((*(unsigned __int64 *)(v_rsi + 48)) <= (*(unsigned __int64 *)(v_stack_p178))) goto loc_004025D5;
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rsi + 2)) != 0) {
    }
    result = ExReleaseFastMutex(a1 + 288, v_stack_p178, a1 + 16, v_stack_p168);
    a3 = 0;
    a2 = 0;
    result = CcUnpinFileDataEx(v_rsi, a2, a3, v_stack_p168);
    result = ExAcquireFastMutex(a1 + 288, a2, a3, v_stack_p168);
    if ((*(unsigned int *)(a6)) != 0) goto loc_00402802;
    goto loc_00402611;
loc_004027BF:
    v_rsi = (*(unsigned __int64 *)(v_stack_p58 + 24)) - (16);
    v_stack_p58 = v_rsi;
    goto loc_00401F97;
loc_004027D6:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsi + 976))) - ((unsigned int)(a1 + 288)));
    *(unsigned int *)(v_rsi + 976) = (unsigned int)(result);
    goto loc_004020E8;
loc_004027E9:
    a3 = 0;
    result = CcUnpinFileDataEx(v_rsi, 1, a3, v_stack_p168);
    result = ExAcquireFastMutex(a1 + 288, 1, a3, v_stack_p168);
loc_00402802:
    goto loc_00402024;
loc_0040280B:
    a4 = 0;
    a3 = 0;
    a2 = 0;
    result = PsBoostThreadIoEx(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, a4);
    goto loc_00401F00;
loc_0040282E:
    goto loc_0040232B;
loc_00402837:
    v_r14 = (*(unsigned __int64 *)(result)) >> (12);
    goto loc_0040233C;
loc_00402843:
    v_r14 = ((unsigned int)(*(unsigned int *)(result + 24))) + (0);
    goto loc_0040235E;
loc_0040284F:
    *(unsigned int *)(result + 28) = (unsigned int)(a2 - 1);
loc_0040286A:
    if ((*(unsigned __int64 *)(v_stack_p178)) >= (*(unsigned __int64 *)(v_rsi + 32))) goto loc_00402005;
    goto loc_0040257C;
loc_0040287C:
    *(unsigned int *)(a1 + 200) = 0;
    goto loc_00402287;
loc_00402888:
loc_00402899:
    v_stack_p20 = 0;
    a4 = 0;
    result = KeBugCheckEx(a4 + 52, (unsigned int)(0x128EULL), 0xFFFFFFFFC0000420ULL, a4);
loc_004028B7:
    result = CcInsertIntoCleanSharedCacheMapList(a1, (unsigned int)(0x128EULL), 0xFFFFFFFFC0000420ULL, a4);
    goto loc_004020F2;
loc_004028C4:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a6))) - (*(unsigned int *)(result + 16)));
    a1 = (unsigned int)((a1) + ((unsigned int)(v_r14)));
    *(unsigned int *)(result + 24) = (unsigned int)(a1);
    goto loc_004026A2;
loc_004028D8:
    a4 = 0;
    a3 = 0;
    result = PsBoostThreadIoEx(*(unsigned __int64 *)(gs_base + (0 + 392)), 1, a3, a4);
    goto loc_00402166;
loc_004028F3:
    v_stack_p20 = 0;
    a4 = 0;
    result = KeBugCheckEx(a4 + 52, (unsigned int)(0x12BDULL), 0xFFFFFFFFC0000420ULL, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CcAcquireByteRangeForWrite(void *Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4, void *Arg5, void *Arg6, void *Arg7, uint8_t Arg8, int64_t Arg9)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg5 = (uint8_t *)Arg5;
    uint8_t *arg6 = (uint8_t *)Arg6;
    uint8_t *arg7 = (uint8_t *)Arg7;

    int64_t result;
    int64_t local_r11;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint32_t v_stack_m104;
    uint32_t v_stack_m108;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p160;
    uint64_t v_stack_p168;
    uint32_t v_stack_p170;
    uint64_t v_stack_p178;
    uint32_t v_stack_p18;
    uint64_t v_stack_p180;
    uint64_t v_stack_p188;
    uint64_t v_stack_p190;
    uint64_t v_stack_p20;
    uint32_t v_stack_p50;
    uint32_t v_stack_p54;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_pA8;
    uint64_t v_stack_pB8;
    uint64_t v_stack_pE0;
    uint64_t v_stack_pE8;

    *(uint64_t *)(local_rsp + 0x20) = Arg4;
    *(uint32_t *)(local_rsp + 0x18) = Arg3;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    *(void **)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (288);
    local_rdi = 0;
    v_stack_m100 = 0;
    *(uint64_t *)(local_rsp - 0xA8) = 0;
    v_stack_m104 = 0;
    v_stack_mF8 = 0;
    v_stack_mE8 = 0;
    v_stack_m108 = 0;
    v_stack_m78 = 0;
    v_stack_mF0 = 0;
    v_stack_mB0 = local_rbx;
    *(uint64_t *)(local_rsp - 0x68) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x58) = 0;
    if (Arg8 != 0) goto loc_0040280B;
loc_00401F00:
    v_stack_mA0 = *(uint64_t *)(arg1 + 0x218);
    v_stack_m70 = *(uint64_t *)(arg1 + 0x218);
    *(uint64_t *)(arg5) = 0;
    *(uint32_t *)(arg6) = 0;
    if (Arg4 != 0) goto loc_00402457;
loc_00401F37:
    result = ExAcquireFastMutex(Arg1 + 288, Arg2, Arg3, Arg4);
    v_stack_mE0 = *(uint64_t *)(arg1 + 0xA8);
    if (*(uint64_t *)(arg1 + 0xA8) == 0) goto loc_00401F5E;
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0xA8) + 0x8)) != 0) goto loc_00402181;
loc_00401F5E:
loc_00401F66:
loc_00401F79:
    local_rsi = (*(uint64_t *)(arg1 + 0x18)) - (16);
    v_stack_m100 = local_rsi;
    if (((*(uint32_t *)(arg1 + 0x98)) & (512)) != 0) goto loc_004022A1;
loc_00401F97:
loc_00401F9F:
loc_00401FA7:
    if ((local_rsi + 16) == (Arg1 + 16)) goto loc_00402024;
    if ((*(uint16_t *)(local_rsi)) != 765) goto loc_00402005;
    if (((*(uint32_t *)(arg1 + 0x98)) & (0x1000000ULL)) == 0) goto loc_00401FEA;
    if (v_stack_p20 == 0) goto loc_00401FEA;
    if ((*(uint64_t *)(local_rsi + 0x30)) <= (*(uint64_t *)(v_stack_p20))) goto loc_00401FEA;
    local_rsi = (*(uint64_t *)(local_rsi + 0x18)) - (16);
    v_stack_m100 = local_rsi;
    goto loc_00401FA7;
loc_00401FEA:
    if (v_stack_p10 != 0) goto loc_00402014;
loc_00401FEF:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg6))) != 0) goto loc_0040241A;
    if ((*(uint8_t *)(local_rsi + 0x2)) != 0) goto loc_00402564;
loc_00402005:
    local_rsi = (*(uint64_t *)(local_rsi + 0x18)) - (16);
    v_stack_m100 = local_rsi;
    goto loc_00401FA7;
loc_00402014:
    result = ((uint32_t)(v_stack_p18)) + (*(uint64_t *)(v_stack_p10));
    if (result > (*(uint64_t *)(local_rsi + 0x8))) goto loc_00401FEF;
loc_00402024:
loc_0040202C:
    if (v_stack_m104 == 0) goto loc_0040226C;
loc_0040203E:
loc_00402042:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA63ADC)))) & (1)) != 0) goto loc_00402888;
loc_00402069:
    if ((((uint32_t)((uint32_t)(v_stack_m108))) & ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mE8))))) != 0) goto loc_004021FD;
loc_00402075:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mE0 + 0x4))))) - ((uint32_t)((uint32_t)(*(uint32_t *)(arg6)))));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_mE0 + 0x4))) & ((uint32_t)(Arg1)));
    *(uint32_t *)(v_stack_mE0 + 0x4) = (uint32_t)(result);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mE0 + 0x8)))) < ((uint32_t)((uint32_t)(*(uint32_t *)(arg6))))) goto loc_004028F3;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_mE0 + 0x8))) - ((uint32_t)((uint32_t)(*(uint32_t *)(arg6)))));
    *(uint32_t *)(v_stack_mE0 + 0x8) = (uint32_t)(result);
    result = KeAcquireInStackQueuedSpinLock(v_stack_mA0 + 768, v_stack_m68, (uint32_t)(*(uint32_t *)(v_stack_mE8)), v_stack_mE8);
    result = CcDeductDirtyPages(Arg1, (uint32_t)(*(uint32_t *)(arg6)), (uint32_t)(*(uint32_t *)(v_stack_mE8)), v_stack_mE8);
    if ((*(uint32_t *)(v_stack_mA0 + 0x3D0)) > ((uint32_t)((uint32_t)(*(uint32_t *)(arg6))))) goto loc_004027D6;
    *(uint32_t *)(v_stack_mA0 + 0x3D0) = 0;
loc_004020E8:
    if ((*(uint32_t *)(arg1 + 0x70)) == 0) goto loc_004028B7;
loc_004020F2:
    result = KeReleaseInStackQueuedSpinLock(v_stack_m68, (uint32_t)(*(uint32_t *)(arg6)), (uint32_t)(*(uint32_t *)(v_stack_mE8)), v_stack_mE8);
    if ((*(uint32_t *)(0 + 0x20)) != 0) goto loc_00402693;
    *(uint32_t *)(0 + 0x1C) = 0;
    result = (*(uint64_t *)(0 + 0x10)) + (0x2000ULL);
loc_0040211C:
    *(uint64_t *)(v_stack_mE0 + 0x20) = result;
loc_00402120:
    if ((*(uint64_t *)(arg1 + 0x10)) == (Arg1 + 16)) goto loc_0040225D;
loc_0040212D:
    result = ExReleaseFastMutex(Arg1 + 288, (uint32_t)(*(uint32_t *)(arg6)), (uint32_t)(*(uint32_t *)(v_stack_mE8)), v_stack_mE8);
    local_r14 = (0) << (12);
    *(uint64_t *)(arg5) = local_r14;
    *(uint64_t *)(arg7) = 0;
loc_00402158:
    if (Arg8 != 0) goto loc_004028D8;
loc_00402166:
    result = ((*(uint32_t *)(arg6)) != 0) ? 1 : 0;
    local_rsp = (local_rsp) + (288);
    return result;
loc_00402181:
    if ((*(uint32_t *)(v_stack_p10 + 0x4)) == 0) goto loc_0040265D;
loc_0040218B:
    if (v_stack_p168 == 0) goto loc_00402320;
    local_r14 = (*(uint64_t *)(v_stack_p168)) >> (12);
    local_rbx = (*(uint64_t *)(v_stack_p168) - 1) + ((uint32_t)((uint32_t)(v_stack_mA0)));
    local_rbx = (local_rbx) >> (12);
    result = CcFindBitmapRangeToClean(v_stack_p10, local_r14, (uint32_t)(*(uint32_t *)(v_stack_mE8)), v_stack_p168);
    Arg1 = ((uint32_t)(*(uint32_t *)(result + 0x18))) + (*(uint64_t *)(result + 0x10));
    if (local_rbx < Arg1) goto loc_00401F66;
    result = (*(uint64_t *)(result + 0x10)) + ((uint32_t)(*(uint32_t *)(result + 0x1C)));
    if (local_r14 > result) goto loc_00401F66;
    if (local_rbx >= result) goto loc_00402362;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) - (*(uint32_t *)(result + 0x10)));
    goto loc_00402362;
loc_004021FD:
    if (v_stack_p10 != 0) goto loc_004022F7;
loc_00402206:
    Arg1 = ((uint32_t)(*(uint32_t *)(result + 0x1C))) >> (5);
    if (v_stack_p168 > (*(uint64_t *)(result + 0x28) + Arg1 * 4)) goto loc_00402899;
    if (v_stack_p10 != 0) goto loc_00402234;
    if ((*(uint32_t *)(arg6)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA08646))))) goto loc_00402075;
loc_00402234:
    Arg3 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_mE8))) - ((uint32_t)(v_stack_mA0)));
    *(uint32_t *)(v_stack_p168) = Arg3;
    local_rsi = (uint32_t)((v_stack_mA0) + ((uint32_t)(v_stack_mA0)));
    if (condition_is_not_equal) goto loc_00402069;
    Arg4 = (v_stack_p168) + (4);
    if (Arg4 > v_stack_mF8) goto loc_00402075;
    goto loc_00402069;
loc_0040225D:
    *(uint32_t *)(arg1 + 0xC8) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x4)));
    goto loc_0040212D;
loc_0040226C:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg6))) == 0) goto loc_0040266A;
    if (v_stack_p168 == 0) goto loc_0040262A;
loc_00402287:
    result = ExReleaseFastMutex(Arg1 + 288, local_r14, Arg3, Arg4);
    if (local_rbx == 0) goto loc_00402158;
    goto loc_004024CC;
loc_004022A1:
    Arg2 = Arg1 + 288;
    if (Arg4 != 0) { Arg2 = Arg4; }
    if (*(uint64_t *)(Arg2) == 0) goto loc_00401F97;
    result = (*(uint64_t *)(Arg2)) + (0x1000ULL);
    v_stack_pA8 = result;
    result = CcFindBcb(Arg1, Arg2, v_stack_pA8, v_stack_p58);
    if ((uint8_t)(result) == 0) goto loc_004027BF;
    goto loc_00401F97;
loc_004022F7:
    result = (*(uint64_t *)(v_stack_p10)) + (0xFFFULL);
    Arg1 = ((uint32_t)((uint32_t)(local_rbx))) + (result);
    Arg1 = (Arg1) >> (12);
    result = ((uint32_t)(*(uint32_t *)(arg6))) + (local_r14);
    if (result >= ((uint32_t)((uint32_t)(Arg1)))) goto loc_00402075;
    goto loc_00402206;
loc_00402320:
    if ((uint32_t)(v_stack_p58) == 0) goto loc_0040282E;
loc_0040232B:
    if (Arg9 != 0) goto loc_00402837;
loc_0040233C:
    result = CcFindBitmapRangeToClean(v_stack_p10, 0, Arg1 + 16, v_stack_p58);
    if (0 > ((uint32_t)(*(uint32_t *)(result + 0x1C)) + *(uint64_t *)(result + 0x10) * 1)) goto loc_00402843;
loc_0040235E:
loc_00402362:
    Arg1 = ((uint32_t)(*(uint32_t *)(result + 0x1C))) >> (5);
    v_stack_p60 = *(uint64_t *)(result + 0x28) + Arg1 * 4;
    Arg2 = ((uint32_t)(*(uint32_t *)(result + 0x18))) + (*(uint64_t *)(result + 0x10));
    if (0 >= Arg2) { Arg2 = 0; }
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg2))) - (*(uint32_t *)(result + 0x10)));
    v_stack_p68 = result;
    Arg1 = ((uint32_t)((uint32_t)(result))) >> (5);
    v_stack_p70 = *(uint64_t *)(result + 0x28) + Arg1 * 4;
    local_rsi = (uint32_t)((v_stack_p58) | (0xFFFFFFFFULL));
    local_rsi = (uint32_t)((local_rsi) << ((uint8_t)(Arg2)));
    if ((((uint32_t)(local_rsi)) & ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x28) + arg1 * 4))))) == 0) goto loc_004026BB;
loc_004023BF:
    local_rsi = (uint32_t)(-(local_rsi));
    v_stack_p50 = (uint32_t)(local_rsi);
    if ((((uint32_t)(local_rsi)) & ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x28) + arg1 * 4))))) != 0) goto loc_004023D6;
loc_004023C9:
    local_rsi = (uint32_t)((local_rsi) + ((uint32_t)(local_rsi)));
    local_r14 = (Arg2) + 1;
    if ((((uint32_t)(local_rsi)) & ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x28) + arg1 * 4))))) == 0) goto loc_004023C9;
    v_stack_p50 = (uint32_t)(local_rsi);
loc_004023D6:
    if (v_stack_p58 == 0) goto loc_00402042;
    Arg1 = ((uint32_t)(v_stack_p170)) + (0xFFFULL);
    Arg2 = (*(uint64_t *)(v_stack_p58)) + (Arg1);
    Arg2 = (Arg2) >> (12);
    if (local_r14 >= Arg2) goto loc_00401F66;
    if ((*(uint64_t *)(arg1 + 0x10)) == (Arg1 + 16)) goto loc_00402042;
    v_stack_p54 = 1;
    goto loc_00401F66;
loc_0040241A:
    if ((*(uint8_t *)(local_rsi + 0x2)) == 0) goto loc_0040202C;
    result = (Arg1 + 16) + (*(uint64_t *)(arg5));
    if ((*(uint64_t *)(local_rsi + 0x8)) != result) goto loc_0040202C;
    if ((*(uint32_t *)(local_rsi + 0x40)) != 0) goto loc_0040202C;
    if (((*(uint64_t *)(local_rsi + 0x8)) & (0x1FFFFFFULL)) == 0) goto loc_0040202C;
    goto loc_0040258B;
loc_00402457:
    result = guard_dispatch_icall(*(uint64_t *)(*(uint64_t *)(arg1 + 0xF8)), *(uint64_t *)(v_stack_p58), *(uint64_t *)(result + 0x28) + Arg1 * 4, v_stack_p58);
    goto loc_00401F37;
loc_004024CC:
    if (((*(uint32_t *)(arg1 + 0x98)) & (0x2000000ULL)) != 0) goto loc_004024EC;
    goto loc_004024F3;
loc_004024EC:
loc_004024F3:
    result = guard_dispatch_icall(*(uint64_t *)(*(uint64_t *)(arg1 + 0xF8)), local_rbx, *(uint64_t *)(result + 0x28) + Arg1 * 4, v_stack_p58);
    goto loc_00402158;
loc_00402564:
    if (v_stack_p58 != 0) goto loc_0040286A;
loc_0040256D:
    if ((*(uint64_t *)(local_rsi + 0x8)) < (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xF8))))) goto loc_00402005;
    goto loc_00402581;
loc_0040257C:
    if (v_stack_p58 == 0) goto loc_0040256D;
loc_00402581:
    if (v_stack_p54 != 0) goto loc_004026F3;
loc_0040258B:
    result = ExReleaseFastMutex(Arg1 + 288, local_rbx, *(uint64_t *)(result + 0x28) + Arg1 * 4, v_stack_p58);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x98))) & (514));
    if (((uint32_t)(result)) == 512) goto loc_0040271F;
    result = CcUnpinFileDataEx(local_rsi, 1, 2, v_stack_p58);
    result = ExAcquireFastMutex(Arg1 + 288, 1, 2, v_stack_p58);
loc_004025D5:
    v_stack_p54 = 0;
    if ((*(uint32_t *)(arg6)) == 0) goto loc_0040270B;
loc_004025E3:
    *(uint64_t *)(arg7) = local_rsi;
    result = (uint32_t)(*(uint32_t *)(local_rsi + 0x4));
    if (((*(uint32_t *)(arg1 + 0x98)) & (0x3000000ULL)) != 0) {
        result = *(uint64_t *)(local_rsi + 0x30);
        if (result > local_rbx) { local_rbx = result; }
    }
loc_00402611:
    local_rsi = (*(uint64_t *)(local_rsi + 0x18)) - (16);
    v_stack_p58 = local_rsi;
    goto loc_00401F9F;
loc_0040262A:
    result = (result) + (*(uint64_t *)(v_stack_p178));
    *(uint64_t *)(arg1 + 0xD0) = result;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg6))) >> (12));
    if ((*(uint32_t *)(arg1 + 0xC8)) <= ((uint32_t)(Arg1))) goto loc_0040287C;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0xC8))) - ((uint32_t)(Arg1)));
    *(uint32_t *)(arg1 + 0xC8) = (uint32_t)(result);
    goto loc_00402287;
loc_0040265D:
    if ((uint32_t)(local_rsi) != 0) goto loc_0040218B;
    goto loc_00401F5E;
loc_0040266A:
    if ((*(uint64_t *)(arg1 + 0xD0)) == 0) goto loc_00402287;
    if (v_stack_p168 != 0) goto loc_00402287;
    *(uint64_t *)(arg1 + 0xD0) = 0;
    goto loc_00401F79;
loc_00402693:
    if ((*(uint32_t *)(result + 0x18)) == ((uint32_t)(v_stack_p68))) goto loc_004028C4;
loc_004026A2:
    if (v_stack_p170 != 0) goto loc_00402120;
    result = ((uint32_t)(*(uint32_t *)(arg6))) + (local_r14);
    goto loc_0040211C;
loc_004026BB:
    local_rsi = (uint32_t)((local_rsi) | (0xFFFFFFFFULL));
    v_stack_p50 = (uint32_t)(local_rsi);
    local_r14 = (local_r14) & (-32);
    v_stack_p68 = v_stack_p68;
loc_004026D0:
    local_r11 = (*(uint64_t *)(result + 0x28) + Arg1 * 4) + (4);
    v_stack_p70 = local_r11;
    local_r14 = (local_r14) + (32);
    if (local_r11 > (Arg1 + 16)) goto loc_0040284F;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_r11))) != 0) goto loc_004023BF;
    goto loc_004026D0;
loc_004026F3:
    result = (*(uint64_t *)(local_rsi + 0x8)) >> (12);
    if (local_r14 <= ((uint32_t)((uint32_t)(result)))) goto loc_0040203E;
    goto loc_0040258B;
loc_0040270B:
    *(uint64_t *)(arg5) = *(uint64_t *)(local_rsi + 0x8);
    goto loc_004025E3;
loc_0040271F:
    Arg2 = ((*(uint32_t *)(arg6)) == 0) ? 1 : 0;
    result = ExAcquireResourceExclusiveLite(local_rsi + 72, Arg2, Arg1 + 16, v_stack_p168);
    if ((uint8_t)(result) == 0) goto loc_004027E9;
    result = ExAcquireFastMutex(Arg1 + 288, Arg2, Arg1 + 16, v_stack_p168);
    if ((uint8_t)(*(uint8_t *)(local_rsi + 0x2)) == 0) goto loc_00402783;
    if (((*(uint32_t *)(arg1 + 0x98)) & (0x1000000ULL)) == 0) goto loc_004025D5;
    if (v_stack_p178 == 0) goto loc_004025D5;
    if ((*(uint64_t *)(local_rsi + 0x30)) <= (*(uint64_t *)(v_stack_p178))) goto loc_004025D5;
    if ((uint8_t)(*(uint8_t *)(local_rsi + 0x2)) != 0) {
    }
    result = ExReleaseFastMutex(Arg1 + 288, v_stack_p178, Arg1 + 16, v_stack_p168);
    Arg3 = 0;
    Arg2 = 0;
    result = CcUnpinFileDataEx(local_rsi, Arg2, Arg3, v_stack_p168);
    result = ExAcquireFastMutex(Arg1 + 288, Arg2, Arg3, v_stack_p168);
    if ((*(uint32_t *)(arg6)) != 0) goto loc_00402802;
    goto loc_00402611;
loc_004027BF:
    local_rsi = (*(uint64_t *)(v_stack_p58 + 0x18)) - (16);
    v_stack_p58 = local_rsi;
    goto loc_00401F97;
loc_004027D6:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsi + 0x3D0))) - ((uint32_t)(Arg1 + 288)));
    *(uint32_t *)(local_rsi + 0x3D0) = (uint32_t)(result);
    goto loc_004020E8;
loc_004027E9:
    Arg3 = 0;
    result = CcUnpinFileDataEx(local_rsi, 1, Arg3, v_stack_p168);
    result = ExAcquireFastMutex(Arg1 + 288, 1, Arg3, v_stack_p168);
loc_00402802:
    goto loc_00402024;
loc_0040280B:
    Arg4 = 0;
    Arg3 = 0;
    Arg2 = 0;
    result = PsBoostThreadIoEx(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, Arg3, Arg4);
    goto loc_00401F00;
loc_0040282E:
    goto loc_0040232B;
loc_00402837:
    local_r14 = (*(uint64_t *)(result)) >> (12);
    goto loc_0040233C;
loc_00402843:
    local_r14 = ((uint32_t)(*(uint32_t *)(result + 0x18))) + (0);
    goto loc_0040235E;
loc_0040284F:
    *(uint32_t *)(result + 0x1C) = (uint32_t)(Arg2 - 1);
loc_0040286A:
    if ((*(uint64_t *)(v_stack_p178)) >= (*(uint64_t *)(local_rsi + 0x20))) goto loc_00402005;
    goto loc_0040257C;
loc_0040287C:
    *(uint32_t *)(arg1 + 0xC8) = 0;
    goto loc_00402287;
loc_00402888:
loc_00402899:
    v_stack_p20 = 0;
    Arg4 = 0;
    result = KeBugCheckEx(Arg4 + 52, (uint32_t)(0x128EULL), 0xFFFFFFFFC0000420ULL, Arg4);
loc_004028B7:
    result = CcInsertIntoCleanSharedCacheMapList(Arg1, (uint32_t)(0x128EULL), 0xFFFFFFFFC0000420ULL, Arg4);
    goto loc_004020F2;
loc_004028C4:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg6))) - (*(uint32_t *)(result + 0x10)));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(local_r14)));
    *(uint32_t *)(result + 0x18) = (uint32_t)(Arg1);
    goto loc_004026A2;
loc_004028D8:
    Arg4 = 0;
    Arg3 = 0;
    result = PsBoostThreadIoEx(*(uint64_t *)(gs_base + (0 + 0x188)), 1, Arg3, Arg4);
    goto loc_00402166;
loc_004028F3:
    v_stack_p20 = 0;
    Arg4 = 0;
    result = KeBugCheckEx(Arg4 + 52, (uint32_t)(0x12BDULL), 0xFFFFFFFFC0000420ULL, Arg4);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x0` | `64` | `W` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x70` | `32` | `R` |
| `Arg1` | `+ 0x98` | `32` | `R` |
| `Arg1` | `+ 0xA8` | `64` | `R` |
| `Arg1` | `+ 0xC8` | `32` | `R` |
| `Arg1` | `+ 0xC8` | `32` | `W` |
| `Arg1` | `+ 0xD0` | `64` | `R` |
| `Arg1` | `+ 0xD0` | `64` | `W` |
| `Arg1` | `+ 0xF8` | `64` | `R` |
| `Arg1` | `+ 0x100` | `64` | `R` |
| `Arg1` | `+ 0x120` | `64` | `R` |
| `Arg1` | `+ 0x218` | `64` | `R` |
| `Arg5` | `+ 0x0` | `64` | `R` |
| `Arg5` | `+ 0x0` | `64` | `W` |
| `Arg6` | `+ 0x0` | `32` | `R` |
| `Arg6` | `+ 0x0` | `32` | `R/W` |
| `Arg6` | `+ 0x0` | `32` | `W` |
| `Arg7` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00401E74&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
