# ExpAllocatePoolWithQuotaTag

- RVA: `0x00B82210`–`0x00B8283E` (길이 `1,582` bytes)
- VA: `0x0000000140B82210`
- 실행 섹션: `POOLCODE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007BDB4`
- 디코드: `370`개 명령, `1,582/1,582` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **15**; 고유 호출 대상: **10**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **17**

### Outgoing calls
- `0x00B82260` → [ExpAllocatePoolWithTagFromNode](../../text/35/ExpAllocatePoolWithTagFromNode_function_0035B970.md) (function, `0x0035B970`)
- `0x00B8241C` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00B824B4` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)
- `0x00B824EB` → [ExFreePoolWithTag](ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00B8251E` → [ExAcquireSpinLockShared](../../text/24/ExAcquireSpinLockShared_function_0024DCE0.md) (function, `0x0024DCE0`)
- `0x00B82592` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00B825E8` → [KiLowerIrqlProcessIrqlFlags](../../text/4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x00B8260E` → [RtlCSparseBitmapBitmaskRead](../../text/36/RtlCSparseBitmapBitmaskRead_function_0036190C.md) (function, `0x0036190C`)
- `0x00B8263F` → [RtlpHpVaMgrCtxQuery](../../text/32/RtlpHpVaMgrCtxQuery_function_003273C0.md) (function, `0x003273C0`)
- `0x00B82658` → [ExAcquireSpinLockShared](../../text/24/ExAcquireSpinLockShared_function_0024DCE0.md) (function, `0x0024DCE0`)
- `0x00B82724` → [KiLowerIrqlProcessIrqlFlags](../../text/4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x00B8277E` → [PspExpandQuota](../../text/39/PspExpandQuota_function_00390660.md) (function, `0x00390660`)
- `0x00B827D2` → [ExpReleaseSpinLockSharedFromDpcLevelInstrumented](../../text/2F/ExpReleaseSpinLockSharedFromDpcLevelInstrumented_function_002F0F48.md) (function, `0x002F0F48`)
- `0x00B827F9` → [ExpReleaseSpinLockSharedFromDpcLevelInstrumented](../../text/2F/ExpReleaseSpinLockSharedFromDpcLevelInstrumented_function_002F0F48.md) (function, `0x002F0F48`)
- `0x00B82821` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)

### Direct callers
- [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) at `0x0035B644`
- [ExAllocatePoolMm](../../text/35/ExAllocatePoolMm_function_0035B690.md) at `0x0035B776`
- [ExAllocatePool2](ExAllocatePool2_function_00B820F0.md) at `0x00B821ED`
- [ExAllocatePool3](ExAllocatePool3_function_00B84270.md) at `0x00B8450D`

### Static image references
- `0x00B82240` → RVA `0x00FC6AB0` (`ALMOSTRO`; read)
- `0x00B8227B` → RVA `0x00EFED20` (`.data`; read)
- `0x00B822CE` → RVA `0x00FC7228` (`ALMOSTRO`; read)
- `0x00B822F4` → RVA `0x00FC7350` (`ALMOSTRO`; read)
- `0x00B823F0` → RVA `0x00E28300` (`.data`; read)
- `0x00B824F5` → RVA `0x00EEEF40` (`.data`; read)
- `0x00B824FC` → RVA `0x00EEEF60` (`.data`; read)
- `0x00B82517` → RVA `0x00EFACF8` (`.data`; read)
- `0x00B82523` → RVA `0x00EFED38` (`.data`; read)
- `0x00B8252D` → RVA `0x00EFED30` (`.data`; read)
- `0x00B825B8` → RVA `0x00FC6B06` (`ALMOSTRO`; read)
- `0x00B825C5` → RVA `0x00EFACF8` (`.data`; read/write)
- `0x00B825D7` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x00B825F9` → RVA `0x00E68610` (`.data`; read)
- `0x00B82600` → RVA `0x00E68608` (`.data`; read)
- `0x00B8262E` → RVA `0x00E68658` (`.data`; read)
- `0x00B827B5` → RVA `0x00F0DE58` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **14**
  - `0x00B82260` → [ExpAllocatePoolWithTagFromNode](../../text/35/ExpAllocatePoolWithTagFromNode_function_0035B970.md) (`POOLCODE` → `.text`)
  - `0x00B8241C` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`POOLCODE` → `.text`)
  - `0x00B824B4` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (`POOLCODE` → `.text`)
  - `0x00B8251E` → [ExAcquireSpinLockShared](../../text/24/ExAcquireSpinLockShared_function_0024DCE0.md) (`POOLCODE` → `.text`)
  - `0x00B82592` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`POOLCODE` → `.text`)
  - `0x00B825E8` → [KiLowerIrqlProcessIrqlFlags](../../text/4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (`POOLCODE` → `.text`)
  - `0x00B8260E` → [RtlCSparseBitmapBitmaskRead](../../text/36/RtlCSparseBitmapBitmaskRead_function_0036190C.md) (`POOLCODE` → `.text`)
  - `0x00B8263F` → [RtlpHpVaMgrCtxQuery](../../text/32/RtlpHpVaMgrCtxQuery_function_003273C0.md) (`POOLCODE` → `.text`)
  - `0x00B82658` → [ExAcquireSpinLockShared](../../text/24/ExAcquireSpinLockShared_function_0024DCE0.md) (`POOLCODE` → `.text`)
  - `0x00B82724` → [KiLowerIrqlProcessIrqlFlags](../../text/4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (`POOLCODE` → `.text`)
  - `0x00B8277E` → [PspExpandQuota](../../text/39/PspExpandQuota_function_00390660.md) (`POOLCODE` → `.text`)
  - `0x00B827D2` → [ExpReleaseSpinLockSharedFromDpcLevelInstrumented](../../text/2F/ExpReleaseSpinLockSharedFromDpcLevelInstrumented_function_002F0F48.md) (`POOLCODE` → `.text`)
  - `0x00B827F9` → [ExpReleaseSpinLockSharedFromDpcLevelInstrumented](../../text/2F/ExpReleaseSpinLockSharedFromDpcLevelInstrumented_function_002F0F48.md) (`POOLCODE` → `.text`)
  - `0x00B82821` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`POOLCODE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B82210  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
00B82215  55                              push rbp
00B82216  57                              push rdi
00B82217  41 54                           push r12
00B82219  41 55                           push r13
00B8221B  41 56                           push r14
00B8221D  48 81 EC 80 00 00 00            sub rsp, 0x80
00B82224  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00B8222D  45 33 F6                        xor r14d, r14d
00B82230  45 8B E8                        mov r13d, r8d
00B82233  48 8B F9                        mov rdi, rcx
00B82236  45 8B E6                        mov r12d, r14d
00B82239  48 8B A8 B8 00 00 00            mov rbp, qword ptr [rax + 0xb8]
00B82240  48 3B 2D 69 48 44 00            cmp rbp, qword ptr [rip + 0x444869]
00B82247  75 04                           jne 0x140b8224d
00B82249  48 83 E7 FE                     and rdi, 0xfffffffffffffffe
00B8224D  48 89 B4 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rsi
00B82255  48 8B CF                        mov rcx, rdi
00B82258  4C 89 BC 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], r15
00B82260  E8 0B 97 7D FF                  call 0x14035b970
00B82265  48 8B D8                        mov rbx, rax
00B82268  48 85 C0                        test rax, rax
00B8226B  0F 84 48 02 00 00               je 0x140b824b9
00B82271  40 F6 C7 01                     test dil, 1
00B82275  0F 84 3E 02 00 00               je 0x140b824b9
00B8227B  8B 05 9F CA 37 00               mov eax, dword ptr [rip + 0x37ca9f]
00B82281  85 C0                           test eax, eax
00B82283  0F 85 33 01 00 00               jne 0x140b823bc
00B82289  48 8B C3                        mov rax, rbx
00B8228C  25 FF 0F 00 00                  and eax, 0xfff
00B82291  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00B82296  0F 84 7B 02 00 00               je 0x140b82517
00B8229C  F6 43 F3 04                     test byte ptr [rbx - 0xd], 4
00B822A0  48 8D 53 F0                     lea rdx, [rbx - 0x10]
00B822A4  74 10                           je 0x140b822b6
00B822A6  0F B7 02                        movzx eax, word ptr [rdx]
00B822A9  0F B6 C8                        movzx ecx, al
00B822AC  48 F7 D9                        neg rcx
00B822AF  48 C1 E1 04                     shl rcx, 4
00B822B3  48 03 D1                        add rdx, rcx
00B822B6  0F B7 42 02                     movzx eax, word ptr [rdx + 2]
00B822BA  44 0F B6 E0                     movzx r12d, al
00B822BE  49 C1 E4 04                     shl r12, 4
00B822C2  66 C1 E8 08                     shr ax, 8
00B822C6  A8 08                           test al, 8
00B822C8  74 0E                           je 0x140b822d8
00B822CA  48 8D 42 08                     lea rax, [rdx + 8]
00B822CE  48 33 15 53 4F 44 00            xor rdx, qword ptr [rip + 0x444f53]
00B822D5  48 89 10                        mov qword ptr [rax], rdx
00B822D8  48 8B CF                        mov rcx, rdi
00B822DB  81 E1 00 01 00 00               and ecx, 0x100
00B822E1  48 3B 2D C8 47 44 00            cmp rbp, qword ptr [rip + 0x4447c8]
00B822E8  0F 84 48 01 00 00               je 0x140b82436
00B822EE  48 85 C9                        test rcx, rcx
00B822F1  41 8B C6                        mov eax, r14d
00B822F4  48 8D 0D 55 50 44 00            lea rcx, [rip + 0x445055]
00B822FB  0F 95 C0                        setne al
00B822FE  44 8B D0                        mov r10d, eax
00B82301  48 8B 85 F8 02 00 00            mov rax, qword ptr [rbp + 0x2f8]
00B82308  45 8B FA                        mov r15d, r10d
00B8230B  49 C1 E7 07                     shl r15, 7
00B8230F  4C 89 54 24 48                  mov qword ptr [rsp + 0x48], r10
00B82314  4C 03 F8                        add r15, rax
00B82317  42 0F B6 0C D1                  movzx ecx, byte ptr [rcx + r10*8]
00B8231C  88 4C 24 30                     mov byte ptr [rsp + 0x30], cl
00B82320  41 0F 0D 0F                     prefetchw byte ptr [r15]
00B82324  49 8B 37                        mov rsi, qword ptr [r15]
00B82327  F0 44 09 34 24                  lock or dword ptr [rsp], r14d
00B8232C  49 8B 47 40                     mov rax, qword ptr [r15 + 0x40]
00B82330  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00B82335  4A 8D 14 26                     lea rdx, [rsi + r12]
00B82339  48 3B D6                        cmp rdx, rsi
00B8233C  0F 82 E0 00 00 00               jb 0x140b82422
00B82342  48 3B D0                        cmp rdx, rax
00B82345  0F 87 FE 03 00 00               ja 0x140b82749
00B8234B  48 8B C6                        mov rax, rsi
00B8234E  F0 49 0F B1 17                  lock cmpxchg qword ptr [r15], rdx
00B82353  48 8B F0                        mov rsi, rax
00B82356  75 D4                           jne 0x140b8232c
00B82358  41 0F 0D 4F 08                  prefetchw byte ptr [r15 + 8]
00B8235D  49 8B 47 08                     mov rax, qword ptr [r15 + 8]
00B82361  48 3B D0                        cmp rdx, rax
00B82364  0F 87 C8 03 00 00               ja 0x140b82732
00B8236A  48 85 ED                        test rbp, rbp
00B8236D  0F 84 C3 00 00 00               je 0x140b82436
00B82373  F6 44 24 30 04                  test byte ptr [rsp + 0x30], 4
00B82378  0F 84 B8 00 00 00               je 0x140b82436
00B8237E  49 8B D4                        mov rdx, r12
00B82381  F0 4A 0F C1 94 D5 00 02 00 00   lock xadd qword ptr [rbp + r10*8 + 0x200], rdx
00B8238B  49 03 D4                        add rdx, r12
00B8238E  42 0F 0D 8C D5 10 02 00 00      prefetchw byte ptr [rbp + r10*8 + 0x210]
00B82397  4A 8B 84 D5 10 02 00 00         mov rax, qword ptr [rbp + r10*8 + 0x210]
00B8239F  48 3B D0                        cmp rdx, rax
00B823A2  0F 86 8E 00 00 00               jbe 0x140b82436
00B823A8  48 8B C8                        mov rcx, rax
00B823AB  F0 4A 0F B1 94 D5 10 02 00 00   lock cmpxchg qword ptr [rbp + r10*8 + 0x210], rdx
00B823B5  48 3B C1                        cmp rax, rcx
00B823B8  75 E5                           jne 0x140b8239f
00B823BA  EB 7A                           jmp 0x140b82436
00B823BC  66 85 DB                        test bx, bx
00B823BF  0F 84 31 02 00 00               je 0x140b825f6
00B823C5  41 8B C6                        mov eax, r14d
00B823C8  48 98                           cdqe
00B823CA  C7 44 24 40 00 00 10 00         mov dword ptr [rsp + 0x40], 0x100000
00B823D2  C7 44 24 44 00 00 00 01         mov dword ptr [rsp + 0x44], 0x1000000
00B823DA  8B 4C 84 40                     mov ecx, dword ptr [rsp + rax*4 + 0x40]
00B823DE  48 8D 04 40                     lea rax, [rax + rax*2]
00B823E2  48 F7 D9                        neg rcx
00B823E5  48 C1 E0 06                     shl rax, 6
00B823E9  48 23 CB                        and rcx, rbx
00B823EC  48 33 49 10                     xor rcx, qword ptr [rcx + 0x10]
00B823F0  48 33 0D 09 5F 2A 00            xor rcx, qword ptr [rip + 0x2a5f09]
00B823F7  48 2B C8                        sub rcx, rax
00B823FA  48 81 E9 40 01 00 00            sub rcx, 0x140
00B82401  48 85 C9                        test rcx, rcx
00B82404  0F 85 EB 00 00 00               jne 0x140b824f5
00B8240A  4C 8B CB                        mov r9, rbx
00B8240D  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
00B82412  45 33 C0                        xor r8d, r8d
00B82415  33 D2                           xor edx, edx
00B82417  B9 C2 00 00 00                  mov ecx, 0xc2
00B8241C  E8 3F B2 97 FF                  call 0x1404fd660
00B82421  CC                              int3
00B82422  48 8D 05 27 4F 44 00            lea rax, [rip + 0x444f27]
00B82429  42 8B 44 D0 04                  mov eax, dword ptr [rax + r10*8 + 4]
00B8242E  85 C0                           test eax, eax
00B82430  0F 88 AF 00 00 00               js 0x140b824e5
00B82436  49 8B F6                        mov rsi, r14
00B82439  4C 39 74 24 50                  cmp qword ptr [rsp + 0x50], r14
00B8243E  0F 84 0D 02 00 00               je 0x140b82651
00B82444  F6 43 F3 04                     test byte ptr [rbx - 0xd], 4
00B82448  48 8D 73 F0                     lea rsi, [rbx - 0x10]
00B8244C  74 10                           je 0x140b8245e
00B8244E  0F B7 06                        movzx eax, word ptr [rsi]
00B82451  0F B6 C8                        movzx ecx, al
00B82454  48 F7 D9                        neg rcx
00B82457  48 C1 E1 04                     shl rcx, 4
00B8245B  48 03 F1                        add rsi, rcx
00B8245E  F6 46 03 08                     test byte ptr [rsi + 3], 8
00B82462  74 4A                           je 0x140b824ae
00B82464  48 8B FE                        mov rdi, rsi
00B82467  48 8B CE                        mov rcx, rsi
00B8246A  48 33 7E 08                     xor rdi, qword ptr [rsi + 8]
00B8246E  48 33 3D B3 4D 44 00            xor rdi, qword ptr [rip + 0x444db3]
00B82475  48 33 0D AC 4D 44 00            xor rcx, qword ptr [rip + 0x444dac]
00B8247C  48 33 CD                        xor rcx, rbp
00B8247F  48 89 4E 08                     mov qword ptr [rsi + 8], rcx
00B82483  48 85 FF                        test rdi, rdi
00B82486  74 26                           je 0x140b824ae
00B82488  48 83 FF FF                     cmp rdi, -1
00B8248C  74 20                           je 0x140b824ae
00B8248E  48 B8 00 00 00 00 00 80 FF FF   movabs rax, 0xffff800000000000
00B82498  48 3B F8                        cmp rdi, rax
00B8249B  0F 82 62 03 00 00               jb 0x140b82803
00B824A1  0F B6 07                        movzx eax, byte ptr [rdi]
00B824A4  24 7F                           and al, 0x7f
00B824A6  3C 03                           cmp al, 3
00B824A8  0F 85 55 03 00 00               jne 0x140b82803
00B824AE  41 8B D5                        mov edx, r13d
00B824B1  48 8B CD                        mov rcx, rbp
00B824B4  E8 57 E2 68 FF                  call 0x140210710
00B824B9  4C 8B BC 24 B8 00 00 00         mov r15, qword ptr [rsp + 0xb8]
00B824C1  48 8B C3                        mov rax, rbx
00B824C4  48 8B 9C 24 C0 00 00 00         mov rbx, qword ptr [rsp + 0xc0]
00B824CC  48 8B B4 24 B0 00 00 00         mov rsi, qword ptr [rsp + 0xb0]
00B824D4  48 81 C4 80 00 00 00            add rsp, 0x80
00B824DB  41 5E                           pop r14
00B824DD  41 5D                           pop r13
00B824DF  41 5C                           pop r12
00B824E1  5F                              pop rdi
00B824E2  5D                              pop rbp
00B824E3  C3                              ret
00B824E4  CC                              int3
00B824E5  41 8B D5                        mov edx, r13d
00B824E8  48 8B CB                        mov rcx, rbx
00B824EB  E8 80 03 00 00                  call 0x140b82870
00B824F0  49 8B DE                        mov rbx, r14
00B824F3  EB C4                           jmp 0x140b824b9
00B824F5  48 8D 05 44 CA 36 00            lea rax, [rip + 0x36ca44]
00B824FC  48 8D 15 5D CA 36 00            lea rdx, [rip + 0x36ca5d]
00B82503  48 3B C2                        cmp rax, rdx
00B82506  0F 8D 7D FD FF FF               jge 0x140b82289
00B8250C  48 3B 08                        cmp rcx, qword ptr [rax]
00B8250F  74 A8                           je 0x140b824b9
00B82511  48 83 C0 08                     add rax, 8
00B82515  EB EC                           jmp 0x140b82503
00B82517  48 8D 0D DA 87 37 00            lea rcx, [rip + 0x3787da]
00B8251E  E8 BD B7 6C FF                  call 0x14024dce0
00B82523  4C 8B 0D 0E C8 37 00            mov r9, qword ptr [rip + 0x37c80e]
00B8252A  48 8B CB                        mov rcx, rbx
00B8252D  4C 8B 15 FC C7 37 00            mov r10, qword ptr [rip + 0x37c7fc]
00B82534  41 BB 01 00 00 00               mov r11d, 1
00B8253A  48 C1 E9 0C                     shr rcx, 0xc
00B8253E  48 69 D1 5F 9E 00 00            imul rdx, rcx, 0x9e5f
00B82545  41 8D 49 FF                     lea ecx, [r9 - 1]
00B82549  0F B6 F0                        movzx esi, al
00B8254C  4C 8B C2                        mov r8, rdx
00B8254F  49 C1 E8 20                     shr r8, 0x20
00B82553  44 33 C2                        xor r8d, edx
00B82556  44 23 C1                        and r8d, ecx
00B82559  41 8B C8                        mov ecx, r8d
00B8255C  48 C1 E1 05                     shl rcx, 5
00B82560  49 03 CA                        add rcx, r10
00B82563  48 8B 01                        mov rax, qword ptr [rcx]
00B82566  48 3B C3                        cmp rax, rbx
00B82569  74 2D                           je 0x140b82598
00B8256B  41 FF C0                        inc r8d
00B8256E  41 8B C0                        mov eax, r8d
00B82571  49 3B C1                        cmp rax, r9
00B82574  72 E3                           jb 0x140b82559
00B82576  45 85 DB                        test r11d, r11d
00B82579  0F 85 B4 02 00 00               jne 0x140b82833
00B8257F  BA 22 00 00 00                  mov edx, 0x22
00B82584  44 8B CF                        mov r9d, edi
00B82587  4C 8B C3                        mov r8, rbx
00B8258A  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
00B8258F  8D 4A F7                        lea ecx, [rdx - 9]
00B82592  E8 C9 B0 97 FF                  call 0x1404fd660
00B82597  CC                              int3
00B82598  48 85 C9                        test rcx, rcx
00B8259B  74 E2                           je 0x140b8257f
00B8259D  F7 41 0C 00 01 00 00            test dword ptr [rcx + 0xc], 0x100
00B825A4  74 12                           je 0x140b825b8
00B825A6  4C 8B 61 10                     mov r12, qword ptr [rcx + 0x10]
00B825AA  48 8B C3                        mov rax, rbx
00B825AD  48 33 05 74 4C 44 00            xor rax, qword ptr [rip + 0x444c74]
00B825B4  48 89 41 18                     mov qword ptr [rcx + 0x18], rax
00B825B8  F6 05 47 45 44 00 01            test byte ptr [rip + 0x444547], 1
00B825BF  0F 85 F0 01 00 00               jne 0x140b827b5
00B825C5  F0 81 25 28 87 37 00 FF FF FF BF  lock and dword ptr [rip + 0x378728], 0xbfffffff
00B825D0  F0 FF 0D 21 87 37 00            lock dec dword ptr [rip + 0x378721]
00B825D7  44 39 35 42 47 44 00            cmp dword ptr [rip + 0x444742], r14d
00B825DE  74 0D                           je 0x140b825ed
00B825E0  44 0F 20 C1                     mov rcx, cr8
00B825E4  40 0F B6 D6                     movzx edx, sil
00B825E8  E8 AB 30 97 FF                  call 0x1404f5698
00B825ED  44 0F 22 C6                     mov cr8, rsi
00B825F1  E9 E2 FC FF FF                  jmp 0x140b822d8
00B825F6  48 8B D3                        mov rdx, rbx
00B825F9  48 8D 0D 10 60 2E 00            lea rcx, [rip + 0x2e6010]
00B82600  48 2B 15 01 60 2E 00            sub rdx, qword ptr [rip + 0x2e6001]
00B82607  48 C1 EA 14                     shr rdx, 0x14
00B8260B  48 03 D2                        add rdx, rdx
00B8260E  E8 F9 F2 7D FF                  call 0x14036190c
00B82613  48 85 C0                        test rax, rax
00B82616  74 0B                           je 0x140b82623
00B82618  FF C8                           dec eax
00B8261A  83 F8 02                        cmp eax, 2
00B8261D  0F 85 A5 FD FF FF               jne 0x140b823c8
00B82623  0F 57 C0                        xorps xmm0, xmm0
00B82626  4C 8D 44 24 58                  lea r8, [rsp + 0x58]
00B8262B  48 8B D3                        mov rdx, rbx
00B8262E  48 8D 0D 23 60 2E 00            lea rcx, [rip + 0x2e6023]
00B82635  0F 11 44 24 58                  movups xmmword ptr [rsp + 0x58], xmm0
00B8263A  0F 11 44 24 68                  movups xmmword ptr [rsp + 0x68], xmm0
00B8263F  E8 7C 4D 7A FF                  call 0x1403273c0
00B82644  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
00B82649  48 8B 08                        mov rcx, qword ptr [rax]
00B8264C  E9 B0 FD FF FF                  jmp 0x140b82401
00B82651  48 8D 0D A0 86 37 00            lea rcx, [rip + 0x3786a0]
00B82658  E8 83 B6 6C FF                  call 0x14024dce0
00B8265D  4C 8B 0D D4 C6 37 00            mov r9, qword ptr [rip + 0x37c6d4]
00B82664  48 8B CB                        mov rcx, rbx
00B82667  4C 8B 15 C2 C6 37 00            mov r10, qword ptr [rip + 0x37c6c2]
00B8266E  48 C1 E9 0C                     shr rcx, 0xc
00B82672  48 69 D1 5F 9E 00 00            imul rdx, rcx, 0x9e5f
00B82679  41 8D 49 FF                     lea ecx, [r9 - 1]
00B8267D  44 0F B6 F8                     movzx r15d, al
00B82681  4C 8B C2                        mov r8, rdx
00B82684  49 C1 E8 20                     shr r8, 0x20
00B82688  44 33 C2                        xor r8d, edx
00B8268B  44 23 C1                        and r8d, ecx
00B8268E  B9 01 00 00 00                  mov ecx, 1
00B82693  41 8B D0                        mov edx, r8d
00B82696  48 C1 E2 05                     shl rdx, 5
00B8269A  49 03 D2                        add rdx, r10
00B8269D  48 8B 02                        mov rax, qword ptr [rdx]
00B826A0  48 3B C3                        cmp rax, rbx
00B826A3  74 1B                           je 0x140b826c0
00B826A5  41 FF C0                        inc r8d
00B826A8  41 8B C0                        mov eax, r8d
00B826AB  49 3B C1                        cmp rax, r9
00B826AE  72 E3                           jb 0x140b82693
00B826B0  85 C9                           test ecx, ecx
00B826B2  0F 84 C7 FE FF FF               je 0x140b8257f
00B826B8  45 8B C6                        mov r8d, r14d
00B826BB  41 8B CE                        mov ecx, r14d
00B826BE  EB D3                           jmp 0x140b82693
00B826C0  48 85 D2                        test rdx, rdx
00B826C3  0F 84 B6 FE FF FF               je 0x140b8257f
00B826C9  F7 42 0C 00 01 00 00            test dword ptr [rdx + 0xc], 0x100
00B826D0  0F 84 51 01 00 00               je 0x140b82827
00B826D6  48 8B 7A 18                     mov rdi, qword ptr [rdx + 0x18]
00B826DA  48 8B C5                        mov rax, rbp
00B826DD  48 33 3D 44 4B 44 00            xor rdi, qword ptr [rip + 0x444b44]
00B826E4  48 33 05 3D 4B 44 00            xor rax, qword ptr [rip + 0x444b3d]
00B826EB  48 33 FB                        xor rdi, rbx
00B826EE  48 33 C3                        xor rax, rbx
00B826F1  48 89 42 18                     mov qword ptr [rdx + 0x18], rax
00B826F5  F6 05 0A 44 44 00 01            test byte ptr [rip + 0x44440a], 1
00B826FC  0F 85 DA 00 00 00               jne 0x140b827dc
00B82702  F0 81 25 EB 85 37 00 FF FF FF BF  lock and dword ptr [rip + 0x3785eb], 0xbfffffff
00B8270D  F0 FF 0D E4 85 37 00            lock dec dword ptr [rip + 0x3785e4]
00B82714  39 35 06 46 44 00               cmp dword ptr [rip + 0x444606], esi
00B8271A  74 0D                           je 0x140b82729
00B8271C  44 0F 20 C1                     mov rcx, cr8
00B82720  41 0F B6 D7                     movzx edx, r15b
00B82724  E8 6F 2F 97 FF                  call 0x1404f5698
00B82729  45 0F 22 C7                     mov cr8, r15
00B8272D  E9 51 FD FF FF                  jmp 0x140b82483
00B82732  48 8B C8                        mov rcx, rax
00B82735  F0 49 0F B1 57 08               lock cmpxchg qword ptr [r15 + 8], rdx
00B8273B  48 3B C1                        cmp rax, rcx
00B8273E  0F 85 1D FC FF FF               jne 0x140b82361
00B82744  E9 21 FC FF FF                  jmp 0x140b8236a
00B82749  F6 C1 01                        test cl, 1
00B8274C  0F 84 D0 FC FF FF               je 0x140b82422
00B82752  4D 39 77 50                     cmp qword ptr [r15 + 0x50], r14
00B82756  0F 84 C6 FC FF FF               je 0x140b82422
00B8275C  49 8B CE                        mov rcx, r14
00B8275F  49 87 4F 48                     xchg qword ptr [r15 + 0x48], rcx
00B82763  48 85 C9                        test rcx, rcx
00B82766  75 37                           jne 0x140b8279f
00B82768  48 8D 44 24 38                  lea rax, [rsp + 0x38]
00B8276D  4D 8B CC                        mov r9, r12
00B82770  4C 8B C6                        mov r8, rsi
00B82773  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00B82778  49 8B D7                        mov rdx, r15
00B8277B  41 8B CA                        mov ecx, r10d
00B8277E  E8 DD DE 80 FF                  call 0x140390660
00B82783  4C 8B 54 24 48                  mov r10, qword ptr [rsp + 0x48]
00B82788  84 C0                           test al, al
00B8278A  0F 84 92 FC FF FF               je 0x140b82422
00B82790  48 8B 44 24 38                  mov rax, qword ptr [rsp + 0x38]
00B82795  0F B6 4C 24 30                  movzx ecx, byte ptr [rsp + 0x30]
00B8279A  E9 96 FB FF FF                  jmp 0x140b82335
00B8279F  48 8B C1                        mov rax, rcx
00B827A2  F0 49 0F C1 47 40               lock xadd qword ptr [r15 + 0x40], rax
00B827A8  48 03 C1                        add rax, rcx
00B827AB  0F B6 4C 24 30                  movzx ecx, byte ptr [rsp + 0x30]
00B827B0  E9 7B FB FF FF                  jmp 0x140b82330
00B827B5  8B 05 9D B6 38 00               mov eax, dword ptr [rip + 0x38b69d]
00B827BB  85 C0                           test eax, eax
00B827BD  0F 85 02 FE FF FF               jne 0x140b825c5
00B827C3  48 8B 94 24 A8 00 00 00         mov rdx, qword ptr [rsp + 0xa8]
00B827CB  48 8D 0D 26 85 37 00            lea rcx, [rip + 0x378526]
00B827D2  E8 71 E7 76 FF                  call 0x1402f0f48
00B827D7  E9 FB FD FF FF                  jmp 0x140b825d7
00B827DC  8B 05 76 B6 38 00               mov eax, dword ptr [rip + 0x38b676]
00B827E2  85 C0                           test eax, eax
00B827E4  0F 85 18 FF FF FF               jne 0x140b82702
00B827EA  48 8B 94 24 A8 00 00 00         mov rdx, qword ptr [rsp + 0xa8]
00B827F2  48 8D 0D FF 84 37 00            lea rcx, [rip + 0x3784ff]
00B827F9  E8 4A E7 76 FF                  call 0x1402f0f48
00B827FE  E9 11 FF FF FF                  jmp 0x140b82714
00B82803  48 85 F6                        test rsi, rsi
00B82806  74 04                           je 0x140b8280c
00B82808  44 8B 76 04                     mov r14d, dword ptr [rsi + 4]
00B8280C  45 8B CE                        mov r9d, r14d
00B8280F  4C 8B C3                        mov r8, rbx
00B82812  BA 0D 00 00 00                  mov edx, 0xd
00B82817  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00B8281C  B9 C2 00 00 00                  mov ecx, 0xc2
00B82821  E8 3A AE 97 FF                  call 0x1404fd660
00B82826  CC                              int3
00B82827  48 C7 C7 FF FF FF FF            mov rdi, 0xffffffffffffffff
00B8282E  E9 C2 FE FF FF                  jmp 0x140b826f5
00B82833  45 8B C6                        mov r8d, r14d
00B82836  45 8B DE                        mov r11d, r14d
00B82839  E9 1B FD FF FF                  jmp 0x140b82559
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpAllocatePoolWithQuotaTag(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned int v_stack_m64;
    unsigned int v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int8 v_stack_m78;
    unsigned __int64 v_stack_m88;
    unsigned int v_stack_mA8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int8 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p8;
    unsigned __int64 v_stack_pA8;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (128);
    v_r14 = 0;
    v_rdi = a1;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184)) == (*(unsigned __int64 *)(v_rip + 4474985))) {
        v_rdi = (a1) & (-2);
    }
    v_stack_p8 = v_rsi;
    v_stack_p10 = v_r15;
    result = ExpAllocatePoolWithTagFromNode(v_rdi, a2, a3, a4);
    if (result == 0) goto loc_00B824B9;
    if ((((unsigned __int8)(v_rdi)) & (1)) == 0) goto loc_00B824B9;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3656351))) != 0) goto loc_00B823BC;
loc_00B82289:
    result = (unsigned int)((result) & (0xFFFULL));
    v_stack_m58 = result;
    if (condition_is_equal) goto loc_00B82517;
    if (((*(unsigned __int8 *)(result - 13)) & (4)) != 0) {
        result = *(unsigned __int16 *)(result - 16);
        a1 = (unsigned __int8)(result);
        a1 = -(a1);
        a1 = (a1) << (4);
        a2 = (result - 16) + (a1);
    }
    v_r12 = ((unsigned __int8)(*(unsigned __int16 *)(a2 + 2))) << (4);
    result = (unsigned __int16)((*(unsigned __int16 *)(a2 + 2)) >> (8));
    if ((((unsigned __int8)(result)) & (8)) != 0) {
        result = a2 + 8;
        a2 = (a2) ^ (*(unsigned __int64 *)(v_rip + 4476755));
        *(unsigned __int64 *)(result) = a2;
    }
    a1 = (unsigned int)((v_rdi) & (256));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184)) == (*(unsigned __int64 *)(v_rip + 4474824))) goto loc_00B82436;
    result = (a1 != 0) ? 1 : 0;
    v_r15 = ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))))) << (7);
    v_stack_m60 = (unsigned int)((unsigned int)(result));
    v_r15 = (v_r15) + (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 760));
    v_stack_m78 = (unsigned __int8)(*(unsigned __int8 *)(v_rip + 4477013 + (unsigned int)((unsigned int)(result)) * 8));
loc_00B8232C:
loc_00B82330:
    v_stack_m70 = *(unsigned __int64 *)(v_r15 + 64);
loc_00B82335:
    if ((*(unsigned __int64 *)(v_r15) + v_r12 * 1) < (*(unsigned __int64 *)(v_r15))) goto loc_00B82422;
    if ((*(unsigned __int64 *)(v_r15) + v_r12 * 1) > (*(unsigned __int64 *)(v_r15 + 64))) goto loc_00B82749;
    if ((*(unsigned __int64 *)(v_r15) + v_r12 * 1) != (*(unsigned __int64 *)(v_r15 + 64))) goto loc_00B8232C;
loc_00B82361:
    if ((*(unsigned __int64 *)(v_r15) + v_r12 * 1) > (*(unsigned __int64 *)(v_r15 + 8))) goto loc_00B82732;
loc_00B8236A:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) == 0) goto loc_00B82436;
    if (((v_stack_m78) & (4)) == 0) goto loc_00B82436;
    a2 = (v_r12) + (v_r12);
loc_00B8239F:
    if (a2 <= (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + (unsigned int)((unsigned int)(result)) * 8 + 528))) goto loc_00B82436;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + (unsigned int)((unsigned int)(result)) * 8 + 528)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + (unsigned int)((unsigned int)(result)) * 8 + 528))) goto loc_00B8239F;
    goto loc_00B82436;
loc_00B823BC:
    if ((unsigned __int16)(result) == 0) goto loc_00B825F6;
loc_00B823C8:
    v_stack_m68 = 0x100000ULL;
    v_stack_m64 = 0x1000000ULL;
    a1 = -((unsigned int)(*(unsigned int *)(v_rsp + 0 * 4 + 64)));
    result = (0 + 0 * 2) << (6);
    a1 = (a1) & (result);
    a1 = (a1) ^ (*(unsigned __int64 *)(a1 + 16));
    a1 = (a1) ^ (*(unsigned __int64 *)(v_rip + 2776841));
    a1 = (a1) - (result);
    a1 = (a1) - (320);
loc_00B82401:
    if (a1 != 0) goto loc_00B824F5;
    v_stack_m88 = 0;
    a3 = 0;
    a2 = 0;
    result = KeBugCheckEx(194, a2, a3, result);
loc_00B82422:
    if (sign_flag) goto loc_00B824E5;
loc_00B82436:
    if (v_stack_m58 == 0) goto loc_00B82651;
    result = (unsigned int)(*(unsigned int *)(v_rip + 4476711 + (unsigned int)((unsigned int)(result)) * 8 + 4));
    v_rsi = result - 16;
    if (((*(unsigned __int8 *)(result - 13)) & (4)) != 0) {
        result = *(unsigned __int16 *)(result - 16);
        a1 = (unsigned __int8)(result);
        a1 = -(a1);
        a1 = (a1) << (4);
        v_rsi = (result - 16) + (a1);
    }
    if (((*(unsigned __int8 *)(v_rsi + 3)) & (8)) == 0) goto loc_00B824AE;
    v_rdi = (v_rsi) ^ (*(unsigned __int64 *)(v_rsi + 8));
    v_rdi = (v_rdi) ^ (*(unsigned __int64 *)(v_rip + 4476339));
    a1 = (v_rsi) ^ (*(unsigned __int64 *)(v_rip + 4476332));
    a1 = (a1) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184));
    *(unsigned __int64 *)(v_rsi + 8) = a1;
loc_00B82483:
    if (v_rdi == 0) goto loc_00B824AE;
    if (v_rdi == -1) goto loc_00B824AE;
    if (v_rdi < result) goto loc_00B82803;
    result = (unsigned __int8)((*(unsigned __int8 *)(v_rdi)) & (127));
    if (((unsigned __int8)(result)) != 3) goto loc_00B82803;
loc_00B824AE:
    result = ObfReferenceObjectWithTag(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), (unsigned int)((unsigned int)((unsigned int)(a3))), a3, result);
loc_00B824B9:
    v_rsp = (v_rsp) + (128);
    return result;
loc_00B824E5:
    result = ExFreePoolWithTag(v_stack_p18, (unsigned int)((unsigned int)((unsigned int)(a3))), a3, result);
    goto loc_00B824B9;
loc_00B824F5:
loc_00B82503:
    if ((v_rip + 3590724) >= (v_rip + 3590749)) goto loc_00B82289;
    if (v_stack_p18 == (*(unsigned __int64 *)(v_rip + 3590724))) goto loc_00B824B9;
    result = (v_rip + 3590724) + (8);
    goto loc_00B82503;
loc_00B82517:
    result = ExAcquireSpinLockShared(v_rip + 3639258, v_rip + 3590749, a3, result);
    a1 = (0) >> (12);
    a2 = (v_rip + 3590749) * (a1);
    a3 = (a2) >> (32);
    a3 = (unsigned int)((a3) ^ ((unsigned int)(a2)));
    a3 = (unsigned int)((a3) & ((unsigned int)(*(unsigned __int64 *)(v_rip + 3655694) - 1)));
loc_00B82559:
    a1 = ((unsigned int)(a3)) << (5);
    a1 = (a1) + (*(unsigned __int64 *)(v_rip + 3655676));
    if ((*(unsigned __int64 *)(a1)) == 0) goto loc_00B82598;
    a3 = (unsigned int)((a3) + 1);
    if (((unsigned int)(a3)) < (*(unsigned __int64 *)(v_rip + 3655694))) goto loc_00B82559;
    if (1 != 0) goto loc_00B82833;
loc_00B8257F:
    v_stack_p20 = 0;
    result = KeBugCheckEx(34 - 9, 34, 0, (unsigned int)((unsigned int)(v_rdi)));
loc_00B82598:
    if (34 - 9 == 0) goto loc_00B8257F;
    if (((*(unsigned int *)(34 - 9 + 12)) & (256)) != 0) {
        v_r12 = *(unsigned __int64 *)(34 - 9 + 16);
        result = 0;
        result = (result) ^ (*(unsigned __int64 *)(v_rip + 4476020));
        *(unsigned __int64 *)(34 - 9 + 24) = result;
    }
    if (((*(unsigned __int8 *)(v_rip + 4474183)) & (1)) != 0) goto loc_00B827B5;
loc_00B825C5:
loc_00B825D7:
    if ((*(unsigned int *)(v_rip + 4474690)) != 0) {
        a1 = v_cr8;
        a2 = (unsigned __int8)((unsigned __int8)(result));
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, 0, (unsigned int)((unsigned int)(v_rdi)));
    }
    goto loc_00B822D8;
loc_00B825F6:
    a2 = (0) - (*(unsigned __int64 *)(v_rip + 3039233));
    a2 = (a2) >> (20);
    a2 = (a2) + (a2);
    result = RtlCSparseBitmapBitmaskRead(v_rip + 3039248, a2, 0, (unsigned int)((unsigned int)(v_rdi)));
    if (result == 0) goto loc_00B82623;
    result = (unsigned int)((result) - 1);
    if (((unsigned int)(result)) != 2) goto loc_00B823C8;
loc_00B82623:
    v_stack_p58 = v_xmm0;
    v_stack_p68 = v_xmm0;
    result = RtlpHpVaMgrCtxQuery(v_rip + 3039267, 0, v_stack_p58, (unsigned int)((unsigned int)(v_rdi)));
    goto loc_00B82401;
loc_00B82651:
    result = ExAcquireSpinLockShared(v_rip + 3638944, 0, v_stack_p58, (unsigned int)((unsigned int)(v_rdi)));
    a1 = (0) >> (12);
    a2 = (0) * (a1);
    a3 = (a2) >> (32);
    a3 = (unsigned int)((a3) ^ ((unsigned int)(a2)));
    a3 = (unsigned int)((a3) & ((unsigned int)(*(unsigned __int64 *)(v_rip + 3655380) - 1)));
loc_00B82693:
    a2 = ((unsigned int)(a3)) << (5);
    a2 = (a2) + (*(unsigned __int64 *)(v_rip + 3655362));
    if ((*(unsigned __int64 *)(a2)) == 0) goto loc_00B826C0;
    a3 = (unsigned int)((a3) + 1);
    if (((unsigned int)(a3)) < (*(unsigned __int64 *)(v_rip + 3655380))) goto loc_00B82693;
    if (1 == 0) goto loc_00B8257F;
    goto loc_00B82693;
loc_00B826C0:
    if (a2 == 0) goto loc_00B8257F;
    if (((*(unsigned int *)(a2 + 12)) & (256)) == 0) goto loc_00B82827;
    v_rdi = (*(unsigned __int64 *)(a2 + 24)) ^ (*(unsigned __int64 *)(v_rip + 4475716));
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184)) ^ (*(unsigned __int64 *)(v_rip + 4475709));
    v_rdi = (v_rdi) ^ (0);
    result = (result) ^ (0);
    *(unsigned __int64 *)(a2 + 24) = result;
loc_00B826F5:
    if (((*(unsigned __int8 *)(v_rip + 4473866)) & (1)) != 0) goto loc_00B827DC;
loc_00B82702:
loc_00B82714:
    if ((*(unsigned int *)(v_rip + 4474374)) != ((unsigned int)((unsigned __int8)(result)))) {
        a1 = (unsigned __int8)(result);
        a2 = (unsigned __int8)((unsigned __int8)(result));
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, 0, *(unsigned __int64 *)(v_rip + 3655380));
    }
    goto loc_00B82483;
loc_00B82732:
    if (result != result) goto loc_00B82361;
    goto loc_00B8236A;
loc_00B82749:
    if ((((unsigned __int8)(result)) & (1)) == 0) goto loc_00B82422;
    if ((*(unsigned __int64 *)((unsigned __int8)(result) + 80)) == 0) goto loc_00B82422;
    if (0 != 0) goto loc_00B8279F;
    v_stack_p20 = v_stack_p38;
    result = PspExpandQuota((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rip + 3655362))), (unsigned __int8)(result), (unsigned __int8)(result), v_r12);
    if ((unsigned __int8)(result) == 0) goto loc_00B82422;
    goto loc_00B82335;
loc_00B8279F:
    result = (v_stack_p30) + (v_stack_p30);
    goto loc_00B82330;
loc_00B827B5:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3716765))) != 0) goto loc_00B825C5;
    result = ExpReleaseSpinLockSharedFromDpcLevelInstrumented(v_rip + 3638566, v_stack_pA8, (unsigned __int8)(result), v_r12);
    goto loc_00B825D7;
loc_00B827DC:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3716726))) != 0) goto loc_00B82702;
    result = ExpReleaseSpinLockSharedFromDpcLevelInstrumented(v_rip + 3638527, v_stack_pA8, (unsigned __int8)(result), v_r12);
    goto loc_00B82714;
loc_00B82803:
    if ((unsigned __int8)(result) != 0) {
        v_r14 = *(unsigned int *)((unsigned __int8)(result) + 4);
    }
    v_stack_p20 = v_rdi;
    result = KeBugCheckEx(194, 13, 0, (unsigned int)((unsigned int)(v_r14)));
loc_00B82827:
    goto loc_00B826F5;
loc_00B82833:
    goto loc_00B82559;
}
```

## 5. (Beta) C Style

```c
int64_t ExpAllocatePoolWithQuotaTag(int64_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint32_t v_stack_m64;
    uint32_t v_stack_m68;
    uint64_t v_stack_m70;
    uint8_t v_stack_m78;
    uint64_t v_stack_m88;
    uint32_t v_stack_mA8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint8_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p48;
    uint64_t v_stack_p58;
    uint64_t v_stack_p68;
    uint64_t v_stack_p8;
    uint64_t v_stack_pA8;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (128);
    local_r14 = 0;
    local_rdi = Arg1;
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8)) == (*(uint64_t *)(v_rip + 0x444869))) {
        local_rdi = (Arg1) & (-2);
    }
    v_stack_p8 = local_rsi;
    v_stack_p10 = local_r15;
    result = ExpAllocatePoolWithTagFromNode(local_rdi, Arg2, Arg3, a4);
    if (result == 0) goto loc_00B824B9;
    if ((((uint8_t)(local_rdi)) & (1)) == 0) goto loc_00B824B9;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x37CA9F))) != 0) goto loc_00B823BC;
loc_00B82289:
    result = (uint32_t)((result) & (0xFFFULL));
    v_stack_m58 = result;
    if (condition_is_equal) goto loc_00B82517;
    if (((*(uint8_t *)(result - 0xD)) & (4)) != 0) {
        result = *(uint16_t *)(result - 0x10);
        Arg1 = (uint8_t)(result);
        Arg1 = -(Arg1);
        Arg1 = (Arg1) << (4);
        Arg2 = (result - 16) + (Arg1);
    }
    local_r12 = ((uint8_t)(*(uint16_t *)(Arg2 + 0x2))) << (4);
    result = (uint16_t)((*(uint16_t *)(Arg2 + 0x2)) >> (8));
    if ((((uint8_t)(result)) & (8)) != 0) {
        result = Arg2 + 8;
        Arg2 = (Arg2) ^ (*(uint64_t *)(v_rip + 0x444F53));
        *(uint64_t *)(result) = Arg2;
    }
    Arg1 = (uint32_t)((local_rdi) & (256));
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8)) == (*(uint64_t *)(v_rip + 0x4447C8))) goto loc_00B82436;
    result = (Arg1 != 0) ? 1 : 0;
    local_r15 = ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))))) << (7);
    v_stack_m60 = (uint32_t)((uint32_t)(result));
    local_r15 = (local_r15) + (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x2F8));
    v_stack_m78 = (uint8_t)(*(uint8_t *)(v_rip + 0x445055 + (uint32_t)((uint32_t)(result)) * 8));
loc_00B8232C:
loc_00B82330:
    v_stack_m70 = *(uint64_t *)(local_r15 + 0x40);
loc_00B82335:
    if ((*(uint64_t *)(local_r15) + local_r12 * 1) < (*(uint64_t *)(local_r15))) goto loc_00B82422;
    if ((*(uint64_t *)(local_r15) + local_r12 * 1) > (*(uint64_t *)(local_r15 + 0x40))) goto loc_00B82749;
    if ((*(uint64_t *)(local_r15) + local_r12 * 1) != (*(uint64_t *)(local_r15 + 0x40))) goto loc_00B8232C;
loc_00B82361:
    if ((*(uint64_t *)(local_r15) + local_r12 * 1) > (*(uint64_t *)(local_r15 + 0x8))) goto loc_00B82732;
loc_00B8236A:
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) == 0) goto loc_00B82436;
    if (((v_stack_m78) & (4)) == 0) goto loc_00B82436;
    Arg2 = (local_r12) + (local_r12);
loc_00B8239F:
    if (Arg2 <= (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + (uint32_t)((uint32_t)(result)) * 8 + 0x210))) goto loc_00B82436;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + (uint32_t)((uint32_t)(result)) * 8 + 0x210)) != (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + (uint32_t)((uint32_t)(result)) * 8 + 0x210))) goto loc_00B8239F;
    goto loc_00B82436;
loc_00B823BC:
    if ((uint16_t)(result) == 0) goto loc_00B825F6;
loc_00B823C8:
    v_stack_m68 = 0x100000ULL;
    v_stack_m64 = 0x1000000ULL;
    Arg1 = -((uint32_t)(*(uint32_t *)(local_rsp + 0x0 * 4 + 0x40)));
    result = (0 + 0 * 2) << (6);
    Arg1 = (Arg1) & (result);
    Arg1 = (Arg1) ^ (*(uint64_t *)(Arg1 + 0x10));
    Arg1 = (Arg1) ^ (*(uint64_t *)(v_rip + 0x2A5F09));
    Arg1 = (Arg1) - (result);
    Arg1 = (Arg1) - (320);
loc_00B82401:
    if (Arg1 != 0) goto loc_00B824F5;
    v_stack_m88 = 0;
    Arg3 = 0;
    Arg2 = 0;
    result = KeBugCheckEx(194, Arg2, Arg3, result);
loc_00B82422:
    if (sign_flag) goto loc_00B824E5;
loc_00B82436:
    if (v_stack_m58 == 0) goto loc_00B82651;
    result = (uint32_t)(*(uint32_t *)(v_rip + 0x444F27 + (uint32_t)((uint32_t)(result)) * 8 + 0x4));
    local_rsi = result - 16;
    if (((*(uint8_t *)(result - 0xD)) & (4)) != 0) {
        result = *(uint16_t *)(result - 0x10);
        Arg1 = (uint8_t)(result);
        Arg1 = -(Arg1);
        Arg1 = (Arg1) << (4);
        local_rsi = (result - 16) + (Arg1);
    }
    if (((*(uint8_t *)(local_rsi + 0x3)) & (8)) == 0) goto loc_00B824AE;
    local_rdi = (local_rsi) ^ (*(uint64_t *)(local_rsi + 0x8));
    local_rdi = (local_rdi) ^ (*(uint64_t *)(v_rip + 0x444DB3));
    Arg1 = (local_rsi) ^ (*(uint64_t *)(v_rip + 0x444DAC));
    Arg1 = (Arg1) ^ (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8));
    *(uint64_t *)(local_rsi + 0x8) = Arg1;
loc_00B82483:
    if (local_rdi == 0) goto loc_00B824AE;
    if (local_rdi == -1) goto loc_00B824AE;
    if (local_rdi < result) goto loc_00B82803;
    result = (uint8_t)((*(uint8_t *)(local_rdi)) & (127));
    if (((uint8_t)(result)) != 3) goto loc_00B82803;
loc_00B824AE:
    result = ObfReferenceObjectWithTag(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg3, result);
loc_00B824B9:
    local_rsp = (local_rsp) + (128);
    return result;
loc_00B824E5:
    result = ExFreePoolWithTag(v_stack_p18, (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg3, result);
    goto loc_00B824B9;
loc_00B824F5:
loc_00B82503:
    if ((v_rip + 3590724) >= (v_rip + 3590749)) goto loc_00B82289;
    if (v_stack_p18 == (*(uint64_t *)(v_rip + 0x36CA44))) goto loc_00B824B9;
    result = (v_rip + 3590724) + (8);
    goto loc_00B82503;
loc_00B82517:
    result = ExAcquireSpinLockShared(v_rip + 3639258, v_rip + 3590749, Arg3, result);
    Arg1 = (0) >> (12);
    Arg2 = (v_rip + 3590749) * (Arg1);
    Arg3 = (Arg2) >> (32);
    Arg3 = (uint32_t)((Arg3) ^ ((uint32_t)(Arg2)));
    Arg3 = (uint32_t)((Arg3) & ((uint32_t)(*(uint64_t *)(v_rip + 0x37C80E) - 1)));
loc_00B82559:
    Arg1 = ((uint32_t)(Arg3)) << (5);
    Arg1 = (Arg1) + (*(uint64_t *)(v_rip + 0x37C7FC));
    if ((*(uint64_t *)(Arg1)) == 0) goto loc_00B82598;
    Arg3 = (uint32_t)((Arg3) + 1);
    if (((uint32_t)(Arg3)) < (*(uint64_t *)(v_rip + 0x37C80E))) goto loc_00B82559;
    if (1 != 0) goto loc_00B82833;
loc_00B8257F:
    v_stack_p20 = 0;
    result = KeBugCheckEx(34 - 9, 34, 0, (uint32_t)((uint32_t)(local_rdi)));
loc_00B82598:
    if (34 - 9 == 0) goto loc_00B8257F;
    if (((*(uint32_t *)(34 - 0x9 + 0xC)) & (256)) != 0) {
        local_r12 = *(uint64_t *)(34 - 0x9 + 0x10);
        result = 0;
        result = (result) ^ (*(uint64_t *)(v_rip + 0x444C74));
        *(uint64_t *)(34 - 0x9 + 0x18) = result;
    }
    if (((*(uint8_t *)(v_rip + 0x444547)) & (1)) != 0) goto loc_00B827B5;
loc_00B825C5:
loc_00B825D7:
    if ((*(uint32_t *)(v_rip + 0x444742)) != 0) {
        Arg1 = v_cr8;
        Arg2 = (uint8_t)((uint8_t)(result));
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, 0, (uint32_t)((uint32_t)(local_rdi)));
    }
    goto loc_00B822D8;
loc_00B825F6:
    Arg2 = (0) - (*(uint64_t *)(v_rip + 0x2E6001));
    Arg2 = (Arg2) >> (20);
    Arg2 = (Arg2) + (Arg2);
    result = RtlCSparseBitmapBitmaskRead(v_rip + 3039248, Arg2, 0, (uint32_t)((uint32_t)(local_rdi)));
    if (result == 0) goto loc_00B82623;
    result = (uint32_t)((result) - 1);
    if (((uint32_t)(result)) != 2) goto loc_00B823C8;
loc_00B82623:
    v_stack_p58 = v_xmm0;
    v_stack_p68 = v_xmm0;
    result = RtlpHpVaMgrCtxQuery(v_rip + 3039267, 0, v_stack_p58, (uint32_t)((uint32_t)(local_rdi)));
    goto loc_00B82401;
loc_00B82651:
    result = ExAcquireSpinLockShared(v_rip + 3638944, 0, v_stack_p58, (uint32_t)((uint32_t)(local_rdi)));
    Arg1 = (0) >> (12);
    Arg2 = (0) * (Arg1);
    Arg3 = (Arg2) >> (32);
    Arg3 = (uint32_t)((Arg3) ^ ((uint32_t)(Arg2)));
    Arg3 = (uint32_t)((Arg3) & ((uint32_t)(*(uint64_t *)(v_rip + 0x37C6D4) - 1)));
loc_00B82693:
    Arg2 = ((uint32_t)(Arg3)) << (5);
    Arg2 = (Arg2) + (*(uint64_t *)(v_rip + 0x37C6C2));
    if ((*(uint64_t *)(Arg2)) == 0) goto loc_00B826C0;
    Arg3 = (uint32_t)((Arg3) + 1);
    if (((uint32_t)(Arg3)) < (*(uint64_t *)(v_rip + 0x37C6D4))) goto loc_00B82693;
    if (1 == 0) goto loc_00B8257F;
    goto loc_00B82693;
loc_00B826C0:
    if (Arg2 == 0) goto loc_00B8257F;
    if (((*(uint32_t *)(Arg2 + 0xC)) & (256)) == 0) goto loc_00B82827;
    local_rdi = (*(uint64_t *)(Arg2 + 0x18)) ^ (*(uint64_t *)(v_rip + 0x444B44));
    result = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8)) ^ (*(uint64_t *)(v_rip + 0x444B3D));
    local_rdi = (local_rdi) ^ (0);
    result = (result) ^ (0);
    *(uint64_t *)(Arg2 + 0x18) = result;
loc_00B826F5:
    if (((*(uint8_t *)(v_rip + 0x44440A)) & (1)) != 0) goto loc_00B827DC;
loc_00B82702:
loc_00B82714:
    if ((*(uint32_t *)(v_rip + 0x444606)) != ((uint32_t)((uint8_t)(result)))) {
        Arg1 = (uint8_t)(result);
        Arg2 = (uint8_t)((uint8_t)(result));
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, 0, *(uint64_t *)(v_rip + 0x37C6D4));
    }
    goto loc_00B82483;
loc_00B82732:
    if (result != result) goto loc_00B82361;
    goto loc_00B8236A;
loc_00B82749:
    if ((((uint8_t)(result)) & (1)) == 0) goto loc_00B82422;
    if ((*(uint64_t *)((uint8_t)(result) + 0x50)) == 0) goto loc_00B82422;
    if (0 != 0) goto loc_00B8279F;
    v_stack_p20 = v_stack_p38;
    result = PspExpandQuota((uint32_t)((uint32_t)(*(uint64_t *)(v_rip + 0x37C6C2))), (uint8_t)(result), (uint8_t)(result), local_r12);
    if ((uint8_t)(result) == 0) goto loc_00B82422;
    goto loc_00B82335;
loc_00B8279F:
    result = (v_stack_p30) + (v_stack_p30);
    goto loc_00B82330;
loc_00B827B5:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x38B69D))) != 0) goto loc_00B825C5;
    result = ExpReleaseSpinLockSharedFromDpcLevelInstrumented(v_rip + 3638566, v_stack_pA8, (uint8_t)(result), local_r12);
    goto loc_00B825D7;
loc_00B827DC:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x38B676))) != 0) goto loc_00B82702;
    result = ExpReleaseSpinLockSharedFromDpcLevelInstrumented(v_rip + 3638527, v_stack_pA8, (uint8_t)(result), local_r12);
    goto loc_00B82714;
loc_00B82803:
    if ((uint8_t)(result) != 0) {
        local_r14 = *(uint32_t *)((uint8_t)(result) + 0x4);
    }
    v_stack_p20 = local_rdi;
    result = KeBugCheckEx(194, 13, 0, (uint32_t)((uint32_t)(local_r14)));
loc_00B82827:
    goto loc_00B826F5;
loc_00B82833:
    goto loc_00B82559;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=poolcode&rva=0x00B82210&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
