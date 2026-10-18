# MiAddKernelStackToPrcbCache

- RVA: `0x00338710`–`0x00338CBB` (길이 `1,451` bytes)
- VA: `0x0000000140338710`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00076AD8`
- 디코드: `324`개 명령, `1,451/1,451` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **12**; 고유 호출 대상: **8**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **8**

### Outgoing calls
- `0x003388E7` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x00338AA8` → [MiValidateKernelShadowStackPage](MiValidateKernelShadowStackPage_function_00338D98.md) (function, `0x00338D98`)
- `0x00338AB9` → [MiPageToNode](MiPageToNode_function_00338CD0.md) (function, `0x00338CD0`)
- `0x00338B51` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x00338BBF` → [MiIsDecayPfn](../2B/MiIsDecayPfn_function_002B9240.md) (function, `0x002B9240`)
- `0x00338BE3` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00338BF2` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00338C12` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00338C21` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00338C32` → [MiUnlockPage](../31/MiUnlockPage_function_0031A3E0.md) (function, `0x0031A3E0`)
- `0x00338C52` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x00338CB1` → [MiPageToNode](MiPageToNode_function_00338CD0.md) (function, `0x00338CD0`)

### Direct callers
- [MmDeleteKernelStack](MmDeleteKernelStack_function_0033A960.md) at `0x0033AB9E`

### Static image references
- `0x003387D1` → RVA `0x00E2DCE0` (`.data`; read)
- `0x003387E6` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x0033893B` → RVA `0x00E30088` (`.data`; read)
- `0x00338946` → RVA `0x00E38D00` (`.data`; read)
- `0x003389AC` → RVA `0x00E37600` (`.data`; read)
- `0x00338B03` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x00338B98` → RVA `0x00E35C00` (`.data`; read)
- `0x00338BD5` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00338710  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
00338715  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
0033871A  53                              push rbx
0033871B  56                              push rsi
0033871C  57                              push rdi
0033871D  41 54                           push r12
0033871F  41 55                           push r13
00338721  41 56                           push r14
00338723  41 57                           push r15
00338725  48 83 EC 40                     sub rsp, 0x40
00338729  4C 8B 41 18                     mov r8, qword ptr [rcx + 0x18]
0033872D  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
00338737  8B 11                           mov edx, dword ptr [rcx]
00338739  33 F6                           xor esi, esi
0033873B  49 C1 E8 09                     shr r8, 9
0033873F  4C 23 C0                        and r8, rax
00338742  89 94 24 90 00 00 00            mov dword ptr [rsp + 0x90], edx
00338749  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
00338753  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
00338758  48 8B C0                        mov rax, rax
0033875B  4C 03 C0                        add r8, rax
0033875E  49 C7 C7 F0 FF FF FF            mov r15, 0xfffffffffffffff0
00338765  83 79 04 05                     cmp dword ptr [rcx + 4], 5
00338769  48 C7 C0 F8 FF FF FF            mov rax, 0xfffffffffffffff8
00338770  4C 0F 44 F8                     cmove r15, rax
00338774  4D 03 F8                        add r15, r8
00338777  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
0033877C  44 0F 20 C2                     mov rdx, cr8
00338780  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00338785  45 33 F6                        xor r14d, r14d
00338788  41 B8 02 00 00 00               mov r8d, 2
0033878E  49 B9 00 00 00 00 00 DE FF FF   movabs r9, 0xffffde0000000000
00338798  49 BA FF FF FF FF FF 00 00 00   movabs r10, 0xffffffffff
003387A2  49 8B 1F                        mov rbx, qword ptr [r15]
003387A5  48 8B F3                        mov rsi, rbx
003387A8  48 C1 EE 0C                     shr rsi, 0xc
003387AC  49 23 F2                        and rsi, r10
003387AF  48 8D 0C 76                     lea rcx, [rsi + rsi*2]
003387B3  48 C1 E1 04                     shl rcx, 4
003387B7  49 8B C1                        mov rax, r9
003387BA  48 03 C8                        add rcx, rax
003387BD  48 89 8C 24 98 00 00 00         mov qword ptr [rsp + 0x98], rcx
003387C5  4C 8B E1                        mov r12, rcx
003387C8  80 FA 02                        cmp dl, 2
003387CB  0F 84 4F 03 00 00               je 0x140338b20
003387D1  48 3B 35 08 55 AF 00            cmp rsi, qword ptr [rip + 0xaf5508]
003387D8  0F 87 BA 03 00 00               ja 0x140338b98
003387DE  45 0F 20 C5                     mov r13, cr8
003387E2  45 0F 22 C0                     mov cr8, r8
003387E6  83 3D 33 E5 C8 00 00            cmp dword ptr [rip + 0xc8e533], 0
003387ED  0F 85 58 03 00 00               jne 0x140338b4b
003387F3  48 8B 41 28                     mov rax, qword ptr [rcx + 0x28]
003387F7  48 8D 79 28                     lea rdi, [rcx + 0x28]
003387FB  48 0F BA E0 36                  bt rax, 0x36
00338800  0F 83 B6 03 00 00               jae 0x140338bbc
00338806  45 33 F6                        xor r14d, r14d
00338809  41 8B F6                        mov esi, r14d
0033880C  F0 48 0F BA 69 18 3F            lock bts qword ptr [rcx + 0x18], 0x3f
00338813  0F 82 E8 02 00 00               jb 0x140338b01
00338819  48 8B 54 24 20                  mov rdx, qword ptr [rsp + 0x20]
0033881E  41 B8 02 00 00 00               mov r8d, 2
00338824  49 B9 00 00 00 00 00 DE FF FF   movabs r9, 0xffffde0000000000
0033882E  49 BA FF FF FF FF FF 00 00 00   movabs r10, 0xffffffffff
00338838  41 80 FD 11                     cmp r13b, 0x11
0033883C  0F 84 60 FF FF FF               je 0x1403387a2
00338842  49 8B 07                        mov rax, qword ptr [r15]
00338845  48 3B D8                        cmp rbx, rax
00338848  0F 85 DD 03 00 00               jne 0x140338c2b
0033884E  4C 8B 8C 24 80 00 00 00         mov r9, qword ptr [rsp + 0x80]
00338856  8B 94 24 90 00 00 00            mov edx, dword ptr [rsp + 0x90]
0033885D  4C 8B 74 24 28                  mov r14, qword ptr [rsp + 0x28]
00338862  41 8B 59 08                     mov ebx, dword ptr [r9 + 8]
00338866  F6 C2 04                        test dl, 4
00338869  0F 84 8B 02 00 00               je 0x140338afa
0033886F  48 8B 07                        mov rax, qword ptr [rdi]
00338872  48 C1 E8 3C                     shr rax, 0x3c
00338876  24 07                           and al, 7
00338878  3C 02                           cmp al, 2
0033887A  0F 85 C1 02 00 00               jne 0x140338b41
00338880  48 8B 07                        mov rax, qword ptr [rdi]
00338883  48 85 C0                        test rax, rax
00338886  78 1C                           js 0x1403388a4
00338888  48 8B 07                        mov rax, qword ptr [rdi]
0033888B  48 0F BA E0 28                  bt rax, 0x28
00338890  72 12                           jb 0x1403388a4
00338892  48 8B 07                        mov rax, qword ptr [rdi]
00338895  48 C1 E8 3C                     shr rax, 0x3c
00338899  24 07                           and al, 7
0033889B  3C 01                           cmp al, 1
0033889D  74 05                           je 0x1403388a4
0033889F  49 8B 44 24 08                  mov rax, qword ptr [r12 + 8]
003388A4  4D 8B 34 24                     mov r14, qword ptr [r12]
003388A8  48 B8 FE FF FF FF FF 0F 00 00   movabs rax, 0xffffffffffe
003388B2  4C 85 F0                        test rax, r14
003388B5  0F 85 2A 02 00 00               jne 0x140338ae5
003388BB  33 F6                           xor esi, esi
003388BD  44 8B F6                        mov r14d, esi
003388C0  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
003388CA  F0 49 21 44 24 18               lock and qword ptr [r12 + 0x18], rax
003388D0  41 80 FD 02                     cmp r13b, 2
003388D4  73 2D                           jae 0x140338903
003388D6  83 3D 43 E4 C8 00 00            cmp dword ptr [rip + 0xc8e443], 0
003388DD  74 1C                           je 0x1403388fb
003388DF  44 0F 20 C1                     mov rcx, cr8
003388E3  41 0F B6 D5                     movzx edx, r13b
003388E7  E8 AC CD 1B 00                  call 0x1404f5698
003388EC  4C 8B 8C 24 80 00 00 00         mov r9, qword ptr [rsp + 0x80]
003388F4  8B 94 24 90 00 00 00            mov edx, dword ptr [rsp + 0x90]
003388FB  41 0F B6 C5                     movzx eax, r13b
003388FF  44 0F 22 C0                     mov cr8, rax
00338903  F6 C2 04                        test dl, 4
00338906  0F 84 2E 02 00 00               je 0x140338b3a
0033890C  41 83 79 04 05                  cmp dword ptr [r9 + 4], 5
00338911  0F 85 09 01 00 00               jne 0x140338a20
00338917  49 83 FE E0                     cmp r14, -0x20
0033891B  0F 85 19 02 00 00               jne 0x140338b3a
00338921  49 8B 41 10                     mov rax, qword ptr [r9 + 0x10]
00338925  4C 8B C6                        mov r8, rsi
00338928  48 85 C0                        test rax, rax
0033892B  74 29                           je 0x140338956
0033892D  48 8B 80 20 02 00 00            mov rax, qword ptr [rax + 0x220]
00338934  0F B7 88 AE 04 00 00            movzx ecx, word ptr [rax + 0x4ae]
0033893B  48 8B 05 46 77 AF 00            mov rax, qword ptr [rip + 0xaf7746]
00338942  4C 8B 34 C8                     mov r14, qword ptr [rax + rcx*8]
00338946  48 8D 05 B3 03 B0 00            lea rax, [rip + 0xb003b3]
0033894D  4C 3B F0                        cmp r14, rax
00338950  0F 85 E4 01 00 00               jne 0x140338b3a
00338956  65 48 8B 14 25 20 00 00 00      mov rdx, qword ptr gs:[0x20]
0033895F  4A 8B 84 C2 30 87 00 00         mov rax, qword ptr [rdx + r8*8 + 0x8730]
00338967  48 85 C0                        test rax, rax
0033896A  0F 85 CA 01 00 00               jne 0x140338b3a
00338970  48 8B 82 C0 00 00 00            mov rax, qword ptr [rdx + 0xc0]
00338977  0F B7 88 8A 00 00 00            movzx ecx, word ptr [rax + 0x8a]
0033897E  3B CB                           cmp ecx, ebx
00338980  0F 85 B4 01 00 00               jne 0x140338b3a
00338986  41 83 79 04 05                  cmp dword ptr [r9 + 4], 5
0033898B  75 67                           jne 0x1403389f4
0033898D  49 C1 E7 19                     shl r15, 0x19
00338991  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
0033899B  48 8B C0                        mov rax, rax
0033899E  48 C1 E0 19                     shl rax, 0x19
003389A2  4C 2B F8                        sub r15, rax
003389A5  49 C1 FF 10                     sar r15, 0x10
003389A9  49 8B CF                        mov rcx, r15
003389AC  48 33 0D 4D EC AF 00            xor rcx, qword ptr [rip + 0xafec4d]
003389B3  33 C0                           xor eax, eax
003389B5  49 89 8F E0 0F 00 00            mov qword ptr [r15 + 0xfe0], rcx
003389BC  49 8D 8F F0 0F 00 00            lea rcx, [r15 + 0xff0]
003389C3  41 C7 87 F8 0F 00 00 01 00 00 00  mov dword ptr [r15 + 0xff8], 1
003389CE  F0 4A 0F B1 8C C2 30 87 00 00   lock cmpxchg qword ptr [rdx + r8*8 + 0x8730], rcx
003389D8  0F 85 5C 01 00 00               jne 0x140338b3a
003389DE  B8 01 00 00 00                  mov eax, 1
003389E3  48 83 C4 40                     add rsp, 0x40
003389E7  41 5F                           pop r15
003389E9  41 5E                           pop r14
003389EB  41 5D                           pop r13
003389ED  41 5C                           pop r12
003389EF  5F                              pop rdi
003389F0  5E                              pop rsi
003389F1  5B                              pop rbx
003389F2  C3                              ret
003389F3  CC                              int3
003389F4  49 8B 49 28                     mov rcx, qword ptr [r9 + 0x28]
003389F8  33 C0                           xor eax, eax
003389FA  F0 4A 0F B1 8C C2 30 87 00 00   lock cmpxchg qword ptr [rdx + r8*8 + 0x8730], rcx
00338A04  BE 00 00 00 00                  mov esi, 0
00338A09  40 0F 94 C6                     sete sil
00338A0D  8B C6                           mov eax, esi
00338A0F  48 83 C4 40                     add rsp, 0x40
00338A13  41 5F                           pop r15
00338A15  41 5E                           pop r14
00338A17  41 5D                           pop r13
00338A19  41 5C                           pop r12
00338A1B  5F                              pop rdi
00338A1C  5E                              pop rsi
00338A1D  5B                              pop rbx
00338A1E  C3                              ret
00338A1F  CC                              int3
00338A20  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
00338A28  4D 8D 67 08                     lea r12, [r15 + 8]
00338A2C  49 8B FF                        mov rdi, r15
00338A2F  4C 8B F6                        mov r14, rsi
00338A32  BB FF FF FF FF                  mov ebx, 0xffffffff
00338A37  48 8D 04 C5 00 00 00 00         lea rax, [rax*8]
00338A3F  48 2B F8                        sub rdi, rax
00338A42  48 83 C7 08                     add rdi, 8
00338A46  49 3B FC                        cmp rdi, r12
00338A49  0F 83 EB 00 00 00               jae 0x140338b3a
00338A4F  49 BD 00 00 00 00 00 DE FF FF   movabs r13, 0xffffde0000000000
00338A59  49 BF FF FF FF FF FF 00 00 00   movabs r15, 0xffffffffff
00338A63  0F 1F 40 00                     nop dword ptr [rax]
00338A67  66 0F 1F 84 00 00 00 00 00      nop word ptr [rax + rax]
00338A70  48 8B 37                        mov rsi, qword ptr [rdi]
00338A73  48 C1 EE 0C                     shr rsi, 0xc
00338A77  49 23 F7                        and rsi, r15
00338A7A  48 8D 14 76                     lea rdx, [rsi + rsi*2]
00338A7E  48 C1 E2 04                     shl rdx, 4
00338A82  49 8B C5                        mov rax, r13
00338A85  48 03 D0                        add rdx, rax
00338A88  4D 85 F6                        test r14, r14
00338A8B  75 18                           jne 0x140338aa5
00338A8D  48 8B 42 28                     mov rax, qword ptr [rdx + 0x28]
00338A91  4C 8B 05 F0 75 AF 00            mov r8, qword ptr [rip + 0xaf75f0]
00338A98  48 C1 E8 2B                     shr rax, 0x2b
00338A9C  25 FF 03 00 00                  and eax, 0x3ff
00338AA1  4D 8B 34 C0                     mov r14, qword ptr [r8 + rax*8]
00338AA5  48 8B CF                        mov rcx, rdi
00338AA8  E8 EB 02 00 00                  call 0x140338d98
00338AAD  48 8B CE                        mov rcx, rsi
00338AB0  83 FB FF                        cmp ebx, -1
00338AB3  0F 85 F8 01 00 00               jne 0x140338cb1
00338AB9  E8 12 02 00 00                  call 0x140338cd0
00338ABE  8B D8                           mov ebx, eax
00338AC0  41 8B 46 04                     mov eax, dword ptr [r14 + 4]
00338AC4  48 83 C7 08                     add rdi, 8
00338AC8  49 3B FC                        cmp rdi, r12
00338ACB  72 A3                           jb 0x140338a70
00338ACD  4C 8B 7C 24 30                  mov r15, qword ptr [rsp + 0x30]
00338AD2  41 B8 01 00 00 00               mov r8d, 1
00338AD8  4C 8B 8C 24 80 00 00 00         mov r9, qword ptr [rsp + 0x80]
00338AE0  E9 61 FE FF FF                  jmp 0x140338946
00338AE5  49 83 E6 FE                     and r14, 0xfffffffffffffffe
00338AE9  48 B8 00 00 00 00 00 F0 FF FF   movabs rax, 0xfffff00000000000
00338AF3  4C 0B F0                        or r14, rax
00338AF6  49 C1 E6 03                     shl r14, 3
00338AFA  33 F6                           xor esi, esi
00338AFC  E9 BF FD FF FF                  jmp 0x1403388c0
00338B01  FF C6                           inc esi
00338B03  85 35 A3 C7 C8 00               test dword ptr [rip + 0xc8c7a3], esi
00338B09  0F 84 C6 00 00 00               je 0x140338bd5
00338B0F  F3 90                           pause
00338B11  48 8B 41 18                     mov rax, qword ptr [rcx + 0x18]
00338B15  48 85 C0                        test rax, rax
00338B18  0F 89 EE FC FF FF               jns 0x14033880c
00338B1E  EB E1                           jmp 0x140338b01
00338B20  41 B5 11                        mov r13b, 0x11
00338B23  41 8B FE                        mov edi, r14d
00338B26  F0 49 0F BA 6C 24 18 3F         lock bts qword ptr [r12 + 0x18], 0x3f
00338B2E  72 50                           jb 0x140338b80
00338B30  49 8D 7C 24 28                  lea rdi, [r12 + 0x28]
00338B35  E9 08 FD FF FF                  jmp 0x140338842
00338B3A  33 C0                           xor eax, eax
00338B3C  E9 CE FE FF FF                  jmp 0x140338a0f
00338B41  49 8B 44 24 08                  mov rax, qword ptr [r12 + 8]
00338B46  E9 35 FD FF FF                  jmp 0x140338880
00338B4B  B2 02                           mov dl, 2
00338B4D  41 0F B6 CD                     movzx ecx, r13b
00338B51  E8 A6 CB 1B 00                  call 0x1404f56fc
00338B56  48 8B 8C 24 98 00 00 00         mov rcx, qword ptr [rsp + 0x98]
00338B5E  41 B8 02 00 00 00               mov r8d, 2
00338B64  49 B9 00 00 00 00 00 DE FF FF   movabs r9, 0xffffde0000000000
00338B6E  49 BA FF FF FF FF FF 00 00 00   movabs r10, 0xffffffffff
00338B78  E9 76 FC FF FF                  jmp 0x1403387f3
00338B7D  0F 1F 00                        nop dword ptr [rax]
00338B80  FF C7                           inc edi
00338B82  85 3D 24 C7 C8 00               test dword ptr [rip + 0xc8c724], edi
00338B88  74 7A                           je 0x140338c04
00338B8A  F3 90                           pause
00338B8C  49 8B 44 24 18                  mov rax, qword ptr [r12 + 0x18]
00338B91  48 85 C0                        test rax, rax
00338B94  79 90                           jns 0x140338b26
00338B96  EB E8                           jmp 0x140338b80
00338B98  48 8B 05 61 D0 AF 00            mov rax, qword ptr [rip + 0xafd061]
00338B9F  48 3B F0                        cmp rsi, rax
00338BA2  0F 82 D1 00 00 00               jb 0x140338c79
00338BA8  48 05 00 08 00 00               add rax, 0x800
00338BAE  48 3B F0                        cmp rsi, rax
00338BB1  0F 82 27 FC FF FF               jb 0x1403387de
00338BB7  E9 BD 00 00 00                  jmp 0x140338c79
00338BBC  48 8B CE                        mov rcx, rsi
00338BBF  E8 7C 06 F8 FF                  call 0x1402b9240
00338BC4  85 C0                           test eax, eax
00338BC6  74 79                           je 0x140338c41
00338BC8  48 8B 8C 24 98 00 00 00         mov rcx, qword ptr [rsp + 0x98]
00338BD0  E9 31 FC FF FF                  jmp 0x140338806
00338BD5  8B 05 DD DE C8 00               mov eax, dword ptr [rip + 0xc8dedd]
00338BDB  A8 40                           test al, 0x40
00338BDD  0F 84 2C FF FF FF               je 0x140338b0f
00338BE3  E8 A8 68 FD FF                  call 0x14030f490
00338BE8  84 C0                           test al, al
00338BEA  0F 84 B4 00 00 00               je 0x140338ca4
00338BF0  8B CE                           mov ecx, esi
00338BF2  E8 69 68 FD FF                  call 0x14030f460
00338BF7  48 8B 8C 24 98 00 00 00         mov rcx, qword ptr [rsp + 0x98]
00338BFF  E9 0D FF FF FF                  jmp 0x140338b11
00338C04  8B 05 AE DE C8 00               mov eax, dword ptr [rip + 0xc8deae]
00338C0A  A8 40                           test al, 0x40
00338C0C  0F 84 78 FF FF FF               je 0x140338b8a
00338C12  E8 79 68 FD FF                  call 0x14030f490
00338C17  84 C0                           test al, al
00338C19  0F 84 6B FF FF FF               je 0x140338b8a
00338C1F  8B CF                           mov ecx, edi
00338C21  E8 3A 68 FD FF                  call 0x14030f460
00338C26  E9 61 FF FF FF                  jmp 0x140338b8c
00338C2B  41 0F B6 D5                     movzx edx, r13b
00338C2F  49 8B CC                        mov rcx, r12
00338C32  E8 A9 17 FE FF                  call 0x14031a3e0
00338C37  48 8B 54 24 20                  mov rdx, qword ptr [rsp + 0x20]
00338C3C  E9 47 FB FF FF                  jmp 0x140338788
00338C41  83 3D D8 E0 C8 00 00            cmp dword ptr [rip + 0xc8e0d8], 0
00338C48  74 27                           je 0x140338c71
00338C4A  44 0F 20 C1                     mov rcx, cr8
00338C4E  41 0F B6 D5                     movzx edx, r13b
00338C52  E8 41 CA 1B 00                  call 0x1404f5698
00338C57  41 B8 02 00 00 00               mov r8d, 2
00338C5D  49 B9 00 00 00 00 00 DE FF FF   movabs r9, 0xffffde0000000000
00338C67  49 BA FF FF FF FF FF 00 00 00   movabs r10, 0xffffffffff
00338C71  41 0F B6 C5                     movzx eax, r13b
00338C75  44 0F 22 C0                     mov cr8, rax
00338C79  49 8B 1F                        mov rbx, qword ptr [r15]
00338C7C  48 8B F3                        mov rsi, rbx
00338C7F  48 C1 EE 0C                     shr rsi, 0xc
00338C83  49 23 F2                        and rsi, r10
00338C86  48 8D 0C 76                     lea rcx, [rsi + rsi*2]
00338C8A  48 C1 E1 04                     shl rcx, 4
00338C8E  49 8B C1                        mov rax, r9
00338C91  48 03 C8                        add rcx, rax
00338C94  48 89 8C 24 98 00 00 00         mov qword ptr [rsp + 0x98], rcx
00338C9C  4C 8B E1                        mov r12, rcx
00338C9F  E9 2D FB FF FF                  jmp 0x1403387d1
00338CA4  48 8B 8C 24 98 00 00 00         mov rcx, qword ptr [rsp + 0x98]
00338CAC  E9 5E FE FF FF                  jmp 0x140338b0f
00338CB1  E8 1A 00 00 00                  call 0x140338cd0
00338CB6  E9 05 FE FF FF                  jmp 0x140338ac0
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiAddKernelStackToPrcbCache(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p100;
    unsigned __int64 v_stack_p110;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;
    unsigned __int64 v_stack_p98;
    unsigned __int64 v_stack_pA8;
    unsigned __int64 v_stack_pF8;

    v_stack_p10 = a2;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (64);
    v_rsi = 0;
    a3 = (*(unsigned __int64 *)(a1 + 24)) >> (9);
    a3 = (a3) & (result);
    v_stack_p18 = (unsigned int)((unsigned int)(*(unsigned int *)(a1)));
    v_stack_m50 = 0;
    a3 = (a3) + (result);
    v_r15 = -16;
    if ((*(unsigned int *)(a1 + 4)) == 5) { v_r15 = -8; }
    v_r15 = (v_r15) + (a3);
    v_stack_m48 = v_r15;
    v_stack_m58 = v_cr8;
    v_r14 = 0;
loc_00338788:
loc_003387A2:
    v_rsi = (*(unsigned __int64 *)(v_r15)) >> (12);
    v_rsi = (v_rsi) & (v_r10);
    a1 = (v_rsi + v_rsi * 2) << (4);
    a1 = (a1) + (a4);
    v_stack_p20 = a1;
    if (((unsigned __int8)(v_cr8)) == 2) goto loc_00338B20;
loc_003387D1:
    if (v_rsi > (*(unsigned __int64 *)(v_rip + 11490568))) goto loc_00338B98;
loc_003387DE:
    if ((*(unsigned int *)(v_rip + 13165875)) != 0) goto loc_00338B4B;
loc_003387F3:
    if ((*(unsigned int *)(v_rip + 13165875)) >= 0) goto loc_00338BBC;
loc_00338806:
    v_r14 = 0;
loc_0033880C:
    if (condition_is_below) goto loc_00338B01;
    if (((unsigned __int8)(v_cr8)) == 17) goto loc_003387A2;
loc_00338842:
    if ((*(unsigned __int64 *)(v_r15)) != (*(unsigned __int64 *)(v_r15))) goto loc_00338C2B;
    if ((((unsigned __int8)((unsigned int)(v_stack_p18))) & (4)) == 0) goto loc_00338AFA;
    result = (*(unsigned __int64 *)(a1 + 40)) >> (60);
    result = (unsigned __int8)((result) & (7));
    if (((unsigned __int8)(result)) != 2) goto loc_00338B41;
loc_00338880:
    if (sign_flag) goto loc_003388A4;
    if (condition_is_below) goto loc_003388A4;
    result = (*(unsigned __int64 *)(a1 + 40)) >> (60);
    result = (unsigned __int8)((result) & (7));
    if (((unsigned __int8)(result)) != 1) {
        result = *(unsigned __int64 *)(a1 + 8);
    }
    if (((result) & (*(unsigned __int64 *)(a1))) != 0) goto loc_00338AE5;
    v_rsi = 0;
loc_003388C0:
    if (((unsigned __int8)(v_cr8)) >= 2) goto loc_00338903;
    if ((*(unsigned int *)(v_rip + 13165635)) != 0) {
        a1 = 2;
        a2 = (unsigned __int8)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, 2, v_stack_p8);
        a4 = v_stack_p8;
        a2 = v_stack_p18;
    }
loc_00338903:
    if ((((unsigned __int8)(a2)) & (4)) == 0) goto loc_00338B3A;
    if ((*(unsigned int *)(a4 + 4)) != 5) goto loc_00338A20;
    if (0 != -32) goto loc_00338B3A;
    if (*(unsigned __int64 *)(a4 + 16) == 0) goto loc_00338956;
loc_00338946:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11499334) + *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 16) + 544) + 1198) * 8)) != (v_rip + 11535283)) goto loc_00338B3A;
loc_00338956:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 0 * 8 + 34608) != 0) goto loc_00338B3A;
    if (((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 192) + 138))) != ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 8))))) goto loc_00338B3A;
    if ((*(unsigned int *)(a4 + 4)) != 5) goto loc_003389F4;
    v_r15 = (v_r15) << (25);
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 192)) << (25);
    v_r15 = (v_r15) - (result);
    v_r15 = (v_r15) >> (16);
    a1 = (v_r15) ^ (*(unsigned __int64 *)(v_rip + 11529293));
    result = 0;
    *(unsigned __int64 *)(v_r15 + 4064) = a1;
    *(unsigned int *)(v_r15 + 4088) = 1;
    if (condition_is_not_equal) goto loc_00338B3A;
    v_rsp = (v_rsp) + (64);
    return 1;
loc_003389F4:
    result = 0;
    v_rsi = (condition_is_equal) ? 1 : 0;
loc_00338A0F:
    v_rsp = (v_rsp) + (64);
    return (unsigned int)((unsigned int)(v_rsi));
loc_00338A20:
    v_rdi = (v_r15) - (v_stack_p100 * 8);
    v_rdi = (v_rdi) + (8);
    if (v_rdi >= (v_r15 + 8)) goto loc_00338B3A;
loc_00338A70:
    v_rsi = (*(unsigned __int64 *)(v_rdi)) >> (12);
    v_rsi = (v_rsi) & (v_r15);
    a2 = (v_rsi + v_rsi * 2) << (4);
    a2 = (a2) + (v_cr8);
    result = v_cr8;
    v_r14 = v_rsi;
    if (v_rsi == 0) {
        result = *(unsigned __int64 *)(a2 + 40);
        a3 = *(unsigned __int64 *)(v_rip + 11498992);
        result = (result) >> (43);
        result = (unsigned int)((result) & (0x3FFULL));
        v_r14 = *(unsigned __int64 *)(a3 + result * 8);
    }
    result = MiValidateKernelShadowStackPage(v_rdi, a2, a3, a4);
    if (((unsigned int)((unsigned int)(0xFFFFFFFFULL))) != -1) goto loc_00338CB1;
    result = MiPageToNode(v_rsi, a2, a3, a4);
loc_00338AC0:
    v_rdi = (v_rdi) + (8);
    if (v_rdi < (v_r15 + 8)) goto loc_00338A70;
    goto loc_00338946;
loc_00338AE5:
    v_r14 = (v_r14) & (-2);
    v_r14 = (v_r14) | ((unsigned int)(*(unsigned int *)(v_r14 + 4)));
    v_r14 = (v_r14) << (3);
loc_00338AFA:
    v_rsi = 0;
    goto loc_003388C0;
loc_00338B01:
    v_rsi = (unsigned int)((v_rsi) + 1);
    if (((*(unsigned int *)(v_rip + 13158307)) & ((unsigned int)(v_rsi))) == 0) goto loc_00338BD5;
loc_00338B0F:
loc_00338B11:
    if (!sign_flag) goto loc_0033880C;
    goto loc_00338B01;
loc_00338B20:
loc_00338B26:
    if (condition_is_below) goto loc_00338B80;
    goto loc_00338842;
loc_00338B3A:
    result = 0;
    goto loc_00338A0F;
loc_00338B41:
    goto loc_00338880;
loc_00338B4B:
    result = KiRaiseIrqlProcessIrqlFlags(17, 2, 1, v_stack_pF8);
    goto loc_003387F3;
loc_00338B80:
    v_rdi = (unsigned int)((v_r15 + 8 + 40) + 1);
    if (((*(unsigned int *)(v_rip + 13158180)) & ((unsigned int)(v_rdi))) == 0) goto loc_00338C04;
loc_00338B8A:
loc_00338B8C:
    if (!sign_flag) goto loc_00338B26;
    goto loc_00338B80;
loc_00338B98:
    if (v_rsi < (*(unsigned __int64 *)(v_rip + 11522145))) goto loc_00338C79;
    result = (*(unsigned __int64 *)(v_rip + 11522145)) + (0x800ULL);
    if (v_rsi < result) goto loc_003387DE;
    goto loc_00338C79;
loc_00338BBC:
    result = MiIsDecayPfn(v_rsi, 2, 2, v_stack_pF8);
    if ((unsigned int)(result) == 0) goto loc_00338C41;
    goto loc_00338806;
loc_00338BD5:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13164253)))) & (64)) == 0) goto loc_00338B0F;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_stack_p110, 2, 2, v_stack_pF8);
    if ((unsigned __int8)(result) == 0) goto loc_00338CA4;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rsi)), 2, 2, v_stack_pF8);
    goto loc_00338B11;
loc_00338C04:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13164206)))) & (64)) == 0) goto loc_00338B8A;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_stack_p110, 2, 2, v_stack_pF8);
    if ((unsigned __int8)(result) == 0) goto loc_00338B8A;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rdi)), 2, 2, v_stack_pF8);
    goto loc_00338B8C;
loc_00338C2B:
    result = MiUnlockPage(v_r15 + 8, 17, 2, v_stack_pF8);
    goto loc_00338788;
loc_00338C41:
    if ((*(unsigned int *)(v_rip + 13164760)) != 0) {
        a1 = (unsigned __int8)(v_cr8);
        a2 = 17;
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, 2, v_stack_pF8);
        a3 = 2;
    }
loc_00338C79:
    v_rsi = (*(unsigned __int64 *)(v_stack_pA8)) >> (12);
    v_rsi = (v_rsi) & (v_r10);
    a1 = (v_rsi + v_rsi * 2) << (4);
    a1 = (a1) + (v_stack_pF8);
    v_stack_p110 = a1;
    goto loc_003387D1;
loc_00338CA4:
    goto loc_00338B0F;
loc_00338CB1:
    result = MiPageToNode(v_stack_p110, a2, a3, v_stack_pF8);
    goto loc_00338AC0;
}
```

## 5. (Beta) C Style

```c
int64_t MiAddKernelStackToPrcbCache(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_p10;
    uint64_t v_stack_p100;
    uint64_t v_stack_p110;
    uint32_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;
    uint64_t v_stack_p98;
    uint64_t v_stack_pA8;
    uint64_t v_stack_pF8;

    v_stack_p10 = Arg2;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (64);
    local_rsi = 0;
    a3 = (*(uint64_t *)(arg1 + 0x18)) >> (9);
    a3 = (a3) & (result);
    v_stack_p18 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1)));
    v_stack_m50 = 0;
    a3 = (a3) + (result);
    local_r15 = -16;
    if ((*(uint32_t *)(arg1 + 0x4)) == 5) { local_r15 = -8; }
    local_r15 = (local_r15) + (a3);
    v_stack_m48 = local_r15;
    v_stack_m58 = v_cr8;
    local_r14 = 0;
loc_00338788:
loc_003387A2:
    local_rsi = (*(uint64_t *)(local_r15)) >> (12);
    local_rsi = (local_rsi) & (local_r10);
    Arg1 = (local_rsi + local_rsi * 2) << (4);
    Arg1 = (Arg1) + (a4);
    v_stack_p20 = Arg1;
    if (((uint8_t)(v_cr8)) == 2) goto loc_00338B20;
loc_003387D1:
    if (local_rsi > (*(uint64_t *)(v_rip + 0xAF5508))) goto loc_00338B98;
loc_003387DE:
    if ((*(uint32_t *)(v_rip + 0xC8E533)) != 0) goto loc_00338B4B;
loc_003387F3:
    if ((*(uint32_t *)(v_rip + 0xC8E533)) >= 0) goto loc_00338BBC;
loc_00338806:
    local_r14 = 0;
loc_0033880C:
    if (condition_is_below) goto loc_00338B01;
    if (((uint8_t)(v_cr8)) == 17) goto loc_003387A2;
loc_00338842:
    if ((*(uint64_t *)(local_r15)) != (*(uint64_t *)(local_r15))) goto loc_00338C2B;
    if ((((uint8_t)((uint32_t)(v_stack_p18))) & (4)) == 0) goto loc_00338AFA;
    result = (*(uint64_t *)(arg1 + 0x28)) >> (60);
    result = (uint8_t)((result) & (7));
    if (((uint8_t)(result)) != 2) goto loc_00338B41;
loc_00338880:
    if (sign_flag) goto loc_003388A4;
    if (condition_is_below) goto loc_003388A4;
    result = (*(uint64_t *)(arg1 + 0x28)) >> (60);
    result = (uint8_t)((result) & (7));
    if (((uint8_t)(result)) != 1) {
        result = *(uint64_t *)(arg1 + 0x8);
    }
    if (((result) & (*(uint64_t *)(arg1))) != 0) goto loc_00338AE5;
    local_rsi = 0;
loc_003388C0:
    if (((uint8_t)(v_cr8)) >= 2) goto loc_00338903;
    if ((*(uint32_t *)(v_rip + 0xC8E443)) != 0) {
        Arg1 = 2;
        Arg2 = (uint8_t)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, 2, v_stack_p8);
        a4 = v_stack_p8;
        Arg2 = v_stack_p18;
    }
loc_00338903:
    if ((((uint8_t)(Arg2)) & (4)) == 0) goto loc_00338B3A;
    if ((*(uint32_t *)(a4 + 0x4)) != 5) goto loc_00338A20;
    if (0 != -32) goto loc_00338B3A;
    if (*(uint64_t *)(a4 + 0x10) == 0) goto loc_00338956;
loc_00338946:
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xAF7746) + *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(a4 + 0x10) + 0x220) + 0x4AE) * 8)) != (v_rip + 11535283)) goto loc_00338B3A;
loc_00338956:
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x0 * 8 + 0x8730) != 0) goto loc_00338B3A;
    if (((uint32_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xC0) + 0x8A))) != ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x8))))) goto loc_00338B3A;
    if ((*(uint32_t *)(a4 + 0x4)) != 5) goto loc_003389F4;
    local_r15 = (local_r15) << (25);
    result = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xC0)) << (25);
    local_r15 = (local_r15) - (result);
    local_r15 = (local_r15) >> (16);
    Arg1 = (local_r15) ^ (*(uint64_t *)(v_rip + 0xAFEC4D));
    result = 0;
    *(void **)(local_r15 + 0xFE0) = Arg1;
    *(uint32_t *)(local_r15 + 0xFF8) = 1;
    if (condition_is_not_equal) goto loc_00338B3A;
    local_rsp = (local_rsp) + (64);
    return 1;
loc_003389F4:
    result = 0;
    local_rsi = (condition_is_equal) ? 1 : 0;
loc_00338A0F:
    local_rsp = (local_rsp) + (64);
    return (uint32_t)((uint32_t)(local_rsi));
loc_00338A20:
    local_rdi = (local_r15) - (v_stack_p100 * 8);
    local_rdi = (local_rdi) + (8);
    if (local_rdi >= (local_r15 + 8)) goto loc_00338B3A;
loc_00338A70:
    local_rsi = (*(uint64_t *)(local_rdi)) >> (12);
    local_rsi = (local_rsi) & (local_r15);
    Arg2 = (local_rsi + local_rsi * 2) << (4);
    Arg2 = (Arg2) + (v_cr8);
    result = v_cr8;
    local_r14 = local_rsi;
    if (local_rsi == 0) {
        result = *(uint64_t *)(Arg2 + 0x28);
        a3 = *(uint64_t *)(v_rip + 0xAF75F0);
        result = (result) >> (43);
        result = (uint32_t)((result) & (0x3FFULL));
        local_r14 = *(uint64_t *)(a3 + result * 8);
    }
    result = MiValidateKernelShadowStackPage(local_rdi, Arg2, a3, a4);
    if (((uint32_t)((uint32_t)(0xFFFFFFFFULL))) != -1) goto loc_00338CB1;
    result = MiPageToNode(local_rsi, Arg2, a3, a4);
loc_00338AC0:
    local_rdi = (local_rdi) + (8);
    if (local_rdi < (local_r15 + 8)) goto loc_00338A70;
    goto loc_00338946;
loc_00338AE5:
    local_r14 = (local_r14) & (-2);
    local_r14 = (local_r14) | ((uint32_t)(*(uint32_t *)(local_r14 + 0x4)));
    local_r14 = (local_r14) << (3);
loc_00338AFA:
    local_rsi = 0;
    goto loc_003388C0;
loc_00338B01:
    local_rsi = (uint32_t)((local_rsi) + 1);
    if (((*(uint32_t *)(v_rip + 0xC8C7A3)) & ((uint32_t)(local_rsi))) == 0) goto loc_00338BD5;
loc_00338B0F:
loc_00338B11:
    if (!sign_flag) goto loc_0033880C;
    goto loc_00338B01;
loc_00338B20:
loc_00338B26:
    if (condition_is_below) goto loc_00338B80;
    goto loc_00338842;
loc_00338B3A:
    result = 0;
    goto loc_00338A0F;
loc_00338B41:
    goto loc_00338880;
loc_00338B4B:
    result = KiRaiseIrqlProcessIrqlFlags(17, 2, 1, v_stack_pF8);
    goto loc_003387F3;
loc_00338B80:
    local_rdi = (uint32_t)((local_r15 + 8 + 40) + 1);
    if (((*(uint32_t *)(v_rip + 0xC8C724)) & ((uint32_t)(local_rdi))) == 0) goto loc_00338C04;
loc_00338B8A:
loc_00338B8C:
    if (!sign_flag) goto loc_00338B26;
    goto loc_00338B80;
loc_00338B98:
    if (local_rsi < (*(uint64_t *)(v_rip + 0xAFD061))) goto loc_00338C79;
    result = (*(uint64_t *)(v_rip + 0xAFD061)) + (0x800ULL);
    if (local_rsi < result) goto loc_003387DE;
    goto loc_00338C79;
loc_00338BBC:
    result = MiIsDecayPfn(local_rsi, 2, 2, v_stack_pF8);
    if ((uint32_t)(result) == 0) goto loc_00338C41;
    goto loc_00338806;
loc_00338BD5:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC8DEDD)))) & (64)) == 0) goto loc_00338B0F;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_stack_p110, 2, 2, v_stack_pF8);
    if ((uint8_t)(result) == 0) goto loc_00338CA4;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rsi)), 2, 2, v_stack_pF8);
    goto loc_00338B11;
loc_00338C04:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC8DEAE)))) & (64)) == 0) goto loc_00338B8A;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_stack_p110, 2, 2, v_stack_pF8);
    if ((uint8_t)(result) == 0) goto loc_00338B8A;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rdi)), 2, 2, v_stack_pF8);
    goto loc_00338B8C;
loc_00338C2B:
    result = MiUnlockPage(local_r15 + 8, 17, 2, v_stack_pF8);
    goto loc_00338788;
loc_00338C41:
    if ((*(uint32_t *)(v_rip + 0xC8E0D8)) != 0) {
        Arg1 = (uint8_t)(v_cr8);
        Arg2 = 17;
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, 2, v_stack_pF8);
        a3 = 2;
    }
loc_00338C79:
    local_rsi = (*(uint64_t *)(v_stack_pA8)) >> (12);
    local_rsi = (local_rsi) & (local_r10);
    Arg1 = (local_rsi + local_rsi * 2) << (4);
    Arg1 = (Arg1) + (v_stack_pF8);
    v_stack_p110 = Arg1;
    goto loc_003387D1;
loc_00338CA4:
    goto loc_00338B0F;
loc_00338CB1:
    result = MiPageToNode(v_stack_p110, Arg2, a3, v_stack_pF8);
    goto loc_00338AC0;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x4` | `32` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00338710&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
