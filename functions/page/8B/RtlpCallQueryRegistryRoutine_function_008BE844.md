# RtlpCallQueryRegistryRoutine

- RVA: `0x008BE844`–`0x008BEBCE` (길이 `906` bytes)
- VA: `0x00000001408BE844`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0008320C`
- 디코드: `247`개 명령, `906/906` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **7**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x008BE919` → [RtlpQueryRegistryDirect](RtlpQueryRegistryDirect_function_008BEBD4.md) (function, `0x008BEBD4`)
- `0x008BE9A8` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x008BEA01` → [WmipSDRegistryQueryRoutine](WmipSDRegistryQueryRoutine_function_008BECE0.md) (function, `0x008BECE0`)
- `0x008BEA63` → [RtlpValidateKeyTrust](RtlpValidateKeyTrust_function_008BE114.md) (function, `0x008BE114`)
- `0x008BEB14` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x008BEB91` → [RtlpValidateKeyTrust](RtlpValidateKeyTrust_function_008BE114.md) (function, `0x008BE114`)
- `0x008BEBC4` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [RtlpQueryRegistryValues](../8C/RtlpQueryRegistryValues_function_008C9050.md) at `0x008C93BA`
- [RtlpQueryRegistryValues](../8C/RtlpQueryRegistryValues_function_008C9050.md) at `0x008C944F`
- [RtlpQueryRegistryValues](../8C/RtlpQueryRegistryValues_function_008C9050.md) at `0x008C94B5`

### Static image references
- `0x008BE9D1` → RVA `0x008BECE0` (`WmipSDRegistryQueryRoutine`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x008BE9A8` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x008BEB14` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x008BEBC4` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x008BEB88` → [sub_00B1AD48](../B1/Unknown_function_00B1AD48.md) (`tail-transfer`)
  - `0x008BEB9C` → [sub_00B1AD48](../B1/Unknown_function_00B1AD48.md) (`tail-transfer`)
  - `0x008BEBBC` → [sub_00B1AD48 + 0x1E](../B1/Unknown_function_00B1AD48.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
008BE844  48 8B C4                        mov rax, rsp
008BE847  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
008BE84B  48 89 68 18                     mov qword ptr [rax + 0x18], rbp
008BE84F  48 89 70 20                     mov qword ptr [rax + 0x20], rsi
008BE853  48 89 48 08                     mov qword ptr [rax + 8], rcx
008BE857  57                              push rdi
008BE858  41 54                           push r12
008BE85A  41 55                           push r13
008BE85C  41 56                           push r14
008BE85E  41 57                           push r15
008BE860  48 83 EC 40                     sub rsp, 0x40
008BE864  45 8B 21                        mov r12d, dword ptr [r9]
008BE867  33 DB                           xor ebx, ebx
008BE869  41 89 19                        mov dword ptr [r9], ebx
008BE86C  49 8B F0                        mov rsi, r8
008BE86F  8B 42 20                        mov eax, dword ptr [rdx + 0x20]
008BE872  4C 8B F2                        mov r14, rdx
008BE875  0F B6 E8                        movzx ebp, al
008BE878  4C 8B D1                        mov r10, rcx
008BE87B  41 8B 40 04                     mov eax, dword ptr [r8 + 4]
008BE87F  85 C0                           test eax, eax
008BE881  0F 84 C0 00 00 00               je 0x1408be947
008BE887  41 8B 50 08                     mov edx, dword ptr [r8 + 8]
008BE88B  83 FA FF                        cmp edx, -1
008BE88E  0F 84 B3 00 00 00               je 0x1408be947
008BE894  41 8B 48 0C                     mov ecx, dword ptr [r8 + 0xc]
008BE898  85 C9                           test ecx, ecx
008BE89A  0F 84 9B 02 00 00               je 0x1408beb3b
008BE8A0  41 8B 46 08                     mov eax, dword ptr [r14 + 8]
008BE8A4  A8 20                           test al, 0x20
008BE8A6  0F 84 B4 00 00 00               je 0x1408be960
008BE8AC  4D 8B 7E 10                     mov r15, qword ptr [r14 + 0x10]
008BE8B0  8B 7E 08                        mov edi, dword ptr [rsi + 8]
008BE8B3  8B 6E 04                        mov ebp, dword ptr [rsi + 4]
008BE8B6  48 03 FE                        add rdi, rsi
008BE8B9  8B 76 0C                        mov esi, dword ptr [rsi + 0xc]
008BE8BC  41 8B 4E 08                     mov ecx, dword ptr [r14 + 8]
008BE8C0  F6 C1 20                        test cl, 0x20
008BE8C3  74 17                           je 0x1408be8dc
008BE8C5  0F BA E1 08                     bt ecx, 8
008BE8C9  0F 83 CF 01 00 00               jae 0x1408bea9e
008BE8CF  41 0F B6 46 23                  movzx eax, byte ptr [r14 + 0x23]
008BE8D4  3B C5                           cmp eax, ebp
008BE8D6  0F 85 99 01 00 00               jne 0x1408bea75
008BE8DC  F6 C1 10                        test cl, 0x10
008BE8DF  75 12                           jne 0x1408be8f3
008BE8E1  83 FD 07                        cmp ebp, 7
008BE8E4  0F 84 D2 01 00 00               je 0x1408beabc
008BE8EA  83 FD 02                        cmp ebp, 2
008BE8ED  0F 84 AE 02 00 00               je 0x1408beba1
008BE8F3  41 8B 56 08                     mov edx, dword ptr [r14 + 8]
008BE8F7  F6 C2 20                        test dl, 0x20
008BE8FA  0F 84 CD 00 00 00               je 0x1408be9cd
008BE900  38 9C 24 A0 00 00 00            cmp byte ptr [rsp + 0xa0], bl
008BE907  0F 85 53 01 00 00               jne 0x1408bea60
008BE90D  4D 8B 4E 18                     mov r9, qword ptr [r14 + 0x18]
008BE911  44 8B C6                        mov r8d, esi
008BE914  48 8B D7                        mov rdx, rdi
008BE917  8B CD                           mov ecx, ebp
008BE919  E8 B6 02 00 00                  call 0x1408bebd4
008BE91E  3D 23 00 00 C0                  cmp eax, 0xc0000023
008BE923  0F 45 D8                        cmovne ebx, eax
008BE926  8B C3                           mov eax, ebx
008BE928  4C 8D 5C 24 40                  lea r11, [rsp + 0x40]
008BE92D  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
008BE931  49 8B 6B 40                     mov rbp, qword ptr [r11 + 0x40]
008BE935  49 8B 73 48                     mov rsi, qword ptr [r11 + 0x48]
008BE939  49 8B E3                        mov rsp, r11
008BE93C  41 5F                           pop r15
008BE93E  41 5E                           pop r14
008BE940  41 5D                           pop r13
008BE942  41 5C                           pop r12
008BE944  5F                              pop rdi
008BE945  C3                              ret
008BE946  CC                              int3
008BE947  85 ED                           test ebp, ebp
008BE949  0F 85 BC 00 00 00               jne 0x1408bea0b
008BE94F  41 8A 46 08                     mov al, byte ptr [r14 + 8]
008BE953  24 04                           and al, 4
008BE955  F6 D8                           neg al
008BE957  1B C0                           sbb eax, eax
008BE959  25 34 00 00 C0                  and eax, 0xc0000034
008BE95E  EB C8                           jmp 0x1408be928
008BE960  85 C9                           test ecx, ecx
008BE962  0F 84 2A 01 00 00               je 0x1408bea92
008BE968  8D 04 11                        lea eax, [rcx + rdx]
008BE96B  41 8B 50 10                     mov edx, dword ptr [r8 + 0x10]
008BE96F  44 8B F8                        mov r15d, eax
008BE972  49 83 C7 07                     add r15, 7
008BE976  4C 03 FE                        add r15, rsi
008BE979  8D 4A 02                        lea ecx, [rdx + 2]
008BE97C  49 83 E7 F8                     and r15, 0xfffffffffffffff8
008BE980  48 63 F9                        movsxd rdi, ecx
008BE983  48 83 FF 02                     cmp rdi, 2
008BE987  0F 82 FB 00 00 00               jb 0x1408bea88
008BE98D  44 03 E6                        add r12d, esi
008BE990  41 8B C4                        mov eax, r12d
008BE993  41 2B C7                        sub eax, r15d
008BE996  3B C1                           cmp eax, ecx
008BE998  0F 8C AF 00 00 00               jl 0x1408bea4d
008BE99E  44 8B C2                        mov r8d, edx
008BE9A1  49 8B CF                        mov rcx, r15
008BE9A4  48 8D 56 14                     lea rdx, [rsi + 0x14]
008BE9A8  E8 93 7E E0 FF                  call 0x1406c6840
008BE9AD  8B 46 10                        mov eax, dword ptr [rsi + 0x10]
008BE9B0  4C 8D 47 07                     lea r8, [rdi + 7]
008BE9B4  4C 8B 54 24 70                  mov r10, qword ptr [rsp + 0x70]
008BE9B9  4D 03 C7                        add r8, r15
008BE9BC  49 83 E0 F8                     and r8, 0xfffffffffffffff8
008BE9C0  45 2B E0                        sub r12d, r8d
008BE9C3  66 42 89 1C 38                  mov word ptr [rax + r15], bx
008BE9C8  E9 E3 FE FF FF                  jmp 0x1408be8b0
008BE9CD  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
008BE9D1  48 8D 0D 08 03 00 00            lea rcx, [rip + 0x308]
008BE9D8  4D 8B 16                        mov r10, qword ptr [r14]
008BE9DB  44 8B CE                        mov r9d, esi
008BE9DE  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008BE9E3  4C 3B D1                        cmp r10, rcx
008BE9E6  48 8B 84 24 90 00 00 00         mov rax, qword ptr [rsp + 0x90]
008BE9EE  4C 8B C7                        mov r8, rdi
008BE9F1  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008BE9F6  8B D5                           mov edx, ebp
008BE9F8  49 8B CF                        mov rcx, r15
008BE9FB  0F 85 C0 01 00 00               jne 0x1408bebc1
008BEA01  E8 DA 02 00 00                  call 0x1408bece0
008BEA06  E9 13 FF FF FF                  jmp 0x1408be91e
008BEA0B  41 8B 76 30                     mov esi, dword ptr [r14 + 0x30]
008BEA0F  4D 8B 7E 10                     mov r15, qword ptr [r14 + 0x10]
008BEA13  49 8B 7E 28                     mov rdi, qword ptr [r14 + 0x28]
008BEA17  85 F6                           test esi, esi
008BEA19  0F 85 9D FE FF FF               jne 0x1408be8bc
008BEA1F  8D 45 FF                        lea eax, [rbp - 1]
008BEA22  48 8B CF                        mov rcx, rdi
008BEA25  83 F8 01                        cmp eax, 1
008BEA28  76 55                           jbe 0x1408bea7f
008BEA2A  83 FD 07                        cmp ebp, 7
008BEA2D  0F 85 89 FE FF FF               jne 0x1408be8bc
008BEA33  48 85 FF                        test rdi, rdi
008BEA36  74 50                           je 0x1408bea88
008BEA38  66 39 1F                        cmp word ptr [rdi], bx
008BEA3B  0F 85 07 01 00 00               jne 0x1408beb48
008BEA41  8B F1                           mov esi, ecx
008BEA43  2B F7                           sub esi, edi
008BEA45  83 C6 02                        add esi, 2
008BEA48  E9 6F FE FF FF                  jmp 0x1408be8bc
008BEA4D  44 2B FE                        sub r15d, esi
008BEA50  B8 23 00 00 C0                  mov eax, 0xc0000023
008BEA55  44 03 F9                        add r15d, ecx
008BEA58  45 89 39                        mov dword ptr [r9], r15d
008BEA5B  E9 C8 FE FF FF                  jmp 0x1408be928
008BEA60  49 8B CA                        mov rcx, r10
008BEA63  E8 AC F6 FF FF                  call 0x1408be114
008BEA68  85 C0                           test eax, eax
008BEA6A  0F 89 9D FE FF FF               jns 0x1408be90d
008BEA70  E9 B3 FE FF FF                  jmp 0x1408be928
008BEA75  B8 24 00 00 C0                  mov eax, 0xc0000024
008BEA7A  E9 A9 FE FF FF                  jmp 0x1408be928
008BEA7F  48 85 FF                        test rdi, rdi
008BEA82  0F 85 D6 00 00 00               jne 0x1408beb5e
008BEA88  B8 3C 00 00 C0                  mov eax, 0xc000003c
008BEA8D  E9 96 FE FF FF                  jmp 0x1408be928
008BEA92  41 8B 40 10                     mov eax, dword ptr [r8 + 0x10]
008BEA96  83 C0 14                        add eax, 0x14
008BEA99  E9 CD FE FF FF                  jmp 0x1408be96b
008BEA9E  84 C9                           test cl, cl
008BEAA0  0F 89 36 FE FF FF               jns 0x1408be8dc
008BEAA6  8D 45 FF                        lea eax, [rbp - 1]
008BEAA9  83 F8 01                        cmp eax, 1
008BEAAC  0F 87 C1 00 00 00               ja 0x1408beb73
008BEAB2  80 E1 04                        and cl, 4
008BEAB5  F6 D9                           neg cl
008BEAB7  E9 9B FE FF FF                  jmp 0x1408be957
008BEABC  44 8B E6                        mov r12d, esi
008BEABF  8B CB                           mov ecx, ebx
008BEAC1  49 83 C4 FC                     add r12, -4
008BEAC5  48 8B F7                        mov rsi, rdi
008BEAC8  4C 03 E7                        add r12, rdi
008BEACB  49 3B FC                        cmp rdi, r12
008BEACE  73 64                           jae 0x1408beb34
008BEAD0  4C 8B AC 24 90 00 00 00         mov r13, qword ptr [rsp + 0x90]
008BEAD8  0F B7 06                        movzx eax, word ptr [rsi]
008BEADB  48 83 C6 02                     add rsi, 2
008BEADF  66 85 C0                        test ax, ax
008BEAE2  75 F4                           jne 0x1408bead8
008BEAE4  41 8B 56 08                     mov edx, dword ptr [r14 + 8]
008BEAE8  8B EE                           mov ebp, esi
008BEAEA  2B EF                           sub ebp, edi
008BEAEC  F6 C2 20                        test dl, 0x20
008BEAEF  0F 85 8C 00 00 00               jne 0x1408beb81
008BEAF5  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
008BEAF9  44 8B CD                        mov r9d, ebp
008BEAFC  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008BEB01  4C 8B C7                        mov r8, rdi
008BEB04  49 8B 06                        mov rax, qword ptr [r14]
008BEB07  BA 01 00 00 00                  mov edx, 1
008BEB0C  49 8B CF                        mov rcx, r15
008BEB0F  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
008BEB14  E8 B7 BF DF FF                  call 0x1406baad0
008BEB19  3D 23 00 00 C0                  cmp eax, 0xc0000023
008BEB1E  8B CB                           mov ecx, ebx
008BEB20  0F 45 C8                        cmovne ecx, eax
008BEB23  85 C9                           test ecx, ecx
008BEB25  78 0D                           js 0x1408beb34
008BEB27  4C 8B 54 24 70                  mov r10, qword ptr [rsp + 0x70]
008BEB2C  48 8B FE                        mov rdi, rsi
008BEB2F  49 3B F4                        cmp rsi, r12
008BEB32  72 A4                           jb 0x1408bead8
008BEB34  8B C1                           mov eax, ecx
008BEB36  E9 ED FD FF FF                  jmp 0x1408be928
008BEB3B  3B C5                           cmp eax, ebp
008BEB3D  0F 84 04 FE FF FF               je 0x1408be947
008BEB43  E9 58 FD FF FF                  jmp 0x1408be8a0
008BEB48  0F B7 01                        movzx eax, word ptr [rcx]
008BEB4B  48 83 C1 02                     add rcx, 2
008BEB4F  66 85 C0                        test ax, ax
008BEB52  75 F4                           jne 0x1408beb48
008BEB54  66 39 19                        cmp word ptr [rcx], bx
008BEB57  75 EF                           jne 0x1408beb48
008BEB59  E9 E3 FE FF FF                  jmp 0x1408bea41
008BEB5E  0F B7 01                        movzx eax, word ptr [rcx]
008BEB61  48 83 C1 02                     add rcx, 2
008BEB65  66 85 C0                        test ax, ax
008BEB68  75 F4                           jne 0x1408beb5e
008BEB6A  8B F1                           mov esi, ecx
008BEB6C  2B F7                           sub esi, edi
008BEB6E  E9 49 FD FF FF                  jmp 0x1408be8bc
008BEB73  83 FD 07                        cmp ebp, 7
008BEB76  0F 85 60 FD FF FF               jne 0x1408be8dc
008BEB7C  E9 31 FF FF FF                  jmp 0x1408beab2
008BEB81  38 9C 24 A0 00 00 00            cmp byte ptr [rsp + 0xa0], bl
008BEB88  0F 84 BA C1 25 00               je 0x140b1ad48
008BEB8E  49 8B CA                        mov rcx, r10
008BEB91  E8 7E F5 FF FF                  call 0x1408be114
008BEB96  8B C8                           mov ecx, eax
008BEB98  85 C0                           test eax, eax
008BEB9A  78 98                           js 0x1408beb34
008BEB9C  E9 A7 C1 25 00                  jmp 0x140b1ad48
008BEBA1  8D 46 FE                        lea eax, [rsi - 2]
008BEBA4  3D FA FF 00 00                  cmp eax, 0xfffa
008BEBA9  0F 87 44 FD FF FF               ja 0x1408be8f3
008BEBAF  40 F6 C6 01                     test sil, 1
008BEBB3  0F 85 3A FD FF FF               jne 0x1408be8f3
008BEBB9  48 8B CF                        mov rcx, rdi
008BEBBC  E9 A5 C1 25 00                  jmp 0x140b1ad66
008BEBC1  49 8B C2                        mov rax, r10
008BEBC4  E8 07 BF DF FF                  call 0x1406baad0
008BEBC9  E9 50 FD FF FF                  jmp 0x1408be91e
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpCallQueryRegistryRoutine(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, unsigned __int8 a7)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_p30;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 32) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (64);
    v_rbx = 0;
    *(unsigned int *)(a4) = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 4))) == 0) goto loc_008BE947;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 8)))) == -1) goto loc_008BE947;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 12))) == 0) goto loc_008BEB3B;
loc_008BE8A0:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 8)))) & (32)) == 0) goto loc_008BE960;
loc_008BE8B0:
    v_rdi = ((unsigned int)(*(unsigned int *)(a3 + 8))) + (a3);
loc_008BE8BC:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 8)))) & (32)) == 0) goto loc_008BE8DC;
    if (condition_is_above_or_equal) goto loc_008BEA9E;
    if (((unsigned int)(*(unsigned __int8 *)(a2 + 35))) != ((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 4))))) goto loc_008BEA75;
loc_008BE8DC:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 8)))) & (16)) != 0) goto loc_008BE8F3;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 4)))) == 7) goto loc_008BEABC;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 4)))) == 2) goto loc_008BEBA1;
loc_008BE8F3:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 8)))) & (32)) == 0) goto loc_008BE9CD;
    if (a7 != 0) goto loc_008BEA60;
loc_008BE90D:
    result = RtlpQueryRegistryDirect((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 4)))), v_rdi, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 12)))), *(unsigned __int64 *)(a2 + 24));
loc_008BE91E:
    if (((unsigned int)(result)) != 0xC0000023ULL) { v_rbx = (unsigned int)(result); }
loc_008BE928:
    return (unsigned int)((unsigned int)(v_rbx));
loc_008BE947:
    if ((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 64)) != 0) goto loc_008BEA0B;
    result = (unsigned __int8)((*(unsigned __int8 *)(a2 + 8)) & (4));
    result = (unsigned __int8)(-(result));
loc_008BE957:
    result = (unsigned int)((result) & (0xC0000034ULL));
    goto loc_008BE928;
loc_008BE960:
    if ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 4))))) == 0) goto loc_008BEA92;
loc_008BE96B:
    v_r15 = ((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 4)))) + v_rdi * 1))) + (7);
    v_r15 = (v_r15) + (*(unsigned __int64 *)(v_stack_m28 + 72));
    v_r15 = (v_r15) & (-8);
    if (((int)((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 12)))) + 16)) + 2))) < 2) goto loc_008BEA88;
    v_r12 = (unsigned int)(((unsigned int)(*(unsigned int *)(a4))) + ((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 72))));
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) - ((unsigned int)(v_r15)));
    if (((unsigned int)(result)) < ((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 12)))) + 16)) + 2))) goto loc_008BEA4D;
    result = memcpy(v_r15, *(unsigned __int64 *)(v_stack_m28 + 72) + 20, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 12)))) + 16)))), *(unsigned __int64 *)(a2 + 24));
    a3 = ((int)((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 12)))) + 16)) + 2)) + 7) + (v_r15);
    a3 = (a3) & (-8);
    v_r12 = (unsigned int)((v_r12) - ((unsigned int)(a3)));
    *(unsigned __int16 *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 16)) + v_r15 * 1) = (unsigned __int16)(*(unsigned __int64 *)(v_stack_m28 + 56));
    goto loc_008BE8B0;
loc_008BE9CD:
    v_stack_m18 = *(unsigned __int64 *)(a2 + 24);
    v_stack_m20 = a5;
    if ((*(unsigned __int64 *)(a2)) != (v_rip + 776)) goto loc_008BEBC1;
    result = WmipSDRegistryQueryRoutine(v_r15, (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 64))), (int)((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 12)))) + 16)) + 2)), (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 72))));
    goto loc_008BE91E;
loc_008BEA0B:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 48))) != 0) goto loc_008BE8BC;
    if (((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 64) - 1)) <= 1) goto loc_008BEA7F;
    if (((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 64))) != 7) goto loc_008BE8BC;
    if (*(unsigned __int64 *)(a2 + 40) == 0) goto loc_008BEA88;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 40))) != ((unsigned __int16)(*(unsigned __int64 *)(v_stack_m28 + 56)))) goto loc_008BEB48;
loc_008BEA41:
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int64 *)(a2 + 40)))) - ((unsigned int)(*(unsigned __int64 *)(a2 + 40))));
    v_rsi = (unsigned int)((v_rsi) + (2));
    goto loc_008BE8BC;
loc_008BEA4D:
    v_r15 = (unsigned int)((*(unsigned __int64 *)(a2 + 16)) - ((unsigned int)(v_rsi)));
    v_r15 = (unsigned int)((v_r15) + ((unsigned int)(*(unsigned __int64 *)(a2 + 40))));
    *(unsigned int *)((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 72)))) = (unsigned int)(v_r15);
    goto loc_008BE928;
loc_008BEA60:
    result = RtlpValidateKeyTrust(*(unsigned __int64 *)(a2), (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 64))), (int)((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 12)))) + 16)) + 2)), (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 72))));
    if (!sign_flag) goto loc_008BE90D;
    goto loc_008BE928;
loc_008BEA75:
    goto loc_008BE928;
loc_008BEA7F:
    if (*(unsigned __int64 *)(a2 + 40) != 0) goto loc_008BEB5E;
loc_008BEA88:
    goto loc_008BE928;
loc_008BEA92:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)((int)((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 12)))) + 16)) + 2)) + 16))) + (20));
    goto loc_008BE96B;
loc_008BEA9E:
    if (!sign_flag) goto loc_008BE8DC;
    if (((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 64) - 1)) > 1) goto loc_008BEB73;
loc_008BEAB2:
    a1 = (unsigned __int8)((*(unsigned __int64 *)(a2)) & (4));
    a1 = (unsigned __int8)(-(a1));
    goto loc_008BE957;
loc_008BEABC:
    v_r12 = ((unsigned int)((unsigned int)(v_rsi))) + (-4);
    v_r12 = (v_r12) + (*(unsigned __int64 *)(a2 + 40));
    if ((*(unsigned __int64 *)(a2 + 40)) >= v_r12) goto loc_008BEB34;
loc_008BEAD8:
    v_rsi = (*(unsigned __int64 *)(a2 + 40)) + (2);
    if ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 40))) != 0) goto loc_008BEAD8;
    v_rbp = (unsigned int)(((unsigned int)((unsigned int)(v_rsi))) - ((unsigned int)(*(unsigned __int64 *)(a2 + 40))));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 8)))) & (32)) != 0) goto loc_008BEB81;
    v_stack_m18 = *(unsigned __int64 *)(a2 + 24);
    v_stack_m20 = a5;
    result = guard_dispatch_icall(v_r15, 1, *(unsigned __int64 *)(a2 + 40), (unsigned int)((unsigned int)(v_rbp)));
    a1 = (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 56)));
    if (((unsigned int)(result)) != 0xC0000023ULL) { a1 = (unsigned int)(result); }
    if (sign_flag) goto loc_008BEB34;
    if (v_rsi < v_r12) goto loc_008BEAD8;
loc_008BEB34:
    goto loc_008BE928;
loc_008BEB3B:
    if (((unsigned int)((unsigned int)((unsigned int)(a1)))) == ((unsigned int)(v_rbp))) goto loc_008BE947;
    goto loc_008BE8A0;
loc_008BEB48:
    a1 = (a1) + (2);
    if ((unsigned __int16)(*(unsigned __int16 *)(a1)) != 0) goto loc_008BEB48;
    if ((*(unsigned __int16 *)(a1)) != ((unsigned __int16)(*(unsigned __int64 *)(v_stack_m28 + 56)))) goto loc_008BEB48;
    goto loc_008BEA41;
loc_008BEB5E:
    a1 = (a1) + (2);
    if ((unsigned __int16)(*(unsigned __int16 *)(a1)) != 0) goto loc_008BEB5E;
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(a1))) - ((unsigned int)(v_rsi)));
    goto loc_008BE8BC;
loc_008BEB73:
    if (((unsigned int)(v_rbp)) != 7) goto loc_008BE8DC;
    goto loc_008BEAB2;
loc_008BEB81:
    result = RtlpValidateKeyTrust(v_stack_p30, 1, *(unsigned __int64 *)(a2 + 40), (unsigned int)((unsigned int)(v_rbp)));
    if (sign_flag) goto loc_008BEB34;
loc_008BEBA1:
    if (((unsigned int)(v_rsi - 2)) > 0xFFFAULL) goto loc_008BE8F3;
    if ((((unsigned __int8)(v_rsi)) & (1)) != 0) goto loc_008BE8F3;
loc_008BEBC1:
    result = guard_dispatch_icall(v_rsi, 1, *(unsigned __int64 *)(a2 + 40), (unsigned int)((unsigned int)(v_rbp)));
    goto loc_008BE91E;
}
```

## 5. (Beta) C Style

```c
int64_t RtlpCallQueryRegistryRoutine(int64_t Arg1, void *Arg2, void *Arg3, void *Arg4, int64_t Arg5, uint64_t Arg6, uint8_t Arg7)
{
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r12;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_p30;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rbp;
    *(uint64_t *)(local_rsp + 0x20) = local_rsi;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (64);
    local_rbx = 0;
    *(uint32_t *)(arg4) = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0x4))) == 0) goto loc_008BE947;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0x8)))) == -1) goto loc_008BE947;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0xC))) == 0) goto loc_008BEB3B;
loc_008BE8A0:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0x8)))) & (32)) == 0) goto loc_008BE960;
loc_008BE8B0:
    local_rdi = ((uint32_t)(*(uint32_t *)(arg3 + 0x8))) + (Arg3);
loc_008BE8BC:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0x8)))) & (32)) == 0) goto loc_008BE8DC;
    if (condition_is_above_or_equal) goto loc_008BEA9E;
    if (((uint32_t)(*(uint8_t *)(arg2 + 0x23))) != ((uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0x4))))) goto loc_008BEA75;
loc_008BE8DC:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0x8)))) & (16)) != 0) goto loc_008BE8F3;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0x4)))) == 7) goto loc_008BEABC;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0x4)))) == 2) goto loc_008BEBA1;
loc_008BE8F3:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0x8)))) & (32)) == 0) goto loc_008BE9CD;
    if (Arg7 != 0) goto loc_008BEA60;
loc_008BE90D:
    result = RtlpQueryRegistryDirect((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0x4)))), local_rdi, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0xC)))), *(uint64_t *)(arg2 + 0x18));
loc_008BE91E:
    if (((uint32_t)(result)) != 0xC0000023ULL) { local_rbx = (uint32_t)(result); }
loc_008BE928:
    return (uint32_t)((uint32_t)(local_rbx));
loc_008BE947:
    if ((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x40)) != 0) goto loc_008BEA0B;
    result = (uint8_t)((*(uint8_t *)(arg2 + 0x8)) & (4));
    result = (uint8_t)(-(result));
loc_008BE957:
    result = (uint32_t)((result) & (0xC0000034ULL));
    goto loc_008BE928;
loc_008BE960:
    if ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0x4))))) == 0) goto loc_008BEA92;
loc_008BE96B:
    local_r15 = ((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0x4)))) + local_rdi * 1))) + (7);
    local_r15 = (local_r15) + (*(uint64_t *)(v_stack_m28 + 0x48));
    local_r15 = (local_r15) & (-8);
    if (((int32_t)((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0xC)))) + 0x10)) + 2))) < 2) goto loc_008BEA88;
    local_r12 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg4))) + ((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x48))));
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) - ((uint32_t)(local_r15)));
    if (((uint32_t)(result)) < ((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0xC)))) + 0x10)) + 2))) goto loc_008BEA4D;
    result = memcpy(local_r15, *(uint64_t *)(v_stack_m28 + 0x48) + 20, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0xC)))) + 0x10)))), *(uint64_t *)(arg2 + 0x18));
    Arg3 = ((int32_t)((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0xC)))) + 0x10)) + 2)) + 7) + (local_r15);
    Arg3 = (Arg3) & (-8);
    local_r12 = (uint32_t)((local_r12) - ((uint32_t)(Arg3)));
    *(uint16_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x10)) + local_r15 * 1) = (uint16_t)(*(uint64_t *)(v_stack_m28 + 0x38));
    goto loc_008BE8B0;
loc_008BE9CD:
    v_stack_m18 = *(uint64_t *)(arg2 + 0x18);
    v_stack_m20 = Arg5;
    if ((*(uint64_t *)(arg2)) != (v_rip + 776)) goto loc_008BEBC1;
    result = WmipSDRegistryQueryRoutine(local_r15, (uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x40))), (int32_t)((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0xC)))) + 0x10)) + 2)), (uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x48))));
    goto loc_008BE91E;
loc_008BEA0B:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x30))) != 0) goto loc_008BE8BC;
    if (((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x40) - 1)) <= 1) goto loc_008BEA7F;
    if (((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x40))) != 7) goto loc_008BE8BC;
    if (*(uint64_t *)(arg2 + 0x28) == 0) goto loc_008BEA88;
    if ((*(uint16_t *)(*(uint64_t *)(arg2 + 0x28))) != ((uint16_t)(*(uint64_t *)(v_stack_m28 + 0x38)))) goto loc_008BEB48;
loc_008BEA41:
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(*(uint64_t *)(arg2 + 0x28)))) - ((uint32_t)(*(uint64_t *)(arg2 + 0x28))));
    local_rsi = (uint32_t)((local_rsi) + (2));
    goto loc_008BE8BC;
loc_008BEA4D:
    local_r15 = (uint32_t)((*(uint64_t *)(arg2 + 0x10)) - ((uint32_t)(local_rsi)));
    local_r15 = (uint32_t)((local_r15) + ((uint32_t)(*(uint64_t *)(arg2 + 0x28))));
    *(uint32_t *)((uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x48)))) = (uint32_t)(local_r15);
    goto loc_008BE928;
loc_008BEA60:
    result = RtlpValidateKeyTrust(*(uint64_t *)(arg2), (uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x40))), (int32_t)((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0xC)))) + 0x10)) + 2)), (uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x48))));
    if (!sign_flag) goto loc_008BE90D;
    goto loc_008BE928;
loc_008BEA75:
    goto loc_008BE928;
loc_008BEA7F:
    if (*(uint64_t *)(arg2 + 0x28) != 0) goto loc_008BEB5E;
loc_008BEA88:
    goto loc_008BE928;
loc_008BEA92:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)((int32_t)((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0xC)))) + 0x10)) + 0x2)) + 0x10))) + (20));
    goto loc_008BE96B;
loc_008BEA9E:
    if (!sign_flag) goto loc_008BE8DC;
    if (((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x40) - 1)) > 1) goto loc_008BEB73;
loc_008BEAB2:
    Arg1 = (uint8_t)((*(uint64_t *)(arg2)) & (4));
    Arg1 = (uint8_t)(-(Arg1));
    goto loc_008BE957;
loc_008BEABC:
    local_r12 = ((uint32_t)((uint32_t)(local_rsi))) + (-4);
    local_r12 = (local_r12) + (*(uint64_t *)(arg2 + 0x28));
    if ((*(uint64_t *)(arg2 + 0x28)) >= local_r12) goto loc_008BEB34;
loc_008BEAD8:
    local_rsi = (*(uint64_t *)(arg2 + 0x28)) + (2);
    if ((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg2 + 0x28))) != 0) goto loc_008BEAD8;
    local_rbp = (uint32_t)(((uint32_t)((uint32_t)(local_rsi))) - ((uint32_t)(*(uint64_t *)(arg2 + 0x28))));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0x8)))) & (32)) != 0) goto loc_008BEB81;
    v_stack_m18 = *(uint64_t *)(arg2 + 0x18);
    v_stack_m20 = Arg5;
    result = guard_dispatch_icall(local_r15, 1, *(uint64_t *)(arg2 + 0x28), (uint32_t)((uint32_t)(local_rbp)));
    Arg1 = (uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x38)));
    if (((uint32_t)(result)) != 0xC0000023ULL) { Arg1 = (uint32_t)(result); }
    if (sign_flag) goto loc_008BEB34;
    if (local_rsi < local_r12) goto loc_008BEAD8;
loc_008BEB34:
    goto loc_008BE928;
loc_008BEB3B:
    if (((uint32_t)((uint32_t)((uint32_t)(Arg1)))) == ((uint32_t)(local_rbp))) goto loc_008BE947;
    goto loc_008BE8A0;
loc_008BEB48:
    Arg1 = (Arg1) + (2);
    if ((uint16_t)(*(uint16_t *)(Arg1)) != 0) goto loc_008BEB48;
    if ((*(uint16_t *)(Arg1)) != ((uint16_t)(*(uint64_t *)(v_stack_m28 + 0x38)))) goto loc_008BEB48;
    goto loc_008BEA41;
loc_008BEB5E:
    Arg1 = (Arg1) + (2);
    if ((uint16_t)(*(uint16_t *)(Arg1)) != 0) goto loc_008BEB5E;
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) - ((uint32_t)(local_rsi)));
    goto loc_008BE8BC;
loc_008BEB73:
    if (((uint32_t)(local_rbp)) != 7) goto loc_008BE8DC;
    goto loc_008BEAB2;
loc_008BEB81:
    result = RtlpValidateKeyTrust(v_stack_p30, 1, *(uint64_t *)(arg2 + 0x28), (uint32_t)((uint32_t)(local_rbp)));
    if (sign_flag) goto loc_008BEB34;
loc_008BEBA1:
    if (((uint32_t)(local_rsi - 2)) > 0xFFFAULL) goto loc_008BE8F3;
    if ((((uint8_t)(local_rsi)) & (1)) != 0) goto loc_008BE8F3;
loc_008BEBC1:
    result = guard_dispatch_icall(local_rsi, 1, *(uint64_t *)(arg2 + 0x28), (uint32_t)((uint32_t)(local_rbp)));
    goto loc_008BE91E;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x8` | `8` | `R` |
| `Arg2` | `+ 0x8` | `32` | `R` |
| `Arg2` | `+ 0x10` | `64` | `R` |
| `Arg2` | `+ 0x18` | `64` | `R` |
| `Arg2` | `+ 0x20` | `32` | `R` |
| `Arg2` | `+ 0x23` | `8` | `R` |
| `Arg2` | `+ 0x28` | `64` | `R` |
| `Arg2` | `+ 0x30` | `32` | `R` |
| `Arg3` | `+ 0x4` | `32` | `R` |
| `Arg3` | `+ 0x8` | `32` | `R` |
| `Arg3` | `+ 0xC` | `32` | `R` |
| `Arg3` | `+ 0x10` | `32` | `R` |
| `Arg3` | `+ 0x14` | `64` | `R` |
| `Arg4` | `+ 0x0` | `32` | `R` |
| `Arg4` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008BE844&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
