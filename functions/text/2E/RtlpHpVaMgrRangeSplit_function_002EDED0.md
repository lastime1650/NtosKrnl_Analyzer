# RtlpHpVaMgrRangeSplit

- RVA: `0x002EDED0`–`0x002EDF3D` (길이 `109` bytes)
- VA: `0x00000001402EDED0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `32`개 명령, `109/109` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [RtlpHpVaMgrCtxFree](RtlpHpVaMgrCtxFree_function_002ED734.md) at `0x002ED9E2`
- [RtlpHpVaMgrAlloc](RtlpHpVaMgrAlloc_function_002EDB1C.md) at `0x002EDBE7`
- [RtlpHpVaMgrAlloc](RtlpHpVaMgrAlloc_function_002EDB1C.md) at `0x002EDD58`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002EDED0  0F B7 42 18                     movzx eax, word ptr [rdx + 0x18]
002EDED4  4C 8B CA                        mov r9, rdx
002EDED7  66 41 2B C0                     sub ax, r8w
002EDEDB  4D 8B D0                        mov r10, r8
002EDEDE  49 C1 E2 05                     shl r10, 5
002EDEE2  4C 03 D2                        add r10, rdx
002EDEE5  66 41 89 42 18                  mov word ptr [r10 + 0x18], ax
002EDEEA  66 45 89 42 1A                  mov word ptr [r10 + 0x1a], r8w
002EDEEF  66 44 89 42 18                  mov word ptr [rdx + 0x18], r8w
002EDEF4  41 8A 02                        mov al, byte ptr [r10]
002EDEF7  45 0F B7 42 18                  movzx r8d, word ptr [r10 + 0x18]
002EDEFC  24 FD                           and al, 0xfd
002EDEFE  0C 01                           or al, 1
002EDF00  41 88 02                        mov byte ptr [r10], al
002EDF03  41 8B C0                        mov eax, r8d
002EDF06  0F 10 42 08                     movups xmm0, xmmword ptr [rdx + 8]
002EDF0A  48 C1 E0 05                     shl rax, 5
002EDF0E  49 03 C2                        add rax, r10
002EDF11  F3 41 0F 7F 42 08               movdqu xmmword ptr [r10 + 8], xmm0
002EDF17  0F B7 51 28                     movzx edx, word ptr [rcx + 0x28]
002EDF1B  48 C1 E2 05                     shl rdx, 5
002EDF1F  48 8D 4A FF                     lea rcx, [rdx - 1]
002EDF23  48 F7 D1                        not rcx
002EDF26  49 23 C9                        and rcx, r9
002EDF29  48 03 CA                        add rcx, rdx
002EDF2C  48 3B C1                        cmp rax, rcx
002EDF2F  72 05                           jb 0x1402edf36
002EDF31  49 8B C2                        mov rax, r10
002EDF34  C3                              ret
002EDF35  CC                              int3
002EDF36  66 44 89 40 1A                  mov word ptr [rax + 0x1a], r8w
002EDF3B  EB F4                           jmp 0x1402edf31
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpHpVaMgrRangeSplit(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_r10;

    result = (unsigned __int16)((*(unsigned __int16 *)(a2 + 24)) - ((unsigned __int16)(a3)));
    v_r10 = (a3) << (5);
    v_r10 = (v_r10) + (a2);
    *(unsigned __int16 *)(v_r10 + 24) = (unsigned __int16)(result);
    *(unsigned __int16 *)(v_r10 + 26) = (unsigned __int16)(a3);
    *(unsigned __int16 *)(a2 + 24) = (unsigned __int16)(a3);
    result = (unsigned __int8)((*(unsigned __int8 *)(v_r10)) & (253));
    result = (unsigned __int8)((result) | (1));
    *(unsigned __int8 *)(v_r10) = (unsigned __int8)(result);
    result = ((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_r10 + 24)))) << (5);
    result = (result) + (v_r10);
    *(unsigned __int64 *)(v_r10 + 8) = v_xmm0;
    a2 = (*(unsigned __int16 *)(a1 + 40)) << (5);
    a1 = ~(a2 - 1);
    a1 = (a1) & (a2);
    a1 = (a1) + (a2);
    if (result < a1) goto loc_002EDF36;
loc_002EDF31:
    return v_r10;
loc_002EDF36:
    *(unsigned __int16 *)(v_r10 + 26) = (unsigned __int16)(*(unsigned __int16 *)(v_r10 + 24));
    goto loc_002EDF31;
}
```

## 5. (Beta) C Style

```c
int64_t RtlpHpVaMgrRangeSplit(void *Arg1, void *Arg2, int64_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r10;

    result = (uint16_t)((*(uint16_t *)(arg2 + 0x18)) - ((uint16_t)(Arg3)));
    local_r10 = (Arg3) << (5);
    local_r10 = (local_r10) + (Arg2);
    *(uint16_t *)(local_r10 + 0x18) = (uint16_t)(result);
    *(uint16_t *)(local_r10 + 0x1A) = (uint16_t)(Arg3);
    *(uint16_t *)(arg2 + 0x18) = (uint16_t)(Arg3);
    result = (uint8_t)((*(uint8_t *)(local_r10)) & (253));
    result = (uint8_t)((result) | (1));
    *(uint8_t *)(local_r10) = (uint8_t)(result);
    result = ((uint32_t)((uint32_t)(*(uint16_t *)(local_r10 + 0x18)))) << (5);
    result = (result) + (local_r10);
    *(uint64_t *)(local_r10 + 0x8) = v_xmm0;
    Arg2 = (*(uint16_t *)(arg1 + 0x28)) << (5);
    Arg1 = ~(Arg2 - 1);
    Arg1 = (Arg1) & (Arg2);
    Arg1 = (Arg1) + (Arg2);
    if (result < Arg1) goto loc_002EDF36;
loc_002EDF31:
    return local_r10;
loc_002EDF36:
    *(uint16_t *)(local_r10 + 0x1A) = (uint16_t)(*(uint16_t *)(local_r10 + 0x18));
    goto loc_002EDF31;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x28` | `16` | `R` |
| `Arg2` | `+ 0x8` | `128` | `R` |
| `Arg2` | `+ 0x18` | `16` | `R` |
| `Arg2` | `+ 0x18` | `16` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002EDED0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002EDED0[BB_002EDED0]
  bb_002EDF31[BB_002EDF31]
  bb_002EDF35[BB_002EDF35]
  bb_002EDF36[BB_002EDF36]
  bb_002EDED0 -->|branch| bb_002EDF36
  bb_002EDED0 -->|fallthrough| bb_002EDF31
  bb_002EDF35 -->|flow| bb_002EDF36
  bb_002EDF36 -->|branch| bb_002EDF31
```
