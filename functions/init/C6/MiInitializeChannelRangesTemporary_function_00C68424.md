# MiInitializeChannelRangesTemporary

- RVA: `0x00C68424`–`0x00C687DC` (길이 `952` bytes)
- VA: `0x0000000140C68424`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C7178`
- 디코드: `276`개 명령, `952/952` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **8**

### Outgoing calls
- `0x00C684A6` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00C687B8` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [MiInitNucleus](../C5/MiInitNucleus_function_00C5FD38.md) at `0x00C5FEE8`

### Static image references
- `0x00C68443` → RVA `0x00E0A740` (`.data`; read)
- `0x00C6845D` → RVA `0x00FC5208` (`ALMOSTRO`; read)
- `0x00C6846E` → RVA `0x00E37615` (`.data`; read)
- `0x00C6847B` → RVA `0x00FC521C` (`ALMOSTRO`; read)
- `0x00C68488` → RVA `0x00E00638` (`.data`; read)
- `0x00C68525` → RVA `0x00E2DBCB` (`.data`; write)
- `0x00C6853D` → RVA `0x00FC5002` (`ALMOSTRO`; write)
- `0x00C687AA` → RVA `0x00E2DC28` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00C684A6` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`INIT` → `.text`)
  - `0x00C687B8` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`INIT` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C68424  48 8B C4                        mov rax, rsp
00C68427  48 89 58 08                     mov qword ptr [rax + 8], rbx
00C6842B  48 89 70 10                     mov qword ptr [rax + 0x10], rsi
00C6842F  48 89 78 18                     mov qword ptr [rax + 0x18], rdi
00C68433  4C 89 68 20                     mov qword ptr [rax + 0x20], r13
00C68437  55                              push rbp
00C68438  41 56                           push r14
00C6843A  41 57                           push r15
00C6843C  48 8B EC                        mov rbp, rsp
00C6843F  48 83 EC 70                     sub rsp, 0x70
00C68443  48 8B 05 F6 22 1A 00            mov rax, qword ptr [rip + 0x1a22f6]
00C6844A  48 33 C4                        xor rax, rsp
00C6844D  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00C68451  83 65 C8 00                     and dword ptr [rbp - 0x38], 0
00C68455  0F 57 C0                        xorps xmm0, xmm0
00C68458  48 83 65 C0 00                  and qword ptr [rbp - 0x40], 0
00C6845D  83 3D A4 CD 35 00 00            cmp dword ptr [rip + 0x35cda4], 0
00C68464  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
00C68468  0F 84 43 03 00 00               je 0x140c687b1
00C6846E  80 3D A0 F1 1C 00 00            cmp byte ptr [rip + 0x1cf1a0], 0
00C68475  0F 85 36 03 00 00               jne 0x140c687b1
00C6847B  83 3D 9A CD 35 00 00            cmp dword ptr [rip + 0x35cd9a], 0
00C68482  0F 84 29 03 00 00               je 0x140c687b1
00C68488  48 8B 05 A9 81 19 00            mov rax, qword ptr [rip + 0x1981a9]
00C6848F  4C 8D 4D C8                     lea r9, [rbp - 0x38]
00C68493  BA 08 00 00 00                  mov edx, 8
00C68498  C7 45 D0 80 00 00 00            mov dword ptr [rbp - 0x30], 0x80
00C6849F  4C 8D 45 C0                     lea r8, [rbp - 0x40]
00C684A3  8D 4A 17                        lea ecx, [rdx + 0x17]
00C684A6  E8 25 26 A5 FF                  call 0x1406baad0
00C684AB  48 8B 4D C0                     mov rcx, qword ptr [rbp - 0x40]
00C684AF  48 85 C9                        test rcx, rcx
00C684B2  0F 84 F9 02 00 00               je 0x140c687b1
00C684B8  45 33 D2                        xor r10d, r10d
00C684BB  45 32 C0                        xor r8b, r8b
00C684BE  48 83 39 FF                     cmp qword ptr [rcx], -1
00C684C2  45 8D 7A 01                     lea r15d, [r10 + 1]
00C684C6  74 6F                           je 0x140c68537
00C684C8  4C 8D 49 0C                     lea r9, [rcx + 0xc]
00C684CC  41 0F B7 11                     movzx edx, word ptr [r9]
00C684D0  41 0F B6 C0                     movzx eax, r8b
00C684D4  66 3B C2                        cmp ax, dx
00C684D7  77 03                           ja 0x140c684dc
00C684D9  45 8A 01                        mov r8b, byte ptr [r9]
00C684DC  41 80 79 02 00                  cmp byte ptr [r9 + 2], 0
00C684E1  74 05                           je 0x140c684e8
00C684E3  45 8B D7                        mov r10d, r15d
00C684E6  EB 2B                           jmp 0x140c68513
00C684E8  41 0F B7 41 FE                  movzx eax, word ptr [r9 - 2]
00C684ED  83 F8 40                        cmp eax, 0x40
00C684F0  73 21                           jae 0x140c68513
00C684F2  83 FA 02                        cmp edx, 2
00C684F5  73 1C                           jae 0x140c68513
00C684F7  8D 14 42                        lea edx, [rdx + rax*2]
00C684FA  8B CA                           mov ecx, edx
00C684FC  83 E2 07                        and edx, 7
00C684FF  48 C1 E9 03                     shr rcx, 3
00C68503  0F BE 44 0D E0                  movsx eax, byte ptr [rbp + rcx - 0x20]
00C68508  0F AB D0                        bts eax, edx
00C6850B  88 44 0D E0                     mov byte ptr [rbp + rcx - 0x20], al
00C6850F  48 8B 4D C0                     mov rcx, qword ptr [rbp - 0x40]
00C68513  49 8B C1                        mov rax, r9
00C68516  49 83 C1 10                     add r9, 0x10
00C6851A  48 2B C1                        sub rax, rcx
00C6851D  48 83 E8 0C                     sub rax, 0xc
00C68521  48 C1 F8 04                     sar rax, 4
00C68525  88 05 A0 56 1C 00               mov byte ptr [rip + 0x1c56a0], al
00C6852B  49 83 79 F4 FF                  cmp qword ptr [r9 - 0xc], -1
00C68530  75 9A                           jne 0x140c684cc
00C68532  45 85 D2                        test r10d, r10d
00C68535  75 03                           jne 0x140c6853a
00C68537  45 32 C0                        xor r8b, r8b
00C6853A  45 02 C7                        add r8b, r15b
00C6853D  44 88 05 BE CA 35 00            mov byte ptr [rip + 0x35cabe], r8b
00C68544  45 3A C7                        cmp r8b, r15b
00C68547  0F 84 64 02 00 00               je 0x140c687b1
00C6854D  41 83 CD FF                     or r13d, 0xffffffff
00C68551  41 80 F8 02                     cmp r8b, 2
00C68555  0F 86 31 01 00 00               jbe 0x140c6868c
00C6855B  4C 8D 41 0C                     lea r8, [rcx + 0xc]
00C6855F  49 83 78 F4 FF                  cmp qword ptr [r8 - 0xc], -1
00C68564  0F 84 1B 01 00 00               je 0x140c68685
00C6856A  66 41 83 38 02                  cmp word ptr [r8], 2
00C6856F  0F 82 07 01 00 00               jb 0x140c6867c
00C68575  41 0F B7 40 FE                  movzx eax, word ptr [r8 - 2]
00C6857A  83 F8 40                        cmp eax, 0x40
00C6857D  0F 83 F9 00 00 00               jae 0x140c6867c
00C68583  8B 75 D0                        mov esi, dword ptr [rbp - 0x30]
00C68586  48 8D 4D E0                     lea rcx, [rbp - 0x20]
00C6858A  83 E1 04                        and ecx, 4
00C6858D  4C 8D 7D E0                     lea r15, [rbp - 0x20]
00C68591  44 8B D0                        mov r10d, eax
00C68594  8B C1                           mov eax, ecx
00C68596  45 03 D2                        add r10d, r10d
00C68599  48 F7 D8                        neg rax
00C6859C  8D 56 FF                        lea edx, [rsi - 1]
00C6859F  1B DB                           sbb ebx, ebx
00C685A1  83 E3 20                        and ebx, 0x20
00C685A4  44 3B D6                        cmp r10d, esi
00C685A7  45 1B DB                        sbb r11d, r11d
00C685AA  45 23 DA                        and r11d, r10d
00C685AD  48 F7 D9                        neg rcx
00C685B0  48 1B C0                        sbb rax, rax
00C685B3  48 83 E0 FC                     and rax, 0xfffffffffffffffc
00C685B7  4C 03 F8                        add r15, rax
00C685BA  83 65 CC 00                     and dword ptr [rbp - 0x34], 0
00C685BE  8D 3C 13                        lea edi, [rbx + rdx]
00C685C1  8B C7                           mov eax, edi
00C685C3  42 8D 0C 1B                     lea ecx, [rbx + r11]
00C685C7  2B C1                           sub eax, ecx
00C685C9  FF C0                           inc eax
00C685CB  83 F8 01                        cmp eax, 1
00C685CE  73 05                           jae 0x140c685d5
00C685D0  41 8B D5                        mov edx, r13d
00C685D3  EB 60                           jmp 0x140c68635
00C685D5  8B C7                           mov eax, edi
00C685D7  41 B9 01 00 00 00               mov r9d, 1
00C685DD  48 C1 E8 06                     shr rax, 6
00C685E1  4D 8D 34 C7                     lea r14, [r15 + rax*8]
00C685E5  48 8B C1                        mov rax, rcx
00C685E8  48 C1 E8 06                     shr rax, 6
00C685EC  80 E1 3F                        and cl, 0x3f
00C685EF  49 D3 E1                        shl r9, cl
00C685F2  49 FF C9                        dec r9
00C685F5  49 8D 14 C7                     lea rdx, [r15 + rax*8]
00C685F9  48 8B 02                        mov rax, qword ptr [rdx]
00C685FC  48 F7 D0                        not rax
00C685FF  4C 0B C8                        or r9, rax
00C68602  49 83 F9 FF                     cmp r9, -1
00C68606  75 11                           jne 0x140c68619
00C68608  48 83 C2 08                     add rdx, 8
00C6860C  49 3B D6                        cmp rdx, r14
00C6860F  77 BF                           ja 0x140c685d0
00C68611  4C 8B 0A                        mov r9, qword ptr [rdx]
00C68614  49 F7 D1                        not r9
00C68617  EB E9                           jmp 0x140c68602
00C68619  49 2B D7                        sub rdx, r15
00C6861C  49 F7 D1                        not r9
00C6861F  48 C1 FA 03                     sar rdx, 3
00C68623  49 0F BC C1                     bsf rax, r9
00C68627  C1 E2 06                        shl edx, 6
00C6862A  03 D0                           add edx, eax
00C6862C  3B D7                           cmp edx, edi
00C6862E  77 A0                           ja 0x140c685d0
00C68630  41 3B D5                        cmp edx, r13d
00C68633  75 19                           jne 0x140c6864e
00C68635  45 85 DB                        test r11d, r11d
00C68638  74 16                           je 0x140c68650
00C6863A  41 8D 52 01                     lea edx, [r10 + 1]
00C6863E  3B D6                           cmp edx, esi
00C68640  0F 47 D6                        cmova edx, esi
00C68643  41 03 D5                        add edx, r13d
00C68646  45 33 DB                        xor r11d, r11d
00C68649  E9 6C FF FF FF                  jmp 0x140c685ba
00C6864E  2B D3                           sub edx, ebx
00C68650  41 3B D2                        cmp edx, r10d
00C68653  72 18                           jb 0x140c6866d
00C68655  41 8D 42 02                     lea eax, [r10 + 2]
00C68659  3B D0                           cmp edx, eax
00C6865B  73 10                           jae 0x140c6866d
00C6865D  41 BF 01 00 00 00               mov r15d, 1
00C68663  66 41 23 D7                     and dx, r15w
00C68667  66 41 89 10                     mov word ptr [r8], dx
00C6866B  EB 0F                           jmp 0x140c6867c
00C6866D  41 BF 01 00 00 00               mov r15d, 1
00C68673  41 C6 40 02 00                  mov byte ptr [r8 + 2], 0
00C68678  66 45 89 38                     mov word ptr [r8], r15w
00C6867C  49 83 C0 10                     add r8, 0x10
00C68680  E9 DA FE FF FF                  jmp 0x140c6855f
00C68685  C6 05 76 C9 35 00 02            mov byte ptr [rip + 0x35c976], 2
00C6868C  48 8D 4D E0                     lea rcx, [rbp - 0x20]
00C68690  45 33 D2                        xor r10d, r10d
00C68693  83 E1 04                        and ecx, 4
00C68696  48 8D 75 E0                     lea rsi, [rbp - 0x20]
00C6869A  8B C1                           mov eax, ecx
00C6869C  48 F7 D8                        neg rax
00C6869F  1B DB                           sbb ebx, ebx
00C686A1  83 E3 20                        and ebx, 0x20
00C686A4  48 F7 D9                        neg rcx
00C686A7  48 1B C0                        sbb rax, rax
00C686AA  83 E0 04                        and eax, 4
00C686AD  48 2B F0                        sub rsi, rax
00C686B0  44 8B 5D D0                     mov r11d, dword ptr [rbp - 0x30]
00C686B4  45 3B D3                        cmp r10d, r11d
00C686B7  45 1B C9                        sbb r9d, r9d
00C686BA  45 23 CA                        and r9d, r10d
00C686BD  41 8D 43 FF                     lea eax, [r11 - 1]
00C686C1  83 65 CC 00                     and dword ptr [rbp - 0x34], 0
00C686C5  8D 3C 03                        lea edi, [rbx + rax]
00C686C8  8B C7                           mov eax, edi
00C686CA  42 8D 0C 0B                     lea ecx, [rbx + r9]
00C686CE  2B C1                           sub eax, ecx
00C686D0  41 03 C7                        add eax, r15d
00C686D3  41 3B C7                        cmp eax, r15d
00C686D6  73 05                           jae 0x140c686dd
00C686D8  41 8B D5                        mov edx, r13d
00C686DB  EB 5D                           jmp 0x140c6873a
00C686DD  8B C7                           mov eax, edi
00C686DF  4D 8B C7                        mov r8, r15
00C686E2  48 C1 E8 06                     shr rax, 6
00C686E6  4C 8D 34 C6                     lea r14, [rsi + rax*8]
00C686EA  48 8B C1                        mov rax, rcx
00C686ED  48 C1 E8 06                     shr rax, 6
00C686F1  80 E1 3F                        and cl, 0x3f
00C686F4  49 D3 E0                        shl r8, cl
00C686F7  4D 2B C7                        sub r8, r15
00C686FA  48 8D 14 C6                     lea rdx, [rsi + rax*8]
00C686FE  48 8B 02                        mov rax, qword ptr [rdx]
00C68701  48 F7 D0                        not rax
00C68704  4C 0B C0                        or r8, rax
00C68707  49 83 F8 FF                     cmp r8, -1
00C6870B  75 11                           jne 0x140c6871e
00C6870D  48 83 C2 08                     add rdx, 8
00C68711  49 3B D6                        cmp rdx, r14
00C68714  77 C2                           ja 0x140c686d8
00C68716  4C 8B 02                        mov r8, qword ptr [rdx]
00C68719  49 F7 D0                        not r8
00C6871C  EB E9                           jmp 0x140c68707
00C6871E  48 2B D6                        sub rdx, rsi
00C68721  49 F7 D0                        not r8
00C68724  48 C1 FA 03                     sar rdx, 3
00C68728  49 0F BC C0                     bsf rax, r8
00C6872C  C1 E2 06                        shl edx, 6
00C6872F  03 D0                           add edx, eax
00C68731  3B D7                           cmp edx, edi
00C68733  77 A3                           ja 0x140c686d8
00C68735  41 3B D5                        cmp edx, r13d
00C68738  75 1B                           jne 0x140c68755
00C6873A  45 85 C9                        test r9d, r9d
00C6873D  74 18                           je 0x140c68757
00C6873F  41 8D 42 01                     lea eax, [r10 + 1]
00C68743  41 3B C3                        cmp eax, r11d
00C68746  41 0F 47 C3                     cmova eax, r11d
00C6874A  41 03 C5                        add eax, r13d
00C6874D  45 33 C9                        xor r9d, r9d
00C68750  E9 6C FF FF FF                  jmp 0x140c686c1
00C68755  2B D3                           sub edx, ebx
00C68757  41 3B D5                        cmp edx, r13d
00C6875A  74 4A                           je 0x140c687a6
00C6875C  41 3B D2                        cmp edx, r10d
00C6875F  72 45                           jb 0x140c687a6
00C68761  4C 8B 45 C0                     mov r8, qword ptr [rbp - 0x40]
00C68765  44 8D 52 01                     lea r10d, [rdx + 1]
00C68769  8B C2                           mov eax, edx
00C6876B  D1 E8                           shr eax, 1
00C6876D  49 83 38 FF                     cmp qword ptr [r8], -1
00C68771  0F 84 39 FF FF FF               je 0x140c686b0
00C68777  49 83 C0 0C                     add r8, 0xc
00C6877B  41 0F B7 48 FE                  movzx ecx, word ptr [r8 - 2]
00C68780  3B C8                           cmp ecx, eax
00C68782  75 12                           jne 0x140c68796
00C68784  0F B7 CA                        movzx ecx, dx
00C68787  66 41 23 CF                     and cx, r15w
00C6878B  66 41 39 08                     cmp word ptr [r8], cx
00C6878F  75 05                           jne 0x140c68796
00C68791  41 C6 40 02 00                  mov byte ptr [r8 + 2], 0
00C68796  49 83 C0 10                     add r8, 0x10
00C6879A  49 83 78 F4 FF                  cmp qword ptr [r8 - 0xc], -1
00C6879F  75 DA                           jne 0x140c6877b
00C687A1  E9 0A FF FF FF                  jmp 0x140c686b0
00C687A6  48 8B 45 C0                     mov rax, qword ptr [rbp - 0x40]
00C687AA  48 89 05 77 54 1C 00            mov qword ptr [rip + 0x1c5477], rax
00C687B1  48 8B 4D F0                     mov rcx, qword ptr [rbp - 0x10]
00C687B5  48 33 CC                        xor rcx, rsp
00C687B8  E8 83 3E A4 FF                  call 0x1406ac640
00C687BD  4C 8D 5C 24 70                  lea r11, [rsp + 0x70]
00C687C2  49 8B 5B 20                     mov rbx, qword ptr [r11 + 0x20]
00C687C6  49 8B 73 28                     mov rsi, qword ptr [r11 + 0x28]
00C687CA  49 8B 7B 30                     mov rdi, qword ptr [r11 + 0x30]
00C687CE  4D 8B 6B 38                     mov r13, qword ptr [r11 + 0x38]
00C687D2  49 8B E3                        mov rsp, r11
00C687D5  41 5F                           pop r15
00C687D7  41 5E                           pop r14
00C687D9  5D                              pop rbp
00C687DA  C3                              ret
00C687DB  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiInitializeChannelRangesTemporary(void)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned int v_stack_m48;
    unsigned int v_stack_m4C;
    unsigned int v_stack_m50;
    unsigned __int64 v_stack_m58;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 24) = v_rdi;
    *(unsigned __int64 *)(v_rsp + 32) = v_r13;
    v_rsp = (v_rsp) - (112);
    result = (*(unsigned __int64 *)(v_rip + 1712886)) ^ (v_rsp);
    v_stack_m28 = result;
    v_stack_m38 = v_xmm0;
    if ((*(unsigned int *)(v_rip + 3526052)) == 0) goto loc_00C687B1;
    if ((*(unsigned __int8 *)(v_rip + 1896864)) != 0) goto loc_00C687B1;
    if ((*(unsigned int *)(v_rip + 3526042)) == 0) goto loc_00C687B1;
    v_stack_m48 = 128;
    result = guard_dispatch_icall(8 + 23, 8, v_stack_m58, v_stack_m50);
    if (v_stack_m58 == 0) goto loc_00C687B1;
    v_r10 = 0;
    a3 = 0;
    if ((*(unsigned __int64 *)(v_stack_m58)) == -1) goto loc_00C68537;
loc_00C684CC:
    if (0 <= ((unsigned __int16)(*(unsigned __int16 *)(v_stack_m58 + 12)))) {
        a3 = *(unsigned __int8 *)(v_stack_m58 + 12);
    }
    if ((*(unsigned __int8 *)(v_stack_m58 + 12 + 2)) == 0) goto loc_00C684E8;
    goto loc_00C68513;
loc_00C684E8:
    if (((unsigned int)(*(unsigned __int16 *)(v_stack_m58 + 12 - 2))) >= 64) goto loc_00C68513;
    result = *(unsigned __int16 *)(v_stack_m58 + 12 - 2);
    if (((unsigned int)(*(unsigned __int16 *)(v_stack_m58 + 12))) < 2) {
        a2 = *(unsigned __int16 *)(v_stack_m58 + 12) + *(unsigned __int16 *)(v_stack_m58 + 12 - 2) * 2;
        a1 = (unsigned int)(a2);
        a2 = (unsigned int)((a2) & (7));
        a1 = (a1) >> (3);
        result = (__int8)(*(unsigned __int8 *)(v_rsp + a1 * 1 - 32));
        *(unsigned __int8 *)(v_rsp + a1 * 1 - 32) = (unsigned __int8)(result);
        a1 = v_stack_m58;
    }
    a4 = (v_stack_m58 + 12) + (16);
    result = (v_stack_m58 + 12) - (a1);
    result = (result) - (12);
    result = (result) >> (4);
    *(unsigned __int8 *)(v_rip + 1857184) = (unsigned __int8)(result);
    if ((*(unsigned __int64 *)(a4 - 12)) != -1) goto loc_00C684CC;
    if ((unsigned int)((unsigned int)((unsigned int)(v_r10 + 1))) == 0) {
        a3 = 0;
    }
    a3 = (unsigned __int8)((a3) + ((unsigned __int8)(v_r10 + 1)));
    *(unsigned __int8 *)(v_rip + 3525310) = (unsigned __int8)(a3);
    if (((unsigned __int8)(a3)) == ((unsigned __int8)(v_r10 + 1))) goto loc_00C687B1;
    v_r13 = (unsigned int)((v_r13) | (0xFFFFFFFFULL));
    if (((unsigned __int8)(a3)) <= 2) goto loc_00C6868C;
loc_00C6855F:
    if ((*(unsigned __int64 *)(a1 + 12 - 12)) == -1) goto loc_00C68685;
    if ((*(unsigned __int16 *)(a1 + 12)) < 2) goto loc_00C6867C;
    if (((unsigned int)(*(unsigned __int16 *)(a1 + 12 - 2))) >= 64) goto loc_00C6867C;
    a1 = (unsigned int)((v_stack_m38) & (4));
    v_r10 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(a1 + 12 - 2)))) + ((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int16 *)(a1 + 12 - 2))))));
    result = -((unsigned int)((unsigned int)(a1)));
    v_rbx = (unsigned int)((v_rbx) & (32));
    v_r11 = (unsigned int)((v_r11) & ((unsigned int)(v_r10)));
    a1 = -(a1);
    result = (result) & (-4);
    v_r15 = (v_stack_m38) + (result);
loc_00C685BA:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rbx + (unsigned int)(v_stack_m48) - 1 * 1))) - ((unsigned int)(v_rbx + v_r11 * 1)));
    result = (unsigned int)((result) + 1);
    if (((unsigned int)(result)) >= 1) goto loc_00C685D5;
loc_00C685D0:
    goto loc_00C68635;
loc_00C685D5:
    result = ((unsigned int)((unsigned int)(v_rbx + (unsigned int)(v_stack_m48) - 1 * 1))) >> (6);
    result = (v_rbx + v_r11 * 1) >> (6);
    a1 = (unsigned __int8)((v_rbx + v_r11 * 1) & (63));
    a4 = (1) << ((unsigned __int8)(a1));
    a4 = (a4) - 1;
    result = ~(*(unsigned __int64 *)(v_r15 + result * 8));
    a4 = (a4) | (result);
loc_00C68602:
    if (a4 != -1) goto loc_00C68619;
    a2 = (v_r15 + result * 8) + (8);
    if (a2 > (v_r15 + result * 8)) goto loc_00C685D0;
    a4 = ~(*(unsigned __int64 *)(a2));
    goto loc_00C68602;
loc_00C68619:
    a2 = (a2) - (v_r15);
    a4 = ~(a4);
    a2 = (a2) >> (3);
    a2 = (unsigned int)((a2) << (6));
    a2 = (unsigned int)((a2) + ((unsigned int)(result)));
    if (((unsigned int)(a2)) > ((unsigned int)(v_rbx + (unsigned int)(v_stack_m48) - 1 * 1))) goto loc_00C685D0;
    if (((unsigned int)(a2)) != ((unsigned int)(v_r13))) goto loc_00C6864E;
loc_00C68635:
    if ((unsigned int)(v_r11) == 0) goto loc_00C68650;
    a2 = v_r10 + 1;
    if (((unsigned int)(v_r10 + 1)) > ((unsigned int)((unsigned int)(v_stack_m48)))) { a2 = (unsigned int)((unsigned int)(v_stack_m48)); }
    a2 = (unsigned int)((a2) + ((unsigned int)(v_r13)));
    v_r11 = 0;
    goto loc_00C685BA;
loc_00C6864E:
    a2 = (unsigned int)((a2) - ((unsigned int)(v_rbx)));
loc_00C68650:
    if (((unsigned int)(a2)) < ((unsigned int)(v_r10))) goto loc_00C6866D;
    if (((unsigned int)(a2)) >= ((unsigned int)(v_r10 + 2))) goto loc_00C6866D;
    a2 = (unsigned __int16)((a2) & (1));
    *(unsigned __int16 *)(a1 + 12) = (unsigned __int16)(a2);
    goto loc_00C6867C;
loc_00C6866D:
    *(unsigned __int8 *)(a1 + 12 + 2) = 0;
    *(unsigned __int16 *)(a1 + 12) = 1;
loc_00C6867C:
    a3 = (a1 + 12) + (16);
    goto loc_00C6855F;
loc_00C68685:
    *(unsigned __int8 *)(v_rip + 3524982) = 2;
loc_00C6868C:
    v_r10 = 0;
    a1 = (unsigned int)((v_stack_m38) & (4));
    result = -((unsigned int)((unsigned int)(a1)));
    v_rbx = (unsigned int)((v_rbx) & (32));
    a1 = -(a1);
    result = (unsigned int)((result) & (4));
    v_rsi = (v_stack_m38) - (result);
loc_00C686B0:
    a4 = (unsigned int)((a4) & (0));
loc_00C686C1:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rbx + (unsigned int)(v_stack_m48) - 1 * 1))) - ((unsigned int)(v_rbx + a4 * 1)));
    result = (unsigned int)((result) + (1));
    if (((unsigned int)(result)) >= 1) goto loc_00C686DD;
loc_00C686D8:
    goto loc_00C6873A;
loc_00C686DD:
    result = ((unsigned int)((unsigned int)(v_rbx + (unsigned int)(v_stack_m48) - 1 * 1))) >> (6);
    result = (v_rbx + a4 * 1) >> (6);
    a1 = (unsigned __int8)((v_rbx + a4 * 1) & (63));
    a3 = (1) << ((unsigned __int8)(a1));
    a3 = (a3) - (1);
    result = ~(*(unsigned __int64 *)(v_rsi + result * 8));
    a3 = (a3) | (result);
loc_00C68707:
    if (a3 != -1) goto loc_00C6871E;
    a2 = (v_rsi + result * 8) + (8);
    if (a2 > (v_rsi + result * 8)) goto loc_00C686D8;
    a3 = ~(*(unsigned __int64 *)(a2));
    goto loc_00C68707;
loc_00C6871E:
    a2 = (a2) - (v_rsi);
    a3 = ~(a3);
    a2 = (a2) >> (3);
    a2 = (unsigned int)((a2) << (6));
    a2 = (unsigned int)((a2) + ((unsigned int)(result)));
    if (((unsigned int)(a2)) > ((unsigned int)(v_rbx + (unsigned int)(v_stack_m48) - 1 * 1))) goto loc_00C686D8;
    if (((unsigned int)(a2)) != ((unsigned int)(v_r13))) goto loc_00C68755;
loc_00C6873A:
    if ((unsigned int)(a4) == 0) goto loc_00C68757;
    result = v_r10 + 1;
    if (((unsigned int)(v_r10 + 1)) > ((unsigned int)((unsigned int)(v_stack_m48)))) { result = (unsigned int)((unsigned int)(v_stack_m48)); }
    result = (unsigned int)((result) + ((unsigned int)(v_r13)));
    a4 = 0;
    goto loc_00C686C1;
loc_00C68755:
    a2 = (unsigned int)((a2) - ((unsigned int)(v_rbx)));
loc_00C68757:
    if (((unsigned int)(a2)) == ((unsigned int)(v_r13))) goto loc_00C687A6;
    if (((unsigned int)(a2)) < 0) goto loc_00C687A6;
    result = (unsigned int)(((unsigned int)((unsigned int)(a2))) >> (1));
    if ((*(unsigned __int64 *)(v_stack_m58)) == -1) goto loc_00C686B0;
    a3 = (v_stack_m58) + (12);
loc_00C6877B:
    if (((unsigned int)(*(unsigned __int16 *)(a3 - 2))) != ((unsigned int)(result))) goto loc_00C68796;
    a1 = (unsigned __int16)(((unsigned __int16)(a2)) & (1));
    if ((*(unsigned __int16 *)(a3)) == ((unsigned __int16)(a1))) {
        *(unsigned __int8 *)(a3 + 2) = 0;
    }
    a3 = (a3) + (16);
    if ((*(unsigned __int64 *)(a3 - 12)) != -1) goto loc_00C6877B;
    goto loc_00C686B0;
loc_00C687A6:
    *(unsigned __int64 *)(v_rip + 1856631) = v_stack_m58;
loc_00C687B1:
    a1 = (v_stack_m28) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
void MiInitializeChannelRangesTemporary(void)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint32_t v_stack_m48;
    uint32_t v_stack_m4C;
    uint32_t v_stack_m50;
    uint64_t v_stack_m58;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    *(uint64_t *)(local_rsp + 0x18) = local_rdi;
    *(uint64_t *)(local_rsp + 0x20) = local_r13;
    local_rsp = (local_rsp) - (112);
    result = (*(uint64_t *)(v_rip + 0x1A22F6)) ^ (local_rsp);
    v_stack_m28 = result;
    v_stack_m38 = v_xmm0;
    if ((*(uint32_t *)(v_rip + 0x35CDA4)) == 0) goto loc_00C687B1;
    if ((*(uint8_t *)(v_rip + 0x1CF1A0)) != 0) goto loc_00C687B1;
    if ((*(uint32_t *)(v_rip + 0x35CD9A)) == 0) goto loc_00C687B1;
    v_stack_m48 = 128;
    result = guard_dispatch_icall(8 + 23, 8, v_stack_m58, v_stack_m50);
    if (v_stack_m58 == 0) goto loc_00C687B1;
    local_r10 = 0;
    a3 = 0;
    if ((*(uint64_t *)(v_stack_m58)) == -1) goto loc_00C68537;
loc_00C684CC:
    if (0 <= ((uint16_t)(*(uint16_t *)(v_stack_m58 + 0xC)))) {
        a3 = *(uint8_t *)(v_stack_m58 + 0xC);
    }
    if ((*(uint8_t *)(v_stack_m58 + 0xC + 0x2)) == 0) goto loc_00C684E8;
    goto loc_00C68513;
loc_00C684E8:
    if (((uint32_t)(*(uint16_t *)(v_stack_m58 + 0xC - 0x2))) >= 64) goto loc_00C68513;
    result = *(uint16_t *)(v_stack_m58 + 0xC - 0x2);
    if (((uint32_t)(*(uint16_t *)(v_stack_m58 + 0xC))) < 2) {
        a2 = *(uint16_t *)(v_stack_m58 + 0xC) + *(uint16_t *)(v_stack_m58 + 0xC - 0x2) * 2;
        a1 = (uint32_t)(a2);
        a2 = (uint32_t)((a2) & (7));
        a1 = (a1) >> (3);
        result = (int8_t)(*(uint8_t *)(local_rsp + a1 * 1 - 0x20));
        *(uint8_t *)(local_rsp + a1 * 1 - 0x20) = (uint8_t)(result);
        a1 = v_stack_m58;
    }
    a4 = (v_stack_m58 + 12) + (16);
    result = (v_stack_m58 + 12) - (a1);
    result = (result) - (12);
    result = (result) >> (4);
    *(uint8_t *)(v_rip + 0x1C56A0) = (uint8_t)(result);
    if ((*(uint64_t *)(a4 - 0xC)) != -1) goto loc_00C684CC;
    if ((uint32_t)((uint32_t)((uint32_t)(local_r10 + 1))) == 0) {
        a3 = 0;
    }
    a3 = (uint8_t)((a3) + ((uint8_t)(local_r10 + 1)));
    *(uint8_t *)(v_rip + 0x35CABE) = (uint8_t)(a3);
    if (((uint8_t)(a3)) == ((uint8_t)(local_r10 + 1))) goto loc_00C687B1;
    local_r13 = (uint32_t)((local_r13) | (0xFFFFFFFFULL));
    if (((uint8_t)(a3)) <= 2) goto loc_00C6868C;
loc_00C6855F:
    if ((*(uint64_t *)(a1 + 0xC - 0xC)) == -1) goto loc_00C68685;
    if ((*(uint16_t *)(a1 + 0xC)) < 2) goto loc_00C6867C;
    if (((uint32_t)(*(uint16_t *)(a1 + 0xC - 0x2))) >= 64) goto loc_00C6867C;
    a1 = (uint32_t)((v_stack_m38) & (4));
    local_r10 = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(a1 + 0xC - 0x2)))) + ((uint32_t)((uint32_t)((uint32_t)(*(uint16_t *)(a1 + 0xC - 0x2))))));
    result = -((uint32_t)((uint32_t)(a1)));
    local_rbx = (uint32_t)((local_rbx) & (32));
    local_r11 = (uint32_t)((local_r11) & ((uint32_t)(local_r10)));
    a1 = -(a1);
    result = (result) & (-4);
    local_r15 = (v_stack_m38) + (result);
loc_00C685BA:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rbx + (uint32_t)(v_stack_m48) - 1 * 1))) - ((uint32_t)(local_rbx + local_r11 * 1)));
    result = (uint32_t)((result) + 1);
    if (((uint32_t)(result)) >= 1) goto loc_00C685D5;
loc_00C685D0:
    goto loc_00C68635;
loc_00C685D5:
    result = ((uint32_t)((uint32_t)(local_rbx + (uint32_t)(v_stack_m48) - 1 * 1))) >> (6);
    result = (local_rbx + local_r11 * 1) >> (6);
    a1 = (uint8_t)((local_rbx + local_r11 * 1) & (63));
    a4 = (1) << ((uint8_t)(a1));
    a4 = (a4) - 1;
    result = ~(*(uint64_t *)(local_r15 + result * 8));
    a4 = (a4) | (result);
loc_00C68602:
    if (a4 != -1) goto loc_00C68619;
    a2 = (local_r15 + result * 8) + (8);
    if (a2 > (local_r15 + result * 8)) goto loc_00C685D0;
    a4 = ~(*(uint64_t *)(a2));
    goto loc_00C68602;
loc_00C68619:
    a2 = (a2) - (local_r15);
    a4 = ~(a4);
    a2 = (a2) >> (3);
    a2 = (uint32_t)((a2) << (6));
    a2 = (uint32_t)((a2) + ((uint32_t)(result)));
    if (((uint32_t)(a2)) > ((uint32_t)(local_rbx + (uint32_t)(v_stack_m48) - 1 * 1))) goto loc_00C685D0;
    if (((uint32_t)(a2)) != ((uint32_t)(local_r13))) goto loc_00C6864E;
loc_00C68635:
    if ((uint32_t)(local_r11) == 0) goto loc_00C68650;
    a2 = local_r10 + 1;
    if (((uint32_t)(local_r10 + 1)) > ((uint32_t)((uint32_t)(v_stack_m48)))) { a2 = (uint32_t)((uint32_t)(v_stack_m48)); }
    a2 = (uint32_t)((a2) + ((uint32_t)(local_r13)));
    local_r11 = 0;
    goto loc_00C685BA;
loc_00C6864E:
    a2 = (uint32_t)((a2) - ((uint32_t)(local_rbx)));
loc_00C68650:
    if (((uint32_t)(a2)) < ((uint32_t)(local_r10))) goto loc_00C6866D;
    if (((uint32_t)(a2)) >= ((uint32_t)(local_r10 + 2))) goto loc_00C6866D;
    a2 = (uint16_t)((a2) & (1));
    *(uint16_t *)(a1 + 0xC) = (uint16_t)(a2);
    goto loc_00C6867C;
loc_00C6866D:
    *(uint8_t *)(a1 + 0xC + 0x2) = 0;
    *(uint16_t *)(a1 + 0xC) = 1;
loc_00C6867C:
    a3 = (a1 + 12) + (16);
    goto loc_00C6855F;
loc_00C68685:
    *(uint8_t *)(v_rip + 0x35C976) = 2;
loc_00C6868C:
    local_r10 = 0;
    a1 = (uint32_t)((v_stack_m38) & (4));
    result = -((uint32_t)((uint32_t)(a1)));
    local_rbx = (uint32_t)((local_rbx) & (32));
    a1 = -(a1);
    result = (uint32_t)((result) & (4));
    local_rsi = (v_stack_m38) - (result);
loc_00C686B0:
    a4 = (uint32_t)((a4) & (0));
loc_00C686C1:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rbx + (uint32_t)(v_stack_m48) - 1 * 1))) - ((uint32_t)(local_rbx + a4 * 1)));
    result = (uint32_t)((result) + (1));
    if (((uint32_t)(result)) >= 1) goto loc_00C686DD;
loc_00C686D8:
    goto loc_00C6873A;
loc_00C686DD:
    result = ((uint32_t)((uint32_t)(local_rbx + (uint32_t)(v_stack_m48) - 1 * 1))) >> (6);
    result = (local_rbx + a4 * 1) >> (6);
    a1 = (uint8_t)((local_rbx + a4 * 1) & (63));
    a3 = (1) << ((uint8_t)(a1));
    a3 = (a3) - (1);
    result = ~(*(uint64_t *)(local_rsi + result * 8));
    a3 = (a3) | (result);
loc_00C68707:
    if (a3 != -1) goto loc_00C6871E;
    a2 = (local_rsi + result * 8) + (8);
    if (a2 > (local_rsi + result * 8)) goto loc_00C686D8;
    a3 = ~(*(uint64_t *)(a2));
    goto loc_00C68707;
loc_00C6871E:
    a2 = (a2) - (local_rsi);
    a3 = ~(a3);
    a2 = (a2) >> (3);
    a2 = (uint32_t)((a2) << (6));
    a2 = (uint32_t)((a2) + ((uint32_t)(result)));
    if (((uint32_t)(a2)) > ((uint32_t)(local_rbx + (uint32_t)(v_stack_m48) - 1 * 1))) goto loc_00C686D8;
    if (((uint32_t)(a2)) != ((uint32_t)(local_r13))) goto loc_00C68755;
loc_00C6873A:
    if ((uint32_t)(a4) == 0) goto loc_00C68757;
    result = local_r10 + 1;
    if (((uint32_t)(local_r10 + 1)) > ((uint32_t)((uint32_t)(v_stack_m48)))) { result = (uint32_t)((uint32_t)(v_stack_m48)); }
    result = (uint32_t)((result) + ((uint32_t)(local_r13)));
    a4 = 0;
    goto loc_00C686C1;
loc_00C68755:
    a2 = (uint32_t)((a2) - ((uint32_t)(local_rbx)));
loc_00C68757:
    if (((uint32_t)(a2)) == ((uint32_t)(local_r13))) goto loc_00C687A6;
    if (((uint32_t)(a2)) < 0) goto loc_00C687A6;
    result = (uint32_t)(((uint32_t)((uint32_t)(a2))) >> (1));
    if ((*(uint64_t *)(v_stack_m58)) == -1) goto loc_00C686B0;
    a3 = (v_stack_m58) + (12);
loc_00C6877B:
    if (((uint32_t)(*(uint16_t *)(a3 - 0x2))) != ((uint32_t)(result))) goto loc_00C68796;
    a1 = (uint16_t)(((uint16_t)(a2)) & (1));
    if ((*(uint16_t *)(a3)) == ((uint16_t)(a1))) {
        *(uint8_t *)(a3 + 0x2) = 0;
    }
    a3 = (a3) + (16);
    if ((*(uint64_t *)(a3 - 0xC)) != -1) goto loc_00C6877B;
    goto loc_00C686B0;
loc_00C687A6:
    *(uint64_t *)(v_rip + 0x1C5477) = v_stack_m58;
loc_00C687B1:
    a1 = (v_stack_m28) ^ (local_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C68424&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
