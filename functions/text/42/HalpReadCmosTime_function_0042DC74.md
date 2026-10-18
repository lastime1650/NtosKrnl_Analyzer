# HalpReadCmosTime

- RVA: `0x0042DC74`–`0x0042DDFD` (길이 `393` bytes)
- VA: `0x000000014042DC74`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00071254`
- 디코드: `170`개 명령, `393/393` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0042DC86` → [HalpAcquireCmosSpinLockAndWait](HalpAcquireCmosSpinLockAndWait_function_0042DE20.md) (function, `0x0042DE20`)
- `0x0042DD7E` → [HalpGetCmosCenturyByte](HalpGetCmosCenturyByte_function_0042DE68.md) (function, `0x0042DE68`)
- `0x0042DDE1` → [HalpReleaseCmosSpinLock](HalpReleaseCmosSpinLock_function_0042DE04.md) (function, `0x0042DE04`)

### Direct callers
- [HalQueryRealTimeClock](HalQueryRealTimeClock_function_0042D810.md) at `0x0042D86C`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0042DC74  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0042DC79  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
0042DC7E  57                              push rdi
0042DC7F  48 83 EC 20                     sub rsp, 0x20
0042DC83  48 8B D9                        mov rbx, rcx
0042DC86  E8 95 01 00 00                  call 0x14042de20
0042DC8B  66 C7 43 0C F4 01               mov word ptr [rbx + 0xc], 0x1f4
0042DC91  33 C0                           xor eax, eax
0042DC93  90                              nop
0042DC94  BE 70 00 00 00                  mov esi, 0x70
0042DC99  8B D6                           mov edx, esi
0042DC9B  EE                              out dx, al
0042DC9C  90                              nop
0042DC9D  90                              nop
0042DC9E  8D 7E 01                        lea edi, [rsi + 1]
0042DCA1  8B D7                           mov edx, edi
0042DCA3  EC                              in al, dx
0042DCA4  90                              nop
0042DCA5  8A D0                           mov dl, al
0042DCA7  C0 EA 04                        shr dl, 4
0042DCAA  24 0F                           and al, 0xf
0042DCAC  8A CA                           mov cl, dl
0042DCAE  C0 E1 02                        shl cl, 2
0042DCB1  02 D1                           add dl, cl
0042DCB3  02 D2                           add dl, dl
0042DCB5  02 D0                           add dl, al
0042DCB7  0F B6 C2                        movzx eax, dl
0042DCBA  8B D6                           mov edx, esi
0042DCBC  66 89 43 0A                     mov word ptr [rbx + 0xa], ax
0042DCC0  90                              nop
0042DCC1  B0 02                           mov al, 2
0042DCC3  EE                              out dx, al
0042DCC4  90                              nop
0042DCC5  8B D7                           mov edx, edi
0042DCC7  90                              nop
0042DCC8  EC                              in al, dx
0042DCC9  90                              nop
0042DCCA  8A D0                           mov dl, al
0042DCCC  C0 EA 04                        shr dl, 4
0042DCCF  24 0F                           and al, 0xf
0042DCD1  8A CA                           mov cl, dl
0042DCD3  C0 E1 02                        shl cl, 2
0042DCD6  02 D1                           add dl, cl
0042DCD8  02 D2                           add dl, dl
0042DCDA  02 D0                           add dl, al
0042DCDC  0F B6 C2                        movzx eax, dl
0042DCDF  8B D6                           mov edx, esi
0042DCE1  66 89 43 08                     mov word ptr [rbx + 8], ax
0042DCE5  90                              nop
0042DCE6  B0 04                           mov al, 4
0042DCE8  EE                              out dx, al
0042DCE9  90                              nop
0042DCEA  8B D7                           mov edx, edi
0042DCEC  90                              nop
0042DCED  EC                              in al, dx
0042DCEE  8A D0                           mov dl, al
0042DCF0  90                              nop
0042DCF1  C0 EA 04                        shr dl, 4
0042DCF4  24 0F                           and al, 0xf
0042DCF6  8A CA                           mov cl, dl
0042DCF8  C0 E1 02                        shl cl, 2
0042DCFB  02 D1                           add dl, cl
0042DCFD  02 D2                           add dl, dl
0042DCFF  02 D0                           add dl, al
0042DD01  0F B6 C2                        movzx eax, dl
0042DD04  8B D6                           mov edx, esi
0042DD06  66 89 43 06                     mov word ptr [rbx + 6], ax
0042DD0A  90                              nop
0042DD0B  B0 06                           mov al, 6
0042DD0D  EE                              out dx, al
0042DD0E  90                              nop
0042DD0F  8B D7                           mov edx, edi
0042DD11  90                              nop
0042DD12  EC                              in al, dx
0042DD13  8A D0                           mov dl, al
0042DD15  90                              nop
0042DD16  C0 EA 04                        shr dl, 4
0042DD19  24 0F                           and al, 0xf
0042DD1B  8A CA                           mov cl, dl
0042DD1D  C0 E1 02                        shl cl, 2
0042DD20  02 D1                           add dl, cl
0042DD22  02 D2                           add dl, dl
0042DD24  02 D0                           add dl, al
0042DD26  0F B6 C2                        movzx eax, dl
0042DD29  66 89 43 0E                     mov word ptr [rbx + 0xe], ax
0042DD2D  90                              nop
0042DD2E  B0 07                           mov al, 7
0042DD30  8B D6                           mov edx, esi
0042DD32  EE                              out dx, al
0042DD33  90                              nop
0042DD34  8B D7                           mov edx, edi
0042DD36  90                              nop
0042DD37  EC                              in al, dx
0042DD38  8A D0                           mov dl, al
0042DD3A  90                              nop
0042DD3B  C0 EA 04                        shr dl, 4
0042DD3E  24 0F                           and al, 0xf
0042DD40  8A CA                           mov cl, dl
0042DD42  C0 E1 02                        shl cl, 2
0042DD45  02 D1                           add dl, cl
0042DD47  02 D2                           add dl, dl
0042DD49  02 D0                           add dl, al
0042DD4B  0F B6 C2                        movzx eax, dl
0042DD4E  8B D6                           mov edx, esi
0042DD50  66 89 43 04                     mov word ptr [rbx + 4], ax
0042DD54  90                              nop
0042DD55  B0 08                           mov al, 8
0042DD57  EE                              out dx, al
0042DD58  90                              nop
0042DD59  8B D7                           mov edx, edi
0042DD5B  90                              nop
0042DD5C  EC                              in al, dx
0042DD5D  44 8A C0                        mov r8b, al
0042DD60  90                              nop
0042DD61  41 C0 E8 04                     shr r8b, 4
0042DD65  24 0F                           and al, 0xf
0042DD67  41 8A C8                        mov cl, r8b
0042DD6A  C0 E1 02                        shl cl, 2
0042DD6D  44 02 C1                        add r8b, cl
0042DD70  45 02 C0                        add r8b, r8b
0042DD73  44 02 C0                        add r8b, al
0042DD76  41 0F B6 C0                     movzx eax, r8b
0042DD7A  66 89 43 02                     mov word ptr [rbx + 2], ax
0042DD7E  E8 E5 00 00 00                  call 0x14042de68
0042DD83  44 8A D8                        mov r11b, al
0042DD86  90                              nop
0042DD87  B0 09                           mov al, 9
0042DD89  8B D6                           mov edx, esi
0042DD8B  EE                              out dx, al
0042DD8C  90                              nop
0042DD8D  8B D7                           mov edx, edi
0042DD8F  90                              nop
0042DD90  EC                              in al, dx
0042DD91  44 8A C0                        mov r8b, al
0042DD94  41 8A D3                        mov dl, r11b
0042DD97  C0 EA 04                        shr dl, 4
0042DD9A  41 80 E3 0F                     and r11b, 0xf
0042DD9E  8A CA                           mov cl, dl
0042DDA0  90                              nop
0042DDA1  C0 E1 02                        shl cl, 2
0042DDA4  02 D1                           add dl, cl
0042DDA6  41 8A C8                        mov cl, r8b
0042DDA9  C0 E9 04                        shr cl, 4
0042DDAC  02 D2                           add dl, dl
0042DDAE  41 02 D3                        add dl, r11b
0042DDB1  41 80 E0 0F                     and r8b, 0xf
0042DDB5  0F B6 C2                        movzx eax, dl
0042DDB8  6B D0 64                        imul edx, eax, 0x64
0042DDBB  8A C1                           mov al, cl
0042DDBD  C0 E0 02                        shl al, 2
0042DDC0  02 C8                           add cl, al
0042DDC2  02 C9                           add cl, cl
0042DDC4  41 02 C8                        add cl, r8b
0042DDC7  0F B6 C1                        movzx eax, cl
0042DDCA  B9 6C 07 00 00                  mov ecx, 0x76c
0042DDCF  66 03 D0                        add dx, ax
0042DDD2  0F B7 C2                        movzx eax, dx
0042DDD5  66 2B C1                        sub ax, cx
0042DDD8  66 83 F8 13                     cmp ax, 0x13
0042DDDC  76 19                           jbe 0x14042ddf7
0042DDDE  66 89 13                        mov word ptr [rbx], dx
0042DDE1  E8 1E 00 00 00                  call 0x14042de04
0042DDE6  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
0042DDEB  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
0042DDF0  48 83 C4 20                     add rsp, 0x20
0042DDF4  5F                              pop rdi
0042DDF5  C3                              ret
0042DDF6  CC                              int3
0042DDF7  66 83 C2 64                     add dx, 0x64
0042DDFB  EB E1                           jmp 0x14042ddde
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpReadCmosTime(__int64 a1)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (32);
    result = HalpAcquireCmosSpinLockAndWait(a1, a2, a3, a4);
    *(unsigned __int16 *)(a1 + 12) = 500;
    result = 0;
    a2 = (unsigned __int8)((0) >> (4));
    result = (unsigned __int8)((result) & (15));
    a1 = (unsigned __int8)(((unsigned __int8)(a2)) << (2));
    a2 = (unsigned __int8)((a2) + ((unsigned __int8)(a1)));
    a2 = (unsigned __int8)((a2) + ((unsigned __int8)(a2)));
    a2 = (unsigned __int8)((a2) + ((unsigned __int8)(result)));
    *(unsigned __int16 *)(a1 + 10) = (unsigned __int16)((unsigned __int8)(a2));
    a2 = (unsigned __int8)((2) >> (4));
    result = (unsigned __int8)((2) & (15));
    a1 = (unsigned __int8)(((unsigned __int8)(a2)) << (2));
    a2 = (unsigned __int8)((a2) + ((unsigned __int8)(a1)));
    a2 = (unsigned __int8)((a2) + ((unsigned __int8)(a2)));
    a2 = (unsigned __int8)((a2) + ((unsigned __int8)(result)));
    *(unsigned __int16 *)(a1 + 8) = (unsigned __int16)((unsigned __int8)(a2));
    a2 = (unsigned __int8)((4) >> (4));
    result = (unsigned __int8)((4) & (15));
    a1 = (unsigned __int8)(((unsigned __int8)(a2)) << (2));
    a2 = (unsigned __int8)((a2) + ((unsigned __int8)(a1)));
    a2 = (unsigned __int8)((a2) + ((unsigned __int8)(a2)));
    a2 = (unsigned __int8)((a2) + ((unsigned __int8)(result)));
    *(unsigned __int16 *)(a1 + 6) = (unsigned __int16)((unsigned __int8)(a2));
    a2 = (unsigned __int8)((6) >> (4));
    result = (unsigned __int8)((6) & (15));
    a1 = (unsigned __int8)(((unsigned __int8)(a2)) << (2));
    a2 = (unsigned __int8)((a2) + ((unsigned __int8)(a1)));
    a2 = (unsigned __int8)((a2) + ((unsigned __int8)(a2)));
    a2 = (unsigned __int8)((a2) + ((unsigned __int8)(result)));
    *(unsigned __int16 *)(a1 + 14) = (unsigned __int16)((unsigned __int8)(a2));
    a2 = (unsigned __int8)((7) >> (4));
    result = (unsigned __int8)((7) & (15));
    a1 = (unsigned __int8)(((unsigned __int8)(a2)) << (2));
    a2 = (unsigned __int8)((a2) + ((unsigned __int8)(a1)));
    a2 = (unsigned __int8)((a2) + ((unsigned __int8)(a2)));
    a2 = (unsigned __int8)((a2) + ((unsigned __int8)(result)));
    *(unsigned __int16 *)(a1 + 4) = (unsigned __int16)((unsigned __int8)(a2));
    a3 = (unsigned __int8)((8) >> (4));
    result = (unsigned __int8)((8) & (15));
    a1 = (unsigned __int8)(((unsigned __int8)(a3)) << (2));
    a3 = (unsigned __int8)((a3) + ((unsigned __int8)(a1)));
    a3 = (unsigned __int8)((a3) + ((unsigned __int8)(a3)));
    a3 = (unsigned __int8)((a3) + ((unsigned __int8)(result)));
    *(unsigned __int16 *)(a1 + 2) = (unsigned __int16)((unsigned __int8)(a3));
    result = HalpGetCmosCenturyByte(a1, (unsigned int)((unsigned int)(112 + 1)), a3, a4);
    a2 = (unsigned __int8)(((unsigned __int8)((unsigned __int8)(result))) >> (4));
    v_r11 = (unsigned __int8)(((unsigned __int8)(result)) & (15));
    a1 = (unsigned __int8)(((unsigned __int8)(a2)) << (2));
    a2 = (unsigned __int8)((a2) + ((unsigned __int8)(a1)));
    a1 = (unsigned __int8)((9) >> (4));
    a2 = (unsigned __int8)((a2) + ((unsigned __int8)(a2)));
    a2 = (unsigned __int8)((a2) + ((unsigned __int8)(v_r11)));
    a3 = (unsigned __int8)((9) & (15));
    a2 = (unsigned int)((a2) * ((unsigned int)((unsigned __int8)(a2))));
    result = (unsigned __int8)(((unsigned __int8)(a1)) << (2));
    a1 = (unsigned __int8)((a1) + ((unsigned __int8)(result)));
    a1 = (unsigned __int8)((a1) + ((unsigned __int8)(a1)));
    a1 = (unsigned __int8)((a1) + ((unsigned __int8)(a3)));
    a2 = (unsigned __int16)((a2) + ((unsigned __int16)((unsigned __int8)(a1))));
    result = (unsigned __int16)(((unsigned __int16)(a2)) - ((unsigned __int16)((unsigned int)(0x76CULL))));
    if (((unsigned __int16)(result)) <= 19) goto loc_0042DDF7;
loc_0042DDDE:
    *(unsigned __int16 *)(a1) = (unsigned __int16)(a2);
    result = HalpReleaseCmosSpinLock((unsigned int)(0x76CULL), a2, a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
loc_0042DDF7:
    a2 = (unsigned __int16)((a2) + (100));
    goto loc_0042DDDE;
}
```

## 5. (Beta) C Style

```c
int64_t HalpReadCmosTime(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r11;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (32);
    result = HalpAcquireCmosSpinLockAndWait(Arg1, a2, a3, a4);
    *(uint16_t *)(arg1 + 0xC) = 500;
    result = 0;
    a2 = (uint8_t)((0) >> (4));
    result = (uint8_t)((result) & (15));
    Arg1 = (uint8_t)(((uint8_t)(a2)) << (2));
    a2 = (uint8_t)((a2) + ((uint8_t)(Arg1)));
    a2 = (uint8_t)((a2) + ((uint8_t)(a2)));
    a2 = (uint8_t)((a2) + ((uint8_t)(result)));
    *(uint16_t *)(arg1 + 0xA) = (uint16_t)((uint8_t)(a2));
    a2 = (uint8_t)((2) >> (4));
    result = (uint8_t)((2) & (15));
    Arg1 = (uint8_t)(((uint8_t)(a2)) << (2));
    a2 = (uint8_t)((a2) + ((uint8_t)(Arg1)));
    a2 = (uint8_t)((a2) + ((uint8_t)(a2)));
    a2 = (uint8_t)((a2) + ((uint8_t)(result)));
    *(uint16_t *)(arg1 + 0x8) = (uint16_t)((uint8_t)(a2));
    a2 = (uint8_t)((4) >> (4));
    result = (uint8_t)((4) & (15));
    Arg1 = (uint8_t)(((uint8_t)(a2)) << (2));
    a2 = (uint8_t)((a2) + ((uint8_t)(Arg1)));
    a2 = (uint8_t)((a2) + ((uint8_t)(a2)));
    a2 = (uint8_t)((a2) + ((uint8_t)(result)));
    *(uint16_t *)(arg1 + 0x6) = (uint16_t)((uint8_t)(a2));
    a2 = (uint8_t)((6) >> (4));
    result = (uint8_t)((6) & (15));
    Arg1 = (uint8_t)(((uint8_t)(a2)) << (2));
    a2 = (uint8_t)((a2) + ((uint8_t)(Arg1)));
    a2 = (uint8_t)((a2) + ((uint8_t)(a2)));
    a2 = (uint8_t)((a2) + ((uint8_t)(result)));
    *(uint16_t *)(arg1 + 0xE) = (uint16_t)((uint8_t)(a2));
    a2 = (uint8_t)((7) >> (4));
    result = (uint8_t)((7) & (15));
    Arg1 = (uint8_t)(((uint8_t)(a2)) << (2));
    a2 = (uint8_t)((a2) + ((uint8_t)(Arg1)));
    a2 = (uint8_t)((a2) + ((uint8_t)(a2)));
    a2 = (uint8_t)((a2) + ((uint8_t)(result)));
    *(uint16_t *)(arg1 + 0x4) = (uint16_t)((uint8_t)(a2));
    a3 = (uint8_t)((8) >> (4));
    result = (uint8_t)((8) & (15));
    Arg1 = (uint8_t)(((uint8_t)(a3)) << (2));
    a3 = (uint8_t)((a3) + ((uint8_t)(Arg1)));
    a3 = (uint8_t)((a3) + ((uint8_t)(a3)));
    a3 = (uint8_t)((a3) + ((uint8_t)(result)));
    *(uint16_t *)(arg1 + 0x2) = (uint16_t)((uint8_t)(a3));
    result = HalpGetCmosCenturyByte(Arg1, (uint32_t)((uint32_t)(112 + 1)), a3, a4);
    a2 = (uint8_t)(((uint8_t)((uint8_t)(result))) >> (4));
    local_r11 = (uint8_t)(((uint8_t)(result)) & (15));
    Arg1 = (uint8_t)(((uint8_t)(a2)) << (2));
    a2 = (uint8_t)((a2) + ((uint8_t)(Arg1)));
    Arg1 = (uint8_t)((9) >> (4));
    a2 = (uint8_t)((a2) + ((uint8_t)(a2)));
    a2 = (uint8_t)((a2) + ((uint8_t)(local_r11)));
    a3 = (uint8_t)((9) & (15));
    a2 = (uint32_t)((a2) * ((uint32_t)((uint8_t)(a2))));
    result = (uint8_t)(((uint8_t)(Arg1)) << (2));
    Arg1 = (uint8_t)((Arg1) + ((uint8_t)(result)));
    Arg1 = (uint8_t)((Arg1) + ((uint8_t)(Arg1)));
    Arg1 = (uint8_t)((Arg1) + ((uint8_t)(a3)));
    a2 = (uint16_t)((a2) + ((uint16_t)((uint8_t)(Arg1))));
    result = (uint16_t)(((uint16_t)(a2)) - ((uint16_t)((uint32_t)(0x76CULL))));
    if (((uint16_t)(result)) <= 19) goto loc_0042DDF7;
loc_0042DDDE:
    *(uint16_t *)(arg1) = (uint16_t)(a2);
    result = HalpReleaseCmosSpinLock((uint32_t)(0x76CULL), a2, a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
loc_0042DDF7:
    a2 = (uint16_t)((a2) + (100));
    goto loc_0042DDDE;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `16` | `W` |
| `Arg1` | `+ 0x2` | `16` | `W` |
| `Arg1` | `+ 0x4` | `16` | `W` |
| `Arg1` | `+ 0x6` | `16` | `W` |
| `Arg1` | `+ 0x8` | `16` | `W` |
| `Arg1` | `+ 0xA` | `16` | `W` |
| `Arg1` | `+ 0xC` | `16` | `W` |
| `Arg1` | `+ 0xE` | `16` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0042DC74&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0042DC74[BB_0042DC74]
  bb_0042DDDE[BB_0042DDDE]
  bb_0042DDF6[BB_0042DDF6]
  bb_0042DDF7[BB_0042DDF7]
  bb_0042DC74 -->|branch| bb_0042DDF7
  bb_0042DC74 -->|fallthrough| bb_0042DDDE
  bb_0042DDF6 -->|flow| bb_0042DDF7
  bb_0042DDF7 -->|branch| bb_0042DDDE
```
