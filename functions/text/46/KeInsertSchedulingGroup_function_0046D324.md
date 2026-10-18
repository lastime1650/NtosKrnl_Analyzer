# KeInsertSchedulingGroup

- RVA: `0x0046D324`–`0x0046D704` (길이 `992` bytes)
- VA: `0x000000014046D324`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000ABA48`
- 디코드: `251`개 명령, `992/992` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **11**; 고유 호출 대상: **11**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **16**

### Outgoing calls
- `0x0046D376` → [KeQueryPerformanceCounter](../37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x0046D3C3` → [KiInitializeScb](KiInitializeScb_function_0046D70C.md) (function, `0x0046D70C`)
- `0x0046D3DE` → [KeAcquireInStackQueuedSpinLock](../27/KeAcquireInStackQueuedSpinLock_function_002757A0.md) (function, `0x002757A0`)
- `0x0046D5AB` → [KiUpdateCpuTargetByRate](KiUpdateCpuTargetByRate_function_0046D7E4.md) (function, `0x0046D7E4`)
- `0x0046D5B5` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x0046D5FE` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0046D60E` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0046D697` → [KiUpdateCpuTargetByWeight](KiUpdateCpuTargetByWeight_function_0046E0E0.md) (function, `0x0046E0E0`)
- `0x0046D69E` → [KiEnableGroupScheduling](../5C/KiEnableGroupScheduling_function_005C8914.md) (function, `0x005C8914`)
- `0x0046D6D8` → [KiAssignSchedulingGroupWeights](KiAssignSchedulingGroupWeights_function_0046D260.md) (function, `0x0046D260`)
- `0x0046D6FA` → [EtwTraceSchedulingGroup](../65/EtwTraceSchedulingGroup_function_00650108.md) (function, `0x00650108`)

### Direct callers
- [PspEstablishDfssHierarchy](../../page/78/PspEstablishDfssHierarchy_function_00784EF0.md) at `0x00784FC1`
- [PspSessionObjectCreate](../../page/78/PspSessionObjectCreate_function_007892A8.md) at `0x00789531`
- [PspEstablishJobHierarchy](../../page/87/PspEstablishJobHierarchy_function_0087E17C.md) at `0x0087E56F`
- [PspEstablishJobHierarchy](../../page/87/PspEstablishJobHierarchy_function_0087E17C.md) at `0x0087E5B6`
- [PspAddSchedulingGroupToJobChain](../../page/99/PspAddSchedulingGroupToJobChain_function_0099DE5C.md) at `0x0099DFEC`

### Static image references
- `0x0046D342` → RVA `0x00FC6ABC` (`ALMOSTRO`; read)
- `0x0046D3A4` → RVA `0x00FC6AE8` (`ALMOSTRO`; read)
- `0x0046D3D7` → RVA `0x00FCF180` (`CACHEALI`; read)
- `0x0046D3E3` → RVA `0x00F23420` (`.data`; read)
- `0x0046D3F3` → RVA `0x00F23428` (`.data`; read)
- `0x0046D40D` → RVA `0x00F23428` (`.data`; write)
- `0x0046D414` → RVA `0x00FC6A80` (`ALMOSTRO`; read)
- `0x0046D43A` → RVA `0x00FC8C40` (`ALMOSTRO`; read)
- `0x0046D45C` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x0046D507` → RVA `0x00F23438` (`.data`; read)
- `0x0046D520` → RVA `0x00F23438` (`.data`; write)
- `0x0046D5BA` → RVA `0x00FC6B14` (`ALMOSTRO`; read)
- `0x0046D5F0` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x0046D649` → RVA `0x00F23434` (`.data`; read)
- `0x0046D65D` → RVA `0x00F2343C` (`.data`; read/write)
- `0x0046D6C2` → RVA `0x00F23434` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0046D324  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
0046D329  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
0046D32E  55                              push rbp
0046D32F  56                              push rsi
0046D330  57                              push rdi
0046D331  41 54                           push r12
0046D333  41 55                           push r13
0046D335  41 56                           push r14
0046D337  41 57                           push r15
0046D339  48 83 EC 40                     sub rsp, 0x40
0046D33D  33 C0                           xor eax, eax
0046D33F  45 33 ED                        xor r13d, r13d
0046D342  44 38 2D 73 97 B5 00            cmp byte ptr [rip + 0xb59773], r13b
0046D349  0F 57 C0                        xorps xmm0, xmm0
0046D34C  49 8B F8                        mov rdi, r8
0046D34F  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0046D354  48 8B DA                        mov rbx, rdx
0046D357  4C 8B F1                        mov r14, rcx
0046D35A  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
0046D35F  0F 84 39 03 00 00               je 0x14046d69e
0046D365  33 C9                           xor ecx, ecx
0046D367  49 89 1E                        mov qword ptr [r14], rbx
0046D36A  4D 89 6E 20                     mov qword ptr [r14 + 0x20], r13
0046D36E  4D 89 6E 0C                     mov qword ptr [r14 + 0xc], r13
0046D372  45 89 6E 14                     mov dword ptr [r14 + 0x14], r13d
0046D376  E8 65 14 F1 FF                  call 0x14037e7e0
0046D37B  49 89 46 18                     mov qword ptr [r14 + 0x18], rax
0046D37F  49 8D 76 38                     lea rsi, [r14 + 0x38]
0046D383  49 8D 46 50                     lea rax, [r14 + 0x50]
0046D387  41 8B ED                        mov ebp, r13d
0046D38A  48 89 40 08                     mov qword ptr [rax + 8], rax
0046D38E  48 89 00                        mov qword ptr [rax], rax
0046D391  48 89 76 08                     mov qword ptr [rsi + 8], rsi
0046D395  48 89 36                        mov qword ptr [rsi], rsi
0046D398  4D 89 6E 60                     mov qword ptr [r14 + 0x60], r13
0046D39C  4D 89 6E 28                     mov qword ptr [r14 + 0x28], r13
0046D3A0  4D 89 6E 30                     mov qword ptr [r14 + 0x30], r13
0046D3A4  44 39 2D 3D 97 B5 00            cmp dword ptr [rip + 0xb5973d], r13d
0046D3AB  76 25                           jbe 0x14046d3d2
0046D3AD  8B C5                           mov eax, ebp
0046D3AF  44 8B CD                        mov r9d, ebp
0046D3B2  48 69 C8 B8 01 00 00            imul rcx, rax, 0x1b8
0046D3B9  4C 8B C7                        mov r8, rdi
0046D3BC  48 83 E9 80                     sub rcx, -0x80
0046D3C0  49 03 CE                        add rcx, r14
0046D3C3  E8 44 03 00 00                  call 0x14046d70c
0046D3C8  FF C5                           inc ebp
0046D3CA  3B 2D 18 97 B5 00               cmp ebp, dword ptr [rip + 0xb59718]
0046D3D0  72 DB                           jb 0x14046d3ad
0046D3D2  48 8D 54 24 20                  lea rdx, [rsp + 0x20]
0046D3D7  48 8D 0D A2 1D B6 00            lea rcx, [rip + 0xb61da2]
0046D3DE  E8 BD 83 E0 FF                  call 0x1402757a0
0046D3E3  4C 8D 3D 36 60 AB 00            lea r15, [rip + 0xab6036]
0046D3EA  48 85 FF                        test rdi, rdi
0046D3ED  0F 85 A1 00 00 00               jne 0x14046d494
0046D3F3  48 8B 05 2E 60 AB 00            mov rax, qword ptr [rip + 0xab602e]
0046D3FA  4C 39 38                        cmp qword ptr [rax], r15
0046D3FD  0F 85 8A 00 00 00               jne 0x14046d48d
0046D403  4C 89 3E                        mov qword ptr [rsi], r15
0046D406  48 89 46 08                     mov qword ptr [rsi + 8], rax
0046D40A  48 89 30                        mov qword ptr [rax], rsi
0046D40D  48 89 35 14 60 AB 00            mov qword ptr [rip + 0xab6014], rsi
0046D414  44 8B 05 65 96 B5 00            mov r8d, dword ptr [rip + 0xb59665]
0046D41B  45 8B E5                        mov r12d, r13d
0046D41E  44 89 84 24 80 00 00 00         mov dword ptr [rsp + 0x80], r8d
0046D426  4C 89 AC 24 90 00 00 00         mov qword ptr [rsp + 0x90], r13
0046D42E  45 85 C0                        test r8d, r8d
0046D431  0F 84 BF 00 00 00               je 0x14046d4f6
0046D437  41 8B C4                        mov eax, r12d
0046D43A  48 8D 2D FF B7 B5 00            lea rbp, [rip + 0xb5b7ff]
0046D441  48 69 F0 B8 01 00 00            imul rsi, rax, 0x1b8
0046D448  48 8B 6C C5 00                  mov rbp, qword ptr [rbp + rax*8]
0046D44D  49 03 F6                        add rsi, r14
0046D450  F0 48 0F BA 6D 30 00            lock bts qword ptr [rbp + 0x30], 0
0046D457  73 1D                           jae 0x14046d476
0046D459  41 FF C5                        inc r13d
0046D45C  44 85 2D 49 7E B5 00            test dword ptr [rip + 0xb57e49], r13d
0046D463  0F 84 87 01 00 00               je 0x14046d5f0
0046D469  F3 90                           pause
0046D46B  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
0046D46F  48 85 C0                        test rax, rax
0046D472  74 DC                           je 0x14046d450
0046D474  EB E3                           jmp 0x14046d459
0046D476  48 8D 8D 88 8A 00 00            lea rcx, [rbp + 0x8a88]
0046D47D  48 8B 51 08                     mov rdx, qword ptr [rcx + 8]
0046D481  48 8D 86 C8 00 00 00            lea rax, [rsi + 0xc8]
0046D488  48 39 0A                        cmp qword ptr [rdx], rcx
0046D48B  74 2B                           je 0x14046d4b8
0046D48D  B9 03 00 00 00                  mov ecx, 3
0046D492  CD 29                           int 0x29
0046D494  48 8D 47 50                     lea rax, [rdi + 0x50]
0046D498  49 89 7E 60                     mov qword ptr [r14 + 0x60], rdi
0046D49C  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
0046D4A0  48 39 01                        cmp qword ptr [rcx], rax
0046D4A3  75 E8                           jne 0x14046d48d
0046D4A5  48 89 06                        mov qword ptr [rsi], rax
0046D4A8  48 89 4E 08                     mov qword ptr [rsi + 8], rcx
0046D4AC  48 89 31                        mov qword ptr [rcx], rsi
0046D4AF  48 89 70 08                     mov qword ptr [rax + 8], rsi
0046D4B3  E9 5C FF FF FF                  jmp 0x14046d414
0046D4B8  F6 84 24 8C 00 00 00 04         test byte ptr [rsp + 0x8c], 4
0046D4C0  48 89 08                        mov qword ptr [rax], rcx
0046D4C3  48 89 50 08                     mov qword ptr [rax + 8], rdx
0046D4C7  48 89 02                        mov qword ptr [rdx], rax
0046D4CA  48 89 41 08                     mov qword ptr [rcx + 8], rax
0046D4CE  0F 85 D4 01 00 00               jne 0x14046d6a8
0046D4D4  45 33 ED                        xor r13d, r13d
0046D4D7  F0 4C 21 6D 30                  lock and qword ptr [rbp + 0x30], r13
0046D4DC  4C 39 AD 40 8E 00 00            cmp qword ptr [rbp + 0x8e40], r13
0046D4E3  75 53                           jne 0x14046d538
0046D4E5  41 FF C4                        inc r12d
0046D4E8  44 3B A4 24 80 00 00 00         cmp r12d, dword ptr [rsp + 0x80]
0046D4F0  0F 82 41 FF FF FF               jb 0x14046d437
0046D4F6  41 8B 46 04                     mov eax, dword ptr [r14 + 4]
0046D4FA  A8 01                           test al, 1
0046D4FC  0F 84 16 01 00 00               je 0x14046d618
0046D502  48 85 FF                        test rdi, rdi
0046D505  75 7E                           jne 0x14046d585
0046D507  8B 0D 2B 5F AB 00               mov ecx, dword ptr [rip + 0xab5f2b]
0046D50D  85 C9                           test ecx, ecx
0046D50F  0F 85 CD 01 00 00               jne 0x14046d6e2
0046D515  48 8B 0D 04 5F AB 00            mov rcx, qword ptr [rip + 0xab5f04]
0046D51C  44 0F B7 C3                     movzx r8d, bx
0046D520  44 89 05 11 5F AB 00            mov dword ptr [rip + 0xab5f11], r8d
0046D527  8B 41 CC                        mov eax, dword ptr [rcx - 0x34]
0046D52A  A8 01                           test al, 1
0046D52C  75 46                           jne 0x14046d574
0046D52E  48 8B 09                        mov rcx, qword ptr [rcx]
0046D531  49 3B CF                        cmp rcx, r15
0046D534  75 F1                           jne 0x14046d527
0046D536  EB 6E                           jmp 0x14046d5a6
0046D538  48 8B 85 48 8E 00 00            mov rax, qword ptr [rbp + 0x8e48]
0046D53F  8A 88 C1 02 00 00               mov cl, byte ptr [rax + 0x2c1]
0046D545  38 8D D1 00 00 00               cmp byte ptr [rbp + 0xd1], cl
0046D54B  0F 85 92 00 00 00               jne 0x14046d5e3
0046D551  66 83 8E F0 00 00 00 40         or word ptr [rsi + 0xf0], 0x40
0046D559  48 8D 8E 08 01 00 00            lea rcx, [rsi + 0x108]
0046D560  48 89 8C 24 90 00 00 00         mov qword ptr [rsp + 0x90], rcx
0046D568  48 89 8E 00 01 00 00            mov qword ptr [rsi + 0x100], rcx
0046D56F  E9 71 FF FF FF                  jmp 0x14046d4e5
0046D574  0F B7 41 C8                     movzx eax, word ptr [rcx - 0x38]
0046D578  33 D2                           xor edx, edx
0046D57A  C1 E0 07                        shl eax, 7
0046D57D  41 F7 F0                        div r8d
0046D580  89 41 D0                        mov dword ptr [rcx - 0x30], eax
0046D583  EB A9                           jmp 0x14046d52e
0046D585  8B 4F 0C                        mov ecx, dword ptr [rdi + 0xc]
0046D588  85 C9                           test ecx, ecx
0046D58A  0F 84 3A 01 00 00               je 0x14046d6ca
0046D590  0F B7 C3                        movzx eax, bx
0046D593  3B C1                           cmp eax, ecx
0046D595  0F 82 2F 01 00 00               jb 0x14046d6ca
0046D59B  C1 E0 07                        shl eax, 7
0046D59E  33 D2                           xor edx, edx
0046D5A0  F7 F1                           div ecx
0046D5A2  41 89 46 08                     mov dword ptr [r14 + 8], eax
0046D5A6  33 D2                           xor edx, edx
0046D5A8  49 8B CE                        mov rcx, r14
0046D5AB  E8 34 02 00 00                  call 0x14046d7e4
0046D5B0  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0046D5B5  E8 26 57 ED FF                  call 0x140342ce0
0046D5BA  F7 05 50 95 B5 00 00 40 00 00   test dword ptr [rip + 0xb59550], 0x4000
0046D5C4  0F 85 28 01 00 00               jne 0x14046d6f2
0046D5CA  48 8B 9C 24 98 00 00 00         mov rbx, qword ptr [rsp + 0x98]
0046D5D2  48 83 C4 40                     add rsp, 0x40
0046D5D6  41 5F                           pop r15
0046D5D8  41 5E                           pop r14
0046D5DA  41 5D                           pop r13
0046D5DC  41 5C                           pop r12
0046D5DE  5F                              pop rdi
0046D5DF  5E                              pop rsi
0046D5E0  5D                              pop rbp
0046D5E1  C3                              ret
0046D5E2  CC                              int3
0046D5E3  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
0046D5EB  E9 78 FF FF FF                  jmp 0x14046d568
0046D5F0  8B 05 C2 94 B5 00               mov eax, dword ptr [rip + 0xb594c2]
0046D5F6  A8 40                           test al, 0x40
0046D5F8  0F 84 6B FE FF FF               je 0x14046d469
0046D5FE  E8 8D 1E EA FF                  call 0x14030f490
0046D603  84 C0                           test al, al
0046D605  0F 84 5E FE FF FF               je 0x14046d469
0046D60B  41 8B CD                        mov ecx, r13d
0046D60E  E8 4D 1E EA FF                  call 0x14030f460
0046D613  E9 53 FE FF FF                  jmp 0x14046d46b
0046D618  48 85 FF                        test rdi, rdi
0046D61B  74 2C                           je 0x14046d649
0046D61D  8B 4F 10                        mov ecx, dword ptr [rdi + 0x10]
0046D620  85 C9                           test ecx, ecx
0046D622  74 07                           je 0x14046d62b
0046D624  0F B7 C3                        movzx eax, bx
0046D627  3B C1                           cmp eax, ecx
0046D629  73 06                           jae 0x14046d631
0046D62B  0F B7 C3                        movzx eax, bx
0046D62E  89 47 10                        mov dword ptr [rdi + 0x10], eax
0046D631  0F B7 C3                        movzx eax, bx
0046D634  01 47 14                        add dword ptr [rdi + 0x14], eax
0046D637  0F 84 73 FF FF FF               je 0x14046d5b0
0046D63D  8B 77 10                        mov esi, dword ptr [rdi + 0x10]
0046D640  4C 8D 7F 50                     lea r15, [rdi + 0x50]
0046D644  49 8B 1F                        mov rbx, qword ptr [r15]
0046D647  EB 27                           jmp 0x14046d670
0046D649  8B 35 E5 5D AB 00               mov esi, dword ptr [rip + 0xab5de5]
0046D64F  85 F6                           test esi, esi
0046D651  74 6C                           je 0x14046d6bf
0046D653  0F B7 C3                        movzx eax, bx
0046D656  3B C6                           cmp eax, esi
0046D658  72 65                           jb 0x14046d6bf
0046D65A  0F B7 C3                        movzx eax, bx
0046D65D  01 05 D9 5D AB 00               add dword ptr [rip + 0xab5dd9], eax
0046D663  0F 84 47 FF FF FF               je 0x14046d5b0
0046D669  48 8B 1D B0 5D AB 00            mov rbx, qword ptr [rip + 0xab5db0]
0046D670  48 8D 4B C8                     lea rcx, [rbx - 0x38]
0046D674  8B 41 04                        mov eax, dword ptr [rcx + 4]
0046D677  A8 01                           test al, 1
0046D679  74 0D                           je 0x14046d688
0046D67B  48 8B 1B                        mov rbx, qword ptr [rbx]
0046D67E  49 3B DF                        cmp rbx, r15
0046D681  75 ED                           jne 0x14046d670
0046D683  E9 28 FF FF FF                  jmp 0x14046d5b0
0046D688  0F B7 01                        movzx eax, word ptr [rcx]
0046D68B  33 D2                           xor edx, edx
0046D68D  C1 E0 07                        shl eax, 7
0046D690  F7 F6                           div esi
0046D692  33 D2                           xor edx, edx
0046D694  89 41 08                        mov dword ptr [rcx + 8], eax
0046D697  E8 44 0A 00 00                  call 0x14046e0e0
0046D69C  EB DD                           jmp 0x14046d67b
0046D69E  E8 71 B2 15 00                  call 0x1405c8914
0046D6A3  E9 BD FC FF FF                  jmp 0x14046d365
0046D6A8  66 83 8E F0 00 00 00 0C         or word ptr [rsi + 0xf0], 0xc
0046D6B0  C7 86 FC 00 00 00 01 00 00 00   mov dword ptr [rsi + 0xfc], 1
0046D6BA  E9 15 FE FF FF                  jmp 0x14046d4d4
0046D6BF  0F B7 F3                        movzx esi, bx
0046D6C2  89 35 6C 5D AB 00               mov dword ptr [rip + 0xab5d6c], esi
0046D6C8  EB 90                           jmp 0x14046d65a
0046D6CA  33 D2                           xor edx, edx
0046D6CC  0F B7 C3                        movzx eax, bx
0046D6CF  4C 8B C7                        mov r8, rdi
0046D6D2  89 47 0C                        mov dword ptr [rdi + 0xc], eax
0046D6D5  8D 4A 01                        lea ecx, [rdx + 1]
0046D6D8  E8 83 FB FF FF                  call 0x14046d260
0046D6DD  E9 C4 FE FF FF                  jmp 0x14046d5a6
0046D6E2  0F B7 C3                        movzx eax, bx
0046D6E5  3B C1                           cmp eax, ecx
0046D6E7  0F 82 28 FE FF FF               jb 0x14046d515
0046D6ED  E9 A9 FE FF FF                  jmp 0x14046d59b
0046D6F2  BA 62 05 00 00                  mov edx, 0x562
0046D6F7  49 8B CE                        mov rcx, r14
0046D6FA  E8 09 2A 1E 00                  call 0x140650108
0046D6FF  E9 C6 FE FF FF                  jmp 0x14046d5ca
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KeInsertSchedulingGroup(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_rbp;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_p10;
    unsigned __int8 v_stack_p14;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p8;
    unsigned __int64 v_stack_p90;

    v_stack_p20 = v_rbx;
    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (64);
    result = 0;
    v_r13 = 0;
    v_stack_m48 = 0;
    v_stack_m58 = v_xmm0;
    if ((*(unsigned __int8 *)(v_rip + 11900787)) == 0) goto loc_0046D69E;
loc_0046D365:
    a1 = 0;
    *(unsigned __int64 *)(a1) = a2;
    *(unsigned __int64 *)(a1 + 32) = 0;
    *(unsigned __int64 *)(a1 + 12) = 0;
    *(unsigned int *)(a1 + 20) = 0;
    result = KeQueryPerformanceCounter(a1, a2, a3, a4);
    *(unsigned __int64 *)(a1 + 24) = result;
    *(unsigned __int64 *)(a1 + 80 + 8) = a1 + 80;
    *(unsigned __int64 *)(a1 + 80) = a1 + 80;
    *(unsigned __int64 *)(a1 + 56 + 8) = a1 + 56;
    *(unsigned __int64 *)(a1 + 56) = a1 + 56;
    *(unsigned __int64 *)(a1 + 96) = 0;
    *(unsigned __int64 *)(a1 + 40) = 0;
    *(unsigned __int64 *)(a1 + 48) = 0;
    if ((*(unsigned int *)(v_rip + 11900733)) <= 0) goto loc_0046D3D2;
loc_0046D3AD:
    a1 = (a1) * (0);
    a1 = (a1) - (-128);
    a1 = (a1) + (a1);
    result = KiInitializeScb(a1, a2, a3, 0);
    v_rbp = (unsigned int)((0) + 1);
    if (((unsigned int)(v_rbp)) < (*(unsigned int *)(v_rip + 11900696))) goto loc_0046D3AD;
loc_0046D3D2:
    result = KeAcquireInStackQueuedSpinLock(v_rip + 11935138, v_stack_m58, a3, 0);
    if (a3 != 0) goto loc_0046D494;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11231278))) != (v_rip + 11231286)) goto loc_0046D48D;
    *(unsigned __int64 *)(a1 + 56) = v_rip + 11231286;
    *(unsigned __int64 *)(a1 + 56 + 8) = *(unsigned __int64 *)(v_rip + 11231278);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11231278)) = a1 + 56;
    *(unsigned __int64 *)(v_rip + 11231252) = a1 + 56;
loc_0046D414:
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11900517)));
    v_stack_p18 = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11900517))) == 0) goto loc_0046D4F6;
loc_0046D437:
    v_rsi = (a1 + 56) * (0);
    v_rsi = (v_rsi) + (a1);
loc_0046D450:
    if (condition_is_above_or_equal) goto loc_0046D476;
loc_0046D459:
    v_r13 = (unsigned int)((v_r13) + 1);
    if (((*(unsigned int *)(v_rip + 11894345)) & ((unsigned int)(v_r13))) == 0) goto loc_0046D5F0;
loc_0046D469:
loc_0046D46B:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11909119 + 0 * 8) + 48) == 0) goto loc_0046D450;
    goto loc_0046D459;
loc_0046D476:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11909119 + 0 * 8) + 35464 + 8))) == (*(unsigned __int64 *)(v_rip + 11909119 + 0 * 8) + 35464)) goto loc_0046D4B8;
loc_0046D48D:
loc_0046D494:
    *(unsigned __int64 *)(a1 + 96) = a3;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 80 + 8))) != (a3 + 80)) goto loc_0046D48D;
    *(unsigned __int64 *)(v_rsi) = a3 + 80;
    *(unsigned __int64 *)(v_rsi + 8) = *(unsigned __int64 *)(a3 + 80 + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 80 + 8)) = v_rsi;
    *(unsigned __int64 *)(a3 + 80 + 8) = v_rsi;
    goto loc_0046D414;
loc_0046D4B8:
    *(unsigned __int64 *)(a3 + 80) = *(unsigned __int64 *)(a3 + 80 + 8);
    *(unsigned __int64 *)(a3 + 80 + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11909119 + 0 * 8) + 35464 + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11909119 + 0 * 8) + 35464 + 8)) = a3 + 80;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 80 + 8) + 8) = a3 + 80;
    if (((v_stack_p14) & (4)) != 0) goto loc_0046D6A8;
loc_0046D4D4:
    v_r13 = 0;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11909119 + 0 * 8) + 36416)) != 0) goto loc_0046D538;
loc_0046D4E5:
    v_r12 = (unsigned int)((0) + 1);
    if (((unsigned int)(v_r12)) < v_stack_p8) goto loc_0046D437;
loc_0046D4F6:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 4)))) & (1)) == 0) goto loc_0046D618;
    if (a3 != 0) goto loc_0046D585;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11231019))) != 0) goto loc_0046D6E2;
loc_0046D515:
    *(unsigned int *)(v_rip + 11230993) = (unsigned int)((unsigned __int16)(a2));
loc_0046D527:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11230980) - 52)))) & (1)) != 0) goto loc_0046D574;
loc_0046D52E:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11230980))) != (v_rip + 11231286)) goto loc_0046D527;
    goto loc_0046D5A6;
loc_0046D538:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 11909119 + 0 * 8) + 209)) != ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11909119 + 0 * 8) + 36424) + 705)))) goto loc_0046D5E3;
    v_stack_p18 = v_rsi + 264;
loc_0046D568:
    *(unsigned __int64 *)(v_rsi + 256) = v_rsi + 264;
    goto loc_0046D4E5;
loc_0046D574:
    a2 = 0;
    result = (unsigned int)((*(unsigned __int16 *)(v_rsi + 264 - 56)) << (7));
    *(unsigned int *)(v_rsi + 264 - 48) = (unsigned int)(result);
    goto loc_0046D52E;
loc_0046D585:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 12))) == 0) goto loc_0046D6CA;
    if (0 < ((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 12))))) goto loc_0046D6CA;
loc_0046D59B:
    result = (unsigned int)((0) << (7));
    a2 = 0;
    *(unsigned int *)(a1 + 8) = (unsigned int)(result);
loc_0046D5A6:
    a2 = 0;
    result = KiUpdateCpuTargetByRate(a1, a2, (unsigned __int16)(a2), 0);
loc_0046D5B0:
    result = KeReleaseInStackQueuedSpinLock(v_stack_m58, a2, (unsigned __int16)(a2), 0);
    if (((*(unsigned int *)(v_rip + 11900240)) & (0x4000ULL)) != 0) goto loc_0046D6F2;
loc_0046D5CA:
    v_rsp = (v_rsp) + (64);
    return result;
loc_0046D5E3:
    goto loc_0046D568;
loc_0046D5F0:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 11900098)))) & (64)) == 0) goto loc_0046D469;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_stack_p90, a2, (unsigned __int16)(a2), 0);
    if ((unsigned __int8)(result) == 0) goto loc_0046D469;
    result = HvlNotifyLongSpinWait(0, a2, (unsigned __int16)(a2), 0);
    goto loc_0046D46B;
loc_0046D618:
    if (a3 == 0) goto loc_0046D649;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 16))) == 0) goto loc_0046D62B;
    result = (unsigned __int16)(v_stack_p20);
    if (((unsigned int)((unsigned __int16)(v_stack_p20))) < ((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 16))))) {
        result = (unsigned __int16)(v_stack_p20);
        *(unsigned int *)(a3 + 16) = (unsigned int)(result);
    }
    if (((unsigned int)((unsigned __int16)(v_stack_p20))) == ((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 16))))) goto loc_0046D5B0;
    goto loc_0046D670;
loc_0046D649:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11230693))) == 0) goto loc_0046D6BF;
    if (((unsigned int)((unsigned __int16)(*(unsigned __int64 *)(a3 + 80)))) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11230693))))) goto loc_0046D6BF;
loc_0046D65A:
    if (((unsigned int)((unsigned __int16)(*(unsigned __int64 *)(a3 + 80)))) == ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11230693))))) goto loc_0046D5B0;
loc_0046D670:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11230640) - 56 + 4)))) & (1)) == 0) goto loc_0046D688;
loc_0046D67B:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11230640))) != (a3 + 80)) goto loc_0046D670;
    goto loc_0046D5B0;
loc_0046D688:
    a2 = 0;
    result = (unsigned int)((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 11230640) - 56)) << (7));
    a2 = 0;
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 11230640) - 56 + 8) = (unsigned int)(result);
    result = KiUpdateCpuTargetByWeight(*(unsigned __int64 *)(v_rip + 11230640) - 56, a2, (unsigned __int16)(a2), 0);
    goto loc_0046D67B;
loc_0046D69E:
    result = KiEnableGroupScheduling(*(unsigned __int64 *)(v_rip + 11230640) - 56, a2, (unsigned __int16)(a2), 0);
    goto loc_0046D365;
loc_0046D6A8:
    *(unsigned int *)((unsigned int)(*(unsigned int *)(v_rip + 11230693)) + 252) = 1;
    goto loc_0046D4D4;
loc_0046D6BF:
    *(unsigned int *)(v_rip + 11230572) = (unsigned int)((unsigned __int16)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11230640))));
    goto loc_0046D65A;
loc_0046D6CA:
    a2 = 0;
    *(unsigned int *)(a3 + 12) = (unsigned int)((unsigned __int16)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11230640))));
    result = KiAssignSchedulingGroupWeights(a2 + 1, a2, a3, 0);
    goto loc_0046D5A6;
loc_0046D6E2:
    if (((unsigned int)((unsigned __int16)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11230640))))) < ((unsigned int)(a2 + 1))) goto loc_0046D515;
    goto loc_0046D59B;
loc_0046D6F2:
    result = EtwTraceSchedulingGroup(a1, (unsigned int)(0x562ULL), a3, 0);
    goto loc_0046D5CA;
}
```

## 5. (Beta) C Style

```c
int64_t KeInsertSchedulingGroup(void *Arg1, int64_t Arg2, int64_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_rbp;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m58;
    uint64_t v_stack_p10;
    uint8_t v_stack_p14;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint32_t v_stack_p8;
    uint64_t v_stack_p90;

    v_stack_p20 = local_rbx;
    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (64);
    result = 0;
    local_r13 = 0;
    v_stack_m48 = 0;
    v_stack_m58 = v_xmm0;
    if ((*(uint8_t *)(v_rip + 0xB59773)) == 0) goto loc_0046D69E;
loc_0046D365:
    Arg1 = 0;
    *(uint64_t *)(arg1) = Arg2;
    *(uint64_t *)(arg1 + 0x20) = 0;
    *(uint64_t *)(arg1 + 0xC) = 0;
    *(uint32_t *)(arg1 + 0x14) = 0;
    result = KeQueryPerformanceCounter(Arg1, Arg2, Arg3, a4);
    *(uint64_t *)(arg1 + 0x18) = result;
    *(void **)(arg1 + 0x50 + 0x8) = Arg1 + 80;
    *(void **)(arg1 + 0x50) = Arg1 + 80;
    *(void **)(arg1 + 0x38 + 0x8) = Arg1 + 56;
    *(void **)(arg1 + 0x38) = Arg1 + 56;
    *(uint64_t *)(arg1 + 0x60) = 0;
    *(uint64_t *)(arg1 + 0x28) = 0;
    *(uint64_t *)(arg1 + 0x30) = 0;
    if ((*(uint32_t *)(v_rip + 0xB5973D)) <= 0) goto loc_0046D3D2;
loc_0046D3AD:
    Arg1 = (Arg1) * (0);
    Arg1 = (Arg1) - (-128);
    Arg1 = (Arg1) + (Arg1);
    result = KiInitializeScb(Arg1, Arg2, Arg3, 0);
    local_rbp = (uint32_t)((0) + 1);
    if (((uint32_t)(local_rbp)) < (*(uint32_t *)(v_rip + 0xB59718))) goto loc_0046D3AD;
loc_0046D3D2:
    result = KeAcquireInStackQueuedSpinLock(v_rip + 11935138, v_stack_m58, Arg3, 0);
    if (Arg3 != 0) goto loc_0046D494;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xAB602E))) != (v_rip + 11231286)) goto loc_0046D48D;
    *(uint64_t *)(arg1 + 0x38) = v_rip + 11231286;
    *(uint64_t *)(arg1 + 0x38 + 0x8) = *(uint64_t *)(v_rip + 0xAB602E);
    *(void **)(*(uint64_t *)(v_rip + 0xAB602E)) = Arg1 + 56;
    *(void **)(v_rip + 0xAB6014) = Arg1 + 56;
loc_0046D414:
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB59665)));
    v_stack_p18 = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB59665))) == 0) goto loc_0046D4F6;
loc_0046D437:
    local_rsi = (Arg1 + 56) * (0);
    local_rsi = (local_rsi) + (Arg1);
loc_0046D450:
    if (condition_is_above_or_equal) goto loc_0046D476;
loc_0046D459:
    local_r13 = (uint32_t)((local_r13) + 1);
    if (((*(uint32_t *)(v_rip + 0xB57E49)) & ((uint32_t)(local_r13))) == 0) goto loc_0046D5F0;
loc_0046D469:
loc_0046D46B:
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0xB5B7FF + 0x0 * 8) + 0x30) == 0) goto loc_0046D450;
    goto loc_0046D459;
loc_0046D476:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB5B7FF + 0x0 * 8) + 0x8A88 + 0x8))) == (*(uint64_t *)(v_rip + 0xB5B7FF + 0x0 * 8) + 35464)) goto loc_0046D4B8;
loc_0046D48D:
loc_0046D494:
    *(uint64_t *)(arg1 + 0x60) = Arg3;
    if ((*(uint64_t *)(*(uint64_t *)(Arg3 + 0x50 + 0x8))) != (Arg3 + 80)) goto loc_0046D48D;
    *(uint64_t *)(local_rsi) = Arg3 + 80;
    *(uint64_t *)(local_rsi + 0x8) = *(uint64_t *)(Arg3 + 0x50 + 0x8);
    *(uint64_t *)(*(uint64_t *)(Arg3 + 0x50 + 0x8)) = local_rsi;
    *(uint64_t *)(Arg3 + 0x50 + 0x8) = local_rsi;
    goto loc_0046D414;
loc_0046D4B8:
    *(uint64_t *)(Arg3 + 0x50) = *(uint64_t *)(Arg3 + 0x50 + 0x8);
    *(uint64_t *)(Arg3 + 0x50 + 0x8) = *(uint64_t *)(*(uint64_t *)(v_rip + 0xB5B7FF + 0x0 * 8) + 0x8A88 + 0x8);
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB5B7FF + 0x0 * 8) + 0x8A88 + 0x8)) = Arg3 + 80;
    *(uint64_t *)(*(uint64_t *)(Arg3 + 0x50 + 0x8) + 0x8) = Arg3 + 80;
    if (((v_stack_p14) & (4)) != 0) goto loc_0046D6A8;
loc_0046D4D4:
    local_r13 = 0;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xB5B7FF + 0x0 * 8) + 0x8E40)) != 0) goto loc_0046D538;
loc_0046D4E5:
    local_r12 = (uint32_t)((0) + 1);
    if (((uint32_t)(local_r12)) < v_stack_p8) goto loc_0046D437;
loc_0046D4F6:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)))) & (1)) == 0) goto loc_0046D618;
    if (Arg3 != 0) goto loc_0046D585;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xAB5F2B))) != 0) goto loc_0046D6E2;
loc_0046D515:
    *(uint32_t *)(v_rip + 0xAB5F11) = (uint32_t)((uint16_t)(Arg2));
loc_0046D527:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xAB5F04) - 0x34)))) & (1)) != 0) goto loc_0046D574;
loc_0046D52E:
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xAB5F04))) != (v_rip + 11231286)) goto loc_0046D527;
    goto loc_0046D5A6;
loc_0046D538:
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0xB5B7FF + 0x0 * 8) + 0xD1)) != ((uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB5B7FF + 0x0 * 8) + 0x8E48) + 0x2C1)))) goto loc_0046D5E3;
    v_stack_p18 = local_rsi + 264;
loc_0046D568:
    *(uint64_t *)(local_rsi + 0x100) = local_rsi + 264;
    goto loc_0046D4E5;
loc_0046D574:
    Arg2 = 0;
    result = (uint32_t)((*(uint16_t *)(local_rsi + 0x108 - 0x38)) << (7));
    *(uint32_t *)(local_rsi + 0x108 - 0x30) = (uint32_t)(result);
    goto loc_0046D52E;
loc_0046D585:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(Arg3 + 0xC))) == 0) goto loc_0046D6CA;
    if (0 < ((uint32_t)((uint32_t)(*(uint32_t *)(Arg3 + 0xC))))) goto loc_0046D6CA;
loc_0046D59B:
    result = (uint32_t)((0) << (7));
    Arg2 = 0;
    *(uint32_t *)(arg1 + 0x8) = (uint32_t)(result);
loc_0046D5A6:
    Arg2 = 0;
    result = KiUpdateCpuTargetByRate(Arg1, Arg2, (uint16_t)(Arg2), 0);
loc_0046D5B0:
    result = KeReleaseInStackQueuedSpinLock(v_stack_m58, Arg2, (uint16_t)(Arg2), 0);
    if (((*(uint32_t *)(v_rip + 0xB59550)) & (0x4000ULL)) != 0) goto loc_0046D6F2;
loc_0046D5CA:
    local_rsp = (local_rsp) + (64);
    return result;
loc_0046D5E3:
    goto loc_0046D568;
loc_0046D5F0:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB594C2)))) & (64)) == 0) goto loc_0046D469;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_stack_p90, Arg2, (uint16_t)(Arg2), 0);
    if ((uint8_t)(result) == 0) goto loc_0046D469;
    result = HvlNotifyLongSpinWait(0, Arg2, (uint16_t)(Arg2), 0);
    goto loc_0046D46B;
loc_0046D618:
    if (Arg3 == 0) goto loc_0046D649;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(Arg3 + 0x10))) == 0) goto loc_0046D62B;
    result = (uint16_t)(v_stack_p20);
    if (((uint32_t)((uint16_t)(v_stack_p20))) < ((uint32_t)((uint32_t)(*(uint32_t *)(Arg3 + 0x10))))) {
        result = (uint16_t)(v_stack_p20);
        *(uint32_t *)(Arg3 + 0x10) = (uint32_t)(result);
    }
    if (((uint32_t)((uint16_t)(v_stack_p20))) == ((uint32_t)((uint32_t)(*(uint32_t *)(Arg3 + 0x10))))) goto loc_0046D5B0;
    goto loc_0046D670;
loc_0046D649:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xAB5DE5))) == 0) goto loc_0046D6BF;
    if (((uint32_t)((uint16_t)(*(uint64_t *)(Arg3 + 0x50)))) < ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xAB5DE5))))) goto loc_0046D6BF;
loc_0046D65A:
    if (((uint32_t)((uint16_t)(*(uint64_t *)(Arg3 + 0x50)))) == ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xAB5DE5))))) goto loc_0046D5B0;
loc_0046D670:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xAB5DB0) - 0x38 + 0x4)))) & (1)) == 0) goto loc_0046D688;
loc_0046D67B:
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xAB5DB0))) != (Arg3 + 80)) goto loc_0046D670;
    goto loc_0046D5B0;
loc_0046D688:
    Arg2 = 0;
    result = (uint32_t)((*(uint16_t *)(*(uint64_t *)(v_rip + 0xAB5DB0) - 0x38)) << (7));
    Arg2 = 0;
    *(uint32_t *)(*(uint64_t *)(v_rip + 0xAB5DB0) - 0x38 + 0x8) = (uint32_t)(result);
    result = KiUpdateCpuTargetByWeight(*(uint64_t *)(v_rip + 0xAB5DB0) - 56, Arg2, (uint16_t)(Arg2), 0);
    goto loc_0046D67B;
loc_0046D69E:
    result = KiEnableGroupScheduling(*(uint64_t *)(v_rip + 0xAB5DB0) - 56, Arg2, (uint16_t)(Arg2), 0);
    goto loc_0046D365;
loc_0046D6A8:
    *(uint32_t *)((uint32_t)(*(uint32_t *)(v_rip + 0xAB5DE5)) + 0xFC) = 1;
    goto loc_0046D4D4;
loc_0046D6BF:
    *(uint32_t *)(v_rip + 0xAB5D6C) = (uint32_t)((uint16_t)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xAB5DB0))));
    goto loc_0046D65A;
loc_0046D6CA:
    Arg2 = 0;
    *(uint32_t *)(Arg3 + 0xC) = (uint32_t)((uint16_t)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xAB5DB0))));
    result = KiAssignSchedulingGroupWeights(Arg2 + 1, Arg2, Arg3, 0);
    goto loc_0046D5A6;
loc_0046D6E2:
    if (((uint32_t)((uint16_t)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xAB5DB0))))) < ((uint32_t)(Arg2 + 1))) goto loc_0046D515;
    goto loc_0046D59B;
loc_0046D6F2:
    result = EtwTraceSchedulingGroup(Arg1, (uint32_t)(0x562ULL), Arg3, 0);
    goto loc_0046D5CA;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `W` |
| `Arg1` | `+ 0x4` | `32` | `R` |
| `Arg1` | `+ 0x8` | `32` | `W` |
| `Arg1` | `+ 0x8` | `64` | `W` |
| `Arg1` | `+ 0xC` | `64` | `W` |
| `Arg1` | `+ 0x14` | `32` | `W` |
| `Arg1` | `+ 0x18` | `64` | `W` |
| `Arg1` | `+ 0x20` | `64` | `W` |
| `Arg1` | `+ 0x28` | `64` | `W` |
| `Arg1` | `+ 0x30` | `64` | `W` |
| `Arg1` | `+ 0x38` | `64` | `R` |
| `Arg1` | `+ 0x50` | `64` | `R` |
| `Arg1` | `+ 0x60` | `64` | `W` |
| `Arg1` | `+ 0xC8` | `64` | `R` |
| `Arg1` | `+ 0xF0` | `16` | `R/W` |
| `Arg1` | `+ 0xFC` | `32` | `W` |
| `Arg1` | `+ 0x100` | `64` | `W` |
| `Arg1` | `+ 0x108` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0046D324&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
