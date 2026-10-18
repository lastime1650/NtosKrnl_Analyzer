# XmEvaluateIndexSpecifier

- RVA: `0x00578928`–`0x00578B7C` (길이 `596` bytes)
- VA: `0x0000000140578928`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C954`
- 디코드: `176`개 명령, `596/596` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **19**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00578941` → [XmGetCodeByte](../47/XmGetCodeByte_function_00473678.md) (function, `0x00473678`)
- `0x005789A2` → [XmGetLongImmediate](../56/XmGetLongImmediate_function_0056DC70.md) (function, `0x0056DC70`)
- `0x00578A12` → [XmGetCodeByte](../47/XmGetCodeByte_function_00473678.md) (function, `0x00473678`)
- `0x00578A22` → [XmGetCodeByte](../47/XmGetCodeByte_function_00473678.md) (function, `0x00473678`)
- `0x00578A35` → [XmGetCodeByte](../47/XmGetCodeByte_function_00473678.md) (function, `0x00473678`)
- `0x00578A48` → [XmGetCodeByte](../47/XmGetCodeByte_function_00473678.md) (function, `0x00473678`)
- `0x00578A63` → [XmGetCodeByte](../47/XmGetCodeByte_function_00473678.md) (function, `0x00473678`)
- `0x00578A96` → [XmGetLongImmediate](../56/XmGetLongImmediate_function_0056DC70.md) (function, `0x0056DC70`)
- `0x00578AA2` → [XmGetLongImmediate](../56/XmGetLongImmediate_function_0056DC70.md) (function, `0x0056DC70`)
- `0x00578AAE` → [XmGetCodeByte](../47/XmGetCodeByte_function_00473678.md) (function, `0x00473678`)
- `0x00578AC1` → [XmGetCodeByte](../47/XmGetCodeByte_function_00473678.md) (function, `0x00473678`)
- `0x00578AD4` → [XmGetCodeByte](../47/XmGetCodeByte_function_00473678.md) (function, `0x00473678`)
- `0x00578AE7` → [XmGetLongImmediate](../56/XmGetLongImmediate_function_0056DC70.md) (function, `0x0056DC70`)
- `0x00578B16` → [longjmp](../4F/longjmp_function_004FD5F0.md) (function, `0x004FD5F0`)
- `0x00578B1F` → [XmGetLongImmediate](../56/XmGetLongImmediate_function_0056DC70.md) (function, `0x0056DC70`)
- `0x00578B2B` → [XmGetLongImmediate](../56/XmGetLongImmediate_function_0056DC70.md) (function, `0x0056DC70`)
- `0x00578B37` → [XmGetLongImmediate](../56/XmGetLongImmediate_function_0056DC70.md) (function, `0x0056DC70`)
- `0x00578B43` → [XmGetLongImmediate](../56/XmGetLongImmediate_function_0056DC70.md) (function, `0x0056DC70`)
- `0x00578B52` → [XmGetLongImmediate](../56/XmGetLongImmediate_function_0056DC70.md) (function, `0x0056DC70`)

### Direct callers
- [sub_006F3DB6](../6F/Unknown_function_006F3DB6.md) at `0x006F3E11`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00578928  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0057892D  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
00578932  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
00578937  57                              push rdi
00578938  48 83 EC 20                     sub rsp, 0x20
0057893C  8B DA                           mov ebx, edx
0057893E  48 8B F9                        mov rdi, rcx
00578941  E8 32 AD EF FF                  call 0x140473678
00578946  0F B6 D0                        movzx edx, al
00578949  41 B8 07 00 00 00               mov r8d, 7
0057894F  8B F2                           mov esi, edx
00578951  8D 04 DD 00 00 00 00            lea eax, [rbx*8]
00578958  8B EA                           mov ebp, edx
0057895A  C1 EE 03                        shr esi, 3
0057895D  41 23 D0                        and edx, r8d
00578960  C1 ED 06                        shr ebp, 6
00578963  41 23 F0                        and esi, r8d
00578966  0B D0                           or edx, eax
00578968  83 FA 0C                        cmp edx, 0xc
0057896B  0F 87 02 01 00 00               ja 0x140578a73
00578971  0F 84 E9 00 00 00               je 0x140578a60
00578977  83 FA 06                        cmp edx, 6
0057897A  77 76                           ja 0x1405789f2
0057897C  74 6C                           je 0x1405789ea
0057897E  85 D2                           test edx, edx
00578980  74 60                           je 0x1405789e2
00578982  83 EA 01                        sub edx, 1
00578985  74 53                           je 0x1405789da
00578987  83 EA 01                        sub edx, 1
0057898A  74 46                           je 0x1405789d2
0057898C  83 EA 01                        sub edx, 1
0057898F  74 39                           je 0x1405789ca
00578991  83 EA 01                        sub edx, 1
00578994  74 18                           je 0x1405789ae
00578996  83 FA 01                        cmp edx, 1
00578999  0F 85 6D 01 00 00               jne 0x140578b0c
0057899F  48 8B CF                        mov rcx, rdi
005789A2  E8 C9 52 FF FF                  call 0x14056dc70
005789A7  8B D0                           mov edx, eax
005789A9  E9 AE 01 00 00                  jmp 0x140578b5c
005789AE  8B 57 28                        mov edx, dword ptr [rdi + 0x28]
005789B1  80 BF 8C 00 00 00 00            cmp byte ptr [rdi + 0x8c], 0
005789B8  0F 85 9E 01 00 00               jne 0x140578b5c
005789BE  C7 47 74 02 00 00 00            mov dword ptr [rdi + 0x74], 2
005789C5  E9 92 01 00 00                  jmp 0x140578b5c
005789CA  8B 57 24                        mov edx, dword ptr [rdi + 0x24]
005789CD  E9 8A 01 00 00                  jmp 0x140578b5c
005789D2  8B 57 20                        mov edx, dword ptr [rdi + 0x20]
005789D5  E9 82 01 00 00                  jmp 0x140578b5c
005789DA  8B 57 1C                        mov edx, dword ptr [rdi + 0x1c]
005789DD  E9 7A 01 00 00                  jmp 0x140578b5c
005789E2  8B 57 18                        mov edx, dword ptr [rdi + 0x18]
005789E5  E9 72 01 00 00                  jmp 0x140578b5c
005789EA  8B 57 30                        mov edx, dword ptr [rdi + 0x30]
005789ED  E9 6A 01 00 00                  jmp 0x140578b5c
005789F2  41 2B D0                        sub edx, r8d
005789F5  74 61                           je 0x140578a58
005789F7  83 EA 01                        sub edx, 1
005789FA  74 49                           je 0x140578a45
005789FC  83 EA 01                        sub edx, 1
005789FF  74 31                           je 0x140578a32
00578A01  83 EA 01                        sub edx, 1
00578A04  74 19                           je 0x140578a1f
00578A06  83 FA 01                        cmp edx, 1
00578A09  0F 85 FD 00 00 00               jne 0x140578b0c
00578A0F  48 8B CF                        mov rcx, rdi
00578A12  E8 61 AC EF FF                  call 0x140473678
00578A17  0F BE D0                        movsx edx, al
00578A1A  E9 3A 01 00 00                  jmp 0x140578b59
00578A1F  48 8B CF                        mov rcx, rdi
00578A22  E8 51 AC EF FF                  call 0x140473678
00578A27  0F BE D0                        movsx edx, al
00578A2A  03 57 20                        add edx, dword ptr [rdi + 0x20]
00578A2D  E9 2A 01 00 00                  jmp 0x140578b5c
00578A32  48 8B CF                        mov rcx, rdi
00578A35  E8 3E AC EF FF                  call 0x140473678
00578A3A  0F BE D0                        movsx edx, al
00578A3D  03 57 1C                        add edx, dword ptr [rdi + 0x1c]
00578A40  E9 17 01 00 00                  jmp 0x140578b5c
00578A45  48 8B CF                        mov rcx, rdi
00578A48  E8 2B AC EF FF                  call 0x140473678
00578A4D  0F BE D0                        movsx edx, al
00578A50  03 57 18                        add edx, dword ptr [rdi + 0x18]
00578A53  E9 04 01 00 00                  jmp 0x140578b5c
00578A58  8B 57 34                        mov edx, dword ptr [rdi + 0x34]
00578A5B  E9 FC 00 00 00                  jmp 0x140578b5c
00578A60  48 8B CF                        mov rcx, rdi
00578A63  E8 10 AC EF FF                  call 0x140473678
00578A68  0F BE D0                        movsx edx, al
00578A6B  03 57 28                        add edx, dword ptr [rdi + 0x28]
00578A6E  E9 3E FF FF FF                  jmp 0x1405789b1
00578A73  83 FA 12                        cmp edx, 0x12
00578A76  77 7B                           ja 0x140578af3
00578A78  74 6A                           je 0x140578ae4
00578A7A  83 EA 0D                        sub edx, 0xd
00578A7D  74 52                           je 0x140578ad1
00578A7F  83 EA 01                        sub edx, 1
00578A82  74 3A                           je 0x140578abe
00578A84  83 EA 01                        sub edx, 1
00578A87  74 22                           je 0x140578aab
00578A89  83 EA 01                        sub edx, 1
00578A8C  74 11                           je 0x140578a9f
00578A8E  83 FA 01                        cmp edx, 1
00578A91  75 79                           jne 0x140578b0c
00578A93  48 8B CF                        mov rcx, rdi
00578A96  E8 D5 51 FF FF                  call 0x14056dc70
00578A9B  8B D0                           mov edx, eax
00578A9D  EB 9E                           jmp 0x140578a3d
00578A9F  48 8B CF                        mov rcx, rdi
00578AA2  E8 C9 51 FF FF                  call 0x14056dc70
00578AA7  8B D0                           mov edx, eax
00578AA9  EB A5                           jmp 0x140578a50
00578AAB  48 8B CF                        mov rcx, rdi
00578AAE  E8 C5 AB EF FF                  call 0x140473678
00578AB3  0F BE D0                        movsx edx, al
00578AB6  03 57 34                        add edx, dword ptr [rdi + 0x34]
00578AB9  E9 9E 00 00 00                  jmp 0x140578b5c
00578ABE  48 8B CF                        mov rcx, rdi
00578AC1  E8 B2 AB EF FF                  call 0x140473678
00578AC6  0F BE D0                        movsx edx, al
00578AC9  03 57 30                        add edx, dword ptr [rdi + 0x30]
00578ACC  E9 8B 00 00 00                  jmp 0x140578b5c
00578AD1  48 8B CF                        mov rcx, rdi
00578AD4  E8 9F AB EF FF                  call 0x140473678
00578AD9  0F BE D0                        movsx edx, al
00578ADC  03 57 2C                        add edx, dword ptr [rdi + 0x2c]
00578ADF  E9 CD FE FF FF                  jmp 0x1405789b1
00578AE4  48 8B CF                        mov rcx, rdi
00578AE7  E8 84 51 FF FF                  call 0x14056dc70
00578AEC  8B D0                           mov edx, eax
00578AEE  E9 37 FF FF FF                  jmp 0x140578a2a
00578AF3  83 EA 13                        sub edx, 0x13
00578AF6  74 57                           je 0x140578b4f
00578AF8  83 EA 01                        sub edx, 1
00578AFB  74 43                           je 0x140578b40
00578AFD  83 EA 01                        sub edx, 1
00578B00  74 32                           je 0x140578b34
00578B02  83 EA 01                        sub edx, 1
00578B05  74 21                           je 0x140578b28
00578B07  83 FA 01                        cmp edx, 1
00578B0A  74 10                           je 0x140578b1c
00578B0C  48 8D 8F A0 00 00 00            lea rcx, [rdi + 0xa0]
00578B13  41 8B D0                        mov edx, r8d
00578B16  E8 D5 4A F8 FF                  call 0x1404fd5f0
00578B1B  CC                              int3
00578B1C  48 8B CF                        mov rcx, rdi
00578B1F  E8 4C 51 FF FF                  call 0x14056dc70
00578B24  8B D0                           mov edx, eax
00578B26  EB 8E                           jmp 0x140578ab6
00578B28  48 8B CF                        mov rcx, rdi
00578B2B  E8 40 51 FF FF                  call 0x14056dc70
00578B30  8B D0                           mov edx, eax
00578B32  EB 95                           jmp 0x140578ac9
00578B34  48 8B CF                        mov rcx, rdi
00578B37  E8 34 51 FF FF                  call 0x14056dc70
00578B3C  8B D0                           mov edx, eax
00578B3E  EB 9C                           jmp 0x140578adc
00578B40  48 8B CF                        mov rcx, rdi
00578B43  E8 28 51 FF FF                  call 0x14056dc70
00578B48  8B D0                           mov edx, eax
00578B4A  E9 1C FF FF FF                  jmp 0x140578a6b
00578B4F  48 8B CF                        mov rcx, rdi
00578B52  E8 19 51 FF FF                  call 0x14056dc70
00578B57  8B D0                           mov edx, eax
00578B59  03 57 24                        add edx, dword ptr [rdi + 0x24]
00578B5C  8B 44 B7 18                     mov eax, dword ptr [rdi + rsi*4 + 0x18]
00578B60  8B CD                           mov ecx, ebp
00578B62  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00578B67  48 8B 6C 24 38                  mov rbp, qword ptr [rsp + 0x38]
00578B6C  48 8B 74 24 40                  mov rsi, qword ptr [rsp + 0x40]
00578B71  D3 E0                           shl eax, cl
00578B73  03 C2                           add eax, edx
00578B75  48 83 C4 20                     add rsp, 0x20
00578B79  5F                              pop rdi
00578B7A  C3                              ret
00578B7B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall XmEvaluateIndexSpecifier(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rbp;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (32);
    result = XmGetCodeByte(a1, a2, a3, a4);
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)((unsigned __int8)(result)))) >> (3));
    a2 = (unsigned int)(((unsigned __int8)(result)) & (7));
    v_rbp = (unsigned int)(((unsigned int)((unsigned int)((unsigned __int8)(result)))) >> (6));
    v_rsi = (unsigned int)((v_rsi) & (7));
    a2 = (unsigned int)((a2) | ((unsigned int)((unsigned int)(a2) * 8)));
    if (a2 > 12) goto loc_00578A73;
    if (a2 == 12) goto loc_00578A60;
    if (a2 > 6) goto loc_005789F2;
    if (a2 == 6) goto loc_005789EA;
    if (a2 == 0) goto loc_005789E2;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_005789DA;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_005789D2;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_005789CA;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_005789AE;
    if (a2 != 1) goto loc_00578B0C;
    result = XmGetLongImmediate(a1, a2, 7, a4);
    goto loc_00578B5C;
loc_005789AE:
loc_005789B1:
    if ((*(unsigned __int8 *)(a1 + 140)) != 0) goto loc_00578B5C;
    *(unsigned int *)(a1 + 116) = 2;
    goto loc_00578B5C;
loc_005789CA:
    goto loc_00578B5C;
loc_005789D2:
    goto loc_00578B5C;
loc_005789DA:
    goto loc_00578B5C;
loc_005789E2:
    goto loc_00578B5C;
loc_005789EA:
    goto loc_00578B5C;
loc_005789F2:
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 48))) - (7));
    if (condition_is_equal) goto loc_00578A58;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_00578A45;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_00578A32;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_00578A1F;
    if (a2 != 1) goto loc_00578B0C;
    result = XmGetCodeByte(a1, a2, 7, a4);
    goto loc_00578B59;
loc_00578A1F:
    result = XmGetCodeByte(a1, (__int8)((unsigned __int8)(result)), 7, a4);
loc_00578A2A:
    a2 = (unsigned int)(((__int8)((unsigned __int8)(result))) + (*(unsigned int *)(a1 + 32)));
    goto loc_00578B5C;
loc_00578A32:
    result = XmGetCodeByte(a1, a2, 7, a4);
loc_00578A3D:
    a2 = (unsigned int)(((__int8)((unsigned __int8)(result))) + (*(unsigned int *)(a1 + 28)));
    goto loc_00578B5C;
loc_00578A45:
    result = XmGetCodeByte(a1, a2, 7, a4);
loc_00578A50:
    a2 = (unsigned int)(((__int8)((unsigned __int8)(result))) + (*(unsigned int *)(a1 + 24)));
    goto loc_00578B5C;
loc_00578A58:
    goto loc_00578B5C;
loc_00578A60:
    result = XmGetCodeByte(a1, (unsigned int)(*(unsigned int *)(a1 + 52)), 7, a4);
loc_00578A6B:
    a2 = (unsigned int)(((__int8)((unsigned __int8)(result))) + (*(unsigned int *)(a1 + 40)));
    goto loc_005789B1;
loc_00578A73:
    if (a2 > 18) goto loc_00578AF3;
    if (a2 == 18) goto loc_00578AE4;
    a2 = (unsigned int)((a2) - (13));
    if (condition_is_equal) goto loc_00578AD1;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_00578ABE;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_00578AAB;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_00578A9F;
    if (a2 != 1) goto loc_00578B0C;
    result = XmGetLongImmediate(a1, a2, 7, a4);
    goto loc_00578A3D;
loc_00578A9F:
    result = XmGetLongImmediate(a1, (unsigned int)((unsigned int)(result)), 7, a4);
    goto loc_00578A50;
loc_00578AAB:
    result = XmGetCodeByte(a1, (unsigned int)((unsigned int)(result)), 7, a4);
loc_00578AB6:
    a2 = (unsigned int)(((__int8)((unsigned __int8)(result))) + (*(unsigned int *)(a1 + 52)));
    goto loc_00578B5C;
loc_00578ABE:
    result = XmGetCodeByte(a1, a2, 7, a4);
loc_00578AC9:
    a2 = (unsigned int)(((__int8)((unsigned __int8)(result))) + (*(unsigned int *)(a1 + 48)));
    goto loc_00578B5C;
loc_00578AD1:
    result = XmGetCodeByte(a1, a2, 7, a4);
loc_00578ADC:
    a2 = (unsigned int)(((__int8)((unsigned __int8)(result))) + (*(unsigned int *)(a1 + 44)));
    goto loc_005789B1;
loc_00578AE4:
    result = XmGetLongImmediate(a1, a2, 7, a4);
    goto loc_00578A2A;
loc_00578AF3:
    a2 = (unsigned int)(((unsigned int)((unsigned int)(result))) - (19));
    if (condition_is_equal) goto loc_00578B4F;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_00578B40;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_00578B34;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_00578B28;
    if (a2 != 1) {
        a1 = a1 + 160;
        a2 = 7;
        result = longjmp(a1, a2, 7, a4);
    }
    result = XmGetLongImmediate(a1, a2, 7, a4);
    goto loc_00578AB6;
loc_00578B28:
    result = XmGetLongImmediate(a1, (unsigned int)((unsigned int)(result)), 7, a4);
    goto loc_00578AC9;
loc_00578B34:
    result = XmGetLongImmediate(a1, (unsigned int)((unsigned int)(result)), 7, a4);
    goto loc_00578ADC;
loc_00578B40:
    result = XmGetLongImmediate(a1, (unsigned int)((unsigned int)(result)), 7, a4);
    goto loc_00578A6B;
loc_00578B4F:
    result = XmGetLongImmediate(a1, (unsigned int)((unsigned int)(result)), 7, a4);
loc_00578B59:
    a2 = (unsigned int)(((unsigned int)((unsigned int)(result))) + (*(unsigned int *)(a1 + 36)));
loc_00578B5C:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + v_rsi * 4 + 24))) << ((unsigned __int8)((unsigned int)((unsigned int)(v_rbp)))));
    result = (unsigned int)((result) + (a2));
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t XmEvaluateIndexSpecifier(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rbp;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (32);
    result = XmGetCodeByte(Arg1, Arg2, a3, a4);
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)((uint8_t)(result)))) >> (3));
    Arg2 = (uint32_t)(((uint8_t)(result)) & (7));
    local_rbp = (uint32_t)(((uint32_t)((uint32_t)((uint8_t)(result)))) >> (6));
    local_rsi = (uint32_t)((local_rsi) & (7));
    Arg2 = (uint32_t)((Arg2) | ((uint32_t)((uint32_t)(Arg2) * 8)));
    if (Arg2 > 12) goto loc_00578A73;
    if (Arg2 == 12) goto loc_00578A60;
    if (Arg2 > 6) goto loc_005789F2;
    if (Arg2 == 6) goto loc_005789EA;
    if (Arg2 == 0) goto loc_005789E2;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_005789DA;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_005789D2;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_005789CA;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_005789AE;
    if (Arg2 != 1) goto loc_00578B0C;
    result = XmGetLongImmediate(Arg1, Arg2, 7, a4);
    goto loc_00578B5C;
loc_005789AE:
loc_005789B1:
    if ((*(uint8_t *)(arg1 + 0x8C)) != 0) goto loc_00578B5C;
    *(uint32_t *)(arg1 + 0x74) = 2;
    goto loc_00578B5C;
loc_005789CA:
    goto loc_00578B5C;
loc_005789D2:
    goto loc_00578B5C;
loc_005789DA:
    goto loc_00578B5C;
loc_005789E2:
    goto loc_00578B5C;
loc_005789EA:
    goto loc_00578B5C;
loc_005789F2:
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x30))) - (7));
    if (condition_is_equal) goto loc_00578A58;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_00578A45;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_00578A32;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_00578A1F;
    if (Arg2 != 1) goto loc_00578B0C;
    result = XmGetCodeByte(Arg1, Arg2, 7, a4);
    goto loc_00578B59;
loc_00578A1F:
    result = XmGetCodeByte(Arg1, (int8_t)((uint8_t)(result)), 7, a4);
loc_00578A2A:
    Arg2 = (uint32_t)(((int8_t)((uint8_t)(result))) + (*(uint32_t *)(arg1 + 0x20)));
    goto loc_00578B5C;
loc_00578A32:
    result = XmGetCodeByte(Arg1, Arg2, 7, a4);
loc_00578A3D:
    Arg2 = (uint32_t)(((int8_t)((uint8_t)(result))) + (*(uint32_t *)(arg1 + 0x1C)));
    goto loc_00578B5C;
loc_00578A45:
    result = XmGetCodeByte(Arg1, Arg2, 7, a4);
loc_00578A50:
    Arg2 = (uint32_t)(((int8_t)((uint8_t)(result))) + (*(uint32_t *)(arg1 + 0x18)));
    goto loc_00578B5C;
loc_00578A58:
    goto loc_00578B5C;
loc_00578A60:
    result = XmGetCodeByte(Arg1, (uint32_t)(*(uint32_t *)(arg1 + 0x34)), 7, a4);
loc_00578A6B:
    Arg2 = (uint32_t)(((int8_t)((uint8_t)(result))) + (*(uint32_t *)(arg1 + 0x28)));
    goto loc_005789B1;
loc_00578A73:
    if (Arg2 > 18) goto loc_00578AF3;
    if (Arg2 == 18) goto loc_00578AE4;
    Arg2 = (uint32_t)((Arg2) - (13));
    if (condition_is_equal) goto loc_00578AD1;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_00578ABE;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_00578AAB;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_00578A9F;
    if (Arg2 != 1) goto loc_00578B0C;
    result = XmGetLongImmediate(Arg1, Arg2, 7, a4);
    goto loc_00578A3D;
loc_00578A9F:
    result = XmGetLongImmediate(Arg1, (uint32_t)((uint32_t)(result)), 7, a4);
    goto loc_00578A50;
loc_00578AAB:
    result = XmGetCodeByte(Arg1, (uint32_t)((uint32_t)(result)), 7, a4);
loc_00578AB6:
    Arg2 = (uint32_t)(((int8_t)((uint8_t)(result))) + (*(uint32_t *)(arg1 + 0x34)));
    goto loc_00578B5C;
loc_00578ABE:
    result = XmGetCodeByte(Arg1, Arg2, 7, a4);
loc_00578AC9:
    Arg2 = (uint32_t)(((int8_t)((uint8_t)(result))) + (*(uint32_t *)(arg1 + 0x30)));
    goto loc_00578B5C;
loc_00578AD1:
    result = XmGetCodeByte(Arg1, Arg2, 7, a4);
loc_00578ADC:
    Arg2 = (uint32_t)(((int8_t)((uint8_t)(result))) + (*(uint32_t *)(arg1 + 0x2C)));
    goto loc_005789B1;
loc_00578AE4:
    result = XmGetLongImmediate(Arg1, Arg2, 7, a4);
    goto loc_00578A2A;
loc_00578AF3:
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(result))) - (19));
    if (condition_is_equal) goto loc_00578B4F;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_00578B40;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_00578B34;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_00578B28;
    if (Arg2 != 1) {
        Arg1 = Arg1 + 160;
        Arg2 = 7;
        result = longjmp(Arg1, Arg2, 7, a4);
    }
    result = XmGetLongImmediate(Arg1, Arg2, 7, a4);
    goto loc_00578AB6;
loc_00578B28:
    result = XmGetLongImmediate(Arg1, (uint32_t)((uint32_t)(result)), 7, a4);
    goto loc_00578AC9;
loc_00578B34:
    result = XmGetLongImmediate(Arg1, (uint32_t)((uint32_t)(result)), 7, a4);
    goto loc_00578ADC;
loc_00578B40:
    result = XmGetLongImmediate(Arg1, (uint32_t)((uint32_t)(result)), 7, a4);
    goto loc_00578A6B;
loc_00578B4F:
    result = XmGetLongImmediate(Arg1, (uint32_t)((uint32_t)(result)), 7, a4);
loc_00578B59:
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(result))) + (*(uint32_t *)(arg1 + 0x24)));
loc_00578B5C:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + local_rsi * 4 + 0x18))) << ((uint8_t)((uint32_t)((uint32_t)(local_rbp)))));
    result = (uint32_t)((result) + (Arg2));
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x18` | `32` | `R` |
| `Arg1` | `+ 0x18 + rsi*4` | `32` | `R` |
| `Arg1` | `+ 0x1C` | `32` | `R` |
| `Arg1` | `+ 0x20` | `32` | `R` |
| `Arg1` | `+ 0x24` | `32` | `R` |
| `Arg1` | `+ 0x28` | `32` | `R` |
| `Arg1` | `+ 0x2C` | `32` | `R` |
| `Arg1` | `+ 0x30` | `32` | `R` |
| `Arg1` | `+ 0x34` | `32` | `R` |
| `Arg1` | `+ 0x74` | `32` | `W` |
| `Arg1` | `+ 0x8C` | `8` | `R` |
| `Arg1` | `+ 0xA0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00578928&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
