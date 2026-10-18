# x86BiosWriteCmosPort

- RVA: `0x00547EE8`–`0x00547F59` (길이 `113` bytes)
- VA: `0x0000000140547EE8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C954`
- 디코드: `35`개 명령, `113/113` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00547F0A` → [x86BiosWriteCmosPortByte](x86BiosWriteCmosPortByte_function_00547F60.md) (function, `0x00547F60`)
- `0x00547F20` → [x86BiosWriteCmosPortByte](x86BiosWriteCmosPortByte_function_00547F60.md) (function, `0x00547F60`)
- `0x00547F31` → [x86BiosWriteCmosPortByte](x86BiosWriteCmosPortByte_function_00547F60.md) (function, `0x00547F60`)
- `0x00547F3E` → [x86BiosWriteCmosPortByte](x86BiosWriteCmosPortByte_function_00547F60.md) (function, `0x00547F60`)

### Direct callers
- [x86BiosWriteIoSpace](../47/x86BiosWriteIoSpace_function_00472E00.md) at `0x00472E93`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00547EE8  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00547EED  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
00547EF2  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
00547EF7  57                              push rdi
00547EF8  48 83 EC 20                     sub rsp, 0x20
00547EFC  0F B7 FA                        movzx edi, dx
00547EFF  8B F1                           mov esi, ecx
00547F01  0F B7 CF                        movzx ecx, di
00547F04  41 8A D0                        mov dl, r8b
00547F07  41 8B D8                        mov ebx, r8d
00547F0A  E8 51 00 00 00                  call 0x140547f60
00547F0F  85 F6                           test esi, esi
00547F11  7E 30                           jle 0x140547f43
00547F13  8B D3                           mov edx, ebx
00547F15  BD 01 00 00 00                  mov ebp, 1
00547F1A  C1 EA 08                        shr edx, 8
00547F1D  8D 0C 2F                        lea ecx, [rdi + rbp]
00547F20  E8 3B 00 00 00                  call 0x140547f60
00547F25  3B F5                           cmp esi, ebp
00547F27  7E 1A                           jle 0x140547f43
00547F29  8B D3                           mov edx, ebx
00547F2B  8D 4F 02                        lea ecx, [rdi + 2]
00547F2E  C1 EA 10                        shr edx, 0x10
00547F31  E8 2A 00 00 00                  call 0x140547f60
00547F36  C1 EB 18                        shr ebx, 0x18
00547F39  8D 4F 03                        lea ecx, [rdi + 3]
00547F3C  8A D3                           mov dl, bl
00547F3E  E8 1D 00 00 00                  call 0x140547f60
00547F43  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00547F48  48 8B 6C 24 38                  mov rbp, qword ptr [rsp + 0x38]
00547F4D  48 8B 74 24 40                  mov rsi, qword ptr [rsp + 0x40]
00547F52  48 83 C4 20                     add rsp, 0x20
00547F56  5F                              pop rdi
00547F57  C3                              ret
00547F58  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall x86BiosWriteCmosPort(int a1, unsigned __int16 a2, int a3)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (32);
    result = x86BiosWriteCmosPortByte(a2, (unsigned __int8)(a3), a3, a4);
    if (condition_is_less_or_equal) goto loc_00547F43;
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a3)))) >> (8));
    result = x86BiosWriteCmosPortByte(a2 + 1 * 1, a2, a3, a4);
    v_rbx = (unsigned int)(a3);
    if (((unsigned int)((unsigned int)(a1))) >= = 1) {
        a2 = (unsigned int)((unsigned int)(a3));
        a1 = a2 + 2;
        a2 = (unsigned int)((a2) >> (16));
        result = x86BiosWriteCmosPortByte(a1, a2, a3, a4);
        v_rbx = (unsigned int)(((unsigned int)(a3)) >> (24));
        a1 = a2 + 3;
        a2 = (unsigned __int8)(v_rbx);
        result = x86BiosWriteCmosPortByte(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t x86BiosWriteCmosPort(int32_t Arg1, void *Arg2, int32_t Arg3)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (32);
    result = x86BiosWriteCmosPortByte(Arg2, (uint8_t)(Arg3), Arg3, a4);
    if (condition_is_less_or_equal) goto loc_00547F43;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg3)))) >> (8));
    result = x86BiosWriteCmosPortByte(Arg2 + 1 * 1, Arg2, Arg3, a4);
    local_rbx = (uint32_t)(Arg3);
    if (((uint32_t)((uint32_t)(Arg1))) >= = 1) {
        Arg2 = (uint32_t)((uint32_t)(Arg3));
        Arg1 = Arg2 + 2;
        Arg2 = (uint32_t)((Arg2) >> (16));
        result = x86BiosWriteCmosPortByte(Arg1, Arg2, Arg3, a4);
        local_rbx = (uint32_t)(((uint32_t)(Arg3)) >> (24));
        Arg1 = Arg2 + 3;
        Arg2 = (uint8_t)(local_rbx);
        result = x86BiosWriteCmosPortByte(Arg1, Arg2, Arg3, a4);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0 + rbp*1` | `32` | `R` |
| `Arg2` | `+ 0x2` | `32` | `R` |
| `Arg2` | `+ 0x3` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00547EE8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00547EE8[BB_00547EE8]
  bb_00547F13[BB_00547F13]
  bb_00547F29[BB_00547F29]
  bb_00547F43[BB_00547F43]
  bb_00547F58[BB_00547F58]
  bb_00547EE8 -->|branch| bb_00547F43
  bb_00547EE8 -->|fallthrough| bb_00547F13
  bb_00547F13 -->|branch| bb_00547F43
  bb_00547F13 -->|fallthrough| bb_00547F29
  bb_00547F29 -->|flow| bb_00547F43
```
