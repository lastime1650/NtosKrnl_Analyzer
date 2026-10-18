# MiBuildMdlForMappedFileFault

- RVA: `0x0036380C`–`0x00363DD0` (길이 `1,476` bytes)
- VA: `0x000000014036380C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00079E78`
- 디코드: `382`개 명령, `1,476/1,476` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **11**; 고유 호출 대상: **11**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00363880` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x003638AE` → [RtlSetAllBits](RtlSetAllBits_function_00362490.md) (function, `0x00362490`)
- `0x003639A4` → [MiGetHardFaultPages](MiGetHardFaultPages_function_0036200C.md) (function, `0x0036200C`)
- `0x003639C4` → [MiProtectionToCacheAttribute](../2B/MiProtectionToCacheAttribute_function_002B8530.md) (function, `0x002B8530`)
- `0x00363A06` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00363B32` → [RtlSetBits](../3E/RtlSetBits_function_003E1610.md) (function, `0x003E1610`)
- `0x00363BC4` → [MiAdvanceFaultList](MiAdvanceFaultList_function_003637A0.md) (function, `0x003637A0`)
- `0x00363BE4` → [MiInitializeHardFaultPfn](MiInitializeHardFaultPfn_function_00363DD8.md) (function, `0x00363DD8`)
- `0x00363BF7` → [MiMakeTransitionPte](MiMakeTransitionPte_function_00363F70.md) (function, `0x00363F70`)
- `0x00363D7B` → [MiReduceMappedFileReadBehind](../3E/MiReduceMappedFileReadBehind_function_003E1B64.md) (function, `0x003E1B64`)
- `0x00363D97` → [MiReduceMappedFileReadAhead](../3E/MiReduceMappedFileReadAhead_function_003E0A54.md) (function, `0x003E0A54`)

### Direct callers
- [MiResolveMappedFileFault](MiResolveMappedFileFault_function_0036B640.md) at `0x0036BAC2`

### Static image references
- `0x00363828` → RVA `0x00E0A740` (`.data`; read)
- `0x00363C63` → RVA `0x00E37438` (`.data`; read)
- `0x00363D1D` → RVA `0x00E2DC80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0036380C  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
00363811  55                              push rbp
00363812  56                              push rsi
00363813  57                              push rdi
00363814  41 54                           push r12
00363816  41 55                           push r13
00363818  41 56                           push r14
0036381A  41 57                           push r15
0036381C  48 8D 6C 24 E0                  lea rbp, [rsp - 0x20]
00363821  48 81 EC 20 01 00 00            sub rsp, 0x120
00363828  48 8B 05 11 6F AA 00            mov rax, qword ptr [rip + 0xaa6f11]
0036382F  48 33 C4                        xor rax, rsp
00363832  48 89 45 10                     mov qword ptr [rbp + 0x10], rax
00363836  48 8B 85 98 00 00 00            mov rax, qword ptr [rbp + 0x98]
0036383D  49 8B F0                        mov rsi, r8
00363840  4C 8B BD 88 00 00 00            mov r15, qword ptr [rbp + 0x88]
00363847  4C 8B F2                        mov r14, rdx
0036384A  4C 8B A5 A0 00 00 00            mov r12, qword ptr [rbp + 0xa0]
00363851  48 8B F9                        mov rdi, rcx
00363854  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
00363858  4D 8B E9                        mov r13, r9
0036385B  48 8B 85 A8 00 00 00            mov rax, qword ptr [rbp + 0xa8]
00363862  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00363867  33 C0                           xor eax, eax
00363869  48 89 54 24 78                  mov qword ptr [rsp + 0x78], rdx
0036386E  33 D2                           xor edx, edx
00363870  48 89 4C 24 70                  mov qword ptr [rsp + 0x70], rcx
00363875  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00363879  89 45 C4                        mov dword ptr [rbp - 0x3c], eax
0036387C  44 8D 40 4C                     lea r8d, [rax + 0x4c]
00363880  E8 BB 33 36 00                  call 0x1406c6c40
00363885  48 8B 87 E8 00 00 00            mov rax, qword ptr [rdi + 0xe8]
0036388C  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00363890  48 8B 9F A8 00 00 00            mov rbx, qword ptr [rdi + 0xa8]
00363897  48 89 45 98                     mov qword ptr [rbp - 0x68], rax
0036389B  48 8D 45 D0                     lea rax, [rbp - 0x30]
0036389F  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
003638A3  48 89 5D A0                     mov qword ptr [rbp - 0x60], rbx
003638A7  C7 45 C0 00 02 00 00            mov dword ptr [rbp - 0x40], 0x200
003638AE  E8 DD EB FF FF                  call 0x140362490
003638B3  48 83 65 90 00                  and qword ptr [rbp - 0x70], 0
003638B8  33 FF                           xor edi, edi
003638BA  4D 8B C6                        mov r8, r14
003638BD  4C 3B F6                        cmp r14, rsi
003638C0  77 34                           ja 0x1403638f6
003638C2  49 8B 00                        mov rax, qword ptr [r8]
003638C5  48 3B C3                        cmp rax, rbx
003638C8  75 23                           jne 0x1403638ed
003638CA  41 8B D0                        mov edx, r8d
003638CD  C1 EA 03                        shr edx, 3
003638D0  81 E2 FF 01 00 00               and edx, 0x1ff
003638D6  8B CA                           mov ecx, edx
003638D8  83 E2 07                        and edx, 7
003638DB  48 C1 E9 03                     shr rcx, 3
003638DF  48 03 4D C8                     add rcx, qword ptr [rbp - 0x38]
003638E3  0F BE 01                        movsx eax, byte ptr [rcx]
003638E6  0F B3 D0                        btr eax, edx
003638E9  88 01                           mov byte ptr [rcx], al
003638EB  FF C7                           inc edi
003638ED  49 83 C0 08                     add r8, 8
003638F1  4C 3B C6                        cmp r8, rsi
003638F4  76 CC                           jbe 0x1403638c2
003638F6  8B D7                           mov edx, edi
003638F8  0F 57 C0                        xorps xmm0, xmm0
003638FB  48 3B 95 80 00 00 00            cmp rdx, qword ptr [rbp + 0x80]
00363902  0F 11 44 24 50                  movups xmmword ptr [rsp + 0x50], xmm0
00363907  48 0F 47 95 80 00 00 00         cmova rdx, qword ptr [rbp + 0x80]
0036390F  45 33 F6                        xor r14d, r14d
00363912  33 C0                           xor eax, eax
00363914  4C 89 74 24 60                  mov qword ptr [rsp + 0x60], r14
00363919  49 B8 00 00 00 00 00 DE FF FF   movabs r8, 0xffffde0000000000
00363923  49 83 FF FF                     cmp r15, -1
00363927  74 37                           je 0x140363960
00363929  4B 8D 0C 7F                     lea rcx, [r15 + r15*2]
0036392D  48 C1 E1 04                     shl rcx, 4
00363931  49 8B C0                        mov rax, r8
00363934  48 03 C8                        add rcx, rax
00363937  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
0036393C  48 89 4C 24 50                  mov qword ptr [rsp + 0x50], rcx
00363941  48 89 01                        mov qword ptr [rcx], rax
00363944  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
00363949  48 85 C0                        test rax, rax
0036394C  48 0F 44 C1                     cmove rax, rcx
00363950  49 FF C6                        inc r14
00363953  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00363958  49 8B C6                        mov rax, r14
0036395B  4C 89 74 24 60                  mov qword ptr [rsp + 0x60], r14
00363960  48 3B C2                        cmp rax, rdx
00363963  0F 84 CA 02 00 00               je 0x140363c33
00363969  48 8B C3                        mov rax, rbx
0036396C  48 0F BA E3 0A                  bt rbx, 0xa
00363971  0F 83 A6 03 00 00               jae 0x140363d1d
00363977  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
0036397C  4D 8B C5                        mov r8, r13
0036397F  48 8B 75 88                     mov rsi, qword ptr [rbp - 0x78]
00363983  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
00363988  4C 8B CE                        mov r9, rsi
0036398B  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00363990  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
00363995  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
0036399A  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0036399F  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
003639A4  E8 63 E6 FF FF                  call 0x14036200c
003639A9  4C 8B 74 24 60                  mov r14, qword ptr [rsp + 0x60]
003639AE  44 89 75 84                     mov dword ptr [rbp - 0x7c], r14d
003639B2  45 8B FE                        mov r15d, r14d
003639B5  44 3B F7                        cmp r14d, edi
003639B8  0F 85 4A 03 00 00               jne 0x140363d08
003639BE  8B 8D 90 00 00 00               mov ecx, dword ptr [rbp + 0x90]
003639C4  E8 67 4B F5 FF                  call 0x1402b8530
003639C9  4C 8B 64 24 70                  mov r12, qword ptr [rsp + 0x70]
003639CE  45 33 C9                        xor r9d, r9d
003639D1  8B 7D C0                        mov edi, dword ptr [rbp - 0x40]
003639D4  89 45 80                        mov dword ptr [rbp - 0x80], eax
003639D7  49 8D B4 24 40 01 00 00         lea rsi, [r12 + 0x140]
003639DF  85 FF                           test edi, edi
003639E1  75 44                           jne 0x140363a27
003639E3  49 2B F4                        sub rsi, r12
003639E6  41 8B C7                        mov eax, r15d
003639E9  48 81 EE 40 01 00 00            sub rsi, 0x140
003639F0  48 C1 FE 03                     sar rsi, 3
003639F4  C1 E6 0C                        shl esi, 0xc
003639F7  41 89 B4 24 B8 00 00 00         mov dword ptr [r12 + 0xb8], esi
003639FF  48 8B 4D 10                     mov rcx, qword ptr [rbp + 0x10]
00363A03  48 33 CC                        xor rcx, rsp
00363A06  E8 35 8C 34 00                  call 0x1406ac640
00363A0B  48 8B 9C 24 70 01 00 00         mov rbx, qword ptr [rsp + 0x170]
00363A13  48 81 C4 20 01 00 00            add rsp, 0x120
00363A1A  41 5F                           pop r15
00363A1C  41 5E                           pop r14
00363A1E  41 5D                           pop r13
00363A20  41 5C                           pop r12
00363A22  5F                              pop rdi
00363A23  5E                              pop rsi
00363A24  5D                              pop rbp
00363A25  C3                              ret
00363A26  CC                              int3
00363A27  4C 8B 5C 24 78                  mov r11, qword ptr [rsp + 0x78]
00363A2C  49 81 E3 00 F0 FF FF            and r11, 0xfffffffffffff000
00363A33  4C 89 5C 24 78                  mov qword ptr [rsp + 0x78], r11
00363A38  83 64 24 40 00                  and dword ptr [rsp + 0x40], 0
00363A3D  45 33 ED                        xor r13d, r13d
00363A40  4C 89 6C 24 48                  mov qword ptr [rsp + 0x48], r13
00363A45  41 3B F9                        cmp edi, r9d
00363A48  0F 86 6B 03 00 00               jbe 0x140363db9
00363A4E  4C 8B 5D C8                     mov r11, qword ptr [rbp - 0x38]
00363A52  8D 4F FF                        lea ecx, [rdi - 1]
00363A55  48 C1 E9 05                     shr rcx, 5
00363A59  41 8B C1                        mov eax, r9d
00363A5C  48 C1 E8 05                     shr rax, 5
00363A60  4D 8D 14 8B                     lea r10, [r11 + rcx*4]
00363A64  41 8B C9                        mov ecx, r9d
00363A67  83 E1 1F                        and ecx, 0x1f
00363A6A  4D 8D 04 83                     lea r8, [r11 + rax*4]
00363A6E  41 8B 10                        mov edx, dword ptr [r8]
00363A71  41 8D 45 01                     lea eax, [r13 + 1]
00363A75  D3 E0                           shl eax, cl
00363A77  FF C8                           dec eax
00363A79  0B D0                           or edx, eax
00363A7B  49 8D 40 04                     lea rax, [r8 + 4]
00363A7F  F7 D2                           not edx
00363A81  85 D2                           test edx, edx
00363A83  75 16                           jne 0x140363a9b
00363A85  49 3B C2                        cmp rax, r10
00363A88  0F 87 60 02 00 00               ja 0x140363cee
00363A8E  49 83 C0 04                     add r8, 4
00363A92  48 83 C0 04                     add rax, 4
00363A96  41 8B 10                        mov edx, dword ptr [r8]
00363A99  EB E4                           jmp 0x140363a7f
00363A9B  8B C2                           mov eax, edx
00363A9D  4D 8B F8                        mov r15, r8
00363AA0  4D 2B FB                        sub r15, r11
00363AA3  49 C1 FF 02                     sar r15, 2
00363AA7  48 0F BC C8                     bsf rcx, rax
00363AAB  41 C1 E7 05                     shl r15d, 5
00363AAF  44 03 F9                        add r15d, ecx
00363AB2  89 4C 24 40                     mov dword ptr [rsp + 0x40], ecx
00363AB6  4C 89 7C 24 68                  mov qword ptr [rsp + 0x68], r15
00363ABB  44 3B FF                        cmp r15d, edi
00363ABE  0F 87 2A 02 00 00               ja 0x140363cee
00363AC4  B8 01 00 00 00                  mov eax, 1
00363AC9  D3 E0                           shl eax, cl
00363ACB  FF C8                           dec eax
00363ACD  0B D0                           or edx, eax
00363ACF  F7 D2                           not edx
00363AD1  85 D2                           test edx, edx
00363AD3  75 14                           jne 0x140363ae9
00363AD5  49 8D 40 04                     lea rax, [r8 + 4]
00363AD9  49 3B C2                        cmp rax, r10
00363ADC  0F 87 E4 02 00 00               ja 0x140363dc6
00363AE2  8B 10                           mov edx, dword ptr [rax]
00363AE4  4C 8B C0                        mov r8, rax
00363AE7  EB E8                           jmp 0x140363ad1
00363AE9  8B C2                           mov eax, edx
00363AEB  48 0F BC C0                     bsf rax, rax
00363AEF  4D 2B C3                        sub r8, r11
00363AF2  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00363AF6  4D 8B E8                        mov r13, r8
00363AF9  49 C1 FD 02                     sar r13, 2
00363AFD  41 C1 E5 05                     shl r13d, 5
00363B01  44 03 E8                        add r13d, eax
00363B04  44 3B EF                        cmp r13d, edi
00363B07  44 0F 47 EF                     cmova r13d, edi
00363B0B  45 2B EF                        sub r13d, r15d
00363B0E  4C 89 6C 24 48                  mov qword ptr [rsp + 0x48], r13
00363B13  4C 8B 5C 24 78                  mov r11, qword ptr [rsp + 0x78]
00363B18  45 85 C9                        test r9d, r9d
00363B1B  0F 85 32 01 00 00               jne 0x140363c53
00363B21  41 8B C7                        mov eax, r15d
00363B24  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00363B28  45 8B C5                        mov r8d, r13d
00363B2B  41 8B D7                        mov edx, r15d
00363B2E  49 8D 3C C3                     lea rdi, [r11 + rax*8]
00363B32  E8 D9 DA 07 00                  call 0x1403e1610
00363B37  45 85 ED                        test r13d, r13d
00363B3A  0F 84 E5 00 00 00               je 0x140363c25
00363B40  4C 8B 7D 88                     mov r15, qword ptr [rbp - 0x78]
00363B44  4C 8B E3                        mov r12, rbx
00363B47  48 8B 5C 24 70                  mov rbx, qword ptr [rsp + 0x70]
00363B4C  41 81 E4 00 04 00 00            and r12d, 0x400
00363B53  48 8B 07                        mov rax, qword ptr [rdi]
00363B56  4C 8B 5C 24 50                  mov r11, qword ptr [rsp + 0x50]
00363B5B  4D 85 DB                        test r11, r11
00363B5E  74 20                           je 0x140363b80
00363B60  49 8B 03                        mov rax, qword ptr [r11]
00363B63  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00363B68  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
00363B6D  48 FF C8                        dec rax
00363B70  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00363B75  48 F7 D8                        neg rax
00363B78  48 1B C0                        sbb rax, rax
00363B7B  48 21 44 24 58                  and qword ptr [rsp + 0x58], rax
00363B80  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
00363B8A  48 8B C0                        mov rax, rax
00363B8D  4D 8B F3                        mov r14, r11
00363B90  4C 2B F0                        sub r14, rax
00363B93  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
00363B9D  49 C1 FE 04                     sar r14, 4
00363BA1  4C 0F AF F0                     imul r14, rax
00363BA5  4C 89 36                        mov qword ptr [rsi], r14
00363BA8  48 83 C6 08                     add rsi, 8
00363BAC  48 8B 07                        mov rax, qword ptr [rdi]
00363BAF  4D 85 E4                        test r12, r12
00363BB2  0F 84 43 01 00 00               je 0x140363cfb
00363BB8  49 89 43 10                     mov qword ptr [r11 + 0x10], rax
00363BBC  4D 85 FF                        test r15, r15
00363BBF  74 08                           je 0x140363bc9
00363BC1  49 8B CF                        mov rcx, r15
00363BC4  E8 D7 FB FF FF                  call 0x1403637a0
00363BC9  8B 45 80                        mov eax, dword ptr [rbp - 0x80]
00363BCC  45 33 C9                        xor r9d, r9d
00363BCF  48 3B 7D 98                     cmp rdi, qword ptr [rbp - 0x68]
00363BD3  4C 8B C7                        mov r8, rdi
00363BD6  48 8B D3                        mov rdx, rbx
00363BD9  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00363BDD  41 0F 94 C1                     sete r9b
00363BE1  49 8B CB                        mov rcx, r11
00363BE4  E8 EF 01 00 00                  call 0x140363dd8
00363BE9  4D 85 E4                        test r12, r12
00363BEC  74 11                           je 0x140363bff
00363BEE  8B 95 90 00 00 00               mov edx, dword ptr [rbp + 0x90]
00363BF4  49 8B CE                        mov rcx, r14
00363BF7  E8 74 03 00 00                  call 0x140363f70
00363BFC  48 89 07                        mov qword ptr [rdi], rax
00363BFF  48 83 C7 08                     add rdi, 8
00363C03  49 83 ED 01                     sub r13, 1
00363C07  0F 85 46 FF FF FF               jne 0x140363b53
00363C0D  48 8B 5D A0                     mov rbx, qword ptr [rbp - 0x60]
00363C11  4C 8B 7C 24 68                  mov r15, qword ptr [rsp + 0x68]
00363C16  4C 8B 74 24 60                  mov r14, qword ptr [rsp + 0x60]
00363C1B  4C 8B 6C 24 48                  mov r13, qword ptr [rsp + 0x48]
00363C20  4C 8B 64 24 70                  mov r12, qword ptr [rsp + 0x70]
00363C25  4D 85 F6                        test r14, r14
00363C28  75 12                           jne 0x140363c3c
00363C2A  44 8B 7D 84                     mov r15d, dword ptr [rbp - 0x7c]
00363C2E  E9 B0 FD FF FF                  jmp 0x1403639e3
00363C33  48 8B 75 88                     mov rsi, qword ptr [rbp - 0x78]
00363C37  E9 72 FD FF FF                  jmp 0x1403639ae
00363C3C  8B 7D C0                        mov edi, dword ptr [rbp - 0x40]
00363C3F  47 8D 0C 2F                     lea r9d, [r15 + r13]
00363C43  4C 8B 5C 24 78                  mov r11, qword ptr [rsp + 0x78]
00363C48  44 3B CF                        cmp r9d, edi
00363C4B  0F 85 E7 FD FF FF               jne 0x140363a38
00363C51  EB D7                           jmp 0x140363c2a
00363C53  45 8B C7                        mov r8d, r15d
00363C56  33 D2                           xor edx, edx
00363C58  45 2B C1                        sub r8d, r9d
00363C5B  74 73                           je 0x140363cd0
00363C5D  41 83 F8 02                     cmp r8d, 2
00363C61  72 53                           jb 0x140363cb6
00363C63  4C 8B 15 CE 37 AD 00            mov r10, qword ptr [rip + 0xad37ce]
00363C6A  48 8D 0D C7 37 AD 00            lea rcx, [rip + 0xad37c7]
00363C71  41 8D 40 FF                     lea eax, [r8 - 1]
00363C75  48 8D 04 C6                     lea rax, [rsi + rax*8]
00363C79  48 3B F1                        cmp rsi, rcx
00363C7C  77 05                           ja 0x140363c83
00363C7E  48 3B C1                        cmp rax, rcx
00363C81  73 33                           jae 0x140363cb6
00363C83  41 8B C8                        mov ecx, r8d
00363C86  83 E1 FE                        and ecx, 0xfffffffe
00363C89  83 C2 02                        add edx, 2
00363C8C  44 8B CA                        mov r9d, edx
00363C8F  3B D1                           cmp edx, ecx
00363C91  72 F6                           jb 0x140363c89
00363C93  48 8D 14 CD 00 00 00 00         lea rdx, [rcx*8]
00363C9B  48 8B FE                        mov rdi, rsi
00363C9E  48 8B CA                        mov rcx, rdx
00363CA1  49 8B C2                        mov rax, r10
00363CA4  48 C1 E9 03                     shr rcx, 3
00363CA8  F3 48 AB                        rep stosq qword ptr [rdi], rax
00363CAB  48 03 F2                        add rsi, rdx
00363CAE  41 8B D1                        mov edx, r9d
00363CB1  45 3B C8                        cmp r9d, r8d
00363CB4  73 1A                           jae 0x140363cd0
00363CB6  44 2B C2                        sub r8d, edx
00363CB9  41 8B C8                        mov ecx, r8d
00363CBC  48 8B 05 75 37 AD 00            mov rax, qword ptr [rip + 0xad3775]
00363CC3  48 89 06                        mov qword ptr [rsi], rax
00363CC6  48 83 C6 08                     add rsi, 8
00363CCA  48 83 E9 01                     sub rcx, 1
00363CCE  75 EC                           jne 0x140363cbc
00363CD0  41 8B 84 24 C0 00 00 00         mov eax, dword ptr [r12 + 0xc0]
00363CD8  4C 8B 74 24 60                  mov r14, qword ptr [rsp + 0x60]
00363CDD  0F BA E8 12                     bts eax, 0x12
00363CE1  41 89 84 24 C0 00 00 00         mov dword ptr [r12 + 0xc0], eax
00363CE9  E9 33 FE FF FF                  jmp 0x140363b21
00363CEE  44 8B FF                        mov r15d, edi
00363CF1  4C 89 7C 24 68                  mov qword ptr [rsp + 0x68], r15
00363CF6  E9 18 FE FF FF                  jmp 0x140363b13
00363CFB  48 8B 45 90                     mov rax, qword ptr [rbp - 0x70]
00363CFF  48 8B 40 10                     mov rax, qword ptr [rax + 0x10]
00363D03  E9 B0 FE FF FF                  jmp 0x140363bb8
00363D08  45 85 F6                        test r14d, r14d
00363D0B  75 56                           jne 0x140363d63
00363D0D  48 85 F6                        test rsi, rsi
00363D10  0F 85 8B 00 00 00               jne 0x140363da1
00363D16  33 C0                           xor eax, eax
00363D18  E9 E2 FC FF FF                  jmp 0x1403639ff
00363D1D  48 8B 0D 5C 9F AC 00            mov rcx, qword ptr [rip + 0xac9f5c]
00363D24  48 85 C9                        test rcx, rcx
00363D27  74 0E                           je 0x140363d37
00363D29  F6 C3 10                        test bl, 0x10
00363D2C  75 09                           jne 0x140363d37
00363D2E  48 8B C1                        mov rax, rcx
00363D31  48 F7 D0                        not rax
00363D34  48 23 C3                        and rax, rbx
00363D37  48 B9 FF FF FF FF FF 00 00 00   movabs rcx, 0xffffffffff
00363D41  48 C1 E8 0C                     shr rax, 0xc
00363D45  48 23 C1                        and rax, rcx
00363D48  48 8D 0C 40                     lea rcx, [rax + rax*2]
00363D4C  48 C1 E1 04                     shl rcx, 4
00363D50  49 8B C0                        mov rax, r8
00363D53  48 03 C8                        add rcx, rax
00363D56  48 89 4D 90                     mov qword ptr [rbp - 0x70], rcx
00363D5A  48 8B 41 10                     mov rax, qword ptr [rcx + 0x10]
00363D5E  E9 14 FC FF FF                  jmp 0x140363977
00363D63  8B 75 98                        mov esi, dword ptr [rbp - 0x68]
00363D66  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00363D6A  44 8B C7                        mov r8d, edi
00363D6D  C1 EE 03                        shr esi, 3
00363D70  81 E6 FF 01 00 00               and esi, 0x1ff
00363D76  45 2B C6                        sub r8d, r14d
00363D79  8B D6                           mov edx, esi
00363D7B  E8 E4 DD 07 00                  call 0x1403e1b64
00363D80  2B F8                           sub edi, eax
00363D82  44 3B F7                        cmp r14d, edi
00363D85  0F 84 33 FC FF FF               je 0x1403639be
00363D8B  41 2B FE                        sub edi, r14d
00363D8E  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00363D92  44 8B C7                        mov r8d, edi
00363D95  8B D6                           mov edx, esi
00363D97  E8 B8 CC 07 00                  call 0x1403e0a54
00363D9C  E9 1D FC FF FF                  jmp 0x1403639be
00363DA1  49 83 BC 24 80 00 00 00 00      cmp qword ptr [r12 + 0x80], 0
00363DAA  0F 85 66 FF FF FF               jne 0x140363d16
00363DB0  C6 46 01 02                     mov byte ptr [rsi + 1], 2
00363DB4  E9 5D FF FF FF                  jmp 0x140363d16
00363DB9  45 8B F9                        mov r15d, r9d
00363DBC  4C 89 7C 24 68                  mov qword ptr [rsp + 0x68], r15
00363DC1  E9 52 FD FF FF                  jmp 0x140363b18
00363DC6  B8 20 00 00 00                  mov eax, 0x20
00363DCB  E9 1F FD FF FF                  jmp 0x140363aef
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiBuildMdlForMappedFileFault(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, unsigned int a7, __int64 a8, __int64 a9, __int64 a10)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned int v_stack_m94;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned int v_stack_mD4;
    unsigned int v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned int v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (288);
    result = (*(unsigned __int64 *)(v_rip + 11169553)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_mD0 = a8;
    v_stack_m110 = a10;
    result = 0;
    v_stack_mE0 = a2;
    a2 = 0;
    v_stack_mE8 = a1;
    v_stack_m94 = 0;
    result = memset(v_stack_m98, a2, result + 76, a4);
    v_stack_mC0 = *(unsigned __int64 *)(a1 + 232);
    v_stack_m90 = v_stack_m88;
    v_stack_mB8 = *(unsigned __int64 *)(a1 + 168);
    v_stack_m98 = 512;
    result = RtlSetAllBits(v_stack_m98, a2, result + 76, a4);
    v_rdi = 0;
    if (0 > a3) goto loc_003638F6;
loc_003638C2:
    result = *(unsigned __int64 *)(0);
    if ((*(unsigned __int64 *)(0)) == (*(unsigned __int64 *)(a1 + 168))) {
        a2 = 0;
        a2 = (unsigned int)((a2) >> (3));
        a2 = (unsigned int)((a2) & (511));
        a1 = (unsigned int)(a2);
        a2 = (unsigned int)((a2) & (7));
        a1 = (a1) >> (3);
        a1 = (a1) + (v_stack_m90);
        result = (__int8)(*(unsigned __int8 *)(a1));
        *(unsigned __int8 *)(a1) = (unsigned __int8)(result);
        v_rdi = (unsigned int)((v_rdi) + 1);
    }
    a3 = (0) + (8);
    if (a3 <= a3) goto loc_003638C2;
loc_003638F6:
    v_stack_m108 = v_xmm0;
    a2 = (unsigned int)((unsigned int)(v_rdi));
    if (((unsigned int)((unsigned int)(v_rdi))) > a5) { a2 = a5; }
    v_r14 = 0;
    result = 0;
    v_stack_mF8 = 0;
    if (a6 != -1) {
        a1 = a6 + a6 * 2;
        a1 = (a1) << (4);
        result = a3;
        a1 = (a1) + (result);
        result = v_stack_m108;
        v_stack_m108 = a1;
        *(unsigned __int64 *)(a1) = result;
        result = v_stack_m100;
        if (result == 0) { result = a1; }
        v_r14 = (v_r14) + 1;
        v_stack_m100 = result;
        result = v_r14;
        v_stack_mF8 = v_r14;
    }
    if (result == a2) goto loc_00363C33;
    if (result >= a2) goto loc_00363D1D;
loc_00363977:
    v_stack_m120 = v_stack_m110;
    v_stack_m128 = *(unsigned __int64 *)(a1 + 168);
    v_stack_m130 = v_stack_mE8;
    v_stack_m138 = a9;
    result = MiGetHardFaultPages(v_stack_m108, a2, a4, v_stack_mD0);
loc_003639AE:
    v_stack_mD4 = (unsigned int)(v_stack_mF8);
    if (((unsigned int)(v_stack_mF8)) != ((unsigned int)(v_rdi))) goto loc_00363D08;
loc_003639BE:
    result = MiProtectionToCacheAttribute((unsigned int)(a7), a2, a4, v_stack_mD0);
    a4 = 0;
    v_stack_mD8 = (unsigned int)(result);
    if ((unsigned int)((unsigned int)(v_stack_m98)) != 0) goto loc_00363A27;
loc_003639E3:
    v_rsi = (v_stack_mE8 + 320) - (v_stack_mE8);
    v_rsi = (v_rsi) - (320);
    v_rsi = (v_rsi) >> (3);
    v_rsi = (unsigned int)((v_rsi) << (12));
    *(unsigned int *)(v_stack_mE8 + 184) = (unsigned int)(v_rsi);
loc_003639FF:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a4, a4);
    v_rsp = (v_rsp) + (288);
    return result;
loc_00363A27:
    v_r11 = (v_stack_p78) & (0xFFFFFFFFFFFFF000ULL);
    v_stack_p78 = v_r11;
loc_00363A38:
    v_r13 = 0;
    v_stack_p48 = 0;
    if (((unsigned int)((unsigned int)(v_stack_m98))) <= 0) goto loc_00363DB9;
    a1 = ((unsigned int)(v_stack_m98) - 1) >> (5);
    result = (0) >> (5);
    a1 = (unsigned int)((0) & (31));
    result = (unsigned int)((v_r13 + 1) << ((unsigned __int8)(a1)));
    result = (unsigned int)((result) - 1);
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m90 + result * 4))) | ((unsigned int)(result)));
loc_00363A7F:
    a2 = (unsigned int)(~(a2));
    if ((unsigned int)(a2) != 0) goto loc_00363A9B;
    if ((v_stack_m90 + result * 4 + 4) > (v_stack_m90 + a1 * 4)) goto loc_00363CEE;
    a3 = (v_stack_m90 + result * 4) + (4);
    result = (v_stack_m90 + result * 4 + 4) + (4);
    goto loc_00363A7F;
loc_00363A9B:
    v_r15 = (a3) - (v_stack_m90);
    v_r15 = (v_r15) >> (2);
    v_r15 = (unsigned int)((v_r15) << (5));
    v_r15 = (unsigned int)((v_r15) + ((unsigned int)(a1)));
    v_stack_p40 = (unsigned int)(a1);
    v_stack_p68 = v_r15;
    if (((unsigned int)(v_r15)) > ((unsigned int)((unsigned int)(v_stack_m98)))) goto loc_00363CEE;
    result = (unsigned int)((1) << ((unsigned __int8)(a1)));
    result = (unsigned int)((result) - 1);
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(a3))) | ((unsigned int)(result)));
    a2 = (unsigned int)(~(a2));
loc_00363AD1:
    if ((unsigned int)(a2) != 0) goto loc_00363AE9;
    if ((a3 + 4) > (v_stack_m90 + a1 * 4)) goto loc_00363DC6;
    goto loc_00363AD1;
loc_00363AE9:
loc_00363AEF:
    a3 = (a3 + 4) - (v_stack_m90);
    v_stack_p40 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 4)))));
    v_r13 = (a3) >> (2);
    v_r13 = (unsigned int)((v_r13) << (5));
    v_r13 = (unsigned int)((v_r13) + ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 4)))))));
    if (((unsigned int)(v_r13)) > ((unsigned int)((unsigned int)(v_stack_m98)))) { v_r13 = (unsigned int)((unsigned int)(v_stack_m98)); }
    v_r13 = (unsigned int)((v_r13) - ((unsigned int)(v_r15)));
    v_stack_p48 = v_r13;
loc_00363B13:
loc_00363B18:
    if (0 != 0) goto loc_00363C53;
loc_00363B21:
    result = RtlSetBits(v_stack_m98, (unsigned int)((unsigned int)(v_r15)), (unsigned int)((unsigned int)(v_r13)), a4);
    if ((unsigned int)(v_r13) == 0) goto loc_00363C25;
    v_r12 = (unsigned int)((v_stack_p18) & (0x400ULL));
loc_00363B53:
    result = *(unsigned __int64 *)(v_stack_p78 + (unsigned int)((unsigned int)(v_r15)) * 8);
    if (v_stack_p50 != 0) {
        result = *(unsigned __int64 *)(v_stack_p50);
        v_stack_p50 = result;
        result = v_stack_p60;
        result = (result) - 1;
        v_stack_p60 = result;
        result = -(result);
    }
    v_r14 = (v_stack_p50) - (result);
    v_r14 = (v_r14) >> (4);
    v_r14 = (v_r14) * (result);
    *(unsigned __int64 *)(v_rsi) = v_r14;
    v_rsi = (v_rsi) + (8);
    if (v_r12 == 0) goto loc_00363CFB;
loc_00363BB8:
    *(unsigned __int64 *)(v_stack_p50 + 16) = *(unsigned __int64 *)(v_stack_p78 + (unsigned int)((unsigned int)(v_r15)) * 8);
    result = *(unsigned __int64 *)(v_stack_p78 + (unsigned int)((unsigned int)(v_r15)) * 8);
    if (v_stack_mD0 != 0) {
        a1 = v_stack_mD0;
        result = MiAdvanceFaultList(a1, (unsigned int)((unsigned int)(v_r15)), (unsigned int)((unsigned int)(v_r13)), a4);
    }
    a4 = 0;
    v_stack_p20 = (unsigned int)((unsigned int)(v_stack_mD8));
    a4 = ((v_stack_p78 + (unsigned int)((unsigned int)(v_r15)) * 8) == v_stack_mC0) ? 1 : 0;
    result = MiInitializeHardFaultPfn(v_stack_p50, v_stack_p70, v_stack_p78 + (unsigned int)((unsigned int)(v_r15)) * 8, a4);
    if (v_r12 != 0) {
        a2 = a7;
        a1 = v_r14;
        result = MiMakeTransitionPte(a1, a2, v_stack_p78 + (unsigned int)((unsigned int)(v_r15)) * 8, a4);
        *(unsigned __int64 *)(v_stack_p78 + (unsigned int)((unsigned int)(v_r15)) * 8) = result;
    }
    v_rdi = (v_stack_p78 + (unsigned int)((unsigned int)(v_r15)) * 8) + (8);
    v_r13 = (v_r13) - (1);
    if (condition_is_not_equal) goto loc_00363B53;
loc_00363C25:
    if (v_stack_p60 != 0) goto loc_00363C3C;
loc_00363C2A:
    goto loc_003639E3;
loc_00363C33:
    goto loc_003639AE;
loc_00363C3C:
    if (((unsigned int)((unsigned int)(v_stack_mD4) + v_stack_p48 * 1)) != ((unsigned int)((unsigned int)(v_stack_m98)))) goto loc_00363A38;
    goto loc_00363C2A;
loc_00363C53:
    a2 = 0;
    a3 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_mD4)))) - ((unsigned int)((unsigned int)(v_stack_mD4) + v_stack_p48 * 1)));
    if (condition_is_equal) goto loc_00363CD0;
    if (((unsigned int)(a3)) < 2) goto loc_00363CB6;
    if (v_stack_mD0 > (v_rip + 11352007)) goto loc_00363C83;
    if ((v_stack_mD0 + a3 - 1 * 8) >= (v_rip + 11352007)) goto loc_00363CB6;
loc_00363C83:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(a3))) & (0xFFFFFFFEULL));
loc_00363C89:
    a2 = (unsigned int)((a2) + (2));
    if (((unsigned int)(a2)) < ((unsigned int)(a1))) goto loc_00363C89;
    a1 = (a1 * 8) >> (3);
    v_rsi = (v_stack_mD0) + (a1 * 8);
    if (((unsigned int)((unsigned int)((unsigned int)(a2)))) >= ((unsigned int)(a3))) goto loc_00363CD0;
loc_00363CB6:
    a3 = (unsigned int)((a3) - ((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a2)))))));
loc_00363CBC:
    *(unsigned __int64 *)(v_rsi) = *(unsigned __int64 *)(v_rip + 11351925);
    v_rsi = (v_rsi) + (8);
    a1 = ((unsigned int)((unsigned int)(a3))) - (1);
    if (condition_is_not_equal) goto loc_00363CBC;
loc_00363CD0:
    *(unsigned int *)(v_stack_p70 + 192) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p70 + 192)));
    goto loc_00363B21;
loc_00363CEE:
    v_stack_p68 = (unsigned int)((unsigned int)(v_stack_mD0));
    goto loc_00363B13;
loc_00363CFB:
    goto loc_00363BB8;
loc_00363D08:
    if ((unsigned int)(v_stack_p60) != 0) goto loc_00363D63;
    if (v_rsi != 0) goto loc_00363DA1;
loc_00363D16:
    result = 0;
    goto loc_003639FF;
loc_00363D1D:
    if (*(unsigned __int64 *)(v_rip + 11312988) == 0) goto loc_00363D37;
    if ((((unsigned __int8)(v_stack_mB8)) & (16)) == 0) {
        result = *(unsigned __int64 *)(v_rip + 11312988);
        result = ~(result);
        result = (result) & (v_stack_mB8);
    }
    result = (result) >> (12);
    result = (result) & (*(unsigned __int64 *)(v_rip + 11312988));
    a1 = (result + result * 2) << (4);
    a1 = (a1) + (a3);
    v_stack_mC8 = a1;
    goto loc_00363977;
loc_00363D63:
    v_rsi = (unsigned int)(((unsigned int)(v_stack_mC0)) >> (3));
    v_rsi = (unsigned int)((v_rsi) & (511));
    a3 = (unsigned int)(((unsigned int)((unsigned int)(v_stack_mD0))) - ((unsigned int)(v_stack_p60)));
    result = MiReduceMappedFileReadBehind(v_stack_m98, (unsigned int)((unsigned int)(v_rsi)), a3, (unsigned int)((unsigned int)(a2)));
    v_rdi = (unsigned int)((v_stack_mD0) - ((unsigned int)(result)));
    if (((unsigned int)(v_stack_p60)) == ((unsigned int)(v_rdi))) goto loc_003639BE;
    v_rdi = (unsigned int)((v_rdi) - ((unsigned int)(v_stack_p60)));
    result = MiReduceMappedFileReadAhead(v_stack_m98, (unsigned int)((unsigned int)(v_rsi)), (unsigned int)((unsigned int)(v_rdi)), (unsigned int)((unsigned int)(a2)));
    goto loc_003639BE;
loc_00363DA1:
    if ((*(unsigned __int64 *)(v_stack_p70 + 128)) != 0) goto loc_00363D16;
    *(unsigned __int8 *)(v_rsi + 1) = 2;
    goto loc_00363D16;
loc_00363DB9:
    v_stack_p68 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(a2))));
    goto loc_00363B18;
loc_00363DC6:
    goto loc_00363AEF;
}
```

## 5. (Beta) C Style

```c
int64_t MiBuildMdlForMappedFileFault(void *Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, int64_t Arg6, uint32_t Arg7, int64_t Arg8, void *Arg9, int64_t Arg10)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg9 = (uint8_t *)Arg9;

    int64_t result;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m48;
    uint64_t v_stack_m58;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint32_t v_stack_m94;
    uint64_t v_stack_m98;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint32_t v_stack_mD4;
    uint32_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p18;
    uint32_t v_stack_p20;
    uint32_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (288);
    result = (*(uint64_t *)(v_rip + 0xAA6F11)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_mD0 = Arg8;
    v_stack_m110 = Arg10;
    result = 0;
    v_stack_mE0 = Arg2;
    Arg2 = 0;
    v_stack_mE8 = Arg1;
    v_stack_m94 = 0;
    result = memset(v_stack_m98, Arg2, result + 76, Arg4);
    v_stack_mC0 = *(uint64_t *)(arg1 + 0xE8);
    v_stack_m90 = v_stack_m88;
    v_stack_mB8 = *(uint64_t *)(arg1 + 0xA8);
    v_stack_m98 = 512;
    result = RtlSetAllBits(v_stack_m98, Arg2, result + 76, Arg4);
    local_rdi = 0;
    if (0 > Arg3) goto loc_003638F6;
loc_003638C2:
    result = *(uint64_t *)(0);
    if ((*(uint64_t *)(0)) == (*(uint64_t *)(arg1 + 0xA8))) {
        Arg2 = 0;
        Arg2 = (uint32_t)((Arg2) >> (3));
        Arg2 = (uint32_t)((Arg2) & (511));
        Arg1 = (uint32_t)(Arg2);
        Arg2 = (uint32_t)((Arg2) & (7));
        Arg1 = (Arg1) >> (3);
        Arg1 = (Arg1) + (v_stack_m90);
        result = (int8_t)(*(uint8_t *)(arg1));
        *(uint8_t *)(arg1) = (uint8_t)(result);
        local_rdi = (uint32_t)((local_rdi) + 1);
    }
    Arg3 = (0) + (8);
    if (Arg3 <= Arg3) goto loc_003638C2;
loc_003638F6:
    v_stack_m108 = v_xmm0;
    Arg2 = (uint32_t)((uint32_t)(local_rdi));
    if (((uint32_t)((uint32_t)(local_rdi))) > Arg5) { Arg2 = Arg5; }
    local_r14 = 0;
    result = 0;
    v_stack_mF8 = 0;
    if (Arg6 != -1) {
        Arg1 = Arg6 + Arg6 * 2;
        Arg1 = (Arg1) << (4);
        result = Arg3;
        Arg1 = (Arg1) + (result);
        result = v_stack_m108;
        v_stack_m108 = Arg1;
        *(uint64_t *)(arg1) = result;
        result = v_stack_m100;
        if (result == 0) { result = Arg1; }
        local_r14 = (local_r14) + 1;
        v_stack_m100 = result;
        result = local_r14;
        v_stack_mF8 = local_r14;
    }
    if (result == Arg2) goto loc_00363C33;
    if (result >= Arg2) goto loc_00363D1D;
loc_00363977:
    v_stack_m120 = v_stack_m110;
    v_stack_m128 = *(uint64_t *)(arg1 + 0xA8);
    v_stack_m130 = v_stack_mE8;
    v_stack_m138 = Arg9;
    result = MiGetHardFaultPages(v_stack_m108, Arg2, Arg4, v_stack_mD0);
loc_003639AE:
    v_stack_mD4 = (uint32_t)(v_stack_mF8);
    if (((uint32_t)(v_stack_mF8)) != ((uint32_t)(local_rdi))) goto loc_00363D08;
loc_003639BE:
    result = MiProtectionToCacheAttribute((uint32_t)(Arg7), Arg2, Arg4, v_stack_mD0);
    Arg4 = 0;
    v_stack_mD8 = (uint32_t)(result);
    if ((uint32_t)((uint32_t)(v_stack_m98)) != 0) goto loc_00363A27;
loc_003639E3:
    local_rsi = (v_stack_mE8 + 320) - (v_stack_mE8);
    local_rsi = (local_rsi) - (320);
    local_rsi = (local_rsi) >> (3);
    local_rsi = (uint32_t)((local_rsi) << (12));
    *(uint32_t *)(v_stack_mE8 + 0xB8) = (uint32_t)(local_rsi);
loc_003639FF:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg4, Arg4);
    local_rsp = (local_rsp) + (288);
    return result;
loc_00363A27:
    local_r11 = (v_stack_p78) & (0xFFFFFFFFFFFFF000ULL);
    v_stack_p78 = local_r11;
loc_00363A38:
    local_r13 = 0;
    v_stack_p48 = 0;
    if (((uint32_t)((uint32_t)(v_stack_m98))) <= 0) goto loc_00363DB9;
    Arg1 = ((uint32_t)(v_stack_m98) - 1) >> (5);
    result = (0) >> (5);
    Arg1 = (uint32_t)((0) & (31));
    result = (uint32_t)((local_r13 + 1) << ((uint8_t)(Arg1)));
    result = (uint32_t)((result) - 1);
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m90 + result * 4))) | ((uint32_t)(result)));
loc_00363A7F:
    Arg2 = (uint32_t)(~(Arg2));
    if ((uint32_t)(Arg2) != 0) goto loc_00363A9B;
    if ((v_stack_m90 + result * 4 + 4) > (v_stack_m90 + Arg1 * 4)) goto loc_00363CEE;
    Arg3 = (v_stack_m90 + result * 4) + (4);
    result = (v_stack_m90 + result * 4 + 4) + (4);
    goto loc_00363A7F;
loc_00363A9B:
    local_r15 = (Arg3) - (v_stack_m90);
    local_r15 = (local_r15) >> (2);
    local_r15 = (uint32_t)((local_r15) << (5));
    local_r15 = (uint32_t)((local_r15) + ((uint32_t)(Arg1)));
    v_stack_p40 = (uint32_t)(Arg1);
    v_stack_p68 = local_r15;
    if (((uint32_t)(local_r15)) > ((uint32_t)((uint32_t)(v_stack_m98)))) goto loc_00363CEE;
    result = (uint32_t)((1) << ((uint8_t)(Arg1)));
    result = (uint32_t)((result) - 1);
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg3))) | ((uint32_t)(result)));
    Arg2 = (uint32_t)(~(Arg2));
loc_00363AD1:
    if ((uint32_t)(Arg2) != 0) goto loc_00363AE9;
    if ((Arg3 + 4) > (v_stack_m90 + Arg1 * 4)) goto loc_00363DC6;
    goto loc_00363AD1;
loc_00363AE9:
loc_00363AEF:
    Arg3 = (Arg3 + 4) - (v_stack_m90);
    v_stack_p40 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg3 + 0x4)))));
    local_r13 = (Arg3) >> (2);
    local_r13 = (uint32_t)((local_r13) << (5));
    local_r13 = (uint32_t)((local_r13) + ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg3 + 0x4)))))));
    if (((uint32_t)(local_r13)) > ((uint32_t)((uint32_t)(v_stack_m98)))) { local_r13 = (uint32_t)((uint32_t)(v_stack_m98)); }
    local_r13 = (uint32_t)((local_r13) - ((uint32_t)(local_r15)));
    v_stack_p48 = local_r13;
loc_00363B13:
loc_00363B18:
    if (0 != 0) goto loc_00363C53;
loc_00363B21:
    result = RtlSetBits(v_stack_m98, (uint32_t)((uint32_t)(local_r15)), (uint32_t)((uint32_t)(local_r13)), Arg4);
    if ((uint32_t)(local_r13) == 0) goto loc_00363C25;
    local_r12 = (uint32_t)((v_stack_p18) & (0x400ULL));
loc_00363B53:
    result = *(uint64_t *)(v_stack_p78 + (uint32_t)((uint32_t)(local_r15)) * 8);
    if (v_stack_p50 != 0) {
        result = *(uint64_t *)(v_stack_p50);
        v_stack_p50 = result;
        result = v_stack_p60;
        result = (result) - 1;
        v_stack_p60 = result;
        result = -(result);
    }
    local_r14 = (v_stack_p50) - (result);
    local_r14 = (local_r14) >> (4);
    local_r14 = (local_r14) * (result);
    *(uint64_t *)(local_rsi) = local_r14;
    local_rsi = (local_rsi) + (8);
    if (local_r12 == 0) goto loc_00363CFB;
loc_00363BB8:
    *(uint64_t *)(v_stack_p50 + 0x10) = *(uint64_t *)(v_stack_p78 + (uint32_t)((uint32_t)(local_r15)) * 8);
    result = *(uint64_t *)(v_stack_p78 + (uint32_t)((uint32_t)(local_r15)) * 8);
    if (v_stack_mD0 != 0) {
        Arg1 = v_stack_mD0;
        result = MiAdvanceFaultList(Arg1, (uint32_t)((uint32_t)(local_r15)), (uint32_t)((uint32_t)(local_r13)), Arg4);
    }
    Arg4 = 0;
    v_stack_p20 = (uint32_t)((uint32_t)(v_stack_mD8));
    Arg4 = ((v_stack_p78 + (uint32_t)((uint32_t)(local_r15)) * 8) == v_stack_mC0) ? 1 : 0;
    result = MiInitializeHardFaultPfn(v_stack_p50, v_stack_p70, v_stack_p78 + (uint32_t)((uint32_t)(local_r15)) * 8, Arg4);
    if (local_r12 != 0) {
        Arg2 = Arg7;
        Arg1 = local_r14;
        result = MiMakeTransitionPte(Arg1, Arg2, v_stack_p78 + (uint32_t)((uint32_t)(local_r15)) * 8, Arg4);
        *(uint64_t *)(v_stack_p78 + (uint32_t)((uint32_t)(local_r15)) * 8) = result;
    }
    local_rdi = (v_stack_p78 + (uint32_t)((uint32_t)(local_r15)) * 8) + (8);
    local_r13 = (local_r13) - (1);
    if (condition_is_not_equal) goto loc_00363B53;
loc_00363C25:
    if (v_stack_p60 != 0) goto loc_00363C3C;
loc_00363C2A:
    goto loc_003639E3;
loc_00363C33:
    goto loc_003639AE;
loc_00363C3C:
    if (((uint32_t)((uint32_t)(v_stack_mD4) + v_stack_p48 * 1)) != ((uint32_t)((uint32_t)(v_stack_m98)))) goto loc_00363A38;
    goto loc_00363C2A;
loc_00363C53:
    Arg2 = 0;
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_mD4)))) - ((uint32_t)((uint32_t)(v_stack_mD4) + v_stack_p48 * 1)));
    if (condition_is_equal) goto loc_00363CD0;
    if (((uint32_t)(Arg3)) < 2) goto loc_00363CB6;
    if (v_stack_mD0 > (v_rip + 11352007)) goto loc_00363C83;
    if ((v_stack_mD0 + Arg3 - 1 * 8) >= (v_rip + 11352007)) goto loc_00363CB6;
loc_00363C83:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(Arg3))) & (0xFFFFFFFEULL));
loc_00363C89:
    Arg2 = (uint32_t)((Arg2) + (2));
    if (((uint32_t)(Arg2)) < ((uint32_t)(Arg1))) goto loc_00363C89;
    Arg1 = (Arg1 * 8) >> (3);
    local_rsi = (v_stack_mD0) + (Arg1 * 8);
    if (((uint32_t)((uint32_t)((uint32_t)(Arg2)))) >= ((uint32_t)(Arg3))) goto loc_00363CD0;
loc_00363CB6:
    Arg3 = (uint32_t)((Arg3) - ((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg2)))))));
loc_00363CBC:
    *(uint64_t *)(local_rsi) = *(uint64_t *)(v_rip + 0xAD3775);
    local_rsi = (local_rsi) + (8);
    Arg1 = ((uint32_t)((uint32_t)(Arg3))) - (1);
    if (condition_is_not_equal) goto loc_00363CBC;
loc_00363CD0:
    *(uint32_t *)(v_stack_p70 + 0xC0) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p70 + 0xC0)));
    goto loc_00363B21;
loc_00363CEE:
    v_stack_p68 = (uint32_t)((uint32_t)(v_stack_mD0));
    goto loc_00363B13;
loc_00363CFB:
    goto loc_00363BB8;
loc_00363D08:
    if ((uint32_t)(v_stack_p60) != 0) goto loc_00363D63;
    if (local_rsi != 0) goto loc_00363DA1;
loc_00363D16:
    result = 0;
    goto loc_003639FF;
loc_00363D1D:
    if (*(uint64_t *)(v_rip + 0xAC9F5C) == 0) goto loc_00363D37;
    if ((((uint8_t)(v_stack_mB8)) & (16)) == 0) {
        result = *(uint64_t *)(v_rip + 0xAC9F5C);
        result = ~(result);
        result = (result) & (v_stack_mB8);
    }
    result = (result) >> (12);
    result = (result) & (*(uint64_t *)(v_rip + 0xAC9F5C));
    Arg1 = (result + result * 2) << (4);
    Arg1 = (Arg1) + (Arg3);
    v_stack_mC8 = Arg1;
    goto loc_00363977;
loc_00363D63:
    local_rsi = (uint32_t)(((uint32_t)(v_stack_mC0)) >> (3));
    local_rsi = (uint32_t)((local_rsi) & (511));
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(v_stack_mD0))) - ((uint32_t)(v_stack_p60)));
    result = MiReduceMappedFileReadBehind(v_stack_m98, (uint32_t)((uint32_t)(local_rsi)), Arg3, (uint32_t)((uint32_t)(Arg2)));
    local_rdi = (uint32_t)((v_stack_mD0) - ((uint32_t)(result)));
    if (((uint32_t)(v_stack_p60)) == ((uint32_t)(local_rdi))) goto loc_003639BE;
    local_rdi = (uint32_t)((local_rdi) - ((uint32_t)(v_stack_p60)));
    result = MiReduceMappedFileReadAhead(v_stack_m98, (uint32_t)((uint32_t)(local_rsi)), (uint32_t)((uint32_t)(local_rdi)), (uint32_t)((uint32_t)(Arg2)));
    goto loc_003639BE;
loc_00363DA1:
    if ((*(uint64_t *)(v_stack_p70 + 0x80)) != 0) goto loc_00363D16;
    *(uint8_t *)(local_rsi + 0x1) = 2;
    goto loc_00363D16;
loc_00363DB9:
    v_stack_p68 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg2))));
    goto loc_00363B18;
loc_00363DC6:
    goto loc_00363AEF;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xA8` | `64` | `R` |
| `Arg1` | `+ 0xE8` | `64` | `R` |
| `Arg9` | `+ 0x80` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0036380C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
