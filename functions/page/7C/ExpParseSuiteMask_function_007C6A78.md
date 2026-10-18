# ExpParseSuiteMask

- RVA: `0x007C6A78`–`0x007C6D9B` (길이 `803` bytes)
- VA: `0x00000001407C6A78`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `238`개 명령, `803/803` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **16**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [ExGetSuiteMask](ExGetSuiteMask_function_007C68D0.md) at `0x007C68E9`

### Static image references
- `0x007C6A8B` → RVA `0x00B4ADB8` (`PAGE`; read)
- `0x007C6ABA` → RVA `0x00B4ADD8` (`PAGE`; read)
- `0x007C6AE9` → RVA `0x00B4ADC0` (`PAGE`; read)
- `0x007C6B18` → RVA `0x00B4ADC8` (`PAGE`; read)
- `0x007C6B47` → RVA `0x00B4ADD0` (`PAGE`; read)
- `0x007C6B76` → RVA `0x00B4ADE0` (`PAGE`; read)
- `0x007C6BA5` → RVA `0x00B4ADE8` (`PAGE`; read)
- `0x007C6BD4` → RVA `0x00B4ADF0` (`PAGE`; read)
- `0x007C6C04` → RVA `0x00B4ADF8` (`PAGE`; read)
- `0x007C6C34` → RVA `0x00B4AE00` (`PAGE`; read)
- `0x007C6C64` → RVA `0x00B4AE08` (`PAGE`; read)
- `0x007C6C94` → RVA `0x00B4AE10` (`PAGE`; read)
- `0x007C6CC4` → RVA `0x00B4AE18` (`PAGE`; read)
- `0x007C6CF4` → RVA `0x00B4AE20` (`PAGE`; read)
- `0x007C6D21` → RVA `0x00B4AE28` (`PAGE`; read)
- `0x007C6D4E` → RVA `0x00B4AE38` (`PAGE`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007C6A78  45 33 DB                        xor r11d, r11d
007C6A7B  4C 8B D1                        mov r10, rcx
007C6A7E  41 8B C3                        mov eax, r11d
007C6A81  66 44 39 19                     cmp word ptr [rcx], r11w
007C6A85  0F 84 0E 03 00 00               je 0x1407c6d99
007C6A8B  4C 8B 0D 26 43 38 00            mov r9, qword ptr [rip + 0x384326]
007C6A92  49 8B CA                        mov rcx, r10
007C6A95  4D 2B CA                        sub r9, r10
007C6A98  0F B7 11                        movzx edx, word ptr [rcx]
007C6A9B  46 0F B7 04 09                  movzx r8d, word ptr [rcx + r9]
007C6AA0  41 2B D0                        sub edx, r8d
007C6AA3  75 09                           jne 0x1407c6aae
007C6AA5  48 83 C1 02                     add rcx, 2
007C6AA9  45 85 C0                        test r8d, r8d
007C6AAC  75 EA                           jne 0x1407c6a98
007C6AAE  85 D2                           test edx, edx
007C6AB0  75 08                           jne 0x1407c6aba
007C6AB2  83 C8 01                        or eax, 1
007C6AB5  E9 BF 02 00 00                  jmp 0x1407c6d79
007C6ABA  4C 8B 0D 17 43 38 00            mov r9, qword ptr [rip + 0x384317]
007C6AC1  49 8B CA                        mov rcx, r10
007C6AC4  4D 2B CA                        sub r9, r10
007C6AC7  0F B7 11                        movzx edx, word ptr [rcx]
007C6ACA  46 0F B7 04 09                  movzx r8d, word ptr [rcx + r9]
007C6ACF  41 2B D0                        sub edx, r8d
007C6AD2  75 09                           jne 0x1407c6add
007C6AD4  48 83 C1 02                     add rcx, 2
007C6AD8  45 85 C0                        test r8d, r8d
007C6ADB  75 EA                           jne 0x1407c6ac7
007C6ADD  85 D2                           test edx, edx
007C6ADF  75 08                           jne 0x1407c6ae9
007C6AE1  83 C8 20                        or eax, 0x20
007C6AE4  E9 90 02 00 00                  jmp 0x1407c6d79
007C6AE9  4C 8B 0D D0 42 38 00            mov r9, qword ptr [rip + 0x3842d0]
007C6AF0  49 8B CA                        mov rcx, r10
007C6AF3  4D 2B CA                        sub r9, r10
007C6AF6  0F B7 11                        movzx edx, word ptr [rcx]
007C6AF9  46 0F B7 04 09                  movzx r8d, word ptr [rcx + r9]
007C6AFE  41 2B D0                        sub edx, r8d
007C6B01  75 09                           jne 0x1407c6b0c
007C6B03  48 83 C1 02                     add rcx, 2
007C6B07  45 85 C0                        test r8d, r8d
007C6B0A  75 EA                           jne 0x1407c6af6
007C6B0C  85 D2                           test edx, edx
007C6B0E  75 08                           jne 0x1407c6b18
007C6B10  83 C8 02                        or eax, 2
007C6B13  E9 61 02 00 00                  jmp 0x1407c6d79
007C6B18  4C 8B 0D A9 42 38 00            mov r9, qword ptr [rip + 0x3842a9]
007C6B1F  49 8B CA                        mov rcx, r10
007C6B22  4D 2B CA                        sub r9, r10
007C6B25  0F B7 11                        movzx edx, word ptr [rcx]
007C6B28  46 0F B7 04 09                  movzx r8d, word ptr [rcx + r9]
007C6B2D  41 2B D0                        sub edx, r8d
007C6B30  75 09                           jne 0x1407c6b3b
007C6B32  48 83 C1 02                     add rcx, 2
007C6B36  45 85 C0                        test r8d, r8d
007C6B39  75 EA                           jne 0x1407c6b25
007C6B3B  85 D2                           test edx, edx
007C6B3D  75 08                           jne 0x1407c6b47
007C6B3F  83 C8 08                        or eax, 8
007C6B42  E9 32 02 00 00                  jmp 0x1407c6d79
007C6B47  4C 8B 0D 82 42 38 00            mov r9, qword ptr [rip + 0x384282]
007C6B4E  49 8B CA                        mov rcx, r10
007C6B51  4D 2B CA                        sub r9, r10
007C6B54  0F B7 11                        movzx edx, word ptr [rcx]
007C6B57  46 0F B7 04 09                  movzx r8d, word ptr [rcx + r9]
007C6B5C  41 2B D0                        sub edx, r8d
007C6B5F  75 09                           jne 0x1407c6b6a
007C6B61  48 83 C1 02                     add rcx, 2
007C6B65  45 85 C0                        test r8d, r8d
007C6B68  75 EA                           jne 0x1407c6b54
007C6B6A  85 D2                           test edx, edx
007C6B6C  75 08                           jne 0x1407c6b76
007C6B6E  83 C8 04                        or eax, 4
007C6B71  E9 03 02 00 00                  jmp 0x1407c6d79
007C6B76  4C 8B 0D 63 42 38 00            mov r9, qword ptr [rip + 0x384263]
007C6B7D  49 8B CA                        mov rcx, r10
007C6B80  4D 2B CA                        sub r9, r10
007C6B83  0F B7 11                        movzx edx, word ptr [rcx]
007C6B86  46 0F B7 04 09                  movzx r8d, word ptr [rcx + r9]
007C6B8B  41 2B D0                        sub edx, r8d
007C6B8E  75 09                           jne 0x1407c6b99
007C6B90  48 83 C1 02                     add rcx, 2
007C6B94  45 85 C0                        test r8d, r8d
007C6B97  75 EA                           jne 0x1407c6b83
007C6B99  85 D2                           test edx, edx
007C6B9B  75 08                           jne 0x1407c6ba5
007C6B9D  83 C8 10                        or eax, 0x10
007C6BA0  E9 D4 01 00 00                  jmp 0x1407c6d79
007C6BA5  4C 8B 0D 3C 42 38 00            mov r9, qword ptr [rip + 0x38423c]
007C6BAC  49 8B CA                        mov rcx, r10
007C6BAF  4D 2B CA                        sub r9, r10
007C6BB2  0F B7 11                        movzx edx, word ptr [rcx]
007C6BB5  46 0F B7 04 09                  movzx r8d, word ptr [rcx + r9]
007C6BBA  41 2B D0                        sub edx, r8d
007C6BBD  75 09                           jne 0x1407c6bc8
007C6BBF  48 83 C1 02                     add rcx, 2
007C6BC3  45 85 C0                        test r8d, r8d
007C6BC6  75 EA                           jne 0x1407c6bb2
007C6BC8  85 D2                           test edx, edx
007C6BCA  75 08                           jne 0x1407c6bd4
007C6BCC  83 C8 40                        or eax, 0x40
007C6BCF  E9 A5 01 00 00                  jmp 0x1407c6d79
007C6BD4  4C 8B 0D 15 42 38 00            mov r9, qword ptr [rip + 0x384215]
007C6BDB  49 8B CA                        mov rcx, r10
007C6BDE  4D 2B CA                        sub r9, r10
007C6BE1  0F B7 11                        movzx edx, word ptr [rcx]
007C6BE4  46 0F B7 04 09                  movzx r8d, word ptr [rcx + r9]
007C6BE9  41 2B D0                        sub edx, r8d
007C6BEC  75 09                           jne 0x1407c6bf7
007C6BEE  48 83 C1 02                     add rcx, 2
007C6BF2  45 85 C0                        test r8d, r8d
007C6BF5  75 EA                           jne 0x1407c6be1
007C6BF7  85 D2                           test edx, edx
007C6BF9  75 09                           jne 0x1407c6c04
007C6BFB  0F BA E8 07                     bts eax, 7
007C6BFF  E9 75 01 00 00                  jmp 0x1407c6d79
007C6C04  4C 8B 0D ED 41 38 00            mov r9, qword ptr [rip + 0x3841ed]
007C6C0B  49 8B CA                        mov rcx, r10
007C6C0E  4D 2B CA                        sub r9, r10
007C6C11  0F B7 11                        movzx edx, word ptr [rcx]
007C6C14  46 0F B7 04 09                  movzx r8d, word ptr [rcx + r9]
007C6C19  41 2B D0                        sub edx, r8d
007C6C1C  75 09                           jne 0x1407c6c27
007C6C1E  48 83 C1 02                     add rcx, 2
007C6C22  45 85 C0                        test r8d, r8d
007C6C25  75 EA                           jne 0x1407c6c11
007C6C27  85 D2                           test edx, edx
007C6C29  75 09                           jne 0x1407c6c34
007C6C2B  0F BA E8 09                     bts eax, 9
007C6C2F  E9 45 01 00 00                  jmp 0x1407c6d79
007C6C34  4C 8B 0D C5 41 38 00            mov r9, qword ptr [rip + 0x3841c5]
007C6C3B  49 8B CA                        mov rcx, r10
007C6C3E  4D 2B CA                        sub r9, r10
007C6C41  0F B7 11                        movzx edx, word ptr [rcx]
007C6C44  46 0F B7 04 09                  movzx r8d, word ptr [rcx + r9]
007C6C49  41 2B D0                        sub edx, r8d
007C6C4C  75 09                           jne 0x1407c6c57
007C6C4E  48 83 C1 02                     add rcx, 2
007C6C52  45 85 C0                        test r8d, r8d
007C6C55  75 EA                           jne 0x1407c6c41
007C6C57  85 D2                           test edx, edx
007C6C59  75 09                           jne 0x1407c6c64
007C6C5B  0F BA E8 0A                     bts eax, 0xa
007C6C5F  E9 15 01 00 00                  jmp 0x1407c6d79
007C6C64  4C 8B 0D 9D 41 38 00            mov r9, qword ptr [rip + 0x38419d]
007C6C6B  49 8B CA                        mov rcx, r10
007C6C6E  4D 2B CA                        sub r9, r10
007C6C71  0F B7 11                        movzx edx, word ptr [rcx]
007C6C74  46 0F B7 04 09                  movzx r8d, word ptr [rcx + r9]
007C6C79  41 2B D0                        sub edx, r8d
007C6C7C  75 09                           jne 0x1407c6c87
007C6C7E  48 83 C1 02                     add rcx, 2
007C6C82  45 85 C0                        test r8d, r8d
007C6C85  75 EA                           jne 0x1407c6c71
007C6C87  85 D2                           test edx, edx
007C6C89  75 09                           jne 0x1407c6c94
007C6C8B  0F BA E8 0B                     bts eax, 0xb
007C6C8F  E9 E5 00 00 00                  jmp 0x1407c6d79
007C6C94  4C 8B 0D 75 41 38 00            mov r9, qword ptr [rip + 0x384175]
007C6C9B  49 8B CA                        mov rcx, r10
007C6C9E  4D 2B CA                        sub r9, r10
007C6CA1  0F B7 11                        movzx edx, word ptr [rcx]
007C6CA4  46 0F B7 04 09                  movzx r8d, word ptr [rcx + r9]
007C6CA9  41 2B D0                        sub edx, r8d
007C6CAC  75 09                           jne 0x1407c6cb7
007C6CAE  48 83 C1 02                     add rcx, 2
007C6CB2  45 85 C0                        test r8d, r8d
007C6CB5  75 EA                           jne 0x1407c6ca1
007C6CB7  85 D2                           test edx, edx
007C6CB9  75 09                           jne 0x1407c6cc4
007C6CBB  0F BA E8 0C                     bts eax, 0xc
007C6CBF  E9 B5 00 00 00                  jmp 0x1407c6d79
007C6CC4  4C 8B 0D 4D 41 38 00            mov r9, qword ptr [rip + 0x38414d]
007C6CCB  49 8B CA                        mov rcx, r10
007C6CCE  4D 2B CA                        sub r9, r10
007C6CD1  0F B7 11                        movzx edx, word ptr [rcx]
007C6CD4  46 0F B7 04 09                  movzx r8d, word ptr [rcx + r9]
007C6CD9  41 2B D0                        sub edx, r8d
007C6CDC  75 09                           jne 0x1407c6ce7
007C6CDE  48 83 C1 02                     add rcx, 2
007C6CE2  45 85 C0                        test r8d, r8d
007C6CE5  75 EA                           jne 0x1407c6cd1
007C6CE7  85 D2                           test edx, edx
007C6CE9  75 09                           jne 0x1407c6cf4
007C6CEB  0F BA E8 0D                     bts eax, 0xd
007C6CEF  E9 85 00 00 00                  jmp 0x1407c6d79
007C6CF4  4C 8B 0D 25 41 38 00            mov r9, qword ptr [rip + 0x384125]
007C6CFB  49 8B CA                        mov rcx, r10
007C6CFE  4D 2B CA                        sub r9, r10
007C6D01  0F B7 11                        movzx edx, word ptr [rcx]
007C6D04  46 0F B7 04 09                  movzx r8d, word ptr [rcx + r9]
007C6D09  41 2B D0                        sub edx, r8d
007C6D0C  75 09                           jne 0x1407c6d17
007C6D0E  48 83 C1 02                     add rcx, 2
007C6D12  45 85 C0                        test r8d, r8d
007C6D15  75 EA                           jne 0x1407c6d01
007C6D17  85 D2                           test edx, edx
007C6D19  75 06                           jne 0x1407c6d21
007C6D1B  0F BA E8 0E                     bts eax, 0xe
007C6D1F  EB 58                           jmp 0x1407c6d79
007C6D21  4C 8B 0D 00 41 38 00            mov r9, qword ptr [rip + 0x384100]
007C6D28  49 8B CA                        mov rcx, r10
007C6D2B  4D 2B CA                        sub r9, r10
007C6D2E  0F B7 11                        movzx edx, word ptr [rcx]
007C6D31  46 0F B7 04 09                  movzx r8d, word ptr [rcx + r9]
007C6D36  41 2B D0                        sub edx, r8d
007C6D39  75 09                           jne 0x1407c6d44
007C6D3B  48 83 C1 02                     add rcx, 2
007C6D3F  45 85 C0                        test r8d, r8d
007C6D42  75 EA                           jne 0x1407c6d2e
007C6D44  85 D2                           test edx, edx
007C6D46  75 06                           jne 0x1407c6d4e
007C6D48  0F BA E8 0F                     bts eax, 0xf
007C6D4C  EB 2B                           jmp 0x1407c6d79
007C6D4E  4C 8B 0D E3 40 38 00            mov r9, qword ptr [rip + 0x3840e3]
007C6D55  49 8B CA                        mov rcx, r10
007C6D58  4D 2B CA                        sub r9, r10
007C6D5B  0F B7 11                        movzx edx, word ptr [rcx]
007C6D5E  46 0F B7 04 09                  movzx r8d, word ptr [rcx + r9]
007C6D63  41 2B D0                        sub edx, r8d
007C6D66  75 09                           jne 0x1407c6d71
007C6D68  48 83 C1 02                     add rcx, 2
007C6D6C  45 85 C0                        test r8d, r8d
007C6D6F  75 EA                           jne 0x1407c6d5b
007C6D71  85 D2                           test edx, edx
007C6D73  75 04                           jne 0x1407c6d79
007C6D75  0F BA E8 10                     bts eax, 0x10
007C6D79  48 83 C9 FF                     or rcx, 0xffffffffffffffff
007C6D7D  48 FF C1                        inc rcx
007C6D80  66 45 39 1C 4A                  cmp word ptr [r10 + rcx*2], r11w
007C6D85  75 F6                           jne 0x1407c6d7d
007C6D87  4D 8D 14 4A                     lea r10, [r10 + rcx*2]
007C6D8B  49 83 C2 02                     add r10, 2
007C6D8F  66 45 39 1A                     cmp word ptr [r10], r11w
007C6D93  0F 85 F2 FC FF FF               jne 0x1407c6a8b
007C6D99  C3                              ret
007C6D9A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpParseSuiteMask(__int64 a1)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;

    v_r11 = 0;
    if ((*(unsigned __int16 *)(a1)) == 0) goto loc_007C6D99;
loc_007C6A8B:
    a4 = (*(unsigned __int64 *)(v_rip + 3687206)) - (a1);
loc_007C6A98:
    a2 = (unsigned int)((*(unsigned __int16 *)(a1)) - ((unsigned int)(*(unsigned __int16 *)(a1 + a4 * 1))));
    if (condition_is_not_equal) goto loc_007C6AAE;
    a1 = (a1) + (2);
    if ((unsigned int)(*(unsigned __int16 *)(a1 + a4 * 1)) != 0) goto loc_007C6A98;
loc_007C6AAE:
    if ((unsigned int)(a2) != 0) goto loc_007C6ABA;
    result = (unsigned int)((0) | (1));
    goto loc_007C6D79;
loc_007C6ABA:
    a4 = (*(unsigned __int64 *)(v_rip + 3687191)) - (a1);
loc_007C6AC7:
    a2 = (unsigned int)((*(unsigned __int16 *)(a1)) - ((unsigned int)(*(unsigned __int16 *)(a1 + a4 * 1))));
    if (condition_is_not_equal) goto loc_007C6ADD;
    a1 = (a1) + (2);
    if ((unsigned int)(*(unsigned __int16 *)(a1 + a4 * 1)) != 0) goto loc_007C6AC7;
loc_007C6ADD:
    if ((unsigned int)(a2) != 0) goto loc_007C6AE9;
    result = (unsigned int)((result) | (32));
    goto loc_007C6D79;
loc_007C6AE9:
    a4 = (*(unsigned __int64 *)(v_rip + 3687120)) - (a1);
loc_007C6AF6:
    a2 = (unsigned int)((*(unsigned __int16 *)(a1)) - ((unsigned int)(*(unsigned __int16 *)(a1 + a4 * 1))));
    if (condition_is_not_equal) goto loc_007C6B0C;
    a1 = (a1) + (2);
    if ((unsigned int)(*(unsigned __int16 *)(a1 + a4 * 1)) != 0) goto loc_007C6AF6;
loc_007C6B0C:
    if ((unsigned int)(a2) != 0) goto loc_007C6B18;
    result = (unsigned int)((result) | (2));
    goto loc_007C6D79;
loc_007C6B18:
    a4 = (*(unsigned __int64 *)(v_rip + 3687081)) - (a1);
loc_007C6B25:
    a2 = (unsigned int)((*(unsigned __int16 *)(a1)) - ((unsigned int)(*(unsigned __int16 *)(a1 + a4 * 1))));
    if (condition_is_not_equal) goto loc_007C6B3B;
    a1 = (a1) + (2);
    if ((unsigned int)(*(unsigned __int16 *)(a1 + a4 * 1)) != 0) goto loc_007C6B25;
loc_007C6B3B:
    if ((unsigned int)(a2) != 0) goto loc_007C6B47;
    result = (unsigned int)((result) | (8));
    goto loc_007C6D79;
loc_007C6B47:
    a4 = (*(unsigned __int64 *)(v_rip + 3687042)) - (a1);
loc_007C6B54:
    a2 = (unsigned int)((*(unsigned __int16 *)(a1)) - ((unsigned int)(*(unsigned __int16 *)(a1 + a4 * 1))));
    if (condition_is_not_equal) goto loc_007C6B6A;
    a1 = (a1) + (2);
    if ((unsigned int)(*(unsigned __int16 *)(a1 + a4 * 1)) != 0) goto loc_007C6B54;
loc_007C6B6A:
    if ((unsigned int)(a2) != 0) goto loc_007C6B76;
    result = (unsigned int)((result) | (4));
    goto loc_007C6D79;
loc_007C6B76:
    a4 = (*(unsigned __int64 *)(v_rip + 3687011)) - (a1);
loc_007C6B83:
    a2 = (unsigned int)((*(unsigned __int16 *)(a1)) - ((unsigned int)(*(unsigned __int16 *)(a1 + a4 * 1))));
    if (condition_is_not_equal) goto loc_007C6B99;
    a1 = (a1) + (2);
    if ((unsigned int)(*(unsigned __int16 *)(a1 + a4 * 1)) != 0) goto loc_007C6B83;
loc_007C6B99:
    if ((unsigned int)(a2) != 0) goto loc_007C6BA5;
    result = (unsigned int)((result) | (16));
    goto loc_007C6D79;
loc_007C6BA5:
    a4 = (*(unsigned __int64 *)(v_rip + 3686972)) - (a1);
loc_007C6BB2:
    a2 = (unsigned int)((*(unsigned __int16 *)(a1)) - ((unsigned int)(*(unsigned __int16 *)(a1 + a4 * 1))));
    if (condition_is_not_equal) goto loc_007C6BC8;
    a1 = (a1) + (2);
    if ((unsigned int)(*(unsigned __int16 *)(a1 + a4 * 1)) != 0) goto loc_007C6BB2;
loc_007C6BC8:
    if ((unsigned int)(a2) != 0) goto loc_007C6BD4;
    result = (unsigned int)((result) | (64));
    goto loc_007C6D79;
loc_007C6BD4:
    a4 = (*(unsigned __int64 *)(v_rip + 3686933)) - (a1);
loc_007C6BE1:
    a2 = (unsigned int)((*(unsigned __int16 *)(a1)) - ((unsigned int)(*(unsigned __int16 *)(a1 + a4 * 1))));
    if (condition_is_not_equal) goto loc_007C6BF7;
    a1 = (a1) + (2);
    if ((unsigned int)(*(unsigned __int16 *)(a1 + a4 * 1)) != 0) goto loc_007C6BE1;
loc_007C6BF7:
    if ((unsigned int)(a2) != 0) goto loc_007C6C04;
    goto loc_007C6D79;
loc_007C6C04:
    a4 = (*(unsigned __int64 *)(v_rip + 3686893)) - (a1);
loc_007C6C11:
    a2 = (unsigned int)((*(unsigned __int16 *)(a1)) - ((unsigned int)(*(unsigned __int16 *)(a1 + a4 * 1))));
    if (condition_is_not_equal) goto loc_007C6C27;
    a1 = (a1) + (2);
    if ((unsigned int)(*(unsigned __int16 *)(a1 + a4 * 1)) != 0) goto loc_007C6C11;
loc_007C6C27:
    if ((unsigned int)(a2) != 0) goto loc_007C6C34;
    goto loc_007C6D79;
loc_007C6C34:
    a4 = (*(unsigned __int64 *)(v_rip + 3686853)) - (a1);
loc_007C6C41:
    a2 = (unsigned int)((*(unsigned __int16 *)(a1)) - ((unsigned int)(*(unsigned __int16 *)(a1 + a4 * 1))));
    if (condition_is_not_equal) goto loc_007C6C57;
    a1 = (a1) + (2);
    if ((unsigned int)(*(unsigned __int16 *)(a1 + a4 * 1)) != 0) goto loc_007C6C41;
loc_007C6C57:
    if ((unsigned int)(a2) != 0) goto loc_007C6C64;
    goto loc_007C6D79;
loc_007C6C64:
    a4 = (*(unsigned __int64 *)(v_rip + 3686813)) - (a1);
loc_007C6C71:
    a2 = (unsigned int)((*(unsigned __int16 *)(a1)) - ((unsigned int)(*(unsigned __int16 *)(a1 + a4 * 1))));
    if (condition_is_not_equal) goto loc_007C6C87;
    a1 = (a1) + (2);
    if ((unsigned int)(*(unsigned __int16 *)(a1 + a4 * 1)) != 0) goto loc_007C6C71;
loc_007C6C87:
    if ((unsigned int)(a2) != 0) goto loc_007C6C94;
    goto loc_007C6D79;
loc_007C6C94:
    a4 = (*(unsigned __int64 *)(v_rip + 3686773)) - (a1);
loc_007C6CA1:
    a2 = (unsigned int)((*(unsigned __int16 *)(a1)) - ((unsigned int)(*(unsigned __int16 *)(a1 + a4 * 1))));
    if (condition_is_not_equal) goto loc_007C6CB7;
    a1 = (a1) + (2);
    if ((unsigned int)(*(unsigned __int16 *)(a1 + a4 * 1)) != 0) goto loc_007C6CA1;
loc_007C6CB7:
    if ((unsigned int)(a2) != 0) goto loc_007C6CC4;
    goto loc_007C6D79;
loc_007C6CC4:
    a4 = (*(unsigned __int64 *)(v_rip + 3686733)) - (a1);
loc_007C6CD1:
    a2 = (unsigned int)((*(unsigned __int16 *)(a1)) - ((unsigned int)(*(unsigned __int16 *)(a1 + a4 * 1))));
    if (condition_is_not_equal) goto loc_007C6CE7;
    a1 = (a1) + (2);
    if ((unsigned int)(*(unsigned __int16 *)(a1 + a4 * 1)) != 0) goto loc_007C6CD1;
loc_007C6CE7:
    if ((unsigned int)(a2) != 0) goto loc_007C6CF4;
    goto loc_007C6D79;
loc_007C6CF4:
    a4 = (*(unsigned __int64 *)(v_rip + 3686693)) - (a1);
loc_007C6D01:
    a2 = (unsigned int)((*(unsigned __int16 *)(a1)) - ((unsigned int)(*(unsigned __int16 *)(a1 + a4 * 1))));
    if (condition_is_not_equal) goto loc_007C6D17;
    a1 = (a1) + (2);
    if ((unsigned int)(*(unsigned __int16 *)(a1 + a4 * 1)) != 0) goto loc_007C6D01;
loc_007C6D17:
    if ((unsigned int)(a2) != 0) goto loc_007C6D21;
    goto loc_007C6D79;
loc_007C6D21:
    a4 = (*(unsigned __int64 *)(v_rip + 3686656)) - (a1);
loc_007C6D2E:
    a2 = (unsigned int)((*(unsigned __int16 *)(a1)) - ((unsigned int)(*(unsigned __int16 *)(a1 + a4 * 1))));
    if (condition_is_not_equal) goto loc_007C6D44;
    a1 = (a1) + (2);
    if ((unsigned int)(*(unsigned __int16 *)(a1 + a4 * 1)) != 0) goto loc_007C6D2E;
loc_007C6D44:
    if ((unsigned int)(a2) != 0) goto loc_007C6D4E;
    goto loc_007C6D79;
loc_007C6D4E:
    a4 = (*(unsigned __int64 *)(v_rip + 3686627)) - (a1);
loc_007C6D5B:
    a2 = (unsigned int)((*(unsigned __int16 *)(a1)) - ((unsigned int)(*(unsigned __int16 *)(a1 + a4 * 1))));
    if (condition_is_not_equal) goto loc_007C6D71;
    a1 = (a1) + (2);
    if ((unsigned int)(*(unsigned __int16 *)(a1 + a4 * 1)) != 0) goto loc_007C6D5B;
loc_007C6D71:
    if ((unsigned int)(a2) == 0) {
    }
    a1 = (a1) | (-1);
loc_007C6D7D:
    a1 = (a1) + 1;
    if ((*(unsigned __int16 *)(a1 + a1 * 2)) != 0) goto loc_007C6D7D;
    v_r10 = (a1 + a1 * 2) + (2);
    if ((*(unsigned __int16 *)(v_r10)) != 0) goto loc_007C6A8B;
loc_007C6D99:
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ExpParseSuiteMask(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;

    local_r11 = 0;
    if ((*(uint16_t *)(arg1)) == 0) goto loc_007C6D99;
loc_007C6A8B:
    a4 = (*(uint64_t *)(v_rip + 0x384326)) - (Arg1);
loc_007C6A98:
    a2 = (uint32_t)((*(uint16_t *)(arg1)) - ((uint32_t)(*(uint16_t *)(arg1 + a4 * 1))));
    if (condition_is_not_equal) goto loc_007C6AAE;
    Arg1 = (Arg1) + (2);
    if ((uint32_t)(*(uint16_t *)(arg1 + a4 * 1)) != 0) goto loc_007C6A98;
loc_007C6AAE:
    if ((uint32_t)(a2) != 0) goto loc_007C6ABA;
    result = (uint32_t)((0) | (1));
    goto loc_007C6D79;
loc_007C6ABA:
    a4 = (*(uint64_t *)(v_rip + 0x384317)) - (Arg1);
loc_007C6AC7:
    a2 = (uint32_t)((*(uint16_t *)(arg1)) - ((uint32_t)(*(uint16_t *)(arg1 + a4 * 1))));
    if (condition_is_not_equal) goto loc_007C6ADD;
    Arg1 = (Arg1) + (2);
    if ((uint32_t)(*(uint16_t *)(arg1 + a4 * 1)) != 0) goto loc_007C6AC7;
loc_007C6ADD:
    if ((uint32_t)(a2) != 0) goto loc_007C6AE9;
    result = (uint32_t)((result) | (32));
    goto loc_007C6D79;
loc_007C6AE9:
    a4 = (*(uint64_t *)(v_rip + 0x3842D0)) - (Arg1);
loc_007C6AF6:
    a2 = (uint32_t)((*(uint16_t *)(arg1)) - ((uint32_t)(*(uint16_t *)(arg1 + a4 * 1))));
    if (condition_is_not_equal) goto loc_007C6B0C;
    Arg1 = (Arg1) + (2);
    if ((uint32_t)(*(uint16_t *)(arg1 + a4 * 1)) != 0) goto loc_007C6AF6;
loc_007C6B0C:
    if ((uint32_t)(a2) != 0) goto loc_007C6B18;
    result = (uint32_t)((result) | (2));
    goto loc_007C6D79;
loc_007C6B18:
    a4 = (*(uint64_t *)(v_rip + 0x3842A9)) - (Arg1);
loc_007C6B25:
    a2 = (uint32_t)((*(uint16_t *)(arg1)) - ((uint32_t)(*(uint16_t *)(arg1 + a4 * 1))));
    if (condition_is_not_equal) goto loc_007C6B3B;
    Arg1 = (Arg1) + (2);
    if ((uint32_t)(*(uint16_t *)(arg1 + a4 * 1)) != 0) goto loc_007C6B25;
loc_007C6B3B:
    if ((uint32_t)(a2) != 0) goto loc_007C6B47;
    result = (uint32_t)((result) | (8));
    goto loc_007C6D79;
loc_007C6B47:
    a4 = (*(uint64_t *)(v_rip + 0x384282)) - (Arg1);
loc_007C6B54:
    a2 = (uint32_t)((*(uint16_t *)(arg1)) - ((uint32_t)(*(uint16_t *)(arg1 + a4 * 1))));
    if (condition_is_not_equal) goto loc_007C6B6A;
    Arg1 = (Arg1) + (2);
    if ((uint32_t)(*(uint16_t *)(arg1 + a4 * 1)) != 0) goto loc_007C6B54;
loc_007C6B6A:
    if ((uint32_t)(a2) != 0) goto loc_007C6B76;
    result = (uint32_t)((result) | (4));
    goto loc_007C6D79;
loc_007C6B76:
    a4 = (*(uint64_t *)(v_rip + 0x384263)) - (Arg1);
loc_007C6B83:
    a2 = (uint32_t)((*(uint16_t *)(arg1)) - ((uint32_t)(*(uint16_t *)(arg1 + a4 * 1))));
    if (condition_is_not_equal) goto loc_007C6B99;
    Arg1 = (Arg1) + (2);
    if ((uint32_t)(*(uint16_t *)(arg1 + a4 * 1)) != 0) goto loc_007C6B83;
loc_007C6B99:
    if ((uint32_t)(a2) != 0) goto loc_007C6BA5;
    result = (uint32_t)((result) | (16));
    goto loc_007C6D79;
loc_007C6BA5:
    a4 = (*(uint64_t *)(v_rip + 0x38423C)) - (Arg1);
loc_007C6BB2:
    a2 = (uint32_t)((*(uint16_t *)(arg1)) - ((uint32_t)(*(uint16_t *)(arg1 + a4 * 1))));
    if (condition_is_not_equal) goto loc_007C6BC8;
    Arg1 = (Arg1) + (2);
    if ((uint32_t)(*(uint16_t *)(arg1 + a4 * 1)) != 0) goto loc_007C6BB2;
loc_007C6BC8:
    if ((uint32_t)(a2) != 0) goto loc_007C6BD4;
    result = (uint32_t)((result) | (64));
    goto loc_007C6D79;
loc_007C6BD4:
    a4 = (*(uint64_t *)(v_rip + 0x384215)) - (Arg1);
loc_007C6BE1:
    a2 = (uint32_t)((*(uint16_t *)(arg1)) - ((uint32_t)(*(uint16_t *)(arg1 + a4 * 1))));
    if (condition_is_not_equal) goto loc_007C6BF7;
    Arg1 = (Arg1) + (2);
    if ((uint32_t)(*(uint16_t *)(arg1 + a4 * 1)) != 0) goto loc_007C6BE1;
loc_007C6BF7:
    if ((uint32_t)(a2) != 0) goto loc_007C6C04;
    goto loc_007C6D79;
loc_007C6C04:
    a4 = (*(uint64_t *)(v_rip + 0x3841ED)) - (Arg1);
loc_007C6C11:
    a2 = (uint32_t)((*(uint16_t *)(arg1)) - ((uint32_t)(*(uint16_t *)(arg1 + a4 * 1))));
    if (condition_is_not_equal) goto loc_007C6C27;
    Arg1 = (Arg1) + (2);
    if ((uint32_t)(*(uint16_t *)(arg1 + a4 * 1)) != 0) goto loc_007C6C11;
loc_007C6C27:
    if ((uint32_t)(a2) != 0) goto loc_007C6C34;
    goto loc_007C6D79;
loc_007C6C34:
    a4 = (*(uint64_t *)(v_rip + 0x3841C5)) - (Arg1);
loc_007C6C41:
    a2 = (uint32_t)((*(uint16_t *)(arg1)) - ((uint32_t)(*(uint16_t *)(arg1 + a4 * 1))));
    if (condition_is_not_equal) goto loc_007C6C57;
    Arg1 = (Arg1) + (2);
    if ((uint32_t)(*(uint16_t *)(arg1 + a4 * 1)) != 0) goto loc_007C6C41;
loc_007C6C57:
    if ((uint32_t)(a2) != 0) goto loc_007C6C64;
    goto loc_007C6D79;
loc_007C6C64:
    a4 = (*(uint64_t *)(v_rip + 0x38419D)) - (Arg1);
loc_007C6C71:
    a2 = (uint32_t)((*(uint16_t *)(arg1)) - ((uint32_t)(*(uint16_t *)(arg1 + a4 * 1))));
    if (condition_is_not_equal) goto loc_007C6C87;
    Arg1 = (Arg1) + (2);
    if ((uint32_t)(*(uint16_t *)(arg1 + a4 * 1)) != 0) goto loc_007C6C71;
loc_007C6C87:
    if ((uint32_t)(a2) != 0) goto loc_007C6C94;
    goto loc_007C6D79;
loc_007C6C94:
    a4 = (*(uint64_t *)(v_rip + 0x384175)) - (Arg1);
loc_007C6CA1:
    a2 = (uint32_t)((*(uint16_t *)(arg1)) - ((uint32_t)(*(uint16_t *)(arg1 + a4 * 1))));
    if (condition_is_not_equal) goto loc_007C6CB7;
    Arg1 = (Arg1) + (2);
    if ((uint32_t)(*(uint16_t *)(arg1 + a4 * 1)) != 0) goto loc_007C6CA1;
loc_007C6CB7:
    if ((uint32_t)(a2) != 0) goto loc_007C6CC4;
    goto loc_007C6D79;
loc_007C6CC4:
    a4 = (*(uint64_t *)(v_rip + 0x38414D)) - (Arg1);
loc_007C6CD1:
    a2 = (uint32_t)((*(uint16_t *)(arg1)) - ((uint32_t)(*(uint16_t *)(arg1 + a4 * 1))));
    if (condition_is_not_equal) goto loc_007C6CE7;
    Arg1 = (Arg1) + (2);
    if ((uint32_t)(*(uint16_t *)(arg1 + a4 * 1)) != 0) goto loc_007C6CD1;
loc_007C6CE7:
    if ((uint32_t)(a2) != 0) goto loc_007C6CF4;
    goto loc_007C6D79;
loc_007C6CF4:
    a4 = (*(uint64_t *)(v_rip + 0x384125)) - (Arg1);
loc_007C6D01:
    a2 = (uint32_t)((*(uint16_t *)(arg1)) - ((uint32_t)(*(uint16_t *)(arg1 + a4 * 1))));
    if (condition_is_not_equal) goto loc_007C6D17;
    Arg1 = (Arg1) + (2);
    if ((uint32_t)(*(uint16_t *)(arg1 + a4 * 1)) != 0) goto loc_007C6D01;
loc_007C6D17:
    if ((uint32_t)(a2) != 0) goto loc_007C6D21;
    goto loc_007C6D79;
loc_007C6D21:
    a4 = (*(uint64_t *)(v_rip + 0x384100)) - (Arg1);
loc_007C6D2E:
    a2 = (uint32_t)((*(uint16_t *)(arg1)) - ((uint32_t)(*(uint16_t *)(arg1 + a4 * 1))));
    if (condition_is_not_equal) goto loc_007C6D44;
    Arg1 = (Arg1) + (2);
    if ((uint32_t)(*(uint16_t *)(arg1 + a4 * 1)) != 0) goto loc_007C6D2E;
loc_007C6D44:
    if ((uint32_t)(a2) != 0) goto loc_007C6D4E;
    goto loc_007C6D79;
loc_007C6D4E:
    a4 = (*(uint64_t *)(v_rip + 0x3840E3)) - (Arg1);
loc_007C6D5B:
    a2 = (uint32_t)((*(uint16_t *)(arg1)) - ((uint32_t)(*(uint16_t *)(arg1 + a4 * 1))));
    if (condition_is_not_equal) goto loc_007C6D71;
    Arg1 = (Arg1) + (2);
    if ((uint32_t)(*(uint16_t *)(arg1 + a4 * 1)) != 0) goto loc_007C6D5B;
loc_007C6D71:
    if ((uint32_t)(a2) == 0) {
    }
    Arg1 = (Arg1) | (-1);
loc_007C6D7D:
    Arg1 = (Arg1) + 1;
    if ((*(uint16_t *)(arg1 + arg1 * 2)) != 0) goto loc_007C6D7D;
    local_r10 = (Arg1 + Arg1 * 2) + (2);
    if ((*(uint16_t *)(local_r10)) != 0) goto loc_007C6A8B;
loc_007C6D99:
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `16` | `R` |
| `Arg1` | `+ 0x0 + r9*1` | `16` | `R` |
| `Arg1` | `+ 0x0 + rcx*2` | `16` | `R` |
| `Arg1` | `+ 0x0 + rcx*2` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007C6A78&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
