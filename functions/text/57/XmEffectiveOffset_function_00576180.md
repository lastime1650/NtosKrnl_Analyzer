# XmEffectiveOffset

- RVA: `0x00576180`–`0x005761EB` (길이 `107` bytes)
- VA: `0x0000000140576180`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `29`개 명령, `107/107` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x005761AC` → [XmEvaluateAddressSpecifier](../47/XmEvaluateAddressSpecifier_function_00473224.md) (function, `0x00473224`)
- `0x005761C6` → [longjmp](../4F/longjmp_function_004FD5F0.md) (function, `0x004FD5F0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00576180  40 53                           push rbx
00576182  48 83 EC 20                     sub rsp, 0x20
00576186  83 64 24 30 00                  and dword ptr [rsp + 0x30], 0
0057618B  48 8B D9                        mov rbx, rcx
0057618E  8A 81 8A 00 00 00               mov al, byte ptr [rcx + 0x8a]
00576194  F6 D8                           neg al
00576196  1B D2                           sbb edx, edx
00576198  83 E2 02                        and edx, 2
0057619B  FF C2                           inc edx
0057619D  89 51 78                        mov dword ptr [rcx + 0x78], edx
005761A0  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
005761A5  C6 81 8F 00 00 00 01            mov byte ptr [rcx + 0x8f], 1
005761AC  E8 73 D0 EF FF                  call 0x140473224
005761B1  80 BB 8E 00 00 00 00            cmp byte ptr [rbx + 0x8e], 0
005761B8  74 12                           je 0x1405761cc
005761BA  48 8D 8B A0 00 00 00            lea rcx, [rbx + 0xa0]
005761C1  BA 0B 00 00 00                  mov edx, 0xb
005761C6  E8 25 74 F8 FF                  call 0x1404fd5f0
005761CB  CC                              int3
005761CC  8B 54 24 30                     mov edx, dword ptr [rsp + 0x30]
005761D0  48 83 C2 06                     add rdx, 6
005761D4  89 43 6C                        mov dword ptr [rbx + 0x6c], eax
005761D7  B8 01 00 00 00                  mov eax, 1
005761DC  48 8D 14 93                     lea rdx, [rbx + rdx*4]
005761E0  48 89 53 58                     mov qword ptr [rbx + 0x58], rdx
005761E4  48 83 C4 20                     add rsp, 0x20
005761E8  5B                              pop rbx
005761E9  C3                              ret
005761EA  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall XmEffectiveOffset(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_p8;

    v_rsp = (v_rsp) - (32);
    result = (unsigned __int8)(-(*(unsigned __int8 *)(a1 + 138)));
    a2 = (unsigned int)((a2) & (2));
    a2 = (unsigned int)((a2) + 1);
    *(unsigned int *)(a1 + 120) = a2;
    *(unsigned __int8 *)(a1 + 143) = 1;
    result = XmEvaluateAddressSpecifier(a1, v_stack_p8, a3, a4);
    if ((*(unsigned __int8 *)(a1 + 142)) != 0) {
        a1 = a1 + 160;
        a2 = 11;
        result = longjmp(a1, a2, a3, a4);
    }
    a2 = ((unsigned int)(v_stack_p8)) + (6);
    *(unsigned int *)(a1 + 108) = (unsigned int)(result);
    *(unsigned __int64 *)(a1 + 88) = a1 + a2 * 4;
    v_rsp = (v_rsp) + (32);
    return 1;
}
```

## 5. (Beta) C Style

```c
int64_t XmEffectiveOffset(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_p8;

    local_rsp = (local_rsp) - (32);
    result = (uint8_t)(-(*(uint8_t *)(arg1 + 0x8A)));
    Arg2 = (uint32_t)((Arg2) & (2));
    Arg2 = (uint32_t)((Arg2) + 1);
    *(uint32_t *)(arg1 + 0x78) = Arg2;
    *(uint8_t *)(arg1 + 0x8F) = 1;
    result = XmEvaluateAddressSpecifier(Arg1, v_stack_p8, a3, a4);
    if ((*(uint8_t *)(arg1 + 0x8E)) != 0) {
        Arg1 = Arg1 + 160;
        Arg2 = 11;
        result = longjmp(Arg1, Arg2, a3, a4);
    }
    Arg2 = ((uint32_t)(v_stack_p8)) + (6);
    *(uint32_t *)(arg1 + 0x6C) = (uint32_t)(result);
    *(void **)(arg1 + 0x58) = Arg1 + Arg2 * 4;
    local_rsp = (local_rsp) + (32);
    return 1;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0 + rdx*4` | `64` | `R` |
| `Arg1` | `+ 0x58` | `64` | `W` |
| `Arg1` | `+ 0x6C` | `32` | `W` |
| `Arg1` | `+ 0x78` | `32` | `W` |
| `Arg1` | `+ 0x8A` | `8` | `R` |
| `Arg1` | `+ 0x8E` | `8` | `R` |
| `Arg1` | `+ 0x8F` | `8` | `W` |
| `Arg1` | `+ 0xA0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00576180&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00576180[BB_00576180]
  bb_005761BA[BB_005761BA]
  bb_005761CC[BB_005761CC]
  bb_005761EA[BB_005761EA]
  bb_00576180 -->|branch| bb_005761CC
  bb_00576180 -->|fallthrough| bb_005761BA
  bb_005761BA -->|flow| bb_005761CC
```
