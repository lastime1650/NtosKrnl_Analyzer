# BgpGxBlendColor

- RVA: `0x0047F034`–`0x0047F118` (길이 `228` bytes)
- VA: `0x000000014047F034`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00071750`
- 디코드: `70`개 명령, `228/228` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [RaspAntiAlias](RaspAntiAlias_function_0047EED4.md) at `0x0047EFE0`
- [BgpGxBlendRectangle](../../pagebgfx/BC/BgpGxBlendRectangle_function_00BC2400.md) at `0x00BC2560`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0047F034  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0047F039  83 64 24 18 00                  and dword ptr [rsp + 0x18], 0
0047F03E  44 8B D2                        mov r10d, edx
0047F041  8B C2                           mov eax, edx
0047F043  45 0F B6 C8                     movzx r9d, r8b
0047F047  C1 E8 10                        shr eax, 0x10
0047F04A  8B D9                           mov ebx, ecx
0047F04C  44 0F B6 C0                     movzx r8d, al
0047F050  41 BB FF 00 00 00               mov r11d, 0xff
0047F056  45 0F AF C1                     imul r8d, r9d
0047F05A  45 2B D9                        sub r11d, r9d
0047F05D  B8 81 80 80 80                  mov eax, 0x80808081
0047F062  41 F7 E0                        mul r8d
0047F065  8B C1                           mov eax, ecx
0047F067  C1 E8 10                        shr eax, 0x10
0047F06A  44 8B C2                        mov r8d, edx
0047F06D  0F B6 C8                        movzx ecx, al
0047F070  B8 81 80 80 80                  mov eax, 0x80808081
0047F075  41 0F AF CB                     imul ecx, r11d
0047F079  41 C1 E8 07                     shr r8d, 7
0047F07D  F7 E9                           imul ecx
0047F07F  03 D1                           add edx, ecx
0047F081  C1 FA 07                        sar edx, 7
0047F084  8B C2                           mov eax, edx
0047F086  C1 E8 1F                        shr eax, 0x1f
0047F089  03 D0                           add edx, eax
0047F08B  41 8B C2                        mov eax, r10d
0047F08E  44 02 C2                        add r8b, dl
0047F091  C1 E8 08                        shr eax, 8
0047F094  0F B6 C8                        movzx ecx, al
0047F097  B8 81 80 80 80                  mov eax, 0x80808081
0047F09C  41 0F AF C9                     imul ecx, r9d
0047F0A0  44 88 44 24 1A                  mov byte ptr [rsp + 0x1a], r8b
0047F0A5  F7 E1                           mul ecx
0047F0A7  8B C3                           mov eax, ebx
0047F0A9  C1 E8 08                        shr eax, 8
0047F0AC  44 8B C2                        mov r8d, edx
0047F0AF  0F B6 C8                        movzx ecx, al
0047F0B2  B8 81 80 80 80                  mov eax, 0x80808081
0047F0B7  41 0F AF CB                     imul ecx, r11d
0047F0BB  41 C1 E8 07                     shr r8d, 7
0047F0BF  F7 E9                           imul ecx
0047F0C1  B8 81 80 80 80                  mov eax, 0x80808081
0047F0C6  03 D1                           add edx, ecx
0047F0C8  C1 FA 07                        sar edx, 7
0047F0CB  8B CA                           mov ecx, edx
0047F0CD  C1 E9 1F                        shr ecx, 0x1f
0047F0D0  03 D1                           add edx, ecx
0047F0D2  41 0F B6 CA                     movzx ecx, r10b
0047F0D6  44 02 C2                        add r8b, dl
0047F0D9  41 0F AF C9                     imul ecx, r9d
0047F0DD  44 88 44 24 19                  mov byte ptr [rsp + 0x19], r8b
0047F0E2  F7 E1                           mul ecx
0047F0E4  0F B6 CB                        movzx ecx, bl
0047F0E7  B8 81 80 80 80                  mov eax, 0x80808081
0047F0EC  48 8B 5C 24 08                  mov rbx, qword ptr [rsp + 8]
0047F0F1  44 8B C2                        mov r8d, edx
0047F0F4  41 0F AF CB                     imul ecx, r11d
0047F0F8  41 C1 E8 07                     shr r8d, 7
0047F0FC  F7 E9                           imul ecx
0047F0FE  03 D1                           add edx, ecx
0047F100  C1 FA 07                        sar edx, 7
0047F103  8B C2                           mov eax, edx
0047F105  C1 E8 1F                        shr eax, 0x1f
0047F108  03 D0                           add edx, eax
0047F10A  44 02 C2                        add r8b, dl
0047F10D  44 88 44 24 18                  mov byte ptr [rsp + 0x18], r8b
0047F112  8B 44 24 18                     mov eax, dword ptr [rsp + 0x18]
0047F116  C3                              ret
0047F117  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall BgpGxBlendColor(int a1, int a2, unsigned __int8 a3)
{
    __int64 result;
    __int64 v_r11;
    unsigned int v_stack_p18;
    unsigned __int8 v_stack_p19;
    unsigned __int8 v_stack_p1A;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    result = (unsigned int)(((unsigned int)(a2)) >> (16));
    a3 = (unsigned int)(((unsigned __int8)(result)) * (a3));
    v_r11 = (unsigned int)((255) - (a3));
    result = (unsigned int)(((unsigned int)(a1)) >> (16));
    a1 = (unsigned int)(((unsigned __int8)(result)) * ((unsigned int)(v_r11)));
    a3 = (unsigned int)(((unsigned int)(a2)) >> (7));
    a2 = (unsigned int)((a2) + (a1));
    a2 = (unsigned int)((a2) >> (7));
    result = (unsigned int)(((unsigned int)(a2)) >> (31));
    a2 = (unsigned int)((a2) + ((unsigned int)(result)));
    a3 = (unsigned __int8)((a3) + ((unsigned __int8)(a2)));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a2)))) >> (8));
    a1 = (unsigned int)(((unsigned __int8)(result)) * (a3));
    v_stack_p1A = a3;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a1)))) >> (8));
    a1 = (unsigned int)(((unsigned __int8)(result)) * ((unsigned int)(v_r11)));
    a3 = (unsigned int)(((unsigned int)(a2)) >> (7));
    a2 = (unsigned int)((a2) + (a1));
    a2 = (unsigned int)((a2) >> (7));
    a1 = (unsigned int)(((unsigned int)(a2)) >> (31));
    a2 = (unsigned int)((a2) + (a1));
    a3 = (unsigned __int8)((a3) + ((unsigned __int8)(a2)));
    a1 = (unsigned int)(((unsigned __int8)((unsigned int)(a2))) * (a3));
    v_stack_p19 = a3;
    a1 = (unsigned int)(((unsigned __int8)((unsigned int)(a1))) * ((unsigned int)(v_r11)));
    a3 = (unsigned int)(((unsigned int)(a2)) >> (7));
    a2 = (unsigned int)((a2) + (a1));
    a2 = (unsigned int)((a2) >> (7));
    result = (unsigned int)(((unsigned int)(a2)) >> (31));
    a2 = (unsigned int)((a2) + ((unsigned int)(result)));
    a3 = (unsigned __int8)((a3) + ((unsigned __int8)(a2)));
    v_stack_p18 = a3;
    return (unsigned int)(v_stack_p18);
}
```

## 5. (Beta) C Style

```c
int64_t BgpGxBlendColor(int32_t Arg1, int32_t Arg2, uint8_t Arg3)
{
    int64_t result;
    int64_t local_r11;
    uint32_t v_stack_p18;
    uint8_t v_stack_p19;
    uint8_t v_stack_p1A;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    result = (uint32_t)(((uint32_t)(Arg2)) >> (16));
    Arg3 = (uint32_t)(((uint8_t)(result)) * (Arg3));
    local_r11 = (uint32_t)((255) - (Arg3));
    result = (uint32_t)(((uint32_t)(Arg1)) >> (16));
    Arg1 = (uint32_t)(((uint8_t)(result)) * ((uint32_t)(local_r11)));
    Arg3 = (uint32_t)(((uint32_t)(Arg2)) >> (7));
    Arg2 = (uint32_t)((Arg2) + (Arg1));
    Arg2 = (uint32_t)((Arg2) >> (7));
    result = (uint32_t)(((uint32_t)(Arg2)) >> (31));
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)(result)));
    Arg3 = (uint8_t)((Arg3) + ((uint8_t)(Arg2)));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg2)))) >> (8));
    Arg1 = (uint32_t)(((uint8_t)(result)) * (Arg3));
    v_stack_p1A = Arg3;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg1)))) >> (8));
    Arg1 = (uint32_t)(((uint8_t)(result)) * ((uint32_t)(local_r11)));
    Arg3 = (uint32_t)(((uint32_t)(Arg2)) >> (7));
    Arg2 = (uint32_t)((Arg2) + (Arg1));
    Arg2 = (uint32_t)((Arg2) >> (7));
    Arg1 = (uint32_t)(((uint32_t)(Arg2)) >> (31));
    Arg2 = (uint32_t)((Arg2) + (Arg1));
    Arg3 = (uint8_t)((Arg3) + ((uint8_t)(Arg2)));
    Arg1 = (uint32_t)(((uint8_t)((uint32_t)(Arg2))) * (Arg3));
    v_stack_p19 = Arg3;
    Arg1 = (uint32_t)(((uint8_t)((uint32_t)(Arg1))) * ((uint32_t)(local_r11)));
    Arg3 = (uint32_t)(((uint32_t)(Arg2)) >> (7));
    Arg2 = (uint32_t)((Arg2) + (Arg1));
    Arg2 = (uint32_t)((Arg2) >> (7));
    result = (uint32_t)(((uint32_t)(Arg2)) >> (31));
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)(result)));
    Arg3 = (uint8_t)((Arg3) + ((uint8_t)(Arg2)));
    v_stack_p18 = Arg3;
    return (uint32_t)(v_stack_p18);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0047F034&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0047F034[BB_0047F034]
  bb_0047F117[BB_0047F117]
```
