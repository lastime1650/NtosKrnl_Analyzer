# RtlFindClearBitsAndSetEx

- RVA: `0x003B60F0`–`0x003B6483` (길이 `915` bytes)
- VA: `0x00000001403B60F0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008C6C0`
- 디코드: `260`개 명령, `915/915` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x003B6144` → [RtlSetBitsEx](RtlSetBitsEx_function_003B6570.md) (function, `0x003B6570`)

### Direct callers
- [RtlpHpFixedVsAllocate](RtlpHpFixedVsAllocate_function_003B47F0.md) at `0x003B4842`
- [ExpSaPageGroupAllocateMemory](ExpSaPageGroupAllocateMemory_function_003B5FF0.md) at `0x003B6061`
- [MiAllocateFromSubAllocatedRegion](../../page/98/MiAllocateFromSubAllocatedRegion_function_00981C24.md) at `0x00981CC9`
- [MiObtainRelocationBits](../../page/98/MiObtainRelocationBits_function_0098997C.md) at `0x00989A02`
- [MiObtainRelocationBits](../../page/98/MiObtainRelocationBits_function_0098997C.md) at `0x00989A8B`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003B60F0  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
003B60F5  48 89 6C 24 18                  mov qword ptr [rsp + 0x18], rbp
003B60FA  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
003B60FF  57                              push rdi
003B6100  41 54                           push r12
003B6102  41 55                           push r13
003B6104  41 56                           push r14
003B6106  41 57                           push r15
003B6108  48 83 EC 20                     sub rsp, 0x20
003B610C  48 8B 29                        mov rbp, qword ptr [rcx]
003B610F  4D 8B E8                        mov r13, r8
003B6112  4C 8B 71 08                     mov r14, qword ptr [rcx + 8]
003B6116  4C 3B C5                        cmp r8, rbp
003B6119  4C 8B DA                        mov r11, rdx
003B611C  4C 8B E1                        mov r12, rcx
003B611F  48 1B DB                        sbb rbx, rbx
003B6122  49 83 CA FF                     or r10, 0xffffffffffffffff
003B6126  49 23 D8                        and rbx, r8
003B6129  4C 8D 4D FF                     lea r9, [rbp - 1]
003B612D  48 85 D2                        test rdx, rdx
003B6130  75 38                           jne 0x1403b616a
003B6132  48 83 E3 F8                     and rbx, 0xfffffffffffffff8
003B6136  49 3B DA                        cmp rbx, r10
003B6139  74 0E                           je 0x1403b6149
003B613B  4D 8B C3                        mov r8, r11
003B613E  48 8B D3                        mov rdx, rbx
003B6141  49 8B CC                        mov rcx, r12
003B6144  E8 27 04 00 00                  call 0x1403b6570
003B6149  48 8B 6C 24 60                  mov rbp, qword ptr [rsp + 0x60]
003B614E  48 8B C3                        mov rax, rbx
003B6151  48 8B 5C 24 58                  mov rbx, qword ptr [rsp + 0x58]
003B6156  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
003B615B  48 83 C4 20                     add rsp, 0x20
003B615F  41 5F                           pop r15
003B6161  41 5E                           pop r14
003B6163  41 5D                           pop r13
003B6165  41 5C                           pop r12
003B6167  5F                              pop rdi
003B6168  C3                              ret
003B6169  CC                              int3
003B616A  4C 8B FB                        mov r15, rbx
003B616D  83 64 24 50 00                  and dword ptr [rsp + 0x50], 0
003B6172  49 8B C1                        mov rax, r9
003B6175  49 2B C7                        sub rax, r15
003B6178  BB 40 00 00 00                  mov ebx, 0x40
003B617D  48 FF C0                        inc rax
003B6180  49 3B C3                        cmp rax, r11
003B6183  72 59                           jb 0x1403b61de
003B6185  49 8B F1                        mov rsi, r9
003B6188  44 8D 43 C1                     lea r8d, [rbx - 0x3f]
003B618C  49 2B F3                        sub rsi, r11
003B618F  41 8A CF                        mov cl, r15b
003B6192  48 FF C6                        inc rsi
003B6195  80 E1 3F                        and cl, 0x3f
003B6198  49 D3 E0                        shl r8, cl
003B619B  48 8B C6                        mov rax, rsi
003B619E  48 C1 E8 06                     shr rax, 6
003B61A2  49 FF C8                        dec r8
003B61A5  49 8D 3C C6                     lea rdi, [r14 + rax*8]
003B61A9  49 8B C7                        mov rax, r15
003B61AC  48 C1 E8 06                     shr rax, 6
003B61B0  49 8D 14 C6                     lea rdx, [r14 + rax*8]
003B61B4  4C 0B 02                        or r8, qword ptr [rdx]
003B61B7  49 83 FB 7F                     cmp r11, 0x7f
003B61BB  0F 87 19 01 00 00               ja 0x1403b62da
003B61C1  4C 3B DB                        cmp r11, rbx
003B61C4  0F 83 CC 00 00 00               jae 0x1403b6296
003B61CA  49 83 FB 01                     cmp r11, 1
003B61CE  77 5D                           ja 0x1403b622d
003B61D0  4D 3B C2                        cmp r8, r10
003B61D3  75 30                           jne 0x1403b6205
003B61D5  48 83 C2 08                     add rdx, 8
003B61D9  48 3B D7                        cmp rdx, rdi
003B61DC  76 22                           jbe 0x1403b6200
003B61DE  49 8B DA                        mov rbx, r10
003B61E1  4D 85 FF                        test r15, r15
003B61E4  0F 84 4C FF FF FF               je 0x1403b6136
003B61EA  4F 8D 0C 2B                     lea r9, [r11 + r13]
003B61EE  4C 3B CD                        cmp r9, rbp
003B61F1  4C 0F 47 CD                     cmova r9, rbp
003B61F5  49 FF C9                        dec r9
003B61F8  45 33 FF                        xor r15d, r15d
003B61FB  E9 6D FF FF FF                  jmp 0x1403b616d
003B6200  4C 8B 02                        mov r8, qword ptr [rdx]
003B6203  EB CB                           jmp 0x1403b61d0
003B6205  49 F7 D0                        not r8
003B6208  48 8B DA                        mov rbx, rdx
003B620B  49 2B DE                        sub rbx, r14
003B620E  48 C1 FB 03                     sar rbx, 3
003B6212  49 0F BC C0                     bsf rax, r8
003B6216  48 C1 E3 06                     shl rbx, 6
003B621A  48 03 D8                        add rbx, rax
003B621D  48 3B DE                        cmp rbx, rsi
003B6220  77 BC                           ja 0x1403b61de
003B6222  49 3B DA                        cmp rbx, r10
003B6225  0F 85 10 FF FF FF               jne 0x1403b613b
003B622B  EB B4                           jmp 0x1403b61e1
003B622D  45 33 D2                        xor r10d, r10d
003B6230  49 C1 E9 06                     shr r9, 6
003B6234  4B 8D 1C CE                     lea rbx, [r14 + r9*8]
003B6238  49 83 F8 FF                     cmp r8, -1
003B623C  74 7B                           je 0x1403b62b9
003B623E  83 64 24 50 00                  and dword ptr [rsp + 0x50], 0
003B6243  B9 40 00 00 00                  mov ecx, 0x40
003B6248  49 0F BC C0                     bsf rax, r8
003B624C  0F 44 C1                        cmove eax, ecx
003B624F  41 8D 0C 02                     lea ecx, [r10 + rax]
003B6253  49 3B CB                        cmp rcx, r11
003B6256  73 59                           jae 0x1403b62b1
003B6258  4D 8B C8                        mov r9, r8
003B625B  45 8B D3                        mov r10d, r11d
003B625E  49 F7 D1                        not r9
003B6261  49 8B C1                        mov rax, r9
003B6264  41 8B CA                        mov ecx, r10d
003B6267  D1 E9                           shr ecx, 1
003B6269  48 D3 E8                        shr rax, cl
003B626C  4C 23 C8                        and r9, rax
003B626F  0F 84 43 01 00 00               je 0x1403b63b8
003B6275  44 2B D1                        sub r10d, ecx
003B6278  41 83 FA 01                     cmp r10d, 1
003B627C  77 E3                           ja 0x1403b6261
003B627E  49 0F BC D9                     bsf rbx, r9
003B6282  49 2B D6                        sub rdx, r14
003B6285  48 C1 FA 03                     sar rdx, 3
003B6289  48 C1 E2 06                     shl rdx, 6
003B628D  48 03 DA                        add rbx, rdx
003B6290  49 83 CA FF                     or r10, 0xffffffffffffffff
003B6294  EB 87                           jmp 0x1403b621d
003B6296  4D 85 C0                        test r8, r8
003B6299  0F 89 4F 01 00 00               jns 0x1403b63ee
003B629F  48 83 C2 08                     add rdx, 8
003B62A3  48 3B D7                        cmp rdx, rdi
003B62A6  0F 87 32 FF FF FF               ja 0x1403b61de
003B62AC  4C 8B 02                        mov r8, qword ptr [rdx]
003B62AF  EB E5                           jmp 0x1403b6296
003B62B1  41 8B DA                        mov ebx, r10d
003B62B4  48 F7 DB                        neg rbx
003B62B7  EB C9                           jmp 0x1403b6282
003B62B9  49 83 CA FF                     or r10, 0xffffffffffffffff
003B62BD  48 83 C2 08                     add rdx, 8
003B62C1  48 3B D7                        cmp rdx, rdi
003B62C4  0F 87 14 FF FF FF               ja 0x1403b61de
003B62CA  4C 8B 02                        mov r8, qword ptr [rdx]
003B62CD  4D 3B C2                        cmp r8, r10
003B62D0  74 EB                           je 0x1403b62bd
003B62D2  45 33 D2                        xor r10d, r10d
003B62D5  E9 64 FF FF FF                  jmp 0x1403b623e
003B62DA  40 F6 C6 3F                     test sil, 0x3f
003B62DE  4C 8D 4F 08                     lea r9, [rdi + 8]
003B62E2  4C 0F 44 CF                     cmove r9, rdi
003B62E6  4D 85 C0                        test r8, r8
003B62E9  0F 84 C2 00 00 00               je 0x1403b63b1
003B62EF  48 83 C2 08                     add rdx, 8
003B62F3  48 83 3A 00                     cmp qword ptr [rdx], 0
003B62F7  75 55                           jne 0x1403b634e
003B62F9  83 64 24 50 00                  and dword ptr [rsp + 0x50], 0
003B62FE  49 0F BD C0                     bsr rax, r8
003B6302  0F 84 70 01 00 00               je 0x1403b6478
003B6308  B9 3F 00 00 00                  mov ecx, 0x3f
003B630D  2B C8                           sub ecx, eax
003B630F  48 8B DA                        mov rbx, rdx
003B6312  44 8B C1                        mov r8d, ecx
003B6315  49 2B DE                        sub rbx, r14
003B6318  48 C1 FB 03                     sar rbx, 3
003B631C  48 C1 E3 06                     shl rbx, 6
003B6320  49 2B D8                        sub rbx, r8
003B6323  48 3B DE                        cmp rbx, rsi
003B6326  0F 87 B2 FE FF FF               ja 0x1403b61de
003B632C  49 8B C3                        mov rax, r11
003B632F  49 2B C0                        sub rax, r8
003B6332  48 C1 E8 06                     shr rax, 6
003B6336  4C 8D 04 C2                     lea r8, [rdx + rax*8]
003B633A  48 83 C2 08                     add rdx, 8
003B633E  49 3B D0                        cmp rdx, r8
003B6341  74 3D                           je 0x1403b6380
003B6343  48 83 3A 00                     cmp qword ptr [rdx], 0
003B6347  74 F1                           je 0x1403b633a
003B6349  BB 40 00 00 00                  mov ebx, 0x40
003B634E  48 8B C2                        mov rax, rdx
003B6351  49 3B D1                        cmp rdx, r9
003B6354  0F 87 84 FE FF FF               ja 0x1403b61de
003B635A  48 83 C2 08                     add rdx, 8
003B635E  48 83 3A 00                     cmp qword ptr [rdx], 0
003B6362  75 EA                           jne 0x1403b634e
003B6364  48 8B 00                        mov rax, qword ptr [rax]
003B6367  83 64 24 50 00                  and dword ptr [rsp + 0x50], 0
003B636C  4C 0F BD C0                     bsr r8, rax
003B6370  0F 84 02 01 00 00               je 0x1403b6478
003B6376  B9 3F 00 00 00                  mov ecx, 0x3f
003B637B  41 2B C8                        sub ecx, r8d
003B637E  EB 8F                           jmp 0x1403b630f
003B6380  45 8B C3                        mov r8d, r11d
003B6383  44 2B C1                        sub r8d, ecx
003B6386  41 83 E0 3F                     and r8d, 0x3f
003B638A  0F 84 92 FE FF FF               je 0x1403b6222
003B6390  83 64 24 50 00                  and dword ptr [rsp + 0x50], 0
003B6395  48 8B 02                        mov rax, qword ptr [rdx]
003B6398  48 0F BC C8                     bsf rcx, rax
003B639C  B8 40 00 00 00                  mov eax, 0x40
003B63A1  0F 44 C8                        cmove ecx, eax
003B63A4  41 3B C8                        cmp ecx, r8d
003B63A7  0F 83 75 FE FF FF               jae 0x1403b6222
003B63AD  8B D8                           mov ebx, eax
003B63AF  EB 9D                           jmp 0x1403b634e
003B63B1  33 C9                           xor ecx, ecx
003B63B3  E9 57 FF FF FF                  jmp 0x1403b630f
003B63B8  48 3B D3                        cmp rdx, rbx
003B63BB  74 20                           je 0x1403b63dd
003B63BD  83 64 24 50 00                  and dword ptr [rsp + 0x50], 0
003B63C2  49 0F BD C0                     bsr rax, r8
003B63C6  74 1E                           je 0x1403b63e6
003B63C8  41 BA 3F 00 00 00               mov r10d, 0x3f
003B63CE  44 2B D0                        sub r10d, eax
003B63D1  48 83 C2 08                     add rdx, 8
003B63D5  4C 8B 02                        mov r8, qword ptr [rdx]
003B63D8  E9 5B FE FF FF                  jmp 0x1403b6238
003B63DD  49 83 CA FF                     or r10, 0xffffffffffffffff
003B63E1  E9 F8 FD FF FF                  jmp 0x1403b61de
003B63E6  41 BA 40 00 00 00               mov r10d, 0x40
003B63EC  EB E3                           jmp 0x1403b63d1
003B63EE  83 64 24 50 00                  and dword ptr [rsp + 0x50], 0
003B63F3  49 0F BD C8                     bsr rcx, r8
003B63F7  0F 84 82 00 00 00               je 0x1403b647f
003B63FD  B8 3F 00 00 00                  mov eax, 0x3f
003B6402  2B C1                           sub eax, ecx
003B6404  48 8B DA                        mov rbx, rdx
003B6407  44 8B C0                        mov r8d, eax
003B640A  49 2B DE                        sub rbx, r14
003B640D  48 C1 FB 03                     sar rbx, 3
003B6411  48 FF C3                        inc rbx
003B6414  48 C1 E3 06                     shl rbx, 6
003B6418  49 2B D8                        sub rbx, r8
003B641B  48 3B DE                        cmp rbx, rsi
003B641E  0F 87 BA FD FF FF               ja 0x1403b61de
003B6424  49 8B CB                        mov rcx, r11
003B6427  49 2B C8                        sub rcx, r8
003B642A  0F 84 F2 FD FF FF               je 0x1403b6222
003B6430  48 83 C2 08                     add rdx, 8
003B6434  41 B9 40 00 00 00               mov r9d, 0x40
003B643A  48 8B 02                        mov rax, qword ptr [rdx]
003B643D  4C 8B C0                        mov r8, rax
003B6440  49 3B C9                        cmp rcx, r9
003B6443  72 15                           jb 0x1403b645a
003B6445  48 85 C0                        test rax, rax
003B6448  75 26                           jne 0x1403b6470
003B644A  49 2B C9                        sub rcx, r9
003B644D  0F 84 CF FD FF FF               je 0x1403b6222
003B6453  48 83 C2 08                     add rdx, 8
003B6457  4C 8B 02                        mov r8, qword ptr [rdx]
003B645A  83 64 24 50 00                  and dword ptr [rsp + 0x50], 0
003B645F  49 0F BC C0                     bsf rax, r8
003B6463  41 0F 44 C1                     cmove eax, r9d
003B6467  48 3B C1                        cmp rax, rcx
003B646A  0F 83 B2 FD FF FF               jae 0x1403b6222
003B6470  49 8B D9                        mov rbx, r9
003B6473  E9 1E FE FF FF                  jmp 0x1403b6296
003B6478  8B CB                           mov ecx, ebx
003B647A  E9 90 FE FF FF                  jmp 0x1403b630f
003B647F  8B C3                           mov eax, ebx
003B6481  EB 81                           jmp 0x1403b6404
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlFindClearBitsAndSetEx(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p50;

    v_stack_p10 = v_rbx;
    v_stack_p18 = v_rbp;
    v_stack_p20 = v_rsi;
    v_rsp = (v_rsp) - (32);
    v_r10 = (v_r10) | (-1);
    v_rbx = (v_rbx) & (a3);
    if (a2 != 0) goto loc_003B616A;
    v_rbx = (v_rbx) & (-8);
loc_003B6136:
    if (v_rbx != v_r10) {
        a3 = a2;
        a2 = v_rbx;
        a1 = a1;
        result = RtlSetBitsEx(a1, a2, a3, *(unsigned __int64 *)(a1) - 1);
    }
    v_rsp = (v_rsp) + (32);
    return v_rbx;
loc_003B616A:
loc_003B616D:
    result = (*(unsigned __int64 *)(a1) - 1) - (v_stack_p10);
    result = (result) + 1;
    if (result < a2) goto loc_003B61DE;
    v_rsi = (*(unsigned __int64 *)(a1) - 1) - (a2);
    v_rsi = (v_rsi) + 1;
    a1 = (unsigned __int8)(((unsigned __int8)(v_stack_p10)) & (63));
    a3 = (64 - 63) << ((unsigned __int8)(a1));
    result = (v_rsi) >> (6);
    a3 = (a3) - 1;
    result = (v_stack_p10) >> (6);
    a3 = (a3) | (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + result * 8));
    if (a2 > 127) goto loc_003B62DA;
    if (a2 >= 64) goto loc_003B6296;
    if (a2 > 1) goto loc_003B622D;
loc_003B61D0:
    if (a3 != v_r10) goto loc_003B6205;
    a2 = (*(unsigned __int64 *)(a1 + 8) + result * 8) + (8);
    if (a2 <= (*(unsigned __int64 *)(a1 + 8) + result * 8)) goto loc_003B6200;
loc_003B61DE:
loc_003B61E1:
    if (v_stack_p10 == 0) goto loc_003B6136;
    a4 = a2 + a3 * 1;
    if ((a2 + a3 * 1) > v_stack_p18) { a4 = v_stack_p18; }
    a4 = (a4) - 1;
    v_r15 = 0;
    goto loc_003B616D;
loc_003B6200:
    goto loc_003B61D0;
loc_003B6205:
    a3 = ~(*(unsigned __int64 *)(a2));
    v_rbx = (a2) - (*(unsigned __int64 *)(a1 + 8));
    v_rbx = (v_rbx) >> (3);
    v_rbx = (v_rbx) << (6);
    v_rbx = (v_rbx) + (result);
loc_003B621D:
    if (v_rbx > v_rsi) goto loc_003B61DE;
loc_003B6222:
    if (v_rbx != v_r10) goto loc_003B613B;
    goto loc_003B61E1;
loc_003B622D:
    v_r10 = 0;
    a4 = (a4) >> (6);
loc_003B6238:
    if (a3 == -1) goto loc_003B62B9;
loc_003B623E:
    if (a3 == -1) { result = 64; }
    if ((v_r10 + result * 1) >= a2) goto loc_003B62B1;
    a4 = ~(a3);
loc_003B6261:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a2))))) >> (1));
    result = (a4) >> ((unsigned __int8)(a1));
    a4 = (a4) & (result);
    if (condition_is_equal) goto loc_003B63B8;
    v_r10 = (unsigned int)(((unsigned int)((unsigned int)(a2))) - ((unsigned int)(a1)));
    if (((unsigned int)(v_r10)) > 1) goto loc_003B6261;
loc_003B6282:
    a2 = (a2) - (*(unsigned __int64 *)(a1 + 8));
    a2 = (a2) >> (3);
    a2 = (a2) << (6);
    v_rbx = (*(unsigned __int64 *)(a1 + 8) + a4 * 8) + (a2);
    v_r10 = (v_r10) | (-1);
    goto loc_003B621D;
loc_003B6296:
    if (!sign_flag) goto loc_003B63EE;
    a2 = (a2) + (8);
    if (a2 > (*(unsigned __int64 *)(a1 + 8) + result * 8)) goto loc_003B61DE;
    goto loc_003B6296;
loc_003B62B1:
    v_rbx = -((unsigned int)((unsigned int)(v_r10)));
    goto loc_003B6282;
loc_003B62B9:
    v_r10 = (v_r10) | (-1);
loc_003B62BD:
    a2 = (a2) + (8);
    if (a2 > (*(unsigned __int64 *)(a1 + 8) + result * 8)) goto loc_003B61DE;
    if ((*(unsigned __int64 *)(a2)) == v_r10) goto loc_003B62BD;
    v_r10 = 0;
    goto loc_003B623E;
loc_003B62DA:
    a4 = *(unsigned __int64 *)(a1 + 8) + result * 8 + 8;
    if ((((unsigned __int8)(v_rsi)) & (63)) == 0) { a4 = *(unsigned __int64 *)(a1 + 8) + result * 8; }
    if (*(unsigned __int64 *)(a2) == 0) goto loc_003B63B1;
    a2 = (a2) + (8);
    if ((*(unsigned __int64 *)(a2)) != 0) goto loc_003B634E;
    if ((*(unsigned __int64 *)(a2)) == 0) goto loc_003B6478;
    a1 = (unsigned int)((63) - ((unsigned int)(result)));
loc_003B630F:
    v_rbx = (a2) - (*(unsigned __int64 *)(a1 + 8));
    v_rbx = (v_rbx) >> (3);
    v_rbx = (v_rbx) << (6);
    v_rbx = (v_rbx) - ((unsigned int)((unsigned int)(a1)));
    if (v_rbx > v_rsi) goto loc_003B61DE;
    result = (a2) - ((unsigned int)((unsigned int)(a1)));
    result = (result) >> (6);
loc_003B633A:
    a2 = (a2) + (8);
    if (a2 == (a2 + result * 8)) goto loc_003B6380;
    if ((*(unsigned __int64 *)(a2)) == 0) goto loc_003B633A;
loc_003B634E:
    if (a2 > a4) goto loc_003B61DE;
    a2 = (a2) + (8);
    if ((*(unsigned __int64 *)(a2)) != 0) goto loc_003B634E;
    if ((*(unsigned __int64 *)(a2)) == 0) goto loc_003B6478;
    a1 = (unsigned int)((63) - ((unsigned int)(a2 + result * 8)));
    goto loc_003B630F;
loc_003B6380:
    a3 = (unsigned int)(((unsigned int)((unsigned int)(a2))) - ((unsigned int)(a1)));
    a3 = (unsigned int)((a3) & (63));
    if (condition_is_equal) goto loc_003B6222;
    if (condition_is_equal) { a1 = 64; }
    if (((unsigned int)(a1)) >= ((unsigned int)(a3))) goto loc_003B6222;
    goto loc_003B634E;
loc_003B63B1:
    a1 = 0;
    goto loc_003B630F;
loc_003B63B8:
    if (a2 == 64) goto loc_003B63DD;
    if (a2 == 64) goto loc_003B63E6;
    v_r10 = (unsigned int)((63) - (64));
loc_003B63D1:
    a2 = (a2) + (8);
    goto loc_003B6238;
loc_003B63DD:
    v_r10 = (v_r10) | (-1);
    goto loc_003B61DE;
loc_003B63E6:
    goto loc_003B63D1;
loc_003B63EE:
    if (condition_is_equal) goto loc_003B647F;
    result = (unsigned int)((63) - (0));
loc_003B6404:
    v_rbx = (a2) - (*(unsigned __int64 *)(a1 + 8));
    v_rbx = (v_rbx) >> (3);
    v_rbx = (v_rbx) + 1;
    v_rbx = (v_rbx) << (6);
    v_rbx = (v_rbx) - ((unsigned int)((unsigned int)(result)));
    if (v_rbx > v_rsi) goto loc_003B61DE;
    a1 = (a2) - ((unsigned int)((unsigned int)(result)));
    if (condition_is_equal) goto loc_003B6222;
    a2 = (a2) + (8);
    if (a1 < 64) goto loc_003B645A;
    if (*(unsigned __int64 *)(a2) != 0) goto loc_003B6470;
    a1 = (a1) - (64);
    if (condition_is_equal) goto loc_003B6222;
    a2 = (a2) + (8);
loc_003B645A:
    result = *(unsigned __int64 *)(a2);
    if (condition_is_equal) { result = 64; }
    if (result >= a1) goto loc_003B6222;
loc_003B6470:
    goto loc_003B6296;
loc_003B6478:
    goto loc_003B630F;
loc_003B647F:
    goto loc_003B6404;
}
```

## 5. (Beta) C Style

```c
int64_t RtlFindClearBitsAndSetEx(void *Arg1, int64_t Arg2, int64_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint32_t v_stack_p50;

    v_stack_p10 = local_rbx;
    v_stack_p18 = local_rbp;
    v_stack_p20 = local_rsi;
    local_rsp = (local_rsp) - (32);
    local_r10 = (local_r10) | (-1);
    local_rbx = (local_rbx) & (Arg3);
    if (Arg2 != 0) goto loc_003B616A;
    local_rbx = (local_rbx) & (-8);
loc_003B6136:
    if (local_rbx != local_r10) {
        Arg3 = Arg2;
        Arg2 = local_rbx;
        Arg1 = Arg1;
        result = RtlSetBitsEx(Arg1, Arg2, Arg3, *(uint64_t *)(arg1) - 1);
    }
    local_rsp = (local_rsp) + (32);
    return local_rbx;
loc_003B616A:
loc_003B616D:
    result = (*(uint64_t *)(arg1) - 1) - (v_stack_p10);
    result = (result) + 1;
    if (result < Arg2) goto loc_003B61DE;
    local_rsi = (*(uint64_t *)(arg1) - 1) - (Arg2);
    local_rsi = (local_rsi) + 1;
    Arg1 = (uint8_t)(((uint8_t)(v_stack_p10)) & (63));
    Arg3 = (64 - 63) << ((uint8_t)(Arg1));
    result = (local_rsi) >> (6);
    Arg3 = (Arg3) - 1;
    result = (v_stack_p10) >> (6);
    Arg3 = (Arg3) | (*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + result * 8));
    if (Arg2 > 127) goto loc_003B62DA;
    if (Arg2 >= 64) goto loc_003B6296;
    if (Arg2 > 1) goto loc_003B622D;
loc_003B61D0:
    if (Arg3 != local_r10) goto loc_003B6205;
    Arg2 = (*(uint64_t *)(arg1 + 0x8) + result * 8) + (8);
    if (Arg2 <= (*(uint64_t *)(arg1 + 0x8) + result * 8)) goto loc_003B6200;
loc_003B61DE:
loc_003B61E1:
    if (v_stack_p10 == 0) goto loc_003B6136;
    a4 = Arg2 + Arg3 * 1;
    if ((Arg2 + Arg3 * 1) > v_stack_p18) { a4 = v_stack_p18; }
    a4 = (a4) - 1;
    local_r15 = 0;
    goto loc_003B616D;
loc_003B6200:
    goto loc_003B61D0;
loc_003B6205:
    Arg3 = ~(*(uint64_t *)(Arg2));
    local_rbx = (Arg2) - (*(uint64_t *)(arg1 + 0x8));
    local_rbx = (local_rbx) >> (3);
    local_rbx = (local_rbx) << (6);
    local_rbx = (local_rbx) + (result);
loc_003B621D:
    if (local_rbx > local_rsi) goto loc_003B61DE;
loc_003B6222:
    if (local_rbx != local_r10) goto loc_003B613B;
    goto loc_003B61E1;
loc_003B622D:
    local_r10 = 0;
    a4 = (a4) >> (6);
loc_003B6238:
    if (Arg3 == -1) goto loc_003B62B9;
loc_003B623E:
    if (Arg3 == -1) { result = 64; }
    if ((local_r10 + result * 1) >= Arg2) goto loc_003B62B1;
    a4 = ~(Arg3);
loc_003B6261:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg2))))) >> (1));
    result = (a4) >> ((uint8_t)(Arg1));
    a4 = (a4) & (result);
    if (condition_is_equal) goto loc_003B63B8;
    local_r10 = (uint32_t)(((uint32_t)((uint32_t)(Arg2))) - ((uint32_t)(Arg1)));
    if (((uint32_t)(local_r10)) > 1) goto loc_003B6261;
loc_003B6282:
    Arg2 = (Arg2) - (*(uint64_t *)(arg1 + 0x8));
    Arg2 = (Arg2) >> (3);
    Arg2 = (Arg2) << (6);
    local_rbx = (*(uint64_t *)(arg1 + 0x8) + a4 * 8) + (Arg2);
    local_r10 = (local_r10) | (-1);
    goto loc_003B621D;
loc_003B6296:
    if (!sign_flag) goto loc_003B63EE;
    Arg2 = (Arg2) + (8);
    if (Arg2 > (*(uint64_t *)(arg1 + 0x8) + result * 8)) goto loc_003B61DE;
    goto loc_003B6296;
loc_003B62B1:
    local_rbx = -((uint32_t)((uint32_t)(local_r10)));
    goto loc_003B6282;
loc_003B62B9:
    local_r10 = (local_r10) | (-1);
loc_003B62BD:
    Arg2 = (Arg2) + (8);
    if (Arg2 > (*(uint64_t *)(arg1 + 0x8) + result * 8)) goto loc_003B61DE;
    if ((*(uint64_t *)(Arg2)) == local_r10) goto loc_003B62BD;
    local_r10 = 0;
    goto loc_003B623E;
loc_003B62DA:
    a4 = *(uint64_t *)(arg1 + 0x8) + result * 8 + 8;
    if ((((uint8_t)(local_rsi)) & (63)) == 0) { a4 = *(uint64_t *)(arg1 + 0x8) + result * 8; }
    if (*(uint64_t *)(Arg2) == 0) goto loc_003B63B1;
    Arg2 = (Arg2) + (8);
    if ((*(uint64_t *)(Arg2)) != 0) goto loc_003B634E;
    if ((*(uint64_t *)(Arg2)) == 0) goto loc_003B6478;
    Arg1 = (uint32_t)((63) - ((uint32_t)(result)));
loc_003B630F:
    local_rbx = (Arg2) - (*(uint64_t *)(arg1 + 0x8));
    local_rbx = (local_rbx) >> (3);
    local_rbx = (local_rbx) << (6);
    local_rbx = (local_rbx) - ((uint32_t)((uint32_t)(Arg1)));
    if (local_rbx > local_rsi) goto loc_003B61DE;
    result = (Arg2) - ((uint32_t)((uint32_t)(Arg1)));
    result = (result) >> (6);
loc_003B633A:
    Arg2 = (Arg2) + (8);
    if (Arg2 == (Arg2 + result * 8)) goto loc_003B6380;
    if ((*(uint64_t *)(Arg2)) == 0) goto loc_003B633A;
loc_003B634E:
    if (Arg2 > a4) goto loc_003B61DE;
    Arg2 = (Arg2) + (8);
    if ((*(uint64_t *)(Arg2)) != 0) goto loc_003B634E;
    if ((*(uint64_t *)(Arg2)) == 0) goto loc_003B6478;
    Arg1 = (uint32_t)((63) - ((uint32_t)(Arg2 + result * 8)));
    goto loc_003B630F;
loc_003B6380:
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(Arg2))) - ((uint32_t)(Arg1)));
    Arg3 = (uint32_t)((Arg3) & (63));
    if (condition_is_equal) goto loc_003B6222;
    if (condition_is_equal) { Arg1 = 64; }
    if (((uint32_t)(Arg1)) >= ((uint32_t)(Arg3))) goto loc_003B6222;
    goto loc_003B634E;
loc_003B63B1:
    Arg1 = 0;
    goto loc_003B630F;
loc_003B63B8:
    if (Arg2 == 64) goto loc_003B63DD;
    if (Arg2 == 64) goto loc_003B63E6;
    local_r10 = (uint32_t)((63) - (64));
loc_003B63D1:
    Arg2 = (Arg2) + (8);
    goto loc_003B6238;
loc_003B63DD:
    local_r10 = (local_r10) | (-1);
    goto loc_003B61DE;
loc_003B63E6:
    goto loc_003B63D1;
loc_003B63EE:
    if (condition_is_equal) goto loc_003B647F;
    result = (uint32_t)((63) - (0));
loc_003B6404:
    local_rbx = (Arg2) - (*(uint64_t *)(arg1 + 0x8));
    local_rbx = (local_rbx) >> (3);
    local_rbx = (local_rbx) + 1;
    local_rbx = (local_rbx) << (6);
    local_rbx = (local_rbx) - ((uint32_t)((uint32_t)(result)));
    if (local_rbx > local_rsi) goto loc_003B61DE;
    Arg1 = (Arg2) - ((uint32_t)((uint32_t)(result)));
    if (condition_is_equal) goto loc_003B6222;
    Arg2 = (Arg2) + (8);
    if (Arg1 < 64) goto loc_003B645A;
    if (*(uint64_t *)(Arg2) != 0) goto loc_003B6470;
    Arg1 = (Arg1) - (64);
    if (condition_is_equal) goto loc_003B6222;
    Arg2 = (Arg2) + (8);
loc_003B645A:
    result = *(uint64_t *)(Arg2);
    if (condition_is_equal) { result = 64; }
    if (result >= Arg1) goto loc_003B6222;
loc_003B6470:
    goto loc_003B6296;
loc_003B6478:
    goto loc_003B630F;
loc_003B647F:
    goto loc_003B6404;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003B60F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
