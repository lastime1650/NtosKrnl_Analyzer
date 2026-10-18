# sub_002329B4

- RVA: `0x002329B4`–`0x00232CA9` (길이 `757` bytes)
- VA: `0x00000001402329B4`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000604BC`
- 디코드: `182`개 명령, `757/757` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **13**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x00232B15` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00232B24` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00232BA4` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00232BAF` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00232BC4` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00232BD3` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00232BEB` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00232BFA` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00232C12` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00232C21` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00232C39` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00232C48` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00232C91` → [EtwTraceKernelEvent](EtwTraceKernelEvent_function_00235350.md) (function, `0x00235350`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x002329E1` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x00232A13` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x00232A25` → RVA `0x00FC5030` (`ALMOSTRO`; read)
- `0x00232B07` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **11**
  - `0x00232A59` → [sub_00232835 + 0xF8](Unknown_function_00232835.md) (`tail-transfer`)
  - `0x00232A7B` → [sub_00232835 + 0x1B](Unknown_function_00232835.md) (`tail-transfer`)
  - `0x00232B0F` → [sub_00232835 + 0x81](Unknown_function_00232835.md) (`tail-transfer`)
  - `0x00232B1C` → [sub_00232835 + 0x81](Unknown_function_00232835.md) (`tail-transfer`)
  - `0x00232B29` → [sub_00232835 + 0x83](Unknown_function_00232835.md) (`tail-transfer`)
  - `0x00232B4A` → [sub_00232835 + 0xF8](Unknown_function_00232835.md) (`tail-transfer`)
  - `0x00232B77` → [sub_00232835 + 0xE](Unknown_function_00232835.md) (`tail-transfer`)
  - `0x00232B92` → [sub_00232835 + 0xE](Unknown_function_00232835.md) (`tail-transfer`)
  - `0x00232C55` → [sub_00232835 + 0x11D](Unknown_function_00232835.md) (`tail-transfer`)
  - `0x00232C96` → [sub_00232835 + 0x11D](Unknown_function_00232835.md) (`tail-transfer`)
  - `0x00232CA4` → [sub_00232835 + 0x106](Unknown_function_00232835.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002329B4  43 C7 44 2F 1C FF FF FF FF      mov dword ptr [r15 + r13 + 0x1c], 0xffffffff
002329BD  66 45 85 C0                     test r8w, r8w
002329C1  0F 85 BC 00 00 00               jne 0x140232a83
002329C7  4D 8D B1 10 01 00 00            lea r14, [r9 + 0x110]
002329CE  49 C1 E6 05                     shl r14, 5
002329D2  4D 03 F5                        add r14, r13
002329D5  33 ED                           xor ebp, ebp
002329D7  F0 49 0F BA 2E 00               lock bts qword ptr [r14], 0
002329DD  73 1A                           jae 0x1402329f9
002329DF  FF C5                           inc ebp
002329E1  85 2D C5 28 D9 00               test dword ptr [rip + 0xd928c5], ebp
002329E7  0F 84 C9 01 00 00               je 0x140232bb6
002329ED  F3 90                           pause
002329EF  49 8B 06                        mov rax, qword ptr [r14]
002329F2  48 85 C0                        test rax, rax
002329F5  74 E0                           je 0x1402329d7
002329F7  EB E6                           jmp 0x1402329df
002329F9  4C 8B 4C 24 30                  mov r9, qword ptr [rsp + 0x30]
002329FE  43 83 7C 2F 1C FF               cmp dword ptr [r15 + r13 + 0x1c], -1
00232A04  75 4E                           jne 0x140232a54
00232A06  43 83 7C 2C 1C FF               cmp dword ptr [r12 + r13 + 0x1c], -1
00232A0C  75 46                           jne 0x140232a54
00232A0E  4C 8B 5C 24 50                  mov r11, qword ptr [rsp + 0x50]
00232A13  48 8D 0D E6 D5 DC FF            lea rcx, [rip - 0x232a1a]
00232A1A  41 0F B6 83 D0 00 00 00         movzx eax, byte ptr [r11 + 0xd0]
00232A22  48 03 C0                        add rax, rax
00232A25  83 3D 04 26 D9 00 00            cmp dword ptr [rip + 0xd92604], 0
00232A2C  48 8B 8C C1 28 85 FC 00         mov rcx, qword ptr [rcx + rax*8 + 0xfc8528]
00232A34  0F 84 F4 00 00 00               je 0x140232b2e
00232A3A  44 8B 54 24 38                  mov r10d, dword ptr [rsp + 0x38]
00232A3F  49 C1 E9 06                     shr r9, 6
00232A43  41 83 E2 3F                     and r10d, 0x3f
00232A47  41 8B C2                        mov eax, r10d
00232A4A  F0 4A 0F B3 04 C9               lock btr qword ptr [rcx + r9*8], rax
00232A50  4A 8D 0C C9                     lea rcx, [rcx + r9*8]
00232A54  F0 49 83 26 00                  lock and qword ptr [r14], 0
00232A59  E9 CF FE FF FF                  jmp 0x14023292d
00232A5E  66 90                           nop
00232A60  FF C3                           inc ebx
00232A62  85 1D 44 28 D9 00               test dword ptr [rip + 0xd92844], ebx
00232A68  0F 84 6F 01 00 00               je 0x140232bdd
00232A6E  F3 90                           pause
00232A70  8B 07                           mov eax, dword ptr [rdi]
00232A72  84 C0                           test al, al
00232A74  78 EA                           js 0x140232a60
00232A76  F0 0F BA 2F 07                  lock bts dword ptr [rdi], 7
00232A7B  0F 83 CF FD FF FF               jae 0x140232850
00232A81  EB DD                           jmp 0x140232a60
00232A83  4D 8D 71 10                     lea r14, [r9 + 0x10]
00232A87  49 C1 E6 05                     shl r14, 5
00232A8B  4D 03 F5                        add r14, r13
00232A8E  F0 49 0F BA 2E 00               lock bts qword ptr [r14], 0
00232A94  73 04                           jae 0x140232a9a
00232A96  F3 90                           pause
00232A98  EB 09                           jmp 0x140232aa3
00232A9A  4D 85 F6                        test r14, r14
00232A9D  0F 85 5B FF FF FF               jne 0x1402329fe
00232AA3  F0 48 83 23 00                  lock and qword ptr [rbx], 0
00232AA8  33 DB                           xor ebx, ebx
00232AAA  F0 49 0F BA 2E 00               lock bts qword ptr [r14], 0
00232AB0  73 1A                           jae 0x140232acc
00232AB2  FF C3                           inc ebx
00232AB4  85 1D F2 27 D9 00               test dword ptr [rip + 0xd927f2], ebx
00232ABA  0F 84 44 01 00 00               je 0x140232c04
00232AC0  F3 90                           pause
00232AC2  49 8B 06                        mov rax, qword ptr [r14]
00232AC5  48 85 C0                        test rax, rax
00232AC8  74 E0                           je 0x140232aaa
00232ACA  EB E6                           jmp 0x140232ab2
00232ACC  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00232AD1  48 81 C3 10 01 00 00            add rbx, 0x110
00232AD8  48 C1 E3 05                     shl rbx, 5
00232ADC  49 03 DD                        add rbx, r13
00232ADF  33 ED                           xor ebp, ebp
00232AE1  F0 48 0F BA 2B 00               lock bts qword ptr [rbx], 0
00232AE7  0F 83 0C FF FF FF               jae 0x1402329f9
00232AED  FF C5                           inc ebp
00232AEF  85 2D B7 27 D9 00               test dword ptr [rip + 0xd927b7], ebp
00232AF5  0F 84 30 01 00 00               je 0x140232c2b
00232AFB  F3 90                           pause
00232AFD  48 8B 03                        mov rax, qword ptr [rbx]
00232B00  48 85 C0                        test rax, rax
00232B03  74 DC                           je 0x140232ae1
00232B05  EB E6                           jmp 0x140232aed
00232B07  8B 05 AB 3F D9 00               mov eax, dword ptr [rip + 0xd93fab]
00232B0D  A8 40                           test al, 0x40
00232B0F  0F 84 A1 FD FF FF               je 0x1402328b6
00232B15  E8 76 C9 0D 00                  call 0x14030f490
00232B1A  84 C0                           test al, al
00232B1C  0F 84 94 FD FF FF               je 0x1402328b6
00232B22  8B CD                           mov ecx, ebp
00232B24  E8 37 C9 0D 00                  call 0x14030f460
00232B29  E9 8A FD FF FF                  jmp 0x1402328b8
00232B2E  45 0F B6 93 D1 00 00 00         movzx r10d, byte ptr [r11 + 0xd1]
00232B36  49 C1 E1 06                     shl r9, 6
00232B3A  49 03 C9                        add rcx, r9
00232B3D  41 8B C2                        mov eax, r10d
00232B40  F0 48 0F B3 01                  lock btr qword ptr [rcx], rax
00232B45  F0 49 83 26 00                  lock and qword ptr [r14], 0
00232B4A  E9 DE FD FF FF                  jmp 0x14023292d
00232B4F  F0 48 83 23 00                  lock and qword ptr [rbx], 0
00232B54  0F B6 47 03                     movzx eax, byte ptr [rdi + 3]
00232B58  33 C9                           xor ecx, ecx
00232B5A  83 E0 3F                        and eax, 0x3f
00232B5D  49 87 4C C5 00                  xchg qword ptr [r13 + rax*8], rcx
00232B62  48 85 C9                        test rcx, rcx
00232B65  0F 85 30 01 00 00               jne 0x140232c9b
00232B6B  F0 44 21 3F                     lock and dword ptr [rdi], r15d
00232B6F  0F B6 47 03                     movzx eax, byte ptr [rdi + 3]
00232B73  33 DB                           xor ebx, ebx
00232B75  84 C0                           test al, al
00232B77  0F 89 C6 FC FF FF               jns 0x140232843
00232B7D  0F 1F 00                        nop dword ptr [rax]
00232B80  FF C3                           inc ebx
00232B82  85 1D 24 27 D9 00               test dword ptr [rip + 0xd92724], ebx
00232B88  74 10                           je 0x140232b9a
00232B8A  F3 90                           pause
00232B8C  0F B6 47 03                     movzx eax, byte ptr [rdi + 3]
00232B90  84 C0                           test al, al
00232B92  0F 89 AB FC FF FF               jns 0x140232843
00232B98  EB E6                           jmp 0x140232b80
00232B9A  8B 05 18 3F D9 00               mov eax, dword ptr [rip + 0xd93f18]
00232BA0  A8 40                           test al, 0x40
00232BA2  74 E6                           je 0x140232b8a
00232BA4  E8 E7 C8 0D 00                  call 0x14030f490
00232BA9  84 C0                           test al, al
00232BAB  74 DD                           je 0x140232b8a
00232BAD  8B CB                           mov ecx, ebx
00232BAF  E8 AC C8 0D 00                  call 0x14030f460
00232BB4  EB D6                           jmp 0x140232b8c
00232BB6  8B 05 FC 3E D9 00               mov eax, dword ptr [rip + 0xd93efc]
00232BBC  A8 40                           test al, 0x40
00232BBE  0F 84 29 FE FF FF               je 0x1402329ed
00232BC4  E8 C7 C8 0D 00                  call 0x14030f490
00232BC9  84 C0                           test al, al
00232BCB  0F 84 1C FE FF FF               je 0x1402329ed
00232BD1  8B CD                           mov ecx, ebp
00232BD3  E8 88 C8 0D 00                  call 0x14030f460
00232BD8  E9 12 FE FF FF                  jmp 0x1402329ef
00232BDD  8B 05 D5 3E D9 00               mov eax, dword ptr [rip + 0xd93ed5]
00232BE3  A8 40                           test al, 0x40
00232BE5  0F 84 83 FE FF FF               je 0x140232a6e
00232BEB  E8 A0 C8 0D 00                  call 0x14030f490
00232BF0  84 C0                           test al, al
00232BF2  0F 84 76 FE FF FF               je 0x140232a6e
00232BF8  8B CB                           mov ecx, ebx
00232BFA  E8 61 C8 0D 00                  call 0x14030f460
00232BFF  E9 6C FE FF FF                  jmp 0x140232a70
00232C04  8B 05 AE 3E D9 00               mov eax, dword ptr [rip + 0xd93eae]
00232C0A  A8 40                           test al, 0x40
00232C0C  0F 84 AE FE FF FF               je 0x140232ac0
00232C12  E8 79 C8 0D 00                  call 0x14030f490
00232C17  84 C0                           test al, al
00232C19  0F 84 A1 FE FF FF               je 0x140232ac0
00232C1F  8B CB                           mov ecx, ebx
00232C21  E8 3A C8 0D 00                  call 0x14030f460
00232C26  E9 97 FE FF FF                  jmp 0x140232ac2
00232C2B  8B 05 87 3E D9 00               mov eax, dword ptr [rip + 0xd93e87]
00232C31  A8 40                           test al, 0x40
00232C33  0F 84 C2 FE FF FF               je 0x140232afb
00232C39  E8 52 C8 0D 00                  call 0x14030f490
00232C3E  84 C0                           test al, al
00232C40  0F 84 B5 FE FF FF               je 0x140232afb
00232C46  8B CD                           mov ecx, ebp
00232C48  E8 13 C8 0D 00                  call 0x14030f460
00232C4D  E9 AB FE FF FF                  jmp 0x140232afd
00232C52  45 84 F6                        test r14b, r14b
00232C55  0F 84 F7 FC FF FF               je 0x140232952
00232C5B  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00232C60  48 89 7C 24 40                  mov qword ptr [rsp + 0x40], rdi
00232C65  41 B9 55 0F 00 00               mov r9d, 0xf55
00232C6B  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00232C70  BA 01 00 00 00                  mov edx, 1
00232C75  48 C7 44 24 60 08 00 00 00      mov qword ptr [rsp + 0x60], 8
00232C7E  41 B8 00 00 02 40               mov r8d, 0x40020000
00232C84  C7 44 24 20 02 06 00 00         mov dword ptr [rsp + 0x20], 0x602
00232C8C  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
00232C91  E8 BA 26 00 00                  call 0x140235350
00232C96  E9 B7 FC FF FF                  jmp 0x140232952
00232C9B  41 B6 01                        mov r14b, 1
00232C9E  41 BF 7F FF FF 00               mov r15d, 0xffff7f
00232CA4  E9 92 FC FF FF                  jmp 0x14023293b
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_002329B4(__int64 a1, __int64 a2, unsigned __int16 a3, __int64 a4, __int64 a5, __int64 a6, unsigned int a7, __int64 a8, __int64 a9, __int64 a10)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r14;
    __int64 v_rbp;
    __int64 v_rbx;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;

    *(unsigned int *)(v_r15 + v_r13 * 1 + 28) = 0xFFFFFFFFULL;
    if (a3 != 0) goto loc_00232A83;
    v_r14 = (a4 + 272) << (5);
    v_r14 = (v_r14) + (v_r13);
    v_rbp = 0;
loc_002329D7:
    if (condition_is_above_or_equal) goto loc_002329F9;
loc_002329DF:
    v_rbp = (unsigned int)((v_rbp) + 1);
    if (((*(unsigned int *)(v_rip + 14231749)) & ((unsigned int)(v_rbp))) == 0) goto loc_00232BB6;
loc_002329ED:
loc_002329EF:
    if (*(unsigned __int64 *)(v_r14) == 0) goto loc_002329D7;
    goto loc_002329DF;
loc_002329F9:
loc_002329FE:
    if ((*(unsigned int *)(v_r15 + v_r13 * 1 + 28)) != -1) goto loc_00232A54;
    if ((*(unsigned int *)(v_r12 + v_r13 * 1 + 28)) != -1) goto loc_00232A54;
    result = (*(unsigned __int8 *)(a10 + 208)) + (*(unsigned __int8 *)(a10 + 208));
    if ((*(unsigned int *)(v_rip + 14231044)) == 0) goto loc_00232B2E;
    a4 = (a6) >> (6);
    v_r10 = (unsigned int)(((unsigned int)(a7)) & (63));
loc_00232A54:
loc_00232A83:
    v_r14 = (a4 + 16) << (5);
    v_r14 = (v_r14) + (v_r13);
    if (condition_is_above_or_equal) goto loc_00232A9A;
    goto loc_00232AA3;
loc_00232A9A:
    if (v_r14 != 0) goto loc_002329FE;
loc_00232AA3:
    v_rbx = 0;
loc_00232AAA:
    if (condition_is_above_or_equal) goto loc_00232ACC;
loc_00232AB2:
    v_rbx = (unsigned int)((v_rbx) + 1);
    if (((*(unsigned int *)(v_rip + 14231538)) & ((unsigned int)(v_rbx))) == 0) goto loc_00232C04;
loc_00232AC0:
loc_00232AC2:
    if (*(unsigned __int64 *)(v_r14) == 0) goto loc_00232AAA;
    goto loc_00232AB2;
loc_00232ACC:
    v_rbx = (a6) + (272);
    v_rbx = (v_rbx) << (5);
    v_rbx = (v_rbx) + (v_r13);
    v_rbp = 0;
loc_00232AE1:
    if (condition_is_above_or_equal) goto loc_002329F9;
loc_00232AED:
    v_rbp = (unsigned int)((v_rbp) + 1);
    if (((*(unsigned int *)(v_rip + 14231479)) & ((unsigned int)(v_rbp))) == 0) goto loc_00232C2B;
loc_00232AFB:
loc_00232AFD:
    if (*(unsigned __int64 *)(v_rbx) == 0) goto loc_00232AE1;
    goto loc_00232AED;
loc_00232B2E:
    a4 = (a4) << (6);
    a1 = (*(unsigned __int64 *)(v_rip - 2304538 + result * 8 + 16549160) + a4 * 8) + (a4);
loc_00232BB6:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14237436)))) & (64)) == 0) goto loc_002329ED;
    result = KiCheckVpBackingLongSpinWaitHypercall(a1, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_002329ED;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rbp)), a2, a3, a4);
    goto loc_002329EF;
loc_00232C04:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14237358)))) & (64)) == 0) goto loc_00232AC0;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)((unsigned int)(v_rbp)), a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00232AC0;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rbx)), a2, a3, a4);
    goto loc_00232AC2;
loc_00232C2B:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14237319)))) & (64)) == 0) goto loc_00232AFB;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)((unsigned int)(v_rbx)), a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00232AFB;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rbp)), a2, a3, a4);
    goto loc_00232AFD;
}
```

## 5. (Beta) C Style

```c
int64_t sub_002329B4(int64_t Arg1, int64_t Arg2, uint16_t Arg3, void *Arg4, uint64_t Arg5, int64_t Arg6, uint32_t Arg7, uint64_t Arg8, uint64_t Arg9, void *Arg10)
{
    uint8_t *arg4 = (uint8_t *)Arg4;
    uint8_t *arg10 = (uint8_t *)Arg10;

    int64_t result;
    int64_t local_r10;
    int64_t local_r14;
    int64_t local_rbp;
    int64_t local_rbx;
    uint32_t v_stack_p20;
    uint64_t v_stack_p40;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;

    *(uint32_t *)(local_r15 + local_r13 * 1 + 0x1C) = 0xFFFFFFFFULL;
    if (Arg3 != 0) goto loc_00232A83;
    local_r14 = (Arg4 + 272) << (5);
    local_r14 = (local_r14) + (local_r13);
    local_rbp = 0;
loc_002329D7:
    if (condition_is_above_or_equal) goto loc_002329F9;
loc_002329DF:
    local_rbp = (uint32_t)((local_rbp) + 1);
    if (((*(uint32_t *)(v_rip + 0xD928C5)) & ((uint32_t)(local_rbp))) == 0) goto loc_00232BB6;
loc_002329ED:
loc_002329EF:
    if (*(uint64_t *)(local_r14) == 0) goto loc_002329D7;
    goto loc_002329DF;
loc_002329F9:
loc_002329FE:
    if ((*(uint32_t *)(local_r15 + local_r13 * 1 + 0x1C)) != -1) goto loc_00232A54;
    if ((*(uint32_t *)(local_r12 + local_r13 * 1 + 0x1C)) != -1) goto loc_00232A54;
    result = (*(uint8_t *)(arg10 + 0xD0)) + (*(uint8_t *)(arg10 + 0xD0));
    if ((*(uint32_t *)(v_rip + 0xD92604)) == 0) goto loc_00232B2E;
    Arg4 = (Arg6) >> (6);
    local_r10 = (uint32_t)(((uint32_t)(Arg7)) & (63));
loc_00232A54:
loc_00232A83:
    local_r14 = (Arg4 + 16) << (5);
    local_r14 = (local_r14) + (local_r13);
    if (condition_is_above_or_equal) goto loc_00232A9A;
    goto loc_00232AA3;
loc_00232A9A:
    if (local_r14 != 0) goto loc_002329FE;
loc_00232AA3:
    local_rbx = 0;
loc_00232AAA:
    if (condition_is_above_or_equal) goto loc_00232ACC;
loc_00232AB2:
    local_rbx = (uint32_t)((local_rbx) + 1);
    if (((*(uint32_t *)(v_rip + 0xD927F2)) & ((uint32_t)(local_rbx))) == 0) goto loc_00232C04;
loc_00232AC0:
loc_00232AC2:
    if (*(uint64_t *)(local_r14) == 0) goto loc_00232AAA;
    goto loc_00232AB2;
loc_00232ACC:
    local_rbx = (Arg6) + (272);
    local_rbx = (local_rbx) << (5);
    local_rbx = (local_rbx) + (local_r13);
    local_rbp = 0;
loc_00232AE1:
    if (condition_is_above_or_equal) goto loc_002329F9;
loc_00232AED:
    local_rbp = (uint32_t)((local_rbp) + 1);
    if (((*(uint32_t *)(v_rip + 0xD927B7)) & ((uint32_t)(local_rbp))) == 0) goto loc_00232C2B;
loc_00232AFB:
loc_00232AFD:
    if (*(uint64_t *)(local_rbx) == 0) goto loc_00232AE1;
    goto loc_00232AED;
loc_00232B2E:
    Arg4 = (Arg4) << (6);
    Arg1 = (*(uint64_t *)(v_rip - 0x232A1A + result * 8 + 0xFC8528) + Arg4 * 8) + (Arg4);
loc_00232BB6:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD93EFC)))) & (64)) == 0) goto loc_002329ED;
    result = KiCheckVpBackingLongSpinWaitHypercall(Arg1, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_002329ED;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rbp)), Arg2, Arg3, Arg4);
    goto loc_002329EF;
loc_00232C04:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD93EAE)))) & (64)) == 0) goto loc_00232AC0;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)((uint32_t)(local_rbp)), Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00232AC0;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rbx)), Arg2, Arg3, Arg4);
    goto loc_00232AC2;
loc_00232C2B:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD93E87)))) & (64)) == 0) goto loc_00232AFB;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)((uint32_t)(local_rbx)), Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00232AFB;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rbp)), Arg2, Arg3, Arg4);
    goto loc_00232AFD;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg4` | `+ 0x10` | `64` | `R` |
| `Arg4` | `+ 0x110` | `64` | `R` |
| `Arg10` | `+ 0xD0` | `8` | `R` |
| `Arg10` | `+ 0xD1` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002329B4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
