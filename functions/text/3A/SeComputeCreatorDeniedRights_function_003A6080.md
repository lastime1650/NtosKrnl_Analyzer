# SeComputeCreatorDeniedRights

- RVA: `0x003A6080`–`0x003A663B` (길이 `1,467` bytes)
- VA: `0x00000001403A6080`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00089B18`
- 디코드: `365`개 명령, `1,467/1,467` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x003A61A2` → [memcmp](../6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x003A620C` → [SepGetScopedPolicySid](SepGetScopedPolicySid_function_003A59AC.md) (function, `0x003A59AC`)
- `0x003A621E` → [SepRmReferenceFindCap](SepRmReferenceFindCap_function_003A58EC.md) (function, `0x003A58EC`)
- `0x003A62FF` → [memcmp](../6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x003A6408` → [SeAccessCheck](SeAccessCheck_function_003A6BC0.md) (function, `0x003A6BC0`)
- `0x003A646A` → [SeAccessCheck](SeAccessCheck_function_003A6BC0.md) (function, `0x003A6BC0`)
- `0x003A650D` → [memcmp](../6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x003A65C2` → [memcmp](../6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x003A65E5` → [memcmp](../6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)

### Direct callers
- [ObpCreateHandle](../../page/86/ObpCreateHandle_function_0086B950.md) at `0x0086BDDD`
- [ObpCreateHandle](../../page/86/ObpCreateHandle_function_0086B950.md) at `0x0086BF20`
- [ObpGrantAccess](../../page/86/ObpGrantAccess_function_0086F250.md) at `0x0086F60B`
- [ObpAdjustCreatorAccessState](../../page/87/ObpAdjustCreatorAccessState_function_00874650.md) at `0x00874732`

### Static image references
- `0x003A612B` → RVA `0x00FD9AA0` (`PAGEDATA`; read)
- `0x003A622A` → RVA `0x00FD80F0` (`PAGEDATA`; read)
- `0x003A62B5` → RVA `0x00011DE0` (`.rdata`; read)
- `0x003A639B` → RVA `0x000118E0` (`.rdata`; read)
- `0x003A6590` → RVA `0x00F04AC5` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003A6080  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
003A6085  44 89 44 24 18                  mov dword ptr [rsp + 0x18], r8d
003A608A  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
003A608F  55                              push rbp
003A6090  56                              push rsi
003A6091  57                              push rdi
003A6092  41 54                           push r12
003A6094  41 55                           push r13
003A6096  41 56                           push r14
003A6098  41 57                           push r15
003A609A  48 81 EC 80 00 00 00            sub rsp, 0x80
003A60A1  C7 44 24 5C 00 00 00 00         mov dword ptr [rsp + 0x5c], 0
003A60A9  4C 8B E1                        mov r12, rcx
003A60AC  C7 44 24 58 00 00 00 00         mov dword ptr [rsp + 0x58], 0
003A60B4  C7 44 24 60 00 00 00 00         mov dword ptr [rsp + 0x60], 0
003A60BC  41 F7 C0 00 00 0C 00            test r8d, 0xc0000
003A60C3  0F 84 25 01 00 00               je 0x1403a61ee
003A60C9  48 8B 42 48                     mov rax, qword ptr [rdx + 0x48]
003A60CD  48 8B 68 30                     mov rbp, qword ptr [rax + 0x30]
003A60D1  48 89 6C 24 70                  mov qword ptr [rsp + 0x70], rbp
003A60D6  48 85 ED                        test rbp, rbp
003A60D9  75 1F                           jne 0x1403a60fa
003A60DB  4C 89 4C 24 70                  mov qword ptr [rsp + 0x70], r9
003A60E0  49 8B E9                        mov rbp, r9
003A60E3  4D 85 C9                        test r9, r9
003A60E6  75 12                           jne 0x1403a60fa
003A60E8  48 8B 6A 40                     mov rbp, qword ptr [rdx + 0x40]
003A60EC  48 89 6C 24 70                  mov qword ptr [rsp + 0x70], rbp
003A60F1  48 85 ED                        test rbp, rbp
003A60F4  0F 84 F4 00 00 00               je 0x1403a61ee
003A60FA  44 0F B7 7D 02                  movzx r15d, word ptr [rbp + 2]
003A60FF  41 F6 C7 04                     test r15b, 4
003A6103  75 11                           jne 0x1403a6116
003A6105  41 F6 C7 10                     test r15b, 0x10
003A6109  0F 85 68 04 00 00               jne 0x1403a6577
003A610F  33 C9                           xor ecx, ecx
003A6111  E9 7A 04 00 00                  jmp 0x1403a6590
003A6116  66 45 85 FF                     test r15w, r15w
003A611A  0F 89 E8 04 00 00               jns 0x1403a6608
003A6120  8B 45 10                        mov eax, dword ptr [rbp + 0x10]
003A6123  85 C0                           test eax, eax
003A6125  74 DE                           je 0x1403a6105
003A6127  48 8D 0C 28                     lea rcx, [rax + rbp]
003A612B  48 8B 05 6E 39 C3 00            mov rax, qword ptr [rip + 0xc3396e]
003A6132  4C 8B B0 00 02 00 00            mov r14, qword ptr [rax + 0x200]
003A6139  48 85 C9                        test rcx, rcx
003A613C  74 C7                           je 0x1403a6105
003A613E  0F B7 71 04                     movzx esi, word ptr [rcx + 4]
003A6142  48 8D 59 08                     lea rbx, [rcx + 8]
003A6146  33 FF                           xor edi, edi
003A6148  3B FE                           cmp edi, esi
003A614A  73 B9                           jae 0x1403a6105
003A614C  F6 43 01 08                     test byte ptr [rbx + 1], 8
003A6150  75 5D                           jne 0x1403a61af
003A6152  0F B6 0B                        movzx ecx, byte ptr [rbx]
003A6155  8D 41 F5                        lea eax, [rcx - 0xb]
003A6158  3C 01                           cmp al, 1
003A615A  76 5E                           jbe 0x1403a61ba
003A615C  8D 41 FB                        lea eax, [rcx - 5]
003A615F  3C 03                           cmp al, 3
003A6161  76 57                           jbe 0x1403a61ba
003A6163  80 F9 0F                        cmp cl, 0xf
003A6166  0F 83 AE 04 00 00               jae 0x1403a661a
003A616C  80 F9 04                        cmp cl, 4
003A616F  0F 84 F9 03 00 00               je 0x1403a656e
003A6175  80 F9 0B                        cmp cl, 0xb
003A6178  0F 83 A5 04 00 00               jae 0x1403a6623
003A617E  48 8D 4B 08                     lea rcx, [rbx + 8]
003A6182  48 85 C9                        test rcx, rcx
003A6185  74 28                           je 0x1403a61af
003A6187  0F B7 01                        movzx eax, word ptr [rcx]
003A618A  66 41 3B 06                     cmp ax, word ptr [r14]
003A618E  75 1F                           jne 0x1403a61af
003A6190  44 8B C0                        mov r8d, eax
003A6193  49 8B D6                        mov rdx, r14
003A6196  49 C1 E8 08                     shr r8, 8
003A619A  4E 8D 04 85 08 00 00 00         lea r8, [r8*4 + 8]
003A61A2  E8 69 09 32 00                  call 0x1406c6b10
003A61A7  85 C0                           test eax, eax
003A61A9  0F 84 8D 00 00 00               je 0x1403a623c
003A61AF  0F B7 43 02                     movzx eax, word ptr [rbx + 2]
003A61B3  FF C7                           inc edi
003A61B5  48 03 D8                        add rbx, rax
003A61B8  EB 8E                           jmp 0x1403a6148
003A61BA  8B 4B 08                        mov ecx, dword ptr [rbx + 8]
003A61BD  8B C1                           mov eax, ecx
003A61BF  83 E0 02                        and eax, 2
003A61C2  83 E1 01                        and ecx, 1
003A61C5  48 C1 E0 03                     shl rax, 3
003A61C9  48 83 C8 0C                     or rax, 0xc
003A61CD  48 C1 E1 04                     shl rcx, 4
003A61D1  48 03 C3                        add rax, rbx
003A61D4  48 03 C8                        add rcx, rax
003A61D7  EB A9                           jmp 0x1403a6182
003A61D9  8B 47 08                        mov eax, dword ptr [rdi + 8]
003A61DC  A8 04                           test al, 4
003A61DE  0F 84 83 03 00 00               je 0x1403a6567
003A61E4  B0 01                           mov al, 1
003A61E6  84 C0                           test al, al
003A61E8  0F 85 A6 01 00 00               jne 0x1403a6394
003A61EE  33 C0                           xor eax, eax
003A61F0  48 8B 9C 24 C8 00 00 00         mov rbx, qword ptr [rsp + 0xc8]
003A61F8  48 81 C4 80 00 00 00            add rsp, 0x80
003A61FF  41 5F                           pop r15
003A6201  41 5E                           pop r14
003A6203  41 5D                           pop r13
003A6205  41 5C                           pop r12
003A6207  5F                              pop rdi
003A6208  5E                              pop rsi
003A6209  5D                              pop rbp
003A620A  C3                              ret
003A620B  CC                              int3
003A620C  E8 9B F7 FF FF                  call 0x1403a59ac
003A6211  48 85 C0                        test rax, rax
003A6214  74 D8                           je 0x1403a61ee
003A6216  48 8D 54 24 68                  lea rdx, [rsp + 0x68]
003A621B  48 8B C8                        mov rcx, rax
003A621E  E8 C9 F6 FF FF                  call 0x1403a58ec
003A6223  48 8B 54 24 68                  mov rdx, qword ptr [rsp + 0x68]
003A6228  85 C0                           test eax, eax
003A622A  48 8B 0D BF 1E C3 00            mov rcx, qword ptr [rip + 0xc31ebf]
003A6231  48 0F 48 D1                     cmovs rdx, rcx
003A6235  8B 42 38                        mov eax, dword ptr [rdx + 0x38]
003A6238  A8 01                           test al, 1
003A623A  74 B2                           je 0x1403a61ee
003A623C  49 8B 34 24                     mov rsi, qword ptr [r12]
003A6240  48 85 F6                        test rsi, rsi
003A6243  75 05                           jne 0x1403a624a
003A6245  49 8B 74 24 10                  mov rsi, qword ptr [r12 + 0x10]
003A624A  66 83 7D 02 00                  cmp word ptr [rbp + 2], 0
003A624F  0F 8D 61 03 00 00               jge 0x1403a65b6
003A6255  8B 45 04                        mov eax, dword ptr [rbp + 4]
003A6258  85 C0                           test eax, eax
003A625A  0F 84 02 01 00 00               je 0x1403a6362
003A6260  4C 8D 34 28                     lea r14, [rax + rbp]
003A6264  48 8D AE E8 00 00 00            lea rbp, [rsi + 0xe8]
003A626B  48 85 ED                        test rbp, rbp
003A626E  0F 84 7A FF FF FF               je 0x1403a61ee
003A6274  4D 85 F6                        test r14, r14
003A6277  0F 84 71 FF FF FF               je 0x1403a61ee
003A627D  41 0F B6 46 01                  movzx eax, byte ptr [r14 + 1]
003A6282  45 0F B7 0E                     movzx r9d, word ptr [r14]
003A6286  66 44 89 4C 24 50               mov word ptr [rsp + 0x50], r9w
003A628C  41 0F B6 4C 86 04               movzx ecx, byte ptr [r14 + rax*4 + 4]
003A6292  44 8D 04 85 08 00 00 00         lea r8d, [rax*4 + 8]
003A629A  8B C1                           mov eax, ecx
003A629C  44 89 44 24 54                  mov dword ptr [rsp + 0x54], r8d
003A62A1  83 E1 0F                        and ecx, 0xf
003A62A4  48 C1 E8 04                     shr rax, 4
003A62A8  48 8B BC C5 90 00 00 00         mov rdi, qword ptr [rbp + rax*8 + 0x90]
003A62B0  48 23 7C CD 10                  and rdi, qword ptr [rbp + rcx*8 + 0x10]
003A62B5  48 8D 0D 24 BB C6 FF            lea rcx, [rip - 0x3944dc]
003A62BC  45 32 ED                        xor r13b, r13b
003A62BF  48 85 FF                        test rdi, rdi
003A62C2  74 62                           je 0x1403a6326
003A62C4  40 0F B6 DF                     movzx ebx, dil
003A62C8  84 DB                           test bl, bl
003A62CA  75 0A                           jne 0x1403a62d6
003A62CC  41 80 C5 08                     add r13b, 8
003A62D0  48 C1 EF 08                     shr rdi, 8
003A62D4  EB E9                           jmp 0x1403a62bf
003A62D6  4C 8B 65 08                     mov r12, qword ptr [rbp + 8]
003A62DA  45 0F B6 FD                     movzx r15d, r13b
003A62DE  0F B6 C3                        movzx eax, bl
003A62E1  0F B6 0C 08                     movzx ecx, byte ptr [rax + rcx]
003A62E5  44 03 F9                        add r15d, ecx
003A62E8  89 4C 24 68                     mov dword ptr [rsp + 0x68], ecx
003A62EC  49 C1 E7 04                     shl r15, 4
003A62F0  4D 03 FC                        add r15, r12
003A62F3  49 8B 17                        mov rdx, qword ptr [r15]
003A62F6  66 44 39 0A                     cmp word ptr [rdx], r9w
003A62FA  75 1B                           jne 0x1403a6317
003A62FC  49 8B CE                        mov rcx, r14
003A62FF  E8 0C 08 32 00                  call 0x1406c6b10
003A6304  85 C0                           test eax, eax
003A6306  74 62                           je 0x1403a636a
003A6308  8B 4C 24 68                     mov ecx, dword ptr [rsp + 0x68]
003A630C  44 8B 44 24 54                  mov r8d, dword ptr [rsp + 0x54]
003A6311  44 0F B7 4C 24 50               movzx r9d, word ptr [rsp + 0x50]
003A6317  0F B6 DB                        movzx ebx, bl
003A631A  0F BB CB                        btc ebx, ecx
003A631D  48 8D 0D BC BA C6 FF            lea rcx, [rip - 0x394544]
003A6324  EB A2                           jmp 0x1403a62c8
003A6326  8B 5D 00                        mov ebx, dword ptr [rbp]
003A6329  83 FB 40                        cmp ebx, 0x40
003A632C  0F 86 BC FE FF FF               jbe 0x1403a61ee
003A6332  41 BD 40 00 00 00               mov r13d, 0x40
003A6338  41 8B FD                        mov edi, r13d
003A633B  3B FB                           cmp edi, ebx
003A633D  0F 83 AB FE FF FF               jae 0x1403a61ee
003A6343  4C 8B 65 08                     mov r12, qword ptr [rbp + 8]
003A6347  44 8B FF                        mov r15d, edi
003A634A  49 C1 E7 04                     shl r15, 4
003A634E  4D 03 FC                        add r15, r12
003A6351  49 8B 17                        mov rdx, qword ptr [r15]
003A6354  66 44 39 0A                     cmp word ptr [rdx], r9w
003A6358  0F 84 61 02 00 00               je 0x1403a65bf
003A635E  FF C7                           inc edi
003A6360  EB D9                           jmp 0x1403a633b
003A6362  45 33 F6                        xor r14d, r14d
003A6365  E9 FA FE FF FF                  jmp 0x1403a6264
003A636A  41 BD 40 00 00 00               mov r13d, 0x40
003A6370  49 8D 4F 08                     lea rcx, [r15 + 8]
003A6374  4D 3B FC                        cmp r15, r12
003A6377  0F 84 DB 01 00 00               je 0x1403a6558
003A637D  8B 01                           mov eax, dword ptr [rcx]
003A637F  A8 04                           test al, 4
003A6381  0F 84 67 FE FF FF               je 0x1403a61ee
003A6387  83 BE 80 00 00 00 00            cmp dword ptr [rsi + 0x80], 0
003A638E  0F 85 EA 00 00 00               jne 0x1403a647e
003A6394  8B B4 24 D0 00 00 00            mov esi, dword ptr [rsp + 0xd0]
003A639B  4C 8D 3D 3E B5 C6 FF            lea r15, [rip - 0x394ac2]
003A63A2  48 8B BC 24 C0 00 00 00         mov rdi, qword ptr [rsp + 0xc0]
003A63AA  41 BE 00 00 04 00               mov r14d, 0x40000
003A63B0  48 8B 5C 24 70                  mov rbx, qword ptr [rsp + 0x70]
003A63B5  41 85 F6                        test r14d, esi
003A63B8  0F 84 53 02 00 00               je 0x1403a6611
003A63BE  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
003A63C7  45 8B CE                        mov r9d, r14d
003A63CA  41 B0 01                        mov r8b, 1
003A63CD  48 8B D7                        mov rdx, rdi
003A63D0  0F B6 88 32 02 00 00            movzx ecx, byte ptr [rax + 0x232]
003A63D7  48 8D 44 24 5C                  lea rax, [rsp + 0x5c]
003A63DC  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
003A63E1  48 8D 44 24 60                  lea rax, [rsp + 0x60]
003A63E6  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
003A63EB  88 4C 24 38                     mov byte ptr [rsp + 0x38], cl
003A63EF  48 8B CB                        mov rcx, rbx
003A63F2  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
003A63F7  48 C7 44 24 28 00 00 00 00      mov qword ptr [rsp + 0x28], 0
003A6400  C7 44 24 20 00 00 00 00         mov dword ptr [rsp + 0x20], 0
003A6408  E8 B3 07 00 00                  call 0x1403a6bc0
003A640D  8B 6C 24 58                     mov ebp, dword ptr [rsp + 0x58]
003A6411  84 C0                           test al, al
003A6413  41 0F 44 EE                     cmove ebp, r14d
003A6417  0F BA E6 13                     bt esi, 0x13
003A641B  73 5A                           jae 0x1403a6477
003A641D  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
003A6426  41 B9 00 00 08 00               mov r9d, 0x80000
003A642C  41 B0 01                        mov r8b, 1
003A642F  48 8B CB                        mov rcx, rbx
003A6432  0F B6 90 32 02 00 00            movzx edx, byte ptr [rax + 0x232]
003A6439  48 8D 44 24 5C                  lea rax, [rsp + 0x5c]
003A643E  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
003A6443  48 8D 44 24 60                  lea rax, [rsp + 0x60]
003A6448  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
003A644D  88 54 24 38                     mov byte ptr [rsp + 0x38], dl
003A6451  48 8B D7                        mov rdx, rdi
003A6454  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
003A6459  48 C7 44 24 28 00 00 00 00      mov qword ptr [rsp + 0x28], 0
003A6462  C7 44 24 20 00 00 00 00         mov dword ptr [rsp + 0x20], 0
003A646A  E8 51 07 00 00                  call 0x1403a6bc0
003A646F  84 C0                           test al, al
003A6471  75 04                           jne 0x1403a6477
003A6473  0F BA ED 13                     bts ebp, 0x13
003A6477  8B C5                           mov eax, ebp
003A6479  E9 72 FD FF FF                  jmp 0x1403a61f0
003A647E  4C 8D BE F8 01 00 00            lea r15, [rsi + 0x1f8]
003A6485  4D 85 FF                        test r15, r15
003A6488  0F 84 D9 00 00 00               je 0x1403a6567
003A648E  41 0F B6 46 01                  movzx eax, byte ptr [r14 + 1]
003A6493  45 0F B7 06                     movzx r8d, word ptr [r14]
003A6497  66 44 89 44 24 50               mov word ptr [rsp + 0x50], r8w
003A649D  41 0F B6 4C 86 04               movzx ecx, byte ptr [r14 + rax*4 + 4]
003A64A3  44 8D 0C 85 08 00 00 00         lea r9d, [rax*4 + 8]
003A64AB  8B C1                           mov eax, ecx
003A64AD  44 89 4C 24 54                  mov dword ptr [rsp + 0x54], r9d
003A64B2  48 C1 E8 04                     shr rax, 4
003A64B6  83 E1 0F                        and ecx, 0xf
003A64B9  49 8B B4 C7 90 00 00 00         mov rsi, qword ptr [r15 + rax*8 + 0x90]
003A64C1  49 23 74 CF 10                  and rsi, qword ptr [r15 + rcx*8 + 0x10]
003A64C6  40 32 ED                        xor bpl, bpl
003A64C9  48 85 F6                        test rsi, rsi
003A64CC  74 60                           je 0x1403a652e
003A64CE  40 0F B6 DE                     movzx ebx, sil
003A64D2  84 DB                           test bl, bl
003A64D4  75 0A                           jne 0x1403a64e0
003A64D6  40 80 C5 08                     add bpl, 8
003A64DA  48 C1 EE 08                     shr rsi, 8
003A64DE  EB E9                           jmp 0x1403a64c9
003A64E0  40 0F B6 FD                     movzx edi, bpl
003A64E4  48 8D 0D F5 B8 C6 FF            lea rcx, [rip - 0x39470b]
003A64EB  0F B6 C3                        movzx eax, bl
003A64EE  44 0F B6 24 08                  movzx r12d, byte ptr [rax + rcx]
003A64F3  41 03 FC                        add edi, r12d
003A64F6  48 C1 E7 04                     shl rdi, 4
003A64FA  49 03 7F 08                     add rdi, qword ptr [r15 + 8]
003A64FE  48 8B 17                        mov rdx, qword ptr [rdi]
003A6501  66 44 39 02                     cmp word ptr [rdx], r8w
003A6505  75 1E                           jne 0x1403a6525
003A6507  45 8B C1                        mov r8d, r9d
003A650A  49 8B CE                        mov rcx, r14
003A650D  E8 FE 05 32 00                  call 0x1406c6b10
003A6512  85 C0                           test eax, eax
003A6514  0F 84 BF FC FF FF               je 0x1403a61d9
003A651A  44 0F B7 44 24 50               movzx r8d, word ptr [rsp + 0x50]
003A6520  44 8B 4C 24 54                  mov r9d, dword ptr [rsp + 0x54]
003A6525  0F B6 DB                        movzx ebx, bl
003A6528  44 0F BB E3                     btc ebx, r12d
003A652C  EB A4                           jmp 0x1403a64d2
003A652E  41 8B 1F                        mov ebx, dword ptr [r15]
003A6531  83 FB 40                        cmp ebx, 0x40
003A6534  76 31                           jbe 0x1403a6567
003A6536  44 3B EB                        cmp r13d, ebx
003A6539  73 2C                           jae 0x1403a6567
003A653B  41 8B FD                        mov edi, r13d
003A653E  48 C1 E7 04                     shl rdi, 4
003A6542  49 03 7F 08                     add rdi, qword ptr [r15 + 8]
003A6546  48 8B 17                        mov rdx, qword ptr [rdi]
003A6549  66 44 39 02                     cmp word ptr [rdx], r8w
003A654D  0F 84 8C 00 00 00               je 0x1403a65df
003A6553  41 FF C5                        inc r13d
003A6556  EB DE                           jmp 0x1403a6536
003A6558  8B 01                           mov eax, dword ptr [rcx]
003A655A  A8 10                           test al, 0x10
003A655C  0F 85 1B FE FF FF               jne 0x1403a637d
003A6562  E9 20 FE FF FF                  jmp 0x1403a6387
003A6567  32 C0                           xor al, al
003A6569  E9 78 FC FF FF                  jmp 0x1403a61e6
003A656E  48 8D 4B 0C                     lea rcx, [rbx + 0xc]
003A6572  E9 0B FC FF FF                  jmp 0x1403a6182
003A6577  66 45 85 FF                     test r15w, r15w
003A657B  0F 89 81 00 00 00               jns 0x1403a6602
003A6581  8B 45 0C                        mov eax, dword ptr [rbp + 0xc]
003A6584  85 C0                           test eax, eax
003A6586  0F 84 A8 00 00 00               je 0x1403a6634
003A658C  48 8D 0C 28                     lea rcx, [rax + rbp]
003A6590  0F B6 05 2E E5 B5 00            movzx eax, byte ptr [rip + 0xb5e52e]
003A6597  48 C7 44 24 68 00 00 00 00      mov qword ptr [rsp + 0x68], 0
003A65A0  84 C0                           test al, al
003A65A2  0F 84 46 FC FF FF               je 0x1403a61ee
003A65A8  48 85 C9                        test rcx, rcx
003A65AB  0F 84 3D FC FF FF               je 0x1403a61ee
003A65B1  E9 56 FC FF FF                  jmp 0x1403a620c
003A65B6  4C 8B 75 08                     mov r14, qword ptr [rbp + 8]
003A65BA  E9 A5 FC FF FF                  jmp 0x1403a6264
003A65BF  49 8B CE                        mov rcx, r14
003A65C2  E8 49 05 32 00                  call 0x1406c6b10
003A65C7  85 C0                           test eax, eax
003A65C9  0F 84 A1 FD FF FF               je 0x1403a6370
003A65CF  44 8B 44 24 54                  mov r8d, dword ptr [rsp + 0x54]
003A65D4  44 0F B7 4C 24 50               movzx r9d, word ptr [rsp + 0x50]
003A65DA  E9 7F FD FF FF                  jmp 0x1403a635e
003A65DF  45 8B C1                        mov r8d, r9d
003A65E2  49 8B CE                        mov rcx, r14
003A65E5  E8 26 05 32 00                  call 0x1406c6b10
003A65EA  85 C0                           test eax, eax
003A65EC  0F 84 E7 FB FF FF               je 0x1403a61d9
003A65F2  44 0F B7 44 24 50               movzx r8d, word ptr [rsp + 0x50]
003A65F8  44 8B 4C 24 54                  mov r9d, dword ptr [rsp + 0x54]
003A65FD  E9 51 FF FF FF                  jmp 0x1403a6553
003A6602  48 8B 4D 18                     mov rcx, qword ptr [rbp + 0x18]
003A6606  EB 88                           jmp 0x1403a6590
003A6608  48 8B 4D 20                     mov rcx, qword ptr [rbp + 0x20]
003A660C  E9 1A FB FF FF                  jmp 0x1403a612b
003A6611  8B 6C 24 58                     mov ebp, dword ptr [rsp + 0x58]
003A6615  E9 FD FD FF FF                  jmp 0x1403a6417
003A661A  80 F9 10                        cmp cl, 0x10
003A661D  0F 86 97 FB FF FF               jbe 0x1403a61ba
003A6623  80 E9 0D                        sub cl, 0xd
003A6626  80 F9 01                        cmp cl, 1
003A6629  0F 86 4F FB FF FF               jbe 0x1403a617e
003A662F  E9 7B FB FF FF                  jmp 0x1403a61af
003A6634  33 C9                           xor ecx, ecx
003A6636  E9 55 FF FF FF                  jmp 0x1403a6590
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SeComputeCreatorDeniedRights(__int64 a1, __int64 a2, int a3, __int64 a4)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m58;
    unsigned int v_stack_m5C;
    unsigned int v_stack_m60;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int8 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int16 v_stack_p50;
    unsigned int v_stack_p54;
    unsigned int v_stack_p58;
    unsigned __int64 v_stack_p5C;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p8;
    unsigned __int64 v_stack_pC0;
    unsigned int v_stack_pD0;

    v_stack_p10 = v_rbx;
    v_stack_p18 = a3;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (128);
    v_stack_m5C = 0;
    v_stack_m60 = 0;
    v_stack_m58 = 0;
    if (((a3) & (0xC0000ULL)) == 0) goto loc_003A61EE;
    v_stack_m48 = *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 48);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72) + 48) != 0) goto loc_003A60FA;
    v_stack_m48 = a4;
    if (a4 != 0) goto loc_003A60FA;
    v_stack_m48 = *(unsigned __int64 *)(a2 + 64);
    if (*(unsigned __int64 *)(a2 + 64) == 0) goto loc_003A61EE;
loc_003A60FA:
    if ((((unsigned __int8)(*(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 64) + 2))) & (4)) != 0) goto loc_003A6116;
loc_003A6105:
    if ((((unsigned __int8)(*(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 64) + 2))) & (16)) != 0) goto loc_003A6577;
    a1 = 0;
    goto loc_003A6590;
loc_003A6116:
    if (!sign_flag) goto loc_003A6608;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 64) + 16))) == 0) goto loc_003A6105;
loc_003A612B:
    if ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 64) + 16)) + *(unsigned __int64 *)(a2 + 64) * 1 == 0) goto loc_003A6105;
    v_rdi = 0;
loc_003A6148:
    if (0 >= ((unsigned int)(*(unsigned __int16 *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 64) + 16)) + *(unsigned __int64 *)(a2 + 64) * 1 + 4)))) goto loc_003A6105;
    if (((*(unsigned __int8 *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 64) + 16)) + *(unsigned __int64 *)(a2 + 64) * 1 + 8 + 1)) & (8)) != 0) goto loc_003A61AF;
    if (((unsigned __int8)(*(unsigned __int8 *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 64) + 16)) + *(unsigned __int64 *)(a2 + 64) * 1 + 8) - 11)) <= 1) goto loc_003A61BA;
    if (((unsigned __int8)(*(unsigned __int8 *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 64) + 16)) + *(unsigned __int64 *)(a2 + 64) * 1 + 8) - 5)) <= 3) goto loc_003A61BA;
    if (((unsigned __int8)(*(unsigned __int8 *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 64) + 16)) + *(unsigned __int64 *)(a2 + 64) * 1 + 8))) >= 15) goto loc_003A661A;
    if (((unsigned __int8)(*(unsigned __int8 *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 64) + 16)) + *(unsigned __int64 *)(a2 + 64) * 1 + 8))) == 4) goto loc_003A656E;
    if (((unsigned __int8)(*(unsigned __int8 *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 64) + 16)) + *(unsigned __int64 *)(a2 + 64) * 1 + 8))) >= 11) goto loc_003A6623;
loc_003A617E:
loc_003A6182:
    if ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 64) + 16)) + *(unsigned __int64 *)(a2 + 64) * 1 + 8 + 8 == 0) goto loc_003A61AF;
    if (((unsigned __int16)(*(unsigned __int16 *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 64) + 16)) + *(unsigned __int64 *)(a2 + 64) * 1 + 8 + 8))) != (*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12794222) + 512)))) goto loc_003A61AF;
    a3 = ((unsigned int)((unsigned int)(*(unsigned __int16 *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 64) + 16)) + *(unsigned __int64 *)(a2 + 64) * 1 + 8 + 8)))) >> (8);
    result = memcmp((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 64) + 16)) + *(unsigned __int64 *)(a2 + 64) * 1 + 8 + 8, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12794222) + 512), a3 * 4 + 8, a4);
    if ((unsigned int)(result) == 0) goto loc_003A623C;
loc_003A61AF:
    v_rdi = (unsigned int)((v_rdi) + 1);
    v_rbx = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 64) + 16)) + *(unsigned __int64 *)(a2 + 64) * 1 + 8) + (*(unsigned __int16 *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 64) + 16)) + *(unsigned __int64 *)(a2 + 64) * 1 + 8 + 2));
    goto loc_003A6148;
loc_003A61BA:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 8))))) & (2));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbx + 8))) & (1));
    result = (result) << (3);
    result = (result) | (12);
    a1 = (a1) << (4);
    result = (result) + (v_rbx);
    a1 = (a1) + (result);
    goto loc_003A6182;
loc_003A61D9:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rdi + 8)))) & (4)) == 0) goto loc_003A6567;
loc_003A61E6:
    if (1 != 0) goto loc_003A6394;
loc_003A61EE:
    result = 0;
loc_003A61F0:
    v_rsp = (v_rsp) + (128);
    return result;
loc_003A620C:
    result = SepGetScopedPolicySid(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12794222) + 512), a3 * 4 + 8, a4);
    if (result == 0) goto loc_003A61EE;
    result = SepRmReferenceFindCap(result, v_stack_p68, a3 * 4 + 8, a4);
    a2 = v_stack_p68;
    if (sign_flag) { a2 = *(unsigned __int64 *)(v_rip + 12787391); }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 56)))) & (1)) == 0) goto loc_003A61EE;
loc_003A623C:
    v_rsi = *(unsigned __int64 *)(a1);
    if (*(unsigned __int64 *)(a1) == 0) {
        v_rsi = *(unsigned __int64 *)(a1 + 16);
    }
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 64) + 2)) >= 0) goto loc_003A65B6;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 64) + 4))) == 0) goto loc_003A6362;
loc_003A6264:
    if (v_rsi + 232 == 0) goto loc_003A61EE;
    if ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 64) + 4)) + *(unsigned __int64 *)(a2 + 64) * 1 == 0) goto loc_003A61EE;
    v_stack_p50 = (unsigned __int16)(*(unsigned __int16 *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 64) + 4)) + *(unsigned __int64 *)(a2 + 64) * 1));
    v_stack_p54 = (unsigned int)(*(unsigned __int8 *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 64) + 4)) + *(unsigned __int64 *)(a2 + 64) * 1 + 1) * 4 + 8);
    a1 = (unsigned int)((*(unsigned __int8 *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 64) + 4)) + *(unsigned __int64 *)(a2 + 64) * 1 + *(unsigned __int8 *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 64) + 4)) + *(unsigned __int64 *)(a2 + 64) * 1 + 1) * 4 + 4)) & (15));
    result = ((unsigned int)((unsigned int)(*(unsigned __int8 *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 64) + 4)) + *(unsigned __int64 *)(a2 + 64) * 1 + *(unsigned __int8 *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 64) + 4)) + *(unsigned __int64 *)(a2 + 64) * 1 + 1) * 4 + 4)))) >> (4);
    v_rdi = (*(unsigned __int64 *)(v_rsi + 232 + result * 8 + 144)) & (*(unsigned __int64 *)(v_rsi + 232 + a1 * 8 + 16));
    v_r13 = 0;
loc_003A62BF:
    if (v_rdi == 0) goto loc_003A6326;
loc_003A62C8:
    if ((unsigned __int8)((unsigned __int8)(v_rdi)) != 0) goto loc_003A62D6;
    v_r13 = (unsigned __int8)((v_r13) + (8));
    v_rdi = (v_rdi) >> (8);
    goto loc_003A62BF;
loc_003A62D6:
    v_r15 = (unsigned int)(((unsigned __int8)(v_r13)) + ((unsigned int)(*(unsigned __int8 *)((unsigned __int8)((unsigned __int8)(v_rdi)) + v_rip - 3753180 * 1))));
    v_stack_p68 = (unsigned int)(*(unsigned __int8 *)((unsigned __int8)((unsigned __int8)(v_rdi)) + v_rip - 3753180 * 1));
    v_r15 = (v_r15) << (4);
    v_r15 = (v_r15) + (*(unsigned __int64 *)(v_rsi + 232 + 8));
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_r15))) != ((unsigned __int16)(*(unsigned __int16 *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 64) + 4)) + *(unsigned __int64 *)(a2 + 64) * 1)))) goto loc_003A6317;
    result = memcmp((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 64) + 4)) + *(unsigned __int64 *)(a2 + 64) * 1, *(unsigned __int64 *)(v_r15), *(unsigned __int8 *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 64) + 4)) + *(unsigned __int64 *)(a2 + 64) * 1 + 1) * 4 + 8, *(unsigned __int16 *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 64) + 4)) + *(unsigned __int64 *)(a2 + 64) * 1));
    if ((unsigned int)(result) == 0) goto loc_003A636A;
loc_003A6317:
    goto loc_003A62C8;
loc_003A6326:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi + 232)))) <= 64) goto loc_003A61EE;
loc_003A633B:
    if (64 >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi + 232))))) goto loc_003A61EE;
    v_r15 = (64) << (4);
    v_r15 = (v_r15) + (*(unsigned __int64 *)(v_rsi + 232 + 8));
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_r15))) == ((unsigned __int16)(v_stack_p50))) goto loc_003A65BF;
loc_003A635E:
    v_rdi = (unsigned int)((64) + 1);
    goto loc_003A633B;
loc_003A6362:
    v_r14 = 0;
    goto loc_003A6264;
loc_003A636A:
loc_003A6370:
    if (v_r15 == (*(unsigned __int64 *)(v_rsi + 232 + 8))) goto loc_003A6558;
loc_003A637D:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_r15 + 8)))) & (4)) == 0) goto loc_003A61EE;
loc_003A6387:
    if ((*(unsigned int *)(v_rsi + 128)) != 0) goto loc_003A647E;
loc_003A6394:
    if ((((unsigned int)((unsigned int)(0x40000ULL))) & ((unsigned int)((unsigned int)(v_stack_pD0)))) == 0) goto loc_003A6611;
    v_stack_p48 = v_stack_p5C;
    v_stack_p40 = v_stack_p60;
    v_stack_p38 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    v_stack_p30 = v_rip - 3754690;
    v_stack_p28 = 0;
    v_stack_p20 = 0;
    result = SeAccessCheck(v_stack_p70, v_stack_pC0, 1, (unsigned int)((unsigned int)((unsigned int)(0x40000ULL))));
    v_rbp = (unsigned int)(v_stack_p58);
    if ((unsigned __int8)(result) == 0) { v_rbp = (unsigned int)((unsigned int)(0x40000ULL)); }
loc_003A6417:
    if (condition_is_above_or_equal) goto loc_003A6477;
    v_stack_p48 = v_stack_p5C;
    v_stack_p40 = v_stack_p60;
    v_stack_p38 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    v_stack_p30 = v_rip - 3754690;
    v_stack_p28 = 0;
    v_stack_p20 = 0;
    result = SeAccessCheck(v_stack_p70, v_stack_pC0, 1, (unsigned int)(0x80000ULL));
    if ((unsigned __int8)(result) == 0) {
    }
    goto loc_003A61F0;
loc_003A647E:
    if ((unsigned int)(v_stack_pD0) + 504 == 0) goto loc_003A6567;
    v_stack_p50 = (unsigned __int16)(*(unsigned __int16 *)((unsigned int)(0x40000ULL)));
    v_stack_p54 = (unsigned int)(*(unsigned __int8 *)((unsigned int)(0x40000ULL) + 1) * 4 + 8);
    result = ((unsigned int)((unsigned int)(*(unsigned __int8 *)((unsigned int)(0x40000ULL) + *(unsigned __int8 *)((unsigned int)(0x40000ULL) + 1) * 4 + 4)))) >> (4);
    a1 = (unsigned int)((*(unsigned __int8 *)((unsigned int)(0x40000ULL) + *(unsigned __int8 *)((unsigned int)(0x40000ULL) + 1) * 4 + 4)) & (15));
    v_rsi = (*(unsigned __int64 *)((unsigned int)(v_stack_pD0) + 504 + result * 8 + 144)) & (*(unsigned __int64 *)((unsigned int)(v_stack_pD0) + 504 + a1 * 8 + 16));
    v_rbp = 0;
loc_003A64C9:
    if (v_rsi == 0) goto loc_003A652E;
loc_003A64D2:
    if ((unsigned __int8)((unsigned __int8)(v_rsi)) != 0) goto loc_003A64E0;
    v_rbp = (unsigned __int8)((v_rbp) + (8));
    v_rsi = (v_rsi) >> (8);
    goto loc_003A64C9;
loc_003A64E0:
    v_rdi = (unsigned int)(((unsigned __int8)(v_rbp)) + ((unsigned int)(*(unsigned __int8 *)((unsigned __int8)((unsigned __int8)(v_rsi)) + v_rip - 3753739 * 1))));
    v_rdi = (v_rdi) << (4);
    v_rdi = (v_rdi) + (*(unsigned __int64 *)((unsigned int)(v_stack_pD0) + 504 + 8));
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rdi))) != ((unsigned __int16)(*(unsigned __int16 *)((unsigned int)(0x40000ULL))))) goto loc_003A6525;
    result = memcmp((unsigned int)(0x40000ULL), *(unsigned __int64 *)(v_rdi), (unsigned int)((unsigned int)(*(unsigned __int8 *)((unsigned int)(0x40000ULL) + 1) * 4 + 8)), *(unsigned __int8 *)((unsigned int)(0x40000ULL) + 1) * 4 + 8);
    if ((unsigned int)(result) == 0) goto loc_003A61D9;
loc_003A6525:
    goto loc_003A64D2;
loc_003A652E:
    if (((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(v_stack_pD0) + 504)))) <= 64) goto loc_003A6567;
loc_003A6536:
    if (64 >= ((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(v_stack_pD0) + 504))))) goto loc_003A6567;
    v_rdi = (64) << (4);
    v_rdi = (v_rdi) + (*(unsigned __int64 *)((unsigned int)(v_stack_pD0) + 504 + 8));
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rdi))) == ((unsigned __int16)(v_stack_p50))) goto loc_003A65DF;
loc_003A6553:
    v_r13 = (unsigned int)((64) + 1);
    goto loc_003A6536;
loc_003A6558:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)((unsigned int)(0x40000ULL))))) & (16)) != 0) goto loc_003A637D;
    goto loc_003A6387;
loc_003A6567:
    result = 0;
    goto loc_003A61E6;
loc_003A656E:
    goto loc_003A6182;
loc_003A6577:
    if (!sign_flag) goto loc_003A6602;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rbp + 12))) == 0) goto loc_003A6634;
loc_003A6590:
    v_stack_p68 = 0;
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rip + 11920686)) == 0) goto loc_003A61EE;
    if ((unsigned int)(*(unsigned int *)(v_rbp + 12)) + v_rbp * 1 == 0) goto loc_003A61EE;
    goto loc_003A620C;
loc_003A65B6:
    goto loc_003A6264;
loc_003A65BF:
    result = memcmp(*(unsigned __int64 *)(v_rbp + 8), *(unsigned __int64 *)(v_rdi), v_stack_p50, (unsigned int)(v_stack_p54));
    if ((unsigned int)(result) == 0) goto loc_003A6370;
    goto loc_003A635E;
loc_003A65DF:
    result = memcmp(*(unsigned __int64 *)(v_rbp + 8), *(unsigned __int64 *)(v_rdi), (unsigned int)((unsigned int)(v_stack_p50)), v_stack_p50);
    if ((unsigned int)(result) == 0) goto loc_003A61D9;
    goto loc_003A6553;
loc_003A6602:
    goto loc_003A6590;
loc_003A6608:
    goto loc_003A612B;
loc_003A6611:
    goto loc_003A6417;
loc_003A661A:
    if (((unsigned __int8)(*(unsigned __int64 *)(v_rbp + 32))) <= 16) goto loc_003A61BA;
loc_003A6623:
    a1 = (unsigned __int8)((*(unsigned __int64 *)(v_rbp + 32)) - (13));
    if (((unsigned __int8)(a1)) <= 1) goto loc_003A617E;
    goto loc_003A61AF;
loc_003A6634:
    a1 = 0;
    goto loc_003A6590;
}
```

## 5. (Beta) C Style

```c
int64_t SeComputeCreatorDeniedRights(void *Arg1, void *Arg2, int32_t Arg3, int64_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint32_t v_stack_m58;
    uint32_t v_stack_m5C;
    uint32_t v_stack_m60;
    uint64_t v_stack_p10;
    uint32_t v_stack_p18;
    uint32_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint8_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint16_t v_stack_p50;
    uint32_t v_stack_p54;
    uint32_t v_stack_p58;
    uint64_t v_stack_p5C;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p8;
    uint64_t v_stack_pC0;
    uint32_t v_stack_pD0;

    v_stack_p10 = local_rbx;
    v_stack_p18 = Arg3;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (128);
    v_stack_m5C = 0;
    v_stack_m60 = 0;
    v_stack_m58 = 0;
    if (((Arg3) & (0xC0000ULL)) == 0) goto loc_003A61EE;
    v_stack_m48 = *(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x30);
    if (*(uint64_t *)(*(uint64_t *)(arg2 + 0x48) + 0x30) != 0) goto loc_003A60FA;
    v_stack_m48 = Arg4;
    if (Arg4 != 0) goto loc_003A60FA;
    v_stack_m48 = *(uint64_t *)(arg2 + 0x40);
    if (*(uint64_t *)(arg2 + 0x40) == 0) goto loc_003A61EE;
loc_003A60FA:
    if ((((uint8_t)(*(uint16_t *)(*(uint64_t *)(arg2 + 0x40) + 0x2))) & (4)) != 0) goto loc_003A6116;
loc_003A6105:
    if ((((uint8_t)(*(uint16_t *)(*(uint64_t *)(arg2 + 0x40) + 0x2))) & (16)) != 0) goto loc_003A6577;
    Arg1 = 0;
    goto loc_003A6590;
loc_003A6116:
    if (!sign_flag) goto loc_003A6608;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x40) + 0x10))) == 0) goto loc_003A6105;
loc_003A612B:
    if ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x40) + 0x10)) + *(uint64_t *)(arg2 + 0x40) * 1 == 0) goto loc_003A6105;
    local_rdi = 0;
loc_003A6148:
    if (0 >= ((uint32_t)(*(uint16_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x40) + 0x10)) + *(uint64_t *)(arg2 + 0x40) * 1 + 0x4)))) goto loc_003A6105;
    if (((*(uint8_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x40) + 0x10)) + *(uint64_t *)(arg2 + 0x40) * 1 + 0x8 + 0x1)) & (8)) != 0) goto loc_003A61AF;
    if (((uint8_t)(*(uint8_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x40) + 0x10)) + *(uint64_t *)(arg2 + 0x40) * 1 + 0x8) - 11)) <= 1) goto loc_003A61BA;
    if (((uint8_t)(*(uint8_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x40) + 0x10)) + *(uint64_t *)(arg2 + 0x40) * 1 + 0x8) - 5)) <= 3) goto loc_003A61BA;
    if (((uint8_t)(*(uint8_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x40) + 0x10)) + *(uint64_t *)(arg2 + 0x40) * 1 + 0x8))) >= 15) goto loc_003A661A;
    if (((uint8_t)(*(uint8_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x40) + 0x10)) + *(uint64_t *)(arg2 + 0x40) * 1 + 0x8))) == 4) goto loc_003A656E;
    if (((uint8_t)(*(uint8_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x40) + 0x10)) + *(uint64_t *)(arg2 + 0x40) * 1 + 0x8))) >= 11) goto loc_003A6623;
loc_003A617E:
loc_003A6182:
    if ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x40) + 0x10)) + *(uint64_t *)(arg2 + 0x40) * 1 + 8 + 8 == 0) goto loc_003A61AF;
    if (((uint16_t)(*(uint16_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x40) + 0x10)) + *(uint64_t *)(arg2 + 0x40) * 1 + 0x8 + 0x8))) != (*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xC3396E) + 0x200)))) goto loc_003A61AF;
    Arg3 = ((uint32_t)((uint32_t)(*(uint16_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x40) + 0x10)) + *(uint64_t *)(arg2 + 0x40) * 1 + 0x8 + 0x8)))) >> (8);
    result = memcmp((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x40) + 0x10)) + *(uint64_t *)(arg2 + 0x40) * 1 + 8 + 8, *(uint64_t *)(*(uint64_t *)(v_rip + 0xC3396E) + 0x200), Arg3 * 4 + 8, Arg4);
    if ((uint32_t)(result) == 0) goto loc_003A623C;
loc_003A61AF:
    local_rdi = (uint32_t)((local_rdi) + 1);
    local_rbx = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x40) + 0x10)) + *(uint64_t *)(arg2 + 0x40) * 1 + 8) + (*(uint16_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x40) + 0x10)) + *(uint64_t *)(arg2 + 0x40) * 1 + 0x8 + 0x2));
    goto loc_003A6148;
loc_003A61BA:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x8))))) & (2));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbx + 0x8))) & (1));
    result = (result) << (3);
    result = (result) | (12);
    Arg1 = (Arg1) << (4);
    result = (result) + (local_rbx);
    Arg1 = (Arg1) + (result);
    goto loc_003A6182;
loc_003A61D9:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x8)))) & (4)) == 0) goto loc_003A6567;
loc_003A61E6:
    if (1 != 0) goto loc_003A6394;
loc_003A61EE:
    result = 0;
loc_003A61F0:
    local_rsp = (local_rsp) + (128);
    return result;
loc_003A620C:
    result = SepGetScopedPolicySid(Arg1, *(uint64_t *)(*(uint64_t *)(v_rip + 0xC3396E) + 0x200), Arg3 * 4 + 8, Arg4);
    if (result == 0) goto loc_003A61EE;
    result = SepRmReferenceFindCap(result, v_stack_p68, Arg3 * 4 + 8, Arg4);
    Arg2 = v_stack_p68;
    if (sign_flag) { Arg2 = *(uint64_t *)(v_rip + 0xC31EBF); }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0x38)))) & (1)) == 0) goto loc_003A61EE;
loc_003A623C:
    local_rsi = *(uint64_t *)(arg1);
    if (*(uint64_t *)(arg1) == 0) {
        local_rsi = *(uint64_t *)(arg1 + 0x10);
    }
    if ((*(uint16_t *)(*(uint64_t *)(arg2 + 0x40) + 0x2)) >= 0) goto loc_003A65B6;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x40) + 0x4))) == 0) goto loc_003A6362;
loc_003A6264:
    if (local_rsi + 232 == 0) goto loc_003A61EE;
    if ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x40) + 0x4)) + *(uint64_t *)(arg2 + 0x40) * 1 == 0) goto loc_003A61EE;
    v_stack_p50 = (uint16_t)(*(uint16_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x40) + 0x4)) + *(uint64_t *)(arg2 + 0x40) * 1));
    v_stack_p54 = (uint32_t)(*(uint8_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x40) + 0x4)) + *(uint64_t *)(arg2 + 0x40) * 1 + 0x1) * 4 + 8);
    Arg1 = (uint32_t)((*(uint8_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x40) + 0x4)) + *(uint64_t *)(arg2 + 0x40) * 1 + *(uint8_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x40) + 0x4)) + *(uint64_t *)(arg2 + 0x40) * 1 + 0x1) * 4 + 0x4)) & (15));
    result = ((uint32_t)((uint32_t)(*(uint8_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x40) + 0x4)) + *(uint64_t *)(arg2 + 0x40) * 1 + *(uint8_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x40) + 0x4)) + *(uint64_t *)(arg2 + 0x40) * 1 + 0x1) * 4 + 0x4)))) >> (4);
    local_rdi = (*(uint64_t *)(local_rsi + 0xE8 + result * 8 + 0x90)) & (*(uint64_t *)(local_rsi + 0xE8 + arg1 * 8 + 0x10));
    local_r13 = 0;
loc_003A62BF:
    if (local_rdi == 0) goto loc_003A6326;
loc_003A62C8:
    if ((uint8_t)((uint8_t)(local_rdi)) != 0) goto loc_003A62D6;
    local_r13 = (uint8_t)((local_r13) + (8));
    local_rdi = (local_rdi) >> (8);
    goto loc_003A62BF;
loc_003A62D6:
    local_r15 = (uint32_t)(((uint8_t)(local_r13)) + ((uint32_t)(*(uint8_t *)((uint8_t)((uint8_t)(local_rdi)) + v_rip - 0x3944DC * 1))));
    v_stack_p68 = (uint32_t)(*(uint8_t *)((uint8_t)((uint8_t)(local_rdi)) + v_rip - 0x3944DC * 1));
    local_r15 = (local_r15) << (4);
    local_r15 = (local_r15) + (*(uint64_t *)(local_rsi + 0xE8 + 0x8));
    if ((*(uint16_t *)(*(uint64_t *)(local_r15))) != ((uint16_t)(*(uint16_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x40) + 0x4)) + *(uint64_t *)(arg2 + 0x40) * 1)))) goto loc_003A6317;
    result = memcmp((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x40) + 0x4)) + *(uint64_t *)(arg2 + 0x40) * 1, *(uint64_t *)(local_r15), *(uint8_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x40) + 0x4)) + *(uint64_t *)(arg2 + 0x40) * 1 + 0x1) * 4 + 8, *(uint16_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x40) + 0x4)) + *(uint64_t *)(arg2 + 0x40) * 1));
    if ((uint32_t)(result) == 0) goto loc_003A636A;
loc_003A6317:
    goto loc_003A62C8;
loc_003A6326:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi + 0xE8)))) <= 64) goto loc_003A61EE;
loc_003A633B:
    if (64 >= ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi + 0xE8))))) goto loc_003A61EE;
    local_r15 = (64) << (4);
    local_r15 = (local_r15) + (*(uint64_t *)(local_rsi + 0xE8 + 0x8));
    if ((*(uint16_t *)(*(uint64_t *)(local_r15))) == ((uint16_t)(v_stack_p50))) goto loc_003A65BF;
loc_003A635E:
    local_rdi = (uint32_t)((64) + 1);
    goto loc_003A633B;
loc_003A6362:
    local_r14 = 0;
    goto loc_003A6264;
loc_003A636A:
loc_003A6370:
    if (local_r15 == (*(uint64_t *)(local_rsi + 0xE8 + 0x8))) goto loc_003A6558;
loc_003A637D:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_r15 + 0x8)))) & (4)) == 0) goto loc_003A61EE;
loc_003A6387:
    if ((*(uint32_t *)(local_rsi + 0x80)) != 0) goto loc_003A647E;
loc_003A6394:
    if ((((uint32_t)((uint32_t)(0x40000ULL))) & ((uint32_t)((uint32_t)(v_stack_pD0)))) == 0) goto loc_003A6611;
    v_stack_p48 = v_stack_p5C;
    v_stack_p40 = v_stack_p60;
    v_stack_p38 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    v_stack_p30 = v_rip - 3754690;
    v_stack_p28 = 0;
    v_stack_p20 = 0;
    result = SeAccessCheck(v_stack_p70, v_stack_pC0, 1, (uint32_t)((uint32_t)((uint32_t)(0x40000ULL))));
    local_rbp = (uint32_t)(v_stack_p58);
    if ((uint8_t)(result) == 0) { local_rbp = (uint32_t)((uint32_t)(0x40000ULL)); }
loc_003A6417:
    if (condition_is_above_or_equal) goto loc_003A6477;
    v_stack_p48 = v_stack_p5C;
    v_stack_p40 = v_stack_p60;
    v_stack_p38 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    v_stack_p30 = v_rip - 3754690;
    v_stack_p28 = 0;
    v_stack_p20 = 0;
    result = SeAccessCheck(v_stack_p70, v_stack_pC0, 1, (uint32_t)(0x80000ULL));
    if ((uint8_t)(result) == 0) {
    }
    goto loc_003A61F0;
loc_003A647E:
    if ((uint32_t)(v_stack_pD0) + 504 == 0) goto loc_003A6567;
    v_stack_p50 = (uint16_t)(*(uint16_t *)((uint32_t)(0x40000ULL)));
    v_stack_p54 = (uint32_t)(*(uint8_t *)((uint32_t)(0x40000ULL) + 0x1) * 4 + 8);
    result = ((uint32_t)((uint32_t)(*(uint8_t *)((uint32_t)(0x40000ULL) + *(uint8_t *)((uint32_t)(0x40000ULL) + 0x1) * 4 + 0x4)))) >> (4);
    Arg1 = (uint32_t)((*(uint8_t *)((uint32_t)(0x40000ULL) + *(uint8_t *)((uint32_t)(0x40000ULL) + 0x1) * 4 + 0x4)) & (15));
    local_rsi = (*(uint64_t *)((uint32_t)(v_stack_pD0) + 0x1F8 + result * 8 + 0x90)) & (*(uint64_t *)((uint32_t)(v_stack_pD0) + 0x1F8 + arg1 * 8 + 0x10));
    local_rbp = 0;
loc_003A64C9:
    if (local_rsi == 0) goto loc_003A652E;
loc_003A64D2:
    if ((uint8_t)((uint8_t)(local_rsi)) != 0) goto loc_003A64E0;
    local_rbp = (uint8_t)((local_rbp) + (8));
    local_rsi = (local_rsi) >> (8);
    goto loc_003A64C9;
loc_003A64E0:
    local_rdi = (uint32_t)(((uint8_t)(local_rbp)) + ((uint32_t)(*(uint8_t *)((uint8_t)((uint8_t)(local_rsi)) + v_rip - 0x39470B * 1))));
    local_rdi = (local_rdi) << (4);
    local_rdi = (local_rdi) + (*(uint64_t *)((uint32_t)(v_stack_pD0) + 0x1F8 + 0x8));
    if ((*(uint16_t *)(*(uint64_t *)(local_rdi))) != ((uint16_t)(*(uint16_t *)((uint32_t)(0x40000ULL))))) goto loc_003A6525;
    result = memcmp((uint32_t)(0x40000ULL), *(uint64_t *)(local_rdi), (uint32_t)((uint32_t)(*(uint8_t *)((uint32_t)(0x40000ULL) + 0x1) * 4 + 8)), *(uint8_t *)((uint32_t)(0x40000ULL) + 0x1) * 4 + 8);
    if ((uint32_t)(result) == 0) goto loc_003A61D9;
loc_003A6525:
    goto loc_003A64D2;
loc_003A652E:
    if (((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(v_stack_pD0) + 0x1F8)))) <= 64) goto loc_003A6567;
loc_003A6536:
    if (64 >= ((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(v_stack_pD0) + 0x1F8))))) goto loc_003A6567;
    local_rdi = (64) << (4);
    local_rdi = (local_rdi) + (*(uint64_t *)((uint32_t)(v_stack_pD0) + 0x1F8 + 0x8));
    if ((*(uint16_t *)(*(uint64_t *)(local_rdi))) == ((uint16_t)(v_stack_p50))) goto loc_003A65DF;
loc_003A6553:
    local_r13 = (uint32_t)((64) + 1);
    goto loc_003A6536;
loc_003A6558:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)((uint32_t)(0x40000ULL))))) & (16)) != 0) goto loc_003A637D;
    goto loc_003A6387;
loc_003A6567:
    result = 0;
    goto loc_003A61E6;
loc_003A656E:
    goto loc_003A6182;
loc_003A6577:
    if (!sign_flag) goto loc_003A6602;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rbp + 0xC))) == 0) goto loc_003A6634;
loc_003A6590:
    v_stack_p68 = 0;
    if ((uint8_t)(*(uint8_t *)(v_rip + 0xB5E52E)) == 0) goto loc_003A61EE;
    if ((uint32_t)(*(uint32_t *)(local_rbp + 0xC)) + local_rbp * 1 == 0) goto loc_003A61EE;
    goto loc_003A620C;
loc_003A65B6:
    goto loc_003A6264;
loc_003A65BF:
    result = memcmp(*(uint64_t *)(local_rbp + 0x8), *(uint64_t *)(local_rdi), v_stack_p50, (uint32_t)(v_stack_p54));
    if ((uint32_t)(result) == 0) goto loc_003A6370;
    goto loc_003A635E;
loc_003A65DF:
    result = memcmp(*(uint64_t *)(local_rbp + 0x8), *(uint64_t *)(local_rdi), (uint32_t)((uint32_t)(v_stack_p50)), v_stack_p50);
    if ((uint32_t)(result) == 0) goto loc_003A61D9;
    goto loc_003A6553;
loc_003A6602:
    goto loc_003A6590;
loc_003A6608:
    goto loc_003A612B;
loc_003A6611:
    goto loc_003A6417;
loc_003A661A:
    if (((uint8_t)(*(uint64_t *)(local_rbp + 0x20))) <= 16) goto loc_003A61BA;
loc_003A6623:
    Arg1 = (uint8_t)((*(uint64_t *)(local_rbp + 0x20)) - (13));
    if (((uint8_t)(Arg1)) <= 1) goto loc_003A617E;
    goto loc_003A61AF;
loc_003A6634:
    Arg1 = 0;
    goto loc_003A6590;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg2` | `+ 0x40` | `64` | `R` |
| `Arg2` | `+ 0x48` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003A6080&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
