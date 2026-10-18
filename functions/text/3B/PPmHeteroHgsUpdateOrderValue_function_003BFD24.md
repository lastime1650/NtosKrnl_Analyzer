# PPmHeteroHgsUpdateOrderValue

- RVA: `0x003BFD24`–`0x003C00AC` (길이 `904` bytes)
- VA: `0x00000001403BFD24`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0008DF30`
- 디코드: `260`개 명령, `904/904` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **8**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x003BFD54` → [KeIsEmptyAffinityEx](../2D/KeIsEmptyAffinityEx_function_002D1580.md) (function, `0x002D1580`)
- `0x003BFD64` → [KeIsEmptyAffinityEx](../2D/KeIsEmptyAffinityEx_function_002D1580.md) (function, `0x002D1580`)
- `0x003BFDB3` → [KeGetPrcb](../2D/KeGetPrcb_function_002D85D0.md) (function, `0x002D85D0`)
- `0x003BFE45` → [KeCountSetBitsAffinityEx](../2C/KeCountSetBitsAffinityEx_function_002CE6E0.md) (function, `0x002CE6E0`)
- `0x003BFE9F` → [KeGetPrcb](../2D/KeGetPrcb_function_002D85D0.md) (function, `0x002D85D0`)
- `0x003BFF50` → [KeGetPrcb](../2D/KeGetPrcb_function_002D85D0.md) (function, `0x002D85D0`)
- `0x003BFFEC` → [KeGetPrcb](../2D/KeGetPrcb_function_002D85D0.md) (function, `0x002D85D0`)
- `0x003C007F` → [KeGetPrcb](../2D/KeGetPrcb_function_002D85D0.md) (function, `0x002D85D0`)

### Direct callers
- [PpmHeteroUpdateHgsConfiguration](PpmHeteroUpdateHgsConfiguration_function_003BF344.md) at `0x003BF86A`
- [PpmHeteroUpdateHgsConfiguration](PpmHeteroUpdateHgsConfiguration_function_003BF344.md) at `0x003BF886`

### Static image references
- `0x003BFDA9` → RVA `0x00F231B8` (`.data`; read)
- `0x003BFE00` → RVA `0x00E0B5A8` (`.data`; read)
- `0x003BFE10` → RVA `0x00E0B5A0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x003C008E` → [sub_006E7DA2](../6E/Unknown_function_006E7DA2.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003BFD24  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
003BFD29  44 88 4C 24 20                  mov byte ptr [rsp + 0x20], r9b
003BFD2E  44 89 44 24 18                  mov dword ptr [rsp + 0x18], r8d
003BFD33  55                              push rbp
003BFD34  56                              push rsi
003BFD35  57                              push rdi
003BFD36  41 54                           push r12
003BFD38  41 55                           push r13
003BFD3A  41 56                           push r14
003BFD3C  41 57                           push r15
003BFD3E  48 83 EC 30                     sub rsp, 0x30
003BFD42  45 33 E4                        xor r12d, r12d
003BFD45  45 8B F0                        mov r14d, r8d
003BFD48  45 8A FC                        mov r15b, r12b
003BFD4B  45 8A E9                        mov r13b, r9b
003BFD4E  48 8B EA                        mov rbp, rdx
003BFD51  48 8B F9                        mov rdi, rcx
003BFD54  E8 27 18 F1 FF                  call 0x1402d1580
003BFD59  85 C0                           test eax, eax
003BFD5B  0F 85 9F 00 00 00               jne 0x1403bfe00
003BFD61  48 8B CD                        mov rcx, rbp
003BFD64  E8 17 18 F1 FF                  call 0x1402d1580
003BFD69  4C 8B 75 08                     mov r14, qword ptr [rbp + 8]
003BFD6D  33 D2                           xor edx, edx
003BFD6F  44 8B A4 24 80 00 00 00         mov r12d, dword ptr [rsp + 0x80]
003BFD77  0F B7 F2                        movzx esi, dx
003BFD7A  89 44 24 2C                     mov dword ptr [rsp + 0x2c], eax
003BFD7E  8D 5A 01                        lea ebx, [rdx + 1]
003BFD81  89 54 24 28                     mov dword ptr [rsp + 0x28], edx
003BFD85  48 85 ED                        test rbp, rbp
003BFD88  74 5E                           je 0x1403bfde8
003BFD8A  0F B7 4D 00                     movzx ecx, word ptr [rbp]
003BFD8E  4D 85 F6                        test r14, r14
003BFD91  74 5C                           je 0x1403bfdef
003BFD93  49 0F BC D6                     bsf rdx, r14
003BFD97  0F B7 CE                        movzx ecx, si
003BFD9A  0F B6 C2                        movzx eax, dl
003BFD9D  49 0F B3 C6                     btr r14, rax
003BFDA1  C1 E1 06                        shl ecx, 6
003BFDA4  0F B6 C2                        movzx eax, dl
003BFDA7  03 C8                           add ecx, eax
003BFDA9  48 8B 05 08 34 B6 00            mov rax, qword ptr [rip + 0xb63408]
003BFDB0  8B 0C 88                        mov ecx, dword ptr [rax + rcx*4]
003BFDB3  E8 18 88 F1 FF                  call 0x1402d85d0
003BFDB8  33 D2                           xor edx, edx
003BFDBA  48 8B 88 50 8A 00 00            mov rcx, qword ptr [rax + 0x8a50]
003BFDC1  45 84 ED                        test r13b, r13b
003BFDC4  74 11                           je 0x1403bfdd7
003BFDC6  42 38 54 A1 04                  cmp byte ptr [rcx + r12*4 + 4], dl
003BFDCB  74 B4                           je 0x1403bfd81
003BFDCD  44 8A FB                        mov r15b, bl
003BFDD0  42 88 54 A1 04                  mov byte ptr [rcx + r12*4 + 4], dl
003BFDD5  EB AA                           jmp 0x1403bfd81
003BFDD7  42 38 54 A1 05                  cmp byte ptr [rcx + r12*4 + 5], dl
003BFDDC  74 A3                           je 0x1403bfd81
003BFDDE  44 8A FB                        mov r15b, bl
003BFDE1  42 88 54 A1 05                  mov byte ptr [rcx + r12*4 + 5], dl
003BFDE6  EB 99                           jmp 0x1403bfd81
003BFDE8  0F B7 CE                        movzx ecx, si
003BFDEB  03 CB                           add ecx, ebx
003BFDED  EB 9F                           jmp 0x1403bfd8e
003BFDEF  66 03 F3                        add si, bx
003BFDF2  0F B7 F6                        movzx esi, si
003BFDF5  3B F1                           cmp esi, ecx
003BFDF7  73 42                           jae 0x1403bfe3b
003BFDF9  4C 8B 74 F5 08                  mov r14, qword ptr [rbp + rsi*8 + 8]
003BFDFE  EB 8E                           jmp 0x1403bfd8e
003BFE00  48 8B 35 A1 B7 A4 00            mov rsi, qword ptr [rip + 0xa4b7a1]
003BFE07  41 0F B7 FC                     movzx edi, r12w
003BFE0B  BB 01 00 00 00                  mov ebx, 1
003BFE10  0F B7 0D 89 B7 A4 00            movzx ecx, word ptr [rip + 0xa4b789]
003BFE17  48 85 F6                        test rsi, rsi
003BFE1A  0F 85 3F 02 00 00               jne 0x1403c005f
003BFE20  66 03 FB                        add di, bx
003BFE23  0F B7 FF                        movzx edi, di
003BFE26  3B F9                           cmp edi, ecx
003BFE28  0F 83 B9 00 00 00               jae 0x1403bfee7
003BFE2E  48 8D 35 73 B7 A4 00            lea rsi, [rip + 0xa4b773]
003BFE35  48 8B 34 FE                     mov rsi, qword ptr [rsi + rdi*8]
003BFE39  EB DC                           jmp 0x1403bfe17
003BFE3B  83 CD FF                        or ebp, 0xffffffff
003BFE3E  48 8B CF                        mov rcx, rdi
003BFE41  89 6C 24 28                     mov dword ptr [rsp + 0x28], ebp
003BFE45  E8 96 E8 F0 FF                  call 0x1402ce6e0
003BFE4A  44 8B 64 24 2C                  mov r12d, dword ptr [rsp + 0x2c]
003BFE4F  45 33 C0                        xor r8d, r8d
003BFE52  89 44 24 24                     mov dword ptr [rsp + 0x24], eax
003BFE56  85 C0                           test eax, eax
003BFE58  0F 84 89 00 00 00               je 0x1403bfee7
003BFE5E  45 85 E4                        test r12d, r12d
003BFE61  41 0F 94 C6                     sete r14b
003BFE65  44 88 74 24 21                  mov byte ptr [rsp + 0x21], r14b
003BFE6A  48 8B 6F 08                     mov rbp, qword ptr [rdi + 8]
003BFE6E  41 0F B7 F0                     movzx esi, r8w
003BFE72  48 85 FF                        test rdi, rdi
003BFE75  74 45                           je 0x1403bfebc
003BFE77  0F B7 0F                        movzx ecx, word ptr [rdi]
003BFE7A  48 85 ED                        test rbp, rbp
003BFE7D  74 44                           je 0x1403bfec3
003BFE7F  48 0F BC D5                     bsf rdx, rbp
003BFE83  0F B7 CE                        movzx ecx, si
003BFE86  0F B6 C2                        movzx eax, dl
003BFE89  48 0F B3 C5                     btr rbp, rax
003BFE8D  C1 E1 06                        shl ecx, 6
003BFE90  0F B6 C2                        movzx eax, dl
003BFE93  03 C8                           add ecx, eax
003BFE95  48 8B 05 1C 33 B6 00            mov rax, qword ptr [rip + 0xb6331c]
003BFE9C  8B 0C 88                        mov ecx, dword ptr [rax + rcx*4]
003BFE9F  E8 2C 87 F1 FF                  call 0x1402d85d0
003BFEA4  45 33 C0                        xor r8d, r8d
003BFEA7  44 38 80 4C 8A 00 00            cmp byte ptr [rax + 0x8a4c], r8b
003BFEAE  74 C2                           je 0x1403bfe72
003BFEB0  44 8A FB                        mov r15b, bl
003BFEB3  44 88 80 4C 8A 00 00            mov byte ptr [rax + 0x8a4c], r8b
003BFEBA  EB B6                           jmp 0x1403bfe72
003BFEBC  0F B7 CE                        movzx ecx, si
003BFEBF  03 CB                           add ecx, ebx
003BFEC1  EB B7                           jmp 0x1403bfe7a
003BFEC3  66 03 F3                        add si, bx
003BFEC6  0F B7 F6                        movzx esi, si
003BFEC9  3B F1                           cmp esi, ecx
003BFECB  73 33                           jae 0x1403bff00
003BFECD  48 8B 6C F7 08                  mov rbp, qword ptr [rdi + rsi*8 + 8]
003BFED2  EB A6                           jmp 0x1403bfe7a
003BFED4  44 02 F3                        add r14b, bl
003BFED7  89 6C 24 28                     mov dword ptr [rsp + 0x28], ebp
003BFEDB  44 88 74 24 21                  mov byte ptr [rsp + 0x21], r14b
003BFEE0  44 39 44 24 24                  cmp dword ptr [rsp + 0x24], r8d
003BFEE5  77 83                           ja 0x1403bfe6a
003BFEE7  48 8B 5C 24 70                  mov rbx, qword ptr [rsp + 0x70]
003BFEEC  41 8A C7                        mov al, r15b
003BFEEF  48 83 C4 30                     add rsp, 0x30
003BFEF3  41 5F                           pop r15
003BFEF5  41 5E                           pop r14
003BFEF7  41 5D                           pop r13
003BFEF9  41 5C                           pop r12
003BFEFB  5F                              pop rdi
003BFEFC  5E                              pop rsi
003BFEFD  5D                              pop rbp
003BFEFE  C3                              ret
003BFEFF  CC                              int3
003BFF00  4C 8B 67 08                     mov r12, qword ptr [rdi + 8]
003BFF04  83 CD FF                        or ebp, 0xffffffff
003BFF07  44 8A B4 24 88 00 00 00         mov r14b, byte ptr [rsp + 0x88]
003BFF0F  41 0F B7 F0                     movzx esi, r8w
003BFF13  44 88 7C 24 20                  mov byte ptr [rsp + 0x20], r15b
003BFF18  44 8B BC 24 80 00 00 00         mov r15d, dword ptr [rsp + 0x80]
003BFF20  44 8B ED                        mov r13d, ebp
003BFF23  48 85 FF                        test rdi, rdi
003BFF26  74 65                           je 0x1403bff8d
003BFF28  0F B7 0F                        movzx ecx, word ptr [rdi]
003BFF2B  4D 85 E4                        test r12, r12
003BFF2E  74 64                           je 0x1403bff94
003BFF30  49 0F BC D4                     bsf rdx, r12
003BFF34  0F B7 CE                        movzx ecx, si
003BFF37  0F B6 C2                        movzx eax, dl
003BFF3A  49 0F B3 C4                     btr r12, rax
003BFF3E  C1 E1 06                        shl ecx, 6
003BFF41  0F B6 C2                        movzx eax, dl
003BFF44  03 C8                           add ecx, eax
003BFF46  48 8B 05 6B 32 B6 00            mov rax, qword ptr [rip + 0xb6326b]
003BFF4D  8B 0C 88                        mov ecx, dword ptr [rax + rcx*4]
003BFF50  E8 7B 86 F1 FF                  call 0x1402d85d0
003BFF55  45 33 C0                        xor r8d, r8d
003BFF58  48 8B 80 50 8A 00 00            mov rax, qword ptr [rax + 0x8a50]
003BFF5F  45 84 F6                        test r14b, r14b
003BFF62  75 1C                           jne 0x1403bff80
003BFF64  42 8A 44 B8 07                  mov al, byte ptr [rax + r15*4 + 7]
003BFF69  8B 54 24 28                     mov edx, dword ptr [rsp + 0x28]
003BFF6D  0F B6 C0                        movzx eax, al
003BFF70  83 FA FF                        cmp edx, -1
003BFF73  75 12                           jne 0x1403bff87
003BFF75  44 3B E8                        cmp r13d, eax
003BFF78  8B E8                           mov ebp, eax
003BFF7A  41 0F 42 ED                     cmovb ebp, r13d
003BFF7E  EB A0                           jmp 0x1403bff20
003BFF80  42 8A 44 B8 06                  mov al, byte ptr [rax + r15*4 + 6]
003BFF85  EB E2                           jmp 0x1403bff69
003BFF87  3B C2                           cmp eax, edx
003BFF89  76 95                           jbe 0x1403bff20
003BFF8B  EB E8                           jmp 0x1403bff75
003BFF8D  0F B7 CE                        movzx ecx, si
003BFF90  03 CB                           add ecx, ebx
003BFF92  EB 97                           jmp 0x1403bff2b
003BFF94  66 03 F3                        add si, bx
003BFF97  0F B7 F6                        movzx esi, si
003BFF9A  3B F1                           cmp esi, ecx
003BFF9C  73 07                           jae 0x1403bffa5
003BFF9E  4C 8B 64 F7 08                  mov r12, qword ptr [rdi + rsi*8 + 8]
003BFFA3  EB 86                           jmp 0x1403bff2b
003BFFA5  4C 8B 67 08                     mov r12, qword ptr [rdi + 8]
003BFFA9  41 0F B7 F0                     movzx esi, r8w
003BFFAD  44 8A 7C 24 20                  mov r15b, byte ptr [rsp + 0x20]
003BFFB2  44 8A 74 24 21                  mov r14b, byte ptr [rsp + 0x21]
003BFFB7  44 8A AC 24 88 00 00 00         mov r13b, byte ptr [rsp + 0x88]
003BFFBF  48 85 FF                        test rdi, rdi
003BFFC2  74 6E                           je 0x1403c0032
003BFFC4  0F B7 0F                        movzx ecx, word ptr [rdi]
003BFFC7  4D 85 E4                        test r12, r12
003BFFCA  74 6D                           je 0x1403c0039
003BFFCC  49 0F BC D4                     bsf rdx, r12
003BFFD0  0F B7 CE                        movzx ecx, si
003BFFD3  0F B6 C2                        movzx eax, dl
003BFFD6  49 0F B3 C4                     btr r12, rax
003BFFDA  C1 E1 06                        shl ecx, 6
003BFFDD  0F B6 C2                        movzx eax, dl
003BFFE0  03 C8                           add ecx, eax
003BFFE2  48 8B 05 CF 31 B6 00            mov rax, qword ptr [rip + 0xb631cf]
003BFFE9  8B 0C 88                        mov ecx, dword ptr [rax + rcx*4]
003BFFEC  E8 DF 85 F1 FF                  call 0x1402d85d0
003BFFF1  8B 94 24 80 00 00 00            mov edx, dword ptr [rsp + 0x80]
003BFFF8  45 33 C0                        xor r8d, r8d
003BFFFB  48 8B 88 50 8A 00 00            mov rcx, qword ptr [rax + 0x8a50]
003C0002  45 84 ED                        test r13b, r13b
003C0005  74 25                           je 0x1403c002c
003C0007  8A 44 91 06                     mov al, byte ptr [rcx + rdx*4 + 6]
003C000B  0F B6 C0                        movzx eax, al
003C000E  3B C5                           cmp eax, ebp
003C0010  75 AD                           jne 0x1403bffbf
003C0012  45 84 ED                        test r13b, r13b
003C0015  75 3A                           jne 0x1403c0051
003C0017  44 38 74 91 05                  cmp byte ptr [rcx + rdx*4 + 5], r14b
003C001C  74 08                           je 0x1403c0026
003C001E  44 88 74 91 05                  mov byte ptr [rcx + rdx*4 + 5], r14b
003C0023  44 8A FB                        mov r15b, bl
003C0026  FF 4C 24 24                     dec dword ptr [rsp + 0x24]
003C002A  EB 93                           jmp 0x1403bffbf
003C002C  8A 44 91 07                     mov al, byte ptr [rcx + rdx*4 + 7]
003C0030  EB D9                           jmp 0x1403c000b
003C0032  0F B7 CE                        movzx ecx, si
003C0035  03 CB                           add ecx, ebx
003C0037  EB 8E                           jmp 0x1403bffc7
003C0039  66 03 F3                        add si, bx
003C003C  0F B7 F6                        movzx esi, si
003C003F  3B F1                           cmp esi, ecx
003C0041  0F 83 8D FE FF FF               jae 0x1403bfed4
003C0047  4C 8B 64 F7 08                  mov r12, qword ptr [rdi + rsi*8 + 8]
003C004C  E9 76 FF FF FF                  jmp 0x1403bffc7
003C0051  44 38 74 91 04                  cmp byte ptr [rcx + rdx*4 + 4], r14b
003C0056  74 CE                           je 0x1403c0026
003C0058  44 88 74 91 04                  mov byte ptr [rcx + rdx*4 + 4], r14b
003C005D  EB C4                           jmp 0x1403c0023
003C005F  48 0F BC D6                     bsf rdx, rsi
003C0063  0F B7 CF                        movzx ecx, di
003C0066  0F B6 C2                        movzx eax, dl
003C0069  48 0F B3 C6                     btr rsi, rax
003C006D  C1 E1 06                        shl ecx, 6
003C0070  0F B6 C2                        movzx eax, dl
003C0073  03 C8                           add ecx, eax
003C0075  48 8B 05 3C 31 B6 00            mov rax, qword ptr [rip + 0xb6313c]
003C007C  8B 0C 88                        mov ecx, dword ptr [rax + rcx*4]
003C007F  E8 4C 85 F1 FF                  call 0x1402d85d0
003C0084  48 8B 88 50 8A 00 00            mov rcx, qword ptr [rax + 0x8a50]
003C008B  45 84 ED                        test r13b, r13b
003C008E  0F 84 0E 7D 32 00               je 0x1406e7da2
003C0094  46 38 64 B1 04                  cmp byte ptr [rcx + r14*4 + 4], r12b
003C0099  0F 84 71 FD FF FF               je 0x1403bfe10
003C009F  44 8A FB                        mov r15b, bl
003C00A2  46 88 64 B1 04                  mov byte ptr [rcx + r14*4 + 4], r12b
003C00A7  E9 64 FD FF FF                  jmp 0x1403bfe10
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PPmHeteroHgsUpdateOrderValue(__int64 a1, __int64 a2, int a3, unsigned __int8 a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m3C;
    unsigned int v_stack_m40;
    unsigned int v_stack_m44;
    unsigned __int8 v_stack_m47;
    unsigned int v_stack_p18;
    unsigned __int8 v_stack_p20;
    unsigned __int8 v_stack_p21;
    unsigned int v_stack_p24;
    unsigned int v_stack_p28;
    unsigned __int64 v_stack_p8;
    unsigned int v_stack_p80;
    unsigned __int8 v_stack_p88;

    v_stack_p8 = v_rbx;
    v_stack_p20 = a4;
    v_stack_p18 = a3;
    v_rsp = (v_rsp) - (48);
    v_r12 = 0;
    result = KeIsEmptyAffinityEx(a1, a2, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_003BFE00;
    result = KeIsEmptyAffinityEx(a2, a2, a3, a4);
    a2 = 0;
    v_stack_m3C = (unsigned int)(result);
loc_003BFD81:
    v_stack_m40 = 0;
    if (0 == 0) goto loc_003BFDE8;
loc_003BFD8E:
    if (*(unsigned __int64 *)(a2 + 8) == 0) goto loc_003BFDEF;
    a1 = (unsigned int)((0) << (6));
    a1 = (unsigned int)((a1) + (0));
    result = KeGetPrcb((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11940872) + a1 * 4)), a2, a3, a4);
    a2 = 0;
    if (a4 == 0) goto loc_003BFDD7;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(result + 35408) + (unsigned int)(v_stack_p18) * 4 + 4)) == 0) goto loc_003BFD81;
    *(unsigned __int8 *)(*(unsigned __int64 *)(result + 35408) + (unsigned int)(v_stack_p18) * 4 + 4) = 0;
    goto loc_003BFD81;
loc_003BFDD7:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(result + 35408) + (unsigned int)(v_stack_p18) * 4 + 5)) == 0) goto loc_003BFD81;
    *(unsigned __int8 *)(*(unsigned __int64 *)(result + 35408) + (unsigned int)(v_stack_p18) * 4 + 5) = 0;
    goto loc_003BFD81;
loc_003BFDE8:
    a1 = (unsigned int)((0) + ((unsigned int)(a2 + 1)));
    goto loc_003BFD8E;
loc_003BFDEF:
    v_rsi = (unsigned __int16)((0) + ((unsigned __int16)(a2 + 1)));
    if (((unsigned int)((unsigned __int16)(v_rsi))) >= ((unsigned int)(a1))) goto loc_003BFE3B;
    goto loc_003BFD8E;
loc_003BFE00:
loc_003BFE10:
loc_003BFE17:
    if (*(unsigned __int64 *)(v_rip + 10794913) != 0) goto loc_003C005F;
    v_rdi = (unsigned __int16)(((unsigned __int16)((unsigned int)(v_stack_p18))) + (1));
    if (((unsigned int)((unsigned __int16)(v_rdi))) >= ((unsigned int)(*(unsigned __int16 *)(v_rip + 10794889)))) goto loc_003BFEE7;
    goto loc_003BFE17;
loc_003BFE3B:
    v_rbp = (unsigned int)((a2) | (0xFFFFFFFFULL));
    v_stack_m40 = (unsigned int)(v_rbp);
    result = KeCountSetBitsAffinityEx((unsigned __int16)(v_rdi), a2, a3, a4);
    a3 = 0;
    v_stack_m44 = (unsigned int)(result);
    if ((unsigned int)(result) == 0) goto loc_003BFEE7;
    v_r14 = ((unsigned int)((unsigned int)(v_stack_m3C)) == 0) ? 1 : 0;
    v_stack_m47 = (unsigned __int8)(v_r14);
loc_003BFE6A:
loc_003BFE72:
    if ((unsigned __int16)(v_rdi) == 0) goto loc_003BFEBC;
loc_003BFE7A:
    if (*(unsigned __int64 *)((unsigned __int16)(v_rdi) + 8) == 0) goto loc_003BFEC3;
    a1 = (unsigned int)((0) << (6));
    a1 = (unsigned int)((a1) + (0));
    result = KeGetPrcb((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11940636) + a1 * 4)), a2, a3, a4);
    a3 = 0;
    if ((*(unsigned __int8 *)(result + 35404)) == 0) goto loc_003BFE72;
    *(unsigned __int8 *)(result + 35404) = 0;
    goto loc_003BFE72;
loc_003BFEBC:
    a1 = (unsigned int)((0) + (1));
    goto loc_003BFE7A;
loc_003BFEC3:
    v_rsi = (unsigned __int16)((0) + (1));
    if (((unsigned int)((unsigned __int16)(v_rsi))) >= ((unsigned int)(a1))) goto loc_003BFF00;
    goto loc_003BFE7A;
loc_003BFED4:
    v_r14 = (unsigned __int8)((v_r14) + (1));
    v_stack_m40 = (unsigned int)(*(unsigned __int64 *)((unsigned __int16)(v_rdi) + (unsigned __int16)(v_rsi) * 8 + 8));
    v_stack_m47 = (unsigned __int8)(v_r14);
    if (v_stack_m44 > 0) goto loc_003BFE6A;
loc_003BFEE7:
    v_rsp = (v_rsp) + (48);
    return 1;
loc_003BFF00:
    v_rbp = (unsigned int)((*(unsigned __int64 *)((unsigned __int16)(v_rdi) + (unsigned __int16)(v_rsi) * 8 + 8)) | (0xFFFFFFFFULL));
    v_stack_p20 = 1;
loc_003BFF20:
    if ((unsigned __int16)(v_rdi) == 0) goto loc_003BFF8D;
loc_003BFF2B:
    if (*(unsigned __int64 *)((unsigned __int16)(v_rdi) + 8) == 0) goto loc_003BFF94;
    a1 = (unsigned int)((0) << (6));
    a1 = (unsigned int)((a1) + (0));
    result = KeGetPrcb((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11940459) + a1 * 4)), a2, a3, a4);
    a3 = 0;
    if ((unsigned __int8)(v_stack_p88) != 0) goto loc_003BFF80;
loc_003BFF69:
    if (((unsigned int)((unsigned int)(v_stack_p28))) != -1) goto loc_003BFF87;
loc_003BFF75:
    v_rbp = (unsigned int)((unsigned int)((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(result + 35408) + (unsigned int)(v_stack_p80) * 4 + 7))));
    if (((unsigned int)((unsigned int)((unsigned int)(v_rbp)))) < ((unsigned int)((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(result + 35408) + (unsigned int)(v_stack_p80) * 4 + 7))))) { v_rbp = (unsigned int)((unsigned int)((unsigned int)(v_rbp))); }
    goto loc_003BFF20;
loc_003BFF80:
    goto loc_003BFF69;
loc_003BFF87:
    if (((unsigned int)(*(unsigned __int8 *)((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(result + 35408) + (unsigned int)(v_stack_p80) * 4 + 7)) + (unsigned int)(v_stack_p80) * 4 + 6))) <= ((unsigned int)((unsigned int)(v_stack_p28)))) goto loc_003BFF20;
    goto loc_003BFF75;
loc_003BFF8D:
    a1 = (unsigned int)((0) + ((unsigned int)(v_stack_p8)));
    goto loc_003BFF2B;
loc_003BFF94:
    v_rsi = (unsigned __int16)((0) + ((unsigned __int16)(v_stack_p8)));
    if (((unsigned int)((unsigned __int16)(v_rsi))) >= ((unsigned int)(a1))) goto loc_003BFFA5;
    goto loc_003BFF2B;
loc_003BFFA5:
loc_003BFFBF:
    if ((unsigned __int16)(v_rdi) == 0) goto loc_003C0032;
loc_003BFFC7:
    if (*(unsigned __int64 *)((unsigned __int16)(v_rdi) + 8) == 0) goto loc_003C0039;
    a1 = (unsigned int)((0) << (6));
    a1 = (unsigned int)((a1) + ((unsigned int)((unsigned __int8)((unsigned int)(v_stack_p28)))));
    result = KeGetPrcb((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11940303) + a1 * 4)), (unsigned int)(v_stack_p28), a3, a4);
    a3 = 0;
    if ((unsigned __int8)(v_stack_p88) == 0) goto loc_003C002C;
loc_003C000B:
    if (((unsigned int)((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(result + 35408) + (unsigned int)(v_stack_p80) * 4 + 6)))) != ((unsigned int)(v_rbp))) goto loc_003BFFBF;
    if ((unsigned __int8)(v_stack_p88) != 0) goto loc_003C0051;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(result + 35408) + (unsigned int)(v_stack_p80) * 4 + 5)) == ((unsigned __int8)(v_stack_p21))) goto loc_003C0026;
    *(unsigned __int8 *)(*(unsigned __int64 *)(result + 35408) + (unsigned int)(v_stack_p80) * 4 + 5) = (unsigned __int8)(v_stack_p21);
loc_003C0023:
loc_003C0026:
    goto loc_003BFFBF;
loc_003C002C:
    goto loc_003C000B;
loc_003C0032:
    a1 = (unsigned int)((0) + ((unsigned int)(v_stack_p8)));
    goto loc_003BFFC7;
loc_003C0039:
    v_rsi = (unsigned __int16)((0) + ((unsigned __int16)(v_stack_p8)));
    if (((unsigned int)((unsigned __int16)(v_rsi))) >= ((unsigned int)(a1))) goto loc_003BFED4;
    goto loc_003BFFC7;
loc_003C0051:
    if ((*(unsigned __int8 *)(a1 + (unsigned int)(v_stack_p80) * 4 + 4)) == ((unsigned __int8)(v_stack_p21))) goto loc_003C0026;
    *(unsigned __int8 *)(a1 + (unsigned int)(v_stack_p80) * 4 + 4) = (unsigned __int8)(v_stack_p21);
    goto loc_003C0023;
loc_003C005F:
    a1 = (unsigned int)(((unsigned __int16)((unsigned __int16)(v_rdi))) << (6));
    a1 = (unsigned int)((a1) + ((unsigned int)((unsigned __int8)((unsigned int)(v_stack_p80)))));
    result = KeGetPrcb((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11940156) + a1 * 4)), (unsigned int)(v_stack_p80), a3, a4);
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(result + 35408) + v_stack_p21 * 4 + 4)) == ((unsigned __int8)(*(unsigned __int64 *)((unsigned __int16)(v_rdi) + (unsigned __int16)(v_rsi) * 8 + 8)))) goto loc_003BFE10;
    *(unsigned __int8 *)(*(unsigned __int64 *)(result + 35408) + v_stack_p21 * 4 + 4) = (unsigned __int8)(*(unsigned __int64 *)((unsigned __int16)(v_rdi) + (unsigned __int16)(v_rsi) * 8 + 8));
    goto loc_003BFE10;
}
```

## 5. (Beta) C Style

```c
int64_t PPmHeteroHgsUpdateOrderValue(int64_t Arg1, void *Arg2, int32_t Arg3, uint8_t Arg4)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m3C;
    uint32_t v_stack_m40;
    uint32_t v_stack_m44;
    uint8_t v_stack_m47;
    uint32_t v_stack_p18;
    uint8_t v_stack_p20;
    uint8_t v_stack_p21;
    uint32_t v_stack_p24;
    uint32_t v_stack_p28;
    uint64_t v_stack_p8;
    uint32_t v_stack_p80;
    uint8_t v_stack_p88;

    v_stack_p8 = local_rbx;
    v_stack_p20 = Arg4;
    v_stack_p18 = Arg3;
    local_rsp = (local_rsp) - (48);
    local_r12 = 0;
    result = KeIsEmptyAffinityEx(Arg1, Arg2, Arg3, Arg4);
    if ((uint32_t)(result) != 0) goto loc_003BFE00;
    result = KeIsEmptyAffinityEx(Arg2, Arg2, Arg3, Arg4);
    Arg2 = 0;
    v_stack_m3C = (uint32_t)(result);
loc_003BFD81:
    v_stack_m40 = 0;
    if (0 == 0) goto loc_003BFDE8;
loc_003BFD8E:
    if (*(uint64_t *)(arg2 + 0x8) == 0) goto loc_003BFDEF;
    Arg1 = (uint32_t)((0) << (6));
    Arg1 = (uint32_t)((Arg1) + (0));
    result = KeGetPrcb((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB63408) + Arg1 * 4)), Arg2, Arg3, Arg4);
    Arg2 = 0;
    if (Arg4 == 0) goto loc_003BFDD7;
    if ((*(uint8_t *)(*(uint64_t *)(result + 0x8A50) + (uint32_t)(v_stack_p18) * 4 + 0x4)) == 0) goto loc_003BFD81;
    *(uint8_t *)(*(uint64_t *)(result + 0x8A50) + (uint32_t)(v_stack_p18) * 4 + 0x4) = 0;
    goto loc_003BFD81;
loc_003BFDD7:
    if ((*(uint8_t *)(*(uint64_t *)(result + 0x8A50) + (uint32_t)(v_stack_p18) * 4 + 0x5)) == 0) goto loc_003BFD81;
    *(uint8_t *)(*(uint64_t *)(result + 0x8A50) + (uint32_t)(v_stack_p18) * 4 + 0x5) = 0;
    goto loc_003BFD81;
loc_003BFDE8:
    Arg1 = (uint32_t)((0) + ((uint32_t)(Arg2 + 1)));
    goto loc_003BFD8E;
loc_003BFDEF:
    local_rsi = (uint16_t)((0) + ((uint16_t)(Arg2 + 1)));
    if (((uint32_t)((uint16_t)(local_rsi))) >= ((uint32_t)(Arg1))) goto loc_003BFE3B;
    goto loc_003BFD8E;
loc_003BFE00:
loc_003BFE10:
loc_003BFE17:
    if (*(uint64_t *)(v_rip + 0xA4B7A1) != 0) goto loc_003C005F;
    local_rdi = (uint16_t)(((uint16_t)((uint32_t)(v_stack_p18))) + (1));
    if (((uint32_t)((uint16_t)(local_rdi))) >= ((uint32_t)(*(uint16_t *)(v_rip + 0xA4B789)))) goto loc_003BFEE7;
    goto loc_003BFE17;
loc_003BFE3B:
    local_rbp = (uint32_t)((Arg2) | (0xFFFFFFFFULL));
    v_stack_m40 = (uint32_t)(local_rbp);
    result = KeCountSetBitsAffinityEx((uint16_t)(local_rdi), Arg2, Arg3, Arg4);
    Arg3 = 0;
    v_stack_m44 = (uint32_t)(result);
    if ((uint32_t)(result) == 0) goto loc_003BFEE7;
    local_r14 = ((uint32_t)((uint32_t)(v_stack_m3C)) == 0) ? 1 : 0;
    v_stack_m47 = (uint8_t)(local_r14);
loc_003BFE6A:
loc_003BFE72:
    if ((uint16_t)(local_rdi) == 0) goto loc_003BFEBC;
loc_003BFE7A:
    if (*(uint64_t *)((uint16_t)(local_rdi) + 0x8) == 0) goto loc_003BFEC3;
    Arg1 = (uint32_t)((0) << (6));
    Arg1 = (uint32_t)((Arg1) + (0));
    result = KeGetPrcb((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB6331C) + Arg1 * 4)), Arg2, Arg3, Arg4);
    Arg3 = 0;
    if ((*(uint8_t *)(result + 0x8A4C)) == 0) goto loc_003BFE72;
    *(uint8_t *)(result + 0x8A4C) = 0;
    goto loc_003BFE72;
loc_003BFEBC:
    Arg1 = (uint32_t)((0) + (1));
    goto loc_003BFE7A;
loc_003BFEC3:
    local_rsi = (uint16_t)((0) + (1));
    if (((uint32_t)((uint16_t)(local_rsi))) >= ((uint32_t)(Arg1))) goto loc_003BFF00;
    goto loc_003BFE7A;
loc_003BFED4:
    local_r14 = (uint8_t)((local_r14) + (1));
    v_stack_m40 = (uint32_t)(*(uint64_t *)((uint16_t)(local_rdi) + (uint16_t)(local_rsi) * 8 + 0x8));
    v_stack_m47 = (uint8_t)(local_r14);
    if (v_stack_m44 > 0) goto loc_003BFE6A;
loc_003BFEE7:
    local_rsp = (local_rsp) + (48);
    return 1;
loc_003BFF00:
    local_rbp = (uint32_t)((*(uint64_t *)((uint16_t)(local_rdi) + (uint16_t)(local_rsi) * 8 + 0x8)) | (0xFFFFFFFFULL));
    v_stack_p20 = 1;
loc_003BFF20:
    if ((uint16_t)(local_rdi) == 0) goto loc_003BFF8D;
loc_003BFF2B:
    if (*(uint64_t *)((uint16_t)(local_rdi) + 0x8) == 0) goto loc_003BFF94;
    Arg1 = (uint32_t)((0) << (6));
    Arg1 = (uint32_t)((Arg1) + (0));
    result = KeGetPrcb((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB6326B) + Arg1 * 4)), Arg2, Arg3, Arg4);
    Arg3 = 0;
    if ((uint8_t)(v_stack_p88) != 0) goto loc_003BFF80;
loc_003BFF69:
    if (((uint32_t)((uint32_t)(v_stack_p28))) != -1) goto loc_003BFF87;
loc_003BFF75:
    local_rbp = (uint32_t)((uint32_t)((uint8_t)(*(uint8_t *)(*(uint64_t *)(result + 0x8A50) + (uint32_t)(v_stack_p80) * 4 + 0x7))));
    if (((uint32_t)((uint32_t)((uint32_t)(local_rbp)))) < ((uint32_t)((uint8_t)(*(uint8_t *)(*(uint64_t *)(result + 0x8A50) + (uint32_t)(v_stack_p80) * 4 + 0x7))))) { local_rbp = (uint32_t)((uint32_t)((uint32_t)(local_rbp))); }
    goto loc_003BFF20;
loc_003BFF80:
    goto loc_003BFF69;
loc_003BFF87:
    if (((uint32_t)(*(uint8_t *)((uint8_t)(*(uint8_t *)(*(uint64_t *)(result + 0x8A50) + (uint32_t)(v_stack_p80) * 4 + 0x7)) + (uint32_t)(v_stack_p80) * 4 + 0x6))) <= ((uint32_t)((uint32_t)(v_stack_p28)))) goto loc_003BFF20;
    goto loc_003BFF75;
loc_003BFF8D:
    Arg1 = (uint32_t)((0) + ((uint32_t)(v_stack_p8)));
    goto loc_003BFF2B;
loc_003BFF94:
    local_rsi = (uint16_t)((0) + ((uint16_t)(v_stack_p8)));
    if (((uint32_t)((uint16_t)(local_rsi))) >= ((uint32_t)(Arg1))) goto loc_003BFFA5;
    goto loc_003BFF2B;
loc_003BFFA5:
loc_003BFFBF:
    if ((uint16_t)(local_rdi) == 0) goto loc_003C0032;
loc_003BFFC7:
    if (*(uint64_t *)((uint16_t)(local_rdi) + 0x8) == 0) goto loc_003C0039;
    Arg1 = (uint32_t)((0) << (6));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)((uint8_t)((uint32_t)(v_stack_p28)))));
    result = KeGetPrcb((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB631CF) + Arg1 * 4)), (uint32_t)(v_stack_p28), Arg3, Arg4);
    Arg3 = 0;
    if ((uint8_t)(v_stack_p88) == 0) goto loc_003C002C;
loc_003C000B:
    if (((uint32_t)((uint8_t)(*(uint8_t *)(*(uint64_t *)(result + 0x8A50) + (uint32_t)(v_stack_p80) * 4 + 0x6)))) != ((uint32_t)(local_rbp))) goto loc_003BFFBF;
    if ((uint8_t)(v_stack_p88) != 0) goto loc_003C0051;
    if ((*(uint8_t *)(*(uint64_t *)(result + 0x8A50) + (uint32_t)(v_stack_p80) * 4 + 0x5)) == ((uint8_t)(v_stack_p21))) goto loc_003C0026;
    *(uint8_t *)(*(uint64_t *)(result + 0x8A50) + (uint32_t)(v_stack_p80) * 4 + 0x5) = (uint8_t)(v_stack_p21);
loc_003C0023:
loc_003C0026:
    goto loc_003BFFBF;
loc_003C002C:
    goto loc_003C000B;
loc_003C0032:
    Arg1 = (uint32_t)((0) + ((uint32_t)(v_stack_p8)));
    goto loc_003BFFC7;
loc_003C0039:
    local_rsi = (uint16_t)((0) + ((uint16_t)(v_stack_p8)));
    if (((uint32_t)((uint16_t)(local_rsi))) >= ((uint32_t)(Arg1))) goto loc_003BFED4;
    goto loc_003BFFC7;
loc_003C0051:
    if ((*(uint8_t *)(Arg1 + (uint32_t)(v_stack_p80) * 4 + 0x4)) == ((uint8_t)(v_stack_p21))) goto loc_003C0026;
    *(uint8_t *)(Arg1 + (uint32_t)(v_stack_p80) * 4 + 0x4) = (uint8_t)(v_stack_p21);
    goto loc_003C0023;
loc_003C005F:
    Arg1 = (uint32_t)(((uint16_t)((uint16_t)(local_rdi))) << (6));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)((uint8_t)((uint32_t)(v_stack_p80)))));
    result = KeGetPrcb((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB6313C) + Arg1 * 4)), (uint32_t)(v_stack_p80), Arg3, Arg4);
    if ((*(uint8_t *)(*(uint64_t *)(result + 0x8A50) + v_stack_p21 * 4 + 0x4)) == ((uint8_t)(*(uint64_t *)((uint16_t)(local_rdi) + (uint16_t)(local_rsi) * 8 + 0x8)))) goto loc_003BFE10;
    *(uint8_t *)(*(uint64_t *)(result + 0x8A50) + v_stack_p21 * 4 + 0x4) = (uint8_t)(*(uint64_t *)((uint16_t)(local_rdi) + (uint16_t)(local_rsi) * 8 + 0x8));
    goto loc_003BFE10;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003BFD24&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
