# KiProcessExpiredTimerList

- RVA: `0x00234200`–`0x002346F8` (길이 `1,272` bytes)
- VA: `0x0000000140234200`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006055C`
- 디코드: `307`개 명령, `1,272/1,272` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **18**; 고유 호출 대상: **15**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **12**

### Outgoing calls
- `0x002342BA` → [KiTimerWaitTest](KiTimerWaitTest_function_002337D0.md) (function, `0x002337D0`)
- `0x002342FC` → [KiProcessThreadWaitList](../25/KiProcessThreadWaitList_function_00252CC0.md) (function, `0x00252CC0`)
- `0x00234308` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00234343` → [KiProcessThreadWaitList](../25/KiProcessThreadWaitList_function_00252CC0.md) (function, `0x00252CC0`)
- `0x00234491` → [PopPepIdleTimeoutDpcRoutine](../4A/PopPepIdleTimeoutDpcRoutine_function_004A5B60.md) (function, `0x004A5B60`)
- `0x0023449B` → [PfSnTraceTimerRoutine](../48/PfSnTraceTimerRoutine_function_0048AEC0.md) (function, `0x0048AEC0`)
- `0x002344E1` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x002344F7` → [KeQueryPerformanceCounter](../37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x0023453A` → [PopFxResidentTimeoutDpcRoutine](../4A/PopFxResidentTimeoutDpcRoutine_function_004A54C0.md) (function, `0x004A54C0`)
- `0x00234544` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00234576` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00234612` → [EtwpLogKernelEvent](../25/EtwpLogKernelEvent_function_0025CC00.md) (function, `0x0025CC00`)
- `0x00234637` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00234646` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00234683` → [KiTimerWaitTest](KiTimerWaitTest_function_002337D0.md) (function, `0x002337D0`)
- `0x002346C6` → [EtwTraceKernelEvent](EtwTraceKernelEvent_function_00235350.md) (function, `0x00235350`)
- `0x002346D6` → [RtlGetSystemTimePrecise](../37/RtlGetSystemTimePrecise_function_0037EDD0.md) (function, `0x0037EDD0`)
- `0x002346E6` → [EtwpGetHostPerfCounter](../3A/EtwpGetHostPerfCounter_function_003A4134.md) (function, `0x003A4134`)

### Direct callers
- [sub_002348D3](Unknown_function_002348D3.md) at `0x00234A4E`
- [sub_002348D3](Unknown_function_002348D3.md) at `0x00234AED`
- [sub_00234FE8](Unknown_function_00234FE8.md) at `0x00235189`
- [sub_00234FE8](Unknown_function_00234FE8.md) at `0x002351BC`

### Static image references
- `0x0023421C` → RVA `0x00E0A740` (`.data`; read)
- `0x0023422A` → RVA `0x00FC6B04` (`ALMOSTRO`; read)
- `0x00234233` → RVA `0x00FC6B08` (`ALMOSTRO`; read)
- `0x00234364` → RVA `0x00FCFC80` (`CACHEALI`; read)
- `0x00234439` → RVA `0x0048AEC0` (`PfSnTraceTimerRoutine`; read)
- `0x0023446E` → RVA `0x004A54C0` (`PopFxResidentTimeoutDpcRoutine`; read)
- `0x0023447E` → RVA `0x004A5B60` (`PopPepIdleTimeoutDpcRoutine`; read)
- `0x00234512` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x0023459A` → RVA `0x00FC6AA8` (`ALMOSTRO`; read)
- `0x00234629` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x00234650` → RVA `0x00FC6F78` (`ALMOSTRO`; read)
- `0x00234672` → RVA `0x00FC7250` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00234200  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00234205  55                              push rbp
00234206  56                              push rsi
00234207  57                              push rdi
00234208  41 54                           push r12
0023420A  41 55                           push r13
0023420C  41 56                           push r14
0023420E  41 57                           push r15
00234210  48 8D 6C 24 D9                  lea rbp, [rsp - 0x27]
00234215  48 81 EC F0 00 00 00            sub rsp, 0xf0
0023421C  48 8B 05 1D 65 BD 00            mov rax, qword ptr [rip + 0xbd651d]
00234223  48 33 C4                        xor rax, rsp
00234226  48 89 45 1F                     mov qword ptr [rbp + 0x1f], rax
0023422A  8B 05 D4 28 D9 00               mov eax, dword ptr [rip + 0xd928d4]
00234230  45 33 FF                        xor r15d, r15d
00234233  44 8B 35 CE 28 D9 00            mov r14d, dword ptr [rip + 0xd928ce]
0023423A  25 80 00 00 00                  and eax, 0x80
0023423F  4C 8B 61 08                     mov r12, qword ptr [rcx + 8]
00234243  0F 57 C0                        xorps xmm0, xmm0
00234246  0F 57 C9                        xorps xmm1, xmm1
00234249  44 89 4D A3                     mov dword ptr [rbp - 0x5d], r9d
0023424D  41 81 E6 00 00 02 00            and r14d, 0x20000
00234254  4C 89 45 8F                     mov qword ptr [rbp - 0x71], r8
00234258  44 89 74 24 30                  mov dword ptr [rsp + 0x30], r14d
0023425D  48 8B F9                        mov rdi, rcx
00234260  48 89 54 24 38                  mov qword ptr [rsp + 0x38], rdx
00234265  45 8B EF                        mov r13d, r15d
00234268  4C 89 7D 87                     mov qword ptr [rbp - 0x79], r15
0023426C  0F 11 45 DF                     movups xmmword ptr [rbp - 0x21], xmm0
00234270  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
00234274  0F 11 45 EF                     movups xmmword ptr [rbp - 0x11], xmm0
00234278  4C 89 65 97                     mov qword ptr [rbp - 0x69], r12
0023427C  0F 11 4D AF                     movups xmmword ptr [rbp - 0x51], xmm1
00234280  0F 11 4D BF                     movups xmmword ptr [rbp - 0x41], xmm1
00234284  41 8B C5                        mov eax, r13d
00234287  49 8B DF                        mov rbx, r15
0023428A  41 FF C5                        inc r13d
0023428D  49 87 1C C0                     xchg qword ptr [r8 + rax*8], rbx
00234291  48 85 DB                        test rbx, rbx
00234294  74 3F                           je 0x1402342d5
00234296  F0 0F BA 2B 07                  lock bts dword ptr [rbx], 7
0023429B  41 8B F7                        mov esi, r15d
0023429E  0F 82 6C 02 00 00               jb 0x140234510
002342A4  45 85 F6                        test r14d, r14d
002342A7  4C 8D 72 08                     lea r14, [rdx + 8]
002342AB  4D 8B C6                        mov r8, r14
002342AE  48 8B D3                        mov rdx, rbx
002342B1  0F 85 99 03 00 00               jne 0x140234650
002342B7  48 8B CF                        mov rcx, rdi
002342BA  E8 11 F5 FF FF                  call 0x1402337d0
002342BF  48 8B F0                        mov rsi, rax
002342C2  48 85 F6                        test rsi, rsi
002342C5  75 62                           jne 0x140234329
002342C7  4C 8B 45 8F                     mov r8, qword ptr [rbp - 0x71]
002342CB  48 8B 54 24 38                  mov rdx, qword ptr [rsp + 0x38]
002342D0  44 8B 74 24 30                  mov r14d, dword ptr [rsp + 0x30]
002342D5  44 3B 6D A3                     cmp r13d, dword ptr [rbp - 0x5d]
002342D9  72 A9                           jb 0x140234284
002342DB  4C 89 BF 60 38 00 00            mov qword ptr [rdi + 0x3860], r15
002342E2  48 83 BF 08 2D 00 00 00         cmp qword ptr [rdi + 0x2d08], 0
002342EA  74 15                           je 0x140234301
002342EC  41 B9 02 00 00 00               mov r9d, 2
002342F2  45 33 C0                        xor r8d, r8d
002342F5  48 8B CF                        mov rcx, rdi
002342F8  41 8D 51 FF                     lea edx, [r9 - 1]
002342FC  E8 BF E9 01 00                  call 0x140252cc0
00234301  48 8B 4D 1F                     mov rcx, qword ptr [rbp + 0x1f]
00234305  48 33 CC                        xor rcx, rsp
00234308  E8 33 83 47 00                  call 0x1406ac640
0023430D  48 8B 9C 24 48 01 00 00         mov rbx, qword ptr [rsp + 0x148]
00234315  48 81 C4 F0 00 00 00            add rsp, 0xf0
0023431C  41 5F                           pop r15
0023431E  41 5E                           pop r14
00234320  41 5D                           pop r13
00234322  41 5C                           pop r12
00234324  5F                              pop rdi
00234325  5E                              pop rsi
00234326  5D                              pop rbp
00234327  C3                              ret
00234328  CC                              int3
00234329  48 83 BF 08 2D 00 00 00         cmp qword ptr [rdi + 0x2d08], 0
00234331  74 15                           je 0x140234348
00234333  41 B9 02 00 00 00               mov r9d, 2
00234339  45 33 C0                        xor r8d, r8d
0023433C  48 8B CF                        mov rcx, rdi
0023433F  41 8D 51 FF                     lea edx, [r9 - 1]
00234343  E8 78 E9 01 00                  call 0x140252cc0
00234348  83 7C 24 44 00                  cmp dword ptr [rsp + 0x44], 0
0023434D  45 8B BC 24 E4 01 00 00         mov r15d, dword ptr [r12 + 0x1e4]
00234355  45 0F B6 A4 24 32 02 00 00      movzx r12d, byte ptr [r12 + 0x232]
0023435E  0F 84 A6 00 00 00               je 0x14023440a
00234364  4C 8B 05 15 B9 D9 00            mov r8, qword ptr [rip + 0xd9b915]
0023436B  33 C0                           xor eax, eax
0023436D  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00234371  8B D8                           mov ebx, eax
00234373  4D 85 C0                        test r8, r8
00234376  0F 84 74 01 00 00               je 0x1402344f0
0023437C  41 8B 90 A8 11 00 00            mov edx, dword ptr [r8 + 0x11a8]
00234383  0F BC CA                        bsf ecx, edx
00234386  89 4C 24 40                     mov dword ptr [rsp + 0x40], ecx
0023438A  74 3F                           je 0x1402343cb
0023438C  0F 1F 40 00                     nop dword ptr [rax]
00234390  8D 42 FF                        lea eax, [rdx - 1]
00234393  23 D0                           and edx, eax
00234395  48 8B C1                        mov rax, rcx
00234398  48 C1 E0 05                     shl rax, 5
0023439C  48 05 CC 11 00 00               add rax, 0x11cc
002343A2  49 03 C0                        add rax, r8
002343A5  74 19                           je 0x1402343c0
002343A7  8B 40 04                        mov eax, dword ptr [rax + 4]
002343AA  84 C0                           test al, al
002343AC  79 12                           jns 0x1402343c0
002343AE  41 0F B6 8C 48 99 11 00 00      movzx ecx, byte ptr [r8 + rcx*2 + 0x1199]
002343B7  B8 01 00 00 00                  mov eax, 1
002343BC  D3 E0                           shl eax, cl
002343BE  0B D8                           or ebx, eax
002343C0  0F BC CA                        bsf ecx, edx
002343C3  75 CB                           jne 0x140234390
002343C5  89 4C 24 40                     mov dword ptr [rsp + 0x40], ecx
002343C9  33 C0                           xor eax, eax
002343CB  F6 C3 02                        test bl, 2
002343CE  0F 85 21 01 00 00               jne 0x1402344f5
002343D4  48 89 45 AF                     mov qword ptr [rbp - 0x51], rax
002343D8  F6 C3 04                        test bl, 4
002343DB  0F 85 F5 02 00 00               jne 0x1402346d6
002343E1  48 89 45 B7                     mov qword ptr [rbp - 0x49], rax
002343E5  F6 C3 08                        test bl, 8
002343E8  0F 84 F9 00 00 00               je 0x1402344e7
002343EE  0F 31                           rdtsc
002343F0  48 C1 E2 20                     shl rdx, 0x20
002343F4  48 0B C2                        or rax, rdx
002343F7  48 89 45 BF                     mov qword ptr [rbp - 0x41], rax
002343FB  33 C0                           xor eax, eax
002343FD  F6 C3 10                        test bl, 0x10
00234400  0F 85 E0 02 00 00               jne 0x1402346e6
00234406  48 89 45 C7                     mov qword ptr [rbp - 0x39], rax
0023440A  48 8B 56 18                     mov rdx, qword ptr [rsi + 0x18]
0023440E  4C 8B 44 24 38                  mov r8, qword ptr [rsp + 0x38]
00234413  48 89 55 87                     mov qword ptr [rbp - 0x79], rdx
00234417  41 8B 08                        mov ecx, dword ptr [r8]
0023441A  8D 41 01                        lea eax, [rcx + 1]
0023441D  83 E1 0F                        and ecx, 0xf
00234420  41 89 00                        mov dword ptr [r8], eax
00234423  48 8D 04 49                     lea rax, [rcx + rcx*2]
00234427  49 8D 1C C0                     lea rbx, [r8 + rax*8]
0023442B  48 B8 20 03 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000320
00234435  48 89 53 10                     mov qword ptr [rbx + 0x10], rdx
00234439  48 8D 0D 80 6A 25 00            lea rcx, [rip + 0x256a80]
00234440  48 8B 00                        mov rax, qword ptr [rax]
00234443  48 89 43 18                     mov qword ptr [rbx + 0x18], rax
00234447  33 C0                           xor eax, eax
00234449  48 89 43 20                     mov qword ptr [rbx + 0x20], rax
0023444D  89 87 5C 86 00 00               mov dword ptr [rdi + 0x865c], eax
00234453  48 8B 45 87                     mov rax, qword ptr [rbp - 0x79]
00234457  C6 87 BA 38 00 00 01            mov byte ptr [rdi + 0x38ba], 1
0023445E  45 8B 48 0C                     mov r9d, dword ptr [r8 + 0xc]
00234462  45 8B 06                        mov r8d, dword ptr [r14]
00234465  48 8B 56 20                     mov rdx, qword ptr [rsi + 0x20]
00234469  48 3B C1                        cmp rax, rcx
0023446C  74 2A                           je 0x140234498
0023446E  48 8D 0D 4B 10 27 00            lea rcx, [rip + 0x27104b]
00234475  48 3B C1                        cmp rax, rcx
00234478  0F 84 B9 00 00 00               je 0x140234537
0023447E  48 8D 0D DB 16 27 00            lea rcx, [rip + 0x2716db]
00234485  48 3B C1                        cmp rax, rcx
00234488  48 8B CE                        mov rcx, rsi
0023448B  0F 85 B3 00 00 00               jne 0x140234544
00234491  E8 CA 16 27 00                  call 0x1404a5b60
00234496  EB 08                           jmp 0x1402344a0
00234498  48 8B CE                        mov rcx, rsi
0023449B  E8 20 6A 25 00                  call 0x14048aec0
002344A0  48 8B 4D 97                     mov rcx, qword ptr [rbp - 0x69]
002344A4  48 B8 20 03 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000320
002344AE  C6 87 BA 38 00 00 00            mov byte ptr [rdi + 0x38ba], 0
002344B5  48 8B 00                        mov rax, qword ptr [rax]
002344B8  48 89 43 20                     mov qword ptr [rbx + 0x20], rax
002344BC  8B 81 E4 01 00 00               mov eax, dword ptr [rcx + 0x1e4]
002344C2  44 3B F8                        cmp r15d, eax
002344C5  0F 84 83 00 00 00               je 0x14023454e
002344CB  4C 8B 45 87                     mov r8, qword ptr [rbp - 0x79]
002344CF  4D 8B CF                        mov r9, r15
002344D2  BA 05 00 00 00                  mov edx, 5
002344D7  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
002344DC  B9 C7 00 00 00                  mov ecx, 0xc7
002344E1  E8 7A 91 2C 00                  call 0x1404fd660
002344E6  CC                              int3
002344E7  48 89 45 BF                     mov qword ptr [rbp - 0x41], rax
002344EB  E9 0D FF FF FF                  jmp 0x1402343fd
002344F0  BB 1E 00 00 00                  mov ebx, 0x1e
002344F5  33 C9                           xor ecx, ecx
002344F7  E8 E4 A2 14 00                  call 0x14037e7e0
002344FC  48 89 45 AF                     mov qword ptr [rbp - 0x51], rax
00234500  33 C0                           xor eax, eax
00234502  E9 D1 FE FF FF                  jmp 0x1402343d8
00234507  66 0F 1F 84 00 00 00 00 00      nop word ptr [rax + rax]
00234510  FF C6                           inc esi
00234512  85 35 94 0D D9 00               test dword ptr [rip + 0xd90d94], esi
00234518  0F 84 0B 01 00 00               je 0x140234629
0023451E  F3 90                           pause
00234520  8B 03                           mov eax, dword ptr [rbx]
00234522  84 C0                           test al, al
00234524  78 EA                           js 0x140234510
00234526  F0 0F BA 2B 07                  lock bts dword ptr [rbx], 7
0023452B  72 E3                           jb 0x140234510
0023452D  48 8B 54 24 38                  mov rdx, qword ptr [rsp + 0x38]
00234532  E9 6D FD FF FF                  jmp 0x1402342a4
00234537  48 8B CE                        mov rcx, rsi
0023453A  E8 81 0F 27 00                  call 0x1404a54c0
0023453F  E9 5C FF FF FF                  jmp 0x1402344a0
00234544  E8 87 65 48 00                  call 0x1406baad0
00234549  E9 52 FF FF FF                  jmp 0x1402344a0
0023454E  48 0F BE 81 32 02 00 00         movsx rax, byte ptr [rcx + 0x232]
00234556  44 3A E0                        cmp r12b, al
00234559  74 21                           je 0x14023457c
0023455B  48 8B 55 87                     mov rdx, qword ptr [rbp - 0x79]
0023455F  4C 8B C0                        mov r8, rax
00234562  41 B9 05 00 00 00               mov r9d, 5
00234568  48 C7 44 24 20 00 00 00 00      mov qword ptr [rsp + 0x20], 0
00234571  B9 F9 01 00 00                  mov ecx, 0x1f9
00234576  E8 E5 90 2C 00                  call 0x1404fd660
0023457B  CC                              int3
0023457C  45 33 FF                        xor r15d, r15d
0023457F  44 39 7C 24 44                  cmp dword ptr [rsp + 0x44], r15d
00234584  0F 84 66 01 00 00               je 0x1402346f0
0023458A  48 8D 45 87                     lea rax, [rbp - 0x79]
0023458E  48 C7 45 17 08 00 00 00         mov qword ptr [rbp + 0x17], 8
00234596  48 89 45 0F                     mov qword ptr [rbp + 0xf], rax
0023459A  48 8B 05 07 25 D9 00            mov rax, qword ptr [rip + 0xd92507]
002345A1  8B 98 A8 11 00 00               mov ebx, dword ptr [rax + 0x11a8]
002345A7  0F BC CB                        bsf ecx, ebx
002345AA  89 4C 24 48                     mov dword ptr [rsp + 0x48], ecx
002345AE  74 70                           je 0x140234620
002345B0  48 8B 15 F1 24 D9 00            mov rdx, qword ptr [rip + 0xd924f1]
002345B7  8D 43 FF                        lea eax, [rbx - 1]
002345BA  23 D8                           and ebx, eax
002345BC  44 8B C1                        mov r8d, ecx
002345BF  8B C1                           mov eax, ecx
002345C1  48 C1 E0 05                     shl rax, 5
002345C5  48 05 CC 11 00 00               add rax, 0x11cc
002345CB  48 03 C2                        add rax, rdx
002345CE  74 47                           je 0x140234617
002345D0  8B 40 04                        mov eax, dword ptr [rax + 4]
002345D3  84 C0                           test al, al
002345D5  79 40                           jns 0x140234617
002345D7  0F B6 84 4A 99 11 00 00         movzx eax, byte ptr [rdx + rcx*2 + 0x1199]
002345DF  41 B9 02 00 00 00               mov r9d, 2
002345E5  46 0F B6 84 42 98 11 00 00      movzx r8d, byte ptr [rdx + r8*2 + 0x1198]
002345EE  C7 44 24 28 02 0A 50 00         mov dword ptr [rsp + 0x28], 0x500a02
002345F6  48 C7 45 07 08 00 00 00         mov qword ptr [rbp + 7], 8
002345FE  48 8D 4C C5 A7                  lea rcx, [rbp + rax*8 - 0x59]
00234603  66 C7 44 24 20 45 0F            mov word ptr [rsp + 0x20], 0xf45
0023460A  48 89 4D FF                     mov qword ptr [rbp - 1], rcx
0023460E  48 8D 4D FF                     lea rcx, [rbp - 1]
00234612  E8 E9 85 02 00                  call 0x14025cc00
00234617  0F BC CB                        bsf ecx, ebx
0023461A  75 94                           jne 0x1402345b0
0023461C  89 4C 24 48                     mov dword ptr [rsp + 0x48], ecx
00234620  4C 8B 65 97                     mov r12, qword ptr [rbp - 0x69]
00234624  E9 9E FC FF FF                  jmp 0x1402342c7
00234629  8B 05 89 24 D9 00               mov eax, dword ptr [rip + 0xd92489]
0023462F  A8 40                           test al, 0x40
00234631  0F 84 E7 FE FF FF               je 0x14023451e
00234637  E8 54 AE 0D 00                  call 0x14030f490
0023463C  84 C0                           test al, al
0023463E  0F 84 DA FE FF FF               je 0x14023451e
00234644  8B CE                           mov ecx, esi
00234646  E8 15 AE 0D 00                  call 0x14030f460
0023464B  E9 D0 FE FF FF                  jmp 0x140234520
00234650  48 8B 0D 21 29 D9 00            mov rcx, qword ptr [rip + 0xd92921]
00234657  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
0023465B  48 89 45 DF                     mov qword ptr [rbp - 0x21], rax
0023465F  48 8B 43 30                     mov rax, qword ptr [rbx + 0x30]
00234663  48 33 C1                        xor rax, rcx
00234666  48 D3 C0                        rol rax, cl
00234669  48 8B CF                        mov rcx, rdi
0023466C  48 33 C3                        xor rax, rbx
0023466F  48 0F C8                        bswap rax
00234672  48 33 05 D7 2B D9 00            xor rax, qword ptr [rip + 0xd92bd7]
00234679  74 55                           je 0x1402346d0
0023467B  48 8B 40 18                     mov rax, qword ptr [rax + 0x18]
0023467F  48 89 45 EF                     mov qword ptr [rbp - 0x11], rax
00234683  E8 48 F1 FF FF                  call 0x1402337d0
00234688  48 8B F0                        mov rsi, rax
0023468B  48 89 5D E7                     mov qword ptr [rbp - 0x19], rbx
0023468F  0F B6 43 01                     movzx eax, byte ptr [rbx + 1]
00234693  48 8D 4D CF                     lea rcx, [rbp - 0x31]
00234697  C0 E8 02                        shr al, 2
0023469A  41 B9 51 0F 00 00               mov r9d, 0xf51
002346A0  88 45 F7                        mov byte ptr [rbp - 9], al
002346A3  BA 01 00 00 00                  mov edx, 1
002346A8  48 8D 45 DF                     lea rax, [rbp - 0x21]
002346AC  48 C7 45 D7 20 00 00 00         mov qword ptr [rbp - 0x29], 0x20
002346B4  41 B8 00 00 02 40               mov r8d, 0x40020000
002346BA  48 89 45 CF                     mov qword ptr [rbp - 0x31], rax
002346BE  C7 44 24 20 02 06 00 00         mov dword ptr [rsp + 0x20], 0x602
002346C6  E8 85 0C 00 00                  call 0x140235350
002346CB  E9 F2 FB FF FF                  jmp 0x1402342c2
002346D0  4C 89 7D EF                     mov qword ptr [rbp - 0x11], r15
002346D4  EB AD                           jmp 0x140234683
002346D6  E8 F5 A6 14 00                  call 0x14037edd0
002346DB  48 89 45 B7                     mov qword ptr [rbp - 0x49], rax
002346DF  33 C0                           xor eax, eax
002346E1  E9 FF FC FF FF                  jmp 0x1402343e5
002346E6  E8 49 FA 16 00                  call 0x1403a4134
002346EB  E9 16 FD FF FF                  jmp 0x140234406
002346F0  4C 8B E1                        mov r12, rcx
002346F3  E9 CF FB FF FF                  jmp 0x1402342c7
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiProcessExpiredTimerList(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m5F;
    unsigned __int64 v_stack_m60;
    unsigned __int8 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned int v_stack_mBC;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned int v_stack_mE4;
    unsigned __int64 v_stack_mF0;
    unsigned int v_stack_mF8;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p28;
    unsigned __int64 v_stack_p38;
    unsigned int v_stack_p40;
    unsigned int v_stack_p44;
    unsigned int v_stack_p48;

    v_stack_p20 = v_rbx;
    v_rsp = (v_rsp) - (240);
    result = (*(unsigned __int64 *)(v_rip + 12412189)) ^ (v_rsp);
    v_stack_m40 = result;
    v_r15 = 0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 14231764))) & (128));
    v_stack_mBC = a4;
    v_r14 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 14231758))) & (0x20000ULL));
    v_stack_mD0 = a3;
    v_stack_mF8 = (unsigned int)(v_r14);
    v_stack_mF0 = a2;
    v_stack_mD8 = 0;
    v_stack_m80 = v_xmm0;
    v_stack_mE4 = (unsigned int)(result);
    v_stack_m70 = v_xmm0;
    v_stack_mC8 = *(unsigned __int64 *)(a1 + 8);
    v_stack_mB0 = v_xmm1;
    v_stack_mA0 = v_xmm1;
loc_00234284:
    v_r13 = (unsigned int)((0) + 1);
    if (0 == 0) goto loc_002342D5;
    if (condition_is_below) goto loc_00234510;
loc_002342A4:
    if ((unsigned int)(v_r14) != 0) goto loc_00234650;
    result = KiTimerWaitTest(a1, 0, a2 + 8, a4);
loc_002342C2:
    if (result != 0) goto loc_00234329;
loc_002342C7:
loc_002342D5:
    if (((unsigned int)(v_r13)) < v_stack_mBC) goto loc_00234284;
    *(unsigned __int64 *)(a1 + 14432) = 0;
    if ((*(unsigned __int64 *)(a1 + 11528)) != 0) {
        a4 = 2;
        a3 = 0;
        a1 = a1;
        a2 = a4 - 1;
        result = KiProcessThreadWaitList(a1, a2, a3, a4);
    }
    a1 = (v_stack_m40) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (240);
    return result;
loc_00234329:
    if ((*(unsigned __int64 *)(a1 + 11528)) != 0) {
        a4 = 2;
        a3 = 0;
        a1 = a1;
        a2 = a4 - 1;
        result = KiProcessThreadWaitList(a1, a2, a3, a4);
    }
    if (v_stack_p44 == 0) goto loc_0023440A;
    result = 0;
    v_stack_p40 = 0;
    if (*(unsigned __int64 *)(v_rip + 14268693) == 0) goto loc_002344F0;
    v_stack_p40 = (unsigned int)(a1);
    if (*(unsigned __int64 *)(v_rip + 14268693) == 0) goto loc_002343CB;
loc_00234390:
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 14268693) + 4520))) & ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 14268693) + 4520)) - 1)));
    result = (a1) << (5);
    result = (result) + (0x11CCULL);
    result = (result) + (*(unsigned __int64 *)(v_rip + 14268693));
    if (condition_is_equal) goto loc_002343C0;
    result = (unsigned int)(*(unsigned int *)(result + 4));
    v_rbx = 0;
    if (sign_flag) {
        a1 = *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 14268693) + a1 * 2 + 4505);
        result = 1;
        result = (unsigned int)((result) << ((unsigned __int8)(a1)));
        v_rbx = (unsigned int)((0) | ((unsigned int)(result)));
    }
    if (condition_is_not_equal) goto loc_00234390;
    v_stack_p40 = (unsigned int)(a1);
    result = 0;
loc_002343CB:
    if ((((unsigned __int8)(v_rbx)) & (2)) != 0) goto loc_002344F5;
    v_stack_mB0 = 0;
loc_002343D8:
    if ((((unsigned __int8)(v_rbx)) & (4)) != 0) goto loc_002346D6;
    v_stack_mA8 = 0;
loc_002343E5:
    if ((((unsigned __int8)(v_rbx)) & (8)) == 0) goto loc_002344E7;
    a2 = (a2) << (32);
    result = (result) | (a2);
    v_stack_mA0 = result;
    result = 0;
loc_002343FD:
    if ((((unsigned __int8)(v_rbx)) & (16)) != 0) goto loc_002346E6;
loc_00234406:
    v_stack_m98 = 0;
loc_0023440A:
    v_stack_mD8 = *(unsigned __int64 *)(result + 24);
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p38))) & (15));
    *(unsigned int *)(v_stack_p38) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p38)) + 1);
    *(unsigned __int64 *)(v_stack_p38 + a1 + a1 * 2 * 8 + 16) = *(unsigned __int64 *)(result + 24);
    *(unsigned __int64 *)(v_stack_p38 + a1 + a1 * 2 * 8 + 24) = *(unsigned __int64 *)(a1 + a1 * 2);
    result = 0;
    *(unsigned __int64 *)(v_stack_p38 + a1 + a1 * 2 * 8 + 32) = 0;
    *(unsigned int *)(a1 + 34396) = 0;
    *(unsigned __int8 *)(a1 + 14522) = 1;
    if (v_stack_mD8 == (v_rip + 2452096)) goto loc_00234498;
    if (v_stack_mD8 == (v_rip + 2560075)) goto loc_00234537;
    if (v_stack_mD8 != (v_rip + 2561755)) goto loc_00234544;
    result = PopPepIdleTimeoutDpcRoutine(0, *(unsigned __int64 *)(result + 32), (unsigned int)(*(unsigned int *)((unsigned int)(v_stack_mF8))), (unsigned int)(*(unsigned int *)(v_stack_p38 + 12)));
    goto loc_002344A0;
loc_00234498:
    result = PfSnTraceTimerRoutine(result, *(unsigned __int64 *)(result + 32), (unsigned int)(*(unsigned int *)((unsigned int)(v_stack_mF8))), (unsigned int)(*(unsigned int *)(v_stack_p38 + 12)));
loc_002344A0:
    *(unsigned __int8 *)(a1 + 14522) = 0;
    *(unsigned __int64 *)(v_stack_p38 + a1 + a1 * 2 * 8 + 32) = *(unsigned __int64 *)(result);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 484)))) == ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mC8 + 484))))) goto loc_0023454E;
    v_stack_p20 = (unsigned int)(*(unsigned int *)(v_stack_mC8 + 484));
    result = KeBugCheckEx(199, 5, v_stack_mD8, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 484)));
loc_002344E7:
    v_stack_mA0 = result;
    goto loc_002343FD;
loc_002344F0:
loc_002344F5:
    a1 = 0;
    result = KeQueryPerformanceCounter(a1, 5, v_stack_mD8, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 484)));
    v_stack_mB0 = result;
    result = 0;
    goto loc_002343D8;
loc_00234510:
    v_rsi = (unsigned int)((result) + 1);
    if (((*(unsigned int *)(v_rip + 14224788)) & ((unsigned int)(v_rsi))) == 0) goto loc_00234629;
loc_0023451E:
loc_00234520:
    if (sign_flag) goto loc_00234510;
    if (condition_is_below) goto loc_00234510;
    goto loc_002342A4;
loc_00234537:
    result = PopFxResidentTimeoutDpcRoutine(v_rsi, v_stack_p38, v_stack_mD8, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 484)));
    goto loc_002344A0;
loc_00234544:
    result = guard_dispatch_icall(v_rsi, v_stack_p38, v_stack_mD8, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 484)));
    goto loc_002344A0;
loc_0023454E:
    result = (__int8)(*(unsigned __int8 *)(v_rsi + 562));
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 8) + 562))) != ((unsigned __int8)((__int8)(*(unsigned __int8 *)(v_rsi + 562))))) {
        a2 = v_stack_mD8;
        a3 = (__int8)(*(unsigned __int8 *)(v_rsi + 562));
        a4 = 5;
        v_stack_p20 = 0;
        a1 = 505;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    v_r15 = 0;
    if (v_stack_p44 == 0) goto loc_002346F0;
    v_stack_m48 = 8;
    v_stack_m50 = v_stack_mD8;
    v_stack_p48 = (unsigned int)(a1);
    if (v_stack_p44 == 0) goto loc_00234620;
loc_002345B0:
    v_rbx = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 14230791) + 4520))) & ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 14230791) + 4520)) - 1)));
    result = ((unsigned int)((unsigned int)(a1))) << (5);
    result = (result) + (0x11CCULL);
    result = (result) + (*(unsigned __int64 *)(v_rip + 14230769));
    if (condition_is_equal) goto loc_00234617;
    result = (unsigned int)(*(unsigned int *)(result + 4));
    if (sign_flag) {
        result = *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 14230769) + a1 * 2 + 4505);
        a4 = 2;
        a3 = *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 14230769) + (unsigned int)((unsigned int)(a1)) * 2 + 4504);
        v_stack_p28 = 0x500A02ULL;
        v_stack_m58 = 8;
        a1 = v_stack_m5F + result * 8 - 89;
        v_stack_p20 = 0xF45ULL;
        v_stack_m60 = a1;
        a1 = v_stack_m60;
        result = EtwpLogKernelEvent(a1, *(unsigned __int64 *)(v_rip + 14230769), a3, a4);
    }
    if ((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 4))) != 0) goto loc_002345B0;
    v_stack_p48 = (unsigned int)(a1);
loc_00234620:
    goto loc_002342C7;
loc_00234629:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14230665)))) & (64)) == 0) goto loc_0023451E;
    result = KiCheckVpBackingLongSpinWaitHypercall(a1, *(unsigned __int64 *)(v_rip + 14230769), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0023451E;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rsi)), *(unsigned __int64 *)(v_rip + 14230769), a3, a4);
    goto loc_00234520;
loc_00234650:
    v_stack_m80 = *(unsigned __int64 *)(v_rbx + 24);
    result = (*(unsigned __int64 *)(v_rbx + 48)) ^ (*(unsigned __int64 *)(v_rip + 14231841));
    result = (result) ^ (v_rbx);
    result = (result) ^ (*(unsigned __int64 *)(v_rip + 14232535));
    if (condition_is_equal) goto loc_002346D0;
    v_stack_m70 = *(unsigned __int64 *)(result + 24);
loc_00234683:
    result = KiTimerWaitTest(a1, *(unsigned __int64 *)(v_rip + 14230769), a3, a4);
    v_stack_m78 = v_rbx;
    result = (unsigned __int8)((*(unsigned __int8 *)(v_rbx + 1)) >> (2));
    v_stack_m68 = (unsigned __int8)(result);
    v_stack_m88 = 32;
    v_stack_m90 = v_stack_m80;
    v_stack_p20 = 0x602ULL;
    result = EtwTraceKernelEvent(v_stack_m90, 1, (unsigned int)(0x40020000ULL), (unsigned int)(0xF51ULL));
    goto loc_002342C2;
loc_002346D0:
    v_stack_m70 = 0;
    goto loc_00234683;
loc_002346D6:
    result = RtlGetSystemTimePrecise(v_stack_m90, 1, (unsigned int)(0x40020000ULL), (unsigned int)(0xF51ULL));
    v_stack_mA8 = result;
    result = 0;
    goto loc_002343E5;
loc_002346E6:
    result = EtwpGetHostPerfCounter(v_stack_m90, 1, (unsigned int)(0x40020000ULL), (unsigned int)(0xF51ULL));
    goto loc_00234406;
loc_002346F0:
    goto loc_002342C7;
}
```

## 5. (Beta) C Style

```c
int64_t KiProcessExpiredTimerList(void *Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m5F;
    uint64_t v_stack_m60;
    uint8_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint32_t v_stack_mBC;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint32_t v_stack_mE4;
    uint64_t v_stack_mF0;
    uint32_t v_stack_mF8;
    uint64_t v_stack_p20;
    uint32_t v_stack_p28;
    uint64_t v_stack_p38;
    uint32_t v_stack_p40;
    uint32_t v_stack_p44;
    uint32_t v_stack_p48;

    v_stack_p20 = local_rbx;
    local_rsp = (local_rsp) - (240);
    result = (*(uint64_t *)(v_rip + 0xBD651D)) ^ (local_rsp);
    v_stack_m40 = result;
    local_r15 = 0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xD928D4))) & (128));
    v_stack_mBC = Arg4;
    local_r14 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xD928CE))) & (0x20000ULL));
    v_stack_mD0 = Arg3;
    v_stack_mF8 = (uint32_t)(local_r14);
    v_stack_mF0 = Arg2;
    v_stack_mD8 = 0;
    v_stack_m80 = v_xmm0;
    v_stack_mE4 = (uint32_t)(result);
    v_stack_m70 = v_xmm0;
    v_stack_mC8 = *(uint64_t *)(arg1 + 0x8);
    v_stack_mB0 = v_xmm1;
    v_stack_mA0 = v_xmm1;
loc_00234284:
    local_r13 = (uint32_t)((0) + 1);
    if (0 == 0) goto loc_002342D5;
    if (condition_is_below) goto loc_00234510;
loc_002342A4:
    if ((uint32_t)(local_r14) != 0) goto loc_00234650;
    result = KiTimerWaitTest(Arg1, 0, Arg2 + 8, Arg4);
loc_002342C2:
    if (result != 0) goto loc_00234329;
loc_002342C7:
loc_002342D5:
    if (((uint32_t)(local_r13)) < v_stack_mBC) goto loc_00234284;
    *(uint64_t *)(arg1 + 0x3860) = 0;
    if ((*(uint64_t *)(arg1 + 0x2D08)) != 0) {
        Arg4 = 2;
        Arg3 = 0;
        Arg1 = Arg1;
        Arg2 = Arg4 - 1;
        result = KiProcessThreadWaitList(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (v_stack_m40) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (240);
    return result;
loc_00234329:
    if ((*(uint64_t *)(arg1 + 0x2D08)) != 0) {
        Arg4 = 2;
        Arg3 = 0;
        Arg1 = Arg1;
        Arg2 = Arg4 - 1;
        result = KiProcessThreadWaitList(Arg1, Arg2, Arg3, Arg4);
    }
    if (v_stack_p44 == 0) goto loc_0023440A;
    result = 0;
    v_stack_p40 = 0;
    if (*(uint64_t *)(v_rip + 0xD9B915) == 0) goto loc_002344F0;
    v_stack_p40 = (uint32_t)(Arg1);
    if (*(uint64_t *)(v_rip + 0xD9B915) == 0) goto loc_002343CB;
loc_00234390:
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xD9B915) + 0x11A8))) & ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xD9B915) + 0x11A8)) - 1)));
    result = (Arg1) << (5);
    result = (result) + (0x11CCULL);
    result = (result) + (*(uint64_t *)(v_rip + 0xD9B915));
    if (condition_is_equal) goto loc_002343C0;
    result = (uint32_t)(*(uint32_t *)(result + 0x4));
    local_rbx = 0;
    if (sign_flag) {
        Arg1 = *(uint8_t *)(*(uint64_t *)(v_rip + 0xD9B915) + arg1 * 2 + 0x1199);
        result = 1;
        result = (uint32_t)((result) << ((uint8_t)(Arg1)));
        local_rbx = (uint32_t)((0) | ((uint32_t)(result)));
    }
    if (condition_is_not_equal) goto loc_00234390;
    v_stack_p40 = (uint32_t)(Arg1);
    result = 0;
loc_002343CB:
    if ((((uint8_t)(local_rbx)) & (2)) != 0) goto loc_002344F5;
    v_stack_mB0 = 0;
loc_002343D8:
    if ((((uint8_t)(local_rbx)) & (4)) != 0) goto loc_002346D6;
    v_stack_mA8 = 0;
loc_002343E5:
    if ((((uint8_t)(local_rbx)) & (8)) == 0) goto loc_002344E7;
    Arg2 = (Arg2) << (32);
    result = (result) | (Arg2);
    v_stack_mA0 = result;
    result = 0;
loc_002343FD:
    if ((((uint8_t)(local_rbx)) & (16)) != 0) goto loc_002346E6;
loc_00234406:
    v_stack_m98 = 0;
loc_0023440A:
    v_stack_mD8 = *(uint64_t *)(result + 0x18);
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p38))) & (15));
    *(uint32_t *)(v_stack_p38) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p38)) + 1);
    *(uint64_t *)(v_stack_p38 + arg1 + arg1 * 2 * 8 + 0x10) = *(uint64_t *)(result + 0x18);
    *(uint64_t *)(v_stack_p38 + arg1 + arg1 * 2 * 8 + 0x18) = *(uint64_t *)(arg1 + arg1 * 2);
    result = 0;
    *(uint64_t *)(v_stack_p38 + arg1 + arg1 * 2 * 8 + 0x20) = 0;
    *(uint32_t *)(arg1 + 0x865C) = 0;
    *(uint8_t *)(arg1 + 0x38BA) = 1;
    if (v_stack_mD8 == (v_rip + 2452096)) goto loc_00234498;
    if (v_stack_mD8 == (v_rip + 2560075)) goto loc_00234537;
    if (v_stack_mD8 != (v_rip + 2561755)) goto loc_00234544;
    result = PopPepIdleTimeoutDpcRoutine(0, *(uint64_t *)(result + 0x20), (uint32_t)(*(uint32_t *)((uint32_t)(v_stack_mF8))), (uint32_t)(*(uint32_t *)(v_stack_p38 + 0xC)));
    goto loc_002344A0;
loc_00234498:
    result = PfSnTraceTimerRoutine(result, *(uint64_t *)(result + 0x20), (uint32_t)(*(uint32_t *)((uint32_t)(v_stack_mF8))), (uint32_t)(*(uint32_t *)(v_stack_p38 + 0xC)));
loc_002344A0:
    *(uint8_t *)(arg1 + 0x38BA) = 0;
    *(uint64_t *)(v_stack_p38 + arg1 + arg1 * 2 * 8 + 0x20) = *(uint64_t *)(result);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x1E4)))) == ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mC8 + 0x1E4))))) goto loc_0023454E;
    v_stack_p20 = (uint32_t)(*(uint32_t *)(v_stack_mC8 + 0x1E4));
    result = KeBugCheckEx(199, 5, v_stack_mD8, (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x1E4)));
loc_002344E7:
    v_stack_mA0 = result;
    goto loc_002343FD;
loc_002344F0:
loc_002344F5:
    Arg1 = 0;
    result = KeQueryPerformanceCounter(Arg1, 5, v_stack_mD8, (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x1E4)));
    v_stack_mB0 = result;
    result = 0;
    goto loc_002343D8;
loc_00234510:
    local_rsi = (uint32_t)((result) + 1);
    if (((*(uint32_t *)(v_rip + 0xD90D94)) & ((uint32_t)(local_rsi))) == 0) goto loc_00234629;
loc_0023451E:
loc_00234520:
    if (sign_flag) goto loc_00234510;
    if (condition_is_below) goto loc_00234510;
    goto loc_002342A4;
loc_00234537:
    result = PopFxResidentTimeoutDpcRoutine(local_rsi, v_stack_p38, v_stack_mD8, (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x1E4)));
    goto loc_002344A0;
loc_00234544:
    result = guard_dispatch_icall(local_rsi, v_stack_p38, v_stack_mD8, (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x1E4)));
    goto loc_002344A0;
loc_0023454E:
    result = (int8_t)(*(uint8_t *)(local_rsi + 0x232));
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x8) + 0x232))) != ((uint8_t)((int8_t)(*(uint8_t *)(local_rsi + 0x232))))) {
        Arg2 = v_stack_mD8;
        Arg3 = (int8_t)(*(uint8_t *)(local_rsi + 0x232));
        Arg4 = 5;
        v_stack_p20 = 0;
        Arg1 = 505;
        result = KeBugCheckEx(Arg1, Arg2, Arg3, Arg4);
    }
    local_r15 = 0;
    if (v_stack_p44 == 0) goto loc_002346F0;
    v_stack_m48 = 8;
    v_stack_m50 = v_stack_mD8;
    v_stack_p48 = (uint32_t)(Arg1);
    if (v_stack_p44 == 0) goto loc_00234620;
loc_002345B0:
    local_rbx = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xD92507) + 0x11A8))) & ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xD92507) + 0x11A8)) - 1)));
    result = ((uint32_t)((uint32_t)(Arg1))) << (5);
    result = (result) + (0x11CCULL);
    result = (result) + (*(uint64_t *)(v_rip + 0xD924F1));
    if (condition_is_equal) goto loc_00234617;
    result = (uint32_t)(*(uint32_t *)(result + 0x4));
    if (sign_flag) {
        result = *(uint8_t *)(*(uint64_t *)(v_rip + 0xD924F1) + arg1 * 2 + 0x1199);
        Arg4 = 2;
        Arg3 = *(uint8_t *)(*(uint64_t *)(v_rip + 0xD924F1) + (uint32_t)((uint32_t)(arg1)) * 2 + 0x1198);
        v_stack_p28 = 0x500A02ULL;
        v_stack_m58 = 8;
        Arg1 = v_stack_m5F + result * 8 - 89;
        v_stack_p20 = 0xF45ULL;
        v_stack_m60 = Arg1;
        Arg1 = v_stack_m60;
        result = EtwpLogKernelEvent(Arg1, *(uint64_t *)(v_rip + 0xD924F1), Arg3, Arg4);
    }
    if ((uint8_t)((uint32_t)(*(uint32_t *)(result + 0x4))) != 0) goto loc_002345B0;
    v_stack_p48 = (uint32_t)(Arg1);
loc_00234620:
    goto loc_002342C7;
loc_00234629:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD92489)))) & (64)) == 0) goto loc_0023451E;
    result = KiCheckVpBackingLongSpinWaitHypercall(Arg1, *(uint64_t *)(v_rip + 0xD924F1), Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0023451E;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rsi)), *(uint64_t *)(v_rip + 0xD924F1), Arg3, Arg4);
    goto loc_00234520;
loc_00234650:
    v_stack_m80 = *(uint64_t *)(local_rbx + 0x18);
    result = (*(uint64_t *)(local_rbx + 0x30)) ^ (*(uint64_t *)(v_rip + 0xD92921));
    result = (result) ^ (local_rbx);
    result = (result) ^ (*(uint64_t *)(v_rip + 0xD92BD7));
    if (condition_is_equal) goto loc_002346D0;
    v_stack_m70 = *(uint64_t *)(result + 0x18);
loc_00234683:
    result = KiTimerWaitTest(Arg1, *(uint64_t *)(v_rip + 0xD924F1), Arg3, Arg4);
    v_stack_m78 = local_rbx;
    result = (uint8_t)((*(uint8_t *)(local_rbx + 0x1)) >> (2));
    v_stack_m68 = (uint8_t)(result);
    v_stack_m88 = 32;
    v_stack_m90 = v_stack_m80;
    v_stack_p20 = 0x602ULL;
    result = EtwTraceKernelEvent(v_stack_m90, 1, (uint32_t)(0x40020000ULL), (uint32_t)(0xF51ULL));
    goto loc_002342C2;
loc_002346D0:
    v_stack_m70 = 0;
    goto loc_00234683;
loc_002346D6:
    result = RtlGetSystemTimePrecise(v_stack_m90, 1, (uint32_t)(0x40020000ULL), (uint32_t)(0xF51ULL));
    v_stack_mA8 = result;
    result = 0;
    goto loc_002343E5;
loc_002346E6:
    result = EtwpGetHostPerfCounter(v_stack_m90, 1, (uint32_t)(0x40020000ULL), (uint32_t)(0xF51ULL));
    goto loc_00234406;
loc_002346F0:
    goto loc_002342C7;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x2D08` | `64` | `R` |
| `Arg1` | `+ 0x3860` | `64` | `W` |
| `Arg1` | `+ 0x38BA` | `8` | `W` |
| `Arg1` | `+ 0x865C` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00234200&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
