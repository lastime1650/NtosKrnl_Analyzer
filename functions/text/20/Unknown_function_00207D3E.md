# sub_00207D3E

- RVA: `0x00207D3E`–`0x0020841E` (길이 `1,760` bytes)
- VA: `0x0000000140207D3E`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D33C`
- 디코드: `383`개 명령, `1,760/1,760` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **12**; 고유 호출 대상: **11**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **11**

### Outgoing calls
- `0x00207DA3` → [KiAcquireSpinLockInstrumented](KiAcquireSpinLockInstrumented_function_002084F0.md) (function, `0x002084F0`)
- `0x00207E1F` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x00207E6A` → [KxWaitForSpinLockAndAcquire](KxWaitForSpinLockAndAcquire_function_002085C0.md) (function, `0x002085C0`)
- `0x002080EF` → [RtlBackoff](RtlBackoff_function_00208620.md) (function, `0x00208620`)
- `0x00208157` → [HalpDisableInterrupts](../25/HalpDisableInterrupts_function_002521A0.md) (function, `0x002521A0`)
- `0x002081FC` → [HalpInterruptSendIpi](../25/HalpInterruptSendIpi_function_00252310.md) (function, `0x00252310`)
- `0x00208222` → [KiSetDpcRequestFlag](../39/KiSetDpcRequestFlag_function_0039DC50.md) (function, `0x0039DC50`)
- `0x0020828C` → [KiReleaseSpinLockInstrumented](../39/KiReleaseSpinLockInstrumented_function_00392EF0.md) (function, `0x00392EF0`)
- `0x002082A4` → [KiSetDpcRequestFlag](../39/KiSetDpcRequestFlag_function_0039DC50.md) (function, `0x0039DC50`)
- `0x00208351` → [EtwTraceXSchedulerPriorityKickSend](../4F/EtwTraceXSchedulerPriorityKickSend_function_004FB2C0.md) (function, `0x004FB2C0`)
- `0x00208373` → [KiCpuPartitionCheckDpcEnqueue](../4F/KiCpuPartitionCheckDpcEnqueue_function_004FCB88.md) (function, `0x004FCB88`)
- `0x002083E1` → [EtwTraceDpcEnqueueEvent](../4F/EtwTraceDpcEnqueueEvent_function_004FBC30.md) (function, `0x004FBC30`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00207D84` → RVA `0x00FC6B06` (`ALMOSTRO`; read)
- `0x00207D91` → RVA `0x00F0DE58` (`.data`; read)
- `0x00207E0E` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x00208030` → RVA `0x00FC6FF8` (`ALMOSTRO`; read)
- `0x00208060` → RVA `0x00FC6B14` (`ALMOSTRO`; read)
- `0x00208140` → RVA `0x00FC6BC5` (`ALMOSTRO`; read)
- `0x002081C0` → RVA `0x00FC504C` (`ALMOSTRO`; read)
- `0x0020830B` → RVA `0x00FC5007` (`ALMOSTRO`; read)
- `0x00208323` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x00208390` → RVA `0x00FC6F78` (`ALMOSTRO`; read)
- `0x0020839A` → RVA `0x00FC7250` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00207D3E  41 8B 6D 24                     mov ebp, dword ptr [r13 + 0x24]
00207D42  49 8B FD                        mov rdi, r13
00207D45  66 3B F5                        cmp si, bp
00207D48  0F 95 C2                        setne dl
00207D4B  88 94 24 F0 00 00 00            mov byte ptr [rsp + 0xf0], dl
00207D52  48 8B 87 C8 00 00 00            mov rax, qword ptr [rdi + 0xc8]
00207D59  4C 89 B4 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], r14
00207D61  48 85 43 10                     test qword ptr [rbx + 0x10], rax
00207D65  75 0D                           jne 0x140207d74
00207D67  0F B6 87 D1 00 00 00            movzx eax, byte ptr [rdi + 0xd1]
00207D6E  F0 48 0F AB 43 10               lock bts qword ptr [rbx + 0x10], rax
00207D74  80 3B 1A                        cmp byte ptr [rbx], 0x1a
00207D77  0F 84 54 05 00 00               je 0x1402082d1
00207D7D  48 8D B7 40 38 00 00            lea rsi, [rdi + 0x3840]
00207D84  F6 05 7B ED DB 00 21            test byte ptr [rip + 0xdbed7b], 0x21
00207D8B  0F 84 C8 00 00 00               je 0x140207e59
00207D91  8B 05 C1 60 D0 00               mov eax, dword ptr [rip + 0xd060c1]
00207D97  85 C0                           test eax, eax
00207D99  0F 85 BA 00 00 00               jne 0x140207e59
00207D9F  48 8D 4E 10                     lea rcx, [rsi + 0x10]
00207DA3  E8 48 07 00 00                  call 0x1402084f0
00207DA8  0F B6 94 24 F0 00 00 00         movzx edx, byte ptr [rsp + 0xf0]
00207DB0  41 3B 6D 24                     cmp ebp, dword ptr [r13 + 0x24]
00207DB4  B8 01 00 00 00                  mov eax, 1
00207DB9  49 8B 8D 90 2D 00 00            mov rcx, qword ptr [r13 + 0x2d90]
00207DC0  48 0F 45 C8                     cmovne rcx, rax
00207DC4  33 C0                           xor eax, eax
00207DC6  F0 48 0F B1 4B 38               lock cmpxchg qword ptr [rbx + 0x38], rcx
00207DCC  0F 84 A2 00 00 00               je 0x140207e74
00207DD2  4D 85 FF                        test r15, r15
00207DD5  74 15                           je 0x140207dec
00207DD7  0F B6 84 24 10 01 00 00         movzx eax, byte ptr [rsp + 0x110]
00207DDF  C1 E0 18                        shl eax, 0x18
00207DE2  0F BA E8 07                     bts eax, 7
00207DE6  F7 D0                           not eax
00207DE8  F0 41 21 07                     lock and dword ptr [r15], eax
00207DEC  F6 05 13 ED DB 00 01            test byte ptr [rip + 0xdbed13], 1
00207DF3  0F 85 79 04 00 00               jne 0x140208272
00207DF9  F0 48 83 66 10 00               lock and qword ptr [rsi + 0x10], 0
00207DFF  44 0F B6 74 24 40               movzx r14d, byte ptr [rsp + 0x40]
00207E05  45 84 F6                        test r14b, r14b
00207E08  0F 85 47 02 00 00               jne 0x140208055
00207E0E  83 3D 0B EF DB 00 00            cmp dword ptr [rip + 0xdbef0b], 0
00207E15  74 0D                           je 0x140207e24
00207E17  44 0F 20 C1                     mov rcx, cr8
00207E1B  41 0F B6 D4                     movzx edx, r12b
00207E1F  E8 74 D8 2E 00                  call 0x1404f5698
00207E24  41 0F B6 CC                     movzx ecx, r12b
00207E28  44 0F 22 C1                     mov cr8, rcx
00207E2C  48 8B BC 24 B8 00 00 00         mov rdi, qword ptr [rsp + 0xb8]
00207E34  41 0F B6 C6                     movzx eax, r14b
00207E38  4C 8B B4 24 B0 00 00 00         mov r14, qword ptr [rsp + 0xb0]
00207E40  48 8B AC 24 08 01 00 00         mov rbp, qword ptr [rsp + 0x108]
00207E48  48 81 C4 C0 00 00 00            add rsp, 0xc0
00207E4F  41 5F                           pop r15
00207E51  41 5D                           pop r13
00207E53  41 5C                           pop r12
00207E55  5E                              pop rsi
00207E56  5B                              pop rbx
00207E57  C3                              ret
00207E58  CC                              int3
00207E59  F0 48 0F BA 6E 10 00            lock bts qword ptr [rsi + 0x10], 0
00207E60  0F 83 4A FF FF FF               jae 0x140207db0
00207E66  48 8D 4E 10                     lea rcx, [rsi + 0x10]
00207E6A  E8 51 07 00 00                  call 0x1402085c0
00207E6F  E9 34 FF FF FF                  jmp 0x140207da8
00207E74  44 8B 46 18                     mov r8d, dword ptr [rsi + 0x18]
00207E78  44 89 44 24 44                  mov dword ptr [rsp + 0x44], r8d
00207E7D  41 8D 40 01                     lea eax, [r8 + 1]
00207E81  89 46 18                        mov dword ptr [rsi + 0x18], eax
00207E84  FF 46 1C                        inc dword ptr [rsi + 0x1c]
00207E87  83 7C 24 48 00                  cmp dword ptr [rsp + 0x48], 0
00207E8C  48 8B 84 24 F8 00 00 00         mov rax, qword ptr [rsp + 0xf8]
00207E94  48 89 43 28                     mov qword ptr [rbx + 0x28], rax
00207E98  48 8B 84 24 00 01 00 00         mov rax, qword ptr [rsp + 0x100]
00207EA0  48 89 43 30                     mov qword ptr [rbx + 0x30], rax
00207EA4  0F 85 D3 04 00 00               jne 0x14020837d
00207EAA  80 7B 01 02                     cmp byte ptr [rbx + 1], 2
00207EAE  48 8D 4B 08                     lea rcx, [rbx + 8]
00207EB2  C6 44 24 40 01                  mov byte ptr [rsp + 0x40], 1
00207EB7  0F 84 8F 03 00 00               je 0x14020824c
00207EBD  48 C7 01 00 00 00 00            mov qword ptr [rcx], 0
00207EC4  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
00207EC8  48 89 08                        mov qword ptr [rax], rcx
00207ECB  48 89 4E 08                     mov qword ptr [rsi + 8], rcx
00207ECF  84 D2                           test dl, dl
00207ED1  74 04                           je 0x140207ed7
00207ED3  66 89 6B 02                     mov word ptr [rbx + 2], bp
00207ED7  48 8B 8F B8 8E 00 00            mov rcx, qword ptr [rdi + 0x8eb8]
00207EDE  48 85 C9                        test rcx, rcx
00207EE1  0F 85 04 05 00 00               jne 0x1402083eb
00207EE7  48 8D 87 40 38 00 00            lea rax, [rdi + 0x3840]
00207EEE  48 3B F0                        cmp rsi, rax
00207EF1  0F 85 DB FE FF FF               jne 0x140207dd2
00207EF7  4C 8B 8F 10 38 00 00            mov r9, qword ptr [rdi + 0x3810]
00207EFE  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
00207F02  4D 85 C9                        test r9, r9
00207F05  0F 84 C7 FE FF FF               je 0x140207dd2
00207F0B  45 8B 59 04                     mov r11d, dword ptr [r9 + 4]
00207F0F  49 C7 C2 FF FF FF FF            mov r10, 0xffffffffffffffff
00207F16  41 8B CB                        mov ecx, r11d
00207F19  41 C1 EB 05                     shr r11d, 5
00207F1D  83 E1 1F                        and ecx, 0x1f
00207F20  49 D3 E2                        shl r10, cl
00207F23  4D 8B C2                        mov r8, r10
00207F26  4C 23 C0                        and r8, rax
00207F29  49 8B C0                        mov rax, r8
00207F2C  49 8B D0                        mov rdx, r8
00207F2F  48 C1 E8 38                     shr rax, 0x38
00207F33  48 89 84 24 98 00 00 00         mov qword ptr [rsp + 0x98], rax
00207F3B  49 8B C0                        mov rax, r8
00207F3E  48 C1 E8 30                     shr rax, 0x30
00207F42  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
00207F4A  49 8B C0                        mov rax, r8
00207F4D  48 C1 E8 28                     shr rax, 0x28
00207F51  48 89 84 24 88 00 00 00         mov qword ptr [rsp + 0x88], rax
00207F59  49 8B C0                        mov rax, r8
00207F5C  48 C1 E8 20                     shr rax, 0x20
00207F60  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
00207F68  49 8B C0                        mov rax, r8
00207F6B  48 C1 E8 18                     shr rax, 0x18
00207F6F  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
00207F74  49 8B C0                        mov rax, r8
00207F77  48 C1 E8 10                     shr rax, 0x10
00207F7B  48 C1 EA 08                     shr rdx, 8
00207F7F  48 89 84 24 F0 00 00 00         mov qword ptr [rsp + 0xf0], rax
00207F87  45 85 DB                        test r11d, r11d
00207F8A  0F 84 42 FE FF FF               je 0x140207dd2
00207F90  41 0F B6 C0                     movzx eax, r8b
00207F94  48 05 CB 5D B1 00               add rax, 0xb15dcb
00207F9A  4C 89 84 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], r8
00207FA2  48 6B C8 25                     imul rcx, rax, 0x25
00207FA6  0F B6 C2                        movzx eax, dl
00207FA9  48 03 C8                        add rcx, rax
00207FAC  0F B6 84 24 F0 00 00 00         movzx eax, byte ptr [rsp + 0xf0]
00207FB4  48 6B D1 25                     imul rdx, rcx, 0x25
00207FB8  48 03 D0                        add rdx, rax
00207FBB  0F B6 44 24 78                  movzx eax, byte ptr [rsp + 0x78]
00207FC0  48 6B CA 25                     imul rcx, rdx, 0x25
00207FC4  48 03 C8                        add rcx, rax
00207FC7  0F B6 84 24 80 00 00 00         movzx eax, byte ptr [rsp + 0x80]
00207FCF  48 6B D1 25                     imul rdx, rcx, 0x25
00207FD3  48 03 D0                        add rdx, rax
00207FD6  0F B6 84 24 88 00 00 00         movzx eax, byte ptr [rsp + 0x88]
00207FDE  48 6B CA 25                     imul rcx, rdx, 0x25
00207FE2  48 03 C8                        add rcx, rax
00207FE5  0F B6 84 24 90 00 00 00         movzx eax, byte ptr [rsp + 0x90]
00207FED  48 6B D1 25                     imul rdx, rcx, 0x25
00207FF1  48 03 D0                        add rdx, rax
00207FF4  48 6B C2 25                     imul rax, rdx, 0x25
00207FF8  41 8D 53 FF                     lea edx, [r11 - 1]
00207FFC  48 03 84 24 98 00 00 00         add rax, qword ptr [rsp + 0x98]
00208004  8B C0                           mov eax, eax
00208006  48 23 D0                        and rdx, rax
00208009  49 8B 41 08                     mov rax, qword ptr [r9 + 8]
0020800D  4C 8D 0C D0                     lea r9, [rax + rdx*8]
00208011  49 8B 09                        mov rcx, qword ptr [r9]
00208014  4C 8B C9                        mov r9, rcx
00208017  F6 C1 01                        test cl, 1
0020801A  0F 85 B2 FD FF FF               jne 0x140207dd2
00208020  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
00208024  49 23 C2                        and rax, r10
00208027  4C 3B C0                        cmp r8, rax
0020802A  75 E5                           jne 0x140208011
0020802C  48 8B 49 10                     mov rcx, qword ptr [rcx + 0x10]
00208030  8B 05 C2 EF DB 00               mov eax, dword ptr [rip + 0xdbefc2]
00208036  48 89 4C 24 58                  mov qword ptr [rsp + 0x58], rcx
0020803B  48 3B C8                        cmp rcx, rax
0020803E  0F 86 8E FD FF FF               jbe 0x140207dd2
00208044  C7 46 28 01 00 00 00            mov dword ptr [rsi + 0x28], 1
0020804B  48 89 4C 24 58                  mov qword ptr [rsp + 0x58], rcx
00208050  E9 7D FD FF FF                  jmp 0x140207dd2
00208055  83 7C 24 48 00                  cmp dword ptr [rsp + 0x48], 0
0020805A  0F 85 30 03 00 00               jne 0x140208390
00208060  F7 05 AA EA DB 00 00 02 00 00   test dword ptr [rip + 0xdbeaaa], 0x200
0020806A  0F 85 FA 02 00 00               jne 0x14020836a
00208070  48 8D 87 70 38 00 00            lea rax, [rdi + 0x3870]
00208077  48 3B F0                        cmp rsi, rax
0020807A  0F 84 16 02 00 00               je 0x140208296
00208080  8B 46 18                        mov eax, dword ptr [rsi + 0x18]
00208083  3B 87 A8 38 00 00               cmp eax, dword ptr [rdi + 0x38a8]
00208089  7D 15                           jge 0x1402080a0
0020808B  0F B6 43 01                     movzx eax, byte ptr [rbx + 1]
0020808F  4C 3B EF                        cmp r13, rdi
00208092  0F 85 6E 01 00 00               jne 0x140208206
00208098  84 C0                           test al, al
0020809A  0F 84 1A 02 00 00               je 0x1402082ba
002080A0  BB 02 00 00 00                  mov ebx, 2
002080A5  44 0F B7 CB                     movzx r9d, bx
002080A9  41 BA AF 00 00 00               mov r10d, 0xaf
002080AF  49 3B FD                        cmp rdi, r13
002080B2  75 0B                           jne 0x1402080bf
002080B4  41 BA A9 00 00 00               mov r10d, 0xa9
002080BA  66 41 83 C9 20                  or r9w, 0x20
002080BF  C7 44 24 50 00 00 00 00         mov dword ptr [rsp + 0x50], 0
002080C7  0F 0D 8F BC 38 00 00            prefetchw byte ptr [rdi + 0x38bc]
002080CE  0F B7 97 BC 38 00 00            movzx edx, word ptr [rdi + 0x38bc]
002080D5  0F B7 CA                        movzx ecx, dx
002080D8  0F B7 C2                        movzx eax, dx
002080DB  66 41 0B C9                     or cx, r9w
002080DF  66 F0 0F B1 8F BC 38 00 00      lock cmpxchg word ptr [rdi + 0x38bc], cx
002080E8  74 2D                           je 0x140208117
002080EA  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
002080EF  E8 2C 05 00 00                  call 0x140208620
002080F4  0F 0D 8F BC 38 00 00            prefetchw byte ptr [rdi + 0x38bc]
002080FB  0F B7 97 BC 38 00 00            movzx edx, word ptr [rdi + 0x38bc]
00208102  0F B7 CA                        movzx ecx, dx
00208105  0F B7 C2                        movzx eax, dx
00208108  66 41 0B C9                     or cx, r9w
0020810C  66 F0 0F B1 8F BC 38 00 00      lock cmpxchg word ptr [rdi + 0x38bc], cx
00208115  75 D3                           jne 0x1402080ea
00208117  66 41 85 D2                     test r10w, dx
0020811B  0F 85 ED FC FF FF               jne 0x140207e0e
00208121  49 3B FD                        cmp rdi, r13
00208124  0F 85 81 00 00 00               jne 0x1402081ab
0020812A  41 80 7D 20 00                  cmp byte ptr [r13 + 0x20], 0
0020812F  74 0A                           je 0x14020813b
00208131  41 C6 45 06 01                  mov byte ptr [r13 + 6], 1
00208136  E9 D3 FC FF FF                  jmp 0x140207e0e
0020813B  33 C0                           xor eax, eax
0020813D  0F 57 C0                        xorps xmm0, xmm0
00208140  38 05 7F EA DB 00               cmp byte ptr [rip + 0xdbea7f], al
00208146  F3 0F 7F 44 24 64               movdqu xmmword ptr [rsp + 0x64], xmm0
0020814C  74 53                           je 0x1402081a1
0020814E  65 4C 8B 04 25 20 00 00 00      mov r8, qword ptr gs:[0x20]
00208157  E8 44 A0 04 00                  call 0x1402521a0
0020815C  41 8B 90 A8 00 00 00            mov edx, dword ptr [r8 + 0xa8]
00208163  44 0F B6 C8                     movzx r9d, al
00208167  8B CA                           mov ecx, edx
00208169  83 C9 04                        or ecx, 4
0020816C  41 89 88 A8 00 00 00            mov dword ptr [r8 + 0xa8], ecx
00208173  85 D2                           test edx, edx
00208175  75 24                           jne 0x14020819b
00208177  B9 15 00 01 C0                  mov ecx, 0xc0010015
0020817C  0F 32                           rdmsr
0020817E  48 C1 E2 20                     shl rdx, 0x20
00208182  48 0B C2                        or rax, rdx
00208185  48 BA 00 00 00 00 01 00 00 00   movabs rdx, 0x100000000
0020818F  48 0B C2                        or rax, rdx
00208192  48 8B D0                        mov rdx, rax
00208195  48 C1 EA 20                     shr rdx, 0x20
00208199  0F 30                           wrmsr
0020819B  45 84 C9                        test r9b, r9b
0020819E  74 01                           je 0x1402081a1
002081A0  FB                              sti
002081A1  C7 44 24 60 05 00 00 00         mov dword ptr [rsp + 0x60], 5
002081A9  EB 47                           jmp 0x1402081f2
002081AB  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
002081AF  48 3B 47 18                     cmp rax, qword ptr [rdi + 0x18]
002081B3  0F 84 AA 00 00 00               je 0x140208263
002081B9  48 8B 87 B8 8E 00 00            mov rax, qword ptr [rdi + 0x8eb8]
002081C0  8B 0D 86 CE DB 00               mov ecx, dword ptr [rip + 0xdbce86]
002081C6  48 85 C0                        test rax, rax
002081C9  0F 85 1B 01 00 00               jne 0x1402082ea
002081CF  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
002081D8  48 C7 44 24 60 06 00 00 00      mov qword ptr [rsp + 0x60], 6
002081E1  89 6C 24 68                     mov dword ptr [rsp + 0x68], ebp
002081E5  FF 80 D4 8E 00 00               inc dword ptr [rax + 0x8ed4]
002081EB  33 C0                           xor eax, eax
002081ED  48 89 44 24 6C                  mov qword ptr [rsp + 0x6c], rax
002081F2  BA 2F 00 00 00                  mov edx, 0x2f
002081F7  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
002081FC  E8 0F A1 04 00                  call 0x140252310
00208201  E9 08 FC FF FF                  jmp 0x140207e0e
00208206  3C 03                           cmp al, 3
00208208  0F 84 92 FE FF FF               je 0x1402080a0
0020820E  3C 02                           cmp al, 2
00208210  0F 84 8A FE FF FF               je 0x1402080a0
00208216  BA 10 00 00 00                  mov edx, 0x10
0020821B  48 8D 8F BC 38 00 00            lea rcx, [rdi + 0x38bc]
00208222  E8 29 5A 19 00                  call 0x14039dc50
00208227  A8 AF                           test al, 0xaf
00208229  0F 85 DF FB FF FF               jne 0x140207e0e
0020822F  48 8B 87 C0 00 00 00            mov rax, qword ptr [rdi + 0xc0]
00208236  48 8B 48 40                     mov rcx, qword ptr [rax + 0x40]
0020823A  48 85 8F C8 00 00 00            test qword ptr [rdi + 0xc8], rcx
00208241  0F 85 59 FE FF FF               jne 0x1402080a0
00208247  E9 C2 FB FF FF                  jmp 0x140207e0e
0020824C  48 8B 06                        mov rax, qword ptr [rsi]
0020824F  48 85 C0                        test rax, rax
00208252  75 04                           jne 0x140208258
00208254  48 89 4E 08                     mov qword ptr [rsi + 8], rcx
00208258  48 89 01                        mov qword ptr [rcx], rax
0020825B  48 89 0E                        mov qword ptr [rsi], rcx
0020825E  E9 6C FC FF FF                  jmp 0x140207ecf
00208263  80 7F 07 00                     cmp byte ptr [rdi + 7], 0
00208267  0F 84 A1 FB FF FF               je 0x140207e0e
0020826D  E9 47 FF FF FF                  jmp 0x1402081b9
00208272  8B 05 E0 5B D0 00               mov eax, dword ptr [rip + 0xd05be0]
00208278  85 C0                           test eax, eax
0020827A  0F 85 79 FB FF FF               jne 0x140207df9
00208280  48 8B 94 24 E8 00 00 00         mov rdx, qword ptr [rsp + 0xe8]
00208288  48 8D 4E 10                     lea rcx, [rsi + 0x10]
0020828C  E8 5F AC 18 00                  call 0x140392ef0
00208291  E9 69 FB FF FF                  jmp 0x140207dff
00208296  BB 02 00 00 00                  mov ebx, 2
0020829B  48 8D 8F BE 38 00 00            lea rcx, [rdi + 0x38be]
002082A2  8B D3                           mov edx, ebx
002082A4  E8 A7 59 19 00                  call 0x14039dc50
002082A9  A8 AF                           test al, 0xaf
002082AB  0F 85 5D FB FF FF               jne 0x140207e0e
002082B1  44 8D 4B 02                     lea r9d, [rbx + 2]
002082B5  E9 EF FD FF FF                  jmp 0x1402080a9
002082BA  8B 87 B0 38 00 00               mov eax, dword ptr [rdi + 0x38b0]
002082C0  39 87 AC 38 00 00               cmp dword ptr [rdi + 0x38ac], eax
002082C6  0F 82 D4 FD FF FF               jb 0x1402080a0
002082CC  E9 45 FF FF FF                  jmp 0x140208216
002082D1  80 BF B8 38 00 00 00            cmp byte ptr [rdi + 0x38b8], 0
002082D8  0F 84 9F FA FF FF               je 0x140207d7d
002082DE  48 8D B7 70 38 00 00            lea rsi, [rdi + 0x3870]
002082E5  E9 9A FA FF FF                  jmp 0x140207d84
002082EA  49 83 BD B8 8E 00 00 00         cmp qword ptr [r13 + 0x8eb8], 0
002082F2  0F 84 D7 FE FF FF               je 0x1402081cf
002082F8  8B 10                           mov edx, dword ptr [rax]
002082FA  8B C2                           mov eax, edx
002082FC  25 00 00 04 00                  and eax, 0x40000
00208301  0F BA E2 14                     bt edx, 0x14
00208305  0F 83 F9 00 00 00               jae 0x140208404
0020830B  80 3D F5 CC DB 00 00            cmp byte ptr [rip + 0xdbccf5], 0
00208312  49 8B 8D B8 8E 00 00            mov rcx, qword ptr [r13 + 0x8eb8]
00208319  89 59 0C                        mov dword ptr [rcx + 0xc], ebx
0020831C  8B 77 24                        mov esi, dword ptr [rdi + 0x24]
0020831F  75 1E                           jne 0x14020833f
00208321  8B C6                           mov eax, esi
00208323  48 8D 15 D6 7C DF FF            lea rdx, [rip - 0x20832a]
0020832A  0F B6 B4 72 60 D2 FC 00         movzx esi, byte ptr [rdx + rsi*2 + 0xfcd260]
00208332  C1 E6 06                        shl esi, 6
00208335  0F B6 84 42 61 D2 FC 00         movzx eax, byte ptr [rdx + rax*2 + 0xfcd261]
0020833D  0B F0                           or esi, eax
0020833F  89 71 08                        mov dword ptr [rcx + 8], esi
00208342  8B 05 CC E7 DB 00               mov eax, dword ptr [rip + 0xdbe7cc]
00208348  A8 20                           test al, 0x20
0020834A  74 0A                           je 0x140208356
0020834C  8B 4F 24                        mov ecx, dword ptr [rdi + 0x24]
0020834F  8B D3                           mov edx, ebx
00208351  E8 6A 2F 2F 00                  call 0x1404fb2c0
00208356  8B D6                           mov edx, esi
00208358  B9 C2 00 00 40                  mov ecx, 0x400000c2
0020835D  48 C1 EA 20                     shr rdx, 0x20
00208361  8B C6                           mov eax, esi
00208363  0F 30                           wrmsr
00208365  E9 65 FE FF FF                  jmp 0x1402081cf
0020836A  4C 8B C7                        mov r8, rdi
0020836D  49 8B D5                        mov rdx, r13
00208370  48 8B CB                        mov rcx, rbx
00208373  E8 10 48 2F 00                  call 0x1404fcb88
00208378  E9 F3 FC FF FF                  jmp 0x140208070
0020837D  8B 46 18                        mov eax, dword ptr [rsi + 0x18]
00208380  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
00208384  8B 46 1C                        mov eax, dword ptr [rsi + 0x1c]
00208387  89 44 24 4C                     mov dword ptr [rsp + 0x4c], eax
0020838B  E9 1A FB FF FF                  jmp 0x140207eaa
00208390  48 8B 05 E1 EB DB 00            mov rax, qword ptr [rip + 0xdbebe1]
00208397  4C 8B D3                        mov r10, rbx
0020839A  4C 33 15 AF EE DB 00            xor r10, qword ptr [rip + 0xdbeeaf]
002083A1  8B C8                           mov ecx, eax
002083A3  48 8B 53 18                     mov rdx, qword ptr [rbx + 0x18]
002083A7  44 8B 4C 24 4C                  mov r9d, dword ptr [rsp + 0x4c]
002083AC  44 8B 44 24 44                  mov r8d, dword ptr [rsp + 0x44]
002083B1  49 0F CA                        bswap r10
002083B4  4C 33 D2                        xor r10, rdx
002083B7  49 D3 CA                        ror r10, cl
002083BA  48 B9 77 72 DD F3 C7 C6 35 7E   movabs rcx, 0x7e35c6c7f3dd7277
002083C4  4C 33 D0                        xor r10, rax
002083C7  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
002083CC  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
002083D1  0F B6 43 01                     movzx eax, byte ptr [rbx + 1]
002083D5  88 44 24 28                     mov byte ptr [rsp + 0x28], al
002083D9  49 0F AF CA                     imul rcx, r10
002083DD  89 6C 24 20                     mov dword ptr [rsp + 0x20], ebp
002083E1  E8 4A 38 2F 00                  call 0x1404fbc30
002083E6  E9 75 FC FF FF                  jmp 0x140208060
002083EB  48 8D 87 40 38 00 00            lea rax, [rdi + 0x3840]
002083F2  48 3B F0                        cmp rsi, rax
002083F5  0F 85 EC FA FF FF               jne 0x140207ee7
002083FB  F0 FF 41 1C                     lock inc dword ptr [rcx + 0x1c]
002083FF  E9 F3 FA FF FF                  jmp 0x140207ef7
00208404  44 0F B6 C2                     movzx r8d, dl
00208408  85 C0                           test eax, eax
0020840A  0F 84 BF FD FF FF               je 0x1402081cf
00208410  44 3B C1                        cmp r8d, ecx
00208413  0F 8D B6 FD FF FF               jge 0x1402081cf
00208419  E9 ED FE FF FF                  jmp 0x14020830b
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00207D3E(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, unsigned __int8 a8, unsigned int a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13, __int64 a14, unsigned __int8 a15, unsigned __int8 a16, unsigned __int8 a17, unsigned __int8 a18, __int64 a19, __int64 a20, __int64 a21, __int64 a22, __int64 a23, __int64 a24, __int64 a25, __int64 a26, __int64 a27, __int64 a28, __int64 a29, unsigned __int8 a30, __int64 a31, __int64 a32, __int64 a33, unsigned __int8 a34)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_p108;
    unsigned __int8 v_stack_p110;
    unsigned __int64 v_stack_p118;
    unsigned __int8 v_stack_p128;
    unsigned int v_stack_p12C;
    unsigned int v_stack_p134;
    unsigned int v_stack_p138;
    unsigned __int64 v_stack_p140;
    unsigned int v_stack_p148;
    unsigned __int64 v_stack_p14C;
    unsigned int v_stack_p150;
    unsigned __int64 v_stack_p154;
    unsigned __int64 v_stack_p160;
    unsigned __int64 v_stack_p168;
    unsigned __int64 v_stack_p170;
    unsigned __int64 v_stack_p178;
    unsigned __int64 v_stack_p180;
    unsigned __int64 v_stack_p188;
    unsigned __int64 v_stack_p1D8;
    unsigned __int64 v_stack_pB0;
    unsigned __int8 v_stack_pF0;

    a2 = (((unsigned __int16)(v_rsi)) != ((unsigned __int16)((unsigned int)(*(unsigned int *)(v_r13 + 36))))) ? 1 : 0;
    v_stack_pF0 = (unsigned __int8)(a2);
    v_stack_pB0 = v_r14;
    result = *(unsigned __int64 *)(v_r13 + 200);
    if (((*(unsigned __int64 *)(v_rbx + 16)) & (*(unsigned __int64 *)(v_r13 + 200))) == 0) {
        result = *(unsigned __int8 *)(v_r13 + 209);
    }
    if ((*(unsigned __int8 *)(v_rbx)) == 26) goto loc_002082D1;
loc_00207D7D:
loc_00207D84:
    if (((*(unsigned __int8 *)(v_rip + 14413179)) & (33)) == 0) goto loc_00207E59;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13656257))) != 0) goto loc_00207E59;
    result = KiAcquireSpinLockInstrumented(v_r13 + 14400 + 16, a2, a3, a4);
loc_00207DA8:
loc_00207DB0:
    a1 = *(unsigned __int64 *)(v_r13 + 11664);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_r13 + 36)))) != (*(unsigned int *)(v_r13 + 36))) { a1 = 1; }
    result = 0;
    if (condition_is_equal) goto loc_00207E74;
loc_00207DD2:
    if (v_r15 != 0) {
        result = a34;
        result = (unsigned int)((result) << (24));
        result = (unsigned int)(~(result));
    }
    if (((*(unsigned __int8 *)(v_rip + 14413075)) & (1)) != 0) goto loc_00208272;
loc_00207DF9:
loc_00207DFF:
    if (a8 != 0) goto loc_00208055;
loc_00207E0E:
    if ((*(unsigned int *)(v_rip + 14413579)) != 0) {
        a1 = v_cr8;
        a2 = (unsigned __int8)(v_r12);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (192);
    return a8;
loc_00207E59:
    if (condition_is_above_or_equal) goto loc_00207DB0;
    result = KxWaitForSpinLockAndAcquire(v_r13 + 14400 + 16, a2, a3, a4);
    goto loc_00207DA8;
loc_00207E74:
    v_stack_p12C = (unsigned int)((unsigned int)(*(unsigned int *)(v_r13 + 14400 + 24)));
    *(unsigned int *)(v_r13 + 14400 + 24) = (unsigned int)((unsigned int)(*(unsigned int *)(v_r13 + 14400 + 24)) + 1);
    *(unsigned __int64 *)(v_rbx + 40) = a31;
    *(unsigned __int64 *)(v_rbx + 48) = a32;
    if (a9 != 0) goto loc_0020837D;
loc_00207EAA:
    v_stack_p128 = 1;
    if ((*(unsigned __int8 *)(v_rbx + 1)) == 2) goto loc_0020824C;
    *(unsigned __int64 *)(v_rbx + 8) = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_r13 + 14400 + 8)) = v_rbx + 8;
    *(unsigned __int64 *)(v_r13 + 14400 + 8) = v_rbx + 8;
loc_00207ECF:
    if ((unsigned __int8)(a2) != 0) {
        *(unsigned __int16 *)(v_rbx + 2) = (unsigned __int16)(a33);
    }
    if (*(unsigned __int64 *)(a23 + 36536) != 0) goto loc_002083EB;
loc_00207EE7:
    if ((v_r13 + 14400) != (a23 + 14400)) goto loc_00207DD2;
loc_00207EF7:
    if (*(unsigned __int64 *)(a23 + 14352) == 0) goto loc_00207DD2;
    v_r11 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a23 + 14352) + 4))) >> (5));
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a23 + 14352) + 4))))) & (31));
    v_r10 = (-1) << ((unsigned __int8)(a1));
    a3 = (v_r10) & (*(unsigned __int64 *)(v_rbx + 24));
    result = (a3) >> (56);
    v_stack_p180 = result;
    result = (a3) >> (48);
    v_stack_p178 = result;
    result = (a3) >> (40);
    v_stack_p170 = result;
    result = (a3) >> (32);
    v_stack_p168 = result;
    result = (a3) >> (24);
    v_stack_p160 = result;
    result = (a3) >> (16);
    a2 = (a3) >> (8);
    v_stack_p1D8 = result;
    if ((unsigned int)(v_r11) == 0) goto loc_00207DD2;
    result = ((unsigned __int8)(a3)) + (0xB15DCBULL);
    v_stack_p188 = a3;
    a1 = (a1) * (result);
    a1 = (a1) + ((unsigned __int8)(a2));
    a2 = (a2) * (a1);
    a2 = (a2) + (a30);
    a1 = (a1) * (a2);
    a1 = (a1) + (a15);
    a2 = (a2) * (a1);
    a2 = (a2) + (a16);
    a1 = (a1) * (a2);
    a1 = (a1) + (a17);
    a2 = (a2) * (a1);
    a2 = (a2) + (a18);
    result = (a18) * (a2);
    result = (result) + (a19);
    a2 = (v_r11 - 1) & ((unsigned int)((unsigned int)(result)));
loc_00208011:
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a23 + 14352) + 8) + a2 * 8))) & (1)) != 0) goto loc_00207DD2;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a23 + 14352) + 8) + a2 * 8) + 8)) & (v_r10);
    if (a3 != result) goto loc_00208011;
    v_stack_p140 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a23 + 14352) + 8) + a2 * 8) + 16);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a23 + 14352) + 8) + a2 * 8) + 16)) <= ((unsigned int)(*(unsigned int *)(v_rip + 14413762)))) goto loc_00207DD2;
    *(unsigned int *)(v_r13 + 14400 + 40) = 1;
    v_stack_p140 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a23 + 14352) + 8) + a2 * 8) + 16);
    goto loc_00207DD2;
loc_00208055:
    if (a9 != 0) goto loc_00208390;
loc_00208060:
    if (((*(unsigned int *)(v_rip + 14412458)) & (512)) != 0) goto loc_0020836A;
loc_00208070:
    if ((v_r13 + 14400) == (a23 + 14448)) goto loc_00208296;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_r13 + 14400 + 24)))) >= (*(unsigned int *)(a23 + 14504))) goto loc_002080A0;
    if (v_r13 != a23) goto loc_00208206;
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rbx + 1)) == 0) goto loc_002082BA;
loc_002080A0:
loc_002080A9:
    v_r10 = 175;
    if (a23 == v_r13) {
        v_r10 = 169;
        a4 = (unsigned __int16)((2) | (32));
    }
    v_stack_p138 = 0;
    a1 = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(a23 + 14524))) | ((unsigned __int16)(a4)));
    if (condition_is_equal) goto loc_00208117;
loc_002080EA:
    result = RtlBackoff(a10, *(unsigned __int16 *)(a23 + 14524), a3, a4);
    a1 = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(a23 + 14524))) | ((unsigned __int16)(a4)));
    if (condition_is_not_equal) goto loc_002080EA;
loc_00208117:
    if ((((unsigned __int16)(v_r10)) & ((unsigned __int16)(*(unsigned __int16 *)(a23 + 14524)))) != 0) goto loc_00207E0E;
    if (a23 != v_r13) goto loc_002081AB;
    if ((*(unsigned __int8 *)(v_r13 + 32)) == 0) goto loc_0020813B;
    *(unsigned __int8 *)(v_r13 + 6) = 1;
    goto loc_00207E0E;
loc_0020813B:
    result = 0;
    v_stack_p14C = v_xmm0;
    if ((*(unsigned __int8 *)(v_rip + 14412415)) == 0) goto loc_002081A1;
    result = HalpDisableInterrupts(a1, *(unsigned __int16 *)(a23 + 14524), *(unsigned __int64 *)(gs_base + (0 + 32)), a4);
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 168))))) | (4));
    *(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 168) = (unsigned int)(a1);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 168))) == 0) {
        a1 = 0xC0010015ULL;
        a2 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 168))) << (32);
        result = (result) | (a2);
        result = (result) | (a2);
        a2 = result;
        a2 = (a2) >> (32);
    }
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
    }
    v_stack_p148 = 5;
    goto loc_002081F2;
loc_002081AB:
    if ((*(unsigned __int64 *)(a23 + 8)) == (*(unsigned __int64 *)(a23 + 24))) goto loc_00208263;
loc_002081B9:
    if (*(unsigned __int64 *)(a23 + 36536) != 0) goto loc_002082EA;
loc_002081CF:
    v_stack_p148 = 6;
    v_stack_p150 = (unsigned int)(a33);
    result = 0;
    v_stack_p154 = 0;
loc_002081F2:
    result = HalpInterruptSendIpi(a12, 47, *(unsigned __int64 *)(gs_base + (0 + 32)), (unsigned __int8)(result));
    goto loc_00207E0E;
loc_00208206:
    if (((unsigned __int8)(result)) == 3) goto loc_002080A0;
    if (((unsigned __int8)(result)) == 2) goto loc_002080A0;
loc_00208216:
    result = KiSetDpcRequestFlag(a23 + 14524, 16, *(unsigned __int64 *)(gs_base + (0 + 32)), (unsigned __int8)(result));
    if ((((unsigned __int8)(result)) & (175)) != 0) goto loc_00207E0E;
    if (((*(unsigned __int64 *)(a23 + 200)) & (*(unsigned __int64 *)(*(unsigned __int64 *)(a23 + 192) + 64))) != 0) goto loc_002080A0;
    goto loc_00207E0E;
loc_0020824C:
    if (*(unsigned __int64 *)(v_r13 + 14400) == 0) {
        *(unsigned __int64 *)(v_r13 + 14400 + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(a23 + 192) + 64);
    }
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a23 + 192) + 64)) = *(unsigned __int64 *)(v_r13 + 14400);
    *(unsigned __int64 *)(v_r13 + 14400) = *(unsigned __int64 *)(*(unsigned __int64 *)(a23 + 192) + 64);
    goto loc_00207ECF;
loc_00208263:
    if ((*(unsigned __int8 *)(a23 + 7)) == 0) goto loc_00207E0E;
    goto loc_002081B9;
loc_00208272:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13655008))) != 0) goto loc_00207DF9;
    result = KiReleaseSpinLockInstrumented(v_r13 + 14400 + 16, a29, *(unsigned __int64 *)(gs_base + (0 + 32)), (unsigned __int8)(result));
    goto loc_00207DFF;
loc_00208296:
    result = KiSetDpcRequestFlag(a23 + 14526, 2, *(unsigned __int64 *)(gs_base + (0 + 32)), (unsigned __int8)(result));
    if ((((unsigned __int8)(result)) & (175)) != 0) goto loc_00207E0E;
    goto loc_002080A9;
loc_002082BA:
    if ((*(unsigned int *)(a23 + 14508)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a23 + 14512))))) goto loc_002080A0;
    goto loc_00208216;
loc_002082D1:
    if ((*(unsigned __int8 *)(a23 + 14520)) == 0) goto loc_00207D7D;
    goto loc_00207D84;
loc_002082EA:
    if ((*(unsigned __int64 *)(v_r13 + 36536)) == 0) goto loc_002081CF;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(a23 + 14512))))))) & (0x40000ULL));
    if (condition_is_above_or_equal) goto loc_00208404;
loc_0020830B:
    *(unsigned int *)(*(unsigned __int64 *)(v_r13 + 36536) + 12) = 2;
    v_rsi = (unsigned int)(*(unsigned int *)(a23 + 36));
    if ((*(unsigned __int8 *)(v_rip + 14404853)) == 0) {
        result = (unsigned int)((unsigned int)(*(unsigned int *)(a23 + 36)));
        a2 = v_rip - 2130730;
        v_rsi = *(unsigned __int8 *)(a2 + (unsigned int)(*(unsigned int *)(a23 + 36)) * 2 + 16568928);
        v_rsi = (unsigned int)((v_rsi) << (6));
        result = *(unsigned __int8 *)(a2 + result * 2 + 16568929);
        v_rsi = (unsigned int)((v_rsi) | ((unsigned int)(result)));
    }
    *(unsigned int *)(*(unsigned __int64 *)(v_r13 + 36536) + 8) = (unsigned int)(v_rsi);
    result = (unsigned int)(*(unsigned int *)(v_rip + 14411724));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14411724)))) & (32)) != 0) {
        a1 = *(unsigned int *)(a23 + 36);
        a2 = 2;
        result = EtwTraceXSchedulerPriorityKickSend(a1, a2, *(unsigned __int64 *)(gs_base + (0 + 32)), 2 + 2);
    }
    a2 = ((unsigned int)((unsigned int)(v_rsi))) >> (32);
    goto loc_002081CF;
loc_0020836A:
    result = KiCpuPartitionCheckDpcEnqueue(2, v_r13, a23, 2 + 2);
    goto loc_00208070;
loc_0020837D:
    v_stack_p12C = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsi + 24)));
    v_stack_p134 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsi + 28)));
    goto loc_00207EAA;
loc_00208390:
    v_r10 = (2) ^ (*(unsigned __int64 *)(v_rip + 14413487));
    v_r10 = (v_r10) ^ (*(unsigned __int64 *)(2 + 24));
    v_r10 = (v_r10) ^ (*(unsigned __int64 *)(v_rip + 14412769));
    v_stack_p118 = a11;
    v_stack_p110 = (unsigned __int8)(*(unsigned __int8 *)(2 + 1));
    a1 = ((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rip + 14412769)))) * (v_r10);
    v_stack_p108 = (unsigned int)(a33);
    result = EtwTraceDpcEnqueueEvent(a1, *(unsigned __int64 *)(2 + 24), (unsigned int)(v_stack_p12C), (unsigned int)(v_stack_p134));
    goto loc_00208060;
loc_002083EB:
    if (v_rsi != (a23 + 14400)) goto loc_00207EE7;
    goto loc_00207EF7;
loc_00208404:
    if ((unsigned int)(a23 + 14400) == 0) goto loc_002081CF;
    if (((unsigned int)((unsigned __int8)(*(unsigned __int64 *)(2 + 24)))) >= ((unsigned int)(a1))) goto loc_002081CF;
    goto loc_0020830B;
}
```

## 5. (Beta) C Style

```c
int64_t sub_00207D3E(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint8_t Arg8, uint32_t Arg9, int64_t Arg10, int64_t Arg11, int64_t Arg12, uint64_t Arg13, uint64_t Arg14, uint8_t Arg15, uint8_t Arg16, uint8_t Arg17, uint8_t Arg18, int64_t Arg19, uint64_t Arg20, uint64_t Arg21, int64_t Arg22, int64_t Arg23, uint64_t Arg24, uint64_t Arg25, uint64_t Arg26, uint64_t Arg27, uint64_t Arg28, int64_t Arg29, uint8_t Arg30, int64_t Arg31, int64_t Arg32, int64_t Arg33, uint8_t Arg34)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_p108;
    uint8_t v_stack_p110;
    uint64_t v_stack_p118;
    uint8_t v_stack_p128;
    uint32_t v_stack_p12C;
    uint32_t v_stack_p134;
    uint32_t v_stack_p138;
    uint64_t v_stack_p140;
    uint32_t v_stack_p148;
    uint64_t v_stack_p14C;
    uint32_t v_stack_p150;
    uint64_t v_stack_p154;
    uint64_t v_stack_p160;
    uint64_t v_stack_p168;
    uint64_t v_stack_p170;
    uint64_t v_stack_p178;
    uint64_t v_stack_p180;
    uint64_t v_stack_p188;
    uint64_t v_stack_p1D8;
    uint64_t v_stack_pB0;
    uint8_t v_stack_pF0;

    Arg2 = (((uint16_t)(local_rsi)) != ((uint16_t)((uint32_t)(*(uint32_t *)(local_r13 + 0x24))))) ? 1 : 0;
    v_stack_pF0 = (uint8_t)(Arg2);
    v_stack_pB0 = local_r14;
    result = *(uint64_t *)(local_r13 + 0xC8);
    if (((*(uint64_t *)(local_rbx + 0x10)) & (*(uint64_t *)(local_r13 + 0xC8))) == 0) {
        result = *(uint8_t *)(local_r13 + 0xD1);
    }
    if ((*(uint8_t *)(local_rbx)) == 26) goto loc_002082D1;
loc_00207D7D:
loc_00207D84:
    if (((*(uint8_t *)(v_rip + 0xDBED7B)) & (33)) == 0) goto loc_00207E59;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD060C1))) != 0) goto loc_00207E59;
    result = KiAcquireSpinLockInstrumented(local_r13 + 14400 + 16, Arg2, Arg3, Arg4);
loc_00207DA8:
loc_00207DB0:
    Arg1 = *(uint64_t *)(local_r13 + 0x2D90);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_r13 + 0x24)))) != (*(uint32_t *)(local_r13 + 0x24))) { Arg1 = 1; }
    result = 0;
    if (condition_is_equal) goto loc_00207E74;
loc_00207DD2:
    if (local_r15 != 0) {
        result = Arg34;
        result = (uint32_t)((result) << (24));
        result = (uint32_t)(~(result));
    }
    if (((*(uint8_t *)(v_rip + 0xDBED13)) & (1)) != 0) goto loc_00208272;
loc_00207DF9:
loc_00207DFF:
    if (Arg8 != 0) goto loc_00208055;
loc_00207E0E:
    if ((*(uint32_t *)(v_rip + 0xDBEF0B)) != 0) {
        Arg1 = v_cr8;
        Arg2 = (uint8_t)(local_r12);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, Arg3, Arg4);
    }
    local_rsp = (local_rsp) + (192);
    return Arg8;
loc_00207E59:
    if (condition_is_above_or_equal) goto loc_00207DB0;
    result = KxWaitForSpinLockAndAcquire(local_r13 + 14400 + 16, Arg2, Arg3, Arg4);
    goto loc_00207DA8;
loc_00207E74:
    v_stack_p12C = (uint32_t)((uint32_t)(*(uint32_t *)(local_r13 + 0x3840 + 0x18)));
    *(uint32_t *)(local_r13 + 0x3840 + 0x18) = (uint32_t)((uint32_t)(*(uint32_t *)(local_r13 + 0x3840 + 0x18)) + 1);
    *(uint64_t *)(local_rbx + 0x28) = Arg31;
    *(uint64_t *)(local_rbx + 0x30) = Arg32;
    if (Arg9 != 0) goto loc_0020837D;
loc_00207EAA:
    v_stack_p128 = 1;
    if ((*(uint8_t *)(local_rbx + 0x1)) == 2) goto loc_0020824C;
    *(uint64_t *)(local_rbx + 0x8) = 0;
    *(uint64_t *)(*(uint64_t *)(local_r13 + 0x3840 + 0x8)) = local_rbx + 8;
    *(uint64_t *)(local_r13 + 0x3840 + 0x8) = local_rbx + 8;
loc_00207ECF:
    if ((uint8_t)(Arg2) != 0) {
        *(uint16_t *)(local_rbx + 0x2) = (uint16_t)(Arg33);
    }
    if (*(uint64_t *)(Arg23 + 0x8EB8) != 0) goto loc_002083EB;
loc_00207EE7:
    if ((local_r13 + 14400) != (Arg23 + 14400)) goto loc_00207DD2;
loc_00207EF7:
    if (*(uint64_t *)(Arg23 + 0x3810) == 0) goto loc_00207DD2;
    local_r11 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg23 + 0x3810) + 0x4))) >> (5));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg23 + 0x3810) + 0x4))))) & (31));
    local_r10 = (-1) << ((uint8_t)(Arg1));
    Arg3 = (local_r10) & (*(uint64_t *)(local_rbx + 0x18));
    result = (Arg3) >> (56);
    v_stack_p180 = result;
    result = (Arg3) >> (48);
    v_stack_p178 = result;
    result = (Arg3) >> (40);
    v_stack_p170 = result;
    result = (Arg3) >> (32);
    v_stack_p168 = result;
    result = (Arg3) >> (24);
    v_stack_p160 = result;
    result = (Arg3) >> (16);
    Arg2 = (Arg3) >> (8);
    v_stack_p1D8 = result;
    if ((uint32_t)(local_r11) == 0) goto loc_00207DD2;
    result = ((uint8_t)(Arg3)) + (0xB15DCBULL);
    v_stack_p188 = Arg3;
    Arg1 = (Arg1) * (result);
    Arg1 = (Arg1) + ((uint8_t)(Arg2));
    Arg2 = (Arg2) * (Arg1);
    Arg2 = (Arg2) + (Arg30);
    Arg1 = (Arg1) * (Arg2);
    Arg1 = (Arg1) + (Arg15);
    Arg2 = (Arg2) * (Arg1);
    Arg2 = (Arg2) + (Arg16);
    Arg1 = (Arg1) * (Arg2);
    Arg1 = (Arg1) + (Arg17);
    Arg2 = (Arg2) * (Arg1);
    Arg2 = (Arg2) + (Arg18);
    result = (Arg18) * (Arg2);
    result = (result) + (Arg19);
    Arg2 = (local_r11 - 1) & ((uint32_t)((uint32_t)(result)));
loc_00208011:
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg23 + 0x3810) + 0x8) + Arg2 * 8))) & (1)) != 0) goto loc_00207DD2;
    result = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg23 + 0x3810) + 0x8) + Arg2 * 8) + 0x8)) & (local_r10);
    if (Arg3 != result) goto loc_00208011;
    v_stack_p140 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg23 + 0x3810) + 0x8) + Arg2 * 8) + 0x10);
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg23 + 0x3810) + 0x8) + Arg2 * 8) + 0x10)) <= ((uint32_t)(*(uint32_t *)(v_rip + 0xDBEFC2)))) goto loc_00207DD2;
    *(uint32_t *)(local_r13 + 0x3840 + 0x28) = 1;
    v_stack_p140 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg23 + 0x3810) + 0x8) + Arg2 * 8) + 0x10);
    goto loc_00207DD2;
loc_00208055:
    if (Arg9 != 0) goto loc_00208390;
loc_00208060:
    if (((*(uint32_t *)(v_rip + 0xDBEAAA)) & (512)) != 0) goto loc_0020836A;
loc_00208070:
    if ((local_r13 + 14400) == (Arg23 + 14448)) goto loc_00208296;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_r13 + 0x3840 + 0x18)))) >= (*(uint32_t *)(Arg23 + 0x38A8))) goto loc_002080A0;
    if (local_r13 != Arg23) goto loc_00208206;
    if ((uint8_t)(*(uint8_t *)(local_rbx + 0x1)) == 0) goto loc_002082BA;
loc_002080A0:
loc_002080A9:
    local_r10 = 175;
    if (Arg23 == local_r13) {
        local_r10 = 169;
        Arg4 = (uint16_t)((2) | (32));
    }
    v_stack_p138 = 0;
    Arg1 = (uint16_t)(((uint16_t)(*(uint16_t *)(Arg23 + 0x38BC))) | ((uint16_t)(Arg4)));
    if (condition_is_equal) goto loc_00208117;
loc_002080EA:
    result = RtlBackoff(Arg10, *(uint16_t *)(Arg23 + 0x38BC), Arg3, Arg4);
    Arg1 = (uint16_t)(((uint16_t)(*(uint16_t *)(Arg23 + 0x38BC))) | ((uint16_t)(Arg4)));
    if (condition_is_not_equal) goto loc_002080EA;
loc_00208117:
    if ((((uint16_t)(local_r10)) & ((uint16_t)(*(uint16_t *)(Arg23 + 0x38BC)))) != 0) goto loc_00207E0E;
    if (Arg23 != local_r13) goto loc_002081AB;
    if ((*(uint8_t *)(local_r13 + 0x20)) == 0) goto loc_0020813B;
    *(uint8_t *)(local_r13 + 0x6) = 1;
    goto loc_00207E0E;
loc_0020813B:
    result = 0;
    v_stack_p14C = v_xmm0;
    if ((*(uint8_t *)(v_rip + 0xDBEA7F)) == 0) goto loc_002081A1;
    result = HalpDisableInterrupts(Arg1, *(uint16_t *)(Arg23 + 0x38BC), *(uint64_t *)(gs_base + (0 + 0x20)), Arg4);
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xA8))))) | (4));
    *(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xA8) = (uint32_t)(Arg1);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xA8))) == 0) {
        Arg1 = 0xC0010015ULL;
        Arg2 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xA8))) << (32);
        result = (result) | (Arg2);
        result = (result) | (Arg2);
        Arg2 = result;
        Arg2 = (Arg2) >> (32);
    }
    if ((uint8_t)((uint8_t)(result)) != 0) {
    }
    v_stack_p148 = 5;
    goto loc_002081F2;
loc_002081AB:
    if ((*(uint64_t *)(Arg23 + 0x8)) == (*(uint64_t *)(Arg23 + 0x18))) goto loc_00208263;
loc_002081B9:
    if (*(uint64_t *)(Arg23 + 0x8EB8) != 0) goto loc_002082EA;
loc_002081CF:
    v_stack_p148 = 6;
    v_stack_p150 = (uint32_t)(Arg33);
    result = 0;
    v_stack_p154 = 0;
loc_002081F2:
    result = HalpInterruptSendIpi(Arg12, 47, *(uint64_t *)(gs_base + (0 + 0x20)), (uint8_t)(result));
    goto loc_00207E0E;
loc_00208206:
    if (((uint8_t)(result)) == 3) goto loc_002080A0;
    if (((uint8_t)(result)) == 2) goto loc_002080A0;
loc_00208216:
    result = KiSetDpcRequestFlag(Arg23 + 14524, 16, *(uint64_t *)(gs_base + (0 + 0x20)), (uint8_t)(result));
    if ((((uint8_t)(result)) & (175)) != 0) goto loc_00207E0E;
    if (((*(uint64_t *)(Arg23 + 0xC8)) & (*(uint64_t *)(*(uint64_t *)(Arg23 + 0xC0) + 0x40))) != 0) goto loc_002080A0;
    goto loc_00207E0E;
loc_0020824C:
    if (*(uint64_t *)(local_r13 + 0x3840) == 0) {
        *(uint64_t *)(local_r13 + 0x3840 + 0x8) = *(uint64_t *)(*(uint64_t *)(Arg23 + 0xC0) + 0x40);
    }
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg23 + 0xC0) + 0x40)) = *(uint64_t *)(local_r13 + 0x3840);
    *(uint64_t *)(local_r13 + 0x3840) = *(uint64_t *)(*(uint64_t *)(Arg23 + 0xC0) + 0x40);
    goto loc_00207ECF;
loc_00208263:
    if ((*(uint8_t *)(Arg23 + 0x7)) == 0) goto loc_00207E0E;
    goto loc_002081B9;
loc_00208272:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD05BE0))) != 0) goto loc_00207DF9;
    result = KiReleaseSpinLockInstrumented(local_r13 + 14400 + 16, Arg29, *(uint64_t *)(gs_base + (0 + 0x20)), (uint8_t)(result));
    goto loc_00207DFF;
loc_00208296:
    result = KiSetDpcRequestFlag(Arg23 + 14526, 2, *(uint64_t *)(gs_base + (0 + 0x20)), (uint8_t)(result));
    if ((((uint8_t)(result)) & (175)) != 0) goto loc_00207E0E;
    goto loc_002080A9;
loc_002082BA:
    if ((*(uint32_t *)(Arg23 + 0x38AC)) < ((uint32_t)((uint32_t)(*(uint32_t *)(Arg23 + 0x38B0))))) goto loc_002080A0;
    goto loc_00208216;
loc_002082D1:
    if ((*(uint8_t *)(Arg23 + 0x38B8)) == 0) goto loc_00207D7D;
    goto loc_00207D84;
loc_002082EA:
    if ((*(uint64_t *)(local_r13 + 0x8EB8)) == 0) goto loc_002081CF;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(Arg23 + 0x38B0))))))) & (0x40000ULL));
    if (condition_is_above_or_equal) goto loc_00208404;
loc_0020830B:
    *(uint32_t *)(*(uint64_t *)(local_r13 + 0x8EB8) + 0xC) = 2;
    local_rsi = (uint32_t)(*(uint32_t *)(Arg23 + 0x24));
    if ((*(uint8_t *)(v_rip + 0xDBCCF5)) == 0) {
        result = (uint32_t)((uint32_t)(*(uint32_t *)(Arg23 + 0x24)));
        Arg2 = v_rip - 2130730;
        local_rsi = *(uint8_t *)(Arg2 + (uint32_t)(*(uint32_t *)(Arg23 + 0x24)) * 2 + 0xFCD260);
        local_rsi = (uint32_t)((local_rsi) << (6));
        result = *(uint8_t *)(Arg2 + result * 2 + 0xFCD261);
        local_rsi = (uint32_t)((local_rsi) | ((uint32_t)(result)));
    }
    *(uint32_t *)(*(uint64_t *)(local_r13 + 0x8EB8) + 0x8) = (uint32_t)(local_rsi);
    result = (uint32_t)(*(uint32_t *)(v_rip + 0xDBE7CC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xDBE7CC)))) & (32)) != 0) {
        Arg1 = *(uint32_t *)(Arg23 + 0x24);
        Arg2 = 2;
        result = EtwTraceXSchedulerPriorityKickSend(Arg1, Arg2, *(uint64_t *)(gs_base + (0 + 0x20)), 2 + 2);
    }
    Arg2 = ((uint32_t)((uint32_t)(local_rsi))) >> (32);
    goto loc_002081CF;
loc_0020836A:
    result = KiCpuPartitionCheckDpcEnqueue(2, local_r13, Arg23, 2 + 2);
    goto loc_00208070;
loc_0020837D:
    v_stack_p12C = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x18)));
    v_stack_p134 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x1C)));
    goto loc_00207EAA;
loc_00208390:
    local_r10 = (2) ^ (*(uint64_t *)(v_rip + 0xDBEEAF));
    local_r10 = (local_r10) ^ (*(uint64_t *)(2 + 0x18));
    local_r10 = (local_r10) ^ (*(uint64_t *)(v_rip + 0xDBEBE1));
    v_stack_p118 = Arg11;
    v_stack_p110 = (uint8_t)(*(uint8_t *)(2 + 0x1));
    Arg1 = ((uint32_t)((uint32_t)(*(uint64_t *)(v_rip + 0xDBEBE1)))) * (local_r10);
    v_stack_p108 = (uint32_t)(Arg33);
    result = EtwTraceDpcEnqueueEvent(Arg1, *(uint64_t *)(2 + 0x18), (uint32_t)(v_stack_p12C), (uint32_t)(v_stack_p134));
    goto loc_00208060;
loc_002083EB:
    if (local_rsi != (Arg23 + 14400)) goto loc_00207EE7;
    goto loc_00207EF7;
loc_00208404:
    if ((uint32_t)(Arg23 + 14400) == 0) goto loc_002081CF;
    if (((uint32_t)((uint8_t)(*(uint64_t *)(2 + 0x18)))) >= ((uint32_t)(Arg1))) goto loc_002081CF;
    goto loc_0020830B;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00207D3E&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
