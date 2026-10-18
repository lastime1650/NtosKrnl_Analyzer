# KiOpDecode

- RVA: `0x003D81F0`–`0x003D85B2` (길이 `962` bytes)
- VA: `0x00000001403D81F0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00093CA4`
- 디코드: `253`개 명령, `962/962` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **6**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x003D82A9` → [KiOpFetchNextByte](KiOpFetchNextByte_function_003D87C0.md) (function, `0x003D87C0`)
- `0x003D8403` → [KiOpDecodeModRM](KiOpDecodeModRM_function_003D868C.md) (function, `0x003D868C`)
- `0x003D848B` → [KiOpFetchNextByte](KiOpFetchNextByte_function_003D87C0.md) (function, `0x003D87C0`)
- `0x003D84B6` → [KiOpFetchNextByte](KiOpFetchNextByte_function_003D87C0.md) (function, `0x003D87C0`)
- `0x003D8548` → [KiOpFetchNextByte](KiOpFetchNextByte_function_003D87C0.md) (function, `0x003D87C0`)
- `0x003D859A` → [KiOpFetchBytes](KiOpFetchBytes_function_003D8778.md) (function, `0x003D8778`)

### Direct callers
- [KiPreprocessFault](KiPreprocessFault_function_003D7E70.md) at `0x003D7F33`

### Static image references
- `0x003D829A` → RVA `0x00013CA0` (`.rdata`; read)
- `0x003D8351` → RVA `0x00002998` (`.rdata`; read)
- `0x003D8358` → RVA `0x00002738` (`.rdata`; read)
- `0x003D8365` → RVA `0x00002740` (`.rdata`; read)
- `0x003D836C` → RVA `0x000025A0` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x003D8504` → [sub_006E9980](../6E/Unknown_function_006E9980.md) (`tail-transfer`)
  - `0x003D851A` → [sub_006E9980](../6E/Unknown_function_006E9980.md) (`tail-transfer`)
  - `0x003D858A` → [sub_006E9980 + 0xD](../6E/Unknown_function_006E9980.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003D81F0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
003D81F5  56                              push rsi
003D81F6  57                              push rdi
003D81F7  41 54                           push r12
003D81F9  41 56                           push r14
003D81FB  41 57                           push r15
003D81FD  48 83 EC 20                     sub rsp, 0x20
003D8201  45 8B F1                        mov r14d, r9d
003D8204  4C 8B D1                        mov r10, rcx
003D8207  48 8B 7C 24 70                  mov rdi, qword ptr [rsp + 0x70]
003D820C  C6 44 24 68 00                  mov byte ptr [rsp + 0x68], 0
003D8211  32 DB                           xor bl, bl
003D8213  45 33 E4                        xor r12d, r12d
003D8216  44 89 64 24 58                  mov dword ptr [rsp + 0x58], r12d
003D821B  88 5C 24 60                     mov byte ptr [rsp + 0x60], bl
003D821F  66 44 89 64 24 70               mov word ptr [rsp + 0x70], r12w
003D8225  0F 57 C0                        xorps xmm0, xmm0
003D8228  0F 11 07                        movups xmmword ptr [rdi], xmm0
003D822B  0F 11 47 10                     movups xmmword ptr [rdi + 0x10], xmm0
003D822F  0F 11 47 20                     movups xmmword ptr [rdi + 0x20], xmm0
003D8233  0F 11 47 30                     movups xmmword ptr [rdi + 0x30], xmm0
003D8237  0F 11 47 40                     movups xmmword ptr [rdi + 0x40], xmm0
003D823B  0F 11 47 50                     movups xmmword ptr [rdi + 0x50], xmm0
003D823F  0F 11 47 60                     movups xmmword ptr [rdi + 0x60], xmm0
003D8243  44 89 4F 3C                     mov dword ptr [rdi + 0x3c], r9d
003D8247  48 8B 8A F8 00 00 00            mov rcx, qword ptr [rdx + 0xf8]
003D824E  48 89 0F                        mov qword ptr [rdi], rcx
003D8251  48 89 4F 10                     mov qword ptr [rdi + 0x10], rcx
003D8255  48 8D 41 10                     lea rax, [rcx + 0x10]
003D8259  48 89 47 08                     mov qword ptr [rdi + 8], rax
003D825D  41 80 F8 01                     cmp r8b, 1
003D8261  75 1C                           jne 0x1403d827f
003D8263  48 B8 00 00 FF FF FF 7F 00 00   movabs rax, 0x7fffffff0000
003D826D  48 3B C8                        cmp rcx, rax
003D8270  48 0F 43 C8                     cmovae rcx, rax
003D8274  90                              nop
003D8275  0F B6 01                        movzx eax, byte ptr [rcx]
003D8278  EB 05                           jmp 0x1403d827f
003D827A  E9 67 01 00 00                  jmp 0x1403d83e6
003D827F  4C 89 57 20                     mov qword ptr [rdi + 0x20], r10
003D8283  48 89 57 18                     mov qword ptr [rdi + 0x18], rdx
003D8287  44 88 47 51                     mov byte ptr [rdi + 0x51], r8b
003D828B  C6 47 61 00                     mov byte ptr [rdi + 0x61], 0
003D828F  66 83 7A 38 23                  cmp word ptr [rdx + 0x38], 0x23
003D8294  75 04                           jne 0x1403d829a
003D8296  C6 47 3A 01                     mov byte ptr [rdi + 0x3a], 1
003D829A  4C 8D 3D FF B9 C3 FF            lea r15, [rip - 0x3c4601]
003D82A1  48 8D 54 24 60                  lea rdx, [rsp + 0x60]
003D82A6  48 8B CF                        mov rcx, rdi
003D82A9  E8 12 05 00 00                  call 0x1403d87c0
003D82AE  85 C0                           test eax, eax
003D82B0  0F 88 30 01 00 00               js 0x1403d83e6
003D82B6  45 8B CC                        mov r9d, r12d
003D82B9  45 32 DB                        xor r11b, r11b
003D82BC  45 8B D4                        mov r10d, r12d
003D82BF  41 8B F4                        mov esi, r12d
003D82C2  44 0F B6 44 24 60               movzx r8d, byte ptr [rsp + 0x60]
003D82C8  40 38 77 3A                     cmp byte ptr [rdi + 0x3a], sil
003D82CC  75 0A                           jne 0x1403d82d8
003D82CE  41 0F B6 C0                     movzx eax, r8b
003D82D2  24 F0                           and al, 0xf0
003D82D4  3C 40                           cmp al, 0x40
003D82D6  74 29                           je 0x1403d8301
003D82D8  41 8B D4                        mov edx, r12d
003D82DB  0F 1F 44 00 00                  nop dword ptr [rax + rax]
003D82E0  83 FA 0B                        cmp edx, 0xb
003D82E3  73 26                           jae 0x1403d830b
003D82E5  8B C2                           mov eax, edx
003D82E7  48 8D 0C 40                     lea rcx, [rax + rax*2]
003D82EB  48 8D 0C 8D 00 00 00 00         lea rcx, [rcx*4]
003D82F3  46 38 04 39                     cmp byte ptr [rcx + r15], r8b
003D82F7  0F 84 73 01 00 00               je 0x1403d8470
003D82FD  FF C2                           inc edx
003D82FF  EB DF                           jmp 0x1403d82e0
003D8301  41 BA 00 08 00 00               mov r10d, 0x800
003D8307  44 88 47 40                     mov byte ptr [rdi + 0x40], r8b
003D830B  45 85 D2                        test r10d, r10d
003D830E  0F 85 29 01 00 00               jne 0x1403d843d
003D8314  41 0F B6 DB                     movzx ebx, r11b
003D8318  45 85 C9                        test r9d, r9d
003D831B  0F 88 09 01 00 00               js 0x1403d842a
003D8321  84 DB                           test bl, bl
003D8323  0F 85 78 FF FF FF               jne 0x1403d82a1
003D8329  41 80 F8 0F                     cmp r8b, 0xf
003D832D  0F 84 4C 01 00 00               je 0x1403d847f
003D8333  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
003D8337  48 FF C8                        dec rax
003D833A  48 89 47 28                     mov qword ptr [rdi + 0x28], rax
003D833E  44 88 47 38                     mov byte ptr [rdi + 0x38], r8b
003D8342  41 0F BA E6 1B                  bt r14d, 0x1b
003D8347  0F 82 1A 01 00 00               jb 0x1403d8467
003D834D  0F B6 47 39                     movzx eax, byte ptr [rdi + 0x39]
003D8351  48 8D 0D 40 A6 C2 FF            lea rcx, [rip - 0x3d59c0]
003D8358  48 8D 35 D9 A3 C2 FF            lea rsi, [rip - 0x3d5c27]
003D835F  84 C0                           test al, al
003D8361  48 0F 45 F1                     cmovne rsi, rcx
003D8365  48 8D 0D D4 A3 C2 FF            lea rcx, [rip - 0x3d5c2c]
003D836C  48 8D 1D 2D A2 C2 FF            lea rbx, [rip - 0x3d5dd3]
003D8373  48 0F 45 D9                     cmovne rbx, rcx
003D8377  48 83 EB 18                     sub rbx, 0x18
003D837B  0F 1F 44 00 00                  nop dword ptr [rax + rax]
003D8380  48 83 C3 18                     add rbx, 0x18
003D8384  48 3B DE                        cmp rbx, rsi
003D8387  74 4F                           je 0x1403d83d8
003D8389  0F B6 03                        movzx eax, byte ptr [rbx]
003D838C  0F B6 4F 38                     movzx ecx, byte ptr [rdi + 0x38]
003D8390  3A C8                           cmp cl, al
003D8392  72 EC                           jb 0x1403d8380
003D8394  FE C8                           dec al
003D8396  02 43 01                        add al, byte ptr [rbx + 1]
003D8399  3A C8                           cmp cl, al
003D839B  77 E3                           ja 0x1403d8380
003D839D  8B 4B 04                        mov ecx, dword ptr [rbx + 4]
003D83A0  85 C9                           test ecx, ecx
003D83A2  0F 85 87 00 00 00               jne 0x1403d842f
003D83A8  80 7B 08 FF                     cmp byte ptr [rbx + 8], 0xff
003D83AC  0F 85 F4 00 00 00               jne 0x1403d84a6
003D83B2  80 7B 09 FF                     cmp byte ptr [rbx + 9], 0xff
003D83B6  0F 85 EA 00 00 00               jne 0x1403d84a6
003D83BC  80 7B 0A FF                     cmp byte ptr [rbx + 0xa], 0xff
003D83C0  0F 85 E0 00 00 00               jne 0x1403d84a6
003D83C6  8B 43 0C                        mov eax, dword ptr [rbx + 0xc]
003D83C9  25 00 00 00 F4                  and eax, 0xf4000000
003D83CE  0F 85 4B 01 00 00               jne 0x1403d851f
003D83D4  48 89 5F 58                     mov qword ptr [rdi + 0x58], rbx
003D83D8  45 8B CC                        mov r9d, r12d
003D83DB  48 8B 5F 58                     mov rbx, qword ptr [rdi + 0x58]
003D83DF  48 85 DB                        test rbx, rbx
003D83E2  75 15                           jne 0x1403d83f9
003D83E4  33 C0                           xor eax, eax
003D83E6  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
003D83EB  48 83 C4 20                     add rsp, 0x20
003D83EF  41 5F                           pop r15
003D83F1  41 5E                           pop r14
003D83F3  41 5C                           pop r12
003D83F5  5F                              pop rdi
003D83F6  5E                              pop rsi
003D83F7  C3                              ret
003D83F8  CC                              int3
003D83F9  8B 43 0C                        mov eax, dword ptr [rbx + 0xc]
003D83FC  A8 04                           test al, 4
003D83FE  74 0F                           je 0x1403d840f
003D8400  48 8B CF                        mov rcx, rdi
003D8403  E8 84 02 00 00                  call 0x1403d868c
003D8408  44 8B C8                        mov r9d, eax
003D840B  85 C0                           test eax, eax
003D840D  78 D7                           js 0x1403d83e6
003D840F  8B 43 0C                        mov eax, dword ptr [rbx + 0xc]
003D8412  A8 01                           test al, 1
003D8414  0F 85 1E 01 00 00               jne 0x1403d8538
003D841A  48 8B 47 58                     mov rax, qword ptr [rdi + 0x58]
003D841E  8B 48 0C                        mov ecx, dword ptr [rax + 0xc]
003D8421  F6 C1 02                        test cl, 2
003D8424  0F 85 58 01 00 00               jne 0x1403d8582
003D842A  41 8B C1                        mov eax, r9d
003D842D  EB B7                           jmp 0x1403d83e6
003D842F  85 4F 30                        test dword ptr [rdi + 0x30], ecx
003D8432  0F 84 48 FF FF FF               je 0x1403d8380
003D8438  E9 6B FF FF FF                  jmp 0x1403d83a8
003D843D  8B 47 30                        mov eax, dword ptr [rdi + 0x30]
003D8440  41 85 C2                        test r10d, eax
003D8443  0F 85 E4 00 00 00               jne 0x1403d852d
003D8449  8B 4F 34                        mov ecx, dword ptr [rdi + 0x34]
003D844C  85 CE                           test esi, ecx
003D844E  0F 85 D9 00 00 00               jne 0x1403d852d
003D8454  41 0B C2                        or eax, r10d
003D8457  89 47 30                        mov dword ptr [rdi + 0x30], eax
003D845A  0B CE                           or ecx, esi
003D845C  89 4F 34                        mov dword ptr [rdi + 0x34], ecx
003D845F  41 B3 01                        mov r11b, 1
003D8462  E9 AD FE FF FF                  jmp 0x1403d8314
003D8467  4C 89 67 58                     mov qword ptr [rdi + 0x58], r12
003D846B  E9 6B FF FF FF                  jmp 0x1403d83db
003D8470  46 8B 54 39 04                  mov r10d, dword ptr [rcx + r15 + 4]
003D8475  42 8B 74 39 08                  mov esi, dword ptr [rcx + r15 + 8]
003D847A  E9 8C FE FF FF                  jmp 0x1403d830b
003D847F  C6 47 39 01                     mov byte ptr [rdi + 0x39], 1
003D8483  48 8D 54 24 60                  lea rdx, [rsp + 0x60]
003D8488  48 8B CF                        mov rcx, rdi
003D848B  E8 30 03 00 00                  call 0x1403d87c0
003D8490  44 8B C8                        mov r9d, eax
003D8493  85 C0                           test eax, eax
003D8495  0F 88 4B FF FF FF               js 0x1403d83e6
003D849B  44 0F B6 44 24 60               movzx r8d, byte ptr [rsp + 0x60]
003D84A1  E9 8D FE FF FF                  jmp 0x1403d8333
003D84A6  4C 8D 77 41                     lea r14, [rdi + 0x41]
003D84AA  80 7F 50 00                     cmp byte ptr [rdi + 0x50], 0
003D84AE  75 17                           jne 0x1403d84c7
003D84B0  49 8B D6                        mov rdx, r14
003D84B3  48 8B CF                        mov rcx, rdi
003D84B6  E8 05 03 00 00                  call 0x1403d87c0
003D84BB  85 C0                           test eax, eax
003D84BD  0F 88 23 FF FF FF               js 0x1403d83e6
003D84C3  C6 47 50 01                     mov byte ptr [rdi + 0x50], 1
003D84C7  0F B6 4B 08                     movzx ecx, byte ptr [rbx + 8]
003D84CB  80 F9 FF                        cmp cl, 0xff
003D84CE  74 11                           je 0x1403d84e1
003D84D0  41 0F B6 06                     movzx eax, byte ptr [r14]
003D84D4  C0 E8 03                        shr al, 3
003D84D7  24 07                           and al, 7
003D84D9  3A C8                           cmp cl, al
003D84DB  0F 85 9F FE FF FF               jne 0x1403d8380
003D84E1  0F B6 4B 0A                     movzx ecx, byte ptr [rbx + 0xa]
003D84E5  80 F9 FF                        cmp cl, 0xff
003D84E8  0F 85 81 00 00 00               jne 0x1403d856f
003D84EE  0F B6 43 09                     movzx eax, byte ptr [rbx + 9]
003D84F2  3C FF                           cmp al, 0xff
003D84F4  0F 84 CC FE FF FF               je 0x1403d83c6
003D84FA  41 0F B6 0E                     movzx ecx, byte ptr [r14]
003D84FE  C0 E9 06                        shr cl, 6
003D8501  80 F9 03                        cmp cl, 3
003D8504  0F 85 76 14 31 00               jne 0x1406e9980
003D850A  3A C1                           cmp al, cl
003D850C  0F 85 6E FE FF FF               jne 0x1403d8380
003D8512  3A C9                           cmp cl, cl
003D8514  0F 84 AC FE FF FF               je 0x1403d83c6
003D851A  E9 61 14 31 00                  jmp 0x1406e9980
003D851F  85 47 3C                        test dword ptr [rdi + 0x3c], eax
003D8522  0F 85 AC FE FF FF               jne 0x1403d83d4
003D8528  E9 53 FE FF FF                  jmp 0x1403d8380
003D852D  41 B9 1D 00 00 C0               mov r9d, 0xc000001d
003D8533  E9 E0 FD FF FF                  jmp 0x1403d8318
003D8538  BE 01 00 00 00                  mov esi, 1
003D853D  48 8D 5C 24 68                  lea rbx, [rsp + 0x68]
003D8542  48 8B D3                        mov rdx, rbx
003D8545  48 8B CF                        mov rcx, rdi
003D8548  E8 73 02 00 00                  call 0x1403d87c0
003D854D  85 C0                           test eax, eax
003D854F  0F 88 91 FE FF FF               js 0x1403d83e6
003D8555  48 FF C3                        inc rbx
003D8558  83 C6 FF                        add esi, -1
003D855B  75 E5                           jne 0x1403d8542
003D855D  45 8B CC                        mov r9d, r12d
003D8560  48 0F BE 44 24 68               movsx rax, byte ptr [rsp + 0x68]
003D8566  48 89 47 48                     mov qword ptr [rdi + 0x48], rax
003D856A  E9 BB FE FF FF                  jmp 0x1403d842a
003D856F  41 0F B6 06                     movzx eax, byte ptr [r14]
003D8573  24 07                           and al, 7
003D8575  3A C8                           cmp cl, al
003D8577  0F 85 03 FE FF FF               jne 0x1403d8380
003D857D  E9 6C FF FF FF                  jmp 0x1403d84ee
003D8582  8B 47 30                        mov eax, dword ptr [rdi + 0x30]
003D8585  48 8B CF                        mov rcx, rdi
003D8588  A8 40                           test al, 0x40
003D858A  0F 84 FD 13 31 00               je 0x1406e998d
003D8590  4C 8D 44 24 70                  lea r8, [rsp + 0x70]
003D8595  BA 02 00 00 00                  mov edx, 2
003D859A  E8 D9 01 00 00                  call 0x1403d8778
003D859F  44 8B C8                        mov r9d, eax
003D85A2  85 C0                           test eax, eax
003D85A4  0F 88 3C FE FF FF               js 0x1403d83e6
003D85AA  48 0F BF 44 24 70               movsx rax, word ptr [rsp + 0x70]
003D85B0  EB B4                           jmp 0x1403d8566
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiOpDecode(__int64 a1, __int64 a2, unsigned __int8 a3, int a4, unsigned __int16 a5)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_p10;
    unsigned __int8 v_stack_p18;
    unsigned __int8 v_stack_p20;
    unsigned __int16 v_stack_p28;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    v_stack_p20 = 0;
    v_rbx = 0;
    v_r12 = 0;
    v_stack_p10 = 0;
    v_stack_p18 = 0;
    v_stack_p28 = 0;
    *(unsigned __int64 *)(a5) = v_xmm0;
    *(unsigned __int64 *)(a5 + 16) = v_xmm0;
    *(unsigned __int64 *)(a5 + 32) = v_xmm0;
    *(unsigned __int64 *)(a5 + 48) = v_xmm0;
    *(unsigned __int64 *)(a5 + 64) = v_xmm0;
    *(unsigned __int64 *)(a5 + 80) = v_xmm0;
    *(unsigned __int64 *)(a5 + 96) = v_xmm0;
    *(unsigned int *)(a5 + 60) = a4;
    *(unsigned __int64 *)(a5) = *(unsigned __int64 *)(a2 + 248);
    *(unsigned __int64 *)(a5 + 16) = *(unsigned __int64 *)(a2 + 248);
    *(unsigned __int64 *)(a5 + 8) = *(unsigned __int64 *)(a2 + 248) + 16;
    if (a3 != 1) goto loc_003D827F;
    a1 = *(unsigned __int64 *)(a2 + 248);
    if ((*(unsigned __int64 *)(a2 + 248)) >= (*(unsigned __int64 *)(a2 + 248) + 16)) { a1 = *(unsigned __int64 *)(a2 + 248) + 16; }
    goto loc_003D827F;
loc_003D827F:
    *(unsigned __int64 *)(a5 + 32) = a1;
    *(unsigned __int64 *)(a5 + 24) = a2;
    *(unsigned __int8 *)(a5 + 81) = a3;
    *(unsigned __int8 *)(a5 + 97) = 0;
    if ((*(unsigned __int16 *)(a2 + 56)) == 35) {
        *(unsigned __int8 *)(a5 + 58) = 1;
    }
loc_003D82A1:
    result = KiOpFetchNextByte(a5, v_stack_p18, a3, a4);
    if (sign_flag) goto loc_003D83E6;
    v_r11 = 0;
    if ((*(unsigned __int8 *)(a5 + 58)) != 0) goto loc_003D82D8;
    result = (unsigned __int8)(((unsigned __int8)(v_stack_p18)) & (240));
    if (((unsigned __int8)(result)) == 64) goto loc_003D8301;
loc_003D82D8:
loc_003D82E0:
    if (0 >= 11) goto loc_003D830B;
    if ((*(unsigned __int8 *)(0 + 0 * 2 * 4 + v_rip - 3950081 * 1)) == ((unsigned __int8)(v_stack_p18))) goto loc_003D8470;
    a2 = (unsigned int)((0) + 1);
    goto loc_003D82E0;
loc_003D8301:
    *(unsigned __int8 *)(a5 + 64) = (unsigned __int8)(v_stack_p18);
loc_003D830B:
    if ((unsigned int)((unsigned int)(0x800ULL)) != 0) goto loc_003D843D;
loc_003D8314:
loc_003D8318:
    if (sign_flag) goto loc_003D842A;
    if (0 != 0) goto loc_003D82A1;
    if (((unsigned __int8)(v_stack_p18)) == 15) goto loc_003D847F;
loc_003D8333:
    result = (*(unsigned __int64 *)(a5 + 16)) - 1;
    *(unsigned __int64 *)(a5 + 40) = result;
    *(unsigned __int8 *)(a5 + 56) = (unsigned __int8)(v_stack_p18);
    if (((unsigned __int8)(v_stack_p18)) < 15) goto loc_003D8467;
    v_rsi = v_rip - 4021287;
    if ((unsigned __int8)(*(unsigned __int8 *)(a5 + 57)) != 0) { v_rsi = v_rip - 4020672; }
    v_rbx = v_rip - 4021715;
    if ((unsigned __int8)(*(unsigned __int8 *)(a5 + 57)) != 0) { v_rbx = v_rip - 4021292; }
    v_rbx = (v_rbx) - (24);
loc_003D8380:
    v_rbx = (v_rbx) + (24);
    if (v_rbx == v_rsi) goto loc_003D83D8;
    if (((unsigned __int8)(*(unsigned __int8 *)(a5 + 56))) < ((unsigned __int8)(*(unsigned __int8 *)(v_rbx)))) goto loc_003D8380;
    result = (unsigned __int8)((*(unsigned __int8 *)(v_rbx)) - 1);
    result = (unsigned __int8)((result) + (*(unsigned __int8 *)(v_rbx + 1)));
    if (((unsigned __int8)(*(unsigned __int8 *)(a5 + 56))) > ((unsigned __int8)(result))) goto loc_003D8380;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 4))) != 0) goto loc_003D842F;
loc_003D83A8:
    if ((*(unsigned __int8 *)(v_rbx + 8)) != 255) goto loc_003D84A6;
    if ((*(unsigned __int8 *)(v_rbx + 9)) != 255) goto loc_003D84A6;
    if ((*(unsigned __int8 *)(v_rbx + 10)) != 255) goto loc_003D84A6;
loc_003D83C6:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbx + 12))) & (0xF4000000ULL));
    if (condition_is_not_equal) goto loc_003D851F;
loc_003D83D4:
    *(unsigned __int64 *)(a5 + 88) = v_rbx;
loc_003D83D8:
loc_003D83DB:
    if (*(unsigned __int64 *)(a5 + 88) != 0) goto loc_003D83F9;
    result = 0;
loc_003D83E6:
    v_rsp = (v_rsp) + (32);
    return result;
loc_003D83F9:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p8 + 12)))) & (4)) == 0) goto loc_003D840F;
    result = KiOpDecodeModRM(a5, a2, v_stack_p18, 0);
    if (sign_flag) goto loc_003D83E6;
loc_003D840F:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p8 + 12)))) & (1)) != 0) goto loc_003D8538;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a5 + 88) + 12)))) & (2)) != 0) goto loc_003D8582;
loc_003D842A:
    goto loc_003D83E6;
loc_003D842F:
    if (((*(unsigned int *)(a5 + 48)) & ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a5 + 88) + 12))))) == 0) goto loc_003D8380;
    goto loc_003D83A8;
loc_003D843D:
    if ((((unsigned int)((unsigned int)(0x800ULL))) & ((unsigned int)((unsigned int)(*(unsigned int *)(a5 + 48))))) != 0) goto loc_003D852D;
    if ((((unsigned int)(v_rsi)) & ((unsigned int)((unsigned int)(*(unsigned int *)(a5 + 52))))) != 0) goto loc_003D852D;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a5 + 48))) | ((unsigned int)((unsigned int)(0x800ULL))));
    *(unsigned int *)(a5 + 48) = (unsigned int)(result);
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a5 + 52))) | ((unsigned int)(v_rsi)));
    *(unsigned int *)(a5 + 52) = (unsigned int)(a1);
    goto loc_003D8314;
loc_003D8467:
    *(unsigned __int64 *)(a5 + 88) = 0;
    goto loc_003D83DB;
loc_003D8470:
    goto loc_003D830B;
loc_003D847F:
    *(unsigned __int8 *)(a5 + 57) = 1;
    result = KiOpFetchNextByte(a5, v_stack_p60, v_stack_p18, (unsigned int)((unsigned int)(result)));
    if (sign_flag) goto loc_003D83E6;
    goto loc_003D8333;
loc_003D84A6:
    if ((*(unsigned __int8 *)(a5 + 80)) != 0) goto loc_003D84C7;
    result = KiOpFetchNextByte(a5, a5 + 65, v_stack_p60, (unsigned int)((unsigned int)(result)));
    if (sign_flag) goto loc_003D83E6;
    *(unsigned __int8 *)(a5 + 80) = 1;
loc_003D84C7:
    if (((unsigned __int8)(*(unsigned __int8 *)(v_stack_p8 + 8))) == 255) goto loc_003D84E1;
    result = (unsigned __int8)((*(unsigned __int8 *)(a5 + 65)) >> (3));
    result = (unsigned __int8)((result) & (7));
    if (((unsigned __int8)(*(unsigned __int8 *)(v_stack_p8 + 8))) != ((unsigned __int8)(result))) goto loc_003D8380;
loc_003D84E1:
    if (((unsigned __int8)(*(unsigned __int8 *)(v_stack_p8 + 10))) != 255) goto loc_003D856F;
loc_003D84EE:
    if (((unsigned __int8)(*(unsigned __int8 *)(v_stack_p8 + 9))) == 255) goto loc_003D83C6;
    a1 = (unsigned __int8)((*(unsigned __int8 *)(a5 + 65)) >> (6));
    if (((unsigned __int8)(*(unsigned __int8 *)(v_stack_p8 + 9))) != ((unsigned __int8)(a1))) goto loc_003D8380;
    if (((unsigned __int8)(a1)) == ((unsigned __int8)(a1))) goto loc_003D83C6;
loc_003D851F:
    if (((*(unsigned int *)(a5 + 60)) & ((unsigned int)(*(unsigned __int8 *)(v_stack_p8 + 9)))) != 0) goto loc_003D83D4;
    goto loc_003D8380;
loc_003D852D:
    goto loc_003D8318;
loc_003D8538:
loc_003D8542:
    result = KiOpFetchNextByte(a5, v_stack_p68, v_stack_p60, (unsigned int)(0xC000001DULL));
    if (sign_flag) goto loc_003D83E6;
    v_rbx = (v_stack_p68) + 1;
    v_rsi = (unsigned int)((1) + (-1));
    if (condition_is_not_equal) goto loc_003D8542;
loc_003D8566:
    *(unsigned __int64 *)(a5 + 72) = (__int8)(v_stack_p68);
    goto loc_003D842A;
loc_003D856F:
    result = (unsigned __int8)((*(unsigned __int8 *)(a5 + 65)) & (7));
    if (((unsigned __int8)(a5)) != ((unsigned __int8)(result))) goto loc_003D8380;
    goto loc_003D84EE;
loc_003D8582:
    result = KiOpFetchBytes(a5, 2, a5, 0);
    if (sign_flag) goto loc_003D83E6;
    goto loc_003D8566;
}
```

## 5. (Beta) C Style

```c
int64_t KiOpDecode(int64_t Arg1, void *Arg2, uint8_t Arg3, int32_t Arg4, void *Arg5)
{
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg5 = (uint8_t *)Arg5;

    int64_t result;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_p10;
    uint8_t v_stack_p18;
    uint8_t v_stack_p20;
    uint16_t v_stack_p28;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    v_stack_p20 = 0;
    local_rbx = 0;
    local_r12 = 0;
    v_stack_p10 = 0;
    v_stack_p18 = 0;
    v_stack_p28 = 0;
    *(uint64_t *)(arg5) = v_xmm0;
    *(uint64_t *)(arg5 + 0x10) = v_xmm0;
    *(uint64_t *)(arg5 + 0x20) = v_xmm0;
    *(uint64_t *)(arg5 + 0x30) = v_xmm0;
    *(uint64_t *)(arg5 + 0x40) = v_xmm0;
    *(uint64_t *)(arg5 + 0x50) = v_xmm0;
    *(uint64_t *)(arg5 + 0x60) = v_xmm0;
    *(uint32_t *)(arg5 + 0x3C) = Arg4;
    *(uint64_t *)(arg5) = *(uint64_t *)(arg2 + 0xF8);
    *(uint64_t *)(arg5 + 0x10) = *(uint64_t *)(arg2 + 0xF8);
    *(uint64_t *)(arg5 + 0x8) = *(uint64_t *)(arg2 + 0xF8) + 16;
    if (Arg3 != 1) goto loc_003D827F;
    Arg1 = *(uint64_t *)(arg2 + 0xF8);
    if ((*(uint64_t *)(arg2 + 0xF8)) >= (*(uint64_t *)(arg2 + 0xF8) + 16)) { Arg1 = *(uint64_t *)(arg2 + 0xF8) + 16; }
    goto loc_003D827F;
loc_003D827F:
    *(uint64_t *)(arg5 + 0x20) = Arg1;
    *(void **)(arg5 + 0x18) = Arg2;
    *(uint8_t *)(arg5 + 0x51) = Arg3;
    *(uint8_t *)(arg5 + 0x61) = 0;
    if ((*(uint16_t *)(arg2 + 0x38)) == 35) {
        *(uint8_t *)(arg5 + 0x3A) = 1;
    }
loc_003D82A1:
    result = KiOpFetchNextByte(Arg5, v_stack_p18, Arg3, Arg4);
    if (sign_flag) goto loc_003D83E6;
    local_r11 = 0;
    if ((*(uint8_t *)(arg5 + 0x3A)) != 0) goto loc_003D82D8;
    result = (uint8_t)(((uint8_t)(v_stack_p18)) & (240));
    if (((uint8_t)(result)) == 64) goto loc_003D8301;
loc_003D82D8:
loc_003D82E0:
    if (0 >= 11) goto loc_003D830B;
    if ((*(uint8_t *)(0 + 0x0 * 2 * 4 + v_rip - 0x3C4601 * 1)) == ((uint8_t)(v_stack_p18))) goto loc_003D8470;
    Arg2 = (uint32_t)((0) + 1);
    goto loc_003D82E0;
loc_003D8301:
    *(uint8_t *)(arg5 + 0x40) = (uint8_t)(v_stack_p18);
loc_003D830B:
    if ((uint32_t)((uint32_t)(0x800ULL)) != 0) goto loc_003D843D;
loc_003D8314:
loc_003D8318:
    if (sign_flag) goto loc_003D842A;
    if (0 != 0) goto loc_003D82A1;
    if (((uint8_t)(v_stack_p18)) == 15) goto loc_003D847F;
loc_003D8333:
    result = (*(uint64_t *)(arg5 + 0x10)) - 1;
    *(uint64_t *)(arg5 + 0x28) = result;
    *(uint8_t *)(arg5 + 0x38) = (uint8_t)(v_stack_p18);
    if (((uint8_t)(v_stack_p18)) < 15) goto loc_003D8467;
    local_rsi = v_rip - 4021287;
    if ((uint8_t)(*(uint8_t *)(arg5 + 0x39)) != 0) { local_rsi = v_rip - 4020672; }
    local_rbx = v_rip - 4021715;
    if ((uint8_t)(*(uint8_t *)(arg5 + 0x39)) != 0) { local_rbx = v_rip - 4021292; }
    local_rbx = (local_rbx) - (24);
loc_003D8380:
    local_rbx = (local_rbx) + (24);
    if (local_rbx == local_rsi) goto loc_003D83D8;
    if (((uint8_t)(*(uint8_t *)(arg5 + 0x38))) < ((uint8_t)(*(uint8_t *)(local_rbx)))) goto loc_003D8380;
    result = (uint8_t)((*(uint8_t *)(local_rbx)) - 1);
    result = (uint8_t)((result) + (*(uint8_t *)(local_rbx + 0x1)));
    if (((uint8_t)(*(uint8_t *)(arg5 + 0x38))) > ((uint8_t)(result))) goto loc_003D8380;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x4))) != 0) goto loc_003D842F;
loc_003D83A8:
    if ((*(uint8_t *)(local_rbx + 0x8)) != 255) goto loc_003D84A6;
    if ((*(uint8_t *)(local_rbx + 0x9)) != 255) goto loc_003D84A6;
    if ((*(uint8_t *)(local_rbx + 0xA)) != 255) goto loc_003D84A6;
loc_003D83C6:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbx + 0xC))) & (0xF4000000ULL));
    if (condition_is_not_equal) goto loc_003D851F;
loc_003D83D4:
    *(uint64_t *)(arg5 + 0x58) = local_rbx;
loc_003D83D8:
loc_003D83DB:
    if (*(uint64_t *)(arg5 + 0x58) != 0) goto loc_003D83F9;
    result = 0;
loc_003D83E6:
    local_rsp = (local_rsp) + (32);
    return result;
loc_003D83F9:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0xC)))) & (4)) == 0) goto loc_003D840F;
    result = KiOpDecodeModRM(Arg5, Arg2, v_stack_p18, 0);
    if (sign_flag) goto loc_003D83E6;
loc_003D840F:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0xC)))) & (1)) != 0) goto loc_003D8538;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg5 + 0x58) + 0xC)))) & (2)) != 0) goto loc_003D8582;
loc_003D842A:
    goto loc_003D83E6;
loc_003D842F:
    if (((*(uint32_t *)(arg5 + 0x30)) & ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg5 + 0x58) + 0xC))))) == 0) goto loc_003D8380;
    goto loc_003D83A8;
loc_003D843D:
    if ((((uint32_t)((uint32_t)(0x800ULL))) & ((uint32_t)((uint32_t)(*(uint32_t *)(arg5 + 0x30))))) != 0) goto loc_003D852D;
    if ((((uint32_t)(local_rsi)) & ((uint32_t)((uint32_t)(*(uint32_t *)(arg5 + 0x34))))) != 0) goto loc_003D852D;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg5 + 0x30))) | ((uint32_t)((uint32_t)(0x800ULL))));
    *(uint32_t *)(arg5 + 0x30) = (uint32_t)(result);
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg5 + 0x34))) | ((uint32_t)(local_rsi)));
    *(uint32_t *)(arg5 + 0x34) = (uint32_t)(Arg1);
    goto loc_003D8314;
loc_003D8467:
    *(uint64_t *)(arg5 + 0x58) = 0;
    goto loc_003D83DB;
loc_003D8470:
    goto loc_003D830B;
loc_003D847F:
    *(uint8_t *)(arg5 + 0x39) = 1;
    result = KiOpFetchNextByte(Arg5, v_stack_p60, v_stack_p18, (uint32_t)((uint32_t)(result)));
    if (sign_flag) goto loc_003D83E6;
    goto loc_003D8333;
loc_003D84A6:
    if ((*(uint8_t *)(arg5 + 0x50)) != 0) goto loc_003D84C7;
    result = KiOpFetchNextByte(Arg5, Arg5 + 65, v_stack_p60, (uint32_t)((uint32_t)(result)));
    if (sign_flag) goto loc_003D83E6;
    *(uint8_t *)(arg5 + 0x50) = 1;
loc_003D84C7:
    if (((uint8_t)(*(uint8_t *)(v_stack_p8 + 0x8))) == 255) goto loc_003D84E1;
    result = (uint8_t)((*(uint8_t *)(arg5 + 0x41)) >> (3));
    result = (uint8_t)((result) & (7));
    if (((uint8_t)(*(uint8_t *)(v_stack_p8 + 0x8))) != ((uint8_t)(result))) goto loc_003D8380;
loc_003D84E1:
    if (((uint8_t)(*(uint8_t *)(v_stack_p8 + 0xA))) != 255) goto loc_003D856F;
loc_003D84EE:
    if (((uint8_t)(*(uint8_t *)(v_stack_p8 + 0x9))) == 255) goto loc_003D83C6;
    Arg1 = (uint8_t)((*(uint8_t *)(arg5 + 0x41)) >> (6));
    if (((uint8_t)(*(uint8_t *)(v_stack_p8 + 0x9))) != ((uint8_t)(Arg1))) goto loc_003D8380;
    if (((uint8_t)(Arg1)) == ((uint8_t)(Arg1))) goto loc_003D83C6;
loc_003D851F:
    if (((*(uint32_t *)(arg5 + 0x3C)) & ((uint32_t)(*(uint8_t *)(v_stack_p8 + 0x9)))) != 0) goto loc_003D83D4;
    goto loc_003D8380;
loc_003D852D:
    goto loc_003D8318;
loc_003D8538:
loc_003D8542:
    result = KiOpFetchNextByte(Arg5, v_stack_p68, v_stack_p60, (uint32_t)(0xC000001DULL));
    if (sign_flag) goto loc_003D83E6;
    local_rbx = (v_stack_p68) + 1;
    local_rsi = (uint32_t)((1) + (-1));
    if (condition_is_not_equal) goto loc_003D8542;
loc_003D8566:
    *(uint64_t *)(arg5 + 0x48) = (int8_t)(v_stack_p68);
    goto loc_003D842A;
loc_003D856F:
    result = (uint8_t)((*(uint8_t *)(arg5 + 0x41)) & (7));
    if (((uint8_t)(Arg5)) != ((uint8_t)(result))) goto loc_003D8380;
    goto loc_003D84EE;
loc_003D8582:
    result = KiOpFetchBytes(Arg5, 2, Arg5, 0);
    if (sign_flag) goto loc_003D83E6;
    goto loc_003D8566;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x38` | `16` | `R` |
| `Arg2` | `+ 0xF8` | `64` | `R` |
| `Arg5` | `+ 0x0` | `8` | `R` |
| `Arg5` | `+ 0x0` | `64` | `W` |
| `Arg5` | `+ 0x0` | `128` | `R` |
| `Arg5` | `+ 0x8` | `64` | `W` |
| `Arg5` | `+ 0x10` | `64` | `R` |
| `Arg5` | `+ 0x10` | `64` | `W` |
| `Arg5` | `+ 0x10` | `128` | `R` |
| `Arg5` | `+ 0x18` | `64` | `W` |
| `Arg5` | `+ 0x20` | `64` | `W` |
| `Arg5` | `+ 0x20` | `128` | `R` |
| `Arg5` | `+ 0x28` | `64` | `W` |
| `Arg5` | `+ 0x30` | `32` | `R` |
| `Arg5` | `+ 0x30` | `32` | `W` |
| `Arg5` | `+ 0x30` | `128` | `R` |
| `Arg5` | `+ 0x34` | `32` | `R` |
| `Arg5` | `+ 0x34` | `32` | `W` |
| `Arg5` | `+ 0x38` | `8` | `R` |
| `Arg5` | `+ 0x38` | `8` | `W` |
| `Arg5` | `+ 0x39` | `8` | `R` |
| `Arg5` | `+ 0x39` | `8` | `W` |
| `Arg5` | `+ 0x3A` | `8` | `R` |
| `Arg5` | `+ 0x3A` | `8` | `W` |
| `Arg5` | `+ 0x3C` | `32` | `R` |
| `Arg5` | `+ 0x3C` | `32` | `W` |
| `Arg5` | `+ 0x40` | `8` | `W` |
| `Arg5` | `+ 0x40` | `128` | `R` |
| `Arg5` | `+ 0x41` | `64` | `R` |
| `Arg5` | `+ 0x48` | `64` | `W` |
| `Arg5` | `+ 0x50` | `8` | `R` |
| `Arg5` | `+ 0x50` | `8` | `W` |

추가 오프셋 6개는 표에서 생략했습니다.

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003D81F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
